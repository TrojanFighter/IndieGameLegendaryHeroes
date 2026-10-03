# Machine-readable Metadata Conventions

本文件定义研究仓库中供人类与机器共同读取的最小元数据约定。目标是：**同一份 canonical Markdown 同时服务阅读、检索、lint 与未来 AI skill，不建立平行数据库。**

## 1. Case frontmatter

所有 `cases/CASE-*.md` 必须以 YAML-compatible frontmatter 开头。

最小字段：

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
- 某个 Case 证据丰富 → 自动成为全书中心。

评分是研究判断，必须允许后续修订。

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

## 6. Canonical rule

- Case 的正文与 frontmatter 在同一个 Markdown 文件中。
- Claim 当前以 `claims/README.md` 为 canonical registry。
- lint 只读取 canonical 文件，不维护一份手工同步的影子数据库。
- 未来若生成网页、搜索索引、PDF、EPUB 或 AI skill，应从这些 canonical 文件派生，而不是反向成为事实源。
