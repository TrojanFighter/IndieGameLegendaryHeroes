# Claims Index

本文件登记可证伪命题及其当前证据状态。`SUPPORTED` 只表示已有多源/跨案例支持，仍不等于普遍规律或因果定论。

| Claim ID | 暂定命题 | 当前状态 |
|---|---|---|
| C001 | 家庭资产、福利与社会安全网会降低独立开发失败成本，但不是成功的充分条件 | UNVERIFIED |
| C002 | 可持续 runway 比单次融资金额更能解释小团队能否把项目做完 | SUPPORTED |
| C003 | 极小团队/OPC 往往是长期能力资本积累后的外在表现，而非“从零突然一人全能” | SUPPORTED |
| C004 | 优秀独立开发者的重要能力之一，是主动制造自己的生产条件而不是继承行业标准成本结构 | SUPPORTED |
| C005 | 合同工作、外包或服务业务可以作为原创项目的交叉补贴机制 | SUPPORTED |
| C006 | 大厂经验对独立游戏成功可能提供能力资本，但并非普遍必要条件 | SUPPORTED |
| C007 | Solo / 小团队的核心优势之一不是复制大团队，而是重新定义问题空间与表现成本 | SUPPORTED |
| C008 | 数字发行、通用引擎、资产市场、远程协作与全球平台降低了地理位置对独立开发的部分约束，同时提高了竞争与可见性压力 | UNVERIFIED |
| C009 | 错误的世界模型本身会成为生产损失，例如把“必须有大团队/大预算/发行商”误当成自然规律 | UNVERIFIED |
| C010 | 市场接入是生产系统的一部分；“零营销”常常只是“零广告预算”的误记 | SUPPORTED |
| C011 | 成功案例的“正式开发周期”经常系统性低估了此前技能、旧项目、工具与失败原型的积累时间 | SUPPORTED |
| C012 | 同一环境变量对不同能力结构的开发者作用不同，不能用国家/福利/资本条件单变量解释独立游戏产出 | UNVERIFIED |
| C013 | 商业游戏训练会积累可迁移的生产能力，同时也会使个人与组织专业化于特定 objective function；跨 production regime 的表现取决于能力与新目标的适配、decision rights 与 deliberate unlearning，而不能由“大厂经验/岗位名称”单独预测。 | WEAK |
| C014 | 在高不确定度的 0→1 游戏生产中，较短的 time-to-player-truth 与“证据增强后再升级资源”的 escalation discipline 会降低单次方向错误的持续成本；当多人生态、内容 obligation、团队与资产规模在核心假设充分验证前升级时，error persistence cost 会显著上升。 | SUPPORTED |
| C015 | 在资源受限的作者型游戏中，一部分高价值项目不是先确定“完整游戏愿景”再被迫缩小，而是主创先识别自己的不对称能力、已知弱项与可获得外围资源，再反向选择或重写项目，使核心体验主要由强项产生，并把弱项相关的高成本 obligation 删除、抽象、复用或外围化；这种“能力反向立项”本身是一种设计能力，而不只是项目管理。 | SUPPORTED |

## 使用规则

- 新 Claim 必须满足 [`../schemas/claim-template.md`](../schemas/claim-template.md)。
- 任何 Claim 升级为 SUPPORTED / VERIFIED 前，必须主动记录反方证据与禁止推论。
- 若命题过大，应拆分而不是用更多形容词掩盖不可证伪性。
- 不要因为某个案例“很像”某个 Claim 就记为证据；先建立 Evidence Record。
- 当前跨案例综合、反例与边界见 [`CROSS-CASE-READINGS.md`](CROSS-CASE-READINGS.md)。
- 证据成熟度、解释重要性、叙事价值、Related Cases 与 Evidence IDs 的机器索引见 [`../metadata/claims.json`](../metadata/claims.json)。
- 本表是人读索引；CI 会检查命题文本与状态是否和 metadata 一致。
