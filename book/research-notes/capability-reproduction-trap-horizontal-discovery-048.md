# 048 — 老兵未必能教未来：能力复制陷阱与横向能力发现网络

- Status: **RESEARCH NOTE / CROSS-CUTTING HYPOTHESIS / PRE-CLAIM**
- Date: 2026-10-08
- Program: A 独立游戏英雄传说 × C 中国国情研究 × 跨行业创新
- Author-origin correction: 本篇起点来自作者对“游戏公司不训练新人”解释的纠偏：很多时候并不是资深从业者已经掌握新做法却拒绝传授，而是旧生产制度中的资深者自己并未掌握正在形成的新范式；保守招聘和培训可能是能力缺口的结果，而不只是成本转嫁。
- Adjacent canonical work: [005 中国商业游戏训练反转](china-commercial-game-training-role-origin-audit-005.md)、[006 腾讯制作人压力测试](china-commercial-game-training-role-origin-audit-006-tencent-producer-pressure-test.md)、[016 追赶成功与前范式创作者](china-catch-up-success-pre-paradigm-creator-016.md)、[043 DOOM组织老化与再年轻](doom-organizational-aging-rejuvenation-043.md)、[DOOM纵向母研究](masters-of-doom-longitudinal-master-study-001.md)
- Boundary: 本篇不把年龄、资历或“大厂出身”当成能力劣势；也不预设年轻人、独立团队、Jam 社群天然掌握真理。研究对象是**某种实践知识是否已经存在于组织内，以及谁有能力评价尚未制度化的新实践**。

## 0. 关键纠偏：Training Withholding 只是三种机制之一

“企业不招 junior / 不培养新人”至少要拆成三种不同机制。

### A. TRAINING WITHHOLDING｜会，但不愿承担培养成本

组织已经拥有成熟知识，例如既有引擎、认证、QA、网络、性能、live-ops 或 production pipeline，但因为短期成本、岗位风险或绩效压力，希望直接购买有经验的人。

这是传统 apprenticeship externalization：

```text
known practice exists inside firm
→ junior needs time to acquire it
→ firm prefers ready-made worker
→ training cost shifts toward worker / school / household
```

### B. INCUMBENT CAPABILITY CEILING｜组织自己也不会目标新实践

如果一个组织长期在成熟赛道、既定商业模型和稳定 production grammar 内优化，资深者可能极擅长：

- 已知系统的大规模实现；
- 线上数据与稳定运营；
- 成熟品类的 benchmark adaptation；
- 大组织中的跨部门交付。

但并没有亲自经历过：

- 从零发现一个未知玩法；
- 两三个人快速 scale down；
- 在没有历史数据时定义问题；
- 用 Jam / mod / prototype 反复失败；
- 利用新工具链重新组合生产函数。

此时“让 senior 带 junior”不能自动产生 frontier capability，因为要传授的知识尚未存在于这条垂直传承链里。

### C. DEFENSIVE CONSERVATISM / EVALUATOR CAPABILITY GAP｜因为不会，所以也可能不会评价

能力缺口未必以“我不知道”呈现。它可能被包装成组织已有的专业标准：

- “这不专业”；
- “没有商业验证”；
- “不是正规流程”；
- “没有大项目经验”；
- “这种小原型说明不了什么”。

问题不必来自恶意。更一般的机制是：

> **评价者使用自己能够识别的旧能力作为质量代理，因此尚未制度化的新能力即使真实存在，也可能无法被正确计价。**

这与单纯的劳资冲突不同：不是“有知识的人故意不传”，而可能是“旧知识持有者同时掌握了新知识的评价权”。

---

## 1. Corporate Apprenticeship 与 Frontier Discovery 不是同一种学习

传统师徒关系的隐含假设是：

> 大师知道正确答案，徒弟需要复制这套已知实践。

但创新问题经常不存在现成答案。

因此应分开：

| 机制 | 主要回答 | 最适合传什么 |
|---|---|---|
| **Vertical Apprenticeship / 垂直学徒制** | 怎样把已知 production 做好？ | 成熟工具、流程、质量标准、工程诀窍、组织协作 |
| **Horizontal Capability Discovery / 横向能力发现** | 哪一种新 practice 可能成立？ | 原型方法、新工具组合、新交互、新分发、新团队形态 |
| **Reality Arbitration / 现实裁决** | 新做法是真的有效，还是圈内自嗨？ | 玩家测试、可玩结果、收入、技术可行性、可重复生产 |

两者不能互相替代。

公司内部 apprenticeship 可以非常强，同时 frontier discovery 很弱；反过来，Jam / mod / indie 网络可以非常会探索，却在工程、ship、商业化或规模化上很弱。

---

## 2. HORIZONTAL CAPABILITY DISCOVERY NETWORK｜横向能力发现网络

当没有人知道标准答案时，知识更可能从同侪网络中生长：

```text
peer ↔ peer
mod scene
game jam
demo / prototype community
open source
small-team indie
tool / creator communities
```

核心不是“年轻人互相鼓励”，而是：

1. 大量低成本尝试；
2. 可公开观察 artifact；
3. 别人能够复制、修改、反驳；
4. 不需要先获得旧组织完整授权；
5. 新做法在重复实践中获得可见性。

因此 itch / mod / Jam 生态的制度价值不能只写成“新人培训”。

更准确地说，它们可能提供：

> **组织外的 capability search space。**

这里产生的是尚未被大公司课程化、岗位化、绩效化的 practice。

---

## 3. CAPABILITY REPRODUCTION TRAP｜能力复制陷阱

如果组织只用既有成功标准招聘、培训和晋升，就可能出现：

```text
legacy success
→ legacy capability becomes professionalism
→ hire people who already display it
→ senior mentors reproduce it
→ promotion rewards it
→ fewer frontier experiments survive internally
→ next generation of senior staff becomes even better at legacy capability
→ organization has even less first-hand knowledge of the new practice
```

这是能力复制陷阱。

它不要求组织“愚蠢”。恰恰相反：

> **一个组织可能非常有效率地复制昨天最赚钱的能力，因此更难产生明天尚未被证明的能力。**

这与 competency trap / exploitation–exploration 文献相邻，但本项目需要继续用具体人物和生产史审计，而不是仅靠理论标签。

---

## 4. EXPERIENCE YEARS ≠ FRONTIER TEACHING CAPACITY

以后研究“老兵能不能培养新人”时，不得再用从业年限直接代理 mentor quality。

至少拆成：

- `TENURE`：从业年份；
- `KNOWN-PRACTICE DEPTH`：对成熟 production 的深度；
- `ZERO-TO-ONE RECENCY`：最近一次亲自从未知问题做出 playable / shipped solution 是何时；
- `PROTOTYPE FREQUENCY`：是否仍持续做低成本实验；
- `EXTERNAL LEARNING CHANNEL`：是否持续从组织外摄取新工具、新社区、新范式；
- `UNLEARNING EVIDENCE`：是否曾主动否定自己过去成功的做法；
- `EVALUATOR CAPABILITY`：能否识别自己不会、但别人已经做出可玩证据的新 practice。

于是：

```text
15 years experience
```

只能说明积累时间，不能自动推出：

```text
15 years of frontier-relevant exploration
```

更不能推出：

```text
can teach the next paradigm
```

---

## 5. 与中国商业游戏研究线怎样连接

[005](china-commercial-game-training-role-origin-audit-005.md) 已经证明“程序 / 策划”职位标签太粗，真正值得看的是 prototype authority、design-loop proximity、ownership span、cost visibility 与 creative reserve。

本篇再补一层：

> **即使组织内部存在资深 mentor，也必须先问 mentor 掌握的是哪一种 production regime 的知识。**

因此“中国商业游戏有大量十年以上老兵”不能直接推出：

> 中国拥有同等规模的下一代原创玩法导师。

两者之间缺少一个变量：

### EXPLORATION CAPITAL｜探索资本

可先定义为：

> 在未知问题、低承诺实验、外部现实反馈和反复重定义中形成的能力存量。

与之相对，成熟商业工业可能积累极强的：

### EXECUTION / PRODUCTION CAPITAL｜执行 / 生产资本

两者可以同时很高，也可以严重不对称。

这与 [016](china-catch-up-success-pre-paradigm-creator-016.md) 的 `Production Capital vs Problem-Framing Capital` 相接，但本篇把重点放在**代际复制和教学**：一个产业积累什么能力，会决定它最容易复制给下一代什么能力。

---

## 6. 与 DOOM / early id 的连接：不是“年轻人天然正确”，而是旧链条里没有现成答案

[CASE-016](../../cases/CASE-016-early-id-software.md)、[DOOM纵向母研究](masters-of-doom-longitudinal-master-study-001.md) 与 [043](doom-organizational-aging-rejuvenation-043.md) 的意义，不应简化成“年轻人反抗老人”。

更有研究价值的问题是：

- id 的关键技术、设计与分发组合是否能从当时成熟游戏组织的标准 apprenticeship 中直接学到？
- 哪些能力来自 peer complementarity、快速 shared build、技术窗口与组织外市场接口？
- 当 id 后来自身老化时，曾经的 frontier capability 是否也变成新的 incumbent grammar？

这使 DOOM 成为双向压力测试：

> **边缘团队可能发现旧组织不知道的东西；但今天的异端一旦成功制度化，明天也可能变成新的能力复制者。**

---

## 7. “不教”与“不会”必须在证据上分开

以后所有相关个案至少编码：

| Field | Question |
|---|---|
| `KNOWN_PRACTICE_INSIDE_ORG` | 目标技能在组织内是否已有成熟持有人？ |
| `TRAINING_AVAILABLE` | 是否存在真实 mentoring / junior ladder？ |
| `FRONTIER_PRACTICE_GAP` | 新做法是否超出组织既有知识？ |
| `MENTOR_GENERATION_MATCH` | mentor 的 formative regime 与当前目标 practice 是否同构？ |
| `EVALUATOR_CAPABILITY` | 谁有资格判断新做法，是否亲自做过相似实践？ |
| `HORIZONTAL_DISCOVERY_CHANNEL` | 新能力来自同侪、Jam、mod、开源还是公司内部？ |
| `UNLEARNING_REQUIRED` | 是否必须主动丢弃旧成功经验？ |
| `REALITY_ARBITRATION` | 最终由什么现实信号裁决新 practice？ |

没有这些字段，不应把“junior 不被招”统一解释成：

```text
firm knows how → refuses to teach
```

---

## 8. 对 Hacker / prototype culture 的进一步修正

前序研究强调中国缺乏大型公开原型池、Jam / itch 式横向交流和 scale-down 基本功。这个方向仍值得研究，但必须加两个边界。

### 8.1 横向网络不是天然真理机器

它也可能复制：

- 同温层审美；
- 工具潮流；
- 模因；
- 低商业可行性；
- 对工程和长期维护的忽视。

所以必须保留现实裁决。

### 8.2 大公司也可以内部制造横向探索空间

NExT 类原型制度、内部孵化、小型 autonomous cell 等都可能在 incumbent 内部创造 exploration。

研究问题不是：

> 大公司 vs indie 谁更创新？

而是：

> **谁真正拥有低成本试错权、跨岗位组合权、快速可玩反馈，以及否决旧 benchmark 的权力？**

---

## 9. 对 First-Credit / junior 问题的修正

“企业减少 junior → 训练成本转嫁给个人家庭”仍可能成立，但不能作为唯一解释。

更完整的模型是：

```text
A. Apprenticeship Externalization
known practice exists
but firm underinvests in teaching it

B. Exploration Deficit
target new practice does not yet exist inside firm
so there is nothing mature to transmit

C. Evaluator Capture
firm evaluates frontier candidates
with legacy capability proxies
```

A 是成本分配问题。

B 是知识生产问题。

C 是选择与权力问题。

三者必须分别取证。

---

## 10. 当前最强可保留命题

### H1 — Capability Reproduction Trap

> 一个组织越围绕已验证成功范式招聘、培训与晋升，越可能高效复制既有能力；如果缺少独立的 exploration channel，这种成功本身可能降低新能力被发现、识别和获得 agency 的概率。

**Status: HYPOTHESIS / MULTIPLE INTERNAL ANCHORS / NO POPULATION EFFECT SIZE.**

### H2 — Horizontal Discovery Complement

> 对尚未制度化的新实践，peer / mod / jam / prototype 网络可以补充传统垂直 apprenticeship，因为参与者不是在学习标准答案，而是在共同搜索答案。

**Status: PLAUSIBLE / NEEDS CROSS-ECOLOGY COMPARISON.**

### H3 — Evaluator Capability Constraint

> frontier talent 的选择质量不仅取决于候选人能力，也取决于评价者是否拥有识别目标新 practice 的能力；旧范式资历可能是必要背景，也可能只是错误代理变量。

**Status: PROMISING / NEEDS DIRECT HIRING OR GREENLIGHT EVIDENCE.**

---

## 11. 明确拒绝的强说法

当前不得写成：

- “老一代游戏人不会创新”；
- “年轻人一定比老兵懂新范式”；
- “大厂经验越多越保守”；
- “公司培训没有价值”；
- “Jam / itch 一定比商业公司更会培养人才”；
- “中国缺乏原创只因为老兵把持评价权”。

这些都需要分母和反例。

本篇只要求以后研究时首先问：

> **这条知识真的已经存在于 mentor 所在组织里吗？**

以及：

> **评价 frontier practice 的人，是否真的有能力识别它？**

---

## 12. 下一轮取证

1. 对中国 Role-Origin Dataset 新增 `ZERO-TO-ONE RECENCY / PROTOTYPE FREQUENCY / EVALUATOR CAPABILITY / EXTERNAL LEARNING CHANNEL`；
2. 找“大厂内部成功产生 frontier practice”的反例，防止把 incumbent 写成静态保守机器；
3. 找“横向 indie / Jam 社群集体追错方向”的失败样本，测试 Horizontal Discovery 的边界；
4. 比较同一组织内 exploitation 团队与 exploration cell 的人才晋升和项目裁决；
5. 对 DOOM 2016、NExT、Nintendo / Pocketpair 等已有研究，仅在有直接证据时判断“谁教谁、谁不会什么”，不得从年龄或组织规模倒推。

**Current verdict:** “不训练新人”至少包含成本外包、组织能力上限和评价能力错配三种机制。对新范式而言，垂直 mentorship 可能没有知识可传；横向原型网络的重要性之一，就是在旧组织知识边界之外生产新的 practice。但这一机制目前仍是跨案例研究假说，不得替代数量级和因果检验。
