# CASE-018 — RollerCoaster Tycoon / Chris Sawyer

- Status: RESEARCHING
- Subject: RollerCoaster Tycoon 1/2 / Chris Sawyer
- Related Claims: C003, C004, C007, C010, C011

## Why this case

RollerCoaster Tycoon 是 OPC 历史谱系里最重要的前数字发行案例之一：核心设计和绝大多数代码由 Chris Sawyer 一人完成，但项目建立在十多年编程史、Transport Tycoon 代码资产、传统出版商体系、专业图形/音频协作者与大量测试之上。

更重要的是，本案不能只看 1999 年的第一作。`RCT1 → 扩展包 → RCT2` 说明这不是一次偶然的“天才 solo miracle”，而是一套能够连续支撑商业产品的个人核心生产系统：**长期能力资本 + 可复用引擎/工具 + 有意识地拒绝昂贵升级 + 专业外围。**

它同时适合拆掉三个相反神话：
- “复杂商业游戏必须有大型团队”；
- “Sawyer 一个人完成了整款商业产品”；
- “续作必须用更昂贵的新技术和画面规格证明升级”。

## Capability Prehistory

Sawyer 官方履历显示：
- 1983 起已在 8-bit 平台写 machine code 游戏；
- 1988–1993 做过多款 PC conversions；
- 1993 后开发原创 PC 游戏；
- Transport Tycoon 1994 上市；
- RollerCoaster Tycoon 的代码从 1996 年的新 Transport Tycoon sequel 尝试演化而来。

因此 RCT 的“一个人”发生在能力积累完成之后，不是第一次项目的异常产能。

## Code Lineage: Transport Tycoon → RCT1 → RCT2

Sawyer 的官方资料说明 RCT 最初是 1996 年开始的新 Transport Tycoon sequel，后来放弃原方向并把代码改造成过山车模拟。2004 年接受 GameSpot 采访时，他进一步明确：**RollerCoaster Tycoon 和 RollerCoaster Tycoon 2 都从为新版 Transport Tycoon 编写的代码中生长出来。**

这使本案比“一人做出大游戏”更有价值：真正被重复利用的是一个开发者多年沉淀的**私有能力栈、代码资产和问题模型**。所谓 OPC 的低沟通成本并不是凭空出现，而是建立在长期 path dependence 上。

## Production / Technical Choice

Sawyer 官方 FAQ 明确：RCT 约 99% 以 x86 assembler/machine code 编写，少量 C 用于 Windows/DirectX 接口。他后来的解释是，在当时硬件上，为了同时保持大量对象、游客和车辆模拟以及帧率，这种低层技术选择直接决定了可承担的系统复杂度。

这不是可普遍复制的“汇编更好”，而是 C004/C007 的典型：开发者使用自己已经极度熟练的工具来改变单位计算/功能成本。

## RCT2: Refusing the Prestige Upgrade

RCT2 对本书尤其重要，因为它暴露出 Sawyer 的成本判断不是只发生在第一作。

2002 年谈 RCT2 时，Sawyer 被问到为什么续作仍大体沿用第一作的视觉风格。他的回答不是“技术做不到”，而是典型的 production allocation 判断：如果追求一次“巨大图形升级”，可能要投入数年；而 RCT 的价值首先来自 interaction、construction 和 gameplay，因此他选择把资源投入这些区域，而不是把续作变成昂贵的图形重制工程。

这是一条很强的 C007 证据：**小团队/个人开发的生产优势，不只来自做得快，还来自敢于不做行业默认认为“续作必须做”的昂贵升级。**

RCT2 最终于 2002 年发布，官方资料列出的主要扩展方向包括 scenario editor、更多 rides、更大的地图/世界、更多细节与建造选项以及 Six Flags parks。它不是一次技术世代跳跃，而是在既有生产系统里把可玩空间继续向外扩。

## Contributor Boundary

必须拒绝“纯一人产品”标签：
- Sawyer 是主要设计者/程序员；
- 历史资料一致指出 Simon Foster 负责大量图形工作，Allister Brimble 参与音乐/音频；
- 出版商参与更广测试和商业发行；
- family/friends 也参与早期 playtest。

第一作由 Hasbro Interactive 体系发行，第二作由 Infogrames Interactive 发行。核心生产高度个人化，并不等于制造、QA、包装、渠道、本地化、版权/品牌合作也由一个人承担。

下一轮仍需把 contributor credit 与合同结构用更强的原始资料逐项锁定。

## Scope / Feature Economics

RCT 还提供一个有价值的删减信号：1999 直接访谈中 Sawyer 说明 mini-golf 因实现工作量过高而从原版放弃，等到扩展包找到更简单办法才加入。

RCT2 又提供第二种删减：不是删一个 feature，而是**拒绝整套高成本表现升级路线**。

两者合在一起说明，即使是技术能力异常强的个人开发者，也不是“想做什么都做”；其核心能力之一恰恰是持续把 feature、技术路线和表现规格放回成本约束里。

## Market / Organization

RCT 不是现代 direct-to-consumer indie：它依赖 boxed retail 时代的 publisher infrastructure。产品核心生产可以极度个人化，同时市场接入和产品化外围仍高度组织化。

因此它最适合作为“OPC core production + industrial periphery”的历史案例，而不是现代自发行模板。

## Preliminary Verdict

> RollerCoaster Tycoon 1/2 证明的不是“一个人等于一家公司”，而是：当一个人经过十多年能力积累，拥有可复用代码、极端熟练的技术栈，并且敢于拒绝昂贵而低边际价值的行业默认升级时，核心设计/工程组织边界可以缩得非常小。OPC 的生产力来自能力资本、复用与选择性不做；外围成本并没有消失，而是被出版社、专业协作者和商业基础设施吸收。

## Evidence Index

- E001 — Chris Sawyer official biography：1983 起开发、PC conversion 前史、Transport Tycoon→RCT、RCT2 发行时间线。
- E002 — Chris Sawyer official FAQ：99% x86 assembler 与工具链。
- E003 — Chris Sawyer official feature：RCT 起初是 1996 Transport Tycoon sequel，代码后来改造。
- E004 — 1999 direct interview republished by CoasterBuzz：删功能/扩展包与制作判断。
- E005 — 2020s direct Sawyer interview：为何 assembler 是当时复杂模拟/帧率条件下的选择。
- E006 — Chris Sawyer official product chronology：RCT1、扩展包、RCT2 及主要新增内容。
- E007 — GameSpot 2004 direct Sawyer interview：RCT1 与 RCT2 都从新版 Transport Tycoon 的代码尝试中生长出来。
- E008 — 2002 HomeLAN direct Sawyer interview preserved by GGMania：拒绝为 RCT2 做耗时数年的巨大图形升级，优先 interaction / construction / gameplay。

## Open Questions

1. Simon Foster / Allister Brimble 在 RCT1 与 RCT2 的准确 contribution、工时和合同结构？
2. Hasbro / Infogrames 在 QA、营销、本地化、制造、渠道和授权合作上投入多少？
3. RCT1 开发期间 Sawyer 的个人收入/runway 来自哪些 Transport Tycoon 版税或预付款？
4. 从 Transport Tycoon sequel → RCT1 → RCT2，代码、工具和数据格式究竟复用了多少？
5. RCT2 的生产周期、核心协作者数量和 outsourcing boundary 能否被强证据锁定？
6. 作为历史 comparator，哪些机制能迁移到现代、哪些因 boxed retail 体系失效？
