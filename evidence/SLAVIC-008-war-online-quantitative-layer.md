# SLAVIC-008 — WoT / WoWP / WoWS / War Thunder 早期量化层

- Type: Quantitative Evidence Ledger
- Program: 《斯拉夫游戏英雄传说》
- Status: ACTIVE — FIRST PASS
- Last updated: 2026-10-03
- Companion: `SLAVIC-007-wot-wowp-wows-war-thunder-product-structure-matrix.md`

## 研究问题

本页不做简单“谁玩家多”的排行榜，而检验：

> **SLAVIC-007 中观察到的产品结构差异，是否在各产品 launch / early-service 阶段留下可观察的商业与活跃度差异？**

必须首先承认数据口径不统一。公开材料混有：

- registered users / registrants；
- beta participants；
- people who have played；
- peak concurrent users（PCCU）；
- daily active users（DAU）；
- total battles / sorties；
- average session / daily play time；
- 公司自己对“成功/不成功”的定性判断。

这些指标不可互换。

因此本页按“指标类型 + 时间点 + 地区 / 版本边界”记录，**禁止把注册量直接当活跃量或留存率。**

---

## 1. World of Tanks — 极快扩大为大众在线产品

### E1 — 2011 年末：18M 注册，>250K 并发里程碑

Wargaming / World of Tanks 官方 2011 年回顾称：

- 2011 年 2 月曾以 90,000+ 单一 cluster 峰值并发创 Guinness 纪录；
- 随后继续刷新，最终超过 250,000 simultaneous players；
- overall audience 超过 18,000,000 registered users。

Source:
- World of Tanks official, `World of Tanks 2011 Video Top 5`
- https://worldoftanks.com/en/news/general-news/world-tanks-2011-video-top-5/
- Evidence class: P0/OFFICIAL-CONTEMPORARY

Boundary:
- 页面在同段同时讨论 single-cluster Guinness 与随后更高 concurrent record，因此 250K 的确切 cluster/global 口径需要进一步核原始 Guinness / server post；暂不把它与其他游戏全球 PCCU 直接等号比较。

### E2 — 2013 年：55M 注册、全球 PCU ~1.3M

Wargaming 2013 GDC 公开材料给出：

- 55 million registered players；
- global Peak Concurrent Users around 1.3 million。

Source:
- World of Warplanes / Wargaming official GDC recap, `Wargaming at GDC`
- https://worldofwarplanes.com/news/wargaming-gdc/
- Evidence class: P0/OFFICIAL-CONTEMPORARY

Interpretation:
- WoT 不只是高注册漏斗；至少到 2013 年已经表现出与注册规模匹配的超大并发活跃池。

### E3 — 2013 年公司级材料：多百万 DAU / 约 1M PCCU

Wargaming 后续官方事实页引用公司管理层说法：

- overall daily active users 已超过 several million；
- PCCU 曾长期约 900K，随后突破 1M。

Source:
- Wargaming, `20 Things You Didn’t Know about Wargaming`
- https://wargaming.com/en/news/wargaming_facts/
- Evidence class: P1/OFFICIAL-RETROSPECTIVE / contemporaneous quote aggregation

Boundary:
- 该页的具体引语时间应继续追原始新闻稿；第一轮只作为规模级别互证。

### First-pass reading

WoT 的早期数据同时具备：

- 大注册盘；
- 大 PCCU；
- 多百万级 DAU 说法。

因此“只是营销拉来很多注册但留不住”与公开数据明显不符。

---

## 2. World of Warplanes — 高注册漏斗，但活跃 / 留存证据明显更弱

### E1 — 2013-08：正式上线前接近 3M beta registrants

World of Warplanes 官方上线预告称：

- Open Beta 启动约两个月后；
- 已接近 3 million beta registrants；
- 累计超过 202 million combat flights。

Source:
- World of Warplanes official, `World of Warplanes Soars to Release`, 2013-08-20
- https://worldofwarplanes.com/news/world-of-warplanes-release-date-announced/
- Evidence class: P0/OFFICIAL-CONTEMPORARY

### E2 — 这个数字不能解释成“3M 活跃用户”

`beta registrants` 是获取 / 注册口径，不是：

- DAU；
- MAU；
- PCCU；
- retention；
- paying users。

当前第一轮官方检索尚未找到与 WoT 2011–2013 同等级清晰的 WoWP DAU / PCCU 披露。

**Absence of evidence 不是 evidence of absence。**

但这个缺口本身非常重要：WoWP 在上线前拥有很强的用户获取和品牌导流，却仍被 Wargaming 自己在 2014 年公开承认为 `not as successful as World of Tanks`。

参见：`SLAVIC-004-world-of-warplanes-contrast.md`。

### First-pass reading

一个关键反例开始成立：

> **高 beta 注册量证明“市场能把人拉进来”，但不能证明核心交互能把人留下。**

这使 WoWP 成为区分 acquisition 与 retention / engagement 的重要案例。

当前不能写：

- “WoWP 只有 3M 用户”；
- “WoWP 留存一定很差”；
- “因为官方没披露 PCCU，所以 PCCU 很低”。

这些都需要进一步数据。

---

## 3. World of Warships — 测试期起量较慢，但可观察 engagement 较强

### E1 — 2014 Global Test Event：约 50K 参与，RU 峰值并发约 5K

Wargaming 2014 年度回顾称：

- nearly 50,000 players 参加首次 global test event；
- just under 100,000 battles；
- RU server peak simultaneous users around 5,000。

Source:
- Wargaming, `Wargaming in 2014: 10 Memorable Events`
- https://wargaming.com/en/news/wargaming_in_review_2014/
- Evidence class: P0/OFFICIAL-CONTEMPORARY

Boundary:
- 这是非常早期测试事件，不能与正式上线后的 PCCU 比较。

### E2 — 2015 Closed Beta：400K+ participants

Wargaming Open Beta 公告称，Closed Beta 结束时有：

- over 400,000 sailors / testers；
- 随后进入 Global Open Beta。

Source:
- Wargaming, `Full Speed Ahead for World of Warships Global Open Beta`
- https://wargaming.com/en/news/obt_launch/
- Evidence class: P0/OFFICIAL-CONTEMPORARY

专业媒体同期引用开发总监 Daniil Volkov 时进一步给出：

- 约 410,000 CBT players；
- 平均每天约 2 小时游戏时间。

Source:
- PCGamesN, `World of Warships proudly sails into global open beta`, 2015-07-02
- https://www.pcgamesn.com/world-of-warships/world-of-warships-proudly-sails-into-global-open-beta
- Evidence class: S1 contemporaneous media quoting developer

### E3 — 2015-09 正式发售前：约 2M players，约 3 hours/day 说法

Game Informer 在正式发售公告时报道：

- Open Beta 阶段已约 2 million players；
- players playing an average of three hours a day。

Source:
- Game Informer, `World Of Warships Leaves Open Beta And Enters Full Release This Month`, 2015-09-02
- Evidence class: S1 contemporaneous professional media; likely based on Wargaming launch material

Boundary:
- “平均每天 3 小时”的分母口径不明：可能是活跃玩家、参与日玩家或其它内部统计；不能直接与现代 DAU session length 横比。

### First-pass reading

WoWS 的早期轨迹更像：

> 早期测试池不巨大 → CBT 扩至 400K+ → OBT 进入百万级 → 正式上线前约 2M，同时有较高 playtime proxy。

这与“海战对象需要更长测试与玩法重构，但一旦找到结构后可以形成强 engagement”的假说相容。

**相容不等于因果证明。**

---

## 4. War Thunder — 从小于 WoT 的起点快速形成强活跃池

War Thunder 的公开里程碑异常连续，适合做早期增长曲线。

### E1 — 2013-01-28 Global Open Beta：CBT 已有 600K+ players / 60M+ matches

官方全球 Open Beta 公告称：

- Closed Beta 超过 600,000 players；
- 超过 60 million matches。

Source:
- War Thunder official, `War Thunder enters global Open Beta!`, 2013-01-28
- https://warthunder.com/en/news/75--en
- Evidence class: P0/OFFICIAL-CONTEMPORARY

### E2 — 2013-03-05：超过 1M players

Source:
- War Thunder official, `More Than One Million Players Served!`
- https://warthunder.com/en/news/91-
- Evidence class: P0/OFFICIAL-CONTEMPORARY

### E3 — 2013-07-25：超过 3M players

官方同时披露：

- 3M+ players；
- 600M+ sorties；
- 30M+ hours flown。

Source:
- War Thunder official, `3 million players!`
- https://warthunder.com/en/news/216-
- Evidence class: P0/OFFICIAL-CONTEMPORARY

### E4 — 2013-11：约 5M players

官方一周年材料称，在 Open Beta 的一年内已有约 5 million players。

Source:
- War Thunder official, `Happy birthday, War Thunder!`, 2013-11-05
- https://warthunder.com/en/news/323--en
- Evidence class: P0/OFFICIAL-CONTEMPORARY

### E5 — 2014-04：6M+ players

Gaijin 宣布腾讯中国发行协议时称：

- War Thunder worldwide more than 6 million players。

Source:
- War Thunder official, `WAR THUNDER TO LAUNCH IN CHINA IN 2014`, 2014-04-21
- https://warthunder.com/en/news/548/current
- Evidence class: P0/OFFICIAL-CONTEMPORARY

### E6 — 2014-05-16：100K concurrent players

官方直接宣布：

- 100,000 concurrent players online；
- 后续活动页明确说是 PC + Mac concurrent players。

Sources:
- https://warthunder.com/en/news/592-100000-Players-Online-en
- https://warthunder.com/en/devblog/current/604
- Evidence class: P0/OFFICIAL-CONTEMPORARY

### First-pass reading

War Thunder 的量化材料说明：

- 它在全球 OBT 后约一个多月达到 1M；
- 约半年达到 3M；
- 约九个月达到 5M；
- 2014 年春达到 6M+；
- 同年 5 月达到 100K concurrent。

这不是“只有少数硬核模拟器玩家”的市场表现。

因此 SLAVIC-007 的一个关键判断获得量化支持：

> **Gaijin 的模式分层 / 控制辅助至少没有把产品困在传统飞行模拟器的小众规模。**

但仍不能仅凭这些数字证明“模式分层导致增长”。

---

## 5. 第一轮可比较矩阵

> 注意：只有同列、同口径、时间位置相近时才适合横向比较。

| Product | Early acquisition / registration | Early engagement / PCCU | Qualitative outcome |
|---|---|---|---|
| World of Tanks | 2011 年末 18M registered | 2011 年 >250K concurrent milestone；2013 global PCU ~1.3M | 超大规模 breakout；Wargaming 公司史转折 |
| World of Warplanes | 2013-08 上线前近 3M beta registrants | 第一轮未找到可与 WoT 对等的公开 DAU/PCCU | Wargaming 2014 明确认可：不如 WoT 成功 |
| World of Warships | 2014 test 50K；2015 CBT 400K+；正式上线前约 2M | 2014 RU test peak ~5K；CBT 媒体引述约 2h/day；OBT/launch 媒体引述约 3h/day | 起量慢于 WoT，但形成持续大规模产品 |
| War Thunder | 2013-01 CBT 600K+ → 3 月 1M → 7 月 3M → 11 月 5M → 2014-04 6M+ | 2014-05 100K PCCU | 独立于 WoT 起源、但进入同一大众军武在线市场 |

---

## 6. 量化层对现有假说的影响

### H1 — `WoT 的优势只是先发 + Wargaming marketing`

**Status: WEAKENED / insufficient**

原因：
- WoWP 能获得近 3M beta 注册，说明 Wargaming 的品牌和流量导入非常强；
- 但公司仍承认其商业表现明显弱于 WoT；
- 因此 acquisition capability 本身不足以解释长期结果。

### H2 — `核心交互摩擦会出现在 acquisition 之后的 engagement / retention 层`

**Status: SUPPORTED AS RESEARCH DIRECTION**

WoWP 是关键：高注册并没有自动变成 WoT 级别的公开活跃规模。

但缺失直接 retention cohort，因此暂不能升级为 VERIFIED。

### H3 — `WoWS 的成功来自更长时间重构海战，而不是简单复制 WoT`

**Status: SUPPORTED / NOT PROVEN CAUSALLY**

已有：
- 早期小规模测试；
- 400K+ CBT；
- 约 2M OBT/launch 用户；
- 高 playtime proxy；
- 开发者明确拒绝“水上坦克”。

这些与“重构后逐步放大”的路径一致。

### H4 — `War Thunder 模式分层把传统模拟能力放大成大众市场`

**Status: SUPPORTED / causality unresolved**

早期用户增长和 100K PCCU 表明，它确实突破了传统飞行模拟器小众规模。

仍需：
- Arcade / Realistic / Simulator 各模式玩家占比；
- 新用户首选模式；
- 各模式留存 / 付费差异。

---

## 7. 一个新的方法论结论：注册量是最危险的“漂亮数字”之一

这四个案例证明，研究 F2P 历史时必须把 funnel 拆开：

> exposure → registration → first battle → return → retained active → payer → long-term hobby

`registered users` 只能证明前半段的一部分。

特别是 WoWP：

> **近 3M beta registrants 与“没有复制 WoT 成功”可以同时成立。**

因此未来任何 Case 出现：

- `10M registered users`；
- `X million downloads`；
- `Y million accounts`；

都不得自动翻译成：

- `成功留存了 X/Y million players`；
- `有同规模活跃社区`；
- `商业表现等同于更高 PCCU / DAU 产品`。

这条应作为整个仓库的定量防错规则候选。

---

## 8. 下一轮证据缺口

1. WoWP 2013–2015：PCCU、DAU、MAU、收入、payer、retention；
2. WoT 2010–2011：将 250K concurrent 的 cluster/global 口径彻底核死；
3. WoWS 2015：找到 Wargaming 原始 2M / 3h-day 新闻稿，替代媒体转述；
4. War Thunder 2013–2015：模式分布、PCCU 时间序列、地区分布；
5. 统一构建“上市/OBT 后第 30/90/180/365 天”的 milestone table，仅在有同口径数字时比较；
6. 搜索 Wargaming / Gaijin 财务、招聘、服务器扩容、地区代理数据，将用户规模与组织扩张联系起来。

## 当前判词

> **第一轮量化数据支持“可迁移商业能力 ≠ 可迁移用户参与结构”。WoT 的 breakout 同时体现于注册和活跃规模；WoWP 证明强品牌可以制造巨大 acquisition，却不能单靠这一点复制 WoT；WoWS 显示经重新设计的相邻载具产品可以逐级形成较强 engagement；War Thunder 则证明长期飞行问题域能力可以被放大到大众在线规模。**

这仍不是因果终局。真正决定性的数据缺口是：WoWP 留存 / DAU，以及 War Thunder 各难度模式的用户分布。
