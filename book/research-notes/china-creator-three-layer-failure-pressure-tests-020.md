# 中国创作者三层失败压力测试 020：自由、经验、支持都不能替代现实验证

- Status: RESEARCH NOTE / FAILURE PRESSURE TEST / PRE-CLAIM
- Last verified: 2026-10-07
- Scope: 教育 × 行业版本现状 × 社会版本意识 × 物质可行性
- Related: `china-creator-constraints-three-layer-map-018.md`, `china-creator-three-layer-pressure-tests-019.md`, `china-catch-up-success-pre-paradigm-creator-016.md`
- Boundary: 本文只用有开发者本人复盘或较完整采访的失败/险失败案例做压力测试。销量差、口碑差本身不等于某一层机制成立。

## 0. 为什么必须专门研究失败者

如果三层框架只收集：

- 王妙一；
- 《太吾绘卷》；
- Carmack；
- Gunpoint；
- The First Tree；

最后很容易退化成：

> “只要保留 Problem Ownership、获得许可、降低成本，就会成功。”

这是错误的。

独立开发真正需要一个更残酷的结论：

> **Problem Ownership 只给你出题权，不给你正确答案。**
>
> **Normative Permission 只给你继续试的资格，不保证玩家会喜欢。**
>
> **Production Capital 只提高做出来的概率，不保证你做的是值得做的东西。**

因此本笔记故意选择三个不同类型的失败压力。

---

## 2026-10-07 重要后续：失败者的第二次机会，不能只看上一次亏了多少

新增完整同期来源研究 [011《边境》→《流浪地球：望日》](../../country-studies/china/011-boundary-wandering-earth-capability-second-chance-2024-2026.md)。2024发行/开发双方对停服责任与付费存在冲突，无法定责；2026-09-10游戏葡萄访问柳叶刀与IP方，开发商承认当年**一年计划实际做七年**、多人竞技商业义务与美术/体验长板错位以及早期生产管线不成熟，失败后靠**外包与小项目**存活。新授权方称其收到近200份团队提案，柳叶刀的太空射击履历成为获得新项目的实际资格；Steam 2026-10仍未发售。

需要将此案例标记为 `SECOND_ATTEMPT_CONTRACT_VERIFIED / NEW_GAME_SHIP_UNKNOWN`，而非 `SUCCESSFUL_RECOVERY`。其新版“导演负责体验、制片人负责资源”的制度是**团队自述并尚未经已上市产物验证的组织改造**。尤其说明 `FAILED_PRODUCT` 可同时产生 `REUSABLE_PRODUCTION_CAPABILITY`，但成立依赖发行/IP采购市场的**第二次合同入口**，不能拿这一存活案例证明失败团队普遍有机会；此前被裁/离开的人员多少得到再入场机会依然未知。

# 一、教育层失败反例：自由、自学、会做东西，也可能没有设计判断

## 1.1 “飞翔的子明”的第一人称复盘

机核用户“飞翔的子明”在 2024 年公开复盘自己两次尝试离职做游戏、最后决定重新找工作的过程。

关键事实：

- 有程序能力，目标方向是 gameplay programmer / technical designer；
- 主动离职后自学、做 3C、研究空气动力学、插件、3D→像素效果、Blender；
- 参加 Game Jam；
- 21 天内确实把平台解谜项目做出来；
- 但试玩结果是“并没有多少人玩明白”；
- 他自己复盘为：设计能力浅、意识流；
- 另一个个人项目则出现“技术先行”，先研究飞行模拟，但没有先定义玩家体验；
- 后续又发现自己喜欢的项目超出单人可完成范围，最终回归就业。

Source:
- 机核 GCORES，《回归工作》，飞翔的子明，2024-11-03  
  https://www.gcores.com/articles/190366

## 1.2 这直接压力测试“自由教育/自学=原创能力”

这个案例里并不缺：

- 自发兴趣；
- 自主学习；
- 技术动手；
- 离开标准职业路径；
- Game Jam；
- 原型能力。

但仍然出现：

```text
会实现
≠
会定义体验

会学习工具
≠
会判断该学什么

能做完原型
≠
玩家能理解／喜欢
```

所以教育层必须继续拆分：

### Learning Agency
我能不能自己学？

### Design Judgment
我能不能判断什么值得做？

### Validation Literacy
我能不能把玩家不理解视为设计反馈，而不是“玩家没看懂”？

### Scope Judgment
我能不能把喜欢的东西缩成自己完成得了的项目？

这四项不能互相替代。

## 1.3 “不被标准答案规训”也可能只是没有反馈

因此三层模型必须防止浪漫化：

> **非标准路径本身不是资产。**

只有当非标准路径同时接上：

- reality feedback；
- measurable iteration；
- taste formation；
- scope control；

它才可能转成原创能力。

否则“自由”可能只是延迟现实裁决。

---

# 二、行业层失败反例：离开腾讯，但旧 objective function 仍可能跟着走

## 2.1 月下 / 《铸仙之境》：最干净的“乙方心态”案例之一

游戏葡萄 2025 年对《铸仙之境》制作人月下（林夏）的长访谈提供了非常直接的自我复盘：

- 他曾任腾讯魔方《王牌战士》执行制作人；
- 离职创业不到两个月拿到悠星和游戏扳机上千万投资；
- 腾讯也曾给出更高投资条件，但没有选择；
- 公司一度扩张到 31 人；
- 后续遭遇版号寒冬、资本环境误判、玩法大改；
- 游戏迭代一年、改了三版，数据越来越差，核心玩家退群；
- 公司一度半年发不出工资，团队从 31 人缩至 10 人；
- 他自己总结：创业三年最大的收获是“不要有乙方心态”；
- 在资金链出问题前，他一直觉得自己只是“换了一个地方上班”，仍然在服务投资方和发行，而不是独立承担市场验证。

Source:
- 游戏葡萄转载，《离开腾讯的制作人：半年发不出工资，31人团队只剩10人》，2025-02-15  
  https://www.sohu.com/a/859551683_204824

## 2.2 这比“腾讯把人训练坏了”更精确

月下不是缺：

- 制作经验；
- 管理经验；
- 大厂流程；
- 资本；
- 团队；
- 行业关系。

真正的问题是：

> **离开组织以后，谁在定义“项目要证明什么”？**

如果创业者仍默认：

```text
投资人 / 发行
→ 给目标
→ 我组织团队完成
```

那么即使形式上已经创业，认知上仍然可能处在：

> **Client-serving Production Mode**

而不是：

> **Market-discovery Founder Mode**

这就是行业层真正的 objective-function lock-in。

## 2.3 所以“离开大厂”不是切换完成

需要审计：

- 谁决定 roadmap？
- 谁决定 target player？
- 数据差时是为投资人改，还是为用户问题改？
- 团队是否直接接触核心用户？
- 创始人是否拥有杀掉原假设的权力？
- 资金是 runway，还是新老板？

因此：

> **Exit from Organization ≠ Exit from Evaluation Function**

这句话应作为行业层固定检查项。

## 2.4 资本也不能自动买来 Problem Ownership

《铸仙之境》还压力测试了一个常见幻想：

> “如果小团队有钱，就能创新。”

事实是资本可以提供：

- 工资；
- 招聘；
- 试错时间；
- 生产质量。

但如果 objective function 仍外置，资本可能只是让错误方向迭代得更久。

这与 `Capitalized Error Persistence` 直接相连。

---

# 三、社会/物质层失败反例：有钱、有团队、有公司支持，产品照样可以错

## 3.1 《重装前哨》：不是“被资本逼死”的简单故事

李秋果对《重装前哨》的公开复盘非常有价值，因为它不是“公司不给机会”的案例。

他总结首发失败主要包括：

1. 宣传与真实产品体验错位；
2. 产品打磨不足，首发存在严重崩溃问题；
3. 商业化/数据目标使研发中途把游戏时长拉长，产品思路变形；
4. 自己在团队扩大后仍然用小团队时期的亲力亲为管理方式，导致信息流、创意授权和决策质量下降。

更重要的是：

- 首发失败后，公司董事长明确表示投资方没有放弃团队；
- 团队没有立即被砍；
- 研发人员继续修复、更新和复盘。

Source:
- 游戏葡萄整理转载，《从备受期待到首发崩盘，上市公司董事长却对制作人说：咱都没垮》，2024  
  https://www.taptap.cn/moment/599101926432312276

## 3.2 这是“支持也不能替代产品正确性”的关键压力

这个案例里并不缺：

- 组织资源；
- 资金；
- 团队；
- 公司许可；
- 失败后的第二次机会。

但玩家仍然用首发反馈指出：

> 预期错了、体验错了、技术质量不够。

所以：

> **Normative Permission、Economic Runway、Institutional Support 只能延长探索生存期，不能替代 Reality Feedback。**

这正好封住社会层最容易形成的浪漫化：

> “只要社会宽容失败，中国就会自然出现好游戏。”

不对。

宽容失败的价值是：

> **让团队有机会真正学会为什么失败。**

而不是让失败自动变成创新。

## 3.3 《重装前哨》还揭示了“创始人路径依赖”

李秋果自己的团队复盘指出：

- 6 人阶段，他亲自把控大量内容是合理的；
- 团队扩大后，他仍然保持同样方式；
- 80% 时间做业务、20% 做管理；
- 信息同步不足；
- 其他成员逐渐只按“秋果想要的”执行；
- 创意没有真正释放；
- 原本自认为擅长整合团队产出的制作人，反而把团队拉进自己的单一路径。

这其实是一个很漂亮的内部 competency trap：

```text
早期成功的小团队工作方式
→ 团队扩大
→ 旧方式继续使用
→ 旧能力从优势变成瓶颈
```

所以“春登/版本锁定”并不只发生在年龄、教育或大厂。

> **一个独立制作人也可以被自己上一阶段的成功锁住。**

---

# 四、三例放在一起后的修正

| 失败样本 | 看起来拥有 | 实际缺口 |
|---|---|---|
| 飞翔的子明 | 自由、自学、技术、原型 | design judgment / experience definition / scope |
| 月下 / 铸仙之境 | 腾讯制作经验、资本、团队 | founder-mode objective function / market discovery |
| 重装前哨 | 公司支持、资金、团队、第二次机会 | product-market expectation alignment / quality / org scaling |

所以以后不能再把任何单项资产神化：

### Problem Ownership
不是正确答案。

### Production Capital
不是产品判断。

### Normative Permission
不是市场需求。

### Economic Runway
不是验证结果。

### External Knowledge
不是自主问题定义。

### Freedom
不是 taste。

---

# 五、Creator Debugger 增加一个新的硬检查：Reality Adjudication

018/019 已经有：

- Problem Ownership；
- Validation Rights；
- Exploration Survival Time；
- Exit–Portability–Recombination；
- Material Feasibility。

020 进一步要求显式记录：

> **Reality Adjudication｜现实裁决是否真正进入决策？**

至少问：

1. 谁是第一批真实玩家？
2. 他们是否理解核心体验？
3. 哪些反馈被团队拒绝？为什么？
4. 失败时团队修改的是产品，还是只修改宣发？
5. 数据恶化是否会杀掉创始人最喜欢的设计？
6. 是否有足够早的 cheap validation？
7. 团队是否把“完成度”误当成“正确性”？

因此 Creator Debugger 的最低闭环应是：

```text
Problem Ownership
→ Cheap Prototype
→ Reality Adjudication
→ Model Update
→ Survival to Next Test
```

少任何一项都可能产生伪创新。

---

# 六、三层模型的第二次正式修正

## 教育层

以前问：
> 有没有自己出题？

现在还要问：
> **有没有能力发现自己出的题其实很差？**

## 行业层

以前问：
> 是否卸载旧 Benchmark？

现在还要问：
> **离开旧组织后，评价函数是否真的内生化到创始人与真实用户之间？**

## 社会层

以前问：
> 有没有偏离生存期？

现在还要问：
> **这段生存期里有没有高质量现实反馈，还是只是在给错误方向续命？**

因此：

> **Survival Time without Reality Feedback = Error Persistence**

这一句应该长期保留。

---

# 七、对“农民发明家”的进一步约束

020 也反向修正前面的“农民发明家/前范式创作者”模型。

真正健康的前范式创作者必须同时满足：

- Problem Ownership；
- Cheap Experimentation；
- Reality Adjudication；
- External Knowledge Absorption；
- Scope Discipline；
- Capability Scaling。

只拥有“自己想做什么就做什么”并不够。

因此：

> **问题主权 ≠ 真理主权。**
>
> **自由探索 ≠ 免于验证。**

---

# 八、当前证据状态

### STRONG

- 第一人称公开复盘足以证明：自学/技术/原型能力与成熟游戏设计判断不是同一能力；
- 月下案例直接支持“退出大厂后仍可能延续 client-serving / 乙方评价函数”的机制；
- 《重装前哨》复盘直接支持“组织支持和资金不能替代产品判断与技术质量”；
- 小团队时期有效的创始人控制方式，可以在团队扩大后变成 competency trap。

### HYPOTHESIS

- “乙方心态”是否是中国大厂制作人创业失败中的高频机制；
- 中国独立开发者是否普遍低估 Reality Adjudication、过度重视“做完”；
- 高社会/物质支持是否可能增加错误续命，而非只增加健康探索。

### REJECT

当前不允许：
- “差生/自由人更适合独立开发”；
- “大厂人创业一定摆脱不了大厂”；
- “资本支持反而有害”；
- “玩家反馈永远正确”；
- “失败只要坚持就能学到东西”。

