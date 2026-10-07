# Machine-readable Metadata Conventions

本文件定义研究仓库中供人类与机器共同读取的最小元数据约定。目标是：**同一份 canonical Markdown 同时服务阅读、检索、lint 与未来 AI skill，不建立平行数据库。**

## 1. Case frontmatter

所有 `cases/CASE-*.md` 建议以 YAML-compatible frontmatter 开头；Schema v2 Case 必须有 frontmatter。

Schema v1 的最小字段：

```yaml
---
type: case
case_id: CASE-001
status: RESEARCHING
subject: "FTL / Subset Games"
related_claims: [C001, C002]
evidence_strength: MEDIUM
explanatory_importance: HIGH
narrative_value: HIGH
last_verified: 2026-10-03
---
```

从 `CASE-027` 起，新建 Case 使用 Schema v2：

```yaml
---
type: case
schema_version: 2
case_id: CASE-027
status: RESEARCHING
subject: "Example / Studio"
related_claims: []
evidence_strength: MEDIUM
explanatory_importance: HIGH
narrative_value: HIGH
context_audit: PENDING
last_verified: 2026-10-04
---
```

Schema v2 在 `metadata/cases.json` 中同时登记：

- `schema_version`: `2`
- `context_audit`: `pending` / `partial` / `complete`

`CASE-001`–`CASE-026` 是历史 Schema v1 Case，不要求库运维任务批量补事实。它们应在后续专门案例研究时逐案迁移。

允许的 `status`：

- `SKELETON`
- `RESEARCHING`
- `REVIEW`
- `STABLE`

允许的三项评分：

- `UNRATED`
- `NONE`
- `LOW`
- `MEDIUM`
- `HIGH`

`last_verified` 使用 `YYYY-MM-DD`；尚未真正核验时用 `null`。

### Creator life audit

当 Case 被用于“人生性价比 / 读者处境匹配”时，可在 Case 正文记录 `Creator Life / Decision Audit`。当前不要求把 household 事实复制进 `metadata/cases.json`，避免形成第二份事实源。

机器索引如需记录，只允许记录覆盖率状态，而不得复制：
- spouse income；
- mortgage；
- children；
- savings；
- household burn；
- personal health / family detail。

Canonical facts 始终保留在 Case / Evidence Markdown。

完整字段见 [`creator-life-decision-audit.md`](creator-life-decision-audit.md)。

### Context audit

`context_audit` 专门回答：**这个 Case 是否已经把关键行动放回当时的时代技术条件和作者具体处境中审计？**

- `pending`：尚未专门恢复 production regime / actor situation；
- `partial`：至少一个关键转折完成 CSA，但仍有主要缺口；
- `complete`：主要生产转折已经完成 Context–Situation–Action 审计与时代差异检查。

详细定义见 [`context-situation-action.md`](context-situation-action.md)。

所有 Schema v2 Case 在进入 `REVIEW` 或 `STABLE` 前必须为 `complete`。

## 2. 三个评分必须正交

### Evidence Strength

回答：**目前支持这个 Case / Claim 关键判断的证据有多强？**

它与 P0/P1/S1/S2 来源等级有关，但不是简单按“来源数量”自动换算。

- `NONE`：基本还是问题骨架 / 假说。
- `LOW`：只有少量弱来源或关键事实未打通。
- `MEDIUM`：已有多条可追溯来源，核心时间线或机制得到一定支持，但仍有重要缺口。
- `HIGH`：关键事实得到强证据与交叉核验，主要反例已主动检查。

### Explanatory Importance

回答：**如果当前判断成立，它对“为什么这个项目能被做出来 / 做完 / 被市场看见”的解释力有多大？**

它不是事实置信度。一个只有 `MEDIUM` Evidence Strength 的机制，可能有 `HIGH` Explanatory Importance。

### Narrative Value

回答：**这个材料在最终书稿中是否值得占据较多叙事空间？**

它也不是事实置信度。传奇性、冲突性或可读性不得反向提升 Evidence Strength。

## 3. 禁止的自动推导

任何模型 / 脚本不得自动做以下推导：

- 来源多 → Explanatory Importance 高；
- 名气大 → Narrative Value 高；
- Narrative Value 高 → Claim 更可能成立；
- P0 多 → 自动 `VERIFIED`；
- 某个 Case 证据丰富 → 自动成为全书中心；
- 年代更晚 → 技术条件必然更有利；
- 某项技术已经存在 → 该作者当时必然可负担、可获得、会使用。

评分与 CSA 都是研究判断，必须允许后续修订。

## 4. Claim 元数据

当前 Claim 仍以 `claims/README.md` 为 canonical index，不复制第二份 JSON/YAML 注册表。

Claims Index 的表格列固定为：

1. Claim ID
2. 暂定命题
3. 状态
4. Evidence Strength
5. Explanatory Importance
6. Narrative Value

当某个 Claim 发展为独立长档案时，使用 `schemas/claim-template.md` 的 frontmatter。

## 5. Evidence 与 aggregate rating 的区别

单条 Evidence 继续使用 `P0 / P1 / S1 / S2 / H` 与 verification status；`Evidence Strength` 是 Case / Claim 层面的综合判断。

不要把二者混为一个字段。

`context_audit` 也不是 Evidence Strength：一个案例可能有很强的来源，却仍没有把这些来源组织成完整的时代—处境—行动审计。

## 6. Canonical rule

- Case 的正文与 frontmatter 在同一个 Markdown 文件中。
- `metadata/cases.json` 是 Case 的机器索引，不得变成第二份叙事事实源。
- Claim 当前以 `claims/README.md` 为 canonical registry。
- lint 只读取 canonical 文件与机器索引，不维护一份手工同步的影子研究数据库。
- 未来若生成网页、搜索索引、PDF、EPUB 或 AI skill，应从这些 canonical 文件派生，而不是反向成为事实源。
- 任何 schema migration 若需要补历史事实，必须交给案例研究流程；库运维只能标记缺口，不能靠常识填充。
