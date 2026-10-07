# 007 — 不以 CUSGA 为唯一主样本：在职作者性、个人项目与产业选择的研究主线重排（2022–2026）

- Program: C / 中国教育 × 行业版本 × 社会版本意识
- Status: **SAMPLING-PIVOT / PRIMARY-SOURCE COMPARATOR AUDIT / CHINA EMPLOYEE DATA GAP OPEN**
- Audited: 2026-10-07
- Related: [005 CUSGA2024](005-cusga-2024-submission-to-finalist-frame.md) / [004 中传课程—就业](004-cuc-creator-training-to-career-cohort-gates.md) / [003 upstream non-entrants](003-nonentrants-upstream-cohort-and-survey-selection-audit.md) / [028 denominator protocol](../../book/research-notes/media-selection-survivorship-and-denominator-protocol-028.md) / [Creator Visibility Sampling Gate](../../schemas/creator-visibility-sampling-gate.md) / [AC-010](../../author-corpus/AC-010-prestige-pipeline-coupling-and-authorial-continuity.md)
- Scope: **公开国际地区从业者调查、活动/项目者公布的匿名聚合数据、可审计研究设计**。私人游戏项目或用户个人经历不作为公开研究来源。
- **Core correction:** 2024 CUSGA 的「初赛75入围」经过作品报名、完成和评审三次选择，即便核齐75项，也**不能回答在职员工有多少在做个人项目、多少原本有创作意愿而没有尝试**。研究问题先于样本；不把“最容易搜到的名册”升级为主线。

## 2026-10-07 样本策略第二次修正（证据升级）

[009 中国游戏雇员劳动田野](009-china-gameworker-creative-subjectivity-fieldwork-2017-2026.md)已找到比此前欧美一般自愿问卷更**直接针对中国游戏员工在岗作者性**的国内研究：2017美术5人访谈、2019上海网络游戏员工访谈、2026《社会》**42位策划/程序/美术+18个月田野**，并发现员工利用**升迁、业余项目**回应组织模块化对创作主体性的片段性调用。因此 `CHINA_EMPLOYEE_AUTHORSHIP_EVIDENCE=QUALITATIVE_PRESENT`，不再只是 `NONE`。

但上述研究都**不是面向中国游戏雇员全体的概率抽样或同人纵向普查**；`CHINA_GAME_EMPLOYEE_PRIVATE_AUTHORSHIP_PREVALENCE=UNKNOWN`。正式行动顺序改为：**现有田野深入阅读→明确具体工作权利与旁路原型→设计概率/可审计雇员纵向调查**。CUSGA学生决赛名册依旧P2辅助，不因新文献而回升为主样本。

## 0. 重新裁决样本：研究问题不同，最优入口也不同

| Question | Most appropriate entrant frame | Existing access/evidence | Priority / gate |
|---|---|---|---|
| **A. 在职作者性是否留存？** | 特定城市/组织/岗位/入职年代的**雇员名册经授权匿名问卷**，同时问工作内 decision rights 与业余创作 | **瑞典 Game Habitat 2022/24 雇员渠道问卷、InGame Job 2024/25 欧洲匿名问卷**为测量先例；中国同口径且覆盖雇员分母 **UNKNOWN** | **P0 / 第一主线**：先补现有国际实测与中国能否取得合法 aggregate，而非追名人 |
| **B. 有意愿为何未试作/未创业？** | 从就业/学校/职业届别定义的**整群调查**；包括没有创业兴趣、做私人原型、在大厂任职、已退出者 | 瑞典从业者直接问 **是否想开自己的工作室**；中国中传导师访谈无法替代全员问卷 | **P0 / 第二主线**：意愿—实际项目—风险—岗位权利分开 |
| **C. 上游家庭/学校是否抑制形成？** | 早于游戏专业报名的年龄/学校整体抽样 | CEPS 学生基线；家庭门控029 | **P1**：不从游戏专业录取者倒推未报考者 |
| **D. 已公开小作品是否继续？** | 固定年份**全部投稿**的 game jam / competition / Steam cohort | GGJ 深圳 2024目录16 listing, CUSGA 2024主办者称500+投稿而只发布75初赛入围 | **P2 辅助**：所有75入围题名核齐有档案价值，但**不是必经、不是优先于A/B** |
| **E. 一次职业与产品抉择如何发生？** | 有同期材料的自愿公开人物/团队传记 | 《鼠鼠来了》→《浣熊推币机》006 等 | **机制案例**，不产生任何发生率 |

**最重要的未覆盖者**：`EMPLOYED_PRIVATE_AUTHOR`（在职持续自发做项目但不公开）、`EMPLOYED_WANTS_TO_CREATE_BUT_CANNOT`（有意愿却无时间/权利/资源）、`EMPLOYED_DOES_NOT_WANT_TO_CREATE`（合理偏好公司内职业与稳定工资）。作品平台和 CUSGA 获奖名录都不能捕获这三组；前两组不能靠猜私人 GitHub、LinkedIn 或家长身份补洞。

## 1. 瑞典南部：直接向雇员问「想不想开游戏工作室」

**Game Habitat, *The South Swedish Game Development Industry 2024*, 2024-11-19；调查 2024年5–6月，地点 Skåne/Blekinge。**

### 同一地区不同来源的两类分母

- **产业行政/公司报告侧：** 2023年底 168 家游戏公司、合计 **1,767 位员工**，自企业年度财务/注册材料汇总。这个是地理产业体量估计，**不是回答问卷的人数**。
- **雇员意愿问卷：** 经当地游戏企业**内部渠道**分发、匿名自愿填写，2024 年答卷 **325人**（2022年 **209人**）。报告明确 **NO probability sampling method**；问题可跳过，创业意愿题图示2024年回答共 **321人**（75+92+131+23）。
- 2024创业意愿问题原文：**Would you like to start your own game studio in the future?**。四项结果：**Yes 23.4%（75人）；Maybe 40.8%（131人）；No 28.6%（92人）；Already started 7.2%（23人）**。2022回答者Yes 24.4%、Maybe 43.0%、No 24.9%、Already 7.7%；**2022/24不是同一批雇员纵向追访**，不能称个人意愿是否变化。
- 报告也收集工作/薪酬、为何选择工作室、为何留在地区、对当地创业支持的需求，但**没有直接询问个人游戏原型是否持续制作**，所以不等于「有23.4%的人正在创业」。`Yes` ≠ `CURRENT_PROTOTYPE`；`Already` ≠ `SHIPPED_STUDIO`。

**重要的正反两面：** 有一个员工渠道问卷可以在同一区域合法匿名触及大公司和小公司在职者，而不先筛项目发表。但真正答卷者仍是自愿人群，不是全地区雇员随机样本。瑞典问卷不能推出瑞典全国创作者意愿率，更不能无匹配中国样本时计算国别差异。受访者国籍有77种：**工作地点在瑞典不代表“瑞典人天性”**。

Source P0:
- Game Habitat official press, 2024-11-19, https://gamehabitat.se/news/the-games-industry-in-south-sweden-continues-to-grow/
- Game Habitat, *The South Swedish Game Development Industry 2024*, pp.31–32 (创业意愿图/方法) & p.4/7（地区公司及人员），https://pub-5eff4704c94a411a8332d60a707c554e.r2.dev/media/industry-report-2024.pdf

## 2. 欧洲在职者不等于零自发创作：2024与2025的 Pet Project 实测

### InGame Job / Values Value, 2024春调查（作者于2025年3月公布）

InGame Job CEO Katya Sabirova 在 *PocketGamer.biz* 2025-03-05 专稿提供其调查项目一手解释：**超过1,800位调查参与者**中，**接近40%自报有业余个人项目**。她又按 EU+UK+Swiss 与非EU欧洲国家查看程序、设计、美术等岗位的分布；讨论了业余项目、eNPS、额外收入、工作与创作动机，举出直接参加采访的在职项目制作者。

**限制：** 该项目来自招聘平台及自愿答卷；参与者偏向关注职业发展者，且“个人项目”不必然是独立可售游戏，游戏制作和职业外包、技术实验、非游戏软件须由原题明确区分。该文章引用项目负责人自己的相关/解释性判断，**eNPS差异不是组织压抑作者性的因果证明**；文内三名主动受访者仍是媒体选择。

Source P1? 更精确：调查组织者原作者自述属于调查方法/自身材料 **P0/organizer explanation**；对动机的解释仍为 **H**。Katya Sabirova, *Who has pet projects in the games industry and what drives them?*, *PocketGamer.biz*, 2025-03-05, https://www.pocketgamer.biz/who-has-pet-projects-in-the-games-industry-and-what-drives-them/

### InGame Job / Values Value, Big Games Industry Employment Survey 2025

- 2025-03至06 **1,650份答卷、来源85国**；但其74页正式PDF明确说明**分析只使用欧洲地区数据**，将 EU+UK+Switzerland 设为 **709名**，非EU欧洲（包括亚美尼亚、白俄罗斯、格鲁吉亚、摩尔多瓦、波黑、黑山、北马其顿、塞尔维亚、乌克兰）设为 **543名**。
- 报告摘要 **41% have a personal project on the side**；这是**调查参与者/欧洲分析口径的摘要结果**，但报告没有在摘要旁给出此题精确 `N_answered`。不能误写为「在全球所有1650人或欧洲所有1252人当中，精确有41%」，更不能写「斯拉夫民族中41%」。正式量化需向研究方核原题定义、筛选方式与答题分母。
- 正文 p.58(图) 按职类和 EU/非EU 组给 pet project 分布（例：EU区程序岗位**60%**、非EU区程序岗位**78%**；EU区游戏设计岗位**59%**、非EU区游戏设计岗位**48%**）。**这些是该职位、该地区、在答题样本中的描述比例**，没有各单元具体 N 和随机抽样，不能据差值推欧洲立法或民族文化因果；小样本/就业结构/项目类型/地区混杂很大。
- 报告还问 freelance + side projects，但 `FREELANCE`（副业收入）与 `PERSONAL_CREATIVE_PROJECT`（自发创作）不同；哪怕“无薪私人实验”也应计入后者，不能仅追兼职工资。
- **严禁将报告的「非EU欧洲」直接译为「斯拉夫国家」**：该分组混含南高加索国家等，且没有俄罗斯参与者。也不能把这个样本与中国行业从业者对照宣称总体比例高低——**中国等同定义调查尚未找到**。

Source P0: InGame Job & Values Value, *Big Games Industry Employment Survey 2025*, pp.2–4 methodology, p.58, 2025, https://investgame.net/wp-content/uploads/2025/11/Big_Games_Industry_Employment_Survey_2025.pdf
P0 publisher 2025-12-09 announcement: https://boost.ingamejob.com/the-results-of-the-big-games-industry-employment-survey-2025-are-out/

### 「拥有个人项目」/「想开工作室」/「做兼职」三个率不可比较

- `PET_PROJECT`：不一定是游戏、不一定为了发售、不一定属于本人原创定义；
- `FOUNDER_INTENTION`：想法/选项，并非已开始；
- `PAID_SIDE_GIG`：为收入的额外劳动，可能与作者性无关；
- `GAME_AUTHORSHIP`：**过去12个月本人实际提出/修改自主问题和玩法，并做过可指认的原型/试玩/机制判断**，无论是否公开。这才贴近研究核心。

对照：GDC 2025 salary survey 所称「约11%受雇开发者做额外有偿工作」有另一种定义，**不能据此说欧美在职个人项目只有11%**。相反 InGame Job 2025的41%也不能推翻11%——两者不是同一个被解释变量。

## 3. 不要用瑞典「被帮助创业」的项目宣传伪造对照实验

Game Habitat 于 **2026-06-15**公开了 **Launchpad** 项目回顾：2025-11至2026-05，针对当地遭裁员及职业转型的开发者，提供免费的办公空间、简历/作品集建议、企业匹配、联合创始人对接、行业讲座、活动门票、社区支持；由 Skåne Region 和 Malmö 市支持；**213人参与项目、23场活动**。

其后仅 **44名参与者**回答 2026年6月问卷；组织者披露 **18%获得新职位、21%创立工作室**。**应精确读成「回访问卷应答者/项目方所报告的状态」**，不能当作213名参与者中21%都创立公司；无未参加 Launchpad 的对照组、原创业意愿/基线变量和未答者资料，**不能把21%解释为 Launchpad 的因果效应**。即使成立公司也不等于有可持续游戏产品。

它有价值地证明的是**一种公开存在、可拆解具体内容的区域制度措施**，而非制度有效性的严格估计。把它放在“支持的供给形式”考察：现金/办公/伙伴网络/会议/联合创始人/风险过渡，而非将单个资助成功者讲成普遍适用的瑞典秘诀。

P0 Game Habitat, *Strong results in concluded Launchpad*, 2026-06-15, https://gamehabitat.se/news/strong-results-in-concluded-launchpad-many-got-new-jobs-and-founded-new-companies

### 3.1 国内旁路证据与制度边界：2026-10-07 后续公开审计

新 [008 — 中国在职旁路创作与软件职务权利](008-china-worker-side-creation-open-source-and-ip-gates.md) 已核到：开源社2024原始报告 **631份自愿答卷**，能观察真实开源使用/社区贡献和贡献者投入时间；2023《中国独立游戏从业者生存现状调查》的公开招募**尚未核得结果**；澎湃2025独立游戏线上社群**6人深访**可用于解释资金、团队和发行约束；司法部2013软件职务著作权条例与2025最高法《劳动争议解释（二）》给出有条件的权利边界。**这些都不是中国在职游戏员工的私人游戏创作发生率**。

该后续研究提出 `SAME_RESPONDENT: TECH_SIDE_PROJECT vs GAME_SIDE_PROJECT` 的中国境内配对观察，不强求先找到一份和欧洲“pet project”字面一致但抽样不同的问卷。需要区分法律赋权、具体合同、员工对规则的主观了解、实际许可/执法，而不是把没有Steam作品解释为竞业约束导致的沉默。

## 4. 本轮对中国同口径调查的公开检索结果

截至 2026-10-07，本轮按中文/英文组合检索：`中国 游戏从业者 个人作品/业余项目/pet project 调研`、`游戏行业 职业发展 问卷`、`游戏设计毕业生 去向`。发现2024中国游戏产业报告、人才/岗位相关文章与多个**网上问卷模板**，但**没有核实到一份既公开原题、能辨认回复者招募/缺失、又报告「在职个人原型/作者决策权」的中国从业者同口径测量**。

这**不是证明中国没有在职私人作者群体或没有任何同类调查**，而是此次检索范围内的**数据可见性缺口**。`NO_MATCH_THIS_SEARCH` 不等于 `NO_CHINA_DATA`。中国官方《2024年中国游戏产业报告》报告市场规模/海外收入，但不应拿行业收入和利润份额冒充研发人员个人创作率。

来源：
- 中国音像与数字出版协会游戏工委，2025-01-17披露《2024年中国游戏产业报告》，https://www.cadpa.org.cn/3277/202501/41718.html 。**市场收入不是创作者人数**。
- IGDA & Western University 2023 DSS（官网报告2024发布），公开问卷覆盖职业人、学生、独立开发者，不是概率雇员名册，https://igda.org/dss/ ；即便英文材料丰富，也不能与瑞典雇员内网问卷当同一覆盖率。
- 商用问卷模板网站未确认真实开展调查、样本与结果；**禁止入证为中国从业者事实**。

## 5. 真正值得试验的匿名员工问项（不是已做调查）

抽样起点先固定**受雇公司/行业/届别/工作岗位类别/就业年份**，经合法接入把同一调查邀请送给**有作品与无作品、想创业与不想、已经离开的人**。优先通过官方协会/受雇公司自愿渠道、具有隐私保护与可信机构中介的匿名聚合；不能自己网搜并联接员工实名账号。

必须至少分六个独立变量：

1. `PERSONAL_DESIGN_INTENT`：过去一年是否**想自己做游戏/自定玩法问题**（no/yes/unsure/decline）；
2. `PERSONAL_ATTEMPT_LAST_12_MONTHS`：是否有纸面方案、修改器/mod、可玩原型、和他人开发；自主定义与雇主指派分开；明确包括**仅私人未公开**；
3. `PROJECT_FORM`：GAME / GAME_TOOL / UNRELATED_CODE_OR_ART / OUTSIDE_PAID_WORK；`pet project`有时非游戏，防止误计；
4. `DECISION_RIGHTS_AT_WORK`：本人是否有题材/玩法/原型方向提出权、砍scope权、否决与验证权，是否可挑战目标函数；分岗和职级核；
5. `FEASIBILITY_AND_RESTRAINT`：合同 IP/竞业规则是否清楚、可用时间/住房/现金缓冲、是否有长期同伴、家庭与雇主是否有权限制、想做但不做的**多选原因**（包括没兴趣/优先工作/健康/照护）；
6. `CAREER_PATH`：在职、已离职、计划转型、曾暂停、何时又开始；只有有授权可回访才允许做匿名纵向关联。

按 `NO_INTEREST`、`INTEREST_NO_ATTEMPT`、`PRIVATE_PERSONAL_ATTEMPT`、`PUBLIC_PERSONAL_ATTEMPT`、`EMPLOYED_STUDIO_AUTHORSHIP`、`PAID_SIDE_GIG_ONLY`、`UNKNOWN/REFUSED` 区分描述，**禁止用无 Steam 作品=无作者性**。

即便得到中国与欧洲的相同问卷，仍必须处理取样来源（企业内网、招聘平台、大学、jam）、工作强度、岗位、年代、受访语言、收入等差异；设计假说和模型可以先建立，**国家间总体频率仍 UNKNOWN**。

## 6. 正式优先级修正及出口

**P0 完成**：已经取得并审查：
- South Sweden 2024 employee report 的**原始创业意愿问题、321答题人数与2022/24交叉年度口径**；
- 2025 InGameJob 的**问卷区域分析样本、正式 pet project 职位图与摘要41%的缺失分母**；
- 2026 Launchpad 的**参与人群与小规模自愿回访的张力**。

**P1 下一项：** 面向中国仍先寻找或获得**能够接触在职人员的合法机构/公开调查**，不是先追75个已入围创作者。取得资料后首先核「是否问到私人项目」与缺失，未达标则承认 `CHINA_EMPLOYEE_AUTHORSHIP_DENOMINATOR=UNKNOWN`。

**P2 辅助：** CUSGA 2024 的75个入围是**已完成作品、受过评选**的便利项目 cohort；可自成外部公开轨迹审计，但不构成P0主线依赖条件。若不发生新的主动研究需要，不再无限增加 contest roster。

**P3 书稿形态：** 以“雇员在公司里有强执行力，与回家后能否仍自主造物是两个维度”为问题；让欧洲问卷提供可问的具体维度，让中国材料回答何种产业制度使其难以被测/转化，而不是生搬欧洲百分比讲「老中劣等」。

### Editorial warning

- `INTENT ≠ ACTION`
- `PET PROJECT ≠ GAME PROJECT`
- `EMPLOYMENT ≠ LOSS OF AUTHORSHIP`
- `STARTED STUDIO ≠ SHIPPED GAME`
- `VOLUNTARY SURVEY ≠ NATIONAL WORKFORCE`
- `CURATED FINALISTS ≠ SUBMISSION COHORT`
- **被纳入我们研究项目的路径，必须独立于希望得到的结果。**
