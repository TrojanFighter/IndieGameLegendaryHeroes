# Evidence Record Schema

每条 Evidence 记录一个可追溯证据单元。它可以支持、削弱或限定一个或多个 Claim，也可以只服务某个 Case 的事实核验。

## Metadata

- Evidence ID:
- Case ID:
- Related Claim IDs:
- Source class: P0 / P1 / S1 / S2 / H
- Source title:
- Author / organization:
- Publication date:
- Event date (if different):
- URL:
- Access date:
- Archive / backup:

## Source-derived Fact

只写来源直接支持的事实。不要把解释混进来。

## Exact Wording

**P0 / P1 来源必填：至少一条逐字引语。** S1 建议提供；S2 / H 不要求。

为什么从 optional 改为必填：摘要会系统性地丢掉三类东西——**因果起点、当事人的话、口径与边界**。而这三类恰恰是下游读者层最难凭空写出来的部分。2026-10-09 对 11 个 Case 的实测：只依赖摘要时，正文会把因果顺序写反（见 CASE-012 把两次收入来源写成一次），也会写不到应有的长度。

规则：

- 引语必须**逐字**，回原文核对；不得由摘要反推，不得把不同来源、不同人的话拼接成一句；
- 引语应当是**直接支撑上面 Source-derived Fact 的那几句**，不为凑数而摘；
- 公开仓库只保留短引语，避免长篇复制受版权保护文本；
- 非中英文来源保留原文，必要时附译文，并注明哪一层是译文；
- 若来源确实读不到，写 `Exact Wording: NOT REACHABLE`，并在 Fetch status 里说明——**不要用摘要冒充引语**。

## Interpretation

项目自己的解释必须与来源事实分开，并标记为推断。

## Supports / Challenges

- Supports:
- Challenges:
- Neutral / context only:

## Boundary

这条证据不能证明什么？有哪些口径、时间、样本或回忆偏差限制？

## Conflict Check

若与其他来源冲突，列出 Evidence ID，并说明冲突尚未解决还是已有解释。

## Fetch status

这条来源**谁能取到、谁取不到**。目的有两个：避免下游反复尝试同一个 403 / JS 空壳，以及避免把"取不到"误当成"不存在"或"内容本来就这么少"。

```text
direct       直接 HTTP 可取
blocked     403 / 429 / 需要登录
shell        200 但正文由 JS 渲染，抓到的是空壳
gone         404，原页面已失效
api          经官方 API 取回（比抓网页稳定）
```

同时记录：

- 已知可行的替代路径（archive.org、官方镜像、Steam / 平台 API、其他语言版本）；
- 若原话由某个会话读到、而下游确实取不到，明确写"该引语仅存于本记录"，供后人引用时保留其 provenance。

判断"抓到的是不是空壳"的方法：搜正文主题词。若页面上只有导航里的项目名、主题词命中为 0，就是空壳——**200 不等于拿到了内容**。

## Verification Status

UNVERIFIED / PARTIAL / VERIFIED / CONFLICTING / RETRACTED
