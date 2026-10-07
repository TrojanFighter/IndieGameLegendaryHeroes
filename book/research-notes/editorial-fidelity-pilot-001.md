# Editorial Anti-Slop / Historical Fidelity Pilot 001

© 2026 洪荒行者。All Rights Reserved.

本笔记属于 Lane C，是候选改稿的审校记录，不是新增研究元数据或事实源。日期：2026-10-07。作者验收前不合并。

## Lock：原稿与范围

基线为已 fetch 的 `origin/main`：`6ae782c288fe7976a80a0f98864b0a34f97c7126`。原版由 Git 保留，不另建正式书稿副本。

| 正文 | 原版 blob SHA | 本轮范围 |
| --- | --- | --- |
| [Gunpoint](../profiles/gunpoint.md) | `359f41637867e920ebed8431f12a6ef9afc75391` | 连续三个小节：“他真正学会的不是复制喜欢的游戏，而是把喜欢的东西压缩”至“品味还会改变你能不能招到人” |
| [early id / DOOM](../profiles/early-id-doom.md) | `ff0e902bf5c7bc50ac5b70da22fe693dadb849b3` | 连续两个小节：“一开始，没有人给他们一张‘成为游戏大师’的路线图”及“Carmack 更极端：他想知道游戏里面到底是什么” |
| [Limit Theory](../profiles/josh-parnell-limit-theory.md) | `e0aa30a0f6fc0a54369b4c9ba4e54f2d70a274d9` | 全文审读，保留原稿作为对照 |

三篇开头、其他小节、结尾、研究边界与时效性段落不在试改范围内。局部改善不能宣称整篇已经通过 Editorial Gate。

恢复路径：`git show 6ae782c288fe7976a80a0f98864b0a34f97c7126:book/profiles/<文件名>.md`。PR diff 提供选定小节的完整旧稿与候选稿。

### 事实锁与权威

| 文本单元 | 必须锁住的事实及认识边界 | Canonical source |
| --- | --- | --- |
| Gunpoint：压缩 | Deus Ex 潜入体验是源头之一；可连接电气对象是具体设计。2014-01-25 方法文章是发售后总结，不证明开发时每一步已有明确框架 | [CASE-007：Taste as Capability Capital / Scope](../../cases/CASE-007-gunpoint.md#taste-as-capability-capital)，[E006](../../evidence/CASE-007-gunpoint-source-ledger.md#e006--non-stick-plan-compress-the-thing-you-love-into-a-small-rule-system) |
| Gunpoint：删减 | 2010-10-25 已写角色及预定发展；重看 roadmap，发现非交互演出编码成本与游戏价值不相称。不能变成“删除全部剧情”或量化节省工时 | CASE-007：品味还决定“不做什么”；[E008](../../evidence/CASE-007-gunpoint-source-ledger.md#e008--scope-taste-cutting-authored-spectacle-that-added-little-as-a-game) |
| Gunpoint：协作 | Francis 对不寻常机制、关注、美术、音乐之间关系的自述；John Roberts、Fabian van Dommelen 及音乐人参与。不是全部独力完成，也不证明点子独立导致招募成功 | CASE-007：Production / Market；[E004](../../evidence/CASE-007-gunpoint-source-ledger.md#e004--road-to-the-igf-journalism-as-taste--selection-capital)、[E001](../../evidence/CASE-007-gunpoint-source-ledger.md#e001--gunpoint-development-breakdown) |
| early id：Romero | 1983 年赴英国美军基地学校、Apple II 机房与 BASIC、早期投稿及售稿来自 2023 年回忆。拒稿—再投—发表的细节按 Kushner S1 记述，不冒充 E011 的直接访谈。不能称为首次接触机器，不能把外部反馈写成后来成功的充分原因 | [CASE-016](../../cases/CASE-016-early-id-software.md)，[E011](../../evidence/CASE-016-early-id-software-source-ledger.md#e011--romero-school-computer-access-basic-and-early-publishing-path)；[E026 的第一章定位](../../evidence/CASE-016-early-id-software-source-ledger.md#e026--masters-of-doom-chapters-14-differentiated-pre-id-household-and-founder-lives)，Case 已关联的 [生命史研究第3节 / Romero](early-id-1980s-america-life-decisions-001.md#3-一个国家内部六条起点迥异的人生路径) 保存拒稿摄取。Case 同时记录更早机器入口 |
| early id：Carmack | 少年修改 Ultima II sector、后来开放取向与少年经验的联系来自 2013 年回顾；不证明玩游戏自动学习、不证明开放的商业因果或单人改造行业 | CASE-016：Modding / Historical Boundary；[E012](../../evidence/CASE-016-early-id-software-source-ledger.md#e012--carmack-teenage-game-hacking-and-later-openness-rationale)，开放生态另见 E007/E008/E013 |
| Limit Theory | 2012 众筹目标 $50,000、5,449 人、$187,865 pledged gross；2017 晚期成员加入；2018 年 1 月官方演示 2000+ 艘与内容待做；2018-09-28 取消；两代代码和 2022 公开记录。不能将工程成果、众筹热度和交付混为一谈 | [CASE-054：CSA / Runway / Production / Verdict](../../cases/CASE-054-limit-theory-fit-trap.md)，[Ledger E001–E008](../../evidence/CASE-054-limit-theory-source-ledger.md) |

三份 Case 均为 RESEARCHING。[Claims Index 中的 C004、C007、C011](../../claims/README.md) 的登记状态为 SUPPORTED；本轮不改变命题状态，不把“品味决定命运”升级成确定性因果规律。

**UNKNOWN / H / Signal 锁：** Gunpoint 的贡献者工时、精确收入分配、媒体身份相对于品味的独立因果份额仍 UNKNOWN；early id 少年经验如何量化造成成功未知；Limit Theory 各次重写的必要性、技术工时占比、团队报酬、取消后家庭与财务恢复仍 UNKNOWN。能力偏好吸引投入的机制解释不等于已证单因。不得把 Signal 用作新增事实，本轮无 Signal 摄取。未锁定的心理、私人对话、现场气氛一律不补。

**Transfer horizon：** Gunpoint 的观察期约 2009–2013，2014 方法总结；GameMaker、媒体与 Steam 窗口依赖历史条件，2026 为 CONDITIONAL，判断—原型—反馈机制保留 DURABLE 分析边界。early id 的 1980s–1990s 机器、杂志与 shareware 路径为历史渠道，不为今天学校/投稿路径承诺效果。Limit Theory 的 2012–2018 众筹/工具条件不能直接外推；工程成熟度与交付成熟度分开审视是可继续核验的机制。原文时效性部分保留。

## Narrative Packets（改写前）

| 项 | Gunpoint | early id / DOOM | Limit Theory |
| --- | --- | --- | --- |
| 叙述对象 | Francis 的设计与协作生产史 | Romero、Carmack 及团队的群像前史 | Parnell 主导、晚期扩团队的失败调查 |
| 人物与时代 | 有媒体工作、以 GameMaker 业余开发，约 2009–2013；公开日志和当时 Steam/媒体窗口，非今日渠道套餐 | 1980s 可编程家用机、学校机房与杂志投稿；后续 Softdisk、PC/shareware，尚非 Steam 众筹时代 | 2012–2018 自研程序化宇宙、众筹与技术日志；当时通用引擎已存在，不能称自研别无选择 |
| 处境与约束 | 无传统开发履历，有评论经验和工资；不能承担 Deus Ex 的完整规模，需要协作者 | 两人机器入口、兴趣和能力结构不同；获得设备和发表入口不等于拥有成熟职业路线，家属与雇主成本不能被抹去 | 有图形/引擎强项和众筹承诺，完整产品义务巨大；资金、时间和精力有上限 |
| 决策节点 | 把潜入快感变成电气规则；重看 roadmap 并砍演出；公开作品并招募美术音乐 | Romero 学 BASIC、投稿并售稿；Carmack 修改游戏磁盘数据，后来将这种经历与开放取向相联系 | 众筹后全职、持续系统开发、换技术代际、晚期扩团队、PAX 演示、取消、公开代码 |
| 主导疑问 | 他的判断怎样具体改变有限时间的用途与可获得的协作？ | 两种玩家经验如何变成不同的生产能力，又有哪些入口支撑这种转换？ | 为什么越来越强的技术成果没有兑现完整游戏承诺？ |
| 叙述位置 | 三个开发决定，最后保留局部分析；以成本选择承载作者的品味判断 | 双人物前史对照；用各自实际行动区别人，而非统一套神话反转 | 保留调查式首尾：2018 演示与取消形成可观察落差，回溯六年，再谈残值与损失 |
| 文风边界 | 不模拟看 roadmap 时的心理、不捏造对话；回顾明确标时点 | 不补课堂、街机厅或家庭场景；不把成年回忆倒写成少年预知行业走向 | 不诊断人格/健康，不把技术路线反事实写成可知结局；保留晚期同伴与财务未知 |

## Delete → Restore Person → Rhythm

| Pass | Gunpoint | early id / DOOM |
| --- | --- | --- |
| Delete | 删“项目死了一半”“一百个人/一个人做灵魂”等未有实数口径的类比，删三节反复拔高品味的落款；留下成本选择和协作两个不同作用 | 删大师路线图的反复反驳、假设玩家内心问句及玩→好奇流程图，删“改变一整个行业”的预告；留下目标形成与实际修改动作 |
| Restore Person | 用 Crosslink 电气规则、2010 roadmap、公开样稿征集、具体美术音乐人和邮件/分成过程承担叙述 | 用 Romero 的机房/BASIC、投稿售稿，与 Carmack 的 Ultima II sector 修改形成两条路径；标记各自成年回忆，不补少年心理 |
| Rhythm | 三节分别从作品体验、一次计划检查、协作者进入开头，段落承载动作后再局部分析；保留一个删减重音 | 两个人各有连续段落，最后交汇到团队前史；不再逐句断行。教育批评仍保留为作者评论，未推广为已证教育命题 |

调整节奏时没有删除全部否定句或所有理论。必要否定保留，用来区分完整规模与核心体验、游玩与制作、点子作用与媒体职业条件。

## A/B 编辑比较（提交前）

以下是有版本身份的编辑比较，**不是匿名盲测，也不是人类阅读数据**。独立 Agent 审校另列；作者验收与普通读者继续阅读意愿尚未测试。对照呈现不使用禁词数量或短句比例评分。

### 代表性旧稿 → 候选稿

| 小节 | 旧稿 A（摘录） | 候选 B（摘录或结构） | 改变与代价 |
| --- | --- | --- | --- |
| Gunpoint / 压缩 | “只要这个问题答得足够准，原本需要一百个人生产的东西，有时可以换一种方式，让一个人先做出它的灵魂。” | “Francis 判断自己究竟想留下哪种体验，再为它寻找负担得起的形式。”；先说明电气对象与重连 | 把夸张规模比喻改为可审计的成本选择，保留品味判断；失去旧稿的强重音 |
| Gunpoint / 删减 | “问题出现了。”、“这可能直接决定项目有没有一天能完成。” | 2010-10-25 日志 → 编码成本/游戏价值 → “喜欢的东西，不等于这款游戏必须拥有的东西。” | 决定仍有生死分量，但读者先看到具体检查和取舍 |
| Gunpoint / 协作 | “于是品味又从‘设计能力’变成了：生产资源获取能力。” | 采访中的链 → 美术/音乐姓名、样稿、邮件、收入分配 → 作者的局部解释 | 增加人和合作方式；保留资源获取观点，也保留媒体职业的替代解释 |
| early id / Romero | “真正重要的是：他第一次拥有了把游戏从消费对象变成可修改对象的入口。” | 学校入口及 2023 回忆 → Kushner 投稿过程 → 目标教育评论 | 去掉与 Case 更早入口冲突的“第一次”；目标不是先知路线图的观点仍在 |
| early id / Carmack | “为什么是这样？数据在哪里？如果我改掉它，会发生什么？”及玩→拆→做流程 | 2013 回忆中的实际 sector 修改 → 游玩不自动学习 → 后来的开放动机回顾 | 实际动作取代拟内心问句；失去图示的速读便利，获得两人的不同经历 |

### 六项判断

| 维度 | Gunpoint A → B | early id A → B | Limit Theory 对照 |
| --- | --- | --- | --- |
| 人物具体性 | 原稿已有 roadmap 与姓名；候选将这些组织成动作，并补入既有 E001 的协作细节。改善来自过程，不是新增场景 | 从“某类天才玩家”转为两种不同操作与发表路径；教育与机器入口仍可见 | 原稿已有演示、路线、资金、团队与告别，不需要再补人 |
| 叙事连贯度 | 体验选择→删减→协作有清楚主题联系；不是声称严格发生顺序，2014总结先于2010日志的叙述顺序明确标年 | 机房/发表与改盘两条前史再接下节1980s环境；不强行编成同一成长模板 | 2018落差→回溯2012→多年工程→取消→源码残值形成调查线 |
| 作者观点保存 | “品味影响成本结构与资源获取”仍明说；删去了夸张泛化，不能把克制误判为撤回命题 | 目标通过行动反馈形成、游玩不自动学习、能力前史均保留；教育批评比旧稿克制，需作者判断力度 | 技术进步不自动兑现产品的主问题贯穿；原稿观点已有事件承担 |
| 语言节奏 | 三种小节入口、连续叙述和一处重音；末段因果限制仍偏说明性 | 双人物路径替代连续短句；回忆限定有解释成本，但避免事后预知 | 短句和否定句有边界用途，不应机械清理 |
| 继续阅读意愿 | 编辑预期：读者更容易跟随制作问题；非实测，旧稿有更强演讲感染力 | 编辑预期：两个人的差异与下节接入条件形成追问；非实测 | 原稿开头落差足以推动回溯，保留 |
| 历史忠实性 | 回顾时点、同期删减、协作者与因果局限更显式；无未纠正倒退 | 更早入口未被覆盖；拒稿按S1归源，开放动机按P1保留；无未纠正倒退 | 只审读，不宣称全文重新完成来源核验；原文不变 |

**主编辑候选裁决：** Gunpoint / early id 为 `ACCEPT_REVISION`（提交给作者的候选，非合并批准）；Limit Theory 为 `KEEP_ORIGINAL`。如果作者认为解释边界挤压了人物叙述、教育批评力度不足，允许 `REVISE_AGAIN`。事实忠实性不能由可读性补偿。

## Fidelity Readback：旧稿 → 候选 → Canonical

| 项 | 回读结果 | 具体核验 |
| --- | --- | --- |
| Actor / credit | PRESERVED | Gunpoint E001/E004：Francis 核心设计编程、美术音乐人均在，不声称全工种独力完成；early id E011/E012：投稿属于 Romero，改盘属于 John Carmack，两位 John 未混同 |
| Chronology / knowledge | PRESERVED | Gunpoint E006 的 2014 发售后总结与 E008 的 2010 同期日志分别标年；early id E011 的1983经历与2023回忆、E012 的2013回忆分开，删除“首次”误断。小节顺序是主题顺序，不是编造发生先后 |
| Numbers / denominators | PRESERVED | 删除“一百个人/一个人”的非实数比喻，没有新增人数、预算、工资、工时或销售额；收入分配只说约定，不报精确比例。Limit Theory pledged gross、2000+官方demo与完成功能的区别未改（E001/E006/E007） |
| Negation / modality | PRESERVED | 保留未复制完整规模、游玩不自动学习；“也可能影响谁愿意参与”不升级为必然；未说砍掉全部剧情，也未说知道后来结果 |
| Causation / alternatives | PRESERVED | E004 边界：不隔离品味与媒体身份的因果；early id 从路径观察到作者评论，不成为所有玩家或教育制度的因果证明；相邻家庭与时代条件原样保留 |
| Evidence boundary | PRESERVED | E006 的回顾性方法、E011/E012 的P1、E026拒稿记述的S1明确。Gunpoint工时/分配/因果份额仍未知；Limit Theory重构必要性、财务、团队报酬与H机制不补成事实。无Signal升级 |
| Historical regime | PRESERVED | 学校Apple II/BASIC/杂志和业余GameMaker保持历史环境；未增今日策略或平台承诺，原文 transfer boundary 原样保留 |
| Quote / rights | PRESERVED | 删除模拟内心/新手对话；方法与开放动机用转述，无新增未核原话或第三方长段版权文字；作者原创观点及版权说明保留 |

**NEEDS_VERIFY / VERIFY_IN_LANE_B（不妨碍局部候选，但不得外推）：** Gunpoint 的每项决定是否从一开始遵循2014框架，以及品味相对媒体职业的独立效应未知；early id 具体能力形成的因果份额未知。Limit Theory 的2022源码发布日期在Ledger E005 Published仍 UNKNOWN，Case及现有源码摄取含2022记录，书稿有该日期，但本轮未独立补证，不宣称已完成原始发布日核验。新增可读性不能提升这些研究状态。

### 独立编辑审查

独立 Agent（`independent_editor_review`）只读审查了完整差异、既有 Case / Ledger 与三篇正文，知道版本身份，未编辑或提交。结论：两篇 `ACCEPT_REVISION` 候选、Limit Theory `KEEP_ORIGINAL`；八项 fidelity 未发现新增 REGRESSION。其六项比较认为人物具体性、连贯度和节奏改善，观点保留；阅读意愿仅为编辑预期。

审查曾提出拒稿细节不能仅归给E011；回读E026及Case已关联的第3节后撤回缺证疑点。候选明确用“Kushner 的传记记述”，本笔记分别列出P1学校回忆与S1拒稿依据。第二编辑同样提醒语势变化、目标教育评论、正文回忆限定的密度与未改开头/结尾要由作者决定。以上是审校意见，不把另一模型当历史事实源，也不冒称人工验收。

## 作者待决与扩展评价

1. Gunpoint 旧稿的演讲式重音是作者特色还是重复负担？候选保留观点但收掉“一百个人/灵魂”等比喻，需作者选择。
2. early id 的目标教育批评从群体断言转为由 Romero 道路引出的评论，是否保住作者想要的锋芒？不能为锋芒重新加“首次机器入口”。
3. 2014回顾、2023回忆等限定在正文里保留多少，既让读者辨认证词时点，又不让后台审计压过人？可改表达，不可消除区别。
4. 本轮没有处理整篇开头/结尾重复。局部首尾与未改段落的语气衔接，需作者连读整篇，不能只从差异判定。
5. 第二编辑意见之外，仍需作者验收；匿名普通读者A/B未做，继续阅读意愿只有编辑假设。

**是否扩展：有条件值得。** 这轮显示具体动作、删减和协作可以承担原来由模板结论承担的观点；Limit Theory也显示相同方法必须允许 KEEP_ORIGINAL。建议作者接受样本后，再逐篇选连续片段，优先事实锁足够成熟且重复分析遮住人物的文章。不建立禁词阈值，不自动批量清洗，不扩大到全库。今次不授权任何后续全文编辑。

## 范围与验证

- 仅两个 profiles 的选定正文与本审校笔记改变；Limit Theory blob不变。
- Case / Evidence / Claim / Schema / 研究元数据 / 研究结论完全未改。没有翻译条目关联这两篇，不修改译文或manifest。
- `reader_layer_lint.py` 通过；`translation_lint.py` 无错误，三条既有 STALE 警告与本轮无关；`git diff --check` 通过。它们只验证结构，不能判定编辑质量。
- 暂存隔离检查：694项，0阻断，2条已有 GRIS 公开来源语境提醒已核对；没有命中本轮文件。额外 `--worktree` 扫描包含未跟踪/忽略的本地插件与缓存，因其中命中而失败，不能称全工作目录清洁；这些内容不在Git索引或本PR，未移动、删除或绕过规则。提交/推送仍按完整Git快照与新增历史运行强制检查。
- PR标题、正文与审校材料已作公开载体语义审阅；无私人项目来源或应用映射，无匿名预算、人员、谈判或设计信息。不公开私有词表或命中原文。
