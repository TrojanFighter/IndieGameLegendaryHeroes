# 独立游戏英雄传说

**Indie Game Legendary Heroes**

作者 / 主创：**洪荒行者**

这是一个关于独立游戏开发者、工作室与作品如何被“生产出来”的长期研究与写作项目。

它不是成功学案例集，也不是把幸存者重新包装成天才神话。项目要研究的是：当开发者面对资金、时间、能力、技术、组织、发行与市场等真实约束时，他们怎样识别哪些约束不能改变，怎样重构其余变量，怎样制造自己的生存条件与生产条件，并最终把一个按行业标准答案“做不起”的项目改造成能够完成、发行和存活的项目。

核心问题可以压缩成一句：

> **这些人面对一个按照行业标准答案根本做不起的问题，是怎样改变问题本身的？**

## 项目目标

本项目同时建设三种东西：

1. **可审计的案例库**：记录开发者/团队的能力前史、现金流、团队结构、技术路线、范围控制、失败、市场路径与偶然性。
2. **可证伪的命题库**：检验关于独立游戏的流行解释，例如“福利国家优势”“富二代优势”“大厂履历必要”“solo 等于一个人包办全部”“零营销”“纯靠运气”等。
3. **最终书稿《独立游戏英雄传说》**：在证据积累之后，把案例与命题组织成可读的生产史，而不是先写故事再找证据装饰。

## 研究结构

本仓库不以“章节”作为最小研究单位，而以 **Case（案例）**、**Claim（命题）** 与 **Evidence（证据记录）** 为核心。

- [`cases/`](cases/)：开发者 / 团队 / 项目的可审计案例档案
- [`claims/`](claims/)：可被支持、削弱或证伪的研究命题
- [`schemas/case-template.md`](schemas/case-template.md)：Case 标准结构
- [`schemas/claim-template.md`](schemas/claim-template.md)：Claim 标准结构
- [`schemas/evidence-record-template.md`](schemas/evidence-record-template.md)：Evidence 核实结构
- [`AGENTS.md`](AGENTS.md)：适用于 GPT / Codex、Reasonix、DeepSeek 等代理的研究宪法

一个 Case 可以同时支持或反驳多个 Claim；一本书的章节应当从证据网络中长出来，而不是反过来要求证据服从预先写好的叙事。

案例统一关注：

**Myth / Origin / Capability / Runway / Production / Scope / Failure / Market / Environment / Luck / Verdict / Transfer / Non-transfer / Evidence**

## 研究立场

本项目的默认前提不是“环境不重要”，也不是“只要努力就能成功”。相反：

- 环境决定行动集合与失败成本；
- 能力决定一个人能把多少资源转化成产品；
- 生产组织决定项目能否活到随机机会到来；
- 市场与运气影响右尾结果；
- 优秀独立开发者的重要能力之一，是**拒绝继承不适合自己的成本结构，并主动制造可生存的生产条件**。

因此，本项目同时记录帮助与阻碍，既不抹去福利、家庭、伴侣收入、储蓄、低成本地区、发行商、众筹、外包、平台红利等外部条件，也不把这些条件自动解释成成功的充分原因。

## 首批研究对象

第一轮先建立六个案例骨架，用来覆盖不同的生产结构，而不是因为它们必然是“最伟大的六款独立游戏”：

- [`CASE-001 FTL / Subset Games`](cases/CASE-001-ftl.md)
- [`CASE-002 Rocket League / Psyonix`](cases/CASE-002-rocket-league.md)
- [`CASE-003 Papers, Please / Lucas Pope`](cases/CASE-003-papers-please.md)
- [`CASE-004 Stardew Valley / ConcernedApe`](cases/CASE-004-stardew-valley.md)
- [`CASE-005 Dwarf Fortress / Bay 12 Games`](cases/CASE-005-dwarf-fortress.md)
- [`CASE-006 R.E.P.O. / semiwork`](cases/CASE-006-repo.md)

这些文件目前只是研究问题骨架，不代表仓库已经接受任何关于其资金、团队、营销或成功原因的结论。

## 工作原则

- **证据先于叙事。** 先建立时间线、来源与反证，再写故事。
- **证伪优先。** 每个重要命题都要主动寻找反例、替代解释和缺失变量。
- **一手资料优先。** 开发者同期访谈、演讲、开发日志、众筹页、公司资料、财务/法务记录等优先于多年后的二手神话。
- **区分必要、充分与概率增益。** “不是必要条件”不等于“没有影响”。
- **拒绝幸存者偏差。** 成功者做过某件事，不意味着那件事导致成功。
- **把前史算进开发史。** 技能、旧项目、失败原型、合同工作和职业经验不因“正式开工日”而消失。
- **不把术语当事实。** `solo dev`、`zero marketing`、`three-person team` 等必须拆开核验。

## 当前阶段

**Phase 1 — Research Skeletons**

项目宪法、证据规则、Case / Claim / Evidence schema 与首批六个案例骨架已经建立。

下一阶段不是写第一章，而是：

1. 为六案建立时间线与来源队列；
2. 逐条生成 Evidence Records；
3. 用证据更新 [`claims/README.md`](claims/README.md) 中的初始命题状态；
4. 等事实网络稳定后再开始长篇叙事。

## 权利与许可

本仓库不是公共领域项目，也不是开放内容项目。

- 本仓库的原创研究、文字、案例分析、命题矩阵、原创表格、书稿和其他非软件原创内容，除非文件另有明确说明，均为 **© 2026 洪荒行者。All Rights Reserved.** 详见 [`LICENSE-CONTENT`](LICENSE-CONTENT)。
- 明确位于软件/工具范围内的脚本、构建工具、检查器等代码，按 [`LICENSE-CODE`](LICENSE-CODE) 的 MIT License 授权。
- 引用、截图、商标、采访内容及其他第三方材料仍属于其各自权利人；本项目不会因为引用它们而取得重新授权的权利。

公开可读不等于放弃版权。合理引用、评论、研究及适用法律规定的其他例外不受上述声明限制。
