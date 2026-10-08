# Representation / Orientation / Paradigm：Alan Kay、Boyd、Kuhn 与前范式搜索

- Status: **CROSS-INDUSTRY SYNTHESIS / THEORY NODE / PRE-CLAIM**
- As-of: 2026-10-08
- Purpose: 解释为什么同样聪明的人面对同一事实，可能因为表征、定向与范式不同而看到完全不同的问题；并把“换视角”从格言升级成可审计的创新机制。
- Related:
  - [Judgment Under Uncertainty](judgment-under-uncertainty-theory-stack-001.md)
  - [Tacit Judgment / Selection Apprenticeship](tacit-judgment-selection-apprenticeship-ai-001.md)
  - [Self-Obsolescence / Second-Answer Test](self-obsolescence-second-answer-test-001.md)
  - [Innovation Constitutionalism](innovation-constitutionalism-exit-voice-loyalty-001.md)
  - [Reversible Bets / Irreversibility Gradient](reversible-bets-irreversibility-gradient-001.md)

## 0. 核心问题

很多创新失败被描述成：
- 信息不够；
- 人不够聪明；
- 执行不够强；
- 数据不够多。

Alan Kay、John Boyd、Thomas Kuhn共同提示另一类失败：

> **真正的问题可能不是“缺少答案”，而是现有表征 / orientation / paradigm 已经预先规定了什么算问题、什么算证据、什么值得注意。**

因此：

```text
more intelligence
+ more data
+ more execution
inside a bad representation
→ faster optimization of the wrong problem
```

本节点提出：

# `REPRESENTATION SOVEREIGNTY / 表征主权`

> **在已有问题定义、行业分类、指标和解释框架之外，保留重新描述对象、重新划定问题边界、重新选择比较维度的合法性。**

它不是“随便换说法”，而是：
> 当旧表征持续制造异常、局部补丁与解释困难时，允许新的表征与旧表征共同接受现实检验。

---

## 1. Alan Kay：Point of View 不是修辞，而是问题难度本身的一部分

Alan Kay 1982年演讲留下了后来被广泛引用的：

> “Point of view is worth 80 IQ points.”

现有最早可查材料来自Andy Hertzfeld当年的讲座笔记；1984年的同期采访也再次记录Kay用相近表述强调：新的看问题方式有时比单纯增加智力更有效。

Source:
- Quote Investigator 对早期资料的追踪：
  https://quoteinvestigator.com/2018/05/29/pov/

这里“80 IQ”显然不是心理测量结论，而是工程启发：

> **困难程度不是只由问题客观复杂度决定，也由你用什么representation描述它决定。**

### Representation Leverage

新增：

# `REPRESENTATION LEVERAGE / 表征杠杆`

> **通过改变对象的表示方式，使原本需要大量搜索、补丁或计算的问题，转化为更容易被看见、组合和解决的问题。**

例如：
- 新数学记号改变可操作问题空间；
- 新编程抽象改变系统复杂度的可见边界；
- 新产品概念改变用户真正需要比较的对象。

Kay的价值不在“换角度很重要”这句常识，
而在于他的技术生涯长期把：
> **新的representation**
当成真正的能力创造。

---

## 2. Kay 1997：真正危险的是把一个Point of View变成宗教

Kay在1997年OOPSLA演讲里直接批评把单一观点固定成宗教式真理，并讨论Smalltalk商业化后不再继续自我重写的问题；他反而强调系统应该保留通向下一层抽象和下一版本自己的能力。

Sources:
- OOPSLA 1997 transcript:
  https://tinlizzie.org/IA/index.php/Alan_Kay_at_OOPSLA_1997%3A_The_Computer_Revolution_has_not_Happened_yet
- Stanford 1997 talk abstract:
  https://web.stanford.edu/class/ee380/9697spr/node10.html

这与本项目已有Self-Obsolescence高度一致：

# `A GOOD REPRESENTATION MUST NOT BECOME IMMUNE TO RE-REPRESENTATION`

即：
> 一个强抽象最大的风险，就是它成功以后把自己的边界伪装成世界本身的边界。

因此新增：

# `REPRESENTATION LOCK-IN / 表征锁定`

不是“坚持某个方案”，而是：
> **整个组织已经只能用某一套概念语言看问题，以至于不符合该语言的现象很难获得问题资格。**

---

## 3. Kay 的“Medium Masquerade”：新媒介常先伪装成更好的旧东西

Kay 1997 Stanford演讲摘要提出一个极重要的历史判断：

> 世界改变型发明刚出现时往往难以被理解，只能先伪装成“better old things”，而不是立刻被当成“completely new things”。

他把印刷、汽车、电影、电视与数字计算都放进这一模式。

Source:
- Stanford EE380 1997:
  https://web.stanford.edu/class/ee380/9697spr/node10.html

新增：

# `MEDIUM MASQUERADE / 新媒介伪装`

```text
new capability appears
→ users / investors / designers interpret it using old category
→ product is optimized as "better old thing"
→ genuinely new affordance remains underused
```

### 对生成式AI / LLM游戏的研究意义

当前很多“AI游戏”仍可能处于：
- better dialogue system；
- more NPC text；
- more quests；
- cheaper content production；

这不等于已经找到：
# `LLM-NATIVE PRODUCT GRAMMAR`

真正的“computer revolution hasn't happened yet”式问题应是：

> **如果不假设传统NPC、任务、对话树和作者内容生产方式必须保留，这种能力到底允许什么以前不存在的完整体验？**

这不是断言现有LLM游戏一定失败，
而是建立一个压力测试：

# `OLD-MEDIUM IMPROVEMENT ≠ NEW-MEDIUM DISCOVERY`

---

## 4. Kuhn：Paradigm 不只是理论，而是“什么题值得做”的生成器

Kuhn的“paradigm”常被商业写作滥用成：
> 大趋势 / 新时代 / 颠覆。

更严格的Kuhn框架要复杂得多。

Stanford Encyclopedia的总结强调：

- normal science依赖稳定的disciplinary matrix；
- paradigm提供可解的puzzles以及解题工具；
-更窄意义的paradigm是`exemplar`：公认的经典问题—解法样本；
- exemplar会告诉共同体：
  1. 以后哪些问题像“正经问题”；
  2. 应该用什么办法解决；
  3. 什么样的结果算高质量答案。

Source:
- Stanford Encyclopedia of Philosophy, Thomas Kuhn:
  https://plato.stanford.edu/entries/thomas-kuhn/

这与我们游戏行业的benchmark研究存在非常强的结构相似。

### Benchmark as Exemplar

工作类比：

```text
successful game / product
→ becomes exemplar
→ defines legitimate problem family
→ defines accepted solution techniques
→ defines evaluation standards
→ trains next generation to perceive similarity
```

因此benchmark最深的影响并不是：
> 大家抄feature。

而可能是：

> **大家逐渐只会看见那些能被成功benchmark语言描述的问题。**

新增：

# `EXEMPLAR CAPTURE / 范例俘获`

这比Feature Copy更深一层。

---

## 5. Normal Science ≈ Puzzle-Solving Competence：高能力不等于前范式能力

Kuhn把正常科学描述为puzzle-solving：
- 基本框架已接受；
- 问题大致可解；
- 方法家族相对熟悉；
- 成功主要依赖专业能力。

这不是贬义。

正常科学之所以强，是因为共同范式让大量人不必每天重新争论基础，可以：
- 深挖细节；
- 提高精度；
- 累积专业能力。

所以对应产业研究必须避免：
> “范式内工作 = 低级模仿。”

成熟产业绝大多数高质量进步本来就是：
# `HIGH-SKILL NORMAL PRODUCTION`

但它与：
# `PARADIGM FORMATION / PRE-PARADIGM SEARCH`
不是同一种能力。

因此此前：
- Production Capital；
- Problem-Framing Capital；
- 同构异性创新；
- 前范式创新

可以获得Kuhn式补充：

```text
Puzzle-Solving Excellence
≠
Paradigm-Formation Capacity
```

一个人可以在既定语言里极其聪明，
却几乎没有训练：
> 重新决定什么才值得成为问题。

---

## 6. Kuhn最值得本项目吸收的是“anomaly不是自动革命”

Kuhn并不主张：
> 看到一个反例就推翻整个范式。

恰恰相反，normal science通常会：
- 忽略异常；
- 归因实验误差；
- 建立局部补丁；
- 继续解决其他puzzles。

只有当某些异常变得：
- 持续；
- 重要；
- 破坏正常研究实践；
- 无法通过既有补丁吸收，

才可能形成crisis。

因此新增：

# `ANOMALY PROMOTION THRESHOLD / 异常升级阈值`

> **一个反常结果需要达到什么程度，才有资格从“局部bug”升级为“可能是整个representation出了问题”？**

### 两种错误

#### Overreaction
每一个坏数据都宣布：
> 范式革命。

结果无法积累任何稳定能力。

#### Underreaction
所有反例都被解释成：
> 特例 / 用户问题 / 执行不到位。

结果范式永远免疫。

健康系统需要：
# `ANOMALY ACCOUNTING`

记录：
- anomaly是否重复；
- 是否跨项目出现；
- 需要多少ad hoc patch才能维持旧解释；
- 是否开始破坏旧模型的预测能力。

---

## 7. Patch Burden：范式衰退可以表现为“补丁税”

新增：

# `PARADIGM PATCH BURDEN / 范式补丁负担`

当一个旧模型仍然能勉强解释现实，但需要越来越多：
- 特例；
- 例外规则；
- 额外KPI；
- 用户细分；
- 特殊流程；
- “这次情况不同”的解释；

组织可能仍感到：
> 模型是对的，只是现实越来越复杂。

另一个解释是：
> **representation已经开始失配。**

这与软件里的technical debt相似：

```text
old paradigm
+ accumulating exceptions
→ explanatory maintenance cost ↑
```

该指标目前是H级机制，不应机械用“规则多”判定范式错误。

---

## 8. Incommensurability：真正的新答案可能先在旧指标上显得更差

Kuhn的incommensurability并不等于：
> 新旧范式完全无法比较。

更准确的是：
- 比较标准本身可能部分改变；
- 不同范式对“什么问题重要”权重不同；
- 相同观察也可能被不同理论结构解释。

SEP明确强调：
> incommensurability不是non-comparability，
但会让比较远比使用一套永久中立指标复杂。

这对产品创新尤其重要。

新增：

# `METRIC REGIME DEPENDENCE / 指标制度依赖`

一个新产品若改变：
- 用户任务；
-使用频率；
-消费方式；
-交互单位；
-产品边界；

那么旧产品最重要的指标未必仍是最重要指标。

这与Christensen高度相邻：
> disruptive trajectory早期可以在主流客户重视的旧性能指标上更差。

但必须保留边界：

# Kuhn ≠ Christensen

- Kuhn研究科学共同体中的理论、方法、标准与范例；
- Christensen研究产业、客户价值网络和资源分配。

二者只能作结构比较，不能互相证明。

---

## 9. John Boyd：真正的OODA核心不是“快”，而是Orientation

商业管理常把OODA简化为：

> Observe → Orient → Decide → Act，谁循环更快谁赢。

Boyd最终版本比这复杂得多。

Air University保存/整理的Boyd材料显示，Orientation内部包含：
- cultural traditions；
- genetic heritage；
- previous experience；
- new information；
- analysis & synthesis。

Boyd把Orientation称为最重要部分，因为它会塑造：
- how we observe；
- how we decide；
- how we act。

Sources:
- Air University, *A Discourse on Winning and Losing*:
  https://www.airuniversity.af.edu/Portals/10/AUPress/Books/B_0151_Boyd_Discourse_Winning_Losing.pdf
- Air University summary:
  https://www.airuniversity.af.edu/News/Display/Article/420819/ooda-loop-makes-its-mark-on-maxwell/

所以：

# `OBSERVATION IS NOT RAW INPUT`

同样的市场、玩家反馈、战场或技术变化，
会因为不同orientation而被分类成不同问题。

这与Kuhn的：
> paradigm shapes observation

形成很强的结构相似。

---

## 10. Boyd 1976《Destruction and Creation》：成熟判断必须能拆毁自己的概念

Boyd在《Destruction and Creation》中直接提出：

> 人为了理解和应对环境，会构建mental patterns / concepts of meaning；而为了适应不断变化的环境，又必须不断destroy and create这些pattern。

Source:
- John Boyd, *Destruction and Creation*, 1976:
  https://en.wikisource.org/wiki/File:Destruction_%26_Creation.pdf

这意味着学习不只是：
# `ADD NEW INFORMATION`

而还包括：
# `DESTROY OLD COHERENCE`

新增：

# `ORIENTATION DEBT / 定向债务`

> **过去经验构成的orientation曾经很有用，但环境改变后，它开始系统性过滤、扭曲或低估新信息。**

它和Self-Obsolescence不同：

- Self-Obsolescence主要研究旧成功公式和资源配置；
- Orientation Debt研究更上游的“你如何解释观察”。

一个组织可能已经换了产品，
却仍用同一套：
- category；
- customer theory；
- talent model；
- risk language；
解释世界。

那只是：
> solution changed, orientation unchanged.

---

## 11. Orientation Updating：不是简单“接受新信息”

Boyd框架真正困难的一点是：

```text
new information
→ enters orientation
→ orientation also filters interpretation of new information
```

因此存在反馈锁：

```text
old model
→ classify new evidence
→ evidence appears to support old model
→ old model strengthens
```

新增：

# `SELF-SEALING ORIENTATION / 自封闭定向`

典型表现：
- 新品成功 → “它其实还是旧品类，只是包装不同”；
- 新玩法失败 → “证明创新没市场”；
- competitor成功 → “他们只是运气/买量/市场特殊”；
- junior提出异常 → “经验不够”。

如果任何结果都能被旧模型重新解释，
那么该模型已经失去现实可证伪性。

---

## 12. Kay × Kuhn × Boyd：三层Representation Escape

三人并非思想师承，
但可形成结构互补：

### Kay — Micro / Design Reframing
问：
> **能不能换一种representation，让问题本身变简单或变成另一个问题？**

核心：
- Point of View；
- abstraction；
- medium discovery；
- self-obsoleting system。

### Kuhn — Community / Paradigm Structure
问：
> **为什么整个专业共同体会长期共享同一套问题、范例和评价标准？什么时候异常积累到必须换框架？**

核心：
- normal science；
- exemplar；
- anomaly；
- crisis；
- paradigm change。

### Boyd — Dynamic / Continuous Reorientation
问：
> **在环境持续变化时，个体和组织如何不断拆解、重组自己的mental pattern？**

核心：
- Orientation；
- analysis/synthesis；
- destruction/creation；
- feedback。

合并：

```text
Representation
→ determines salience

Shared representation
→ becomes paradigm / exemplar system

Accumulated paradigm
→ becomes orientation

Changing reality
→ generates anomalies

Adaptive actor
→ destroys / recombines orientation

New representation
→ reveals new action space
```

---

## 13. 与Polanyi的连接：Paradigm本身也通过隐性范例学习

Kuhn后期特别强调：
> paradigm-as-exemplar。

研究者并不是先背完一套完整rules，
而是通过典型题解、训练和实践，
学会“这个新问题像哪种经典问题”。

这与Polanyi高度兼容：

```text
exemplar exposure
→ perceived similarity
→ tacit classification
→ normal problem solving
```

因此师承既能生产：
# `TASTE`

也能生产：
# `PARADIGM BLINDNESS`

同一个训练机制既让新人快速学会看，
也让某些东西从此变得：
> 看不见。

所以Selection Apprenticeship必须加入一个新目标：

# `REPRESENTATION PLURALITY / 表征复数性`

导师不只教：
> “怎样正确看。”

还应在适当阶段问：
> **如果我们现在的看法就是问题的一部分呢？**

---

## 14. 与中国“做题能力 / benchmark”研究的严格接口

不能简单写：

> 中国教育 = Kuhnian normal science。

Kuhn研究的是科学史，不是教育社会学。

但可以提出待证机制类比：

### Puzzle-Solving Formation Hypothesis

如果一个训练系统长期奖励：
- 问题由上游定义；
- 评价标准明确；
- 解题方法有成熟范例；
- 高分来自在固定representation中快速识别和执行；

那么它很可能强化：
# `PARADIGM-INTERNAL COMPETENCE`

但未必同强度训练：
# `PROBLEM / REPRESENTATION SOVEREIGNTY`

同样，在商业游戏行业：
```text
successful benchmark
→ feature grammar
→ hiring vocabulary
→ pitch template
→ KPI
→ new projects perceived through old exemplar
```

可能形成：
# `INDUSTRIAL NORMAL SCIENCE`

这个命题必须继续用：
- 原型历史；
- pitch；
-立项材料；
-人员职业路径；
-失败项目；
跨国比较验证。

它不是“中国人天生范式内思考”的文化论。

---

## 15. AI：最大的风险可能不是平均化答案，而是加速既有Representation

AI常被描述成：
> generation machine。

但它同样是：
# `REPRESENTATION AMPLIFIER`

如果prompt已经默认：
- 当前品类；
- 当前feature vocabulary；
- 当前benchmark；
- 当前metric；

AI可以极快生成大量：
> **within-paradigm alternatives。**

于是：
```text
variation count ↑↑
representation diversity ↔ / ↓
```

这就是为什么：
> 多agent ≠ 多范式。

如果所有agent共享：
-相似训练语料；
-相似prompt；
-相似评价器；

它们可能只是：
> 一群在同一世界模型里高效争论的人。

新增：

# `REPRESENTATIONAL DIVERSITY / 表征多样性`

和：
# `OUTPUT DIVERSITY`

必须分开。

---

## 16. AI也可以成为Reorientation工具，但必须被刻意使用

更高价值的AI工作流不是：

> 给我10个玩法方案。

而是：

1. 用现有行业语言描述问题；
2. 要求列出该描述隐含的分类、假设和比较维度；
3. 用另一学科 / 另一产品范式重新表述同一现象；
4. 生成互不兼容的三种causal representation；
5. 分别预测哪些现实证据会被各模型视为关键；
6. 找到能区分这些模型的低成本实验。

即：

# `REPRESENTATION PROTOTYPING / 表征原型`

在做产品prototype之前，
先prototype：
> **我们到底如何描述这个问题。**

这可能是AI时代非常便宜却高价值的新能力。

---

## 17. 新增：Problem Difficulty Decomposition

当团队觉得：
> “这个问题很难。”

先区分四种不同困难：

### Compute Difficulty
答案存在，但计算量大。

### Search Difficulty
候选很多，不知道哪个最好。

### Evidence Difficulty
无法低成本获得真实反馈。

### Representation Difficulty
当前描述方式让真正结构不可见。

前3种通常靠：
- 更多算力；
- 更强搜索；
- 更好实验。

第4种如果不解决，
前三种投入可能全部放大浪费。

所以新增：

# `REPRESENTATION-FIRST DIAGNOSIS`

> **在投入更多人力、数据或AI以前，先确认问题是不是被错误表示。**

---

## 18. Paradigm Shift不应成为烂项目免死金牌

Kuhn在商业语境最常见的滥用是：

> “大家看不懂我，因为我是新范式。”

这在逻辑上没有任何证明力。

因此强制边界：

### 18.1 Anomaly ≠ Revolution
旧模型出现异常不代表你的替代模型正确。

### 18.2 Incommensurability ≠ No Evaluation
比较困难不等于不需要现实检验。

### 18.3 New Language ≠ New Capability
改一套术语并不创造新产品价值。

### 18.4 Paradigm Claim Needs Superior Puzzle Power
替代框架至少应：
- 解释重要旧问题；
- 解释旧框架解释不了的异常；
- 产生新的可验证预测或产品可能性。

否则只是：
# `RHETORICAL REFRAMING`

---

## 19. Reader-facing Debugger

遇到一个“行业共识”：

问：
1. 它最初解决了什么真实问题？
2. 哪些成功案例成为exemplar？
3. 现在大家是不是通过与这些exemplar的相似性评价新项目？
4. 有哪些异常正在被持续解释成“执行问题”？
5. 维持旧模型需要多少例外和补丁？

遇到一个“技术革命”：

问：
1. 它现在是不是只被做成更好的旧产品？
2. 哪种能力只有新技术才出现？
3. 如果旧品类名称不存在，会怎样重新描述用户体验？
4. 哪些旧metrics可能不再是主要价值指标？

遇到一个“聪明但做不出来”的团队：

问：
> 是能力不够，还是representation让他们一直在解错题？

遇到一个AI工作流：

问：
> 它增加的是output diversity，还是representation diversity？

---

## 20. 当前最值得继续验证的问题

1. 游戏史上有哪些新范式在早期主要被理解成“更好的旧品类”，之后才形成独立语言；
2. 哪些游戏公司公开记录过“我们原来连问题都问错了”的representation shift；
3. benchmark在pitch/hiring/design review里究竟怎样从参考案例变成exemplar；
4. LLM /生成式AI游戏目前哪些项目真正改变了product grammar，哪些主要是medium masquerade；
5. AI是否能通过representation-prototyping显著提高前范式搜索质量；
6. 中国/美国/日本设计教育分别训练多少“解给定题”与“重写问题”的能力；
7. Anomaly Promotion Threshold能否从真实项目复盘中操作化；
8.组织的Paradigm Patch Burden与后续大转向之间是否存在可观察关系。

## Sources

- Alan Kay, 1982 “Point of view is worth 80 IQ points” source tracing:
  https://quoteinvestigator.com/2018/05/29/pov/
- Alan Kay, Stanford EE380, 1997, *The Computer Revolution Hasn't Happened Yet*:
  https://web.stanford.edu/class/ee380/9697spr/node10.html
- Alan Kay, OOPSLA 1997 transcript:
  https://tinlizzie.org/IA/index.php/Alan_Kay_at_OOPSLA_1997%3A_The_Computer_Revolution_has_not_Happened_yet
- Thomas Kuhn overview / paradigm, normal science, anomaly, incommensurability:
  https://plato.stanford.edu/entries/thomas-kuhn/
- John Boyd, *A Discourse on Winning and Losing*:
  https://www.airuniversity.af.edu/Portals/10/AUPress/Books/B_0151_Boyd_Discourse_Winning_Losing.pdf
- John Boyd, *Destruction and Creation* (1976):
  https://en.wikisource.org/wiki/File:Destruction_%26_Creation.pdf
- Air University on Orientation:
  https://www.airuniversity.af.edu/News/Display/Article/420819/ooda-loop-makes-its-mark-on-maxwell/
