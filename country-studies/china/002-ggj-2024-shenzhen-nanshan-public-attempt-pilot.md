# 002 — 从英雄传记转向可计数的尝试：GGJ 2024 深圳南山站 Public-Attempt Pilot

- Program: C / 中国国情研究
- Status: **PILOT INTAKE / ROSTER RECONCILIATION OPEN / NO POPULATION INFERENCE**
- As-of audit: 2026-10-07
- Unit: **公开提交的游戏项目**，不是开发者个人、雇员、报名者、团队或公司
- Research boundary: 只研究公开资料；不建个人隐私档案，不以姓名猜测任职、经济或家庭状况。
- Method gate: [Creator Visibility / Sampling Gate](../../schemas/creator-visibility-sampling-gate.md)；[028 Media Selection & Denominator](../../book/research-notes/media-selection-survivorship-and-denominator-protocol-028.md)
- Hypothesis routing: [AC-010 Prestige Pipeline](../../author-corpus/AC-010-prestige-pipeline-coupling-and-authorial-continuity.md)；[中国三层图 018](../../book/research-notes/china-creator-constraints-three-layer-map-018.md)

## 0. 为什么先做这个，而不再找一个「大厂出走成功」故事

既有 CASE-059/061/062/046 与中国案例能够检查作者线程、工业经验、家庭与项目决策的**机制**，不能回答这些人在游戏产业从业者中有多常见。著名失败者同样经过媒体可见性筛选。

本次换一个与成功、失败、受访、发售无关的起点：**固定年份、固定场地、固定公开上传名册**。选择本地小型站点，是为了审查能否完整列举和复查记录，并非声称深圳具有全国代表性，也不是事后按热门游戏挑样本。

本轮的工作产物是**审计得了的 sampling frame 尝试**，不是新的一篇成功学，也不是中国雇员的概率样本。

## 1. 抽样声明 / Preregistered frame statement

```yaml
question: "一个不按媒体报道选人的公开 game-jam 入口，到底能观察到多少项目与什么类型的后续痕迹？"
target_population: "2024 GGJ China × CiGA 深圳南山站在官方页面保留的游戏提交记录"
unit_of_analysis: project
cohort_entry_event: "游戏作为 2024 GGJ 深圳南山站作品提交到官方 GGJ 网站"
geography_and_year_window: "深圳南山站，2024-01-26 至 2024-01-28"
sampling_frame: "GGJ 官网该场地的 Games 目录；不使用媒体/GDC/Steam 畅销榜筛选"
inclusion_exclusion_rules: "收录目录中的全部游戏提交；不按奖项、题材、开发者履历或后续命运删选；站外未提交和仅报名者不计入"
denominator_status: PARTIAL
denominator_count: "官方当前目录显示 16 个项目；条目逐个完整重建尚未完成"
visible_entries: "已追索到 14 个不重复的候选标题，尚待与完整 16 条目录逐项核对"
visibility_reasons: "official jam archive; official jam project pages; official site page"
missingness: "官网目录读取不稳定、个别 403/500；至少 2 个目录项目名未确认；个人履历、私人原型、学校/雇主和团队完整成员未知"
outcome_definitions: "GGJ submission visible / post-jam continuation unknown / commercial release unknown / abandonment unknown / return-to-job unknown"
followup_window_and_censoring: "2024 jam 至 2026-10-07；尚未系统追踪后续；网页失联/匿名身份不等于停止创作"
rival_explanations: "自愿报名、场地主办网络、岗位/专业结构、团队合作、匿名程度、发布平台、社会经济支持"
permitted_inference: "官方站点展示了固定时空内的一批公开参赛项目；可以核验特定项目是否留下官方提交页面"
forbidden_inference: "中国独立项目或大厂员工的创业率、创新能力分布、中美差距、私人创作缺失、被家长阻挠/被绩优主义规训的个体归因"
```

**分母精确语义：** “16”是官方场地页 `Displaying 1 - 16 of 16` 所报告的**现存公开游戏页计数**（访问记录见来源），不是16名创作者、16支唯一团队、16个报名者，也不证明当年从未发生删除/合并/迟补页面。因此它是一个**有限的目录条目计数**，并非研究目标人群的覆盖率。

## 2. 起点证据与入选规则

1. 官方站点信息：GGJ China 2024 × CiGA – Shenzhen - Nanshan；线下站点、年龄 18+、开放报名（Anyone）；开始 2024-01-26 16:30，结束 2024-01-28 21:00。
2. 官方作品目录：`https://globalgamejam.org/group/499/games`；检索快照显示 `Displaying 1 - 16 of 16`。
3. 官方站点：`https://globalgamejam.org/jam-sites/2024/ggj-china-2024-ciga-shenzhen-nanshan`。
4. 此入口只由**站点+时间**确定，不要求项目在 Steam 上架、被采访或后续商业成功。

当前搜索与目录内容存在抓取不稳定：部分官方游戏页可打开，部分出现 403，目录尝试出现 500。**未取得可重用的完整目录导出，因此不能宣布“16/16 名册重建完成”。**

## 3. 逐项候选名册（当前 14 条；不是 14/16 完整成果）

下表只记录项目**在第一方页面/搜索快照中的名称与入口**。未核的后续情况一律为 `NOT_ASSESSED`，不贴 `PUBLIC_UNFEATURED`、`FAILED`、`DROPPED_OUT` 等标签。

| ID | 公开项目题名（保留原文拼写） | 来源入口 | 2024 后续/开发者就业史 |
|---|---|---|---|
| SZ24-01 | :>omit (Vomit) | https://globalgamejam.org/games/2024/omit-vomit-4 | NOT_ASSESSED / UNKNOWN |
| SZ24-02 | PutTogether | https://globalgamejam.org/group/499/games | NOT_ASSESSED / UNKNOWN |
| SZ24-03 | BOOM CHASE | https://globalgamejam.org/group/499/games | NOT_ASSESSED / UNKNOWN |
| SZ24-04 | MoMo Operater | https://globalgamejam.org/group/499/games | NOT_ASSESSED / UNKNOWN |
| SZ24-05 | 我爱摸鱼，天天摸鱼（Office Laziness Battle） | https://globalgamejam.org/games/2024/woaimoyutiantianmoyuoffice-laziness-battle-9 | NOT_ASSESSED / UNKNOWN |
| SZ24-06 | Attack on otter | https://globalgamejam.org/games/2024/attack-otter-7 | NOT_ASSESSED / UNKNOWN |
| SZ24-07 | 美丽的球 BraveNewBall | https://globalgamejam.org/games/2024/meilideqiu-bravenewball-8 | NOT_ASSESSED / UNKNOWN |
| SZ24-08 | LaughMaker | https://globalgamejam.org/games/2024/laughmaker-3 | NOT_ASSESSED / UNKNOWN |
| SZ24-09 | Laugh at Life | https://globalgamejam.org/games/2024/laugh-life-1 | NOT_ASSESSED / UNKNOWN |
| SZ24-10 | 口腔妙妙屋 | https://globalgamejam.org/games/2024/kouqiangmiaomiaowu-2 | NOT_ASSESSED / UNKNOWN |
| SZ24-11 | 赛博算命酒保行动 | https://globalgamejam.org/games/2024/saibosuanmingjiubaoxingdong-5 | NOT_ASSESSED / UNKNOWN |
| SZ24-12 | 笑到最后 Laugh2Die | https://globalgamejam.org/games/2024/xiaodaozuihoulaugh2die-6 | NOT_ASSESSED / UNKNOWN |
| SZ24-13 | 酶你不行 Funzyme | https://globalgamejam.org/games/2024/meinibuxingfunzyme-6 | NOT_ASSESSED / UNKNOWN |
| SZ24-14 | Buy More | https://globalgamejam.org/jam-sites/2024/ggj-china-2024-ciga-shenzhen-nanshan | NOT_ASSESSED / UNKNOWN |

**Reconciliation debt**：剩余约 2 项的名称与永久链接尚未确认；目前14条也需同一时间点完整列表去重复核（项目别名、改名、删除以及新增均可能改变计数）。不得为了凑 16 猜标题或把别站项目挪入。

第一方抽查的最小观察例：`Attack on otter` 页面可直接核对 2024 / Make Me Laugh / 深圳南山站 / Windows / Unreal Engine；`Office Laziness Battle` 页面列有 Windows / Unity 及作品说明。**引擎或题材不能证明开发者来自大厂/名校，也不能证明后续有商业发行。**

### 3.1 页面 UI 的一个实际误归因风险（2026-10-07 抽查）

`Attack on otter` 与 `Office Laziness Battle` 的游戏页有 `Jammers` 标签；点击分别指向成员页面，但本轮返回 403，**不能声称已核实名册中任何个人**。页面下方 `Recently Joined` 是动态组件，不能误作当前游戏的参与名单或开发分工。由此，`16 games` 目前既不能转换为 `16 people`，也不能转换为“公开职业史缺失的人数”。

## 4. 这个 frame 能识别什么、不能识别什么

| 研究对象 | 本目录可以直接回答 | 不能回答 / 需要另一 sampling frame |
|---|---|---|
| 作品公开意愿 | 存在官方提交页与项目说明 | **全部报名者**或**全部私有原型**是否愿意公开 |
| 自主创作实践 | 某人在固定 48h 场合**参与了公开项目**，若成员页可复核 | 他入职之前/任职期间有无持续的自发创作 |
| 项目继续推进 | 未来若有**同一项目明确的后续证据**，可记录公开轨迹 | 没搜到后续 = 取消 / 商业失败 / 不再做游戏 |
| 职业/教育背景 | 只有当事人公开、可核对、且身份对应时方可记录 | 缺 LinkedIn/校友资料就推定“非名校/非大厂” |
| 家庭/社会干预 | 如有**自愿公开、明确归因、同期证据**，可研究机制 | 没有采访时推断父母禁止、欺凌、失败耻感 |
| 体制总体问题 | 检验一个**公开尝试入口是否可追踪** | 中国雇员与欧美雇员作者性留存率 |

本试点最大的发现不是任何显著性或“成功者比例”，而是**可观察入口与目标问题的断裂**：找到“公开做过一个 game jam”的人，不等于知道“从名校走进大厂之后，有多少人不敢再自己出题”。

## 5. 下轮操作——严格先抽样后追踪，禁止追名人

### Gate A｜名册完整性（当前未通过）
- 以同一官网分页/快照核齐 16 个**永久游戏项目链接**，记录快照时间、总条目、重名/重复/已移除项。
- 保留网站不可用证据，必要时交叉官方 Web Archive / organiser 导出；不可使用“媒体搜得到”为补齐唯一标准。
- 如名单一直无法完整复原，`denominator_status=PARTIAL`；可展示个案但不可推断站内任何频率。

### Gate B｜同规则、同字段后续追踪（未执行）
每一个项目按一致的顺序检查：官方游戏页及 jammers → 官网链接到的公开项目账号/仓库（如有）→ 同名更新日志/发布页 → 2026-10-07 时点是否存在**能证实同一项目**的后续作品。必须留 `UNKNOWN`，不得根据「没有新帖子」填 `ABANDONED`。

最小字段：

```yaml
entry_id: SZ24-xx
official_project_url: "url or UNKNOWN"
roster_confirmed: YES | NO
duplicate_of: "entry id or NONE or UNKNOWN"
jam_artifact_exists: VERIFIED | LINK_ONLY | UNKNOWN
public_followup_trace: VERIFIED | NONE_FOUND_WITH_SEARCH_SCOPE | NOT_ASSESSED
identity_match_to_followup: VERIFIED | AMBIGUOUS | UNKNOWN
career_preentry_publicly_documented: VERIFIED | PARTIAL | UNKNOWN
role_employer_publicly_documented: VERIFIED | PARTIAL | UNKNOWN
family_or_household_publicly_documented: VERIFIED | UNKNOWN
press_biography: VERIFIED | NONE_FOUND_WITH_SEARCH_SCOPE | NOT_ASSESSED
last_observed_at: "YYYY-MM-DD"
source_links: []
```

`NONE_FOUND_WITH_SEARCH_SCOPE` 只能写在已记录查询平台、关键词、时间的字段，**不是生活状态**。不要抓取隐私、匿名账号实名映射、亲属资料；个人主动公开之前都写 UNKNOWN。

### Gate C｜独立的雇员/毕业生 frame（仍是更高优先级问题）
真正检验 AC-010 必须从**入职/毕业以前定义的队列**切入，尽量获得组织/学校可复核的人群分母，再追作者性改变与私人作品不可观测情况。若只能找到曾参赛者，最多分析该参赛者子群，不得偷换为所有员工。

三层检验必须有独立证据：
- **教育**：进入制度之前是否已持续自出题、作品与反馈；不可由学校名声倒推创造力。
- **行业版本现状**：项目目标、岗位 decision rights、旧 KPI 与玩家验证时序；48h jam 不能替代商业项目的 scope 审计。
- **社会版本意识**：公开披露的家庭风险、社会认可与失败合法性；不强求个体披露。

## 6. Reader-layer 出口：补进「没有写成英雄故事的人」

这批记录将来只有在身份、项目与上下游证据足够时才挑选传记/机制深描。重要的不是给他们追封失败或成功，而是正视：

> **有些人在履历、收入和家庭安排之外，还留下过一个公开的48小时小游戏。这个事实值得被记录；它本身并不能说明后来为什么没有出现另一款作品。**

- 不再由“值得讲故事”决定抽样名单；只由既定名册决定被观察的机会。
- 不再把沉默误当放弃、把没发售误当能力不足、把进大厂误当作者性消亡。
- 即使之后能逐项追踪全部 16 个公开项目，也只能说明**这个站点的公开项目轨迹**，不能把比例套进国民性或中美比较。

## 7. Source ledger / review debt

- **P0 / first-party venue:** Global Game Jam, `GGJ China 2024 × CiGA – Shenzhen - Nanshan`, event page, 2024 event, accessed/search-audited 2026-10-07. https://globalgamejam.org/jam-sites/2024/ggj-china-2024-ciga-shenzhen-nanshan
- **P0 / first-party dynamic roster with partial accessibility:** Global Game Jam, `Games — group 499`, current directory reports 16 items in the search cache; full page could not be fetched consistently on 2026-10-07. https://globalgamejam.org/group/499/games
- **P0 / first-party project details, partial:** individual game page URLs in §3. Verified directly when accessible; search-index excerpts are **DISCOVERY/REQUIRES_RECHECK** until the corresponding page can be opened.
- **H / analytical limitation:** why prior media case selection cannot identify national prevalence: [028](../../book/research-notes/media-selection-survivorship-and-denominator-protocol-028.md); no project outcomes or social causes inferred in this file.

**Exit criteria for this WIP:** verify 16/16 roster items; execute uniform public-trace checks; publish missingness table; and explicitly judge whether this frame can support any inference beyond "visible game-jam submission exists". Until then **no rate, no country comparison, no creator-status labeling**.
