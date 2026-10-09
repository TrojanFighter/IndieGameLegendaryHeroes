> **试写候选 v2（修订稿）/ Cross-model narrative trial — Kenshi（作者模型 A）。**
> 非正式书稿，非 canonical Profile。与 v1 同事件实包，仅作编辑修订：拆掉两节相同的格言式起手；补回“公开销售之后”的真实摩擦（Early Access 稳定性压力、玩家不信任、引擎老化、长评论与 bug 清单、自压工资）；结尾不再替读者归纳意义。
> 事实基础：`cases/CASE-012-kenshi.md` 与 `evidence/CASE-012-kenshi-source-ledger.md`（PR #288 head `693b3de29b75f0c30e61c3cdbbdaebe16b72b583`）。原始访谈见文末。
> 正式 `book/profiles/`、`cases/`、`evidence/`、`claims/` 未改动。

---

# 一间酒吧，一把椅子，一场内战

Chris Hunt 的游戏里有一小队佣兵。他给他们的差事很简单：去镇上找一间酒吧。

代码里藏着一个几乎看不见的错误——佣兵有时会把一间普通民宅当成酒吧，推门进去，坐下来。屋主发现家里多了个陌生人，吓了一跳，抄起家伙就动手；镇上的守卫随后赶到，佣兵的同伙也卷了进来。转眼之间，整座小镇已经为一吧椅子打起了内战。

“模拟世界就是这样，纯粹是混乱。”Hunt 后来这样解释。

他是 Kenshi 的作者，也是 Lo-Fi Games 的创始人。这游戏不太好归类：开放世界、小队控制、沙盒 RPG，没有主线，没有任务清单。玩家扮演的不是天选之人，而是废土上一个谁都能欺负的普通人。他看不惯那些大厂 RPG 一开场就让你当英雄的做法——在他的世界里，你什么都不是，光活着就很难，可能只是在城里歇脚，就被一场土匪袭击卷进去。那间被认错的房子，就是这个世界的日常。

## 一个人的系统

Kenshi 的前五六年，只有 Hunt 一个人在做。白天他把时间给游戏，到了夜里，他去做保安，挣最低工资，够糊口就行。

再往前，他二十出头就在当游戏程序员，却受不了那些在他看来纯粹浪费时间的小成本捞钱项目，2008 年辞了职，全职做自己的游戏。他学做游戏其实算晚。多年后他在一次网上问答里回忆，自己直到十八岁左右才弄明白怎么真正做出一款游戏——那时他已经会编程，卡住他的是显示画面这类最基础的事。他入行那会儿，想做游戏只有一条路：先学会 C++，再自己拿零碎的东西拼出引擎。他把这些一个人熬出来的时间，大多花在了底层的系统上，而不是能看的画面上；用他的话说，比起玩游戏，他其实更喜欢造游戏。

## 放手

第一个进来的程序员叫 Sam。他会来问 Hunt 下一个做什么，而 Hunt 的第一反应总是“不，这个我自己来，只有我知道它怎么运转”。他花了不少时间才学会把东西交出去；但很快，让别人替他分担一部分工作，就成了他上瘾的感觉。

钱是按这个顺序来的。2013 年在 Steam 上线 Early Access 之前，他已经在自己网站上卖 alpha 版本，那笔钱够养活他本人，还能雇几个自由职业者搭把手；真正让他组起一个小团队的，是 Steam 的收入。接下来大约两年，他身边陆续出现了编程、世界设计、公关写作和美术的位置。

麻烦也跟着来了。把游戏挂上去卖，等于答应它会一直能玩——可游戏里的佣兵还在到处认错门牌。Hunt 说，Early Access 最难的地方正在这里：一边往里加东西，一边得保证已经付钱的人手上那个版本稳定、能玩。更新一旦间隔久了，玩家就开始怀疑他是不是也跑了；那几年确实有不少 Early Access 的游戏半路消失，让他这样的人更难被信任。引擎也越来越旧，升级一次要反复打补丁，真想往前走就得大改。长长的 bug 清单、成千上万条评论，有时压得他不想看；可他也说，恰恰是那些骂得很凶的反馈里，偶尔藏着真正该修的东西。

团队来了，钱也来了。但他说，自己那份工资，还是一直压得很低。

---

## 来源（不属于正文）

1. **ESpalding / GameSkinny，2017-03-14**，`Behind the Scenes With the Developers of Kenshi`，受访者 Chris Hunt（Ledger E003）。
   佣兵轶事：`The biggest problem is the sheer chaos of a simulated world. For instance, a single mercenary in a town, looking for a bar. There was a tiny bug where they would sometimes pick a house instead of a bar, wander into this person’s house and sit down. Then the house owner freaks out at this intruder, attacks him, then the town guard gets involved, then the mercenary’s buddies get involved, and before you know it the whole town is having a civil war over a chair.`
   放手回忆：`It took me a while to gradually release control of things, like our programmer Sam, would ask “what shall I work on next?” and everything I thought of I was like “No, I better do that myself, only I know how it works”. But pretty quickly I got addicted to the feeling of other people doing some of my work for me.`
   引擎：`Back when I started the only way to make a game was to learn C++ and cobble your own engine together out of parts.`
   玩家不信任：`Over the years other alpha-funded games have gone under or been abandoned which has made players more distrustful, which puts more pressure on the rest of us.`
2. **Chris Priestman / Siliconera，2015-08-30**，`Kenshi’s Eight Year Development Journey From One-Man RPG To A Team’s Success`，受访者 Chris Hunt（Ledger E001）。
   `For the first five or six years, I worked alone on it full time whilst juggling a minimum wage security guard job during the nights to get by.`；`Before we got Greenlit in 2013, I was alpha funding it myself through my own website, which was enough to support myself and hire freelancers.`；`The only difficulty of Early Access is that we have to work under more pressure to keep the game steady and playable for the players while we work.`；`I even enjoy creating Kenshi more than I enjoy playing games themselves.`
3. **Lo-Fi Games，`Fact Sheet`**（机构历史页，无发布日）（Ledger E002）。`Chris Hunt, founder of Lo-Fi Games, spent his early 20s working as a game programmer but hated working on small cash-cow games… In 2008 he left, working on Kenshi full-time while working night shifts as a security guard to make just enough money to scrape by.`
4. **徳岡正肇 / 4Gamer，2018-09-26**，TGS 2018 访谈（Ledger E004）。Hunt 述：前期每周两晚保安、五天开发；并称自己保持最低薪水、经历过困难时期。（回忆口径，非审计日程/薪资。）
5. **Natalie Clayton / PC Games Insider，2018-12-06**，`How Kenshi survived Steam Greenlight and over a decade in development`（Ledger E005）。更新间隔期与“其他 Early Access 游戏被放弃”之后的玩家不信任；反复引擎升级、更深改进需大重写。
6. **一條貴彰 / Business 4Gamer，2018-10-02**（Ledger E006）。公开前偶尔抽一周休息、公开后持续忙碌；长长的 bug 清单与数千条评论可能令人气馁，但愤怒的 bug 反馈里也有有用原因。属其自述，非调查情绪或工时。
7. **Chris Hunt（Reddit 账号 Captain_Deathbeard）/ r/IAmA，2019-08-08**（Ledger E007）。约十八岁才弄明白怎么做游戏、此前已会编程；多年后回忆。

## 有意舍弃的材料及原因

- **2017 访谈里 Hunt 对玩家开局行为的描述**（跑出城打土匪、一秒被打趴）。属创作者对受众反应的说明，Ledger 记为非代表样本调查，且会把主线从“人”拉向“市场反应”，故舍弃。
- **售价、销量与奖项等商业成就**（`$29.99`、卖出百万份、TGS 获奖页）。与“人物与决策”主题无直接关系，容易滑向成功学。
- **逐年人员规模、EA 收入金额、夜班精确排班**。Ledger 将精确金额与逐年 headcount 列为 `UNKNOWN`；E004 的“两晚保安 + 五天开发”属多年后回忆、非审计口径，故不细化。
- **续作计划（E008）及其“两年内发行”估计**。属 2019 年意向与预测，超出本篇时间范围，未被后续履行事实核验。
- **同名的 Reddit 提问者经历**（E007 已明确不属于 Hunt）。

## 最需事实核验的两处

1. **佣兵轶事的性质与归属。** 出自 2017 年 Hunt 本人在 GameSkinny 访谈中的口述，是开发者用来说明“模拟世界 bug 如何连锁”的举例，并非可独立见证的现实城市冲突。部分可访问副本已失效，本次依赖 Wayback 快照；需确认是否存在 Hunt 本人的其他版本。
2. **单人期与“自压工资”的口径。** “前五六年”取自 2015 年 Siliconera 口径（当时整体约八年）；2018 年多家媒体标题写作“一人十年”，与 E004/E006 的“六年 solo”冲突，需防倒写。结尾“自己那份工资一直压得很低”取自 2018 年 TGS 采访的回忆陈述，**无公开薪资数字**，不得补具体金额或与其他年份比较。
