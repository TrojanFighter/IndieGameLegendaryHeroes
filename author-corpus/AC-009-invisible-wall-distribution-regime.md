# AC-009 — 看不见的墙：分发体制误认、市场接口选择与认知路径依赖

- Type: A0 — Author-Origin
- Author: 洪荒行者
- Status: AUTHOR THESIS TO BE TESTED
- Related: AC-003, AC-004, AC-007, AC-008, `book/INDIE-MOVEMENT.md`, `book/research-notes/pvz-hybrid-ugc-production-and-spread-001.md`

## 原始命题

作者在 2024 年《中西方互联网底层逻辑差异》材料以及后续关于中国游戏产业、独立开发、发行和平台的讨论中，长期提出一个比“国内渠道难做”更强的判断：

> **分发体制不只是决定一个产品能不能被看见；它还会长期训练开发者、投资人和玩家对“什么叫市场、什么叫营销、什么叫好产品、谁掌握成功权”的基础世界模型。**

因此，一些开发者真正撞上的并不是显性的技术墙，而是：

> **把自己长期生活的本地平台规则误认成世界规则。**

作者把这种现象概括为“**看不见的墙 / Invisible Wall**”。

这里的“墙”不等于某一条网络访问限制，也不能被简化成单一政策因素。它至少包括：

- 分发渠道结构；
- 推荐与搜索机制；
- 支付基础设施；
- 发行/渠道议价权；
- 监管与准入；
- 语言与信息获取；
- 玩家付费习惯；
- 开发者长期接受的行业知识；
- 对海外市场是否“可直接触达”的认知。

## Distribution-Regime Misrecognition / 分发体制误认

工作定义：

> **开发者把某个局部市场的分发、变现和渠道规则，当作游戏商业化的一般规律，并据此错误设计产品、组织、营销预算或发行路线。**

典型错误不是“不会投广告”，而可能是：

- 默认必须先拿国内渠道/发行资源，才有资格接触玩家；
- 默认营销等于买量、推荐位、平台关系或头部媒体；
- 把本地平台没有反馈误判为全球不存在需求；
- 把本地高分成/联运模式当成行业天然成本；
- 不理解 Steam、YouTube、TikTok、Twitch、Reddit、Discord、creator outreach 等可形成另一套市场接口；
- 英文商店页、海外 demo、全球节庆、海外 creator outreach 长期缺位，却继续在墙内重复优化同一套低反馈动作；
- 反过来，也可能把“海外自然量”浪漫化，低估全球市场同样高度拥挤、算法化和竞争激烈。

因此，本命题不是“海外一定更容易”，而是：

> **市场接口本身就是产品战略变量。开发者首先需要知道自己究竟在向哪个市场学习。**

## 历史锚点：为什么中国开发者更容易形成另一套默认世界模型

以下只是外部证据锚点，不由作者语料单独证明因果。

### 1. 长期主机禁令与 premium 产业链断层

Reuters 2014 报道中国暂停实施长达约 14 年的游戏机禁令，并指出一代玩家成长于免费 PC / mobile 为主的市场环境。

Source:
https://finance.yahoo.com/news/china-suspends-ban-sale-foreign-060329486.html

这意味着中国并非“没有游戏用户”，而是合法主机零售、premium console development 与对应消费习惯的连续性被显著削弱。

### 2. 第三方安卓渠道的高议价权是真实历史结构

2014 年公开 SEC 文件直接记录：

- 第三方应用商店在中国移动游戏分发中占据主导；
- 渠道集中提高了 channel players 的 bargaining power；
- 某些渠道费用可达到 gross billings 的 40%–70%；
- 另一份基于 Analysys 的材料给出 2013 年 publisher / developer 分配口径：publisher 侧占 gross billings 75%–85%，developer 侧 15%–25%（其中 publisher 侧还包含支付、渠道、税等成本）。

Sources:
https://www.sec.gov/Archives/edgar/data/1600527/000119312514260689/d677329df1.htm
https://www.sec.gov/Archives/edgar/data/1600527/000119312515159477/d902553d20f.htm
https://www.sec.gov/Archives/edgar/data/1600527/000119312514280606/d677329df1a.htm

这说明“渠道为王”并非纯修辞；至少在 2010s 前中期中国手游产业，渠道掌握巨大市场接入与议价能力有可审计历史基础。

但比例会随时期、平台、合同显著变化，禁止把某一年的最高值写成永恒国情。

### 3. 50/50 渠道分成并非历史遗物

Reuters 2024 关于《地下城与勇士：起源》退出部分 Android 商店的报道仍将典型合作描述为约 50% revenue split，并把事件放在开发商与手机应用商店长期分成冲突背景中。

Source:
https://www.reuters.com/technology/tencents-dungeon-fighter-game-pulled-some-android-app-stores-2024-06-20/

这说明中国渠道结构的历史惯性持续很久，但也同时说明大型内容方正在尝试绕开旧接口。

### 4. 中国现代 indie 的制度基础形成较晚

CiGA / indiePlay 的官方历史把 indiePlay 起点放在 2015 年；中国独立游戏小史则将 2013–2016 的 indienova、IndieAce、CiGA、Global Game Jam / indiePlay 等视为国内独立社区基础设施快速成形期。

Sources:
https://www.indieplay.cn/
https://www.ciga.me/indieplay
https://www.thepaper.cn/newsDetail_forward_16370628

这意味着大量中国开发者直到 2010s 才逐步获得稳定的本地 peer network、展示、比赛、全球连接与独立身份认同。

## “看不见的墙”为什么会耗尽人

如果开发者的世界模型是：

```text
产品
↓
国内发行 / 渠道
↓
推荐位 / 买量 / 平台关系
↓
本地用户
```

那么当这条路不工作时，他可能会得出：

- 自己产品不行；
- 自己没钱所以没有资格做游戏；
- 必须继续扩功能 / 提规格；
- 必须继续找更大的发行商；
- 必须继续在同一渠道买曝光；
- “独立游戏只能靠运气”。

但另一个可能存在的路径是：

```text
可读的产品 hook
↓
Steam / itch / demo / Next Fest
↓
YouTube / TikTok / Twitch / Reddit / Discord / creator network
↓
全球 niche aggregation
↓
wishlist / sales / community evidence
↓
再决定是否需要 publisher / localization / regional operation
```

后一路径也会失败，而且当代全球 Steam 同样高度拥挤。

关键区别不是“国外没有墙”，而是：

> **开发者是否意识到自己可以选择不同的市场接口，并用真实数据比较哪套接口更适合产品。**

## 与“中国好学生综合征”的区别

AC-008 研究：

> **别人出题以后很会解，但不会自己形成问题、目标和学习 agenda。**

AC-009 研究：

> **即使已经有产品和目标，也可能因为错误的市场世界模型，把产品送进一个不适合它的评价与分发系统。**

两者可以叠加：

```text
外部出题习惯
+
本地渠道世界模型
↓
把平台/发行商的规则当成标准答案
↓
在错误接口上高投入优化
↓
越努力越难看到真实需求
```

但两者必须分别取证，不能把所有中国项目失败都归因于教育或渠道。

## 与 AC-007 Benchmark Meta Convergence 的关系

AC-007 研究：

> 外部成功案例如何被压缩成 benchmark / KPI / feature list，形成版本答案。

AC-009 再增加一层：

> **谁有资格成为 benchmark，本身受分发体制影响。**

如果一个开发者长期只看到：

- 国内渠道榜单；
- 国内买量成功产品；
- 国内融资故事；
- 国内大厂招聘标准；

那么全球大量依靠：

- niche market；
- creator network；
- mod / UGC；
- Steam organic discovery；
- community-led growth；
- unconventional pricing / scope；

活下来的项目，甚至不会进入其候选答案空间。

这不是简单的信息量不足，而是**可见样本被制度筛选**。

## 《植物大战僵尸杂交版》为什么值得放进这条研究线

《杂交版》天然跨越中国与全球 PVZ 社群，因此很适合研究：

- 一个高度可视化 fan game 如何跨平台复制；
- Bilibili / 抖音 / YouTube / Reddit / TikTok / 海外 PVZ creator 之间的传播先后；
- 本地爆发与海外二次放大之间是否存在反馈环；
- 海外转载是否把作品重新带回国内推荐系统；
- 一个 creator 是否真正知道自己的流量来自哪里。

但当前公开可检索证据**不能支持“杂交版主要依赖 TikTok 先于中国互联网走红”这一强命题**。

当前可核时间线反而包括：

- 2023-11 已有“杂交植物”高播放概念视频；
- 2024-03-27 v1.0 发布；
- 2024-04 中旬 Bilibili 已出现连续实况；
- 2024-05-18 一名观察海外传播的中文 UP 主仍形容“杂交版在外国是真的不温不火”；
- 2024-05-22 TapTap 已将其写成国内爆火案例；
- 2024-05-25 Reddit 已能看到英语玩家下载、分享和求资源。

因此现阶段更稳妥的结论是：

> **中国平台先形成明显可见爆发，海外平台很快跟进并形成跨境二次传播；TikTok 在其中的真实权重仍需原始时间戳、播放量和 creator analytics 才能判断。**

这条边界本身也说明为什么研究“分发链”不能只看事后媒体叙事。

## 候选案例 / 对照

- 《植物大战僵尸杂交版》：中国 UGC → 国内爆发 → 跨境传播的时间线审计；
- CASE-032 PUBG：mod / creator network → 全球社区验证 → 商业组织放大；
- CASE-007 Gunpoint：作者已有媒体受众与公开开发如何构成 market access；
- CASE-011 Lethal Company：creator/community amplification；
- CASE-023 despelote：incubator / grant / publisher / platform 的市场接口；
- 中国 premium indie：哪些项目 domestic-first，哪些 global-first，结果如何；
- 中国手游渠道史：渠道议价与产品设计是否存在可验证联动；
- 非中国对照：韩国、日本、俄罗斯等是否也存在“本地商业模型遮蔽全球独立路径”的时期。

## 需要量化的变量

以后研究中国项目，尽量记录：

- Steam 页面建立日期；
- 首个英文商店页日期；
- demo / Next Fest 时间；
- 国内与海外 wishlist 来源占比；
- 国内 / 海外 creator 数量与地理分布；
- YouTube / TikTok / Twitch / Bilibili / 抖音的首个可见传播节点；
- publisher 接入发生在验证前还是验证后；
- 国内买量/公关预算与海外 creator outreach 成本；
- 首发销售地域；
- 本地审批/版号对 timing 的影响；
- 是否因“国内没反应”提前杀掉项目；
- 是否因“海外看不见”而根本没有尝试 global market。

## 反压力 / 禁止推论

不得写成：

- “中国互联网没有自然传播”；
- “国外算法天然公平”；
- “TikTok / Steam 会自动奖励好产品”；
- “所有中国开发者基础认知差”；
- “国内发行商和平台没有价值”；
- “只要翻译英文就能成功”；
- “中国市场没有高质量玩家”；
- “海外市场没有买量、渠道权力和信息不对称”。

更可检验的命题是：

> **一个高度依赖特定本地分发体制成长的产业，会让参与者形成相应的商业世界模型；当全球数字直销、creator network 和 niche aggregation 已经提供另一套接口时，未能更新世界模型可能成为额外的项目风险。**

## 当前状态

保留为 Author-Origin。它可以指导中国案例 intake、发行史研究和传播链审计；只有在跨项目数据证明“错误市场接口选择”具有重复性以后，才有资格升级为正式 Claim。
