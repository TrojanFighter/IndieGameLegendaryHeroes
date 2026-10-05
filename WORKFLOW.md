# WORKFLOW

本仓库把工作拆成三条车道：

- **Library Operations / 库运维**：schema、metadata、lint、CI、README、Case Explorer、source health、build。
- **Case Research / 案例研究**：Case、Evidence、Claim、Contributor / Market-access / CSA audits、反例与 comparator。
- **Editorial / Book Layer**：reader profiles、书级 thesis、TOC 与成书。

详细边界与 handoff contract 见：[`schemas/workflow-lanes.md`](schemas/workflow-lanes.md)。

默认原则：**库运维不替案例研究补历史事实；案例研究不顺手改 schema/lint；书稿不创造 canonical facts。**

## Issue Intake

公开输入统一走 GitHub Issue chooser，而不是空白 issue。当前四类：

1. **Case 纠错**：修正已有事实、口径、时代条件或因果外推；
2. **新增 Evidence**：给已有 Case 提供可追溯来源，并明确它直接支持什么、不能证明什么；
3. **候选 Case**：提出新案例，同时给出生产史解释价值、初步 CSA 与至少一个可核验来源；
4. **库流程 / 工具问题**：schema、metadata、lint、CI、README、Explorer、source health、build 等 Lane A 问题。

入口：<https://github.com/TrojanFighter/IndieGameLegendaryHeroes/issues/new/choose>

Issue 只是 intake，不自动成为 canonical fact。进入 Case / Evidence / Claim 仍需 Lane B 核验。

## Source Health

外部来源可达性由 [`tools/check_source_health.py`](tools/check_source_health.py) 与 Source Health workflow 维护。状态定义与边界见 [`schemas/source-health.md`](schemas/source-health.md)。

Live check 会在两种情况下运行：

- 每周一的定时维护；
- `main` 上 `evidence/**`、Source Health 脚本 / schema / workflow 发生变化后。

PR 阶段只做 URL extraction smoke test，不主动访问外站。

Source Health **不阻断 merge，也不自动修改 Evidence**。404/410、重定向、访问受限和临时网络故障只作为维护信号；来源内容是否仍然支持原 Evidence，仍需人工 / Lane B 复核。

## Case Explorer

[`explorer/index.html`](explorer/index.html) 是研究 corpus 的只读浏览视图。它运行时直接读取：

- `metadata/cases.json`
- `metadata/claims.json`

不维护第二份 Case / Claim 事实。当前支持搜索、tags、research status、explanatory importance、Contributor audit、Market-access audit、CSA 状态与 Claim 关系。

本地使用与 v0 边界见 [`explorer/README.md`](explorer/README.md)。当前不为了 UI 完整而给 Schema v1 老案例补 CSA；`CASE-001`～`CASE-026` 未迁移时显示 `legacy-v1`。

Explorer 依赖的 metadata contract 由 [`tools/explorer_lint.py`](tools/explorer_lint.py) 在 CI 中检查；UI 不得硬编码 CASE ID 形成第二份手工数据库。

## Obsidian Compatibility

仓库可以直接作为 Obsidian Vault 打开，但 Obsidian 只作为本地阅读、编辑和关系探索层，不成为 canonical facts 或 machine metadata 的来源。

边界与推荐设置见 [`docs/OBSIDIAN-COMPATIBILITY.md`](docs/OBSIDIAN-COMPATIBILITY.md)。当前原则：

- `.obsidian/` 作为个人本地状态忽略；
- 标准 Markdown links 优先于大量 `[[wikilink]]`；
- 不为 Dataview / Bases 人工复制 `metadata/*.json`；
- 暂不引入 Obsidian 插件作为仓库读取前提。

## Repository Hygiene

[`branch-hygiene.yml`](.github/workflows/branch-hygiene.yml) 在 `main` 每次更新后清理已经完全合并且没有 open PR 的 `chatgpt/*` 分支。

它只处理同时满足以下条件的分支：

1. 分支名以 `chatgpt/` 开头；
2. 所有提交已经进入 `main`；
3. 当前没有 open PR 使用该分支。

这解决 merged working branches 的积累问题，但**不等价于 main branch protection**。分支保护 / ruleset 仍属于 GitHub repository-admin 设置，应单独开启 required PR + `research-lint`，而不是依赖 workflow 模拟。

## Lane A 常用维护命令

### 完整本地检查

```bash
python tools/research_lint.py --strict
python tools/research_evidence_lint.py
python tools/context_audit_lint.py
python tools/reader_layer_lint.py
python tools/explorer_lint.py
```

不要因为某项检查失败就放宽规则；先判断是 canonical 数据错、派生数据漂移，还是工具本身需要修正。

### 刷新派生统计

`metadata/research-stats.json` 不是独立事实源，而是从 `metadata/cases.json` 与 `metadata/claims.json` 计算出的 snapshot。

当 Case / Claim 数量、状态或评级变化后运行：

```bash
python tools/research_lint.py --write-stats
python tools/research_lint.py --strict
```

不要手工重算 `research-stats.json`；CI 会拒绝 stale snapshot。

### 本地打开 Case Explorer

```bash
python -m http.server 8000
```

然后访问：

```text
http://localhost:8000/explorer/
```

### 手动 Source Health

常规健康检查由 GitHub Actions 执行。需要本地排查时，优先查看 `tools/check_source_health.py --help`，不要把网络失败直接写回 Evidence 的 verification status。

## PR 交接

### 姊妹篇目录与检查

独立篇保留根目录 `cases/`、`claims/`、`evidence/` 和 `book/`；斯拉夫篇使用 [sister-projects/slavic/](sister-projects/slavic/README.md)。共享 schemas、来源规则和工具，分别登记资料与统计；根目录 Case Explorer 仍只消费独立篇 metadata。

`python tools/slavic_research_lint.py` 校验姊妹篇归属、编号、并行稿登记与链接。来源健康检查按篇运行：

```powershell
python tools/check_source_health.py --evidence-dir evidence --list-only
python tools/check_source_health.py --evidence-dir sister-projects/slavic/evidence --list-only
```

专题档案不自动成为 Case，Profile 不复制研究账本。英文译文开始建立时在对应篇的 `translations/en/` 中维护，不混入另一篇的译文索引。

公开研究隔离规则、本地提交/推送检查和 GitHub 门禁设置见 [公开研究与私人项目隔离](docs/public-research-boundary.md)。每次 PR 必须检查私人信息的上下文映射，自动词表检查不能代替语义审阅。

新 PR 默认使用 [`.github/pull_request_template.md`](.github/pull_request_template.md)。

模板的作用不是增加审批负担，而是把已经反复出现的三件事显性化：

1. 这次属于哪条 Lane；
2. 是否改变 canonical facts；
3. 哪些问题明确留给下一条 Lane / 后续任务。

一个 PR 原则上只承担一条 Lane。跨 Lane 不是禁止，但必须说明为什么不能拆分。

## 公开贡献与双语检查

新贡献按 [CONTRIBUTING.md](CONTRIBUTING.md) 使用独立公开上下文、单任务分支和实际差异审阅。英文入口见 [translations/en/README.md](translations/en/README.md)。译文版本与人工审阅规则见 [双语维护](docs/bilingual-maintenance.md)；运行 `python tools/translation_lint.py` 检查登记、源版本、ID 与本地链接。

### Obsidian 只读使用与本地状态

- 打开仓库根目录作为现有 Vault，不再在仓库内新建嵌套 Vault。
- 在设置的 Editor / 编辑器中将默认视图设为 Reading view / 阅读视图，避免误触编辑；这不是文件权限层面的只读锁。
- `.obsidian/` 的工作区、浏览状态和个人设置不提交。默认欢迎笔记也不进入研究库；个人笔记放在仓库外的个人 Vault。
- Markdown 由 `.gitattributes` 固定为 LF，避免 Obsidian 保存 LF 与 Windows Git 预期 CRLF 不一致造成空差异。
- 若 Git 列出改动却没有差异，先核对原始内容，再刷新 Git 状态；不要直接批量丢弃。若存在真正的正文差异，照正常研究修改审阅。
- Git 忽略规则仅控制提交，不保证操作系统、Obsidian 或同步服务没有阅读记录。需要完全隔离阅读与编辑时，在仓库外使用独立阅读副本，并独立管理同步。

每个新 clone 首次使用，以及出现 `No content changes found` 时：

```powershell
python tools/worktree_eol.py
python tools/worktree_eol.py --repair
```

修复会先检查暂存区和所有 tracked 文本内容；发现真实差异即停止。通过检查后仅统一工作树换行为 LF，并设置本仓库 `core.autocrlf=false`、`core.eol=lf`、`core.checkstat=minimal`、`core.trustctime=false`、`core.ignorestat=false`。随后刷新等价文件索引，不提交、不添加未跟踪文件。不要使用 `assume-unchanged` 或 `skip-worktree` 隐藏正文修改。

`.gitattributes` / `.editorconfig` 是共享规则，本地 Git 配置不随 clone 复制。共享修复须合入正在使用的分支才生效；仅推送 PR 不等于 main 已获得修复。阅读视图和 EditorConfig 均不能保证编辑器完全不写盘。
