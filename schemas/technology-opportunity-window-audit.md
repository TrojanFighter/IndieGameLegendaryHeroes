# Technology Opportunity Window Audit v1 — 全案例技术条件分代与玩家验证路径

- **适用**：所有 `cases/CASE-*.md`、新旧人物Profile的事实核验包、斯拉夫篇正式Case、跨行业技术比较。
- **性质**：在 [CSA](context-situation-action.md) 基础上增加可复用的**技术环境 / 技术获取 / 体验验证**审计。既有文学性人物篇不要硬塞七个相同小标题，应在研究Case和证据表先填，再选对人物选择真正发生作用的部分进入叙事。
- **源基准**：[工业革命003](../cross-industry/industrial-revolutions/003-game-industry-technology-regimes.md)、[004 Unity中间件到AI](../cross-industry/industrial-revolutions/004-unity-asset-store-network-middleware-ai-indie-industrialization.md)、[民间多人游戏两次浪潮](../book/research-notes/grassroots-online-multiplayer-opportunity-window-1999-2025.md)。

## 1. 每个Case必须回答的问题（可以UNKNOWN，不能胡填）

| 字段 | 必须记录 | 禁止的推论 |
| --- | --- | --- |
| `OPPORTUNITY_YEAR` | **作者决定投入/做原型时**的年份，而非1.0或2026年 | 用后来的技术、AI、Steam Direct/UEFN责怪早期作者 |
| `ENGINE_AND_AUTHORING` | 自研/可用引擎、语言、版本、二手技术资产；是否在当时有低价商用授权 | 知道“Unity存在”=当事人会用、用得起、实际采用 |
| `MIDDLEWARE_AND_CAPABILITY_MARKET` | 插件、素材、API、音频/网络、云服务和外围采购的**实际来源**；KNOWN/UNKNOWN | 代码引用一个DLL = 全部系统由该库实现或开发成本可直接推算 |
| `NETWORK_AND_SERVER_BOUNDARY` | 无网络/平台托管/P2P/房主/专服/跨区云；哪些状态局内短暂、局外保留 | 同服人数、全部CCU、总售出数可以直接代替人效或成本 |
| `PLAYER_VALIDATION_LADDER` | 小样→Mod/UGC公开试玩→玩家留存/付费/口碑→验证后组队/融资→EA/Standalone，**实际发生哪些阶段** | 所有项目都经历Mod→获投资→Standalone；mod总能零风险移植 |
| `INNOVATION_RELATION` | 技术创造、现成能力重组、体验需求牵引技术、联合共演进；允许多选和阶段变化 | 只要自研技术就“技术做题”；只要买插件就“懂体验” |
| `STAFFING_AND_UNIT_ECONOMICS` | 实际FTE×人年、外包与中间件费、first playable、paid validation及失败队列；缺数据标UNKNOWN | 用公司年末人数/游戏片尾署名替代首发前开发人年 |

## 2. 时间分代（重叠，而不是整齐换代）

- **T0 Proprietary/Hacker Toolchains**：1990年代及之前以个人底层编程/自研工具、模组源技术、游戏专用编辑器为主；此时已有RPG Maker、Flash、GameMaker等小创作者工具，不能说Unity以前完全无通用软件。
- **T1 General Commercial Engines**：2005–09 Unity普及、GameMaker/Torque等长期并行，使通用低成本、多目标引擎可获取。
- **T2 Composable Marketplace & Direct Market**：2010 Unity Asset Store（从一开始不只卖模型，还含脚本、工作流）、2011 Photon/第三方网络、2012–13 Greenlight/Steam EA、数字直销/移动商店、UGC和社群发行，扩大“买能力而不建部门”。
- **T3 Commodity Multiplayer**：2015 UNet，2015 uMMORPG、2018–19 Mirror社区维护链，Photon系列、Steamworks/独立框架共存；多年积累，而非Mirror独家发明小团队联网。
- **T4 Platformed Social/Co-op**：2020–23多平台合作/语音、Unity NGO 1.0(2022)、Steam/UGC联机/平台服务等可组合；2023《Lethal Company》实物DLL是NGO+Facepunch Transport+Dissonance，**不是Mirror**。
- **T5 Agentic/Generative Production**：2024–26部分代码、图像、音频、测试工作可用模型/Agent辅助；质量、运行时、一致性、IP和实际交付仍需要审计。

这些是**当代可供选择的生态**，而不是“同年所有团队拥有同样技能、授权或社群入口”。跨代案例应按关键节点分别编码，不能用发售年来压平十年经历。

## 3. 技术—设计关系类型（不做相互排斥的英雄排序）

- `CREATED_WINDOW`：团队本身推进当时技术边界，并使某种玩法可行。锚点 early id/Carmack/DOOM。其他引擎作者也可构成此类型，不能因今天用中间件就把它宣判绝迹。
- `RECOMBINED_WINDOW`：在现成引擎、物理、模组、资产或网络基础上重组规则/体验。例：Greene在Arma/DayZ反复试BR规则。
- `INHERITED_WINDOW`：熟练调用已有引擎/商业前作/团队、第三方工具并组合成作者作品。如Gunpoint、The First Tree、Tarkov的Contract Wars前史。
- `PLATFORM_UGC_WINDOW`：创作、托管、即时发行、用户反馈、部分收益在同一平台上进行。如Roblox，2023后UEFN。
- `CO_EVOLUTION`：技术目标与玩法相互塑形；**DOOM不是“只懂技术做题不懂玩家”，不能被新的意识形态标签逆向消除**。
- `UNKNOWN`：还没有确定材料，不为了填表编造引擎或初期资金来源。

**要研究而非预设**：“随着可商品化的基础技术越来越多，成功产品中以体验需求/既有能力重组为主要进入路线者的占比是否上升？”必须定义成功/非成功同代队列、编码规则、起点年份、直接技术原创判断标准和成本，否则DOOM式“罕见”只能是观察与候选假说。

## 4. MOD / UGC → 验证 → Standalone 的“可能路径”，不是标准轨道

```text
可借用的底层世界 / 游戏 / 服务器 / 工具
  → 低成本修改规则与公开玩法试验
  → 玩家采用、留存、观众传播与同侪反馈
  ├→ 继续在Mod/UGC内运营并商业化（不独立）
  ├→ 被原技术/平台方聘用或收编，组织规模化（CS/Valve、PUBG/Bluehole）
  ├→ 主创带着可证明需求与能力另做Standalone（DayZ、Red Orchestra、部分商业续作）
  └→ 停止、失败或保留技巧/作品集（缺分母，必须研究）
```

- **Mod≠Standalone可迁移代码**：引擎授权、IP、分发、玩家账户、网络/物理运行时不同；通常可迁移的是**规则证据、作者能力、受众、声誉和合作关系**，不是所有源代码或资产。
- **Roblox**：Roblox Studio原生的实时多人、跨平台托管、Creator Store、DevEx、即时发布与社交图谱使“产品验证—生产—收入”可以在平台内闭环。不能把平台内成熟游戏强行称“未正式独立发售的技术Demo”。Roblox官方2025年10-K披露年末**>35,500**符合DevEx登记资格、当年**>23,500**确实获得兑换款；这些是资格/支付人头，**不等于开发了35,500款独立游戏或有同等收入**。源：https://www.sec.gov/Archives/edgar/data/1315098/000131509826000024/rblx-20251231.htm
- **Fortnite Creative / UEFN**：Epic于**2023-03-22**上线UEFN Public Beta并同步开放 engagement payouts；Verse、现有玩家基础、托管与跨平台入口使其成为可信的**平台内体验测试**、作品集及收入路径。不能预设UEFN工程可一键出口为独立UE游戏，也不能在缺少公司完整人员/权利资料时杜撰UGC岛→Steam单独项目的直接血缘。官方：https://www.unrealengine.com/blog/unreal-editor-for-fortnite-is-now-available-in-beta ；https://www.epicgames.com/site/news/introducing-unreal-editor-for-fortnite-creator-economy-2-0-fab-and-more
- **历史具体节点**：Arma/DayZ→PLAYERUNKNOWN BR MOD→H1Z1合作→Bluehole PUBG；Unreal Tournament mod→Red Orchestra→Tripwire，Killing Floor mod→独立产品；Roblox→Unity→Lethal Company属于**开发者技能与生产生态迁移**，不是同一款Roblox游戏直接改名移植；必须在叙事里区别。

## 5. 人物/游戏的两张账

**生产能力账**：当时可获得的软件引擎、插件、社区、现有商业代码、团队技能、外包/素材/后端义务与FTE年；不能把大量公共已完成人年的成果计为主创全部自研。

**玩法验证账**：最早哪版原型、几名真实陌生玩家、mod/UGC多少次测试、什么验证了核心体验、哪时转为收费/融资/规模化、此时什么反证被忽略。

这两张账对应不同的独立性：自己拥有资产或IP、可以决定规则、可以独立接触玩家、可以持有收益、能够退出平台，彼此不自动相等。

## 6. 入库写法与维护规则

- Case后端加短小而**针对该案具体证据**的“技术机会窗口与验证路径”附录，不能批量粘贴空模板或判定“所有成功都是体验驱动”。
- **未知写UNKNOWN**，来源若只有开发者本人回顾标P1 retrospective，玩家/二进制/代码则另标来源。
- Reader Profile选择对人物抉择有作用的技术变化写进故事，不在每一页机械列同一张工业年代表。
- 在 `metadata/technology-opportunity-window-matrix.md` 中登记全部 Case 的主路径、初步时代分代和需要补证的变量；未经原始资料核实的具体引擎，不写进机器可作为真值的字段。
- 各版本历史事实采用独立技术史004及工具/平台官方来源；实际采用按游戏开发文档、信用署名、分发文件、代码或同期作者说明核查。
