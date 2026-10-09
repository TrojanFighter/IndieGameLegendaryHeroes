# Context–Situation–Action Audit

这个协议用于防止独立游戏生产史最常见的一种误读：

> 看到后来成功的动作，就脱离当时可用的技术、平台、资金与个人处境，把它写成普遍正确的“方法”。

本项目要求从 Case Schema v2 开始，把关键决策写成：

> **时代技术条件 / Production Regime → 作者当时的具体处境 / Actor Situation → 在这个可行选择集合内采取的行动 / Action**

简称 **CSA**。

CSA 不是新的因果理论，也不是“时代决定论”。它只是要求先恢复当时的选择集合，再评价作者的判断。

## 1. Era / Production Regime

不要只写年份。年份本身不能说明一个独立开发者当时能做什么。

至少检查以下维度中与本案有关的部分：

### Production technology

- 主流或可获得的引擎；
- 自研引擎的必要性与成本；
- middleware；
- 版本控制；
- 3D / 2D / 音频 / 动画工具；
- 资产商店与可复用素材生态；
- 硬件性能与开发机成本；
- 自动化、程序生成与 AI 工具。

### Distribution

- shareware / retail / portals / Steam / App Store / console storefront / UGC platform；
- 上架门槛；
- 平台抽成；
- 是否存在 Greenlight、Steam Direct、Early Access；
- 是否容易自发行；
- 支付与跨境收款条件。

### Discovery

- 游戏媒体；
- 论坛 / mailing list / developer blog；
- YouTube / Twitch；
- 平台首页与算法推荐；
- festival / showcase / demo event；
- influencer / creator economy 是否已经成熟。

### Collaboration

- 同地办公 vs remote；
- IRC / forum / email / Discord / Slack 等协作工具；
- 云存储、云构建、远程版本控制；
- freelance / outsourcing 市场成熟度；
- 全球人才调用成本。

### Capital / financing

- 工资和兼职；
- publisher advance；
- crowdfunding；
- Early Access / paid alpha；
- grant / incubator；
- creator-platform income；
- 是否能直接向全球玩家收钱。

### Institutional / regional conditions

- 地区生活成本；
- 医疗 / 福利 / 再就业安全网；
- 公司设立、支付、税务、签证与监管；
- 当地产业人才密度；
- 语言市场。

## 2. Explicitly record what did NOT yet exist

这一项非常重要。

每个历史案例至少问一次：

> 今天看起来理所当然的哪种工具、平台、商业模式或传播渠道，当时尚不存在、尚未成熟，或贵得不适用于该作者？

例如，不得默认：

- 1990s 开发者拥有成熟数字商店；
- 2000s 小团队拥有今天的 Unity/Godot + Asset Store 生态；
- 2011 年团队拥有成熟 Steam Direct / Next Fest / Discord / Patreon；
- 早期独立开发者拥有生成式 AI 辅助程序、美术、研究与营销生产。

这不是为了强调“以前更难”，而是为了恢复**真实可选方案**。

## 3. Actor Situation

同一个时代条件，对不同人不是同一个机会集合。

关键决策发生时至少检查：

- 已有技能；
- 已有代码、引擎、工具、素材或 IP；
- 当前职业与收入；
- 储蓄、runway、burn；
- 家庭 / 伴侣支持与照护责任；
- 住房、医疗、签证等尾部风险；
- 地理位置；
- 已有玩家 / 粉丝；
- 媒体身份或公开作品；
- 行业人脉；
- 可调用的合作者与外包；
- 当时真正可以选择的其他路径。

不要把后来获得的资源倒写成决策当时已经拥有。

## 4. Binding Constraint

每一个关键 Decision Unit 要尽量指出当时真正卡住作者的约束。

常见但不穷尽：

- 缺时间；
- 缺现金；
- 缺特定技术；
- 缺内容产能；
- 缺可信履历；
- 缺团队；
- 缺市场验证；
- 缺发行渠道；
- 缺受众；
- 缺对某一玩法问题的正确理解；
- 风险过高，不能一次性承诺全部资源。

不要看到结果以后才虚构一个“他们一定是在解决 X”的目的。若动机只有回顾性证词，明确标 P1。

## 5. Action / Maneuver

记录具体动作，而不是人格形容词。

坏写法：

- 他很坚持；
- 他很有品味；
- 团队很灵活；
- 他们相信玩家。

好写法：

- 把工作压成每周两个 12 小时班，以保护其余连续开发日；
- 继续接 work-for-hire，让合同收入覆盖原创团队；
- 删除多人模式，把网络与 live-ops 成本从问题里移除；
- 用前置产品训练团队并产生下一项目现金流；
- 把 full launch 改成 demo，先验证 Steam audience；
- 采用付费 alpha，让用户现金流逐步替代工资或投资；
- 改用可读性更高的默认控制与 onboarding。

## 6. Decision Unit

重大转折建议统一记录为：

| 时间/窗口 | Era condition | Actor situation | Binding constraint | Action | Immediate result | Evidence | Transfer boundary |
|---|---|---|---|---|---|---|---|

一个 Case 可以有多个 Decision Unit。

不要强迫所有开发年表事件进入这个表；只收真正改变生产路径的选择。

## 7. Context audit status

### `pending`

尚未专门恢复生产时代和决策处境。

### `partial`

至少一个主要转折已经完成 CSA，但关键阶段仍缺：

- 时代技术条件；
- 作者当时资源；
- 替代方案；
- 或同期证据。

### `complete`

主要生产转折均已做到：

1. 可辨认当时的 production regime；
2. 可辨认作者当时的 actor situation；
3. 可指出 binding constraint；
4. 记录具体行动与直接结果；
5. 明确哪些今天常见的选择当时并不可用；
6. Transfer / Non-transfer 已考虑时代差异；
7. 没有把后来的结果倒写成决策时已知信息。

`complete` 不等于 Case 已经没有未知，只表示“时代—处境—行动”这一维完成了最低审计。

## 8. Anachronism Check

每个成熟 Case 至少回答：

> 如果拿掉后来才出现的工具、平台、融资或传播条件，作者当时的行动是否仍然能被解释？

重点防止：

- 用今天的成本结构评价过去；
- 用后来被证明成功的市场窗口解释早期动机；
- 把技术“存在”误写成对该作者“可负担且可获得”；
- 把平台后来形成的生态倒写成早期已经成熟；
- 从“今天可以更快做”直接推出“当年作者判断错误”。

## 9. Cross-case comparison rule

跨案例比较时，不直接比较动作名称，而比较：

> **在各自时代和处境中，它们解决的是不是同一种约束？**

例如：

- 1991 shareware；
- 2011 Kickstarter；
- 2013 paid alpha / Early Access；
- 2025 Steam demo + creator funnel；

可能都是不同 production regime 下的 **market validation / runway acquisition** 手段。

真正可迁移的通常不是表面动作，而是它在生产系统中承担的功能。

## 10. Legacy migration

`CASE-001`–`CASE-026` 属于 Schema v1 历史 Case。

不要在库运维流程中靠常识批量补 CSA。它们应在后续专门案例研究中逐案迁移：

1. 补 CSA 证据；
2. frontmatter / metadata 加 `schema_version: 2`；
3. 加 `context_audit`；
4. 通过 context lint；
5. 再考虑升 `REVIEW` / `STABLE`。

从 `CASE-027` 起，新 Case 必须直接使用 Schema v2。

## 2026-10-09 Technology Window Audit｜补充实际可用技术与UGC验证的CSA检查

将[技术机会窗口v1](technology-opportunity-window-audit.md)作为CSA的具体执行表：

- **Context**：技术出现、商业化、能买到、作者真正会用、成熟可复用，**五个日期可能完全不同**。区分1993 Doom、2011 FTL、2017 PUBG、2023 Lethal Company和2023后UEFN。
- **Situation**：程序技能、旧产品技术资本、商业引擎license、资产市场、平台玩家、可用团队与实际完整人年；别把只有代码的学生modder与有前作收入和团队的Battlestate写成同一种“从零创业”。
- **Action**：主动研发`CREATED`、现成技术重组`RECOMBINED`、能力继承`INHERITED`、Mod/Roblox/UEFN验证`PLATFORM_UGC`，及共同演进`CO_EVOLUTION`可并存；分别注明最早验证体验与真正扩大组织/资本投入的时点。

Mod/UGC可以是游戏本身的长期商业终点、被大厂收编、发展Standalone，也可以没有后续；不要把成功的幸存者路径解释成所有玩家作者的通用阶梯。

