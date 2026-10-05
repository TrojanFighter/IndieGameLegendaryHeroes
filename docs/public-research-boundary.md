# 公开研究与私人项目隔离

本仓库只接收公开行业案例、公开来源和可独立表达的通用概念。私人项目不得成为案例、比较对象、应用目标或语料来源。对话去名称、摘要或泛化，不能代替公开来源审查。

## 内容审阅

每次提交与 PR 确认：

- 案例选择来自行业研究问题，不是私人项目的竞品或执行需要。
- 新事实可回指公开来源；历史行业对话只提供线索，不提供事实权威。
- 无私人项目名称、路径、角色、技术架构、预算、人员、谈判或执行计划。
- 无“因此我们的项目当前应当……”的私人应用段落。
- 行业通用概念保留；普通发行、融资、团队规模等词不单独判定为泄露。

## 私有词表

JSON 结构为 `{"deny": ["<高置信私有标识>"], "review": ["<需上下文判断的词>"]}`，示例中的占位符不能用于正式配置。

真实词表保存在仓库外的受限文件，或 GitHub Actions Secret `PRIVATE_CONTENT_RULES` 中。不能提交词表、真实私有词测试样例、命中原文或包含它们的审计报告。缺失或无效词表导致检查失败。

`deny` 命中阻断；`review` 命中只输出位置与规则编号，须人工判断。输出不包含命中原文，文件路径中的匹配词也会遮蔽。审阅者通过本地私有词表识别编号，不在公开 PR 中粘贴词表。

## 本地检查与安装

以下 `<仓库外词表路径>` 替换为本机私有 JSON 文件的绝对路径：

```bash
python tools/private_content_guard.py --rules <仓库外词表路径> --worktree
python tools/private_content_guard.py --rules <仓库外词表路径> --staged
python tools/private_content_guard.py --rules <仓库外词表路径> --range <base-sha>..<head-sha>
python tools/install_private_content_hooks.py --rules <仓库外词表路径>
```

安装只写本地 Git hooks，不覆盖已有 hook 或 `core.hooksPath`。已有自定义 hook 时需人工接入。安装后：

- `pre-commit` 检查完整暂存快照和文件路径。
- `commit-msg` 检查待提交的消息。
- `pre-push` 检查每条推送新增的所有 commit 快照和消息，包括合并带入的提交。

新远端分支从完整可达历史检查，因此带有既有污染历史的分支会被阻止。不要通过关闭 hooks 来绕过；历史清理需独立备份、精确重写和验证。缺失远端基准对象时应先 fetch，再重试。

## GitHub 检查

将与本地相同的 JSON 配置为 Actions Secret `PRIVATE_CONTENT_RULES`。合并检查器与 workflow 到目标分支后，`public-research-boundary` 使用可信 base 版本的扫描器，读取 PR 对象，逐一检查新增 commits；不会 checkout 或执行 PR 代码。检查器/工作流的修改本身也需要人工审阅。

此工作流使用 `pull_request_target` 来支持 fork PR 的受限配置。它只有 contents/read 权限，不在日志或产物中输出私有词表。缺失 Secret 时检查失败。配置分支规则将 `private-content-guard` 设为必需，并禁止绕过 PR 直接写入发布分支，才能形成远端强制门禁。workflow 文件尚未合并时，不应声称门禁已在远端生效。

自动词表检查不能发现所有无名称的私人信息，不能证明完整历史已清理。历史 scrub 还要单独检查所有 branches、tags、PR refs 及旧 SHA 的服务端可访问性。

## 检查器验证

```bash
python -m unittest discover -s tests -p test_private_content_guard.py
```

测试仅使用虚构标识，不嵌入真实私人项目词表。
