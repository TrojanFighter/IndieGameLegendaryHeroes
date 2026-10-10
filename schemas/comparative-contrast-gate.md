# Comparative Contrast Gate｜跨案例对照设计与反例保全

- Owner: **Lane A**（研究方法与质量门）；事实取证和对照结论仍归 **Lane B**
- Status: ACTIVE ON MERGE / 2026-10-10 correction proposal
- Scope: 跨人物、公司、技术、品类、国家的研究比较；尤其是「资源不对称 × 产品结果不对称」研究
- Boundary: 本协议不创造 Case/Evidence/Claim，不替代 [evidence rules](evidence-record-template.md) 和 [workflow lanes](workflow-lanes.md)

## 0. 先回答“为什么选择这几个人/作品”，才问“他们是不是同一个品类”

研究本书不是为每个游戏寻找更多相似作品，而是研究**创作能力、组织资源、实际玩法成果、验证与迭代决策之间为何不等价**。

任何一组跨案研究，开始前先写一句可被质疑的共同研究问题（Shared Decision Problem），以及**为什么每个案例都必须入组**。允许不同品类回答同一生产问题，也允许同题材产品因为缺失核心机制而成为关键反例。不得为了让对照组变成“纯同类产品”而抹掉作者刻意选入的负例。

### 两个已出现的校准例子（仅导航，事实仍在原档）

- [四案例 Production Fundamentals Matrix：SYNCED / Boundary / Gunfire Reborn / Tripwire](../book/research-notes/china-production-fundamentals-four-case-matrix-011.md)：四条**未必同品类**的开发路线，比较 Time-to-Player-Truth、验证前资源暴露、错误持续成本、市场模式与能力-范围匹配。
- [海盗船四作研究候选（PR #324，仍待审）](https://github.com/TrojanFighter/IndieGameLegendaryHeroes/pull/324)：**Blackwake、Blazing Sails、Sea of Thieves、Skull and Bones**。研究「实际可操作的船员/破坏/修复/登船闭环是否与组织资源相称」。最后一作**不满足合格互动品类的入组门槛，但必须保留在研究比较矩阵作为负面对照**。Rare 是大型组织做出正例的压力测试。

四个是这两组对照适合的规模，不是强制“每篇都找四个”；选例以因果解释力和反证强度而非版面整齐度为准。

## 1. 四个互不等价的集合标签，禁止一个标签统治全部

| 标签 | 问题 | 允许值 | 不可做的偷换 |
|---|---|---|---|
| `RESEARCH_SET` | 为什么要把它拿来比较？ | 必须有对照角色和选入理由 | “不同品类”≠“不能比较” |
| `MECHANIC_COHORT` | 是否真正实现我们研究的核心交互？ | `QUALIFIED / NOT_QUALIFIED / UNKNOWN` | 游戏有主题/火炮/联网≠满足船员可破坏交互 |
| `DENOMINATOR` | 是否属于某个成功率/发生率的统计总体？ | `IN / OUT / UNRESOLVED`，需写抽样框 | 研究对照集≠代表性抽样；负例未必属于合格玩法品类分母 |
| `OUTCOME` | 哪些维度成功/失败/尚未知？ | 玩家体验、销量、利润、留存、服务、生涯/再入场等**分别标注** | 不得用玩家数当销量，用好评当利润，用停服判技术毫无价值 |

**强制不变式：**`MECHANIC_COHORT=NOT_QUALIFIED` 不允许自动删除 `RESEARCH_SET` 成员。它可能正是研究要解释的失败；如果创作者明确指定四项，则四项都应保留。需改动时必须说明要回答的新问题、对照角色的改变及损失的反证能力，未经作者同意不能默默改表。

## 2. 比什么：产品函数先于生产身份

先列出玩家实际可操作的机制，而不是照开发商宣传或“技术含量”表象分类：

1. **Player action**：玩家到底能做什么，哪些需要真人在场与协作？
2. **World/part state**：哪个对象/部位可以受损、改变状态，是否有后果与修复？
3. **Feedback/decision loop**：这项变化如何迫使玩家采取新决策，而不是仅播放动画或扣总 HP？
4. **Interaction topology**：单机、合作、竞争、服务器状态、人口与配对依赖分别是什么？
5. **Version**：原型、EA、1.0、后续赛季/扩展分别什么时候拥有这个系统？

**验证步骤：**平台/官方版本信息 → 游戏内素材与开发录像、实际操作演示 → 玩家具体抱怨/褒奖与专业评测互证 → 技术内幕（有则补，无则 `UNKNOWN`）。区分**可交互的系统完整性**与**渲染/底层网络工程复杂度**；两者可以不同，不靠形容词互相推断。未亲自实际游玩时要声明依据是公开实机与资料。

## 3. 再比什么：单位资源能换来什么验证与玩家价值

用相同时间切片建立资源与成果的对照，不得把“创始3人”“发售 credits 60人”和“百人峰值”放在同一列直接排名：

| 资源/决策 | 必问字段 |
|---|---|
| 作者与能力前史 | 原型/MOD/UGC/学历/职业、谁定义产品和能亲自验证核心机制 |
| 人力与外围 | 首版核心、EA、1.0、峰值全职、累计 credits、外包、发行/资金支持分别多少，UNKNOWN留空 |
| 验证前投入 | Time-to-Playable、Time-to-Player-Truth、付费意愿测试、扩张前成本暴露 |
| 错误处理 | 何时发现问题、为何维持或砍掉、错误持续年限与已锁定义务 |
| 技术/内容/市场义务 | 自研/购买、可复用内容、服务器、匹配人口、QA、长期运营 |
| 可观察结果 | 可操作交互、评价与分布、销量与观察日、收入/退款、服务生命周期、技术/人才残值 |

无法获得可比的审计开发成本或人年时，只能进行有边界的**序数/机制判断**，不得用不明预算算 ROI 或断言整体组织人效的统计倍数。

## 4. 对照组设计：寻找“最能使直觉出错”的格子

单案例研究结束时，执行一次**主动对照扫描**，而非等待作者再提醒：

- 相近题材/任务、不同团队规模：谁真的实现核心体验？
- 相近资源/履历、不同验证路径：谁先把 playable 交给玩家？
- 相近技术资产、不同产品/市场选择：谁扩范围、谁删功能、何时受惩罚？
- **不方便的反例**：有没有大型团队做得好的例子？有没有小团队虽掌握技术仍失败的例子？
- **同历史窗口的失败者/中位数**：不能以四个有意选出的典型案例推出行业成功率或因果效应量。

选例角色可写为 `POSITIVE / NEGATIVE / MIXED / BOUNDARY / HISTORICAL_CONTEXT / INCONVENIENT_COUNTEREXAMPLE`。这些是**研究职责**，不是对作品全部价值的总评分；角色必须写关联哪一个研究问题，不能脱离问题宣布永久胜负。

特别注意：`BOUNDARY` 或 `NEGATIVE` 不是“剔除”，只是提醒作者这一项揭示了品类/产品形成失败或研究边界。只有**计算明确定义的某个统计分母**才检查资格；书稿的比较可以故意选择它。

## 5. Lane B 最小交付：必须先锁对照意图，再做资料与行文

新建或更新四案/多案矩阵时，文件开头至少出现：

```text
Research Question:
Why These Cases (one reason per case):
Case Role / Research Set membership:
Mechanic Cohort definition + verdict (may be OUT but retained):
Denominator: explicit population/timeframe; or N/A (purposive cases)
Product Function: player action → part state → decision → feedback
Time Scope: prototype / EA / 1.0 / live version
Resource Exposure: core team / perimeter / funding / time, missingness
Contradictory Evidence / Inconvenient Positive and Negative Cases:
Hypothesis vs Verified Facts vs UNKNOWN:
What Would Change the Interpretation:
Reader-Layer Eligibility: evidence-locked only
```

具体笔记可以自然叙事，不要求僵硬地逐行套模板；但这些问题必须能在研究中找到答案或显式 `UNKNOWN`。

## 6. 阻断式语义审查（Checklist；Lane B交回时和PR审查时）

- [ ] 是否先写共同研究问题，再讨论分类归属？
- [ ] 用户/作者指定的所有对照对象都存在于**研究矩阵**，包含不合格产品和失败者？
- [ ] 每个案例都有明确选择理由、反例角色及版本时间边界？
- [ ] 是否先检查真实玩家交互，再看团队名气、技术宣传和预算？
- [ ] 是否分别呈现资源规模、验证路径、玩家成果、商业指标，没有把它们相互代指？
- [ ] 是否有能否证强解释的“不方便”正反例，并说明尚缺什么分母？
- [ ] 假说、当事回忆、同期一手、二手、UNKNOWN 是否分级；是否避免道德化的动机推定？
- [ ] 是否明确结论的适用范围、因果限制、可以推翻结论的证据？
- [ ] 如重新定义品类/抽样框，是否保留原研究对象并说明对照角色变化，而非删除反例？

**若不通过：**先恢复完整研究集和比较目的，再修产品机制与来源；不通过的材料保留为工作笔记，不直接进入 Claim/成品书稿。文义审查暂不可安全由 lint 自行判定，不能制造一个表面“机器通过”的假质量门。

## 7. Lane 边界与错误复盘

- Lane B：真实案例、证据、验证状态与矩阵对照；不以“为了配合 schema”为借口填入虚构成本或人数。
- Lane A：流程、模板、发现反例遗漏的非事实性校验；不替 Lane B 宣称历史结论。
- Lane C：可在成书中采用有选择性的四例故事张力，但只消费 Lane B 已锁定来源，不将统计“抽样”与有意挑选的戏剧性对照混同。
- **每次研究错误复盘**至少记录 `INTENT_MISREAD / CATEGORY_CONFLATION / COUNTEREXAMPLE_DROPPED / RESOURCE_PROXY_BIAS / SOURCE_GAP / SCALE_OVERCLAIM` 中的实际模式及其具体修复，并将此次修复提交所改动的研究集与主档链接留下。反复故障先调整本协议，再考虑确定性 lint 检查；不能靠代理口头保证“以后注意”。

**核心规则：对照集服务于解释问题；品类标签服务于某个分类；统计分母服务于发生率。三者永远不能互相替代。**
