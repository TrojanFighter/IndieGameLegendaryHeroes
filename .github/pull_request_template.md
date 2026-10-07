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

## Editorial drafting review (for new Lane C reader prose)

- [ ] 已在正文生成前按 [Writing Entry Gate](../book/EDITORIAL-GATE.md#05-新稿写作入口预防模板化) 留下事实锁与 Narrative Packet
- [ ] 已说明人物/问题、时代处境、关键行动、主问题、叙述方式及作者观点边界；未套统一神话反转大纲
- [ ] 初稿已执行 Delete → Restore Person → Rhythm 与 Fidelity Readback；没有虚构场景或补 UNKNOWN
- [ ] 已按六项维度说明编辑判断、独立审查/读者测试是否完成；没有旧稿时未伪造 A/B
- [ ] 作者验收状态已明确；Agent 自评未冒充作者批准

## Editorial rewrite review (for existing Lane C prose rewrites)

- [ ] 已保存原稿 SHA 与具体修改范围，未顺手改 Case/Evidence/Claim
- [ ] 已按 [Editorial Rewrite Protocol](../book/EDITORIAL-REWRITE-PROTOCOL.md) 执行 Delete → Person → Rhythm
- [ ] 已回读 chronology / actor / negation / modality / source / UNKNOWN / time-regime
- [ ] 重大改写的 Evidence 依据和 `NEEDS_VERIFY` 项已列出
- [ ] A/B 对照结果或尚未盲测的原因已说明；作者验收仍是独立步骤

## Translation checks (when applicable)

- [ ] 共享原文 ID 与 Evidence，未新增事实或补齐 UNKNOWN
- [ ] 核对数字、日期、团队口径、否定词、证据状态和反方证据
- [ ] manifest 原文哈希对应实际翻译版本；过期译文已声明 STALE
- [ ] AI 自检没有冒充人工 REVIEWED；修改译文后重新审阅或退回 DRAFT
- [ ] `python tools/translation_lint.py`
- [ ] 人工检查 PR 标题、正文、截图、附件等本地钩子未覆盖的公开载体
