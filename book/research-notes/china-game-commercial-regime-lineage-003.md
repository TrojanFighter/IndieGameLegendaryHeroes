# 中国游戏商业制度谱系：从《传奇》的收钱基础设施，到《征途》、渠道为王与内容方议价回流

- Status: RESEARCH NOTE / STRUCTURAL HISTORY / LINEAGE
- Last verified: 2026-10-05
- Related: `china-game-industry-prehistory-002.md`, `china-indie-distribution-regime-001.md`, `CASE-033 《征途》 / 史玉柱`, `runestone-keeper-vs-gumballs-001.md`
- Purpose: 不再把中国游戏商业史写成“点卡 → 氪金 → 渠道 → 原神”的标签年表，而是追踪每一代**谁控制收钱、谁控制用户入口、谁承担研发风险、什么能力因此最值钱**，以及这些制度怎样反过来训练产品与人才。

## 0. 核心结论：不是一种“中国游戏模式”，而是连续几次生产函数重写

当前证据更支持六段谱系：

```text
A. premium/零售回款弱
↓
B. 盛大：在线服务 + 网吧 + 点卡，把“玩的人”变成“能收钱的人”
↓
C. 免费制扩张；《征途》把免费人口、阶级化数值、高付费者和地推整成一套社会—商业系统
↓
D. 智能手机 + 碎片化 Android 商店 + 联运发行，把“入口”本身变成高租值资产
↓
E. 《刀塔传奇》等证明：玩法差异化 + 高数值/LTV + 发行/渠道工业可以制造极高流水，行业能力树被强力筛选
↓
F. 《万国觉醒》《原神》等强内容/全球化产品减少对单一本地渠道依赖，研发方议价权回流；但渠道租并未消失
```

这条线的关键不是“哪家公司更道德”，而是：

> **收入接口会筛选能力；能力又会筛选下一代项目。**

所以中国游戏产业后来异常擅长 monetization、live ops、UA、渠道运营、数值成长和大规模在线服务，并不是“整个行业突然不会做玩法”，而是长期资本回报对这些技能进行了高强度正向选择。

---

## 1. Author-Origin：保留旧命题，但拆掉两个过强历史归因

作者既有《正在到来的中度数值通胀率游戏设计革命》提出了两条对本项目仍有价值的母题：

1. **高数值通胀商业体制**会提供远高于传统 premium / 低数值产品的付费深度，因此会改变渠道、投资人与从业者的激励；
2. **渠道为王**不只是“营销很重要”，而是一套能反向塑造产品立项、商业化和人才结构的市场接口。

### Terminology ruling — “富豪阶级游戏性”

作者旧稿里关于《征途》需求结构的正式术语统一为 **“富豪阶级游戏性”**；“资产阶级游戏性”不作为本项目正式术语。

这里的“富豪阶级”不是现实人口统计阶层标签，而是需求模型：**现实财富能否通过规则被持续转换为游戏内稀缺能力、地位、可见权力和相对优势。**

详细机制拆解见：
- [018 — 富豪阶级游戏性、玩家社会化与 Design Attractor](../../country-studies/china/018-wealth-class-gameplay-player-socialization-design-attractor.md)

新增强制区分：
- F2P ≠ 自动等于富豪阶级游戏性；
- 抽卡 ≠ 自动等于富豪阶级游戏性；
- cosmetic monetization ≠ 富豪阶级游戏性；
- 关键变量是 `RESOURCE_CONVERSION_RIGHT` 与相对优势是否可持续购买。

旧稿同时提出“类型与受众互相塑造”的母题；现统一由018中的 `PREFERENCE_SOCIALIZATION / GENRE↔AUDIENCE CO-EVOLUTION / DESIGN_ATTRACTOR` 承接。

但旧稿里有两类表述需要正式修正：

### 修正 A：不能再写“史玉柱发明免费网游 / 世界第一款免费网游”

巨人自己的 2007 F-1 已明确写：F2P MMO 在中国至少 2003 年已经出现；到 2006 年，F2P 已约占中国网游收入 51.6%，略高于 pay-to-play 的 47.9%。

此外盛大在 **2005 Q4** 已把《热血传奇》《梦幻国度》《传奇世界》等核心 MMORPG 转为 basic play free + in-game value-added services。

因此《征途》的更准确历史位置不是“发明 F2P”，而是：

> **在已经存在的 F2P 条件上，把免费人口、高付费玩家、阶级化数值、社会关系、快速运营和全国地推进一步整合成高度一致的产品—商业系统。**

对应正式档案：[`CASE-033`](../../cases/CASE-033-zhengtu-shi-yuzhu.md)。

### 修正 B：不能再把“渠道拿 70%–90% 是常态”当成已证事实

公开行业材料确实存在极端个案与多层抽成，但当前更硬的 SEC 证据是 iDreamSky：其与第三方渠道合作时，渠道费通常为 gross billings 的 **40%–70%**；在其典型发行安排下，开发者通常拿 gross billings 的 **15%–30%**。

这已经足够支持“渠道拥有很强 bargaining power”，无需把未经统一口径审计的 70%–90% 写成常态。

---

## 2. Phase A → B：盛大先解决的不是“玩法创新”，而是收钱与触达

### 2.1 《热血传奇》证明在线服务可以绕开零售软件的脆弱回款

盛大 2004/2005 SEC 申报材料给出一组非常清楚的数据：

- 《热血传奇》2001 年 11 月商业上线；
- 2002 年盛大 online game revenue 约 **RMB344.4m**，当年基本全部来自 Mir II；
- average concurrent users 从 2001 年末约 43,736 上升到 2002 年约 **278,186**；
- 2002 年 operating income 约 **RMB162.6m**。

这里不能把成功全部归因于产品原创——Mir II 是韩国授权产品。

真正值得研究的是盛大在中国本地搭出来的 monetization/distribution perimeter。

### 2.2 点卡 + 网吧 + 全国零售网络，是一种“支付基础设施创业”

盛大 2004 年 SEC 文件写：

- 全国 distribution/payment network 触及 **317,000+ retail POS**；
- 其中 **40%+ 是网吧**；
- 公司还在建设把网吧联入信息系统的管理网络；
- 2003 年其 online-game revenue 中，预付卡给 e-sales distributors 的折扣约 23%，给 offline distributors 约 14%。

这说明早期中国网游的关键竞争力之一不是今天意义上的“投广告”，而是：

> **让没有信用卡、没有成熟线上支付、常在网吧玩游戏的人，能持续、低摩擦地把现金变成在线服务时长。**

盛大当前官方历史页也把当年问题总结为“没有 online payment mechanism”，并回顾其网吧和预付卡网络。官方回忆可作为 P0/P1 自述使用，但具体规模仍以同期 SEC 文件优先。

### 2.3 这一步首先改变的是商业可行性

因此 2000s 中国产业的第一次重大制度重写可以表达为：

```text
可复制的软件商品
→ 盗版/零售回款脆弱

在线持续服务
+
账号/服务器控制
+
点卡/网吧网络
→ 可持续收费
```

它解释了为什么人才会大规模迁往网游：不是因为所有人突然觉得 MMO 更“高级”，而是服务型产品第一次把真实玩家规模稳定映射成现金流。

### Sources

- Shanda Interactive Entertainment F-1 / 2004–2005 SEC filings:  
  https://www.sec.gov/Archives/edgar/data/1278308/000114554904000629/u98811b4e424b4.htm  
  https://www.sec.gov/Archives/edgar/data/1278308/000114554905000033/u99471fv1.htm
- Shanda company retrospective:  
  https://www.shanda.com/shanda-games/

---

## 3. 2005–2006：从“卖时间”到“免费人口 + 增值服务”

### 3.1 盛大已经在《征途》商业上线前做 F2P 转换

盛大 2005 年 Q4 的公开披露写明，公司把《热血传奇》《梦幻国度》《传奇世界》改为 free-to-play + in-game value-added services。

其后年报把这个模式称为 **Come-Stay-Pay (CSP)**。

这一步的逻辑是：

```text
先付费才进场
→
先让人进场
→
让部分用户在游戏内部为增值服务付费
```

这已经把“每个用户都必须贡献近似相同的时间费”改成了“用户价值可以高度不均匀”。

Source:
https://www.sec.gov/Archives/edgar/data/1278308/000130901406000154/exhibit1.htm

### 3.2 《征途》的真正增量：把不均匀付费做成社会结构

CASE-033 当前证据支持：

- 史玉柱明确把大量免费玩家视为高付费玩家愿意消费的社会环境；
- 团队把 lower-tier city / rural market、网吧、地推与游戏内关系结构同时考虑；
- 巨人形成 250+ liaison offices、2,000+ liaison personnel 的全国推广外围；
- 游戏以虚拟商品/服务而不是统一时间费作为核心收入；
- 公司高频更新，并把 player preference adaptation 当成核心能力。

因此从盛大到《征途》不是“点卡突然变氪金”的断裂，而是：

> **先有 service monetization 基础设施，再有 F2P 入口改革，最后才出现把异质付费能力、社会地位与数值成长高度系统化的《征途》。**

这条顺序比“史玉柱一人发明中国氪金游戏”更接近产业史。

---

## 4. Phase C：智能手机没有消灭渠道，反而制造了新的渠道租

### 4.1 Google Play 缺席后的中国 Android 是多商店生态

学术研究对 16 个中国 Android 市场的比较明确指出：中国用户无法使用 Google Play 获取应用，于是形成手机厂商商店（Huawei / Xiaomi / OPPO 等）和互联网公司商店（Baidu / Qihoo / Tencent 等）并存的碎片化生态。

Source:
https://arxiv.org/abs/1810.07780

这不是单纯“多几个下载站”。

当某个 app store 同时拥有：

- 预装入口；
- 用户账号；
- 支付；
- 推荐位；
- 联运能力；
- 设备出货；

它在游戏价值链里就不仅是 CDN，而成为**用户获取与收款的地主节点**。

### 4.2 2014：发行商需要管理上千渠道

iDreamSky 的 2014 20-F 写得很直白：公司当年通过 **1,000+ distribution channels** 在中国分发游戏，包括应用商店、微信、手机预装、三大运营商、浏览器、广告联盟等。

同一文件还披露：

- 渠道费典型为 gross billings 的 **40%–70%**；
- 开发商在典型 revenue-sharing arrangement 下通常拿 gross billings 的 **15%–30%**；
- 渠道成本在 2013 年一度约占公司 total revenues 的 **50.3%**；
- 公司明确把与 payment/distribution channels 的谈判条件写成影响 profitability 的关键因素。

Source:
https://www.sec.gov/Archives/edgar/data/1600527/000119312515159477/d902553d20f.htm

这给“渠道为王”一个比情绪化叙述更精确的定义：

> **当内容方必须通过掌握安装入口、支付和推荐流量的第三方才能规模触达用户时，渠道条款本身成为产品单位经济的重要变量。**

### 4.3 这里会产生一种能力筛选

在这种制度下，最容易被持续奖励的能力包括：

- retention；
- ARPU / ARPPU / LTV；
- virtual-item economy；
- live ops；
- events / content cadence；
- UA；
- channel negotiation；
- data operations；
- multi-SDK / multi-channel publishing。

这并不等于“玩法无用”。

更准确的是：

> **玩法如果不能转译成足够强的留存、付费深度或获客效率，就较难与掌握流量的渠道形成同向激励。**

这就是作者“高数值通胀率体制会训练行业能力树”命题目前最坚实的外部机制基础。

---

## 5. 《刀塔传奇》：产业特化并不等于没有创新

### 5.1 创始团队本身来自成熟商业网游体系

王信文公开回忆：2009–2013 年在腾讯互娱做 MMO 端游运营和策划；2013 年和同事离职创业莉莉丝。

其早期演讲并不是“我们找一个已经验证的卡牌模板换皮”，反而明确提出：手机上能不能出现三消、回合、ARPG、塔防之外的新主流战斗玩法？

Source:
https://m.huxiu.com/article/100622.html

这点必须保留，否则会把真实产业史简化成“渠道只会奖励抄袭”。

### 5.2 但它同时拥有极强的商业化与发行经济

公开重组材料显示：

- 2014 年《刀塔传奇》gross billings 约 **RMB2.16bn**；
- 扣除渠道后，中清龙图和莉莉丝按 65% / 35% 分配；
- 莉莉丝当年实际分成约 **RMB418m**；
- 约 42% 流水来自 iOS，接近六成来自 Android；
- 中清龙图 2014 年市场营销费用超过 RMB90m。

Source lead / secondary reconstruction from transaction materials:
https://games.sina.cn/cyfw/2015-05-08/detail-icpkqeaz3425722.d.html

原始交易预案仍应作为最终财务引用优先来源。

### 5.3 关键历史含义：创新与高变现第一次形成了极强示范组合

所以《刀塔传奇》的历史位置不应写成：

> “中国渠道把大家逼成抄袭卡牌。”

而应该写成：

> **一个有玩法差异化意识的商业游戏团队，在移动端同时证明了战斗创新、长线数值成长、留存、渠道发行和高流水可以被捏成同一套产品。**

这种结果对后续创业者、资本和人才产生的模仿激励，远强于一个口碑很好但只卖几十万份的 premium 小品。

因此 `industry specialization` 是筛选结果，而不是“所有参与者都没有创造力”。

---

## 6. 从《刀塔传奇》到“卡牌化”：应该研究的是复制了什么

作者旧稿把中国手游大量“卡牌化”与高数值通胀联系在一起，这个方向值得继续，但必须拆成三个可检验层：

1. **representation layer**：角色/单位被包装为可收集卡牌；
2. **progression layer**：等级、品质、碎片、装备、技能等多轴成长；
3. **monetization layer**：抽取、刷新、体力、材料、活动、竞争压力与成长加速。

以后不能只看到 UI 是“卡牌”就判断其商业制度相同。

真正值得追的是：

> 哪些系统被复制，是因为它们提高了玩法可读性与内容复用；哪些系统被复制，是因为它们提高了付费深度、留存或渠道侧预期收入？

《符石守护者》→《不思议迷宫》的比较就是一个很好的微观切片，详见 [`runestone-keeper-vs-gumballs-001.md`](runestone-keeper-vs-gumballs-001.md)。

---

## 7. Phase D：内容方为什么在 2020 年突然有资格说“不”

### 7.1 不是渠道突然变善良，而是 outside option 变强

2020 年《万国觉醒》《原神》同时没有按传统方式进入多个主流安卓商店。

同期公开报道普遍把中国 Android 游戏传统分成概括为约 **5:5**，而 Apple / Google 的标准模式约为平台 30%、内容方 70%。

《万国觉醒》只通过 App Store、官网、TapTap、九游等接口上线；《原神》初期也缺席华为、小米等部分安卓渠道。

Sources:
https://m.thepaper.cn/newsDetail_forward_9323897
https://m.21jingji.com/article/20201023/herald/acfd31a2c02e14a7071e1ed4b824e8d5_zaker.html

关键不是“内容为王”四个字，而是 bargaining model 变了：

```text
旧模型：
没有渠道 → 很难触达用户

新模型：
品牌预约 + 官网直装 + TapTap + 自有账号 + 社交媒体/creator + 全球商店 + 跨平台
→ 渠道只是多个入口之一
```

内容方只要拥有可信的 outside option，就能要求更好的分成。

### 7.2 《万国觉醒》进入中国前，已经先证明全球市场

公开 Sensor Tower 数据显示，《万国觉醒》2019 年海外收入估算约 **US$458m**，美国、韩国、中国香港为前三市场。

这意味着莉莉丝 2020 年与国内渠道谈判时，并不是一个“没有渠道就会死”的新工作室。

Source:
https://www.ithome.com/0/469/499.htm

### 7.3 《原神》则把 outside option 做成全球多平台产品

《原神》2020-09-28 全球同步上线移动端，同时也有 PC / PlayStation 版本。Sensor Tower 估算其首月仅 App Store + Google Play 就产生约 **US$245m** 玩家支出；首周已有约 58% mobile revenue 来自中国以外。

Sources:
https://sensortower.com/blog/genshin-impact-first-month-revenue
https://sensortower.com/blog/genshin-impact-first-week-revenue

因此《原神》对渠道议价的真正底层能力不是“游戏品质好所以渠道服软”，而是：

> **它能在多个国家、多个平台、多个支付与分发接口上直接找到用户。**

这才是研发权力回流最可迁移的制度解释。

---

## 8. 但 Phase D 不是“渠道时代结束”

2024 年 Tencent 把《地下城与勇士：起源》从部分 Android app stores 移除时，Reuters 仍然把中国 Android 游戏渠道常见的 **50% revenue split** 描述为长期争议焦点。

Source:
https://www.reuters.com/technology/tencents-dungeon-fighter-game-pulled-some-android-app-stores-2024-06-20/

这说明：

> **2020 以后发生的是议价权重平衡，而不是渠道租金消失。**

头部内容方、自有社区强、全球发行强、可官网直装的产品能绕开；弱品牌、小团队、纯本地 mobile 产品仍可能高度依赖渠道。

到 2026 年，Apple 在中国大陆也把标准 App Store commission 从 30% 下调到 25%。这属于另一个平台治理体系，但同样说明“数字分发租金”仍在持续被开发者、平台与监管重新谈判。

Source:
https://www.reuters.com/world/china/apple-cuts-china-app-store-commission-fees-after-government-pressure-2026-03-13/

---

## 9. 这条谱系怎样连接中国独立游戏

中国现代 premium indie 的关键，不是终于出现了一群“更有艺术追求”的人。

更重要的是另一套生产函数终于变得可用：

```text
Unity / UE / middleware
+
Steam / console / global digital stores
+
Alipay / cards / global settlement infrastructure
+
YouTube / TikTok / Bilibili / creator network
+
Discord / Reddit / community tools
+
publisher / grant / crowdfunding / Early Access
↓
小团队不再必须把自己塞进本地 F2P channel model 才能活
```

于是中国开发者第一次更大规模地拥有选择：

- 留在高 LTV / live-service 体系；
- 做全球 F2P；
- 做 premium Steam；
- 做小团队 niche product；
- 做 creator-led distribution；
- 混合使用 publisher / crowdfunding / self-publishing。

这就是为什么本书研究 `indie movement` 必须同时写《传奇》《征途》《刀塔传奇》《原神》：它们本身未必是独立游戏，但它们改变了**独立开发者所处的生产制度背景**。

---

## 10. 制度矩阵

| 阶段 | 核心瓶颈 | 谁最有权力 | 被奖励的能力 | 典型锚点 |
|---|---|---|---|---|
| 1990s–early 2000s premium | 盗版、支付、零售、收入水平 | 盗版/零售环境本身；正规内容方弱 | 技术制作但难回款 | 国产单机、《七夜》前史 |
| 2001–2005 service/pay-time | 收钱与持续服务 | 掌握服务器、点卡、网吧网络的运营商 | server ops、distribution、billing、community | 盛大 / Mir II |
| 2005–2010 F2P deepening | 扩用户与异质变现 | 运营商/研发一体公司 | virtual economy、social status、live ops、ground marketing | 盛大 CSP、《征途》 |
| 2010s mobile channel regime | 安装入口/支付/推荐位 | app stores、发行商、平台、手机厂商 | LTV、UA、渠道、活动、数值、SDK/联运 | iDreamSky 生态、《刀塔传奇》 |
| late 2010s global mobile | 全球获客和长期产品 | 强研发 + 全球发行/买量平台 | global UA、localization、SLG/live ops、品牌 | 《万国觉醒》 |
| 2020s content rebalancing | 多接口市场接入 | 强内容方与平台重新博弈 | cross-platform、brand、direct community、global publishing | 《原神》《万国觉醒》渠道冲突 |
| 2020s premium indie | selection / scope / discoverability | 内容方与平台共同决定；creator network 权重上升 | hook、demo、wishlist、creator legibility、low burn | 中国 Steam 新独立谱系 |

---

## 11. 对“渠道为王”命题的证据分层

### STRONGLY SUPPORTED

- 2000s 中国 online service 相对 premium/retail 更容易形成可持续收费；
- 盛大建立了巨大 prepaid card / Internet-cafe distribution network；
- 中国 F2P 在《征途》前已存在并快速扩大；
- 2010s 中国 Android 分发高度碎片化，发行商需要同时管理大量渠道；
- 2014 前后渠道可拿 gross billings 的非常高比例，并拥有强 bargaining power；
- 《刀塔传奇》证明 mobile F2P 可以产生十亿人民币级年流水；
- 2020 《原神》《万国觉醒》公开绕开/拒绝部分传统 Android 渠道；
- 2024 Android revenue-share conflict 仍然存在。

### SUPPORTED AS MECHANISM, NOT YET A UNIVERSAL LAW

- 高抽成 + 推荐位稀缺会使渠道偏好高 LTV / 高变现产品；
- 这种收入结构会提高 monetization / live ops / UA 等岗位和公司的相对价值；
- 长期激励会造成产业能力路径依赖，使 premium indie selection/scope/creator marketing 相对薄弱。

### AUTHOR HYPOTHESIS / NEEDS MORE EVIDENCE

- 渠道在行业层面有意识地“压制更好玩的低变现产品”；
- 高数值产品取得推荐主要是因为渠道逐利，而非同时受到留存、题材、买量效率、用户偏好等因素影响；
- 这种机制足以单独解释中国玩家品味或全部产品形态；
- “70%–90% 抽成是常态”；
- 《征途》是免费制的发明者。

这些旧表达在 reader layer 应改成可证伪机制，不再作为事实句使用。

---

## 12. 下一轮最值得核的四个缺口

1. **盛大 → 《征途》的机制迁移**：哪些具体增值服务、装备/身份/社会设计已经在 2005 盛大 CSP 中出现，哪些是《征途》真正强化的新组合？
2. **《刀塔传奇》复制链**：2014–2017 同类产品到底复制了战斗表示、数值成长、抽卡/碎片、运营活动还是渠道打法？需要挑 3–5 个跟进者做结构对照。
3. **渠道推荐因果**：寻找渠道内部招商/评级/推荐规则、CP 合同、渠道人士访谈，直接验证“高 LTV → 更多推荐资源”，避免只靠开发者侧推断。
4. **内容方议价回流的单位经济**：对《原神》《万国觉醒》以及 2024 DNF Mobile 比较官网直装、渠道服、iOS、全球商店的用户获取成本、抽成、账号关系与长期价值。

若这四项核完，就有资格把“**收入接口会筛选产业能力**”升级为正式跨案例 Claim 候选。
