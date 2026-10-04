# 《独立游戏英雄传说》｜Thesis Candidates

© 2026 洪荒行者。All Rights Reserved.

这个文件只保存**已经值得追踪、但还没有资格写成全书定论**的书级命题。

它和 `claims/` 的区别：

- `claims/` 是正式、可证伪、带 Evidence ID 的跨案例命题；
- 本文件允许保存尚在孵化中的叙事母题、未来假设与解释框架；
- 任何条目在升格为正式 Claim 前，都必须经过 Case / Evidence / 反例审计。

定向审计记录见：[`research-notes/taste-capital-audit-001.md`](research-notes/taste-capital-audit-001.md)。

---

## TC-001 — 品味决定命运 / Taste Capital

- Status: PROVISIONAL — MULTI-CASE AUDIT STARTED
- Anchor: CASE-007 Gunpoint / Tom Francis
- Strong positive candidates: CASE-003 Papers, Please; CASE-020 Into the Breach
- Positive candidate: CASE-008 Dream Quest
- Counterpressure candidates: Artifact / Richard Garfield + Valve; Brigador / Stellar Jockeys
- Author-Origin: [`AC-005`](../author-corpus/AC-005-taste-capital-and-selection.md)

候选表述：

> **当执行资源有限时，开发者的比较能力、显性偏好、问题选择、体验抽象和 scope deletion，会显著影响有限产能最终被投入到哪里。**

这里的“品味”不是审美身份，而是一组可能可观察的选择能力。

Tom Francis 仍是最清晰锚点，但第一轮定向审计已经表明，这条线不再只有一个赢家样本：

- **Papers, Please**：日常观察 → 找到可玩的 bureaucracy interaction → 反转常见玩家视角 → 极便宜 interaction proof → public feedback → payoff/cost 删除；
- **Into the Breach**：多个 prototype 中选出最有潜力的方向 → 明确偏好 clear rules / lower RNG / legible failure → clarity over cool → 四年大量 scope deletion；
- **Dream Quest**：深度 card-game knowledge + custom-card habit + reusable engine + 长期 balance/test 很强，但“项目选择 / scope deletion”证据仍不够，暂不升 strong positive。

### 第一次重要修正：Taste 可能不是单一标量

Artifact 与 Brigador 提醒我们，“有品味”如果被写成一个总分，几乎一定会过度解释。

更值得验证的拆分是：

```text
product / interaction selection
scope selection
representation selection
market / audience selection
business-model selection
feedback integration
```

一个创作者可能在 product design 上极强，却在 business model / audience model 上判断失败；也可能做出好产品，却无法正确 frame、position 或 distribute。

### 需要什么才能升级？

- 至少 3 个不同生产结构的强正例；
- 至少 1–2 个完成审计的强反例 / counterpressure case；
- 能把 taste 和职业网络、资金、传播优势、执行能力区分开；
- 能识别成功前的判断行为，而不是成功后给赢家贴“有品味”标签；
- 能明确“哪一种 selection domain”成立，而不是拿一个模糊 taste 概念解释所有成功。

在 Brigador 或其他失败样本完成正式 audit 前，**不得建立 C013**。

---

## TC-002 — 两种失败：执行失败与选择失败

- Status: PROVISIONAL FRAME — FAILURE SAMPLE NEEDED
- Related: TC-001, C002, C004, C007, C009

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

### 研究要求

这条必须大量纳入失败者和商业表现不佳的作品。只研究成功案例无法证明“选择失败”存在，更无法估计它的重要性。

当前已有三类不同强度的线索：

- **CASE-025 Bills Must Be Paid**：mobile rapid-prototype 经验既是能力资本，也携带可能不适用于 Steam premium 的错误市场模型；团队后来通过 demo / Steam feedback 修正；
- **Artifact**：世界级 card-game design pedigree 仍不能自动覆盖 monetization / community relationship 判断；
- **Brigador**：好评、press、conventions 与产品质量并未自动转化为 launch success，官方 GDC postmortem 本身就以 audience expectations / bad decisions 为主题。

其中 Artifact 暂时只作为 non-indie comparator；Brigador 应优先进入正式 failure audit。

---

## TC-003 — Execution abundance → Selection scarcity

- Status: FUTURE HYPOTHESIS
- Period: AI-era, 2020s+
- Related: AC-005, TC-001, TC-002

候选表述：

> **当 AI 和通用工具显著降低部分执行成本以后，项目瓶颈可能部分从“能不能做出来”前移到“什么值得做、什么应该尽快杀掉”。**

这不是 CASE-007 能证明的历史事实。

Gunpoint、Papers, Please、Into the Breach 的作用只是帮助定义：如果未来“选择能力”变得更稀缺，我们应该观察什么行为。

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

这条目前只作为编辑结构，不是因果模型。后续 Tarkov、despelote、Roblox、Among Us 等 profile 可能支持它，也可能迫使它重写。

---

## 使用规则

1. 这里的句子不能在正文中被写成“研究已经证明”；
2. 每个 Thesis Candidate 必须注明锚点、反例需求与升级门槛；
3. 如果后续 Case 反驳它，应修改或删除，而不是增加修辞保护；
4. 能够精确可证伪后，才迁移到 `claims/`；
5. 一旦成为正式 Claim，本文件只保留叙事层摘要并回链 canonical Claim。
