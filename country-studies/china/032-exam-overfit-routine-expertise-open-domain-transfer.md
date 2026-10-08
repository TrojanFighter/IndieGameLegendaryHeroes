# 032 — Exam Overfit：应试教育过拟合、Routine Expertise 与开放问题迁移失败

- Program: C / 中国国情研究 × 教育社会化 × 创新认知 × 游戏生产
- Status: **SYNTHESIS FRAMEWORK / AUTHOR-ORIGIN + EXTERNAL LITERATURE PRESSURE TEST**
- As-of: 2026-10-08
- Parents:
  - [AC-008 — 中国好学生综合征](../../author-corpus/AC-008-china-good-student-syndrome.md)
  - [027 — Individualism as Innovation Infrastructure](027-individualism-as-innovation-infrastructure.md)
  - [028 — Hacker Spirit × Scale Down × Commercial Anti-Training](028-hacker-spirit-scale-down-commercial-antitraining.md)
  - [031 — Education × East-Asian Discipline × Reference Repertoire](031-education-east-asian-discipline-reference-repertoire.md)
- Boundary:
  - `EXAM OVERFIT / 应试教育过拟合` 是本项目的分析隐喻，不声称人脑等同机器学习模型；
  - 它不等于“考试有害”“成绩好的人不会创新”“中国学生都没有创造力”；
  - 正式学术邻接概念主要是 `routine expertise / adaptive expertise`、transfer、teaching-to-the-test 与评价收窄；
  - 个体截图/轶事只能作为作者原始观察与机制例，不用于估计发生率。

## 0. 核心纠偏：此前我们已经有材料，却没有把它提升为教育主机制

项目此前已经积累大量同构观察：
- “中国好学生综合征”：别人出题，我们做题；
- 有限材料、短上下文、快速收敛；
- 离开老师/主管/考试后不知道该学什么；
- 会议现场临时出题、现场收卷，而不是提前研究；
- 高学历走上领导岗位后仍把开放决策当作临场答题；
- 立项以后把方向当成考题，不重新检查问题定义；
- 大厂里 benchmark / KPI / feature list 成为新考纲；
- 独游里不会 scale down，而倾向于把缺能力翻译成“缺资源”。

此前这些被拆散在教育、组织、行业与独游章节中。

本章统一提出：
# `EXAM-OVERFIT / 应试教育过拟合`

> **长期在题目外部给定、评价标准稳定、信息边界清晰、短周期评分的环境中优化后，个体形成极强的封闭域效率；随后把这套认知与工作习惯错误泛化到题目本身不确定、评价函数未知、需要调查与反复重定义的开放域。**

这不是说受教育者“笨”，而恰恰经常意味着：
> **在训练分布内非常强，在分布外迁移不足。**

---

# 1. 与成熟研究最接近的概念：Routine Expertise vs Adaptive Expertise

Hatano & Inagaki 系列传统把 expertise 区分为：
- `routine expertise`：熟悉情境中高效、准确、稳定地执行既有方法；
- `adaptive expertise`：面对任务、方法或目标都不预先确定的新情境时，仍能理解 why / when，并重组或发明方法。

综述材料强调：两类专家可能拥有相当高的领域知识和熟练度；真正差异往往在陌生情境中暴露。

Sources:
- https://www.sciencedirect.com/science/article/pii/S1747938X14000116
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9645329/

所以我们自己的 `EXAM-OVERFIT` 更正式地可以理解为：
```text
high routine efficiency
+ narrow evaluation ecology
+ weak open-domain practice
→ routine-expertise lock-in
→ closed-domain transfer error
```

不是：
> 学会 routine skill 本身有害。

真正问题是：
> **只在 routine / rubric-known 环境中获得成功，却把这种成功误当作 general intelligence / general decision competence。**

---

# 2. 什么样的训练环境最容易产生“过拟合”？

不是“有考试”就会产生。

本项目关注的是以下条件长期同时存在：

## 2.1 `EXTERNAL PROBLEM DEFINITION`
题目由外部给定。

## 2.2 `KNOWN EVALUATOR`
存在老师、命题人、领导、评审等明确评分者。

## 2.3 `STABLE RUBRIC`
评分逻辑相对稳定，可以通过刷题、总结采分点、识别偏好来提高成绩。

## 2.4 `BOUNDED CONTEXT`
信息范围大致清楚，通常不要求自己决定“还应该去哪里找信息”。

## 2.5 `SHORT-HORIZON FEEDBACK`
做完很快得到分数、排名、对错。

## 2.6 `HIGH CONSEQUENCE OF DEVIATION`
偏离标准路径会直接影响分数、升学、资格。

长期运行后，环境会高奖励：
- examiner-intent inference；
- rapid convergence；
- template retrieval；
- parameter optimization；
- clean completion；
- answer presentation。

而较少奖励：
- problem finding；
- “我现在信息不够”；
- 延迟决策；
- 自己扩展上下文；
- 修改题目；
- 拒绝前提；
- 设计新的评价标准；
- 长期无即时反馈探索。

---

# 3. `CLOSED-DOMAIN TRANSFER ERROR`：把考试能力错误迁移到开放世界

AC-008 已经提出封闭题域迁移谬误。

本章进一步把它写成：
```text
exam success
→ self-model: I am good at solving problems
→ open-domain role
→ assumes problems are already correctly specified
→ optimizes answer before validating question
```

真正的开放问题往往先问：
- 这是不是正确问题？
- 谁说这是目标？
- 哪些信息还没搜？
- 哪个前提可能错？
- 应该先做实验还是先决策？
- 有没有理由暂时不决定？
- 这个成功标准是谁定义的？

所以：
# `PROBLEM-DEFINITION GAP > ANSWER-QUALITY GAP`

> **很多开放域失败，并不是答案写得不够好，而是根本没有先验证题目。**

---

# 4. 截图中的会议现象：`MEETING-AS-EXAM`

作者旧观察反复出现一种会议结构：

```text
leader arrives
→ asks a broad problem on the spot
→ subordinates immediately produce opinions
→ meeting seeks quick convergence
→ consensus / leader choice becomes answer
→ execution begins
```

这里并不一定存在明确恶意，也不一定只是权力压制。

更值得检验的是：
# `MEETING-AS-EXAM / 会议考试化`

> **把本应通过预研、证据搜集、方案生成与多轮比较完成的开放决策，组织成一次现场限时答题。**

其典型症状：
- 开会前不提前布置研究问题；
- 现场才知道题目；
- 默认“聪明人应该马上有答案”；
- “我需要几天查资料”被视为拖延或能力不足；
- 讨论的终点是达成答案，而不是识别未知；
- 会后执行，而非先做 cheap probe / research sprint。

这和应试习惯高度同构：
```text
题目发下来
→ 限时
→ 调用已有知识
→ 给出完整答案
→ 交卷
```

### 信息不对称不能解释全部

某些会议问题当然只是：
- 上级掌握更多背景；
- 下级不知道已有约束；
- 任务本来就只需要执行。

但如果：
- 上级自己也没有完成预研；
- 问题本身是开放决策；
- 可以低成本提前几天研究；
- 却仍长期偏好“当场问、当场定”；

则“考试化会议”是值得独立研究的组织习惯。

---

# 5. `COMPLETION OVER IMPROVEMENT`：完成答卷，而不是继续提升决策

截图里的另一类现象是：
> “只要我现在给了一个能交的方案，下次就会默认更快。”

这可以定义为：
# `ANSWER-CLOSURE BIAS / 答案闭合偏差`

> **一旦形成可提交答案，系统倾向于把任务认定为完成，而不是继续问：更多调查是否能显著提高决策质量？**

应试环境里：
- 交卷以后不能再继续查；
- 时间到就必须完成；
- 90分答案比“再研究三天可能更好”更有现实价值。

开放决策里却常常相反：
- 多一天用户研究可能改变产品方向；
- 多一个 prototype 可能推翻立项；
- 多读十个案例可能发现整个方案空间此前都错了。

所以：
# `DEADLINE TRANSFER ERROR`

> **把考试中的固定交卷时刻，迁移成所有认知工作的默认截止逻辑。**

---

# 6. `PARAMETER EXCELLENCE WITHOUT GOAL FORMATION`：中国好学生综合征的核心

作者旧命题：
> **被环境训练成参数优秀的人，而不是目的驱动的人。**

这和“应试过拟合”完全一致。

在考试中，目标函数固定：
- 分数更高；
- 排名更前；
- 正确率更高。

因此训练的是：
```text
given objective
→ optimize parameters
```

而开放创新要求：
```text
choose objective
→ inspect reality
→ revise objective
→ invent metric
→ then optimize
```

所以一个人可以：
- 学得快；
- 测试成绩高；
- 执行可靠；
- 参数调得漂亮；

却仍然缺：
- 自己找问题；
- 形成长期兴趣；
- 判断什么值得做；
- 从现实反馈中改变目标。

这不矛盾。

---

# 7. 为什么“转专业先要原专业表现好”也同构？

截图讨论的“先在原专业表现好，才允许转专业”，其隐含逻辑可能是：

```text
current track score
→ proof of worthiness
→ permission to choose another track
```

这会把：
> “你真正想学什么？”

改写成：
> “你先证明自己是一个合格答题者，才获得修改题目的资格。”

因此定义：
# `CHOICE-BY-PERFORMANCE GATE / 选择权绩效化`

其潜在后果：
- 强化 sunk-cost；
- 延迟兴趣发现；
- 鼓励在不匹配领域继续优化；
- 把“改变方向”理解成对既有评分系统的奖赏，而不是基本探索权。

美国 undeclared / flexible-major 只是可能的比较对象，不能用几个学校制度直接推出国别总论。

---

# 8. `PROJECT INITIATION AS EXAM QUESTION`：为什么会“立项定生死”

这直接连接中国游戏工业。

如果长期训练的是：
> 题目一旦发下来，下一步就是把它答好。

那么项目组织很容易自然变成：
```text
greenlight / 立项
→ question fixed
→ execution quality becomes the main variable
→ changing premise feels like failure
```

于是出现：
- 先立赛道；
- 先定 benchmark；
- 先定完整产品想象；
- 然后拼执行；
- 中途发现 premise 有问题，也更倾向于“补资源”而非“改题”。

这和028的 `SPEC PRESERVATION / RESOURCE REFLEX` 完全接通。

正式链条：
```text
EXAM OVERFIT
→ external problem acceptance
→ project-spec sanctification
→ resource reflex
→ weak scale-down / weak problem reformulation
```

---

# 9. Benchmark 为什么像“标准答案”？

后发商业游戏尤其容易出现：
```text
successful product
→ becomes benchmark
→ benchmark becomes answer key
→ feature list becomes rubric
→ production team competes on execution score
```

这不是普通借鉴。

当 benchmark 从：
> “一个值得研究的案例”

变成：
> “命题人已经告诉我们正确答案长什么样”

就形成：
# `BENCHMARK AS ANSWER KEY`

它和应试教育的认知结构高度兼容：
- 不必自己定义问题；
- 不必证明目标函数；
- 只要找到评分器认可的现成答案；
- 再用组织资源把答案做得更完整。

这也是为什么后发答案红利、数据驱动抄赛道和应试认知可能发生互相强化，而不是独立发生。

---

# 10. 为什么这对独立游戏尤其是反训练？

独立游戏的核心环境几乎与考试相反：

| Exam-like closed domain | Indie/open domain |
|---|---|
| 题目外部给定 | 自己选问题 |
| 标准答案存在 | 答案可能不存在 |
| 范围清晰 | 上下文必须自己扩展 |
| 命题人知道评分标准 | 玩家需求可能连玩家自己都说不清 |
| 时间到必须交卷 | 何时继续、何时砍掉都要自己决定 |
| 错题可以按答案订正 | 错误可能来自题目本身 |
| 高分代表成功 | demo可能证明整个方向应放弃 |

因此独立制作需要的不是更强“做题能力”，而是：
- `PROBLEM OWNERSHIP`；
- `REFERENCE REPERTOIRE`；
- `RESEARCH BEFORE COMMITMENT`；
- `THESIS-PRESERVING SCALE DOWN`；
- `CHEAP PROTOTYPE`；
- `REALITY ADJUDICATION`；
- `GOAL REVISION`。

这正好解释为什么：
> **商业游戏中的高绩效员工，未必自动拥有独立游戏所需的开放域能力。**

---

# 11. “最适合做独游的人不是技术专家”为什么可能成立？

用户旧观察中提到：
- 一些技术全能的“好学生”做飞行射击/学生作品时，乐趣与成绩不成比例；
- 一些独游作者初始技术并不完整，却是资深玩家，先判断方向，再现学引擎或补技能。

这不能推出：
> 技术不重要。

更准确的模型是：
```text
REFERENCE / TASTE / PROBLEM JUDGMENT
→ choose tractable thesis
→ acquire missing skill just-in-time
→ prototype
```

对比：
```text
high generic skill
→ no strong self-authored problem
→ reproduce familiar product grammar
```

所以：
# `SKILL ACQUISITION AFTER THESIS`

> **在独游里，一部分具体技能可以后补；但“玩过什么、想做什么、为什么值得做”的判断资本更难在立项后临时生成。**

这与 The First Tree、Gunpoint、Pope 等能力塑形案例相容，但不能把所有成功作者都归为“技术差的资深玩家”。

---

# 12. 游戏玩得少为什么会让“应试过拟合”更加严重？

031/028 已提出 reference repertoire。

现在可以得到更完整的乘法：
```text
EXAM-OVERFIT
×
NARROW REFERENCE REPERTOIRE
×
COMMERCIAL BENCHMARK REINFORCEMENT
=
STRONG ONTOLOGY LOCK
```

应试过拟合让人倾向寻找“正确答案”。

游戏阅历窄则意味着：
> **可供选择的答案样本本来就很少。**

商业大厂再不断重复少数成功模板：
> **其中一个局部答案就会被强化成“游戏本体”。**

所以“不广泛阅读 / 不广泛玩游戏 / benchmark化 / 不会scale down”不是四件孤立问题。

---

# 13. `SHORT-CONTEXT INTELLIGENCE`：有限材料速答为什么会被误认成通用聪明

作者旧讨论曾把应试环境概括为：
> 有限材料速答。

这可以操作化为：
# `SHORT-CONTEXT PERFORMANCE`

擅长：
- 在给定材料里迅速提取；
- 识别题型；
- 组织完整回答；
- 时间压力下收敛。

开放研究则需要：
# `LONG-CONTEXT MODEL BUILDING`

- 长期积累跨域知识；
- 知道当前材料不够；
- 主动找外部一手资料；
- 容忍几天/几周没有完整答案；
- 让模型在证据进入后持续改变。

所以：
> **“现场答得快”与“最终判断质量高”不能视为同一个能力。**

这正是截图中“不开会前预研、现场硬想”的核心问题。

---

# 14. 应试教育为什么可能“抬底部、卡顶部”？

华东师大2023综述非常适合作为边界材料：
- 没有足够证据简单断言中国学生总体创造力低；
- 但作者认为应试教育可能对拔尖/高创造力学生造成更明显约束；
- 候选机制包括知识宽度/深度、冒险质疑精神、不确定容忍和内在动机。

Source:
- https://xbjk.ecnu.edu.cn/EN/10.16382/j.cnki.1000-5560.2023.04.006

这与“过拟合”模型并不矛盾。

统一解释：
```text
standardized training
→ raises routine floor
→ improves comparable execution
→ narrows variance / exploration for some cohorts
→ top-end adaptive / divergent capability may face higher opportunity cost
```

这里必须保留：
> **“可能”“特定群体”“机制候选”，不能升级成已证明全国因果。**

---

# 15. Teaching-to-the-test：为什么“分数涨了”也不能自动证明广义学习涨了？

教育研究长期担心：
> 针对具体测验的训练可能提高该测验表现，却把教学资源从更广泛理解与问题解决移开。

一项研究直接比较了 test-specific preparation 与更广泛测试表现，明确把“test score improvement是否代表general learning”作为独立问题。

Source:
- https://www.sciencedirect.com/science/article/pii/S0738059321000754

这给 `EXAM-OVERFIT` 一个重要方法边界：
> **训练集成绩必须和跨任务迁移表现分开测。**

不能用：
- 高考高分；
- 名校学历；
- 大厂绩效；
- KPI完成；

直接替代：
- open-ended research；
- original problem framing；
- founder judgment；
- indie 0→1。

---

# 16. 组织为什么会继续复制这种认知结构？

因为这种人并不是“没用”。

相反，他们往往：
- 可预测；
- 交付稳定；
- 执行快；
- 接受清晰目标；
- 对指标敏感；
- 擅长高强度竞争。

大型组织非常需要这些能力。

于是可能形成：
# `ROUTINE-EXPERTISE PROMOTION LOOP`

```text
school rewards rubric performance
→ firm hires credentialed high performers
→ firm rewards execution against KPI
→ high performers become managers
→ managers reproduce exam-like task structures
→ next generation trains under same logic
```

这解释截图中的一个关键直觉：
> **高学历升成领导以后，认知方式未必自动从“答题”升级成“命题/研究/判断”。**

角色升级 ≠ 认知制度升级。

---

# 17. 父权 / 权力不是替代解释，而可能是放大器

截图中也出现“父权/家族式权力混入形式权力”的讨论。

本章不把所有现场决策归因于考试认知。

更可能存在交互：
```text
examiner-subject habit
+ paternal authority
+ organizational hierarchy
→ leader expected to know answer
→ subordinate expected to answer immediately
→ admitting uncertainty becomes status loss
```

因此：
- 权力结构决定谁有资格出题；
- 应试过拟合决定大家默认怎样对待题目；
- 父权文化可能提高“上级必须显得知道答案”的压力。

这是三个不同变量。

---

# 18. 反例：为什么不能把它写成“中国人天生不会开放问题”？

项目已有大量内部反例：
- DeepSeek / 梁文锋：frontier problem ownership；
- NExT：小队demo、100人日review、逐级资源；
- 66RPG：hobbyist self-directed making；
- CUSGA / 中传：大量学生完成完整作品；
- Game Science / 4A / Supergiant等不同路径说明工业技能可以被重新组织。

所以真正问题是：
# `DISTRIBUTION OF ADAPTIVE PRACTICE`

> **一个社会有多少人，在成长过程中反复接受“题目不确定、答案不唯一、必须自己找证据并允许重写目标”的训练？**

不是：
> “这个民族会不会思考。”

---

# 19. 如何真正测量“应试教育过拟合”？

不能问：
> “你觉得应试教育害了你吗？”

应该设计迁移任务与真实行为指标。

候选维度：

### A. Problem framing
给一个模糊业务/设计问题，看是否先重写问题而非立即答。

### B. Information acquisition
是否主动指出缺信息、寻找外部资料、要求时间。

### C. Evaluation creation
能否自行提出成功/失败标准。

### D. Premise rejection
能否指出上级/题目本身可能错误。

### E. Delayed closure
是否能接受“今天不下结论”。

### F. Cheap experiment
是否用prototype / research sprint换信息，而不是继续争论。

### G. Goal revision
新证据进来后是否愿意改目标而非只修答案。

### H. Cross-context transfer
在新领域能否迁移原理而不是复制表面模板。

然后才比较：
- 不同教育经历；
- 不同公司经历；
- 学生/普通员工/manager/founder；
- 中国内部不同地区/学校；
- 日本/台湾/韩国/美国等comparators。

---

# 20. 对游戏行业研究的直接修改

以后研究中国策划/制作人，不只记录：
- 职级；
- 项目；
- 技能；
- decision rights。

还记录：
- `problem_source`：问题是谁提出的；
- `research_latency`：问题提出后多久开始决策；
- `context_expansion`：是否主动找外部资料；
- `prototype_before_commitment`；
- `premise_revision_count`；
- `benchmark_role`：reference还是answer key；
- `meeting_as_exam`；
- `answer_closure_bias`；
- `goal_revision_evidence`；
- `adaptive_practice_history`：jam / mod / research / hobby making。

这样才能把“执行强/原创弱”从情绪判断变成可观察行为。

---

# 21. 对第四次工业革命的含义

AI会进一步削弱 routine-answer production 的稀缺性。

如果：
- 标准代码；
- 标准文案；
- 标准分析；
- benchmark总结；
- 常规方案生成

越来越便宜，那么价值更集中到：
- 提什么问题；
- 找什么证据；
- 哪个答案不该信；
- 何时不做；
- 如何设计现实实验；
- 如何把不同领域reference重组。

因此：
# `AI PUNISHES CLOSED-DOMAIN OVERFIT`

不是因为AI让考试知识“没用”，而是：
> **当标准答案生产被自动化，无法自主定义问题与更新目标的人，其比较优势会下降。**

这与本项目此前“AI负责更多答案，人负责问题与现实裁决”的方向一致。

---

# 22. 当前最小结论

> **“应试教育过拟合”是本项目对中国好学生综合征更上游、更统一的机制描述：一个系统长期奖励外部出题、稳定rubric、有限上下文、快速收敛与按时交卷，可以生产极强的routine expertise，却不保证adaptive expertise。真正的产业风险发生在这种封闭域高表现被错误外推到开放决策：会议被组织成现场考试，立项被当成题目冻结，benchmark变成答案册，缺资源替代改问题，完成答卷替代持续研究。中国商业游戏工业随后可能进一步奖励这种能力，于是教育形成与行业版本产生连续性。独立游戏则处在几乎相反的任务分布：题目要自己找、上下文要自己扩、答案可能不存在、现实反馈可以推翻目标。因此老中研究以后不能只问“执行为什么强、原创为什么弱”，而必须测 TRAINING-DISTRIBUTION FIT：一个人在什么题域里被训练得很强，这套能力又被错误泛化到了哪里。**