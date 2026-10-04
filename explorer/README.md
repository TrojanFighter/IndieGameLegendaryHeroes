# Case Explorer v0

这是《独立游戏英雄传说》的**研究浏览视图**，不是新的事实数据库。

## Canonical source

Explorer 只消费：

- `metadata/cases.json`
- `metadata/claims.json`

页面本身不得手工维护：

- Case 名单；
- Claim 文本；
- research status；
- evidence strength；
- audit status；
- tags；
- Case / Evidence 路径。

如果页面和 metadata 冲突，以 metadata 为准。

## 当前能力

v0 支持：

- Case / 人物 / 团队全文搜索；
- tag 搜索与点击过滤；
- research status；
- explanatory importance；
- contributor audit；
- market-access audit；
- Context / CSA audit 状态；
- related Claims 与 Claim status；
- 直接进入 Case 和 Evidence Ledger。

当前 `CASE-001`～`CASE-026` 大多仍是 Schema v1，因此 CSA 会显示 `legacy-v1`。这不是数据错误，也不能由 Lane A 为了页面完整而批量补历史事实。

## 本地使用

推荐在仓库根目录启动静态服务器：

```bash
python -m http.server 8000
```

然后打开：

```text
http://localhost:8000/explorer/
```

如果直接双击 `index.html`，部分浏览器会禁止 `file://` 页面读取相邻 JSON。页面会尝试回退到 GitHub `main` 的 raw metadata；这只适合快速浏览，不适合预览尚未合并的分支数据。

## 为什么现在不直接开 GitHub Pages

当前仓库 Pages 尚未启用。v0 先验证两个问题：

1. 这些过滤维度是否真的帮助研究与编辑；
2. metadata contract 是否稳定到足以长期作为公开界面。

只有实际使用证明有价值后，再单独做 Pages / deployment。不要让部署基础设施先于真实消费需求。

## 下一阶段

随着 Schema v2 案例增长，Explorer 才逐步增加：

- Era / Production Regime；
- Actor Situation；
- Binding Constraint；
- Action / Maneuver；
- Decision Units；
- reader profile availability；
- source-health state。

这些维度必须来自 canonical metadata / Case audits，不得为 UI 方便在 Explorer 内单独发明 taxonomy。
