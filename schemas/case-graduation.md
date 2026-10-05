# Case Graduation / 结案与稳定化协议

本协议解决一个长期治理问题：**研究库不能只擅长开新 Case，还必须能够让成熟 Case 停止无限扩张。**

Case 的正式状态继续沿用现有体系，不新增第七、第八种状态：

```text
SKELETON → RESEARCHING → REVIEW → STABLE
```

其中 `REVIEW-READY` 只允许作为**派生判断**，不是 frontmatter 中的新正式状态。

---

## 1. Graduation 的目标

Graduation 不是“证明所有问题都已解决”，而是判断：

> 这个 Case 是否已经达到可引用、可进入书稿、可停止常规扩张研究的稳定程度？

STABLE 不等于永远不修改。出现重大反证、重要新一手材料、关键 Contributor / finance / chronology 错误时，可以：

```text
STABLE → REVIEW
```

然后重新核验。

---

## 2. 机器资格与人工裁决分开

### Machine eligibility

机器可以检查结构性硬门槛：

- Case / Evidence Ledger / metadata 都存在并互相指向；
- YAML / Schema 合法；
- `evidence_strength` 不为 LOW；
- Schema v2 案例的 Context–Situation–Action 已达到所需成熟度；
- Contributor / Market-access perimeter 已完成或明确标记 N/A / bounded unknown；
- 派生 metadata 没有漂移；
- 没有影响核心结论的未处理 source-maintenance blocker。

通过机器资格只能得到：

```text
REVIEW-READY
```

### Human / Agent adversarial review

正式进入 REVIEW / STABLE 前必须做一次压力测试：

1. 核心 Verdict 最强的替代解释是什么？
2. 有没有把相关性写成因果？
3. 有没有把成功后获得的优势倒推成成功前优势？
4. 有没有漏掉 hidden contributor / family support / publisher / platform support？
5. 有没有把今天的技术、市场或制度条件投射回当年？
6. 有没有幸存者偏差？
7. 如果商业结果相反，同样事实是否仍支持当前 Transfer？
8. 哪些关键句只靠一个来源，一旦该来源失效就失去支撑？
9. 重要未知是否已经正确分类：可继续核验、基本不可恢复、弱 Signal、H、或真正无关紧要？

机器不能替作者完成这一步。

---

## 3. 不采用总分制

不要给 Case 打“成熟度 82 分”。

Graduation 只显示：

```text
BLOCKED
NEEDS_RESEARCH
REVIEW_READY
STABLE
```

含义：

### BLOCKED
基础研究条件不足，例如：

- `SKELETON`；
- Evidence LOW；
- 缺 Ledger / metadata；
- Schema broken；
- 核心事实依赖已确认失效且尚未修复的来源。

### NEEDS_RESEARCH
基础结构成立，但仍有明确、可执行的研究缺口，例如：

- CSA 未闭合；
- Contributor perimeter 未审；
- Market-access audit 未审；
- material open question 仍有现实可核验路径；
- 缺少足以挑战核心解释的反方检查。

### REVIEW_READY
硬门槛已通过，继续无边界搜资料的边际收益已经较低，应停止扩张式 intake，进入 adversarial review。

### STABLE
人工 review 完成，正式状态被作者 / 维护者升级为 STABLE。

---

## 4. UNKNOWN / H / Signal 不自动阻止 STABLE

一个成熟历史 Case 可以合法保留：

```text
Known
Supported
Plausible but unresolved
Weak signal / oral history
Unknown and probably unrecoverable
```

STABLE 的关键不是“没有未知”，而是：

> **所有对核心解释有影响的未知都被正确分类，并且该查的已经查到合理边界。**

未解决项目只有同时满足以下条件时才阻塞：

1. 对核心 Verdict / Transfer 有实质影响；
2. 仍有合理、可执行、成本相称的核验路径；
3. 当前尚未完成。

如果一个传闻可能永远无法恢复，但已经清楚标为 Signal / H / UNKNOWN，就不应为了毕业而删除，也不应迫使 Case 永远停留 RESEARCHING。

详见 [`signal-decision-protocol.md`](signal-decision-protocol.md)。

---

## 5. Freshness 与 Graduation 分离

历史 Case 的稳定性与实时行业判断的时效性不是同一件事。

- 历史事实稳定，可长期 STABLE；
- 一个与 Case 相关的实时发行 / 平台 / 渠道判断可以同时需要较短 `Review by`；
- 不因为某个实时 Signal 过期，就自动把整个历史 Case 降级。

因此：

```text
Epistemic maturity ≠ temporal freshness ≠ decision posture
```

三者分别管理。

---

## 6. STABLE 后的修改门槛

STABLE Case 不再作为“任何新采访都继续塞进去”的开放容器。

默认只在以下情况重新修改：

1. 新 P0 / P1 材料显著修正已有结论；
2. Source Health 需要修复关键 Evidence；
3. Claim 关系发生实质变化；
4. 发现重要 Contributor / finance / chronology 错误；
5. 出版 / 翻译核验发现事实边界问题；
6. 新反证足以使核心 Verdict 需要重审。

重复性访谈、已经知道的数字、没有改变任何判断的新表述，默认不进入 STABLE Case。

---

## 7. Owner 与传播规则

沿用本仓库的 single-owner 原则：

```text
Evidence Ledger = 来源事实 Owner
Case = 个案综合解释 Owner
Claim = 跨案例命题 Owner
Signal = 弱线索 Owner
Book profile = 读者叙事视图
```

Graduation 不改变这些 Owner。

如果一个 Case 升为 STABLE：

- 不把结论全文复制进 README / profile / thesis；
- 下游只链接 Case / Claim；
- Reader layer 可以重述，但不得产生新的 canonical facts。

---

## 8. 建议的 Graduation Review 输出

每次人工 review 只需要一份短记录：

```markdown
# Graduation Review — CASE-XXX

- Date:
- Reviewer:
- Machine eligibility: PASS / FAIL
- Proposed formal status: REVIEW / STABLE / REMAIN RESEARCHING

## Core verdict pressure test
- Strongest alternative explanation:
- Survivor-bias check:
- Hidden-support check:
- Anachronism check:

## Material unknowns
- Still actionable to verify:
- Probably unrecoverable:
- Weak Signals / H retained:

## Source fragility
- Single-source critical claims:
- Dead / archived / restricted sources:

## Decision
- What changes before graduation:
- What is explicitly allowed to remain unknown:
```

Review 记录是审计历史，不是新的 Case 主档。

---

## 9. 对治理 KPI 的影响

以后不要只统计：

```text
33 Cases
12 Claims
```

还应同时看：

```text
SKELETON
RESEARCHING
REVIEW
STABLE
REVIEW-READY (derived)
```

以及主要研究债：

- Evidence LOW；
- CSA incomplete；
- Contributor incomplete；
- Market-access incomplete；
- material source-maintenance blockers；
- material open questions with an actionable verification path。

目标不是追求固定毕业率，而是防止研究系统无限 intake、永不收口。
