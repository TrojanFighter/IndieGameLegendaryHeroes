# 015 — 台北 × 深圳 GGJ：业余创作者的公共作品栈、全球可发现性与平台分流

- Status: PUBLIC-ATTEMPT PLATFORM-STACK AUDIT / OBSERVABILITY-CORRECTION / NO CREATOR-RATE CLAIM
- Program: C Taiwan comparator
- As of: 2026-10-08
- Parents:
  - [004 — GGJ 2024台北第一会场 Public-Attempt Cohort](004-ggj2024-taipei-public-attempt-cohort.md)
  - [012 — 外部资讯摩擦与弱信号时延](012-external-information-friction-signal-latency.md)
  - [013 — 学生/业余独游默认生产意识](013-student-amateur-indie-default-production-awareness.md)
  - [014 — 放视大赏 × CUSGA 决赛层商品化压力测试](014-selected-student-cohort-productization-taiwan-vs-cusga.md)
- Mainland comparator:
  - [中国002 — GGJ 2024深圳南山 Public-Attempt Pilot](../china/002-ggj-2024-shenzhen-nanshan-public-attempt-pilot.md)
- Core question: 在比学生决赛更低选择强度的48小时game-jam层，两岸业余创作者是否真的表现出“公共作者意识”差距，还是首先存在不同的发布平台栈与可观察性？
- Restriction:
  - 不以Google/全球搜索结果数量直接当“创作者公开意愿”；
  - GitHub/itch缺失不能证明大陆项目未公开，因为中国区并行使用GmHub、B站等本地基础设施；
  - 深圳分母仍为16个目录位置 / 15个不同题名，唯一项目ID reconciliation未完成，因此本文件不计算深圳artifact比例；
  - 台北“至少7/10有公开源码/仓库链接”是当前可确认下限，不等于台湾所有jam平均水平；
  - 同名项目跨平台匹配必须依赖题名、描述、作者或链接链条，不凭模糊搜索猜身份。

## 0. 第一轮结论

在014中，台湾放视大赏与大陆CUSGA的强筛选学生决赛层已经出现明显收敛：Steam商品化比例、Demo与publisher接口没有显示台湾压倒性领先。

把观察层下移到2024 GGJ普通公开尝试者后，出现的第一个强差异并不是：

> 台湾人会公开作品，大陆人不会。

而是：

> 两岸参加同一个Global Game Jam，却默认生活在不同的public-artifact stack里。

台湾台北第一会场的作品页大量直接连接：
- Global Game Jam全球站；
- GitHub；
- itch.io；
- GitHub Pages；
- YouTube / Twitch；
- 英文或双语项目说明。

大陆CiGA则主动构建：
- GmHub本地报名 / 组队 / 展示；
- GGJ全球站作为第二层全球归档；
- B站等本地公开视频；
- 部分作者再主动跨发itch/GitHub等全球平台。

更关键的是，CiGA官方从2019到2024多次明确提醒：
> 注册Global Game Jam官网时，验证码步骤“可能需要科学上网”。

2024官方报名说明同时明确：
- GmHub负责中国区报名、组队、作品展示和直播；
- GGJ全球官网用于让作品进入全球展示和交流；
- 参与者最好两个体系都注册。

Sources:
https://www.ciga.me/blog/13-21-ggj-2024-x-ciga
https://www.ciga.me/blog/global-game-jam-9a674d9d-2441-4d70-b356-be7e7c7c2467

这意味着：

GLOBAL PUBLICATION ROUTE在大陆不是不存在，而是多了一层额外操作与平台切换成本。

建议新增变量：

PUBLIC_ARTIFACT_STACK
GLOBAL_DISCOVERABILITY
PLATFORM_SUBSTITUTION
OBSERVABILITY_FRICTION
CROSS_BORDER_SERENDIPITY
DUAL_POSTING_COST
ARCHIVE_CONTINUITY

---

# 1. 台北第一会场：全球公共栈几乎是活动默认界面

## TW-GGJSTACK-E01｜固定分母仍是10个实际组，不是11个目录listing

主办方IGDSHARE活动复盘明确列A—J十组：
https://igdshare.org/content/mitjam12-ggj2024-archives

GGJ目录则有11条，其中 test-taipei-2024 是测试条目：
https://globalgamejam.org/group/639/games

因此：
- actual teams = 10；
- directory listings = 11；
- artifact test entry = 1。

这一点沿用004，不重新计算人口比例。

## TW-GGJSTACK-E02｜至少7/10实际项目留下直接公共代码/仓库链接

当前可由GGJ第一方页面或GGJ个人页直接确认：

### A — 猜猜我是誰
- GGJ source files；
- GitHub repository。

Source:
https://globalgamejam.org/games/2024/caicaiwoshishui-2

### E — 神說，讓我笑
- itch playable；
- source files；
- GitHub repository；
- 中英双语项目说明。

Source:
https://globalgamejam.org/games/2024/jizhiwenda-8

### F — Make Me Laugh
- GGJ用户页直接记录源码 GitHub；
- 同一参与者后来继续参加2025、2026 jam；
- 其GGJ profile还公开列有2023 Steam商业作品。

Source:
https://globalgamejam.org/users/guminghong

### G — The Slap
- source files；
- GitHub repository；
- 明确程序/美术/设计音效分工；
- 英文项目说明。

Source:
https://globalgamejam.org/games/2024/slap-3

### H — 笑到終點：迷因三寶之路
- source files；
- GitHub repository。

Source:
https://globalgamejam.org/games/2024/xiaodaozhongdianmiyinsanbaozhilu-5

### I — Win87
- itch playable；
- website；
- source files；
- GitHub repository。

Source:
https://globalgamejam.org/games/2024/teami-6

### J — LetMeLaugh
- GitHub Pages playable；
- source files；
- GitHub repository；
- 中英双语；
- Mac / Windows。

Source:
https://globalgamejam.org/games/2024/letmelaugh-5

因此当前可以写：

> 在这个固定台北会场里，至少70%的实际团队在GGJ全球页上或由GGJ个人页直接暴露了可复查的代码仓库/源码链路。

但不能写：
“台湾70%的业余游戏开发者都公开源码。”

这是单会场、18+、有一定制作熟悉度的自选样本。

---

# 2. 台湾活动组织层本身就在“全球公开栈”里

台北第一会场GGJ官方页直接包含：
- KKTIX本地报名；
- Twitch live stream；
- 中英文活动说明；
- 国际参与者欢迎说明；
- Photon Engine现场支持；
- GGJ全球作品页。

Source:
https://globalgamejam.org/jam-sites/2024/mit-game-jam-12-x-global-game-jam-2024

这里的关键不是“台湾人比较爱GitHub”，而是：

> 本地报名、全球身份、全球作品归档、GitHub/itch/Twitch可以在默认网络环境里同时工作。

因此一个普通参与者完成作品后，把它留在全球开发者可搜索的位置几乎不需要切换网络制度。

---

# 3. 深圳南山：不能拿“搜不到GitHub”证明公共意识弱

## CN-GGJSTACK-E01｜中国区官方主动构建GmHub替代/并行层

CiGA 2024官方GGJ说明：
- GmHub用于报名、开发者身份设置、组队、线上参与；
- 成品上传中国区线上展示；
- 作品可进入直播展示；
- 线下站点另有本地展示；
- 同时要求注册GGJ全球官网，以便作品进入全球展示和交流。

Source:
https://www.ciga.me/blog/13-21-ggj-2024-x-ciga

这是一种典型的：

LOCAL INFRASTRUCTURE
+
GLOBAL ARCHIVE BRIDGE

而不是完全封闭的本地活动。

## CN-GGJSTACK-E02｜全球GGJ注册本身存在明确额外网络摩擦

同一2024官方说明写明：
- GGJ全球站注册时验证码可能需要“科学上网”。

CiGA 2019生存指南也使用同样提醒：
https://www.ciga.me/blog/global-game-jam-9a674d9d-2441-4d70-b356-be7e7c7c2467

2022、2023等组织说明继续出现类似提醒。

这说明该摩擦不是一次偶发故障。

研究含义不是：
“大陆参与者无法参加GGJ。”

恰好相反，CiGA建立GmHub和组织流程成功绕过了很多摩擦。

真正含义是：

> 大陆创作者要进入同一个全球公共作品栈，需要比台湾创作者多完成至少一层平台/网络切换。

---

# 4. 深圳也存在主动全球公开的普通作者，不能被“信息茧房”总论吞掉

## CN-GGJSTACK-E03｜《口腔妙妙屋》同时进入itch与B站

GGJ深圳南山官方目录包含《口腔妙妙屋》：
https://globalgamejam.org/group/499/games

itch页面：
- downloadable Windows game；
- 中英双语说明；
- 标记为Released。

Source:
https://fuju233.itch.io/mouthful-challenge

B站在GGJ结束当日即有：
“〖48小时独立游戏〗口腔妙妙屋（操纵你的舌头牙齿）GGJ2024”
公开视频。

这展示了一种大陆常见的双栈行为：

global playable artifact on itch
+
domestic video/social visibility on Bilibili.

因此只查GitHub会漏掉一部分真实公开行为。

## CN-GGJSTACK-E04｜《酶你不行 Funzyme》作者本身已有长期全球indie痕迹

深圳南山GGJ目录包含《酶你不行 Funzyme》：
https://globalgamejam.org/group/499/games

对应itch项目由 warlinestudio 发布：
- downloadable；
- 48小时Game Jam说明；
- 两人本地合作；
- Name your own price。

Source:
https://warlinestudio.itch.io/funzyme

同一itch账号在2022已经发布《You are second to none》：
- 作者自述项目花费整个高中三年；
- 单人开发；
- 中英文；
- Name your own price；
- GameMaker制作。

Source:
https://warlinestudio.itch.io/you-are-second-to-none

更值得注意的是，同一账号还直接在Mega Crit的itch作品评论区以英文交流，并主动表示愿意免费把新作翻译给中国玩家。

Source:
https://megacrit.itch.io/dancing-duelists/comments

这不是“大陆普通作者都很国际化”的比例证据。

它的作用恰好相反：
> 在一个非媒体明星、固定GGJ目录抽出的普通公开项目中，也能发现已经长期使用全球独游平台、英文沟通和跨境本地化思维的作者。

因此“大陆业余层整体没有全球作者意识”不能由信息环境直接推出。

---

# 5. 真正的新差异：GLOBAL DISCOVERABILITY ≠ PUBLIC CREATION

现在必须区分四个概念：

### PUBLIC CREATION
有没有公开做出可玩的东西。

### DOMESTIC DISCOVERABILITY
国内玩家/开发者是否能在B站、GmHub、TapTap等看到。

### GLOBAL DISCOVERABILITY
海外开发者/玩家是否能从itch、GitHub、GGJ、Steam等直接找到。

### SOURCE REUSABILITY
是否公开源码/仓库，方便他人fork、学习、issue、贡献或长期追踪。

台湾第一会场当前的强项主要体现在：
GLOBAL DISCOVERABILITY + SOURCE REUSABILITY。

深圳现有材料至少证明：
PUBLIC CREATION存在；
DOMESTIC + GLOBAL双栈个案存在；
但完整比例尚无法计算。

因此不要把：
“Google没搜到”
翻译成：
“作者没有公开”。

---

# 6. 一个研究者自己的偏差：OBSERVABILITY ASYMMETRY

这条尤其重要，因为它会直接制造错误国别结论。

台北：
- GGJ group页搜索稳定；
- 单项目页大量被索引；
- GitHub/itch链接直接暴露；
- organiser还保存A—J活动录像目录。

深圳：
- GGJ group 499页面在实际抓取中时常403；
- 16 listing / 15 unique-title仍需稳定ID reconciliation；
- 中国区另有GmHub内容层；
- 部分作品痕迹分散于B站/itch等；
- GGJ全球站注册还存在官方承认的网络摩擦。

所以如果研究方法写成：

> “Google项目名 + GitHub，没搜到就记0”

一定会系统性低估大陆公开创作。

新增：

OBSERVABILITY_FRICTION

定义：
> 一个真实存在的公开作品，被外部研究者用统一搜索工具发现、唯一匹配和长期复查所需的额外成本。

它与creator awareness相关，但不是同一个变量。

---

# 7. 平台分流本身仍然会产生真实后果

虽然不能把它当“创作者不行”，但平台栈差异不是无关紧要。

## H1｜CROSS-BORDER SERENDIPITY

GitHub / itch / GGJ全球页上的作品：
- 更容易被海外作者偶然撞见；
- 更容易进入全球搜索；
- 更容易直接收到英文反馈；
- 更容易产生fork / issue / collaboration。

GmHub / B站上的作品：
- 在中国本地可能拥有更强曝光；
- 但海外随机开发者发现它们的概率可能更低。

需要流量/推荐系统证据进一步验证。

## H2｜REFERENCE RECIPROCITY

一个人不仅“看国外”，还把自己的东西放到国外可以回应的平台，才形成：

foreign signal
→ local creator
→ artifact
→ global feedback
→ next iteration

的闭环。

台湾公共栈让这个闭环默认更短。

大陆高主动性创作者可以通过dual-posting达到同样效果，
但需要额外操作。

## H3｜LOCAL PLATFORM ADVANTAGE

不能只看损失。

GmHub / B站也可能提供：
- 更低语言门槛；
- 更强本地玩家反馈；
- CiGA活动聚合；
- 直播与赛事曝光；
- 更适合中国社交传播。

因此平台分流可能提高国内conversion，同时降低国际serendipity。

这需要真实访问/互动数据而不是价值判断。

---

# 8. 台北“仓库多”还有一个竞争解释：活动规范本身

多个台北项目勾选GGJ diversifier：
Sharing is caring - (Sponsored by Github)。

这意味着GitHub公开行为可能部分受到活动diversifier激励，而不是台湾社会自然产生。

因此不能将7/10仓库下限全部归因于：
- 台湾网络自由；
- 台湾学生意识；
- 台湾开源文化。

真正需要比较：
- 同一GGJ全球活动中深圳项目是否也参加此diversifier；
- organisers是否主动教学/推荐GitHub；
- participant prehistory。

这也是为什么015不报告“台湾比深圳高X倍”。

---

# 9. 这怎样修正“意识差距巨大”命题

014已经发现：

### 强筛选学生决赛层
两岸Steam productization高度收敛。

015现在进一步发现：

### 较低选择强度jam层
大陆也能抽到：
- itch作者；
- 长期个人indie开发；
- 英文全球社区互动；
- 双语作品；
- B站+itch双栈发布。

因此：
> “大陆普通业余作者没有独立作者意识”仍然过强。

但台湾依然存在一个更结构性的优势候选：

> GLOBAL AUTHORSHIP BY DEFAULT。

即：
不用先解决网络工具、平台替代、国内/国际双重发布，就可以从报名、开发、源码、试玩到社群反馈一直留在同一全球公共栈里。

大陆更像：

> GLOBAL AUTHORSHIP BY ACTIVE BRIDGING。

有能力、有主动性的人完全可以做到；
CiGA也在制度化帮助他们做到；
但默认路径多了一层friction。

这可能是“中位数意识差距”形成的机制之一，而不是能力本身的差距。

---

# 10. 下一步应该比较dual-posting，不是比较“有没有GitHub”

深圳下一轮固定15个不同题名，逐项建立：

- GGJ page；
- GmHub page；
- Bilibili；
- TapTap；
- itch；
- GitHub；
- Gitee；
- playable build；
- source repository；
- bilingual description；
- post-2024 followup。

台北10组则同字段编码：
- GGJ；
- KKTIX/IGDSHARE；
- YouTube/Twitch；
- itch；
- GitHub；
- Steam；
- post-2024 followup。

真正值得比较的指标：

### LOCAL_ONLY
只存在本地区域平台。

### GLOBAL_ONLY
只存在全球平台。

### DUAL_POSTED
国内/本地与全球平台均有。

### SOURCE_OPEN
源码/仓库可复用。

### PLAYABLE_GLOBAL
无需本地账号即可全球试玩/下载。

### LONGITUDINAL_IDENTITY
作者账号可连续追踪到下一次公开创作。

这比“搜到几个GitHub”更接近我们真正研究的：
一个普通创作者能否进入全球创作者共同体。

---

# 11. 当前 Verdict

本轮不支持：

> 台湾普通jam作者会公开、大陆普通jam作者不会。

当前支持：

> 台湾与大陆业余创作者都存在很强的公开创作与全球化个体；差异首先体现在默认公共平台栈和进入全球创作者共同体的摩擦。台湾可以把GGJ、GitHub、itch、Twitch等全球基础设施当默认连续环境；大陆CiGA则不得不建立GmHub等本地替代/桥接层，并明确处理GGJ全球网站的网络访问摩擦。高主动性的大陆作者可以通过dual-posting跨过这一层，但普通创作者是否因此更少进入全球弱信号—反馈循环，仍待完整固定队列验证。

这比“台湾人意识先进、大陆人意识落后”更具体，也更可证伪。
