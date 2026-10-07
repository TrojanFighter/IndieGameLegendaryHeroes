# Creator Life / Decision Audit 023：把案例库升级成人生条件可比系统

- Status: RESEARCH NOTE / SCHEMA MIGRATION / FIRST-WAVE BACKFILL
- Last verified: 2026-10-07
- Canonical schema: `../../schemas/creator-life-decision-audit.md`
- Coverage index: `../../metadata/creator-life-audit-coverage.json`
- Related: `china-creator-three-layer-case-matrix-021.md`, `china-creator-three-layer-missing-cells-022.md`

## 0. 为什么要做这一轮

《独立游戏英雄传说》已经能回答：

- 谁会什么；
- 项目怎么做；
- 资金从哪来；
- 市场怎么进；
- 哪些失败留下能力。

但“人生性价比指南”还缺一层：

> **同样一个方法，对什么处境的人才成立？**

例如：

- 24 岁单身程序员；
- 31 岁大厂制作人；
- 35 岁有房贷有孩子；
- 有高收入伴侣；
- 有稳定 day job；
- 有前作收入；
- 有公司工资但没有资本独立；
- 有完全 ownership 但没有 household runway。

这些人面对的是不同问题。

所以这一轮不是增加“成功规律”，而是建立：

> **Case → Life Conditions → Decision Boundary**

---

## 1. 统一字段

每个重要 Case 从现在起尽量补：

### Household
- relationship；
- children；
- dependents；
- housing；
- location cost；
- visa / relocation。

### Runway
- savings；
- salary / day job；
- spouse income；
- family transfers；
- prior-game income；
- publisher / grant / crowdfunding；
- debt / credit。

### Hidden Cost
- mortgage / rent；
- childcare；
- domestic labor；
- founder unpaid period；
- partner opportunity cost；
- medical / insurance；
- relocation。

### Exit / Recovery
- prior profession；
- reemployment；
- sabbatical；
- ability to return；
- whether failure means bankruptcy or only career delay。

### Capability / Ownership
- capability vector；
- problem ownership；
- who can kill the thesis；
- who controls commercial objective。

### Validation
- first playable；
- first stranger；
- first market signal；
- first paid signal；
- pivot / escalation。

### Reality / Market
- reality adjudication；
- capability capture risk；
- market sufficiency / legibility；
- capability scaling。

---

# 二、第一批反向回填

本轮已按统一字段回填 16 个 Case。

## A. Individual / life-comparable

### CASE-001 FTL
主要可比：
- professional dev prehistory；
- savings runway；
- résumé / return-to-job option；
- competition → Kickstarter validation ladder。

主要未知：
- household；
- 上海实际 burn；
- spouse / family support。

### CASE-004 Stardew Valley
主要可比：
- early-career CS graduate；
- part-time cinema job；
- partner stipend / income；
- four-year skill acquisition inside project。

主要未知：
- household monthly burn；
- housing；
- exact partner-income ratio。

### CASE-007 Gunpoint
目前是最完整的 day-job comparator 之一：

```text
stable salary
→ nights/weekends
→ prototype / tester
→ public devlog
→ launch threshold
→ only then full-time indie
```

适合：
- employed programmer / designer / writer；
- 不想一开始就裸辞的人。

### CASE-015 Hollow Knight
主要可比：
- prior savings；
- multiple partner incomes；
- Adelaide cost；
- Kickstarter；
- later Indie Fund。

适合研究：
> small-team project budget 为什么不能只看 crowdfunding headline。

### CASE-028 中国式网游
主要可比：
- solo core；
- 约五年业余开发；
- publisher perimeter。

但：
- household / primary income 完全未知。

因此目前只能回答：
> “part-time production structure”

不能回答：
> “普通上班族是否能复制五年”。

### CASE-029 Boundary
可比较：
- 三位 founder 离开稳定工作；
- platform / corporate support；
- long-cycle multiplayer risk；
- acquisition truth vs ecosystem truth。

但：
- household / ownership / financing 都不完整。

### CASE-038 Sultan's Game
可比较：
- mature commercial-game veterans；
- organization collapse；
- capability repricing；
- demo / wishlist before launch。

最大缺口：
- household；
- developer compensation；
- actual runway；
- publisher / legacy-investor control。

### CASE-042 The First Tree
非常适合：
- employed parent；
- strong TA / visual capability；
- salary runway；
- capability-shaped project；
- external asset / porting perimeter。

这是以后 “TA / visual-first + family” reader route 的高价值案例。

### CASE-048 The Magic Circle
非常适合：
- mature AAA veterans；
- deliberate unlearning；
- strong fit；
- market failure。

它回答：
> 就算人生条件、能力和 ownership 都不错，市场仍然可以说 no。

### CASE-054 Limit Theory
非常适合：
- high-capability student / technical founder；
- full ownership；
- crowdfunding；
- strong market interest；
- capability capture；
- six-year closure failure。

它回答：
> 自由 + 技术强 + 市场兴趣，仍不足够。

---

## B. Organization-level / 不得伪装成人生个案

### CASE-024 Escape from Duckov
可以研究：
- corporate salary runway；
- small R&D cell；
- product autonomy；
- publisher / localization / market periphery。

不能研究成：
> 五个创始人自己承担家庭风险。

### CASE-033 Zhengtu
适合：
- mature entrepreneur；
- capital / distribution / business-model capability；
- industry-regime formation。

不适合：
> 普通独立开发者辞职风险。

### CASE-039 Gunfire Reborn
可研究：
- product ownership span；
- EA；
- evidence-following escalation。

个人 life history 仍未知。

### CASE-041 NExT / SYNCED
完全属于：
> organization-level regime comparator。

household 不是当前变量。

---

## C. PENDING / 不准做人身建议

### CASE-027 Dyson Sphere Program
source recovery 不足。

### CASE-030 Outpost
当前 Case 仍是 SKELETON，虽然 research note 有额外线索，但尚未正式恢复进 Evidence Ledger / Case。

所以这两个目前不能用于：
- 是否应该辞职；
- 有多少 runway；
- 家庭支持；
- founder risk。

---

# 三、现在已经能区分的读者类型

## 1. Salaried creator / 有稳定工作

最相关：
- Gunpoint；
- The First Tree；
- 中国式网游（证据较弱）。

核心问题：

> 能不能先用工资购买 evidence，而不是先购买“独立开发者身份”？

关键变量：
- work-hour control；
- family time；
- job energy drain；
- first public artifact；
- quit threshold。

---

## 2. Early-career / 刚毕业

最相关：
- Stardew Valley；
- FTL；
- Limit Theory。

三者结果完全不同：

### Stardew
项目内学成 generalist，最终 ship。

### FTL
已有职业训练，再低承诺试验，证据后扩张。

### Limit Theory
技术极强、ownership 极高，但能力捕获 scope，最终取消。

所以：
> 年轻 + 没家庭负担

只意味着 runway 结构可能更轻。

不意味着 product judgment 自动更强。

---

## 3. Visual / TA specialist

最相关：
- The First Tree；
- Nomada / GRIS（待补 Audit）；
- Everything（待补 Audit）。

核心不是：
> 补成程序员。

而是：
> 哪种产品形态能让你的 visual / motion / technical-art capability 进入产品架构上游？

---

## 4. Big-company veteran

最相关：
- The Magic Circle；
- Sultan's Game；
- Boundary；
- Sea / 月下 research notes；
- Game Science research notes。

真正要问：

> 什么是能力资本，什么只是旧组织 objective function？

---

## 5. Married / household-risk creator

当前最好：
- Stardew；
- Hollow Knight；
- The First Tree；
- 022 中国 household cases。

但中国编号 Case 仍严重缺：
- mortgage；
- childcare；
- spouse income；
- household burn。

这仍是下一轮重要 evidence deficit。

---

## 6. Corporate small-cell creator

最相关：
- Escape from Duckov；
- Gunfire Reborn；
- NExT。

必须告诉读者：

> 小团队 ≠ 独立承担全部风险。

工资、QA、发行、localization、platform relationships、legal、marketing 都可能在公司外围。

---

# 四、第一版 Life-Risk Decision Matrix

| 处境 | 可承担的合理实验 | 最危险误判 | 首要参考 |
|---|---|---|---|
| 有稳定工资、无必须立即辞职理由 | nights/weekends 小 prototype + stranger test | 把“想独立”误写成“必须先辞职” | Gunpoint / First Tree |
| 刚毕业、技能还在形成 | 小项目购买 shipping + capability | 一上来做 lifelong dream project | FTL / Stardew / Limit Theory |
| TA / visual specialist | 让 visual capability 进入 product form | 先补齐所有程序/系统能力 | First Tree / GRIS |
| 大厂老兵 | 先做 1–2 人 evidence prototype | 把旧 process / KPI 当专业性本身 | Magic Circle / Sultan / Sea |
| 已婚、有孩、high burn | 极低 fixed-cost / 可退出 experiment | 只算公司预算、不算 household burn | 022 household cases |
| 有公司工资的小团队 | 用 corporate buffer 快速验证 | 把公司外围误当“5人就能做到” | Duckov / Gunfire |
| 拿到众筹/融资 | 用钱关闭已知 obligation | 用资金继续扩大未知问题 | FTL vs Limit Theory |
| 强技术 founder | 给 tech frontier 设置 stop condition | 能力越强，项目越被最强项吸走 | Limit Theory / Factorio待补 |

这个表不是成功率预测。

它只是：

> **当你处于某种现实条件时，哪些失败模式特别值得先防。**

---

# 五、覆盖率与下一批

机器覆盖率见：

`metadata/creator-life-audit-coverage.json`

第一批优先回填的下一组建议：

### P0 — 直接影响 reader archetypes
- CASE-003 Papers, Please；
- CASE-012 Kenshi；
- CASE-016 Early id；
- CASE-020 Into the Breach；
- CASE-035 Factorio；
- CASE-036 Manor Lords；
- CASE-043 Everything；
- CASE-049 Outer Wilds；
- CASE-050 Nomada；
- CASE-053 Kenny Sun；
- CASE-055 Factorio deep-tech counterpoint；
- CASE-056 Playdead governance。

### P1 — market / team / runway comparison
- CASE-002 Rocket League；
- CASE-006 R.E.P.O.；
- CASE-009 Project Wingman；
- CASE-014 Minecraft；
- CASE-017 Among Us；
- CASE-031 Jonas Tyroller；
- CASE-034 Landfall；
- CASE-037 Darkwood；
- CASE-040 Tripwire；
- CASE-052 House House。

### P2 — 主要作为特殊比较
其余 Case 根据章节需求逐步补，不为了填表而制造 UNKNOWN 噪音。

---

# 六、迁移规则

从现在起：

1. 新 Case 若可能进入 reader layer，默认检查 Creator Life / Decision Audit；
2. 旧 Case 只在有真实来源时回填；
3. organization-level comparator 明确标识，不伪装个人风险；
4. household UNKNOWN 本身是结果；
5. Profile 不能比 Case 更“知道”人物家庭条件；
6. 任何 reader recommendation 都必须说明：
   - 本人处境；
   - 对应历史案例；
   - 最大不可比条件；
   - 失败时的退出路径。

最终目标不是：

> “你像 Tom Francis，所以应该做 Gunpoint。”

而是：

> **“你和 Tom Francis 相同的是有稳定工资与低承诺试错期；不同的是家庭、技能、2026 市场和工具条件。因此真正能迁移的只有 staged commitment。”**
