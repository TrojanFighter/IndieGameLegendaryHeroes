# Research Authority / Ownership Map

本文件借鉴策划文档库中的“控制层 + 唯一 Owner + 输入不自动晋级”原则，但针对公开研究仓库重新定义。

核心原则：

> **作者 / 维护者是最终裁决者；`main` 是已发布研究基线；Evidence / Case / Claim 各自拥有不同事实职责；聊天、Issue、Signal、外部 AI 输出永远只是输入，除非经过明确核验与晋级。**

---

## 1. 权威顺序

发生冲突时按以下顺序判断：

```text
1. 作者 / 维护者当前明确裁决
2. 控制层：AGENTS.md / WORKFLOW.md / schemas/
3. Canonical research：Evidence Ledger / Case / Claim
4. Derived views：metadata / Explorer / stats / translation registry
5. Reader layer：book profiles / thematic synthesis
6. Intake：Signals / research-intake / Issues / chat / screenshots / external AI output
```

下层不能自动覆盖上层。

特别是：

```text
Signal ≠ Evidence
Hypothesis ≠ Claim
Reader profile ≠ Case
Issue ≠ canonical fact
Chat ≠ repository decision
Derived metadata ≠ independent fact source
```

---

## 2. 对象 Owner

每一种信息只允许一个规范性 Owner：

| 对象 | Owner | 其他地方如何使用 |
|---|---|---|
| 来源直接支持的事实 | Evidence Ledger | Case / Claim 链接并解释，不复制完整账本 |
| 一个案例的综合生产史与边界 | Case | Profile / research note 链接并重述 |
| 跨案例可证伪命题 | Claim | Case / thesis 链接，不在多个地方各写一版命题 |
| 弱口述 / 传闻 / 未核线索 | Signal | Case / note 只链接或标 H，不当事实 |
| 作者自己的理论方向 | Author-Origin / thesis incubator | Claim 只有过证据门槛后才晋级 |
| 读者叙事 | Book profile | 只消费 canonical research，不创造新事实 |
| 统计 / Explorer | metadata + derived tooling | 从 canonical 计算，不手工造第二数据库 |

如果不知道应该把一句话写在哪里，先问：

> **这句话是在记录来源事实、案例解释、跨案例命题、弱线索，还是读者叙事？**

---

## 3. 晋级链条

信息不是“写进 repo 就算正式”。推荐路径：

```text
Chat / Issue / external material
        ↓
Research intake / Signal
        ↓  核验
Evidence Record
        ↓  综合
Case
        ↓  跨案例检验
Claim
        ↓
Book / synthesis
```

不是每条输入都必须走完整链：

- 无价值线索可以终止；
- 无法恢复的口述可以长期留 Signal；
- 单案事实不一定需要进入 Claim；
- 作者理论可以长期留 thesis incubator；
- STABLE Case 也可以保留 bounded UNKNOWN。

---

## 4. 不允许的自动升级

任何 Agent / Codex / 外部模型不得擅自：

- 把 Signal 改写成 Evidence；
- 因多个转载重复出现就判断“已被多个独立来源证实”；
- 把 H 改成 P0/P1/S1；
- 把 RESEARCHING Case 自动升为 REVIEW / STABLE；
- 把 reader profile 中的顺畅叙事反向写回 Case 当事实；
- 因“行业常识”补齐 UNKNOWN；
- 为了毕业删掉仍有解释价值的弱证据或反方材料；
- 因 Decision Posture = ACT 就声称底层 Signal 已经 VERIFIED。

---

## 5. Maturity 与 Action 分离

研究对象至少存在三条互不替代的轴：

```text
Epistemic maturity   这件事我们知道到什么程度？
Temporal freshness   这个判断多久可能过期？
Decision posture     在仍有不确定性时，现在采取什么姿态？
```

例如：

```text
某发行商正在收缩某类项目预算

Epistemic: WEAK SIGNAL
Temporal freshness: VERY_HIGH
Decision posture: PROBE / HEDGE
```

完全合法。

反过来：

```text
DOOM 1993 production history

Epistemic: STABLE Case
Temporal freshness: LOW
Decision posture: N/A
```

也合法。

---

## 6. GitHub `main` 的含义

`main` 表示：

> **当前公开发布的研究基线。**

它不表示每一句内容都已经 VERIFIED，也不表示所有 Case 都 STABLE。

因此 `main` 中可以存在：

- SKELETON；
- RESEARCHING；
- H；
- Weak Signal；
- open questions；
- CONTRADICTED / rejected hypotheses 的历史记录。

前提是状态和边界明确。

GitHub 的职责是保存：

- 什么时间加入了某判断；
- 后来如何被支持、削弱或推翻；
- 谁改变了状态；
- 旧版本为什么不再现行。

---

## 7. 什么时候新建文件

新建对象前先问：

1. 是否已经有对应 Owner？
2. 能否作为现有主档的一节？
3. 新文件是否承担长期独立职责？
4. 谁会持续维护 / 路由它？

通常值得独立新建的包括：

- 正式 Case / Claim / Evidence Ledger；
- 独立 Signal；
- 一个长期专题协议 / audit；
- Graduation Review；
- 需要单独保存演化史的 Author-Origin thesis。

不要为一次聊天摘要、同一结论的另一种措辞或单纯方便复制再造新 Owner。

---

## 8. 与现有协议的关系

- Evidence 标准：[`evidence-record-template.md`](evidence-record-template.md)
- CSA：[`context-situation-action.md`](context-situation-action.md)
- Signal 与时效判断：[`signal-decision-protocol.md`](signal-decision-protocol.md)
- Case 收口：[`case-graduation.md`](case-graduation.md)
- Workflow lanes：[`workflow-lanes.md`](workflow-lanes.md)

这些协议负责不同问题，不互相复制整套规则。
