# 005 — Japan Game Parade 2023—2024：游戏类别、可玩性与「未完成作品入场」的原始页面压力测试

- As of: 2026-10-08
- Program: C Japan comparator × China/Taiwan creator formation
- Status: **PRIMARY-PAGE ARTIFACT AUDIT / SEARCH-DISCOVERED CONVENIENCE CASES ONLY / YEARLY DENOMINATOR OPEN**
- Unit: `gameparade work page`, not verified student person or first project.
- Main counterparts: [China CUSGA finals 40](../china/030-cusga-2024-full-finalist-40-project-reconstruction.md), [Taiwan DIY jam five-account cohort](../taiwan/019-diy-game-jam-2024-five-submitter-account-cohort.md), [Taiwan cross-East Asia 018](../taiwan/018-east-asian-pre-greenlight-author-support-and-global-premium-proxy.md)
- Governing rule: No after-outcome selection for any inferred conversion *rate*. This document only tests what Game Parade exposes publicly and documents the sampling limitations.

## 0. Actual discovery and one major correction

Game Parade public portal:
- https://gameparade.creators-guild.com/works
- https://gameparade.creators-guild.com/works/?category=%E3%82%B2%E3%83%BC%E3%83%A0

The site distinguishes `ゲーム` (game), `企画書` (proposal), `キャラクター（2D・3D）`, `サウンド`, `コンセプトアート・ムービー`, `フリースタイル`. Individual work pages further distinguish `プレイ可` (playable), `動画公開中` (video only at that snapshot), declared `完成` and `製作中`.

**CRITICAL:** `作品形式=ゲーム` DOES NOT IMPLY `PUBLICLY PLAYABLE GAME`. For example 2024 *Puppeteer* is categorised `ゲーム`, declares 2024-11-15 `動画公開中` and `製作中`, and lacks a confirmed downloadable game target on inspected page. 2024 *Under The Sun* is `ゲーム` and has an actual external file link for playing, plus dated Alpha/Demo/November revisions.

Therefore:
`GAME_ENTRY ≠ PLAYABLE_ARTIFACT ≠ FINISHED_GAME ≠ PAID_RELEASE ≠ SAME_AUTHOR_SECOND_GAME`.

Original P0 pages:
- Puppeteer: https://gameparade.creators-guild.com/works/2731 (redirect may yield /works/legacy-1868/)
- Under The Sun: https://gameparade.creators-guild.com/works/2237 (redirect may yield /works/legacy-1373/)

## 1. Primary-page evidence examples, explicitly NOT a complete or random cohort

These are **search-discovered examples** chosen to test schema categories, not a sampling frame. DO NOT report frequencies over these as population or annual participant statistics.

| entry | official work page | year / printed publication | platform category | artefact gate / baseline declaration | school/team identity boundary |
| --- | --- | --- | --- | --- | --- |
| はしれ！ぼうにんげん！ | https://gameparade.creators-guild.com/works/1441 | 2023-11-06 | ゲーム | creator declared finished, possible later refinements; `ゲームを遊ぶ` display seen but actual link target not independently audited | `てぃー` team handle only |
| ベジタブルプラネット！ | https://gameparade.creators-guild.com/works/1408 | 2023-11-06 | ゲーム | described as minimally playable at T0; not declared fully finished | `ソイルポケット` team |
| 光郷ノ灯神 | https://gameparade.creators-guild.com/works/1294 | 2023-10-23 | ゲーム | 2023-10-23 finished / 2023-11-09 patched | `12FPS` team; awarded label visible but no sampling inference |
| Gravity Down | https://gameparade.creators-guild.com/works/1776 | 2023-11-09 | **企画書** | production/proposal text describes 80% plan; no verified playable build | `新生制作組メンバーS` team |
| Humanoid Robot | https://gameparade.creators-guild.com/works/2223 | 2024-08-05 | ゲーム | 2024-08-05 declared completed; public game link may require separate target verification | `beta` team |
| Under The Sun | https://gameparade.creators-guild.com/works/2237 | 2024-08-05 listing, updates to 2024-11-14 | ゲーム | playable external download link confirmed on 2026-observed page; version history shows Aug alpha/Oct demo/Nov revisions | `サルバドールバッドマン` team; member listing does not imply sole developer over all lifespan |
| アメあめふレイン | https://gameparade.creators-guild.com/works/2259 | 2024-08 baseline / later update | ゲーム | author described Aug complete, Nov complete with no future additions planned; two creator declarations can differ | creator identity not independently cross-platform linked |
| Puppeteer | https://gameparade.creators-guild.com/works/2731 | 2024-11-15 | **ゲーム** | **動画公開中** and `製作中`; no confirmed playable download anchor | `leonyarudo`, author handle only |

Status logic:
- `ENTRY_PAGE_EXISTS` = observed metadata only.
- `WORK_CATEGORY_GAME` = page taxonomy, not playability.
- `DIRECT_PLAY_LINK_CONFIRMED` = a clickable game link with target exposed; *not* verification that external download still works in 2026.
- `VIDEO_ONLY` = snapshot only, not proof creator could not play private build or has stopped.
- `AUTHOR_DECLARED_COMPLETE` = author description, not commercial release.
- `CROSS_PLATFORM_SAME_AUTHOR` requires developer alias, art/mechanics, project lineage; do not attribute similarly named Steam games without evidence.

## 2. Why this does not yet answer Japanese creator formation rates

2025 Game Creator Koshien official `873 submitted works / 2,751 student entrants` aggregates multiple art/plan/game work forms and repeat submissions; it is **not** `873 complete playable games`. Original 2025 event terms and overall results:
https://game.creators-guild.com/gck2025-terms/
https://prtimes.jp/main/html/rd/p/000000072.000126454.html

This pilot did not establish:
- all 2023/2024 works in category=game, restricted to annual event;
- `GAME_ENTRY` with directly playable build across that entire year;
- number of unique author accounts vs works or group membership;
- repeat entrants within or across years;
- linked Steam commercial releases or jobs;
- time-locked state of game links at baseline instead of later edits;
- off-site cross-identity linkage.

The public catalogue exposes a game/category filter but a tool-readable **stable snapshot of all matching records** is still missing. Search results routinely show indexed pages but cannot stand in for a complete roster. A 2026-observed public page may also migrate old numeric `/works/####` to `/works/legacy-####/` IDs; preserve the original entry URL and canonical redirect together.

## 3. What actual data acquisition should do

Potential complete-cohort query, to be executed only after source completeness can be verified:
1. Enter public *works* catalogue, filter `作品形式=ゲーム`, year/tag=GC甲子園2023 OR 2024, freeze stable ordering & pagination; independently verify counts and archive each canonical work URL.
2. On each page record first publish date, current update date, exact work form, displayed status `プレイ可 / 動画公開中 / 製作中`, whether external play URL has a genuine target, and T0 version declaration. Count missing pages explicitly.
3. Deduplicate page IDs, then deduplicate author handles separately and retain many-to-many team memberships.
4. Search post-T0 author continuation across clearly self-linked official accounts only; `NOT_FOUND` cannot be called `DROPPED_OUT`.
5. Match to 2024 China CUSGA *finalists* only if using equal selection degree, or else compare Game Parade low-selection posts with unselected ordinary students in China/Taiwan. If mainland all-submission lists stay unavailable, **do not rank national rates**.

## 4. Mechanism comparison (H)

The Japanese portal makes something genuinely observable that is often lost in winner-only archives: **a work may be unfinished, only a pitch, demonstrably playable, or author-declared finished; version timelines reveal design iteration before any commercial success**. Those are valuable traces of `EARLY_CREATOR_LEARNING` and `FIRST_ARTIFACT_THRESHOLD`.

However this does not prove Japanese participants are more innovative, better trained, or commercially more successful than Taiwanese or mainland peers. The existence of an archive may also create a **measurement advantage**, making Japanese amateurs more *observable* even if real behaviours are closer than they appear. This is `OBSERVABILITY ASYMMETRY`; record it before converting any figures into national ranking.

Source status: platform creator-upload pages (P0 as self-disclosed public artefact; status itself is user-declared and unverified), organiser terms (P0), interpretation H. No private data.
