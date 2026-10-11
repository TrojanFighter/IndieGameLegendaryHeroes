# 024 — 把三线历史图填满：六个关键缺格、联网版本与缩放生产路径

> **历史版本已被2026-10-11反向审计修正。** 本页所写9类27/27、65条以及[023旧SVG](023-representative-three-rails-filled-first-pass.svg)是**上一阶段选样快照**；当前请以[025审计结论](025-flagship-era-audit-earlier-small-authors-and-missing-genres.md)及[12类33/36轨道的纠错时代图](025-audited-era-by-genre-three-rails.svg)为准。现同一[023来源CSV](023-representative-genre-three-rails-1958-2026.csv)已扩展**82条原版与功能模式历史记录**；新增1990 Alpha Waves、1991 Hunter、1993 Ken's Labyrinth、2002 Soldat、2011 Ace of Spades以及原图漏掉的赛车/RTS/RPG。特定“第一”“成熟/独立”认定需以25正文核查。原023图仍保留供对比纠错。


- **2026-10-11 / Status: VERIFIED REPRESENTATIVE MILTESTONE COMPLETION — Not first-ever, not equal-fidelity full industry census**
- **最新可读主图：[023 v2 — 9个玩法族×L/M/I共27个角色均有标志节点](023-representative-three-rails-filled-first-pass.svg)** / [65条案例与源头](023-representative-genre-three-rails-1958-2026.csv)。
- 为读者服务：主图优先完整呈现标志性历史作品，**不同规格、不同网络与依赖技术用注释明确**；不将102格组合表当成稿件完成条件。
- 本专题原始来源以当期制作方记录、当期presskit、团队2018/2020回顾或原作credits为主；不要把几十上百个发行/配音/本地化credits误当全职核心。

## 1. 023上一次剩下的六格，已有可引用的年份和代表作

| 九类中的缺位 | 新锚点 | 可靠的制作信息 | 可填充程度和限制 |
|---|---|---|---|
| 2D俯视/街机射击 M | **2016 `Neon Chrome`** | 开发商10tons；2016 Win首发。[MobyGames原版开发credits](https://www.mobygames.com/game/79064/neon-chrome/credits/windows/)列五位具名设计贡献者、四位程序人员；总40个credit人含测试与外包。 [Steam](https://store.steampowered.com/app/428750/Neon_Chrome/)证实单人/本地联机。 | **专业小核心M的代表性候选**，但真正FTE、劳动时间尚未核，不强行写40人制作。和早期Robotron属于较近的双摇杆机制。 |
| 2D经营/农场专业体系 L | **1996 `Harvest Moon`（牧场物语SNES）** | [首作SNES原始开发署名](https://www.mobygames.com/game/6585/harvest-moon/credits/snes/)显示Amccus / Pack-In-Video完整制作/商业发行体系；总30署名含不少销售、致谢。 [Yasuhiro Wada原作GDC Postmortem](https://www.gamedeveloper.com/design/video-the-making-of-the-original-snes-i-harvest-moon-i-)解释如何将赛马经营玩法改为农场、以及公司倒闭等制作曲折。 | **专业公司产出成立、但不是“大于50人核心团队”**；这是L的专业制作发行条件，不代表L核心人头。 |
| 2D经营/农场 M | **2024 `Fields of Mistria`（米斯特里亚牧场）EA** | [2024原始Steam credits](https://www.mobygames.com/game/229134/fields-of-mistria/credits/windows/)与[NPC Studio官方团队名单](https://www.fieldsofmistria.com/team)包含程序、美术、设计、制作、编剧、音乐等专业岗位。[官方发行公告2024-08-05](https://www.fieldsofmistria.com/post/fields-of-mistria-early-access-roadmap-have-arrived)。 | **有多职能中型制作核心的代表案例**，大credits集合混有供应商、外包、贡献者，实际FTE未查；本作品初期为单机农场，不填进在线合作。 |
| 3D系统世界专业体系 L | **2014 `Elite: Dangerous`** | [Frontier Developments 2014-12-16证券公告](https://www.investegate.co.uk/announcement/rns/frontier-developments--fdev/announces-full-public-release-of-elite-dangerous/3729348)已确认正式发行、专业开发公司及众筹+官网累计筹得1,000万英镑，超过20万支持者。 | 公司组织规模和服务器模式比1984年二人离线Elite复杂得多；**需要在线连接，即使有Solo mode**。1984作品与2014作品不是相同资产与线上成本。 |
| 3D城市世界 M | **2020 `Cloudpunk`** + **2025 `The Precinct`** | [ION LANDS 2020同期presskit](https://ionlands.com/cloudpunk/presskit/)披露程序、关卡、体素美术、叙事和音频多人协作；[2020访谈](https://www.gamedeveloper.com/game-platforms/cloudpunk-creator-marko-dieckmann-on-cyberpunk-voxel-art-and-constant-fight-that-is-indie-development)开发者解释为什么弃用枪战、选择送货与体素城市；[The Precinct制作者访谈](https://www.pushsquare.com/features/interview-learning-all-about-the-precinct-ps5s-super-promising-sandbox-cop-game)确认**早期2程序+2美术，共4人**，后来增专职设计与额外程序、外部合作。2025-05-13上市。 | 都是**有专业化开发与外部支持的中小制作链**；2020 Cloudpunk更偏叙事低资产，2025 Precinct更偏驾驶追捕、犯罪事件生成；均不等于同保真GTA III。|
| 3D城市世界 I | **2019 `American Fugitive`** + **2023 `Shadows of Doubt` EA** | [2019 Fallen Tree Games一手介绍](https://fallentreegames.com/americanfugitive/)明言由两名AAA履历创始人创建，完成3D俯视犯罪/追车城市；[Steam](https://store.steampowered.com/app/934780/American_Fugitive/)确认2019-05-21商业发行并由Curve出版；[ColePowered 2023开发日志](https://colepowered.com/shadows-of-doubt-devblog-35-post-launch-progress/)确认Cole开发，同时Josh提供开发工作以及另有音频/写作协作者，2023-04-24 EA。 | 前者贴近GTA玩法，但刻意换回俯视3D和缩减内容体量；后者是程序化体素侦探城市，不能误叫个人无外援制作GTA规格城市。|

**六个角色都有可具体写作的历史案例；填满的是「代表标志位」，不是「六个完全同规格首次商用」**。如果想做同等画面和制作规格，部分位置仍应保留并列分支和证据警示。空心/问号不代表图不能出版。

## 2. 最有价值的额外一线验证：15人造3D程序化宇宙，不等于当时造出了完整互联网合作

[Sean Murray于2018年的回顾](https://www.nomanssky.com/2018/07/a-message-to-the-community/)明确称`No Man's Sky`2016首发**平均制作团队6人，上市时15人**。该游戏在2016年已有联网数据服务/发现等要素，但不是2018年以后完整多人同行体验。 [Hello Games 2018年7月24日同期公告](https://hellogames.org/2018/07/24/no-mans-sky-next-update-and-xbox-one-release/)确认NEXT更新追加完整可组队多人。

**时间线应该分两条同一作品版本节点：**
- 2016：M／3D程序化开放探索／以单人会话为主，带有联网元数据，开发团队上市15人；
- 2018：M／同一作品，增加正式互联网多人共享游戏状态与合作；
- 绝不能把2018实现的网络状态同步技术追认成2016年首发就已经具备的开发能力。
- [2018 `X4: Foundations`官方presskit](https://www.egosoft.com/press/sheet.php?p=x4_foundations)和[2018-12在线实验公告](https://www.egosoft.com/news/archive/2018December_es.php)提供另一对：11月离线空间经济沙盒、12月开始实验性跨玩家宇宙Online Ventures；并非已经加入多人同局射击。X4的2018开发核心FTE没有可靠数字，故仅作M候选侧证，不能写成确定20名员工。

## 3. 极有价值的中国游戏业对照：缩小规格、先验证机制、再增加人员

**《American Fugitive》(2019) →《The Precinct》(2025) 是同一工作室跨作品的扩张/定位案例**：

2019公司由两名有大制作履历的创作者设立，利用现成工具、俯视3D表现和开发范围约束，做出犯罪追车/城市任务的商业游戏。其2025项目采访披露早期编制**2程序+2美术**，并在后续随着内容品质要求提升增加设计、额外程序和专业外部协助；其游戏玩法从逃犯犯罪变为追捕执法，二者不是相同作品的画质升级，而是**相似沙盒架构下不同规则体验、增加制作能力**的连续实践。须注意从2019到2025并非线性全程只靠4人，作品最后完整credits很多；**绝不许用4人声称已独力完成全部2025成品**。

这个样本对书中技术史关键：成熟的引擎/资产工具使小型高素质作者不必再以大资本同保真竞争；可寻找高保真作品中可抽离的**核心玩法、视角、空间连续性、可破坏/可交互的有限子系统**，用小成本完整交付并凭此对下一款决策。

## 4. 图表边界：核心组织与资源支持是两根轴

- `professional_company_L`和`5_49_core_M`可以同年并存：同一款《Harvest Moon》同时可能有小型开发核心和完整商业公司发行支持。因此**组织支持**不能替换为开发核心人数。
- 2016 Neon Chrome ≠ 40开发者，2020 Cloudpunk ≠ 134开发者，2024 Fields of Mistria ≠ 146开发者，2025 Precinct ≠ 284开发者——这些是**所有署名角色与扩展支持人员**集合，跨作品不能直接用于项目人效比计算。必须审计程序、美术、设计、外包、QA、本地化、宣传、配音和发行区别。
- 2014 Elite Dangerous O∞、2016 No Man’s Sky S*(在线元数据)、2018 No Man's Sky NEXT O、2018 X4 S/后续实验联机，都是**不同联网负担**；2018 X4 Online Ventures不是同步的多人同局系统。
- 2023 Shadows of Doubt不是纯独力1人完成，至少Cole+Josh及音频/文案协作者；“solo-led”只指主导而非总人数。

## 5. 还差什么才升级成严肃的产业量产推论？

不缺标志性作品。缺的是**严格同子品类的开发人年、外包总额、公开商业合同、成本和真正的跨作者重复交付**。这批资料可以针对主图20—30个最关键标杆逐案补，而不是对102个假设组合逐格填满。

**阶段性里程碑：主图现在已经有9个选择的玩法族×L/M/I＝27/27个可读标志作品角色，65条记录（非65款互斥游戏），且有明确的网络/制作规格警戒；“填满”不等于“全球游戏产业所有品类已被证明达到同一规格”。**
