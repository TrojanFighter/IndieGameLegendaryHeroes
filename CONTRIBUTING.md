# 贡献与提交流程

[English](translations/en/CONTRIBUTING.md) · [双语维护](docs/bilingual-maintenance.md)

本仓库研究开发者与小团队的生产条件。优先贡献事实纠错、来源、时间线、反例与证据指针；遵守 [AGENTS.md](AGENTS.md) 的证据等级和禁止外推规则。

研究对象的权威顺序与唯一 Owner 见 [Research Authority / Ownership Map](schemas/research-authority-map.md)。弱口述、传闻、作者记忆和未索引线索见 [Signal / Decision-Posture Protocol](schemas/signal-decision-protocol.md)。

## 开始工作

1. 从最新、已清理的 `origin/main` 建立单一任务分支；旧分支先检查完整新增历史，不直接合并。
2. 为公开研究使用独立对话，只加载本仓库与公开来源。不要续用混合私人项目上下文的对话。
3. 先区分输入类型：可追溯事实进入 Evidence；弱口述 / 传闻进入 Signal；作者解释标 H / Author-Origin；不要直接把输入写成 Claim。
4. 先写 Case / Evidence / Claim，再写摘要或读者层。没有来源的内容保留 UNKNOWN；推断标为 H。
5. 不导入私人项目的文件、对话、路径、预算、人员、计划或设计；去名称和改写都不能使其成为公开来源。

可复制给研究代理的任务范围：

> 只处理本公开研究仓库。只使用公开可核验来源与仓库内研究材料。不得读取或映射私人项目。先记录证据与不确定性，再写判断。弱信号不得自动升级为 Evidence。通用 Transfer 面向未指定的开发者群体，不指导任何私人项目当前执行。

## 弱信号 / 口述 / 传闻

如果一条信息值得继续核验，但暂时没有达到 Evidence 门槛：

- 使用 GitHub Issue 的“弱信号 / 口述 / 传闻”入口，或按 `SIG-XXX` 记录到 `sources/research-intake/signals/`；
- Signal 可以改变核验优先级，不能直接提升 Case `evidence_strength` 或 Claim 状态；
- 对高时效问题可以记录 `WATCH / PROBE / HEDGE / ACT / NO_ACTION`，但这只是可审计建议姿态，不是事实状态，也不自动触发行动；
- 未授权私人信源身份、私聊原文、截图、合同、可反推身份的细节不得进入公开仓库。

## 提交前

- 阅读实际修改，而非只读生成摘要：关键事实有来源，金额、团队人数、开发起点的口径清楚；UNKNOWN、H、Signal、反方证据没有被润色掉。
- 检查匿名化的私人内容，以及“所以我们的项目现在应该……”这类映射。
- 只暂存本任务文件，检查暂存差异与提交消息，避免夹带其他研究或书稿改动。
- 按 [隔离规则](docs/public-research-boundary.md) 安装本地钩子并运行 `python tools/private_content_guard.py --staged`；缺词表必须修复，不绕过检查。
- 运行本次改动相关的研究检查；译文运行 `python tools/translation_lint.py`。
- 推送前本地钩子会检查新增历史。GitHub 检查发生在上传之后，因此不能代替本地检查。

## PR 与其他公开载体

按 PR 模板说明范围、证据和检查结果。逐项人工检查 PR 标题、正文、Issue、评论、截图、附件及外链；本地词表钩子不覆盖这些载体。不要公开私有词表、命中原文、污染历史备份或审计原始数据。

自动检查只是一层防错。名称扫描通过不代表匿名私人信息不存在；行业词汇单独出现不构成泄露。

## Case 收口

`REVIEW-READY` 只是一项派生机器资格，不是新的正式 Case 状态。机器不得自动把 Case 升级为 `REVIEW` 或 `STABLE`。

正式结案前按 [Case Graduation](schemas/case-graduation.md) 做 adversarial review。Case 可以带着明确分类的 UNKNOWN / H / weak Signal 进入 STABLE；真正阻塞的是对核心解释有实质影响、且仍有合理核验路径但尚未处理的问题。

## 翻译与权利

中文原文及其 Case / Evidence / Claim 是研究依据；英文沿用同一 ID，不创建另一份事实账本。按 [双语维护](docs/bilingual-maintenance.md) 登记译文状态和原文版本。

公开研究、正式书稿和第三方材料的权利分别遵守 [LICENSE-CONTENT](LICENSE-CONTENT)。官方翻译须由维护者授权；第三方翻译投稿须另行确认发布许可，不能从 CC BY-NC-ND 推定衍生作品已获授权。投稿不自动授权未来商业书稿使用贡献者的原创文字。