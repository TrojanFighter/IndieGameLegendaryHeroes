# Steam 第二次发行生存基线 037：先解决右删失，再比较中国的 Second-Attempt Capacity

- Status: **PLATFORM-LEVEL BASELINE / NON-COUNTRY / RIGHT-CENSORING AUDIT / PRE-COMPARISON**
- As-of: 2026-10-07
- Related: [中国012完整团队供给代理](../../country-studies/china/012-full-cycle-authoring-team-supply-proxy-china-vs-comparators.md) / [中国011失败后二次尝试](../../country-studies/china/011-boundary-wandering-earth-capability-second-chance-2024-2026.md) / [媒体与分母协议028](media-selection-survivorship-and-denominator-protocol-028.md)
- Question: **一个开发者第一次在Steam发售以后，多少会在固定时间窗口内再次发行？“多做几款更容易成功”到底是经验复利还是幸存者选择？**
- Boundary: Steam开发者名称不是自然人/公司法人唯一ID；同名/改名/发行商账号/移植与下架会污染职业轨迹。这里建立的是平台级观测基线，不是开发者人生的完整退出率。

## 0. 结论：常见“只有1/5会做第二款”是原始截面，不是生命周期发生率

2024/2025 Game Oracle 对Steam目录做过过滤后分析：
- 排除其定义中的大厂、2017年前首发者及超高频发行者后，使用 **56,007个indie developer identifiers**；
- raw观察里，非首作即大成功者中约 **1/5** 后续再次发行；
- 2026更新的62,000+开发者生存曲线称，首次发行之后长期约**60%最终未在Steam观察到第二款**，而已经做过两三款者后续不再发行的概率更低；
- 作者明确承认“没有后续Steam作品”可能包括转到其他平台，而非真正离开游戏开发。

这组结果适合作为**初步全平台形状**，不应直接写成“80%独立开发者失败/退出”。主要问题是 **right censoring（右删失）**：最近首发者尚未来得及做下一款，却会在简单目录快照里被算作“没有第二款”。

Sources:
- Game Oracle, *How Many Games Does it Take to Find Success on Steam?*, 2024-11-13 / update 2025-05-13: https://www.game-oracle.com/blog/how-many-games
- Game Oracle, *What if the key to success is survival?*, 2026-06-24: https://www.game-oracle.com/blog/indie-dev-survival

## 1. 独立复核：21.7% raw可以复制，但固定观察龄以后大幅上升

2026年一个独立分析者对其维护的Steam全目录快照进行复核：
- 总目录约 **115,281 games / 48,049 developer names**；
- paid games约 **97,271**；
- 直接目录计数：**21.7%** 的开发者名称出现第二款发行；
- 但按首次发行距今时长限制：
  - 首发已至少3年：约 **27%** 后来有第二款；
  - 至少5年：约 **31%**；
  - 至少8年：约 **38%**；
  - 至少10年：约 **47%**。
- 用固定**3年观察窗**比较不同年代首发者，约 **80%** 在三年内没有第二款，即**约20%** 三年内再次发行。
- 对首发已8年以上人群看“最终是否再发”，首次→第二款“未再次发行”的累计比例约 **64%**，即约36%出现后续；与上面8年lookback约38%的量级一致。

该分析的核心价值不是把某个百分比当真理，而是证明：
**不同观察窗口会把同一平台行为讲成完全不同的故事。**

Source: a327ex / Claude Fable 5, *What predicts indie success, tested against all of Steam*, 2026, https://a327ex.com/posts/what-predicts-indie-success

### 1.1 两个数据源为什么不完全一致

| Dimension | Game Oracle | independent reanalysis |
|---|---|---|
| developer scope | 过滤大厂/老Steam/高频者后的indie identifiers | 全Steam开发者名称职业序列，再按年代/自发行切片 |
| raw second release | 约20% | 21.7% |
| long-run first→second | survival curve约40%会再发 | 8y约38%、10y约47% |
| censoring treatment | 2026用生存曲线 | 明确3/5/8/10年lookback和固定3年窗 |
| missing delisted games | 未完全消除 | 明确live catalog漏下架 |
| identity problem | developer name identifier | developer name identifier |

因此以后任何国别比较必须预注册：
`FIRST_RELEASE_COHORT_YEAR`
`FOLLOWUP_WINDOW_YEARS`
`DELISTED_POLICY`
`DEVELOPER_ID_RECONCILIATION`
`PLATFORM_EXIT_POLICY`。

不能把一个2024首发团队与2018首发团队放在2026同一天看“有没有第二款”。

## 2. 更重要的纠偏：多发行并不自动提高下一款成功率

Game Oracle 2024文章观察到：
- 首作达到1000评测的“unicorn”约3.3%（其过滤定义下）；
- 其多作幸存样本中，越到后面的game index，达到高评测阈值的比例看起来越高；
- 因而文章将其解释为坚持、迭代、经验复利。

独立复核提出关键反驳：
- 现代Steam时代（2015+）首作达到其约25k销量代理阈值（556 reviews）的比例约 **8.8%**，现代self-published首作更接近 **6%**；
- 按“第几款游戏”直接比较，game 3附近达到约11.8%后反而下降，game 10约5.8%；
- 真正强预测变量是**此前最好作品的市场牵引**：从没有超过10 reviews到此前超过5000 reviews，下款达到hit阈值的观察概率逐级提高；
- 在相同历史表现层内，“只是多发了几款”并没有呈现稳定的成功概率递增；
- 因此“第五款比第一款成功概率高五倍”主要混入了**失败者退出、成功者继续发行的 survivor selection**。

这不意味着经验没有价值。它意味着更准确的可检验命题是：

> **经验、代码、团队默契可能复利，但能真正显著改变下一次融资/发现/购买概率的，是可观察到的市场牵引、产品判断与信誉资产；单纯把失败作品数量加一，不会机械产生成功。**

这对中国“Second-Attempt Capacity”尤其关键：我们要测的不是“做第二款的人多不多” alone，而是**什么资源让第一次失败的人仍有能力做下一次真正不同且更有市场信息的尝试**。

## 3. 对中国012的直接方法修正：不要先比较“曾经发过两款的比例”

错误的跨国做法：
```
截至2026：
中国开发者A有2款
波兰开发者B有1款
=> 中国第二次尝试能力更强
```

可能只是：
- A 2018首发，B 2025首发；
- B第二款还在制作；
- A两款相隔8年；
- B改名/联合工作室导致developer identifier变化；
- A的第二款只是移植/DLC/资产复用；
- B转Epic/console/itch并未退出；
- 商业发行商将开发者名展示不同。

### 3.1 最低合格的固定窗设计

优先选**首次商业发行发生在2018–2020**的团队：
- 截至2026都有至少6年观察窗口；
- Steam Direct制度已基本稳定；
- COVID与2020–21市场异常仍需年份固定效应；
- 可观测2019–2026二次发行/失败/改组。

每国先固定一个**首发队列**，然后对所有人统一看：
- `SECOND_RELEASE_WITHIN_3Y`
- `SECOND_RELEASE_WITHIN_5Y`
- `ANY_SECOND_RELEASE_BY_2026`
- `SECOND_DISTINCT_IP`
- `SAME_CORE_TEAM_VERIFIED`
- `ANNOUNCED_NOT_SHIPPED`
- `STUDIO_CLOSED`
- `RETURNED_TO_EMPLOYMENT`
- `PLATFORM_SWITCH`
- `DEVELOPER_NAME_CHANGED`
- `UNKNOWN`

**核心团队**必须由官网/credits/采访核，不用Steam developer字符串当最终身份。

### 3.2 两种不同的“继续”

`PLATFORM_CONTINUATION`：
同一developer identifier在Steam又发了一款。

`AUTHORIAL_CONTINUATION`：
原核心人保留problem ownership，继续启动另一款自主产品；可以换公司、换publisher、换平台。

中国真正需要与波兰/韩国/北欧比较的是第二种。Steam只负责做成本较低的**第一层筛选**。

## 4. 还有一个必须防止的新幸存者偏差：重复发行者不是随机留下来的

平台数据已经显示：
- 首作市场牵引高的人更可能继续；
- 后续高表现者本身也更容易获得资金、publisher、用户社区；
- 因此只研究做了第二、三、五款的人，会越来越像**赢家后代样本**。

这和本项目此前研究明星开发者的偏差结构完全同构。

所以 country cohort 不应该：
- 从“2026仍活跃的中国工作室”抽样；
- 从“做过至少两款”抽样；
- 从“Steam愿望单高”抽样；
- 从媒体知名度抽样。

必须从 **FIRST RELEASE AT T0** 建 cohort，然后追所有后果，包括没有第二款的人。

## 5. 中国真正需要测的是“失败后的再入场基础设施”

结合[011《边境》](../../country-studies/china/011-boundary-wandering-earth-capability-second-chance-2024-2026.md)：
- 柳叶刀第一款的完整制作能力后来成为新IP合同资格；
- 中间靠外包/小项目维持公司；
- 新项目还需要融资和IP方；
- 这是一种 `FAILURE -> CAPABILITY SIGNAL -> CONTRACT REENTRY`。

对照Steam全平台：
- 三年内没有第二款其实是**大多数开发者的正常平台状态**；
- 所以中国即使低，也不能只说“老中不坚持”；
- 要问为什么：现金烧完？回就业？核心人散了？publisher不再投？原型版权不能带？第二项目在别的平台？还是主动不想再创业？

真正有政策/产业解释力的指标应是：

```
SECOND_ATTEMPT_CAPACITY =
  P(meaningful second attempt within 5y | first commercial release)
  stratified by
  first-project traction,
  team size,
  funding model,
  country,
  product regime,
  and whether the core team retained authorial rights.
```

不能只看 `P(second Steam app)`。

## 6. 全球平台基线对012“老中不行”命题的实际影响

它**没有削弱**012观察到的中国Top200愿望单管线偏薄，反而帮我们避免错误解释：

- 如果全球首发者本来就有大约60–70%在5–8年观察中没有第二款，那么**第二次尝试是普遍困难**，并非中国独有。
- 中国的结构性问题若存在，应表现为在控制首作年份/市场牵引/团队规模以后：
  1. **中国首次形成完整team的数量较少**；
  2. 或同样首发之后，**核心团队5年继续率更低**；
  3. 或第二次尝试更多回到大厂执行/承制而不是保留product ownership；
  4. 或失败后的资本、publisher、政府资助、IP采购等再入场渠道更窄。
- 如果中国同类首发团队的5年再尝试率其实与波兰/韩国相近，那么“人才→团队转化率低”的问题应主要落在**第一次完整团队形成之前**，而不是失败后的恢复能力。

这是一个非常重要的可证伪分叉，不预设结论。

## 7. Data status

### Relatively robust for descriptive baseline
- raw second-release rate ~20–22% across independent snapshots；
- fixed-age cohorts substantially higher than raw snapshots；
- 3-year follow-up约20%、5-year lookback约31%、8-year约38%、10-year约47%这种**随观察窗增长**的方向稳定；
- repeated-release groups高度选择性，不能把其后续表现当首次创作者的反事实。

### Weak / needs direct dataset
- country-specific second-release rates；
- team/person continuity inside developer account；
- console/itch/Epic follow-up；
- dissolved studios and return-to-employment；
- funding/publisher treatment effects；
- China/Poland/Korea/Finland matching.

## 8. Next reproducible step

如果能合法取得当前VGI/Sensor Tower Developer Database等带 **HQ country + released games + unreleased games** 的可导出开发者表，第一阶段只做：
1. country；
2. earliest Steam release date；
3. number of released titles；
4. coming soon；
5. classification / in-house flag；
6. first-game review traction。

再人工核**固定小样本**的团队身份与作品类型，避免把developer账号等于真实团队。

VGI当前公开数据库页面（2026-09快照）显示其索引 **13万+ developer records**，字段包括 Released games、Unreleased games、HQ country、classification、in-house比例和收入估计，是一个潜在抽样框；**本轮没有取得国家过滤后的可导出结果，因此不自行构造中国/波兰二次发行率。**

Source: Sensor Tower / Video Game Insights developers database, https://app.sensortower.com/vgi/developers-database

**Verdict：**
平台层已经说明“第二款游戏”本身是稀缺结果，但简单21.7%是截面偏低；公平的国别比较必须固定首次发售年份与观察窗。更关键的是：**作品数量不是能力复利的充分指标，上一款已经取得的市场牵引和下一次仍拥有的团队/资金/作者权，才是 Second-Attempt Capacity 的核心资产。**
