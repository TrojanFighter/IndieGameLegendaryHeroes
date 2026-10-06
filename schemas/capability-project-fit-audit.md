# Capability–Project Fit Audit — 能力偏科与立项适配审计

## Purpose

独立游戏研究不能把 `Origin` 写成人物简历，把 `Capability` 写成技能清单，然后直接跳到作品结果。

本审计专门回答一个更接近生产函数的问题：

> **创作者在立项前已经拥有什么强项、缺什么能力；项目是否被主动设计成“让强项高杠杆、让弱项不必做或少做”的问题？**

这与简单的 `scope small` 不同。真正高效的项目通常不是把行业标准产品等比例缩小，而是**改变问题定义**：删除、替代、程序化、抽象化、外部化或审美化那些对本团队最昂贵的生产环节。

本审计适用于成功案例与失败案例。不得因为作品成功，就事后把作者的所有前史解释成“天生适配”；也不得因为失败，就把非主流能力结构写成缺陷。

---

## Core Distinction

至少区分三种小团队压缩方式：

### A. Labor Compression / 劳动压缩

同一个常规生产问题仍然存在，只是更少的人承担更多工种。

例：一个人同时做导演、建模、绑定、动画、渲染、剪辑。

这可以极度节省现金，但通常用**时间、身心负担和质量波动**支付成本。

### B. Problem Redefinition / 问题重定义

昂贵问题被取消或改写，因此根本不需要以行业标准方式解决。

例：不为大量动物制作传统骨骼动画，而采用程序化/抽象运动，并把结果转化为作品审美的一部分。

### C. Capability Leverage / 能力杠杆

项目的核心体验、视觉、技术或市场表达被设计成创作者原有强项可以反复产生复利。

例：技术美术出身的 solo 作者选择视觉辨识度高、系统/代码复杂度相对受控、适合短 GIF 传播的探索作品。

优秀案例往往混合三者；研究时要判断主要机制是哪一种，而不是一律写成“少人多能”。

### D. Capability Trap / 能力陷阱

强项也可能成为错误立项的诱因。

典型结构不是“团队不会做”，而是：

```text
某项能力很强
→ 因为做得到，所以默认项目应该需要它
→ 功能 / 技术 / 表现 / 组织复杂度不断向该能力扩张
→ 生产成本、固定组织和市场解释负担同步上升
```

因此必须区分：

- `能力可以解决这个问题`；
- `这个问题值得存在`。

大厂工程、网络、3A 美术、工业管线、多人服务能力等都可能产生 `Capability Trap`。已有能力不是免费资源：一旦它诱发更高资产密度、更多依赖关系、更长周期或更大固定团队，它同样会提高 opportunity cost。

失败 / comparator Case 应专门检查：项目是在利用强项，还是在**为强项寻找用武之地**。

---

## Required Questions

对每个进入 `REVIEW / STABLE` 的人物型、OPC、micro-team 或强作者性 Case，尽量回答：

### 0. Project-formation direction / 项目到底从哪里长出来

先于一般的 capability map，必须问一次：

> **这是“先有项目，再补能力”，还是“先有能力向量，再反向生成项目”？**

至少区分：

- `CAPABILITY-SHAPED`：立项 / 早期定义已经明确围绕主创强项与弱项塑形；
- `CAPABILITY-ADAPTED`：项目先存在，开发中才因能力/成本约束被大幅改写；
- `CAPABILITY-COMPOSED`：项目 thesis 已有雏形，founding team 通过互补 cofounder capability 被重新组成；成本主要不是工资，而是 equity / authorship / control sharing（如 CASE-050）；
- `CAPABILITY-EXPANDED`：项目核心愿景先存在，缺失能力不是被删除，而是通过 retained earnings、publisher、融资、招聘或 specialist periphery 被主动补齐。继续拆成：`SELF-FINANCED EXPANSION`（如 CASE-047）、`EXTERNAL-CAPITAL EXPANSION`（如 CASE-049）与 `GRANT / NON-DILUTIVE EXPANSION`（如 CASE-052）；
- `LABOR-COMPRESSED`：项目基本保留行业标准问题，只由更少的人硬扛；
- `UNKNOWN`：没有足够立项期证据。

判断 `CAPABILITY-SHAPED` 不能只看成品“好像很适合作者”。至少寻找一条立项期 / 开发期行动链：

`self-knowledge / constraint → project decision → removed/transformed obligation → player-facing result`

正式跨案例命题见 [C015 — Capability-Shaped Project Formation](../claims/C015-capability-shaped-project-formation.md)。

### 1. Pre-project capability map

- 主创在立项前的职业、教育、长期爱好、mod/UGC、旧作、工具经验是什么？
- 哪些能力达到职业级 / 高熟练度？
- 哪些能力明显薄弱、刚学、依赖外部帮助，或对其而言机会成本极高？
- 哪些能力不是技术技能，而是品味、叙事、社群、媒体表达、商务、发行或领域知识？

### 2. Project-shape response

- 产品最初的形态是否主动利用已有强项？
- 哪些行业标准功能被砍掉，而不是“以后再做”？
- 哪些复杂度被程序生成、物理系统、抽象表现、文本、库存资产、现成 middleware、UGC、玩家社交或社区内容取代？
- 哪些生产难题被转移给外部 contributor / publisher / platform？
- 哪些弱项没有消失，而是被作者用长期手工劳动硬扛？

### 3. Aesthetic conversion

特别检查：

> **成本规避是否同时变成了玩家能感知的风格、笑点、清晰度或卖点？**

如果“便宜做法”只让作品看起来便宜，它只是成本削减；如果它同时生成独特美学或传播性，它可能是更强的 production design。

### 4. Market-expression fit

- 项目的强项是否天然适合商店截图、GIF、短视频、主播或 demo？
- 主创是否拥有与该表达形式匹配的既有能力？
- 市场传播面是否是产品设计的一部分，而不是完成后临时补营销？
- 不得把传播结果全部归因于设计；保留平台窗口、算法、媒体、主播和 luck。

进一步检查 `double dividend`：

> **同一个降本决策，是否同时降低 production cost，并提高 market legibility？**

这是比单纯“省钱”更强的信号。矩形角色、翻滚动物、极低精度但高辨识度的 3D、单一核心 mechanic 等都可能属于这一类；但必须由立项期 / 开发期证据证明，而不能只看成品倒推。

### 4.5. Temporal fit / 能力—项目—时代三者是否同时匹配

能力—项目适配不能脱离年份。

同一能力结构在 2013、2019、2026 可能面对完全不同的：
- engine / asset / AI tool availability；
- platform competition；
- creator / social discovery；
- labor / outsourcing cost；
- audience expectation；
- financing and distribution options。

因此任何“这类出身适合做这类项目”的结论都必须同时记录：

| Creator strength | Project shape | Observed years | Enabling regime | 2026 transfer status |
|---|---|---:|---|---|

The First Tree 尤其作为首个示范：
> 2017–2019 的 visual-first / technical-art 路径值得研究，但当年的 Reddit / Imgur / Tumblr / Twitter 传播生态不能默认在 2026 仍以同样方式成立。

具体时效规则见 `../book/TEMPORAL-VALIDITY.md`。

### 5. Counterfactual

至少问一次：

> 如果把这个项目交给能力结构完全不同、但总人数相同的团队，它仍然会是同一个合理项目吗？

如果答案明显是否定的，说明项目与创作者能力结构高度耦合。

再问：

> 如果作者补齐弱项的唯一办法是多招 5–20 人，这个项目是否还保持原来的经济性？

再加一组 **capability acquisition** 问题：

- 缺失能力是被删除、抽象，还是被购买？
- 缺失能力是通过 cofounder / employee / contractor / publisher service / grant-funded specialist 哪一种关系进入？
- 如果是 cofounder，支付的不是现金而是哪些 equity / authorship / veto / long-term dependency？
- 谁支付招聘 / contractor / specialist 的现金成本？
- 资本来自 prior hit、publisher、VC、grant、work-for-hire 还是家庭资产？
- 资本是否带来 ownership / approval / milestone / recoup 等 control obligation？
- 是否新增 backer / platform / storefront expectation？
- 资本方能否否决 prototype / scope / launch window，还是只提供 runway？
- external capital 的“钱”与“能力”分别是什么：招聘预算、QA、发行、平台、营销、技术支持还是用户入口？
- team capability 扩张以后，authorial decision density 是否仍然存在？
- 如果不允许 hiring，这个项目会被改写成什么样？

### 6. Failure-side audit

失败案例同样检查：

- 是否选择了一个系统性放大自身弱项的项目？
- 是否把“我想做什么”优先于“我的组织能便宜地做什么”？
- 是否用招聘、融资、外包和开发周期去填补能力错配？
- 是否出现 `feature accumulation`、工业化模仿或组织先行？
- 是否有强项未能转化为 market legibility？
- 是否出现 `Capability Trap`：因为某项能力很强，于是给产品增加了本来不必存在的技术/资产/组织问题？

这不是要求所有独立作者只做舒适区项目；而是要把**跨出舒适区的成本与补偿机制**写清楚。

---

## Evidence Standard

不能只根据成品倒推主创能力。

优先证据：

1. 项目立项前的履历、旧作、作品集、招聘记录；
2. contemporaneous devlog / prototype / pitch；
3. 开发者本人复盘，明确说明“为什么这样做 / 为什么不做另一个方案”；
4. credits / contributor audit；
5. 工具、素材、外包和代码来源；
6. 营销素材与开发期传播记录。

`作者看起来很会美术，所以一定是为了省程序成本才做这个项目` 只属于 H，除非有行动链证据。

特别防止两种 biography fallacy：

- `曾在赌博公司工作 → 所以一定把赌博设计方法带入游戏`；
- `曾在大厂 / AAA 工作 → 所以其后所有技术与组织决策都来自大厂训练`。

职业前史只能建立候选机制，必须进一步证明**具体能力 → 具体项目动作 → 具体生产结果**。

---

## Recommended Case Insert

在 Case 的 `Origin` 与 `Capability` 后增加一个小节即可，不强制新增 machine metadata：

```md
### Capability–Project Fit

| Pre-existing strength / weakness | Project maneuver | Cost removed / transferred | Player-facing effect | Evidence | Boundary |
|---|---|---|---|---|---|
```

正文至少给出一句结论：

- `FIT-STRONG`：项目明显围绕团队能力不对称设计；
- `FIT-MIXED`：有部分重定义，但仍大量依靠手工劳动/外部资本填坑；
- `FIT-WEAK`：项目系统性要求团队补齐昂贵弱项；
- `FIT-EXPANDED`：项目本身不贴合 founder 当前能力，但团队有意识地用资本/招聘/外围扩张能力集合，并保留核心产品 thesis；
- `FIT-TRAP`：强项反而诱发不必要复杂度 / 固定成本 / feature accumulation；
- `FIT-COMPOSED`：核心项目通过互补 founding team 形成可执行 capability set；
- `UNKNOWN`：缺少立项期证据。

另设一个**纵向 overlay**，不与上述 fit score 互斥：

- `FIT-LOCK-IN`：长期成功的 capability–project match 沉淀为工具、品牌、受众、团队流程与身份，使继续做同类项目更便宜、转型却更昂贵。CASE-051 Zachtronics 是第一锚点。

这些标签目前只用于人读审计，不进入 `metadata/cases.json`，避免在跨案例证据不足时过早固化分类。

---

## Anchor Examples / Research Leads

这些不是预先判决，只是当前最值得核验的锚点：

### 已有第一批锚点

- **The First Tree / David Wehle** — technical artist / visual-first background、明确自述 coding 弱；项目短、视觉可识别、使用现成资产并通过 GIF / Reddit / Imgur 等形成强传播面。检验“视觉强项 → 产品形态 → marketing surface”是否在立项期已经耦合。
- **Everything / David OReilly** — 动画作者把抽象能力带入游戏；大量对象/动物不采用传统写实 rig animation，而以程序化/翻滚运动解决，并把限制转化为作品语言。是 `problem redefinition + aesthetic conversion` 的强候选。
- **Landfall Games** — 物理、喜剧、社交和 community interaction 逐渐形成团队能力资本；反复使用 jam、短周期和小固定团队，同时保留 TABS/HASTE 等长项目作为内部反例。重点研究“工作室是否学会让产品形态服从自己的高杠杆能力”。长期 intake：Issue #25。
- **CASE-007 Gunpoint / Tom Francis** — 评论者/资深玩家背景如何影响问题选择，需区分 taste 与实现能力。
- **CASE-018 RollerCoaster Tycoon / Chris Sawyer** — 极强工程能力和长期代码资本如何支撑非常规 OPC production。
- **CASE-026 Brigador** — 已升级为 `FIT-STRONG / LAUNCH-FAILED`：多轮 prototype、团队特定 taste、custom engine、precision aiming 与 digital-kitbash art pipeline 都与成品高度耦合，但首发仍因 onboarding / market legibility / audience expectation 等失败。它证明 fit 不是商业成功充分条件。
- **CASE-047 The Witness** — `FIT-EXPANDED / CAPABILITY-EXPANDED`：Blow 没有把项目削成只需要自己会的东西，而是用 Braid retained earnings 购买 art / architecture / landscape / specialist capability；用于审计“资本让 capability set 追上 project thesis”的另一条路线。
- **CASE-048 The Magic Circle** — 第二份 `FIT-STRONG / MARKET-FAILED`：creator capability、题材与 mechanic 高度耦合，但商业仍不可持续；用于强制把 `Creator–Project Fit` 与 `Project–Market Selection` 分开。
- **CASE-049 Outer Wilds** — `FIT-EXPANDED / EXTERNAL-CAPITAL`：学生 thesis 先产生 playable/design evidence，再由 Mobius/Fig/publisher/platform 资金扩张团队与 production perimeter；用于比较 founder-owned capital 与 external capital 的 stakeholder/control surface。
- **CASE-050 Nomada / GRIS → Neva** — `FIT-COMPOSED / CAPABILITY-COMPOSED`：visual-author thesis 先出现，再由 artist + AAA programmers 组成互补 founding capability；研究 cofounder equity/authorship 与普通 hiring 的不同成本。
- **CASE-051 Zachtronics** — `FIT-STRONG + FIT-LOCK-IN`：engineering literacy 长期变成产品语言、niche audience 与 production system，同时 creator 明确报告难以做出不像 Zachtronics 的作品。
- **CASE-052 House House / Untitled Goose Game** — `GRANT / PUBLISHER EXPANSION`：public completion funding 直接增加 local developer/accessibility capability，publisher 再补 audio / platform / market periphery；用于拆 external capital 的不同 capability bundle。
- **CASE-053 Kenny Sun / Circa Infinity → Mr. Sun's Hatbox → BALL x PIT** — `FIT-STRONG / LONGITUDINAL CAPABILITY ACCRETION`：不是新增 fit 标签，而是提醒 capability map 本身会随项目、职业工作、收入与外围协作变化。Kenny 从 Flash / jam / solo commercial artifact，经 Harmonix + weekend shipping、2016 主动搁置过大 Hatbox、2019 重启、Raw Fury release periphery，最终走到 BALL x PIT 的 first team-lead + specialist core；用于把静态的 `capability → project` 改写成可研究的 `project_t → capability_(t+1)`。
- **CASE-054 Limit Theory / Josh Parnell** — `FIT-TRAP`：real-time rendering / engine 强项支撑 infinite procedural thesis，同时持续打开 custom engine、custom scripting、procedural simulation、economy/AI、modding、performance 与 rewrite 的技术投入面。2018 官方先宣告 2000+ ships / full AI 的 engine success、content/gameplay 尚在后面；取消时 creator 又明确记录 `far from feature completion` 且 engine 比 game code 更 solid。它是第一个真正独立/小团队内部的强 FIT-TRAP 锚点。
- **《牛来》 / 信雨萌** — 跨媒介 comparator，不作为游戏 Case。公开访谈显示其从艺术景观背景转入动画、长期自学并以单人核心承担大量传统动画工序。研究重点不是嘲笑粗糙，而是区分：哪些成本被真正重新定义，哪些只是由五年个人劳动替代专业团队。

### Wave 2 — 优先补证对象

- **A Short Hike / Adam Robinson-Yu — PRIORITY A**：CS / software-engineering + game-jam 前史；在大型 Paper-Mario-like RPG 做了一年仍看不到终点后，转向有明确短期限的小型开放世界。重点核 `大项目撤退 → 4-month deadline → tiny open world`，以及 crunchy pixel 3D、对话写法等是否直接降低其弱项成本。它是“不是把 RPG 缩小，而是换一个自己能完成的问题”的强候选。
- **Thomas Was Alone / Mike Bithell — PRIORITY A**：早期 prototype 因能力/时间限制只使用矩形；后续没有补成传统角色资产，而是利用 graphic-design / minimalism 把矩形升级成视觉语言和叙事投射面。强测 `aesthetic conversion + double dividend`。
- **Vampire Survivors / Luca Galante — PRIORITY A/B**：程序/系统、Ultima Online server admin、赌博软件前史 + 极低初始资产投入。尤其适合做 biography fallacy 反例：Galante 后来明确说其赌博行业工作主要是 pipeline automation、front-end、modular UI architecture，而非“从老虎机学会了 Vampire Survivors 设计”。研究应拆开系统能力、现成资产、负面行业经验、定价伦理和成品 reward presentation。
- **Baba Is You / Arvi Teikari — PRIORITY B**：长期实验作 / jam / Clickteam 工具 + Noita artist + puzzle literacy，在 48 小时 jam 中形成核心规则机制。重点核“狭窄工具能力并未被补齐，而是通过规则系统让内容生产更多发生在 puzzle space 而非资产 space”。
- **Downwell / Ojiro Fumoto — PRIORITY B**：从声乐学生、几乎无编程经验切入，通过 game-a-week 快速形成领域能力；Downwell 不是第一作，而是多次短实验后押中的高杠杆核心 mechanic。重点核 `rapid capability acquisition → mechanic compression → mobile/PC legibility`，避免把“歌剧出身”硬解释成设计因果。
- **Sokpop Collective — STUDIO-CADENCE COMPARATOR**：把 game-jam 经验直接制度化为高频发售和 Patreon/Steam 商业结构。这里 project fit 不只是单作，而是“什么样的游戏才适合一个月 / 两个月生产函数”。可与 Landfall 做 `cadence as capability capital` 对照。Wave-2 intake 见 Issue #28。
- **Strange Scaffold / Xalavier Nelson Jr. — ACTIVE PRACTITIONER / PRIORITY A**：项目筛选、contractor constellation、scope rejection、风险分配和高频出货均有大量公开一手言论；2026 仍持续公开 DIDIT 等选题/功能筛选方法。长期 intake：Issue #27。这个对象尤其适合检验“生产方法能否制度化，而不是只依赖创作者直觉”。

### Capability Trap / 反压力线

- **CASE-054 Limit Theory** 已补上第一个真正独立/小团队内部的强 `FIT-TRAP`：局部 engineering capability 持续成功，但 engine maturity 与 shipped-game maturity 明显脱钩。
- **CASE-029 Boundary** 与 **CASE-030 Outpost: Infinity Siege** 仍保留为不同组织尺度的候选压力样本：用于检验强商业/工程/工业化能力是否诱发组织扩张、feature accumulation、表现成本和 fixed burn，而不再承担“唯一 FIT-TRAP 反例”的职责。
- 还需寻找 `FIT-STRONG but commercially failed`：即能力—项目高度适配、产品也完成得好，但市场需求不足或 market access 失败。只有这样才能证明 Capability–Project Fit 不是“成功充分条件”。

---

## Formal Claim Status

本审计框架中的一个**窄命题**已经升级为正式 Claim：

- [C015 — Capability-Shaped Project Formation / 能力反向立项](../claims/C015-capability-shaped-project-formation.md) — `SUPPORTED`。

C015 只主张：

> **显性认识 capability constraints，并把它们用于项目定义，可以成为作者型独立开发的一种可观察设计技术。**

它**不**主张：
- 这种方法普遍提高成功率；
- 所有优秀独游都从 founder capability 反向生成；
- 能力匹配可以替代市场、runway、execution 或 luck。

更强的普遍命题——例如“高效率独立项目通常由能力反向立项产生”——仍未成立。要升级到这种强度，仍需：

- 已有 2 个 `CAPABILITY-SHAPED but commercially failed`（Brigador / The Magic Circle），后续重点转向失败类型分解；
- 已有多种 capability expansion（The Witness / Outer Wilds / House House），仍缺 VC/equity 与真实 control-term 对照；
- 已有 CASE-054 作为第一份强 `FIT-TRAP`；下一步重点不是机械补第二个，而是找成功的 deep-tech stop-condition 对照，验证何时能力会变成 trap；
- `CAPABILITY-COMPOSED` 与 `FIT-LOCK-IN` 各只有一个强锚点，需要第二样本；
- 立项期证据而非成功后叙事；
- 与资金、平台窗口、既有受众和 luck 的分离。
