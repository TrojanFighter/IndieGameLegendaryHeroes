# 《独立游戏英雄传说》｜Thesis Candidates

© 2026 洪荒行者。All Rights Reserved.

这个文件只保存**已经值得追踪、但还没有资格写成全书定论**的书级命题。

它和 `claims/` 的区别：

- `claims/` 是正式、可证伪、带 Evidence ID 的跨案例命题；
- 本文件允许保存尚在孵化中的叙事母题、未来假设与解释框架；
- 任何条目在升格为正式 Claim 前，都必须经过 Case / Evidence / 反例审计。

定向审计记录：
- [`Taste Capital Audit 001`](research-notes/taste-capital-audit-001.md) — Gunpoint / Papers, Please / Into the Breach / Dream Quest + 初步反压力；
- [`Taste Capital Audit 002`](research-notes/taste-capital-audit-002-brigador.md) — CASE-026 Brigador，强执行下的 selection-domain failure。

---

## TC-001 — 品味决定命运 / Taste Capital

- Status: PROVISIONAL — MULTI-CASE + FAILURE AUDIT STARTED
- Anchor: CASE-007 Gunpoint / Tom Francis
- Strong positive candidates: CASE-003 Papers, Please; CASE-020 Into the Breach
- Positive candidate: CASE-008 Dream Quest
- Formal counterpressure: CASE-026 Brigador / Stellar Jockeys
- Additional comparator: Artifact / Richard Garfield + Valve
- Author-Origin: [`AC-005`](../author-corpus/AC-005-taste-capital-and-selection.md)

候选表述：

> **当执行资源有限时，开发者的比较能力、显性偏好、问题选择、体验抽象和 scope deletion，会显著影响有限产能最终被投入到哪里。**

这里的“品味”不是审美身份，而是一组可能可观察的选择能力。

Tom Francis 仍是最清晰锚点，但第一轮定向审计已经表明，这条线不再只有一个赢家样本：

- **Papers, Please**：日常观察 → 找到可玩的 bureaucracy interaction → 反转常见玩家视角 → 极便宜 interaction proof → public feedback → payoff/cost 删除；
- **Into the Breach**：多个 prototype 中选出最有潜力的方向 → 明确偏好 clear rules / lower RNG / legible failure → clarity over cool → 四年大量 scope deletion；
- **Dream Quest**：深度 card-game knowledge + custom-card habit + reusable engine + 长期 balance/test 很强，但“项目选择 / scope deletion”证据仍不够，暂不升 strong positive；
- **Brigador**：核心产品、美术与技术身份都很强，却在 2016 首发阶段出现 onboarding、market legibility 与 audience-expectation 错位，成为第一个正式 failure counterpressure。

### 第一次重要修正：Taste 不是单一标量

Brigador 的正式 audit 已经把这条修正从“提醒”推进为具体失败样本。

更值得验证的拆分是：

```text
product / interaction selection
scope selection
representation selection
onboarding selection
market / audience selection
business-model selection
feedback integration
```

一个创作者可以在 product design 上极强，却在 business model / audience model 上判断失败；也可能做出好产品，却无法正确 frame、position 或 distribute。

所以后续研究不得再问“这个人有没有品味”这种总分问题，而应问：

> **他在哪些 selection domain 上表现出可观察优势？这些优势是否覆盖了项目真正的瓶颈？**

### 需要什么才能升级？

- 至少 3 个不同生产结构的强正例；
- 至少 1–2 个完成审计的强反例 / counterpressure case；
- 能把 taste 和职业网络、资金、传播优势、执行能力区分开；
- 能识别成功前的判断行为，而不是成功后给赢家贴“有品味”标签；
- 能明确“哪一种 selection domain”成立，而不是拿一个模糊 taste 概念解释所有成功。

CASE-026 已满足第一份正式反压力样本，但正例门槛和第二类反例仍未完成，因此**仍不得建立 C013**。

---

## TC-002 — 两种失败：执行失败与选择失败

- Status: PROVISIONAL FRAME — FIRST FORMAL FAILURE SAMPLE ADDED
- Related: TC-001, C002, C004, C007, C009, C010

候选表述：

> **独立开发失败至少有必要区分“执行不出来”和“把执行能力投入了错误问题”。**

### 执行失败

- 没有足够 runway；
- 技能或工具不足；
- 组织能力不足；
- scope 超过团队承载；
- 技术、内容或交付管线崩溃。

### 选择失败

- 选择了不存在 / 不足够大的需求；
- 把大量成本投给玩家并不在乎的部分；
- 继承了错误平台或商业模式的世界模型；
- 明明可以删除，却因为惯性继续扩大 scope；
- 创作者自己喜欢的价值主张无法转化为玩家价值；
- 产品内部判断正确，但 audience / business-model / positioning 判断错误。

### CASE-026 带来的修正

Brigador 说明“执行失败 vs 选择失败”也不能被写成简单二选一标签。

它更像：

> **execution capacity × selection quality × feedback-loop speed**

团队可以非常擅长完成困难工作，却因为某些 selection domain 较弱、反馈回路又太慢，高效地积累一个昂贵错误。

这也是为什么“产品已经很好”不能结束商业审计：产品质量、market legibility 与 commercial fit 是不同变量。

### 研究要求

这条仍必须继续纳入失败者和商业表现不佳的作品。一个 Brigador 只能证明这类结构存在，不能估计其普遍程度。

当前已有几类不同强度的线索：

- **CASE-025 Bills Must Be Paid**：mobile rapid-prototype 经验既是能力资本，也携带可能不适用于 Steam premium 的错误市场模型；团队后来通过 demo / Steam feedback 修正；
- **Artifact**：世界级 card-game design pedigree 仍不能自动覆盖 monetization / community relationship 判断；
- **CASE-026 Brigador**：好评、press、conventions 与产品质量并未自动转化为 launch success；开发者 postmortem 把 audience expectations、presentation、controls/entry friction 与 visibility 纳入失败复盘。

Artifact 继续只作为 non-indie comparator；CASE-026 已成为正式 failure comparator。

---

## TC-003 — Execution abundance → Selection scarcity

- Status: FUTURE HYPOTHESIS
- Period: AI-era, 2020s+
- Related: AC-005, TC-001, TC-002

候选表述：

> **当 AI 和通用工具显著降低部分执行成本以后，项目瓶颈可能部分从“能不能做出来”前移到“什么值得做、什么应该尽快杀掉”。**

这不是 CASE-007 或 CASE-026 能证明的历史事实。

Gunpoint、Papers, Please、Into the Breach、Brigador 的作用只是帮助定义：如果未来“选择能力”变得更稀缺，我们应该观察什么行为与失败结构。

### 需要验证的指标 / 案例

- 同等规模团队单位时间可生产 prototype 数是否显著增加；
- AI 原生团队的失败主要发生在 execution 还是 selection；
- 更快制作是否也让错误方向积累更多 sunk cost；
- 能否通过更快 kill prototype 降低 selection error；
- 有明确 taste/selection process 的团队是否从 AI 工具获得更高边际收益；
- 市场是否因供给暴增而进一步奖励“可识别的选择”而不是单纯制作完整度。

### 禁止推论

- AI 不会自动让 engineering / art direction / production 不重要；
- 执行成本下降不等于总成本下降；
- 作品数量增加不等于选择能力更重要已经被证明；
- “有创意”不能替代市场接入、runway 与完成能力；
- product taste 强不等于 market / business-model judgment 强。

---

## TC-004 — 先活下来，再判断，再执行

- Status: EMERGING BOOK STRUCTURE

目前五篇 reader profile 已自然暴露出一个可能的上位结构：

- **Kenshi**：如何购买时间；
- **Rocket League**：如何购买组织存续；
- **Bills Must Be Paid**：如何通过大量原型与失败购买能力；
- **Gunpoint**：有了有限能力以后，如何决定把它花在哪里；
- **FTL**：如何只购买一个有限试验窗口，再让真实证据决定下一轮承诺。

候选的书级生产链因此不是“灵感 → 制作 → 成功”，而更接近：

> **生存条件 → 能力资本 → 选择 / 判断 → bounded experiment → scope → 执行 → 市场接入 → 反馈 / 现金流 → 下一轮生产条件。**

FTL 加入后，这条链出现了一个很重要的中间变量：**commitment level / 承诺等级**。

同一个项目并不必从第一天就承担“完整公司 / 完整产品 / 完整商业成功”的风险。开发者可以先购买一个有限、可失败的试验窗口，再根据 prototype、竞赛、玩家、市场等外部证据提高承诺。

CASE-026 Brigador 又增加了另一条边界：这条链并不是走到“执行完成”就结束；**市场能否正确读取产品、反馈能否及时返回生产系统**，会决定一个完成度很高的作品是否仍在最后一段失配。

这条目前只作为编辑结构，不是因果模型。后续 Tarkov、despelote、Roblox、Among Us 等 profile 可能支持它，也可能迫使它重写。

---

## TC-005 — 英雄为什么还没出发？教育与家校选择权可能是更上游的筛选器

- **Status:** AUTHOR-ORIGIN / PROVISIONAL / CAUSAL EFFECT UNMEASURED
- **Canonical mechanism:** [中国037](../country-studies/china/037-family-school-agency-risk-hero-nondeparture.md)；[三层研究018](research-notes/china-creator-constraints-three-layer-map-018.md)。
- **论题：** 国内游戏行业版本变更可以让旧能力失效，但一些可能的创作者从未积累起游戏参照、独立选题、首个作品与公开反馈。教育、家校控制与自主权转移不足，可能是这些“不可见的未出发者”的上游解释。**更早发生 ≠ 数量级更大，仍须实证比较。**
- **四类门槛：** 没形成兴趣、没完成第一件作品、有作品却无法承受职业风险、已入行而难转作者。第五类“自愿没有创作意愿”不得算作失败。
- **明确反压力：** 中国教育体系中有优质社团与原创者；有受过严格应试训练的原创开发者；有人获得家庭和经济支持仍没有成功；他国也存在家长控制与非标准创作机会不均。
- **证据升级门槛：** 至少一个纳入**从未制作/未入行者**的固定队列，来自家庭/学校/社群的自主选择机会资料，控制家庭资源并追踪首作、重复尝试、职业/市场反馈；否则不升级书级确定性断言。

该论题改变人物传记的提问顺序：先问“这个人为什么曾有机会出发”，再问“后来为何成功/失败”，还要研究那些不曾产生传记的人。

---


### TC-005 实证压力（2026-10-10）

[中国038](../country-studies/china/038-education-maker-funnel-empirical-measurement-ceps-pisa-ggj.md)提供三重反压力：新加坡与韩国高创意测验分数和学业成绩共存，中国已存在CiGA与GGJ Next创作站点，人大CEPS已经有全国学校样本可以研究机会分配。然而这些资料均不能给出普通青年转成首个自定作品、二次制作和职业作者的同口径漏斗。TC-005保持`PROVISIONAL`，不许从东亚身份或考试分数直接推断创作者发生率。

## 使用规则

1. 这里的句子不能在正文中被写成“研究已经证明”；
2. 每个 Thesis Candidate 必须注明锚点、反例需求与升级门槛；
3. 如果后续 Case 反驳它，应修改或删除，而不是增加修辞保护；
4. 能够精确可证伪后，才迁移到 `claims/`；
5. 一旦成为正式 Claim，本文件只保留叙事层摘要并回链 canonical Claim。
