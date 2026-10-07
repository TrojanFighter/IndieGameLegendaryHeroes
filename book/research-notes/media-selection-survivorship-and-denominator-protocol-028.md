# 028 — 媒体可见性不是创作者总体：幸存者偏差、二次选择与分母重建

- Status: METHODOLOGY / RESEARCH-GATE / PRE-CLAIM
- Updated: 2026-10-07
- Scope: 《独立游戏英雄传说》所有人物传记及跨地域职业比较；优先修正 `AC-010`、“教育×行业版本×社会版本”与 LR-001 / LR-005。
- Applies to: Case intake / biography / cross-case comparative claims / reader-facing life advice
- Key restriction: **Media-discovered cases are mechanism cases, never denominator evidence.**

## 0. 对目前研究方法的自我纠错

过去我们的搜索链条经常是：

```text
「从大厂出来仍然很有作者性」的问题
       ↓
能被搜索引擎发现的采访 / GDC postmortem / 媒体明星
       ↓
Mega Crit、Supergiant、Red Hook、Sandfall 等成功/出名作者
       ↓
这些人物的故事非常合理而鲜明
       ↓
不知不觉把「成功者存在某机制」替换成「普通从业者通常如何」
```

这是**两级甚至三级选择偏差**：

1. **Career / Attempt selection**：只有尝试离开大厂、公开项目、注册公司、发售、存活的人，才可能进入后续研究；大量**没有尝试、想尝试但从未行动、做过私人原型却没有发布、项目中止、转回就业**的人不在报道视野。
2. **Outcome / Survivorship selection**：取得醒目销量、奖项或职业转折的人较容易进入公开史料；失败/未发售项目容易失联。
3. **Media / Narratability selection**：即使都是成功/失败，媒体还偏向**故事可讲、英语或主流市场可报道、愿意受访、有公关渠道、能输出自我解释**的人。受访后的回忆本身还可能被成功结局重写。

**失败案例被媒体报道，也没有自动解除偏差。** “引人瞩目的失败者”同样是媒体选择后的样本。

特别是“从大厂规训中逃逸”的叙事具有很强文学吸引力；对研究而言，这可能增加被采访/转载的概率。这个方向目前是 selection-mechanism HYPOTHESIS，未完成定量验证。

## 一、我们的四类问题，最多能用什么证据回答？

| 研究问题 | 合格证据 | 明令禁止 |
|---|---|---|
| **某个机制是否可能发生？** 如作者线程与工业技能并存 | 一手同期材料+开发日志+关键决策时间线，追踪单人/团队即可 | 把可能性当普遍性 |
| **为什么此人如此选择？** | 尽可能有同期材料、角色和现金约束，比较 rival explanations；当事人回忆保留回顾性质 | 单靠获奖后采访断言内心动机 |
| **某群体中有多少人如此选择？** | 可定义起点、时间窗口、覆盖率的完整/概率抽样与可观察分母 | 用 5、20 或 100 个媒体人物当比例样本 |
| **中国更严重还是美国更严重？** | 统一职业定义、era、收入/家庭/职业阶段、公开度与未公开缺失；可比队列与选择机制 | “中国几个反例+美国几个成功”计算国别差 |

已有 CASE-059 / 061 / 062 / 046 是很好的一手机制档案；**对频率问题，它们没有有效分母**。

## 二、不要把 collider 选择伪装成证据累积

简化变量：
- `A` — 作者性持续/独立问题定义能力；
- `F` — 雇佣岗位与旧组织目标函数暴露；
- `R` — runway / 家庭/社会网络；
- `Y` — 独立项目得到成功/市场承认；
- `V` — 媒体曝光/被访谈；
- `S` — 被我们纳入人物库。

示意：

```text
A ──→ Y ──→ V ──→ S
│             ↑
└────────────→ V
R ──→ Y ──→ V
F ──→ A ?  / Y ? / V ?
语言、媒体关系、发行商、公关、地域 ──→ V
```

当我们只分析 `V=1` 的明星采访，又以 `Y=1` 的创业成功者为主，便可能在人群中制造、放大或反向扭曲 A/F/R 之间的观察关系。是否构成严格 collider bias 取决于具体因果图；至少明确存在 **selection on outcome / media visibility** 风险。

不能凭媒体案例计算：
- 大厂校招对作者性的破坏率；
- “作者线程”在不同国家的总体普遍程度；
- 离职创业者整体成功率；
- 名校绩优者与非名校的平均创新能力。

即使 100% Case 研究都准确，**非代表性样本上的整体结论仍然可能错**。

## 三、在可观测现实中重建分母：三层不同的 frame

先写清研究目标人群，不能把几个分母相加。

### Frame A｜雇员队列（最接近“教育/大厂是否改变一个人”的问题）

起点：某国家/地区、特定年份入职的具体岗位人群，或名校相关专业的毕业 cohort。

按固定窗口观察：
- 进入公司前是否已经有作者 artifact；
- 任职期是否持续发布；
- 是否离职/尝试创作；
- 原型、发售、转回就业、仍在职；
- 各阶段 `UNKNOWN / UNOBSERVABLE`。

**困难：** 完整名册、私人创作、未来职业轨迹通常不可公开取得。公开校友名单、GitHub 贡献、公开 jam 记录、作品 credits 也有强烈自选偏差。**如无法获得较完整 frame，就明确写 `EMPLOYEE DENOMINATOR UNKNOWN`，不宣布任何发生率。**

### Frame B｜公开独立项目发起队列（较可行，但不回答所有雇员）

起点可以选择明确年月/规则截面的 **itch.io game jam、Kickstarter 游戏项目、Steam 已上架作品、地方公开 grant 申请/获奖公告（注意完整申请者通常不可见）**。

此时分母只覆盖“已经留下某种公开痕迹的尝试”，而非所有有意向创业的大厂员工。

- Kickstarter 全体 campaign（含未达标）、游戏 jam 所有参赛项目，比“成功 KS”好；
- Steam **发售队列**包括销量弱的小作、但天然排除没发售/没上 Steam 的尝试；
- 初期原型/报名队列优于发售队列，但 private abandoned projects 仍可能漏掉；
- 只能追溯公开认证的就业/学校背景，不可推断没有公开写出背景的就是“非大厂”。

分类：`PUBLIC ATTEMPT COHORT`，所有率的分母只在该 frame 内有效。

### Frame C｜媒体报道队列（我们现有 62 Case 的主要问题）

起点：媒体与一手开发者复盘、游戏展会、公开传记和用户兴趣。

用途：**机制发现、人物传记、决策链复盘**。

限制：不能推断总体发生率、国别差异或“典型从业者”的概率。

失败案例也应记录 `MEDIA-SAMPLED FAILURE`，不是自动的随机对照。

## 三点五、Frame D｜入学/就业之前已被家庭与学校筛掉的潜在创作者

前述 A/B/C 三种队列仍然从雇佣、公开项目或采访者出发，而 **家庭门控可能早在高中兴趣、大学专业志愿、课堂选课、首次游戏原型之前发生**。因此新设独立起点 **Frame D — PRE-ENTRY INTEREST / ATTEMPT COHORT**，只作为研究方案，不冒充已经拥有的数据库。

- **D1 意向/报考前队列**：某时段高中生、大学新生、职业培训意向者自愿报告对游戏制作/游戏专业兴趣及志愿，在最终选专业之前采集。记录实际未申请、家庭否决、临时改专业者；必要时与艺术/计算机等相邻兴趣组比较。
- **D2 前作品社群队列**：同一公开游戏制作课程、mod/地图工具课、校园社团/作品比赛的**所有入门者**，记录报名、练习、作品未完成、转向和发售，而不是只有优胜者。
- **D3 职业近失队列**：能核实游戏行业岗位、实习、playable prototype、offer，但最终未转行/未入职的人；父母反对与薪资、迁移、行业风险、房贷、照护、本人意愿一起编码。
- **边界**：D1/D2/D3 是不同分母，不能合并为“多少中国人被父母阻碍”。未获得本人自愿匿名调查/完整起点名单以前 `DENOMINATOR UNKNOWN`；观察“无公开作品”不等于没有私下创作。

**来源**：[Family Gate 029](family-gates-game-creator-us-china-029.md)、[梁其伟2014第一人称中断复工研究 030](family-gate-china-near-miss-liang-qiwei-030.md)；[张兆弓2022访谈](https://www.sohu.com/a/555164638_118576)明言该校只能见到已经与父母完成专业志愿沟通者，真实有异议却未申请者系统性缺席。梁其伟属于 **RECOVERED NEAR-MISS / MEDIA-SELECTED**，不能用他估计永久未出发者占比。

## 四、分层取样的可执行最小方案

研究“名校—大厂绩优主义是否导致独立操作变形”，下一批不再用搜索词“successful ex-AAA indie founder”。

**Step 1：预先选取起点而非结局。** 例如明确时段（2014–2020）、角色（gameplay programmer / design / production / QA）、中国和美国各至少一种公开项目起点；保存抽样规则、总体可观察条目数及链接。具体年窗仅为示例，须依可获得的数据决定，不追溯选择“恰好出了明星”的 cohort。

**Step 2：先记录全体可见条目，再决定深入案例。** 尽可能不依商业表现筛选：失败 KS、低评价/低销量发布、无人报道原型、后来停更的作者都要登记。筛选依据记录为机械的纳入条件而非“有故事价值”。

**Step 3：先做缺失性审计。** 公开作品是否可核校友/雇主来源？如果“无记录”很多，说明该组只能研究作品命运，不足以研究大厂员工命运。记录 `career_provenance_observable`，不得把 UNKNOWN 视作否定。

**Step 4：横向四格 + 沉默者。**
- 被报道成功；
- 被报道失败；
- 有公开原型/作品但无媒体人物专访；
- 有学校/岗位背景但未发现任何公开作者产物（`NO PUBLIC ARTIFACT OBSERVED` ≠ `NO AUTHORSHIP`）。

**Step 5：既有 Case 是 purposive mechanism sample。** Mega Crit / Supergiant / Sandfall / 王妙一 / The Magic Circle 可以作为解释具体转型的深描；另建 uncelebrated comparison frame 后才讨论分布。

**Step 6：必须承认外部可见性的国别差异。** 语言、媒体报道生态、保密协议、版号/发行制度、公开作品渠道、失败耻感、招聘与校友档案的开放程度本身不同；可能使美国故事更容易被观察到。**这既不能直接证明国内作者性更弱，也不能证明其真实差异不存在。**

## 五、固定的六项样本出处字段

后续每项跨人群研究在 Research Note / Cohort Ledger 中（不是个人隐私数据库）记录：

```yaml
target_population: "who exactly counts"
sampling_frame: "who could have been observed before outcome"
unit_of_analysis: "person / project / studio, never silently mix"
selection_rule: "when, where, inclusion/exclusion"
visibility_tier: "MEDIA_FEATURED / PUBLIC_UNFEATURED / INSTITUTIONAL_RECORD / UNKNOWN"
outcome_and_missingness: "success/failure/nonlaunch/censored, UNKNOWN tracked"
```

若没有稳定总体索引，附 `denominator_status: UNKNOWN`。

额外建议：
- `source_era` / `source_language`；
- `first_public_trace`；
- `career_prehistory_observable`；
- `interview_after_success: yes/no/unknown`；
- `failed/unreleased_projects_traceable`；
- `coverage_reason` 与 `why_this_case_was_selected`。

**媒体采访数量不是作者数量；报道来源不是统计单位。**

## 六、现有案例的纠正示范

| Case | 目前为何能观察到？ | 能回答什么 | 不能回答什么 |
|---|---|---|---|
| CASE-059 Mega Crit | 成功产品/创始人采访 + 早期 2017 采访 | 同一合作关系、作者喜好与部分职业能力如何延续；较早采访可减轻后见之明 | Amazon 或西方员工整体能保留作者性的概率 |
| CASE-061 Supergiant | 成功《堡垒》/GDC/官方回顾 | EA 技能怎样转化为七人作品；家庭场地/收入支持如何降低 burn | EA 老兵通常会离职且更容易原创成功 |
| CASE-062 Red Hook | 获得声望的产品/融资回顾 | 成熟工业能力与房贷/育儿风险如何并存 | 多数有孩子/房贷者创业结局如何 |
| CASE-046 Sandfall | 2025 爆款与事后高能见度采访 | 从在职原型→伙伴组合→公司化的已披露路径 | Ubisoft 中常见何种独立作者能力 |
| CASE-048 The Magic Circle | 失败被公开，且受访者/媒体能提供复盘 | 成熟 AAA 专家退出后，也会面临市场不足 | 普通未成名失败者的代表性 |
| CASE-054 Limit Theory | 长期 KS 与公开停更/取消记录 | 技术能力捕获某些游戏 scope 的具体机制 | 工程型创作者整体失败率 |

**这一行表是 retrospective methodological annotation，不是对 62 Case 逐案统计取样等级。不得声称已经完成全面分布校正。**

## 七、媒体之外的第一批可用证据接口（只支持各自适用的总体）

- **GDC 2026 State of the Game Industry**：调查 >2,300 名回应者，多岗位多行业角色；可用于描绘**样本受访者**的裁员/就业压力（其中 28% 表示两年内遭裁员），但自愿回应不等于全行业概率，也不能作为“大厂作者性连续率”的分母。
- **Game industry project-cohort quantitative study**：Szatmari、Deichmann、van den Ende（2025）的电子游戏行业组织研究曾从 22 家组织的 **6,041 项 PS2 项目**构造基础记录并对选择机制做稳健性检验。它不是我们问题的直接答案，而是一个“研究取样应从完整可定义项目队列而非十个成名采访开始”的方法示范。
- **Case study methodology**：Widner（2022）强调精英访谈的取样/范围边界；观察机制与代表人群是不同任务。
- **Collider / selected cohort methodology**：文献表明对被选中的样本条件化可制造看似真实的相关性；应先画选择过程而非反复比较明星。

Sources:
- https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/
- https://journals.sagepub.com/doi/abs/10.1177/14761270241271021
- https://www.cambridge.org/core/books/case-for-case-studies/descriptive-accuracy-in-interviewbased-case-studies/5A2722EFDEF1F485BD28EE1FE47543E7
- https://www.bmj.com/content/381/bmj.p1135

## 七点五、2026 GGJ官方自愿问卷以及2027旧站退出：分母与证据保全有新约束

新研究 [038](ggj-2026-survey-and-archive-denominator-038.md) 对2026-04-13 GGJ调查、2026-07-03官方归档公告与2026-06-19 Springer一站点15人长时访谈进行逐层取样审计：
- GGJ 2026最终报告中**39,197名参与者、9,874项游戏提交、3,535份自愿答卷（约9%响应）**是三种不同单位。答卷里37%学生、28%hobbyist等只能描述响应者的自我定位；被家庭/学校限制到从未报名者根本不在分母中。
- 15人曾经参与Jam的多年后质性访谈适合理解“有些人参加Jam就是为了社交、学习或业余创作”，但受自愿应答与站点选择影响，不是职业转型率或亲子认可率估计。
- GGJ已宣布逐步结束**V3旧站2014–2023作品文件**的长期公开提供：官方同一公告叙述称2027-03-31结束、末尾关键日期表称2027-02-28结束下载/03-01下线，时间矛盾未解决，按较早2027-02-28谨慎安排素材目录核验。**2024深圳南山GGJ站属于V4，不受这次V3删除直接波及；2022 Week Sauce使用itch.io不是GGJ网站。**
- 已参加的人与根本没机会参加的人需要不同frame，公开metadata保全又与本人游戏资产授权/隐私两回事。绝不能为完整“分母”私自批量收集他人家庭经历或复制游戏程序。

同轮[039 加拿大Giguère与越南SOGA](ordinary-indie-household-runway-two-hits-selection-039.md)说明即使主动添加“失败者”，我们往往仍只抓到愿意公开财务失败博客、或第二作成功以后才愿意追忆家人的人。**形象鲜明的失败故事也是经过筛选的故事**，不能直接弥补公众队列的比例问题。

## 八、在没有分母以前，研究结论应该怎样写

**允许：**
> 可以观察到一些工业游戏从业者保持并发展独立作者线程；但我们主要通过媒体和开发者自述发现他们，不知道这在人群中多普遍，也不知道各国是否存在频率差。

**不允许：**
> 美国大厂不太影响创造力，中国大厂让多数优秀员工失去作者性。

**允许：**
> 大厂声望可能带来使项目过早扩大规格的动机，这是个值得检验的机制；目前个案因访谈可见性偏差，不足以断言整体趋势。

**不允许：**
> 明星独立游戏开发者普遍不在乎原公司身份，因此规训可以靠勇气摆脱。

对于本书更重要的转向：

> **人物故事回答“如果发生，这条路是怎样走通/走不通的”；不预设“普通读者有多大机会走这条路”。**

## 九、下一批研究的优先级（不是盲目扩明星案例）

P0：建立第一份 **PUBLIC-ATTEMPT / PUBLIC-UNFEATURED** 小型可复查 pilot，先验证是否能观察到就业史，不直接做跨国胜率。

P1：找“公开小项目却从未接受人物报道”的欧美与中国开发者；确保同岗/同年代而非两组榜单上的明星。

P2：拆分 NO PROJECT / PRIVATE UNOBSERVED / CANCELLED / SHIPPED / RETURNED TO JOB 等退出状态；不能只看仍可售项目。

P3：有合理共同 frame 之后才建立国别对比；样本缺失严重就永远停在机制层，不把差异写成统计结论。
