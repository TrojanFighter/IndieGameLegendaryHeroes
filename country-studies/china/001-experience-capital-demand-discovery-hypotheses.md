# 001 — Experience Capital / Demand Discovery：作者旧文假说的研究化改写

- Status: HYPOTHESIS INTAKE / NOT A FORMAL CLAIM
- Program: 中国国情研究
- Purpose: 把作者旧文中“体验水平 / 有效需求 / 技术价值”相关判断，改写成可以被案例、跨国比较和反例检验的问题。
- Commercial boundary: 不讨论私人项目的具体游戏设计、规则、数值或产品竞争方案。

## 1. Author-origin sources

### A. 《体验水平落后——中国的有效体验创造力与相关竞争力低下之根源》

Public URL:
https://mp.weixin.qq.com/s/kkn8w4QFSxs5DxyL3V21CA

作者原始判断大致包括：

- 消费者与从业者长期接触的文化产品会影响其 reference stock；
- 能否识别“什么体验值得做”会影响有效需求发现与资源投向；
- 市场闭塞 / 文化产品接触狭窄可能让创作者的比较素材减少；
- 技术路线的商业价值最终要落到人是否能识别有意义的使用目标。

这些只能作为作者自己的 H，不是本仓库已经证实的国别结论。

### B. 《在技术饱和时代，技术是体验水平的忠仆》

Public URL:
https://mp.weixin.qq.com/s/4K0lWTMFE3WKkAAgogBLpQ

作者原始判断大致包括：

- 技术是达到产品/体验结果的手段，不等于结果本身；
- 当某类底层技术已经广泛扩散，竞争优势可能从“是否拥有技术”转移到“能否用它形成有价值产品”；
- 同样或稍弱的技术条件，也可能被更强的产品判断转化成更高市场价值。

技术史部分的 canonical 研究归入：
[cross-industry/industrial-revolutions/](../../cross-industry/industrial-revolutions/)

## 2. 为什么不用“国民体验水平”直接做变量

“体验水平高 / 低”过于总括，容易同时混入：

- 收入；
- 海外文化接触；
- 教育；
- 城市化；
- 年龄；
- 游戏史长度；
- 语言；
- 平台准入；
- 品类偏好；
- 社群结构；
- 创作者职业路径。

因此正式研究应拆成可观察变量。

## 3. 可操作化变量

### 3.1 Reference Breadth

可尝试测量：

- 玩家 / 从业者接触的游戏品类数；
- 海外作品比例；
- 不同年代作品比例；
- PC / console / mobile / UGC 跨平台经验；
- 非游戏媒介经验；
- 专业评论 / 论坛 / 社群讨论的 breadth。

不预设 breadth 越大一定越会创新。

### 3.2 Comparative Literacy

研究一个人是否能从：

> “喜欢 / 不喜欢”

进一步到：

> “我能指出具体差异、解释机制、找到同类反例。”

可用来源：
- 长期评论；
- developer blog；
- postmortem；
- interview；
- prototype history。

Tom Francis / CASE-007 是已有强锚点。

### 3.3 Demand Discovery

记录：

- 新项目最初来自 benchmark、老板 mandate、个人不满、社区需求还是 prototype signal；
- 创作者什么时候第一次明确“现有产品没满足我想要的东西”；
- 这个 unmet need 后来有没有被真实玩家验证；
- 个人需求是否错误地被外推成大市场。

### 3.4 Player → Producer Conversion

国家 / 平台层可以追：

- mod / UGC 工具可获得性；
- public publishing friction；
- creator monetization；
- artifact 是否能被招聘认可；
- 社区→职业转换案例；
- 学校 / 家庭 / 公司是否承认 side project / mod 的能力信号。

这比笼统说“某国更个人主义，所以更有创意”更容易检验。

### 3.5 Benchmark / Reference Dependence

研究：
- 立项是否必须先有成功对标；
- 缺 benchmark 时是否更难获得预算 / 权力；
- benchmark 是降低信息风险，还是把项目锁进已有 category；
- 哪些组织允许 artifact 先于 benchmark 获得资源。

这与中国商业游戏组织研究、C013 的 objective-function specialization 都有关，但当前不建立“中国行业普遍如此”的正式 Claim。

## 4. 跨国比较：不要只做 China vs USA

为了避免把所有差异归因于“东方 / 西方”，优先建立自然反压力：

### 东亚内部
- 中国大陆
- 日本
- 韩国
- 台湾地区

问题：
- 同样存在高教育压力 / 东亚家庭结构时，console / PC / mod / doujin / creator ecology 有何差异？
- 日本长期强单机作者工业是否削弱“应试教育直接导致创新弱”的粗命题？
- 韩国强在线游戏工业与中国有哪些同构、哪些不同？

### 资源/市场规模反压力
- 波兰 / 捷克
- 俄罗斯 / 乌克兰
- 芬兰 / 瑞典
- 新西兰

问题：
- 小本土市场是否反而更早强迫国际化？
- 低购买力 / 盗版是否一定削弱创作工业？
- mod / PC culture 是否能形成替代职业入口？
- grant / welfare / regional cost 与 creator ecology 怎样交互？

## 5. 第一批已有仓库锚点

### Positive / pathway anchors

- CASE-007 Gunpoint：长期评论 → comparison / unusual-idea judgment → GameMaker prototype → tester / public feedback。
- CASE-016 early id：玩家 / hacking → programming / shipping；DOOM mod ecosystem 又生产后续 creators。
- CASE-021 Roblox Creator Cluster：tool + audience + distribution + monetization 同平台的 creator pipeline。
- CASE-032 PLAYERUNKNOWN：player/server tinkering → mod artifact → community validation → commercial organization。
- CASE-040 Tripwire：mod/community playable → contest/recognition → company / commercialization。

### China pressure set

- CASE-033 Zhengtu：高回报商业函数怎样改变行业能力树；
- CASE-038 Sultan's Game：旧手游能力在 premium small-team regime 中重新组合；
- CASE-039 Gunfire Reborn：公司内部 premium / EA comparator；
- CASE-041 NExT → SYNCED：同组织跨 production regime 的 portfolio 对照；
- 008–015 China research notes：岗位、objective function、benchmark、resource escalation 等当前材料。

## 6. 需要反驳的几个作者旧文强判断

### H1
“接触更高质量 / 更多样的文化产品，会提高未来创作者发现 unmet need 的概率。”

需要：
- longitudinal creator biographies；
- cross-country exposure measures；
- negative cases：体验丰富但作品普通 / 失败；
- selection bias control。

### H2
“市场隔离会降低 creator reference breadth，从而降低部分原创能力。”

需要区分：
- 正式进口；
- 盗版；
- 网络传播；
- 留学 / 外语；
- 本地模仿；
- 地下 / 同人 / mod circulation。

政策壁垒不等于真实文化接触为零。

### H3
“技术广泛扩散后，experience / product judgment 的相对重要性上升。”

需要与工业革命区共同检验：
- 技术是否真的已经 mass-diffused；
- 是否仍存在重大 engineering bottleneck；
- product differentiation 是否从技术 possession 转向 application；
- 同技术层团队的结果方差是否扩大。

### H4
“中国游戏创新问题主要是‘体验水平落后’。”

当前应视为**过强、未操作化、不得直接采用**。

更可研究的版本是：

> 中国不同代际、平台和职业群体的 reference breadth、creator conversion、decision rights、market feedback 与 benchmark dependence，是否与若干创新产出指标存在稳定关系？

## 7. 下一步证据任务

1. 为五代玩家 × 四代从业者加入 exposure / reference variables；
2. 找中国、日本、韩国三个相似岗位的 creator biography / interview 小样本；
3. 对 Roblox / DOOM / Arma / Warcraft III 类 creator ecology 建制度矩阵；
4. 从国内 JD / 制作人访谈中编码 benchmark / prototype authority / decision rights；
5. 收集“经验极丰富但产品选择失败”的反例，防止 Experience Capital 变成成功者美化；
6. 与工业革命区联动：区分技术还没扩散 vs 技术已经扩散但产品吸收不足。

## 8. 当前最小可保留结论

现在只能安全保留：

> **文化产品消费、比较、修改和公开创作在部分开发者身上能够转换成可验证的生产能力；要解释国家或行业差异，必须研究这种转换路径是否存在、是否开放、是否能获得反馈和职业回报，而不能把“体验水平”当作一个无需测量的民族属性。**

其余继续保留为 H。
