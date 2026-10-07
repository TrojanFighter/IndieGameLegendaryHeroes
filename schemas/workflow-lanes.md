# Workflow Lanes

本项目把工作拆成三条车道。目的不是增加流程，而是防止“研究事实”“库治理”“成品叙事”在同一个任务里互相偷换。

## Lane A — Library Operations / 库运维

负责：

- 目录与信息架构；
- README / reader navigation；
- schemas；
- metadata conventions；
- lint / CI；
- Issue intake；
- source health；
- Case Explorer / search index；
- build / release pipeline；
- 自动统计与派生视图；
- workflow documentation；
- Case Graduation 的机器资格规则与派生 maturity 视图。

### Lane A 禁止事项

库运维任务不得为了填满新字段而自行补研究事实。

尤其禁止：

- 看到旧 Case 没有时代条件，就靠常识批量补；
- 为了让 lint 通过而降低证据标准；
- 在 schema migration 时顺手改变 Case 的历史判断；
- 把工具层的推断写回 canonical evidence；
- 因为 maturity 工具判断 `REVIEW-READY` 就自动把 Case 升为 REVIEW / STABLE。

如果新 schema 暴露旧案例信息缺口，应记成 `pending / migration queue`，交给 Lane B。

## Lane B — Case Research / 案例与课题研究

负责：

- 新案例输入；
- Case 时间线；
- Evidence Ledger；
- 来源核验；
- 弱 Signal / 口述 / 传闻的登记与核验；
- Contributor audit；
- Market-access audit；
- Context–Situation–Action audit；
- Claim 支持 / 反例；
- comparator / failure audit；
- thesis candidate 的定向取证；
- Case Graduation 前的 adversarial review 与 material unknown 分类。

### Lane B 输入分流

收到聊天、Issue、口述、截图、旧记忆、外部 AI 结果或未核稿时，先判断它属于：

```text
可追溯来源事实 → Evidence
弱口述 / 传闻 / 未索引线索 → Signal
作者自己的解释 → H / Author-Origin / thesis incubator
跨案例可证伪命题 → Claim candidate
```

Signal 协议见 [`signal-decision-protocol.md`](signal-decision-protocol.md)。

**Signal 可以改变“先查什么、是否 PROBE / HEDGE”，不能改变“什么已经被证明”。**

### Lane B 输出合同

一个研究任务交回仓库时，尽量明确：

- Case ID / Subject；
- Period covered；
- 新增或修改了哪些 Evidence IDs；
- 新增或处理了哪些 Signal IDs；
- 哪些事实仍 UNKNOWN；
- 哪些未知仍有现实可核验路径，哪些基本不可恢复；
- 哪些 Claim 被支持 / 削弱；
- Contributor audit 状态；
- Market-access audit 状态；
- Context audit 状态；
- 关键 CSA Decision Units；
- 是否存在反例 / 替代解释；
- 是否已达到 `REVIEW-READY` 的研究条件；
- 哪些内容有资格进入 reader layer。

### Lane B 禁止事项

研究任务原则上不顺手修改：

- schema；
- lint 规则；
- CI；
- build；
- repo-wide taxonomy。

如果研究暴露了新的结构需求，记录成流程问题，交回 Lane A 单独处理。

## Lane C — Editorial / Book Layer

负责：

- `book/profiles/`；
- 书级 thesis synthesis；
- TOC；
- 章节结构；
- 叙事节奏；
- 写作风格；
- 成书导出。
- 既有 reader prose 的逐篇编辑与历史忠实性回读；具体过程见 [Editorial Rewrite Protocol](../book/EDITORIAL-REWRITE-PROTOCOL.md)。

Lane C 只能消费已经进入 Case / Evidence / Claim 的事实。

### Lane C 写作入口

新稿先执行 [Editorial Gate：新稿写作入口](../book/EDITORIAL-GATE.md#05-新稿写作入口预防模板化)，留下事实锁与 Narrative Packet 后再组织正文；初稿也需 Delete → Restore Person → Rhythm、Fidelity Readback 和明确的作者验收状态。人物模板的研究字段不能自动成为每篇相同的叙事大纲。旧稿改写按既有 Rewrite Protocol 保存基线及 A/B；没有旧版的新稿不伪造比较结果。

这些编辑流程规则由 Lane A 维护；Lane C 执行，不以源头防错为由改变 canonical research facts。

### Lane C 禁止事项

- 为了故事顺畅补 UNKNOWN；
- 把 Signal / 口述传闻写成已证事实；
- 把 Thesis Candidate 写成已证明 Claim；
- 把 reviewer / publisher / platform / family support 隐去；
- 因为文章需要高潮而重排真实因果顺序；
- 在 reader layer 直接创造 canonical facts。
- 因为表面上的“AI 文风问题”对全部文章进行无差别批量重写或强行统一叙述风格。

## Handoff rule

推荐工作流：

```text
Chat / Issue / external material
      ↓
Lane B: intake classification
      ├─ Signal / H / research-intake
      └─ verified Evidence
               ↓
         Case + audits
               ↓
      adversarial review / graduation
               ↓
canonical research corpus
               ↓
Lane C: reader profile / synthesis
               ↓
reader layer

Lane A 横向维护 schema / lint / navigation / tools，
但不替 Lane B 生产历史事实或自动完成研究裁决。
```

研究对象的权威 Owner 关系见 [`research-authority-map.md`](research-authority-map.md)。Case 收口规则见 [`case-graduation.md`](case-graduation.md)。

## Maturity / Freshness / Action 必须分离

不要把三个问题压成一个“置信度分数”：

```text
Epistemic maturity   研究知道到什么程度？
Temporal freshness   这个判断多久可能过期？
Decision posture     在仍然不确定时现在采取什么姿态？
```

例如一个 `WEAK_SIGNAL` 可以因为窗口短、核验成本低而对应 `PROBE`；一个 STABLE 的历史 Case 则可能完全不需要 Decision Posture。

`WATCH / PROBE / HEDGE / ACT / NO_ACTION` 不是新的 Case / Claim 状态，也不自动触发任何外部动作。最终裁决仍由作者 / 维护者作出。

## Why separate conversations / work sessions

不同车道适合不同上下文：

- Lane A 需要长期记住仓库结构、lint、漂移事故和工具债务；
- Lane B 需要把上下文预算集中给来源、时间线、反例和证据；
- Lane C 需要集中处理人物、节奏和跨案例主题。

把三类工作长期混在一个对话里，会导致：

- 运维讨论被大量案例事实淹没；
- 案例研究被 schema/CI 细节打断；
- 编辑时误把临时研究假说当成正式规则；
- Agent 容易因为“当前任务很顺手”跨层修改不该修改的东西。

因此默认建议三条车道分开维护，并用 Git / Case ID / Evidence ID / Signal ID 作为交接接口。

## Change escalation

当真实工作中重复出现同一问题时，按以下顺序升级：

1. 第一次：人工修正；
2. 再次出现：写进对应 schema / workflow rule；
3. 仍然重复且可机械判断：写 lint / tool；
4. 必须每次保证：进入 CI；
5. 只有真实用户需要消费时：再做新的 reader surface / export / skill。

这条原则借鉴 HowToLiveBetter 的演化经验：**不要预建所有治理；让重复故障决定下一层自动化。**
