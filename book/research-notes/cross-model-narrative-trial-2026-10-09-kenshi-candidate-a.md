> **试写候选 / Cross-model narrative trial — Kenshi（作者模型 A）。**
> 非正式书稿，非 canonical Profile。仅用于 2026-10-09 跨模型盲读比较，按 PR #292 任务书第 1 关产出。
> 事实基础：`cases/CASE-012-kenshi.md` 与 `evidence/CASE-012-kenshi-source-ledger.md`（PR #288 head `693b3de29b75f0c30e61c3cdbbdaebe16b72b583`）。原始访谈见文末。
> 正式 `book/profiles/`、`cases/`、`evidence/`、`claims/` 未改动。

---

# 一间酒吧，一把椅子，一场内战

Chris Hunt 的游戏里有一小队佣兵。他给他们的差事很简单：去镇上找一间酒吧。

代码里藏着一个几乎看不见的错误——佣兵有时会把一间普通民宅当成酒吧，推门进去，坐下来。屋主发现家里多了个陌生人，吓了一跳，抄起家伙就动手。镇上的守卫随后赶到，佣兵的同伙也卷了进来。转眼之间，整座小镇已经为一吧椅子打起了内战。

“模拟世界就是这样，纯粹是混乱。”这是 Hunt 后来讲起这件事时的说法。

Hunt 是 Kenshi 的作者，也是 Lo-Fi Games 的创始人。这游戏不太好归类：开放世界、小队控制、沙盒 RPG，没有主线，也没有任务清单。玩家扮演的不是天选之人，而是废土上一个谁都能欺负的普通人。他看不惯那些大厂 RPG 一开场就让你当英雄、什么都不用担心的做法——在他的世界里，你什么都不是，光活着就很难——你可能只是在城里歇脚，就被一场土匪袭击卷进去。那间被认错的房子，就是这个世界的日常。

## 一个人的系统

很长一段时间里，Kenshi 只有 Hunt 一个人在做。

他二十出头就在当游戏程序员，却受不了那些在他看来纯粹浪费时间的小成本捞钱项目，2008 年辞了职，全职做自己的游戏。钱从哪来？他晚上去做保安，挣最低工资，够糊口就行。前五六年就是这样过来的：白天一个人写游戏，夜里替别人看门。

他学做游戏其实算晚。多年后他在一次网上问答里回忆，自己直到十八岁左右才弄明白怎么真正做出一款游戏——那时他已经会编程，卡住他的是显示画面这类最基础的事。他入行那会儿，想做游戏只有一条路：先学会 C++，再自己拿零碎的东西拼出引擎。他把这些一个人熬出来的时间，大多花在了底层的系统上，而不是能看的画面上；用他的话说，比起玩游戏，他其实更喜欢造游戏。至于一个人怎么撑住，他的说法很朴素：这跟写一本书、拍一部片没什么两样，关键是能不能每天都接着做下去，而不觉得腻。

## 椅子与团队

一个连门牌都会认错的世界，终究不是一个人能一直攥在手里的。

Hunt 说，放手这件事他花了不少时间。团队里第一个程序员 Sam 会来问他下一个做什么，他脑子里的第一反应总是“不，这个我自己来，只有我知道它怎么运转”。可没过多久，他就对另一种感觉上了瘾——有人替他分担掉一部分工作。

Kenshi 的钱也是这么一步步来的。2013 年在 Steam 上线 Early Access 之前，他已经在自己网站上卖 alpha 版本，那笔钱够养活他本人，还能雇几个自由职业者搭把手；真正让他组起一个小团队的，是 Steam 的收入。接下来大约两年，他身边陆续出现了编程、世界设计、公关写作和美术的位置。

那间被当成酒吧的房子，就出现在这样一个世界里。它是 Hunt 口中“模拟世界的混乱”的一部分——他把它当作最大的麻烦来讲，而不是一个该被顺手修掉的错误。

---

## 来源（不属于正文）

1. **ESpalding / GameSkinny，2017-03-14**，`Behind the Scenes With the Developers of Kenshi`，受访者 Chris Hunt。
   正文用到的直接表述：`The biggest problem is the sheer chaos of a simulated world. For instance, a single mercenary in a town, looking for a bar. There was a tiny bug where they would sometimes pick a house instead of a bar, wander into this person’s house and sit down. Then the house owner freaks out at this intruder, attacks him, then the town guard gets involved, then the mercenary’s buddies get involved, and before you know it the whole town is having a civil war over a chair.`；`It took me a while to gradually release control of things, like our programmer Sam, would ask “what shall I work on next?” and everything I thought of I was like “No, I better do that myself, only I know how it works”. But pretty quickly I got addicted to the feeling of other people doing some of my work for me.`；`Back when I started the only way to make a game was to learn C++ and cobble your own engine together out of parts.`
   （Ledger 记 E003，核验状态 PARTIAL；2026-10-09 原访谈正文经 Wayback 快照 `20230816032008` 复核。）
2. **Chris Priestman / Siliconera，2015-08-30**，`Kenshi’s Eight Year Development Journey From One-Man RPG To A Team’s Success`，受访者 Chris Hunt。
   关键表述：`For the first five or six years, I worked alone on it full time whilst juggling a minimum wage security guard job during the nights to get by.`；`Before we got Greenlit in 2013, I was alpha funding it myself through my own website, which was enough to support myself and hire freelancers.`
   （Ledger 记 E001。）
3. **Lo-Fi Games，`Fact Sheet`**（机构历史页，无发布日）。`Chris Hunt, founder of Lo-Fi Games, spent his early 20s working as a game programmer but hated working on small cash-cow games… In 2008 he left, working on Kenshi full-time while working night shifts as a security guard to make just enough money to scrape by.`
   （Ledger 记 E002；2026-10-09 经 Wayback 快照 `20260903090101` 复核。）
4. **Chris Hunt（Reddit 账号 Captain_Deathbeard）/ r/IAmA，2019-08-08**，关于约十八岁才弄明白怎么做游戏、此前已会编程的回复。
   （Ledger 记 E007，核验状态 PARTIAL，属多年后回忆。）

## 有意舍弃的材料及原因

- **2017 访谈里 Hunt 对玩家开局行为的描述**（跑出城打土匪、一秒被打趴、随后改变玩法）。它属于创作者对受众反应的说明，Ledger 明确记为非代表样本调查；且会拉长篇幅、把主线从“人”拉向“市场反应”，故舍弃。
- **售价、销量与奖项等商业成就**（`$29.99`、卖出百万份、TGS 获奖页）。与“人物与决策”的主题无直接关系，容易把文章滑向成功学，故舍弃。
- **逐年人员规模、EA 收入金额、夜班具体排班**。Ledger 将精确金额与逐年 headcount 列为 `UNKNOWN`；E004 的“两晚保安 + 五天开发”是他多年后的回忆、非审计口径，故只在“前五六年夜班维生”这一可核层级使用，不再细化。
- **续作计划（E008）与其“两年内发行”的估计**。属 2019 年的意向与预测，超出本篇时间范围，也未被后续履行事实核验，故不采用。
- **同名的 Reddit 提问者经历**（E007 已明确不属于 Hunt）。避免混入当事人传记。

## 最需事实核验的两处

1. **佣兵轶事的性质与归属。** 它出自 2017 年 Hunt 本人在 GameSkinny 访谈中的口述，是开发者用来说明“模拟世界 bug 如何连锁”的举例，并非可独立见证的现实城市冲突。需确认采访原文（部分可访问副本已丢失，本次依赖 Wayback 快照）并检查是否存在 Hunt 本人的其他版本，以免把开发者的示例读成真实事件记录。
2. **单人期的时间口径。** 本文“前五六年”取自 2015 年 Siliconera 口径（当时整体开发约八年）。2018 年多家媒体标题写作“一人十年”，与 E004/E006 的“六年 solo”相冲突。需按 Case/Ledger 复核，避免把后期媒体压缩口径倒写成“一个人做了十年”。
