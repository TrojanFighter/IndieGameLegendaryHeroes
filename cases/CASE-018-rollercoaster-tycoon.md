# CASE-018 — RollerCoaster Tycoon / Chris Sawyer

- Status: RESEARCHING
- Subject: RollerCoaster Tycoon / Chris Sawyer
- Related Claims: C003, C004, C007, C010, C011

## Why this case

RollerCoaster Tycoon 是 OPC 历史谱系里最重要的前数字发行案例之一：核心设计和绝大多数代码由 Chris Sawyer 一人完成，但项目建立在十多年编程史、Transport Tycoon 代码资产、出版商体系、专业图形/音频协作者与大量测试之上。

它同时适合拆掉两个相反神话：
- “复杂商业游戏必须有大型团队”；
- “Sawyer 一个人完成了整款商业产品”。

## Capability Prehistory

Sawyer 官方履历显示：
- 1983 起已在 8-bit 平台写 machine code 游戏；
- 1988–1993 做过多款 PC conversions；
- 1993 后开发原创 PC 游戏；
- Transport Tycoon 1994 上市；
- RollerCoaster Tycoon 的代码又从 1996 年的新 Transport Tycoon sequel 尝试演化而来。

因此 RCT 的“一个人”发生在能力积累完成之后，不是第一次项目的异常产能。

## Production / Technical Choice

Sawyer 官方 FAQ 明确：RCT 约 99% 以 x86 assembler/machine code 编写，少量 C 用于 Windows/DirectX 接口。他后来的解释是，在当时硬件上，为了同时保持大量对象、游客和车辆模拟以及帧率，这种低层技术选择直接决定了可承担的系统复杂度。

这不是可普遍复制的“汇编更好”，而是 C004/C007 的典型：开发者使用自己已经极度熟练的工具来改变单位计算/功能成本。

## Contributor Boundary

必须拒绝“纯一人产品”标签：
- Sawyer 是主要设计者/程序员；
- 历史资料一致指出 Simon Foster 负责大量图形工作，Allister Brimble 参与音乐/音频；
- 出版商参与更广测试和商业发行；
- family/friends 也参与早期 playtest。

下一轮需要把 contributor credit 用更强的原始资料逐项锁定。

## Scope

RCT 还提供一个有价值的失败/删减信号：1999 直接访谈中 Sawyer 说明 mini-golf 因实现工作量过高而从原版放弃，等到扩展包找到更简单办法才加入。

这说明即使是技术能力异常强的个人开发者，也不是“想做什么都做”，而是持续把功能放回成本约束里。

## Market / Organization

RCT 不是现代 direct-to-consumer indie：它通过 Hasbro Interactive 等传统 publisher 体系发行。产品核心生产高度个人化，与市场/QA/包装/渠道的组织化外围同时存在。

因此它最适合作为“OPC core production”历史案例，而不是现代自发行模板。

## Preliminary Verdict

> RollerCoaster Tycoon 证明的不是“一个人等于一家公司”，而是当一个人经过十多年能力积累并拥有可复用代码、极端熟练的技术栈与专业外围时，核心设计/代码的组织边界可以缩得非常小。OPC 是能力资本积累后的外在形式，而不是团队成本凭空消失。

## Evidence Index

- E001 — Chris Sawyer official biography：1983 起开发、PC conversion 前史、Transport Tycoon→RCT。
- E002 — Chris Sawyer official FAQ：99% x86 assembler 与工具链。
- E003 — Chris Sawyer official feature：RCT 起初是 1996 Transport Tycoon sequel，代码后来改造。
- E004 — 1999 direct interview republished by CoasterBuzz：删功能/扩展包与制作判断。
- E005 — 2020s direct Sawyer interview：为何 assembler 是当时复杂模拟/帧率条件下的选择。

## Open Questions

1. Simon Foster / Allister Brimble 的准确 contribution 与合同结构？
2. Hasbro/MicroProse 在 QA、营销、本地化、制造、发行上投入多少？
3. RCT 开发期间 Sawyer 的个人收入/runway 来自哪些版税或预付款？
4. Transport Tycoon 代码/工具究竟复用了多少？
5. 作为历史 comparator，哪些机制能迁移到现代、哪些因 boxed retail 体系失效？
