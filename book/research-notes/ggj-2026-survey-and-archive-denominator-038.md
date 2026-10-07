# 038 — 四万人参加、三千五百份答卷、近万份作品：GGJ 真正覆盖了哪些“普通创作者”？

- **Status:** RESEARCH NOTE / SAMPLING-FRAME & DATA-LIFECYCLE AUDIT / 2026-10-07 / PRE-CLAIM
- **Issue:** 用有名有姓的父母访谈补中国/国外开发者的成长史仍然只在筛选成功的创作者；宏观 GGJ 参赛名册覆盖了大量普通制作行为，却同样不能覆盖未报名的人，且公开旧作品资料正面临实质删除。
- **Research links:** [028 媒体/幸存者偏差](media-selection-survivorship-and-denominator-protocol-028.md) · [031 Week Sauce 18作品固定分母](public-unfeatured-week-sauce-apr-2022-cohort-031.md) · [033 Week Sauce主账号四年跟踪](week-sauce-2022-public-creator-followup-033.md) · [037 家庭认可不靠爆款](family-legitimacy-visible-labor-and-fifteen-year-exit-037.md) · [中国 GGJ 2024 深圳南山站16目录条目，待去重](../../country-studies/china/002-ggj-2024-shenzhen-nanshan-public-attempt-pilot.md)。
- **Sources accessed:** 2026-10-07，官方 2026-04-13 Survey、2026-07-03 Archives Policy、2026-01-06 Licensing Policy、2026-06-19 Springer学术研究。
- **Important:** 某些官网原站返回403；2026 GGJ数字和档案政策引用的是由搜索引擎展示的官方全文索引（`OFFICIAL INDEXED`），不是宣称已从原页成功打开。首次2026-02与最终2026-04汇总数字不同；官网政策正文与末尾日期表亦相互冲突，全部保留。

## 1. 四套不同的“分母”：现有调查为什么回答不了“被家长拦在门外的有多少人”

**2026-04-13 GGJ官方调查**：https://globalgamejam.org/news/global-game-jam-2026-jammer-survey-data

| Unit/frame | 2026官方数字 | 真正观察到什么 | 禁止推断 |
|---|---:|---|---|
| 活动已注册参与者（Event people） | 39,197 | 94国、824站点最终汇总；含站内/线上，首次官方2026-02初报39,069人/811站，选用4月后核版 | 参与 ≠ 独立个人开发职业；未参与者的家庭障碍 **不在这里** |
| 当届上传作品（Submission / artifact） | 9,874 | 作品/提交记录，不等于游戏开发者人数；一个团队可有多人，页面可能多version | 不要用 9,874/39,197 算「个人成为游戏作者的成功率」 |
| 事后问卷参与者（Volunteer respondents） | 3,535，回复率约9% | 37题自选问卷；单项答复覆盖75–99%，与问卷前后顺序有关 | 不能因`n>3,500`就自动具备总体代表性；未回答者可能系统性更不满意、疲惫或缺时间 |
| 从来没有报名/原型未公开/愿望被家校否决 | 无 | Frame D：真正缺失的上游未出发者 | 不可用 GGJ任何参加者/问卷样本来估计家庭阻止制作的总体比率 |

官网自称样本量足够`statistically valid`，同时也承认自愿样本不一定随机：统计**抽样误差小不等于选择偏差小**。记 `VOLUNTARY_RESPONSE_SELECTION`、`DROPOUT_BY_QUESTION_ORDER`、`POST-EVENT_ONLY`，不能把事后收集的参与意见当事先职业抉择或未来长期职业状态。

**其中几项可描述“在愿意回答问题的 GGJ 参加者中”而非一般人口：**
- Student 37%、Hobbyist 28%、Solo Dev 18%、Small Studio 9% 等为答卷中**自我定位的工作实践类型**，不是职业上互斥、永久不变的法律就业类型。学历 High school or below 24%、Some college 22%、Bachelor 29%、Master 13%。
- 年龄 18–22岁40%、23–25岁18%； under18 3%，**GGJ NEXT的10–18岁参赛者未包含在这组数字里**，不宜据此描述少年潜在玩家/作者。
- 过去参加过任意game jam者61%，第一次参与 GGJ可能是63%（官方说仅37%参加过往届GGJ）；这两种`previous jam`定义并不矛盾。
- 99%以上称“肯定/可能再来”，发生在**完成后且自愿回答满意度调查的人**，不是所有报名者的真实明年返场率。94%报“提交游戏”也不是有售游戏比例。
- 2025同官方问卷：4,108份自愿答卷、约11%回复率、2025 survey site称35,427参加者；2026 survey 3,535/39,197。横向比率变化缺逐格回应概率，**不能直接宣布“2026新人的意愿比2025下降/增长”**。
- `work practice`、`age`、`prior experience`的已报百分比都是后事件**答卷人口**, 不是中国家庭和美国家庭“有多少人变成开发者”的分母。

**来源：** 2026-04-13 GGJ https://globalgamejam.org/news/global-game-jam-2026-jammer-survey-data ；2025-03-25 https://globalgamejam.org/news/global-game-jam-2025-jammer-survey-data ；2026-02初报 https://globalgamejam.org/news/thanks-making-ggj-2026-success

## 2. 2026学术研究证实另一种分母陷阱：十五人纵向访谈≠随机挑选了十五个后来的人生

Ali Arya & Omar Bani-Taha, `Insights on game jams as bridging educational activities`, **Discover Education**, 2026-06-19, https://link.springer.com/article/10.1007/s44217-026-01810-5。

- 2023秋至2024冬访问15位：曾在**同一机构/一处GGJ站点**有记录、至少两年以前参与的14名jammer + 1位别站组织者；受访者能联系到、同意接受采访、在回顾时仍可以说明职业生活。研究采用grounded theory质性抽样，意图形成机制理论，而非抽样加权推算全国/国际职业转换率。
- 研究者明言以往许多game jam研究大多发生在事中或紧接结束，缺乏长期效应，特别强调时间、能力焦虑、团体信任、交通、家庭照护/儿童、设备成本及排斥感等**上游参与门槛**。但这些门槛来自入场者/文献，尚不足以观察“**根本没有出发的人**”。
- 研究参与者包括早已具有职业经验或在别的行业工作的jammer。实证现象是**一些人在下班后来玩/学习、获得友谊/自由、未必寻求游戏从业工作**。这对“没成为职业开发者就是失败”产生关键否证：很多参加者根本没有将职业游戏视为目标。
- 样本包括不少有继续创作的主动参与者；其研究为一个站点、匿名伦理保护、无公开原始个体数据，不能把15个匿名人生再识别以建传记数据库。
- **该研究最值得迁移的不是任何比例，而是访谈框架**：`参加时的预期`→`当时获得的能力/伙伴`→`实际职业路线`→`多年后再评价`；未来若研究家庭，还要加`入场前家人反对/资助/时间/照护支持`，并设访谈中表达**自愿和家庭匿名边界**。

**特别反压力：** 论文使用“jam是桥梁”理论并非证明所有人必须“过桥去做商业游戏”；一部分人选择始终在桥上做低风险实验，也可能达成初衷。

## 3. 2027前研究材料会真实消失：GGJ公布旧站档案下线

GGJ 2026-07-03官方公告： https://globalgamejam.org/news/updating-our-global-game-jam-archive-policy

- GGJ历届四套旧站：V1 2009–2012、V2 2013、**V3 2014–2023**、V4 2024以后。未来GGJ只保留最近四届作品；所有历史场站、年份、参赛/游戏数与**作品标题**将长期保留，但旧版游戏档案内容/构建/页面可能不继续可访问。
- 2026-10-07 时GGJ V3 仍在10月1–7日的**本月开放窗口**，之后按公告10月8日下线，11月1–7日再开放。
- **政策同一页内部有期限冲突：** 叙述正文称V3 `2026-12-01至2027-03-31`持续开放，`2027-03-31`以后永久移除；但页面结尾**Key Dates**明确写`2027-02-28`结束游戏下载、`2027-03-01` V1/V2/V3全部sunset。因此研究计划要采取**更早的2027-02-28作为保守实际截止**，并保留`GGJ_INTERNAL_DATE_CONFLICT`；这不是我们替GGJ发布正式更正。
- V1/V2此前已退出线上，原游戏提交者可申请找回自身作品；V3旧站一部分仍在线；GGJ还计划向愿意接收的保存机构捐赠2009–2023年旧归档硬盘，**尚未证实已有接收机构**。
- 官网称十余年100,000+历史jam游戏/17TB资料，早期旧构建可能无法在新系统运行；它本身只有当年的初版，不能代替后来Steam发行版本。**失去GGJ文件不等于作者停做、作品被取消或之后无产品**。
- 2026-01-06 GGJ已改变提交授权：允许团队自行选择游戏license（需授GGJ永久托管权），不再一律采用同一模板。因此**旧archive可公开下载，不代表研究者可任意批量复制、镜像、重发或用于模型训练**。尤其本书属于可能发行出版的研究，避免下载和重发非本人游戏资产，须按每个作品许可和隐私规则。官方：https://globalgamejam.org/news/updating-license-terms-ggj-game-submissions 。

### 与现有本库有什么即时关系

**中国GGJ2024深圳南山** [pilot 002](../../country-studies/china/002-ggj-2024-shenzhen-nanshan-public-attempt-pilot.md)属于V4(2024+)而非V3，不应写作2027-02会被整站删除；它目前仍有16 listing / 15 unique titles、重复提交未核、permalink不全的质量问题，仍需去重和freeze元数据。

**Week Sauce 2022.04 的18个作品**来自`itch.io`而**不是GGJ旧站**，不能因为GGJ旧站删除就说这18个项目也会消失。它们有自己的URL失效/作品修改风险、独立照样需要 source ledger，但这不是同一个网站政策。

**新增待处理高价值入口（非现在声称已经搜完）**：如要对比2020/2021/2022/2023 GGJ，时间窗口内优先**合法记录官方公开目录的title+event+year+public URL+metadata provenance+capture date及查看可用性**，选定一两个原本事前固定的本地站点，不从获奖页挑。对受许可分享的作品可留外链，**不得未经许可自动复制10000个可执行文件或找出私人个人身份**。作品/个人/团队继续分开。

### 证据生存风险矩阵（研究自身最值得增加的字段）

| 字段 | 可观测/谁能说 | 研究不可推断 |
|---|---|---|
| `listed_at_initial_jam`、`url_accessed_at` | 官网名册与访问日期 | 页面消失 `=>` 项目取消 |
| `game_build_license_at_jam` | 版权页/当届官方规则/作者许可 | 2026新许可反过来覆盖早年上传文件 |
| `archive_policy_url`、`scheduled_sunset` | 2026-07-03公告+内部矛盾 | 官网一条互相矛盾的日期说明已解决 |
| `independent_official_release_after_jam` | Steam/itch/GitHub可核连线 | 同名产品就是同作者的延续 |
| `participant_self_selected_for_survey`、`nonresponse_rate` | 2025/26官方调查方法 | 自愿问卷即总体随机分布 |
| `family_permission_or_household_support` | 仅本人/家属在知情允许后愿讲 | 已参与GGJ者当成“未经家庭许可被迫放弃者”的代表 |

## 4. 实际建议：把“职业成功率”问题拆成两个可招募面板

**Frame B / already-attempted：** 从年度/站点完整GGJ报名/提交名单构建`本人自愿参加`的开发者面板，未来观察6/12/36个月：做新项目、只做非商业爱好、就业、家庭支持、职业/家庭成本等。名单只提供接触候选；在没有个人知情同意时不创作所谓“家庭经历”。

**Frame D / not-yet-attempted：** 在游戏课/计算机/艺术/普通高校/职业培训/地方社群**报名之前**（或所有相关学生构成的抽样群）询问`是否想制作游戏`、`有没有设备/时间`、`家人是否在去年否决报考/职业选择`、`课程/收入/地域与签证`及`是否真正做过最小原型`。不要仅从已经入游戏专业的班级取样。两组不能共享同一个“成为开发者概率”分母。

失访与尊严：`NOT CONTACTED`、`DECLINED`、`LOST TO FOLLOWUP`、`PRIVATE WORK`、`NONCOMMERCIAL BY CHOICE`、`EXIT DUE FAMILY`、`EXIT DUE MONEY`、`EXIT DUE OTHER`分别记录；退出职业游戏不等于失败或无创造力。不得对未公开人物家属进行所谓“背景调查”。

**方法论结论：** 我们已经找到普通人留存作品的分母，但并没有普通人家庭支持的分母；GGJ自选调查能说明参加者的一些特征，却没有测量潜在未入场者。就算有十万个公开作品，也不能自动把“没有参赛者”的人生从历史上救回来。

### Sources / date / provenance

1. GGJ Inc., `Global Game Jam 2026: Jammer Survey Data`, 2026-04-13, official indexed, https://globalgamejam.org/news/global-game-jam-2026-jammer-survey-data
2. GGJ Inc., `Global Game Jam 2025: Jammer Survey Data`, 2025-03-25, official indexed, https://globalgamejam.org/news/global-game-jam-2025-jammer-survey-data
3. GGJ Inc., `Thanks for Making GGJ 2026 a Success!`, 2026-02-10, official indexed, https://globalgamejam.org/news/thanks-making-ggj-2026-success
4. GGJ Inc., `Updating Our Global Game Jam Archive Policy`, 2026-07-03, official indexed, https://globalgamejam.org/news/updating-our-global-game-jam-archive-policy
5. GGJ Inc., `Updating the License Terms for GGJ Game Submissions`, 2026-01-06, official indexed, https://globalgamejam.org/news/updating-license-terms-ggj-game-submissions
6. Ali Arya & Omar Bani-Taha, `Insights on game jams as bridging educational activities`, Discover Education 5(811), 2026-06-19, S1 academic original study, https://link.springer.com/article/10.1007/s44217-026-01810-5

**Transfer (2026):** `CURRENT time-limited archival concern` for GGJ V3, `DURABLE selection/consent mechanism` for sample building. No claims about comparative national prevalence, success rates, family approval rates.
