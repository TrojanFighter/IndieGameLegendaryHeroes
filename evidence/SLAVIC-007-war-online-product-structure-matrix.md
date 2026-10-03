# SLAVIC-007 — WoT / WoWP / WoWS / War Thunder 产品结构矩阵

- Type: Comparative Evidence Matrix
- Program: 《斯拉夫游戏英雄传说》
- Status: ACTIVE — FIRST PASS
- Last updated: 2026-10-03

## 研究问题

> **为什么在相近的军武受众、F2P 长线运营和科技树结构下，World of Tanks、World of Warplanes、World of Warships 与 War Thunder 会形成截然不同的产品结构与市场结果？**

本矩阵不试图用单一变量解释成败，而是把“商业模板能迁移什么、具体载具问题又迫使团队重新发明什么”拆开。

## 一、四项产品结构矩阵

| 维度 | World of Tanks | World of Warplanes | World of Warships | War Thunder |
| --- | --- | --- | --- | --- |
| 主要生产谱系 | Wargaming 长期战争 / 策略产品 → WoT | Wargaming 在 WoT 成功后主动扩展 `World of...` | Wargaming + Lesta；在 Tanks / Warplanes 后建立海战产品 | Gaijin + Dagor；IL-2: Birds of Prey / Apache / Birds of Steel 等军事航空能力前史 |
| 基本空间 | 地面为主；导航主要在二维平面完成 | 完整三维空域 | 水面导航主要在二维平面，但射击包含远距离弹道、提前量、视野 / 隐蔽 | 按载具与模式变化；空战完整三维，陆战地面二维主导，后续扩展海战与联合载具 |
| 载具运动约束 | 可停、可倒车、可利用掩体；车体与炮塔可相对分离 | 必须持续运动；姿态、速度、高度、转向耦合 | 不能瞬停 / 瞬转，惯性明显，但无需持续管理完整飞行姿态 | 模式分层；Arcade 降低操控负担，Realistic / Simulator 保留更多飞行 / 物理约束 |
| 新手控制模型 | WASD 驾驶 + 鼠标炮塔 / 瞄准；官方提供 auto-aim、arcade/sniper 等辅助 | 团队长期重做 flight model 与 mouse controls；甚至使用 AI 辅助飞机朝鼠标方向飞行 | WASD 航行 + 鼠标瞄准；难点从“控制船体姿态”转向提前量、航向预测、武器切换和视野 | 不用一个控制深度强迫所有玩家；不同模式分别提供简化、真实和模拟层级 |
| 核心认知门槛 | “先会开，再学战术”；驾驶直觉接近日常车辆 | 玩家需要先学会“如何在三维空间里存在”，然后才能稳定进入战术层 | 载具慢、转向可预测；主要学习的是未来位置、射击提前量、隐蔽和职业分工 | 把认知门槛分层：新人可先 Arcade，深度玩家再进入 Realistic / Simulator |
| 战斗节奏 | 中速；移动—停稳—瞄准—射击节奏清晰 | 高速；持续运动使目标获取、瞄准和空间判断同时发生 | 明显偏慢且更 methodical；必须提前规划转向、航线和射击窗口 | 强烈依模式和载具变化；Arcade 快，Realistic / Simulator 更惩罚失误 |
| “真实性”处理方式 | 大量抽象后保留装甲、穿深、模块、载具差异等军武感 | 原计划是 arcade flyer + simulator mixture；难点在简化后仍要让“飞行本身有意义” | 开发者明确拒绝把它做成“水上坦克”；保留舰种、弹道、隐蔽、惯性，但重构为可读的海战动作 / 策略 | 不在“真实性 vs 大众化”之间二选一，而是通过 Arcade / Realistic / Simulator 分层承载不同真实性 |
| 成长 / 长线 | F2P、科技树、载具收集、长期运营 | 明确继承 WoT 式 tech tree、统一账户 / Premium 等框架 | 延续科技树、历史载具、长期更新、PvP / PvE 等运营能力 | F2P、research tree、载具研究 / modifications；2013 年已公开重构 research progression |
| 可迁移的公司能力 | 服务器、账户、运营、历史载具内容、F2P、社区、全球市场 | 上述能力大多可以直接继承 | 上述能力继续继承，并由 Lesta 提供海战开发能力 | Dagor、军事载具建模、飞行 / 物理、主机控制、在线产品经验 |
| 不可直接迁移的问题 | — | 飞机三维操控、持续运动与高速交战本身不能从坦克模板解决 | 舰船尺度、缓慢惯性、超远距离弹道、隐蔽与舰种关系必须重新设计 | 多真实性层、不同载具域的控制与伤害模型必须由自身传统解决 |
| 当前证据支持的核心判断 | WoT 是 Wargaming 公司史明确转折点 | 同公司、同商业模板并未复制 WoT 规模；Wargaming 公开承认更高学习曲线 | “World of”组织资产可迁，但开发者主动重新定义海战，而非复制坦克交互 | 项目 / 能力前史早于 WoT；WoT 更像市场验证，而非起源原因 |

## 二、关键来源与证据

### A. World of Tanks：为什么坦克交互具有低第一层门槛

World of Tanks 官方控制指南显示，核心驾驶就是 WASD，炮塔 / 火炮由鼠标控制；同时提供默认 Arcade aiming、Sniper mode 和 Auto-Aim。

Source:
- World of Tanks official, `Controls and Firing`
- https://worldoftanks.com/en/content/guide/newcomers-guide/game_controls/
- Evidence class: P0 / OFFICIAL-LIVE-DOCUMENTATION

官方 Random Battles 的标准目标仍是“占领基地或摧毁全部敌车”，15v15 是长期标准格式之一。

Source:
- World of Tanks official rules / Arcade Cabinet pages using Random Battles baseline
- https://worldoftanks.com/en/news/general-news/arcade_cabinet/
- Evidence class: P0 / OFFICIAL-LIVE-DOCUMENTATION

Interpretation:

> **WoT 并非“简单”，而是把第一层操作建立在高度熟悉的地面驾驶直觉上；复杂度主要在之后的装甲、穿深、视野、地图、位置与载具知识中逐步展开。**

Status: SUPPORTED

### B. World of Warplanes：同商业模板撞上不同物理对象

2011 年 Wargaming 制作人 Anton Sitnikau 已明确说，World of Warplanes 会采用 `arcade flyer + simulator` 的混合，并刻意简化控制，让玩家把注意力放在战斗而不是“操作飞机”上。

Source:
- World of Warplanes official mirror of GameSpy interview, 2011-08-18
- https://worldofwarplanes.com/news/gamespy-world-warplanes-interview/
- Evidence class: P0 / CONTEMPORANEOUS-DEVELOPER-INTERVIEW

2013 年 Executive Producer Alex Zezulin 又说明，flight mechanics 与 mouse controls 在 beta 中经历持续重做。

Source:
- Gaming Nexus, `World of Warplanes Interview`, 2013-04-14
- https://www.gamingnexus.com/Article/3945/World-of-Warplanes-Interview
- Evidence class: P0/P1-adjacent / CONTEMPORANEOUS-DEVELOPER-INTERVIEW

World of Warplanes 官方在 2013 年还公开说明，默认 mouse control 使用 AI 帮助预测并引导飞机运动，证明“把飞行映射到鼠标直觉”本身就是核心产品工程问题。

Source:
- World of Warplanes official, `Mouse Controls Explained`, 2013-10-17
- https://worldofwarplanes.com/news/mouse-controls-explained
- Evidence class: P0 / OFFICIAL-CONTEMPORANEOUS

2014 年 Wargaming 方面在 PAX Australia 明确承认 WoWP `was not as successful as World of Tanks`，并把更高难度曲线直接归因于三维环境与飞机控制；同时暂停亚洲发行、继续尝试更 arcade、更易理解的设计。

Sources:
- https://futurefive.co.nz/story/tanks-for-the-memories-wargamingnet-at-paxaus-2014
- https://vicbstard.com/wargaming-net-at-paxaus-2014/
- Evidence class: P1 / CONTEMPORANEOUS-COMPANY-INTERVIEW

Victor Kislyi 在 TGS 2014 又给出更强的内部反思：团队在 WoT 成功后以为已经掌握“成功秘诀”，但后来发现 Tanks、Warplanes、Warships 实际上是不同游戏，成功公式不能直接复制。

Source:
- Game*Spark, TGS 2014 Victor Kislyi interview
- https://www.gamespark.jp/article/2014/09/24/51803.html
- Evidence class: P1 / CEO-CONTEMPORANEOUS-INTERVIEW

Interpretation:

> **WoWP 是最强内部反事实：账户、Premium、科技树、军武内容生产和全球运营都能迁移，但三维高速飞行这个核心交互对象不能靠旧模板消解。**

Status: STRONGLY SUPPORTED

### C. World of Warships：不是复制坦克，而是重新定义“可玩海战”

Wargaming 官方设计回顾明确指出：前两作都是“close command of one vehicle”，但这一点不能直接翻译到舰船的尺度；团队把 WoWS 定义成更 strategic / methodical 的整体战场，并明确讨论舰种差异、舰船尺度与海洋空间。

Source:
- Wargaming, `Getting it Right: World of Warships`
- https://wargaming.com/en/news/wows_getting_it_right/
- Evidence class: P1/OFFICIAL-DESIGN-RETROSPECTIVE

官方 2015 年回顾显示 WoWS PvP 使用 12v12，并已经形成 PvE、Ranked、信号旗、迷彩等长期运营内容。

Source:
- Wargaming, `Wargaming's Top 10 Moments of 2015`
- https://wargaming.com/en/news/wargaming-top-news-2015/
- Evidence class: P0/P1-adjacent / OFFICIAL-CONTEMPORANEOUS

当前官方 / 官方 Wiki 的基础教学仍强调：舰船不能瞬间加速、停止或转向，玩家需要提前规划航向，并在远距离射击时计算移动目标的提前量。

Source:
- World of Warships Wiki, `Game Basics`
- https://wiki.worldofwarships.com/Ship:Game_Basics
- Evidence class: P0 / OFFICIAL-LIVE-DOCUMENTATION

Interpretation:

> **WoWS 的大众化路径并不是让舰船“像坦克一样灵活”，而是接受慢速、惯性和远程弹道，再把操作难点从载具姿态控制转成预判、航线和信息管理。**

Status: SUPPORTED

### D. War Thunder：通过模式分层而不是一次性压平复杂度

War Thunder 官方 FAQ 明确把三个主要 PvP 层级区分为：

- Arcade：简化、适合新手；
- Realistic：更强调历史 / 物理真实性；
- Simulator：面向更高沉浸与操控复杂度。

Source:
- War Thunder official FAQ
- https://warthunder.com/en/game/faq
- Evidence class: P0 / OFFICIAL-LIVE-DOCUMENTATION

官方 Wiki 对 Arcade 的描述进一步说明：它是最简化、最易学习、节奏最快的模式，并用更容易的控制、强化机动和瞄准辅助降低进入门槛；Realistic / Simulator 则逐层减少辅助、增加物理与历史约束。

Sources:
- https://wiki.warthunder.com/gamemode
- https://wiki.warthunder.com/gamemode/realistic_battles
- Evidence class: P0 / OFFICIAL-LIVE-DOCUMENTATION

2013 年官方开发日志已经显示 War Thunder 的研究树 / progression 是长期产品结构的一部分，并按历史时期与战斗效能组织载具。

Source:
- War Thunder official, `Developer's Diaries: New Progression System`, 2013-11-26
- https://warthunder.com/en/news/350/
- Evidence class: P0 / CONTEMPORANEOUS-OFFICIAL

结合 `SLAVIC-003` 中 Anton Yudintsev 对项目起源的回顾，可以把 War Thunder 的产品策略理解为：

> **不把真实性整体删除，而是通过不同模式让玩家选择自己承受多少真实性。**

Status: STRONGLY SUPPORTED

## 三、可以开始支持的跨产品命题

### M1 — 商业模板比核心交互更容易迁移

**Status: SUPPORTED**

Wargaming 成功迁移了：

- F2P；
- 科技树；
- 账户 / Premium；
- 历史载具内容生产；
- 全球社区 / 服务器 / 市场能力。

但 WoWP 表明，这些并不能替代新的控制模型与空间认知设计。

### M2 — “载具本体”是产品市场规模的重要中介变量

**Status: SUPPORTED, NOT CAUSALLY CLOSED**

当前证据支持：

- 坦克：地面运动 + 可停 + 炮塔独立，使第一层操作最容易被日常驾驶经验映射；
- 飞机：高速 + 持续运动 + 三维姿态，使玩家必须先解决空间存在感；
- 舰船：也有持续运动与惯性，但主要留在二维平面，速度更慢，因而可把复杂度转移到提前量、隐蔽和职业关系。

但不能写成：

> “二维一定成功，三维一定失败。”

War Thunder 的存在本身就是反例。

### M3 — War Thunder 提供了 WoWP 没有采用的另一种“大众化模拟”解法

**Status: SUPPORTED / CAUSAL LINK UNVERIFIED**

WoWP 试图在一个默认产品中同时做到“足够简单 + 足够像飞行”；War Thunder 后来更明确地把不同真实性需求拆成 Arcade / Realistic / Simulator。

这可以支持“模式分层是一种有效问题重切”，但当前不能写成：

- Gaijin 是因为观察 WoWP 失败才采用分层；
- War Thunder 的成功主要由三模式结构单独造成。

这些因果仍未证。

### M4 — World of Warships 证明“成功模板迁移”最重要的不是复用玩法，而是复用组织资产后重新解决问题

**Status: SUPPORTED**

WoWS 没有否定 Wargaming 的 World of 商业体系，而是：

1. 继承科技树、F2P、历史内容、运营、品牌与市场能力；
2. 放弃把坦克近身载具操控直接复制到舰船；
3. 重新围绕舰船速度、尺度、弹道、隐蔽和舰种关系设计产品。

因此它与 WoWP 构成非常强的公司内部对照。

## 四、一个更强的“斯拉夫战争网游产业簇”工作模型

现在可以把原先模糊的“这里为什么盛产战争网游”拆成至少四层：

1. **能力资本层**：长期 PC、军武、模拟、历史载具、美术 / 物理 / 引擎能力；
2. **商业验证层**：WoT 把军武 F2P 从小众假设推成全球大市场；
3. **组织复制层**：服务器、科技树、F2P、社区、历史内容生产等可跨项目迁移；
4. **问题重切层**：每种载具必须重新解决自身的控制、空间、节奏与真实性问题。

因此目前最有力的工作假说不是：

> “斯拉夫玩家更喜欢军武，所以出了很多战争游戏。”

而是：

> **俄语 / 东欧 PC 产业长期积累了军武与系统型能力；WoT 又验证了全球大众市场；随后不同团队把既有能力与新的 F2P / 在线发行条件重新组合。但真正能形成大产品的团队，仍然必须为具体载具重新定义交互问题，而不能只复制题材与商业模型。**

Status: WORKING HYPOTHESIS

## 五、当前不能支持的强结论

- `WoWP 弱只是因为飞机三维运动。`
- `WoWS 成功只是因为船比飞机更容易控制。`
- `War Thunder 成功主要因为有 Arcade / Realistic / Simulator。`
- `WoT 直接导致 WoWS 或 War Thunder 的全部设计。`
- `俄罗斯 / 白俄罗斯 / 乌克兰玩家天然更喜欢军武。`
- `四款游戏足以证明整个斯拉夫产业的因果结构。`

## 六、下一轮最值钱的证据缺口

1. WoT / WoWP / WoWS 早期留存、DAU、注册、付费率、地区结构的可比数据；
2. WoWP 2.0 前后 onboarding / retention 的变化；
3. Lesta 是否在开发 WoWS 时明确引用 WoWP 的失败经验；
4. War Thunder 2012–2015 Arcade / Historical / Full Real Battles 的用户占比；
5. 玩家调查或 telemetry：不同空间维度 / 控制门槛与流失之间是否有数据联系；
6. Wargaming 与 Gaijin 的团队配置、内容生产成本和 live-ops 组织规模对照；
7. 把本矩阵扩展为“产品结构 + 商业结果 + 团队能力资本”的三层比较，而不是只看玩法。
