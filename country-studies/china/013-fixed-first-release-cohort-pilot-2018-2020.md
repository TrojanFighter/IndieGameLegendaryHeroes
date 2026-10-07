# 013 — 固定首发队列真的能不能算？中国 × 波兰 × 韩国 Steam 2018–2020 实证试跑

- Program: C / 中国国情研究：完整团队形成 × 第二次尝试能力
- Status: **FEASIBILITY PILOT / MANUALLY VERIFIED CONVENIENCE CASES / NO COUNTRY RATE**
- As-of: 2026-10-07
- Related: [012 完整作者型团队供给代理](012-full-cycle-authoring-team-supply-proxy-china-vs-comparators.md) / [Steam第二次发行生存基线037](../../book/research-notes/steam-second-release-survival-baseline-037.md) / [011 失败后二次尝试](011-boundary-wandering-earth-capability-second-chance-2024-2026.md)
- Core question: **能否用同一规则，从中国、波兰、韩国2018–2020首次Steam商业发行者出发，统一观察3年/5年第二次发行与第二次真实项目？**
- Critical boundary: **本表是索引可见案例的管线验证，不是随机抽样，也绝不计算国别发生率。** 当前公开VGI/Sensor Tower网页索引不构成完整抽样框；完整国家过滤/导出受账户权限限制。下列案例的作用是检查变量、识别数据污染和证明研究设计可执行。

## 0. 试跑结论：能算，但“第二款Steam app率”远远不够

本轮实际把中国、波兰、韩国多个2018–2020首发主体放进统一表后，立刻出现四个不能忽略的问题：

1. **Early Access vs 1.0**：首个付费EA已经是一次真实商业发行，必须作为T0；否则Green Hell、Bright Memory、No Umbrellas Allowed等会被人为推迟1–2年。
2. **developer string != real studio**：平台开发者字符串可能拆分/改名/合并，必须人工核工作室身份；不能只靠数据库“First Game Developed”判定职业首作。
3. **corporate entity != authoring team**：LINE Games这类公司可以在平台上反复发行，但公司层连续不等于同一核心团队作者性连续。
4. **second shipped game != second meaningful attempt**：Creepy Jar在2019年底已经启动StarRupture，但直到2026才Steam EA；如果只看5年内第二款“发售”，会把真实持续开发误判成退出。

因此，正式指标至少需要同时保留：
- `SECOND_STEAM_RELEASE_WITHIN_3Y`
- `SECOND_STEAM_RELEASE_WITHIN_5Y`
- `SECOND_MEANINGFUL_ATTEMPT_WITHIN_5Y`
- `SECOND_DISTINCT_IP_WITHIN_5Y`
- `CORE_TEAM_CONTINUITY`

## 1. 统一规则

### 1.1 T0 = 首次商业可购买/可付费Steam发行

- **付费 Early Access 算T0**；
- 1.0若晚于EA，不重新计时；
- 免费Demo、Prologue、限时测试不算；
- 若免费游戏本身就是正式F2P产品，则算商业发行，但必须标 `F2P_FULL_PRODUCT`；
- 同一作品从EA到1.0不是“第二款”。

### 1.2 第二次尝试分三层

```text
SECOND_STEAM_RELEASE
    = 第二个可独立购买/正式F2P的Steam product

SECOND_DISTINCT_IP
    = 非同一作品完整重制/续作/同IP扩建，至少是新的产品问题

SECOND_MEANINGFUL_ATTEMPT
    = 有公开可核的正式研发启动、团队投入、原型/公告/融资/招聘，
      即使5年内尚未ship
```

### 1.3 单位分层

- `PLATFORM_ENTITY`：Steam/VGI显示的developer name；
- `LEGAL_STUDIO`：公司/法人；
- `AUTHOR_TEAM`：可识别核心制作组；
- `INDIVIDUAL_AUTHOR`：单人或极小团队主创。

**国别比较只允许同层比较。** 企业级LINE Games不能与FYQD单人工作室直接混成“团队继续率”。

## 2. 实证试跑表：只验证管线，不给国家比例

### 2.1 中国 convenience cases

| Entity | Type | T0 / first commercial Steam product | 2nd commercial product | <=3y? | <=5y? | distinct IP <=5y? | Key warning |
|---|---|---|---|---|---|---|---|
| **SF** | indie platform entity | 2018-03-01 *Dreams of Greatness* | none observed in VGI as of 2026 | NO | NO | NO | developer-name identity not independently reconstructed |
| **Potato Games** | indie platform entity | 2018-03-30 *Ball Driver* | 2023-01-25 *Handyman Corporation* | NO | **YES** | YES | cross-developer/co-development credit needs core-team check |
| **FYQD-Studio / 曾贤成** | individual author / studio label | **2019-01-11 EA** *Bright Memory* | 2021-11-11 *Bright Memory: Infinite* | **YES** | **YES** | **NO / same franchise-rebuild** | platform repeat is not a new IP; still clear authorial continuity |
| **Hippo Games** | indie platform entity | 2020-05-21 *Kinda Heroes* | 2021-09-28 *Tap Tap Builder* | **YES** | **YES** | likely YES | exact same-core continuity still unverified |

**China source notes**
- VGI/Sensor Tower: SF HQ China, one developed game, first/last 2018-03-01.
- VGI/Sensor Tower: Potato Games HQ China, first game 2018-03-30; *Handyman Corporation* 2023-01-25.
- PLAYISM and Steam: FYQD-Studio is a Chinese individual indie developer; *Bright Memory* paid EA 2019-01-11, *Infinite* Steam 2021-11-11. PLAYISM explicitly describes Infinite as the greatly evolved/full version lineage of the 2019 product, so `SECOND_DISTINCT_IP=NO`.
- VGI/Sensor Tower: Hippo Games HQ China; *Kinda Heroes* 2020-05-21, *Tap Tap Builder* 2021-09-28.

Public URLs:
- https://app.sensortower.com/vgi/developer/3585/sf
- https://app.sensortower.com/vgi/developer/8334/potato-games
- https://app.sensortower.com/vgi/developer/37046/hippo-games
- https://help.steampowered.com/en/wizard/HelpWithGameTechnicalIssue?appid=955050
- https://playism.com/news/2021/1028/1340/
- https://store.steampowered.com/app/1178830/Bright_Memory_Infinite/

### 2.2 波兰 convenience cases

| Entity | Type | T0 / first commercial Steam product | 2nd commercial product | <=3y? | <=5y? | meaningful attempt <=5y? | Key warning |
|---|---|---|---|---|---|---|---|
| **Monster Couch** | indie studio | 2018-05-29 *Die for Valhalla!* | 2019-07-26 *Tetsumo Party* | **YES** | **YES** | YES | later *Wingspan* includes licensed board-game IP; distinguish authorial/product type |
| **Creepy Jar** | premium indie studio | **2018-08-29 EA** *Green Hell* | 2026-01-06 *StarRupture* | NO | NO | **YES — development started late 2019** | strongest proof that ship-only metric undercounts continuation |
| **VARSAV Game Studios** | studio / publisher-investor | **2020-11-17 Steam** *Bee Simulator* | 2021-11-02 *Giants Uprising* | **YES** | **YES** | YES | studio says Bee Simulator first game released cross-platform Nov 2019; Steam-only T0 differs from studio career T0 |

**Poland source notes**
- VGI: Monster Couch HQ Poland, *Die for Valhalla!* 2018-05-29, *Tetsumo Party* 2019-07-26; Monster Couch official press sheet independently says based in Poznań, Poland.
- Creepy Jar official: Warsaw, Poland; *Green Hell* Steam EA 2018-08-29, full 2019-09-05; company says it **started work on StarRupture in late 2019**; Steam launch of StarRupture occurred 2026-01-06.
- VARSAV official: Warsaw studio; studio’s first game *Bee Simulator* released cross-platform Nov 2019, but Steam page dates PC Steam release 2020-11-17; *Giants Uprising* Steam 2021-11-02. This is a deliberate warning that “first Steam release” is not always “first commercial product anywhere”.

Public URLs:
- https://app.sensortower.com/vgi/developer/20026/monster-couch
- https://www.monstercouch.com/press/sheet.php?p=tetsumo_party
- https://creepyjar.com/en/company/
- https://store.steampowered.com/developer/CreepyJar/
- https://varsav.com/en/about-us/
- https://store.steampowered.com/app/914750/Bee_Simulator/
- https://store.steampowered.com/app/1109160/Giants_Uprising/

### 2.3 韩国 convenience cases

| Entity | Type | T0 / first commercial Steam product | 2nd commercial product | <=3y? | <=5y? | distinct IP <=5y? | Key warning |
|---|---|---|---|---|---|---|---|
| **TEAM HORAY** | small author-team studio | 2018-02-14/15 *Dungreed* | **2025-04-03 EA** *Sephiria* | NO | NO | NO within5y | second project eventually appears ~7y later; team continuity is unusually well documented |
| **LINE Games Corporation** | **corporate control** | 2018-03-16 *Next Hero* | 2021-11-29 *BURIED STARS* | NO | **YES** | YES at company level | **do not mix into author-team rate**; corporate developer string can span unrelated teams |
| **Hoochoo Game Studios** | Seoul indie studio | **2020-06-24 EA** *No Umbrellas Allowed* | **2023-08-02 EA** *Golden Record Retriever* | NO (~3y1m) | **YES** | YES | official studio retrospective says second title failed commercially, then third title followed in 2025 |

**Korea source notes**
- KOCCA directory: TEAM HORAY is a Korean game company founded by four core developers; first project *Dungreed* in 2018 and later *Sephiria*. Steam: *Dungreed* 2018-02-14 Korean-store date; *Sephiria* EA 2025-04-03, 1.0 2026-07-31. Thus no second commercial Steam release within5y, but core-team continuation later is directly visible.
- VGI: LINE Games HQ South Korea; *Next Hero* 2018-03-16, *BURIED STARS* 2021-11-29. It is retained only as a **corporate-level negative control**.
- KOCCA: Hoochoo is based in Seoul. Steam: *No Umbrellas Allowed* paid EA 2020-06-24; *Golden Record Retriever* EA 2023-08-02. Hoochoo’s own 2026 About page explicitly says the second title **did not achieve commercial success** and describes design/balance/entry-barrier lessons leading to 2025 *Forest Heroes*. This is a rare direct `SECOND_ATTEMPT -> FAILURE -> THIRD_ATTEMPT` sequence.

Public URLs:
- https://welcon.kocca.kr/mobile/en/directory/content/dungreed--10252
- https://store.steampowered.com/app/753420/Dungreed/
- https://store.steampowered.com/app/2436940/Sephiria/
- https://app.sensortower.com/vgi/developer/2706/line-games-corporation
- https://welcon.kocca.kr/en/directory/company/hoochoo-game-studios-coltd--2807
- https://store.steampowered.com/app/1301390/No_Umbrellas_Allowed/
- https://store.steampowered.com/app/2119580/Golden_Record_Retriever/
- https://hoochoogamestudios.com/about

## 3. 本轮最重要的不是表里谁“胜”，而是五种测量故障已经被实证发现

### 3.1 Early Access 会改变国别继续率

如果错误地用1.0日期：
- FYQD T0从2019推到2020；
- Green Hell从2018推到2019；
- Hoochoo从2020推到2021；
- TEAM HORAY第二款从2025 EA推到2026 1.0。

这会系统性缩短开发者可观察等待时间，并把一些 `NO_3Y` 误改成 `YES_3Y`。

**正式规则：首次有价/正式F2P公开商业可玩版本 = T0。**

### 3.2 “第二款”可能只是同一作者项目完成版

FYQD是最清楚的例子：
- Steam上确实有两个独立App；
- 时间上2019→2021符合3年内第二次发行；
- 但PLAYISM把Infinite明确描述为2019 *Bright Memory* 大幅进化的完整版本，同一世界/产品线。

所以：
`SECOND_STEAM_APP=YES`
但
`SECOND_DISTINCT_IP=NO`。

研究作者性不能只靠AppID数。

### 3.3 真正的第二次尝试可以在“第二款尚未发售”时已经发生

Creepy Jar：
- *Green Hell* 2018 EA；
- 官方称StarRupture **late 2019开始研发**；
- Steam直到2026才EA。

因此：
- `SECOND_SHIP_WITHIN_5Y=NO`
- `SECOND_MEANINGFUL_ATTEMPT_WITHIN_5Y=YES`

如果我们的真正问题是“第一款以后团队还有没有下一次机会”，后者更接近目标变量。

### 3.4 企业名可以伪造“作者团队连续性”

LINE Games在数据库中2018、2021、2023、2026持续作为developer出现，但这不能证明2018 *Next Hero* 的核心创作者在2021 *BURIED STARS*仍拥有问题定义权。

因此至少分：
- `ENTITY_COHORT`
- `AUTHOR_TEAM_SUBCOHORT`

企业连续率可以研究公司资源配置，**绝不能冒充创作者团队连续率**。

### 3.5 Steam-only会错认真正的首次商业产品

VARSAV官方称 *Bee Simulator* 已于2019年11月在PC/PS/Xbox/Switch发行，但Steam页面显示2020-11-17。若研究“职业团队第一次面对市场”，跨平台T0更正确；若研究“Steam平台第二次发行”，Steam T0更可复制。

因此正式研究要建立两个时钟：
- `FIRST_COMMERCIAL_ANY_PLATFORM_DATE`
- `FIRST_STEAM_COMMERCIAL_DATE`

012的Steam队列只用后者；“团队人生”分析优先前者。

## 4. 这组便利样本**绝不能**算中国/波兰/韩国百分比

原因不是“样本太小”这么简单，而是**入组机制不独立于结果**：

- VGI公开网页容易被搜索引擎索引的开发者不是随机开发者；
- 我们主动搜索过已知案例，知名/持续开发者更容易被发现；
- “没有第二款”的主体反而更难拥有官网、采访和公司档案；
- 国家标签由VGI或公开公司地址提供，缺失国家的开发者更容易被淘汰；
- 目前每国案例是为了覆盖不同数据故障，有意加入正/负例。

所以严禁从当前表写：
- “中国2/4三年内继续、波兰2/3，所以……”
- “韩国团队更长寿/更失败”
- “FYQD代表中国solo dev”
- “TEAM HORAY七年后回归证明韩国生态更耐心”

**这个表已经完成它的任务：证明数据模型能跑，并把会让大样本结论出错的字段提前暴露。**

## 5. 可复现的正式schema

```yaml
country: CN | PL | KR
entity_name: string
entity_type: INDIVIDUAL_AUTHOR | AUTHOR_TEAM | STUDIO | CORPORATE_ENTITY
country_verification: VGI | OFFICIAL_COMPANY | INDUSTRY_ASSOCIATION | MULTI_SOURCE
identity_reconciliation: VERIFIED | PARTIAL | STRING_ONLY

first_commercial_any_platform_date: YYYY-MM-DD | UNKNOWN
first_steam_commercial_date: YYYY-MM-DD
first_steam_release_type: PAID_EA | PAID_1_0 | F2P_FULL_PRODUCT
first_product: string

second_steam_commercial_date: YYYY-MM-DD | NONE_OBSERVED
second_product: string | NONE_OBSERVED
second_ship_within_3y: YES | NO | UNKNOWN
second_ship_within_5y: YES | NO | UNKNOWN

second_meaningful_attempt_start_date: YYYY-MM-DD | APPROX_YEAR | UNKNOWN
second_meaningful_attempt_within_5y: YES | NO | UNKNOWN
second_distinct_ip_within_5y: YES | NO | AMBIGUOUS | UNKNOWN

core_team_continuity: VERIFIED | PARTIAL | UNKNOWN | NO
authorial_problem_ownership: VERIFIED | PARTIAL | UNKNOWN
platform_switch: YES | NO | UNKNOWN
studio_closed: YES | NO | UNKNOWN
return_to_employment: YES | NO | UNKNOWN

source_links: []
last_observation: 2026-10-07
```

## 6. 数据管线：公开数据已经足够跑时间线，真正卡的是“国家×真实团队”抽样框

本轮核到两类可用基础设施：

### A. Steam Dataset 2025：时间线层

公开GitHub/Zenodo数据集：
- **239,664 applications**
- **101,226 unique developers**
- 1997–2025
- 来自Steam官方API
- 含release-date/developer等字段
- CC BY 4.0数据许可

GitHub:
https://github.com/vintagedon/steam-dataset-2025

DOI:
https://doi.org/10.5281/zenodo.17286923

**优点**：可以批量重建developer string的首发/后续发行时间。

**缺点**：没有可靠HQ country字段；developer字符串也不是法人/核心团队唯一ID。

### B. Sensor Tower / Video Game Insights：国别与公司档案层

公开单个developer页可见：
- Headquarters Country
- First/Last Game Developed
- Released/Unreleased titles
- developer classification

但批量历史下载/部分筛选能力需要账户等级，公开搜索索引也不完整。

因此当前技术状态是：

```text
Steam full public dataset
    -> can construct release timelines at scale
    -> cannot assign trustworthy country/team alone

VGI public/paid company data
    -> can assign HQ country for many entities
    -> public web index is NOT a complete sample frame

manual official verification
    -> can reconcile team identity / EA / cross-platform / authorial continuity
    -> expensive, suitable for stratified subsample
```

正式国别率仍被**country/team frame access**而不是时间序列算法卡住。

## 7. 下一步不是再手工加十个知名工作室，而是做“两阶段抽样”

### Stage 1 — Platform entity cohort
取得完整或足够接近完整的中国/波兰/韩国2018–2020 Steam-first-release entity frame：
- 先用数据集筛首次Steam商业发行日期；
- 再用国家字段/公司地址批量标国家；
- 不按销量/媒体/是否做第二款筛选；
- 预注册排除规则。

输出：
`ENTITY_SECOND_SHIP_3Y/5Y`

### Stage 2 — Author-team audit
从每国Stage 1按**首作市场牵引×首发年份×团队规模/公司类型**分层抽样，人工核：
- 核心团队是否继续；
- 第二项目是否已启动但尚未ship；
- 是否同IP；
- 是否转平台；
- 是否回大厂/公司关闭；
- 有没有product problem ownership。

输出：
`AUTHORIAL_SECOND_ATTEMPT_5Y`

这两层结果很可能不同，而差值本身就是产业组织信息。

## 8. 本轮可以保留的三个机制发现

### Finding A — 第二次机会有时比第二次发售早很多
Creepy Jar 2019已经进入第二项目，2026才ship。若中国团队常在融资/制作期卡更久，单纯“5年内第二款Steam”会把**开发周期差异误判成团队死亡**。

### Finding B — 第二款也可以失败，但团队继续第三次
Hoochoo官方主动承认 *Golden Record Retriever* 商业失败，并把具体设计/难度/入门门槛错误转入2025第三作 *Forest Heroes*。它是比“坚持就成功”更有研究价值的序列：
`SHIP -> SECOND ATTEMPT -> COMMERCIAL FAILURE -> THIRD ATTEMPT`。

### Finding C — 同一IP持续生产与新题材能力要分开
FYQD两款Bright Memory明确证明一个独立作者可以把首次商业验证扩大成更完整产品；但它不能证明该作者已经建立“不断提出不同原创IP”的工作室机器。

因此未来的 `FULL_CYCLE_TEAM_DENSITY` 要分别统计：
- `repeat shipping`
- `distinct problem generation`
- `core-team continuity`

## 9. Verdict

**我们已经从“应该怎么研究”推进到了“同一规则可以实际编码公开案例”，但还没有资格报国别继续率。**

目前最硬的结论不是“中国样本比波兰差多少”，而是：

> **要验证“中国游戏工业的人才→完整团队→连续作者转化率异常低”，平台第二款只是第一层。真正的检验必须固定首发时间、处理EA、拆开公司与团队、识别第二项目启动，并避免从2026仍然有新闻的人反向抽样。**

这也给012的核心命题增加了一个真正可执行的证伪条件：

- 若完整抽样后，中国 `ENTITY_SECOND_SHIP_5Y` 和 `AUTHORIAL_SECOND_ATTEMPT_5Y` 与韩国/波兰接近，则中国主要问题更可能发生在**首次完整团队形成之前**；
- 若首作团队数量已经少、且首作后作者团队5年继续率仍更低，则“低出生率 + 高流失率”同时成立；
- 如果实体继续率正常、作者团队继续率低，则问题集中在**公司连续、作者权不连续**。

**三种结果都会改变“老中不行”的具体诊断，所以不能预设答案。**
