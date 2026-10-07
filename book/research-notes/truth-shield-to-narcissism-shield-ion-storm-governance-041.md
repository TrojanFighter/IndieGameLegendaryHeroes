# 041 — “真理之盾”什么时候变成“自恋之盾”：early id → Quake → Ion Storm 的判断、规模与反馈完整性

- **Status:** RESEARCH NOTE / LONGITUDINAL GOVERNANCE PRESSURE TEST / PRE-CLAIM / 2026-10-08
- **Parent:** [040 战略性不忠诚 / 美国个人主义](early-id-strategic-disloyalty-american-individualism-040.md) · [Masters of Doom longitudinal 001](masters-of-doom-longitudinal-master-study-001.md)
- **Question:** 同样的“相信自己的判断、切掉旧约束、追求下一阶段最好的东西”，为什么在 early id 1990–1993 是优势，而到 Quake / Ion Storm Dallas 可能反噬？怎样区分 **truth shield** 与 **narcissism shield**？
- **Core boundary:** 本笔记**不诊断John Romero有临床自恋人格**。“自恋之盾”只作为读者层隐喻，后台对应可观测变量：`FEEDBACK_INTEGRITY`、`SCALE_DISCONTINUITY`、`COMPLEMENT_DEPENDENCE`、`DECISION_RIGHT_ACCOUNTABILITY`、`SUCCESS_FORMULA_TRANSFER_ERROR`。
- **Internal control:** Ion Storm Austin / Deus Ex 是最重要的同公司反例：同样获得巨大创作自主，但保留清晰项目负责人、局部团队连续性、后期砍范围和publisher延长期，最终完成优秀产品。故“自由/设计师主导”本身不是Dallas失败的充分原因。

## 0. 结论先行：Romero 2023自己给出了最重要的解释

GamesBeat 2023长访谈中，Romero直接回看Ion Storm：

- 他承认在id有“很多运气”；
- 自己假设能在Ion Storm继续采用在id时的做法；
- 但“整个formula已经完全变了”，**自己没有改变做法**；
- 很多事情其实需要变化，而当时不知道自己需要学什么；
- 他将Warren Spector/Harvey Smith团队做出Deus Ex视为Ion Storm最重要的救赎之一。

Source: https://gamesbeat.com/making-doom-and-building-the-fps-industry-at-100-miles-per-hour-john-romero-interview/

因此最强解释不是“成功让Romero人格腐化”，而是：

> **他把一个在小团队、内部能力极强、反馈极快环境中有效的操作系统，错误迁移到一个规模、依赖、资本结构和治理完全不同的组织。**

定义 `SUCCESS_FORMULA_TRANSFER_ERROR`：
[
	ext{Past success heuristic} + 	ext{new environment} - 	ext{environmental recalibration}
ightarrow 	ext{systematic overconfidence}
]

这与中国研究中的 `Success-Path Version Lock` 可以连线，但人物层必须保留Romero自己的反思和Ion Storm内部反例。

## 1. early id 的“真理之盾”为什么更容易得到现实校正

### 1.1 小团队：判断错误很快撞上作品本身

early id核心团队人数少、项目周期短、创始人直接写代码/做关卡/画图/测试，玩家通过shareware直接给销售与口碑反馈。

这意味着：
- `judgement latency`短；
- 设计争执很快变成build；
- 技术上不可能的想法会被Carmack的现实约束迅速暴露；
- 不好玩的内容被团队自己反复deathmatch/试玩暴露；
- 市场不买单会较快出现在订单上。

**个人自信没有脱离反馈，而是包在一个很硬的反馈回路里。**

### 1.2 Romero与Carmack不是两个独立天才，而可能是一个互相校正系统

本研究暂设H：
- Carmack提供`TECHNICAL REALITY CHECK`：什么现在可实现、性能边界、技术窗口；
- Romero提供`PLAYER/PRODUCT REALITY CHECK`：什么值得做、什么有冲击力、玩家如何体验；
- Hall/Adrian/Cloud等进一步提供设计、美术与生产反压力。

所以early id的强不是“几个极端人物互不妥协”，而是**极端判断在同一房间里高频互相碰撞**。

待证：每个具体争议需人物一手/同期开发记录，不能凭角色标签把Carmack=技术理性、Romero=玩家直觉固定化。

## 2. Quake 已经出现第一个预警：追求“每件事都要更好”不等于选择了最优项目方向

2023 Doom 30周年Carmack/Romero联合回顾中，Carmack承认：
- Quake有几种不同可能路线；
- 团队“probably did not pick the optimal direction”；
- 当时心态是把能想到的“更好”全部丢进去、尽最大努力实现。

Source: https://arstechnica.com/gaming/2023/12/dooms-creators-reminisce-about-as-close-to-a-perfect-game-as-anything-we-made/

这非常关键：

> **“追求最好的事情”有两种完全不同的失败：**
> 1. 目标判断错；
> 2. 每个局部都更好，但组合成的系统不再是最优项目。

DOOM时期“新技术+新grammar+高互补”一起收敛；Quake时期技术野心本身开始占据巨量项目容量。

因此新增变量：
- `LOCAL_BEST vs SYSTEM_BEST`
- `TECHNICAL_FRONTIER_LOAD`
- `INTEGRATION_COST`

## 3. Ion Storm Dallas：最大变化不是Romero“更狂”，而是规模、能力图与治理同时变了

### 3.1 规模不连续：从核心小队变成约85人、多团队、多游戏

1997 Mike Wilson在Game Developer采访称Ion Storm已约85人；Todd Porter、Tom Hall、John Romero各带约15–17人的项目组，另接Dominion与Austin团队。
Source: https://www.gamedeveloper.com/design/an-interview-with-ion-storm-s-mike-wilson

PC Gamer 2020多方口述指出，Dallas从一开始就**缺清晰公司层级**：
- Romero是公众figurehead，却无意负责日常经营；
- Hall专注Anachronox；
- Porter/O'Flaherty既是创始人又各有项目；
- Mike Wilson名义CEO却缺真实最终权力；
- 四位创始人形成所谓“Four Corners of Power”，治理冲突长期存在。

Source: https://www.pcgamer.com/the-history-of-ion-storm/

这不是小团队flat hierarchy自然放大的结果，而是 `SCALE_DISCONTINUITY`：
[
	ext{small-team informal coordination}

otRightarrow
	ext{multi-project company governance}
]

### 3.2 互补能力断裂：Romero离开id以后失去的不只是“Carmack这个程序员”

GamesBeat 2023追问Daikatana等待/迁移引擎的问题。Romero承认：
- Carmack级引擎人才极少；
- 将项目从Quake engine中途迁到Quake II变成巨大time sink；
- 他此前从未经历这种中途整体换引擎的生产代价。

这说明early id的“快速抛弃旧技术”可以成立，一个隐含条件是：
> **你内部就拥有创造下一代技术的Carmack，并且技术作者和产品作者在同一反馈循环里。**

Ion Storm把部分技术能力外部化/依赖许可引擎后，继续采用“有更好的就换”会遭遇完全不同的integration cost。

新增：`COMPLEMENT_DEPENDENCE BLINDNESS`——成功者把“团队拥有的能力”误记成“我的方法拥有的能力”。

## 4. “Design is Law”的真正问题：自主权没有与清晰责任边界绑定

Ion Storm最初口号`Design is Law`，意图反转id后期“技术先行”的挫败；PC Gamer 2020访谈中Tom Hall称公司梦想就是“设计自己想做的游戏”，通过license现成技术让design主导。

这不是愚蠢理念。最强证据恰恰是**同一家公司Austin做出了Deus Ex**。

真正区别：

### Dallas
- 公司层级含糊；
- 多位创始人拥有重叠权力；
- 多项目并行；
- CEO/owner权力错位；
- 高宣传使错误成本公共化；
- 团队流失严重；
- Daikatana最终出现多位lead programmer更换。

### Austin / Deus Ex
Warren Spector 2000 postmortem虽然也承认最初team structure失败，却给出相反的治理结论：
> 必须有明确chain of command；共识可以大量使用，但**一个项目只能有一个boss，每个department也只能有一个boss，负责人向项目负责人负责**。

同时他承认：
- 巨大预算、无外部时间约束、完全创作自由让团队“变软”；
- 原始设计太大；
- 后来必须做大量删减、聚焦；
- 有些技术风险未提前解决。

Source: https://www.gamedeveloper.com/design/postmortem-ion-storm-s-i-deus-ex-i-

因此：
[
	ext{Creative autonomy}
+
	ext{clear accountable owner}
+
	ext{scope correction}
+
	ext{publisher time buffer}
]
可以工作；

而不是：
[
	ext{Creative autonomy}
=
	ext{no hierarchy / no kill rights}
]

## 5. Deus Ex还是Romero“自由主义”最有力的正面证据

不能因为Dallas失败就把Romero的Ion Storm理念全部判错。

Warren Spector 2023回顾说，Romero亲自给他：
- 最大预算；
- 最大营销预算；
- **no creative interference**；
并且Ion Storm与Eidos兑现了承诺。他说自己欠Romero极大人情。

Source: https://www.gamedeveloper.com/business/my-40-years-in-the-game-industry

PC Gamer口述史还记载：
- Dallas有人几次想取消/干预Deus Ex；
- Romero多次挡住这些干预，明确要求“leave them be”；
- 到Alpha后，Eidos又给Austin约六个月额外时间；
- 团队用这段时间重做技能系统、调优并“find the fun”。

Source: https://www.pcgamer.com/the-history-of-ion-storm/2/

所以Romero的`DESIGNER SOVEREIGNTY`不是错：
**给正确的人足够自治，本身确实能产生Deus Ex。**

真正问题是：
> **谁有资格获得这种主权？主权的边界在哪里？谁负责在方向错误时强制收敛？**

这直接连接中国/日本研究的`PROBLEM_ORIGIN_RIGHT / GREENLIGHT_RIGHT / KILL_RIGHT / FAILURE_SHELTER`。

## 6. Hirschman：我们前面一直在讨论的其实是 Exit / Voice / Loyalty

Albert O. Hirschman 1970经典框架：
- `EXIT`：离开组织/停止购买；
- `VOICE`：留在内部表达、试图改变；
- `LOYALTY`：使成员愿意延迟exit，并可能增强voice。

现代AER/Harvard对该模型的总结仍保留这一核心。
Sources:
- https://www.hks.harvard.edu/faculty-research/policy-topics/advocacy-social-movements/liz-mckenna-making-sense-social-movements
- https://www.aeaweb.org/articles?id=10.1257%2Fmic.20180085

把它放到本项目：

### early id：高EXIT能力
Softdisk不满足 → 退出；
传统publisher不足 → shareware；
Sierra估值不满意 → 保留公司；
旧产品/技术不适合 → pivot。

### 日本黄金时代：更多局部VOICE / protected slot
现有日本研究提示部分公司内部：
- prototype权；
- 高层恩主；
- frontier exemption；
- 项目失败后仍可留组织。
即“不一定退出，也能得到异常大的问题主权”。

### Ion Storm悖论
Ion Storm是一次**由EXIT建立的新组织**，但新组织内部不能只靠继续EXIT：
- 员工频繁退出意味着能力流失；
- founder之间如果只有exit/互相切割而缺乏有效voice和最终裁决，组织会碎裂；
- loyalty完全消失同样不是创新天堂。

这说明：
> **Exit创造新组织；Voice治理组织；Loyalty保存长期协作资本。**

战略性不忠诚只解决“什么时候该走”，不能单独成为公司治理哲学。

## 7. 真理之盾 vs 自恋之盾：建议正式使用五道检验

这里给 reader layer 一套可证伪、避免心理诊断的Gate。

### Gate 1 — 独立外部证据是否仍在增加？
真理之盾：
- playable build；
- 用户行为；
- 销售；
- 技术benchmark；
- 合作者独立判断。

自恋之盾：
- 主要证据变成“我以前赢过”；
- 反对意见被解释成人不懂、嫉妒、拖累。

### Gate 2 — 能不能说出“什么结果会证明我错了”？
真理之盾有 `KILL / RESCOPE THRESHOLD`。
自恋之盾不断移动goalpost。

### Gate 3 — 反对者还有没有真实Voice？
如果所有能否决创始人的人都已被赶走，剩下“大家都支持我”是弱证据。

### Gate 4 — 你是不是把团队能力误记成个人能力？
early id成功可能属于`Carmack × Romero × Hall × Adrian × Cloud × Miller × shareware`的组合。
离开后还假设“我以前做到过，所以这个组织也能做到”，属于`COMPLEMENT BLINDNESS`风险。

### Gate 5 — 规模变了以后，决策机制有没有升级？
5人团队的每天试玩、口头共识和全员互知，不能直接扩到85人、多游戏、外部publisher。

**一句话：**
> 真理之盾保护的是一个仍接受现实伤害的判断；自恋之盾保护的是判断者不受现实伤害的自我形象。

## 8. 前面提过但一直没有真正展开的研究欠账

这次明确列账，不再被新案例覆盖。

### A. 认识论 / 人格
1. **Complementary Founder as Error-Correction System — PARTIALLY CLOSED by [042](carmack-romero-complementary-error-correction-network-042.md)**  
   已核出 Dangerous Dave 战略解释、Apple II角色重划、Wolf3D push-wall 技术洁癖让步、Doom design↔engine翻译层与 Quake correction-latency 断裂；同时以 Playdead CASE-056 压力测试“能力互补成功≠治理可持续”。仍缺Doom Bible、1995-11 meeting、Adrian/Cloud/Wilbur等逐事件第二方补证。
2. **Authority Discounting vs Expertise Discounting**  
   不迷信Ken Williams是对的；但什么时候“权威折价”变成“拒绝真正懂行的人”？
3. **Winner's Amnesty / Merit-Conditional Tolerance**  
   社会为什么在怪人成功后把同一行为从“不成熟”重新命名为“远见”？失败者对应分母怎么找？
4. **Success-Path Version Lock**  
   过去正确的答案如何变成下一阶段最大的认知资产/负债？Romero/Ion、Ken Williams/Sierra、任天堂老组织都可比较。

### B. 组织治理
5. **Exit / Voice / Loyalty完整比较**  
   美国exit-heavy、日本slot/voice-heavy、中国可能同时存在high agency tax与高exit cost；需历史和企业内普通员工分母。
6. **Small-Team OS → Scale Discontinuity**  
   5–10人有效的flat/高信任结构，在哪个规模需要显式层级、接口和kill rights？
7. **Creative Sovereignty vs Accountability**  
   Deus Ex、Supercell、Nintendo prototype、Valve等是否存在“高自治+强收敛”的共同结构？
8. **Founder Equity ≠ Decision Architecture**  
   Ion Storm equal-ish founder ownership、CEO无权等问题；股权、公平与最终产品裁决权必须拆开。
9. **Relationship Capital**  
   “过去贡献不构成永久decision right”是真的；但过快切割会损失哪些不可重建的tacit knowledge和trust？

### C. 资本 / 市场
10. **When Should You Sell?**  
    Sierra/id只是正例；必须找“拒绝收购后来归零”和“卖早了反而更好”的压力样本，才能做人生指南。
11. **Direct Market as Epistemic Infrastructure**  
    shareware不仅是渠道，还是更快的真伪检验器；Steam/itch/TikTok/demo节日是否仍承担同类功能？
12. **Incumbent Blindness**  
    Ken Williams看不懂Wolf3D到底是老权威僵化，还是当时理性地面对高不确定性？找当年可比失败FPS/3D项目做分母。
13. **Publisher = Capital + Governance + Distribution**  
    “不要publisher”太粗。真正是哪些decision rights值得卖，哪些不值得卖。

### D. 比较社会
14. **American Civil Religion and Entrepreneur Myth**  
    “山巅之城/新世界实验”如何转译成self-made founder神话，需要文化史，而非直接诊断游戏人。
15. **UK bedroom coder / Finland demoscene / Slavic studios**  
    若这些地方也产生极强作者，则可进一步拆美国特殊性：到底是individualism、计算机普及、福利/教育、demo scene还是市场接口？
16. **Japan's Creator Replacement Problem**  
    旧一代作者很强不代表新人仍能获得同等破格权；任天堂、Falcom、SEGA等要看作者代际更新率。
17. **China's Dual Deficit or Different Route?**  
    中国到底是内部prototype slot少、外部exit昂贵，还是已有NExT/DeepSeek/Steam indie等新替代接口，只是密度不足？

### E. 人生伦理
18. **“砍掉拖累”与人的价值分离**  
    项目上退出一个合作者可以正确；不能因此把这个人降格为“落后者”。如何处理production truth和relational obligation？
19. **Family / Partner as Runway Infrastructure**  
    家庭不仅给态度，也提供住房、照护、工资、容错；成功故事如何把这些隐去？
20. **Meaningful Life Without the Hit**  
    Berardi等已经开始回答：没有成为Romero，创作者的人生是否仍然值得？

## 9. 下一步排序

### P0
1. **Exit / Voice / Loyalty × Ion Storm Dallas/Austin**：因为它能同时解释美国、日本、中国组织差异。
2. **Complementary Founder = Error-Correction System**：重新读early id，不再只按“技术天才+设计天才”。
3. **When Should You Sell?**：给Sierra/id找失败反例，避免把拒绝收购变成成功学。

### P1
4. UK bedroom coding / Finland demoscene，检验“美国特殊性”；
5. 权威折价 vs expertise discount；
6. relationship capital / 切割的隐性成本；
7. Japan creator replacement。

### P2
8. American civil religion与创业神话文化史；
9. family/partner hidden infrastructure；
10. meaningful no-hit life进一步扩普通分母。

## Sources
- John Romero 2023 GamesBeat direct interview: https://gamesbeat.com/making-doom-and-building-the-fps-industry-at-100-miles-per-hour-john-romero-interview/
- Carmack/Romero Doom 30-year retrospective, Ars 2023: https://arstechnica.com/gaming/2023/12/dooms-creators-reminisce-about-as-close-to-a-perfect-game-as-anything-we-made/
- Mike Wilson contemporaneous Ion Storm interview, Game Developer 1997: https://www.gamedeveloper.com/design/an-interview-with-ion-storm-s-mike-wilson
- Ion Storm multi-party oral history, PC Gamer 2020: https://www.pcgamer.com/the-history-of-ion-storm/
- Warren Spector, Deus Ex postmortem, 2000: https://www.gamedeveloper.com/design/postmortem-ion-storm-s-i-deus-ex-i-
- Deus Ex oral history: https://www.gamedeveloper.com/design/developing-i-deus-ex-i-an-oral-history
- Warren Spector 40-year retrospective, 2023: https://www.gamedeveloper.com/business/my-40-years-in-the-game-industry
- Hirschman framework modern summaries: https://www.hks.harvard.edu/faculty-research/policy-topics/advocacy-social-movements/liz-mckenna-making-sense-social-movements ; https://www.aeaweb.org/articles?id=10.1257%2Fmic.20180085

**Transfer 2026:** durable framework, historical cases. Do not reduce clinical personality, national character or organization success to one variable.
