# 中英文文档维护

中文研究原文保留现有路径；英文内容放在 `translations/en/`，共享 Case / Claim / Evidence ID。英文入口见 [README](../translations/en/README.md)，贡献指南见 [CONTRIBUTING](../translations/en/CONTRIBUTING.md)。

## 一个研究依据，两套阅读入口

- 中文 Case / Evidence / Claim 是 canonical research；译文不得新增事实、补齐 UNKNOWN、提升证据等级或删除反方证据。
- 英文入口是面向读者的导航摘要，不声称逐句覆盖中文 README；全文译文需完整保留段落结构和研究边界。
- 首批只做英文入口、贡献指南和 CASE-001 FTL 试点。其研究状态仍为 RESEARCHING / FIRST EVIDENCE PASS。
- 未翻译的 Evidence / Claim 链接明确指回中文资料，不生成英语影子账本。
- 页面按语言分开；术语表允许双语对照。原文与译文互链，避免读者误认英文覆盖全部资料。

## 版本与状态

`translations/manifest.json` 保存 source、target、doc_id、kind、source_sha256、status 与 reviewer。

- DRAFT：可阅读草稿，尚未通过人工翻译审阅。
- REVIEWED：审阅者已核对事实口径、否定词、不确定性和研究边界，登记真实姓名或账号；AI 自检不能冒充人工审阅。
- STALE：中文版本变化，译文仍对应登记的旧版本。页面统一要求读者优先核对中文原文。

校验器读取 UTF-8 文本，去除 BOM 并统一 CRLF 为 LF 后计算 SHA-256，避免 Windows / GitHub 换行差异误报。源文变化但未声明 STALE 会使检查失败；明确登记 STALE 后检查提示警告，允许正常中文研究继续。更新译文并审阅后才能更新 source_sha256；不能只刷新哈希来消除警告。译文变更会使此前的人工审阅失效，应退回 DRAFT，或由审阅者重新确认。

## 翻译提交步骤

1. 确定原文 ID、路径与当前版本；先核对原文不是待提交私人材料。
2. 使用 [术语表](glossary.md)；保留数字的币种、毛净口径和时间定义，保留 UNKNOWN、H、SUPPORTED 等状态。
3. 全文译文保留所有标题层级、段落、列表和证据链接；不要把译文写成重新研究。
4. 比对两个语言的 ID、数字、日期、人物、否定和因果边界。自动校验不能判断完整语义等价。
5. 登记 manifest，运行 `python tools/translation_lint.py`，审阅实际差异。
6. 原文变化时更新译文；暂时不能更新则明确标 STALE。成熟后再扩展下一篇，不批量铺满占位译文。

官方译文沿用对应原文的权利结构；这不扩大第三方的翻译、改写或商业使用授权。正式书稿翻译仍需单独授权。

## 可参考的实践

[Vue 的翻译入口](https://vuejs.org/translations/) 区分语言版本与进行中的翻译；[Vue Router 中文翻译说明](https://router.vuejs.org/zh/about-translation) 记录同步版本并维护术语；[Read the Docs 本地化文档](https://docs.readthedocs.com/platform/stable/localization.html) 将语言版本关联到主文档。这里采用语言分目录、共享原文身份和显式同步版本，保留本仓库中文研究为依据。
