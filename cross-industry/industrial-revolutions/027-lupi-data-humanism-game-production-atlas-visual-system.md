# 027 — 从 Giorgia Lupi《The Digital in Architecture》学到什么：游戏生产能力演化地图的视觉设计规范

> **配套图形语言试验板：**[027 — 九例作品的小型 glyph 可视化SVG](027-project-glyph-visual-language-study.svg)。展示角色、能力主题、联网模式、交付阶段及外部支援的独立编码；**仅图形语法试作，不代表已经完成新主图**。


- Date: 2026-10-12
- Status: **DESIGN REFERENCE AUDITED / PRODUCTION BRIEF**。已核对 Pentagram 项目陈述、Lupi本人项目与 Data Humanism 宣言，以及原版折页PDF可提取图例。**不是已经完成一张新正式主图**。
- Scope: 《独立／斯拉夫游戏英雄传说》的公共游戏产业历史研究。仅引用本库的 [023 90条节点CSV](023-representative-genre-three-rails-1958-2026.csv)、[026 12×3参考图](026-audited-era-twelve-genre-complete-tracks.svg)、[020 ZXDB真实复算](020-zxdb-1982-1992-measured-supply-and-genre.md) 和其他既有史料，不接触KWP项目。
- Reference: [Pentagram一手项目说明](https://www.pentagram.com/work/the-digital-in-architecture/story)、[Lupi本人完整项目](https://giorgialupi.com/the-digital-in-architecture)、[五折页原件PDF](https://pentagram-production-uploads.s3.amazonaws.com/nullce0a8c37-7943-494f-9d14-0b68dab64edf/Space10_Digital_Arch_Timeline.pdf)、[Lupi《Data Humanism》](https://giorgialupi.com/data-humanism-my-manifesto-for-a-new-data-wold/)、[Vizzuality《Evolution of the Web》设计复盘](https://www.vizzuality.com/project/evolution-of-the-web)、[Calculating Empires](https://calculatingempires.net/)。

## 一、观察，不是风格形容词：对方真正怎么做

| 一手原作动作 | 为何有用 | 用在游戏技术史要怎样变形 |
|---|---|---|
| 以**建筑项目**而非“明星建筑师”作为历史主体；精选160个作品 | 用户先看到人的环境/作品实际实现了什么，不是名人清单 | 作品核心玩法体验为第一入口；John Carmack、Koshutin等作为生产者信息，不挤占图面中心 |
| 所有项目有含多层信息的**小型图形 glyph**（创新、功能、形态、规模、位置、完成状态等） | 节省文字篇幅、允许密集浏览，多条件可以共存 | 每个游戏独立视觉编码：玩法/视觉、独创技术、**真实的开发人数口径**、外援、网络/发行状态。禁止“一个橙点代替所有事实” |
| **设计运动是地图背景纹理**，一个项目可跨多个运动 | 体现横向时代思潮，避免做160条并列轨道 | 画受证据支持的生产范式背景：8位机卧室开发、Shareware/MOD、自助引擎与数字分发、托管UGC。它们可同时存在而非相互排斥，不能假装严格分期或规模占比 |
| **工具和数字技术是图底部的一条独立带**，原作挑选28个工具 | 解释作品与可复用的技术底座，不与作品打架 | 游戏引擎/编辑器/网络库/发行与UGC宿主分别按出现/开放/商用年份记工具节点，不与开发者的产品首发年混为一谈 |
| 近五英尺宽的**五折页**，少数重要项目有放大的叙事注释 | 全图、时期局部、单项目可逐级阅读；允许高密度而不使每个字都同等重要 | 出版版：宽幅主图+3张局部+图例/史料附录；在线版同数据缩放、高亮与证据卡片；不把90项都设成同号18px文字 |
| 为排版改变局部年代宽度，却**另外显示真正逐年分布** | 直面设计压缩带来的失真 | 主图默认严格线性`x=(year-1958)/(2026-1958)`；如启用非线性艺术排版，必须标出断轴和另给真实线性小图。不可将2018放到2020右侧 |
| 复杂图例位于折页**背面**，可以翻开对照 | 把复杂字段解释放在周边，主体更清晰 | 正面只需6个简易图例；背面/下层/弹出卡承载完整代码簿；不要求小读者从未解释的彩虹配色猜出含义 |
| 并行的16页报告承担背景解释 | 总图不必承载史料与所有方法论 | 正文解释“为何能做”“如何商业化”，图负责可比较的空间定位；正文/案例页带GitHub证据ID |

以上可在 Pentagram 一手页面与其[原PDF折页图例](https://pentagram-production-uploads.s3.amazonaws.com/nullce0a8c37-7943-494f-9d14-0b68dab64edf/Space10_Digital_Arch_Timeline.pdf)核查。本章学习**设计原理，不复制对方的视觉造型和内容**。

### 从 Lupi《Data Humanism》追加的三条约束

1. **数据不等于不容置疑的真实。** 我们的`project_core_FTE`很多仍是未知数；不能从一个完整 credits 名单或者工作室人数擅造准确开发人年。
2. **上下文比漂亮的单个数字重要。** 1993《Ken's Labyrinth》单人自研技术、2018《DUSK》现成引擎与New Blood发行，是两套生产约束，不是“两个橙色独立FPS节点”。
3. **密集不等于晦涩。** 给读者一个总览入口、可阅读的放大局部、可以追溯的详细说明；符号语法必须一贯且可学习，而不是每条历史独立手绘一套代码。

## 二、结构：一幅完整的多层历史地图，不是36条等权平行轨

**总图版式（准确年代 x 轴贯通每个层）：**

```
横向 1958 ───── 1980 ───── 1990 ───── 2000 ───── 2010 ───── 2026
A 背景层    受证据支持的创作、分发与组织环境（浅纹理，重叠而非依次替换）
B 作品层    [2D 规则/内容] [3D 实时世界] [联网/可破坏/服务] 等“能力生态”
            每个作品只有一个可核的年代主坐标，可存在多个技术/玩法标签
            ★ 放大12个关键作品，其它保留可识别的glyph及编号
C 路线层    仅画证据确凿的MOD→standalone、同作者→续作、共享引擎/技术迁移
D 工具层    ZX/家用开发包 / Shareware / GameMaker / Unity / UE4 / Steam / UEFN
E 统计层    只有经实测数据库的年产量/作者量才能以密度或宽度呈现（ZXDB限平台）
```

- L/M/I是**点击或阅读细节时展开的生产组织对照视图**；在首页全局改为项目glyph编码，不让36条横线消耗全部版面。
- 12个旧品类是**筛选分类**而非必须逐一平分地图高度。若以体验/技术负担构图，一款作品可以有多个`genre`与`technology`标签，但保留一个清楚可解释的定位锚点。
- 时间真实线性。作品拥挤时只允许y方向错位、侧向标签、细节放大或展开局部，**不改变真实的x(year)**。
- 时间轴下方的工具节点注明：开发/发布/开放可得/广泛商用是不同年份与不同命题，不得默认工具一上市“人人会做”。
- 历史运动/价值网络背景是**定性研究框架，不能用色带面积冒充开发者/销售总量**；如缺数量，带宽恒定。图上用`MODEL`或`INTERPRETATION`标记。

## 三、Project Glyph 视觉语法：最多六个直观编码

**禁止**图形颜色同时代表组织规模、年代、玩法与网络形态。每个视觉通道仅表达一个变量。

| 视觉通道 | 唯一含义 | 缺失值怎么画 |
|---|---|---|
| x轴绝对位置 | **年份/特定版本年份** | 不明年份不得精确排在年轴上 |
| 节点形状 | **旧L/M/I组织标签**：方块L / 圆M / 菱形I；多义记录旁加`!` | 人数/身份未确认则空心+`?`，并提供解释 |
| 节点内部主色 | **被证明的核心生产能力类型**：渲染/物理、玩法系统、联网会话、内容制作、工具/宿主（建议五色，不强行单色表达全项目） | 主题不能判定为该能力首次/技术转移时用灰底 |
| 节点右下模式文字 | `S/C/X/N/O/D/∞`，原版和后续变体必须区分 | 不确定填`N?`并在数据层记录依据 |
| 节点底边 | **交付性质**：实线完整商业、短虚线EA、点线免费beta/MOD/原型 | 未核交付性质：细空线+问号 |
| 节点外侧辅助条 | **外部生产支援来源**：发行/委外/现成引擎/MOD底座/用户托管服务，必要时可多条并列 | 不知道：不画，不等于“没有” |

注意：**L/M/I本身既往定义并不完全互斥。** `Alpha Waves`是“一个主要程序员在Infogrames体制内开发”，而非“完全独立个人商业工作室”；`Sonic`是公司内部小组而非独立中厂；`BattleBit`三位具名研发不等于零运维零外援。因此新版理想数据模型中，`core_headcount`与`organizational_backing`应当独立编码。老标签只作为旧史图兼容字段，不将`L`称为所有游戏`>=50 FTE`。

### 六个示范glyph（只展示可以支持的差异，不画成本假数据）

| 案例 | 必须标出的差异 | 绝对不要画成 |
|---|---|---|
| 1984 `Elite` | 两名作者核心/线框3D/离线/Acornsoft出版 | 1984整个3D产业普及 |
| 1993 `DOOM` | 专业小型id核心/2.5D单机 + IPX局域网原版另一节点 | 公网在线服务/大厂50人核心 |
| 1999 `Counter-Strike` MOD | 少作者改造规则/共享Half-Life图形与网络底座/联网MOD | 自造完整独立FPS引擎+服务器 |
| 2011 `Ace of Spades` | 原始免费测试版/可破坏体素/自托管PvP | 2023`BattleBit`的商业交付规格 |
| 2016→2018 `Stardew Valley` | 2016单机一人主体 → 2018新多人版本，外部Tom Coxon/Chucklefish主要网络工程 | 一个人在2016已独自完成在线四人同步 |
| 2019`American Fugitive`→2025`The Precinct` | 同开发商/Fallen Tree、俯视3D都市系统/早期团队扩容/发行支援 | 4个人完成全部GTAIII级复杂制作任务 |

## 四、连接线／创新关系：证据优先

- **实线可画**：同一作品版本升级、同开发商系列续作、明确的MOD→独立版、实证相同技术库的复用；来源与年份由证据支持。
- **虚线可画**：真实采访有明确“受到某作启发”的创作者表述，但不能直接等同源码继承。
- **不能画**：仅凭时间先后、品类相同、两者名声相似而推断“直接影响”“技术转移”“A诞生了B”。
- 竞争/发行关系的线用另一语法，而不是混在“技术继承”中。
- 完全无因果证据的作品并置是有效的**结构对照**，不画线也可以产生强叙事。

## 五、可出版且可复核的双层产品

**出版/海报（线性矢量）**：
- A0横向或更宽折页，矢量`SVG→印刷PDF`。一页总图+3个专题放大图+“正反两面图例与证据代码”。
- 90条底库：只选代表性的作品作为一级标注，例如`Elite/Alpha Waves/Hunter/DOOM/Ken's Labyrinth/Counter-Strike/Minecraft/Stardew/BattleBit`与跨团队成长的`The Messenger/Sea of Stars`；其余作二级微图形，不能让字体小到无法阅读。
- 技术流程放底部，真实时间/测量统计单独小区。不要做“研究成功90条”的KPI海报。

**在线／书内互动（不在本轮承诺实现）**：
- Zoom0：读者看一条产业史、多条创新运动与约10张重要作品卡。
- Zoom1：展开选择的5年/10年、某种技术路线与多作品glyph（不显示不相关族）。
- Zoom2：个别作品证据卡，含`原版`、`网络架构`、`核心人数口径`、`公司/发行支援`、`原始链接`、`不应被误解为何`。
- 显示`headcount_denominator=studio/team/FTE/credits`与证据等级。不要让尚未审计的数量影响 glyph 面积。

**数据应补充的字段**：`case_id,release_date,version,release_stage,primary_gameplay,secondary_tags,render_mode,network_mode,authority_model,max_players,core_headcount,headcount_date,headcount_denominator,organizational_backing,publisher_support,engine_reuse,innovation_tags,reference_source,relation_type,relation_target,evidence_grade,known_limitations`。尚无确证的字段填`UNKNOWN`，绝不从V4视觉反推事实。

## 六、绘制的明确验收门禁

1. **精确坐标**：相同年同x；所有显示年份与来源原版对得上；非线性图必须标断轴与真实年代分布。
2. **分类**：`Northgard=RTS3`不是RTS2；`The Messenger=M`；`Alpha Waves`不能被图例偷换为独立公司；`Counter-Strike MOD`和`Ace of Spades beta`不被画成完整商业standalone。
3. **网络状态**：`Stardew 2016 S→2018 O`，`No Man's Sky 2016 S*→2018 NEXT O`，`Sea of Stars 2023 S→2024 C`，版本/支援变更要显示且不追溯。
4. **组织**：任何精确人头必须附与开发阶段匹配的实际口径。公司人数可以用说明但不得隐性代入制作团队FTE。
5. **图面**：一屏能读标题+时代趋势+5—12标志案例；放大后读所有节点；正面图例不多于六条，完整legend可读；文本不相撞、不能依赖色觉辨认唯一属性。
6. **关系**：每一条有语义的连接线必须关联`relation_type`及具体出处；无证据就只作相邻展示。不能用技术河流线宽暗示产业规模，除非真有横向统计。
7. **产出**：来自同一研究CSV/结构化源，SVG为主、PNG为衍生；发布前自动核对节点数量、版本年份、技术连线和UTF-8排版。
8. **审稿**：必须有视觉截图复核，不允许只验SVG标签和节点年份就自称出版质量合格。

## 七、值得保留的参考项目各占一个岗位

- **Giorgia Lupi/Pentagram：**多层叙事、glyph、工具与运动、长期可读、真实不确定性。主构图参考。
- **Google/Hyperakt/Vizzuality `Evolution of the Web`：**仅供**有来源的技术路线关系**，也可借鉴SVG缩放交互。[Vizzuality称其在线作品已下线](https://www.vizzuality.com/project/evolution-of-the-web)，不把停服页描述为现可用工具。
- **Crawford/Joler `Calculating Empires`：**跨制度与技术的概念地图/专题索引方式，不把它的复杂性照搬成90个互相连线的网。
- **Harvard Growth Lab `Product Space`：**未来在有团队能力/技能的相似性与转移证据后才可尝试“创新可达性”网络，当前禁止凭直觉画因果拓扑。

**最关键的学习结果**：从`一条时间线上的90个游戏名`升级为`实际产品×生产底座×组织条件×时代技术变革`的可缩放解释系统。真正要继承的是精确的信息设计，而非Pentagram的表面审美。
