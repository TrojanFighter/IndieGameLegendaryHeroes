# 006 — 年度观察数据字典（1958–2026）

**年度数据 CSV**：[`006-annual-production-capability-observations.csv`](006-annual-production-capability-observations.csv)

范围包括每年一行（1958—2026），但不意味着 1959 等年份缺少游戏；**空单元格=本次没有匹配的已核事实，不是产量为零、不证明不可制作**。

| 字段 | 分母及解释 |
|---|---|
| `historical_anchor` / `anchor_kind` | 人工挑选的同期有日期事件；**非全量**，非“该年首次”；只做索引 |
| `steam_total_games` | SteamDB 全站「该年发行」口径，2006—2025；不是全部游戏产业 |
| `steam_2d_platformer_tag` | SteamDB 标签 `2D Platformer`，包含当年以外补标、交叉标签；不代表 2D 游戏总量 |
| `steam_3d_platformer_tag` | SteamDB 标签 `3D Platformer`，与上列平行但标签可变化，不能保证作品不会被同时标注 |
| `steam_top_down_shooter_tag` | SteamDB「Top-Down Shooter」，**不能直接把这个标签等于全部 2D** |
| `steam_open_world_survival_craft_tag` | SteamDB「Open World Survival Craft」，**不能直接把它等于全部 3D** |
| `ggj_submitted_games` | GGJ 当年活动提交作品；均为 jam 原型，非商业发售；作者、游戏不能一一对应 |
| `ggj_registered_jammers` | GGJ 当年官方登记参与者；2026 采 2026-04-13 官方调研公布 39,197，GGJ 2026-02-10 早报 39,069 |
| `fortnite_creators` | Epic 年度创作者规模，2023=24,000、2024=70,000；可能与商业发行商口径不同 |
| `fortnite_published_islands` | Epic 2024=198,000 公开岛屿；其中 137,000 via UEFN，不能视为 198,000 个互不关联的独立商业游戏 |

## 来源与冻结口径（2026-10-09）

- [SteamDB 全站年度发售](https://steamdb.info/stats/releases/)
- [SteamDB 2D Platformer](https://steamdb.info/stats/releases/?tagid=5379)
- [SteamDB 3D Platformer](https://steamdb.info/stats/releases/?tagid=5395)
- [SteamDB Top-Down Shooter](https://steamdb.info/stats/releases/?tagid=4637)
- [SteamDB Open World Survival Craft](https://steamdb.info/stats/releases/?tagid=1100689)
- [GGJ 历史逐年统计](https://globalgamejam.org/history)（2011 games 标作「1,500+」，所以该数值栏 **留空**）
- [GGJ 2026-04-13 Survey](https://globalgamejam.org/news/global-game-jam-2026-jammer-survey-data)
- [Epic 2024 Creator Year in Review（发布于2025-01-22）](https://www.fortnite.com/news/fortnite-ecosystem-2024-year-in-review-celebrating-creators-and-looking-ahead)
- [历史节点与证据等级规则](005-game-production-capability-timeline.md)

注意：SteamDB 是**实时重算的标签快照**。例如原 005 曾记录 2024 3D Platformer 为 1,355，而本次重新读取页面曾见 1,374，2025 从 1,445 变化到 1,479；**不能将不同日期的快照画成历史增长**。本表当作 `snapshot_version=2026-10-09-web-observation`，不承诺站点保持不变。2026 平台发行年尚未完结且网页统计可能包含后来修改，Steam 列一律空。

2013 GGJ 官方页面与不同文稿关于注册人数存在冲突（例如 press kit 使用约 40,000），CSV 优先 `/history` 逐年表的 `16,705`，并不表示冲突已解决。2025 的官方数据也有 35,427 与 35,470 等版本，应保留来源冲突记录，暂不用于精确人效比。

## 历史锚点外链 Key

- `CHM`: https://www.computerhistory.org/timeline/graphics-games/
- `ARCADE`: https://www.arcade-museum.com/Videogame/battlezone
- `NINTENDO`: https://www.nintendo.com/jp/character/mario/en/history/index.html
- `WOS`: https://worldofspectrum.net/item/0003012/
- `ELITE`: https://elite.bbcelite.com/
- `GM`: https://gamemaker.io/en/blog/gamemaker-25
- `UNITY`: https://unity.com/news/unity-technologies-celebrates-six-years-continual-leadership-and-innovation
- `UE4`: https://www.unrealengine.com/blog/epic-games-releases-unreal-engine-4-for-all
- `KICK`: https://www.kickstarter.com/projects/jonaskaerlev/a-hat-in-time-3d-collect-a-thon-platformer
- `XBOX`: https://www.xbox.com/en-US/games/store/pumpkin-jack/9N7TB1SB2M0K
- `STEAM`: https://store.steampowered.com/app/1966720/Lethal_Company/
- `EPIC`: https://www.fortnite.com/news/fortnite-ecosystem-2024-year-in-review-celebrating-creators-and-looking-ahead
- `GGJ`: https://globalgamejam.org/news/global-game-jam-2026-jammer-survey-data
- `VALVE`: https://store.steampowered.com/news/
- `CASE`: https://github.com/TrojanFighter/IndieGameLegendaryHeroes/blob/main/cases/README.md

- `NINTENDO_HISTORY`: https://careers.nintendo.com/our-history/
- `COUNTER_STRIKE`: https://blog.counter-strike.net/history/
- `STEAM_HAT`: https://store.steampowered.com/app/253230/A_Hat_in_Time/
- `EPIC_CREATIVE`: https://www.fortnite.com/news/creative
- `EPIC_UEFN`: https://www.fortnite.com/news/unreal-editor-for-fortnite-and-creator-economy-2-0-are-here-new-worlds-await

## 可做与不可做

**可以**：在相同数据快照和 Steam 平台内比较 2D/3D Platformer 各发售年份的*标签数量*、可观察品类供应趋势；比较 GGJ 同口径 jam 原型与人群规模的不同年度；讨论 UEFN 作者生态的生产量级。

**不可以**：据 Steam 标签数宣称「2D／3D 哪一个开发者更多」、据 GGJ 推测全职业开发者、据 3D 个案声称某一年中型团队普及、以有一部爆款认定 Q1/Q2/Q3 已成立。真正作者群体量产还要有 developer ID 去重、项目类型核验、商业／非商业分类和被取消项目分母。

## 2015 Jam 一个可计算的作者量级锚点

[GGJ 官方 2015 回顾](https://v3.globalgamejam.org/news/ggj-2015-official-stats) 同时披露 **5,438 games、约 28,800 registered jammers、1,032 solo / single-member teams**。单人团队数据与官方某些团队人数加总并非完全一致，不能直接除出独立完成率；它足以证明至少需要将个人制作和社区量产的产出类型分开。

