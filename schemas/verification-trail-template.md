# Verification Trail Template

Verification Trail 只用于记录**研究判断发生实质变化的节点**，不是普通检索流水账。

## 何时必须建立

满足任一条件时建立：

- Claim status 发生变化，例如 `UNVERIFIED → SUPPORTED`、`SUPPORTED → CONTESTED`；
- 一个重要流行叙事被关键证据推翻或明显收窄；
- 关键数字、团队规模、开发周期、资金口径被纠正；
- P0/P1/S1 之间存在不能静默合并的冲突；
- canonical Case / Claim 的核心解释因为新证据发生变化。

普通新增来源、无争议补充事实、格式修正不需要单独 Trail。

## Template

- Trail ID: VT-YYYYMMDD-XXX
- Date:
- Affected Case / Claim / Evidence:
- Trigger source(s):
- Previous reading:
- New evidence:
- Why the previous reading changed:
- New canonical reading:
- What remains unresolved:
- Files updated:

## Rules

1. 必须保留旧判断是什么，不能只写“已修正”。
2. 必须指出改变判断的具体证据，而不是写“进一步研究发现”。
3. 若只是把强因果降级成弱因果，要明确保留下来的部分。
4. Trail 不替代 Evidence Record；它记录的是**研究判断如何改变**。
5. 重要纠偏应在对应 Case / Claim 中同步更新，Trail 只是 provenance。

## Example pattern

> Previous reading: “A 导致 B 立项。”  
> New evidence: B 的开发在 A 发布前已经开始。  
> New canonical reading: “A 不是 B 的起源原因，但可能改变了 B 所处市场的合法性与融资环境。”

这种记录尤其适用于本项目频繁出现的“起源原因 vs 市场验证”“solo 神话 vs contributor network”“众筹起点 vs 前史积累”等纠偏。
