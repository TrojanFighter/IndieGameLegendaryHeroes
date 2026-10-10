> **试写候选 v5（窄修稿）/ Cross-model narrative trial — Kenshi（作者模型 A）。**
> 非正式书稿，非 canonical Profile。v1 / v2 / v3 / v4 原样保留，不覆盖。
> 本稿回应 PR #333 的独立审阅结论 `REVISE_AGAIN（窄修）`：不重写结构与风格，只做四项窄修，并恢复两处**已由原始采访证实、被 v4 因依赖 ledger 摘要而误删**的人物信息（同 PR 的 Lane B commit 已先把这两节点补进 E001）。
> 事实基础：`cases/CASE-012-kenshi.md`、`evidence/CASE-012-kenshi-source-ledger.md` @ `main`（本分支已补录 E001 的 design-intent 与 team-roster 节点）。
> **这是 writer 自我修正，不替代独立 fact-checker；不得据此宣称漂移已全部修复或通过。** 正式 `book/profiles/`、`cases/`、`claims/` 未改动。

---

# 一间酒吧，一把椅子，一场内战

2017 年，Chris Hunt 在一次访谈里举过一个例子：镇上一个佣兵正找酒吧。

可代码里有个很小的错误：佣兵有时会把民宅当成酒吧，走进去，坐下。屋主因为家里闯进个生人而发作，动手打他；守卫被牵扯进来，佣兵的同伙也被牵扯进来——不知不觉，整座小镇就为了一把椅子打起了内战。

Hunt 说，这就是开发 Kenshi 时最大的问题：模拟世界带来的那种纯粹的混乱。

他是 Kenshi 的作者，也是 Lo-Fi Games 的创始人。这游戏不太好归类：开放世界、小队控制、沙盒 RPG，没有主线，没有任务清单。他说自己一直不喜欢许多大型 RPG 的照顾：一开局就是英雄，从一开始就很强，什么都不用怕。在 Kenshi 里，玩家开始时只是个普通的弱者，没有特殊能力，属性也不高，什么都不是，连活下去都不容易；可能只是在城里歇脚，就被卷进一场土匪袭击。那间被认错的房子，就属于这个世界。

## 一个人的系统

Kenshi 的前五六年，只有 Hunt 一个人在做。白天他把时间给游戏，到了夜里，他去做保安，挣最低工资，够糊口就行。

再往前，他二十出头就在当游戏程序员，却受不了那些小成本捞钱的项目，2008 年辞了职，全职做自己的游戏。他学做游戏其实算晚。多年后他在一次网上问答里回忆，自己直到十八岁左右才弄明白怎么真正做出一款游戏——那时他已经会编程，卡住他的是显示画面这类最基础的事。按他 2017 年回顾自己起步年代的说法，那时想做游戏只有一条路：先学会 C++，再自己拿零碎的东西拼出引擎。他把这些一个人熬出来的时间，大多花在了底层系统和让它能玩起来上；用他的话说，比起玩游戏，他其实更喜欢造游戏。

## 放手

团队的第一位程序员是 Sam。他会来问 Hunt 下一个做什么，而 Hunt 的第一反应总是“不，这个我自己来，只有我知道它怎么运转”。他花了不少时间才学会把东西交出去；但很快，让别人替他分担一部分工作，就成了他上瘾的感觉。

钱是按这个顺序来的。2013 年通过 Steam Greenlight 之前，他已经在自己网站上卖 alpha 版本，那笔钱够养活他本人，还能雇几个自由职业者搭把手；真正让他组起一个小团队的，是 Steam 的收入。接下来大约两年，他身边陆续出现了编程、世界设计、公关写作和美术的位置。

麻烦也跟着来了。把游戏挂上去卖，等于答应它会一直能玩。Hunt 说，Early Access 最难的地方正在这里：一边往里加东西，一边得保证已经付钱的人手上那个版本稳定、能玩。更新一旦间隔久了，玩家就更难信任他；那几年确实有不少靠 alpha 集资的游戏半路消失，Hunt 说这让剩下的人承受了更多压力。引擎也越来越旧，升级一次要反复打补丁，真想往前走就得大改。长长的 bug 清单、成千上万条评论，有时会让人泄气；可他也说，恰恰是那些骂得很凶的反馈里，偶尔藏着真正该修的东西。

团队来了，钱也来了。但在 2018 年那次采访里，他说自己给自己开的工资，还是很少。

---

## v5 相对 v4 的修改记录（不属于正文）

审阅要求四项窄修 + 两项恢复。逐条如下。

| # | v4 写法 | v5 处理 | 依据 |
| --- | --- | --- | --- |
| 1 | 删除“他看不惯那些大厂 RPG 一开场就让你当英雄的做法”，理由是 E001 摘要未记 | **恢复**，并按原话重写：“他说自己一直不喜欢许多大型 RPG 的照顾：一开局就是英雄，从一开始就很强，什么都不用怕。” | E001（本分支已补录）：`I've never liked the hand-holding that most of the big RPGs give the player where you'll start off a hero, strong from the very beginning, nothing to fear.` 原文说的是 **most of the big RPGs**（类型与体量），不是“大厂”（公司大小），故不沿用 v3/v4 之前的“大厂”措辞 |
| 2 | “团队里的程序员叫 Sam” | **恢复为**“团队的第一位程序员是 Sam” | E001：`During the last two years I've managed to grow a small team – Sam, our first programmer; …`。这是**岗位排序**，不代表 Sam 是团队第一位成员或第一位雇员，正文不作此延伸 |
| 3 | “一个佣兵走进镇子，要找一间酒吧” | “镇上一个佣兵正找酒吧” | 2017 GameSkinny 原文为 `a single mercenary in a town, looking for a bar`，没有进入镇子的动作；避免额外的运动镜头 |
| 4 | “他入行那会儿，想做游戏只有一条路……” | “按他 2017 年回顾自己起步年代的说法，那时想做游戏只有一条路……” | 这是 Hunt 2017 年对自己入行年代的回顾，不是该时代独立游戏业的客观普遍断言 |

其余段落与 v4 一致，未改结构、未改风格、未增加第三个案例。

## Fidelity Readback（v5 对 canonical 来源逐项回读）

按 [EDITORIAL-REWRITE-PROTOCOL §3](../../book/EDITORIAL-REWRITE-PROTOCOL.md)，并采纳本轮审阅新增的一类检查。

| 不可偷换项 | v5 的处理 | 判定 |
| --- | --- | --- |
| **Actor / credit** | 佣兵事件标明是 Hunt 访谈中的举例；“第一位程序员”限定为岗位排序；收入阶段区分本人 / freelancers / 团队 | `PRESERVED` |
| **Chronology / knowledge at the time** | 前五六年 solo（E001 2015 口径）；2008 年离职（E002）；Greenlight 前自营 alpha（E001）；Steam EA 后组队（E001/E002）；低薪限定 2018（E004）；“只有一条路”标明为 2017 年回顾 | `PRESERVED` |
| **Negation / modality** | “有时会把民宅当成酒吧”保留 `sometimes`；“他说自己一直不喜欢”对应 `I've never liked`；“据说/他回忆”保持在句内 | `PRESERVED` |
| **Causation / alternative** | 不写“因为 Steam 才有玩家收入”；玩家不信任写成 Hunt 的说法而非因果结论 | `PRESERVED` |
| **Numbers / denominators** | 全篇无金额、销量、headcount 数字；低薪只说“很少” | `PRESERVED` |
| **Evidence boundary** | 佣兵事件性质、单人期口径、薪水口径保留在文末《仍待独立核实》 | `PRESERVED` |
| **Historical regime** | 不把 2013 Greenlight / EA 窗口当作今天可复制的路径 | `N/A（本稿未作可迁移主张）` |
| **Quote / 著作权** | 正文两处中文引语均对应 E001/E003 原句；英文长篇只留在文末来源区 | `PRESERVED` |
| **Recall / 同期** | “十八岁”明确写为“多年后在一次网上问答里回忆”（E007 2019）；“更喜欢造游戏”归 E001（2015） | `PRESERVED` |
| **UNKNOWN** | 家庭与住房、储蓄、夜班排班、逐年 headcount、EA 收入金额、完整协作者边界，均未写 | `PRESERVED` |
| **Documented voice（本轮新增检查项）** | v4 曾因只核 ledger 摘要而删掉两处**有原始证词**的人物信息；v5 已恢复，且两条已由 Lane B 补进 E001 并附边界 | `FIXED` |

**本轮新增的检查规则**（执行既有 source-first 约束，不新增 Gate）：Fidelity Readback 除查 **invented detail（凭空添加）**，还需查 **documented voice accidentally deleted（有史料却因账本摘要遗漏而被误删）**。判据不是“账本里有没有”，而是“原始来源里有没有”。

## 来源（不属于正文）

1. **Chris Priestman / Siliconera，2015-08-30**（Ledger E001）：
   - 单人期与收入顺序：`For the first five or six years, I worked alone on it full time whilst juggling a minimum wage security guard job during the nights to get by.`；`Before we got Greenlit in 2013, I was alpha funding it myself through my own website, which was enough to support myself and hire freelancers. Steam Early Access, however, has given me the funding I need to get a team together and make progress.`；`The only difficulty of Early Access is that we have to work under more pressure to keep the game steady and playable for the players while we work.`；`I even enjoy creating Kenshi more than I enjoy playing games themselves.`
   - 设计立场：`I've never liked the hand-holding that most of the big RPGs give the player where you'll start off a hero, strong from the very beginning, nothing to fear. In Kenshi you start out as a normal runt with no special powers, no higher stats. You are not special, you are nothing, and even survival itself is a struggle.`（答“Kenshi 的核心概念是什么”）
   - 2015 年团队名单：`During the last two years I've managed to grow a small team – Sam, our first programmer; Oli, our world designer; Natalie, our PR contact & writer; Otto, our 3D & concept designer; and Maykol, our second programmer.`
2. **ESpalding / GameSkinny，2017-03-14**（Ledger E003）：佣兵轶事 `The biggest problem is the sheer chaos of a simulated world. For instance, a single mercenary in a town, looking for a bar. There was a tiny bug where they would sometimes pick a house instead of a bar, wander into this person's house and sit down. Then the house owner freaks out at this intruder, attacks him, then the town guard gets involved, then the mercenary's buddies get involved, and before you know it the whole town is having a civil war over a chair.`；放手 `It took me a while to gradually release control of things, like our programmer Sam, would ask "what shall I work on next?" and everything I thought of I was like "No, I better do that myself, only I know how it works". But pretty quickly I got addicted to the feeling of other people doing some of my work for me.`；引擎与起步年代 `Back when I started the only way to make a game was to learn C++ and cobble your own engine together out of parts.`；玩家不信任 `Over the years other alpha-funded games have gone under or been abandoned which has made players more distrustful, which puts more pressure on the rest of us.`
3. **Lo-Fi Games，`Fact Sheet`**（机构历史页，无发布日）（Ledger E002）：`Chris Hunt, founder of Lo-Fi Games, spent his early 20s working as a game programmer but hated working on small cash-cow games… In 2008 he left, working on Kenshi full-time while working night shifts as a security guard to make just enough money to scrape by.`
4. **徳岡正肇 / 4Gamer，2018-09-26**（Ledger E004）：前期每周两晚保安、五天开发；四名核心成员与两位自由职业者；自称保持最低薪水、经历困难时期。（回忆口径，无薪资数字。）
5. **Natalie Clayton / PC Games Insider，2018-12-06**（Ledger E005）：更新间隔期与其他 Early Access 游戏被放弃之后的玩家不信任；反复引擎升级、更深改进需大重写。
6. **一條貴彰 / Business 4Gamer，2018-10-02**（Ledger E006）：公开后持续忙碌；长长的 bug 清单与数千条评论可能令人气馁，但愤怒的 bug 反馈里也有有用原因。
7. **Chris Hunt（Reddit 账号 Captain_Deathbeard）/ r/IAmA，2019-08-08**（Ledger E007）：约十八岁才弄明白怎么做游戏、此前已会编程。

**口径提示：** E001（2015）列出的五名团队成员与 E004（2018）的四名核心成员不是同一时点的名单，正文只用其中“第一位程序员”这一岗位排序，未列人数。

## 有意舍弃的材料及原因

- 2017 访谈里 Hunt 对玩家开局行为的描述（属创作者对受众的说明、非代表样本）。
- 售价、销量与奖项等商业成就（易滑向成功学，与“人物与决策”无关）。
- 逐年人员规模、EA 收入金额、夜班精确排班（`UNKNOWN`）。
- 2019 续作计划与其“两年内发行”估计（超出时间范围，未核）。
- 同名 Reddit 提问者经历（E007 已明确不属于 Hunt）。
- 一切原文未给的场景与动作润色（“推门”“抄起家伙”“赶到”“走进镇子”等）。

## 仍待独立核实

1. **佣兵轶事的性质与归属**：2017 年 Hunt 口述的游戏内 bug 示例，非现实事件；部分副本失效，本次依赖 Wayback 快照，需确认是否存在 Hunt 本人的其他版本。
2. **单人期口径**：本稿取 2015 年“前五六年”；2018 年媒体标题的“一人十年”与 E004/E006 的“六年 solo”冲突，已避免倒写。
3. **薪水表述**：E004 的“自压工资”属 2018 年采访期回忆，无公开金额与年份范围。

## 与 v1–v4 的关系与版本保留

- v1 / v2 / v3 / v4 原样保留，本稿不覆盖它们。
- v5 相对 v4 的改动集中在文首四段与三处用词（见修改记录表），其余段落未动。
- 本分支的 Lane B commit 已把两处被误删的节点补进 `evidence/CASE-012-kenshi-source-ledger.md` 的 E001，并附归属与边界；正文据此恢复。
- 独立事实审稿（作者、Lane B 或另一模型执行）尚未对 v5 进行；本文件不构成事实通过，也不构成作者验收。
- 另需注意（审阅已指出，非本稿可解）：本候选更像**可作为章节开头的紧凑人物特写**，尚不覆盖正式 `book/profiles/kenshi.md` 的完整人生跨度；是否开发为完整传记，另属 Lane C 与作者决策。
