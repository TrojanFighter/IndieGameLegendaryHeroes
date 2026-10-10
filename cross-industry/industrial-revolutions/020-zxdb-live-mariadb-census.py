#!/usr/bin/env python3
"""ZXDB pinned MySQL-dump year-cohort counter. Must be run against a loaded source DB.

Conservative population: game-word genre classifications, original standalone
releases with a known date, explicitly identifiable human credits. This is NOT
an independent commercial author census. Emits genre/status and coverage audits.
"""
import csv
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

import pymysql

OUT = Path("zxdb-results")
OUT.mkdir(exist_ok=True)
PINNED_SHA = "0a634a1165bd3690ea24e3c6b67bbbbb1b1ebd09"

def output(path, head, rows):
    with (OUT / path).open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(head)
        w.writerows(rows)

def main():
    db = pymysql.connect(
        host=os.getenv("ZXDB_DB_HOST", "127.0.0.1"),
        port=int(os.getenv("ZXDB_DB_PORT", "3306")),
        user=os.getenv("ZXDB_DB_USER", "root"),
        password=os.environ["ZXDB_DB_PASSWORD"],
        database="zxdb",
        charset="utf8mb4",
        autocommit=True,
        cursorclass=pymysql.cursors.Cursor,
    )
    with db.cursor() as cur:
        for table, expected in {
            "entries": {"id", "genretype_id"},
            "releases": {"entry_id", "release_seq", "release_year"},
            "authors": {"entry_id", "label_id"},
            "labels": {"id", "labeltype_id", "owner_id"},
            "genretypes": {"id", "text"},
        }.items():
            cur.execute("SHOW COLUMNS FROM " + table)
            seen = {c[0] for c in cur.fetchall()}
            if not expected.issubset(seen):
                raise RuntimeError(table + " schema changed: " + str(expected-seen))
        cur.execute("""SELECT g.id, g.text, COUNT(e.id)
            FROM genretypes g LEFT JOIN entries e ON e.genretype_id=g.id
            GROUP BY g.id, g.text ORDER BY COUNT(e.id) DESC""")
        genres = cur.fetchall()
        output("zxdb-genre-audit.csv",
               ["genretype_id", "genre_text", "all_catalog_entries"], genres)
        # No historical ZXDB->Steam tag mapping is being invented here.
        # Label as GAME_KEYWORD_PROXY until manually reviewed.
        game_ids = [
            int(gid) for gid, name, n in genres
            if re.search(r"\bgame\b", str(name), flags=re.I)
            and not re.search(r"non.game|utility|compilation|game maker", str(name), re.I)
        ]
        if not game_ids:
            raise RuntimeError("No game-like genres. Review the candidates CSV.")
        # Safety gate against absurd genre classification.
        if len(game_ids) > 200:
            raise RuntimeError("Too many game-like genre IDs, requires manual review")
        placeholders = ",".join(["%s"]*len(game_ids))
        cur.execute("""SELECT e.id, e.title, e.genretype_id, r.release_year,
              a.label_id, l.labeltype_id, l.owner_id, owner.labeltype_id
            FROM entries e
            JOIN releases r ON r.entry_id=e.id AND r.release_seq=0
            LEFT JOIN authors a ON a.entry_id=e.id
            LEFT JOIN labels l ON l.id=a.label_id
            LEFT JOIN labels owner ON owner.id=l.owner_id
            WHERE e.genretype_id IN (""" + placeholders + """)
              AND r.release_year BETWEEN 1982 AND 1992
            ORDER BY r.release_year, e.id""", tuple(game_ids))
        records = cur.fetchall()
    games={}
    genres_by_game={}
    for eid,title,gid,year,label,typ,owner,owner_type in records:
        key=(int(year),int(eid))
        genres_by_game[key]=int(gid)
        if key not in games:
            games[key]={"people":set(),"unresolved":False,"title":title,"has_credit":False}
        z=games[key]
        if label is None:
            z["unresolved"]=True
        else:
            z["has_credit"]=True
            pid=None
            if typ=="+":
                pid=int(label)
            elif typ=="-" and owner is not None and owner_type=="+":
                pid=int(owner)
            if pid is None:
                z["unresolved"]=True
            else:
                z["people"].add(pid)
    years=defaultdict(lambda: {"titles":set(),"known_credit":set(),
                                "unresolved":set(),"one_explicit":set(),"people":set()})
    first_seen={}
    by_genre=defaultdict(lambda: {"titles":set(),"people":set()})
    for (year,eid),item in games.items():
        y=years[year]
        y["titles"].add(eid)
        if item["people"]: y["known_credit"].add(eid)
        if item["unresolved"]: y["unresolved"].add(eid)
        if len(item["people"])==1 and not item["unresolved"]: y["one_explicit"].add(eid)
        y["people"].update(item["people"])
        for person in item["people"]:
            first_seen[person]=min(first_seen.get(person,year),year)
        g=by_genre[(year,genres_by_game[(year,eid)])]
        g["titles"].add(eid)
        g["people"].update(item["people"])
    year_out=[]
    for year in range(1982,1993):
        y=years[year];n=len(y["titles"]);human=len(y["people"])
        year_out.append([
            year,"GAME_KEYWORD_PROXY","ORIGINAL_STANDALONE_DATED",
            PINNED_SHA,
            n,len(y["known_credit"]),len(y["unresolved"]),
            len(y["one_explicit"]),human,
            sum(first_seen[p]==year for p in y["people"]),
            len(y["people"] & years[year-1]["people"]),
            round(100*len(y["known_credit"])/n,2) if n else "",
            "UNVERIFIED",  # independent commercial Q has NOT been established
        ])
    heads=["year","genre_scope","release_scope","source_sha","dated_original_games",
           "games_with_identifiable_person","games_with_unresolved_credit",
           "one_person_only_in_known_credits","distinct_credited_human_ids",
           "first_seen_humans_in_window","prior_year_returning_humans",
           "title_person_credit_coverage_pct","indie_Q_status"]
    output("zxdb-1982-1992-yearly-credited-people.csv",heads,year_out)
    output("zxdb-1982-1992-by-genre.csv",
           ["year","genretype_id","original_standalone_games","distinct_credited_humans"],
           [(yr,gid,len(v["titles"]),len(v["people"]))
            for (yr,gid),v in sorted(by_genre.items())])
    print("ZXDB source:",PINNED_SHA)
    print("Genre candidates",len(genres),"game-word proxy IDs",len(game_ids))
    print("YEAR | Original dated games | Distinct identifiable people | Person credit coverage")
    for row in year_out:
        print(row[0],"|",row[4],"|",row[8],"|",str(row[11])+"%")
    with open(os.environ.get("GITHUB_STEP_SUMMARY","/dev/null"),"a",encoding="utf8") as fo:
        fo.write("### ZXDB 1982–1992: game-word genre proxy\n\n")
        fo.write("Original standalone titles with date; identified human authors (not indie studios).\n\n")
        fo.write("| Year | Game entries | Identified humans | Coverage |\n")
        fo.write("|---:|---:|---:|---:|\n")
        for row in year_out:
            fo.write(f"| {row[0]} | {row[4]} | {row[8]} | {row[11]}% |\n")
        fo.write("\n**Q-indie = UNKNOWN**, labels include commercial and non-commercial.\n")
    db.close()

if __name__=="__main__":
    main()
