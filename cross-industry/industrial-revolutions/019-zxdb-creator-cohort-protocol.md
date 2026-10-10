# 019 — ZXDB：1982—1992逐年去重作者人数的可复核统计协议

> **2026-10-10 实际结果更新：**本文件的SQLite抽取路线仍是备选研究协议；现已另用 [020 — GitHub Actions上的临时MariaDB全库实算](020-zxdb-1982-1992-measured-supply-and-genre.md) 完成[11年有机器型号过滤的ZX Spectrum个人署名数据](020-zxdb-1982-1992-yearly-credited-people.csv)，固定 [运行#38037611540](https://github.com/TrojanFighter/IndieGameLegendaryHeroes/actions/runs/38037611540)。此前“只能设计提取协议不能执行”对020已过时；但严格 indie-Q 人数尚未核实。


- Status: **EXTRACTOR COMMITTED — NOT EXECUTED ON SOURCE DB**
- Updated: 2026-10-10
- Tool: [019-zxdb-annual-author-cohort.py](019-zxdb-annual-author-cohort.py)
- Supporting research: [018 CGW/Atari APX 的真正出版社数量与发行接口](018-cgw-apx-1982-publisher-vs-indie-evidence.md)
- Repository: [zxdb/ZXDB](https://github.com/zxdb/ZXDB), by Einar Saukas and community; ODbL 1.0 requires attribution/open-derived-data obligations
- Pinned available source at audit time: [ZXDB commit `0a634a1165bd3690ea24e3c6b67bbbbb1b1ebd09`](https://github.com/zxdb/ZXDB/tree/0a634a1165bd3690ea24e3c6b67bbbbb1b1ebd09) (2026-10-03); [database ZIP](https://github.com/zxdb/ZXDB/blob/0a634a1165bd3690ea24e3c6b67bbbbb1b1ebd09/ZXDB_mysql.sql.zip), blob `193df1d6575b7a1912bf87ea2e9ef2d67f0c9268`, **27,036,060 bytes compressed**
- **Meaningful blocker**: GitHub connector only handles UTF-8; rejected fetching binary ZIP. Public ZXInfo search page is JS-driven and API cannot be used for complete reproducible set extraction in this chat. Neither source archive nor SQLite mirror has been ingested. **Do not fabricate the missing yearly author counts, even if full-year Spectrum product counts are available from MobyGames.**

## 1. Source-model audit (from source repository, not invention)

ZXDB official [README — Database model](https://github.com/zxdb/ZXDB/blob/master/README.md) and [ZXDB_help_search.sql](https://github.com/zxdb/ZXDB/blob/master/scripts/ZXDB_help_search.sql) describe:

| Relation | What can be inferred | Critical pitfall |
|---|---|---|
| `entries` / `genretypes` | Item and its entry-type/genre | Contains books, hardware, demos and utilities as well as games; cannot COUNT(*) across all |
| `releases` | `release_seq=0` stands for original standalone release; `release_year` | Items first distributed via compilation, magazine, cover tape or type-in might have an **empty original standalone release** — excluding them biases production down |
| `authors` | Credited contributors `entry_id, label_id, team_id` | Author link may be firm, person, pen-name, or subteam. `COUNT(DISTINCT label_id)` **is not a unique human headcount** |
| `labels` / `labeltypes` | Whether named subject is a person, nickname, or company; `owner_id` may resolve nickname | Credit a company as 1 person = false positive; credit two nicknames of same person as 2 persons = false positive |
| `roles`/`roletypes` | Code, design, music, graphics, etc. | All contributors ≠ unique *lead game designer*; “1 identified coder” ≠ total project team size |
| `search_by_origins` auxiliary table | Full original publication channel and date including cover tapes/type-ins | [Helper SQL](https://github.com/zxdb/ZXDB/blob/master/scripts/ZXDB_help_search.sql) constructs/updates tables, so don't execute it blindly on the source DB; import into disposable copy first |

Source [ZXDB_health_check.sql](https://github.com/zxdb/ZXDB/blob/master/scripts/ZXDB_health_check.sql) checks that a nickname's `owner_id` maps back to a person, and that authors in a team belong to appropriate company types. Person ID mapping still needs empirical validation in the **actual imported dump**.

## 2. Protocol / pipeline

**Step 0: Obtain a fixed snapshot outside GitHub text connector**, keep full `commit_sha`, ZIP checksum, extraction time and SQLite conversion method. Do not call the current evolving default branch “frozen”.

**Step 1: Convert the source using the repository's official method**, e.g. [ZXDB_to_SQLite.py](https://github.com/zxdb/ZXDB/blob/master/scripts/ZXDB_to_SQLite.py) followed by a fresh SQLite database import. The provided conversion is legacy and **has not been tested in this response**, so schema conversion failures must be resolved and logged rather than filled with guesses. Any derived DB remains read-only during analysis.

**Step 2: Explore `genretypes`**. Run the committed script with `--list-genres` to generate `genretype-candidates.csv`. Manually decide which are actually game categories, and establish parent cohorts: `PLATFORM_2D`, `ARCADE_SHOOTER_2D`, `ADVENTURE`, `STRATEGY`, `SYSTEM_SIM` (and a remainder `OTHER_GAME`). ZXDB historical genre is **not automatically the same as today's Steam tags**. The script has no auto-selected game genre IDs by design.

**Step 3: Extract a conservative headcount**. Run one explicit verified `--genre-ids` list per genre family. The current script counts only dated original standalone releases. A person must be positively identified as such in the author's `labels`; nickname `-` is mapped to its `+` person owner; company/team or unresolved aliases are excluded from the **explicit_person_ids** numerator, and retained as unresolved coverage. Thus counts are **lower-bounded identifiable credited persons** on this snapshot, **not all working developers**.

**Step 4: Do not misreport first-seen authors**. `first_observed_person_ids_within_sample` looks only at supplied 1982—1992 window. It is **left-truncated**: someone recorded first in 1982 may already have authored ZX81, Atari or other platform games earlier. `previous_year_returning_person_ids` is continuity *within the ZXDB catalog*, not proof of full-time employment.

**Step 5: Extend to all original publication channels**. Only after fixing standalone corpus, run helper `search_by_origins` on **disposable copy** to include original magazines, type-ins, cover tapes and compilations. Export both "standalone-only" and "all documented first published" counts; original-only is a lower-scope count, not an estimate of complete industry production.

**Step 6: Commercial / independent Q classification**. Manually check individual/firm roles, whether the author kept independent creative control, publisher/advance/royalty terms, whether a game is commercial vs type-in/shareware. Record original release year, not reprint. The same person can participate in a large company's products. **Do not mark Q1+ (true independent developer count) as passed just because `distinct_explicit_person_ids >=20`.**

## 3. Usage after source database is available

```bash
# Example after importing a fixed SQLite DB from the official ZIP
python 019-zxdb-annual-author-cohort.py --db /path/to/zxdb.sqlite \
  --snapshot-commit 0a634a1165bd3690ea24e3c6b67bbbbb1b1ebd09 \
  --list-genres --output results

# After manually inspecting results/genretype-candidates.csv:
python 019-zxdb-annual-author-cohort.py --db /path/to/zxdb.sqlite \
  --snapshot-commit 0a634a1165bd3690ea24e3c6b67bbbbb1b1ebd09 \
  --genre-ids <CONFIRMED_COMMA_SEPARATED_GAME_IDS> \
  --family PLATFORM_2D --from-year 1982 --to-year 1992 --output results
```

No placeholder genre numbers are valid without viewing the source `genretype-candidates.csv`.

## 4. How to read the returned CSV

| Output field | What it actually means |
|---|---|
| `original_standalone_titles_dated` | Unique ZXDB entry IDs with an original standalone release year, within selected genre |
| `titles_with_at_least_one_identifiable_person` | Numerator for author credit completeness |
| `titles_with_unresolved_author_credit` | Items with missing, firm-only or ambiguous `authors` identity; helps quantify identification bias |
| `titles_one_identifiable_person_no_unknown_credits` | *Solo credited by available entries* only; **not proof only one human worked on it** |
| `distinct_explicit_person_ids` | Snapshot-wide unique credited person IDs per calendar year / selected genre, **not independent studios** |
| `first_observed_person_ids_within_sample` | First observed in window; not necessarily industry first |
| `previous_year_returning_person_ids` | Continuity on same ZXDB platform and genre |
| `is_20_person_threshold_proxy` | Research filter to prioritize years for manual Q inspection; NOT true Q1 |
| `is_strict_indie_commercial_Q_confirmed` | Always NO until independent and commercial identity audit is complete |

There are 11 year-rows (1982–1992) per cohort when the script is actually executed. An all-zero output is **not evidence of no developers**: first verify genre IDs, original-release date completeness and explicit person label mapping.

## 5. Validation before any annual author chart can be published

1. Dataset ZIP file hash recorded; only audit after data import succeeds and the core schema matches.
2. Known author case `Manic Miner` 1983 Matthew Smith: cross-verify author ID, role, release year and ZXDB entry, and explicitly track all credited roles. `Elite` 1984 BBC Micro is **not** a ZX Spectrum-origin example; cannot require it to appear in Spectrum census.
3. Visualize `genretype-candidates.csv` distribution; disambiguate text adventure, software utility and demos, plus pseudo-3D vs polygonal 3D.
4. For each year publish coverage ratio `credited_titles/dated_original_titles`, and unresolved identities rather than silently treating missing data as zero authors.
5. Sensitivity: original standalone only vs all recorded first channels, all credited individuals vs programmer-only, any commercial vs publisher-audited, ≥10/20/50 unique independent entities thresholds, one year vs three years.
6. Never combine annual ZXDB unique person counts with [CGW 1982 publisher respondents](018-cgw-apx-1982-publisher-vs-indie-evidence.md) or [Epic 2024 Creator IDs](017-creator-economy-economic-viability.md) as if they shared a denominator.

## Completion boundary

**Completed this turn**: source database and helper schema reviewed via GitHub, pinned repository commit and binary ZIP blob, fail-closed parser/extractor source committed, paper-like contemporary 1982 publisher evidence entered separately.

**Not completed**: imported and executed 27MB ZXDB ZIP, actual 1982—1992 person headcounts, Q1–Q3 independent commercial population and yearly 2D/3D creator production curves. The feature branch should keep UNKNOWN cells until those steps are actually run and their output audited.
