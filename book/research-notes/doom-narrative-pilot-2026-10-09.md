# Early id / DOOM 群像叙事试验：事实锁与编辑记录

状态：AUTHOR_REVIEW_PENDING。Lane C；真实读者盲测 NOT TESTED。

## 写入预检与基线

- 目标 remote：`TrojanFighter/IndieGameLegendaryHeroes`，公开行业生产史及书稿。
- 分支：`codex/doom-editorial-pilot-20261009`；基线 main：`44cc729e1e4ab6e127cd31a6b730bb52823119c2`。
- 原稿：[`early-id-doom.md`](../profiles/early-id-doom.md)，blob `896862916e3acda7345e0d017c5bf29cfed914b2`。
- 本轮只新增本笔记与 [A/B 样段](doom-narrative-pilot-2026-10-09-ab.md)。正式 Profile、Case、Evidence、Claim、Schema、研究元数据均不改。原稿可从以上 commit/blob 恢复。
- 历史 Owner：[`CASE-016`](../../cases/CASE-016-early-id-software.md) 及其 [Evidence Ledger](../../evidence/CASE-016-early-id-software-source-ledger.md)。Case 仍为 RESEARCHING；本次不提升任何证据状态。
- 按 PR #281 的交接次序：Gunpoint 候选已交 PR #283，现做 DOOM 分幕与小样；Chapter 06 留待独立任务。本轮不批量重写。
- 只使用公开材料，不含其他项目的内部资料、执行建议或匿名私人信息。通过独立 PR 审阅，作者批准前不合并。

## 正文生成前的事实锁

| 锁定项 | 依据 | 不可偷换的边界 |
| --- | --- | --- |
| Keen 在任职期间的夜间、周末制作；约两个半月 | E002，Hall 2015 回忆；Case Capability Prehistory | 回顾性一手证词；不是同期工时表或各人投入总和 |
| 使用 Softdisk 电脑；Keen 收入影响全职独立决定 | E003，Miller 2015 回忆；Case Runway | 设备许可、工资替代额及家庭预算 UNKNOWN；不得判定合法或违法 |
| 离职后继续交付游戏，Hall 暂留培训替代者、同时为 id 工作 | E002/E003 | 无原合同；不在小样写精确承诺数量或法律裁决 |
| 分集 shareware、Apogee 的商业接口 | Case Market；E003/E010 | 不是无营销或只有程序员的功劳；不作今天可照抄的渠道建议 |
| Wolfenstein 超过 Keen 的 shareware 销售纪录 | E007，1994-01 同期行业报道；Case From Keen to Wolfenstein | 未审计的报道口径；不添加销售数字，不把毛利写成净利润 |
| 前作资金余量与开发 DOOM 的空间 | E010；Case From Keen to Wolfenstein | 历史综合；不能逐项证明哪笔收入支付哪项工具；选择权是作者分析 |
| 报道时七人公司、NeXTStep、Romero DoomEd 约五个人月 | E007；Case Toolchain | 公司人数不是全部参与者；工作量不是延迟五个月；无效率倍率 |
| DoomEd 让设计师直接设计；ANSI C 主体与少量汇编 | E007；Case Toolchain | 不造人物心理，不宣称某语言必然优越；保留艺术、声音、网络与分发外围贡献 |
| 时效与因果 | Case Temporal boundary；原稿分析 | 1990 年代 shareware、DOS/NeXT 为 HISTORICAL；分阶段风险、选择权、工具与协作是有边界的作者判断，非成功保证 |

小样不消费新的 H/Signal，也不以新报道填 UNKNOWN。原稿其他部分的家庭成本、暴力、创始人分歧和后来的家庭回忆均保留。选段外的事实尚未完成逐句回读；分幕蓝图不等于全篇可发布稿。

## Narrative Packet

对象为团队群像，不是“两位 John 独力创造 DOOM”。这一段处于工资雇佣、磁盘/网络 shareware 与早期 PC 技术快速变化的生产环境；人们已有职业制作经历，却仍要解决时间、旧交付义务和收款渠道。

主导疑问：他们怎样从下班后的原创项目走到能投入下一作工具的公司？已知节点是夜间制作、市场收入、退出雇佣、继续履约、前作成绩和 DoomEd。叙述沿工作安排的变化推进，让 Hall 的双重责任、Miller 的发行接口、Romero 的工具和 Carmack 的程序选择各有位置。

作者观点保留三项：分阶段承担风险；成功带来后续选择权；工具也是组织能力。分析紧随对应事件，不再每节同时讲一次辞职教程、工具建议和研究方法。无证据的房间气氛、争吵、表情、内心计划、对话、家属态度与精确支付关系均不得补写。

## 全篇四幕剪辑蓝图

这是待作者审议的顺序建议，尚未实施全篇重排。

| 幕 | 保留的人物与行动 | 剪辑与边界 |
| --- | --- | --- |
| 少年们怎样获得制作入口 | Romero、Carmack、Hall、Adrian 的不同前史；计算机接触、家庭许可与伤害、已有技能 | 合并重复的机会结构解释；保留家庭成本与暴力，不能把帮助解释成伤害合理化；各人经历分别归责 |
| Softdisk：相遇、出货与离职 | 工资及设备、Gamer's Edge 交付训练、夜间 Keen、Apogee、市场反馈、旧义务 | 将完整的 Keen 过程放在 Wolfenstein/DOOM 之前；地区环境解释紧随具体就业处境；精确合同 UNKNOWN |
| 造出窗口，并把它做成游戏 | Carmack 技术推进，Romero 工具/关卡，Hall 与美术同事的工作；Wolfenstein 收入、DOOM 分发及玩家制作 | “造窗口”分散到具体技术变化处，不先预讲终点再退回 Keen；Hall 离开置于 DOOM 制作内部，不拖成成名后冲突；七人公司与外部贡献并列 |
| 成功没有结束关系 | Quake 的制作压力和分歧、后续职业路径、家庭认可与代际后续 | 区分当时报道和多年后解释；Ion Storm 如扩写须另核已有档案；保留认可未必修复伤害与反例，不以成功学收尾 |

## 三节 Structural Cut 与三遍编辑

| 原节与段落用途 | 操作 | 判断的去向 |
| --- | --- | --- |
| 夜间 Keen：N/R → N/A/R → N/A → D/A/R | 合并制作与发行背景；Hall 的离职后工作接在市场反馈之后；删重商业接口说明 | 分阶段风险保留在本节末；设备许可、无个人预算、历史渠道边界仍在正文 |
| Wolfenstein：N/R → A/D/R → A/过渡 | 不再次复述 Keen 离职；删未核成具体行为的假设清单 | 选择权保留为作者判断；未核交易/机器购买清单原文可查，非事实遗漏 |
| DoomEd：N/R → N/A/R → N/R → A/D | 聚焦 Romero 工具如何让设计师工作；Carmack 语言选择后接；不虚构两人的对话 | “工具也是组织能力”原判断保留；数值口径、贡献者边界、不可复制条件留在正文 |

Delete：删除重复介绍和假设性举例，而非替换禁词。Restore Person：用 Hall 的双重工作、Miller 的商业接口、Romero 的投入推进。Rhythm：保留三节连续性，长段承载过程，短段只承载局部判断。样段没有新增现场描写或戏剧化对白。

## 网上报道审读记录

访问日期均为 2026-10-09。以下是编辑阅读记录，不是新 Evidence 登记；读过全文也不代表全文所有陈述已获核验。

| 来源、作者、发布日期 | 阅读范围及用途 | 入稿权限 |
| --- | --- | --- |
| [The Science of Happiness: An Interview with Tom Hall – Part 2 of 2](https://episodiccontentmag.com/2015/04/17/tomhall2/)，David L. Craddock，2015-04-17 | 访谈正文完整读；注意离职后仍承担工作 | 仅消费 E002 已承担内容；支票、更多制作分工等新增细节待 Lane B |
| [Bigger in Texas: An Interview with Scott Miller, Part 2](https://episodiccontentmag.com/2015/08/17/bigger-in-texas-an-interview-with-scott-miller-part-2/)，David L. Craddock，2015-08-17 | 访谈正文完整读；对照独立决定与商业接口 | 仅消费 E003；法律解释须归属于 Miller，不作裁决 |
| [Monsters From the Id: The Making of Doom](https://www.gamedeveloper.com/game-platforms/the-game-developer-archives-monsters-from-the-id-the-making-of-i-doom-i-/)，Alexander Antoniades，原刊 1994-01、重刊 2009-01-15 | 报道正文完整读；制作与商业快照 | E007 已登记的工具、人数及程序语言可用；不照搬报道中的历史压缩、技术描述或未来预测 |
| [Romero and Hall on creating Doom](https://www.gamespot.com/articles/romero-and-hall-on-creating-doom/1100-6302251/)，Guy Cocker，2011-03-04 | 报道正文完整读；为群像与设计分歧找线索 | 多年后演讲的媒体报道，不能当 1993 同期证据；新增细节 VERIFY_IN_LANE_B |
| [The story of Doom and how it changed everything—as told by co-creator John Romero](https://www.pcgamer.com/the-story-of-doom-and-how-it-changed-everythingas-told-by-co-creator-john-romero/)，Andy Kelly，2020-08-11 | 正文完整读；关卡试作、工具与玩法迭代的叙述参考 | 回忆与记者解释分开；新增迭代细节 VERIFY_IN_LANE_B，不移植天才修辞 |
| [Q&A: Doom's Creator Looks Back on 20 Years of Demonic Mayhem](https://www.wired.com/2013/12/john-carmack-doom/)，Chris Kohler，2013-12-10 | 问答正文完整读；技术选择与回顾的边界 | E012/E015 的已登记内容可供后续全篇使用；本小样不增加新细节 |
| [Quake turns 25: John Romero looks back on the legendary FPS that almost tore id Software apart](https://www.gamesradar.com/the-making-of-quake/)，Rory Milne，2021-08-19（由该媒体[作者索引](https://www.gamesradar.com/author/rory-milne/)核日期；纸刊原始日期未确认） | 正文完整读；范围变化与制作摩擦的叙述参考 | 新人数、会议、收益及权利说法 VERIFY_IN_LANE_B |

此次阅读影响的是选段焦点与结构：让具体责任和工作接口承担故事，而非把多篇报道拼成无缝的共同回忆。新细节仍留给证据 Owner 核验后再扩写。

## 冲突与仍需人工判断

1. E007 对离职的压缩叙述与 E002/E003 的任职期间制作、收入后退出、继续履约过程不完全一致。样段明确归属于 Hall/Miller 的回忆，未用同期报道替其背书；时间线差异待 Lane B 核清。
2. Hall 与 Miller 对继续交付义务给出的时长/数量不同；无原合同。本轮仅写共同可承担的“继续交付”，不拼出统一数字，不判法律权责。
3. WIRED 2013 引言与 GameSpot 2011 对发布服务器地点的说法不一致。本轮不需要地点，也不选边；如将来写发布现场须补证。
4. PC Gamer 的关卡试作细节、GamesRadar 的 Quake 会议与重做经历值得后续核证；媒体的全称、天才评价和责任归因不能整段继承。
5. 作者需判断三处观点压缩是否保留了自己的力度，以及风险段应留下多少今天的提示。不可用模型“更好读”的结论代替作者选择。

## Fidelity Readback

| 项目 | 状态 | A → B → 证据的回读 |
| --- | --- | --- |
| 人物归责 | PRESERVED | Hall 培训替代者、Miller/Apogee 发行接口、Romero DoomEd、Carmack ANSI C 均保留；E002/E003/E007；七人公司不包办全部贡献 |
| 时间与当时认知 | PRESERVED | 任职制作 → 收入影响退出 → 仍履约；Hall/Miller 明示 2015 回忆；1994 报道只承担当时公司与制作快照 |
| 数字与分母 | PRESERVED | 约两个半月、约五个人月、报道时七人公司；无销量/净利/预算新增；E002/E007 |
| 否定与情态 | PRESERVED | 资金余量不证明必然成功；工具无量化效率；许可与个人门槛未核；E003/E007/E010 |
| 因果及替代解释 | PRESERVED | 未断言前作特定款项支付 DoomEd；三项作者解释仍有范围，不升级为已证规律 |
| 回忆/同期区别 | PRESERVED | E002/E003 回忆与 E007 同期报道分别标识；E010 后来综合承担资金余量联系 |
| UNKNOWN/H/Signal | PRESERVED | 原合同、工资替代额、家庭预算、工具效率未知保留；样段外未知未作修改；新来源不升级为 Evidence |
| 历史环境 | PRESERVED | 当年渠道与工具明示，未建议今天照抄；历史方法不构成设备使用许可或成功保证 |
| 引语与版权 | PRESERVED | 无新直接引语；中文候选为本项目独立表述；A 为本库原文快照，不转载报道全文 |
| 外部新线索 | NEEDS_VERIFY | 以上报道新增细节与冲突交 Lane B，未用于 B 的确定性事实 |

## 编辑内测 A/B

这是明示版本的编辑定性比较，未盲测；真实读者继续阅读意愿 NOT TESTED。

独立 AI 编辑于 2026-10-09 核对 A 与基线三节及分隔符一致（仅统一换行、去除选段首尾空白），未发现阻断交付的 REGRESSION。其建议将 B 的“退出雇佣关系以后”改为“团队转向id以后”，避免暗示 Hall 本人已经离职又继续留任；已采纳。审读认为三项作者判断保留、人物职责更突出、样段连贯；未知合同、净利润及效率仍待研究。该意见不是人类盲测、全篇核准或作者验收。

| 维度 | 本轮判断与限制 |
| --- | --- |
| 人物具体性 | B 将 Hall 的持续工作与 Romero 工具安排放到过程中心；仍缺其他成员在此段的具体动作，不补造 |
| 连贯度 | B 不重讲 Keen 退出，连续推进工作义务、收入与工具；全篇前面的跳时序尚未实施修复 |
| 作者观点保存 | 分阶段风险、选择权、工具作为组织能力均保留；删的是假设清单与重复解释，作者需复核力度 |
| 语言节奏 | B 减少每段“解释—警告—总结”的循环，保留必要限制；不是越短越好，亦不计算 AI 词频 |
| 继续阅读意愿 | 编辑预期工具段能自然接后续分发段；没有人类读者数据，不声明已改善 |
| 历史忠实性 | 对已锁事实回读未发现 REGRESSION；新材料留待补证，不能因篇幅变顺放行 |

暂定 AUTHOR_REVIEW_PENDING，允许 KEEP_ORIGINAL 或 REVISE_AGAIN。值得继续同一篇的有限扩写与人工阅读比较；尚不足以全库推广或把四幕变成固定模板。Limit Theory 继续保留作负对照。

## 交付检查

`python tools/reader_layer_lint.py` 通过；A 与基线一致由独立编辑核对。只新增两份 Lane C 编辑材料，未覆盖 Profile 或研究主档；新增文字、提交消息与 PR 描述已做公开内容语义审阅。提交及推送仍由本库安装的私人内容 hooks 检查，远端 required checks 结果见 PR。作者验收未完成。

## Limit Theory 对照审读与三份候选验收缺口

本节是首轮试验的对照校准，沿用既有PR，不扩写DOOM或替换任何Profile。2026-10-09完整阅读[Limit Theory原稿](../profiles/josh-parnell-limit-theory.md)，对照[CASE-054](../../cases/CASE-054-limit-theory-fit-trap.md)与[Ledger](../../evidence/CASE-054-limit-theory-source-ledger.md)。基线commit仍为`44cc729e1e4ab6e127cd31a6b730bb52823119c2`，原稿blob为`e0aa30a0f6fc0a54369b4c9ba4e54f2d70a274d9`。

**编辑裁决：KEEP_ORIGINAL适用于现有叙事结构；不是对所有史实签收。** 对照没有生成B稿，不伪造A/B实验。下列问题须保留供核证；KEEP_ORIGINAL不抵消NEEDS_VERIFY。

### Narrative Packet与结构审读

对象是Josh Parnell及一个未完成产品的调查叙事。2012年的众筹窗口使程序化宇宙愿景成为公开承诺；他已有图形与引擎能力，缺的是完成广泛产品义务的生产结构。资源来自众筹与个人投入，精确净额、年度支出、家计和成员报酬未知。关键节点为众筹后全职投入、持续开发、技术代际迁移、晚期加入成员、2018演示与取消、后续源码残值。

主导疑问是“为什么真实的工程进展仍没有交付完整游戏”。开头从2018演示与取消建立疑问，再回到前史及2012承诺，沿制作过程追到资源耗尽；这是调查性披露顺序，不假装2012人物已知失败。作者关于能力也可能成为昂贵岔路的观点有保留价值，不应为语言柔和而删去。没有证据的房间布置、情绪场景、健康诊断、家庭冲突和取消后的励志归来均不添加。

| 原稿功能 | 对照裁决 |
| --- | --- |
| N/A：PAX演示与八个月后取消 | 保留。具体成果与产品缺口直接形成阅读问题；不需另加“天才神话”的统一导语 |
| N/A/R：前史、众筹、连续更新、两代实现、加入成员 | 保留因果限制与阶段顺序；技术迁移不写成已证明的错误，晚期团队不能消失 |
| N/A/R：损失与源码残值 | 保留。残值与未履约损失各自成立，不能合成“交了学费”的安慰结论 |
| A/D/R：技术进步应怎样衡量，事实附录 | 尾声略密，可供作者以后局部压缩；目前有必要反驳与时效限制，不因含教学功能自动删除 |

Delete审读：部分短段可合并，但“不是不要写引擎／也不是不要做复杂系统”分别排除两种不同误读，有独立作用。Restore Person审读：前史、选择、成果、加入成员与告别构成了人物经历，无需靠新场景补活。Rhythm审读：开头与结尾重回同一产品缺口有结构作用；无需为了每节长短均匀而改写。上述判断是编辑观察，没有读者测试数据。

### Fidelity Readback

| 核验项 | 依据与裁决 |
| --- | --- |
| 人物归责 | E006及Case Production有晚期成员，原稿保留，PRESERVED；不把六年写成纯solo，不由成员加入推定合同/工资 |
| 时间与当时知识 | E001/E004/E005/E006/E007/E008分别承担众筹、系统、实现代际、晚期演示、取消和回顾性前史；叙述倒回不改事件次序，PRESERVED |
| 数字与分母 | E001的50,000美元目标、187,865美元gross pledged、5,449支持者，与E006官方演示超过2,000艘的口径均保留；PRESERVED，不把演示当独立性能基准或成品验收 |
| 支付措辞 | 原稿“从它被支付的那一刻”紧接承诺总额，可能让读者误认pledged等于到账。NEEDS_VERIFY：未来局部改稿宜明确“公开承诺与资金投入”，不能据此补净额或实际扣款日 |
| 因果、否定与情态 | 不认定每次重写都错、不认定商业引擎必救项目；局部能力与产品失败并存，PRESERVED。失败形成机制为作者解释，不能升级为单因证明 |
| 回忆、健康、UNKNOWN/H/Signal | E008职业记录为回顾；E007为取消时自述，不作健康诊断。家计/报酬/反事实职业收益未知，PRESERVED。“这条历史不存在”表达未发生的反事实，不视为已知另一份收益表 |
| 源码年份 | Case Period列2022，但Ledger E005的Published为UNKNOWN，仅承担两代技术实现；本轮读两库README确认架构，未取得2022公开发布公告。NEEDS_VERIFY：仓库存在或旧代码commit日期不能证明公开日期。原稿精确年份须Lane B补定位，不能宣称本轮已核实 |
| 时代与版权 | 保留2012–2018条件与2026限制，不新增引语/场景；PRESERVED。“想象PAX现场”后只复述已登记演示，不因此自动认定为虚构场景 |

本轮直接读取[官网新闻](https://ltheory.com/news.html)的2017性能/成员、2018演示/取消及2013原型段，核对关键时间线；读取两代源码仓库README，未编译运行，未观看嵌入视频。其他证据消费既有Case/Ledger，未宣称全部外链重核。官网2013原型仅给特定支持档位，原稿“支持者可以拿到”不可扩大为所有支持者均收到完整游戏。

### 六维校准与验收现状

人物具体性来自能力、持续制作和资源损失；连贯度来自“局部进展／整体未完成”的调查线；作者观点保留成果与损失的双重事实；短句重音有时有效、尾声密度仍可讨论；继续阅读意愿NOT TESTED；历史忠实性有上述两项NEEDS_VERIFY。它说明方法应允许保留有作用的否定句和既有结构，不能仅凭词频启动清洗，也不宜把Gunpoint、DOOM都写成同样的失败调查。

2026-10-09查询[Gunpoint #283](https://github.com/TrojanFighter/IndieGameLegendaryHeroes/pull/283)、[DOOM #284](https://github.com/TrojanFighter/IndieGameLegendaryHeroes/pull/284)、[Chapter 06 #285](https://github.com/TrojanFighter/IndieGameLegendaryHeroes/pull/285)：均OPEN，评论及正式reviews均为空。此状态只说明本次查询未见反馈，不能代作者判定接收。三个候选已有事实锁、编辑对照与回读；Gunpoint的新报道接入和本对照日期问题仍有核证工作，真实读者阅读意愿没有验证。

**当前不具备回传main的完整验收证据。** 作者可对三份具体候选分别决定KEEP_ORIGINAL、REVISE_AGAIN或ACCEPT_REVISION，尤其判断观点强度、回顾插入和附录密度。方法值得继续用于有史料的局部编辑；尚无依据推广成全库统一模板或宣称阅读体验已经提高。正式正文、Case、Evidence、Claim、Schema与研究结论本轮均未修改。
