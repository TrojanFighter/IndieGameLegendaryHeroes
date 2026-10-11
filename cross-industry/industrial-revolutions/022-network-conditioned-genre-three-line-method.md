# 022 — 按玩法×渲染×网络结构严格重建三条生产能力时间线（取代021主图）

> **当前优先入口（2026-10-11实质纠错）：**[025 — 对代表作年份、个人制作能力、联网与类型漏项的反向审计](025-flagship-era-audit-earlier-small-authors-and-missing-genres.md)｜[新12类×大型／中型／微型时代图SVG](025-audited-era-by-genre-three-rails.svg)｜[82条逐案例来源](023-representative-genre-three-rails-1958-2026.csv)。相较023九类图的65条，新增17条早期/缺漏作品，**12类×3轨已有33/36选样角色；赛车、RTS、RPG三类M核心仍缺明确团队FTE证据**。原023/024的27/27只是旧选样宽度，非全产业完整。


> **先看更适合读者的[023标志性作品三线主图](023-first-readable-historical-three-line-atlas.md)／[SVG](023-representative-three-rails-filled-first-pass.svg)。** 本页102格笛卡尔积保留为研究数据库的控制变量及查漏工具，不再是“画全书历史主图之前必须填满的102个格子”。023已选65条有出处的里程碑记录，9个主品类×L/M/I共27个轨道有21个案例锚定，其余保留限制，不能为了排版编造历史首次。


- Status: **CANONICAL RESEARCH FRAMEWORK / 仅有证据的产品锚点，NOT INDUSTRY FIRST OR GENRE-WIDE DIFFUSION**
- Date: 2026-10-10。属于《独立游戏英雄传说》公开产业研究，不涉及其他工程。
- **先看：[022系统矩阵](022-genre-network-lmi-matrix.svg)、[022严格分单元的L/M/I时间图](022-network-conditioned-three-rail-timeline.svg)**。此前 [021](021-three-track-genre-production-capability.md) 仅作为历史草稿，因网络状态混搭、玩法不等价，取消作为首选图。
- 底层数据：[022版本级证据CSV](022-version-specific-lmi-evidence.csv)；[022完整研究格网CSV](022-genre-network-coverage-grid.csv)。**图表不对无数据格子补0或编造首次年份**。

## 1. 上一版本的三个结构性错误

1. “同品类”的逻辑不成立：2008《Left 4 Dead》是合作关卡射击、2021《Valheim》是合作建造生存、2023《Lethal Company》是合作恐怖拾荒。三者共享联机多人底座，**不构成一个严格玩法子品类的L→M→I链**。
2. 同作品的网络模式本身影响产能。《Stardew Valley》2016纯单人已上市，**2018多人**才上线，还引入Chuckelfish工程师Tom Coxon完成主要网络代码；《Overcooked》2016的两人组用本地合作完成产品，在线合作直到2018续作并与Team17共同制作。不能用单人时代的开发者规模证明他们独自完成联机工程。([Stardew官方2018](https://www.stardewvalley.net/stardew-valley-1-3-multiplayer-update-is-now-available/)，[ConcernedApe 2018](https://www.stardewvalley.net/update-on-1_3/)，[Overcooked! 2 原创作者访谈](https://news.xbox.com/en-us/2018/08/07/return-to-the-onion-kingdom-overcooked-2-xbox-one/)，[Team17 FAQ](https://www.team17.com/news/overcooked-2-faq))
3. 3D“破坏”跨技术架构混搭。2008 Frostbite场景破坏、2020《Teardown》离线体素、2020《Noita》离线2D逐像素、2023《BattleBit》多人低模可破坏，不是同等玩法/联网保真任务；破坏技术应作为**物理/世界可变性轴**，而非笼统当独立genre。

## 2. 生产能力单元（cell）应怎样定义

**同类比较的真正主键**：

```
cell = (gameplay_subgenre,
        render_form_and_fidelity_tier,
        player_interaction_mode,
        connectivity_and_session_architecture,
        peak_concurrent_players_band,
        world_persistence_class,
        content_scope_tier,
        physics_mutability_tier,
        delivery_substrate)
```

不是“同样叫射击/开放世界”就能连接年份。每种玩法是**根分类 + 细分体验**；2D/3D和保真规格不能混同；网络是下面至少六类（**类别而非线性难度等级**）：

| N | 联机/交互实现 | 典型新增生产负担 | 特别警惕 |
|---|---|---|---|
| **S0 离线单人** | 本机玩家、非实时网络权威 | 玩法、存档、本地性能/QA | 仍可能非常复杂；不代表低总成本 |
| **C1 同机本地多人** | 分屏/共屏/同机多控制器 | 多输入、相机、同屏性能、局部UI | 不需要网络同步，但不等于一人游戏 |
| **L2 局域网/串口多人** | 同步网络会话、较短典型时延 | 同步/确定性、序列化、掉线与不同机器状态 | **有网络代码**，不能将1993《DOOM》的LAN模式记成互联网在线 |
| **O3 小会话互联网多人** | 朋友房间/房主或平台中继，常见2—16人（不作硬阈值） | 网络延迟、状态同步、权限/会话恢复/匹配、版本差异 | 是否房主/平台转发需按项目核查；合作与对抗也需另标 |
| **D4 专门服务器会话** | 由专门服务器或权威服务组织的多人 | 服务器成本、状态复制、延迟补偿、匹配、反作弊、压力测试 | 玩家数和服务器架构要分列，不能从人数猜服务器所有权 |
| **P5 跨会话持续在线世界/服务** | 玩家持久账号/资产/经济或世界 | 持久数据库、一致性、运维、风控、事务安全、滚动更新 | **与D4不构成简单升级链**；持久性需单独以P轴编码 |

重要：S0/C1/L2/O3/D4/P5不是单调增加的“难度等级”。真正的网络工程复杂度是 `sync_mode × player_count × PvP/PvE × authority × persistence × topology × external_platform_subsidy`。同样8人，快节奏PvP射击可能比慢速回合策略要求更严的同步和作弊治理；同样可选专用服务器，开发者是否需要自己提供官方服务器会极大改变成本。

**其余正交维度，必须在CSV记录：**
- `gameplay_subgenre`：平台跳跃/竞技战场FPS/生存建造/农场经营/合作厨房/合作恐怖拾荒/物理沙盒；**合作是交互模式，不是独立玩法genre**。
- `render`：2D像素、2.5D、3D低资源、3D高资产。不能把《Minecraft》低规格体素模拟和《GTA III》任务城市等价。
- `persistent_world`：P0单局重置，P1本机或房主存档，P2多人可重入世界，P3账号与服务持久状态；与联网类分离。
- `physics`：F0预设/简单碰撞、F1可移动刚体、F2局部建筑结构破坏、F3体素/逐像素系统仿真。
- `substrate`：自主商用成品Standalone、依附宿主MOD、UGC平台地图、工具辅助但独立发行。**MOD/UEFN作品不能等同开发整个联机服务器的能力**。
- `fidelity_target`：同年代商业规格/复古规格/当代高规格；如果变更画面目标、资产密度、地图规模，**标注生产路线切换**，不宣称同等规格能力下沉。

## 3. 三条线L/M/I与开发者人数分别登记

- **L 大型专业生产基础**：大公司/专业平台专用研发、大资本或跨项目专职支撑的交付。此条是“整体生产组织资源”，**不等于本游戏核心超过50人**。
- **M 中型开发核心**：实际承担主要开发的5—49人项目核心。标明`corporate_internal`（大公司内部小组）、`independent_publisher_backed`、`independent_self_funded`；**任何M不自动是中型独立公司**。
- **I 个人/微型创作核心**：约1—4人创作主导。若依赖外部网络程序员、发行商技术或母游戏服务，将`external_network_development`和`network_substrate`明示，**不能声称微团队独力完成了全部在线技术栈**。
- 三层可以存在**同项目重叠**（例如5人公司内部团队既有M核心又享L支持），比较必须分出谁提供发动机、服务器、QA、内容与推广。资源保障不能当作“技术降维”的自发创新。
- 年份必须写`version_or_mode_release_date`：同一标题单人与后来联网更新应分别记录（**Stardew 2016与2018**；《Overcooked》1/2作为受控机制对比）。

## 4. 系统图和研究路由

**矩阵图**先用玩法×视觉/保真族定义行、网络体系定义列，格内最多分别记录L/M/I的**可证产品年**，空格写`?`并保持UNKNOWN，不意味着从未出现；另有`counterexamples/changed_scope`。

**轨道图**只对已命名的`gameplay × render × net`单元画独立L/M/I：每个产品标注年份、开发主体、**外部支持**。不把《Valheim》《Left 4 Dead》《Lethal Company》放同一技术产品轨道；可在上级“3D online co-op技术底座”中另绘**非同品类**辅助参照。

**网络转换图（最重要的一组因果证据）**：

| 案例 | 原有模式 | 扩展联网模式 | 增加的开发资源 | 因果可用性 |
|---|---|---|---|---|
| Stardew Valley | 2016 S0 单人农场 | 2018 O3 4人网络房主共用存档 | Tom Coxon 完成主要联网代码；同时ConcernedApe与Chucklefish协助测试 | **同一游戏同一玩法**，高可比性；同时有补丁与内容变化 |
| Overcooked | 2016 C1 本地2—4人厨房合作 | 2018 O3《Overcooked! 2》4人在线、本地均可 | 原作两人工作室通过Team17共同开发第二作 | **续作对比**，增加网络同时也有新内容；不能算严格控制实验 |
| DOOM | 1993 S0单人关卡FPS | **同年L2 IPX LAN 最多4人** | id软件自研底层网络与同步 | 同一标题支持双模式，证明**LAN≠互联网在线**；不是先有单机很多年后才联网 |

[《DOOM》原始 IPX网络源代码](https://github.com/id-Software/DOOM/blob/master/ipx/DOOMNET.H)有`MAXPLAYERS 4`与deathmatch字段，一手检验1993产品已有网络能力；不能把这条LAN轨道与2002《Battlefield 1942》大规模Internet专服混为一类。

## 5. 三类研究尤其应当严禁混用

1. **同类游戏但网不一样**：2016单人农场≠2018在线合作农场；1993四人LAN FPS≠2002 64人专用服务器FPS≠2023 254人专服FPS。《BattleBit》官网店页实证2023年3位署名主创/254人和低多边形/破坏，展示三人作者可以做到相当高的N，但这并不意味着制作总成本或运维完全由3人承担。([Steam](https://store.steampowered.com/app/671860/BattleBit_Remastered/))
2. **同网但玩法不一样**：2008合作关卡射击《Left 4 Dead》、2021合作生存建造《Valheim》、2023合作恐怖《Lethal Company》都能在线，但不是一个严格genre。Valheim官方确认玩家数上限10、P2P会话可选独立专服、Iron Gate不提供官方服务器；不能认为P2P和官方后端一回事。([Valheim FAQ](https://valheim.com/faq/))
3. **破坏同名但计算架构不一样**：离线《Teardown》体素沙盒、《Noita》2D逐像素、联网FPS《BattleBit》可破坏地图、Frostbite大厂局部战场破坏，分别按`physics F2/F3`、`network mode`和`render`对齐。硬把它们画在一条“物理破坏下降”曲线会再次犯原来错误。

## 6. 证据到年表的唯一允许操作

合格新增研究必须提供 `cell_id`、`year`、`role`、`version`、`project_size`、`external_network_work`、`hosted_substrate`、`source_url`，至少改变一个可比较的格。不能再收集无助于填三条生产时间线的作者收入平台总数。

**证据门禁**：官方首次发布日期/功能支持优先；商业实发产品优先于原型/模组；无核心人数证明时角色写`L_SUPPORT / M_CANDIDATE / I_ORIGIN_ONLY`，图用空心/附注。某项目在N3或N4区间上线不证明它覆盖之前所有网络模式；每个产品可以产生多个版本级记录但**作者主体数不能跨模式累计**。

**剩余硬问题**：目前仍没有同一玩法同一网况同一保真规格下的行业第一次大中小商业生产年份，更没有所有生产者的连续数量级。我们应先系统填矩阵和三条线，随后用ZXDB/Steam/官方财报作为“普及量”校验，而非替主图画不相干的人头曲线。
