# 斯拉夫游戏工业技术分代与生产资料吸收：全部研究主题接入（2026-10-09）

- **Status:** THEMATIC APPLICATION / EVIDENCE REVIEW REQUIRED
- **通用规范：** [Technology Opportunity Window Audit](../../schemas/technology-opportunity-window-audit.md) · [游戏工业技术分代003](../../cross-industry/industrial-revolutions/003-game-industry-technology-regimes.md) · [Unity/中间件/AI分代004](../../cross-industry/industrial-revolutions/004-unity-asset-store-network-middleware-ai-indie-industrialization.md)。
- **编制方法：** 本区目前不是根目录的63个Case，而是8个主题证据研究组，SLAVIC-007存在并行表，因此只在此处统一编码，不改写单条来源账本、不杜撰不存在的人物Case，也不把已有技术史故事套进某一个“自研坏、买中间件好”的先验。

| 研究主题 | 可用生产资料/技术窗口 | 创作者/公司做出的具体选择 | 需要新增的比较与证据 |
| --- | --- | --- | --- |
| [001《坦克世界》](evidence/SLAVIC-001-wargaming-world-of-tanks-turning-point.md) | **BigWorld**澳大利亚专有商业MMO技术，Wargaming 2010产品采用并于**2012收购** | 先利用外部中间件支撑15v15战争网游，再把关键生产资料购入公司，深化控制与定制。不是“先组大队自研万物” | license费用、首发时改动、引擎人数/服务器运维、收购前后FTE/性能指标 |
| [002 GSC→4A](evidence/SLAVIC-002-gsc-4a-studio-schism.md) | GSC的X-Ray技术与工作室协作传统；4A分离后建立专用4A Engine | **可携带团队技术资本+重新建立独立技术栈**，不能用今日Unity插件现成度否定当时选择 | 2006–10采用/重用的X-Ray技术边界、4A初期研发人年与跨公司产权 |
| [003 IL-2→Gaijin→War Thunder](evidence/SLAVIC-003-il2-gaijin-war-thunder-lineage.md) | Gaijin基于长期飞行/军武游戏技术、Dagor演化 | 原有模拟/飞行技术迁移到面向大众、长期F2P的多人车辆游戏 | 2000s–12引擎能力、哪些为手游/飞行平台复用、哪些为War Thunder增改 |
| [004《World of Warplanes》](evidence/SLAVIC-004-world-of-warplanes-contrast.md) | Wargaming内部《坦克世界》成熟后端、已有技术/团队与品牌 | 同一组织技术投入不能自动生成同品类成功体验；对照Gaijin飞行游戏前史 | 首发引擎/中间件继承、玩家反馈、航空设计与运营效果差异 |
| [005 GSC→4A人才迁移](evidence/SLAVIC-005-gsc-4a-personnel-migration.md) | 真实可携带的工程、工具、项目管理能力，不全能复制旧企业代码 | 技术能力/默会知识离开旧产权主体后在新公司组合 | 人才/代码/技能与法律技术授权分别核，禁止把跳槽直接等于代码转让 |
| [006 Dagor演进](evidence/SLAVIC-006-gaijin-dagor-capability-timeline.md) | Dagor从2002前后持续发展；2023 Gaijin公开部分引擎代码 | **CREATED + INHERITED + DIFFUSED**：有商业长期更新价值的自有引擎，后来成为外部可取得的技术能力 | 2023 BSD-3开源范围、商业运行时未开源部分、同年具体示例 |
| [007战争网游设计矩阵](evidence/SLAVIC-007-war-online-product-structure-matrix.md) | 多人分局/配对/联网系统与模型反复复用 | WoT/War Thunder/World of Warplanes/Warships：设计规则、商业结构与技术规模不应只按同题材排名 | 按用户真实交互、实际服务器/计算时间、玩家规模和历史版本比较 |
| [008量化层](evidence/SLAVIC-008-war-online-quantitative-layer.md) | 工程人年和中间件投入是生产函数的输入 | 量化“掌握技术但未转化玩家价值”的缺口 | 核名义人数 vs FTE年、部门共用资源、license支付、收入与多期留存 |

### 历史核验新增的两条最重要证据

**Wargaming / BigWorld：** Wargaming官方2012收购公告明确说《World of Tanks》建立在BigWorld Technology之上，收购澳大利亚中间件厂商以获得更深控制、集成和更快开发。这是 **BUY→DE-RISK PRODUCT→ACQUIRE SUPPLIER/DEEP CUSTOMIZE** 的先例，不只是独游造轮子的反证。
- 官方：https://worldoftanks.eu/en/news/general-news/wargaming-acquires-bigworld/
- 2012年年度公司官方总结同步确认收购：https://worldoftanks.com/en/news/general-news/2012-warpath/

**Gaijin / Dagor：** Gaijin官方2023-11-02说明部分Dagor源码以BSD-3开放，但其War Thunder产品并未因此开源；引擎与游戏资产/商业产品的版权边界必须保留。
- 官方：https://gaijinent.com/news/dagor-engine-gone-open-source
- 官方GitHub：https://github.com/GaijinEntertainment/DagorEngine

### 必须防止的两种错误

1. 技术平台自研就说明“技术做题失败”：**错**。若独特的模拟/规模/性能构成不可买的价值，自研有可能很经济；要按当时中间件成熟度、许可、人年与产品收益判断。
2. BigWorld外购就说明“Wargaming没技术”：**错**。采购、修改、服务化、扩运营和最终收购供应商都是高技术/高组织能力的不同表现。

**跨代比较锚点：** 先确定1990s–2000s与2010–2026每家公司实际的技术许可和采购条件，再讨论体验主导与技术先行份额变化；不能拿2026 Unity/AI工具责备2006的4A。
