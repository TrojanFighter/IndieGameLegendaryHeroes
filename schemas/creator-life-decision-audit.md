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

## 6B. Complement / Correction Architecture

当人物或Case依赖共同创始人、核心搭档、强技术/创意二人组时，不再只写 capability complementarity。参考 [042](../book/research-notes/carmack-romero-complementary-error-correction-network-042.md) 与 CASE-056 Playdead，补以下字段：

- Cross-domain fluency：双方是否理解彼此专业到能提出可执行反意见；
- Veto / voice reality：弱势专业是否真的改变过强势专业的决策；
- Role plasticity：比较优势变化后是否能重划角色而不触发身份战争；
- Shared artifact frequency：争论多久能转成共同可玩的build / prototype / data；
- Correction latency：错误从产生到暴露需要多久；
- Complement portability：组合拆开后，哪些能力能带走，哪些属于关系本身；
- Governance durability：ownership / credit / schedule / exit / final decision rights能否长期重谈；
- High-status epistemic opponent：核心作者身边是否存在不依赖取悦他、且其能力足以让他重新考虑判断的人。

最小结论区分三层：
1. Capability composition：能否把产品做出来；
2. Epistemic correction：能否互相改答案；
3. Governance durability：多年后是否仍能在权利和节奏变化下合作。

产品成功只能直接支持第一层，不能自动证明后二层。

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

## 7B. Authorial Access / Institutional Path to Authorship

当 Case 涉及公司内部晋升、创业、spinout、失败项目接管、side project 转正或新产业窗口时，必须额外追问：

> **这个人究竟通过什么路径取得了“我有权决定做什么”的资格？这种资格是制度化的、恩主授予的、市场换来的，还是必须退出原组织以后才获得？**

这不是“自由人格”评分，而是可观察的 decision-right chain。

### Authorial Rights Chain

至少检查：

| 字段 | 核心问题 |
|---|---|
| `problem_origin_right` | 能否自己提出项目 / 核心问题？ |
| `pre_greenlight_resource` | 正式立项前能否获得带薪时间、工具、人手或基础设施？ |
| `prototype_right` | 能否先做 playable / artifact 再接受评审？ |
| `greenlight_right` | 谁决定进入更高资源级别？ |
| `kill_right` | 谁能终止项目或核心假设？ |
| `rescope_right` | 项目遇阻时能否缩队 / 回炉，而不是作者与问题一起清零？ |
| `parent_budget_right` | 工作室之外谁能撤销整个项目 / 创新制度的预算？ |
| `credit_appropriation` | 成功后个人能否获得声誉、财富、职位或下一轮 decision rights？ |

### Access Mechanism

如果证据允许，标记取得作者权的主要机制（可多选）：

- `INSTITUTIONALIZED`：稳定流程赋权，与特定领导者无关；
- `FRONTIER_EXEMPTION`：新产业 / 新技术使旧资历暂时失去信息价值；
- `PATRON_GATED`：关键高层直接开闸、绕过正常层级；
- `FAILURE_SHELTER`：边缘 / 失败项目因控制下降反而获得实验空间；
- `SIDE_PROJECT_CONVERSION`：私人 / 业余原型被组织吸收为正式项目；
- `EXIT_REQUIRED`：离开原组织、创业或spinout后才取得完整作者权；
- `MARKET_LEGITIMATED`：demo / mod / sales / community等外部结果先赋予合法性，再换取组织资源；
- `UNKNOWN / MIXED`。

### Agency / Seniority / Regime Cost

对取得作者权之前的成本分开记录：

- `AGENCY_TAX`：坚持非共识判断需要额外承担的家庭、收入、身份、职业、融资与失败成本；
- `SENIORITY_TAX`：当前能力兑换成正式职位 / 决策权前必须支付的年资成本；
- `REGIME_TAX`：从旧生产制度的成功路径转向新范式时，需要放弃多少既有职位、收入、团队、声誉与行业常识。

**不得因为当事人最终成功，就把这些成本事后改写成“必要磨炼”。**

### Second Attempt / Creator Replacement

一次成功不能证明生态健康。至少继续追：

- `failure_shelter`：首个项目失败后人是否仍有工资 / 组织位置；
- `second_attempt_capacity`：是否真实获得下一次自定问题的机会；
- `team_continuity`：核心能力与协作关系是否保留；
- `creator_replacement_context`：当已有大师 / founder / director占据资源后，新一代是否仍有进入同等级作者权的可见通道。

这组字段尤其用于避免两种幸存者偏差：
1. 只研究最终破格成功的人，而忽略同代未穿透者；
2. 看到一个组织培养过一位大师，就推定它持续拥有创作者代际更新能力。

Comparative research anchors:
- [Japan 001 — Bounded eccentricity → frontier exemption / seniority tax / creator replacement](../country-studies/japan/001-japan-east-asian-counterexample-weird-kinship-and-game-creator-ecology.md)
- [China 015 — frontier location / agency tax / regime tax / authorial continuity](../country-studies/china/015-japan-comparator-frontier-permeability-author-rights-and-creator-replacement.md)

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

## 11B. Demand-Side Selection / Consumer Veto

当 Case 的作者权、续作预算或长期生存明显依赖玩家市场时，额外记录：

- `taste_capital_context`：目标玩家是否拥有足够reference breadth / comparative literacy；
- `creator_selection_capacity`：玩家是否把认可转成购买、传播、捐赠、测试、mod或众筹；
- `consumer_veto`：产品/品牌错配后，玩家是否真的停止消费；
- `channel_mediation`：平台推荐、发行、买量、商店入口是否显著决定可见性；
- `demand_weighting`：收入更接近bounded purchase，还是由少数高LTV玩家强烈加权；
- `reputational_carryover`：市场认可是否真的转换成作者下一轮预算与decision rights。

必须区分：
- sentiment ≠ purchase；
- majority preference ≠ revenue-weighted preference；
- visibility ≠ demand；
- fandom ≠ sustainable unit economics。

Canonical research anchor:
- [China 017 — Demand-Side Creator Selection](../country-studies/china/017-demand-side-creator-selection-player-veto.md)

---

## 11C. Author Brand / Portable Demand

当人物已经有至少一款公开作品，且后续融资、创业、离职、换IP或平台合作可能受个人声誉影响时，额外记录：

- `brand_locus`: author / studio / IP / publisher-platform / hybrid；
- `author_recognition`: 玩家/媒体是否识别具体作者；
- `attention_portability`: 换IP/公司后注意力是否跟随；
- `revenue_portability`: 注意力是否真的转成购买；
- `financing_conversion`: 名声是否降低融资/发行门槛；
- `bargaining_power_conversion`: 是否换来更大decision rights；
- `outside_option`: 离开原组织后能否带走合作机会/玩家需求；
- `IP_ownership`；
- `customer_relationship_ownership`；
- `brand_capture_risk`；
- `expectation_lock_in`；
- `succession_model`。

强制区分：
- creator visibility ≠ portable demand；
- media attention ≠ revenue portability；
- name in title ≠ current auteur control；
- successful IP ≠ author brand；
- author brand ≠ superior industrial model。

Canonical research anchor:
- [China 020 — Author Brand Capital](../country-studies/china/020-author-brand-capital-portable-demand-bargaining-power.md)

---

## 11D. Attribution Politics / Credit Regime

当人物来自大团队、外包、F2P/GaaS、多人创作，或后世归因可能受媒体/公司叙事影响时，额外记录：

- `credit_visibility`: 是否公开署名；
- `credit_persistence`: 离职/版本更新后是否保留；
- `role_legibility`: 外界能否知道实际负责什么；
- `credit_money_coupling`: credit是否连接royalty/bonus/薪资/融资；
- `credit_rights_coupling`: 成功credit是否转成下一轮decision rights；
- `attribution_risk`: harassment / poaching / scapegoating / credit appropriation；
- `decision_provenance`: 谁提出问题、谁定quality bar、谁有kill right；
- `attribution_authority_alignment`: public attribution是否大致匹配真实权力与贡献。

强制检查两个极端：
- `CREDIT WITHOUT POWER`
- `POWER WITHOUT CREDIT`

Canonical:
- [China 021 — Attribution Politics](../country-studies/china/021-attribution-politics-credit-regimes-author-power.md)

---

## 11E. Creative Surplus Allocation / Future Capture

当案例涉及创业、离职、publisher deal、IP、版税、股权、自发行或平台依赖时，额外记录：

- `labor_cash`: 工资/项目奖金；
- `revenue_participation`: royalty / profit share；
- `equity`: 是否持有studio/company长期价值；
- `credit_retention`: 成功credit是否可带走；
- `ip_ownership`；
- `sequel_derivative_rights`；
- `publishing_distribution_rights`；
- `customer_relationship_control`；
- `audience_brand_portability`；
- `future_decision_rights`；
- `platform_mediation`；
- `future_capture_ratio`: low / medium / high / unknown；
- `authorship_reset_cost`: 换组织后多少资产归零。

强制区分：
- IP ownership ≠ creative sovereignty；
- equity ≠ control；
- royalty ≠ decision rights；
- self-publishing ≠ direct customer ownership；
- salary/title growth ≠ reusable author capital。

Canonical:
- [China 022 — Creative Surplus Allocation](../country-studies/china/022-creative-surplus-allocation-rights-customer-future-control.md)

---

## 11F. Creator-Class Formation / Ecosystem Externality

当人物/工作室已经有显著商业成功、长期存续或资本积累时，额外记录：

- `future_transfer`: 是否把资源给其他creator；
- `capital_recycling`: funding / advance / investment / grants；
- `taste_recycling`: greenlight / curation / mentoring；
- `audience_lending`: showcase / newsletter / cross-promo / event；
- `infrastructure_recycling`: tools / SDK / publishing / QA / localization；
- `human_capital_reproduction`: alumni / spinout / modder→professional；
- `governance_recycling`: 是否把developer autonomy写入下一代制度；
- `creator_surplus_multiplier`: low / medium / high / unknown；
- `second_generation_success`: 是否存在受益者成功样本；
- `third_generation_transfer`: 第二代是否继续扶持第三代；
- `institution_persistence`: 是否跨5年/创始人/收购继续存在。

强制边界：
- 1个成功publisher ≠ creator class；
- 1个mentor ≠ intergenerational reproduction；
- developer-founded publisher ≠ automatically creator-friendly；
- individual generosity ≠ institution；
- case existence ≠ same quantity / same causal strength.

Canonical:
- [China 023 — Creator Class Formation](../country-studies/china/023-creator-class-formation-intergenerational-reproduction.md)

---

## 11G. Mobility / Spinout Topology

当人物从大厂离职、创业、重组团队，或案例涉及竞业/挖角/前同事网络时，额外记录：

- `effective_mobility_friction`: low / medium / high / unknown；
- `noncompete_or_restrictions`；
- `mobility_to_ownership_conversion`: 跳槽是否转成founder/equity/IP；
- `spinout_conversion_rate_context`；
- `alumni_network_capital`；
- `left_with_team`；
- `parent_behavior`: hostile / neutral / supportive / investor / first-client；
- `first_funding_after_exit`；
- `first_contract_after_exit`；
- `spinout_legitimation_effect`；
- `second_generation_spinout`；
- `knowledge_protection_vs_general_skill_boundary`。

强制区分：
- job hopping ≠ entrepreneurship；
- entrepreneurship ≠ creator ownership；
- noncompete law ≠ effective mobility by itself；
- case existence ≠ high spinout rate；
- parent hostility/support must be evidenced, not inferred.

Canonical:
- [China 024 — Creator Mobility & Spinout Topology](../country-studies/china/024-creator-mobility-spinout-topology-noncompete.md)

---

## 11H. Spinout vs Indie-Mode Conversion

当人物/团队从成熟组织离职创业时，禁止把 founder 身份直接编码成 indie author。

额外记录：

- `employment_exit`
- `ownership_exit`
- `product_divergence`
- `objective_function_exit`
- `production_mode_exit`
- `spinout_mode`: SCALE-CONTINUITY / AUTHORIAL-STUDIO / INDIE-MODE / INFRASTRUCTURE-CAPITAL-TOOL / UNKNOWN
- `problem_ownership`
- `scope_plasticity`
- `fixed_burn_discipline`
- `hands_on_creator_density`
- `player_truth_proximity`
- `capability_shaped_formation`
- `governance_optionality`
- `selective_capability_retention`
- `subtraction_capability`
- `status_decompression`
- `pre_existing_authorial_substrate`
- `mode_by_phase`

强制区分：
- entrepreneurship ≠ indie；
- new product ≠ new objective function；
- founder ownership ≠ authorial autonomy；
- premium ≠ indie；
- small team ≠ indie；
- studio identity can change across projects.

Canonical:
- [China 026 — Spinout ≠ Indie](../country-studies/china/026-spinout-vs-indie-mode-conversion.md)

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
- Demand-side selection / consumer veto: # when relevant
- Author brand / portable demand: # when relevant
- Attribution politics / credit regime: # when relevant
- Creative surplus allocation / future capture: # when relevant
- Creator-class formation / ecosystem externality: # when relevant
- Mobility / spinout topology: # when relevant
- Spinout vs indie-mode conversion: # when relevant
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
