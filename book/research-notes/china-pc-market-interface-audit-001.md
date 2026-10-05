# 中国 PC 独立游戏 Market-Interface Audit 001：七个项目如何找到、错过或失去自己的市场接口

- Status: RESEARCH NOTE / CROSS-CASE AUDIT
- Scope: 中国 PC premium / indie / indie-adjacent projects
- Related: `author-corpus/AC-009-invisible-wall-distribution-regime.md`, `book/research-notes/china-indie-distribution-regime-001.md`
- Cases / comparators: My Time at Portia, Dyson Sphere Program, Eastward, The Scroll of Taiwu, Amazing Cultivation Simulator, Sultan's Game, Boundary
- Core question: **中国开发者真正缺的是“国内流量”还是“知道自己的玩家在哪里、该用什么市场接口接触他们”的能力？**

---

## 0. 结论先行

这七个项目不支持一个简单结论：

> “国产独立游戏只要出海就会成功。”

它们更支持一个精确得多的判断：

> **市场接口（market interface）必须与产品的真实可寻址受众、传播语法、本地化成本和生产/运营能力相匹配。**

七个项目至少形成五种不同路径：

1. **GLOBAL-FIRST / 全球先验型**：My Time at Portia、Eastward；
2. **DUAL-MARKET FROM OUTSET / 从立项即双市场型**：Dyson Sphere Program；
3. **CHINA-FIRST, GLOBAL-LATER / 中文市场先完成验证，再补海外接口**：The Scroll of Taiwu、Amazing Cultivation Simulator；
4. **STEAM-DIRECT, CHINA-DOMINANT / 绕开传统国内渠道，但主要由中文 creator network 驱动**：Sultan's Game；
5. **GLOBAL-ACCESS BUT OPERATIONAL FAILURE / 全球入口充分，但产品/组织/服务续航失败**：Boundary。

因此，“看不见的墙”不是一堵统一的墙。

它更接近：

> **开发者是否把自己产品放进了正确的需求发现系统，并且是否知道当前数据究竟来自哪个市场。**

---

# 1. 审计矩阵

| 项目 | Steam/公开市场入口 | 验证发生在哪里 | 发行/平台外围 | 可见市场结构 | 当前解释 |
|---|---|---|---|---|---|
| My Time at Portia | SteamDB first seen 2017-06-23；2017 Kickstarter；2018 EA | 全球玩家 / Kickstarter / Steam | Team17 | 2019 公开口径：海外销量约64%，海外收入约80% | **最干净的 global-first 正例**：国内团队但从产品、众筹、发行到市场都按全球接口设计 |
| Dyson Sphere Program | SteamDB first seen 2020-07-06；2021-01 EA | 中外同步，自动化/建造品类全球受众 | Gamera Game | 2021 公开材料约三分之一海外；今日 Steam 英文评论约2.46万 vs 简中约4.89万 | **dual-market**：题材/玩法天然跨文化，发行商做笨重但真实的全球 outreach |
| Eastward | Chucklefish 2018-04全球宣布；SteamDB first seen 2018-11；2019 Nintendo Indie World；2020 IGF | 全球媒体/展会/主机平台 + 中国玩家 | Chucklefish / XD | Steam 评论简中约8.5k、英文约3.6k；主机销量地域未知 | **global interface from birth**：中国地理位置不决定市场接口 |
| The Scroll of Taiwu | SteamDB first seen 2018-03；2018-09 EA | 中文 Steam 市场先爆 | 自发行 | 首周约30万；2019 约200万；2026 超300万；2018 起已有海外 Discord/民间翻译需求 | **China-first success**：海外不是必要前提，但本地化成为长期机会成本 |
| Amazing Cultivation Simulator | SteamDB first seen 2018-10；2019-01 EA；2020-11 英文1.0 | 先在中文市场完成大规模验证 | GSQ + Gamera | 英文版前已在中国卖约70万；当前 Steam 简中评论约1.63万、英文约1.84k | **local proof → localization expansion**：文化解释成本真实存在，但不是“外国人不喜欢中国题材” |
| Sultan's Game | SteamDB first seen 2024-07；2024-09 Demo；2024-10 Next Fest；2025-03正式 | Steam Demo + 中文 creator / 二创网络为主 | 2P Games | Demo后不到2个月10万 wishlist；美/日愿望单已有明显数据；发行方称几乎无买量；2025-07破100万销量；Steam评论高度中文主导 | **绕开旧渠道 ≠ 海外先行**：Steam 本身就是全球接口，但实际增长可主要来自中文 creator network |
| Boundary | 2016 China Hero Project；SteamDB first seen 2020-07；2023-04 EA | 全球 FPS 受众 / PlayStation / Steam | China Hero Project + Huya + Skystone | 上线前公开材料称>50万 wishlist；首日>10万销量；2024停服 | **global access is not enough**：入口、曝光、首销都成功，retention / update / live ops / publisher relation 仍可把项目杀死 |

### 数据边界

- Steam review language 只能作为**受众语言结构 proxy**，不能直接等于销量地域。
- “海外销量占比”只有在开发者/发行商明确公开时才记为事实；媒体估算必须另标。
- Wishlist 只能证明兴趣，不证明长期 retention。
- 本轮不比较利润率，因为多数项目没有可审计完整成本。

---

# 2. My Time at Portia：最干净的“全球市场不是后补项”

## 时间线

- SteamDB first seen：2017-06-23。
- 2017-09 左右在 Kickstarter 发起海外众筹。
- 公开复盘称，Team17 正是在 Kickstarter 期间发现项目，并在约两周后达成合作。
- 2018 年初 Steam Early Access。
- EA 上线前公开 wishlist 约 7 万；首日销售约 1.4–1.5 万份。
- 2019 年团队公开口径：累计销量 86 万时，海外销量约 64%，海外收入约 80%。

Sources:
- SteamDB: https://steamdb.info/app/666140/info/
- GameRes / Pathea postmortem: https://www.gameres.com/850614.html
- GameRes / wishlist + Kickstarter + Team17: https://www.gameres.com/forum/t/857225
- Game Daily / Pathea global publishing history: https://news.yxrb.net/202209/19230849.html
- GamesBeat / Team17 partnership: https://gamesbeat.com/my-time-at-portia-marks-team17s-first-ever-partnership-with-a-chinese-developer/

## 关键机制

《波西亚时光》不是“中国游戏先做出来，再想办法出口”。

帕斯亚公开回顾显示，其更早的《星球探险家》本来就主要面向海外；创始人吴自非有海外行业经历，团队从很早就把：

- Kickstarter；
- Steam Early Access；
- 英语社区；
- 海外 publisher；
- 主播/KOL；
- 多语言；

作为正常生产外围，而不是“出海部门”。

Team17 的价值也不是神秘流量，而是明确的：

- 海外媒体关系；
- 平台关系；
- KOL / creator 关系；
- 主机发行经验。

## 对 AC-009 的意义

这是一个反例：

> **中国公司完全可以在 2010s 就不把国内渠道当默认世界。**

因此“看不见的墙”不是地理宿命；它部分取决于创始人世界模型和组织历史。

---

# 3. Dyson Sphere Program：全球 niche aggregation + 笨办法发行

## 时间线

- SteamDB first seen：2020-07-06。
- 2021-01-21 Early Access。
- 发售约一周销量 35 万，Steam 全球热销长期前列。
- 2021-09 发行商公开口径：全球销量已突破 150 万。

Sources:
- SteamDB: https://steamdb.info/app/1366540/info/
- GameRes研发采访: https://www.gameres.com/880221.html
- Gamera访谈: https://k.sina.cn/article_1887344341_707e96d5020014sty.html

## 市场接口

Youthcat 主创明确说过，全球发行是较早就做好的决定，并考虑中英文同步。

Gamera 的海外动作反而非常“低科技”：

- 给媒体逐封发邮件；
- 主动给目标玩家和社区发消息；
- 参加 TGS 线上活动；
- 建海外社区；
- 寻找自动化/建造类玩家；
- 与同类型游戏玩家圈互动。

发行负责人后来甚至概括为：前期就是一个玩家一个玩家积累。

Sources:
- GameRes marketing interview: https://www.gameres.com/880415.html
- Observers/Gamera interview: https://k.sina.cn/article_1887344341_707e96d5020014sty.html

## 海内外结构

公开二手行业材料曾给出约三分之一海外用户/销量口径；更稳妥的当前可见 proxy 是 Steam 评论：英文评论约 2.46 万，简中约 4.89 万，显示它确实拥有大规模英语用户，而不是纯中国爆款。

Sources:
- Steam English: https://store.steampowered.com/app/1366540/Dyson_Sphere_Program/?l=english
- Steam Chinese: https://store.steampowered.com/app/1366540/Dyson_Sphere_Program/?l=schinese

## 对 AC-009 的意义

它说明全球化不必等于：

> 大笔海外投放 + 国际大厂发行商。

更基础的动作是：

> **先确认全球存在一个已经会寻找这类产品的 niche，再把产品放到他们能看见的接口上。**

自动化/Factory 类玩家本来就跨国存在；《戴森球计划》没有先教育世界“为什么应该喜欢自动化游戏”。

---

# 4. Eastward：出生在上海，但市场接口从一开始就是全球

## 时间线

- Pixpil 2013 年成立，2015 年开始做 Eastward。
- Chucklefish 2018-04-26 正式宣布合作和游戏。
- 2018 EGX 英国提供试玩。
- SteamDB first seen：2018-11-05。
- 2019 Nintendo Indie World 宣布 Switch。
- 2020 获 IGF 视觉提名，并公开 demo / 社区活动。
- 2021 Nintendo Indie World 公布发售日，Steam + Switch 同期全球发售。

Sources:
- Chucklefish announcement: https://chucklefish.org/blog/introducing-eastward-by-pixpil/
- EGX 2018: https://chucklefish.org/blog/chucklefish-at-egx-2018/
- Nintendo Indie World 2019: https://chucklefish.org/blog/eastward-is-coming-to-nintendo-switch/
- Release date / Nintendo Indie World 2021: https://chucklefish.org/blog/all-aboard-for-the-eastward-release-date/
- SteamDB: https://steamdb.info/app/977880/screenshots/

## 市场接口

Chucklefish 在作品仍开发很早时就已经承担：

- 全球 announcement；
- 英语社区；
- 展会；
- Nintendo 平台关系；
- creator form；
- Discord / Reddit / Twitter；
- dev blogs；
- IGF 传播。

2021 AMA 里 Chucklefish community manager 直接把社区内容拆成：

- engagement；
- entertainment；
- education。

Source:
https://www.reddit.com/r/NintendoSwitch/comments/pyh9vo

## 当前受众结构

Steam 当前 purchaser reviews 大约：

- 简体中文 8.5k；
- 英文 3.6k；
- 另有繁中、葡语、西语、俄语等。

Steam 只是其中一个平台，不能由 review language 推出全平台销售地域；但至少说明：

> **全球发行并没有让它“脱离中国市场”，而是同时拥有两个大市场接口。**

Source:
https://store.steampowered.com/app/977880/Eastward/?l=english

## 对 AC-009 的意义

这是最直接的地理反证：

> **工作室在哪，不等于市场接口在哪。**

真正决定接口的是 publisher network、语言、平台、展会、creator 与社区布局。

---

# 5. The Scroll of Taiwu：中文市场足以证明产品，海外需求被本地化卡住

## 时间线

- SteamDB first seen：2018-03-30。
- 2018-09-20 Early Access。
- 上线首周公开采访称销量约 30 万。
- 2019 已有约 200 万销量报道。
- 2026 完整版阶段公开报道称累计销量超过 300 万。

Sources:
- SteamDB: https://steamdb.info/app/838350/history/
- 2018 producer interview: https://www.sohu.com/a/256802866_662623
- 2019 2m coverage: https://games.sina.com.cn/y/n/2019-10-11/icezuev1411495.shtml
- 2026 CNR 3m: https://www.cnr.cn/yn/jdt/20260618/t20260618_527665946.shtml

## “墙”是什么

2018 年发售时，游戏缺英语版本；制作人公开承认：

- 团队太小；
- 文本量巨大；
- 琴棋书画诗酒茶等传统文化概念很难高质量翻译。

与此同时，外国玩家已经在评论区主动求英文版。

到 2026 年，团队又公开表示：

- 从 2018 年就有官方 Discord；
- 群中有一万多名外国玩家；
- 玩家来自欧美、韩国、越南、菲律宾等；
- 长期存在玩家自主翻译；
- 非中文用户 wishlist 已达到几十万量级的内部调查口径。

Sources:
- 2018 interview: https://www.sohu.com/a/258522909_115479
- 2026 UCG interview: https://www.ucg.cn/newsinfo/10941699.html

## 对 AC-009 的意义

太吾不是“因为没出海所以失败”。恰恰相反，它证明：

> **本地市场足够大时，China-first 完全可以是理性策略。**

真正的问题是 optionality：

> 当海外已经主动证明需求存在时，团队有没有能力购买 localization / cultural translation，把 latent demand 转成第二增长曲线？

这比口号式“必须出海”更准确。

---

# 6. Amazing Cultivation Simulator：先中文卖 70 万，再尝试跨文化解释

## 时间线

- SteamDB first seen：2018-10-01。
- 2019-01 Early Access。
- 2020-11 正式版 / 英文版本上线。
- 海外英文版本上线前，公开报道称其已在中国市场卖出超过 70 万份。

Sources:
- SteamDB: https://steamdb.info/app/955900/info/
- Steam current page: https://store.steampowered.com/app/955900/Amazing_Cultivation_Simulator/?l=english

## 海外进入的实际难题

Gamera 发行负责人公开说，《修仙模拟器》海外发行的困难不是“外国人不接受中国文化”，而是：

- 五行；
- 八卦；
- 风水；
- 修仙语法；

这些都需要额外玩家教育。

他们并没有全部改写成西方熟悉词汇，而是保留概念，让愿意进入这个 niche 的玩家自己学习；后来确实出现海外玩家主动分享、解释这些概念。

Source:
https://k.sina.cn/article_1887344341_707e96d5020014sty.html

## 当前受众 proxy

Steam 当前可见 reviews：

- 简中约 16.3k；
- 英文约 1.84k；
- 繁中约 470。

说明英语 niche 确实存在且好评率高，但整体仍明显中文主导。

Source:
https://store.steampowered.com/app/955900/Amazing_Cultivation_Simulator/?l=english

## 对 AC-009 的意义

这里的“墙”不是渠道，而是：

> **semantic / cultural onboarding cost。**

所以 market interface audit 必须区分：

- 玩家根本看不到产品；
- 玩家看到了但看不懂；
- 玩家看懂了但不想要；
- 玩家想要，但本地化/支付/平台还没准备好。

这四种失败不能统称“海外难做”。

---

# 7. Sultan's Game：Steam-direct 可以高度中国化，也可以几乎不买量

## 时间线

- SteamDB first seen：2024-07-18。
- 2024-09 Demo。
- 2024-10 Steam Next Fest。
- 2024-11 初：官方宣布 wishlist 突破 10 万；采访称从 Demo 到 10 万不到两个月。
- 2024-12 摩点众筹。
- 2025-03-31 正式发售。
- 2025-07-10 官方宣布销量突破 100 万。

Sources:
- SteamDB: https://steamdb.info/app/3117820/history/
- 10w wishlist / interview: https://www.sohu.com/a/823126740_628730
- Next Fest 10w milestone: https://www.gamersky.com/news/202411/1838467.shtml
- crowdfunding: https://www.gamersky.com/news/202412/1862237.shtml
- 1m official Weibo: https://weibo.com/7836958764/PAqQThO40

## 市场接口

开发团队 2024 采访明确表示：

- 日本和美国 wishlist 数据也不错；
- 发行商在协助多语言本地化；
- 但大文本量使翻译成本很高。

Source:
https://www.sydneytoday.com/content-50004821794

后续媒体引用 2P Games 负责人说法称，项目“几乎没有买量”，并且没有走传统国内游戏渠道，而是 Steam 买断制；国内增长大量来自：

- Demo；
- Steam 新品节；
- Bilibili；
- 小红书；
- 抖音；
- 剧情讨论；
- 二创 / Cos / 玩家内容。

Sources:
- https://cj.sina.com.cn/articles/view/1750070171/684ff39b02001ck2a
- https://www.sohu.com/a/905972037_114778

## 对 AC-009 的意义

它非常重要，因为它证明：

> **“离开国内旧渠道”与“主要靠海外市场”完全不是同一个命题。**

Steam 是全球市场接口，但中文用户完全可以在 Steam + 国内 creator network 上形成巨大自然量。

因此真正要问的是：

> **谁拥有购买意愿，而不是服务器/平台在国内还是国外。**

---

# 8. Boundary：市场入口其实成功了，项目仍然死了

CASE-029 已经研究其生产与组织扩张。本轮只审计 market access。

## 时间线与入口

- 2016 即进入 PlayStation China Hero Project 第一批体系；
- 后续公开 PS4/PC、VR 等方向；
- 2019–2020 已持续接受海外媒体采访；
- SteamDB first seen：2020-07-02；
- 2021 Skystone 接手大中华区以外全球发行，Huya 负责 Greater China；
- 2023-04-13 Steam Early Access。

Sources:
- China Hero / studio interview: https://passthecontrolleruk.weebly.com/features/boundary-interview-with-surgical-scalpels
- International interview: https://www.capsulecomputers.com.au/2020/08/boundary-interview-with-technical-director-and-co-founder-frank-mingbo-li/
- SteamDB: https://steamdb.info/app/1364020/subs/
- Launch press release: https://www.gamespress.com/Boundary-Launches-via-Steam-on-April-13th

## 首发 proof 并不差

公开宣传材料称：

- Steam wishlist 超过 50 万；
- Early Access 上线 24 小时销量超过 10 万。

Source:
https://worthplaying.com/article/2023/4/14/news/136766-boundary-sells-100k-steam-early-access-copies-in-its-first-24-hours/

这意味着至少首发阶段：

> **发现性不是最主要瓶颈。**

## 后续失败

2024-06 Skystone 宣布 relinquish publishing rights，并称长期更新延迟、内容缺失；开发商随后公开反驳，并称存在运营权与收入争议。由于双方公开陈述冲突，本项目不得单方判责。

Source:
https://steamcommunity.com/app/1364020/allnews/

但无论责任归属如何，一个事实很清楚：

> **一个拥有全球 publisher、平台背书、50万级 wishlist 和首日10万销量的产品，仍然可以在一年多后失去服务能力。**

## 对 AC-009 的意义

Boundary 是本轮最重要的反压力：

> “看不见的墙”不能退化为“只要懂海外营销，一切问题都会解决”。

多人产品必须同时拥有：

- acquisition；
- retention；
- concurrency density；
- live ops；
- update throughput；
- publisher / revenue / server continuity。

市场接口只负责让人进门，不能替代房子本身。

---

# 9. 七个案例推出来的六条规则

## Rule 1 — Geography != Market Interface

中国工作室可以 global-first；外国 publisher 也可以服务中国用户；Steam 也可以承载高度中文主导的产品。

所以“国产游戏 / 出海游戏”这种二元词汇经常遮蔽真正的市场结构。

---

## Rule 2 — Market selection should happen before marketing optimization

先问：

> **谁会自然想玩？他们在哪？他们怎样发现新游戏？**

再问：

> 买量、媒体、主播、展会、publisher、Next Fest 中哪一个值得投入？

反过来先拿一个平台/发行商当标准答案，容易形成 AC-009 的 Distribution-Regime Misrecognition。

---

## Rule 3 — China-first can be rational

太吾、修仙模拟器、苏丹都说明：

> 中文 Steam 市场本身已经足够支持非常大的 premium PC 成功。

因此“必须海外先验证”同样是一种错误答案化。

真正问题是：

> 是否知道自己放弃海外时放弃了多少 optionality，以及未来补接口需要多少钱。

---

## Rule 4 — Global-first is easiest when the product grammar is already global

《波西亚时光》《戴森球计划》分别借用了：

- life sim / crafting；
- factory / automation；

这些已经存在全球玩家语法。

团队主要工作是让目标用户看到产品，而不是先教育全球玩家为什么这种 genre 值得存在。

---

## Rule 5 — Cultural difference is an onboarding-cost problem, not a binary demand problem

太吾、修仙模拟器都证明：

- 海外需求可以存在；
- 文化越深，本地化越不只是翻译；
- fan translation / Discord / guide 甚至可以成为 community production capacity。

所以以后记录海外失败时，必须区分：

`no demand` / `no visibility` / `no localization` / `high learning cost` / `bad packaging`。

---

## Rule 6 — Market Access != Sustainable Business

Boundary 证明：

> wishlist、首销、平台和 publisher 都可以很好，仍然不能替代 retention 和组织交付。

因此 market-interface audit 必须和：

- production audit；
- scope audit；
- organizational audit；
- live-service audit；

并列，而不是凌驾于它们之上。

---

# 10. 对“中国独立游戏为什么晚/菜”的更精确表述

这七个案例暂时不支持把问题简化成：

> 中国开发者技术差 / 不够努力 / 没钱。

更值得继续验证的是五类错配：

### A. Historical Interface Lag

中国开发者更晚获得 premium PC / global digital distribution 的稳定路径，因此 peer knowledge 晚一代形成。

### B. Capability Path Dependence

网游/F2P/mobile 训练出的强能力，不一定直接迁移到 premium small-team product selection。

### C. World-model Lag

市场基础设施已经变了，但开发者仍按旧渠道/买量/发行商中心模型规划产品。

### D. Product–Market Interface Mismatch

产品本来面向全球 niche，却只在本地接口上找用户；或者产品高度本地化，却把“全球化”当 KPI 强推。

### E. Selection / Product Failure

有时没有墙：产品本身的 hook、retention、scope、质量或组织就是不够好。

这五类必须分开。

---

# 11. 以后每个中国 PC 案例强制补的 Market-Interface 字段

以后新增或回填中国案例，建议至少记录：

1. Steam page / SteamDB first-seen date；
2. 首个中文与英文商店页时间；
3. demo / festival / public alpha 时间；
4. wishlist milestone 及其发生窗口；
5. publisher 介入时间：验证前还是验证后；
6. 国内 creator / 海外 creator 的首批传播节点；
7. 是否买量，若有则市场与规模；
8. Kickstarter / crowdfunding / grant / platform showcase；
9. launch sales 与首月 retention；
10. sales region / language proxy；
11. localization 首发还是后补；
12. 玩家教育成本：genre grammar / cultural grammar；
13. 中国平台和海外平台是否出现 cross-border feedback loop；
14. 团队事前认为“玩家在哪”，事后真实用户又在哪；
15. 如果失败：是 no visibility、no demand、no retention、no localization 还是 organization failure。

---

# 12. 下一轮值得补的对象

为了避免这七个案例变成选择性样本，下一轮优先补：

- `Chinese Online Game`：极端 China-specific 文化模拟，验证“本地语法就是产品核心”的边界；
- `Outpost: Infinity Siege`：全球视觉包装、复杂 feature stack 与首发口碑/后续修复；
- `Volcano Princess`：小团队、美术/角色二创、东亚与海外受众传播；
- `Party Animals`：中国团队、全球 creator-first、多人与平台接口；但必须单列资本/所有权，不冒充 core indie；
- `F.I.S.T.: Forged In Shadow Torch`：China Hero / console/global publisher 路径；
- `The Rewinder` / `Firework`：中式题材的小体量全球化边界；
- `Sandrock`：用《波西亚时光》积累的海外用户直接降低续作 market-access 成本。

这些对象能继续回答：

> **当中国开发者真正知道世界有多个市场接口以后，他们是否开始形成可复用的全球发行能力资本？**

---

## Preliminary Verdict

> **中国独立游戏的“看不见的墙”不是简单的网络墙、渠道墙或文化墙，而是市场世界模型与产品真实需求网络之间的错位。最成熟的团队不是“更会营销”，而是更早知道自己的玩家是谁、在哪、需要什么证据才值得继续投入。**

同样重要的反命题是：

> **全球市场不是万能逃生舱。市场入口只能解决发现性；产品选择、范围、质量、retention、组织交付和持续运营仍然必须分别成立。**
