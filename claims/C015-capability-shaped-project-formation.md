# C015 — Capability-Shaped Project Formation / 能力反向立项

- Claim ID: C015
- Statement: 在资源受限的作者型游戏中，一部分高价值项目不是先确定“完整游戏愿景”再被迫缩小，而是主创先识别自己的不对称能力、已知弱项与可获得外围资源，再反向选择或重写项目，使核心体验主要由强项产生，并把弱项相关的高成本 obligation 删除、抽象、复用或外围化；这种“能力反向立项”本身是一种设计能力，而不只是项目管理。
- Scope: 作者型 / 极小团队 / 小团队的 0→1 立项与早期产品定义；不主张所有成功独游都必须按个人短板设计，也不主张能力越偏科越好。
- Status: SUPPORTED
- Last reviewed: 2026-10-07
- Related Cases: CASE-007, CASE-008, CASE-018, CASE-042, CASE-043

## Definition

这里把机制暂定名为：

> **Capability-Shaped Project Formation（能力反向立项）**

它不是简单的 `scope cut`。

判据是：

1. 主创对自己的 capability vector 有显性或可观察的认识；
2. 这种认识发生在核心产品定义 / 早期制作阶段，而不是只在后期救火；
3. 项目的价值密度被主动压到强项上；
4. 弱项对应的昂贵生产 obligation 被删除、抽象、借用工具、复用旧资产或交给 specialist periphery；
5. 最终“这个游戏是什么”因此被改变，而不只是“同一个游戏少做一些内容”。

## Falsification Test

支持证据：
- creator contemporaneously says what they are good/bad at and changes project shape accordingly;
- project mechanics / representation / tooling align unusually well with pre-existing asymmetric capability;
- costly weak-skill obligations are consciously removed or externalized;
- later project history shows this was a repeatable selection method rather than one accidental fit.

反驳证据：
- project concept was fixed independently of creator capability and only later survived through brute-force labor;
- the alleged “fit” appears only in post-success storytelling;
- creators repeatedly choose projects requiring their weakest capabilities without compensating structures yet perform equally well;
- controlling for tool access, runway, collaborators and market timing removes most of the supposed advantage.

## Evidence For

| Evidence ID | Case | Mechanism | Weight |
|---|---|---|---|
| CASE-007:E004 | Gunpoint | Francis uses years of criticism to judge whether a small idea is unusual/testable rather than reproducing large games | high |
| CASE-007:E006 | Gunpoint | creator explicitly describes compressing the thing he loves into a simple reusable rule system | high |
| CASE-007:E008 | Gunpoint | contemporaneous roadmap cut removes scripted content that was expensive but low-value for “Gunpoint as a game” | high |
| CASE-008:E001 | Dream Quest | Whalen enters with card-game/math/system capital, existing engine and weak/unstable art access; product remains abstract and system-dense | medium |
| CASE-018:E005 | RollerCoaster Tycoon | Sawyer uses the language/toolchain in which he personally works fastest and most reliably to support simulation density | high |
| CASE-018:E008 | RollerCoaster Tycoon 2 | deliberately refuses a multi-year graphical prestige upgrade and invests in interaction/construction/gameplay instead | high |
| CASE-042:E005 | The First Tree | contemporaneous Wehle post explicitly names his strengths/weaknesses, keeps project short/simple and buys/modifies models/music/scripts | very high |
| CASE-042:E006 | The First Tree | launch-period reflection ties scope, Asset Store use and visual market surface into one production strategy | high |
| CASE-043:E006 | Everything | OReilly explicitly frames abstraction/procedural movement as both limitation-aware and artistically intentional | high |
| CASE-043:E009 | Everything | later direct account confirms locomotion was optimization/problem-redefinition, while still technically difficult | medium-high |

## Counterpressure

- CASE-043 shows redefinition can merely **move** cost: rolling/procedural locomotion deleted conventional animation obligations but created hard systems work.
- CASE-008 does not yet prove Dream Quest was selected *because* Whalen lacked art; abstraction may be both taste and constraint. It is supporting, not decisive.
- CASE-018 is an extreme capability outlier. Sawyer's assembler choice is evidence for personal capability-fit, not a general recommendation to choose niche technology.
- CASE-042 still lacks full household-burn accounting; project fit does not remove runway requirements.
- Gunpoint benefited from PC Gamer salary/network and GameMaker. Correct self-tailoring did not operate in a vacuum.

## Distinction from Existing Claims

### C004 — manufacture production conditions
C004 asks:
> How does a developer build a production environment that makes the project feasible?

C015 asks one step earlier:
> **How does the developer choose what project should exist given who they actually are?**

### C007 — redefine problem / cost structure
C007 asks:
> How can a small team redefine an expensive game problem?

C015 asks:
> **Why was this particular problem chosen/redefined in this direction? Was the product itself tailored around the creator's capability vector?**

### C003 — capability capital
C003 says the capability existed before the apparent “solo miracle.”

C015 says:
> **The creator can use knowledge of that capability distribution as an input to project formation.**

## Current Reading

The five cases support a stronger interpretation of indie design than “do less”:

> **Indie scope can be personalized rather than merely reduced.**

For a large organization, project definition often assumes a broad labor market: missing capabilities can be hired.

For a very small authorial team, the team itself is a hard design constraint. The sophisticated response is not necessarily to imitate a normal project with fewer people. It can be to invent a project whose highest-value problems are exactly the problems this person is unusually cheap/good at solving.

That creates several recurring transformations:

- critic / systems thinker → rule-dense game rather than content-heavy imitation;
- technical artist → environment / motion / presentation becomes gameplay and market surface;
- weak art access + strong systems/taste → abstraction becomes product language;
- unusually strong low-level programmer → simulation scale becomes viable while prestige graphics are rejected;
- animation auteur + programmer dyad → abstraction becomes interaction grammar instead of missing polish.

This is why some independent games look “strange” relative to industry genre templates:

> their form is partly the visible shape of the creator's capability vector.

## Boundary / Forbidden Inference

不得推出：

- “只做自己擅长的事”；
- “不要学习弱项”；
- “偏科一定比均衡能力更好”；
- “solo dev 天生更有创意”；
- “缺钱会自动逼出好设计”；
- “只要项目贴合个人能力就会成功”；
- “外包弱项永远比内部学习更优”；
- “所有成功独立游戏都是按主创能力反向定制的”。

真正的命题是：
> **显性认识 capability constraints，并把它们用于项目定义，可以成为作者型独立开发的一种可观察设计技术。**

## Next Evidence Needed

1. 找至少 2 个“明确知道能力边界 → 反向立项”的失败项目，避免只看成功者。
2. 把 Lucas Pope / Papers, Please 是否属于此机制重新核：目前更多证据是 disciplined cutting，而非明确以弱项反向立项。
3. 在 Jonas Tyroller 多项目里寻找同一个人是否越来越显性地做 capability–project matching。
4. 检验 2020s AI / asset / no-code 环境是否扩大了 creator 可选择的项目集合，从而改变“能力反向立项”的边界。
5. 与商业团队做对照：当缺失能力可以通过招聘补齐时，project formation 是否更少受 founder capability vector 约束。
