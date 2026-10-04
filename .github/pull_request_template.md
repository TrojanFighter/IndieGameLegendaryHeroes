## Lane

- [ ] **Lane A — Library Operations**: schema / metadata / lint / CI / navigation / source health / Explorer / build
- [ ] **Lane B — Case Research**: Case / Evidence / Claim / audits / comparators
- [ ] **Lane C — Editorial / Book**: profiles / synthesis / TOC / publication

> 一个 PR 原则上只选一条 Lane。确需跨 Lane，请在下面解释为什么不能拆分。

## Summary

<!-- 这次改了什么？尽量写具体文件、Case ID、Evidence ID 或工具。 -->

## Why now

<!-- 哪个真实问题、重复故障、研究缺口或编辑需要触发了这次改动？ -->

## Canonical facts boundary

- [ ] 本 PR **没有**新增或改变历史事实 / Case 判断
- [ ] 本 PR **有**新增或改变 canonical research facts，并已落到 Case / Evidence / Claim
- [ ] Reader layer 只消费已存在的 canonical facts，没有补 UNKNOWN

如改变 canonical facts，请列出：

- Case ID：
- Evidence ID：
- Related Claim(s)：
- Contributor audit：
- Market-access audit：
- Context / CSA audit：

## Derived / generated state

涉及 metadata 或索引时确认：

- [ ] `cases/README.md` / `claims/README.md` 与 metadata 同步
- [ ] `metadata/research-stats.json` 已通过 `python tools/research_lint.py --write-stats` 刷新（如需要）
- [ ] Reader layer / Explorer 没有复制第二份 canonical facts
- [ ] 新字段 / taxonomy 来自真实 corpus 需求，不是为了 UI 看起来完整

## Checks

- [ ] 已按 `docs/public-research-boundary.md` 检查新增 commits 与提交消息
- [ ] 无私人项目作为案例、竞品、语料来源或应用目标；无匿名化的私人执行、预算、人员或设计信息
- [ ] 需判断的词已核对上下文；公开 PR 未粘贴私有词表或命中原文

- [ ] `python tools/research_lint.py --strict`
- [ ] `python tools/research_evidence_lint.py`
- [ ] `python tools/context_audit_lint.py`
- [ ] `python tools/reader_layer_lint.py`
- [ ] `python tools/explorer_lint.py`

<!-- 不相关的检查可以说明原因，不要为了勾选而放宽规则。 -->

## Transfer boundary / follow-up

<!-- 这次明确没有解决什么？哪些缺口应交给另一条 Lane / 后续 Issue？ -->
