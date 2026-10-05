# SLAVIC-007 — WoT / WoWP / WoWS / War Thunder 产品结构矩阵

- Type: Comparative Evidence Matrix
- Status: ACTIVE — FIRST PASS
- Last updated: 2026-10-03

## 研究问题

这份矩阵不是比较“哪个游戏更好玩”，而是检验：

> **为什么同属 2010s 俄语区战争载具在线游戏谱系，采用相近题材、成长线和 F2P 结构的产品，最终表现出非常不同的大众化路径？**

尤其检验两个工作假说：

1. **可迁移能力**（品牌、F2P、科技树、服务器、全球运营、军武内容生产）并不能自动解决**不可迁移的核心交互问题**；
2. 战争载具游戏的大众化难度，很大程度由“玩家必须实时解决的运动/瞄准/空间认知问题”决定，而不是仅由题材或商业模型决定。

## 第一轮对照矩阵

| 维度 | World of Tanks | World of Warplanes | World of Warships | War Thunder |
|---|---|---|---|---|
| 核心对象 | 坦克/装甲车辆 | 固定翼飞机 | 大型舰船 | 飞机 + 坦克 + 后续舰艇等多载具 |
| 主要空间问题 | 地面二维位移 + 炮塔朝向 | 持续三维运动 + 姿态控制 | 大尺度二维航行 + 提前量/航线判断 | 依模式与载具不同；飞机要求三维运动，地面载具接近二维 |
| 玩家能否停下思考 | 可以；停车、隐蔽、瞄准都是正常行为 | 基本不可以；持续飞行本身是任务 | 不能真正静止，但速度慢、决策窗口长 | 飞机通常不能；坦克可以；不同模式容忍度不同 |
| 新手已有现实直觉 | 高：汽车/地面驾驶、掩体、视线 | 低：绝大多数玩家没有飞行经验 | 中：方向/速度易懂，但炮击提前量与舰种职责陌生 | 通过控制辅助与模式分层降低门槛 |
| 控制大众化难度 | 相对低 | 高；开发期长期重做 flight model / mouse control | 中；核心难点更多在尺度、节奏和信息而非基本方向控制 | 高，但通过 Arcade / Realistic / Simulator 分层处理 |
| 瞄准问题 | 直接视线 + 炮弹飞行 + 装甲弱点 | 自机高速运动 + 敌机高速运动 + 三维夹角 | 长射程提前量 + 弹道飞行时间 + 航向预测 | 随载具/模式变化；飞行战斗仍有复杂三维预判 |
| 单局节奏 | 短至中；局势离散、接触清晰 | 快、高速、连续 | 中至慢；位置和航线决定较早，接触持续 | Arcade 快，Realistic/Simulator 更慢、更惩罚 |
| 失败可读性 | 较高：暴露、弱点、走位、火力交换较易回溯 | 较低：能量、姿态、视野、角速度等常同时起作用 | 中：位置错误可在数十秒后才显现 | 通过模式层级部分解决；高拟真模式失败原因仍复杂 |
| 核心商业结构 | F2P + 科技树 + 长期收集/升级 | 大体继承 WoT | 大体继承 World of 系列，但玩法重做 | F2P + 多国科技树 + 多模式 + 多载具 |
| 商业模板来源 | Wargaming 的产业转折源头 | 直接继承 WoT 成功模板 | 继承 World of 商业/运营能力 | 非 Wargaming；Gaijin 自有长期载具/在线能力 |
| 能力前史 | 多年战争/策略产品 + Wargaming 运营转型 | Wargaming 品牌/运营强，但飞行并非原有核心专长 | Lesta/Wargaming 需要重建海战尺度、舰种与地图设计 | Dagor + IL-2: Birds of Prey + Apache + Birds of Steel + 在线经验 |
| 对“真实”的处理 | 大幅抽象以服务 PvP 可读性 | 想在 arcade 与 sim 间平衡，长期摇摆 | 保留历史感，但围绕战略/方法论节奏重构 | 把真实性分层为 Arcade / Realistic / Simulator |
| 市场验证关系 | 本身成为军武 F2P 大众市场的重要验证者 | 试图复制 WoT 市场成功 | 直接建立在 World of 系列成功之后 | 项目概念早于 WoT；WoT 后来强化品类合法性 |
| 第一轮判断 | 产品对象本身极适合大众化压缩 | 证明“商业模板可迁移 ≠ 核心交互可迁移” | 证明成功经验可以迁移，但必须重新定义新对象 | 证明另一条长期能力资本路线可以通过模式分层进入大众市场 |

## 证据锚点

### A. World of Tanks：商业模板为什么首先在坦克上成立

Victor Kislyi 在 GDC Europe 2012 已把 World of Tanks 作为 Wargaming 进入 online free-to-play 的核心成功案例，当时公开口径为超过 2000 万玩家，并强调公司从 boxed games 转向 online F2P 的战略。

来源：
- GDC Vault — *World of Free-to-Play - AAA by Wargaming.net*  
  https://gdcvault.com/play/1016771/World-of-Free-to-Play

当前可支持：
- `WoT 对 Wargaming 商业结构是转折` → VERIFIED（公司/创始人层面）
- `WoT 的成功仅靠题材与 F2P` → NOT SUPPORTED

仍需补：
- 更早设计访谈中对 15v15、单载具、局长、瞄准与装甲抽象的明确设计理由；
- 新手 retention / session length / conversion 的同期口径。

### B. World of Warplanes：同模板为何没有自动复制

Wargaming 在 2011–2013 的采访中反复承认：

- 飞机天然要求三维空间判断；
- 玩家必须持续运动；
- “飞机显然比坦克更难控制”；
- 团队长期反复修改 flight model、mouse control 与 joystick balance；
- 控制问题超出团队最初预期。

这不是评论者事后解释，而是开发者在 beta / launch 前后的直接表述。

来源：
- PC Gamer — *World of Warplanes first details...*  
  https://www.pcgamer.com/world-of-warplanes-first-details-will-have-same-gold-experience-economics-as-world-of-tanks/
- Gaming Nexus — *World of Warplanes Interview*  
  https://www.gamingnexus.com/Article/3945/World-of-Warplanes-Interview
- World of Warplanes official — *Mouse Controls Explained*  
  https://worldofwarplanes.com/news/mouse-controls-explained
- World of Warplanes official / GameSpy interview  
  https://worldofwarplanes.com/news/gamespy-world-warplanes-interview/

当前可支持：
- `WoWP 的核心困难部分来自飞行控制/空间认知，而非仅商业运营` → SUPPORTED
- `WoT 商业模板足够跨载具复制` → REFUTED AS STRONG CLAIM

### C. World of Warships：不是把坦克搬到水上

Wargaming 在开发回顾中明确承认：

- WoT / WoWP 的“近距离单载具操控”不能直接平移到巨型舰船；
- 海战需要更 strategic / methodical 的设计；
- 舰种之间形成新的职责结构；
- 地图、尺度、速度和接触逻辑都需要重做。

来源：
- Wargaming — *Getting it Right: World of Warships*  
  https://wargaming.com/en/news/wows_getting_it_right/
- Wargaming — *Level Design in World of Warships*  
  https://wargaming.com/en/news/creating_levels/

这说明 Wargaming 在 WoWP 之后至少在公开设计语言上明确认识到：

> **“World of”品牌与运营体系可以复用，但新载具对象必须重新提炼自己的核心战斗。**

当前可支持：
- `WoWS 是 WoT 的简单 reskin` → REFUTED
- `WoWS 继承商业/运营体系但重做核心玩法` → STRONGLY SUPPORTED

### D. War Thunder：把“sim vs arcade”问题改成模式分层问题

Anton Yudintsev 对 War Thunder 起源的回顾指出：

- 传统飞行模拟门槛过高，市场缩小；
- Gaijin 在主机飞行游戏阶段就必须发明替代控制方案；
- War Thunder 的概念前史早于 WoT 上线；
- 团队后来把不同受众的要求拆到不同模式，而不是要求一个 flight model 同时满足所有玩家。

当前官方模式结构也仍然体现：

- Arcade：最简化、最快、控制和瞄准辅助更多；
- Realistic：更复杂；
- Simulator：高沉浸、高控制要求。

来源：
- War Thunder — *The Big Q&A with CEO Anton Yudintsev*  
  https://warthunder.com/en/news/3275--en
- War Thunder Wiki — *Game modes*  
  https://wiki.warthunder.com/gamemode

当前可支持：
- `War Thunder 的大众化策略包含显式难度/真实性分层` → VERIFIED
- `War Thunder 只是 WoWP 的另一套同质商业模板` → REFUTED

## 第一轮比较结论

### 1. “载具题材”不是一个足够精细的设计类别

坦克、飞机、军舰在美术题材上都属于“军武载具”，但在玩家实时控制问题上差异巨大。

必须至少拆：

- 运动维度；
- 是否允许停止；
- 姿态控制；
- 目标运动速度；
- 玩家是否需要建立三维空间心智模型；
- 从错误决策到惩罚之间的时间延迟；
- 失败原因是否可读。

因此：

> **“军武网游”是商业/题材类别，不足以成为核心玩法设计类别。**

### 2. WoT 的真正优势之一可能是“物理对象本身可被压缩”

工作假说：

> 坦克并不只是“受欢迎的军武题材”，它还是一种非常适合从半模拟压缩到大众 PvP 的载具对象。

原因可能包括：

- 地面运动接近二维；
- 玩家已经拥有汽车式移动直觉；
- 可以停止、观察、瞄准；
- 掩体/视线/装甲朝向可形成直接空间语法；
- 即使去掉大量模拟细节，仍能保留“像坦克”的核心体验。

状态：**H — 需要更多同期设计/用户数据支持。**

### 3. WoWP 提供最重要的内部反例

如果 WoT 的成功主要来自：

- Wargaming 品牌；
- F2P；
- 科技树；
- 军武题材；
- 全球运营；

那么 WoWP 理应高度接近 WoT。

但它没有。

因此 WoWP 对任何“宏观商业模板解释”形成强约束：

> **核心交互对象仍然可以压倒品牌、资本、运营与商业模式优势。**

### 4. WoWS 显示组织学习的另一条路

WoWS 并没有证明 Wargaming 找到了“万能 World of 模板”，反而更接近证明：

> **成功经验的真正可迁移部分，是组织能力，而不是旧玩法。**

可迁移：
- 全球 F2P 运营；
- 科技树与内容生产；
- 历史资料研究；
- 服务器与账号体系；
- 社区与长期更新；
- 大规模军武资产生产。

不可直接迁移：
- 控制；
- 地图尺度；
- 节奏；
- 武器交互；
- 职业/舰种分工；
- 战术可读性。

### 5. War Thunder 展示另一种解决飞行门槛的方法

WoWP 试图在一个统一产品中寻找“够真实又够容易”的控制平衡；War Thunder 更进一步把不同用户需求制度化为模式层级。

这形成一个待继续验证的对照命题：

> **当同一底层模拟无法同时满足大众和硬核用户时，产品分层可能比寻找单一折中点更有效。**

状态：**SUPPORTED AS DESIGN INTERPRETATION，尚未证明为商业成功的主要因果。**

## 对《斯拉夫游戏英雄传说》的生产史意义

四个产品放在一起后，2010s 俄语区战争网游崛起不宜写成：

> “俄罗斯/白俄罗斯玩家喜欢军武，所以出现了一批战争游戏。”

更有解释力的版本是：

> **这里已经存在军武内容、PC 技术、模拟传统和在线运营能力；不同公司随后分别找到把这些能力压缩成大众产品的不同方法。WoT 通过选择可压缩的坦克对象与 F2P 结构打开市场；WoWP 暴露了同模板在三维飞行上的失效；WoWS 迫使 Wargaming重新设计海战；War Thunder 则用长期飞行模拟能力 + 模式分层解决另一部分市场。**

这仍是工作模型，需要销量、活跃、留存、商业收入与同期竞争者进一步约束。

## 下一轮证据缺口

1. WoT 早期 prototype / Alpha 时对局人数、地图、操控与 session length 的设计演化；
2. WoWP 2013–2015 活跃、收入或区域发行数据，避免只用“公司承认较弱”描述；
3. WoWS 早期设计是否明确吸收了 WoWP 的失败经验；
4. War Thunder 各模式真实玩家占比、留存与付费差异；
5. Wargaming 与 Gaijin 在同一时期的招聘/团队专业结构；
6. 俄罗斯/白俄罗斯/乌克兰以外战争载具在线游戏作为外部对照，防止把全球趋势误写成斯拉夫特性。
