# 011 — 台湾成人独游的钱如何流动：平台抽成、发行组合估值与合同黑箱

- Status: REVENUE-WATERFALL AUDIT / CONTRACT-OPAQUE / PRE-CLAIM
- Program: C Taiwan comparator
- As of: 2026-10-08
- Scope: Steam / DLsite成人独游从消费者支付到开发者可支配现金之间的层层扣减；专业发行商的portfolio economics；公开合同缺失
- Predecessors:
  - [008 — 成人独游市场长尾与发行基础设施](008-adult-indie-market-long-tail-publisher-infrastructure.md)
  - [009 — 2025可见发行队列与作者存活](009-adult-indie-2025-visible-cohort-author-persistence.md)
  - [010 — 工资制 vs 作者押注](010-adult-indie-creator-economics-wage-vs-author-risk.md)
- Restriction:
  - VGI/SensorTower等模型估算不是财报；
  - publisher gross不是developer net；
  - Steam/DLsite平台条款不能替代发行商合同；
  - 不假设所有作品使用相同publisher split、advance、recoup或IP条款。

## 0. 为什么“销量×价格”不是创作者收入

公开媒体常见叙事：

100,000 copies
× US$10
= US$1m

然后直接把“百万美元游戏”理解成：
开发者拿到接近百万美元。

这是错误的。

一个成人独游的现金流至少可能经过：

consumer gross
→ VAT / sales tax / refunds / regional pricing
→ storefront platform share
→ publisher recoup / revenue share
→ localization / voice / QA / marketing / porting cost allocation
→ contractors / core-team splits
→ company / personal tax
→ developer disposable cash.

所以真正需要研究的是 **REVENUE WATERFALL**。

---

# 1. Steam：绝大多数小成人游戏仍处30%平台抽成档

Steam公开财务文档说明，支付给合作伙伴的金额基于net revenue再乘约定revenue share，具体以Steam Distribution Agreement为准。

Official:
https://partner.steamgames.com/doc/finance/taxfaq

Valve 2018以后公开的阶梯结构为：
- 单款累计收入前US$10m：Steam 30%；
- US$10m—50m以上部分：25%；
- US$50m以上部分：20%。

Public record / Valve announcement reference:
https://techcrunch.com/2018/12/03/valve-changes-revenue-sharing-tiers-on-steam/
https://steamcommunity.com/groups/steamworks/announcements/detail/1697191267930157838

对本研究中的台湾R18小团队，几乎所有公开可见项目都远低于US$10m阈值，因此可以把“约30% storefront share”当作大多数项目的合理平台层级假设。

但：
- 仍需扣VAT/销售税、退款等才能到net revenue；
- Steam keys、bundles、不同地区价格会改变实际实现价格；
- 不能简单用标价×销量×0.7当开发者收入。

---

# 2. DLsite：公开批发价表显示创作者侧也不是接近100%售价

DLsite台湾版公开“作品登录销售服务条款”：
https://www.dlsite.com.tw/circle_regulations

台湾版示例：
- 售价NT$500 → 社团批发价NT$300；
- NT$400 → NT$220；
- NT$300 → NT$150；
- NT$200 → NT$100；
- 售价NT$500以上，批发价为售价60%。

DLsite台湾社团指南也明确说：
- 500元以上时，社团收入为售价60%。

https://www.dlsite.com.tw/guide/circle/

日本DLsite公开表也显示不同价格点的批发价比例不同，并非固定“平台只抽一小部分”。

因此成人创作者即使绕开Steam，数字商店层仍可能吃掉售价的显著比例。

### 产业含义

多平台发行的价值不是“零平台费”，而是：
- 多市场；
- 不同成人内容政策；
- 不同发现机制；
- 风险分散；
- 不同价格与用户群。

---

# 3. 专业发行商条款是目前最大的公开黑箱

本轮针对：
- Mango Party；
- PlayMeow；
- LewdLoco

搜索了：
- revenue split；
- advance；
- minimum guarantee；
- recoup；
- IP ownership；
- sequel option；
- exclusivity；
- localization / voice cost allocation。

没有找到公开标准term sheet。

### LewdLoco公开的是“服务”，不是经济条款

官方网站：
https://www.lewdloco.com/
https://www.lewdloco.com/%E5%90%88%E4%BD%9C%E6%9F%A5%E8%A9%A2

公开承诺：
- 开发到销售的技术支持；
- 翻译/配音；
- 测试/优化；
- Steam/DLsite上架；
- 数据监测；
- 精准流量；
- 活动促销；
- 媒体/Vtuber；
- 团队配对。

合作方式是：
developer提交Demo / proposal / portfolio
→ internal review
→ publisher contact.

没有公开：
- 预付款；
- 分成百分比；
- 回收顺序；
- 谁拥有Steam app；
- IP归属；
- 续作优先权。

### PlayMeow公开同样是business contact

Steam：
https://store.steampowered.com/publisher/playmeow/about/

明确公开商务合作联络，但不公开合同模板。

### Mango Party

公开公司/发行资料强调：
- publishing；
- marketing；
- localization；
- investment；
- product consulting；
- technical support；
- porting。

但同样未发现标准合同。

### 新变量：CONTRACT OPACITY

专业发行商已经成为行业关键基础设施，但开发者在签约前外部很难比较真实“资本价格”。

这可能造成：
- 信息不对称；
- 新作者议价能力弱；
- 熟悉行业的serial developers更容易判断条款；
- 爆款后的第二作作者可能拥有显著更高谈判权。

Status: STRUCTURAL HYPOTHESIS.

---

# 4. 第三方portfolio估算显示：成人发行商之间本身也有巨大质量差

Video Game Insights / SensorTower模型当前估算：

## Mango Party

https://app.sensortower.com/vgi/publisher/47475/mango-party

模型：
- 96已发行；
- lifetime gross estimate ~US$26.2m；
- average ~US$275k/game；
- median ~US$115k/game。

Mango Party News另一个Steam publisher label：
https://app.sensortower.com/vgi/publisher/6553150/mango-party-news

模型：
- 92 titles；
- lifetime ~US$21.7m；
- median ~US$106k。

这两个label有大量重叠，绝对不能相加。

## LewdLoco

https://app.sensortower.com/vgi/publisher/4088265/lewdloco

模型：
- 30已发行；
- lifetime ~US$4.1m；
- average ~US$137k；
- median ~US$80k。

## 更小成人发行标签

Lewd Formosa：
https://app.sensortower.com/vgi/publisher/33043/lewd-formosa
- 9 games；
- estimated lifetime ~US$948k；
- median ~US$15.7k。

Dark Light Studio：
https://app.sensortower.com/vgi/publisher/4236/dark-light-studio
- 10 games；
- lifetime ~US$58k；
- median ~US$1.8k。

### 如何读这些数

这些模型可以帮助判断：
**发行组合之间可能存在一个甚至两个数量级的商业质量差。**

不能用来：
- 当公司财报；
- 推开发者净收入；
- 做精确市场规模；
- 比较同名publisher label而不去重；
- 推台湾总市场。

但它们对“不是所有成人发行商都一样赚钱”这一点非常有用。

---

# 5. 发行商为什么值得分成：它们购买的是“共享能力”

008/009/010已看到：
- 小团队经常没有程序、营销、本地化、QA、配音能力；
- 发行商有Steam follower池；
- 可做日/英/韩/简繁中本地化；
- 组织配音；
- 管理商店页；
- 参加G-EIGHT；
- 投放媒体/Vtuber；
- 做促销；
- 提供技术/测试；
- 甚至提供资金或人才。

这使publisher cut的经济逻辑可能是：

developer gives up part of upside
→ obtains market access + specialized labor + portfolio audience + execution bandwidth
→ increases probability / scale of launch.

真正需要判断的不是：
“发行商拿几成是不是黑？”

而是：
> **每让渡1%的revenue，究竟购买了多少additional sales、开发时间、风险转移和专业服务？**

没有合同与counterfactual，当前无法回答。

---

# 6. 一个非常重要的“gross → author”示意

假设某游戏在Steam产生US$100k consumer gross。

这不是收入预测，只做结构示意：

US$100k consumer gross
→ taxes/refunds/regional realization
→ Steam share（大多数小作约30%平台层）
→ remaining partner pool
→ publisher recoup / split UNKNOWN
→ external production cost UNKNOWN
→ developer/company tax
→ creator take-home.

因此：
> VGI估算某publisher median gross US$80k或115k，不意味着普通开发者可以拿US$56k或80k。

发行合同很可能比平台费更决定作者最终收入。

---

# 7. 与工资制轨道结合后，作者的真正决策问题变成“所有权期权值”

010显示：
- PlayMeow内容企划/写手当前公开NT$30k–40k/月；
- 侍达成人剧本企划NT$29.5k–50k/月；
- 低端非常接近台湾法定最低工资。

于是同一个有写作/美术能力的人可以选择：

### Employee
每月获得可预测工资
→ 公司承担项目失败风险
→ 自己不一定拥有IP/长期分成。

### Author
前1—3年可能低收入/靠接案
→ 承担项目失败风险
→ 如果作品成功，保留某种IP/分成上行空间（具体取决于publisher contract）。

这就是一个非常典型的：
**salary certainty vs ownership option**。

台湾R18生态真正吸引人的地方可能不是平均工资，而是：
> 对原本只能接案/拿工资的美术与作者开放了“拥有一款全球销售数字产品”的期权。

---

# 8. 2026最重要的行业黑箱已经不是“有没有市场”，而是“谁捕获价值”

市场存在已经很清楚：
- 100+产品publisher；
- 数千CCU头部；
- serial authors；
- 全球多语言；
- 专门展区；
- 多家发行商。

下一步更值得研究：

## VALUE CAPTURE
消费者付的100元最终：
- Steam/DLsite拿多少；
- publisher拿多少；
- 开发工作室拿多少；
- 主创拿多少；
- 外包人员拿多少；
- 税拿多少。

## BARGAINING POWER
哪些作者能获得：
- advance；
- MG；
- 更高split；
- IP保留；
- sequel control；
- publisher bidding。

## FAILURE FINANCE
一个peak 30、50、100的游戏：
- 是否已经回本；
- 是否靠publisher portfolio补贴；
- 作者为什么还做下一款；
- 是否靠本职工作/接案/FANBOX维持。

只有回答这些，才能知道：
> 台湾成人indie是“作者经济”，还是“发行商掌握价值捕获、作者提供低成本供给”的平台型产业。

当前证据不足以偏向任何一边。

---

# 9. 下一轮取证优先级

1. 找开发者公开复盘中的publisher split / advance / recoup。
2. 找招聘/离职者访谈，核员工是否有项目奖金或分红。
3. 找台湾成人开发社群匿名调查，询问：
   - 开发月数；
   - 核心人数；
   - 总成本；
   - gross；
   - publisher take；
   - creator take-home。
4. 用固定发行队列联系/追踪低尾作者，而不是只问爆款作者。
5. 对Steam与DLsite同一作品比较：
   - 定价；
   - review；
   - 排名；
   - 版本；
   - 是否能推断渠道组合。
6. 不拿VGI gross估算直接做“作者收入排行榜”。

## 当前结论

> 台湾成人独游已经证明“市场存在”；下一阶段真正决定它是不是健康创作者生态的，是价值分配，而不是总销量。

这应该成为008—011之后的研究主轴。
