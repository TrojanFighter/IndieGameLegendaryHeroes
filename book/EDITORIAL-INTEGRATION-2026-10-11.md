# 《独立游戏英雄传说》总编整合与下一轮写作分工｜2026-10-11

© 2026 洪荒行者。All Rights Reserved.

> **Lane C 编辑整合提案／不晋级研究事实／不代表作者验收已完成。** 本页是已有 `BOOK-ARCHITECTURE`、`EDITORIAL-GATE`、`WORKFLOW` 的一次具体应用，不设新的强制 Gate，不改变 Case/Evidence/Claim。公开项目：`TrojanFighter/IndieGameLegendaryHeroes`；私人项目不进入本仓。

## 1. 本轮收稿后的成书结构

**保留现有六部主线和七篇跨人物章节，不为研究题目增设新部。** 六部是一条人生链，而不是六项成功学步骤；第六章是贯穿其中的**插章／横向专题**，不构成独立第七部。

| 阅读次序 | 叙事责任 | 优先人物与真正的矛盾 |
| --- | --- | --- |
| Part I / Chapter 01 目标形成 | 从玩家、学生、员工到主动试做；教育与家庭不等于预定命运 | early id、Tom Francis；主体行为先于抽象归因 |
| Part II / Chapter 02 购买试错时间 | 谁承担生活成本，何时获得逐步加码的资格 | FTL、Kenshi、Psyonix；夜班／自营付费／Steam 扩张严格分期 |
| Part III / Chapter 03 失败的残留 | 失败保留下何种能力、工具、信用，什么没有回来 | Psyonix、Bills Must Be Paid、Limit Theory、Brigador 压力对照 |
| Part IV / Chapter 04 技术机会 | 继承工具、重组平台、创造窗口是不同的选择 | Carmack、Tom Francis、Brendan Greene；分清技术可得与技术自创 |
| Part V / Chapter 05 市场接入 | 玩家、反馈、付款何时改变继续生产的条件 | Minecraft、Factorio、Kenshi、Brigador；不能把曝光当销量 |
| **Interlude / Chapter 06 能力与团队** | 已有作品问题，却缺关键能力：删项目、学习、外包、合伙或融资如何改变命运 | GRIS、Gunpoint、The First Tree、Playdead；章节写故事，LR-004 才写决策操作 |
| Part VI / Chapter 07 成功之后 | 初次成功买来的不是永恒自由，而是新的组织、权利与职业选择 | Subset、thatgamecompany、id、Zach Barth |

**人物传记（Profiles）** 保存完整的人与时序；**跨人物章节（Chapters）** 负责同一问题下的冲突与比较；**Life Routes / Decision Router** 只负责读者当下的行动辨析，不侵占叙事正文。研究后台继续维护证据与未知数。技术分代大图属于 Part IV 的佐证入口，不自动把整本书变成年表。

## 2. 不再扩大章节数量，先进行文本整合

- 先将已有 14 篇 Profile 与 7 篇跨人物章节作为**编辑样本池**，而非默认 21 篇可出版定稿。
- 同一理论不应在每篇结尾重复宣读：人物篇以人物的下一步或仍未解的生活问题收束，横向结论留给 Chapter。
- 未有可核实的人物行动，不应为了统一文风虚构“具体场景”；无材料时退回 Lane B。
- 已有 Gunpoint / early id / Limit Theory 多代候选只做**相互比较**。合入 `book/research-notes/` 仅意味着保存候选及实验记录，**不意味着替换 `book/profiles/`**。
- 读者正文的事实错误优先校正：Kenshi 自营 alpha 早于 Steam 团队扩张；Gunpoint 起点年份；Limit Theory 2013 prototype／2022 source release；Zach Barth 2017 暂停与2022结束不是一回事。

## 3. 2026-10-11 收稿清点与冲突处置

本轮已按可回退、不过度修改已发布正文的原则合入 #281、#283、#284、#285、#286、#288、#289、#292、#293、#295、#326（总计11项）。这些变更**不构成候选稿的作者验收**。

- #294：原 PR 与 #281 共改 `book/EDITORIAL-INDEX.md`，合并发生冲突；本整合分支**无损转移**其两份独立流程／资料包文档，并以当前 main 为基线重写索引。旧 PR 应在整合合入后标明 superseded；不能 force merge。
- #311：含跨 Lane 的44文件变更，且当前不能合并；按 Reasonix 已核对的 PR #311–#314 诊断，必须拆开“事实补证／工具修正／读者正文／新 reader surface”分别验收。尤其 `reader/` 不进入正式导航，除非先有真实阅读反馈。
- #312→#318：分母和粗体 Class 匹配、稳定完整缺口队列，应作为一条独立 Lane A 修复，顺序上后于 #311 所依赖的基础代码；统计脚本仍 report-only。
- #313→#314：先修 CASE-051 同源 E006/E011 重复和 Microsoft 面试节点，再审叙事，不因追求流畅越过证据。
- #291/#308/#85 等大规模、含研究欠账或 draft 的 PR 不因为“清仓”就自动合并；逐案核完成状态、数据口径、文件重叠及 CI。
- #315 继续作为既有跨 Lane 整合 Issue，避免再创建并行“总控”流程。

## 4. 编辑评价：DS／Reasonix 与 Codex

**Reasonix/DS：审稿与找事实断裂强，成书候选仍需第二轮。** 其审查准确揭露了 Kenshi 收入顺序、Zach暂停历史、Limit Theory 未核年份与文章公式化结尾。#314 Zach 新段落保持了大体事实时序，但对 Ironclad 时点写成“那段时间”有指代歧义，增加约四段解释性文本，并以抽象口号收束，尚不达可出版质量。裁决：`REVISE_AGAIN / AUTHOR_ACCEPTANCE_PENDING`；只授权**一篇窄幅人物修订试验**，独立再审通过后才扩大到第二篇，不许自动批量改稿。

**Codex：适合做执行主编／制作监工**——处理 GitHub 分支收口、事实锁、source pack、段落差异、引文回读、盲读材料准备，明确记录保留/拒绝理由。其 #326 Gunpoint/early id 候选在结构上更接近可连续阅读传记，但仍有研究缺口、重复观点和未测真实读者意愿；标为 `AUTHOR_REVIEW_CANDIDATE`，不自动覆盖正式人物稿。

**主编（本轮 ChatGPT）：** 负责全书主问题、篇章节奏、跨人物对比与有证据的编辑裁决；作者洪荒行者保留最终文字／出版裁决。没有独立盲测时禁止写“读者证明新版更好”。

## 5. 接下来交付，不增加全库 Gate

1. **Codex / Lane A+B 整合：** 在最新 main 的独立 PR 中修复 #311 核心事实与 PR #312/#318 的报告错误；避免重复吸收已合并的 #288。同一内容只保留 canonical Owner，禁用 force overwrite；必须列出被保留的 main 变化。关联 Issue #315。
2. **DS / Lane C 修改：** 对 #314 Zach 写两段以内的事实锁改稿：Ironclad 时点明确，先回 Lane B 纳入 E006 或相应节点的 Microsoft 面试；去重复收束，保留所有已核决定与负面证据。附原文/修订/A-B Fidelity Readback。不要改正式 profile。
3. **Codex / Lane C 对照编辑：** 从 #326 的 Gunpoint 与 early id，和 #289/#283/#284 的旧候选进行对照，输出各篇最有生命力的事件段和不得取用的未证细节；Limit Theory 为对照组，原文若更强应保留。
4. **真实读者反馈：** 只测试少量内容的具体理解/继续阅读意愿，不以 AI 自评、词频或短句率代替。无结果时继续保留候选状态。

### 退出条件

- 关键人物、时序、数字口径、否定、来源时点、UNKNOWN 不发生倒退；
- 正文中未证事实不能因“有审稿意见”继续以肯定句传播；
- 读者能复述某个人做了什么、付出了什么，而不只是记得一句理论；
- 作者明确接受后，才允许替换正式 `profiles/` 或 `chapters/`。

**本计划只是本轮总编排产；具体研究、写作仍遵守现行 AGENTS / WORKFLOW / EDITORIAL-GATE。**
