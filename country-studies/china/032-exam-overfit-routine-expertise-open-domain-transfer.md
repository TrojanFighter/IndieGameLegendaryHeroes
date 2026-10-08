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

**教育方法增量（2026-10-08）：** [034 — 认识论规训、遗制权威与知识载体污染](034-epistemic-discipline-authority-legacy-and-knowledge-aversion.md) 把 `RUBRIC-AS-TRUTH`、`JUDGMENT-RIGHTS DECOUPLING`、`KNOWLEDGE-CARRIER AVERSION` 独立为待检验假说，并提出以历史决策节点/同期史料取代人物表彰式标准答案的教学对照协议；区分“反对说教”与“证据能力已经形成”。

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


# 22. FULL-CYCLE AUTHOR PRACTICE：技术任务熟练，不等于经历过完整的作者循环

本节只补“训练任务的实际分布”这一增量，不重复[作者筛选制度比较050](../../book/research-notes/creator-selection-institution-comparison-050.md)的企业门槛、greenlight和IP/退出权。

一名专业人士可以很熟练地完成被分配的关卡、代码或美术任务，却从未经历以下整轮工作：

1. 自己提出一个值得验证的玩家体验问题；
2. 将它压成能力与时间允许的小型可玩原型；
3. 向真实玩家交付并观察预期外的反馈；
4. 根据现实证据保留或推翻原始目标；
5. 独立裁定做与不做，并为结果保留可复用的知识与作品。

这称为 **FULL-CYCLE AUTHOR PRACTICE / 全周期作者练习**；**不是**“每个人必须兼任所有专业岗位”。多人分工团队也可能共同经历完整作者循环。

*教育实验线索*：
- **S1（2023）** Riikka Aurava与Kati Sormunen：系统性综述汇集2010–2022年25篇Game Jam原始研究，归纳跨学科知识、认知与元认知、社交及实践技能的可能学习收益；同时指出研究场景异质，不能将jam自动等同于长期能力形成。原文：https://www.sciencedirect.com/science/article/pii/S2666557323000071
- **S1（2026-06-19发表；2026-08-31正式版本）** Arya与Bani-Taha：以一处GGJ站点的回顾性访谈研究Game Jam如何连接业余/正式教育与职业经验；受访者把从idea到working prototype的全流程经验视作重要收益。研究明确承认单站点、自述回忆、缺乏雇主和指导者访谈的限制；**不能**推算“参赛者几年后成为职业主创”的胜率。原文：https://link.springer.com/article/10.1007/s44217-026-01810-5
- **S1（2021）** Aurava、Meriläinen等在芬兰普通高中环境的研究：Game Jam可嵌入正式教育，但资源、教师能力、非竞技性和包容设计影响参与门槛与体验，不能将高强度jam浪漫化为人人适用的教育替代品。原文：https://www.sciencedirect.com/science/article/pii/S2212868921000192

**核心边界**：一次48小时活动的完成度 ≠ 可持续作者能力；持续做项目的能力还取决于家庭经济、时间、合作网络、作品署名、受众与重试机会。此处仅说明“训练目标”和“训练格式”可能不同，并未估计中国与欧美参与者的形成率差异。

---

# 23. 两次不同的筛选：有没有形成能力，以及有没有资格使用能力

必须将教育与组织选择明确分开：

- **FORMATION GATE / 形成关**：学生或员工是否真实获得过自定题目、外部取材、原型验证、目标修正的完整练习机会？
- **AUTHORITY GATE / 授权关**：当他已经做出证据充分的作品后，是否有资格发起下一轮原型，掌握核心方向、争取资源并在失败后再次尝试？

二者不能互为代理。存在专业执行很强但尚无完整作者练习的人；也存在已建立作者能力，却长期缺少组织内创作授权的人。

### 可证伪的研究变量

| 字段 | 不应只问 | 应测量 |
|---|---|---|
| FORMATIVE TASK DISTRIBUTION | 从业多少年、毕业于哪所学校 | 做过几次自己定义题目并完成全循环的原型 |
| GOAL REVISION UNDER FEEDBACK | 善不善于写方案 | 出现反例后曾否主动改变目标、删去原定功能 |
| ARTIFACT-TO-RIGHTS CONVERSION | 有多少优秀Demo | 哪些Demo作者获得团队、持续项目权、署名和后续再尝试权 |
| SECOND-ATTEMPT SURVIVAL | 是否曾参与成功产品 | 失败后能力、关系、资金与原型通道有多少被保存 |
| NEGATIVE CONTROLS | 学历高/低、中资/外资 | 控制职业、家庭资本、项目类型、入行年代、领域知识和组织规模 |

这里的竞争性解释包括行业成熟商业函数、组织治理、招聘结构、平台市场条件、家庭与个人经历。**不能因为“应试结构”和“执行者困在原岗位”同现，就断定前者已被证明造成后者**；也不能以一家特殊孵化部门的存在反推全行业数量级。

与[050](../../book/research-notes/creator-selection-institution-comparison-050.md)、[048 能力复制陷阱](../../book/research-notes/capability-reproduction-trap-horizontal-discovery-048.md)及[中国023创作者阶层再生产](023-creator-class-formation-intergenerational-reproduction.md)联动。

---

# 24. 当前最小结论

> **“应试教育过拟合”是本项目对中国好学生综合征更上游、更统一的机制描述：一个系统长期奖励外部出题、稳定rubric、有限上下文、快速收敛与按时交卷，可以生产极强的routine expertise，却不保证adaptive expertise。真正的产业风险发生在这种封闭域高表现被错误外推到开放决策：会议被组织成现场考试，立项被当成题目冻结，benchmark变成答案册，缺资源替代改问题，完成答卷替代持续研究。中国商业游戏工业随后可能进一步奖励这种能力，于是教育形成与行业版本产生连续性。独立游戏则处在几乎相反的任务分布：题目要自己找、上下文要自己扩、答案可能不存在、现实反馈可以推翻目标。因此老中研究以后不能只问“执行为什么强、原创为什么弱”，而必须测 TRAINING-DISTRIBUTION FIT：一个人在什么题域里被训练得很强，这套能力又被错误泛化到了哪里。**


---

# 25. JUDGMENT DEVALUATION：将不确定性决策误判成随机/投机（2026-10增量）

## 25.1 作者新增观察与独立理论命题

作者指出的现象不只是“应试精英缺乏模糊决策能力”，而是**部分封闭题域高绩效者会在价值与方法上贬低这种能力的存在**：数学/考试式、快速确定对错的hard skill才算真本事；涉及概率、模糊目标、市场时机、作者审美、可逆转向的判断被笼统归为运气、投机或事后归因；错误立项时则主张“失败以后再选就行”。

定义工作术语：
- `CERTAINTY-SKILL BIAS / 确定性技能崇拜`：误把有唯一标准答案/短期可评分，当作衡量全部专业能力的标准。
- `JUDGMENT DEVALUATION / 决策能力贬值`：将可学习、可校准、可审计的概率判断与深度不确定性决策，错误归入不可评价的纯随机。
- `RESIDUAL-AS-LUCK / 把模型残差归因于运气`：仅凭粗粒度范式解释成败，遗漏变量一律视作噪声，拒绝校正自身领域知识或模型。
- `RESELECT FALLACY / 重新选择即重置谬误`：认为失败后再选便能回到首次选择前状态，忽视沉没投入、不可逆专用技能、人员、发行窗口、团队信任与资本机会成本。

**注意**：这是作者对某些交谈与职场经验提出的机制假说，不是对“中国高学历者”或任何学校毕业生的已测定普遍属性；职业、产业、家庭与企业激励可能共同作用。

## 25.2 必须区分五层任务，而不是“确定技术 vs 纯运气”二分

1. **确定性求解**：规则完整、存在可靠标准答案，重在推理/执行。
2. **可估计风险决策**：已知或能合理估计概率及损失，重在收益/风险/校准。
3. **不确定条件下预测**：对未来事件作概率预测，通过长期校准与区分能力评价。
4. **深度不确定性决策**：未知选项、市场与概率，重在试验、控制可承受损失、获取信息、保留转向余地。
5. **创造性问题/目标定义**：决定何种体验或新市场值得被创造，重在跨领域知识、作者目的、原型检验与动态修改目标。

训练/评分方法不可互推。不能因为第五类无法事先证明成功，就宣称它不具备专业性；也不能因为有人作出大胆判断，便免除后续证据责任。

## 25.3 外部理论与可直接利用的证据

- **Frank H. Knight（1921）风险与真正不确定性**：不能计算精确风险的决策仍然是创业判断和组织能力的重要研究对象。1921原著： https://www.econlib.org/library/Knight/knRUP.html 。现代澄清Westgren & Holmes（2022）：https://link.springer.com/article/10.1007/s40926-021-00183-z 。
- **Baron & Hershey（1988），Outcome Bias in Decision Evaluation**：5个实验显示，被试在对决策前信息相同的情境，仍因结果好坏评价思考质量与人更好/更差。说明单次成功/失败不能充分测量当时的决策质量。 https://pubmed.ncbi.nlm.nih.gov/3367280/ 。
- **Mellers等（2014），Psychological Strategies for Winning a Geopolitical Forecasting Tournament**：多大学两年预测竞赛中的概率训练、团队讨论与跟踪改进概率校准和辨别力；反驳“未来不确定=预测只有运气”，但不能把地缘事件预测实验直接外推成游戏原发范式的预测准确率。 https://www.psychologicalscience.org/journals/psychological-science/0956797614524255/ 。
- **Sarasvathy（2001），Causation and Effectuation**：在创业未知环境中可从已有手段/伙伴/可承担损失开始创造机会，而非一定先预测最优市场目标。该论文主要建立理论框架，不当作已证实的国别成功率。 https://journals.aom.org/doi/10.5465/AMR.2001.4378020 。
- **Dixit & Pindyck（1994），Investment under Uncertainty**：不可逆投资下保留等待/实验选择权有价值，重选不是时光倒流。https://press.princeton.edu/books/paperback/9780691034102/investment-under-uncertainty ；检索版 https://www.jstor.org/stable/j.ctt7sncv 。
- **Klein等，Recognition-Primed Decision**：资深消防指挥员能利用丰富领域图式作快速情境判断；快决策可以是高水平专业能力，但必须区分经验型快速识别与缺乏领域积累的拍脑袋。原研究重刊：https://journals.sagepub.com/doi/10.1518/155534310X12844000801203 。

## 25.4 与2K模型相连：模型无法表达的不是全部随机

```text
narrow reference repertoire + high closed-domain score
→ confidence in simple familiar rubrics
→ complex rationale treated as poor communication / unnecessary
→ unexplained business outcomes assigned to chance
→ little motive to expand knowledge or learn probabilistic judgment
→ choice-making rights remain concentrated despite weak model
```

这条是机制推演而非已识别的教育因果。与“2K内存”概念的关系是：**有效领域图式/外部记录/团队知识集成不足**，而非人体硬件容量真的等于2K或学历越高硬件越差。

识别关键反例：高水平领域专家有时也用极短规则迅速决策，但可交代何种经验支撑规则、何种信号说明规则失效。判断是否“2K”不能看PPT页数/脑图尺寸，要看**是否识别反例与未纳入变量**。

## 25.5 必须分开评价事前质量、事后结果、学习能力

- **EX ANTE DECISION QUALITY**：作选择当时掌握的证据、假设、已知风险、低成本检验以及可接受损失。
- **EX POST OUTCOME**：作品最终结果；仍需时间尺度、市场条件及可比项目基准。
- **CALIBRATION / LEARNING**：同类多次判断中，概率是否校准、能否主动更新信念、避免自我保护式事后归因。

同理：优秀决策可能遭遇失败，不良决策可能幸运成功；但长期结果也不可被无限用“运气”忽略。

## 25.6 下一轮测量实验

对持有真实决策权的人使用同类游戏提案，要求：
1. 预先记录“成功/失败信号、关键变量、假设被推翻条件”；
2. 对预期结果以概率或区间表达不确定性，而不是要求每次唯一正确答案；
3. 允许有成本的查资料、采访玩家、做demo或等待以取得信息；
4. 在补充反证后决定继续、删减、停项或改写目标；
5. 复盘时盲化最终市场结果，先评估当时的判断，再观察长期预测准确率；
6. 固定同口径分母比较教育经历/原型经验/职位/组织权限，不用少数精英的轶事推国家差异。

## 25.7 与中国普通作者PABL的具体连接

[研究054（内购人生PABL）](../../book/research-notes/pabl-solo-author-scope-down-career-054.md) 2018第一手访谈指出作者先测试搜索机制可行，再据已有阅读写作/PS资源主动缩小范围，未知商业结果时仍完成并发行。《前程似锦》是**不确定条件下主动管理可控变量**的例子，不是证明他事先准确预测销量。第三作至2026能观察到作品延续，但其生存资金、就业与失败路径未知；不可将持续发售误写成“决策总是正确”。

---


---

# 26. 决策能力的合法性：为什么“只有确定答案才算硬功夫”可能阻断作者培养

本节续第25节 `JUDGMENT DEVALUATION`：新增的不只是“谁能作出模糊决策”，更是**谁承认在不确定性条件下仍存在可学习、可评估、可负责的专业判断力**。以下为作者提出的解释框架及可核反例，尚无证据支持将该态度归因于中国所有高学历者。

## 26.1 知识处理、理性信念和决策目标必须分开

**Keith E. Stanovich（1994）：Dysrationalia**，独立于智力测验成绩的理性信念与合理行动能力，不能把高智力/成绩直接视作理性决策的充分条件。原文：https://journals.sagepub.com/doi/10.3102/0013189X023004011；Stanovich & West（2014）关于 IQ≠RQ 的研究摘要：https://eric.ed.gov/?id=EJ1032814 。

本项目进一步提出 `COMPETENCE-LEGITIMACY OVERFIT / 能力合法性过拟合`：当长期评分生态只承认存在清晰答案、短期可判对错的技能，参与者可能误认“不能立刻给出唯一正确解”的审美、市场、创业、战略判断只是运气/投机。**这是机制假说而非Stanovich本人对中国教育的结论**。它与第25节的“具体决策能力不足”不同：这里指**否认别人拥有可学习的决策能力**，进而影响人才选拔与资源配置。

**Kahneman与Gary Klein（2009）**《Conditions for Intuitive Expertise》，将真正可训练专家直觉的两个重要条件限定为：
- 环境中存在可学习的规律（不全是随机且非完全不可预测）；
- 判断者有充分、有效的反馈以习得规律；
主观自信不是准确性的可靠指标。https://doi.org/10.1037/a0016755 。

故“秒懂／一页报告”既可能是多年专业模式学习后的高质量压缩，也可能是稀疏知识下的低质量拟合。**不能通过报告篇幅、决策速度或职级判断是否有‘2K瓶颈’；必须观察模型失效边界、推翻条件和反馈校准。**

## 26.2 决策不仅是“预测答案”，还包括控制行动的不可逆性

**Bezos 2015、2016亚马逊股东信**分别提出one-way（高不可逆，慎重）与two-way door（容易回退，快速试验），并指出高质量、高速度决策须能及时校正而非要求每次收齐全部资料。2016信“70%”仅是管理经验法则，不能变成游戏研发投入的定量通过线。
- 2015：https://ir.aboutamazon.com/files/doc_financials/annual/2015-Letter-to-Shareholders.PDF
- 2016：https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders

由此修正第25节“再选谬误”：**并不是重新选择总错误**；在低成本可逆的试验中，快速重选就是好决策。错误是误以为已经招聘大团队、投入多年、产生项目专用资产、丢失窗口之后，下一次选择还能回到原始状态。

真正的模糊决策技能至少包括：问题定义、获得新信息、建立小试验、限制损失、管理可逆性、识别异常、概率校准，以及保留继续选择的经济/心理/组织空间。

## 26.3 LocalThunk：学校分数不代表作者形成，设计先例的缺席有时也是主动决策

**P0作者第一手博客（2026-02-20）《Bad Grades》**：https://localthunk.com/blog/bad-grades

- 其原机械工程成绩尚可，但为追随编程兴趣在接近毕业时转到计算机科学，部分课程勉强及格；课外则长期编写模拟程序。
- 曾花两年多制作未完成、未命名的战略模拟游戏，回顾时仍将其视为自己坚持创作十年的重要训练；不能以学分/毕业时间/首个作品是否发售评价这段作者能力形成史。

**P0作者个人开发年表（2025-03-06）**：https://localthunk.com/blog/balatro-timeline-3aarh

- `Balatro`始于2021-12私人朋友间纸牌游戏，随后迭代为单人机制实验；不是先做成熟赛道数据选择。
- 作者**有意识回避同类Roguelike/Deckbuilder**，为了保留“自己探索、犯错、重复造轮子”的兴趣，并明确承认此举不等于商业最优；2023-05出于手柄操作研究才首次玩《Slay the Spire》。
- 2022年有朋友投入几十小时试玩，令作者调整范围；2023年因迁居离职、已有储蓄而短期全职3–6个月，并不表明人人都可无成本全职独游。
- 2023-05底Steam仅48愿望单；2023-06底通过小主播、社区反馈及发行商接触，才形成更新的商业判断；不能后验编造作者一开始准确预测数百万销量。
- 作者的后来成功需考虑伙伴支持、个人时间资本、外部传播与运气；本人2025-09《I’m Slow》反思了冲刺工作带来的倦怠：https://localthunk.com/blog/im-slow 。

**解释：`DELIBERATE REFERENCE ISOLATION`（有意识参考隔离）**≠被动信息茧房。前者拥有实践经验和查找渠道，选择暂时不吸收特定类型惯例并持续接受现实反馈；后者可能不知道有哪些选择或否认其他路径的合法性。**广泛知识储备对作者可能有益，但不是要求所有创作者在新项目构想阶段先玩遍同一赛道的唯一正确流程。**此人是幸存者，不能由成功反推主动回避参考必然提高成功率。

## 26.4 两个普通失败者：作者自主权不等于判断能力、完成作品不等于经济存活

**P0开发者本人 2024-04《Zofia — Post Mortem》**：https://itch.io/blog/716710/zofia-post-mortem

- 原始构想是本地合作RPG需求；团队多轮改动魔法、美术与对话系统，美术路线更换约使项目多两年工作量，局部意见不断冲淡核心设计支柱。
- 抢先体验时作品完成度与用户预期错配，测试反馈不充分且影响士气；作者回顾发现本地合作实际使用比例很小。
- 案例说明即使**有权自发题、允许充分讨论**，若缺少系统耦合分析、范围控制、阶段性止损和准确市场反馈，也会失败。不能把失败简单归类为创作者不够勇敢或仅仅市场随机。

**P0开发者本人 2020《Rose Seed Replica postmortem》**：https://lezliz.itch.io/rose-seed-replica/devlog/179880/rose-seed-replica-postmortem-mistakes-were-made

- 作者自报约三年开发及生活维持成本超过€26,000，首周卖130份、约€1,000收入；成本含最低生活与基础设施，不是单项制作预算。
- 资金来源包括政府创业支持、零工和私人存款，不能省略其存活条件；作者详细反思分支内容过多、工期低估、营销入口不足，发售前只有268个愿望单。
- 这是**有个人目的主权、能完成作品，但没建立可持续商业判断与资本约束**的案例。失败者一手账本应同《Balatro》作者时间线并列分析，不能只讲后来成功者如何“早有洞见”。

## 26.5 三案例加中国普通作者PABL的最小比较

| 案例 | 有证据的决策行为 | 已知结果 | 禁止后验推断 |
|---|---|---|---|
| PABL《前程似锦》2017–18 | 自主提出搜索调查玩法，测试可行性，现学编程缩小范围 | 首作完成、2019/2026仍有后续作品 | 连续全职/净利润/早期销量预测正确 |
| LocalThunk《Balatro》2021–24 | 业余长期实验、有意识参考隔离、依据试玩与商业信号渐增投入 | 成功上市，市场远超初期预期 | 事先看准赛道、回避学习同类作品是成功原因 |
| 《Zofia》2024复盘 | 有原创目标与协作授权，但未控制范围及产品/反馈时机 | 完成1.0，未达作者商业预期 | 所有充分授权的团队都不擅长项目管理 |
| 《Rose Seed Replica》2020复盘 | 明确作者目标，最终完成，但制作估时与需求判断不足 | 作者自报严重财务失败 | 原创内容没价值、后续一定失败 |

以上四例是**机制对照，不是代表性国别样本**。与第25节的 `EX ANTE DECISION QUALITY / EX POST OUTCOME / CALIBRATION` 三层相连：不同案例都能贡献对失败成本、反馈机会与判断质量的理解，只有足够完整的时间线与当时可得信息，才能避免结果偏差。

## 26.6 对作者传记与企业评价的四项补充字段

- `COMPETENCE_LEGITIMACY`：管理者承不承认独立判断/概率/体验取舍是可检验的职业技能？
- `VALID_FEEDBACK`：当事人是否在有规律环境中反复获得明确反馈？何时转入新领域，经验是否失效？
- `REVERSIBILITY_AUDIT`：每项关键决定会损失多少现金、人员、时间与后续选项？
- `REFERENCE_POLICY`：主动隔离已有范式、广泛参考、还是被动信息缺失？是否能在需要时主动搜索和修正？

**本轮最小结论：确定性执行、开放问题理性和作者实践是交叉而不等同的能力；更危险的不是某个人不会预测，而是其拥有资源裁决权时，否认专业决策判断可被训练、且把自己既有的封闭评分器推广为唯一合法的能力标准。**

---


# 27. 谁评判新作者：创意预测能力与证据阶段（2026-10-08增量）

本节从第25–26节的“模糊决策能力被贬值”推进到独立的**创意预测／创意鉴别能力**（creative forecasting / idea selection）。作者先前对高校应试精英、管理者认知容量、同行霸凌与创新者识别困难的观察是待测机制，**不能直接当作国别群体平均差异的证据**。

## 27.1 管理者不一定比真正参与创作的人更会识别新创意

**S1：Justin M. Berg（2016），《Balancing on the Creative Highwire》，Administrative Science Quarterly。** 339名马戏创意行业从业者预测新演出的观众评价，并用13,248位观众反馈评估预测准确性；研究还包括实验。发现：**创作者预测别人的新创意时比管理者准确，但评价自己的创意时未保持优势；过去偶然成功的低质量创意也会削弱这种优势。** 实验支持角色训练的解释：创作者通常兼有发散（生成）和收敛（筛选）练习，管理者可能长期主要练习收敛评估。领域为马戏，**不是已测的中国游戏策划，亦非“所有经理都不如作者”。**
- 一手学术摘要：https://www.gsb.stanford.edu/faculty-research/publications/balancing-creative-high-wire-forecasting-success-novel-ideas
- 期刊：https://doi.org/10.1177/0001839216642211

**S1：Mueller, Melwani & Goncalo（2012），《The Bias Against Creativity》，Psychological Science。** 两项实验操纵对减少不确定性的动机，发现人们即使表面赞成创造力，也可能在希望消除不确定性时产生隐性反创造力偏差，且影响识别创造性方案的能力。该实验不能估计中国教育造成多少百分点的偏差，但提供“口号支持创新 ≠ 真实判定能力”的可实验机制。
- https://www.psychologicalscience.org/journals/psychological-science/0956797611421018/

**S1：Berg（2019），《When Silver Is Gold》，OBHDP。** 五项实验中，参与者评价自身尚未完成的创意，往往低估最有潜力的初始方案、将后来最好的选项排第二；提高抽象层次的评估方式可改善。**不能认为创作者自己对自己永远最准。**
- https://www.gsb.stanford.edu/faculty-research/publications/when-silver-gold-forecasting-potential-creativity-initial-ideas

## 27.2 数量级压力测试：专家项目评审与完成稿评审不必同方向

| 场景 / 研究 | 观察规模 | 主要结果 | 不能推出 |
|---|---|---|---|
| 医学科研项目申请（Boudreau、Guinan、Lakhani、Riedl 2012/后续论文） | 142名专家、150份提案、**2,130随机匹配评价** | 方案新颖性增加1个标准差，预期排名下降约4.5个百分点；认知距离/理解问题可能重要 | “所有专家审查总是惩罚新颖性” |
| 科学期刊完成稿（Teplitskiy、Peng、Blasco、Lakhani 2022《PNAS》） | **49期刊、27,323份投稿**（20,538生命科学+6,785物理科学） | 论文新颖性最高五分位录用概率较最低五分位高约**6.5个百分点**（摘要的模型口径）；“常规性”同时也正相关 | “投稿录用=早期项目容易取得经费”；不能认为所有机制厌恶新颖性 |

- 项目随机评审研究：https://dash.harvard.edu/entities/publication/73120378-ab5f-6bd4-e053-0100007fdf3b ；后续同行评审文章：https://pmc.ncbi.nlm.nih.gov/articles/PMC5062254/
- PNAS：https://www.pnas.org/doi/10.1073/pnas.2118046119

**核心区分**：early proposal ≠ working prototype ≠ completed artifact。事前未知越大，概念陌生且评审者缺少相关领域图式时，可能更难识别价值；作品可验证性提高后，新颖性不必然受到惩罚。两项研究的领域、评价单位和新颖性测量方法不同，差异不能未经识别就全部归因为“从提案到成品”的时间效应。

## 27.3 游戏一手误判对照：不要用结果成功直接谴责当时评审人

**P1：吉田修平2012-02-10《Game Informer》访谈** https://gameinformer.com/b/news/archive/2012/02/10/shuhei-yoshida-interview

索尼当年拒绝承担《Demon's Souls》欧美发行，吉田修平承认失误。他回顾曾试玩接近完成的版本约2小时仍卡在开头，形成负面印象；同时说明早期版本帧率和网络功能有问题，无法清晰展示最终体验。Atlus与Namco接手相应地区发行。

这可以分为：**A.作品阶段展示/Vertical Slice未充分呈现产品价值；B.评审者未有效识别潜在体验价值。** 不能从后来成功推出当时那个有技术问题的版本已十分优秀；也不能把日本大企业一次误判推导成中国或西方的比例结论。

## 27.4 与应试过拟合／2K模型的精确关系

机制假说：

\`\`\`text
长期在外部题目/单一评分器中获得高绩效
→ 将可快速给出答案视作唯一合法技能
→ 既无充分原创实践，也没有对新创意的校准记录
→ 倾向以既有作品相似性替代未知创意价值
→ 取得项目否决权后将自身理解困难误判为“创意没有价值”
→ 原型机会受限，后续作者训练与评价分母进一步收窄
\`\`\`

但必须同时测试**逆向机制**：有些组织可能激励实际新颖性；资深经理可能拥有更好的预算纪律/跨项目风险管理；创作者可能高估自己的创意；方案被拒绝可能因为测试条件、资金和技术问题，而非“领导2K”。

**以评审人的履历/职级替代 creative-forecasting 记录，是当前作者研究应警惕的外生代理变量错误。**

## 27.5 训练和鉴别的建议，不要再陷入“只换一套评分器”

对初学者保留低成本原型入口；对成熟创作者可用**盲评可玩作品→作者解释玩家体验目标→小额实验→观众行为→记录事前判断及否决理由→追踪下一次提案**。

最需要追踪的是：评审者对不同作者的预测是否在长期得到校准；新颖作品被拒后是否存在低成本证伪机会；多次失败者是否展现可观察的学习和有效重构。单个名校/海外履历、经理简历、一次销量或一次投票**都不构成原创鉴别能力的充分证据**。

与[研究050](../../book/research-notes/creator-selection-institution-comparison-050.md)、[研究051](../../book/research-notes/double-fine-amnesia-public-pitch-cohorts-051.md)及[普通作者PABL研究054](../../book/research-notes/pabl-solo-author-scope-down-career-054.md)联动。固定比较时点、提案分母和重复进入的作者，不能只访成功作品与高曝光工作室。

---


---

# 28. 决策节奏过拟合：开放问题为何被做成现场收卷？（2026-10-08增量）

这一节不另立“中国人不会决策”的并行理论，而是在 `EXAM-OVERFIT` / `MEETING-AS-EXAM` 基础上，补入一个此前没有真正量化的维度：**组织究竟如何决定“什么时候回答、什么时候还应该研究”？**

## 28.1 `DECISION-TEMPO OVERFIT / 决策节奏过拟合`

作者提供的交流材料显示一种待验证的日常组织行为：

- 模糊而重要的问题直到会议开始才交给相关人员；
- 参与者在缺少资料与预研的条件下现场给出方案；
- 上级把“很快能得到一个答复”视为工作效率；
- 在非紧急情境下，主动申请更多调查、比较与试验时间的建议仍难被理解；
- 当一份方案可以提交时，知识工作就被认定为已完成。

这不是纯粹的权力压制，也不是“某位管理者性格差”的充分证据。问题在于：

> **把封闭考试中“必须立即作答、到点交卷”的时间制度，迁移到本可通过新增信息大幅改善的开放决策。**

对应旧章：
- `EXTERNAL PROBLEM DEFINITION`；
- `SHORT-CONTEXT PERFORMANCE`；
- `ANSWER-CLOSURE BIAS`；
- `COMPLETION OVER IMPROVEMENT`。

但本节要再分开三个不同变量：
1. `RESPONSE SPEED`：多快提交一个可听的方案？
2. `DECISION QUALITY`：事前有多少证据、方案比较、错误代价审计？
3. `LEARNING VALUE`：决策过程保留了多少可迁移知识和修正能力？

高 response speed 不自动等于高 decision quality，也不自动意味着低质量。有些紧急、可逆、熟悉任务就应该立即决策。

## 28.2 `VALUE-OF-INFORMATION BLINDNESS / 信息增益盲区`

在决策分析中，额外调查、测试与证据搜集是否值得做，核心是比较：

- 通过新增信息降低错误决策概率及损失的预期收益；
- 调查/实验的直接成本；
- 延迟决策带来的窗口损失和机会成本。

正式邻接概念：`Expected Value of Information (EVI/VOI)` 与 `Expected Value of Sample Information (EVSI)`；这里借鉴其逻辑，**不声称能从匿名对话给出精确货币化数值**。

S1：
- ISPOR 2020 Value of Information Introduction：https://www.ispor.org/heor-resources/good-practices/article/value-of-information-analysis-for-research-decisions-an-introduction
- 美国国家研究委员会《Environmental Decisions in the Face of Uncertainty》信息价值部分：https://www.ncbi.nlm.nih.gov/books/NBK200840/

```text
If expected benefit from better information > research + delay costs:
    investigate / prototype first
Else:
    decide now / cheap reversible probe
```

因此：
> **“现场拿出方案”与“先研究数日”之间不存在永远正确的答案；优秀的决策能力包括判断何时值得延迟收敛。**

截图个例的诊断条件是：问题并非迫在眉睫、存在可低成本取得的新材料/对照方案、这些材料有实质可能改变决策，却没有被要求或允许获得。

## 28.3 `RESEARCH WORK INVISIBILITY / 研究劳动不可见性`

部分组织对“工作”的默认可见形态可能是：
- 当场表态；
- 很快提交PPT或方案；
- 会议达成一致；
- 任务开始执行。

而：
- 追踪资料来源；
- 核验需求前提；
- 扩展陌生案例；
- 对冲突证据保留不确定性；
- 设计能否证伪的 cheap experiment；

容易被误认成尚未开始工作。

这是一种**评价偏差候选机制**，不能根据一例认定普遍存在。

它能使“做得好的人”承担额外不利：
```text
fast deliverable
→ supervisor learns "one-day answer is available"
→ next task allocates even less research time
→ research/information-gathering becomes unbudgeted
→ stronger exam-like decision loop
```

真正要问：
> **组织记录的是“第一份方案何时交”，还是“最终决策在投入相同资源后有多大改善”？**

这也连接 `双环学习`：如果组织只改进“下次开会更快提交”，却不检验“为什么要在会上决定”，反馈仍停在single-loop。
- [跨行业：Double-Loop Learning / Defensive Routines](../../cross-industry/double-loop-learning-defensive-routines-001.md)。

## 28.4 权力、父权、信息不对称与应试过拟合：四者不能互相替代

对会议现场速答，至少存在四种竞争解释：

| 候选机制 | 关键预测 | 反证方式 |
|---|---|---|
| `EXAM OVERFIT` | 非紧急开放问题也偏向现场速答、不能容忍“待查”，跨组织持续 | 同人遇开放问题会主动争取资料/时间 |
| `AUTHORITY / STATUS` | 越高级越难承认未知、越有权现场收卷；下级缺修改题目权 | 同等组织权力下不同训练者行为明显不同 |
| `INFORMATION ASYMMETRY` | 领导事先掌握资料/目标，实际只在分配执行任务 | 证据表明上级自身也无预研，需团队真正决策 |
| `REAL URGENCY / COORDINATION` | 时间窗口短、决策可逆或信息难在期限内改善 | 低紧迫、收益大的研究同样被禁止 |

相关动力还可能来自商业压力、行业经验、资源预算，而非仅教育经历。

所谓“父权混入形式权力”目前保留为H；不能凭一段私聊证明具体组织或管理者的长期心理机制。

## 28.5 决策过程四种正交能力

1. `PROBLEM OWNERSHIP`：敢问目标本身对不对。
2. `INFORMATION SEARCH`：知道缺什么，主动找材料。
3. `DECISION-TEMPO CALIBRATION`：知道何时立即定、何时等证据、何时做可逆小实验。
4. `FEEDBACK-BASED REVISION`：新信息来了会改题，而不只是优化原答案。

“能立刻给出一个看上去合理的方案”主要测第2与第3项以外的一部分表达/经验调用能力；不能代表四项全部。

## 28.6 反考试化会议协议：`QUESTION FIRST, EVIDENCE NEXT, DECISION LAST`

仅用于**非紧急且真实存在多种开放选项**的任务，不把程序官僚化成另一套强制考试。

**A. 明确决策问题和裁决权**
- 谁决定？
- 谁提出目标？
- 谁承担错误代价？
- 目标本身能不能被修改？

**B. 先列最小信息缺口**
- 现有事实/推测/未知；
- 可能改变结论的证据；
- 哪项资料几小时可得、哪项要几天；
- 不等待的损失。

**C. 至少保留两个可行动方案**
- 包括“不行动/分阶段试”；
- 每个方案的可逆性、资源、失败成本；
- 避免把第一份上交方案当成默认获选方案。

**D. 决定信息获取节奏**
- 紧急、信息价值低：立即决策；
- 不确定但可逆：小实验/原型；
- 不确定、损失大且新证据可能改结论：先分配调查周期；
- 若延迟本身代价高：同时购买选项或分阶段提交。

**E. 会议不是收卷，而是裁决**
- 哪项新证据改变了原方案？
- 为什么此时已有足够理由commit？
- 什么条件出现时我们会撤销本次决定？
- 何时复盘预测误差和研究成本？

这个协议绝不是说“每次都开三天会”；它强调以**信息价值与可逆性**选择动作时间。

## 28.7 可证伪审计：同类项目比较即时会议与预研会议

如果要验证此机制，采用固定起点的项目或会议队列，比较：
- `ADVANCE_BRIEF_LEAD_TIME`：会前多久明确任务？
- `EVIDENCE_EXPANSION`：有多少新的独立资料被吸纳？
- `ALTERNATIVES_COUNT`：讨论过多少实质不同的方案？
- `PREMISE_CHALLENGE`：是否允许改变目标？
- `DECISION-TO-EXPERIMENT_LATENCY`：从意见到首个低成本验证多久？
- `FORECAST_CALIBRATION`：事前置信区间与后续结果差异；
- `REWORK_COST`：方向错误造成的返工与错失窗口；
- `LEARNING_RETENTION`：复盘是否修改后续规则与决策权配置。

测量时对任务难度、紧迫度、资料可得性、组织权力、行业生命周期和成员资历分层；不要“研究组赢一回”就推出普遍规律。

**公开材料边界**：聊天截图仅用于匿名机制抽取，不保留普通人的可识别姓名、群聊细节和可反推的工作岗位。

## 28.8 本轮结论

> **应试过拟合不只决定“谁来出题”，还可能决定“大家认为多快交卷才算聪明”。真正的开放决策能力包括对新增信息价值的判断：必要时快速行动，必要时保护调查与原型窗口，必要时推翻最初题目。若组织把快速提交等同于高绩效，甚至把会前搜证和延迟收敛当成低效率，便会系统性地惩罚本来能改善决策的认识劳动。**


---

# 29. CLOSED-BOOK DECISION VS RESEARCH-FIRST DECISION：把“会议考试化”做成可检验实验（2026-10-09）

本节是现有 `MEETING-AS-EXAM / DECISION-TEMPO OVERFIT` 的测量增量，**不是**另立应试过拟合理论。

## 29.1 从截图中提取的作者观察（不作人群比例证据）

案例中的关键不是上级是否有正式决定权，而是一个尚未明确方向、可以事先调查的问题被压成现场答题：没有提前提供研究问题，讨论迅速收敛，执行被立即启动，而提出“分几天研究、比较方案再定”未获得可见的正面处理。

相邻案例包括：
- “大厂会议：无预研→现场问答→即时定案”；
- “学生转专业：只有先在原专业得到高分才具备转专业资格”；
- “独游创业：把先写完整规格、拿融资、配置部门看作唯一正统”；
- “评判模糊决策：认为只有确定答案的技能有价值，未知决策都是运气”。

前两条分别指组织与校园规则；后两条涉及生产惯例与社会评价。**相似性只证明值得比较，不证明同一教育因果已经成立。**

## 29.2 最小双条件对照实验

选择同等开放程度的实际产品提案与研究题目，以同类资历人员随机分组：

- **A：CLOSED-BOOK / EXAM-TEMPO**：会议现场首次收到问题，20分钟交一份答案。
- **B：RESEARCH-FIRST / QUESTION-REVISION**：提前72小时收到问题，允许公开资料、竞品试玩、采访、讨论和小原型；参与者可提交“先改题”或“暂不决策”方案。
- **C：TIME-MATCHED CONTROL**：同样72小时日历时间，但限制外部信息搜集，观察收益是来自思考时间、信息扩展还是题目修改权。

尽可能记录实际工作时长与参与成本，避免简单把 B 的资源优势误判为认知能力优势。以配对任务或交叉设计控制领域专长和题目差异。

### 预先锁定的评价指标

1. `QUESTION_CHALLENGE_RATE`：主动识别初始题目隐含假设并提出可检验替代定义的比例。
2. `EVIDENCE_EXPANSION`：新增外部资料的相关性、来源独立性与反证覆盖，而非链接数量。
3. `OPTION_SET_BREADTH`：实际可执行备选方案种类及关键 trade-off。
4. `UNCERTAINTY CALIBRATION`：预报成功概率、关键假设与失败信号，长期观测后校准。
5. `REVERSIBILITY AWARENESS`：是否区分可廉价试错与难以逆转的资源承诺。
6. `EX-ANTE DECISION QUALITY`：由盲评专家根据当时已知资料评估，不以最终结果回填“当时理应知道”。
7. `ARTIFACT / PROTOTYPE QUALITY`：有条件时用真实玩家/用户任务验证，而不是由上级满意度评分。

**禁止把“方案更长、会议更多”当质量提升。** 若 B 只是材料更多却不能推翻错误前提，实验不支持我们的强假说。

## 29.3 理论接口：迁移不是自动发生

- 2007年 `Transfer from structured to open-ended problem solving in a computerized metacognitive environment` 研究以231名13–14岁学生开展不同元认知支持条件的实验，发现支持组在近迁移与远迁移的过程/结果上优于控制组。它支持“训练安排可改变开放问题表现”，**不直接证明中国应试教育造成产业决策缺陷**。https://www.sciencedirect.com/science/article/abs/pii/S0959475207001053
- 2022年 `Transfer of metacognitive skills in self-regulated learning` 指出，远迁移依赖学习者对目标任务具有充分的领域策略知识；不能只说“聪明人会自动迁移”。https://link.springer.com/article/10.1007/s11409-022-09322-x
- 2025年 `Far Transfer of Metacognitive Regulation` 在学生随机分组训练中观察到幅度较小的远迁移效应；说明可训练，但不能把教学干预写成万能药。https://link.springer.com/article/10.1007/s10648-024-09983-x

## 29.4 对作者创新教育的操作修正

在“完整作者练习”中保留两种不同任务：

- **给定题目做原型**：训练专业执行、约束处理、缩模、交付；
- **允许推翻题目的原型**：训练题目是否值得做、如何提出反证、什么时候不做或另做。

二者都应练；若只练第二种，可能失去专业交付纪律；若只练第一种，则继续把原型制作成新型考试。

> **本项目新的判断纪律：不能因某人能快速拿出一个答案就默认他具备开放决策能力，也不能因某人要求更多资料就默认他更有判断力。判断质量须看：信息增量是否改变了方案、反证是否被认真对待、成本是否可逆、长期校准是否改善。**
