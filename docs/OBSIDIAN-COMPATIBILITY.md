# Obsidian Compatibility Layer

本仓库可以直接作为 Obsidian Vault 打开，但 Obsidian 只是本地阅读、编辑与关系探索界面，不是事实源。

## 使用方式

在 Obsidian 中选择 **Open folder as vault**，打开仓库根目录即可。

当前推荐目标是 **Obsidian-friendly, not Obsidian-dependent**：

- GitHub / Git / Markdown 仍是项目正本；
- `metadata/*.json` 仍是 Case / Claim 的 canonical machine index；
- Case / Evidence / Claim / Profile / Thesis 关系继续使用标准 Markdown 与现有 metadata 表达；
- Obsidian backlinks / graph 只用于发现关系，不构成证据；
- 关闭 Obsidian 后，仓库仍必须完整可读、可 lint、可被 Agent 使用。

## 当前约束

### 不追踪本地 Obsidian 状态

`.obsidian/` 被 `.gitignore` 忽略。工作区布局、主题、插件、快捷键等属于个人本地状态，不进入仓库。

### 标准 Markdown 链接优先

优先使用 GitHub 也能理解的标准 Markdown links，例如：

```md
[CASE-007 Gunpoint](../cases/CASE-007-gunpoint.md)
```

暂不要求把仓库改成大量 `[[wikilink]]`。

### 不建立第二套 metadata

不要为了 Dataview / Bases 在 YAML frontmatter 中复制以下 canonical 字段：

- Case status
- related Claims
- evidence strength
- audit state
- CSA status
- tags

如果未来确有需要，应优先从 `metadata/cases.json` / `metadata/claims.json` 生成 view，而不是人工双写。

### 暂不引入插件依赖

当前不要求：

- Dataview
- Bases
- Templater
- Tasks
- QuickAdd
- Obsidian Git
- Digital Garden / Publish

只有当真实使用证明某项能力持续有价值，而且无法被现有 Explorer / Markdown / scripts 更简单地满足时，再进入 Lane A 评估。

## Obsidian 与 Case Explorer 的分工

- **Case Explorer**：结构化过滤、audit 状态、Claim 关系、metadata 视图。
- **Obsidian**：快速打开、backlinks、graph、跨文档阅读与写作。

两者都消费同一套 canonical corpus，不互相复制数据库。

## 未来可能升级的方向

只有在真实使用后再考虑：

1. 生成式 MOC（Runway / Market Access / Taste Capital / Failure Comparator 等）；
2. 更密的标准 Markdown cross-links；
3. 从 canonical metadata 生成 Obsidian-friendly view；
4. 对 `.obsidian/` 只追踪极少数真正团队共享的配置。

这些都不是当前要求。

## 失败条件

如果 Obsidian 化开始导致以下任一情况，应回退：

- canonical metadata 出现第二份手工副本；
- 只有装特定插件才能读懂核心知识；
- GitHub / Agent 读取体验变差；
- 大量维护时间花在 graph / tag / Canvas 美化，而不是研究与出版；
- wikilink / plugin syntax 让普通 Markdown 兼容性下降。
