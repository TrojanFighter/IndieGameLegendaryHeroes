# 独立游戏英雄传说

[English entry](translations/en/README.md) | [贡献指南](CONTRIBUTING.md) | [研究计划总图](PROGRAM-MAP.md)

**Indie Game Legendary Heroes**  
作者 / 主创：**洪荒行者**

> **那些按照行业标准答案，本来“做不起游戏”的人，究竟是怎样把游戏做出来的？**

这是一个关于独立游戏开发者、极小团队与异常工作室如何被“生产出来”的长期研究与写作项目。

这里不把成功者重新包装成天才神话，也不把“坚持”“热爱”“运气”当作万能解释。我们追踪的是更具体的问题：他们开工前已经会什么，靠什么活下来，哪些失败其实变成了下一作的资产，什么时候开始有人付钱，团队何时扩张，哪些成本被主动砍掉，哪些机会纯属右尾事件，以及最后到底有什么能复制、什么不能复制。

当前仓库已经形成：

- **41 个编号 Case 档案**，其中 39 个 RESEARCHING、2 个 SKELETON；中国研究组包括《戴森球计划》《中国式网游》《边境》《重装前哨》《苏丹的游戏》《枪火重生》与 NExT→SYNCED 等正反 comparator，另以《征途》作为中国产业制度转折样本，编号不代表其生产史与独立资格已全部核实；
- **41 份对应 Evidence Ledger**，把流行故事拆回可核验来源；
- **14 个跨案例 Claim**，检验 runway、能力资本、solo/OPC、服务业务交叉补贴、市场接入、失败成本等命题；
- 姊妹研究 **《斯拉夫游戏英雄传说》**，追踪 GSC→4A、Wargaming、Gaijin 等组织与产业谱系；
- 正在建立的 [`book/`](book/) **读者层 / 成品叙事层**，让研究档案真正长成可连续阅读的《英雄传说》；
- [`book/INDIE-MOVEMENT.md`](book/INDIE-MOVEMENT.md) 解释本书所说的“独立游戏运动”、`independent` 与 `indie` 的区别，以及为什么 mod / UGC → 商业放大的桥梁案例也属于生产谱系研究；
- [`cross-industry/industrial-revolutions/`](cross-industry/industrial-revolutions/) 建立工业革命比较实验室，追踪技术从 invention → engineering maturity → economic viability → diffusion → complementary fit → organizational absorption，并为每个英雄人物的 Technical Opportunity Window 提供时代背景。

---

## 你想先知道什么？

不必按 CASE 编号顺读。可以从你真正关心的问题进去。

| 你想知道…… | 建议先读 |
|---|---|
| **没钱的人到底怎么把游戏做出来？** | [Kenshi](cases/CASE-012-kenshi.md) · [FTL](cases/CASE-001-ftl.md) · [Gunpoint](cases/CASE-007-gunpoint.md) · [Stardew Valley](cases/CASE-004-stardew-valley.md) · [Bills Must Be Paid](cases/CASE-025-bills-must-be-paid.md) · [Darkwood](cases/CASE-037-darkwood.md) |
| **“一个人做游戏”到底有多真？** | [Papers, Please](cases/CASE-003-papers-please.md) · [RollerCoaster Tycoon](cases/CASE-018-rollercoaster-tycoon.md) · [Schedule I](cases/CASE-019-schedule-i.md) · [Kenshi](cases/CASE-012-kenshi.md) · [中国式网游](cases/CASE-028-chinese-online-game.md) · [Manor Lords](cases/CASE-036-manor-lords.md) |
| **失败前作 / 废案是不是白做了？** | [Rocket League](cases/CASE-002-rocket-league.md) · [R.E.P.O.](cases/CASE-006-repo.md) · [Escape from Tarkov](cases/CASE-022-escape-from-tarkov-lineage.md) · [Bills Must Be Paid](cases/CASE-025-bills-must-be-paid.md) · [Landfall Games](cases/CASE-034-landfall-games.md) |
| **好游戏为什么仍然可能卖不动？** | [Brigador](cases/CASE-026-brigador.md) · [Among Us](cases/CASE-017-among-us.md) |
| **上班养游戏、接活养原创，真的能成立吗？** | [Kenshi](cases/CASE-012-kenshi.md) · [early id Software](cases/CASE-016-early-id-software.md) · [Gunpoint](cases/CASE-007-gunpoint.md) · [Rocket League](cases/CASE-002-rocket-league.md) · [Darkwood](cases/CASE-037-darkwood.md) |
| **众筹到底解决什么，不解决什么？** | [FTL](cases/CASE-001-ftl.md) · [Hollow Knight](cases/CASE-015-hollow-knight.md) · [Project Wingman](cases/CASE-009-project-wingman.md) · [Factorio](cases/CASE-035-factorio-wube.md) · [Darkwood](cases/CASE-037-darkwood.md) |
| **Early Access / 付费 Alpha 怎样变成生产资本？** | [Minecraft](cases/CASE-014-minecraft.md) · [Kenshi](cases/CASE-012-kenshi.md) · [Schedule I](cases/CASE-019-schedule-i.md) · [Factorio](cases/CASE-035-factorio-wube.md) |
| **“首款成功”之前其实练了多少年？** | [Lethal Company](cases/CASE-011-lethal-company.md) · [Dream Quest](cases/CASE-008-dream-quest.md) · [Escape from Duckov](cases/CASE-024-escape-from-duckov.md) · [Roblox creator cluster](cases/CASE-021-roblox-creator-cluster.md) · [Bills Must Be Paid](cases/CASE-025-bills-must-be-paid.md) |
| **同一个开发者 / 工作室的方法到底能不能跨项目复现？** | [Jonas Tyroller](cases/CASE-031-jonas-tyroller.md) · [Tom Francis](cases/CASE-007-gunpoint.md) · [Into the Breach / Subset](cases/CASE-020-into-the-breach.md) · [Landfall Games](cases/CASE-034-landfall-games.md) |
| **玩家 / modder 能不能先发明规则，再进入商业游戏工业？** | [PUBG / Brendan Greene](cases/CASE-032-pubg-brendan-greene.md) · [early id / DOOM](cases/CASE-016-early-id-software.md) · [Roblox creator cluster](cases/CASE-021-roblox-creator-cluster.md) |
| **发行商、孵化器和 grant 什么时候真正有用？** | [despelote](cases/CASE-023-despelote.md) · [Hollow Knight](cases/CASE-015-hollow-knight.md) · [Manor Lords](cases/CASE-036-manor-lords.md) · [Dyson Sphere Program（待核）](cases/CASE-027-dyson-sphere-program.md) |
| **为什么有的游戏发行时没爆，后来却突然爆了？** | [Among Us](cases/CASE-017-among-us.md) · [Brigador](cases/CASE-026-brigador.md) |
| **小团队怎样挑战成熟大厂品类？** | [Project Wingman](cases/CASE-009-project-wingman.md) · [Escape from Tarkov](cases/CASE-022-escape-from-tarkov-lineage.md) · [Dyson Sphere Program（待核）](cases/CASE-027-dyson-sphere-program.md) |
| **“小团队”就一定是独立游戏吗？** | [Escape from Duckov](cases/CASE-024-escape-from-duckov.md) · [Boundary（待核）](cases/CASE-029-boundary.md) · [Outpost: Infinity Siege（待核）](cases/CASE-030-outpost-infinity-siege.md) |
| **中国商业开发者的职业前史怎样影响个人或小团队创作？** | [Sultan's Game](cases/CASE-038-sultans-game.md) · [商业游戏训练反转 / Role-Origin Audit](book/research-notes/china-commercial-game-training-role-origin-audit-005.md) · [Dyson Sphere Program](cases/CASE-027-dyson-sphere-program.md) · [Boundary](cases/CASE-029-boundary.md) · [Outpost: Infinity Siege](cases/CASE-030-outpost-infinity-siege.md) · [中国式网游](cases/CASE-028-chinese-online-game.md) |
| **为什么中国可以同时拥有更好的小团队生产条件和旧产业路径依赖？** | [中国独立游戏“双层环境”](book/research-notes/china-indie-dual-environment-capability-transfer-004.md) · [Sultan's Game](cases/CASE-038-sultans-game.md) · [渠道/市场接口制度](book/research-notes/china-indie-distribution-regime-001.md) |
| **中国网游为什么会从卖时间走向 F2P、虚拟商品与运营工业？** | [《征途》/ 史玉柱](cases/CASE-033-zhengtu-shi-yuzhu.md) · [中国游戏产业前史](book/research-notes/china-game-industry-prehistory-002.md) · [《符石守护者》vs《不思议迷宫》](book/research-notes/runestone-keeper-vs-gumballs-001.md) |
| **平台本身能不能把玩家训练成开发者？** | [Roblox creator cluster](cases/CASE-021-roblox-creator-cluster.md) |
| **成功以后，第一次成功怎样改变第二作？** | [Into the Breach](cases/CASE-020-into-the-breach.md) |
| **错误的平台经验会不会反过来害你？** | [Bills Must Be Paid](cases/CASE-025-bills-must-be-paid.md) · [Sultan's Game](cases/CASE-038-sultans-game.md) · [Outpost: Infinity Siege（待核）](cases/CASE-030-outpost-infinity-siege.md) · [跨案例 Claim C009](claims/README.md) |
| **所谓“纯靠天才 / 纯靠运气 / 零营销”哪里不对？** | [跨案例综合](claims/CROSS-CASE-READINGS.md) · [Claims Index](claims/README.md) |

想先读“故事版”而不是研究档案：进入 **[`book/`](book/)**。当前样板包括 [`Kenshi`](book/profiles/kenshi.md)、[`Rocket League`](book/profiles/rocket-league.md)、[`Bills Must Be Paid`](book/profiles/bills-must-be-paid.md)、[`品味决定命运：Gunpoint 的 Tom Francis`](book/profiles/gunpoint.md) 与 [`FTL`](book/profiles/ftl.md)。

---

## 41 个编号案例档案

这些 Case 是研究后台的档案，39 个为 RESEARCHING，2 个为 SKELETON。Case ID 用于审计，不代表证据成熟度或推荐阅读顺序；少量 `NON-INDIE COMPARATOR` / `LINEAGE / TRANSITION CASE` / `BUSINESS-MODEL COMPARATOR` 保留编号用于比较生产制度或追踪原创能力的跨组织迁移，但不得因此被包装成“独立英雄”。

| Case | Subject | 它主要让我们看见什么 |
|---|---|---|
| [CASE-001](cases/CASE-001-ftl.md) | **FTL / Subset Games** | runway、地理成本、众筹与“低 burn” |
| [CASE-002](cases/CASE-002-rocket-league.md) | **Rocket League / Psyonix** | work-for-hire 养原创、失败前作、长期迭代 |
| [CASE-003](cases/CASE-003-papers-please.md) | **Papers, Please / Lucas Pope** | 大厂能力资本如何转成个人作者生产 |
| [CASE-004](cases/CASE-004-stardew-valley.md) | **Stardew Valley / ConcernedApe** | 长期 solo、伴侣/家庭支持、能力积累 |
| [CASE-005](cases/CASE-005-dwarf-fortress.md) | **Dwarf Fortress / Bay 12** | 极长周期、替代性收入、表现成本重定义 |
| [CASE-006](cases/CASE-006-repo.md) | **R.E.P.O. / semiwork** | 失败前作、再投资与更短 failure loop |
| [CASE-007](cases/CASE-007-gunpoint.md) | **Gunpoint / Tom Francis** | 工资 runway、品味→自我生产、全球协作者 |
| [CASE-008](cases/CASE-008-dream-quest.md) | **Dream Quest / Peter Whalen** | 玩家能力、职业转向与首作生产 |
| [CASE-009](cases/CASE-009-project-wingman.md) | **Project Wingman / Sector D2** | 小团队挑战成熟品类、引擎/社区/众筹 |
| [CASE-010](cases/CASE-010-undertale.md) | **Undertale / Toby Fox** | UGC、音乐与社区前史如何形成能力资本 |
| [CASE-011](cases/CASE-011-lethal-company.md) | **Lethal Company / Zeekerss** | Roblox→多次发售→Patreon/playtest→爆款 |
| [CASE-012](cases/CASE-012-kenshi.md) | **Kenshi / Lo-Fi Games** | 夜班工资、极长个人时间资本、EA 后扩团队 |
| [CASE-013](cases/CASE-013-rise-of-the-white-sun.md) | **Rise of the White Sun** | 系统抽象、历史研究与外围协作如何压成本 |
| [CASE-014](cases/CASE-014-minecraft.md) | **Minecraft / Markus Persson → Mojang** | 周末原型、付费 Alpha、公开开发、自融资 |
| [CASE-015](cases/CASE-015-hollow-knight.md) | **Hollow Knight / Team Cherry** | jam→Kickstarter，家庭收入/储蓄/基金共同构成 runway |
| [CASE-016](cases/CASE-016-early-id-software.md) | **early id Software / Commander Keen** | moonlighting、高频职业出货与 shareware 前史 |
| [CASE-017](cases/CASE-017-among-us.md) | **Among Us / Innersloth** | “完成后两年才爆”以及爆发后的组织技术压力 |
| [CASE-018](cases/CASE-018-rollercoaster-tycoon.md) | **RollerCoaster Tycoon / Chris Sawyer** | OPC 神话、长期能力资本与 contributor boundary |
| [CASE-019](cases/CASE-019-schedule-i.md) | **Schedule I / TVGS** | solo core、专业外围、EA/community infrastructure |
| [CASE-020](cases/CASE-020-into-the-breach.md) | **Into the Breach / Subset Games** | 第一次成功如何购买第二作的低 burn 与长试错 |
| [CASE-021](cases/CASE-021-roblox-creator-cluster.md) | **Roblox Creator Cluster** | 学习、出货、收入、就业与 studio formation 被压进一个平台 |
| [CASE-022](cases/CASE-022-escape-from-tarkov-lineage.md) | **Escape from Tarkov / Contract Wars → Battlestate** | 商业前置项目如何积累技术、团队、现金流与市场资格 |
| [CASE-023](cases/CASE-023-despelote.md) | **despelote** | incubator、文化资金、bridge grant、vertical slice、publisher fit |
| [CASE-024](cases/CASE-024-escape-from-duckov.md) | **Escape from Duckov / Team Soda** | `NON-INDIE COMPARATOR`：小核心≠独立所有权；公司工资、发行与流量外围如何改变可复制性 |
| [CASE-025](cases/CASE-025-bills-must-be-paid.md) | **Bills Must Be Paid / Rike Games** | 七年 mobile/web 失败与高频原型能力压缩进七个月项目；demo / Steam market model course correction |
| [CASE-026](cases/CASE-026-brigador.md) | **Brigador / Stellar Jockeys** | 强产品执行仍可被 onboarding、market legibility、受众预期与成本—市场错位击穿 |
| [CASE-027](cases/CASE-027-dyson-sphere-program.md) | **Dyson Sphere Program / Youthcat Studio** | SKELETON：人数、自筹、职业前史与发行关系待核，不预设独立正例 |
| [CASE-028](cases/CASE-028-chinese-online-game.md) | **中国式网游 / 648工作室** | 官方自述单人业余约五年；模拟网游体验的表现成本解释为 H，职业前史仍 UNKNOWN |
| [CASE-029](cases/CASE-029-boundary.md) | **Boundary / Surgical Scalpels Studio** | 已恢复制作人 / 创始人资料与首发商业信号；检验强 novelty / acquisition 已成立时的长周期 error persistence 与 multiplayer ecosystem obligation |
| [CASE-030](cases/CASE-030-outpost-infinity-siege.md) | **Outpost: Infinity Siege / Team Ranger** | SKELETON：团队归属、职业前史与产品范围待核，不预设企业负例 |
| [CASE-031](cases/CASE-031-jonas-tyroller.md) | **Jonas Tyroller / ISLANDERS → Will You Snail? → Thronefall** | 同一开发者跨三人、solo-core、两人团队的纵向方法审计：原型筛选、范围压缩、公开沟通与运气 |
| [CASE-032](cases/CASE-032-pubg-brendan-greene.md) | **PLAYERUNKNOWN / Brendan Greene: DayZ Battle Royale → H1Z1 → PUBG** | `LINEAGE / TRANSITION CASE`：mod 规则发明与社区验证怎样先于商业职位，再被 SOE / Bluehole 放大成大型公司产品 |
| [CASE-033](cases/CASE-033-zhengtu-shi-yuzhu.md) | **Zhengtu / Shi Yuzhu** | `CHINA INDUSTRY TRANSITION / BUSINESS-MODEL COMPARATOR`：市场调研、F2P、虚拟商品、县乡地推与 live ops 怎样组成新商业函数，并改变后续行业能力树 |
| [CASE-034](cases/CASE-034-landfall-games.md) | **Landfall Games** | 纵向微型工作室：产品验证后扩张、短周期原型、失败分母、长项目技术债与弹性外围 |
| [CASE-035](cases/CASE-035-factorio-wube.md) | **Factorio / Wube Software** | 自筹 demo、众筹模型修正、官网 paid alpha、creator 放大与 product-led scaling |
| [CASE-036](cases/CASE-036-manor-lords.md) | **Manor Lords / Slavic Magic** | solo core 与完整 production perimeter 的边界；grant、freelancer、QA 与 publisher 的分工 |
| [CASE-037](cases/CASE-037-darkwood.md) | **Darkwood / Acid Wizard Studio** | paid contract bridge、crowdfunding gross→真实 runway、工期误判与 EA 延展 |
| [CASE-038](cases/CASE-038-sultans-game.md) | **Sultan's Game / Double Cross** | 商业手游老兵在组织收缩后的能力迁移、scope/管理/world-model 重写与 human-cost 边界 |
| [CASE-039](cases/CASE-039-gunfire-reborn.md) | **Gunfire Reborn / Duoyi Games Gunfire Studio** | `NON-INDIE PRODUCTION-FUNDAMENTALS COMPARATOR`：premium / Early Access、T9 高 ownership span 与 evidence-led escalation；公司内部资源和 T9 formative history 保持边界 |
| [CASE-040](cases/CASE-040-tripwire-lineage.md) | **Tripwire / Red Orchestra → Killing Floor → Rising Storm** | `VALIDATION-LADDER / COMMUNITY-AS-PRODUCTION`：mod/community 先产生 playable 与 evidence，再公司化、商业化、吸收外部团队 |
| [CASE-041](cases/CASE-041-next-synced.md) | **NExT Studios portfolio → SYNCED** | `CORPORATE-INNOVATION / REGIME-TRANSITION COMPARATOR`：比较早期小型 0→1 与大型 F2P/GaaS 的 resource escalation 与 error persistence |

完整候选池、comparators 与下一批优先级见 [`cases/BACKLOG.md`](cases/BACKLOG.md)。后续新 Case 按证据与解释价值升级。`Sultan's Game` 已升级为 CASE-038，但工作室所有权、旧投资关系和 publisher financing 仍待继续审计；Artless Games 保留为中国创作路径候选。

---

## 这不是“成功学”

本项目真正想拆掉的是过度顺滑的传奇叙事。

我们会同时记录：

- **Capability**：开工前已经积累了什么能力；
- **Runway**：储蓄、工资、接活、伴侣收入、众筹、发行商、补助、前作收入；
- **Production**：核心团队、峰值团队、外包、合同工、素材、移植、QA、发行支持；
- **Scope**：到底砍掉了什么、延后了什么、把什么问题改写掉了；
- **Failure**：失败前作、废案、危机、返工与差点死亡的节点；
- **Market**：Steam、EA、付费 Alpha、平台推荐、主播、媒体、社区、发行与定价；
- **Environment**：住房、医疗、社会保障、地区成本、平台与产业环境；
- **Luck**：团队无法控制但实质改变结果的事件；
- **Transfer / Non-transfer**：什么值得学，什么只是这个人恰好拥有。

例如，“solo dev”不会自动被解释成一个人包办代码、美术、音乐、QA、市场、移植与商务；“零营销”也不会被解释成“没有任何市场接入”；同样，“五六个人开发”不会自动被解释成资本、所有权和发行意义上的 independent studio。

研究宪法与完整防错规则见 [`AGENTS.md`](AGENTS.md)。

---

## 研究后台怎么读？

本仓库把**研究档案**和**成品叙事**分开。

### Reader layer / 成品叙事

- [`book/`](book/)：面向读者的《独立游戏英雄传说》正文孵化区；
- [`book/profiles/`](book/profiles/)：已经有足够证据支持的案例叙事样板；
- [`book/INDIE-MOVEMENT.md`](book/INDIE-MOVEMENT.md)：独立游戏运动的历史、工作定义、谱系边界与中国路径差异。

这里允许有节奏、有故事、有作者判断，但关键事实必须能回指 Case / Evidence；不允许为了戏剧性隐藏支持条件或把 UNKNOWN 写成事实。

### Research backend / 研究后台

- [`cases/`](cases/)：开发者 / 团队 / 项目的可审计 Case；
- [`evidence/`](evidence/)：逐案来源核实、证据等级与边界；
- [`claims/`](claims/)：12 个跨案例、可支持也可反驳的命题；
- [`author-corpus/`](author-corpus/)：洪荒行者既有公开观点与授权历史讨论的命题来源；
- [`sources/`](sources/)：来源方法、纪录片 / 演讲 / 媒体协议；
- [`schemas/`](schemas/)：Case / Claim / Evidence 标准结构；
- [`metadata/`](metadata/)：机器可读索引；
- [`tools/`](tools/)：research lint 与维护工具。

默认链路是：

> **流行神话 / 作者旧命题 → Case → Evidence → Claim → 跨案例比较 → book 叙事。**

不是反过来先写一个好听故事，再去找证据装饰。

---

## 当前研究状态

**Phase 2 — Evidence Ingestion + Reader Layer Bootstrap**

截至 2026-10-06：

- 41 个编号 Case 已建档，其中 39 个 RESEARCHING、2 个 SKELETON；
- 41 个对应 Case Evidence Ledger 已建立；
- 14 个核心 Claims 中，C002 / C003 / C004 / C005 / C006 / C007 / C010 / C011 / C014 当前为 `SUPPORTED`；C013 当前为 `WEAK`；
- CASE-027–030 构成“中国生产制度候选组”；《中国式网游》已核官方开发自述，其余三个来源待恢复，不把候选解释视为已证正反例；
- CASE-031 将 Jonas Tyroller 作为 longitudinal practitioner，持续检验同一开发者跨项目的方法复现、方法修正、市场接入与运气边界；
- CASE-032 将 Brendan Greene / PLAYERUNKNOWN 作为 `LINEAGE / TRANSITION CASE`，区分 DayZ/Arma mod 的规则发明与社区验证、H1Z1 商业合作、Bluehole/PUBG 公司化放大；
- CASE-033 将《征途》/史玉柱作为 `CHINA INDUSTRY TRANSITION / BUSINESS-MODEL COMPARATOR`，检验市场调研、F2P、虚拟商品、县乡地推和快速运营如何组成高回报商业函数并塑造产业路径；
- CASE-034–037 为欧洲/中东欧生产结构组：Landfall（纵向工作室与失败分母）、Factorio/Wube（paid-alpha runway）、Manor Lords（solo-core 与外围边界）、Darkwood（众筹与 EA scope 压力）；
- CASE-038 将《苏丹的游戏》作为中国商业手游老兵重组为 premium 小团队的能力迁移与组织模型切换案例；
- `book/research-notes/china-commercial-game-training-role-origin-audit-005.md` 开始以腾讯及相邻样本审计岗位子类型、prototype authority、design-loop proximity 与 ownership span，不把“程序员 > 策划”当成既成结论；
- CASE-026 仍是第一例正式以 **failure comparator** 为中心编号的 Case；
- `book/` 已有 Kenshi、Rocket League、Bills Must Be Paid、Gunpoint、FTL 等 profile，并已建立独立游戏运动史、目标形成、玩家→生产者等书级研究入口。

研究状态以 [`cases/BACKLOG.md`](cases/BACKLOG.md)、各 Case / Evidence Ledger 与 [`claims/README.md`](claims/README.md) 为准；README 只做项目级导航，不替代正式档案。

---

## 姊妹篇：《斯拉夫游戏英雄传说》

[`sister-projects/slavic/`](sister-projects/slavic/README.md) 独立保存《斯拉夫游戏英雄传说》的研究、证据与书稿入口，研究俄罗斯、乌克兰、白俄罗斯及邻接产业网络中的游戏生产谱系，包括：

- GSC Game World → 4A Games / Metro 的人才与组织迁移；
- Wargaming / World of Tanks 的产业级转折；
- Gaijin / War Thunder 的技术与产品谱系；
- 俄罗斯系统型、军武型与作者型工作室的长期生产结构。

这里同样拒绝“某一个民族天生更会做某类游戏”之类的简化解释，而是追踪人才、技术、资本、组织与市场路径。

本篇 [证据索引](sister-projects/slavic/evidence/README.md) 包含 8 个编号专题及 2 份保留的并行矩阵稿；专题不等同正式 Case，不计入上面的 38 个独立篇 Case。本篇 [书稿入口](sister-projects/slavic/book/README.md) 当前没有正式 Profile。两篇共享方法论与工具，分别维护资料索引与阅读入口；不按开发者国籍机械搬动独立篇案例。

---

## 作者思想来源与证据边界

项目的一部分问题意识来自洪荒行者此前在知乎、微信公众号“游戏炼乳”、长文与历史讨论中形成的观点。这些历史材料统一作为 **A0 — Author-Origin**：用于回答“命题从哪里来”，不自动成为外部事实。

默认流程：

> **作者旧命题 → 精确化为 Claim → 外部 Case / P0-P1-S1 Evidence → 支持、修正或反驳。**

作者语料与历史公开行业研究的边界见 [`sources/SOURCE-001-author-platforms-and-chat-corpus.md`](sources/SOURCE-001-author-platforms-and-chat-corpus.md)。纪录片、GDC、访谈和媒体的分级方法见 [`sources/SOURCE-002-documentary-talk-media-protocol.md`](sources/SOURCE-002-documentary-talk-media-protocol.md)。

---

## 传播、权利与许可

本项目希望论证被看见、讨论和传播，但不希望第三方未经许可改写成另一个版本、制造“洪荒行者其实是在说……”的伪官方解释，或直接拿去商业出版。

因此采用分层许可：

- **公开研究内容**：`cases/`、`claims/`、`schemas/` 及其他明确作为公开研究发布的原创非软件内容，采用 **CC BY-NC-ND 4.0**。欢迎非商业地复制、转发、镜像和重新发布未经改编的原文，但必须合理署名，且不得发布未经授权的改写、翻译或其他衍生版本。详见 [`LICENSE-CONTENT`](LICENSE-CONTENT)。
- **正式书稿 / reader layer**：`book/` 目录中的正式章节、出版稿、叙事样稿，以及任何明确标注 `All Rights Reserved` 的内容，均为 **© 2026 洪荒行者。All Rights Reserved.**
- **工具代码**：明确属于软件 / 工具范围内的脚本、构建工具、检查器等代码，按 [`LICENSE-CODE`](LICENSE-CODE) 的 MIT License 授权。
- **第三方材料**：引用、截图、商标、采访内容及其他第三方材料仍属于其各自权利人。

### Canonical source / 权威原文

欢迎对本项目进行摘要、评论、批评和讨论，但第三方解释只代表其作者。

如需确认“洪荒行者 / 《独立游戏英雄传说》究竟主张什么”，请以本仓库中对应 Case / Claim / book 文章的**最新版原文**为准。

合理署名时，建议至少保留：

> 作者：洪荒行者  
> 项目：《独立游戏英雄传说 / Indie Game Legendary Heroes》  
> 原文：对应 GitHub canonical URL  
> 许可：按对应目录的许可说明

公开可读不等于放弃版权；鼓励传播也不等于允许商业利用或擅自改写。
