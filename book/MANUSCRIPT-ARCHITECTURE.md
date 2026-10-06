# 《独立游戏英雄传说》书稿结构｜从资料库到人类读物

© 2026 洪荒行者。All Rights Reserved.

本文件定义公开书稿的三层结构。目标不是削弱研究后台，而是让普通读者不必先学习研究系统，仍然能从一套真实人生问题进入。

## 一、三层结构

### Layer 1 — Research Backend / 研究后台

目录：`cases/`、`evidence/`、`claims/`、`book/research-notes/`。

回答：

> 这件事到底发生过没有？证据是什么？还有什么不知道？

特点：
- 可审计；
- 可以重复；
- 允许枯燥；
- 明确 UNKNOWN；
- 为反例、边界和后续修正保留空间。

这里首先服务研究者、作者和机器。

### Layer 2 — Hero Profiles / 人物材料层

目录：`book/profiles/`。

回答：

> 这个人怎样一步步变成后来那个能做出异常作品的人？

Profile 以一个人 / 团队为单位，保留完整生命史和生产史。它不是最终书的章节单位，而是给章节提供经审计的“人物材料”。

Profile 可以被多个章节重复调用。例如 early id 同时可以服务：
- 目标怎样形成；
- 玩家怎样变成生产者；
- 技术窗口怎样被自己创造；
- 怎么在辞职前先获得证据；
- 成功以后组织为什么变难。

### Layer 3 — Human Chapters / 人类章节层

目录：`book/chapters/`。

回答：

> 如果我正处于某种人生处境，这些人的经历能让我看见什么？

章节不按 Case 编号，也不以“介绍某款游戏”为目标。

它从一个普通人真正会问的问题出发，横向调用多个 Profile，再把不同人生放在一起比较。

例如：

> “我不知道自己以后要做什么。”

这一章可以同时调用 Romero、Carmack、Tom Francis、Toby Fox、Peter Whalen 等人物，而不要求读者先知道他们属于哪个 Case。

## 二、读者默认路径

第一次进入仓库：

```text
README
→ START-HERE
→ chapters/
→ 感兴趣的人物 Profile
→ 想核事实时进入 Case / Evidence
```

禁止倒过来要求普通读者先学：
`P0 / P1 / S1 / S2`、`RESEARCHING`、Case ID、Claim ID。

这些仍然存在，但属于“展开更多”。

## 三、章节不是案例合集

坏章节：

> FTL 告诉我们 A。  
> Kenshi 告诉我们 B。  
> Rocket League 告诉我们 C。

好章节应该围绕一个真实矛盾推进：

> 你需要时间才能做自己的东西；  
> 但你又需要工作才能活下去。  
> 那么真实世界里，人究竟怎样买时间？

然后人物自然进入论证：
- Hunt 用夜班工资购买个人时间；
- Psyonix 用 work-for-hire 购买组织时间；
- FTL 用储蓄购买有限试验时间。

读者最后获得的不是“三个案例摘要”，而是一张更清晰的选择地图。

## 四、暂定 Part 结构

这不是最终出版目录，但作为当前写作顺序。

### Part I — 你不需要先知道自己要成为什么人

核心问题：
- 目标是发现的，还是做出来的？
- 兴趣什么时候只是娱乐，什么时候开始变成能力？
- 长期体验怎样形成比较能力与需求发现？
- 玩家、modder、评论者怎样跨过生产者门槛？

首章：
- [01 — 你不需要十八岁就知道自己要做什么](chapters/01-goals-are-made-not-found.md)

主要人物池：
early id、Gunpoint、Dream Quest、Undertale、Lethal Company、Roblox creator cluster。

### Part II — 先买时间，再谈梦想

核心问题：
- 没有融资时，谁替你支付试错时间？
- 工资、储蓄、服务业务、伴侣收入、众筹、Early Access 分别解决什么？
- 辞职什么时候是风险升级，什么时候只是仪式化勇敢？

人物池：
Kenshi、FTL、Rocket League、Stardew Valley、Hollow Knight、despelote。

### Part III — 失败是不是白费，要看它留下了什么

核心问题：
- 前作、废案、服务项目、原型留下了什么残值？
- 什么叫能力资本、组织记忆、市场知识？
- 为什么“坚持”不是充分解释？

人物池：
Rocket League、Bills Must Be Paid、R.E.P.O.、Landfall、Tarkov lineage。

### Part IV — 技术时代给你什么牌，你又能不能自己造牌

核心问题：
- 技术怎样真正扩散到普通开发者？
- Inherited / Recombined / Created Window 有什么区别？
- 为什么 Carmack 不是“赶上 PC 红利”，而是 frontier creator？
- 为什么新工具降低执行成本，不等于自动产生好选择？

人物池：
early id、Gunpoint、PLAYERUNKNOWN、Project Wingman、Manor Lords。

技术史背景链接：
`cross-industry/industrial-revolutions/`。

### Part V — 市场不是最后一步

核心问题：
- 玩家什么时候第一次真正进入生产系统？
- paid alpha、Early Access、demo、众筹、社区怎样改变项目寿命？
- 好产品为什么仍然可能死在市场接口上？

人物池：
Minecraft、Factorio、Kenshi、Bills Must Be Paid、Brigador、Among Us。

### Part VI — 第一次成功不是结局

核心问题：
- 钱真正买到的是什么？
- optionality 怎样改变第二作？
- 为什么成功后反而更容易出现组织、方向和治理问题？

人物池：
early id → Quake、Subset → Into the Breach、Minecraft、Among Us、Tom Francis 后续作品。

## 五、章节写作规则

每章都应尽量具备：

1. 一个普通人能在十秒内理解的人生问题；
2. 至少两个结构明显不同的人生样本；
3. 一处真正的反例 / 边界，不允许把结论写成万能建议；
4. 少量必要数字与历史条件；
5. 一张“选择地图”，而不是一串成功秘诀；
6. 文末再提供“继续读人物 / 核证据”链接。

章节正文尽量避免：
- Case ID；
- Claim ID；
- Evidence 等级；
- “当前研究状态”；
- 大段研究方法说明；
- 把每个人压成一句 transferable lesson。

## 六、什么叫“人生性价比”

这里不是算一个公式，也不是寻找稳赚路线。

本书所谓更好的选择，是尽量提高：

> **可学习性 + 可回撤性 + 可积累残值 + 真实反馈速度**

同时降低：

> **不可逆成本 + 在错误方向上持续太久的概率**

但任何跨案例判断都必须由研究后台支撑；书稿只把它翻译成人能使用的语言，不把作者偏好伪装成统计定律。

## 七、当前出版优先级

1. 先写 3–4 篇真正的跨案例章节，验证“普通人问题 → 多人物比较”的阅读形式。
2. Profile 继续作为人物材料层补全，不追求每个 Case 都有 Profile。
3. 每新增一个 Profile，都至少回答它能服务哪一章，而不是为了“41 Case → 41 Profile”机械补齐。
4. 根 README 和 START-HERE 始终优先把普通读者送入章节层。
5. 研究后台的严谨度不为可读性让步；可读性由分层解决。
