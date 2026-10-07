# Editorial Rewrite & Historical Fidelity Protocol

> **适用范围：** `book/profiles/`、`book/chapters/`、`book/life-routes/` 中准备对外阅读的叙事正文。**Owner：Lane C / Editorial。** Lane A 维护流程，Lane B 维护证据。本协议是 [EDITORIAL-GATE](EDITORIAL-GATE.md) 的执行补充，不是第二套事实源，也不创建新的 Case 状态。

## 目标与非目标

本协议处理两种不同的失败：

1. **Narrative sameness / AI 写作串味**：不同作者、不同人生被写成同一套“神话—反转—抽象结论”、短句断行、连续强调和行业术语。
2. **Fidelity regression / 忠实性倒退**：为使文章更生动，把回忆写成同期事实、把可能写成必然、把多人工作写成独力、把有条件的历史经验写成当代通则。

目标是让读者记住**谁，在怎样的时代和处境下，选择了什么、付出了什么、后来发生了什么**；不是躲避所谓“AI 检测器”，也不是删除作者本来的分析能力。

**绝不能**将禁词计数、短句比例或模型自称“更自然”作为质量合格证明。研究后台可以保留技术术语和审计语言；本协议主要治理 reader prose，不针对 Case / Evidence 做“去 AI 味”润色。

## 唯一事实源与权限

- 历史事实：`cases/` 与 `evidence/`；正式跨案例命题：`claims/`；未经核实的口述、传闻：Signal/H，不是可直接写成事实的来源。
- 书稿：只能组合和阐释已被以上材料承担的内容；不能因为改写时“需要一个场景”而补人名、对话、表情、家庭心理、时间、预算或因果。
- 本协议与 [research authority map](../schemas/research-authority-map.md)、[CSA](../schemas/context-situation-action.md)、[TEMPORAL VALIDITY](TEMPORAL-VALIDITY.md) 并行有效；冲突时以更严格的证据边界为准。
- 修改/批准正文属于作者或明确委托的编辑决策；Agent 可以提供候选、比对与问题清单，不自动将新稿覆盖旧稿。

## 编辑流程（一次只处理一篇或可比较的一组片段）

### 0. Lock：先封存事实边界，不立即重写

在编辑 PR 描述或审校笔记中记录：

- **Text & baseline**：目标正文路径、基线 commit / blob SHA、修改范围（章节 / 段落），使原文可回溯。
- **Authority**：对应 Case、Evidence Ledger、相关 Claim/Thesis 状态。
- **Historical fact lock**：至少列出可能被改写扭曲的关键人名、身份、时间、金额口径、团队/家属/外包参与、角色归责、否定、条件、原话归属、当事人回忆时点。
- **Unknown/weak evidence**：哪些细节缺来源、哪些属于 H/Signal、哪些原因只有事后猜测。
- **Transfer horizon**：涉及“现在也可以这么做”的句子，注明当年 regime 与当前适用边界。

> 不能在 Case / Evidence 找到出处的关键句：标记 `VERIFY_IN_LANE_B`，不要在 Lane C 猜一个合理版本。

### 1. Narrative packet：先确定这篇怎样讲人

短纸条即可，**不是新增 canonical metadata**：

| 项 | 必须回答 |
| --- | --- |
| 叙述对象 | 是单人传记、团队群像、失败调查，还是跨案例专题？ |
| 人物与时代 | 谁处于什么 production/distribution/capital regime？当时哪种今天常见的工具或渠道尚不存在？ |
| 处境与约束 | 当事人当时拥有什么、缺什么、可选择什么？ |
| 决策节点 | 具体行动、直接后果和可观察的反馈是什么？ |
| 主导疑问 | 读者读完最想知道的一个现实问题是什么？ |
| 叙述位置 | 传记、群像、调查、技术史、评论性随笔；为什么适合这个对象？ |
| 文风边界 | 哪些形象细节并无证据，不得用来营造戏剧性？ |

**统一的是作者判断的诚实程度，不是每篇文章的开头、段落节奏、视角或结尾。** 特别避免把不同主创者都写成同一种励志范本或同一位评论员的代言人。

### 2. Editorial Rewrite Pass：按顺序做三遍

**Pass A — Delete / 去冗余**

- 删除重复的 thesis 说明、每节末尾例行拔高、没有新增信息的“换句话说”。
- 发现连续“不是 X 而是 Y / 真正重要 / 这证明”时，先判断整段是否多余；**优先删，不能只替换同义词**。
- 保留必要的重大反驳、研究边界与精确判断。删除不等于抹平复杂度。

**Pass B — Restore the Person / 恢复人物及行动**

- 每段检查：读者是否看见真实的人、处境、动作和后果，还是只读到抽象机制？
- 能用同期日志、实际删减、具体收入结构、会议决定、版本变化、外部反馈讲清楚的，不先堆“runway / scope / selection capability”。
- 不得为“让人物活起来”虚构气氛、目光、内心独白、家庭冲突或戏剧性对话；若无足够事实，则选择说明性叙述。

**Pass C — Rhythm & Authorial Voice / 调节节奏**

- 连续长短段混合，以时间、动作、局部解释推进；短句和强调句只在真正需要重音处出现。
- 开头可以是时间线、人物具体处境、转折事件、失败现场、作品机制或问题，但不同篇不得机械重复“神话→否定→真相”。
- Profile 主要结束人物的故事；全书性归纳交给 Chapter / synthesis。
- 技术和商业术语先通过事例解释；保留作者独特见解，但不要让每个人物替作者朗诵同一套理论。

### 3. Fidelity Readback：逐项核改写是否改变认识

逐项审校**原文 → 修订文 → canonical source**，至少检查：

| 不可偷换项 | 典型倒退 |
| --- | --- |
| Actor / credit | 核心开发者被写成“独自完成”；外包、伴侣、资方、发行商被隐去 |
| Chronology / knowledge at the time | 事后回顾被改成当时预知成功；结果反推为先验规划 |
| Negation / modality | “可能 / 据回忆 / 并未 / 一部分”变为“必然 / 一定 / 全部” |
| Causation / alternative | 同期出现被写成因果证明；对立解释和失败前史被删 |
| Numbers / denominators | 毛收入变净利润、wishlist 变销量、奖项变市场验证、团队核心人数变总参与人数 |
| Evidence boundary | UNKNOWN、H、Signal、争议性回忆被润色成肯定句 |
| Historical regime | 当年的平台、工具、制度和生活成本被套用到今天 |
| Quote / intellectual property | 概括性转述被加上引号；未经核对的原话与长篇受版权保护文本被引入 |

**输出一个“Fidelity Readback”摘要**：每项 `PRESERVED / NEEDS_VERIFY / REGRESSION`，至少引用每个重大修改涉及的 Case / Evidence 位置。发现 `REGRESSION` 必须改回或交给 Lane B 核证，不能因为新稿更好读而放行。

### 4. A/B comparison 与验收

- 保留原文快照；新稿在独立 branch/PR 中审阅，不在同一轮顺手改 Case、Claim 或证据状态。
- 用 `A/B` 匿名对照旧稿与新稿；至少检查**人物具体性、叙事连贯度、作者观点保存、节奏变化、继续阅读意愿、事实忠实性**。
- 比较时不要把“改得更短”“禁词更少”自动当作进步；允许编辑结论为 `KEEP_ORIGINAL / REVISE_AGAIN / ACCEPT_REVISION`。
- **事实忠实性是不可补偿门槛**：即使 A/B 更好读，只要引入未纠正的史实/证据倒退，就不能接收。
- 作者/维护者验收后才合并。保存原版可由 Git commit 追溯；可读对照材料不必永久塞进 `book/`，避免制造双份正式书稿。

### 5. 交付合同

每次 Lane C 交付应说明：

1. 修改范围与 baseline SHA；
2. 删除/恢复/调整了哪些叙事结构，**而非统计替换了多少个禁词**；
3. Fidelity Readback 的重大核验点与未解决项；
4. A/B 或编辑对照的差异与编辑裁决；未盲测须明说；
5. Case / Evidence / Claim 是否**完全未改**；如果不成立则拆出 Lane B 任务；
6. 原文可恢复路径和下一步是否继续整篇编辑。

## 首轮校准：三个不同用途的样本

这不是全库自动清洗命令，也不是对三篇文章质量的最终判决。

| 样本 | 目的 | 建议试验 |
| --- | --- | --- |
| [Gunpoint](profiles/gunpoint.md) | 理论总结与转折句可能过密 | 选连续 2–3 个小节，做删除重复论点、恢复决策过程的候选稿 |
| [early id / DOOM](profiles/early-id-doom.md) | 群像、代际与技术史容易被写成概念演讲 | 选连续 2–3 个小节，保留真实关系、时代条件和相反观点 |
| [Limit Theory](profiles/josh-parnell-limit-theory.md) | **对照样本**：原稿较接近连续调查叙事 | 先只审读，必要时少量试改，检查新 Gate 是否反而破坏自然文章 |

推荐先各取有足够事实支撑的片段，再决定是否扩至全文。**禁止一次性批量改写全部 profile/chapters/life-routes。**

## 自动化边界

可以用脚本输出供编辑参考的段落长度、断行密度、重复套句候选和未链接的来源提示，但**不得**通过固定阈值设立“AI 文风 CI”、自动决定文风好坏或降低 Case 的事实约束。

Repeated defect → editorial rule；stable and mechanically decidable defect → tooling；critical structural obligation → CI。该顺序保持不变。
