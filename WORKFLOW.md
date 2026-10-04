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

外部来源可达性由 [`tools/check_source_health.py`](tools/check_source_health.py) 与每周 workflow 维护。状态定义与边界见 [`schemas/source-health.md`](schemas/source-health.md)。

Source Health **不阻断 merge，也不自动修改 Evidence**。404/410、重定向、访问受限和临时网络故障只作为维护信号；来源内容是否仍然支持原 Evidence，仍需人工 / Lane B 复核。
