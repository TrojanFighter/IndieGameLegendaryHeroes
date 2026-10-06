# 003 — Game Industry Technology Regimes

- Status: WORKING MAP
- Purpose: 为《独立游戏英雄传说》的 Technical Opportunity Window 提供时代背景。
- Boundary: 这里只研究公开技术条件与产业扩散，不推导私人项目设计方案。

## 1. 为什么不能只写“8-bit → 16-bit → 3D → AI”

游戏开发者真正面对的可行解空间至少由五组条件共同决定：

1. **Compute substrate**：CPU / GPU / memory / storage / device；
2. **Authoring substrate**：语言、引擎、编辑器、middleware、asset tools；
3. **Network substrate**：互联网、宽带、服务器、platform services、backend；
4. **Market substrate**：发行、支付、Steam / app stores、众筹、EA、creator discovery；
5. **Production ecology**：mod / UGC、开源、素材市场、远程协作、外包、AI。

同一块更快的硬件，在 market / tool / distribution 没变化时，不一定改变独立开发的最优组织方式。

## 2. 暂定分代：按“新可行解”而不是硬件营销代际

### Regime A — Hardware-Bound Craft

典型问题：
- 内存/CPU/存储直接决定内容和交互边界；
- 团队经常需要自己写底层工具；
- 发行渠道仍高度物理化或平台化。

研究候选：
- Apple II / early PC；
- MSX / early console；
- early id / Commander Keen。

人物篇要问：
- 当事人具体掌握哪台机器？
- 是消费者、hacker 还是 professional developer？
- 技术限制怎样进入 product decision？

### Regime B — Engine / Middleware Diffusion

关键变化：
- 越来越多开发者不再从 renderer / physics / toolchain 的最底层开始；
- 商用引擎和作者工具缩短 first playable 时间；
- 但“会用引擎”不等于产品判断、内容生产和市场接入已经解决。

研究候选：
- GameMaker → Gunpoint；
- Unity-era micro teams；
- Unreal → Project Wingman / Manor Lords 等。

### Regime C — Internet / Mod / Community Production

关键变化：
- 玩家能修改、上传、运营服务器、形成公开身份；
- mod / map / server 从娱乐活动变成低风险 production apprenticeship；
- artifact-first credential 出现。

强锚点：
- DOOM / WAD；
- Red Orchestra；
- Arma / DayZ → PLAYERUNKNOWN；
- Roblox creator ecosystem。

### Regime D — Direct Digital Market Interface

关键变化：
- 数字商店与支付降低物理发行门槛；
- crowdfunding / paid alpha / Early Access 改变融资和反馈顺序；
- devlog / video / streamer / social discovery 直接进入生产循环。

强锚点：
- Minecraft；
- FTL；
- Kenshi；
- Factorio；
- Gunpoint。

### Regime E — Production-Service Abundance

关键变化：
- cloud / SaaS / marketplace / remote contractor / platform services 继续压缩外围建设成本；
- 小团队可以租用过去必须自建的部分能力；
- bottleneck 更可能移动到 integration、selection、validation、coordination。

### Regime F — Generative / Agentic Production

当前只建立研究问题，不宣布结论：

- coding / art / text / QA / research / ops 哪些成本真实下降？
- 哪些只是 demo 能做、production 不能稳定做？
- 哪些岗位从“亲自执行”变成“定义 / 审核 / integration”？
- 哪些新 coordination cost 出现？
- frontier model capability 何时扩散到普通小团队的可负担工具？
- 当 execution cost 下降后，selection / taste / problem formation 是否成为相对更稀缺变量？

最后一项目前属于 thesis candidate，不能因当前 AI 热潮直接写成定论。

## 3. Technical Opportunity Window — 人物篇接口

人物 Profile 不写“某年技术进步了”这种背景板。

应该回答：

| 问题 | 说明 |
|---|---|
| 当时他实际能拿到什么？ | 不是全球最先进，而是本人可获得 |
| 前几年为什么难做？ | 成本、工具、网络、分发、技能哪项卡住 |
| 新条件改变了什么？ | 哪个约束下降 |
| 他本人是否意识到？ | 找同期访谈 / 日记 / prototype |
| 同时代别人也能拿到吗？ | 防止把公共条件写成个人天才 |
| 仍然做不到什么？ | 防止“技术一到位就无所不能” |

## 4. 第一批现有案例回填

### Early id / DOOM

已有 Evidence 支持：
- Softdisk 高频职业出货形成能力；
- Commander Keen 在工资/公司硬件条件下 moonlight；
- NeXTStep、DoomEd、ANSI C 等工具选择用于降低迭代/porting friction；
- shareware / direct distribution 改变小公司的资金与发行边界；
- WAD / specs openness 形成外部 mod 生态。

因此这里不是“PC 性能突然够了”，而是：

> compute + 自研工具 + shareware + 小团队高频出货 + open mod ecology 的组合窗口。

### Gunpoint / Tom Francis

CASE-007 E004 支持：Francis 看到 Spelunky 使用 GameMaker 后，才明确意识到自己可以用 novice-friendly tool 把判断快速做成 movement prototype。

因此：

> GameMaker 的历史意义不是“它很便宜”，而是缩短 judgment → playable → tester truth 的路径。

### PLAYERUNKNOWN / Brendan Greene

CASE-032 已支持：

> Arma / DayZ 提供现成大型地图、simulation、server/mod substrate，使一个不具备完整大型在线工程能力的作者可以先验证 ruleset；H1Z1 和 Bluehole 再承担后续工业化。

这里尤其能证明 Technology Availability ≠ Complete Capability。

## 5. 下一批待审计

- 小岛秀夫 / MSX2 Metal Gear：硬件限制、screen handling、敌人/射击约束与 stealth 方向之间到底有哪些同期直接证词；
- Wolfenstein / DOOM：PC 性能、VGA、networking 与 shareware 各自贡献；
- Minecraft：Java、网页支付、论坛、paid alpha；
- Unity / Steam Greenlight / Kickstarter 同期如何重构 2010s indie feasible set；
- broadband / streaming / Twitch 对多人新玩法市场验证的作用；
- Roblox / UGC 平台把 tool + audience + distribution + monetization 合并后的职业形成效应；
- generative AI 的 frontier / professional / indie diffusion 分离。

任何对象都先补时间线，再写“技术导致了什么”。
