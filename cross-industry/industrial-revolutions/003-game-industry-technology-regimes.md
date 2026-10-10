# 003 — Game Industry Technology Regimes

- Status: WORKING MAP
- Purpose: 为《独立游戏英雄传说》的 Technical Opportunity Window 提供时代背景。
- Boundary: 这里只研究公开技术条件与产业扩散，不推导私人项目设计方案。

## 1. 为什么不能只写“8-bit → 16-bit → 3D → AI”

游戏开发者真正面对的可行解空间至少由五组条件共同决定：

1. **Compute substrate**：CPU / GPU / memory / storage / device；
2. **Authoring substrate**：语言、引擎、编辑器、middleware、asset tools；
3. **Network substrate**：互联网、宽带、服务器、platform services、backend；
4. **Market substrate**：发行、支付、Steam / app stores、众筹、EA、creator discovery；
5. **Production ecology**：mod / UGC、开源、素材市场、远程协作、外包、AI。

同一块更快的硬件，在 market / tool / distribution 没变化时，不一定改变独立开发的最优组织方式。

## 2. 暂定分代：按“新可行解”而不是硬件营销代际

### Regime A — Hardware-Bound Craft

典型问题：
- 内存/CPU/存储直接决定内容和交互边界；
- 团队经常需要自己写底层工具；
- 发行渠道仍高度物理化或平台化。

研究候选：
- Apple II / early PC；
- MSX / early console；
- early id / Commander Keen。

人物篇要问：
- 当事人具体掌握哪台机器？
- 是消费者、hacker 还是 professional developer？
- 技术限制怎样进入 product decision？

### Regime B — Engine / Middleware Diffusion

关键变化：
- 越来越多开发者不再从 renderer / physics / toolchain 的最底层开始；
- 商用引擎和作者工具缩短 first playable 时间；
- 但“会用引擎”不等于产品判断、内容生产和市场接入已经解决。

研究候选：
- GameMaker → Gunpoint；
- Unity-era micro teams；
- Unreal → Project Wingman / Manor Lords 等。

### Regime C — Internet / Mod / Community Production

关键变化：
- 玩家能修改、上传、运营服务器、形成公开身份；
- mod / map / server 从娱乐活动变成低风险 production apprenticeship；
- artifact-first credential 出现。

强锚点：
- DOOM / WAD；
- Red Orchestra；
- Arma / DayZ → PLAYERUNKNOWN；
- Roblox creator ecosystem。

### Regime D — Direct Digital Market Interface

关键变化：
- 数字商店与支付降低物理发行门槛；
- crowdfunding / paid alpha / Early Access 改变融资和反馈顺序；
- devlog / video / streamer / social discovery 直接进入生产循环。

强锚点：
- Minecraft；
- FTL；
- Kenshi；
- Factorio；
- Gunpoint。

### Regime E — Production-Service Abundance

关键变化：
- cloud / SaaS / marketplace / remote contractor / platform services 继续压缩外围建设成本；
- 小团队可以租用过去必须自建的部分能力；
- bottleneck 更可能移动到 integration、selection、validation、coordination。

### Regime F — Generative / Agentic Production

当前只建立研究问题，不宣布结论：

- coding / art / text / QA / research / ops 哪些成本真实下降？
- 哪些只是 demo 能做、production 不能稳定做？
- 哪些岗位从“亲自执行”变成“定义 / 审核 / integration”？
- 哪些新 coordination cost 出现？
- frontier model capability 何时扩散到普通小团队的可负担工具？
- 当 execution cost 下降后，selection / taste / problem formation 是否成为相对更稀缺变量？

最后一项目前属于 thesis candidate，不能因当前 AI 热潮直接写成定论。

## 2.5 技术窗口不是都由“时代”发下来：Inherited / Recombined / Created

工业革命研究如果只追踪“某项技术何时扩散到开发者手里”，仍然会漏掉一类最重要的创新者：**他们自己就是技术前沿的创造者。**

人物 / 团队与技术窗口至少有三种关系：

1. **Inherited / Diffused Window — 继承窗口**  
   核心能力已经被别的公司、研究机构或上一代工程师创造并扩散，当事人的任务主要是识别和吸收。
   - 示例：GameMaker → Gunpoint。
   - 研究重点：价格、可得性、学习成本、diffusion lag。

2. **Recombined Window — 重组窗口**  
   单项技术并不新，但某个作者首次把已有平台、mod substrate、网络能力、market interface 或 production ecology 组合成一个过去少见的 product opportunity。
   - 示例：Arma / DayZ substrate → PLAYERUNKNOWN。
   - 研究重点：为什么这组能力此前没有被这样组合；规则 / market / community innovation 与底层工程如何分工。

3. **Endogenous / Created Window — 主动创造窗口**  
   创作者 / 团队本身就在推进 frontier。新的技术能力不是“时代背景”，而是作品生产过程的一部分，并直接创造新的 design / product space。
   - 强锚点：early id / John Carmack。
   - 研究重点：技术突破从哪里来；目标体验如何反过来驱动工程；新 capability 何时从单团队优势扩散成行业基础设施。

这一区分对第四次工业革命研究尤其重要。不能因为今天很多模型、引擎、云服务已经以 API / SaaS 形态提供，就倒推历史上的所有英雄也只是“聪明地使用现成工具”。同样，也不能因为少数 frontier creator 能主动推进技术，就把普通开发者都想象成可以同时发明全部底层能力的万能个体。

## 3. Technical Opportunity Window — 人物篇接口

人物 Profile 不写“某年技术进步了”这种背景板。

应该回答：

| 问题 | 说明 |
|---|---|
| 当时他实际能拿到什么？ | 不是全球最先进，而是本人可获得 |
| 前几年为什么难做？ | 成本、工具、网络、分发、技能哪项卡住 |
| 新条件改变了什么？ | 哪个约束下降 |
| 他本人是否意识到？ | 找同期访谈 / 日记 / prototype |
| 同时代别人也能拿到吗？ | 防止把公共条件写成个人天才 |
| 仍然做不到什么？ | 防止“技术一到位就无所不能” |

## 4. 第一批现有案例回填

### Early id / DOOM

CASE-016 E015 使它成为本框架的 **Created Window** 锚点，而不只是“PC diffusion”案例。

已有 Evidence 支持：
- Softdisk 高频职业出货形成能力；
- Commander Keen 在工资 / 公司硬件条件下 moonlight；
- Carmack 直接描述 early id 从 2D scrolling 到 Wolfenstein / ShadowCaster / DOOM 的工作方式，是不断探索当时 **barely possible** 的技术边界，再围绕实际做到的能力决定游戏形态；
- DOOM 相对 Wolfenstein 扩大了可用空间表达、动态光照、地板 / 天花板变化等实时世界能力，且 multiplayer 也是关键技术—产品突破；
- NeXTStep、DoomEd、ANSI C 等工具选择进一步降低迭代 / porting friction；
- shareware / direct distribution 改变小公司的资金与发行边界；
- WAD / specs openness 又把内部技术突破扩散成外部 mod / talent ecology。

因此不能再写成：

> compute + 自研工具 + shareware 恰好构成了 id 抓住的时代窗口。

更准确的是：

> **外部 PC / shareware substrate + Carmack 等人的 endogenous frontier creation + Hall / Romero / art / level-design 的快速产品化 + 市场反馈 → id 给自己制造窗口，并把其中一部分窗口扩散成后来整个产业的基础设施。**

这是工业革命研究里非常重要的一类机制：

> **innovation actor can be both the user of a technological regime and one of the agents changing that regime.**

### Gunpoint / Tom Francis

CASE-007 E004 支持：Francis 看到 Spelunky 使用 GameMaker 后，才明确意识到自己可以用 novice-friendly tool 把判断快速做成 movement prototype。

因此：

> GameMaker 的历史意义不是“它很便宜”，而是缩短 judgment → playable → tester truth 的路径。

### PLAYERUNKNOWN / Brendan Greene

CASE-032 已支持：

> Arma / DayZ 提供现成大型地图、simulation、server/mod substrate，使一个不具备完整大型在线工程能力的作者可以先验证 ruleset；H1Z1 和 Bluehole 再承担后续工业化。

这里尤其能证明 Technology Availability ≠ Complete Capability。

## 5. 下一批待审计

- 小岛秀夫 / MSX2 Metal Gear：硬件限制、screen handling、敌人/射击约束与 stealth 方向之间到底有哪些同期直接证词；
- Wolfenstein / DOOM：PC 性能、VGA、networking 与 shareware 各自贡献；
- Minecraft：Java、网页支付、论坛、paid alpha；
- Unity / Steam Greenlight / Kickstarter 同期如何重构 2010s indie feasible set；
- broadband / streaming / Twitch 对多人新玩法市场验证的作用；
- Roblox / UGC 平台把 tool + audience + distribution + monetization 合并后的职业形成效应；
- generative AI 的 frontier / professional / indie diffusion 分离。

任何对象都先补时间线，再写“技术导致了什么”。


## 6. 物理破坏的横向产品技术分代：2026-10-10新增证据种子

- Status: RESEARCH SEEDS / P0 + H; 非新Claim。
- 范围：2001—2026的技术演进与独立商品化窗口；同一作品依阶段记录原型、EA、1.0、Mod/多人追加功能。
- 方法：不要把可破坏程度 D0–D5 当作线性的技术等级。材料模拟、体素更新、结构物理、节点梁软体、联网复制、UGC内容生产彼此正交。

| 技术轴 | 实际约束 | 用于比较的作品 |
|---|---|---|
| 2D材料/逐像素模拟 | CPU并行、材料更新、物理预算与规则可读性 | Cortex Command; Noita |
| 3D体素环境破坏 | 存储、实时渲染、碰撞、碎块与动态关卡 | Space Engineers; 7 Days to Die; Teardown |
| 载具软体/节点梁 | 求解与稳定性、车辆内容制作 | Rigs of Rods; BeamNG.drive |
| 刚体约束/机械建造 | 联动结构、玩家建造门槛与任务转化 | Besiege; Brick Rigs; Instruments of Destruction |
| 破坏的多人同步 | 权威状态、确定性重放、带宽、兼容旧Mod | BattleBit Remastered; THE FINALS（非独立对照）; Teardown多人 |
| 社区/UGC/Mod | 编辑器、分发、内容持续生产 | Besiege; Brick Rigs; Teardown |

### 已核P0事实种子

1. Nolla Games官方Steam简介列出Noita三位创始作者 Petri Purho（Crayon Physics Deluxe）、Olli Harjola（The Swapper）、Arvi Teikari / Hempuli（Baba Is You）。团队创始人数≠发售总贡献人数。来源：https://store.steampowered.com/app/881100/Noita/ （P0，访问2026-10-10）。
2. Teardown：Steam显示EA 2020-10-29、1.0 2022-04-21；Dennis Gustafsson 2026-03-13技术复盘描述早期联网试验、混合确定性/状态同步、旧Mod兼容与长时间分支整合。**2026多人状态不得倒写回2020EA**。来源：https://store.steampowered.com/app/1167630/Teardown/ 和 https://blog.voxagon.se/2026/03/13/teardown-multiplayer.html （P0）。
3. 2013—2016年已有独立3D物理破坏商品化多条路径：Space Engineers、BeamNG.drive、Besiege、Brick Rigs；它们不能被简化为2020 Teardown相同的技术路线，恰好是“GTX10xx之后才开始独立3D破坏”说法的反例。Brick Rigs EA 2016-11-07： https://store.steampowered.com/app/552100/Brick_Rigs/ （P0）。
4. Instruments of Destruction：Radiangames开发、Secret Mode发行，EA 2022-03-02，1.0 2024-05-10；不能误归 VoR Games。来源：https://store.steampowered.com/app/1428100/Instruments_of_Destruction/ （P0）。
5. NVIDIA官方GTX1060公告日期2016-07-07、上市2016-07-19，**并非2018推出**。Teardown目前Steam配置文字中的“GTX 1060 or similar. 4 Gb VRAM”应读作独立最低显存要求，不是英伟达有GTX1060 4GB型号的证据。来源：https://nvidianews.nvidia.com/news/a-quantum-leap-for-every-gamer%3A-nvidia-unveils-the-geforce-gtx-1060 和 https://store.steampowered.com/app/1167630/Teardown/ （P0）。
6. “PUBG热潮加速GTX1060安装基础，从而让Teardown可卖”仍是**H假说**：需同一期间硬件销量/Steam安装占比/玩家升级动机和同时期其它驱动因素，不能凭年代相邻宣布强因果。

### 外部AI研究输入隔离：禁止直接升级为Evidence

2026-10的一份“21游戏数据库”报告存在多项可被一手来源否定的误指认，故其未追溯数字不得导入本库：

- Lethal Company写作“2022免费/Scrappy Turtles”是错的。Steam：2023-10-23、Zeekerss、付费。https://store.steampowered.com/app/1966720/Lethal_Company/
- R.E.P.O.写作“2019 Therion Games的科幻载具破坏”是错的。Steam：2025-02-26、semiwork、多人合作恐怖物理搬运；仓库已有CASE-006。https://store.steampowered.com/app/3241660/REPO/
- PEAK写作“2022像素恐怖”是错的。Landfall+Aggro Crab于2025-06-16推出多人攀爬游戏；仓库已有CASE-034。https://steamdb.info/patchnotes/18844069/
- Teardown写作“Seumas McNally制作”是错的。开发商Tuxedo Labs、官方技术文作者Dennis Gustafsson。来源见上。
- Instruments of Destruction写作“VoR Games/2023-10 EA”是错的。来源见上。
- 首月销量/收入/退款率、评论与销量固定比例、单一T1–T6技术难度不具备独立可核来源，保留UNKNOWN，不用模型数字填空。

### 待补证/对照设计

按技术轴×年份×单/多人×原型/EA/1.0建立**可复现的完整候选池**，加入冷门与失败样本；核主创前史、团队核心/外围、技术是否自研、性能最低门槛、开发人年、实际消费闭环（任务/UGC/观看/社交）、销售与退款来源。硬件普及属于公共机会，关键创新可能是创作者主动改变模拟表示；需分别检验 Inherited / Recombined / Created 窗口。


## 7. 海盗船多人对战：破坏模拟 × 岗位协作 × 登船战（2026-10-10，Lane B intake）

**研究对象边界：**这里关注的是船只作为多人共同操作、可受损、可维修且可登临的战斗空间，而非把所有海战或“真实船体连续破坏”统称同一种技术。比较至少分四条互不代替的轴：①船体损伤/进水/维修的交互状态；②移动船舶上的玩家行动、火炮操作、同步和跨船转移；③局内目标（舰队竞技、大逃杀、持久 PvPvE、装备成长）；④整个生产组织、服务规模和商业验证。具体底层物理架构及网络拓扑，除非开发者证实，**UNKNOWN**。

### 作品分组（P0来源种子；非独立项仅作比较）

| 作品 | 实证时间点 | 核心差异 | 容易犯的错误 |
|---|---|---|---|
| Assassin's Creed IV: Black Flag / Ubisoft | 2013 单机海盗动作；官方说明包括海战、操船与亲自登船战斗。https://www.ubisoft.co.jp/ac4/about/ | AAA 航海/登船体验标杆 | **不是**海战游戏或该类 Mod 的最早发明者，也不是同期大规模真人合作海战的同一产品形态 |
| Blackwake / Mastfire Studios | 2017 EA → 2020-02-19 正式发行 → 2024-02-27 改免费；Steam app 420290。https://steamcommunity.com/app/420290/allnews/ | 54人、至多13人船员、多人装炮/维修/补给/舰长决策/登船；核心是“船员交互回路” | 不按2024 免费制倒推2017付费市场结果；不声称其具备任意连续船体破坏 |
| Sea of Thieves / Rare–Microsoft | 2018 初发；2024-04-17 官方称累计玩家超4000万（Xbox、Windows、Steam合计）。https://www.seaofthieves.com/news/40-million-players | 持续 PvPvE 沙盒、社交协作、长期内容运营，存在大型团队高产品体验对照 | 累计玩家不是销售份数、利润、峰值同时在线，也不是可直接对比付费独游的单位 |
| Blazing Sails / Get Up Games–Iceberg | Steam app 1158940；2020-09-09 EA → 2023-11-13 1.0。https://store.steampowered.com/app/1158940/ | 将船员岗位与海战、登岛搜刮、淘汰制大逃杀/短局竞技重组；有亲缘创始团队与发行外围 | 不能因几个表兄弟发起，就把整个发售期贡献与成本说成只有3人 |
| Skull and Bones / Ubisoft Singapore | 2024-02 首发，2024-08-22 Steam上架；Steam app 2853730。https://store.steampowered.com/app/2853730/ | 在线舰船战斗、船舶配置与装备成长；2026官方确认停止开发 Land Combat，继续围绕 naval core。https://www.ubisoft.com/en-gb/game/skull-and-bones/news-updates/1d5st5v5gmBMCjN4DcIRHw/through-the-spyglass-year-2-in-review | 不能无工程底层指标就下结论称其代码技术含量低于独游；Steam口碑不能覆盖主机/Ubisoft Connect市场 |

### Blackwake：具名开发者自己提供了极少见的七年过程证据（P1 retrospective direct participant；2020发售时公告）

来源：[Steam Blackwake Full Release, 2020-02-19](https://steamcommunity.com/app/420290/allnews/)，Mastfire Studios开发者正文；关于2013—2019的回忆属于**P1**，对2020当时累计销售口径的开发者同期披露可视为**P0自报**，不能推算净收入/利润。

1. 2013年 Dakota 提出项目；Tyler 在论坛看到 demo 后加入。团队明确表示受更早的 Pirate Ship Wars、Battlefield Pirates mods 启发（**直接反证“2013 Ubi发明海盗船对战”**）。
2. 2014年 Kickstarter 失败：当时严肃模拟、范围过大；演示给主播及朋友后，团队发现多人混乱和喜剧性互动才是吸引力。
3. 2015年调整定位后第二次 Kickstarter 获约 **AUD 170,000**，开发者称额外聘用了美术、动画、配音；所以不可把两位核心开发者等同全成本劳动。
4. 2017年 EA 首发碰到 **PUBG beta服务器停机、等待中的主播尝试Blackwake** 的偶然事件，这是**开发者自述的传播路径**，并非大样本因果。
5. 团队回顾称首发前预期约 300 concurrent、一个月3万份；2020年正式版公告披露 EA三年**累计销售超过120万份**。这些是不同时间、不同指标，不能转为利润或常态并发。
6. 开发者坦承某一升级版 Conquest 综合模式不受专门喜欢纯海战玩家欢迎，后来删除；功能扩充未必提升核心体验。随后为长尾玩家提供机器人。

**特别价值：**此前讨论 PUBG→GTX1060→Teardown 属于硬件安装基础的 H 假说；在 Blackwake 中，PUBG 被当事者明确记述为**发行时流量分发的一次外部偶然性**。两条机制完全不同，不能混为“PUBG导致物理破坏游戏”。

### 需要检验而非抢先宣布的跨项目命题（H）

- **H-NAVAL-01：**多人船战的玩家体验密度可能主要来自“岗位相互依赖、损伤与修复引起的持续压力、登船突发事件”，而非船体网格/破坏粒度。验证：拆操作状态、视频/开发者设计笔记、各游戏回合长度和玩家会话观察。
- **H-NAVAL-02：**大公司将航海玩法整合进装备成长、内容生产、在线服务时，可能弱化了多人船员即时协作的闭环。**不得**由 Skull and Bones 的口碑自动推广至大公司或所有海战作品；Sea of Thieves 是重要反压力。
- **H-NAVAL-03：**小团队更容易识别并维持单个戏剧性体验循环，但多人联机长线供给、活跃衰减、反作弊和服务器可靠性也可能造成小团队短板。需固定对照分母，不只挑大公司失败、小公司成功。
- **H-NAVAL-04：**“开发十年/多人参与/巨额预算”是研发投入、版本战略及多次返工的研究问题；传闻 Skull and Bones 达 \$200m 与大规模跨工作室人力是媒体引述匿名消息，不是经审计成本表。https://insider-gaming.com/skull-and-bones-players-total/ （S1报道但财务**未证实**）。

### 待采证及下次增量

- 实际船体破坏技术类别：预设受损区域/碰撞体/进水层级/刚体船只/连续形变/跨船同步，逐作核技术讲解；无技术证据时不打“技术含量排行榜”。
- 两种“乐趣”指标分别取：①高密度单局情境/社交惊喜（原型、玩家证言与机制观察）；②长期留存、可达玩家、生命期运营、销售与人年回报（同口径真实数据）。不可用个人主观体感替代全玩家评价。
- 上述时间线补早期 Mod 的发行日期与创作者；考察 AirBuccaneers、Guns of Icarus Online、Holdfast: Nations At War、Naval Action 等**候选**，仅当符合具体机制/市场入组门槛时加入对照。
- 建议人物候选：Dakota 与 Tyler 的相遇、首次失败众筹、主播玩法识别、受雇外围支持、EA删减迭代、长尾转免费，应优先完成独立 Case 的 Contributor/Market/Failure 审计。新 Case 编号受 BACKLOG gate 约束，不在技术史文件抢号。
