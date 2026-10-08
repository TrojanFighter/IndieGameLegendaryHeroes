# 中国商业游戏训练反转假说：岗位、反馈回路与独立游戏能力迁移审计

- Status: RESEARCH NOTE / HYPOTHESIS / ROLE-ORIGIN AUDIT v1
- Last verified: 2026-10-06
- Scope: 中国商业游戏从业者转向 premium / small-team / author-driven production 时的能力迁移；重点观察腾讯及相邻样本
- Related: `china-indie-dual-environment-capability-transfer-004.md`, `china-game-commercial-regime-lineage-003.md`, `CASE-028 Chinese Online Game`, `CASE-038 Sultan's Game`
- Claim status: **NOT A FORMAL CLAIM**

> **2026-10-08制度补证入口**：[050 — NExT × 网易Mini × Supercell Spark](creator-selection-institution-comparison-050.md)。新增2018同期NExT孵化项目数/100人天评审与网易新人六周Demo、2025 Supercell选团队制度，以免将“存在个别原型策划”误写成“商业大厂没有或普遍拥有原创作者训练”。本文件现有职业便利样本仍不得当作发生率分母。

## 0. 研究问题：真正需要检验的不是“程序员是不是比策划更会做独立游戏”

一个反复出现的中国游戏行业观察是：

> 一些商业游戏体系出身的程序、技术、美术或文案，在转向极小团队项目后，做出的产品反而比部分受过成熟商业游戏“专业策划训练”的从业者更接近作者型独立游戏的生产逻辑。

这个观察有研究价值，但最粗糙的版本——“程序员 > 策划”——目前证据不足，而且会把完全不同的岗位训练误压成一个二分法。

更精确、也更可证伪的候选命题是：

> **当一个产业长期围绕特定商业目标训练岗位时，它会同时制造可迁移的专业能力与只适用于原目标函数的职业先验。进入 premium / small-team / author-driven production 后，后者如果未经转换，可能形成负迁移。一个岗位越接近可玩原型、实现成本、完整玩家反馈与端到端产品 ownership，转换距离可能越短；但职位名称本身只是弱代理。**

本笔记暂称：

- **Commercial-Game Training Inversion Hypothesis / 商业游戏训练反转假说**；
- 子问题：**Role-conditioned Design Transfer / 岗位条件化设计迁移**。

当前不接受以下强说法：

- 程序员天然比策划更懂游戏；
- 腾讯策划普遍不适合做独立游戏；
- 商业手游经验总体有害；
- “独游味”可以靠职位标签直接预测。

---

## 1. “目标函数反转”应当拆成职业训练问题，而不是审美鄙视链

商业 F2P / live-service 与 premium 小团队并不是两个互斥世界。两边都需要玩家体验、留存意义上的“愿意继续”、商业判断、数据和制作纪律。

真正可能发生冲突的是：**某个岗位长期被什么指标奖励、什么问题被反复要求解决。**

下表不是全行业事实，而是待检验的“目标压力差异”模型：

| 商业 F2P / live-service 中常见的岗位压力 | premium / 极小团队常见的约束压力 | 可能发生的迁移问题 |
|---|---|---|
| 长期留存、用户生命周期 | 有限作品内的总体满意度与完整体验 | 把“延长使用”误当成“增加价值” |
| 养成、投放、经济稳定 | 每一个系统是否值得占据 scope | 为维持循环而增加不必要层级 |
| 高频版本与长期内容消耗 | 在有限 runway 内完成并 ship | 把无限运营习惯带入有限作品 |
| 用户分层、高付费深度 | 是否完整满足目标受众 | 目标玩家定义可能被“大盘最大化”替代 |
| 数据指标、线上验证 | taste / fantasy / feel + 可玩验证 | 只信可量化代理变量，忽略难量化体验 |
| benchmark / 成熟品类范式 | differentiation / novelty / store hook | 把对标当成立项本身 |
| 大组织专业分工 | generalist ownership / 直接协作 | 默认“缺岗位”而不是先重新定义问题 |
| 组织可交付、方案通过 | idea → playable → fail/delete | 优化“怎样让方案被组织执行”而非“怎样让东西本身成立” |

重要边界：

1. premium 游戏也会关注留存、漏斗和转化；
2. F2P 团队也大量关注手感、乐趣、世界观和原创性；
3. 大公司中不同岗位面对的目标函数差异极大；
4. 因而研究对象必须从“公司/职位”下钻到**岗位子类型 + 反馈回路 + ownership span**。

---

## 2. 比“程序 / 策划”更值得测量的六个变量

### 2.1 Design-loop proximity / 设计闭环距离

从产生想法到亲手看到可玩结果需要经过多少组织节点？

```text
短：idea → prototype → play → delete / iterate
长：idea → 文档 → 评审 → 排期 → 多岗位实现 → QA → 线上数据 → 再修改
```

短闭环不保证设计好，但会让错误更快暴露给提出者本人。

### 2.2 Prototype authority / 原型权

个人是否有权直接做一个能玩的东西，而不是先获得完整项目资源？

凉屋 2017 年的公开团队描述提供了一个极端清楚的组织样本：任何成员都可做原型，原型验证有效后就可能成为自己的项目；单项目通常 1–3 人，常由程序担任制作人。

### 2.3 Ownership span / 产品 ownership 跨度

一个人负责的是单一模块，还是需要同时承担：

- 核心循环；
- scope；
- 实现成本；
- 体验测试；
- 市场接口；
- ship；
- 发售后代价？

极小团队制作人往往被迫看到完整因果链。

### 2.4 Cost visibility / 实现成本可见度

提出一个系统的人，是否同时知道它会增加多少代码、美术、动画、QA、文本与维护负担？

程序 generalist 的潜在优势并非“技术人更聪明”，而是机制构想与实现代价可能存在于同一认知回路里。

### 2.5 Feature-kill authority / 删除权

发现不好玩、做不起或价值不足时，是否可以快速砍掉，而不需要维护已经形成的跨部门承诺、KPI 或 sunk cost？

### 2.6 Creative reserve / 创作储备

正式项目之外，一个人是否长期积累：

- 私人 prototype；
- 小说 / 剧本；
- mod / 工具；
- 未被采用的机制；
- side project；
- 长期玩家经验与个人 taste？

这类储备意味着“独立后突然有创意”可能是假象：创作资本早已形成，只是旧组织没有给它产品权。

---

## 3. 腾讯本身就证明“策划”不是一种训练

为了避免把讨论变成公司标签，本轮抽查了腾讯 2026 年公开招聘中的不同游戏岗位。它们不能代表 2010s 的历史岗位，也不能证明某位前员工当年受到同样训练；用途只是证明：**同一家公司今天就同时存在完全不同的工作反馈函数。**

### 数值 / 经济岗位

当前《部落冲突》资深数值策划职责包括英雄/关卡战斗数值、养成与投放经济数值，并要求有经过线上验证的战斗/经济模块经验。

这类岗位天然训练：

- 平衡；
- 经济结构；
- 长期稳定；
- 在线验证；
- 对复杂系统的精确控制。

这些能力可以迁移，但也可能使“多一层成长系统”成为熟悉的默认解法。

### 系统 / 线上岗位

当前《三角洲行动》系统策划与其他系统策划岗位强调主流程、成长系统、表格、竞品运营、统计数据、线上反馈与持续优化。

这类岗位对 mature product optimization 很强，但与从零选择“什么问题值得做”不是同一个任务。

### 关卡 / 技术 / 创意原型岗位

腾讯当前开放世界关卡策划岗位明确要求用 3D 引擎搭白模、验证可行性并持续根据玩家体验迭代；技术/AI 创作岗位也强调从创意到可玩结果的快速验证。

小枝对自己在 NExT 的旧岗位描述更直接：创意原型孵化 / gameplay 或技术策划，需要快速把想法做成白盒，通常每周甚至两三天迭代一个核心玩法。

因此：

> **“策划训练”至少要分成 meta/economy/live-ops、系统、关卡/gameplay、technical/prototyping、narrative 等多种子类型。**

如果把小枝和一个长期负责 F2P 经济投放的数值策划都编码成“腾讯策划”，研究变量已经失真。

---

## 4. Role-Origin Audit v1：腾讯及相邻样本

当前样本仍是 convenience sample，不用于计算成功率。它只用于寻找机制、反例和下一轮取证方向。

| 样本 | 原岗位 / 前史 | 原型权 / ownership 特征 | 转向后的可观察 maneuver | 当前证据读法 |
|---|---|---|---|---|
| **凉屋游戏早期组织** | 非腾讯；深圳独立团队 | 全员可原型；1–3 人项目；通常程序制作人 | 原型验证后立项；先考虑擅长/想做什么，再考虑市场 | **强机制样本**：短闭环与程序制作人制度可存在，但不是职位优越性的因果证明 |
| **庾楼月 /《末剑》** | 腾讯程序；入职前已自己写引擎、做游戏 Demo | 自己做可玩 Demo；内部孵化 | 围绕“御剑”单核心交互组织体验 | **支持但有强 selection confound**：作者性和动手习惯在进腾讯前已存在 |
| **乌鸦 /《末刀》** | 程序出身，约 10 年开发/主程，后转策划通道 | 先做内部 Demo，再同事试玩、技术测试 | 移动/挥刀/冲刺；敌我一刀即死；主动压缩成长/数值复杂度 | **很强的“deliberate reduction”样本**；但本人已跨程序→策划，不能作为纯程序组 |
| **Hellson + GamerJ /《迷失幻途》** | 腾讯旧同事；视觉设计 + 程序 | 两人共同决定 scope；直接迭代玩法 | 明确放弃想做的银河城，因为美术量会把团队拖死；改做卡牌+战棋；Demo 后获发行预付款 | **强 capability-shaped product selection 样本** |
| **咖啡 /《因狄斯的谎言》** | 软件开发→腾讯制作人；研发/策划/Demo/测试/管理全链路 | broad producer ownership | 形成内容扎实、结构完整的小团队产品；制作人自述独立制作更像 generalist “打杂” | **强反例**：成熟商业 production competence 可以显著正迁移；不能把“专业化”整体判负 |
| **邱崇志 + 陈帅 /《伏龙记》** | 腾讯主文案 +《怪物猎人OL》主策；13 年从业 | 6 人创业团队 | 主创回顾早期认为“做十几年游戏，别人能赚钱为什么我们不能”，离开腾讯后被现实教育 | **过度自信 / 创业世界模型 comparator**；不能仅凭产品风格证明“策划训练导致失败” |
| **郑德权 /《一亿小目标》《逐光：启航》** | 腾讯数值策划，MMO/MOBA | 小团队快速做 Demo；2–3 周一个方向，上 TapTap 验证 | 把长养成压缩成一局；先制作人 idea，Demo 后再用吸量/留存数据调优；后来明确讨论“作者游戏” | **策划侧强反例**：旧技能可被反转/重组，数据能力不必统治立项 |
| **Loka /《声探疑云》** | 腾讯 NExT《疑案追声》主策，后在大项目做文案/策划 | 2025 离职，自费 4 人团队；自己承担制作/编剧/配音导演，保留最终修改权 | 要求尽早用粗 Demo 测试；自己参与每一环；玩法/关卡优先于单纯剧本文案 | **策划侧强反例**：高 ownership + 原型/关卡导向比“策划”职位更有解释力；新作尚未正式发售 |
| **小枝 /《太太！我喜欢你！》** | 腾讯 NExT 创意原型孵化；gameplay/技术策划 | 白盒原型、两三天到一周迭代；本人能策划+程序 | 2018 主题原型；2021–2022 多个 side prototype 分拆验证收集/代餐/创作/社交，最后合并为完整产品 | **最强岗位异质性反例**：她名义上是策划，但训练函数极接近 programmer-producer |
| **Double Cross /《苏丹的游戏》** | 商业手游老兵混合团队；十字星长期班底 | 组织崩塌后极小团队直接暴露个人能力 | 放弃高规格竞争；按现有人才重构 scope；故事/文本/卡牌承载主要复杂度；管理规范显著放松 | **强“规训解除 + 能力重组”样本**；不能推出手游训练总体有害 |
| **刘永涛 / 648工作室 /《中国式网游》** | 制作人实名已有公开活动资料；当事人直接个人通信确认此前任凉屋程序，具体年份/项目未知 | 官方自述 solo、业余约五年、策划/程序/简单美术一人承担 | 不复制 MMO 组织/服务器，而把氪金、成长、排行榜等“网游玩家经验”改造成买断单机模拟/讽刺 | **Domain Knowledge Inversion + programmer-generalist 候选**；但凉屋本身是特殊 programmer-producer 制度，不能代表普通商业手游程序岗位 |

---

## 5. 第一轮结果：职位名称的解释力下降，feedback architecture 的解释力上升

### 5.1 程序出身样本确实频繁出现“核心交互集中 + 快速原型 + scope 可见”

《末剑》《末刀》《迷失幻途》和凉屋早期组织都支持一种机制可能性：

```text
想法
→ 提出者本人或极近协作者直接实现
→ 很快得到可玩反馈
→ 实现成本同步暴露
→ 删除 / 修改 / 继续
```

这种回路与极小团队 premium production 高度匹配。

但这里不能偷换为“程序员 taste 更高”。

庾楼月在进入腾讯前已经自己写引擎和 Demo；乌鸦本身后来转入策划通道；GamerJ 是“愿意离开稳定组织并长期做独立项目”的非随机程序员。我们看到的是经过强烈自选择后的 programmer-generalist 子集。

### 5.2 策划侧反例直接击穿“程序 > 策划”

小枝尤其关键：她的职位就是 gameplay / technical planner，但日常训练是白盒、快速原型、亲自实现、两三天一轮。这种 feedback architecture 和凉屋“程序制作人”其实比和大型 F2P 数值策划更接近。

Loka同样说明，策划一旦拥有：

- 全产品控制权；
- 直接玩家测试；
- 自己承担真实现金成本；
- 改版/延期/删改最终权；

其行为也会明显向 author-driven small-team production 收敛。

郑德权则证明数值策划也能完成 deliberate inversion：不是忘掉数值和数据，而是把原先的长养成压缩成单局结构，并把数据放在 Demo 后验证，而不是让指标代替 project selection。

### 5.3 最强的正迁移往往来自“广义制作能力”，不是岗位纯度

咖啡从软件开发转制作人，积累研发、策划、Demo、测试和管理的完整链路。他的案例反而提示：

> 大公司经验如果扩大了一个人的 ownership span，而不是把他压成狭窄模块专家，可能非常适合独立团队。

因此“商业训练反转”真正反转的不是**专业能力本身**，而可能是：

- 只在既定题目内优化的习惯；
- 对高规格组织的依赖想象；
- 把成熟 benchmark 当成问题定义；
- 把线上指标代理变量当成完整产品价值。

---

## 6. 《伏龙记》提供的不是“策划做独游失败”，而是 world-model reset 的负压力样本

《伏龙记》两位核心创始人有非常成熟的大厂履历：主文案、主策、约 13 年行业经验。

他们在 2017 采访里自己回顾创业前的判断：做了十几年游戏、见过很多项目，于是自然觉得“别人能赚钱，我们为什么不能”；离开腾讯后才被创业现实重新教育。

这条证据支持的是：

> **大组织中的“我会做游戏”与“我能用六个人承担完整产品、现金流、发行、市场、scope 和生存风险”不是同一个能力集合。**

它不支持：

> 文案/策划不如程序。

要真正证明 Role-conditioned Design Transfer，必须比较同等 runway、品类、团队规模和 ownership 条件下，不同职业前史人群的行为差异，而不是用一个项目成绩做职位归因。

---

## 7. 《苏丹的游戏》补出了此前讨论中最重要但容易漏掉的一层：Creative Reserve

2025 年钻咖应游戏葡萄邀请写的创作复盘给出了一条非常强的直接证词：

- 《苏丹的游戏》从她已经写完的一篇短篇小说生长出来；
- 小说中已经存在“苏丹强迫别人玩游戏”“苏丹卡”等规则种子；
- 团队过去合作也常以内部已经成型的故事作为立项起点；
- 一篇可读故事能同时给文案提供 voice sample、给美术提供概念理解、给策划提供可转成关卡的素材，汇合后接近 vertical slice。

Steam 后来直接把《一个适合苏丹的游戏》作为“原著小说”DLC 发布，也确认小说与游戏之间不是事后营销编造的关系。

这形成一个新的子假说：

> **Creative Reserve Hypothesis：职业组织之外长期形成的私人作品、原型和兴趣资本，可以在组织条件改变时迅速转化为 product seed。**

它解释了为什么一些从业者离开旧制度后看起来像“突然会创作了”：

```text
能力/题材/故事/机制储备
早已存在
↓
旧组织没有给它产品权
↓
组织收缩 / 离职 / side project / 小团队
↓
储备第一次获得立项权
```

这同样不是《苏丹》独有。小枝在腾讯任职期间不断把同人生活经验拆成多个低成本 prototype；庾楼月在进入腾讯前已经完成个人 Demo。两者都说明正式项目时间线可能严重低估此前私人创作资本。

当前状态：**PROMISING SUBHYPOTHESIS / NEEDS MORE CASES**。

---

## 8. 刘永涛 / 648 /《中国式网游》更适合作为 Domain Knowledge Inversion，而不是用作品反推履历

截至本轮检索，公开可可靠确认的是：

- 小黑盒 2024 金盒奖活动页把刘永涛标为《中国式网游》制作人；
- 648工作室为单人核心；
- 约 2018 年立项；
- 大量策划、程序和简单美术由作者利用业余时间完成；
- 开发约五年；
- 游戏把中国网游的充值、成长、排行榜、活动和付费文化重新包装成买断单机模拟/讽刺体验；
- publisher 为 Wise Games。

职业前史现在获得一条当事人直接个人通信：刘永涛本人确认此前曾任凉屋游戏程序岗位。该条没有公开 URL，因此必须标注 firsthand personal communication；具体任职年份、参与项目与职责边界仍缺公开 corroboration。作品本身不能承担这些履历事实的证明。

因此本案当前最稳妥的研究概念是：

### Domain Knowledge Inversion / 领域知识反转

不是把熟悉的商业网游知识继续用于生产另一个长线网游，而是：

> **把旧产业的系统语言本身变成可供玩家消费、反思和讽刺的游戏对象。**

即使未来证明作者确实有商业从业前史，也应该把“职业履历证据”和“作品的领域知识反转结构”分开记录。

---

## 9. 当前最强版本的“商业游戏训练反转假说”

### H1 — Objective-function mismatch

> 商业游戏职业训练中的一部分能力针对特定收入、留存、运营和组织目标优化；迁移到 premium small-team production 时，如果目标函数已经改变而职业先验未改变，可能产生负迁移。

**Status: PLAUSIBLE / MECHANISM SUPPORTED / CAUSAL GENERALIZATION NOT YET PROVEN.**

### H2 — Design-loop proximity

> 在极小团队项目里，距离 playable prototype、实现成本和直接玩家反馈更近的职业经历，可能比“策划/程序”职位标签本身更能预测 scope judgment 与快速删改能力。

**Status: STRONGER THAN ROLE-TITLE VERSION / NEEDS LARGER SAMPLE.**

### H3 — Ownership-span transfer

> 具有跨研发、测试、制作、scope 与 ship 经验的商业从业者，可能比长期局限在单一模块的人更容易完成独立项目的角色转换，无论原职位叫程序、策划还是制作人。

**Status: SUPPORTED BY CONTRAST CASES, NOT YET FORMAL CLAIM.**

### H4 — Creative Reserve

> 私人小说、prototype、mod、工具和长期兴趣可能构成被正式公司低估的“创作储备”；组织变化后，它们可以迅速成为新项目的 premise / vertical-slice seed。

**Status: PROMISING SUBHYPOTHESIS.**

### REJECTED CURRENT FORMULATION — “程序员比策划更适合做独立游戏”

当前证据直接存在多组反例，而且“策划”内部训练函数差异过大。这个句子不应进入正式 Claim。

---

## 10. 必须正面处理的偏差与反例

### 10.1 Survivor / selection bias

愿意离职、业余做五年项目、主动参加内部孵化的程序员，本来就不是随机程序员。

### 10.2 Pre-existing author bias

《末剑》作者入职腾讯前已经做个人游戏；不能把后来的作者性归因于“腾讯程序训练”。

### 10.3 Role switching

《末刀》作者程序出身、做过主程，后来转策划。把他硬编码进任意一侧都会失真。

### 10.4 Incubator ≠ independent ownership

《末剑》《末刀》是腾讯内部/相关孵化环境中的作者项目，能够调用大公司美术、技术、测试等资源，不等于离职创业的 production perimeter。

### 10.5 Planner heterogeneity

小枝的“策划”工作就是直接做可玩白盒；Loka是叙事/关卡型作者；郑德权是数值策划。三者不能合并成同一 treatment group。

### 10.6 Outcome bias

本轮主要是被媒体采访、已经做出作品的人。失败、取消、未发售、低评价项目严重缺失。

### 10.7 Genre / platform confound

动作核心、卡牌、文字叙事、模拟经营的最优 scope 不同；不能把“系统少”直接当成“独游味更纯”。

---

## 10.8 下一轮 Role-Origin Dataset 新增强制字段

本轮四案例与截图摄取显示，原来的 role-title 编码仍然不够。后续每个人必须再补：

- **formative regime**：真正形成能力的生产制度，而不是最后一家公司；
- **adaptive regime**：后来为了市场/岗位临时适配的制度；
- **team continuity**：与核心同伴共同 ship / prototype 的年限；
- **benchmark dependence**：无 benchmark 时是否还能工作；
- **time-to-playable**：idea 到 playable 的典型延迟；
- **capital-at-risk-before-validation**：验证前已有多少人力/资金暴露；
- **error persistence cost**：重大错误能活多久；
- **market-interface literacy**：是否知道目标玩家在哪、如何得到付费反馈；
- **platform capital dependence**：旧组织替个人提供了多少默认能力；
- **unlearning evidence**：是否主动删掉旧 regime 的做法。

这些字段优先于“程序/策划”二分。

## 11. 下一轮应该怎样把它做成真正可检验的人才史研究

### 11.1 建立 Role-Origin Dataset，而不是继续收段子

目标至少 30–50 名中国商业游戏→小团队/indie 转型主创，逐项编码：

- 原公司；
- 原岗位与**岗位子类型**；
- 在旧项目中的 ownership span；
- 是否能写代码 / 搭白盒 / 独立做 prototype；
- idea→playable latency；
- 是否拥有 feature-kill authority；
- 是否直接接触玩家；
- 是否负责过 ship / live / P&L；
- 离职前是否已有 side project / 小说 / mod / prototype；
- 独立后第一作团队规模、runway、publisher、外包外围；
- 第一作是否沿用原岗位典型系统语法；
- 是否明确出现 deliberate unlearning；
- 成功、失败、取消与长期未发售都必须计入。

### 11.2 “独游味”必须操作化，不使用印象打分

可观察指标建议拆成：

- 核心 loop 集中度；
- meta / economy / progression 层级数量；
- 是否围绕一个新交互组织产品；
- scope 是否从团队能力倒推；
- 立项前是否有 playable prototype；
- 重大 feature deletion 次数与理由；
- benchmark 使用方式：验证市场还是直接定义产品；
- authorial premise 的来源；
- 商店 hook 可解释性；
- 首发前真实玩家测试次数。

这些指标仍需盲测/双人编码，否则研究者会把自己喜欢的游戏自动判成“更独立”。

### 11.3 腾讯内部最有价值的对照不是“程序 vs 策划”，而是同公司不同 feedback architecture

优先找：

1. 长期数值/经济/live-ops → indie；
2. gameplay/level/technical prototype planner → indie；
3. gameplay/client programmer → indie；
4. narrative writer → indie；
5. producer / PM → indie；
6. 同岗位但没有转型成功或项目取消的负样本。

如果控制公司文化后，仍然发现 prototype authority、ownership span 与独立项目完成/设计压缩之间存在稳定关系，这个假说才真正开始站住。

### 11.4 刘永涛身份已公开核定，职业履历继续单独核

当前制作人实名已由公开活动资料解决；此前任凉屋程序岗位由当事人直接个人通信确认。具体任职年份、参与项目与职责边界仍需要公开履历、credits、采访或前公司记录继续核验。不得用《中国式网游》的题材熟悉度代替超出证词范围的职业履历证据。

---

## 12. Source anchors / 第一轮外部证据

### 组织与程序制作人

- 游侠网 / 凉屋游戏采访（2017-04-27）：“全员可做原型”“项目 1–3 人”“通常程序作为制作人”。  
  https://www.ali213.net/news/html/2017-4/293569.html
- 游戏茶馆转载同一访谈。  
  https://youxichaguan.com/archives/57624

### 腾讯程序 / mixed-role 样本

- 游戏之音 / 新浪：《末剑》制作人庾楼月采访；2015 入腾讯、一直做游戏程序。  
  https://k.sina.cn/article_6622677490_18abe09f200100ecsw.html
- 游戏日报：《末剑》大学个人 Demo / 自写引擎→入腾讯前史。  
  https://www.sohu.com/a/561179849_118576
- 游戏日报：《末刀》乌鸦采访；软件/程序出身、约十年开发与主程后转策划通道；先做内部 Demo 再技术测试。  
  https://news.yxrb.net/202207/07230185.html
- 游戏日报：《迷失幻途》Hellson + GamerJ；两人 scope、放弃银河城、Demo 后发行预付款、日本销量早期高于中国。  
  https://news.yxrb.net/2022/1117/456.html

### 商业制作能力正迁移 / 策划反例

- 有饭研究 / TapTap：《因狄斯的谎言》制作人咖啡；软件开发→制作人，全链路能力。  
  https://www.taptap.cn/moment/303970499682109390
- 机核：《伏龙记》主创访谈；腾讯主文案 +《怪物猎人OL》主策，创业前后 world-model reset 自述。  
  https://www.gcores.com/articles/24382
- GameRes / 游戏葡萄：郑德权；腾讯数值策划，6 人团队用 2–3 周 Demo 快速试错，《一亿小目标》把商业经验重组为单机化结构。  
  https://www.gameres.com/881854.html
- 游戏日报：郑德权回顾《一亿小目标》为“网游设计思路的单机化”，并讨论后来从买量昂贵赛道继续转向。  
  https://news.yxrb.net/mobile/index.php?a=show&c=index&catid=7&id=370&m=mobile
- 数数科技：郑德权“作者游戏”分享。  
  https://www.thinkingdata.cn/thinking/course/3217.html
- 游戏葡萄 / TapTap：Loka《声探疑云》，自费、4 人、全环节参与、粗 Demo 早测与玩法优先。  
  https://www.taptap.cn/moment/835782571051713477
- 游戏葡萄 / TapTap：小枝《太太！我喜欢你！》，腾讯创意孵化前史与多个 side prototypes。  
  https://www.taptap.cn/moment/561046714060899432
- 手游那点事 / 新浪：小枝详细解释 NExT 创意原型孵化岗位，两三天/每周一轮原型，本人策划+程序。  
  https://cj.sina.com.cn/articles/view/2611781342/9bac9ede01901hkha

### 刘永涛 / 648

- 小黑盒 2024 金盒奖活动页：公开标注“刘永涛 / 《中国式网游》制作人”。  
  https://web.xiaoheihe.cn/activity/heybox_gold_2024
- CASE-028 与独立 Evidence Ledger 继续承担当事人身份、solo / part-time 开发与职业履历证据边界；其中“此前任凉屋程序岗位”为当事人直接 personal communication，具体年份/项目仍待公开 corroboration；凉屋组织制度的公开纵向比较见 `chillyroom-programmer-producer-to-plannerized-live-service-007.md`。

### Sultan's Game / Creative Reserve

- 游戏葡萄（钻咖主创复盘，搜狐可访问转载）：《苏丹的游戏》从已完成短篇小说生长；团队惯用成型故事作为立项起点；故事同时服务文案、美术、策划与切片构建。  
  https://www.sohu.com/a/884557438_204824
- Steam 官方 DLC：《一个适合苏丹的游戏》明确标为游戏原著小说。  
  https://store.steampowered.com/app/3728320/

### 当前腾讯岗位：只用于证明岗位训练异质性，不倒推历史个人经历

- 腾讯招聘：《部落冲突》资深数值策划——战斗数值、经济数值、养成与投放。  
  https://careers.tencent.com/jobdesc.html?postId=2087091672277233664
- 腾讯招聘：开放世界关卡策划——3D 引擎白模、可行性验证、玩家体验迭代。  
  https://careers.tencent.com/search.html?keyword=demo
- 腾讯招聘：《三角洲行动》系统策划——主流程/成长、表格、竞品运营、统计数据与反馈迭代。  
  https://careers.tencent.com/jobdesc.html?postId=1942052496046424064
- 腾讯招聘：3C 客户端开发——核心玩法技术可行性、操作手感与跨团队落地。  
  https://careers.tencent.com/jobdesc.html?postId=2086656013209092096

## 13. 当前结论边界

截至 2026-10-06，本轮研究最多支持：

> **中国商业游戏训练存在“能力资本 + 目标函数特化”双重效果。进入极小团队 premium production 后，决定迁移难度的关键变量可能是 design-loop proximity、prototype authority、ownership span、cost visibility 与 creative reserve，而不是职位名称本身。**

它还不能支持：

> “腾讯程序员系统性比腾讯策划更会做独立游戏。”

下一轮必须靠更大的 Role-Origin Dataset、失败样本和岗位子类型对照来决定这个更强假说是否成立。


---

## 14. 2026-10-08 关键纠偏：缺训练不等于“会而不教”

本轮新增一个必须写进后续分析的边界：

> **不能默认老一代 / 资深从业者已经掌握目标新范式，只是因为成本、保守或利益而不愿意教新人。很多时候，旧 production regime 的资深者本人就没有亲自形成这种 frontier practice。**

因此“junior 不被招 / 不被教”至少拆成：

1. **TRAINING WITHHOLDING**：组织会这套已知 practice，但不愿承担培养成本；
2. **INCUMBENT CAPABILITY CEILING**：目标新 practice 尚未存在于组织知识库，mentor 本身没有可传授的成熟答案；
3. **EVALUATOR CAPABILITY GAP / DEFENSIVE CONSERVATISM**：组织用旧成功范式的代理指标评价自己并不熟悉的新能力，于是“不会识别”可能表现成“这不专业 / 没验证 / 没大项目经验”。

这意味着“多年行业经验”不能直接作为 frontier mentor quality 的代理。后续 Role-Origin Dataset 除岗位与 ownership 外，应增加：

- `ZERO-TO-ONE RECENCY`；
- `PROTOTYPE FREQUENCY`；
- `EXTERNAL LEARNING CHANNEL`；
- `UNLEARNING EVIDENCE`；
- `EVALUATOR CAPABILITY`。

更完整的机制见：[048 — 老兵未必能教未来：能力复制陷阱与横向能力发现网络](capability-reproduction-trap-horizontal-discovery-048.md)。

这不是年龄本质论。年轻人、Jam、indie 社群也可能集体追错；大公司也可能通过内部孵化和小型自主单元产生 frontier practice。研究对象始终是**knowledge location / feedback architecture / decision rights / reality arbitration**，而不是出生年份或职位声望。


---

## 15. 2026-10-08 新增：同一开发者转制度的观察，与“有作者权仍失败”的反证

本批只补具体决策行为，不新增“中国人普遍怎样”的结论。与 [中国033 技术代理与体验需求](../../country-studies/china/033-technology-proxies-experience-demand-and-commercial-feedback.md) 互参。**不是抽样队列，不推发生率；不把后来的市场结果当当初决策必然正确的证据。**

### 15.1 鱼尾 /《卡片魔王：只剩个头！》：全闭环 ownership 与识别意外 affordance

- **P1，2026-06-30 游戏葡萄访谈**：鱼尾自述四川大学计算机出身、早期美术积累、曾在小型手游公司跨战斗/数值/文案/关卡/发行/买量岗位；早期参与《幸运猎人》的设计与美术，不能把独立制作的全部技能记为“离职后突然获得”。
- 2025年3月先用复用素材做出**约一天**的初始战斗演示后离职；这不是“所有完整Demo只需一天”。2025年5月推出玩家可测试Demo；6月由玩家发现同步回合制行动与动画结算时差带来的额外闪避行为；主创判断该异常值得保留，扩成闪避/弹反，约7月完成核心玩法。**设计发现与工程实现共演化**，不是“技术不重要”。
- 当事人明确对比：小团队手游阶段，删除已交给其他岗位实现的功能有显著协调负担；独立后拥有即时 `FEATURE_KILL_RIGHT` 与 `FULL-CYCLE OWNERSHIP`。同时保留手游/发行/买量技能对视频传播和市场知识的**正迁移**，及数值化偏好和画面定位的**负迁移**。
- 制作规模：通过极少动画、少量图像复用制作多样Boss；同时研究《节奏地牢》《空洞骑士》《黑暗之魂》等具体机制与体验目标，不能把结果说成无外部参考的纯原发革命。
- **商业证据分层**：2026-06-02开发者在Steam公告“10万销量达成”；2026-06-30媒体报道首月销售10万、流水超过RMB700万。媒体“流水”不可直接当开发者净收入/利润。也不能据此断言所有小厂策划有相同成功率。
- P1 source: 游戏葡萄/耳朵，《单人开发首月流水700万：一天做完Demo，我就从手游公司离职了》，2026-06-30，https://www.taptap.cn/moment/821200272406610420
- P0 first-party sales announcement: Steam community, 《卡片魔王：只剩个头！》“十万销量达成 & 更新路线图”，2026-06-02，https://steamcommunity.com/app/3720420/allnews/?l=schinese

**识别限制**：本案近似 within-person regime switch 的过程观察，但离职前后时间、个人能力积累、第一款作品市场验证、受众、平台与产品类型均变化，**不是准实验**。只支持该开发者有更短反馈回路与可追踪设计改变，不证明若留在公司必然无法创造同一机制。

### 15.2 凉屋游戏李泽阳：原型自由不保证内容设计与机制诊断

- **P1，2024年8月公开演讲、2025-03-05整理发布（文字经调整删节）**：本人披露数个失败/延期原型及正式游戏，包含2D空战、叙事解谜、武侠卡牌、《荣誉打工人》《异形指令》。这些**不是完整失败项目名单**，不能据此统计整个工作室失败率。
- 2D空战：基础操控形态成立，但缺乏便宜构造关卡变化的方法；叙事原型：短篇创意密度无法自动延展到完整游戏；武侠卡牌：反复重构基础机制，却未必识别真实内容瓶颈；《异形指令》：弱化RTS空间控制后出现策略维度不足，后期系统删改未恢复目标体验。
- 发言人特别区分 `MECHANIC POSSIBILITY`（基础机制的可能性）与 `CONTENT DESIGN CAPABILITY`（关卡、敌人、事件、编排能力）。某些技术/系统背景团队会把内容创作不足误诊为底层机制不优雅，于是无限重新做系统；有些美术背景负责人则偏向成本极高的视觉升级。
- 因此“设计能力”不能缩成“有机制/复杂决策树/有原型权”这一项，必须单测 `CONTENT_COMPOSITION`、`SCOPE_CONVERGENCE` 与 `BOTTLENECK_DIAGNOSIS`。
- Source: COREBLAZER整理，GameRes，《李泽阳〈凉屋游戏的凉凉经验〉》，2025-03-05（演讲2024-08），https://www.gameres.com/911199.html

### 15.3 《孤星猎人》：高作者权、高评价、仍可能没有经济正收益

- **P1，2025-04-08 制作人术纷叁访谈**：两位前大厂策划共同制作策略游戏，独立之前也试作过未上市DBG原型；自行分担程序/美术/设计，辅以小额外包和朋友投资。
- 采访时自述约6万销量，制作接近4年，按团队目前工资口径尚未完全回本；其反事实自评“如果两年做完则能盈利”不是严格成本模拟或有审计的财务报表。
- 这直接否定“有作者权＋精品口碑就一定形成可持续创作事业”。`AUTHORED DESIGN QUALITY`、`PRODUCTION ECONOMICS`、`MARKET RETURN` 三者分开评价。
- Source: 游戏陀螺，《92%好评率背后的现实：离职大厂开发4年，却连工资都没赚回？》，2025-04-08，https://www.tuoluo.cn/article/detail-10121164.html

### 15.4 “差点离开却没有离开”的观察：勿只采成功退出者

- **S1采访+当事自述，2025-12-24**：《触乐》采访从业者“严文”（应保留报道使用称谓，不反查私人身份）及Loki。严文2015起积累SRPG私人文档，曾在公司活动和业余时间试作，面对程序、沟通、时间与经济问题，未能形成持续的正式产品；他所在组织一度存在独立游戏部门，后因考核与业务调整被撤销。Loki表达业余创作愿望但因房租、收入与就业风险未离职。
- 这些不是“不会设计游戏”的证据，而是 `DESIRE → PROTOTYPE → SHIP` 之间存在真实阻断与生活成本。
- Source: 触乐/许艺丹，《“每隔两三个月，我就想离职做独游”》，2025-12-24，https://www.chuapp.com/article/291091.html

### 15.5 2026发行视角：评估者也会遇到市场预测失败

- **S1/P1被访者，2026-04-29**：《触乐》采访一名2025年开始经营独游投资发行的负责人，其团队看过**80款**候选，仅签**2款**，截至采访**两款均未收回预付款**；自述初筛偏好约1小时可玩Demo与人民币100万元以内预付款。另一位投资人分享其团队2024年接触过学生项目原型并在后续新原型形成投资意向。
- **分母限制**：80是此发行团队筛选过的候选项目、不是中国全部游戏/提案；2是签约而不是成功，0回收仅截至采访，不能外推发行商全行业命中率，也不能反推所有未签作品品质。
- 这为 `EVALUATOR CAPABILITY GAP` 增加两种可观察对象：预测误差、选中/拒绝项目的可比实际结果。**“有Demo”也不等于“有正确投资判断”。**
- Source: 触乐/许艺丹，《从大厂离职做独游，你一定能拿到投资吗？》，2026-04-29，https://www.chuapp.com/article/291336.html

### 15.6 综合裁决：将“转制度”拆成五种可分辨效果

1. `LATENT_CAPABILITY`：离开前已经形成的美术、程序、游戏阅历、原型与创作储备；
2. `DECISION-RIGHT RELEASE`：离开后获得决定试什么、改什么、删什么、何时发售的权利；
3. `ERROR-DIAGNOSIS CAPABILITY`：遇到失败时能否分清底层机制、具体内容、技术、市场问题；
4. `PRODUCTION-COST DISCIPLINE`：是否能以合理固定成本交付目标体验，而非无限复杂化；
5. `MARKET-INTERFACE ACCESS`：能否将玩家兴趣变成足够收入和下一轮生产条件。

**目前能保留：**案例证明五项能力/条件可能分离；既有手游职业训练可有正迁移和负迁移；高自主权不等于必胜。**不能保留：**单个大卖案例证明“离职导致创新”；数个内部失败项目证明“中国技术人员普遍不会内容”；选择性的采访证明国别数量级。

下一步不是再添加明星正例，而是建立一个固定时间窗的失败/继续从业者队列、并获得同公司项目绿灯的**被拒候选与后续命运**资料。参见 OQ-018。

