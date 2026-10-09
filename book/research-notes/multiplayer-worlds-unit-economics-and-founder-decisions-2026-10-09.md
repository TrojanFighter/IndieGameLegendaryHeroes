# 多人游戏的架构、单位经济与创始人决策：Improbable × PUBG × Tarkov × Party Animals × Prologue

- **Status:** RESEARCH NOTE / SOURCE-ANCHORED / COUNTERFACTUALS OPEN
- **As-of:** 2026-10-09
- **定位：** 以决策节点为主线的跨案例研究，不新占编号 CASE。连接 [CASE-022：Contract Wars→Tarkov](../../cases/CASE-022-escape-from-tarkov-lineage.md)、[CASE-032：Greene / PUBG](../../cases/CASE-032-pubg-brendan-greene.md)、[032：Exam Overfit](../../country-studies/china/032-exam-overfit-routine-expertise-open-domain-transfer.md)、[033：Technology Proxy](../../country-studies/china/033-technology-proxies-experience-demand-and-commercial-feedback.md)、[动态竞争决策笔记](static-target-trap-chiang-and-strategic-recalibration-2026-10-09.md)。
- **Privacy / method:** 私人聊天、面试印象只构成研究线索，不以姓名、引文或未经证实的内部指控录入公开仓库。制作人访谈能证明其陈述存在，不自动证明解释正确。
- **严格区分：** 同服同时在线、全平台 CCU、局内人数、历史峰值、实体数、总销量、单玩家小时成本以及营收并不具有直接可比性。

## 0. 不是“哪个国家更会优化”，而是谁在什么阶段敢重写题目

| 路线 | 先得到什么证据 | 做大了什么义务 | 产品结果和反压力 |
|---|---|---|---|
| **Improbable / SpatialOS → Worlds Adrift** | 分布式持续模拟技术有可行性 | 依赖中间件升级、跨进程状态、永久模拟及伙伴技术支持 | Bossa 2019关闭游戏；Improbable本体仍在经营/转型，不能写“公司破产” |
| **Greene + Bluehole / PUBG** | ARMA/DayZ、H1Z1相关玩法通过真实玩家/社群先验证 | 百人短局、网络同步、反作弊和服务运营 | 2017起商业爆发，服务器负载问题仍十分真实；需记录韩国团队的生产贡献 |
| **Contract Wars → Battlestate / Tarkov** | 旧FPS商业开发形成Unity、射击、团队、现金流 | 战局同步、反作弊、经济系统、长期用户义务 | 买断/版本升级与长期迭代；严重技术债，不能假设其服务成本极低或为零 |
| **Recreate / Party Animals** | 2020免费Demo已有显著真实兴趣 | 物理同步、专用/房主机架构、内容规模、管理组织 | 2023正式上市并运营；2020–23长期延期究竟必要多少**未获验证** |
| **Greene / Prologue → Melba** | 地形生成技术进展；不同于PUBG的规则验证 | 单人探索产品研发及宏大技术路线的融资/制作义务 | 2026《Prologue》停止开发、转免费，继续Melba；不能混入多人服务器亏损解释 |

**机制：** 技术可行性 ≠ 产品吸引力 ≠ 经济可行性 ≠ 生态扩散能力。技术亦可能先于游戏启发真正新体验；不得抹去 Carmack/DOOM 式“技术—玩法共演化”路径。可批评的是替代性选择被忽略、证据未及时回写产品定义，而不是“技术创新本身错误”。

## 1. 需要保留的同期工程证据

### SpatialOS / Bossa：技术义务的可见价格

2019年2月，Bossa CTO Sylvain Cornillon在《The Path Ahead》中说过：SpatialOS 底层架构变化，使团队若迁入新版可能需要改写**超过40%项目代码**，服务端还可能重写为另一语言。**这是当事人的工程估算，非最终审计数字。**

2019年4月3日 Bossa 开发日志《Tech Twednesday - Death to all Ships》具体报告：通过保存离线船只、将其从实时世界移出、上线再重建，实体数从约**300万**降至约**4.3万**，CPU及快照峰值降低。**实体≠玩家；这不是把Tarkov商业逻辑直接安装到SpatialOS的证明。**

不能将《Worlds Adrift》失败全因果归给SpatialOS：早期游戏玩法市场吸引力、开发优先级、商业运营都需竞争解释；同样不应将Improbable出售MPG（2023年Keywords以**7650万英镑**收购）误记为SpatialOS当初的平台战略成功。

来源（S1同期，非事后传记）：
- Bossa 官方 Steam 公告合集（含上述两篇）：https://steamcommunity.com/app/322780/allnews/
- Keywords 2023-12-18收购公告：https://www.investegate.co.uk/announcement/rns/keywords-studios--kws/acquisition/7947327

### PUBG：玩家需求既成之后以性能分析改善同步

2018年官方性能分析在一次**90人生存**剖析中测出Net Flush **43.2ms**；据此减少距离较远角色的复制：超过70米跳过1帧、超过400米跳过2帧。官方报告一次**85人**样本 tick **18.5→22.9**，开火响应延迟 **149.4→61.6ms**。这些均非总体均值、真实成本或“传统服务器解决一切”的证明。

来源（S1）：https://steamcommunity.com/games/578080/announcements/detail/1689300456332644145

### Tarkov：把持久性集中到战利品、经济和用户状态

Unity 官方案例核实《Contract Wars》为Battlestate核心成员积累了FPS/Unity、协作经验和创建工作室的资金；其「小众硬核」赌注不是从零制造全部能力。塔科夫通过短期战局+局外账户/仓库持续状态组织体验，转而承担漫长技术债、运维与收费方案调整。研究2024 PvE本地运行的成本减负时必须另核补丁版本与适用战局。**绝不能从140/150/250美元定价，直接宣布老用户必然亏损或游戏为“庞氏”。**

来源（S1）：https://unity.com/made-with-unity/escape-from-tarkov ；进一步证据由CASE-022追踪。

### Party Animals：高同步量的自述不是三年延期免责证

- **2020-11同期专访**：罗子雄称当时约三年制作8张地图，糖果工厂多次推翻、耗时约一年；也承认程序员抱怨其频繁调整需求。说明**内容返工在服务器危机后的长期延期之前就存在**。
- **2022-05-25官方DEV LOG 01**：2022直接参与制作人数是2020的**三倍**，并自述人数增长带来沟通/流程效率下降；外部审批、疫情也可能影响节点。
- **2022-06-29官方DEV LOG 02**：明确探索房主承担计算/转发、P2P以及其他网络结构；意味着可替代设计空间**至少在2022已被讨论**，但不证明2020以前“完全没调查过”。
- **2023上市**：产品实现了商业发售和持续运营，不能据此倒推所有延期、完美主义打磨都最优；公开“成本四倍”“一角色同步量抵CS:GO整局”等制作方说法，应列为**被访者估计、账单及测试配置未知**。
- **同行压力测试**：《Human: Fall Flat》《Besiege》等有分阶段追加多人或主机承担物理模拟的路线；这只能证明**有不同选择空间**，不能推断某个方案必然可无代价移植到实时物理乱斗。

来源：
- 2020原采访转载：https://www.gameres.com/876152.html
- DEV LOG 01：https://store.steampowered.com/news/posts/?enddate=1653485767&feed=steam_community_announcements
- DEV LOG 02：https://steamcommunity.com/games/1260320/announcements/detail/3319730991323784713

### Greene 的第二次创业：拒绝“成功者每次都对”

《PUBG》作者Greene后来转向大地形生成与更宏大的虚拟世界路线。PLAYERUNKNOWN Productions官方于**2026-06-17**宣布停止《Prologue: Go Wayback!》游戏开发并改为免费，缩编后继续Melba技术。《Prologue》是单人产品，**不能把其失败写成多人服务器费用过高**。技术积累可能有后续价值，但不是首款商业产品市场适配的证明。

来源（S1工作室声明）：https://pp.studio/news/prologue-go-wayback-goes-free

## 2. 服务器成本比较：严格禁止伪实测倍数

```text
成本/付费玩家小时 =
 [实际实例小时 × 地区/合同有效单价 + 实际计费出站GB × 有效带宽单价
  + 玩家相关持久化后端/反作弊/支付/客服变动成本]
 ÷ 同期付费玩家实际游戏小时
```

需要同时控制 `active_sessions_per_instance`、每局实际玩家数、空转率、p95 CPU/内存、tick、跨区域流量、固定与变动成本边界、价格/退款/版本升级、Lifetime play-hours。

**已发生的研究错误（禁止复用）：** 曾用「猛兽一机4局，塔科夫一机2局」等自行设定装箱率，算出“塔科夫成本为猛兽的1.6–3.2倍”。那是**纯场景演算**；装箱率没有实测/厂家合同支持，不能变成两家公司实际成本比值。当前 **actual Tarkov / Party Animals unit cost ratio = UNKNOWN**。同步字节数八倍也绝不等于CPU或总账单八倍。

买断制卖一份后持续服务，可能出现负单位经济，但不自动构成金融意义的庞氏骗局。要验证的是用户生命周期净收入、边际服务成本和固定研发/运营总支出的时间结构。可以严格批评老板把自己选择的复杂性叙述为“行业自然规律”，但批评必须指向可验证的选型、性能、方案与机会成本。

## 3. 不再把制作人口述写成胜利者传记：七项审计

1. **CLAIM vs MEASUREMENT**：谁在何时说“太贵/做不了”，使用了什么实例、负载、价单、代码版本？有无独立复测？
2. **CHOSEN OBLIGATION**：哪些架构义务由产品主动选择（物理精度、持久世界、并发、局数、实时同步、专有平台依赖）？
3. **ALTERNATIVE-SEARCH TIMING**：同行已实践了什么？团队在重大承诺前有没有做最小可行性测试？不能因为存在一个同行例子就断言适用性/发生率。
4. **PLAYER TRUTH BEFORE SCALE**：何时有真实付费或可重复玩家证据？技术投资与团队增员发生在其前还是后？
5. **FOUNDER / ORGANIZATION**：产品眼光、技术长板与项目组织能力分别评估；成功不意味着三项全优，批评一项也不否认其他能力。
6. **OPTION REGISTER**：在2020 Demo之后，《猛兽派对》立即EA、局部修复EA、追加高完成度三种方案的前瞻性效用，均需记下可行条件与未知，不用2023发售反证其他方案必劣。
7. **POST-HOC NARRATIVE GATE**：先看同期记录，再看后来的开发者自述；不同证据来源不独立时不能算“多源印证”。

**可证伪工作假说：** 负责人若只会对既定规格持续解题，而没有在需求、成本、同行、发行窗口变化时重新审题，强执行能力会扩张错误选择的持续成本。与[动态竞争笔记](static-target-trap-chiang-and-strategic-recalibration-2026-10-09.md)共享 `STATIC_TARGET_FALLACY` 和 `STRATEGIC_RECALIBRATION_FAILURE` 机制，但不把所有长制作周期或复杂技术都判为管理失败。

## 4. OPEN QUESTIONS / 缺失分母

- Party Animals 2020–2023人月、总研发成本、关键架构选择时点、真实CCU/服务器帐单和2020 EA风险评估？
- Improbable的SpatialOS单位客户成本、SDK迁移/退出成本与Bossa投入细目？
- Tarkov 同口径每付费玩家小时成本、地区与平台账单，以及多版本付费结构的长期利润？
- Greene/Prologue产品收入、Melba技术路线的分拆目标与下一轮可审计退出标准？
- 固定同代、多人形态、资本规模和成功/失败全集，避免选5个故事就推国别普遍性。

## 2026-10-09 增量：技术准备好≠已有产业愿意/擅长发现新规则

参见[1999—2025民间多人游戏创新的两次浪潮](grassroots-online-multiplayer-opportunity-window-1999-2025.md)：2010索尼《MAG》已有256人同场；1999《CS》、2003《DotA》说明民间玩家规则发现比PUBG早得多。2013 Steam EA/2014 UE4开放/2016 GameLift降低生产或发行门槛，PUBG、Tarkov和大量在线合作游戏不需要从零发明“联网”。Epic在2017年9月数月内推出借鉴PUBG的《Fortnite》BR，说明大公司可以迅速利用成熟的外部规则，不能简单写为大厂无技术/无能力。SteamDB“Online Co-op”回溯发布数量2013年31款、2018年143款、2024年846款；占Steam全部上市比例在2013→2018反而下降，不能把绝对量爆发冒充相对份额暴涨。此阶段更可靠的命题是 **PERMISSIONLESS RULE DISCOVERY + CAPABILITY-TO-DESIGN TRANSLATION GAP**，国别/业态频率待统计。
