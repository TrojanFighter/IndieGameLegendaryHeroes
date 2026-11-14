# Lane C 新稿道交付｜Spiderweb / Jeff Vogel Profile 候选（2026-11-15）

> **Status: AUTHOR_REVIEW_PENDING — 新稿道，无旧 reader 稿；无真实读者盲测（NOT TESTED）。**
>
> 本文件是 [EDITORIAL-GATE §0.5 新稿写作入口](EDITORIAL-GATE.md#05-新稿写作入口预防模板化) 的候选交付：从 mature Case 生成一篇人物 Profile 候选。它**不覆盖任何现有正文文件**，不创建 canonical facts；`cases/`、`evidence/`、`claims/`、`schemas/`、lint 与姊妹篇 canonical 语料零改动。

## 1. Baseline 与范围

| 项 | 值 |
| --- | --- |
| 目标 Case | `CASE-058 Spiderweb Software / Jeff Vogel` |
| 目标人物 | Jeff Vogel / Spiderweb Software：Exile / Avernum / Geneforge 等低成本 CRPG 语法 → Queen's Wish 转型实验 |
| Baseline commit | `8e46c1f8a0d928efcb87a16a8e3d564b9a368676`（main HEAD，2026-11-15 clone） |
| Baseline blob SHA | Case `e51ea3259343f425ea2e9dc3d049660140b357f4`；Evidence Ledger `f6d8cbff734e43a51bc2c737848905bcf98352c0` |
| 交付路径 | 本文件；不写入 `book/profiles/`，不改 README/索引 |
| Authority | [CASE-058](../cases/CASE-058-spiderweb-fit-lock-in.md)、[Evidence Ledger](../evidence/CASE-058-spiderweb-fit-lock-in-source-ledger.md)（E001–E012）、[C015 Capability-Shaped Project Formation](../claims/C015-capability-shaped-project-formation.md) |
| 选题理由 | 偶数 ISO 周新稿道；CASE-058 为 `evidence_strength: HIGH`、`narrative_value: CRITICAL`、Creator Life audit `SUBSTANTIAL`，且尚无 `book/profiles/` reader 稿。它提供了 Zachtronics 之外第二个可观察的长期 `FIT-LOCK-IN` 锚点，人物线清楚、直接证据多、且有 2026 年本人回顾作为结果边界。 |
| Open PR collision check | 已查 open PRs：#351 Gunpoint 改写、#336 FTL、#333 Kenshi、#314/#313 Zachtronics 等均不覆盖 Spiderweb/Jeff Vogel；本 PR 只新增本交付文档。 |

## 2. Fact Lock（动笔前事实边界）

- **叙述对象**：单人/极小工作室纵向传记，主线是 Jeff Vogel 与 Spiderweb 如何把一套低成本 CRPG 生产语法做成长期生存系统，又在 Queen's Wish 上付出转型成本。
- **关键人名/身份**：Jeff Vogel 是 Spiderweb Software 的长期创作者/经营者；妻子参与 mom-and-pop business、公开提到孩子，但更细 household finance `UNKNOWN`（CASE-058 §14, E002/E009）。
- **时间口径**：Case 覆盖 1994–2026；Evidence Ledger 未单列公司创建年份的一手来源。正文采用“1990 年代中期起步 / 三十多年”的低精度表述，不把 1994 当作已核精确 founding year；若后续要精确到年，交 Lane B 补 source。
- **金额口径**：E009 的约 20 万美元 net-sales target 与约 6 万美元 business expenses/insurance 是 Vogel 为 Queen's Wish 举的 illustrative business arithmetic，不是 audited P&L；正文必须保留“他举例算账”的口径，不写成实际收入/利润。
- **团队/家属/外包**：Spiderweb 是极小团队/自有小公司、自发行取向；具体 contributor totals、合同工、外包、equity、decision rights `UNKNOWN`。不得写成“一个人完成全部”。
- **否定限定词**：Queen's Wish underperformance 不能单因“改变”解释；Vogel 自己也列 marketer failure、visual execution、indie glut 等共同因素（E012）。不得把 QW1 后来找到受众写成 QW2 必然失败，也不得把 repeat 直接写成停滞。
- **回忆时点**：2008/2009/2010/2012 为同期或近同期访谈/博客；2018–2019 为转型前后自述；2021 postmortem 是第一作回顾；2026 retrospective 是多年后总结。后来的诊断不得倒写成 2018 当时已预知 QW2 销量。
- **UNKNOWN / H / Signal**：精确年收入、QW1/QW2 全平台 units、marketing spend、household balance sheet、outside-employment fallback、不同 genre 反事实表现均 `UNKNOWN`。本稿不使用这些未知数字。
- **史实问题处理**：公司创建年份精度、Queen's Wish 全平台销量、转型成本中 technology/audience/presentation 的相对份额，均保留为 `VERIFY_IN_LANE_B` 或不写；不在 Lane C 猜。
- **可学清单边界**：只保留“fit 会复利、转型要同时支付 production reset + audience replacement cost”的机制判断；不把 1990s shareware / Mac niche / early direct-sales 写成 2026 通则。

## 3. Narrative Packet

- **叙述对象与主问题**：一位长期经营小型 CRPG 工作室的人，怎样在“同一套生产语法越来越便宜”的同时，被这套语法抬高转向新产品的成本？读者追问：当你已经很会做一类游戏，什么才算真正改变它？
- **人物、时代与处境**：Vogel 的优势不是单次灵感，而是十几年重复生产形成的 engine/assets/workflow/audience/back catalog；约束是极小团队、低预算、家庭生计与“一次 flop 可能关门”的风险。1990s shareware/direct-sales、2000s portal/自营网站、2010s Steam/GOG、2020s Kickstarter/Steam demo 是不同 regime，不能混成今天的打法。
- **处境约束**：他能复用旧技术和受众，也被旧受众惩罚；他能做低成本 text-heavy RPG，却不愿意用高成本美术正面竞争 AAA；他知道 niche 稳定，也知道 creator fatigue 与平台变化会让旧 grammar 逐渐失效。
- **决策节点**：长期复用 engine/assets；把 audience expectation 当成 production constraint；2018 把 Queen's Wish 定义为 new world/new engine/new system/new presentation 的转型实验；2026 在 QW2 变差后选择 remasters 稳定业务、免费 epilogue 收尾，而不是无限硬撑第三作。
- **主导疑问**：成功的 fit 如何既是资产又是负债？
- **叙述位置**：传记叙事 + 制度/市场解释；以时间、动作、反馈和本人后来的判断推进，不先宣判理论。
- **文风边界**：不补办公室场景、家庭争吵、成员心理、未核对对白；不把 Vogel 的幽默博客标题当成性格证明；不把作者分析安到他头上。

## 4. Structural Cut / 新稿结构决策

新稿无旧段落可标 N/A/D/R；以下是写作前的结构剪辑清单：

| 结构单元 | 来源材料 | 处置 |
| --- | --- | --- |
| 开场 | E003 2009 blog + E002 survival constraint | 保留：用“改变会被要求改回去”的具体约束开场，不用“神话—反转”起手 |
| 语法形成 | CASE-058 §3–§5, E001/E004/E005/E006/E011 | 保留：说明复用是 survival economics，不是懒 |
| 转型实验 | E007/E008/E009 | 保留：Queen's Wish 的 new engine/system、20 个月 vs 12–14 个月、illustrative budget |
| 结果与反例 | E010/E012 | 保留：QW1 后期找到受众、QW2 约一半 Steam sales、其他共同原因、remasters/epilogue |
| 机制判断 | CASE-058 §10–§15, C015 | 合并：只把 fit compounding / switching cost 压缩成一节，不重复全书 thesis |
| 研究边界 | Case §14/§16–§18, Ledger unknowns | 下沉到文末“研究与证据入口”，正文只在影响理解处留一句边界 |
| 删除项 | 无旧稿；主动删除“Spiderweb 三十年做差不多的游戏只是懒”“创新失败”“家人让他保守”等诱惑性简化 | 不写入正文 |

### 来源阅读状态（§0.6）

| 材料 | 本轮状态 | 说明 |
| --- | --- | --- |
| `cases/CASE-058-spiderweb-fit-lock-in.md` | FULL_READ | 全文读取，提供人物线、机制、反例与 UNKNOWN 边界。 |
| `evidence/CASE-058-spiderweb-fit-lock-in-source-ledger.md` | FULL_READ | E001–E012 全部条目全文读取；本候选只把 Ledger 作为 canonical 依据，不新增事实。 |
| `claims/C015-capability-shaped-project-formation.md` | FULL_READ | 全文读取，用于确认 C015 对 CASE-058 的支持边界与反方压力。 |
| E001–E012 原始 URL | NOT_FETCHED_FULL_TEXT | 本环境网络受限，直接抓取一手页面失败；未把搜索摘要或互相转载当作全文阅读。 |
| 作品官方/商店入口 | SEARCH_VERIFIED | Queen's Wish、Geneforge、Avernum、Exile 的官网/Steam 入口已用公开搜索核对身份；未逐页全文抓取，不写动态价格或评测量。 |

## 5. 候选 Profile 正文

---

# Jeff Vogel：一套被验证过的生产语法，怎样变成转型的账单

© 2026 洪荒行者。All Rights Reserved.

2009 年，Jeff Vogel 在博客里写了一篇题为[《Why Nobody Should Ever Change Anything, Ever》](https://jeff-vogel.blogspot.com/2009/04/why-nobody-should-ever-change-anything.html)的文章。标题故意像玩笑，内容却不是：他经营 Spiderweb Software 时反复听到同一种批评——你是不是又在做同一个游戏？他也承认，每次改动都会有人要求改回去。

这句话后来很容易被读成“老玩家保守”。但放在 Spiderweb 的处境里，它更像一份生产约束。Vogel 从 1990 年代中期开始做极小成本的回合制、文本密集、开放式 fantasy RPG：早期是 [Exile](https://www.spiderwebsoftware.com/exile/winexile.html)（官网 Windows 历史版入口）、[Avernum 系列](https://spiderwebsoftware.com/avernum/)（官网系列入口，含后续重制版）和 [Geneforge 1](https://store.steampowered.com/app/200960/Geneforge_1/)（Steam 现行入口）这类作品，后续作品也沿着同一套低成本 CRPG 语法继续积累。公司规模很小，市场也不是大众主流；它能活下来，靠的不是每次都冒险换一种游戏，而是把同一套玩家会认、自己也做得动的东西反复做准。

## 复用不是偷懒，是把最贵的资产留下来

Vogel 很早就把这件事说成生存问题。2008 年他在 [GameBanshee 访谈](https://www.gamebanshee.com/interviews/28315-spiderweb-software-interview/all-pages.html)谈资产复用时，核心理由是时间：小团队没有预算每作重做全部美术、动画和内容，他只替换最差的那一部分，把精力留给写作、系统和玩法。2010 年他在[自己的博客](https://jeff-vogel.blogspot.com/2010/04/how-i-saved-gaming-industry-overnight.html)更直白地承认，核心技术十年几乎没变，而 audience 和 profit 仍在增长；复用不是没有代价，而是用可预测的低成本换取持续出货。

这套语法后来被压成几个可观察的条件：熟悉的 engine 和 code、能反复使用的 art/asset library、低成本的文本叙事、回合制战术战斗、稳定的 niche audience，以及 back catalog 带来的现金流。到 2018 年，他在 [GeekWire 访谈](https://www.geekwire.com/2018/im-still-humble-toymaker-chat-indie-rpg-developer-jeff-vogel-seattles-spiderweb-software/)里把它概括为“一台引擎、许多游戏”：写一套 engine，然后在里面持续做多款 RPG。

这不是没有选择的宿命。2008–2009 年的访谈里（[GameBanshee](https://www.gamebanshee.com/interviews/28315-spiderweb-software-interview/all-pages.html) / [RPG Codex](https://rpgcodex.net/article.php?id=187)），他说明自己每年都会想到别的游戏类型，但也清楚地说，一次真正的 flop 可能让一家小公司关门；他已经有一个自己很擅长服务的 niche。选下一作时要考虑的不只是市场，还有家：这家公司由他与妻子共同经营，他也公开提到孩子；更细的家庭收支仍没有公开账本。换句话说，重复不是因为不会变，而是因为已经验证过的 fit 改变了风险函数：留下旧路，失败概率下降；离开旧路，可能同时失去技术复用、资产复用、受众预期、制作估算和渠道可信度。

## Queen's Wish：一次有意的生产语法重置

2018 年，Vogel 做了一个相对少见的决定：在 Spiderweb 二十五年里，他把 [Queen's Wish: The Conqueror](https://store.steampowered.com/app/1058130/Queens_Wish_The_Conqueror/) 称为第五个全新 game world，并同时更换 engine、system、story/world、graphics approach，还第一次用 Kickstarter。这不是随手换皮，而是一次刻意的技术与产品重置。

重置的成本很快显形。2019 年他在 [GamesBeat 访谈](https://gamesbeat.com/queens-wish-the-conqueror-interview-jeff-vogel-wants-you-to-be-a-fantasy-ceo/)谈到，Queen's Wish 第一作用了约二十个月，而他平常一作更接近十二到十四个月；新 engine、interface、graphics 和 programming 都要重新学。那篇[后来被 Game Developer 转载的文章](https://www.gamedeveloper.com/design/i-am-the-cheapest-bastard-in-indie-games)甚至给这笔账算了一个很小的例子：约二十万美元 net-sales target、约六万美元业务开支与保险。那只是他举例说明小公司现金流如何约束项目，不是审计过的利润表；但它足以说明，Queen's Wish 不是一次可以无限透支的“艺术实验”。

这里的关键不是“新引擎更先进”，而是旧资产被部分失效了。熟悉的 engine 曾经让每个细节都更便宜；新 engine 让每个细节都重新计价。Vogel 当时相信，如果后面能做 Queen's Wish 2/3，第二作会轻松很多——因为新的技术资本已经付过一次。这正是 switching cost 的另一面：第一笔重置成本会沉淀成下一次的资产，只是这一次能不能活到那时，取决于市场是否给它足够的新受众。

## 第一作找到受众，第二作没有替换够多流失的玩家

Queen's Wish 第一作并不是立刻失败。2021 年的 [postmortem](https://bottomfeeder.substack.com/p/queens-wish-the-conqueror-post-mortem)里，Vogel 说它改动太多，很多旧玩家觉得突兀，首发反馈和销量一开始都不理想；但后来 review 转好，长尾仍强，最终找到了自己的 audience。这个结果很重要：一次大改并不必然死，可能只是迟到地被理解。

到 2026 年，他在 [Portmortem](https://bottomfeeder.substack.com/p/queens-wish-a-portmortem-of-mixed)里回看整个 Queen's Wish 系列时，结论变得更冷。第一作卖得不错；第二作销量明显更差，他给出的当前口径是 Steam 销量约为第一作的一半，并且低于 Spiderweb 历史水平。完整第三作因此不再 financially feasible；公司先用 remasters 把业务拉回稳定，最后用一个更小的免费 epilogue 给故事收尾。

他对这件事的解释几乎就是机制本身：新设计必须变化才能保持新鲜，但改变会丢掉旧玩家；如果新方向不能找到足够的新玩家补回来，系列就会同时支付 production reset 和 audience replacement 两份成本。Queen's Wish 改得很多，一部分旧玩家离开，而替代者没有足够多。

但这不是单一原因的失败公告。他自己还列出了营销合作或推广执行失利、视觉呈现不够统一、indie glut 让新用户更难获得等因素；第一作也有不错的长尾。所以更准确的说法是：转型没有赚回足够的新 audience，而不是“改变本身”自动等于失败。

## 这套语法真正留下的，不是“别变”，而是切换成本的算法

Spiderweb 的故事不能被简化成“保守所以成功”或“创新所以失败”。它展示的是另一件事：长期 fit 会把能力、工具、资产、受众、品牌和 back catalog 变成资本；这些资本降低了继续做同类项目的成本，也提高了换一种玩法时要重新支付的总成本。

这和 Zach Barth / Zachtronics 的结局有相似处，也有重要差别。两者都不是“不会做别的”，而是多年成功把产品选择从创意判断变成资产配置判断；但 Spiderweb 没有像 Zachtronics 那样关门，而是用 remasters 和较小的 epilogue 给系列降压。换句话说，这种长期锁定不只会锁住创作者，也会锁住公司下一步必须从哪里省钱。

对今天的读者，能保留的是机制，不是 1990s shareware 或 Mac niche 的具体打法：重复要按资产记账；转型要同时估算生产重置和受众替换；稳定的受众既是护城河也是约束；而“还在做同一类游戏”在被市场长期验证时，可能不是停滞，而是一种有代价的 exploitation strategy。Vogel 到 2026 年也没有离开游戏，他只是先让公司回到能承受下一次选择的位置。

---

## 研究与证据入口

- Case / Evidence / Claim：[CASE-058](../cases/CASE-058-spiderweb-fit-lock-in.md) · [Evidence Ledger](../evidence/CASE-058-spiderweb-fit-lock-in-source-ledger.md) · [C015](../claims/C015-capability-shaped-project-formation.md)
- 关键来源入口（书目信息与原文链接；阅读状态见 §4A）：
  - E001 — GameBanshee / Jeff Vogel, “Spiderweb Software Interview”, 2008-01-22, [原文](https://www.gamebanshee.com/interviews/28315-spiderweb-software-interview/all-pages.html)
  - E002 — RPG Codex / Jeff Vogel, “Interview with Jeff Vogel of Spiderweb Software”, 2009-01-05, [原文](https://rpgcodex.net/article.php?id=187)
  - E003 — Jeff Vogel / The Bottom Feeder, “Why Nobody Should Ever Change Anything, Ever”, 2009-04-27, [原文](https://jeff-vogel.blogspot.com/2009/04/why-nobody-should-ever-change-anything.html)
  - E004 — Jeff Vogel / The Bottom Feeder, “How I Saved the Gaming Industry Overnight By Being Awesome”, 2010-04-21, [原文](https://jeff-vogel.blogspot.com/2010/04/how-i-saved-gaming-industry-overnight.html)
  - E005 — Engadget / Jeff Vogel, “The enduring web of indie veteran Spiderweb Software”, 2012-02-03, [原文](https://www.engadget.com/2012-02-03-the-enduring-web-of-indie-veteran-spiderweb-software.html)
  - E006 — GeekWire / Jeff Vogel, “‘I’m still a humble toymaker’: A chat with veteran indie RPG developer Jeff Vogel”, 2018-02-22, [原文](https://www.geekwire.com/2018/im-still-humble-toymaker-chat-indie-rpg-developer-jeff-vogel-seattles-spiderweb-software/)
  - E007 — Jeff Vogel / The Bottom Feeder, “We Did Our First Kickstarter! And It Worked!”, 2018-05-31, [原文](https://jeff-vogel.blogspot.com/2018/05/we-did-our-first-kickstarter-and-it.html)
  - E008 — GamesBeat / Jeff Vogel, “Queen's Wish: The Conqueror interview — Jeff Vogel wants you to be a fantasy CEO”, 2019-09-09, [原文](https://gamesbeat.com/queens-wish-the-conqueror-interview-jeff-vogel-wants-you-to-be-a-fantasy-ceo/)
  - E009 — Jeff Vogel / Game Developer, “I Am the Cheapest Bastard In Indie Games”, 2019-09-04, [原文](https://www.gamedeveloper.com/design/i-am-the-cheapest-bastard-in-indie-games)
  - E010 — Jeff Vogel / The Bottom Feeder, “Queen's Wish: The Conqueror Post-Mortem”, 2021-08-23, [原文](https://bottomfeeder.substack.com/p/queens-wish-the-conqueror-post-mortem)
  - E011 — RPGWatch / Jeff Vogel, “Jeff Vogel Interview”, 2022-08-31, [原文](https://rpgwatch.com/articles/jeff-vogel-interview-525.html)
  - E012 — Jeff Vogel / The Bottom Feeder, “Queen's Wish: A Portmortem Of Mixed Success”, 2026-03-11, [原文](https://bottomfeeder.substack.com/p/queens-wish-a-portmortem-of-mixed)
- 作品入口（版本已标明，不写动态售价/评测量）：
  - [Spiderweb Software 官网](https://www.spiderwebsoftware.com/) · [产品页](https://spiderwebsoftware.com/products.html)
  - Exile: [官网 Windows 历史版入口](https://www.spiderwebsoftware.com/exile/winexile.html)
  - Avernum: [官网系列入口](https://spiderwebsoftware.com/avernum/)（含后续重制版；历史原版与 remake 边界以 Case 时间线为准）
  - Geneforge 1: [Steam 现行入口](https://store.steampowered.com/app/200960/Geneforge_1/)
  - Queen's Wish: The Conqueror: [Steam 现行入口](https://store.steampowered.com/app/1058130/Queens_Wish_The_Conqueror/)
- 仍需 Lane B / 后续核验：公司创建年份精确来源、Queen's Wish 全平台销量与 marketing spend、转型成本中技术/受众/呈现的相对份额、完整 contributor 与 household finance。
- 时效性：

| 历史做法 / 机制 | 观察年份 | 2026 状态 | 今天值得保留的部分 |
|---|---:|---|---|
| 1990s shareware / direct-sales 与早期 niche 平台条件 | 1990s–2010s | `HISTORICAL / CONDITIONAL` | 小团队要把现金流、资产复用和受众预期放在同一张账上算；具体渠道不可照抄 |
| engine/assets reuse、稳定 niche grammar、back catalog 现金流 | 2008–2022 | `DURABLE` | 重复生产会复利，但必须持续回答“这次复用到底替换了什么成本” |
| Queen's Wish transition / switching-cost 判断 | 2018–2026 | `DURABLE`（机制） / `CONDITIONAL / UNKNOWN`（当时平台打法） | 转型要同时估算生产重置与受众替换；Kickstarter/Steam 的具体规则与曝光必须重核 |

  Queen's Wish 的销量结果只按 2026-03 本人回顾记录，不外推为所有 veteran niche studio 的规律。

## 6. 三遍编辑记录（新稿道）

- **Delete**：初稿中曾把“Spiderweb 三十年做差不多的游戏”直接归因为懒、把 Queen's Wish 简化为“创新失败”、把家庭责任写成保守人格；均删除或改写为有边界的机制判断。没有把研究免责声明在正文重复堆叠。
- **Restore Person**：把 Vogel 放回动作位：他在 2008–2010 年解释复用是生存经济学；2018 年主动选择 new engine/system；2019 年承认新技术要重新学习；2021 年复盘 QW1 后期找到受众；2026 年用 remasters/epilogue 收束。没有补心理、对白或现场细节。
- **Rhythm**：开场用 2009 年博客标题这一具体约束进入；中段按“复用—重置—结果—机制”推进；结尾回到公司选择而非全书总结。短句只用于“这不是没有选择的宿命”“不是单一原因的失败公告”等真正需要停顿的地方。

## 7. Fidelity Readback

| 项 | 结果 | 说明 |
| --- | --- | --- |
| Actor / credit | PRESERVED | Vogel/Spiderweb 为核心；未写成 solo 完成全部，未隐去妻子/孩子/小公司经营背景；contributor totals 保持 UNKNOWN。 |
| Chronology / knowledge at the time | PRESERVED | 2008–2010 复用论述、2018 转型决定、2019 成本自述、2021 QW1 postmortem、2026 系列回顾分层呈现；未把 2026 诊断倒写成 2018 预知。 |
| Negation / modality | PRESERVED | “不是懒/不是单一原因/不必然失败/不等于所有 veteran studio”均保留；QW2 “约一半 Steam sales”保留 creator-reported 与平台口径。 |
| Causation / alternative | PRESERVED | QW2 underperformance 同时保留营销/推广执行、视觉呈现、indie glut、QW1 长尾等反方/共同原因；未把 repeat 写成停滞，也未把 fit 写成商业成功保证。 |
| Numbers / denominators | PRESERVED | 12–14 个月 vs 约 20 个月、约 20 万 net-sales target/约 6 万 expenses 均标明为 Vogel 举例或生产周期口径；未把 illustrative arithmetic 写成 audited P&L。 |
| Evidence boundary | PRESERVED | UNKNOWN 项集中在文末；公司创建年份用低精度表述并说明 Ledger 缺口；无 H/Signal 写成事实。 |
| Historical regime | PRESERVED | shareware/direct-sales/Steam/GOG/Kickstarter 被写成不同时期 regime；未把 1990s Mac niche 或当年 direct-sales 当成 2026 通则。 |
| Quote / intellectual property | PRESERVED | 只使用来源标题《Why Nobody Should Ever Change Anything, Ever》作为可核标题；未编造对白、心理或长篇引语。 |
| 来源入口 / §0.6 | NEEDS_VERIFY | Case/Ledger/C015 全文读取；E001–E012 原文全文因网络受限未取得，未把搜索摘要当已核引文；作品官方/Steam 入口经搜索核对身份并标明版本边界。 |
| 双向回读 | NEEDS_VERIFY | 公司创建年份精确性、QW 全平台销量、转型成本分解仍需 Lane B；正文已避开精确断言。无 REGRESSION。 |

## 8. A/B 与编辑判断

- **A/B：NOT TESTED。** 本案此前没有 reader profile 旧稿，不存在可匿名对照的正式版本；本轮也未组织真实读者盲测，不伪称已有读者反馈。
- 编辑内测判断：候选稿的优点是人物动作链清楚（复用→主动重置→市场结果→收束），理论只在最后一节压缩出现；风险是“fit/lock-in/switching cost”术语仍偏研究化，因此正文先用“同一套生产语法”“换一种玩法要重新支付的成本”等人话解释，再在研究入口保留 C015/Temporal Validity。另如实记录：本环境未能抓取 E001–E012 原文全文，来源阅读状态与入口已补齐，但作者验收时可决定是否要求 Lane B/补读原文后再晋级。建议状态：`AUTHOR_REVIEW_PENDING`。
- 六维比较（编辑自评，非盲测）：人物具体性较高；连贯度依赖 2009→2018→2021→2026 的时间链；作者观点保留为“机制判断”而非人物原话；节奏中等偏稳；继续阅读意愿取决于读者是否接受慢热纵向传记；历史忠实性无已知倒退，遗留 NEEDS_VERIFY 已列明。

## 9. 交付合同核对

1. **修改范围与 baseline**：仅新增本文件；baseline commit/blob SHA 见 §1。
2. **结构调整**：新稿无旧稿可剪；结构决策见 §4，三遍编辑见 §6。
3. **Fidelity Readback**：见 §7，无 REGRESSION；NEEDS_VERIFY 项集中列出（含 §0.6 原文全文未取得的来源缺口）。
4. **A/B**：无旧稿、无真实盲测，明示 NOT TESTED；编辑判断见 §8。
5. **canonical zero-change**：`cases/`、`evidence/`、`claims/`、`schemas/`、lint、姊妹篇 canonical 语料均未改；本 PR 不新增历史事实。
6. **恢复路径**：本文件为新增候选；不进入 `book/profiles/`，原 Case/Evidence/Profile 均可由 main 原样恢复。作者验收前不合并。

**下一步建议**：作者验收后，若认可新稿道格式，可将候选正文单独晋级为 `book/profiles/spiderweb-jeff-vogel.md` 并同步 `book/profiles/README.md` / `book/README.md`；在此之前保持 `AUTHOR_REVIEW_PENDING`。
