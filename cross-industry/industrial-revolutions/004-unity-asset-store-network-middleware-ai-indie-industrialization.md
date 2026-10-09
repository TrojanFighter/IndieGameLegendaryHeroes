# 004 — 从 Unity、Asset Store 到联网中间件与 AI：独立游戏生产资料的商品化与模块化（1990s—2026）

- **Status:** HISTORICAL TECHNOLOGY-REGIME STUDY / SOURCE-ANCHORED / CAUSAL PREVALENCE OPEN
- **As-of:** 2026-10-09
- **Purpose:** 将独立游戏的技术代际按可实际获取的生产能力分代，而不是仅按显卡规格、融资额、就业人数或销售成绩。
- **Parent:** [003 — Game Industry Technology Regimes](003-game-industry-technology-regimes.md) · [民间多人游戏创新机会窗口](../../book/research-notes/grassroots-online-multiplayer-opportunity-window-1999-2025.md) · [多人基础设施经济比较](../../book/research-notes/multiplayer-worlds-unit-economics-and-founder-decisions-2026-10-09.md)。
- **Method gate:** 严格拆开“一个技术存在”“小团队可获得”“实际项目采用”“新游戏品类扩散”四层；有软件使用证据不等于有开发工时、成本因果或行业平均值的证据。

## 0. 核心论断：不仅是“技术发展”，而是生产资料可交易和可组合

**PUBLICLY REUSABLE PRODUCTION CAPITAL / 公共可复用生产资本：** 长期研发生成的引擎、语言、工具、协议、内容管线与工程资产，通过授权、开源、数字商店或云API，从公司内部固定资产转为其他开发者可调用的外部投入。

**SOFTWARE ASSEMBLY INDUSTRIALIZATION / 软件攒机式工业化：** 作者不用复制一个游戏工作室的各个内部部门，而是识别自己的核心判断/能力后，组合引擎、资产、插件、运营接口与外围专业劳动，并在其中构建自身不可替代的玩法。

**COMPLEMENTARY MARKET / 双边能力市场：** 外部创作者可以出售通用模块并获得维生或研发收入；客户可以购买比自建便宜的能力；上游模块投入被众多下游产品分摊，进一步刺激新的模块开发。不是说一切插件都值得买或拥有同一质量。

**MULTIPLAYER AS CONTENT GENERATOR / 玩家交互作为内容生产：** 在特定PvE/社交游戏里，其他玩家的误判、分工、叙事与失误构成可重复变化源，和程序化/肉鸽生成一起改变每小时体验相对手工内容投入的比率；不能写成“联机自动省内容成本”。

**AI AS NEXT COMPOSITION LAYER / AI是下一层而非无先例的凭空革命：** 一些代码/贴图/动画/音频/测试/文案劳动从固定岗位转成可调用模型/Agent，但可用性、端到端成本、项目一致性、权利与质量检验待实测。

## 1. 时间轴：五个层次叠加，而非互相淘汰

| 时间 | 面向小团队可用的生产条件 | 改变的约束 | 不能误述为 |
|---|---|---|---|
| 1990s—2004 | RPG Maker、GameMaker、Torque、Flash、SDL/OpenGL、模组工具、早期商用引擎 | 已能避免从头编写所有游戏代码；但跨平台、通用编辑器和商用模块生态分散 | “Unity 是世界第一款小开发者可购买的游戏引擎” |
| **2005—2009** | Unity 2005首发；2009 Windows编辑环境与免费开发工具进一步推广，Web/移动/桌面跨平台逐渐组合 | 通用跨平台开发门槛显著降低；共享Unity工作流开始形成 | 2005第一版已经拥有2015完整跨平台支持 |
| **2010—2014** | Unity Asset Store **2010-11-10**推出，Photon PUN **2011**；2013 Unity iOS/Android基本导出纳入免费；Steam EA 2013 | 非官方素材、模板、工具及中间件产生市场；开发、收费测试与扩散的反馈链缩短 | Asset Store仅出售美术贴图；联网直到2018才有可复用技术 |
| **2015—2021** | UNet **2015**公共Beta、uMMORPG **2015-12-23**发布、Mirror **2018–19**成长为UNet社区替代；Photon、其他中间件平行发展 | SyncVar、RPC、对象生命周期、transport和常用server/client同步更商品化；民间反向维护厂商放弃的层 | Mirror独家发明联网、MMO或在2018突然创造全部网络技术 |
| **2022—2023** | Unity Netcode for GameObjects **1.0 2022-06-27**；Steamworks传输、语音插件、关卡生成器等可组合 | 少人即可构建主机托管合作及社交高重玩游戏；但还要完成集成、性能、反作弊、可用性 | 《Lethal Company》使用Mirror（错误） |
| **2024—2026** | 云模型、生成式内容和Agent编程/测试/生产链工具进一步可用 | 通用代码/素材/协调等服务的边际取用成本与原型速度改变 | 所有游戏的实际质量、发售率、利润都自动提高 |

### 可量化早期扩散数据（不是队列因果）

- Unity 2010-11 Asset Store官方新闻稿记载**25万+注册用户**；https://unity.com/news/unity-technologies-launches-3rd-party-marketplace-unity-asset-store
- Unity 2013-07-09新闻稿记载**200万+注册开发者、40万+月活**，并明确晚2009年免费工具以及2013年基本iOS/Android导出纳入免费；https://unity.com/news/unity-technologies-doubles-community-two-million-developers
- Unity官网2026 Asset Store发布者页称**1.2万+活跃发布者、每月170万+用户**，官方营销口径非第三方审计；https://assetstore.unity.com/publishing/publish-and-sell-assets
- Photon官方PUN历史页列出**2011**（Photon Fusion列2021）；https://www.photonengine.com/pun/

## 2. 《FTL》的时代问题：为何规则/程序生成可以替代人工内容，而联网后来又进一步扩张设计空间

《FTL: Faster Than Light》（2012）是典型单人PvE：有限资产/事件模块、路径随机、风险抉择及permdeath构成可反复体验的差异。该作依赖C++/SDL而非Unity；FTL作者没有因“没通用引擎”而无法做游戏。同期还有丰富的解谜、平台动作、叙事、沙盒和多人作品，所以**不得**从FTL一例推“2012年绝大多数独游皆肉鸽单人”。

两种可以复用的低内容义务机制：
- `PROCEDURAL CONTENT COMBINATORICS`：系统/随机数/选择使手工事件重复形成多种体验；
- `SOCIAL CONTENT COMBINATORICS`：少量系统、空间、敌人和战利品，在不同玩家协作、语言、误判和欺骗中生成故事。

后者不是PVE的取代，而是可以**叠加**：多人PvE+随机环境+共用风险。同时对代码、延迟、好友联机、作弊/掉线等提出新要求。这些高门槛需要成熟的网络框架、语音和平台服务来压低，**社交机制本身才决定是否真正产生体验价值**。

原始软件技术旁证：2012 Subset Forum对FTL二进制和开发库的讨论，列出C++/SDL；属社区技术观察而非作者亲述：https://www.subsetgames.com/forum/viewtopic.php?t=2782

## 3. 最值得写人物篇的基础设施作者：vis2k / uMMORPG → Mirror

**2015-12-23**，vis2k将正在自制的Unity+UNet MMO通用系统上架Asset Store，产品叫**uMMORPG**。他在自己的技术史中提及，当年专业MMO引擎的授权报价格远超其预算；他原本只预期每月赚一点零花钱。商品后来进入商店热门，并让他能够全职从事这类技术开发。

随着UNet在维护、封闭底层和高并发方面出现严重问题，社区通过开源高层API和自行替换底层传输来接管。这催生Mirror（应写作**2018–2019社区转型窗口**，2019-02 Mirror v1.4源码化与组件化、2019-03发布迁移工具已有确切更新日志；若要写精确首次发布日期必须进一步查最早仓库tag或官方档案）。

vis2k称Mirror在UNet之上投入**10,000+人小时**、其社区曾达**每年约10万下载**，均记为维护者自述估计，非独立计量。项目自称覆盖1000+ Steam游戏，不拿宣传页自述冒充实际都付费/长寿。

- P1自述及版本史：https://mirror-networking.gitbook.io/docs/trivia/a-history-of-mirror
- 2019正式变更日志：https://mirror-networking.gitbook.io/docs/manual/general/changelog/2019-change-log
- Mirror仓库：https://github.com/MirrorNetworking/Mirror

**历史机制重点：** 原来一个想做MMO但买不起专用引擎的人，将自己制造的“一个项目所需的能力”变为一个公共工具，再和其他小团队补上被Unity厂商放弃的网络层。技术劳动的成果因此在其他作者项目中重用；他们不是“纯粹依靠资本雇佣游戏程序员”，而是在真实插件市场中交换生产资料。可是开源并不意味着零投入：研发和维护的真实人小时仍存在，只是跨产品摊销。

## 4. 最强的“攒机”实物证据：《Lethal Company》2023-10-14发布版文件

SteamDB保存的《Lethal Company Demo》**2023-10-14** depot列表可逐项看见：
- `Unity.Netcode.Runtime.dll`：Unity Netcode for GameObjects；
- `Facepunch Transport for Netcode for GameObjects.dll`：Steam传输适配；
- `Facepunch.Steamworks.Win64.dll`：Steam平台API；
- `DissonanceVoip.dll`：语音聊天中间件；
- `ClientNetworkTransform.dll`：对象网络变换扩展；
- `AmazingAssets.TerrainToMesh.dll`：其他第三方库。

原始证据：https://steamdb.info/depot/2563241/apps/
模组社区技术验证：https://lethal.wiki/dev/advanced/networking
Dissonance商品页：https://marketplace.unity.com/packages/tools/audio/dissonance-voice-chat-70078

**纠错：Lethal Company并不使用Mirror。** 实际采用Unity NGO+Facepunch Steam传输+语音中间件。Mirror作为2018–19网络扩散的重要节点仍成立，但**不能编造一条Mirror→Lethal Company的直接技术因果关系**。

**年代纠错：** SteamDB **2026-04**《Lethal Company》版本可看到 `DunGen.dll` 等工具，但不能将2026二进制里的所有库回填到2023 Demo，尤其不能用2026包证明2023就采购过某插件：https://steamdb.info/depot/1966721/manifests/ 。

有这些组件存在≠“官方确认插件采购金额”≠“作者只会拼装没有写核心代码”。核心玩法定义与稳定集成才是产品作者不可替代的劳动。

## 5. 与AI阶段之间的严格同构与差别

| 生产层级 | 2010年代插件/工具市场 | 2024–26 AI工具 | 是否已经可交付 |
|---|---|---|---|
| 引擎/运行时 | 通用编辑器与引擎 | Agent使用既有Unity/Godot/UE，少数自动生成辅助代码 | 引擎仍不可轻易由语言模型替代 |
| 玩法逻辑 | 库、脚本、模板、RPC | 根据规格生成/修改代码和测试 | 可加速部分工作，持续兼容与调试仍需评估 |
| 美术/内容 | Asset Store模型、动作、音频、工具 | 生成图片、3D、音频、动画/场景的不同成熟度能力 | 风格一致性、版权、迭代控制、可用资产约束 |
| 网络/运营 | UNet/Mirror/NGO/Photon+Steam/GameLift | 可辅助网络程序/运维脚本/诊断 | 无法凭代码生成取消服务器物理/网络成本 |
| 创作者能力 | 借用外部专业模块，做作者最擅长部分 | 用模型+工具增强个人能力上限 | 可能使项目“反向能力适配”空间扩大，不等于人人自动懂玩法 |
| 市场 | EA/视频/直播/Steam | 原型产量更高，竞争/发现更难 | 更多生成供给不保证单项目曝光/销售 |

同构在于 **`FIXED-CAPABILITY COST → SHARED REUSABLE SERVICE`**；不同在于插件是较确定的可复用产品，模型的输出可能是动态、不稳定、需要测试和修订的生产过程。2026阶段新瓶颈包括上下文/一致性、版权/IP、长期维护、供应商依赖及产出过剩。

对资本/UBI叙事的可证伪对照：现金转移政策可能影响个人runway/家庭风险，但不会单独把开发一套联网引擎的工程工时从成百上千人日缩为一键调用。工具扩散直接改变**生产函数**，不能将二者简单放在同一类变量上。反过来，低成本工具不自动解决家庭生活成本、市场需求与收入分配，UBI也有不同于引擎工具的政策目标。**两者不是同一问题的完全替代政策。**

## 6. 作者型游戏英雄传里的生产条件字段（制度化）

每个跨年代CASE增加：
- `AUTHORING_TECH_GENERATION`：当时可取得的引擎/素材/源码/商业许可；
- `MIDDLEWARE_SOURCE`：自研/插件市场/开源/厂家/专业外包；
- `NETWORK_TECH_GENERATION`：无联网/自写/Legacy/Photon/UNet/Mirror/NGO/其他；
- `COMPOSITION_RISK`：供应商跑路、许可证、版本迁移、技术债和debug难度；
- `CONTENT_SUPPLY_STRATEGY`：手工内容/程序生成/玩家生成/互动生成/混合；
- `CASH_VS_TOOLS`：当时增加$X融资与增加某工具可用性分别解除什么约束；
- `AI_DISPLACED_LABOR`：如果当前AI工具被用到，哪个具体岗位/流程工时实际减少、成品质量如何；
- `TEMPORAL_VALIDITY`：2026“今天容易”不能倒写成2012项目“本来也应该很容易”。

**优先研究任务：** 提取一组2012–2015单人/联机作品与2020–2025多人合作作品的可核组件清单、首次推出日期、团队和成本；以软件分发文件/技术讲演/仓库tag进行取证，而不是成功开发者口述“我一个人做的”。

## 7. 中国非均衡吸收的压力测试：有中间件供应链，不代表玩法选择权同步扩散

本笔记原先着重技术能力被商品化，现补充**工业知识吸收的用途分流**：`TOOL_ACCESS`、`TOOL_ADOPTION`、`TECHNICAL_SPECIALIZATION`、`AUTHORIAL_DECISION_RIGHT`、`GAME_DESIGN_DISCOVERY`分属不同变量，不能由前者自动推后者。

**供应侧正例（2026-10-09查）：** 中国开发者开源QFramework（https://github.com/liangxiegame/qframework）、Luban（https://github.com/focus-creative-games/luban）、HybridCLR（https://github.com/focus-creative-games/hybridclr）、YooAsset（https://github.com/tuyoogame/YooAsset）。他们明确实现工具/代码复用、跨项目交易或公共维护。HybridCLR项目方所述千余款上线项目仍属其自述、不得当独立抽样调查。

**创作权正例（2017同期）：** 凉屋《元气骑士》访谈报告员工先原型后立项、每项目常1–3人，程序担任制作人；这不是“某国人普遍意识强”的证据，而是可复制的中国组织制度设计：https://www.ali213.net/news/html/2017-4/293569.html 。2020《枪火重生》选择EA+合作Roguelite而非完整GaaS，详见[CASE-039](../../cases/CASE-039-gunfire-reborn.md)。

**压力负例：** 《猛兽派对》2020–23内容返工、网络方案迭代和组织增长并列存在；不能把技术困难自动写成必要延期，也不应在没有架构演变源码/成本记录时判定“造轮子”是唯一原因。《边境》证明强技术hook与短期销量不能消除持续多人生态的义务；失败责任分配仍有争议，见[CASE-029](../../cases/CASE-029-boundary.md)。

进一步研究框架见[中国033的中间件能力转化缺口](../../country-studies/china/033-technology-proxies-experience-demand-and-commercial-feedback.md)。

**AI后继的具体预测**：中间件和AI将降低原型技术供给成本，但如果原创验证、跨圈资料吸收、作者原型权、失败退出及国际市场入口不变，最可能的表现是**更快完成既定规格、更多看起来像产品的原型，未必更多真正形成新体验的新产品**。反证包括新手/非传统作者借AI在短时间制造原创玩法，或传统公司修改原型权/市场验证制度后同样提高转化。都需固定发行队列与玩家反馈，而不能拿国别成功者名字做结论。
---


## 8. 被前述工具史漏掉的核心分母：游戏项目每单位产出耗费多少完整人年

[2026-10-09中国与海外项目人效对照](../../book/research-notes/china-indie-manpower-efficiency-middleware-build-buy-incentives-2026-10-09.md)建立`FTE_YEARS + BUY/BUILD/DELETE + MARKET_VALIDATED_HOOK + FIRST_PAID_ACCESS`。已有技术市场且存在中国产中间件，均**无法**证明中国创作者以全球同样的成本形成体验。工具创造者可能帮助别国开发者降低人年，国内同业若反而常用旧式部门自研方式，生产函数转化会出现缺口；“员工以自研捍卫岗位”属于委托代理及NIH候选机制。科研不可先验认定全部自研或全部大型员工为寄生。最关键的下一步是固定队列的工具利用率、实际开发/外包人年、玩家实验数、上市率、收入、失败者分母。成熟大厂的高`REVENUE_PER_EMPLOYEE`也不能取代新玩法的`ORIGINAL_HOOKS_PER_DEV_YEAR`。

## UGC技术史增量：Nelson Sexton与Future Trash的两条反方向路径

[源证据与完整对照](../../book/research-notes/ugc-to-standalone-and-platform-finance-ladders-2026-10-09.md)：Nelson Sexton于2012–13 Roblox中的《Deadzone》起步，换Unity重建《Unturned》并2014 Steam发行，2021年Xbox本人访谈证实。这是`UGC→Standalone`真实产品路线，与Zeekerss“在Roblox学习制作技能，后来另外制作《Lethal Company》”不同。Future Trash 2023时UE5独立产品难获融资，反而转入UEFN，并经多轮产品试验与2014? **更正：2024年底**累计二十亿分钟UEFN玩家体验后融得500万美元seed，显示`STANDALONE_ATTEMPT→UGC→FINANCING`的反向链。详细披露为Epic与合作工作室2026-08-19案例，不能据此判断一般创作者融资成功率。2026-06 Epic宣布UE6未来统一传统Unreal与UEFN、目标2027年底EA；**不是现有UGC项目已无障碍迁出**。

## 9. MOD / Roblox / UEFN：买中间件之外的更大工业生产能力市场

[全案例审计Schema](../../schemas/technology-opportunity-window-audit.md)已将`PLATFORM_UGC_WINDOW`独立编码。借助已有游戏的Mod/服务器直接验证玩法（1999 CS、2000s Red Orchestra/Killing Floor、2013 Arma大逃杀）和Unity插件市场的意义相通：**作者不必先从零支付完整基础设施**，先把新规则交给玩家。Roblox在此基础上进一步提供托管、账号、跨平台分发、作品发现和DevEx收入；UEFN于**2023-03-22**上线，直接让创作者向Fortnite生态发行UEFN岛并使用Epic的全球玩家及分成系统。Roblox与UEFN产品有可能**长期留在平台内商业运营**，不意味着UGC只是某个Steam项目融资前的免费Demo；Standalone需重新审技术/资产产权、运行时、后端、发行和成本。

硬来源：Epic https://www.unrealengine.com/blog/unreal-editor-for-fortnite-is-now-available-in-beta ；Roblox 2025 10-K https://www.sec.gov/Archives/edgar/data/1315098/000131509826000024/rblx-20251231.htm 。多案例验证见[案例全矩阵](../../metadata/technology-opportunity-window-matrix.md)与[书稿第八篇](../../book/chapters/08-the-tools-were-already-there.md)。
