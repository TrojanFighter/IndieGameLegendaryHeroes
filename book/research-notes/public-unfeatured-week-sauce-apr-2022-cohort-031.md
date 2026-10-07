# 031 — 不在新闻里的 18 次公开创作：Week Sauce 2022.04 全体参赛作品试点

- Status: PUBLIC-ATTEMPT COHORT / SMALL RETROSPECTIVE PILOT / NOT A RATE OF GAME-DEVELOPER SUCCESS
- Observation cutoff: 2026-10-07
- Unit of analysis: **jam submission / project**，不是作者人数或独立工作室
- Frame: [Week Sauce (Apr 2022) 公开提交总表](https://itch.io/jam/weeksauce-4/entries) · [当期规则与 18 条公开项目目录](https://itch.io/jam/weeksauce-4)
- Companion gate: [028 媒体选择与分母协议](media-selection-survivorship-and-denominator-protocol-028.md) / [Creator Visibility Sampling Gate](../../schemas/creator-visibility-sampling-gate.md)
- Scope restriction: 英文 itch.io 公开小型 jam，**不是中国/斯拉夫研究**；不增加 Case / Claim，也不声称统计总体失败率。

## 一、先保住分母：谁被列入，为什么

本轮要修复一种长期误差：过去我们习惯打开成名游戏的 GDC 演讲，再往回寻找作者的努力和失败。这样做很容易找到善于解释自己、具有媒体故事性的作者，找不到未成名、从未接受专访、只留下小作品的人。

因此本轮不从“成功/失败”“是否采访”“销量多少”搜索人物，改从一个**事先由活动页面保留的完整公开提交名册**出发。

选中 *Week Sauce (Apr 2022)* 的方法理由：

- 页面记录 2022-04-01 至 2022-05-01 的月期，并公开展示 **18 Entries**；
- 主办方明确承认创作者有工作、家庭或其他责任，所以制作七天可以不连续；
- 明确欢迎把**没做完的东西直接提交**；不要求模拟完整商业生产；
- 题目是可选的“把一个喜欢的音乐团体名称改写成游戏主题”，报名人数不决定作品是否能收录；
- 18 条足以完成逐项审计，不需挑“最有代表性”的成功和失败者。

**必须坦白的设计边界**：这是可行性导向的回顾性便利选取，按名册规模和活动规则选jam；并没有在 2022 年预注册取样计划，也不是任何随机抽样。我们看见的是 `PUBLIC_SUBMISSIONS`，不包括注册但从未交作品者、没有电脑/时间参与者，以及所有私人原型。若它内部显示某种比例，**也只能描述这期18项提交在本次审计中出现了什么状态**，不能外推到独立游戏总体。

整个试点没有用访谈人数、赞助商声望、作品评分来挑条目：**18项全部列入**。也没有因为有人作品是 PDF 桌游，就偷偷排除它来抬高“电子游戏发售率”。

### Sampling declaration

```yaml
question: "在明确的小型公开 jam 提交队列中，2026 年究竟还能核查到哪些不同的作品/作者继续状态？"
target_population: "2022-04 Week Sauce jam 页面收录的所有提交作品，不含未提交者"
unit_of_analysis: project_submission
cohort_entry_event: "被 itch.io 当期 /entries 页面收录"
geography_and_year_window: "online / no country filter / 2022-04-01..2022-05-01"
sampling_frame: "https://itch.io/jam/weeksauce-4/entries"
selection_rule: "当期18个页面条目全收，无作品质量与销量筛选"
denominator_status: KNOWN_FOR_PUBLIC_SUBMISSIONS_ONLY
denominator_count: 18
visible_entries: 18
platform_page_inspection: "17 direct game pages accessible on 2026-10-07; 1 original project URL 404"
visibility_tier: "PUBLIC_COHORT / press exposure not systematically verified; not chosen from media coverage"
followup_window_and_censoring: "public itch pages inspected at 2026-10-07; last public update often UNKNOWN"
career_prehistory_observable: "mostly UNKNOWN; no employer/education cohort claim"
outcome_definitions: "itch status as platform metadata, not shipped-product/business outcome"
missingness: "deleted page, incomplete biographies, external builds, post-jam offsite updates, private work, dates and financials unknown"
rival_explanations: "casual jam, optional theme, entrant self-selection, mixed analog/digital category, teams vs solo"
permitted_inference: "what public traces and contradictory status labels occur among these 18 listed entries"
forbidden_inference: "typical independent developer success/failure rate, studio closures, unemployment, cause of non-updates, earnings"
```

## 二、完整名册：18/18，不按后来命运挑故事

以下顺序沿 [2022.04 jam 总览页面](https://itch.io/jam/weeksauce-4) 展示的顺序；不能把今天的 `Released / In development / Prototype` 页面标签倒当成 2022 年当时的真实项目阶段。每条的主体均是可点击的原始提交页，唯一访问失败的链接仍保留以供未来复查。

| # | 原始提交（公开页面） | 公开作者账号 | 本轮能确认的最小事实 | 2026 页面/项目观察 |
|---:|---|---|---|---|
| 01 | [THE CURE: Peculiar Pestilence](https://juliehirt.itch.io/the-cure-peculiar-pestilence) | JulieHirt 等多人 | 瘟疫治疗模拟；团队明确按各成员日程约定最多七个工作日并开例会 | `Released` 标签；网页/Windows可见；不是“单人七天完成” |
| 02 | [Screams and Queens](https://ladyorthetiger.itch.io/screams-and-queens) | ladyorthetiger | 桌面 RPG PDF，标价 $1，且入围其他主题 bundle | `Released` 标签；**非电子游戏**；标价不等于售出数量 |
| 03 | [Kaiju Finger Death Punch](https://pulsecoder.itch.io/kaiju-game) | pulsecoder 等 | Unity 怪兽石头剪刀布作品；有网页版本 | **`Prototype`** 标签；不代表已正式上市 |
| 04 | [AgainstheCurrent](https://cerbyo.itch.io/againsthecurrent-the-legend-of-the-chunchuntree) | Cerbyo | PICO-8 射击游戏；作者在同一页面提供 jam 版和后续 full version | **`In development`** 标签，但实际可见后续较完整版本和下载 |
| 05 | [Guns N' Roses](https://lake-monster-games.itch.io/guns-n-roses) | Lake Monster Games | Unity 跳台玩法；注明制作七天；May 11, 2022 有修复瞄准和增加计时功能的 devlog | `Released`；**可证明 jam 后短期继续修改**，远期未知 |
| 06 | [D3 Inc.](https://manofstories.itch.io/d3-inc) | ManOfStories | 提供规则、地图、游戏表格的 Print & Play 桌游 | `Released`；**非电子游戏** |
| 07 | [Snails in Peril](https://zeyt8.itch.io/snails-in-peril) | Zeyt8 等 3 人 | Unity? **引擎未作核定**；3D 双蜗牛协作潜行解谜，三位制作者有公开署名 | `Released`；Windows 下载页仍可见 |
| 08 | [Gravitation](https://volditedev.itch.io/gravitation) | Voldite | 2D 小型闪避/射击，ZIP 下载 | `Released`；作者后续工作 `UNKNOWN` |
| 09 | [Pop Idol Fight](https://alexgarbus.itch.io/pop-idol-fight) | Alex Garbus | Godot 双人格斗；公开写明编程与绘画由不同协作者完成；四平台包 | `Released`；页面有源代码链接、2022-04-30 下载文件版本 |
| 10 | [Plugging In Simulator (Proof of Concept)](https://yousayrandy.itch.io/plugging-in-simulator) | yousayrandy | 作者写明只投入两天，因**未具体解释的生活事件**无法继续，承认严重 BUG 和未完成 | 页面却标 **`Released`**；其 itch 主页仍显示其他游戏，不能断定退圈 |
| 11 | [sad boys club](https://popit-master.itch.io/sad-boys-club) | POPIT_MASTER | 简短 Twine 监狱逃脱 | `Released`；未确认有商业后续 |
| 12 | [the Diamond story](https://ifstoryman13.itch.io/the-diamond-story) | IFstoryman13 | Twine 互动故事；当时参与者留言讨论分支与结局 | `Released`；不能断定后来是否继续写作 |
| 13 | [The Queen — interactive fiction](https://mrsunflower.itch.io/the-queen-an-interactive-fiction-for-week-sauce) | Mr.Sunflower | Twine 熊与王冠故事；作者公开承认范围过大、时间用尽、分支不足，未来是否修订未知 | **`In development`**，不是已核的永久废弃 |
| 14 | [The Dangerous Journey to Happiness](https://aspiring-developer.itch.io/the-dangerous-journey-to-happiness-interactive-fiction-for-week-sauce) | Aspiring Developer | 作者明确称制作不到七小时的 Twine 互动故事 | `Released`；不等于商业发行 |
| 15 | [The secrets of jynx](https://jynxa.itch.io/the-secrets-of-jynx) | jynxa | Twine 互动小说 | **`In development`**；无证据判定活跃或停工 |
| 16 | [L.H.C.B.](https://wulf-denloft.itch.io/lhcb) | Wulf | Jam 名册仍保留名字与作者，但目标页面本轮返回 **404** | `GAME_PAGE_UNAVAILABLE`，不可归因为失败、删号或退出 |
| 17 | [For the Glory — Interactive fiction](https://thebluejade.itch.io/for-the-glory) | TheBlueJade | Twine 游戏秀互动故事 | `Released`；后续职业和制作 `UNKNOWN` |
| 18 | [A new planet](https://bruhnaldo.itch.io/a-new-planet) | Bruhnaldo | 页面提供 HTML 下载文件 | `Released`；作者职业背景 `UNKNOWN` |

**口径自审：** 18/18 提交可从活动名册确认；本轮 17 个作品页面可访问，1 项页面失效。页面平台状态快照为 13 个 `Released`、3 个 `In development`、1 个 `Prototype`、1 个因 404 无法查验。这里的 `Released` 包含两项实体/桌游和若干明确未完原型；其本意是 itch 页面的自选分类，**不是商业游戏“完成率 13/18”**。浏览器可玩数量等分类以活动官网计数为准，不能把所有 18 款都假定为 PC 商业作品。

## 三、四段可以直接写进书里的小人物故事

### 1. Randy：页面说“发布”，作者说“实在没有做完”

Randy Fluharty 的 [Plugging In Simulator](https://yousayrandy.itch.io/plugging-in-simulator) 是一款插电源插头的谜题原型。

他在页面上告诉来访者：只用了两天；第三关存在严重 bug；想过更复杂的旋转和观察方式，但未能实现；生活事件使自己无法继续花足够时间。

同一页的状态却写着 `Released`。

这对我们的研究提出了比“他的游戏卖了几份”更基础的要求：

**作品可以已经公开发布，同时作者认为它还远远没完成。**

另一方面，Randy 的 [公开 itch 作品集](https://yousayrandy.itch.io/) 还列有多款别的游戏。即便本项目不再更新，也不能断言这个人从此退出游戏创作。作品集未逐项确认日期，亦不能据此重建固定年份后连续产出的详细职业轨迹。

本案所需变量：
`JAM_SUBMITTED = yes`；
`PROJECT_PUBLIC = yes`；
`AUTHOR_DESCRIBED_INCOMPLETE = yes`；
`CAREER_EXIT = UNKNOWN`；
`COST = TWO_DAYS_DECLARED + LIFE_EVENT_UNSPECIFIED`。

### 2. Mr.Sunflower：作者知道哪里做得不够，却不知道还会不会回来

[《The Queen》](https://mrsunflower.itch.io/the-queen-an-interactive-fiction-for-week-sauce) 是关于一只熊、饥饿和王冠的短篇互动作品。

读者留言说：他希望有更多真正会改变结果的选择。

作者的回应并没有虚构一套高大上的设计理念。他承认自己做得太大，时间用完，许多选择不能造成足够不同的结局；他觉得这个题材有潜力，但不确定以后还会不会回来修改，因为时间稀缺。

这一段特别适合进入《失败不是资产》的书稿。

真实的创作生活里，决定是否继续开发的，不总是一个客观的“市场证明不行”。有时候作者清楚地看到改进方法，却没有下一段可支配时间。

不能把这件事写成他“放弃梦想”，也不能从一句“maybe”断言数年后的具体生涯。

`PROJECT_FUTURE = UNKNOWN`；
`AUTHOR_REPORTED_SCOPE_ERROR = YES`；
`AUTHOR_REPORTED_TIME_CONSTRAINT = YES`。

### 3. Cerbyo：平台写着“开发中”，作者已经放出下一版

Cerbyo 的 [AgainstheCurrent](https://cerbyo.itch.io/againsthecurrent-the-legend-of-the-chunchuntree) 是 PICO-8 射击游戏。

同一页区分 jam 版本与后续可下载的 full version。作者写到自己修了 BUG、改了数值、拓展了内容；在玩家评论里明确说后来的更完善版本可以玩。

但是平台项目状态仍然是 `In development`。

这反过来否定了一种简单的数据库操作：把长期显示“开发中”的项目自动视作“几年没做完”。

它证明在这个项目上确有**公开可观察到的后续迭代**。但我们仍然不知道作者在 2026 年是否活跃、有没有靠它赚钱、是否把其他作品变成正式商业游戏。

### 4. 一款看似“七天小游戏”的背后，可能是一整个分时协作组织

[《THE CURE: Peculiar Pestilence》](https://juliehirt.itch.io/the-cure-peculiar-pestilence) 的署名里有程序、策划、美术、音频、制作等许多协作者。

团队在页面解释：大家根据各自日程，一人最多贡献七个工作日，并且每周同步一次进展。

所以“七天 game jam 游戏”的日历长度，绝不能自动当成总劳动七人日或一人周。

同一队列还有只投入两天的 Randy、不到七小时的短篇作者、不同岗位的双人团队、PDF 桌游作者。

这类差异本身就是后来分析“人生性价比”时不能跳过的成本变量。

## 四、这份最小分母究竟教会我们什么

第一个结论并不惊人，但很关键：

**过去用著名成功者和著名失败者构成的案例档案，并没有覆盖这十八条微小生产经历。**

有的人把不足一周的时间做成了自己的第一份公开作品。有的人投入两天，却因生活事件无法继续。有的人已看见自己原型设计上的具体缺陷，尚未决定以后是否值得再改。还有人将 jam 作品继续修订，旧页面的状态标签甚至没有及时反映这个事实。

这些经历缺乏可出版的名人访谈、财务数据和“命运被一次发售改变”的戏剧性。

但如果读者正在考虑下班以后做游戏，这些状态比那些投资回报异常的大作更接近现实。

**第二个结论是严格的负面结论：** 18 个 jam submission **没有足够的数据**告诉我们“普通创作者多少人能够养活自己”。它连“每个人之前是不是职业游戏开发者”“为什么再也没更新”都无法确定。

如果现在写“13/18 成功，3/18 开发中，1/18 失败”，研究方法就彻底出错了。

正确的说法只能是：这是一个公开提交项目的全名册，我们已经核验出若干可观察轨迹和大量未知，不能推断项目或职业成功率。

**第三个结论：** “退出”至少需要拆成五个不同问题：

- 作品有没有在 jam 里上传？
- 作品有没有被作者自己称为完整？
- 作者有没有继续改同一作品？
- 作者有没有做别的作品？
- 作者有没有在游戏行业就业／转行／继续维持工资？

这五个问题的公开证据可见性完全不同。不宜用某一页没更新来替代其它四个答案。

## 五、下一轮如何才可能减少 UNKNOWN，而不是假装知道了

1. 固定 18 条 URL 的历史快照，并记录页面最后可见的**确切日期**（没有的写 UNKNOWN；不以 2026 抓取日期冒充发布日期）。
2. 对所有 18 个作者页面以同一协议核查公开后续项目。要注意有的作品多人、有的账号不是真实身份；需要改用 project-to-creator 的多对多关系，不能偷偷把“18项目”改成“18人”。
3. 单独记录 `NO NEW PUBLIC PROJECT OBSERVED`，**永远不编码为** `STOPPED_DEVELOPING`。
4. 不主动挖掘私人家庭财务、居住、医疗或社会账户；若要补机会成本，优先使用作者自己公开说明的时间、工资/工作状态、协作者、收费、发行节点。
5. 第二个独立公开队列应选 **不同组织条件** 的小型 jam（例如严格两天、限制报名者身份或允许长期协作），测试这次 Week Sauce 对工作/家庭议题的**自选择效应**。
6. 只有建立多组同口径项目以及可观察的真正职业起点之后，才考虑“发售后多少年还有公开创作”等有限统计；对未公开作品和就业者仍应标观察盲区。

**结论：** 本轮首次实质完成 `PUBLIC-ATTEMPT` 小分母完整列名册，而不是在成功者故事后面随便贴两位失败者。它给书稿提供了四组可用的人物片段，也更明确暴露了我们仍然无法看到哪些人和哪些成本。

---

## 原始证据入口

- [Week Sauce 2022.04 总览、官方规则和完整名册](https://itch.io/jam/weeksauce-4)
- [Week Sauce 2022.04 /entries 18条独立条目](https://itch.io/jam/weeksauce-4/entries)
- [Randy 两天原型与生活事件自述](https://yousayrandy.itch.io/plugging-in-simulator)
- [Mr.Sunflower 关于 scope/time 的原作者回应](https://mrsunflower.itch.io/the-queen-an-interactive-fiction-for-week-sauce)
- [Cerbyo jam vs full version 的同页记录](https://cerbyo.itch.io/againsthecurrent-the-legend-of-the-chunchuntree)
- [THE CURE 项目多人协作与七日分工](https://juliehirt.itch.io/the-cure-peculiar-pestilence)
- [Guns N' Roses 2022.05.11 的两个 devlogs](https://lake-monster-games.itch.io/guns-n-roses)
- [yousayrandy 公开多个其它游戏的项目页](https://yousayrandy.itch.io/)

上述 URL 只指向公开作品与本人公开写下的制作信息；不使用未核实的媒体稿、第三方商业估值，也不推测私人生活事件细节。
