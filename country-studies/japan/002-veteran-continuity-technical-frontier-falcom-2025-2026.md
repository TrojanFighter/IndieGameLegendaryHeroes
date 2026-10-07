# 002 — “老登游戏”到底是什么？日本的组织记忆、技术前沿与《空之轨迹 the 1st》

- Program: Japan / East Asian internal counterfactual
- Status: **CURRENT-STATE CASE / FALCOM DEEP DIVE / INDUSTRY-SURVEY CONTEXT / NOT A CLAIM THAT JAPAN IS GENERALLY OLD OR TECHNICALLY BACKWARD**
- As-of: 2026-10-08
- Related: [001 日本作为东亚内部反例](001-japan-east-asian-counterexample-weird-kinship-and-game-creator-ecology.md) / [中国014 DeepSeek组织反例](../china/014-liang-wenfeng-deepseek-positive-deviant-innovation-organization.md) / [中国012完整团队密度](../china/012-full-cycle-authoring-team-supply-proxy-china-vs-comparators.md)
- Core question: **日本为什么既能长期保存“老派游戏”的作者性和手艺，又会周期性表现出技术/流程迟滞？这种连续性对中国有什么真正可比价值？**
- Boundary: “老登游戏”只作为讨论入口，正式分析拆成组织记忆、任职年限、职业流动、技术基础设施和作者权。不能把年龄本身当创新能力代理，也不能把Falcom外推成整个日本。

## 0. 从任职年限观察组织记忆

CESA《游戏开发者的就业与职业形成2023》是自愿网络调查，不是行业人口普查，但提供了一个比印象可靠的日本商业游戏开发者截面：
- 有效回答 **658**；
- 平均年龄 **36.1岁**；
- 当前职场平均任职 **7.52年**；
- **10.3%** 在当前职场已18年以上；
- 游戏业内转职 **0次占54.1%**、1次22.3%、2次10.0%。

这组数据不支持“日本游戏开发者普遍都是老人”。它呈现的是相当强的公司/团队连续性：职业流动并没有高到把组织记忆持续冲散。自愿样本的范围仍须保留。

P0/P1 industry survey:
CESA, 《ゲーム開発者の就業とキャリア形成2023》, 2024-03:
https://www.cesa.or.jp/uploads/2024/info20240315.pdf

### Falcom是这一特征的极端案例

Falcom 2026年6月官方招聘页：
- 员工 **74人**
- 平均年龄 **39岁**
- 平均勤续 **18年**

Source:
https://www.falcom.co.jp/recruit/culture/

《轨迹》背后是一个非常小、成员长期共事的组织。本篇关注的，是这种连续性怎样承载跨代传递的隐性知识；平均年龄本身解释不了制作过程。

## 1. 《空之轨迹 the 1st》：技术底座与表现方式

Falcom社长近藤季洋2025接受AUTOMATON采访时明确说：
- 《空之轨迹 the 1st》为了Switch也能运行，技术目标并不按最高规格设计；
- 使用自研 **FDK / Falcom Developer Kit**；
- FDK基于《黎之轨迹》时期自建的图形/声音技术；
- 本作内部没有“大版本引擎升级”，主要只是做了少量shader调整；
- 玩家感受到的画面/动作大幅提升，更多来自**表现方式改变**。

同一采访还谈到团队怎样改变表现：
- 团队把20年来对原作的理解带进重制；
- 新加入的年轻开发者与资深员工结合后，镜头和动画反而比过去更细；
- 近藤这次对模型与动作下的详细指令比主线作品更少。

Source:
https://automaton-media.com/en/game-development/nihon-falcoms-in-house-game-engine-is-called-fdk-we-ask-ceo-toshihiro-kondo-about-the-technology-behind-trails-in-the-sky-1st-chapter/

技术代差与制作知识需要分别考察。本篇据这篇访谈归纳的《空轨 the 1st》制作优势包括：
- 已有RPG production grammar；
- 20年角色/世界理解；
- 长期协作形成的审美判断；
- 跨代员工能够在同一产品语言下快速调整；
- 足够小的组织让不同职种可直接互相纠错。

本篇将这些长期积累称为**组织记忆资本**。

## 2. 但同一套组织记忆也会变成 LEGACY_GRAMMAR_LOCK_IN

同一篇2025近藤采访里，Falcom自己承认了旧组织的副作用：
- 《轨迹》连续制作20多年；
- 团队疲惫；
- 越来越习惯“为已经懂《轨迹》的人制作”；
- 长期系列让团队默认有些设定“不解释玩家也会懂”；
- 因此重制《空轨》的一项明确目标，就是让团队“回到初心”，重新面对第一次接触系列的玩家。

近藤还说：
- 20年里仅《轨迹》就做了14作；
- 公司长期保持高频率出货；
- 制作方式是少人数、高密度、很多内容直到接近master仍在反复调整；
- 公司主动限制单作投入时间，不认为无限延期会自动让游戏变得数倍更好；
- 即便因此经常被批评图形规格不高，他们仍把“限定时间里最大化游戏内容”作为生产哲学。

Source:
https://automaton-media.com/articles/interviewsjp/kiseki-20250901-355966/

近藤的描述让同一套长期经验呈现出两种状态：

### ORGANIZATIONAL_MEMORY
知道哪些细节真正影响玩家体验，能在低成本下快速做对。

### LEGACY_GRAMMAR_LOCK_IN
因为长期面对同一系列/用户，默认过去的语言仍然成立，越来越难看到新玩家的问题。

## 3. 这比“日本设计迭代慢”更准确

日本在2009–2010左右确实出现过强烈的“技术/HD开发落后”自我批评：
- 稻船敬二、和田洋一等公开谈过日本游戏相对欧美的落后；
- CEDEC 2010讨论过日本开发环境、集成工具与大规模制作适应较慢；
- 当时日本开发者内部也有人指出，差距更可能来自**市场规模、雇佣形态、职务结构、预算与知识积累方向**，而不是“日本程序员天生技术差”。

Contemporaneous industry discussion:
https://www.4gamer.net/games/000/G000000/20100320001/
https://www.4gamer.net/games/105/G010549/20100831056/

因此历史上确实有：
> console/arcade-era accumulated know-how
→ HD/global AAA production regime shift
→ old capability partly devalued

但不能把2009年的诊断直接冻结到2026。

## 4. Capcom证明“日本=技术落后”已经不能作为整体判断

Capcom 2025官方资料：
- 所有当前标题都使用 **RE ENGINE**；
- 基础技术研发部门约 **200名工程师**；
- 其中约 **160名**负责引擎开发；
- 引擎组直接进入各产品团队收集需求并做定制；
- 资产和工具跨项目共享；
- 公司继续开发下一代 **REX**；
- 官方明确把统一引擎视为提升技术共享和人员流动的基础。

Source:
https://www.capcom.co.jp/ir/english/data/oar/2025/re-engine.html

因此日本当前至少存在两种完全不同的组织：

### Falcom
- 小规模
- 极高组织记忆
- 中低技术规格取舍
- 快速高密度内容生产
- 强系列延续

### Capcom
- 大规模
- 高组织记忆
- 高基础技术投资
- 自研工具链
- 全球AAA/多平台

这两者共同说明：

> **VETERAN CONTINUITY 与 TECHNICAL FRONTIER 是两个独立维度。**

“老员工多”不能直接推出“技术落后”。

## 5. Falcom甚至给出一个很清晰的“跨代传承生产线”

2026官方招聘材料里可以看到年轻员工如何被吸收：

### 2024年入职游戏设计师
- 从短对话事件开始；
- 先辈逐镜头反馈camera work；
- 熟练后逐步承担更长、更复杂事件；
- 员工明确说会反复看先辈作品学习。

Source:
https://www.falcom.co.jp/recruit/interview/03.html

### 2025年入职CG设计师
- 不只做model；
- 同时接monster、animation、effect、script；
- 用内部Wiki学习人物、地图和生产方式；
- 直接向先辈求助；
- 强调作品很快会进入游戏、被真实玩家看到。

Source:
https://www.falcom.co.jp/recruit/interview/05.html

### 2025年入职programmer
- 新项目里从debug tooling开始；
- 会参考旧产品中的类似功能，但重新理解其设计意图后从头实现。

Source:
https://www.falcom.co.jp/recruit/interview/02.html

这些招聘自述呈现出一条接入路径：新人先承担可完成的任务，借助先辈反馈与内部档案学习，再逐步扩大负责范围，并从作品出货中获得反馈。这样的师徒训练和工具支持，可以帮助新人接入一个存在几十年的产品语言；材料本身仍是公司的招聘叙事。

## 6. 这就是日本“老派游戏”难以仿制的一部分原因

如果只看成品，《轨迹》类型产品可能显得：
- 引擎不前沿；
- 系统没有技术奇观；
- 画面规格不高；
- 很多设计语法传统；
- 新作甚至在继承20年前的世界。

于是外部年轻团队容易产生错觉：

> “这些东西我技术上都能做，所以应该很好复制。”

但真正要复制的是：
- 长期系列 pacing；
- NPC与世界状态更新的生产惯例；
- 叙事/事件演出手艺；
- 数十作累积的scope intuition；
- 什么地方该省、什么地方不能省的 tacit judgment；
- 熟悉这种RPG的跨职种团队；
- 一年左右把产品收束到ship的纪律；
- 已经存在的稳定受众反馈。

这些资产多数不会显示在“技术feature list”上。

所以可以提出：

### MEMORY-INTENSIVE GAME
> 技术门槛不一定高，但成功高度依赖长期生产记忆、品类判断、内容pipeline与团队默契的游戏。

这种游戏并不比技术密集型产品“容易”。

## 7. 对中国研究最重要的反压力：快迭代可能同时意味着“没有形成传统”

目前我们**没有同口径中国开发者任职/转职普查**，所以不能直接写：
> 中国团队更年轻、流动更快，因此做不出Falcom。

中国2026游戏劳动田野样本确实以年轻从业者为主，但不是代表性人口统计。

因此只保留一个待证假说：

### H-JP-CN-01
如果中国商业游戏工业经历：
- 快速扩张；
- 高频换项目；
- 公司/工作室重组；
- 更强的市场版本迁移；
- 创作者决策权不稳定；

则它可能同时获得：
- 更快的新技术/新商业模式吸收；
但损失：
- 长周期组织记忆；
- 品类内部师徒传承；
- 核心团队连续；
- “我们已经一起做过十年这种东西”的 tacit capital。

这可以解释一个看似矛盾的现象：

> **中国可能更快学到新工具，却更难复制某些“技术不高但只有老团队知道怎么做”的产品。**

这必须用中国公司任职年限、团队解散率、项目连续性和作者团队生存数据验证。

## 8. 日本“制度化怪人”理论因此要增加一个维度：传统本身也是基础设施

[001](001-japan-east-asian-counterexample-weird-kinship-and-game-creator-ecology.md)提出 BOUNDED_ECCENTRICITY：
日本社会总体从众，却通过漫画家、director、同人circle、匠人等合法角色容纳强作者性。

Falcom案例增加了第二层：

### INSTITUTIONALIZED_LINEAGE
> 不只是允许怪人出现，还让一个创作语法、团队和品牌活得足够久，使下一代可以直接继承几十年已经形成的 tacit knowledge。

这和美国式高职业流动、独立创业并不是同一条作者生产路线。

## 9. 但这条路线的代价也很清楚

长期组织记忆会带来：
- 高语境；
- 老用户偏见；
- legacy technical debt；
- 对旧产品语法过度忠诚；
- 新人可能只能优化传统而难以重定义问题；
- senior authority可能限制新路线；
- 对外部前沿技术吸收速度下降。

本篇要追问的是：组织怎样保留长期记忆，同时避免把新人和新用户锁在旧语法里？这里将问题记为 **MEMORY WITHOUT LOCK-IN**。

Falcom《空轨 the 1st》本身就是一个很好的阶段性正例：
- 老团队提供20年记忆；
- 年轻人提供新的camera / animation sensibility；
- 领导减少微观指令；
- 用重制这种低世界观风险项目强迫团队重新面对新用户；
- 技术底座基本不变，却重新组合出明显更现代的表现。

### INTERGENERATIONAL_RECOMBINATION
本篇将这种组合称为跨代重组：资深员工提供长期品类资本，年轻人获得真实修改权，作品因此有机会超出对上一代答案的复刻。

## 9.5 任天堂说明：高组织记忆并不必然导致legacy lock-in

[003](003-nintendo-pocketpair-two-alien-routes-originality-vs-recombination.md)提供一个重要反例。任天堂2026平均勤续14.6年，同样是长期雇佣型组织；但官方长期记录了年轻开发者获得新IP责任、程序员prototype竞争和高层主动委托authority。因而Falcom式 MEMORY 与 Nintendo式 MEMORY+RENEWAL 必须分开编码。

换言之，真正目标不是降低资深员工比例，而是测：**长期记忆是否同时伴随新人problem ownership。**

## 10. 以后日本线要正式用四维矩阵，而不是“先进/落后”

每个公司/项目编码：

1. **TECHNICAL_FRONTIER**
   - engine / tooling / rendering / networking / production scale

2. **ORGANIZATIONAL_MEMORY**
   - tenure / core-team continuity / series experience / reusable pipeline

3. **AUTHORIAL_RENEWAL**
   - 新人是否能改问题、带项目，而非只执行旧语法

4. **LEGACY_LOCK_IN**
   - 是否因旧用户/旧工具/旧组织而难以进入新市场或新设计

第一版：
- Falcom：TECH中 / MEMORY极高 / RENEWAL部分可见 / LOCK-IN高且正在主动修正
- Capcom：TECH高 / MEMORY高 / RENEWAL待细查 / LOCK-IN较低但并非零
- 日本大型保守公司：不能先填，逐案核实

## 11. 对当前中国比较最有价值的问题

下一轮应直接找中国对应物：

- 有没有平均任职10–20年的游戏核心团队？
- 中国有多少“一个品类连续做十年以上”的作者小组，而不仅是同一家公司/IP？
- 大厂员工换项目但不换公司时，**team memory** 是否仍然被切断？
- 新人是通过师徒/内部作品档案继承品类手艺，还是主要通过外部benchmark学习？
- 中国哪类游戏已经形成了自己的“老登传统”？
  - MMO？
  - 数值卡牌？
  - 二游？
  - SLG？
- 为什么这些领域中国能长期积累，而premium单机团队反而稀薄？

这个问题能把“渠道为王”研究推进一步：
**商业制度不只是选择产品，也选择哪些传统能够活到下一代。**

## 12. Verdict

日本部分游戏公司长期保留了稳定的人员、品类语言与生产记忆，能够持续生产技术规格并不激进、却高度依赖隐性手艺和作者传统的作品。同一结构也会制造高语境与技术/设计锁定，不能用“日本技术差，所以只能做老东西”概括。

《空之轨迹 the 1st》展示了本篇推崇的一种更新方式：让年轻人获得修改表达的实际空间，与老团队积累的记忆共同工作。保留资深员工与改变制作方式可以同时发生。这个局部案例尚不能替整个日本行业回答跨代更新的问题。
