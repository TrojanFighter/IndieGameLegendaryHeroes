# Signal / Weak-Evidence / Decision-Posture Protocol

本协议处理一种 Evidence / Claim 系统不能单独解决的问题：**信息可能重要、时效性很高，但当前无法达到公开可核验的强证据门槛。**

典型来源包括：

- 当事人或从业者口述，但没有公开录音、文字或可归属材料；
- 二手转述、圈内长期流传的说法；
- 已删除帖子、老论坛记忆、无法恢复的旧网页；
- 作者本人曾见过但当前无法重新定位的材料；
- 多个弱来源反复指向同一现象，但尚无 P0 / P1 / S1 支撑；
- 会快速过期的行业信号，例如发行偏好、平台政策执行、渠道生态、AI 工作流变化。

本协议的目标不是降低 Evidence 标准，而是把两件事分开：

> **这件事有多可信？**
>
> **在仍然不确定时，我们现在应该如何对待它？**

---

## 1. Signal 不是 Evidence

Signal 是**研究线索对象**，不是事实账本。

- Signal 可以提高核验优先级；
- Signal 可以触发低成本、可逆的调查或准备动作；
- Signal 可以长期保留为“plausible but unresolved”；
- Signal **不能直接提高 Case 的 `evidence_strength`**；
- Signal **不能单独把 Claim 升为 SUPPORTED / VERIFIED**；
- Signal **不能在 reader profile 中改写成确定事实**。

只有找到可归属、可追溯、足以进入 Evidence Ledger 的材料后，相关部分才能按正常 P0 / P1 / S1 / S2 / H 规则晋级。

---

## 2. Single Owner / 唯一主档

公开可保存的 Signal 统一放在：

```text
sources/research-intake/signals/
```

编号：

```text
SIG-001
SIG-002
...
```

Case、Claim、research note、Issue 只链接 Signal 主档，不复制完整内容。

Signal 晋级为 Evidence 后：

- Evidence Ledger 成为已核事实的 Owner；
- 原 Signal 保留为 intake / provenance history；
- 不把已晋级内容继续维护成两套并行事实。

这沿用本仓库的一般规则：**一个规范性对象只保留一个主文档，其他页面链接而不是复制。**

---

## 3. 私人口述与公开边界

本仓库是公开仓库。Signal 协议**不构成上传私人信源的许可**。

以下内容不得进入公开 GitHub：

- 能识别未授权私人信源身份的信息；
- 私聊原文、联系方式、私人截图、未公开合同或保密资料；
- 通过组合细节可反推出信源身份的记录；
- 私人项目资料或内部商业信息。

处理规则：

1. 原始私人信源保留在公开仓库之外；
2. 只有在安全且有研究价值时，公开库可以记录**去身份、不可反推来源的假说摘要**；
3. 若连摘要都会暴露来源，则完全不入库；
4. `private-content-guard` 只能做词表防错，不能替代人工语义判断。

---

## 4. Signal 记录字段

每个公开 Signal 至少记录：

```markdown
# SIG-XXX — 简短标题

- Status: UNVERIFIED / WEAK_SIGNAL / PARTIALLY_CORROBORATED / CONTRADICTED / PROMOTED
- First recorded:
- Last reviewed:
- Related Cases / Claims / Research Notes:
- Provenance class:
- Independent sources:
- Specificity: LOW / MEDIUM / HIGH
- Time sensitivity: LOW / MEDIUM / HIGH / VERY_HIGH
- Temporal decay: LOW / MEDIUM / HIGH / VERY_HIGH
- Review by:
- Decision relevance:
- Publicability: PUBLIC_SAFE / SANITIZED_SUMMARY

## Signal
准确记录当前实际知道的说法，不润色成事实。

## Provenance
说明是亲历、当事人口述、二手转述、圈内传闻、作者记忆、删除材料残影等。
不要在公开库暴露未授权身份。

## Current Corroboration
目前找到的支持、冲突和空白。

## What Would Verify It
什么材料能使相关内容晋级正式 Evidence？

## What Would Falsify It
什么材料会显著削弱或推翻？

## Decision Consequence
如果该 Signal 为真 / 为假，分别会改变什么研究或行业判断？

## Decision Posture
WATCH / PROBE / HEDGE / ACT / NO_ACTION
并写明理由、可逆性、错误代价和复核日期。
```

`Status` 是 Signal 自己的线索状态，不替代 Case / Claim 的状态词。

---

## 5. Provenance 不是搜索排名

“公开检索不到”不等于“没有信息价值”。评估 Signal 时优先问：

1. 距事件有几手？
2. 能否说明来源角色与时间，而不暴露私人身份？
3. 是否存在相互独立的重复来源？
4. 说法是否具体到人物、时间、金额、动作或结果？
5. 是否存在可证伪细节？
6. 当前公开材料与它一致、冲突还是完全沉默？

多个相互抄袭的帖子不算多个独立来源。

---

## 6. Evidence Strength 与 Decision Posture 分轴

研究可信度与行动时效性不得合并成一个分数。

### Epistemic axis

沿用现有 Evidence / Claim 体系：

- P0 / P1 / S1 / S2 / H
- VERIFIED / SUPPORTED / CONTESTED / WEAK / UNVERIFIED / REFUTED

### Decision axis

仅用于明显具有时间窗口或机会成本的问题：

- `WATCH`：继续观察，没有理由现在承担行动成本；
- `PROBE`：做低成本、可逆的核验或小实验；
- `HEDGE`：证据不足但错过成本高，先购买选择权 / 保留备选；
- `ACT`：现有证据与时间窗口已足以支持当前行动；
- `NO_ACTION`：当前明确选择不行动，并记录原因与复核条件。

Decision Posture **不是事实状态，也不是对作者的自动指令**。它是当前资料条件下的可审计建议姿态，最终裁决仍由作者作出。

---

## 7. 不行动不是零成本基线

对于会快速变化的问题，必须显式考虑：

- 等待更强证据会不会错过窗口？
- 错判为真（false positive）的代价是什么？
- 错判为假（false negative）的代价是什么？
- 当前动作是否可逆？
- 能否通过小额成本购买 optionality？

推荐原则：

> **证据越弱，行动越应该可逆；窗口越短，越不能把等待确定性当作无成本。**

因此：

| 情况 | 默认姿态 |
|---|---|
| 弱 Signal + 低时效 | WATCH |
| 弱 Signal + 高时效 + 低成本可逆 | PROBE |
| 弱 Signal + 高时效 + 错过代价高 | HEDGE |
| 强证据 + 高时效 | ACT |
| 明确不值得投入 | NO_ACTION |

这只是默认起点，必须写具体理由。

---

## 8. Freshness / Judgment Decay

历史事实与行业判断的衰减速度不同。

- 1993 年 DOOM 的开发史：通常 `Temporal decay = LOW`；
- 2026 年发行商签约偏好：可能 `HIGH / VERY_HIGH`；
- 平台算法、渠道政策、AI 生产工具：通常需要更短的 `Review by`。

`last_verified` 只能说明上次核验时间，不能自动说明知识已经过期。只有明显具有时效性的判断才增加 `Temporal decay / Review by`，不要把所有历史 Case 都变成定期刷新任务。

---

## 9. Signal 的晋级与终止

### PROMOTED
找到足以进入 Evidence Ledger 的来源后：

1. 新建 / 更新 Evidence Record；
2. Signal 标记 `PROMOTED`；
3. 链接 Evidence ID；
4. 后续事实维护归 Evidence Ledger。

### CONTRADICTED
有明确反证时保留 Signal 历史，不删除。记录为什么被推翻，以防旧传闻再次复活。

### 长期 unresolved
如果常规公开检索已经没有合理的信息增益，但该说法仍有解释价值，可长期保持 `WEAK_SIGNAL / UNVERIFIED`。**未晋级不是研究失败。**

---

## 10. 与 Case Graduation 的关系

存在未解决 Signal / H **不自动阻止 Case 进入 STABLE**。

真正的阻塞条件是：

- 该未知对核心 Verdict / Transfer 有实质影响；
- 仍存在合理、可执行的核验路径；
- 尚未完成该核验。

如果某传闻重要但基本不可恢复，应在 Case 中明确标记边界，而不是为了“毕业”删除或伪造确定性。

详见 [`case-graduation.md`](case-graduation.md)。


---

## 11. Decision Tempo / Value-of-Information Gate（与 Exam Overfit 032 共用）

在 WATCH / PROBE / HEDGE / ACT / NO_ACTION 之前，补充五个检查点：

1. `decision_urgency`：截止时间真由外部窗口决定，还是由会议/汇报制造？
2. `expected_information_value`：未来数小时/数日的调查、样本或原型，有没有实质可能改变决策？
3. `information_acquisition_cost`：搜集证据及等待损失分别是多少？
4. `reversibility`：先做可撤销试验是否比立即全面投入更好？
5. `stop_rule`：什么信息足以决定行动？什么反证足以撤销？

**不可把“回应速度”当“判断质量”；也不可把“继续调研”无条件当美德。**
当新增信息期望收益低于调查与延迟成本时，迅速做决定是合理的。

学理锚点：
- ISPOR 2020 VOI good practices：https://www.ispor.org/heor-resources/good-practices/article/value-of-information-analysis-for-research-decisions-an-introduction
- [中国032 / Section 28：决策节奏过拟合](../country-studies/china/032-exam-overfit-routine-expertise-open-domain-transfer.md)

这个Gate用于明确决策姿态与研究/等待成本，不会把Signal自动升级为Evidence。
