# Creator Life / Decision Audit Schema

本 Schema 用于把 Case 从“项目生产史”继续推进到可比较的人生决策史。

它不是第二套 Case Schema，也不建立平行事实数据库。

目标：

> **在不牺牲 Case 现有生产史结构的前提下，用同一组字段回答：这个创作者在什么生活条件、能力结构、验证条件下，承担了多大的人生风险？**

适用于：
- 独立开发者；
- 极小团队 founder；
- 大厂→作者型创业；
- 非传统 outsider；
- 已婚 / 有孩 / 有房贷 / 高 household burn 的中年开发者；
- 学生 / 业余开发 / day-job 开发者。

所有字段都必须允许 `UNKNOWN`。

禁止为了“表格完整”自行推断配偶收入、家庭资产、房贷、健康、父母支持或未公开职业条件。

---

## 1. Audit Status

每个 Case 可记录：

- `PENDING`：尚未按本 Schema 审计；
- `PARTIAL`：至少一半关键字段有可核证材料，仍存在明显缺口；
- `SUBSTANTIAL`：主要人生条件已可支持横向比较，但仍有次要空白；
- `COMPLETE`：关键人生 / household / capability / validation 条件均有可靠证据。

这个状态只表示**覆盖率**，不表示 Case 结论正确程度。

Evidence Strength 继续由 Case Schema 单独管理。

---

## 2. Household Structure

至少检查：

| 字段 | 允许值 / 记录方式 |
|---|---|
| relationship_status | single / partnered / married / divorced / UNKNOWN |
| children | number / none / UNKNOWN |
| dependents | parents / relatives / none / UNKNOWN |
| housing | rent / mortgage / family-owned / company/school / UNKNOWN |
| location_cost_context | 城市 / 国家 + 当时成本线索 |
| immigration_or_visa_constraint | yes / no / UNKNOWN |

禁止通过年龄或地区常识推断婚育。

---

## 3. Cash Runway

必须拆开：

- founder savings；
- salary / day job；
- spouse / partner income；
- family transfers；
- housing subsidy / family housing；
- severance；
- previous-game revenue；
- contract / freelance income；
- publisher advance；
- grant；
- crowdfunding；
- debt / credit；
- founder salary during production。

推荐表：

| 时段 | 现金来源 | household / project 哪一侧 | 金额或口径 | Evidence | Confidence |
|---|---|---|---|---|---|

如果只知道“伴侣支持”，不能自动写成伴侣承担主要收入。

---

## 4. Household Burn / Hidden Cost

至少检查：

- rent / mortgage；
- childcare；
- medical / insurance；
- debt service；
- partner income shock；
- elder-care；
- founder unpaid period；
- below-market founder salary；
- unpaid domestic labor；
- emotional / logistical support；
- relocation cost；
- healthcare / welfare context。

重点：

> **公司 burn ≠ 创作者真实 burn。**

家庭劳动如果公开可确认，也属于生产外围，不应从英雄叙事中删除。

---

## 5. Exit / Recovery Option

记录：

- prior profession；
- reemployment ability；
- licensing / credential portability；
- whether day job was retained；
- whether sabbatical / leave existed；
- whether founder could return to prior sector；
- whether project failure implied bankruptcy or only career delay；
- whether partner / household had independent income。

推荐状态：

- `HIGH EXIT OPTIONALITY`
- `MEDIUM EXIT OPTIONALITY`
- `LOW EXIT OPTIONALITY`
- `UNKNOWN`

不得仅凭“程序员”自动判定为高。

---

## 6. Capability Vector

不用职位替代能力。

至少按实际证据记录：

- programming / engineering；
- technical art；
- visual art / animation；
- game design；
- level design；
- writing / narrative；
- audio；
- production / PM；
- business / publishing；
- marketing / community；
- research / criticism / taste capital；
- prior team tacit capital；
- tools / reusable code / IP / audience。

### Capability Asymmetry

明确：

- strongest capability；
- weakest / missing capability；
- capability intentionally outsourced；
- capability intentionally not acquired；
- capability added later through cofounder / hire / capital。

---

## 7. Problem Ownership

检查：

- 谁决定“这个项目值得做”？
- 谁可以改产品 thesis？
- 谁能杀掉核心假设？
- founder 是否直接接触用户？
- publisher / investor / employer 是否拥有 milestone / approval / commercial veto？
- 旧公司 objective function 是否仍支配创业后的产品？

状态建议：

- `HIGH`
- `MEDIUM`
- `LOW`
- `MIXED`
- `UNKNOWN`

必须附解释，不能只给等级。

---

## 7A. Career Prestige / Authorial Continuity

当 Case 涉及名校、名企、AAA、大厂、专业服务公司或其他高声望职业路径时，额外检查三项。

### Identity Coupling

> 学历 / 雇主 / 职级是否只是能力与收入来源，还是已经成为主要自我价值证明？

可观察：
- 离开高声望机构是否被当成身份降级；
- 小项目/粗原型是否带来 status shame；
- 是否必须做“配得上履历”的项目；
- 是否仍等待外部权威批准方向。

建议：
- `LOW`
- `MEDIUM`
- `HIGH`
- `UNKNOWN`

### Parallel Authorial Thread

> 正式教育/雇佣之外，是否长期存在独立问题定义—作品—反馈链？

可记录：
- side project；
- game jam / mod / UGC；
- criticism / writing；
- open-source；
- board game / music / film / art；
- non-work collaborator；
- public artifact / audience。

关键不是“有爱好”，而是是否存在：

```text
self-generated problem
→ artifact
→ external feedback
→ revision
→ continuity
```

### Prestige-Preserving Project Distortion

> 独立项目是否为了维持过去学历/雇主/职级的专业身份，而承担了产品验证并不需要的成本？

检查：
- prototype over-polish；
- headcount-before-evidence；
- pipeline-before-problem；
- benchmark-as-legitimacy；
- status-preserving scope；
- 对 2D / toy / mod / ugly prototype 的 status aversion。

核心反事实问题：

> **If nobody knew your résumé, would you still build the project this way?**

没有证据时写 `UNKNOWN`，不得从“中国大厂”“AAA veteran”“名校生”标签直接推断。

---

## 8. Validation Architecture

必须重建：

```text
Hypothesis
→ First Playable
→ First Stranger Feedback
→ First Market Signal
→ First Paid Signal
→ Escalation / Kill / Pivot
```

至少记录：

| 阶段 | 时间 | 真实对象 | 反馈形式 | 是否改变项目 | Evidence |
|---|---|---|---|---|---|

重点检查：

- friends-only feedback；
- stranger playtest；
- public demo；
- mod/community；
- game jam；
- Kickstarter；
- wishlist；
- paid alpha；
- Early Access；
- launch；
- retention / sales / review；
- streamer / creator response。

---

## 9. Reality Adjudication

独立记录：

> **现实有没有权力否决创作者？**

至少检查：

- player confusion 是否被视为设计问题；
- negative data 是否改变 scope；
- favourite feature 是否会被删；
- benchmark 是否能被现实推翻；
- creator 是否把失败归因于“玩家不懂”；
- market failure 是否只被归因于 marketing。

推荐状态：

- `STRONG`
- `PARTIAL`
- `WEAK`
- `UNKNOWN`

---

## 10. Capability Capture Risk

检查：

> **最强能力是否把项目吸向自己最擅长、最喜欢、最容易获得正反馈的方向，而非最需要解决的 product obligation？**

典型信号：

- engine / tooling 持续进步但 product closure 落后；
- art fidelity 上升但 onboarding / loop 未闭合；
- narrative volume 上升但 core interaction 未成立；
- live-ops infrastructure 先于用户价值；
- high-spec pipeline 先于 product thesis。

状态：

- `LOW`
- `MEDIUM`
- `HIGH`
- `UNKNOWN`

必须依赖具体 timeline，不可从职业标签推断。

---

## 11. Market Sufficiency / Legibility

分开检查：

### Legibility
玩家能否快速理解：
- 这是什么；
- 为什么不同；
- 该和什么比较；
- 为什么值得花时间 / 钱。

### Sufficiency
即便产品成立：
- audience 是否足够大；
- price × audience 是否可能覆盖 burn；
- multiplayer 是否需要足够 liquidity；
- niche 是否小到无法支撑组织；
- content / live-service obligation 是否与收入匹配。

状态建议：

- `STRONG`
- `PARTIAL`
- `WEAK`
- `UNKNOWN`

---

## 12. Capability Scaling

当核心成立后，创作者是否能把它做成稳定产品：

- QA；
- performance；
- localization；
- porting；
- customer support；
- content production；
- team management；
- publisher / platform interface；
- legal / finance；
- post-launch maintenance。

区分：

- founder personally scaled；
- cofounder added；
- hired specialists；
- publisher / platform handled；
- never scaled / project cancelled。

---

## 13. Temporal Validity

每个“人生建议”必须附：

- observed years；
- location；
- production regime；
- tool / distribution regime；
- household cost regime；
- 2026 transfer status；
- today’s mechanism vs obsolete tactic。

例如：

> “保留 day job 三年做 Gunpoint”

只能迁移：

> **用稳定收入购买低承诺试错期**

不能自动迁移：

> “今天任何人都应当白天全职上班、晚上三年开发”。

---

## 14. Minimum Comparable Record

一个 Case 如果要进入“人生性价比横向比较”，至少要有：

- Capability Vector；
- Problem Ownership；
- Validation Architecture；
- Runway type；
- household / location 至少有一项可核现实条件；
- Exit / Recovery 至少 partial；
- Market Sufficiency / Legibility 至少 partial；
- UNKNOWN 明确列出。

否则仍可用于游戏设计/生产研究，但不得用来回答：

> “这种人适不适合辞职 / 创业 / 做几年独立游戏？”

---

## 15. Standard Case Insert

建议在 Case 中加入：

```markdown
## Creator Life / Decision Audit

- Audit status:
- Life stage:
- Household:
- Runway:
- Household burn:
- Exit / recovery:
- Capability vector:
- Problem ownership:
- Identity coupling: # when relevant
- Parallel authorial thread: # when relevant
- Prestige-preserving distortion: # when relevant
- Validation architecture:
- Reality adjudication:
- Capability capture risk:
- Market sufficiency / legibility:
- Capability scaling:
- Major unknowns:
```

允许更详细表格，但字段名称保持一致，便于未来 lint / skill 抽取。

---

## 16. Reader Archetype Translation

当字段足够成熟时，才允许把 Case 映射到读者类型：

- student / early-career；
- salaried programmer；
- TA / visual specialist；
- designer / producer；
- AAA / big-company veteran；
- married, dual-income；
- married, single-income；
- children / mortgage；
- unemployed / runway-only；
- outsider / career switcher；
- founder with prior hit；
- founder with publisher / VC。

这个映射只用于回答：

> **哪些历史案例与你的处境更像？**

不得变成人群成功率预测，除非未来有统计数据。
