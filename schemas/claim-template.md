# Claim Schema

每个 Claim 是一个可证伪命题，不是口号。

## Machine Metadata

Claim 的机器可读索引保存在 `../metadata/claims.json`。当前 Claim 正文仍集中在 `../claims/README.md`；metadata 只保存索引字段、研究状态与关系，不复制完整论证。

最小机器字段：

- `claim_id`
- `statement`
- `status`: `UNVERIFIED / WEAK / SUPPORTED / CONTESTED / VERIFIED / REFUTED`
- `evidence_strength`: `none / low / medium / high`
- `explanatory_importance`: `low / medium / high / critical`
- `narrative_value`: `low / medium / high`
- `related_cases`
- `evidence_ids`
- `last_reviewed`

`status` 不等于重要性。一个 VERIFIED 命题可以只是边缘事实；一个对全书极重要的命题也可能长期停留在 CONTESTED。

任何 Claim 状态、Statement 或 Related Cases 修改后，必须同步 `metadata/claims.json` 并通过 `python tools/research_lint.py --strict`。

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
