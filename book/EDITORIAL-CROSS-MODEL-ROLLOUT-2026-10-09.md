# 多案例跨模型非虚构编辑试点｜从 Kenshi A 稿走向全书（2026-10-09）

> **状态：PROPOSED / STAGED PILOT / AUTHOR APPROVAL REQUIRED。** 本文件是 #292 [单案例跨模型实验](https://github.com/TrojanFighter/IndieGameLegendaryHeroes/pull/292)的扩展计划；不宣称 #292、DS 第二版、其他候选或整书已获文学验收。
>
> **仓库：** `TrojanFighter/IndieGameLegendaryHeroes`。**Owner：Lane A（试点流程与资料包接口）**；每篇研究取证仍属 Lane B，组稿、匿名试写、编辑裁决与成书属 Lane C。
>
> **唯一升级对象：生产流程，而不是 DeepSeek / Codex 某种统一文风。** AI 供给候选，人类作者负责文学价值与最终判断；事实核验不由文学模型自证。

## 1. 起点：已有证据与尚未发生的验证

- 截至本轮核验，现有读者层为 [14 篇 Profiles](profiles/README.md) 与 [7 篇 Chapters](chapters/README.md)。这些数量是现有目录，不等于 21 篇都已具备改写所需的独立一手素材。
- Kenshi 首次跨模型试写目前有 [A v1](research-notes/cross-model-narrative-trial-2026-10-09-kenshi-candidate-a.md) 与 [A v2](research-notes/cross-model-narrative-trial-2026-10-09-kenshi-candidate-a-rev2.md)（来自独立试写分支，**不在 main**）。实验记录称 Reasonix agent，底层实际模型版本 UNKNOWN；**尚无真正独立模型 B、真人盲读或独立全篇保真通过**。
- A v2 的确出现更主动的事件组织与幽默，也暴露风险：口述的模拟系统 Bug 被添入动作／时间细节；Hunt 认为混乱是开发问题的态度可能在翻译中被改变。**后续史料包必须连同动词、情态、引语立场和事件时点一起交付。**
- [#289](https://github.com/TrojanFighter/IndieGameLegendaryHeroes/pull/289) 是其他模型人物长候选，不是最终对照胜者；[来源补证 #288](https://github.com/TrojanFighter/IndieGameLegendaryHeroes/pull/288) 与其分支 base 关系须独立核对，不能把未合并事实描述为 main 已正式收录。
- 此前 [EDITORIAL-GATE](EDITORIAL-GATE.md) 与 [REWRITE-PROTOCOL](EDITORIAL-REWRITE-PROTOCOL.md) 已解决事实门槛、去模板及历史回读。本计划只新增 **「候选源包」与「逐类试验—推广决策」接口**，不增加 Humanizer、AI 检测器、词频配额、全库自动批改。

## 2. 生产链：责任隔离、输入隔离、可审核的输出

```text
Lane B: Evidence/Case/Claim、原始来源与争议核查
    ↓ 原件快照；不能只给已有 Profile
Lane C 的资料编辑：NARRATIVE SOURCE PACK
    - chronology / incident inventory / actor & voice / limits
    - 不交给独立作者旧稿、结论提纲或他人样稿
    ↓ 同一事实包、同一任务条件
    ├── Writer A（独立模型／人） → 候选 A
    └── Writer B（独立模型／人） → 候选 B
    ↓ 两份写作均封存（可有原稿 baseline 作第三候选）
编辑/读者先读去身份正文 → 记录偏好与原因 → 解盲
    ↓
独立 fact-checker: 全部 Evidence / 引文 / 时态 / 归责 / 暗添动词
    ↓ 如有叙事潜力且修正所有 REGRESSION
作者选择：KEEP / REWORK / SELECT FOR EXPANSION
    ↓ 扩成整篇还要再次验收，不能以千字小样代替
Lane C 独立 PR → 作者审核 → 正文采纳或撤回
```

**不能混淆的四种检查：**

1. **素材有效性：** Writer Pack 中每项材料有 E-ID / 来源 / 发布时间 / 口述时点；没有证据就留白。
2. **文学判断：** 人物是否可辨认、事件是否有继续阅读吸引力、段落是否形成独特节奏；不由研究字段的覆盖率或 AI 自评分替代。
3. **忠实性：** 行动、引语、态度、时序、因果、数字、协作者、历史环境的逐句反向回读；发生史实倒退则阻止采用。
4. **生产效率：** 只记录真实耗时、尝试稿份数、编辑返工和最终是否采用；**不要**将少量成功候选反推“某模型胜率”。

独立作者不能阅读彼此候选、旧版完整 Profile 或事先写好的统一叙事结构；**这是对独立 A/B 的约束，不是出版永远不能使用旧稿**。编辑和保真审稿人可以读取全部材料，但须在封存 A/B 之后进行。

## 3. 样本矩阵：先跨类型，再扩篇幅

| Wave / 地位 | 人物或作品 | 必须检验的写作难点 | 拟采用材料 Owner |
| --- | --- | --- | --- |
| W0，已生成 A v1/v2，**尚未完成对照** | [Kenshi / Chris Hunt](profiles/kenshi.md) | 黑色幽默的模拟失控；夜班与多年制作；控制权交给同伴 | CASE-012 |
| W1-A，优先 | [Gunpoint / Tom Francis](profiles/gunpoint.md) | 开发者本人自嘲、同期博客和后见访谈；不能写成品味理论讲座 | CASE-007 |
| W1-B，优先 | [Limit Theory / Josh Parnell](profiles/josh-parnell-limit-theory.md) | 失败／未交付、工程高光与个人成本同时成立；拒绝单因归罪 | CASE-054 |
| W1-C，优先 | [early id / DOOM](profiles/early-id-doom.md) | 多位当事人、家属与出版者；先选 **一个相遇／合作／冲突** 故事，不总述整部史 | CASE-016 |
| W1-D，优先 | [GRIS → Neva / Nomada](profiles/nomada-gris-neva.md) | 三个共同作者的动机、视觉与技术相遇；人数与融资不凭空补 | CASE-050 |
| W2，W1后选择 | [FTL](profiles/ftl.md) | 两人、工资与职业风险；限制「极小团队一夜成功」叙事 | 对应已有 Case/Evidence，开工时重新定位 |
| W2，W1后选择 | [The Magic Circle → The Blackout Club](profiles/question-magic-circle-blackout-club.md) | 完成、获关注却经营受挫，然后作出第二次产品选择 | CASE-048 |
| W2，W1后选择 | [第六篇跨案例专题](chapters/06-you-do-not-need-a-standard-studio.md) | **章节非传记**：允许争论与作者判断，不把五篇传记缩成每人一段 | CASE-007 / 042 / 048 / 050 / 056 等 |

**W0 → W1：** 完成 Kenshi 的新稿事实修正与一个真正未读过 A 的独立 B；若没有 B，W0 只能用于编辑校准，仍可开始 W1 的资料准备，不能宣称 A 胜出。

**W1：** 四种差异大的类型各取一个 800–1500 汉字左右的连续试写片段，每例使用两份独立候选；原稿可在**盲读阶段**成为第三文本，但不要把原稿交给 Writer A/B。若素材不足以形成真实事件链，就先核资料或缩短，不以凑字数补细节。

**W2：** 从 W1 获得明确叙事优势且通过历史回读的案例中，选择**两例不同类型**扩写约 2500–3500 汉字，再加入 FTL、Question 或 Chapter 06 中值得测的不同类型。跨案例 Chapter 使用专门的多对象事实包，不给模型「照着 X、Y、Z 三例证明一个结论」的材料安排。

**W3：** 由作者决定是否扩大到其余 Profiles/Chapters 与 [斯拉夫姊妹篇](../sister-projects/slavic/)。**不是每个 Case 必须生成 Profile，也不是每篇书稿必须接受跨模型改写。** 史料稀缺时可优先补取证、保留原稿或用短篇评论替代长传记。斯拉夫篇遵守独立的 Evidence/Case Owner，不把其研究矩阵直接变成传记。

## 4. 推广前的可证伪判断，而不是「好像更好」

W1 四例完成后，形成一页 **editorial experiment register**，如实记录每个样本的：

- source pack 的精确 Git SHA／Case+Ledger 版本及是否包含尚未合并的补证；
- 两位独立作者是否拿到相同材料，具体模型标识是否可查、是否有交叉阅读／提示词变化；
- 原版 / A / B 的匿名稿路径、试写内容长度、实际写作修订轮次；
- 人类作者与其他读者的**真实**匿名比较（没有就 `NOT TESTED`），至少记一处真正吸引人的段落及一处跳读／出戏的段落；
- 事实审稿发现的 `MISSING`、`ADDED_WITHOUT_EVIDENCE`、`ALTERED_MEANING`、`CHRONOLOGY_DRIFT` 和修复证据；**不以机器人自称通过替代独立核对**；
- 真实耗时／编辑返工／是否产生可扩写的人物线；结论为 `KEEP_EXISTING / REVISE / SELECT_AS_PILOT`；
- 不能把**审稿前的主观观感**写成事实通过，也不能只统计胜者、不登记放弃的失败稿。

推广条件**不是一个漂亮的总分数**，而是作者在不同类型中反复观察到：(a) 候选的阅读意愿或人物记忆优于旧稿且可说清楚为何；(b) 历史事实问题可在合理编辑成本内修正；(c) 研究资料包能支持两个模型各自作不同选择；(d) 至少一篇较长文本仍能保持节奏；(e) 没有把作者的独立思想和失败者的复杂性抹平。

若失败：先分析事实包是否把理论／目标预装为必写、原始来源是否不够、任务是否强迫解释完整生产史、独立性是否破坏；**不得自动用新增禁词表或强制模板修理实验。**

## 5. 研究资料的双轨交付制度（今后研究进入写作时执行）

**Lane B 的 canonical 研究**仍严格按现行 Case / Evidence / Claim / Source 规则；完整覆盖跑道、团队、资金、工具、市场、失败、来源等级、反例与统计分母等，不为「戏剧化」删除普通样本或不利事实。

**新增衍生层：Narrative Source Pack**，见 [writer-facing source packet contract](EDITORIAL-NARRATIVE-SOURCE-PACK-CONTRACT.md)。这层在人物进入 W1/W2 时才创建，不要求现在给全部 63+ Case 补模板。由 Lane C 的资料编辑从 Lane B 已核材料整理，写作模型只接触中性事实与原话，不看原 Profile、理论结论、其他候选或故事开头范例。Pack 不是新的 Evidence，也不是「事实本体」；每项直接回链来源，原源有冲突就显式保留。

未来资料收集的优先级可由 `有利于判断事实` 和 `有利于文学非虚构` 双轴决定：

- **必须搜：** 同期日记、开发日志、具体制作事故、版本取舍、工作状态、行动后果、访谈提问者与当事人直接答复、可信的反面见证和同时期公开作品；
- **同样重要：** 青少年／职业形成、同伴与家庭真实参与、产品未成功时的状态、人物真实用过的术语与自嘲，而非事后已成功者的抽象智慧；
- **必须分清：** 可观察动作 vs 当事人多年后的自我解释；玩家实际行为 vs 开发者举例；产出的源文原话 vs 编辑的中文译述；高光技术样本 vs 大规模成功概率；
- **不必为叙事强搜：** 未公开私人生活、臆测家庭谈话、真假难辨的戏剧性现场、没有来源的情绪和心理描写。

### 为什么这是工作流革新而不是把材料写成新模板

Case 可以保有完整研究矩阵；**Pack 应允许作者跳过 70% 或更多暂时无关的事实**（比例不是目标），只让几个经证据支持、相互形成张力的事件进入文章；其余由独立核查层兜底。

Pack 提供「人物当时说了什么、做了什么」，不提供「这证明了什么」「应如何写一个爆款开头」或已写的漂亮段落。每位创作者可以决定从哪件事开篇、哪些东西暂时不讲。**给作者的是自由选择空间，给审稿人的是完整追溯链。**

## 6. 文件、分支、验收与权限

- 试点计划及接口：**Lane A 文档 PR**，不能修改 Case/Evidence/Claim 或 reader 正文。
- 首批中性事实包：**独立 Lane C 筹备 PR**，每个包标明来源版本、作者不可读旧稿、哪些口径仅来自待审研究分支；不宣称新增史实。
- 独立 A/B 稿：**每样本单独 Lane C PR/候选文件**。实测模型和提示词、版本、交叉阅读的披露在编辑记录，不要求正文透露模型身份。
- 事实增量：单独 **Lane B PR**；不得在 Lane C 文稿里顺手追加 canonical 研究事实。
- 主库 `main` 受保护；作者批准前不覆盖正式稿。遵守 [Project Routing Gate](../docs/project-routing-gate.md) 与 [public research boundary](../docs/public-research-boundary.md)；不得导入私人项目资料或未授权素材。
- 与 #292 保持**试点扩展关系**，不是推翻或复制它。#292 的 Kenshi 单次试验可作为校准样本，但其结果没有真人盲读支持。

**下一执行批次：** 先复核 Kenshi A v2 的动词、Hunt 引语立场、bug 时点与薪水时间范围；让独立模型 B 在未读 A 的条件下按冻结包试写；并行准备 Gunpoint、Limit Theory、early id / DOOM、GRIS 的首批中性素材包，再逐例出独立新稿。未经作者确认不进入 W3。
