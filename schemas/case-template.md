# Case Schema

每个 Case 是一个开发者、团队、工作室或项目的可审计研究档案。不要把 Case 直接写成书稿章节。

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

正文负责研究事实与论证，metadata 只负责机器索引；两者必须通过 `tools/research_lint.py` 与 `tools/research_evidence_lint.py` 保持一致。

### Audit gate

以下两类神话必须在 Case 进入成熟状态前完成独立审计：

1. **Contributor audit**：凡带 `solo` / `micro-team` / `three-person-team` 等标签，必须核外包、音乐/音效授权、商店素材、QA、移植、本地化、发行商支持、平台支持，以及家庭/伴侣提供的非开发支持。
2. **Market-access audit**：凡关联 `C010` 或 `market-access` 标签，必须核商店页、demo、节庆、众筹、开发日志、社区、媒体、主播、平台推荐、publisher、既有粉丝与定价/EA，而不能把“无广告预算”写成“无营销”。

`REVIEW` / `STABLE` 案例若属于上述范围，相应 audit 必须为 `complete`。

## Header

- Case ID:
- Subject:
- Related games:
- Period covered:
- Research status: SKELETON / RESEARCHING / REVIEW / STABLE
- Last verified:
- Related Claims:

## 1. Myth

流行叙事怎样概括这个案例？逐条记录，不立即接受。

## 2. Origin

- 教育与训练：
- 此前职业：
- 地理位置与生活成本：
- 家庭/伴侣/社会支持：
- 进入本项目之前的重要经历：

## 3. Capability

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

## 4. Runway

按时间记录生存来源，不把 Kickstarter 或发行预付款直接等同总预算。

| 时段 | 来源 | 金额/口径 | 证据 | 置信度 |
|---|---|---|---|---|

同时检查：储蓄、工资、兼职/合同工、伴侣/家庭、前作收入、众筹、发行、平台款项、补助/奖金。

## 5. Production

- 核心创作团队：
- 同期全职团队：
- 峰值团队：
- 累计 contributors：
- 外包/合同工：
- publisher / platform support：
- 工具链：
- 工作地点与组织方式：

## 6. Scope

- 最初问题是什么？
- 哪些需求被删掉？
- 哪些复杂度被转移到工具、表现层、玩家行为或程序生成？
- 最终为何变成“他们做得完的问题”？

## 7. Failure

- 前作失败：
- 废弃原型：
- 返工：
- 现金流危机：
- 团队冲突：
- 技术危机：
- 接近放弃的节点：

## 8. Market

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

## 9. Environment

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

## 10. Luck

只记录团队无法直接控制、但对结果有实质影响的事件。不要用“运气”代替未知因果。

## 11. Verdict

逐条回到 Myth：

- 成立：
- 部分成立：
- 夸大：
- 无法验证：
- 被证伪：

## 12. Transfer

哪些是其他独立开发者可以尝试迁移的生产决策？写适用条件。

## 13. Non-transfer

哪些依赖个人能力资本、特殊关系、时代窗口、资本、地区条件或偶然性？

## 14. Evidence Index

只列 Evidence ID 与一句说明；完整核实信息放 evidence/。

Evidence 在 Claim metadata 中引用时必须使用全局可解析格式：

`CASE-001:E001`

不要只写 `E001`，因为不同 Case 可以各自拥有 `E001`。

## 15. Open Questions

尚未解决的问题。重要空白必须保留，不准模型自行填平。
