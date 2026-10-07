# 《独立游戏英雄传说》｜书稿结构

© 2026 洪荒行者。All Rights Reserved.

这份文件描述 **读者最终会读到的书**，而不是研究数据库的目录。

研究后台继续按 Case / Evidence / Claim 工作；Profile 继续保存一个人物或团队的完整生产史；真正的章节则跨人物、跨时代回答一个普通人会遇到的问题。

## 阅读前门｜按处境诊断，再寻找人物

这本书的阅读前门不应是案例编号，也不应直接是“程序员 / 美术 / 策划”职业分类。读者首先需要知道自己的当前约束与下一步生产选择。

- [START-HERE](START-HERE.md)：按当下困惑、阅读问题进入。
- [DECISION-ROUTER](DECISION-ROUTER.md)：总分诊，按 **Capability Position × Risk Position × Project Maneuver** 判断该移动项目、能力、团队、资本还是承诺。
- [Life Risk Routes](life-routes/README.md)：确定具体人生/生产处境后深入审计；含 [LR-001 大厂转作者](life-routes/big-company-veteran-to-author-001.md)、[LR-002 有工资的分阶段投入](life-routes/salaried-creator-staged-commitment-002.md)、[LR-003 家庭现金风险](life-routes/household-high-burn-creator-003.md)、[LR-004 项目能力缺口](life-routes/project-thesis-capability-gap-004.md)。
- [READER-ARCHETYPES](READER-ARCHETYPES.md)：第二级按专业能力结构寻找相似创作者的索引。

默认链路：

`现实问题 / 当前处境 → 约束与决策变量 → life route 或 capability archetype → 正反案例 → Chapter / Profile → 必要时 Case / Evidence`

只共享职业、国籍、年龄、学历或一家曾经供职的公司，不足以证明某个历史成功者与读者具有可比性；至少同时核对 **能力、runway / household / exit risk、项目阶段、外部验证、资本治理** 之中的两个独立维度。

## 三层结构

### Layer 1 — Research Backend

`cases/`、`evidence/`、`claims/`。

作用：保证事实、来源、反例、UNKNOWN 和禁止外推都可审计。

它可以难读，因为它首先服务真实性。

### Layer 2 — Hero Profiles

`book/profiles/`。

作用：把单个开发者 / 团队的一生与生产史写完整。

Profile 回答：

> 这个人是怎么一步步变成后来那个能做出这款游戏的人？

它必须保留人物差异、历史条件和不可复制部分。

### Layer 3 — Book Chapters

`book/chapters/`。

作用：把多个 Profile 放到同一个现实问题下比较。

Chapter 不再问：

> FTL 的故事是什么？

而问：

> 当你想做自己的事，但没有资格一次性赌几年人生时，有哪些已经发生过的路径？

人物是证据和故事，问题才是章节的主角。

---

# 暂定全书结构

章节顺序不是“成功方法步骤”，而是一条人通常会经历的生命链。

## 横向问题簇 — 英雄为什么没有出发

这不是新增一套“国民性章节”，而是一条贯穿全书的创作者反向审计线：

> **一个本来能力很高的人，可能在哪里被学校、行业、成功经验和成熟评分器提前优化成了“上一版本的优秀执行者”？**

总路由：
- [中国创作者约束三层图：教育 × 行业版本现状 × 社会版本意识](research-notes/china-creator-constraints-three-layer-map-018.md)
- [第一次人物压力测试：王妙一 × 《太吾绘卷》](research-notes/china-creator-three-layer-pressure-tests-019.md)
- [失败压力测试：自由、经验、支持都不能替代现实验证](research-notes/china-creator-three-layer-failure-pressure-tests-020.md)
- [系统案例矩阵：教育 × 行业版本 × 社会版本](research-notes/china-creator-three-layer-case-matrix-021.md)
- [缺口补全：高自主失败 / 去旧函数仍失败 / Household Economics](research-notes/china-creator-three-layer-missing-cells-022.md)
- [Creator Life / Decision Audit：把案例库升级成人生条件可比系统](research-notes/creator-life-decision-audit-backfill-023.md)
- [Creator Life P0 回填：第一版人生风险决策对照](research-notes/creator-life-decision-audit-p0-backfill-024.md)
- [Creator Life P1 回填：Runway 结构与 Evidence-Following Scaling](research-notes/creator-life-decision-audit-p1-backfill-025.md)
- [声望管道与作者连续性：名校 / 名企 / 大厂老兵为什么会出现不同转型](research-notes/prestige-pipeline-authorial-continuity-026.md)

### A. 教育｜你是否学会自己出题？

主要研究：
- learning ownership；
- closed-domain → open-world transfer；
- credential substitution；
- artifact-first learning；
- failure-as-information；
- Selection Function Mismatch。

入口：
- [AC-008 中国好学生综合征](../author-corpus/AC-008-china-good-student-syndrome.md)；
- [追赶成功、前范式创作者与问题主权](research-notes/china-catch-up-success-pre-paradigm-creator-016.md)；
- [目标如何在生产中形成](research-notes/goal-formation-through-production-001.md)；
- [从玩到生产](research-notes/play-to-production-fourth-industrial-revolution-001.md)。

边界：
> 不把“应试教育”直接等同于“低创造力”；研究的是外部评分器退出后，学习主权和问题定义是否完成迁移。

### B. 行业版本现状｜你在解哪一版的题？

主要研究：
- production regime；
- revenue / market interface；
- Benchmark Meta Convergence；
- exploration vs exploitation；
- competency trap；
- Production Capital vs Problem-Framing Capital；
- error persistence；
- demand/production lag；
- 所有成功经验的年份与版本有效期。

入口：
- [AC-007 Benchmark 答案化与版本时滞](../author-corpus/AC-007-benchmark-meta-convergence.md)；
- [中国结构性能力审计](research-notes/china-indie-structural-capability-audit-010.md)；
- [五代玩家 × 四代从业者](research-notes/china-player-worker-generations-009.md)；
- [领域性能力与需求侧评鉴资本](research-notes/domain-specific-capability-demand-evaluation-017.md)；
- Role-Origin、NExT、四案例 Production Fundamentals、Black Myth / Sultan 等现有压力测试。

边界：
> 大厂/商业游戏经验既可能留下可迁移能力资本，也可能留下旧 objective function；不能把“有大厂经验”或“没有大厂经验”直接当成创新力 proxy。

### C. 社会版本意识｜你有没有资格在成功前与众不同？

主要研究：
- Deviance Sanction；
- Merit-Conditional Tolerance；
- Winner's Amnesty；
- Unproven Deviance Survival Time；
- family/career expectation；
- Success-Path Version Lock；
- version-lagged life advice；
- runway、再就业能力、关系支持与退出成本。

入口：
- [AC-006 偏离惩罚、成功者赦免](../author-corpus/AC-006-deviance-sanctions-and-winners-amnesty.md)；
- [中国独立创作“三座大山”](../author-corpus/AC-004-china-three-mountains.md)；
- [追赶成功、前范式创作者与问题主权](research-notes/china-catch-up-success-pre-paradigm-creator-016.md)。

边界：
> “春登”只允许作为成功路径版本锁定的 H-layer 工作标签；同一机制可以出现在年轻人、欧美 AAA 老兵或任何被旧成功高额奖励的人身上。

### 三层合起来才是完整问题

```text
教育决定：
你有没有形成 Problem Ownership

行业决定：
你的异质题目能不能得到 prototype / market validation

社会决定：
在结果出现之前，你能不能承担继续偏离的成本
```

这条线服务的是“人生性价比指南”的负面镜像：不仅写英雄怎么成功，也写**英雄可能怎样在出发之前就被合理地训练成另一种优秀。**

## Reader Decision Interfaces｜Life Risk Routes

研究笔记足够成熟以后，不要求读者自己翻 Case 拼答案。

先从 [DECISION-ROUTER 总分诊](DECISION-ROUTER.md)识别处境、最大风险与应移动的生产变量，再进入 [`life-routes/`](life-routes/README.md) 的具体人生路径，按现实处境提供：

```text
处境
→ 最大风险
→ 最小实验
→ quit / scale threshold
→ 正反案例
→ 不可迁移条件
```

当前可用路线：
- [LR-001 — 名校 / 大厂高绩效者转作者型独立](life-routes/big-company-veteran-to-author-001.md)
- [LR-002 — 有稳定工资的创作者：先购买证据，再购买自由](life-routes/salaried-creator-staged-commitment-002.md)
- [LR-003 — 高家庭支出创作者：项目风险与家庭现金分开](life-routes/household-high-burn-creator-003.md)
- [LR-004 — 作品方向明确但团队能力不足：项目、学习、外包、合伙、招聘与融资怎么选](life-routes/project-thesis-capability-gap-004.md)

Route 不是成功公式；新证据若推翻现有判断，优先修改 Route。

## Part I — 目标不是先想明白的

核心问题：

> 我不知道自己真正想做什么，怎么办？

研究：
- 兴趣怎样从消费变成主动比较；
- 玩、拆、mod、评论、编程、写作怎样转成生产；
- 第一次公开作品 / 第一次陌生人反馈为什么重要；
- Experience Capital、Demand Discovery 与 Goal Formation；
- 为什么“十八岁就确定职业目标”不是创造者形成的必要条件。

主要人物池：
- early id / Romero / Carmack；
- Tom Francis；
- Dream Quest / Peter Whalen；
- Toby Fox；
- Zeekerss；
- Roblox creator cluster。

## Part II — 先买时间，不要先赌命

核心问题：

> 我想做自己的东西，但靠什么活到它有资格被验证？

研究：
- 工资、储蓄、伴侣收入、夜班、接活、work-for-hire；
- bounded experiment；
- staged commitment；
- runway 不只是“一笔融资”；
- 回撤能力和再就业能力也是风险资产。

主要人物池：
- FTL；
- Kenshi；
- Rocket League / Psyonix；
- Stardew Valley；
- Hollow Knight；
- despellote。

## Part III — 失败到底有没有价值

核心问题：

> 已经做错、做砸、没卖出去的几年，是不是全浪费了？

研究：
- failure residue；
- capability capital；
- staging project；
- 前作如何留下工具、代码、领域知识、社区、渠道和判断；
- 哪些失败真的只留下 sunk cost；
- 为什么“坚持”本身不是解释。

主要人物池：
- Rocket League / SARPBC；
- Bills Must Be Paid；
- R.E.P.O.；
- Escape from Tarkov lineage；
- Landfall；
- Brigador 作为反压力。

## Part IV — 技术时代不会替你做选择

核心问题：

> 新技术到底改变了什么？为什么有人只是用工具，有人却创造了一个时代窗口？

研究：
- Inherited / Diffused Window；
- Recombined Window；
- Endogenous / Created Window；
- 技术出现、成熟、成本下降、扩散与组织吸收的时间差；
- 技术 frontier 与普通开发者真实可得能力的区别。

主要人物池：
- early id / Carmack；
- Gunpoint / GameMaker；
- PLAYERUNKNOWN / Arma-DayZ；
- 后续的小岛秀夫 / MSX2、Minecraft、Unity/Steam 时代样本。

历史背景由 `cross-industry/industrial-revolutions/` 提供，不在这里写成技术年表。

当前首章：
- [技术时代不会替你做选择：有人用现成工具，有人重组平台，有人自己造出窗口](chapters/04-technology-will-not-choose-for-you.md)

## Part V — 市场不是最后一步

核心问题：

> 东西做出来以后，为什么有的项目仍然没人知道；为什么有的市场接口反而提前进入生产系统？

研究：
- demo；
- paid alpha；
- Early Access；
- Kickstarter；
- Steam / platform visibility；
- creator / community；
- “零营销”神话；
- market access 如何影响产品生存时间与反馈质量。

主要人物池：
- Minecraft；
- FTL；
- Factorio；
- Kenshi；
- Bills Must Be Paid；
- Among Us；
- Brigador。

当前首章：
- [市场不是最后一步：有时玩家、钱和反馈在“做完之前”就已经进入生产系统](chapters/05-market-interface-is-production.md)

## Part VI — 第一次成功以后，题目会换掉

核心问题：

> 为什么成功以后反而更难？成功的钱应先购买新能力，还是购买暂不承诺的选择权？

研究：
- optionality / retained earnings；
- **扩 capability** 与 **保留 option value** 的区别；
- 团队扩张、永久 headcount 与 fixed burn；
- founder alignment / authorship / governance；
- capital source 与 control surface；
- 第二作的试错权、延迟公开与 `LOCK-IN PREVENTION`；
- 长期 `FIT-LOCK-IN`：production grammar、资产复利、受众替换成本；
- 成熟工作室真正跨越固定 grammar 的转型条件。

主要人物池：
- early id → Quake → Ion Storm（[纵向母案例研究](research-notes/masters-of-doom-longitudinal-master-study-001.md)：早期互补如何在成功后产生治理与项目适配成本，另以 Daikatana / Deus Ex 作同公司对照）；
- FTL → Into the Breach：第一次成功后保留 option value；
- The Witness：自有资金购买额外 capability；
- House House：grant/publisher 支持与后续 retained earnings；
- thatgamecompany：equity 扩组织，也扩治理义务；
- Zachtronics + Spiderweb：成熟 FIT-LOCK-IN；
- Croteam / Serious Sam → The Talos Principle：成熟 FPS grammar 分叉成新解谜 IP，保留旧技术并新增测试/叙事，后来才在不同所有权制度下换 engine；
- Playdead：共同创始人治理压力；
- Minecraft / Mojang、Among Us、Rocket League / Psyonix：成功后的组织变化。

**明确保留的证据缺口：** Croteam 已提供第一份多年固定 FPS grammar 之后的有效分叉，但完整融资/营销/受众转移成本与跨工作室可复制性仍 UNKNOWN。不得用 FTL → Into the Breach 的早期分叉冒充成熟 lock-in 逃逸，也不得把 Croteam 一例升格为通用配方。

---

# 每章的编辑结构

一章原则上不是“列五个案例然后总结”。

优先使用：

1. **现实问题开场**：让非游戏开发者也知道为什么值得读；
2. **一个最反直觉的人物场景**；
3. **第二、第三个案例形成比较**；
4. **失败 / 反例压力**；
5. **把流行神话拆掉**；
6. **读者可以带走的判断框架**；
7. **明确哪些不能照抄**；
8. 文末给出 Profile / Case / Evidence 入口。

正文不出现 P0 / P1 / S1、RESEARCHING、lint、metadata 等后台术语，除非该术语本身是叙事对象。

---

# 人类读物与“成功学”的边界

这本书希望提高读者的选择质量，但不承诺复制成功。

每章必须同时展示：

- 当事人真正拥有的前置能力；
- 隐形支持；
- 实际风险；
- 失败与错误判断；
- 历史窗口；
- 右尾运气；
- 不可复制条件。

所谓“人生性价比”不是：

> 找一条稳赚路线。

而是：

> **在投入几年人生之前，知道有哪些成本会被成功故事删掉；知道什么时候应该先做一个更便宜的实验；知道过去的几年究竟有没有形成下一次可以使用的资本。**

---

# 当前生产规则

- Chapter 只能使用已经进入 Profile / Case / Evidence 的事实。
- Profile 尚未稳定时，可以进入章节候选池，但不得为完整叙事补齐 UNKNOWN。
- 新研究优先补 Profile；新写作优先补 Chapter。
- 以后根 README 和 book README 都优先把普通读者导向 Chapter / START-HERE，而不是 Case 编号。
- Profile 的研究状态、Case / Evidence backlinks 原则上下沉到文末，不占第一屏。
