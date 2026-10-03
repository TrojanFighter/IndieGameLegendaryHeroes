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
