# Codex 交接任务｜《独立／斯拉夫游戏英雄传说》叙事与阅读体验试验（2026-10-09）

> **状态：READY FOR CODEX / NOT STARTED。** 本文件是任务交接，不是已批准的正文、事实源、第二套 Editorial Gate 或已完成的改写。
>
> **目标仓库：** `TrojanFighter/IndieGameLegendaryHeroes`（只处理该公开研究／书稿仓库）。
>
> **Owner / 实施 Lane：** Lane C — Editorial / Book Layer。任务文档本身与索引属于 Lane A；如确需修改流程规则，另开 Lane A PR。史料缺口走 Lane B。
>
> **主要目标：** 把大量已经整理的 Case / Evidence / Claim 转化为读者愿意连续阅读的人物传记和专题，而不牺牲历史忠实性、作者的有锋芒的观点与决策应用价值。
>
> **交接边界：** 仅供 Codex 在用户发起执行时接班。不要把本计划的存在视为授权自动合并任何新稿；必须遵守主分支保护、PR 检查与作者最终验收。

## 0. Codex 接班先读、先核

按顺序读：

1. [AGENTS.md](../AGENTS.md) → [Project Routing Gate](../docs/project-routing-gate.md) → [WORKFLOW.md](../WORKFLOW.md) → [workflow lanes](../schemas/workflow-lanes.md) 与 [公开／私人边界](../docs/public-research-boundary.md)。
2. [Editorial Mission](EDITORIAL-MISSION.md)、[Book Architecture](BOOK-ARCHITECTURE.md)、[Editorial Gate](EDITORIAL-GATE.md)、[Editorial Rewrite Protocol](EDITORIAL-REWRITE-PROTOCOL.md)、[Temporal Validity](TEMPORAL-VALIDITY.md)。
3. [书稿首页](README.md)、[读者入口](START-HERE.md)、[人物目录](profiles/README.md)、[Chapter 目录](chapters/README.md)、[Life Routes](life-routes/README.md)。
4. 本任务指定的三份正文、其各自的 Case / Evidence / Claim 来源，以及作为风格对照的 [Limit Theory](profiles/josh-parnell-limit-theory.md)。

**写入前预检：** 精确 repo、主分支最新状态、事实 Owner、允许更改的路径、PR 可回退方案、是否夹带任何私人项目的资料。只消费该公开库已有可追溯材料；聊天中产生的改写示范不可充当一手史料。

### 原稿定位（2026-10-09 交接时的 blob SHA；开始时重新核当前 main）

| 对象 | 原文路径 | 交接时 blob SHA |
| --- | --- | --- |
| 单人传记 | `book/profiles/gunpoint.md` | `8d473f8de08c2a98d246c5f9e9f0103c41fcd5b5` |
| 群像 | `book/profiles/early-id-doom.md` | 开工前重新读取并保存 |
| 跨人物专题 | `book/chapters/06-you-do-not-need-a-standard-studio.md` | `436914e480d542b9d6db999abe36ba627da359ef` |
| 不主动改写的负对照 | `book/profiles/josh-parnell-limit-theory.md` | 开工前保存 |

若正文已被其他 PR 更新，先分析差异，不能在旧版上盲目整篇覆盖。原有版本由 Git 历史与 PR baseline 可恢复。

## 1. 问题诊断：不要把写作问题误诊为禁词问题

研究底层已相对成熟，阅读层的典型故障是：

- **命题优先于人物：** 当事人刚登场，作者就连续给出理论解释、方法标签、证据警告，故事难以展开。
- **结构剪辑不足：** 叙事时间线被频繁打断，关键行动被事后总结代替。以 Gunpoint 为例，GameMaker 进入制作的经历在辞职故事之后才讲，不利于连贯理解形成过程。
- **功能混排：** Profile / Chapter 中插入可单独成立的教学清单、假设性咨询场景、证据口径复述；这些并非无价值，但常应移至 Life Routes、脚注或 research backend。
- **单一写法泛滥：** 不同人生都被套进“神话→反转→机制→不可复制条件→今天如何做”的类似节奏，结尾频繁再次总结全书主题。
- **导读与正文体验脱节：** 读者已能按人生处境找到文章，但找到以后读到的仍像研究说明，而非人物与命运。

禁止以“AI 味下降了”、字数减少、禁止词命中率、AI 自评分数来替代编辑审稿。

## 2. 工作法：新增一次 Structural Cut，但不要新建第二套 Gate

每一篇开始时，在 PR 工作记录中（而非 reader 正文里）给现有段落标记用途：

- **N / Narrative：** 人物、真实事件、行动、即时反馈及后果；
- **A / Analysis：** 作者判断、必要的时代解释、产业比较；
- **D / Decision：** 面向读者的建议、操作清单、假设性项目诊断；
- **R / Research：** 来源等级、研究缺口、重复的证据免责声明。

**标记用来查找断点，不是硬性的内容比例或统一写作模板。** 先给出段落顺序的剪辑图：保留、移位、合并、删重复或链接下沉。必要的时效、来源争议与认识边界仍留在读者可找到的地方；不得因下沉而消失。

执行顺序为：

`Fact Lock + baseline SHA → Narrative Packet → Structural Cut → Delete → Restore Person → Rhythm / Authorial Voice → Fidelity Readback → A/B → Author Acceptance`。

**优先改变信息揭露顺序、叙事焦点、行动与后果关系；最后才润色句子。** 不允许为追求悬念虚构未经证明的对话、心理、场景细节，也不允许通过倒叙暗示当事人在当时已经知道未来。必要时在段内明确“多年后回忆”。

## 3. 依次执行的三个样章试验（不要并行大规模覆盖）

### Pilot 1 — Gunpoint：第一个重点交付

**原文：** [`profiles/gunpoint.md`](profiles/gunpoint.md)。
**主要来源：** [CASE-007](../cases/CASE-007-gunpoint.md)、[CASE-007 Evidence Ledger](../evidence/CASE-007-gunpoint-source-ledger.md)，尤其 E008（2010-10-25 开发日志：`Gunpoint And The Other Game`）。

**候选叙事弧：**
1. 从 2010 年重新审查 roadmap、发现预设剧情演出成本过高的真实决策开篇；
2. 倒回 PC Gamer 评论职业、长期游戏阅历、喜欢的玩家体验与差异判断；
3. 发现 GameMaker、做出可供外部反馈的原型；
4. 用 Crosslink 等可组合规则留下希望保留的体验，并交代路线图删改；回到开头而不伪造直接因果；
5. 公开开发、测试者、美术／音乐协作者与分工、媒体／网络可见性；
6. 2013 年首发周销售跨过本人辞职阈值，此后才退出 PC Gamer；
7. 可用极短尾声展示后续作品中的判断方法，但故事结尾应落回 Francis 个人，而非“普通人应该做的十件事”。

**编辑操作：** 先做 2–3 个相连小节的匿名 A/B 候选；在审读基础上再扩成完整候选稿。将“什么可以学／不能直接抄”的操作型材料优先链接到合适的既有 Life Route；不删除有价值的原创判断，也不把它重复宣讲三次。保留艺术、音乐、工资、行业网络、市场接入的参与，避免“一个有品味的人自己做出爆款”的神话。

**必须核对：** GameMaker 与 roadmap 的真实时序、2010 当事人同期表述与 2014 方法总结不可混同、辞职发生在何时及触发条件、协作者署名／权益、作者未公开的收入或家庭成本 UNKNOWN。E008 的来源等级如与总规则不一致，只提出 Lane B 核对问题，不在 Lane C 顺手修改 Ledger。

**产物：** 一篇 Gunpoint 结构改造候选稿 + 结构差异说明 + 原稿—新稿—证据三方忠实性回读。文风无需与其他 Profile 同构。

### Pilot 2 — early id / DOOM：先完成群像结构审稿

**原文：** [`profiles/early-id-doom.md`](profiles/early-id-doom.md)。
**范围：** 第一轮优先交付分幕大纲与 2–3 节连续叙事试改；不要在未核证整部时间线前自动把它扩成几万字。

建议检验的四条人物／故事线：

- **少年们：** Romero、Carmack、Hall、Adrian Carmack 等不同前史；家庭许可与伤害、计算机接触、制作技能形成、真实可用的 1980 年代美国环境；
- **Softdisk 与创业：** 团队相遇、工资与交付训练、Keen、职业义务、外部发行合作、独立决定；
- **造出窗口：** Wolfenstein、DOOM，Carmack 推动的工程技术突破与 Romero 等人的玩法／工具／商业协作；技术发明不是单独产生商业成功的充分原因；
- **成功后的分歧与人生：** Quake、Ion Storm 对照、职业取向分歧、技术—制作协同问题，以及经证据支持的长期家庭／代际后续。

参考已有 research notes（按必要性选择）：
[`masters-of-doom-longitudinal-master-study-001.md`](research-notes/masters-of-doom-longitudinal-master-study-001.md)、
[`family-gates-game-creator-us-china-029.md`](research-notes/family-gates-game-creator-us-china-029.md)、
[`doom-intergenerational-reconciliation-032.md`](research-notes/doom-intergenerational-reconciliation-032.md)、
[`carmack-romero-complementary-error-correction-network-042.md`](research-notes/carmack-romero-complementary-error-correction-network-042.md)。

避免把群像拆成研究主题的机械清单；不能为了“连贯”抹掉家庭伤害、真实劳动义务、资助者、第三方工作和历史细节。把“所以这本书该教普通年轻人什么”等教学式总结标为迁移候选；保留相关作者立场，但不强迫传记以课堂讲义结束。

### Pilot 3 — 第六篇：跨人物主题与决策工具分流

**原文：** [`chapters/06-you-do-not-need-a-standard-studio.md`](chapters/06-you-do-not-need-a-standard-studio.md)。
**互补目标：** [`life-routes/project-thesis-capability-gap-004.md`](life-routes/project-thesis-capability-gap-004.md)。

让案例**彼此冲突／比较**，而不是机械轮流举例：

- Roset / Nomada：为何核心视觉意图需要其他共同作者；
- Francis：为何优先改变产品制作义务，再补外围协作者；
- Wehle：已有能力如何借用外部服务而塑造短篇作品；
- Playdead：互补合伙的治理与长期退出矛盾；
- Question / The Magic Circle：能力匹配、产品完成，仍不保证市场可持续。可按叙事必要性引用 Croteam、The Witness、thatgamecompany、Brigador，但不要求一次讲完每种融资与招聘类型。

**特别处理：** 当前“最容易犯错的时刻，是你第一次看到自己的原型不够漂亮”这一假设性小团队诊断及“怎样判断缺口需要哪种合作”等偏 D 类内容，优先检查 LR-004 是否已有对应判断。已存在则删重并链接；缺少的通用决策判断可以作为**另一个独立的 Lane C 文本任务**加入 LR-004，不可不核对就重复拷贝。同一 PR 应保持范围紧凑，避免同时大改 Chapter 与 Route。Chapter 不替 Route 当招聘教程；Route 不复制所有传记。

**产物：** 可连续阅读、真正产生多人生交锋的专题候选稿，附“保留／搬离／链接”差异表。

## 4. 对照、验收与编辑边界

1. **负对照：** [Limit Theory](profiles/josh-parnell-limit-theory.md) 首轮只读审校，不主动全文重写。用它检验新流程有没有把已具连续叙事能力的旧稿改得更像模板。
2. **A/B：** 原版与候选版匿名比较。第一轮可由编辑做明示为“编辑内测”的定性对照；如未组织真实读者盲测，必须写 **NOT TESTED**，不得伪称已有读者反馈。
3. **可选外部读者检验：** 经作者安排后，找不同背景读者回答“记住了什么人、哪两个决定、哪段想跳过、还想知道什么”，避免只问“是不是更像人写的”。人类读者数量和结果必须真实记录，不设造假的既成门槛。
4. **Fidelity Readback 为不可补偿门槛：** 至少核人物归责、年代、回忆时点、被删除的限定、因果、金额/分母、UNKNOWN、引用版权与今天的适用条件。发现 REGRESSION 即回滚或交 Lane B。
5. **作者声音：** 保留有证据支撑、真正属于作者的批判与论点；不要为了“中性”全部磨平，也不要让每位传记人物都替同一套理论代言。允许人物没有可转移的成功学启示。
6. **高质量的短篇不必强制加长；史料丰富者不必被模板截短。** 先看真实行动／关系／冲突能否承载篇幅；不以已收集多少研究 Case 决定叙事长度。
7. **不得批量覆盖整个 `book/`；不得改 `cases/`、`evidence/`、`claims/` 或姊妹篇 canonical corpus**。必要的历史新问题交 Lane B；纯方法规范变更交 Lane A。

### 每份样章 PR 必须交付

- 明确 baseline commit/blob SHA、该次修改的路径与范围；
- Structural Cut 标记摘要与新的故事动线（无需写进正文）；
- 可直接连续阅读的**完整候选片段或候选章**；
- 重排、剪切、合并、迁移、删除内容的差异记录，特别说明重要作者判断是否保留；
- 独立的 Fidelity Readback：`PRESERVED / NEEDS_VERIFY / REGRESSION` 与证据回链；
- A/B 结果，或明示未做真实盲测；
- 私人信息／跨仓库写入预检、运行的 lint 与未能运行的检查；
- 明确的状态：`KEEP_ORIGINAL / REVISE_AGAIN / AUTHOR_REVIEW_PENDING`。只有作者批准后才能 `ACCEPT_REVISION` 并合并。

## 5. 与《人生性价比指南》借鉴的正确范围

可以学习**阅读产品层**的“直接问题入口、由当下处境寻人、证据与适用范围可查、同一材料支持不同阅读路径”。现有 [START-HERE](START-HERE.md)、[DECISION-ROUTER](DECISION-ROUTER.md)、[Life Routes](life-routes/README.md) 已具基础，无须另造 taxonomy。

**必须区分两个消费界面：**

- **故事模式：** 传记／跨人物专题，人物关系、冲突、行动、后果与命运优先；
- **决策模式：** 现实问题、能力与风险、边界、历史年份、具体动作、正反案例与证据。

它们链接相通，但不可将所有 Profile 生硬写成“背景—成本—收益—建议”的同一套六段模板。

优秀人物非虚构与开发纪实可用于学习编辑技法（如 `Masters of Doom`、`Blood, Sweat, and Pixels`、`The Making of Prince of Persia`），不得照抄受版权保护的文字，更不能把文学叙述中未经核验的情绪／对话编入本库。

**后续事项而非本轮任务：** 等上述三篇样章验证后，再讨论出版级书稿编排、网页书／EPUB／PDF、人物年表与合法配图。不要用网站装修掩盖正文结构问题，不要提前创建独立阅读应用。

## 6. Codex 建议的实际接班次序

1. **先选 Gunpoint**：读全原稿和 E008、锁事实、交 2–3 节小样 + Structural Cut 清单，再扩到完整候选稿，单独 Lane C PR。
2. **再做 DOOM**：先提交群像人物线／分幕蓝图；视源材料与作者意见继续样段，不与 Gunpoint 同 PR。
3. **然后做 Chapter 06**：检查 LR-004 去重范围，制作专题阅读稿，单独 PR。
4. **最后汇总小样效果**：是否值得更新现有 Gate 或 Book Architecture，由 Lane A 另 PR 处理，不能反向把实验模板固定成新的全书强制写法。
5. 斯拉夫线 [书稿入口](../sister-projects/slavic/book/README.md) 目前尚无正式 Profile/Chapter；本轮不把研究矩阵批量改成“人物传记”，以后挑史料真正成熟的人物另立案。

**本任务的成功定义：** 至少让 Gunpoint 候选稿在事实不倒退的前提下呈现一条可读的个人命运线，且提供可审核的 A/B 和编辑差异。整个项目的目标不是“降低 AI 味指标”，而是让读者能记住人物、追随他的关键决定，并愿意继续阅读，同时能在需要时方便查验事实和使用独立的决策工具。

---

**给 Codex 的一句话指令：** 请读取本文件与仓库治理规则，从最新 `main` 新建单独的 Lane C 分支，先完成 Gunpoint 的事实锁、结构剪辑、2–3 节叙事候选及可审计对照，再继续完整样章；不要提前改写全库，不要跳过史实回读或作者批准。
