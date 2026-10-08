# Judgment Under Uncertainty：March / Simon / Knight / Hayek / Buxton 理论栈

- Status: **CROSS-INDUSTRY SYNTHESIS / THEORY STACK / PRE-CLAIM**
- As-of: 2026-10-08
- Purpose: 补齐现有 Christensen / Jobs / Grove / Hirschman / Reversible Bets 框架中关于探索、有限理性、不可量化不确定性、分散知识与多方案原型的理论基础。
- Related:
  - [Innovation Constitutionalism](innovation-constitutionalism-exit-voice-loyalty-001.md)
  - [Reversible Bets / Irreversibility Gradient](reversible-bets-irreversibility-gradient-001.md)
  - [Self-Obsolescence / Second-Answer Test](self-obsolescence-second-answer-test-001.md)
  - [Complementary Taste / Founder Pair Lifecycle](complementary-taste-founder-pairs-001.md)

## 0. 为什么需要这一组，而不是继续堆“创新名言”

现有主干已经能回答：
- 谁有权判断；
- 谁有权实验；
- 什么时候Exit / Voice；
- 怎样让旧组织不杀死新答案；
- 怎样用可逆下注降低早期错误成本。

仍然缺五个上游问题：

1. 为什么组织会系统性偏向 exploitation，而不是 exploration？
2. 为什么再聪明的组织也不可能拥有完全理性和完整信息？
3. 为什么“没有可量化数据”并不等于“没有可判断的机会”？
4. 为什么前线/局部知识无法完全被中央KPI和统计汇总替代？
5. 为什么“先把一个方案做对”经常不如“先比较多个可能方案”？

本节点用五位理论家分别补位。

---

## 1. James G. March：Exploration / Exploitation 不是口号，而是自毁型适应机制

March 1991《Exploration and Exploitation in Organizational Learning》的核心不是“探索和利用要平衡”这么简单。

他明确区分：
- **Exploration**：search、variation、risk taking、experimentation、play、flexibility、discovery、innovation；
- **Exploitation**：refinement、choice、production、efficiency、selection、implementation、execution。

最关键的机制是：

> exploitation的回报通常更近、更确定、更容易归因；exploration成本现在发生，收益更远、更分散、更不确定。

所以组织即使完全理性，也容易出现：
```text
short-term adaptive success
→ exploitation strengthens faster
→ exploration loses resources
→ organization becomes locally excellent
→ long-run self-destruction risk rises
```

March原文摘要直接指出：适应过程因为更快强化exploitation，可能“短期有效、长期自毁”。

### 与现有框架的连接

这为我们此前的：
- Local Optimization Competence；
- Benchmark Capture；
- Success-Path Version Lock；
- Innovation Entropy；
- Exploitation core / Exploration fringe

提供了更硬的组织学习理论基础。

也意味着：

> **创新不足未必来自领导“保守人格”，可能来自回报结构本身持续奖励exploitation。**

### 新增判断：Exploration Tax Visibility

组织通常能精确看到：
- prototype花了多少钱；
- 未上线feature浪费了多少人月。

却很难看到：
- 因为没探索而错失的品类；
- 因为没下注而失去的未来人才；
- 因为过早benchmark化而从未出现的产品。

因此：
# `VISIBLE EXPLORATION COST / INVISIBLE NON-EXPLORATION COST`

是一种结构性偏差。

Primary:
- James G. March, “Exploration and Exploitation in Organizational Learning,” *Organization Science* 2(1), 1991:
  https://pubsonline.informs.org/doi/10.1287/orsc.2.1.71

---

## 2. Herbert Simon：真正的敌人不是“人不够聪明”，而是有限理性 + 注意力稀缺

Simon的`bounded rationality`把“为什么组织无法像全知优化器一样决策”说得非常彻底。

人和组织：
- 不知道全部选项；
- 不知道全部后果；
- 计算能力有限；
- 时间有限；
- attention有限；
- 因此经常不是maximize，而是找到“足够好”的可行解。

这意味着：

> **一个看起来“最优”的组织流程，往往只是在当前representation、搜索范围和注意力预算内最优。**

### Design不是分析世界，而是改变世界

Simon在《The Sciences of the Artificial》中给出的经典定义：

> everyone designs who devises courses of action aimed at changing existing situations into preferred ones.

这对游戏/产品研究尤其重要：

自然科学问：
> 世界是什么？

设计问：
> **我们想让世界变成什么，并怎样让它发生？**

因此纯数据分析永远不能替代Product Judgment，因为数据只能描述：
- 已发生的行为；
- 已存在的产品空间；
- 当前measurement framework。

设计必须引入：
# `PREFERRED STATE`

也就是一个现实中尚不存在的目标状态。

### 与Jobs的连接

Jobs所谓：
> 从customer experience倒推技术

本质上就是Simon式design：

```text
preferred experience
→ required system
→ required capability
```

而不是：
```text
available technology
→ find somewhere to use it
```

### 与AI时代的连接

当AI把候选方案数量放大时，瓶颈进一步从：
- generation

移向：
- attention allocation；
- representation；
- search boundary；
- selection。

所以Simon甚至比“AI生成更多东西”更值得重读。

Sources:
- Herbert A. Simon, *The Sciences of the Artificial*:
  https://books.google.com/books?id=k5Sr0nFw7psC
- Herbert A. Simon, “Rational Decision-Making in Business Organizations,” Nobel Lecture, 1978:
  https://www.nobelprize.org/prizes/economic-sciences/1978/simon/lecture/

---

## 3. Frank Knight：创新不是Risk，很多时候是Uncertainty

Knight 1921最重要的区分：

### Risk
- outcome不知道；
- 但概率分布大致可估。

### True Uncertainty
- 连可靠概率分布都没有；
- 情境可能是新的、唯一的、结构正在变化。

这对创新研究至关重要。

成熟赛道里：
```text
CAC
retention
conversion
genre comps
historical sales
```
可能足以形成risk model。

前范式创新里：
> “用户会不会想要一种过去没有的体验？”

很多时候不存在可靠历史分布。

所以：

> **要求一个真正pre-paradigm项目像成熟项目一样先交出可量化概率，本身就是category error。**

### Data Requirement Trap

工作命题：

```text
Knightian uncertainty
→ management asks for measurable risk
→ team fabricates analogies / benchmarks
→ unknown future is forced into known category
→ project is selected only if it resembles past products
```

这正好解释Benchmark Capture为什么不只是“胆小”。

组织试图把：
# `UNCERTAINTY`
伪装成：
# `RISK`

因为只有后者容易进入Excel、greenlight、ROI模型。

### 但Knight不等于“相信直觉”

正确结论不是：
> 数据没有用，所以创始人随便拍脑袋。

而是：
> 在没有可防御概率分布时，需要judgment、small bets、optionality和现实更新机制。

因此Knight与Reversible Bets天然组成一对：
```text
Uncertainty high
→ confidence in forecast low
→ commitment size should initially be low
→ information-producing action high
```

Primary:
- Frank H. Knight, *Risk, Uncertainty, and Profit* (1921):
  https://www.econlib.org/library/Knight/knRUP.html

Secondary overview:
- Reserve Bank of Australia, “Risk versus Uncertainty”:
  https://www.rba.gov.au/publications/rdp/2000/2000-10/risk-versus-uncertainty.html

---

## 4. Hayek：Formal Authority 不等于 Local Knowledge

Hayek 1945《The Use of Knowledge in Society》的知识论部分对创新组织非常有用，即使完全不接受其更广泛政治主张。

他的核心问题是：

> 相关知识从来不会完整集中在一个头脑里，而是以分散、不完整、甚至互相矛盾的形式存在于很多人手里。

尤其重要的是：
# `knowledge of particular circumstances of time and place`

即：
- 某个工程师刚发现的工具摩擦；
- 某个设计师连续观察到的玩家异常行为；
- 某个客服发现的新痛点；
- 某个modder知道但管理层dashboard还没有的使用方式；
- 某个一线员工关于“这套流程实际哪里坏了”的具体知识。

这些东西经常：
- 不能完整标准化；
- 不能及时进入统计；
- 一旦汇总就失去关键语境。

Hayek甚至直接指出，统计聚合本质上会抽掉具体地点、质量和时机差异，而这些差异恰恰可能决定具体决策。

### 与Grove的连接

Grove的Cassandras现在可以获得更深解释：

> senior不是因为笨而落后，而是**战略拐点的早期知识往往首先以分散的局部异常出现**。

所以：
# `FORMAL AUTHORITY != INFORMATION LOCATION`

### 与Innovation Constitutionalism连接

Voice的价值之一就是：
> 把组织中分散的local knowledge带进资源分配。

而Experiment Right的价值是：
> 某些local knowledge无法用汇报传输，只能做成artifact。

### 边界

不能把Hayek机械翻译成：
> 所有决策都应该去中心化。

组织仍需要：
- integration；
- shared strategy；
- resource coordination；
- system-level tradeoff。

问题是：
> **哪些知识必须中央整合，哪些判断必须留给“man on the spot”？**

Primary:
- F. A. Hayek, “The Use of Knowledge in Society,” *American Economic Review*, 1945:
  https://www.econlib.org/library/Essays/hykKnw.html

---

## 5. Buxton / Tohidi：Getting the Right Design 应当先于 Getting the Design Right

2006年Tohidi、Buxton、Baecker、Sellen做了一个非常适合我们prototype研究的实验：

- 一组用户只看到一个设计；
- 另一组同时看到三个功能等价但样式不同的设计。

结果：
- 只看到一个设计时，用户给出更高评分；
- 负面意见更少；
- 多方案比较时，批评更多、更强。

作者因此主张：

> **testing many is better than one**

并区分：

### Getting the design right
把一个选定方向越来越完善。

### Getting the right design
先判断到底哪个方向值得被完善。

这与我们前面所有研究直接对接。

### Single-Prototype Commitment Bias

一旦只给团队/用户一个方案：
- 它容易被心理上当成“产品”而不是“候选”；
- 反馈变成局部修补；
- 人开始问“哪里需要优化”；
- 而不再问“为什么是这个方向？”

所以：

```text
one prototype
→ refinement frame
→ local criticism
→ premature commitment
```

而：
```text
multiple alternatives
→ comparison
→ contrastive judgment
→ stronger selection signal
```

这给了我们一个非常实用的探索原则：

# `COMPARE BEFORE COMMIT`

如果成本允许，早期不要问：
> 这个prototype够不够好？

而先问：
> **和另外两个真正不同的候选相比，它为什么值得继续？**

Primary:
- Tohidi, Buxton, Baecker, Sellen, “Getting the Right Design and the Design Right: Testing Many Is Better Than One,” CHI 2006:
  https://www.microsoft.com/en-us/research/publication/getting-the-design-right-and-the-right-design-testing-many-is-better-than-one/
  https://www.billbuxton.com/rightDesign.pdf

Related:
- Lim, Stolterman, Tenenberg, “The Anatomy of Prototypes,” TOCHI 2008:
  https://doi.org/10.1145/1375761.1375762

---

## 6. 五人合并后得到一套非常完整的“前范式决策理论”

### Knight
先提醒：
> **你面对的可能不是可统计Risk，而是无法可靠量化的Uncertainty。**

↓

### Simon
因此：
> **不存在全知最优器，只能在有限搜索和有限注意力中设计preferred state。**

↓

### Hayek
同时：
> **关键知识分散在组织各处，中央dashboard不可能天然拥有全部真实信息。**

↓

### March
而组织又会：
> **因为近期、可归因收益而系统性过投Exploitation、欠投Exploration。**

↓

### Buxton
所以实践上：
> **不要太快精炼唯一方案；先并行制造多个低成本候选，让比较帮助选择。**

这五层和已有主干拼起来：

```text
Knight — 你究竟知道多少？
Simon — 你的理性和attention边界在哪里？
Hayek — 相关知识实际分布在哪里？
March — 资源分配为什么会系统性偏向旧答案？
Buxton — 如何用多个候选降低过早commit？
Jobs — 哪个完整体验值得存在？
Grove — 旧成功是否已经过期？
Christensen — 旧selection system是否会杀掉它？
Hirschman — Voice失败以后有没有Exit？
Reversible Bets — 该下注多少来换取下一轮信息？
```

这已经构成一套相当完整的：
# `JUDGMENT UNDER UNCERTAINTY STACK`

---

## 7. 对游戏行业特别值得保留的三个新命题

### 7.1 Metric abundance can hide Knightian uncertainty

有很多数据：
- 不代表问题已经从uncertainty变成risk。

如果产品范式变了，旧数据分布本身可能失效。

所以：
> **数据很多，不等于未来可量化。**

### 7.2 Production excellence can be Marchian exploitation

pipeline、polish、live-ops、monetization、benchmark：
- 都可以很强；
- 但如果组织缺少exploration allocation，能力越强越可能更快爬上旧山峰。

### 7.3 Prototype portfolio is a governance mechanism

多prototype不只是设计技术。

它在治理上避免：
- 最早提出的方案自动成为默认；
- senior的第一个想法自动获得资源；
- 团队因沉没成本过早进入refinement。

因此：
# `PORTFOLIO OF PROTOTYPES = TEMPORARY PLURALISM`

---

## 8. 次级高价值候选，暂不升主干

### Alan Kay — Point of View is worth 80 IQ points
价值：强调representation / reframing可能比单纯增加分析强。
适合接：
- Representation；
- Pre-paradigm search；
- Problem framing。

但目前主要是强思想性格言，理论体系不如上述五人完整，先作候选。

Reference:
https://quoteinvestigator.com/2018/05/29/pov/

### Michael Polanyi — We know more than we can tell
价值：Tacit Knowledge、apprenticeship、Taste transmission。
非常适合下一轮研究：
- 为什么设计Taste不能只靠文档；
- 为什么AI读取全部文档仍不等于拥有craft judgment；
- Nintendo师承 / apprenticeship。

### Karl Popper — falsification / conjectures and refutations
价值：强意见必须有可失败条件。
但容易被简化成“做实验就行”，需要和design research、Knight uncertainty区分后再用。

### John Boyd — OODA / Orientation
价值不在“转得快”，而在：
> Orientation决定你如何解释观察。
可接Representation / Model Updating。
但军事语境跨域需要谨慎。

---

## 9. 当前Reader-facing核心问句

遇到一个新项目，不要先问：

> 数据证明它能成吗？

先依次问：

1. **Knight：** 这是risk还是uncertainty？
2. **Simon：** 我们到底搜索了多少方案，哪些东西只是没进入attention？
3. **Hayek：** 谁掌握我没有的局部知识？
4. **March：** 当前资源系统是不是天然奖励旧答案？
5. **Buxton：** 在把这个方案做精前，我们真的比较过别的方向吗？
6. **Jobs：** 最终用户真正得到的完整体验是什么？
7. **Grove：** 如果把旧成功清零，还会做同样判断吗？
8. **Christensen：** 旧组织的selection function有能力选中它吗？
9. **Hirschman：** 内部Voice失败后，它还有别的生存通道吗？
10. **Reversible Bets：** 下一步最小必要承诺是多少？

这比“要敢于创新”有更高操作性。
