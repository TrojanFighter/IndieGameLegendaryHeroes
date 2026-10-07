# 044 — 失败以后去哪里：Creator Exit & Re-entry Economics 第一轮

- Status: **TARGETED LIFE-OUTCOME EVIDENCE / CONVENIENCE COUNTERCASES / NOT A POPULATION RATE**
- As-of: 2026-10-08
- Routes: OQ-002 Second Attempt / OQ-005 Authorial Right vs Salary / OQ-006 Failure Reversibility
- Parent: [人生性价比的第一份硬账](creator-life-cost-exit-comparison-2026-10-07.md)
- Sampling boundary: 本轮主动寻找公开写下“退出全职独立、回受雇、转行业、法人死亡、后来再入场”的第一人称或直接工作室记录，因此**不能用来计算发生率**。它解决的是 outcome taxonomy 和机制缺口，不是 denominator。

## 0. 为什么“第二款游戏”仍然不是我们真正想知道的答案

Steam 的第二次发行基线已经告诉我们：一个 developer identifier 有没有第二款产品，是有用的第一层平台观测，但它不能直接回答创作者的人生是否恢复。

失败以后至少可能同时发生：

- 项目停止，但人回到受雇岗位；
- 公司死亡，但成员很快找到新工作；
- 人继续做游戏，却从 full-time 退回 nights/weekends；
- 人离开游戏业，把部分能力迁移到别的数字职业；
- 多年后通过桌游、mod、小项目等旁路重新进入；
- 作品/IP/源码留下，但个人没有时间继续；
- 经济恢复了，但作者权没有恢复；
- 作者性延续了，但收入仍不足以再次全职。

因此需要把单一的 `SUCCESS / FAILURE` 改写成一个 **Exit Outcome Vector**。

## 1. Exit Outcome Vector

每个退出/失败样本至少拆成七项：

| 维度 | 建议状态 |
|---|---|
| PROJECT_OUTCOME | SHIPPED / CANCELLED / ABANDONED / HOBBY_CONTINUED / OPEN_SOURCED / UNKNOWN |
| COMPANY_OUTCOME | CONTINUED / DOWNSIZED / INSOLVENT / LIQUIDATED / NEVER_FORMED / UNKNOWN |
| EMPLOYMENT_OUTCOME | REMAINED_EMPLOYED / RETURNED_EMPLOYMENT / CAREER_PIVOT / STILL_FULLTIME_INDIE / UNKNOWN |
| AUTHORIAL_OUTCOME | CONTINUED_SIDE_CREATION / SECOND_ATTEMPT / MEDIA_SWITCH / PAUSED / EXIT_UNKNOWN |
| HOUSEHOLD_PRESSURE | PUBLICLY_OBSERVED / NOT_OBSERVED / UNKNOWN |
| RESIDUAL_CAPITAL | SKILL / PORTFOLIO / NETWORK / IP / SOURCE / AUDIENCE / NONE_OBSERVED / UNKNOWN |
| REENTRY_TIME | KNOWN / BOUNDED / UNKNOWN |

另外强制保留：
- `SALARY_BEFORE = UNKNOWN`，除非本人公开；
- `SALARY_AFTER = UNKNOWN`，除非本人公开；
- `FULL_FINANCIAL_RECOVERY` 不得由“找到工作”自动推出；
- `CAREER_EXIT` 不得由“项目没更新”自动推出。

## 2. 六条公开人生路径

### 2.1 Gianfranco Berardi / GBGames：回公司不是梦想死亡，而是风险阈值被家庭重写

Berardi 2022 年的年度回顾给出一条异常清楚的纵向链：

- 2010 年辞职，成为 full-time indie；
- 现金耗尽后，2012 年重新找 day job；
- 原计划是重新积累储蓄后再辞职；
- 结婚和家庭形成以后，他明确说自己的 risk assessment 以及家庭可接受风险改变了；
- 此后一直保留 day job，同时极低强度继续 GBGames；
- 2021 年他记录了约 299 小时游戏开发，但全年相关产品销量仍很低；
- 他甚至写了一份 Full-time Indie Plan，把当前工资、家庭预算、必要开支、销售与营销门槛放在一起比较。

这比“失败后还能不能再做一款”更有价值，因为它直接显示：

```
FULLTIME_INDIE
→ CASH_EXHAUSTION
→ RETURNED_EMPLOYMENT
→ HOUSEHOLD_RISK_THRESHOLD_RISES
→ CONTINUED_SIDE_AUTHORSHIP
→ SECOND_FULLTIME_EXIT_NOT_YET_TRIGGERED
```

**关键机制：`REEMPLOYMENT ≠ AUTHORIAL_EXIT`；同时 `AUTHORIAL_CONTINUATION ≠ SECOND_FULLTIME_ATTEMPT`。**

Sources:
- Gianfranco Berardi, “A Review of My 2021, and Looking at 2022, Already In Progress”, 2022-01-17: https://www.gbgames.com/2022/01/17/a-review-of-my-2021-and-looking-at-2022-already-in-progress/
- GBGames press/about chronology: https://www.gbgames.com/press/

### 2.2 CJ Cenizal / Atomic Armies：残值不是“学到了很多”，而是哪些能力还能被劳动力市场重新定价

Cenizal 的自述比一般失败 postmortem 多了一段最重要的后续：

- 2010 年结束 visual-effects contract，主动进入独立开发；
- 两年里做了几个游戏、几乎没有收入；
- 同期关系进入结婚/未来住房等更高现金责任阶段；
- 到退出点时，他自己判断大量 social-game 知识、Flash / ActionScript 投入已经因技术和市场迁移而明显贬值；
- 他面试过 social game 公司和 Riot，但最后不想继续游戏职业；
- 真正幸存下来的不是“游戏开发者”这个身份，而是项目中发现并强化的 UI/UX 兴趣与能力；
- 后续约四年，他逐步建立起 UI engineer / front-end web developer 职业，并明确写到家庭账单重新得到支付。

因此 Residual Capital 必须进一步拆成：

```
RESIDUAL_CAPITAL =
  transferable_skill
+ portfolio_signal
+ network
+ reusable_asset
- obsolete_skill
- regime_specific_knowledge
```

Atomic Armies 反驳两种相反神话：
1. “失败了什么都没留下”——不成立，UI/UX 能力真实迁移；
2. “失败就是交学费，学到的东西最终都会值钱”——同样不成立，作者自己明确识别出部分技术栈和行业知识已经贬值。

Sources:
- CJ Cenizal, *Atomic Armies: A Post-Mortem*: https://www.atomicarmies.com/
- CJ Cenizal software portfolio: https://cjcenizal.netlify.app/

### 2.3 PONCHO / Delve Interactive：产品发售之后，CV 可以比下一份设计文档更早出现

Dan Hayes 的 postmortem 给出了从 day job 到债务再回就业的完整中段：

- 2011 起两位主创边上班边做 PONCHO；
- 2013 左右辞职全职开发，依赖储蓄并继续寻求 Kickstarter / 发行等资金；
- 为展会和继续开发承担较大贷款；后期又贷款以完成 Steam 版本；
- 2015-11-03 Steam / PS4 上市；
- 销售结果出来后，他们马上开始写 CV 寻找 day job；
- 一年后作者明确说他们已经在新的 day jobs 下继续做 Wii U / PS4 patch；
- 债务并未因为“重新就业”自动消失。

因此本案的正确编码不是：
`SHIPPED = SUCCESS`

而是：

```
SHIPPED
+ MARKET_INSUFFICIENT
+ DEBT_REMAINS
+ RETURNED_EMPLOYMENT
+ PRODUCT_MAINTENANCE_AFTER_HOURS
```

它还提供 OQ-009 的旁证：作者明确说有 publisher 并没有自动带来预期中的大型媒体覆盖，因此“签发行商”不能被编码成 `MARKETING_PROBLEM_SOLVED`。

Source:
- Dan Hayes, “PONCHO — A Postmortem”, Game Developer, 2017-01-06: https://www.gamedeveloper.com/business/poncho-a-postmortem

### 2.4 Mountaincore / Rocket Jump Technology：公司死亡、人重新就业、源码/IP残值是三条不同结局

Mountaincore 是本轮最干净的组织层退出样本之一：

- 前身 King under the Mountain 已长期开发；
- 后来 publisher funding 允许项目从单人 hobby 扩成小型全职团队；
- publisher 退出后，团队在很短营销窗口内进入 Early Access；
- 开发者明确说 launch revenue 远低于维持哪怕一名 full-time developer 所需水平；
- 2023 年团队停止全职开发，成员被裁；创始人的公开更新明确写到自己重新回 full-time work，且 commute 显著挤压开发时间；
- Rocket Jump Technology 后来因收入不足覆盖小额债务而 insolvency / liquidation；
- 2025 更新进一步确认剩余两位人员当时必须迅速找到新工作；
- Mountaincore 本体法律权属因 publisher funding 变得复杂，但前身 King under the Mountain 以及后来的 Mountaincore 最终都以开放源码形式留下。

这里至少有四个不同 outcome：

```
COMPANY = INSOLVENT / LIQUIDATED
EMPLOYMENT = RETURNED_EMPLOYMENT
AUTHORIAL_TIME = COLLAPSED_TO_HOBBY, THEN EFFECTIVELY_PAUSED
RESIDUAL_ASSET = SOURCE / CODE / COMMUNITY, PARTLY OWNERSHIP-CONSTRAINED
```

**法人死亡不等于劳动者失业多年；劳动者重新就业也不等于作品仍有可持续开发时间。**

Source:
- Mountaincore Steam developer announcements, 2023-05 to 2025-04: https://steamcommunity.com/app/2370310/allnews/

### 2.5 Tomislav Čipčić / Iron Cross → board games → Attack at Dawn：第二次机会可以跨媒介、跨很多年

Panzer Division Games 的 founder biography 提供一种与“失败后立刻再做第二款 Steam 游戏”完全不同的 re-entry：

- 第一款 Iron Cross 与朋友做了约六年，最终没有完成；
- 此后他把重心放回家庭和 day job；
- 创作并没有完全停止，而是转向 board games；
- 其中 Brotherhood & Unity 后来由 Compass Games 出版；
- 这成为其自述中的 tipping point，之后他重新“fully returned” to game design，并开始制作 PC wargame Attack at Dawn: North Africa。

所以：

```
UNFINISHED_FIRST_PROJECT
→ FAMILY + EMPLOYMENT
→ MEDIA_SWITCH / SIDE_AUTHORSHIP
→ EXTERNAL_VALIDATION
→ LATER_FULL_REENTRY
```

这说明 OQ-002 的 “Second Attempt” 不能把固定窗口内的 `SECOND_STEAM_APP` 当唯一结果。真正的作者性可能在桌游、mod、工具或其它媒介里保存，再晚很多年重新资本化。

Source:
- Panzer Division Games, “About Us”: https://www.panzerdivisiongames.com/about-us

### 2.6 Drunk Shotgun：保留主业可以把商业失败从“职业退出事件”降成有限实验损失

Alexey Strelkov 的 Drunk Shotgun 是很好的 control：

- 2019 年末开始 prototype；
- 几周后加入 Listenable 成为 full-time CTO；
- 游戏此后主要在 evenings / weekends / nights 完成；
- 他估算 1.0 约 50 个工作日，现金支出约 US$4,006；
- 截至复盘时总收入只有约 US$35.57。

这是极端商业失败，但因为作者没有把全部工资和职业身份押进去，它与 PONCHO / Atomic Armies 的人生后果完全不是一个类型。

正确比较不是：
“Drunk Shotgun 比 PONCHO 失败得更多/更少。”

而是：
**两个产品都可以商业失利，但 employment option 是否被提前行权，会改变失败的不可逆程度。**

Source:
- Alexey Strelkov, “How I wasted $4k+ and half a year of my life to develop a game that earned only $30”, Game Developer, 2021-01-04: https://www.gamedeveloper.com/business/how-i-wasted-4k-and-half-a-year-of-my-life-to-develop-a-game-that-earned-only-30

## 3. 第一轮比较矩阵

| 路径 | 离开主业 | 项目结果 | 失败后就业 | 作者性是否延续 | 可见残值 | 仍然 UNKNOWN |
|---|---|---|---|---|---|---|
| GBGames | 是 | full-time business 未达可持续 | 2012 回 day job | 是，长期 part-time | 技能、作品、业务学习 | 工资前后、完整净损失、何时能再全职 |
| Atomic Armies | 是 | 未形成可持续业务 | 转 UI/front-end 新职业 | 游戏作者身份未作为主业延续 | UI/UX、产品开发经验、关系 | 精确收入损失、再就业工资 |
| PONCHO | 是 | shipped / sales insufficient | 已回新的 day jobs | 至少短期继续维护 | shipped title、技能、publisher/platform经验 | 各成员长期去向、债务最终清偿、工资 |
| Mountaincore | 从 hobby 扩为全职 | EA商业不足 / 后续停摆 | 成员快速再就业 | full-time停止；hobby尝试后近乎暂停 | source、社区、部分IP/代码 | 个体工资、长期作者重返、完整publisher合同 |
| Iron Cross | 未明确 | 约6年未完成 | day job / family | 通过桌游保存并后来重返 | 设计能力、board-game validation | 精确时间窗、财务、首次项目投入 |
| Drunk Shotgun | 否；开发期已有 CTO 主业 | shipped / 极低收入 | 不需要“回归” | 可自由决定后续 | shipped artifact、学习、职业工资仍在 | 总工时、机会成本、税后损失 |

这张表仍然**不是统计样本**。它只证明“失败以后”至少存在多种可观测路径，足以推翻把 `NO SECOND_GAME`、`STUDIO_CLOSED`、`RETURNED_TO_JOB` 当同一个状态的做法。

## 4. 从这六条路径能提炼什么，不能提炼什么

### 4.1 可以暂时成立：就业回撤能力是一种真实的生产资产

在独立开发前保留或积累的职业能力，不只是“机会成本”。

它同时可能是一张 **exit option**：

```
marketable external skill
→ lower expected downside of indie attempt
→ easier employment return
→ household solvency restored
```

但这不是“程序员失败也无所谓”。

PONCHO 显示债务可以在重新就业后继续存在；Atomic Armies 显示技术栈会贬值；Mountaincore 显示新 day job 会吃掉原本打算用于作品的时间。

所以更准确的概念是：

### `REVERSIBILITY CAPITAL / 可逆性资本`

> 在创作者项目失败、停止或商业不足后，使其能够恢复稳定现金流、重新组织职业身份、保留部分创作选择权的可迁移能力、履历、关系、就业市场需求与低债务结构。

它是 **bounded downside 的来源**，不是失败免疫。

### 4.2 家庭不是单纯“支持/反对”，而是在改变重新下注门槛

GBGames 与 Atomic Armies 都显示：
- 同一人年轻/未婚时可接受的失败概率，
- 在婚姻、家庭预算、未来住房/育儿责任出现后，
- 可能不再满足再次 full-time exit 的阈值。

因此 OQ-004 与 OQ-005 应连接成：

```
AUTHORIAL_RIGHT_VALUE
vs
FOREgone salary
+ household fixed claims
+ debt
+ re-entry uncertainty
```

不是“父母/妻子支持不支持”二元变量。

### 4.3 “失败留下经验”必须接受市场折旧

Atomic Armies 是最直接的反例。

经验是否是 residual capital，至少取决于：
- 技能是否跨技术栈可迁移；
- 新劳动力市场是否认可；
- 是否能用作品/履历证明；
- 该生产 regime 是否仍存在需求；
- 作者是否愿意继续在同一行业。

所以以后禁止写：
> “即使失败，经验也是资产。”

应改为：
> **失败可能留下资产；只有后来仍可使用、可证明、可重新定价的部分，才计入 residual capital。**

### 4.4 公司退出、职业退出、作者退出必须分离

Mountaincore 给出最直观的四层拆分：

- company can die；
- developers can quickly re-enter employment；
- project can lose active labor；
- code can remain public and reusable。

任何单一 “studio survived / failed” 指标都会丢失大半信息。

## 5. 对 OQ-002 / 005 / 006 的方法修正

### OQ-002 Second Attempt

新增至少四种 continuation：

- `SECOND_COMMERCIAL_RELEASE`
- `SECOND_AUTHORIAL_ATTEMPT_NOT_SHIPPED`
- `SIDE_AUTHORSHIP_WHILE_EMPLOYED`
- `MEDIA_SWITCH_THEN_REENTRY`

因此“第二作率”只是 continuation 的一个子类。

### OQ-005 Authorial Right vs Salary

以后比较“为什么不辞职”至少同时记录：

- current employment retained?
- household fixed claims?
- debt?
- previous failed full-time attempt?
- external labor-market value?
- explicit threshold for quitting again?
- authorial work possible part-time?

GBGames 是目前最直接的“家庭预算 + 工资 + 再辞职门槛”一手样本。

### OQ-006 Failure Reversibility

先不要追求一个假精确的 `REVERSIBILITY_SCORE`。

先记录 outcome vector，并至少在失败后观察：
- T+12m；
- T+36m；
- T+60m。

最低变量：

```
employment_status
industry_status
authorial_activity
company_status
project_status
debt_publicly_known
household_constraint_publicly_known
residual_asset
second_attempt
last_verified_date
```

如果 salary 没公开，就保持 UNKNOWN；不允许用地区平均薪资替个人补值。

## 6. 现在真正缺的不是更多传奇失败，而是 denominator

本轮故意加入较低知名度的个人/小团队，但仍然是**公开写 postmortem 的人**，存在强 selection effect：

- 愿意写长篇失败复盘的人不是随机失败者；
- 能在多年后写“我后来恢复了”的人天然更可见；
- 完全退出互联网、改行后不再谈游戏的人最难观察；
- 公司 liquidation 比个人就业状态更容易核；
- 人的工资、家庭资产与债务最终结果通常不公开。

因此本轮不能回答：
- “多少失败 indie 能找到工作？”
- “美国/欧洲失败更可逆吗？”
- “失败后平均多久恢复工资？”
- “家庭是否提高/降低成功率？”

它只把**要测什么**从作品层推进到了人生层。

## 7. 下一轮应如何做成真正的 cohort

优先使用已有 [028 媒体选择与分母协议](media-selection-survivorship-and-denominator-protocol-028.md) 的 fixed-entry 思路：

1. 从 2016–2020 某个公开、完整 entry frame 建失败/低表现项目队列；
2. 预注册 T0 与 T+3y / T+5y 观察窗；
3. 不因能搜到后续采访才纳入；
4. 逐项找 creator/studio 公开职业轨迹；
5. 将看不见的人保留为 `EMPLOYMENT_UNKNOWN`，不把沉默编码为退出；
6. 只在同一抽样框内报告比例。

更值得做的第一个 cohort 不是“100 个著名 indie 失败案例”，而是：

> **一个固定年份、固定入口、所有首作都进入观察的 30–100 个小团队，然后追踪其 T+5 年的就业、作者性与第二次尝试。**

这才有可能真正关闭 OQ-002 / OQ-006 的 rate 问题。

## 8. Reader-layer 可用结论

当前最值得写进最终书的不是“辞职还是不辞职”的口号，而是：

> **独立创作的风险不是“游戏失败概率”一个数字，而是失败后你还剩多少可行选项。**

产品期望值相同的两个人，如果一个：
- 没有债务；
- 有可迁移职业技能；
- 能兼职验证；
- 失败后仍能回到高需求岗位；

另一个：
- 已经举债；
- 技能高度绑定正在衰退的技术栈；
- 家庭固定支出高；
- 项目还附带多年交付义务；

两人的“同一次独立开发”根本不是同一笔赌注。

因此人生性价比模型下一步不应只问：

`P(game succeeds) × payoff`

而应至少同时看：

```
expected upside
- irreversible downside
+ reversibility capital
+ residual authorial options
```

这仍然不是可直接算成单一分数的公式，而是读者必须逐项核算的决策框架。
