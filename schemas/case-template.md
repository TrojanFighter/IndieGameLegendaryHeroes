# Case Schema

每个 Case 是一个开发者、团队、工作室或项目的可审计研究档案。不要把 Case 直接写成书稿章节。

从 `CASE-027` 起，新建 Case 默认使用 **Case Schema v2**。v2 的核心新增要求是：不能只记录“谁做了什么”，还必须把行动放回当时可用的技术、平台、资本和组织条件中解释。

详细方法见：[`context-situation-action.md`](context-situation-action.md)。

## Machine index requirement

每个 `cases/CASE-*.md` 都必须在 [`../metadata/cases.json`](../metadata/cases.json) 中登记一次，至少包含：

- `case_id`
- `file`
- `subject`
- `research_status`: SKELETON / RESEARCHING / REVIEW / STABLE
- `evidence_strength`: none / low / medium / high
- `explanatory_importance`: unrated / low / medium / high / critical
- `narrative_value`: unrated / low / medium / high / critical
- `related_claims`
- `tags`
- `last_verified`
- `evidence_ledger`
- `contributor_audit`: pending / partial / complete / not_applicable
- `market_access_audit`: pending / partial / complete / not_applicable

Schema v2 另外必须包含：

- `schema_version`: `2`
- `context_audit`: pending / partial / complete

正文负责研究事实与论证，metadata 只负责机器索引；两者必须通过 lint 保持一致。

### Audit gate

以下三类神话必须在 Case 进入成熟状态前完成独立审计：

1. **Contributor audit**：凡带 `solo` / `micro-team` / `three-person-team` 等标签，必须核外包、音乐/音效授权、商店素材、QA、移植、本地化、发行商支持、平台支持，以及家庭/伴侣提供的非开发支持。
2. **Market-access audit**：凡关联 `C010` 或 `market-access` 标签，必须核商店页、demo、节庆、众筹、开发日志、社区、媒体、主播、平台推荐、publisher、既有粉丝与定价/EA，而不能把“无广告预算”写成“无营销”。
3. **Context audit / CSA**：必须核当时实际存在的技术、发行、协作、支付、融资与发现条件，以及创作者当时的技能、现金流、义务、网络与替代方案；再记录他们在这些约束下做出的具体行动。禁止用后来才出现的工具或市场条件评价早期案例。

`REVIEW` / `STABLE` 案例若属于前两类范围，相应 audit 必须为 `complete`；所有 Schema v2 Case 在进入 `REVIEW` / `STABLE` 前，`context_audit` 必须为 `complete`。

## Header

Schema v2 推荐 frontmatter：

```yaml
---
type: case
schema_version: 2
case_id: CASE-027
status: RESEARCHING
subject: "Example / Studio"
related_claims: []
evidence_strength: MEDIUM
explanatory_importance: HIGH
narrative_value: HIGH
context_audit: PENDING
last_verified: 2026-10-04
---
```

正文头部继续保留：

- Case ID:
- Subject:
- Related games:
- Period covered:
- Research status: SKELETON / RESEARCHING / REVIEW / STABLE
- Last verified:
- Related Claims:

## 1. Myth

流行叙事怎样概括这个案例？逐条记录，不立即接受。

## 2. Context–Situation–Action Snapshot

这一节不是泛泛的“时代背景”，而是为了回答：**在当时可行的选择集合中，这个作者为什么采取了这一步？**

### Era / Production Regime

至少记录与本案关键决策直接相关的：

- 年代与关键窗口；
- 当时可用的引擎、middleware、硬件、版本控制与资产工具；
- 数字发行 / 实体发行 / shareware / portal / Steam / mobile / UGC 平台处于什么阶段；
- 当时的 discoverability：媒体、论坛、平台首页、主播、算法推荐、节庆、邮件列表等；
- 协作条件：同地办公、IRC/论坛、云协作、远程工具、外包市场；
- 融资与收款条件：工资、信用、众筹、Early Access、平台分成、publisher、grant、支付基础设施；
- 可获得的人才 / 素材 / middleware 生态；
- 自动化与 AI 工具是否存在、成熟到什么程度；
- **后来很常见、但当时尚不存在或昂贵得不可用的东西。**

### Actor Situation

在关键决策发生时，作者 / 团队具体处于什么位置：

- 已有技能与旧代码 / 工具 / IP；
- 工作状态与收入来源；
- runway 与 burn；
- 家庭责任、住房、医疗、签证等现实约束；
- 地理位置与本地成本；
- 既有受众、媒体身份、社区关系、行业网络；
- 核心团队与可调用外围资源；
- 当时真正可选的替代方案。

### Action / Maneuver

不要写“坚持”“努力”“有创意”这类抽象词。写具体动作：

- 辞职 / 不辞职；
- 选某个低负担工作换连续开发时间；
- 先接合同工养原创；
- 砍多人 / 砍 3D / 砍内容量；
- 先做前置产品积累技术与现金流；
- 先做免费 demo / public alpha；
- 用 Greenlight / Kickstarter / Early Access / grant / publisher pitch 购买下一阶段 runway；
- 改定价、改商店呈现、改 onboarding；
- 选择某种引擎、发行方式或团队结构。

每个关键转折尽量记录成一个 Decision Unit：

| 时间/窗口 | 时代条件 | 作者处境 | Binding constraint | 具体行动 | 直接结果 | Evidence | Transfer boundary |
|---|---|---|---|---|---|---|---|

### Anachronism Check

至少回答一次：

> 如果把今天常见的工具、平台、融资或传播方式拿掉，这个行动还是否合理？

禁止：

- 用 2026 年的 Unity/Godot/AI/Discord/Steam Direct 生态去责备 1990s/2000s 开发者“为什么不这么做”；
- 把后来的市场窗口倒写成作者当时已经知道；
- 把技术后来普及等同于当时已低成本可得；
- 把今天的成功路径直接投影回过去。

## 3. Origin

- 教育与训练：
- 此前职业：
- 地理位置与生活成本：
- 家庭/伴侣/社会支持：
- 进入本项目之前的重要经历：

## 4. Capability

开工之前已经具备什么能力？

- 编程 / 工程
- 设计
- 美术
- 音乐 / 音效
- 写作
- 制作 / 项目管理
- 商务 / 市场
- 社群 / 媒体
- 旧代码 / 工具 / 素材 / IP

## 5. Runway

按时间记录生存来源，不把 Kickstarter 或发行预付款直接等同总预算。

| 时段 | 来源 | 金额/口径 | 证据 | 置信度 |
|---|---|---|---|---|

同时检查：储蓄、工资、兼职/合同工、伴侣/家庭、前作收入、众筹、发行、平台款项、补助/奖金。

## 6. Production

- 核心创作团队：
- 同期全职团队：
- 峰值团队：
- 累计 contributors：
- 外包/合同工：
- publisher / platform support：
- 工具链：
- 工作地点与组织方式：

## 7. Scope

- 最初问题是什么？
- 哪些需求被删掉？
- 哪些复杂度被转移到工具、表现层、玩家行为或程序生成？
- 最终为何变成“他们做得完的问题”？

## 8. Failure

- 前作失败：
- 废弃原型：
- 返工：
- 现金流危机：
- 团队冲突：
- 技术危机：
- 接近放弃的节点：

## 9. Market

不要把“无广告预算”写成“无营销”。

- 商店页：
- demo：
- 节庆/展会：
- 众筹：
- 开发日志：
- Discord / 社区：
- 媒体：
- 主播 / YouTube：
- 平台推荐：
- publisher：
- 既有粉丝：
- 定价 / 折扣 / EA：

## 10. Environment

分别记录帮助与阻碍：

- 住房 / 家庭资产
- 医疗 / 福利
- 再就业能力
- 地区成本
- 监管 / 准入
- 融资
- 平台 / 支付
- 全球发行
- 语言 / 媒体
- 行业人才结构

注意：`Environment` 是长期结构条件；`Context–Situation–Action` 是把某个**具体决策点**放回当时的可行选择集合。两者不能互相替代。

## 11. Luck

只记录团队无法直接控制、但对结果有实质影响的事件。不要用“运气”代替未知因果。

## 12. Verdict

逐条回到 Myth：

- 成立：
- 部分成立：
- 夸大：
- 无法验证：
- 被证伪：

## 13. Transfer

哪些是其他独立开发者可以尝试迁移的生产决策？写适用条件。

迁移时必须注明：**原案例的时代技术条件与今天是否相同。** 如果机制依赖已经消失的窗口，只能迁移上位原理，不能照抄动作。

## 14. Non-transfer

哪些依赖个人能力资本、特殊关系、时代窗口、资本、地区条件或偶然性？

## 15. Evidence Index

只列 Evidence ID 与一句说明；完整核实信息放 evidence/。

Evidence 在 Claim metadata 中引用时必须使用全局可解析格式：

`CASE-001:E001`

不要只写 `E001`，因为不同 Case 可以各自拥有 `E001`。

## 16. Creator Life / Decision Audit

当 Case 需要进入“人生性价比”横向比较时，按 [`creator-life-decision-audit.md`](creator-life-decision-audit.md) 增补统一字段：

- Audit status；
- Life stage；
- Household；
- Runway；
- Household burn；
- Exit / recovery；
- Capability vector；
- Problem ownership；
- Validation architecture；
- Reality adjudication；
- Capability capture risk；
- Market sufficiency / legibility；
- Capability scaling；
- Major unknowns。

这不是 Schema v2 的强制事实补齐项；没有来源时必须写 `UNKNOWN`。历史 Case 不得在库运维中凭常识补家庭、收入、婚育、房贷等事实。

只有完成最低可比记录的 Case，才可用于回答“这种人是否适合辞职 / 创业 / 做几年独立游戏”一类 reader-facing 问题。

## 16.5 Sampling Origin / Visibility Check（用于跨案例研究）

当 Case 被用来评估“名校毕业生/大厂员工/某国家创作者通常怎样”时，必须在研究笔记或 Case 对照中明示：**它是怎样被发现的**。

- MEDIA_FEATURED / PUBLIC_UNFEATURED / INSTITUTIONAL_FRAME / UNKNOWN；
- 是否因为 commercial success / awards / public failure / founder media interview 而入选；
- 该个案是说明可能机制，还是来自含失败/未发布项目的独立抽样框；
- 受访时间与重大成功/失败节点先后；
- 缺少哪一层分母，故哪些频率、国别推断被禁止。

执行 [Creator Visibility / Sampling Gate](creator-visibility-sampling-gate.md)。

不要求凭空为现有全部 Case 填个人取样字段；也不把此 Gate 伪装成已完成全库代表性校正。在无法建立 population frame 时保留 purposive biography 模式。

## 17. Open Questions

尚未解决的问题。重要空白必须保留，不准模型自行填平。

## 2026-10-09 Technology Window Audit｜全案必审

所有63个旧Case已建立[技术分代与验证阶梯初步补录](../metadata/technology-opportunity-window-matrix.md)。今后创建或重新核验任何 Case，必须依[独立规范](technology-opportunity-window-audit.md)记录：最早原型时的**实际**可得引擎/中间件；自研、借用旧资产与模块采购的边界；网络及服务器义务；Mod/Roblox/UEFN/Steam等平台如何验证真实体验；外包与完整FTE年；当时尚不存在或不可负担的工具；以及`CREATED/INHERITED/RECOMBINED/PLATFORM_UGC/CO_EVOLUTION/UNKNOWN`可重叠分类。

**不强制经过Mod→融资→Standalone**；未能核实技术栈/插件时写UNKNOWN。每个Case附录是initial backfill，不把分类或2026年可用工具倒填成已核史实。已有 `metadata/cases.json` 的正式状态字段暂不扩充，避免造成metadata lint失败。

