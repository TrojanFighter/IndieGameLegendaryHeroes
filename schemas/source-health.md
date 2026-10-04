# Source Health Monitoring

本协议属于 **Lane A / Library Operations**。它只维护 Evidence 来源的可访问性，不替 Lane B 判断历史事实。

## 目标

Evidence Ledger 会随时间发生链接腐烂、重定向、访问限制和站点故障。Source Health 的目标是尽早暴露这些维护问题，而不是自动宣布某条 Evidence 失效。

## v0 自动状态

- `HEALTHY`：URL 当前返回 2xx，且没有观察到最终地址变化。
- `REDIRECTED`：请求最终落到不同 URL；需要人工判断是否应更新 canonical URL。
- `ACCESS_RESTRICTED`：401 / 402 / 403。可能是付费墙、登录要求、地区限制或 CI 反爬；自动化不得擅自判成某一种原因。
- `TEMPORARILY_UNREACHABLE`：408 / 425 / 429 / 5xx、超时、DNS 或临时网络错误。单次出现不等于来源死亡。
- `DEAD`：404 / 410。优先寻找 archive / backup，并保留原始书目信息。
- `CLIENT_ERROR`：其他 4xx，需要人工判断 URL 是否 malformed、已迁移或被站点策略拒绝。
- `UNKNOWN_ERROR`：自动检查无法可靠归类的异常。

## v0 明确不做什么

自动化目前**不能可靠判断**：

- `PAYWALLED`：403/402 并不等于付费墙；
- `BLOCKED_FROM_CI`：需要人工或多环境复核；
- `SOURCE_CONTENT_CHANGED`：URL 还活着不代表内容没变；
- 页面中的具体事实是否仍支持 Evidence；
- Wayback / archive 是否保存了我们需要的具体版本。

这些状态只有在后续建立内容 fingerprint、archive baseline 或人工复核机制后再升级。

## Enforcement strength

Source Health 是**维护报告，不是 merge gate**。

原因：外部网站可达性不受仓库控制，尤其政府站、旧媒体站和反爬站点容易在 GitHub Actions 中产生假失败。

推荐处理：

1. `DEAD` 连续出现：Lane B / 维护者寻找 archive 或替代一手来源；
2. `REDIRECTED`：确认内容相同后更新 canonical URL；
3. `ACCESS_RESTRICTED`：人工浏览器复核，再决定是否标 paywall / bot block；
4. `TEMPORARILY_UNREACHABLE`：至少跨两次周期再升级；
5. 任何 URL 修复都不得凭记忆重建来源内容。

## Output

`tools/check_source_health.py` 扫描 `evidence/**/*.md` 中的 HTTP(S) URL，按 URL 去重，同时保留引用它的 Evidence Ledger 文件与行号。

每周工作流输出：

- Markdown Summary；
- JSON 明细 artifact；
- 不自动修改 Evidence Ledger；
- 不自动创建或关闭 Issue。
