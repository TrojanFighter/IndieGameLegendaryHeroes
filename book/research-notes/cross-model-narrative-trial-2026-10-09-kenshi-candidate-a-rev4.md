> **试写候选 v4（保真修订稿）/ Cross-model narrative trial — Kenshi（作者模型 A）。**
> 非正式书稿，非 canonical Profile。v1 / v2 / v3 原样保留，不覆盖。
> 本稿回应 Issue #332 Task A。**注意：v3 已先于本稿逐条修正了 Task A 的主要条目**（动词链、Hunt 立场、bug 时点、Greenlight 锚点、`could be discouraging`、薪水限定），Task A 的表述基于 v2，未包含 v3。v4 修的是 v3 的**遗留项**与本稿逐句回读新发现的未证细节，逐条见文末《Fidelity Readback》。
> 事实基础：`cases/CASE-012-kenshi.md`、`evidence/CASE-012-kenshi-source-ledger.md` @ `main`（已含 PR #319 的 E001 修正与 E003–E008）。
> **这是 writer 自我修正，不替代独立 fact-checker；不得据此宣称漂移已全部修复或通过。** 正式 `book/profiles/`、`cases/`、`evidence/`、`claims/` 未改动。

---

# 一间酒吧，一把椅子，一场内战

2017 年，Chris Hunt 在一次访谈里举过一个例子。游戏里，一个佣兵走进镇子，要找一间酒吧。

可代码里有个很小的错误：佣兵有时会把民宅当成酒吧，走进去，坐下。屋主因为家里闯进个生人而发作，动手打他；守卫被牵扯进来，佣兵的同伙也被牵扯进来——不知不觉，整座小镇就为了一把椅子打起了内战。

Hunt 说，这就是开发 Kenshi 时最大的问题：模拟世界带来的那种纯粹的混乱。

他是 Kenshi 的作者，也是 Lo-Fi Games 的创始人。这游戏不太好归类：开放世界、小队控制、沙盒 RPG，没有主线，没有任务清单。在他的游戏里，玩家扮演的不是天选之人，而是废土上一个谁都能欺负的普通人——光活着就很难，可能只是在城里歇脚，就被卷进一场土匪袭击。那间被认错的房子，就属于这个世界。

## 一个人的系统

Kenshi 的前五六年，只有 Hunt 一个人在做。白天他把时间给游戏，到了夜里，他去做保安，挣最低工资，够糊口就行。

再往前，他二十出头就在当游戏程序员，却受不了那些小成本捞钱的项目，2008 年辞了职，全职做自己的游戏。他学做游戏其实算晚。多年后他在一次网上问答里回忆，自己直到十八岁左右才弄明白怎么真正做出一款游戏——那时他已经会编程，卡住他的是显示画面这类最基础的事。他入行那会儿，想做游戏只有一条路：先学会 C++，再自己拿零碎的东西拼出引擎。他把这些一个人熬出来的时间，大多花在了底层系统和让它能玩起来上；用他的话说，比起玩游戏，他其实更喜欢造游戏。

## 放手

团队里的程序员叫 Sam。他会来问 Hunt 下一个做什么，而 Hunt 的第一反应总是“不，这个我自己来，只有我知道它怎么运转”。他花了不少时间才学会把东西交出去；但很快，让别人替他分担一部分工作，就成了他上瘾的感觉。

钱是按这个顺序来的。2013 年通过 Steam Greenlight 之前，他已经在自己网站上卖 alpha 版本，那笔钱够养活他本人，还能雇几个自由职业者搭把手；真正让他组起一个小团队的，是 Steam 的收入。接下来大约两年，他身边陆续出现了编程、世界设计、公关写作和美术的位置。

麻烦也跟着来了。把游戏挂上去卖，等于答应它会一直能玩。Hunt 说，Early Access 最难的地方正在这里：一边往里加东西，一边得保证已经付钱的人手上那个版本稳定、能玩。更新一旦间隔久了，玩家就更难信任他；那几年确实有不少靠 alpha 集资的游戏半路消失，Hunt 说这让剩下的人承受了更多压力。引擎也越来越旧，升级一次要反复打补丁，真想往前走就得大改。长长的 bug 清单、成千上万条评论，有时会让人泄气；可他也说，恰恰是那些骂得很凶的反馈里，偶尔藏着真正该修的东西。

团队来了，钱也来了。但在 2018 年那次采访里，他说自己给自己开的工资，还是很少。

---

## v4 相对 v3 的修改记录（不属于正文）

| # | v3 写法 | v4 处理 | 依据 |
| --- | --- | --- | --- |
| 1 | “整座小镇就为**一吧椅子**打起了内战” | “一把椅子” | 错别字。E003 原文为 `a civil war over a chair`；Task A §5 已明文要求改正，v3 未改 |
| 2 | “Chris Hunt 的游戏里有一小队佣兵。**他给他们的差事**很简单：去镇上找一间酒吧。” | 改为“2017 年，Chris Hunt 在一次访谈里举过一个例子。游戏里，一个佣兵走进镇子，要找一间酒吧。” | Task A §3 已明文点名“`Hunt 给佣兵差事`不能凭口述补叙操作者”，v3 未改；E003 只有 `a single mercenary in a town, looking for a bar`，没有派活这一动作，也没有“一小队” |
| 3 | 事件的归属（Hunt 口述的 bug 示例）在**下一段**才交代，本段以“代码里有个很小的错误”作客观陈述 | 归属前置到段首（“在一次访谈里举过一个例子”） | Task A §1：不能在开头未经交代就写成独立实证录像 |
| 4 | “**他看不惯那些大厂 RPG 一开场就让你当英雄的做法**——在他的世界里，你什么都不是” | 删除对创作者态度的推断，改为“**在他的游戏里**，玩家扮演的不是天选之人，而是废土上一个谁都能欺负的普通人” | E001 只记 `a weak starting character`，全库无 Hunt 评价大厂做法的原话。这是给人物加的立场，不是事实 |
| 5 | “**第一个**进来的程序员叫 Sam” | “团队里的程序员叫 Sam” | E003 为 `our programmer Sam`；E004 列出的四名核心成员没有先后顺序，“第一个”无依据 |
| 6 | “大多花在了底层的系统上，**而不是能看的画面上**” | “大多花在了底层系统和让它能玩起来上” | E001 原文为 `fundamental systems and reaching a playable state`，没有与画面作对比 |
| 7 | “更新一旦间隔久了，玩家就开始**怀疑他是不是也跑了**” | “更新一旦间隔久了，玩家就更难信任他” | E005 记 `distrust during update gaps`；“怀疑他跑了”是把玩家的心理内容补写了出来 |
| 8 | “那几年确实有不少 Early Access 的游戏半路消失，**让他这样的人**更难被信任” | “那几年确实有不少靠 alpha 集资的游戏半路消失，Hunt 说这让剩下的人承受了更多压力” | 贴近 E003 原话 `other alpha-funded games have gone under or been abandoned which has made players more distrustful, which puts more pressure on the rest of us`，并标明是 Hunt 的说法 |
| 9 | “却受不了那些**在他看来纯粹浪费时间**的小成本捞钱项目” | “却受不了那些小成本捞钱的项目” | E002 为 `hated working on small cash-cow games`；“纯粹浪费时间”是添加的解释 |
| 10 | v3 只有《对 v2 的修正记录》表，没有按项回读 | 增加《Fidelity Readback》 | Task A §7 要求 actor / chronology / quote / causation / recall / UNKNOWN 逐项回读 |

## Fidelity Readback（v4 对 canonical 来源逐项回读）

按 [EDITORIAL-REWRITE-PROTOCOL §3](../../book/EDITORIAL-REWRITE-PROTOCOL.md) 的不可偷换项逐条核。

| 不可偷换项 | v4 的处理 | 判定 |
| --- | --- | --- |
| **Actor / credit** | 佣兵事件标明是 Hunt 在访谈中举的例子，不写成现实事件；“团队里的程序员 Sam”不称“第一个”；收入阶段区分本人 / freelancers / 团队 | `PRESERVED` |
| **Chronology / knowledge at the time** | 前五六年 solo（E001 2015 口径）；2008 年离职（E002）；Greenlight 之前自营 alpha（E001）；Steam EA 后组队（E001/E002）；2018 年访谈期的低薪（E004）。全篇不出现“十年 solo” | `PRESERVED` |
| **Negation / modality** | “有时会把民宅当成酒吧”保留 `sometimes`；“他说/他回忆”保持在句内；删去“总是”“一直”一类无据范围词 | `PRESERVED` |
| **Causation / alternative** | 不写“因为 Steam 才有玩家收入”，保留自营 alpha → freelancer → Steam 组队的顺序；玩家不信任写成 Hunt 的说法，不写成因果结论 | `PRESERVED` |
| **Numbers / denominators** | 全篇无金额、无销量、无 headcount 数字。低薪只说“很少”，不换算 | `PRESERVED` |
| **Evidence boundary** | 佣兵事件的性质、单人期口径、薪水口径三处在文末《仍待独立核实》保留 | `PRESERVED` |
| **Historical regime** | 不把 2013 Greenlight、2013 EA 的窗口当作今天可复制的路径 | `N/A（本稿未作可迁移主张）` |
| **Quote / 著作权** | 正文只剩一处短引语（Sam 那段，E003）；英文原句集中在文末来源区，正文不复述整段英文访谈 | `PRESERVED` |
| **Recall / 同期** | “十八岁才弄明白做游戏”明确写为“多年后在一次网上问答里回忆”（E007 2019）；“更喜欢造游戏”归 E001（2015） | `PRESERVED` |
| **UNKNOWN** | 家庭与住房、储蓄、夜班排班、逐年 headcount、EA 收入金额、完整协作者边界，均未写 | `PRESERVED` |

**仍标 `NEEDS_VERIFY` 的一处**：v4 删掉了“他看不惯大厂做英雄的做法”（修改 4）。若 Lane B 能取到 Hunt 本人关于“不做天选之人”的原话（E003 的玩家开局段落只被概括为 `creator explanations of design`，未见动词），这一句可以按原文恢复。**在取到之前不得以肯定句回到正文。**

## 来源（不属于正文）

1. **ESpalding / GameSkinny，2017-03-14**（Ledger E003）：佣兵轶事 `The biggest problem is the sheer chaos of a simulated world. For instance, a single mercenary in a town, looking for a bar. There was a tiny bug where they would sometimes pick a house instead of a bar, wander into this person's house and sit down. Then the house owner freaks out at this intruder, attacks him, then the town guard gets involved, then the mercenary's buddies get involved, and before you know it the whole town is having a civil war over a chair.`；放手 `It took me a while to gradually release control of things, like our programmer Sam, would ask "what shall I work on next?" and everything I thought of I was like "No, I better do that myself, only I know how it works". But pretty quickly I got addicted to the feeling of other people doing some of my work for me.`；引擎 `Back when I started the only way to make a game was to learn C++ and cobble your own engine together out of parts.`；玩家不信任 `Over the years other alpha-funded games have gone under or been abandoned which has made players more distrustful, which puts more pressure on the rest of us.`
2. **Chris Priestman / Siliconera，2015-08-30**（Ledger E001）：`For the first five or six years, I worked alone on it full time whilst juggling a minimum wage security guard job during the nights to get by.`；`Before we got Greenlit in 2013, I was alpha funding it myself through my own website, which was enough to support myself and hire freelancers. Steam Early Access, however, has given me the funding I need to get a team together and make progress.`；`The only difficulty of Early Access is that we have to work under more pressure to keep the game steady and playable for the players while we work.`；`I even enjoy creating Kenshi more than I enjoy playing games themselves.`
3. **Lo-Fi Games，`Fact Sheet`**（机构历史页，无发布日）（Ledger E002）：`Chris Hunt, founder of Lo-Fi Games, spent his early 20s working as a game programmer but hated working on small cash-cow games… In 2008 he left, working on Kenshi full-time while working night shifts as a security guard to make just enough money to scrape by.`
4. **徳岡正肇 / 4Gamer，2018-09-26**（Ledger E004）：前期每周两晚保安、五天开发；四名核心成员（Hunt、Sam Gin、Natalie、Oli Hatton）与两位自由职业者；自称保持最低薪水、经历困难时期。（回忆口径，无薪资数字。）
5. **Natalie Clayton / PC Games Insider，2018-12-06**（Ledger E005）：更新间隔期与其他 Early Access 游戏被放弃之后的玩家不信任；反复引擎升级、更深改进需大重写。
6. **一條貴彰 / Business 4Gamer，2018-10-02**（Ledger E006）：公开后持续忙碌；长长的 bug 清单与数千条评论可能令人气馁，但愤怒的 bug 反馈里也有有用原因。属其自述，非调查情绪或工时。
7. **Chris Hunt（Reddit 账号 Captain_Deathbeard）/ r/IAmA，2019-08-08**（Ledger E007）：约十八岁才弄明白怎么做游戏、此前已会编程。

## 有意舍弃的材料及原因

- 2017 访谈里 Hunt 对玩家开局行为的描述（属创作者对受众的说明、非代表样本）。
- 售价、销量与奖项等商业成就（易滑向成功学，与“人物与决策”无关）。
- 逐年人员规模、EA 收入金额、夜班精确排班（`UNKNOWN`）。
- 2019 续作计划与其“两年内发行”估计（超出时间范围，未核）。
- 同名 Reddit 提问者经历（E007 已明确不属于 Hunt）。
- **v4 新增舍弃：** Hunt 对大厂 RPG 的态度的推断（无原话）；“第一个员工”“一小队佣兵”“怀疑他跑了”等来源未给的具体化。宁可句子更素，也不补写。

## 仍待独立核实

1. **佣兵轶事的性质与归属**：2017 年 Hunt 口述的游戏内 bug 示例，非现实事件；部分副本失效，本次依赖 Wayback 快照，需确认是否存在 Hunt 本人的其他版本。
2. **单人期口径**：本稿取 2015 年“前五六年”；2018 年媒体标题的“一人十年”与 E004/E006 的“六年 solo”冲突，已避免倒写。
3. **薪水表述**：E004 的“自压工资”属 2018 年采访期回忆，无公开金额与年份范围。

## 与 v3 的关系与版本保留

- v1 / v2 / v3 原样保留于 `trial/kenshi-narrative-candidate-a-2026-10-09`，本稿不覆盖它们。
- v4 的正文与 v3 差异集中在文首四段与两处用词，其余段落与 v3 一致（已逐句复核，未发现新的时序或归责变化）。
- 独立事实审稿（由作者、Lane B 或另一模型执行）尚未进行；本文件不构成事实通过，也不构成作者验收。
