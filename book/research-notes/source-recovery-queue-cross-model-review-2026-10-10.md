# 跨模型审查：原始资料补取队列（2026-10-10）

© 2026 洪荒行者。All Rights Reserved.

- Scope: 把本轮审查里"必须回到原文才能解决"的证据缺口，写成一份可直接投喂给对话侧模型的任务队列
- Status: OPEN TASK QUEUE / NOT CANONICAL EVIDENCE
- Companion: [跨模型协作与书稿质量整顿](cross-model-collaboration-and-prose-review-2026-10-10.md)（PR #320）
- Excludes: 私人项目材料；本文件不下结论、不提升任何 Case / Claim 状态

---

## 这份文件是干什么的

它只问一件事：**把证据层缺的那句话、那个日期、那个原句带回来。**

它不要求、也不接受在投喂过程中产生解释、推论或状态升级。带回的内容按 [`schemas/evidence-material-refresh.md`](../../schemas/evidence-material-refresh.md) 的交接合同落库，由 Lane B 决定它支持什么。

## 交付格式（每条都按这个回）

```text
[Case]      CASE-0XX
[来源]      URL / 平台 / 发布日期 / 作者或机构
[定位符]    可复现的定位：timecode / 页码 / appid / release tag / commit（不是「某次采访」）
[可达性]    direct | blocked | shell | gone | api
[逐字引语]  短引语；英文原文照抄，非英文保留原文并可附译文
[事实节点]  这条引语支撑哪些事实
[边界]      不能证明什么；口径、时点、回忆偏差
[仍缺]      还差哪一条具体证据
```

## 三条硬约束

1. **不交摘要，交原话。** 摘要压掉的正是因果起点、当事人的话和口径边界——这三类下游无论如何补不出来。
2. **标注可达性。** 200 不等于拿到内容：JS 渲染页会返回 200 + 空壳。
3. **取不到就说取不到。** 写 `NOT REACHABLE` 并说明，不要用摘要冒充引语，也不要把「取不到」当成「不存在」。

---

## 队列

### R1 — Limit Theory：源码公开的实际日期与范围 ★最高优先

- **为什么**：`book/profiles/josh-parnell-limit-theory.md` 第 135–153 行有一整节讲「2022 年他兑现了另一种承诺」，但 `evidence/CASE-054-limit-theory-source-ledger.md` 里**没有任何 2022 年记录**（`rg "2022"` 在两个版本中均零命中）；E005 只写"repositories exist"，`Published: UNKNOWN`。该断言已扩散到 `book/profiles/README.md` 第 35 行与 `book/chapters/03-failure-only-matters-if-something-survives.md` 第 105 行。`book/research-notes/editorial-fidelity-pilot-001.md` 已把它登记为 `NEEDS_VERIFY`，但读者层仍是肯定句。
- **来源**：`github.com/JoshParnell/ltheory`，以及 `github.com/JoshParnell/ltheory-old`
- **定位符**：首个 release tag、首次公开 commit 的日期；仓库 README 中关于「这段代码是什么/不是什么」的原句
- **可达性**：direct
- **要带回**：公开日期（年-月）；公开范围（全部代码？只引擎？）；发布时作者自己的说法原句
- **回填到**：`CASE-054` ledger 新 E 记录（或补进 E005 的 `Published`），再决定 profile 那一节是保留、改措辞还是删除

### R2 — Gunpoint：开发到底从哪一年开始

- **为什么**：`book/profiles/gunpoint.md` 第 131 行的时效性卡写 `Observed: c. 2009–2013`，但 ledger 最早记录是 `2010-10-25`，而同一份 ledger 的 STRONGLY SUPPORTED 写 "about three years"。文内第 45 行小标题是「2010 年，他重新看了一遍 roadmap」。editorial 分支已把这条记成 year drift note，但**未解决**。
- **来源**：`pentadact.com` 的 devlog 首篇；GDC Europe 2013 演讲《How Reviewing Games for Nine Years Helped in Designing Gunpoint》视频；IGF 2012 的报名／入围材料
- **定位符**：任何一处**有日期**的「第一次做出可玩原型」记录
- **可达性**：`pentadact.wordpress.com` **403**；`pentadact.com` 现为作者当前站点，不再提供 2012 年那份 resume
- **要带回**：原型的日期，或明确结论"没有任何公开材料支持 2009"
- **回填到**：CASE-007 ledger 新增 E 记录 → 然后 profile 要么保留 2009 要么改成 `c. 2010–2013`。**先证据后正文。**

### R3 — The Amp Hour #332：timecode 与团队规模原句

- **为什么**：`evidence/CASE-051-zachtronics-source-ledger.md` 的 E011 `Locator` 只写 "around 'we shut down the studio'"，**没有 timecode**，不符合 AGENTS.md §10 对音视频来源的要求。另外转录里 Barth 说过 `currently we're four and we've peaked as hig…`，涉及团队规模口径（AGENTS.md §6 要求区分核心/峰值/累计）。
- **来源**：`theamphour.com/332`（官网转录已是**发言归属**文本，我已直连核对过三条引语，事实链成立）；音频本身尚未独立听
- **定位符**：音频 timecode（`we shut down the studio` / `worked there for 10 months` / `tired of running the business`）；含 `currently we're four` 那段的完整句
- **可达性**：官网转录 direct；音频需下载后自行核对
- **要带回**：三处 timecode + team-size 原句 + 说明该处是 Barth 本人还是主持人的推测
- **回填到**：E011（或合并后的 E006）的 `Locator` 与 `Fetch status`

### R4 — CASE-051：Alliance 收购的公开信息

- **为什么**：profile 与 Case 都写「Alliance 收购了 Zachtronics」，但收购方全名、日期、是否公开金额全部 UNKNOWN。这是「出售公司换取不做管理」这条解释链的关键一环。
- **来源**：Zachtronics / Alliance 官方声明；2018 年前后的行业报道；Alliance 的公司资料
- **定位符**：带有日期的官方声明或报道
- **可达性**：未探（需要用企业名 + 年份搜）
- **要带回**：收购方全名、公告日期、是否披露金额；**若确认从未公开，也要明确写"从未公开"**
- **回填到**：CASE-051 ledger 新 E 记录；Case §4.5 与 Open Questions

### R5 — CASE-012：自营 alpha 的原句、售价与团队名单

- **为什么**：#319 已把「Greenlight 之前就在自己网站卖 alpha，收入足以养活本人并雇 freelancers」写进正文与 Case，但**金额、时间跨度、原句**都还没有。editorial 分支补的 E003–E008 也还没被 profile 消费。
- **来源**：Siliconera 2015 interview（自营 alpha 那句）；GameSkinny 2017；4Gamer 2018（日文）；PC Games Insider 2018；2019 Reddit AMA；游研社 2019
- **定位符**：Siliconera 原文中该段落的逐字英文；4Gamer 日文原文中「两个夜班 + 五个开发日」那句
- **可达性**：部分 direct、部分 shell / blocked，详见 ledger 各条 `Fetch status`
- **要带回**：自营 alpha 的**售价与原句**；4Gamer 的核心四人 + 两位 freelancer 名单原句
- **回填到**：CASE-012 ledger E001 与 E003–E008

### R6 — CASE-016：把 `- **Class:**` 那批记录的引语补齐

- **为什么**：E020–E031 这批记录使用粗体 `- **Class:**` 格式，此前连审计工具都漏读（已由 #318 修正）。它们是 early id 一章里少见的**同期机构数据**（Census 1984/1989、IBM PC、NES 治理），值得有逐字引语而不是摘要。
- **来源**：ledger 内已有 URL：U.S. Census `P23-155` / `P23-171` PDF、IBM 官方 PC 史、Smithsonian 藏品档案、TIME 1982 封面
- **定位符**：PDF 页码 / 表格名；机构页面小标题
- **可达性**：官方 PDF 与机构页面通常 direct
- **要带回**：8.2% / 1.7% / 22.9% / 15.0% 等数字的**原表名与页码**，以及原文对口径的表述（household 还是 person）
- **回填到**：CASE-016 ledger E020–E031 的 `Exact Wording`

### R7 — early id：Kushner 书与 WIRED 1998 的可引用定位

- **为什么**：`book/profiles/early-id-doom.md` 有多个关键场景只有转述（1993 年餐厅道歉、1999 年保龄球馆、WIRED《Legion of Doom》里的地图作者就业）。它需要的是**可引用的定位**，而这正是 profile 目前最薄的地方。
- **来源**：David Kushner, *Masters of Doom*（2003）；WIRED 1998 年 *Legion of Doom* 报道
- **定位符**：书的**页码与版次**（不同版页码不同，必须注明）；WIRED 文章的段落定位
- **可达性**：书需实体/电子版；WIRED 旧文可能 direct 或需 archive
- **要带回**：页码 + 可直接引用的短原句；若某场景只有转述而无原文，写清「仅有转述」
- **回填到**：CASE-016 ledger 相应 E 记录

### R8 — CASE-051：2015 年财务变动的原始出处

- **为什么**：Case 的 Open Questions 第 2 项仍是 `temporary shutdown capitalization and ownership details`。profile 的「明确未知」清单里也列着「工作室暂停期间的完整财务数据」。
- **来源**：2015 年前后 Barth 的公开说法；当时的报道
- **定位符**：任何带日期的公开陈述
- **可达性**：未探
- **要带回**：原始出处，或明确结论"公开材料不存在"
- **回填到**：CASE-051 ledger / Case Open Questions

---

## 不要做的事

- 不要用 200 响应当作拿到内容；
- 不要把 show notes、聚合稿、转载稿当成一手来源（它们是 S2，只能登记为 Lead）；
- 不要为了填满这条队列而用模型知识补日期或金额；
- 不要在本队列里下结论——带回原话就结束，判断留给 Lane B。
