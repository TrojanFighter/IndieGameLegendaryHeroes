#!/usr/bin/env python3
"""ZXDB 1982–1992 conservative author-cohort extractor; Python stdlib only.

Not a publisher or indie-studio census. Requires an imported ZXDB SQLite file.
Run --list-genres first, manually confirm game genre IDs, then export.
"""
import argparse
import csv
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path


NEEDED = {
    "entries": {"id", "genretype_id"},
    "releases": {"entry_id", "release_seq", "release_year"},
    "authors": {"entry_id", "label_id"},
    "labels": {"id", "labeltype_id", "owner_id"},
    "genretypes": {"id", "text"},
}


def check_schema(conn):
    for table, fields in NEEDED.items():
        columns = {r[1] for r in conn.execute("PRAGMA table_info(" + table + ")")}
        if not fields <= columns:
            raise RuntimeError(
                "ZXDB schema mismatch in %s. Missing: %s" %
                (table, sorted(fields - columns))
            )


def write_csv(file, headers, rows):
    file.parent.mkdir(parents=True, exist_ok=True)
    with file.open("w", encoding="utf-8", newline="") as handle:
        out = csv.writer(handle)
        out.writerow(headers)
        out.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True, type=Path, help="ZXDB SQLite snapshot")
    parser.add_argument("--list-genres", action="store_true")
    parser.add_argument("--genre-ids", help="Manually reviewed ZXDB genretype IDs, e.g. 1,2")
    parser.add_argument("--family", default="UNCLASSIFIED")
    parser.add_argument("--from-year", type=int, default=1982)
    parser.add_argument("--to-year", type=int, default=1992)
    parser.add_argument("--snapshot-commit", required=True,
                        help="Exact ZXDB GitHub source commit SHA for provenance")
    parser.add_argument("--output", type=Path, default=Path("zxdb-results"))
    args = parser.parse_args()

    if not args.db.is_file():
        parser.error("SQLite database file does not exist")
    if args.to_year < args.from_year:
        parser.error("to-year must not precede from-year")

    conn = sqlite3.connect("file:" + str(args.db.resolve()) + "?mode=ro", uri=True)
    check_schema(conn)

    if args.list_genres:
        rows = conn.execute(
            """SELECT g.id, g.text, COUNT(e.id)
               FROM genretypes g LEFT JOIN entries e ON e.genretype_id=g.id
               GROUP BY g.id, g.text ORDER BY COUNT(e.id) DESC"""
        ).fetchall()
        write_csv(args.output / "genretype-candidates.csv",
                  ["genretype_id", "description", "catalog_entries_in_all_periods"],
                  rows)
        print("Wrote genretype-candidates.csv; review before exporting cohorts.")
        return

    if not args.genre_ids:
        parser.error("No unreviewed genre default: pass --genre-ids after --list-genres.")
    try:
        gids = sorted({int(p.strip()) for p in args.genre_ids.split(",")})
    except ValueError:
        parser.error("genre-ids must contain numeric IDs only")
    if not gids:
        parser.error("At least one game-specific genre must be chosen")
    qmarks = ",".join("?" * len(gids))

    # ZXDB README: release_seq=0 is first standalone release.
    # Entries published ONLY in a compilation, magazine, covertape or book may
    # have blank release #0: these are OMITTED; never infer 0 games/authors.
    # Label type + = person; - = nickname; owner_id maps nickname to person.
    # Companies, teams and ambiguous labels are NOT treated as individual people.
    sql = """
    SELECT e.id, r.release_year, a.label_id,
           l.labeltype_id, l.owner_id, owner.labeltype_id
    FROM entries e
    JOIN releases r ON r.entry_id=e.id AND r.release_seq=0
    LEFT JOIN authors a ON a.entry_id=e.id
    LEFT JOIN labels l ON l.id=a.label_id
    LEFT JOIN labels owner ON owner.id=l.owner_id
    WHERE e.genretype_id IN (""" + qmarks + """)
      AND r.release_year BETWEEN ? AND ?
    ORDER BY r.release_year,e.id
    """
    records = conn.execute(sql, tuple(gids) +
                           (args.from_year, args.to_year)).fetchall()

    # Only a positive person classification makes a credited individual count.
    # A nickname is only counted if it resolves to an explicit person owner.
    # Any other label is unresolved: not an individual and not proof of company.
    games = {}
    for entry, year, label, typ, owner, owner_typ in records:
        key = (int(year), entry)
        if key not in games:
            games[key] = {"people": set(), "unresolved": False, "credited": False}
        g = games[key]
        if label is None:
            g["unresolved"] = True
        else:
            g["credited"] = True
            person_id = None
            if typ == "+":
                person_id = label
            elif typ == "-" and owner is not None and owner_typ == "+":
                person_id = owner
            if person_id is not None:
                g["people"].add(person_id)
            else:
                g["unresolved"] = True

    year_games = defaultdict(set)
    year_credited = defaultdict(set)
    year_people = defaultdict(set)
    year_solo_credit = defaultdict(set)
    year_unresolved = defaultdict(set)
    first_seen = {}
    for (year, eid), g in games.items():
        year_games[year].add(eid)
        if g["people"]:
            year_credited[year].add(eid)
        if g["unresolved"]:
            year_unresolved[year].add(eid)
        if len(g["people"]) == 1 and not g["unresolved"]:
            year_solo_credit[year].add(eid)
        year_people[year].update(g["people"])
        for pid in g["people"]:
            first_seen[pid] = min(first_seen.get(pid, year), year)

    columns = [
        "year", "family", "source_sha", "genre_ids",
        "original_standalone_titles_dated",
        "titles_with_at_least_one_identifiable_person",
        "titles_with_unresolved_author_credit",
        "titles_one_identifiable_person_no_unknown_credits",
        "distinct_explicit_person_ids",
        "first_observed_person_ids_within_sample",
        "previous_year_returning_person_ids",
        "people_coverage_pct",
        "is_20_person_threshold_proxy",
        "is_strict_indie_commercial_Q_confirmed",
        "notes",
    ]
    output = []
    for year in range(args.from_year, args.to_year + 1):
        total = len(year_games[year])
        covered = len(year_credited[year])
        people = year_people[year]
        output.append([
            year, args.family, args.snapshot_commit, ";".join(map(str, gids)),
            total, covered, len(year_unresolved[year]),
            len(year_solo_credit[year]), len(people),
            sum(first_seen[p] == year for p in people),
            len(people & year_people[year - 1]),
            round(100 * covered / total, 2) if total else "",
            int(len(people) >= 20),
            "NO",  # independent commercial development entity not proved
            "Standalone original only; >0 personal credits != all individual indie;"
            "first-observed is left-truncated; unmapped & undated titles excluded",
        ])
    out = args.output / (
        "zxdb_%s_%d_%d_annual_creators.csv" %
        (args.family.lower().replace(" ", "_"), args.from_year, args.to_year)
    )
    write_csv(out, columns, output)
    print("Wrote", out, "dated originals", len(games),
          "explicit unique persons", len(first_seen))
    if len(games) == 0:
        print("WARNING: Empty selection. Check genre IDs and source release dates.",
              file=sys.stderr)
    if sum(len(v) for v in year_people.values()) == 0:
        print("WARNING: No explicit person labels were found; audit ZXDB labeltypes.",
              file=sys.stderr)


if __name__ == "__main__":
    main()
