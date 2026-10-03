# Machine-readable Research Metadata

本目录把《独立游戏英雄传说》的研究状态暴露给脚本、搜索、统计工具与未来 AI skill。

## 两层结构

- **人读正文层**：`cases/`、`claims/`、`evidence/` 中的 Markdown。事实、论证、边界与证据解释以这些文件为准。
- **机器索引层**：`cases.json`、`claims.json`、`research-stats.json`。只保存 ID、状态、关系、标签、证据成熟度、解释重要性与叙事价值等结构字段。

不要求 Case/Claim 正文使用 YAML frontmatter。机器层与正文层是 sidecar 关系：正文负责研究内容，metadata 负责索引和一致性检查。

如果两层冲突，必须显式修正；不能默默接受漂移。

## 三个正交评分轴

### `evidence_strength`

当前证据有多成熟：

- `none`
- `low`
- `medium`
- `high`

它只表示证据成熟度，不表示命题有多重要。

### `explanatory_importance`

如果该判断成立，它对“为什么这个开发者 / 团队能把项目做成”解释了多少：

- `unrated`
- `low`
- `medium`
- `high`
- `critical`

### `narrative_value`

未来正式书稿中，这个 Case / Claim 是否值得展开成读者可感知的生产史：

- `unrated`
- `low`
- `medium`
- `high`
- `critical`

一个事实可以证据极硬但解释力很低；一个母题也可以对全书极重要但长期处于 CONTESTED。

## Canonical machine indexes

- `cases.json`：所有 `cases/CASE-*.md` 必须且只能登记一次。
- `claims.json`：所有 Claim ID、状态、反向 Case 关系必须登记。
- `research-stats.json`：由 lint 从前两者计算，不手工编造。

Case ↔ Claim 关系必须双向一致。

## Lint

本地检查：

```bash
python tools/research_lint.py --strict
```

更新统计快照：

```bash
python tools/research_lint.py --write-stats
```

GitHub Actions 会运行 `--strict`。

### Error — 阻止 CI

- Case / Claim ID 重复；
- 非法 status / rating；
- metadata 指向不存在的 Markdown / Evidence Ledger；
- `cases/README.md` 或 `claims/README.md` 与 metadata 状态漂移；
- Case 正文 `Related Claims` 与 metadata 不一致；
- Related Cases / Related Claims 指向不存在对象；
- Case ↔ Claim 关系不对称；
- SUPPORTED / VERIFIED Claim 缺少最低 Evidence 记录；
- VERIFIED Claim 的 `evidence_strength` 不是 `high`；
- REVIEW / STABLE Case 没有 Evidence Ledger；
- STABLE Case 仍含 TODO；
- `research-stats.json` 过期。

### Warning — 当前允许通过

- 已进入研究阶段但证据成熟度仍低；
- REFUTED Claim 尚未登记 Evidence ID；
- 正文缺少可供人读的 Related Claims 行。

原则：**结构错误立即失败；研究尚未完成则显式暴露，但不能因为仍在研究期让 CI 永久红灯。**

## 当前快照

不要手抄数字到这里。需要统计时读取 `research-stats.json` 或运行 lint；这样不会出现 README 数字与实际仓库长期漂移。
