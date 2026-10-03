# Machine-readable Research Metadata

本目录把《独立游戏英雄传说》的研究状态暴露给脚本、搜索、未来 AI skill 和统计工具。

## Canonicality

- **研究事实与论证正文**：仍以 `cases/`、`claims/`、`evidence/` 中的 Markdown 为准。
- **机器索引**：`cases.json` 与 `claims.json` 只保存 ID、状态、关系、标签、解释重要性与叙事价值等结构字段。
- metadata 不得复制整段 Evidence 或把推断写成新事实来源。
- metadata 与 Markdown 不一致时，必须修正并通过 lint；不能默默接受漂移。

## 为什么分开 Evidence Strength / Explanatory Importance / Narrative Value

这三个轴故意正交：

- `evidence_strength`：当前证据有多成熟；
- `explanatory_importance`：如果成立，对“为什么这个项目/开发者能做成”的解释力有多大；
- `narrative_value`：未来成书时是否值得展开为有阅读价值的故事。

一个事实可以非常确定但解释力很低；一个母题也可以对全书极重要但长期处于 CONTESTED。

## 当前机器快照

- Cases: 6
- RESEARCHING: 1
- SKELETON: 5
- REVIEW: 0
- STABLE: 0
- Claims: 12
- UNVERIFIED: 12

这些数字只是当前快照。未来应由脚本计算，不应手工作为研究结论引用。

## Lint

运行：

```bash
python tools/research_lint.py --strict
```

CI 会自动运行同一检查。

当前第一版分两层：

### Error — 阻止 CI

- Case / Claim ID 重复；
- 非法 status / importance 枚举；
- metadata 指向不存在的文件；
- Case header 与 registry 的 ID / status / Related Claims 不一致；
- Claim README 表与 registry 的 ID / status 不一致；
- Related Cases / Related Claims 指向不存在对象；
- Case ↔ Claim 关系不对称；
- VERIFIED Claim 没有任何 Evidence ID；
- STABLE Case 仍有 TODO；
- REVIEW / STABLE Case 没有 Evidence Ledger。

### Warning — 当前允许通过

- solo / 一人开发案例仍没有完成 contributor / external support audit；
- zero marketing / organic hit 叙事仍没有完成 Market Access 拆解；
- SKELETON 长期没有 Evidence Ledger；
- 重要字段仍为空。

原则：**结构错误要立即失败；研究尚未完成要显式暴露，但不能因为项目仍在研究期而让 CI 永久红灯。**
