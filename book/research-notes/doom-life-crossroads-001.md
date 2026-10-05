# Early id / DOOM Life Crossroads Audit 001

- Status: RESEARCH NOTE / READER-LAYER PREP
- Related Case: [`CASE-016`](../../cases/CASE-016-early-id-software.md)
- Evidence Ledger: [`CASE-016 Evidence`](../../evidence/CASE-016-early-id-software-source-ledger.md)
- Purpose: 把 `Keen → Wolfenstein 3D → DOOM → Quake` 从产品史改写成人物选择史，为 reader profile 提供结构；不替代 Case / Evidence。

## Core Question

`Masters of Doom` 最容易被读成“两个天才改变世界”。

本项目更关心：

> **John Carmack、John Romero、Tom Hall 等人在几个关键人生节点上，当时拥有什么、缺什么、可以去哪里、为什么做了这个选择？这些选择怎样逐步改变下一轮可行选择集合？**

重点不是把成年成就倒推成童年宿命，而是恢复当时的 uncertainty。

---

## Crossroad 1 — 游戏不是课余噪声，而是第一次遇到“我想进去改它”的对象

### Romero

Romero 2023 年回忆，1983 年转学到英国一座美军基地学校后，学校机房使用 Apple II，并教授 BASIC。这不是“学校直接培养了 DOOM 设计师”，但它提供了一个低门槛转换点：游戏兴趣和计算机第一次进入可以亲手修改 / 编程的环境。

此后 Romero 不是只做玩家。他向杂志提交游戏代码、经历拒稿，也逐渐获得实际发表和报酬。

来源：
- Shacknews, `Becoming Doom Guy: John Romero on his memoir and a life in games`, 2023: https://www.shacknews.com/article/136450/becoming-doomguy-john-romero-on-his-memoir-and-a-life-in-games

### Carmack

Carmack 后来回忆，少年时就会直接修改 *Ultima II* 的磁盘 sector 数据。这个动作很关键：他与游戏的关系不是“消费一个封闭成品”，而是把软件视为可以拆、可以观察、可以改变的系统。

来源：
- WIRED, `Q&A: Doom's Creator Looks Back on 20 Years of Demonic Mayhem`, 2013: https://www.wired.com/2013/12/john-carmack-doom/

### Reader-layer interpretation

这不是“打游戏让人变程序员”。

而是：

```text
游戏兴趣
→ 想理解规则 / 内部结构
→ 获得机器 / 编程入口
→ 修改 / 编写
→ 外部反馈
```

真正发生能力转换的，是中间这些动作。

---

## Crossroad 2 — Softdisk：先进入一个高频出货系统，而不是先成立梦想公司

在 Softdisk / Gamer's Edge，Romero、Carmack、Tom Hall、Adrian Carmack 等人首先是职业生产者。

关键条件：

- 有工资；
- 有机器和工作环境；
- 有明确交付周期；
- 必须反复 ship；
- 可以观察彼此工作；
- 大量已有 Apple II / PC 技术和旧作可以复用。

Romero 回忆 Gamer's Edge 的出货节奏极高；后来的 Catacomb 3-D 口述史也说明，为了满足月度生产，他们会主动重写 / 移植自己已有作品，而不是每次从零发明。

来源：
- CASE-016:E001
- Shacknews, `Living the Dream: The Making of Catacomb 3-D`, 2025: https://www.shacknews.com/article/143288/living-the-dream-the-making-of-catacomb-3-d

### Reader-layer interpretation

他们的“独立能力”不是在辞职当天生成的。

更接近：

> **先在有工资的生产系统里，把“我喜欢做游戏”训练成“我可以稳定完成游戏”。**

这对目标教育很重要：职业路径不一定是梦想的反面。某些工作首先提供能力资本和安全试错空间。

---

## Crossroad 3 — 有技术突破以后，先偷偷做一个 proof，而不是直接辞职

Carmack 的 PC scrolling 技术让团队意识到，PC 可以逼近当时更像主机的横版动作表现。

他们没有先成立公司、融资、组几十人。

而是利用夜晚 / 周末做出 proof，并最终形成 Commander Keen。

这段历史最重要的不是“偷用公司电脑”的传奇感，而是 commitment level：

```text
职业工作仍在
→ 技术 proof
→ 游戏 prototype / shareware opportunity
→ 市场验证
→ 收入足以改变职业选择
→ 才全职独立
```

来源：
- CASE-016:E002 / E003 / E004

### Reader-layer interpretation

这不是“勇敢辞职追梦”。

恰恰相反：

> **他们先把梦想做成足以改变现实约束的证据，再提高承诺等级。**

---

## Crossroad 4 — Apogee / shareware：第一次有人为“另一种发行结构”打开门

Scott Miller 不是普通意义上的老板。

他的 shareware 模式提供了：

- 免费 episode 作为获客；
- 玩家直接体验；
- 后续内容直接转订单；
- 小团队不必先进入传统零售生产结构。

Keen 的成功使 id 有资格离开 Softdisk，但离开仍伴随合同义务和 legal settlement，而不是“有灵感所以自由”。

来源：
- CASE-016:E002 / E003 / E007

### Reader-layer interpretation

人生岔路不仅由个人决定，也由**新制度出现**决定。

一个人可能早几年同样有技术、同样有野心，却因为缺少合适分发机制无法走同一路。

---

## Crossroad 5 — Wolfenstein：有第一桶金以后，没有立刻购买大组织

Keen 购买了独立时间。

Wolfenstein 3D 又把：

- 3D 技术；
- action design；
- shareware；
- 品牌；
- 现金流

进一步耦合。

关键问题不是“Wolfenstein 赚了多少”，而是：

> **第一次成功之后，id 首先扩大的是可选项，而不只是 headcount。**

他们可以继续做更危险的技术 / 产品实验，同时维持小核心。

来源：
- CASE-016:E007 / E010

---

## Crossroad 6 — DOOM：钱多了以后，真正值得买的是 leverage

DOOM 阶段最值得从生产史而不是技术史理解的投入：

### DoomEd / NeXT

Romero 的 DoomEd 约投入五个人月，其意义是让 level designer 在编辑器里直接设计，而不是不断请求 programmer 改数据。

### C over assembly where appropriate

Carmack 并没有把“越底层越硬核”当身份。他把大部分代码放在 ANSI C，只在关键渲染 routine 使用汇编。

### Strategic control + outsourced operations

DOOM 阶段 id 把分发战略控制内收，但没有因此自己做所有运营，而是把电话订单等执行外包。

来源：
- CASE-016:E007

### Reader-layer interpretation

成功后的成熟，不是“终于什么都自己做”。

而是开始问：

> **哪些能力必须掌握，哪些工作只要有人可靠地做就行？**

这是从个人英雄进入组织设计的第一步。

---

## Crossroad 7 — 为什么 Carmack 愿意让玩家进去改

Carmack 2013 年回忆自己少年时期修改 *Ultima II* 的经验，并明确把后来愿意公开代码 / 支持修改，与“让下一代得到自己当年想要的东西”联系起来。

DOOM 的 WAD / specs / editor ecosystem 随后把产品边界打开。

到 1998 年，WIRED 已经记录 Doom 圈中的专业级地图作者怎样从消费者身份进入职业 level design。

来源：
- WIRED 2013: https://www.wired.com/2013/12/john-carmack-doom/
- CASE-016:E008
- WIRED, `Legion of Doom`, 1998: https://www.wired.com/1998/03/doom/

### Fourth Industrial Revolution significance

这是一个非常早的数字能力生态原型：

```text
commercial software
→ exposed structure / moddability
→ player experiments
→ public artifact
→ reputation
→ professional opportunity
```

平台不是学校，但它产生了一条非正式的 capability pipeline。

---

## Crossroad 8 — Tom Hall 离开：互补不是永恒稳定

Tom Hall 在 DOOM 早期承担创意方向，但团队对 DOOM 应该成为什么产生实质冲突，最终离开。

这不能简化成“谁对谁错”。

更重要的是：

> **当产品方向开始变化，原本互补的人可能不再对同一个目标函数达成一致。**

来源：
- CASE-016:E007
- *Masters of Doom*（E006）作为叙事补充，不独立承担动机裁决。

---

## Crossroad 9 — DOOM 成功以后，为什么 Quake 反而更难

成功改变了所有人的外部选择：

- 更有钱；
- 更有名；
- 技术野心更大；
- 可以招到顶级人才；
- 每个人更有能力坚持自己的目标。

WIRED 1996 的同期现场报道已经记录 Quake 开发中的 delay、false starts、war-room 集中生产和高压冲突。

来源：
- WIRED, `The Egos at Id`, 1996: https://www.wired.com/1996/08/id/

### Reader-layer interpretation

小团队早期的超低协调成本，部分来自：

- 人少；
- 目标近；
- 钱少；
- 交付快；
- 彼此能力高度互补。

成功以后，这些条件同时被破坏。

所以：

> **成功购买选择权，也购买分歧的能力。**

这应该成为 `Masters of Doom` reader profile 的后半段，而不能在 DOOM 发售高潮处结束。

---

# *Masters of Doom* 应怎样被拆，而不是怎样被膜拜

## 1. Two capability systems

不要只写“两位 John”。

要拆：

### Carmack

- 计算机 / 图形 / engine frontier；
- 问“现在机器刚好能做到什么”；
- 技术约束直接塑造产品可能性；
- 对开放代码 / hacking culture 有长期价值偏好。

### Romero

- 长期游戏玩家 / maker / shipper；
- game feel / level / tool / product momentum；
- 强烈吸收游戏文化并快速试验；
- 把技术 possibility 变成具体玩家体验。

这是初步 reader-layer abstraction，不是人格心理诊断。

## 2. Complementarity as temporary capital

他们早期真正的 superpower 不是单个人的天赋，而是：

> Carmack 扩大技术可行域；Romero / Hall / artists 把它迅速翻译成可玩的产品；高频 ship 又不断给技术反馈。

## 3. Cash changes the feasible set

Keen / Wolfenstein / DOOM 的钱不能只写成财富数字。

每次收入都改变：

- 是否需要老板；
- 是否需要 publisher；
- 能买什么硬件；
- 能花多久做 tool；
- 能不能拒绝某个 deal；
- 能不能承担下一次更大的实验。

## 4. Success creates organization problems

`Masters of Doom` 后半段最值得保留，因为它拒绝“爆款以后幸福结束”。

产品成功并不能自动生成：

- governance；
- role clarity；
- founder alignment；
- decision rights；
- sustainable work culture。

这是 early id 从“项目型英雄团队”转成“必须成为组织”时遇到的断层。

---

## Reader Profile Requirements

正式 profile 至少要覆盖：

1. 两位 John 的游戏 / 计算机前史；
2. Softdisk 为什么重要；
3. 为什么没有一开始辞职；
4. Keen 如何把 proof 变成职业独立；
5. Wolfenstein 如何把第一轮成功变成下一轮 optionality；
6. DOOM 为什么优先买工具 / 技术 / control 而不是先买大 headcount；
7. WAD / openness 怎样把玩家变成外围生产者与未来专业人才；
8. Hall conflict；
9. Quake / Romero split：成功为什么产生新的组织问题；
10. 哪些内容来自 *Masters of Doom*，哪些已经被 P0/P1 来源独立确认。

## Boundary

- 不把违法 / 叛逆经历浪漫化成创业必要条件；
- 不把极端工时当现代建议；
- 不把 1990s shareware 直接类比 Steam；
- 不把 Carmack / Romero 简化成“技术脑 vs 创意脑”的漫画人格；
- 不把游戏兴趣直接等同职业能力；必须展示转换动作；
- 不把 DOOM modding 证明成“所有玩家都能靠 mod 入行”，只能证明该 pathway 真实存在并在特定生态中形成职业入口。
