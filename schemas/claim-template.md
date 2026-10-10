# Claim Schema

每个 Claim 是一个可证伪命题，不是口号。

## Machine index requirement

每个 Claim 都必须在 [`../metadata/claims.json`](../metadata/claims.json) 中登记，至少包含：

- `claim_id`
- `statement`
- `status`: UNVERIFIED / WEAK / SUPPORTED / CONTESTED / VERIFIED / REFUTED
- `evidence_strength`: none / low / medium / high
- `explanatory_importance`: unrated / low / medium / high / critical
- `narrative_value`: unrated / low / medium / high / critical
- `related_cases`
- `evidence_ids`
- `last_reviewed`

正文负责论证和边界；metadata 负责状态、关系与机器检索。Case ↔ Claim 关系必须双向一致。

### Evidence reference rule

`evidence_ids` 必须使用全局可解析格式：

`CASE-001:E001`

而不是单独写 `E001`。不同 Case 可以各自拥有 `E001`，因此 Case ID 是引用的一部分。

当 Claim 升级为 `SUPPORTED` / `VERIFIED`：

- `evidence_ids` 不得为空；
- 引用必须实际存在于对应 Case 的 evidence ledger；
- 至少应包含 P0 / P1 / S1 之一；
- `VERIFIED` 若完全没有 P0/P1，应重新审视状态是否过强。

上述规则由 `tools/research_evidence_lint.py` 检查。

## Header

- Claim ID:
- Statement:
- Scope:
- Status: UNVERIFIED / WEAK / SUPPORTED / CONTESTED / VERIFIED / REFUTED
- Last reviewed:
- Related Cases:

## Falsification Test

- 什么证据会支持这个命题？
- 什么证据会削弱或反驳这个命题？
- 哪些变量必须控制？
- 哪些替代解释必须排除？

## Evidence For

| Evidence ID | Source class | Case | Summary | Weight |
|---|---|---|---|---|

## Evidence Against

| Evidence ID | Source class | Case | Summary | Weight |
|---|---|---|---|---|

## Current Reading

只写当前证据允许的最强表述，不把概率性关系升级为必要/充分关系。

## Boundary / Forbidden Inference

明确哪些结论不能由本 Claim 推出。

## Next Evidence Needed

列出最值得补的证据缺口。

## Review trigger / 复审触发

Claim 不能无限期停在同一个状态。

**当前规则的盲区**：整套设计只防"过早声称"（不得把 H 写成结论、必须记反方证据），但不防"永不收敛"。截至 2026-10-09，15 个 Claim 中 `VERIFIED` 为 **0**、`REFUTED` 为 **0**，C001–C012 长期停留在原有状态。加一个 Case 的成本低，升级一个 Claim 的成本高，于是系统会一直加 Case。

出现下列任一情况，**必须写一次明确的复审判断**：

- `related_cases` 达到 5 个或以上，状态仍是 `UNVERIFIED` / `WEAK`；
- 经历两轮语料更新（新增 Case 或 Evidence）后状态未变；
- Evidence For 与 Evidence Against **都非空**，且跨越多个复审周期仍未处理；
- 某条被引用的 Evidence 标为 `RETRACTED`，或来源已失效。

复审结论只有三种，且必须明写：

1. **升级** —— 并说明反方证据已检查到什么程度；
2. **降级或拆分** —— 命题过大时应拆分，而不是用更多形容词掩盖不可证伪性；
3. **维持** —— 必须写清「还缺哪一条**具体**证据才能动」。不接受"证据还不够""需要更多研究"这类无指向的表述。

复审记录写在 Claim 正文的 `## Current Reading` 之下，不能只改 metadata 的状态字段；`last_reviewed` 不得在未做上述判断的情况下刷新。
