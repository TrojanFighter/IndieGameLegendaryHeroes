# Failure Workshop — 失败生产史与复盘索引

- Status: ACTIVE
- Scope: public industry research only
- Last updated: 2026-10-05

本栏目专门收集**开发者公开讲述“哪里失败了、为什么失败、后来怎样恢复或改写问题”**的一手/近一手材料。

它不是“失败游戏排行榜”，也不要求每个对象都服务某个既有 Claim。目的恰恰是降低成功者偏差：把没有爆、没有活下来、没有按计划完成、甚至在商业上失败但设计仍然优秀的生产史保留下来。

GDC 的 `Failure Workshop` 是本栏最重要的长期来源之一。GDC Vault 显示该系列至少从 2011 延续到 2022，并覆盖设计、生产、商业、市场、组织、健康与成功后的心理问题。

## Failure taxonomy

每个对象至少区分失败发生在哪一层，禁止用一个 `FAILED` 标签抹平因果：

- `DESIGN FAILURE`：核心 fantasy、规则组合、UX、onboarding 或玩法问题没有成立；
- `SCOPE / PRODUCTION FAILURE`：时间、工具、团队或复杂度失控；
- `MARKET FAILURE`：产品成立，但需求、定位、定价、可读性或受众规模不足；
- `MARKET-ACCESS FAILURE`：没有形成足够的 wishlist、媒体、creator、平台推荐、发行触达或社区密度；
- `PUBLISHING / BUSINESS FAILURE`：合同、publisher、平台、渠道、融资或收入结构出现问题；
- `ORGANIZATION FAILURE`：团队、工作室结构、沟通、固定成本或成长方式失效；
- `TECHNICAL FAILURE`：技术债、服务器、性能、工具或平台条件击穿项目；
- `TIMING / EXTERNAL SHOCK`：无法控制的窗口、竞争、政策、平台或其他外生变化；
- `HEALTH / HUMAN COST`：项目可能“做完了”，但以不可持续的身体、心理或关系代价完成；
- `POST-SUCCESS FAILURE`：商业成功之后仍出现组织、心理、技术或下一阶段失败；
- `ABANDONED / UNFINISHED`：未发布项目；不要因为没有销量就把它和商业失败混为一谈。

一个项目可以同时命中多类，但必须按时间链说明哪个是原因、哪个是后果。

## Promotion rule

Failure Workshop 条目不自动获得正式 Case ID。

只有满足至少一项才升级：

1. 能直接检验现有 Claim 或形成强反例；
2. 有足够 P0/P1/S1 证据重建生产时间线；
3. 暴露当前 corpus 尚未覆盖的失败机制；
4. 对“独立游戏为什么活不下来”具有高解释价值；
5. 成功/失败边界本身值得重新定义。

正式 Case 必须同时记录：**作者当时为什么认为这个项目值得做**，不能只从结局倒推“早该知道”。

---

## Anchor 01 — VIDEOBALL / Action Button Entertainment

- Speaker: Tim Rogers
- Key public source: GDC 2017 `Failure Workshop`
- Current status: `PRIORITY DEEP-DIVE / NOT YET NUMBERED`
- Initial failure classes: `MARKET FAILURE` + `PUBLISHING / BUSINESS FAILURE` + `SCOPE / PRODUCTION DRIFT?` + `MARKET-ACCESS / NETWORK-DENSITY RISK?`

### Why it matters

`VIDEOBALL` 是本栏非常强的锚点，因为它不是一个容易用“产品做烂了”解释的失败。

公开资料同时显示：

- 2016 年 Tim Rogers 还在 GDC 以 `Videogames Are Better Than Sports` 为题，把 VIDEOBALL 当作长期思考后的“电子运动”设计实验公开讲述；
- 游戏正式发行于 2016-07-12，Steam 当前仍是 `Very Positive`，商店页显示约 90% Steam purchaser reviews 为正面；
- GDC 2017 的 Failure Workshop 明确把它作为失败案例，官方简介称 Rogers 将讨论 VIDEOBALL 的 `business accidents` 与各种 `what went wrongs`；
- 同期报道概括其路径为：一个表面简单、深度很高的抽象电竞/运动项目，经历了过度复杂的开发过程、publisher 问题，以及最终的财务失败；
- 2016 年 Game Developer 的采访已经暴露一个关键矛盾：团队主动追求极简、可读、可观战，但这种极简同时让外部观察者不断建议他们“AAA it up”或改成更容易卖的视觉/产品形式。

这使 VIDEOBALL 特别适合研究：

> **一个设计上高度自洽、评价良好、甚至极度重视 legibility 的游戏，为什么仍然无法生成足够市场密度？**

### First-pass research questions

1. 原型最初的目标到底是 `one-button StarCraft`、新体育项目，还是可成为 esport 的数字运动？目标在几年开发中怎样漂移？
2. “极简”究竟降低了多少 production cost，又制造了多少 market-legibility / fantasy 缺失？
3. 这个项目需要的是否不是“普通销量”，而是高密度重复对局、朋友局、赛事、线上匹配池，因此存在明显 network-threshold problem？
4. publisher 关系具体发生了什么？Midnight City、Iron Galaxy、平台版本、延期与商业条款之间怎样串联？
5. 开发周期为何从早期 prototype 拉长到多年？哪些工作真正提高了产品，哪些属于支持多平台/online/ranked/大量地图等复杂度扩张？
6. Tim Rogers 的媒体/评论者身份是否提供了 awareness，却不能转化为持续活跃玩家密度？
7. 好评与商业失败为什么同时成立？
8. 如果今天有 Remote Play Together、Discord、短视频、Steam Next Fest 等条件，机制是否改变，还是核心 fantasy 仍然难卖？

### Evidence anchors

- GDC 2017 — `Failure Workshop`: https://www.gdcvault.com/play/1024287/Failure
- GDC 2016 — `Videogames Are Better Than Sports`: https://gdcvault.com/play/1023454/Videogames-Are-Better-Than-Sports
- Game Developer 2016 — `Videoball, and the challenge of designing (and selling) simplicity`: https://www.gamedeveloper.com/business/-i-videoball-i-and-the-challenge-of-designing-and-selling-simplicity
- Game Developer 2017 — Failure Workshop recap: https://www.gamedeveloper.com/business/watch-and-learn-what-these-game-devs-learned-from-failure
- Steam store: https://store.steampowered.com/app/277390/VIDEOBALL/

这些来源足以证明它值得深挖，但**尚不足以写精确销量、亏损额、publisher 合同因果或“电竞失败的唯一原因”**。

---

## GDC Failure Workshop seed index

以下先作为 intake 索引，不代表已完成核验：

| Year | Speaker / Project | Why it may matter | Current action |
|---|---|---|---|
| 2011 | George Fan, Kyle Gabler, Kyle Gray, Chris Hecker, Brad Wardell, Matthew Wegner | 早期 Failure Workshop；用于恢复栏目源流 | source recovery |
| 2012 | Shadow Physics; Sugar Rush; Bastion development failure; unfinished Colin Northway project | 明确扩展到 business / marketing / production；成功作品也可拥有失败阶段 | priority source ingestion |
| 2015 | Steve Swink; Ben Esposito; Adam Saltsman; Will Stallwood | GDC 明确批评 conference success bias | source ingestion |
| 2016 | Tower of Guns aftermath; Frozen Cortex; Chaim Gingold small-project drift | post-success failure、genre/fantasy mismatch、prototype hell | priority cluster |
| 2017 | Game Oven closure; Citystream; VIDEOBALL | studio closure、platform experiment、market/business failure | VIDEOBALL priority |
| 2018 | Moon Hunters; Brigador | buggy launch vs commercial failure; Brigador 已有 CASE-026 | back-link CASE-026 |
| 2019 | Failure Workshop 2019 | exact project/speaker inventory 待恢复 | source recovery |
| 2020 | DualJoy; Quench; Love Is Dead; FutureGrind | premature spend、too-many-hats、mental health、6-month→4.5-year scope failure | priority cluster |
| 2021 | Failure Workshop 2021 | exact project inventory 待恢复 | source recovery |
| 2022 | SkyRider; jam→full-time mismatch; genre mismatch; success/failure beyond sales | sunk-cost persistence、jam translation、genre fit、failure definition | high priority |

## Existing corpus back-links

- `CASE-026 Brigador / Stellar Jockeys` 已经是正式 failure comparator，应把 GDC 2018 Failure Workshop 作为其关键一手来源之一继续补证；
- `Capability–Project Fit` 的反压力可以从本栏取材，但本栏**不以证明该框架为目的**；
- 一个 Failure Workshop 对象如果最终证明产品/能力适配很好但商业仍失败，可以作为 `FIT-STRONG but commercially failed`；如果完全不相关，则保留在 Failure Workshop，不强行服务任何理论。

## Intake discipline

以后发现开发者复盘失败时，优先记录：

1. 当时的原始目标；
2. 当时实际可见的信息，而不是今天 hindsight；
3. 决策链与关键 pivot；
4. 团队、预算、runway、publisher/platform 条件；
5. 产品质量与商业结果分开；
6. 开发者自己认为失败在哪里；
7. 外部证据是否支持其自我解释；
8. 后来是否把失败资产转成下一作能力资本；
9. 是否真正恢复、关闭、转行，或成功后仍承担长期代价。

Failure Workshop 的价值不是证明“失败也很美”，而是建立一套**失败的生产史**。