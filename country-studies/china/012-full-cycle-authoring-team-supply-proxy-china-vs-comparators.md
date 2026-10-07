# 012 — 中国缺的究竟是不是“完整作者型团队”？用 Steam 高关注产品管线与工作室密度做第一轮量化代理

- Program: C / 中国国情研究：行业版本 × 团队形成 × 产品自主权
- Status: **QUANTITATIVE PROXY / CROSS-COUNTRY SNAPSHOT / NOT A DIRECT COUNT OF AUTHOR-LED TEAMS**
- As-of: 2026-10-07
- Related: [009 中国游戏雇员创造性劳动](009-china-gameworker-creative-subjectivity-fieldwork-2017-2026.md) / [010 NExT立项权](010-next-studios-greenlight-rights-governance-lifecycle-2017-2024.md) / [011 失败后的第二次机会](011-boundary-wandering-earth-capability-second-chance-2024-2026.md) / [中国商业制度谱系](../../book/research-notes/china-game-commercial-regime-lineage-003.md)
- Core question: **中国拥有巨大玩家市场、成熟商业游戏工业和大量专业人才，却是否相对缺少能独立定义、完成并向全球PC/主机市场推出新产品的稳定团队？**
- Boundary: 本文使用**Steam愿望单Top200国别来源、各国官方/行业协会的工作室与从业者统计、人口**作为代理指标。它们测量的是不同东西，不能直接相除为“创作者比例”；尤其 `TOP200_STEAM_WISHLIST != AUTHOR_LED_TEAM_COUNT`。

## 0. 结论先行：用户的直觉获得了一个强代理信号，但还不是终局证明

2025年7月，波兰官方产业报告引用 Game Industry Conference 对 **Steam Top200愿望单**的开发国统计：

- 瑞典：**14.75** 个标题，占 7.53%
- 波兰：**12**
- 韩国：**10**
- 中国：**8**
- 捷克：**3**
- 芬兰：**2**

中国按绝对数并非没有未来PC产品，但它以约**14.09亿人口**、全球最大级别游戏市场，只在这一个“全球高关注Steam在研产品”截面上排到第10位；波兰、瑞典、韩国的绝对标题数都高于中国。原表因跨国共同开发/来源分摊出现 0.25/0.5 等小数，因此不是简单“工作室个数”。来源：Polish Agency for Enterprise Development / Game Industry Conference，*The Game Industry of Poland – Report 2025*, Table 2, p.29（PDF页码29/文件P28）。

如果只做**人口粗调**（World Bank 2024人口；并非研发人力调节）：

| Country | Top200 wishlist title-equivalents | 2024 population (million) | titles / million population | Relative to China |
|---|---:|---:|---:|---:|
| China | 8 | 1,408.975 | **0.0057** | 1.0× |
| South Korea | 10 | 51.751 | **0.1932** | **34.0×** |
| Poland | 12 | 36.559 | **0.3282** | **57.8×** |
| Czechia | 3 | 10.905 | **0.2751** | **48.5×** |
| Finland | 2 | 5.620 | **0.3559** | **62.7×** |
| Sweden | 14.75 | 10.570 | **1.3955** | **245.8×** |

**这个人口校正只是压力测试，不能解释为生产效率。** 大国人口包含非游戏劳动力；小国人才国际化率高；Steam愿望单有语言、曝光、平台与品类偏差。但差距如此大，足以把“完整全球PC产品团队供给偏薄”升级为一个**值得正式检验的产业结构命题**，而不是继续只靠个案印象。

Sources:
- PARP / GIC, 2025 report p.29: https://www.parp.gov.pl/storage/publications/pdf/EBOOK-GAM-WCAG_27112025.pdf
- World Bank 2024 population: https://data.worldbank.org/indicator/SP.POP.TOTL

## 1. 为什么这个代理比“国产Steam游戏总数”更接近我们的问题

2025年中国第三方“国游销量榜”报告称全年纳入统计国产游戏约**2,091款**，其中大量为低价独立/买断作品；2024同口径约1,660款。该统计为社区/行业观察者数据，**不是官方完整Steam开发者数据库**，且媒体二次转述存在“买断制1757/757”文字冲突，因此这里只作为发现线索，不承担精确分母。

这反而说明一个重要区分：

```
LOTS_OF_RELEASES
    !=
MANY_TEAMS_WITH_GLOBAL_HIGH-DEMAND_PIPELINE
    !=
MANY_TEAMS_CAPABLE_OF_HIGH-SPEC_FRONTIER_IP
```

中国可能同时拥有：
- 很多低成本Steam作品；
- 极强手游/F2P工业；
- 少数头部PC/主机产品；
- 但**中间层——持续产生全球高关注、原创、完整PC/主机产品的稳定团队——密度仍偏低**。

Steam Top200愿望单比“总上架量”更接近**市场已经提前验证有较强全球关注**的生产管线，但仍包括大小项目、IP续作、外包/联合开发，也不能等同“原创作者型工作室”。

## 2. 更强的反事实：韩国同样手游主导，却没有掉到中国的相对密度

中国2024官方报告：
- 国内游戏市场实际销售收入 **3257.83亿元**
- 移动游戏占 **73.12%**
- 客户端游戏占 **20.87%**
- 自研海外收入 **185.57亿美元**

韩国2024官方白皮书（2025版）：
- 游戏市场约 **23.8515万亿韩元**
- 移动游戏占 **59.0%**
- 游戏研发/发行企业 **1,398家**
- 游戏研发/发行人员 **54,285人**（全产业87,576人）

因此韩国也不是一个“天然premium单机社会”。它有强烈的移动/F2P历史和大型在线游戏工业，却在2025-07 Steam Top200愿望单中有 **10个title-equivalents**，高于中国的8；按人口粗调约为中国 **34倍**。

这不能证明韩国组织制度更好，因为：
- 韩国统计“研发+发行企业”与中国缺少同口径企业数；
- Top200可能受2025特定项目周期影响；
- 韩国近年主动向主机/PC转向，本身就是产业政策与公司策略结果；
- 中国拥有庞大的本地PC在线产品和移动跨端产品，Steam不是所有全球化产品的唯一入口。

但它足以**削弱一个过于简单的解释**：

> “中国只是因为手游/F2P占比高，所以Steam完整产品团队少。”

移动商业制度可能是原因之一，但**不是充分解释**。

Sources:
- 中国音数协《2024年中国游戏产业报告》：https://www.cadpa.org.cn/3277/202501/41718.html
- KOCCA, 2025 Game Industry White Paper summary（2024 data）：https://welcon.kocca.kr/ko/info/report/1957738

## 3. 欧洲小国不是“几个明星工作室”，而是有可见的团队密度

### 3.1 Poland

2025 PARP报告：
- **824 active game producers & publishers**
- **14,568** specialists
- 2024 revenue约 **€1.293bn**
- 年度**450+ platform-wise releases**
- studio survey：主要平台 **PC 71.8%**
- 主要商业模式：**premium 69%**
- **40+ Polish game brands**累计销量超过100万
- 97%在波兰开发的游戏面向全球市场

824这个数字因2025数据挖掘方法升级，报告明确说**不宜直接与往年工作室数增长率比较**；其中含publisher/service等主体，不是824个作者型开发组。可是报告目录里还能看到大量6人、8人、10人、30人级别的独立/专业小工作室——不是只靠CDPR、Techland两家公司支撑。

Source: PARP 2025 https://kpo.parp.gov.pl/component/publications/publication/the-game-industry-of-poland---report-2025

### 3.2 Finland

Neogames 2024：
- **270 active studios**
- **4,300** employees（其中约3,800在芬兰、500在芬兰公司海外工作室）
- 2024 turnover **€2.85bn**
- 2023–24两年发布约**120款商业游戏**
- 其中只有约**10款移动游戏**，PC/在线/其他平台发行明显上升
- 研究采访71家公司，但通过注册与公开资料补到141/185家不同字段，主动承认 active studio 定义不可能绝对完整

这很重要：芬兰历史上同样是**移动/GaaS强国**，并非只生产传统买断制，却仍保留了大量活跃工作室和PC/其他平台的新产品供给。它进一步削弱“手游工业天然让完整产品团队消失”的单因解释。

Source: Neogames / PlayFinland https://www.playfinland.fi/state-of-the-industry

### 3.3 Sweden

2025 Game Developer Index（2024数据）：
- **1,101** game companies
- 其中 **202家至少5名员工**
- 行业就业 **9,100+**
- 瑞典境内收入 **SEK36.8bn**
- 93%的公司少于10人

“1,101”显然包含大量微型公司，因此不能和韩国1,398研发/发行企业直接比较。但仅**202个5人以上studio**这一层，就说明一个约1,057万人国家拥有相当厚的稳定制作主体层。

Source: Dataspelsbranschen https://www.dataspelsbranschen.se/rapporter/swedish-games-industry-2025-game-developer-index/

### 3.4 Czechia

2026 Czech Game Developers Association最新数据：
- **178 active studios**
- **3,092** industry workers
- 2025 revenue **CZK9.08bn**
- 2024 record revenue **CZK9.19bn**

更早2024行业报告也指出大多数工作室在10人以下，90%以上企业本地所有，收入98%以上来自海外市场。这里同样体现的是“多节点、小中团队、全球产品市场”的产业结构，而不是单一巨头。

Source: GDA Czech 2026 https://gda.cz/czech-games-industry-outperforms-expectations-generating-more-than-czk-9-billion-in-revenue/

## 4. 不能直接写“中国应该有几万家工作室”，但可以提出一个可核的数量级问题

如果机械按人口匹配：
- 波兰约22.5个“活跃producer/publisher”/百万人；
- 芬兰约48.0个active studio/百万人；
- 捷克约16.3个active studio/百万人；
- 瑞典所有game company约104/百万人，5人以上studio约19.1/百万人。

把这些比例直接乘中国14亿人口，会得到**数万甚至十万级**公司要求；这是**不合法的推断**：
- 国别市场、工资、资本、城市密度、出口依赖、公司注册定义完全不同；
- 瑞典/芬兰大量外国人才，不能把团队数解释为“本民族天生更创作”；
- 中国也可能有大量工商注册/小团队没有被统一行业统计；
- 中国大公司内部一个studio可包含数百/数千人和多个项目，欧洲“公司”单位更碎。

所以我们不需要“证明中国本应有X万工作室”。

真正值得建立的可比指标是：

```
FULL-CYCLE TEAM DENSITY
= number of stable teams that
  1) originated or substantially redefined a product problem;
  2) shipped >=1 complete commercial title;
  3) retained a recognisable core for >=1 additional attempt;
  4) had meaningful scope / prototype / kill decisions;
  5) faced direct external market feedback;
  6) can be observed without success-media selection.
```

这里的**团队**而非公司法人是核心单位。腾讯一个事业群里可能有几十个项目团队；一个芬兰法人可能只有5人；不能直接以公司数替代。

## 5. “前沿IP承制团队少”如何被严谨改写

用户直觉：
> 中国那么大，为什么到了《流浪地球》这种前沿IP，还会落到做砸过《边境》的柳叶刀来做？那还是说明供给不行。

现在可以改写为三个强度不同的命题：

### C1 — VERIFIED CASE
**《流浪地球：望日》IP方确实从接近200份团队提案中挑中柳叶刀；柳叶刀此前《边境》商业/运营受挫，但其太空射击与硬科幻制作经历成为新合同的正资产。**

详见 [011](011-boundary-wandering-earth-capability-second-chance-2024-2026.md)。

### C2 — SUPPORTED PROXY
**中国面向全球PC premium市场的高关注在研产品管线，相对其人口与整个游戏产业规模明显偏薄。**

支持：Top200 Steam wishlist国别快照；韩国/波兰/瑞典对照；中国行业收入/用户体量。
限制：Steam-only，愿望单是市场注意力，不是完整团队数。

### C3 — OPEN / 核心待证
**中国“能从0→1定义并完整交付高规格原创PC/主机产品、且失败后还能再试”的稳定团队密度，显著低于韩国/波兰/北欧/捷克。**

这才是我们真正想证明的“老中不行”产业命题。**目前尚无中国全量team denominator，也没有各国同定义 longitudinal roster，所以状态必须保持 OPEN。**

## 6. 为什么这比“独立游戏数量”更接近真正问题

一个国家可以有很多：
- Game Jam作品；
- Steam低价小游戏；
- 大厂数千人的模块执行岗位；
- 外包团队；
- publisher；
- live-ops事业部；

却依然缺少：

> **“一起做过完整产品→共同吃过市场反馈→仍保留下一次自定问题能力”的核心团队。**

这种主体是产业的**可复用创新节点**。

柳叶刀恰好说明：即便第一次产品商业受挫，**完整做过一次**本身也有稀缺价值。反过来，如果一个行业把一万名专业人才组织成少数超大流水线，却很少产生可以独立重新组合的完整产品核心，那么总就业、总收入和“作者型团队密度”可以同时朝相反方向发展。

这也解释为什么单看中国游戏收入会低估问题。

## 7. 下一轮真正可量化的设计

### A. 不要先统计所有Steam国产游戏，先建“Full-cycle Team Sample Frame”

按**发布年份固定**，例如2020–2022首次商业发行的中国/韩国/波兰/捷克/芬兰原创PC产品，预注册：
- 不按销量筛选；
- 团队有公开开发者/公司身份；
- 非纯移植、纯外包、素材拼装；
- 首次完整商业产品或可识别新核心团队；
- 之后追5年。

每个核心团队编码：
`TEAM_SIZE_START`
`CORE_RETENTION_2Y/5Y`
`SECOND_PROJECT_ATTEMPT`
`SECOND_PROJECT_SHIP`
`PROJECT_KILLED_BUT_TEAM_RETAINED`
`FOUNDER_EXIT`
`RETURN_TO_EMPLOYMENT`
`PUBLISHER/FUNDING`
`PROBLEM_DEFINITION_RIGHTS`
`KILL_RIGHTS`

### B. 对中国大厂另开“内部团队”框架

不能只看法人。
NExT的100人日Demo小组、网易/腾讯/米哈游内部立项cell，都应以**project team**为单位；问：
- 初始2–10人组有多少；
- 多少完成vertical slice；
- 多少得到二次尝试；
- 主创在第一次失败后2/5年是否仍有立项权。

这将直接检验“巨大工业把人才变成专业部件，而不是持续制造完整团队”的命题。

### C. “前沿IP可承制团队”单独做 procurement frame

以后遇到《流浪地球》这类公开征集：
- 全部合格申请团队数；
- 已经ship过何种规模产品；
- 有完整3D pipeline的比例；
- 有原创/承制经历；
- 通过技术测试数量；
- 未入选原因（匿名）；
- 两年后存续/第二项目情况。

这比从最终承制商倒推“全国只有一家能做”严谨得多。

## 8. Verdict

**现在可以比上一轮更强地说：**

中国的症结已经越来越不像“没有人会做游戏”，而像是：

> **庞大的专业人才、收入与用户规模，没有按同等数量级转化为大量稳定、独立承担完整产品判断和全球市场验证的核心团队。**

2025 Steam高愿望单快照不是最终证明，但它第一次给这个判断提供了一个**跨国、同时点、非明星传记式的量化压力测试**。

尤其是**韩国**：
- 同为东亚；
- 同样大型商业公司占据核心；
- 同样移动游戏占主导；
- 但在人口只有中国约1/27的情况下，Top200 Steam wishlist 的来源标题仍比中国更多。

因此，未来不能再只用“儒家/家庭”“手游/F2P”“人口”任一单变量解释中国。更可能是一条**长期团队形成链**的复合损耗：

```
experience capital
→ self-defined prototype
→ small-team ownership
→ greenlight
→ full-cycle ship
→ external market feedback
→ core-team survival
→ second attempt
```

每一层中国都有人通过；真正需要核的是**每一层损失多少，以及为什么**。
