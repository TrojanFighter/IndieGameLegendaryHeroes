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
- `FIT-TRAP`：强项反而诱发不必要复杂度 / 固定成本 / feature accumulation；
- `UNKNOWN`：缺少立项期证据。

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
- **CASE-026 Brigador** — 作为失败压力样本，检查强技术/美术执行与市场表达之间是否存在能力—产品错配。
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

- **CASE-029 Boundary** 与 **CASE-030 Outpost: Infinity Siege** 可作为候选压力样本：重点不是“中国团队不会独立游戏”，而是核验强商业/工程/工业化能力是否诱发了组织扩张、feature accumulation、表现成本和固定 burn 的提前上升。
- 后续必须继续找**真正独立、小团队内部**的 `FIT-TRAP` 失败例，避免只拿大组织或中国项目充当反例。
- 还需寻找 `FIT-STRONG but commercially failed`：即能力—项目高度适配、产品也完成得好，但市场需求不足或 market access 失败。只有这样才能证明 Capability–Project Fit 不是“成功充分条件”。

---

## Claim Gate

当前只作为审计框架，不立即新增正式 Claim。

未来若要形成类似：

> `高效率独立项目往往不是缩小行业标准产品，而是围绕创作者的能力不对称重新定义产品。`

至少需要：

- 3–5 个结构不同的强正例；
- 2 个以上失败/反压力样本；
- 至少 1 个 `FIT-STRONG but commercially failed`，防止把 fit 当成成功充分条件；
- 至少 1 个 `FIT-TRAP`，证明强项也可能把项目带向错误复杂度；
- 立项期证据，而非纯事后复盘；
- 能把能力适配与资金、市场窗口、既有受众、运气分开；
- 有案例能真正反驳该命题。
