> **试写候选 v3（漂移修正稿）/ Cross-model narrative trial — Kenshi（作者模型 A）。**
> 非正式书稿，非 canonical Profile。针对 PR #294 `book/EDITORIAL-CROSS-MODEL-ROLLOUT-2026-10-09.md` §1 / §6 对 A v2 指出的风险逐条修正：口述 bug 被添入动作／时间细节；Hunt 视混乱为“最大问题”的态度可能在翻译中被改变；bug 时点；薪水时间范围。v1、v2 原样保留，不覆盖。
> 事实基础同前：`cases/CASE-012-kenshi.md`、`evidence/CASE-012-kenshi-source-ledger.md`（PR #288 head `693b3de29b75f0c30e61c3cdbbdaebe16b72b583`）。
> **这是 writer 自我修正，不替代独立事实审稿；不得据此宣称漂移已全部修复或通过。** 正式 `book/profiles/`、`cases/`、`evidence/`、`claims/` 未改动。

---

# 一间酒吧，一把椅子，一场内战

Chris Hunt 的游戏里有一小队佣兵。他给他们的差事很简单：去镇上找一间酒吧。

代码里有个很小的错误：佣兵有时会把一间民宅当成酒吧，走进去，坐下。屋主因为家里闯进个生人而发作，动手打他；城里的守卫被牵扯进来，佣兵的同伙也被牵扯进来——不知不觉，整座小镇就为一吧椅子打起了内战。

Hunt 说，这就是开发 Kenshi 时最大的问题：模拟世界带来的、那种纯粹的混乱。

他是 Kenshi 的作者，也是 Lo-Fi Games 的创始人。这游戏不太好归类：开放世界、小队控制、沙盒 RPG，没有主线，没有任务清单。玩家扮演的不是天选之人，而是废土上一个谁都能欺负的普通人。他看不惯那些大厂 RPG 一开场就让你当英雄的做法——在他的世界里，你什么都不是，光活着就很难，可能只是在城里歇脚，就被卷进一场土匪袭击。那间被认错的房子，就属于这个世界。

## 一个人的系统

Kenshi 的前五六年，只有 Hunt 一个人在做。白天他把时间给游戏，到了夜里，他去做保安，挣最低工资，够糊口就行。

再往前，他二十出头就在当游戏程序员，却受不了那些在他看来纯粹浪费时间的小成本捞钱项目，2008 年辞了职，全职做自己的游戏。他学做游戏其实算晚。多年后他在一次网上问答里回忆，自己直到十八岁左右才弄明白怎么真正做出一款游戏——那时他已经会编程，卡住他的是显示画面这类最基础的事。他入行那会儿，想做游戏只有一条路：先学会 C++，再自己拿零碎的东西拼出引擎。他把这些一个人熬出来的时间，大多花在了底层的系统上，而不是能看的画面上；用他的话说，比起玩游戏，他其实更喜欢造游戏。

## 放手

第一个进来的程序员叫 Sam。他会来问 Hunt 下一个做什么，而 Hunt 的第一反应总是“不，这个我自己来，只有我知道它怎么运转”。他花了不少时间才学会把东西交出去；但很快，让别人替他分担一部分工作，就成了他上瘾的感觉。

钱是按这个顺序来的。2013 年通过 Steam Greenlight 之前，他已经在自己网站上卖 alpha 版本，那笔钱够养活他本人，还能雇几个自由职业者搭把手；真正让他组起一个小团队的，是 Steam 的收入。接下来大约两年，他身边陆续出现了编程、世界设计、公关写作和美术的位置。

麻烦也跟着来了。把游戏挂上去卖，等于答应它会一直能玩。Hunt 说，Early Access 最难的地方正在这里：一边往里加东西，一边得保证已经付钱的人手上那个版本稳定、能玩。更新一旦间隔久了，玩家就开始怀疑他是不是也跑了；那时候确实有不少 Early Access 的游戏半路消失，让他这样的人更难被信任。引擎也越来越旧，升级一次要反复打补丁，真想往前走就得大改。长长的 bug 清单、成千上万条评论，有时会让人泄气；可他也说，恰恰是那些骂得很凶的反馈里，偶尔藏着真正该修的东西。

团队来了，钱也来了。但在 2018 年那次采访里，他说自己给自己开的工资，还是很少。

---

## 对 v2 的修正记录（不属于正文）

| 处 | v2 写法 | v3 处理 | 依据 |
| --- | --- | --- | --- |
| 开场动作 | “推门进去”“吓了一跳”“抄起家伙就动手”“随后赶到” | 贴回原文动词链：走进去、坐下；屋主发作、动手打他；守卫与同伙被牵扯进来 | E003 原文只有 `wander into … and sit down` / `freaks out at this intruder` / `attacks him` / `gets involved`，无门、无武器、无“赶到” |
| Hunt 立场 | 轶事被组织成轻快开场，删去了“最大的问题”交代 | 正文明确：这是开发 Kenshi 时最大的问题，即模拟世界的混乱 | E003：`The biggest problem is the sheer chaos of a simulated world.` |
| bug 时点 | “把游戏挂上去卖……可游戏里的佣兵还在到处认错门牌”（暗示 EA 期间仍在发生） | 删除该暗示 | E003 未给时点，属一般性举例（`sometimes`） |
| Greenlight / EA | “2013 年在 Steam 上线 Early Access 之前” | “2013 年通过 Steam Greenlight 之前” | E001 锚点为 `Before we got Greenlit in 2013`；CASE-012 要求 Greenlight 与 EA 分开 |
| bug 清单 | “有时压得他不想看”（具体心理） | “有时会让人泄气” | E006：`could be discouraging`，未描述其具体反应 |
| 薪水范围 | “自己那份工资，还是一直压得很低” | “在 2018 年那次采访里，他说自己给自己开的工资，还是很少” | E004 为采访期陈述（`keeping his own salary minimal`），无“一直”依据 |

## 来源（不属于正文）

1. **ESpalding / GameSkinny，2017-03-14**（Ledger E003）：佣兵轶事原文（见上表依据）；放手回忆 `It took me a while to gradually release control of things, like our programmer Sam…`；引擎 `Back when I started the only way to make a game was to learn C++…`；玩家不信任 `Over the years other alpha-funded games have gone under or been abandoned which has made players more distrustful…`。
2. **Chris Priestman / Siliconera，2015-08-30**（Ledger E001）：`For the first five or six years, I worked alone on it full time whilst juggling a minimum wage security guard job during the nights to get by.`；`Before we got Greenlit in 2013, I was alpha funding it myself through my own website…`；`The only difficulty of Early Access is that we have to work under more pressure to keep the game steady and playable…`；`I even enjoy creating Kenshi more than I enjoy playing games themselves.`
3. **Lo-Fi Games，`Fact Sheet`**（Ledger E002）：`spent his early 20s working as a game programmer but hated working on small cash-cow games… In 2008 he left, working on Kenshi full-time while working night shifts as a security guard…`
4. **徳岡正肇 / 4Gamer，2018-09-26**（Ledger E004）：前期每周两晚保安、五天开发；并述自己保持最低薪水、经历困难时期（回忆口径，无薪资数字）。
5. **Natalie Clayton / PC Games Insider，2018-12-06**（Ledger E005）：更新间隔期与“其他 Early Access 游戏被放弃”之后的玩家不信任；反复引擎升级、更深改进需大重写。
6. **一條貴彰 / Business 4Gamer，2018-10-02**（Ledger E006）：公开后持续忙碌；长长的 bug 清单与数千条评论可能令人气馁，但愤怒的 bug 反馈里也有有用原因。
7. **Chris Hunt / r/IAmA，2019-08-08**（Ledger E007）：约十八岁才弄明白怎么做游戏、此前已会编程。

## 有意舍弃的材料及原因

- 2017 访谈里 Hunt 对玩家开局行为的描述（属创作者对受众的说明、非代表样本）。
- 售价、销量与奖项等商业成就（易滑向成功学，与“人物与决策”无关）。
- 逐年人员规模、EA 收入金额、夜班精确排班（`UNKNOWN`）。
- 2019 续作计划与其“两年内发行”估计（超出时间范围，未核）。
- 同名 Reddit 提问者经历（E007 已明确不属于 Hunt）。
- **v3 新增舍弃：** 一切原文未给的场景与动作润色（“推门”“抄起家伙”“赶到”等），宁可使句子更素，也不补写。

## 最需事实核验的三处

1. **佣兵轶事的性质与归属**：2017 年 Hunt 口述的游戏内 bug 示例，非现实事件；需独立核对原文（部分副本失效，本次依赖 Wayback 快照）。
2. **单人期口径**：本文取 2015 年“前五六年”；2018 年媒体标题“一人十年”与 E004/E006 的“六年 solo”冲突，需防倒写。
3. **薪水表述**：E004 的“自压工资”属 2018 年采访期回忆，**无公开金额与年份范围**；v3 已限定为“2018 年那次采访”，仍待独立审稿确认无过度概括。
