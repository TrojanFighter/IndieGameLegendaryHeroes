# Editorial Audit 001 — first five reader profiles

审计对象：

- `book/profiles/kenshi.md`
- `book/profiles/rocket-league.md`
- `book/profiles/bills-must-be-paid.md`
- `book/profiles/gunpoint.md`
- `book/profiles/ftl.md`

目的不是改案例事实，而是识别 **reader layer 已经重复出现、值得流程化处理的问题**。

## 1. 重复开头结构：Myth → debunk → thesis

五篇都不同程度依赖：

1. 先说独立游戏圈怎样讲这个传奇；
2. 承认其中一部分是真的；
3. 再宣布“真正值得研究的是……”；
4. 进入生产史解释。

单篇有效，但连续读会出现明显模板感。

### 处理

不禁止 Myth 入口，但新 profile 默认优先尝试：

- 具体决策时刻；
- 一项令人意外的现实约束；
- 失败节点；
- 当时真实数字；
- 行动与结果之间的反差。

至少连续两篇不要使用同一种开头。

## 2. Research voice 渗入 reader voice

高频出现：

- “真正值得研究 / 真正重要”；
- “当前证据支持”；
- “从生产史角度”；
- `runway / scope / capability capital / market access / production function`；
- “这不能证明……”等证据边界插入正文。

这些在 Case 中必要，但 reader layer 过密会让文章像研究 memo。

### 处理

- 核心术语第一次先翻成人话；
- 研究边界尽量集中到文末；
- 正文优先写处境、动作和直接结果；
- 不删除不确定性，只改变它出现的位置。

## 3. 人物出现得太晚，理论出现得太早

Kenshi、Rocket League、FTL 的开头尤其容易先让读者遇到“项目神话 / 生产史命题”，再遇到具体的人。

Gunpoint 因为 Tom Francis 的职业前史本身就是论点，人物感更强；Bills Must Be Paid 因为时间线和具体 wishlist / demo 节点较多，行动链更自然。

### 处理

未来 profile 尽量在前 300–500 字给出可核验的：

> 人 + 当时处境 + 关键动作 / 约束。

这不是硬字数 lint，只是人工 gate。

## 4. “不是 X，而是 Y”承担过多推进功能

样稿大量通过纠正错误解释推进：

- 不是新手，而是已有能力；
- 不是突然爆，而是多年积累；
- 不是没有营销，而是另一种 market access；
- 不是勇敢下注，而是 staged commitment。

这些判断很多是正确的，但句法重复会产生明显模型写作节奏。

### 处理

同一小节里出现第二、第三次反转句时，优先改成：

- 时间线；
- 决策—结果；
- 前后状态变化；
- 一个具体数字或外部事件。

## 5. 跨案例 synthesis 过早回灌个案

FTL 等文章结尾已经开始串联 Kenshi、Rocket League、Bills Must Be Paid、Gunpoint，帮助形成全书理论。

这对研究有价值，但如果每篇都这样，profile 会逐渐变成 thesis proof，而不是独立人物史。

### 处理

- 个案结尾优先结束个案；
- 章节导语 / thematic synthesis 再承担跨案例比较；
- Profile 内只在确有解释价值时做一两个对照。

## 6. Provenance 结构是优点，但位置可优化

五篇都清楚回链 Case / Evidence，并保留 UNKNOWN。这一点必须保留。

问题不是“研究边界太多”，而是它与叙事混排的频率。

### 处理

形成两层 provenance：

- 顶部：Case + Evidence + 极短状态；
- 文末：UNKNOWN / Evidence / Transfer boundary 集中处理。

## 7. 当前各样稿最值得保留的差异

### Kenshi

优势：runway → Early Access → team growth 的生产转折非常清楚。

风险：分析语气最强，人物日常与时代条件目前偏薄；待 CASE-012 做 CSA 后再增强，不在 editorial task 中补史料。

### Rocket League

优势：work-for-hire 作为 company-level runway，以及 SARPBC 作为 capability prototype 的链条清楚。

风险：抽象名词密度较高，容易把公司史写成商业机制论文。

### Bills Must Be Paid

优势：有大量 contemporaneous 数字和明确决策节点，时间推进最自然；“full launch → demo”的 course correction 很适合生产史写法。

风险：信息量太大，后续成书时可能需要减少“每一个营销动作都解释一次”的长度。

### Gunpoint

优势：人物最鲜明，职业前史与核心 thesis 高度绑定；“品味”能落回具体 scope deletion / rule compression。

风险：书级命题“品味决定命运”容易压过 Tom Francis 本人，也容易让 AI 时代推论占据历史个案篇幅。

### FTL

优势：`staged commitment` 的主问题最清楚，项目阶段划分整齐。

风险：结尾跨案例 synthesis 最明显；部分段落像给整个项目写方法论总结。

## 8. 本轮决定

### 升级为 Editorial Gate

- 开头结构去模板化；
- 人 / 处境优先于 theory；
- 术语先翻成人话；
- 控制 Myth-debunk 与“不是…而是…”密度；
- 跨案例 synthesis 从 profile 回收到 book-level；
- provenance 保留，但集中分层；
- 场景化禁止虚构。

### 暂不进入 lint

以下目前都属于语境判断，不做机械检查：

- “真正”出现次数；
- “不是…而是…”出现次数；
- 前 500 字是否足够人物化；
- jargon 是否过多；
- 文章是否“像论文”。

如果以后某一问题能定义成稳定、低误报的机器条件，再升级。

## 9. 下一次 audit 触发条件

满足任一即可再审：

- reader profiles 达到 8–10 篇；
- 正式形成第一版 thematic TOC；
- 出现第二次明显相同的 reader-layer 写作事故；
- 开始生成 PDF / EPUB 前。
