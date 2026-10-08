# 002 — 台湾×大陆：人物命运与非明星样本的可比研究设计

- Status: PRE-REGISTERED DESIGN / FIRST INTAKE / PUBLIC-ATTEMPT & SELECTED-FINALIST COHORT PILOTS COMPLETE / POPULATION DENOMINATORS OPEN
- Program: C comparator + A biography linkage
- As of: 2026-10-07
- Method: [媒体可见性与分母协议028](../../book/research-notes/media-selection-survivorship-and-denominator-protocol-028.md)、[大陆GGJ公开项目试点](../china/002-ggj-2024-shenzhen-nanshan-public-attempt-pilot.md)
- Restriction: 台湾是有意义的**自然比较**，不是除社会制度外所有变量相同的实验组。

## 一、同步比较单元与年份

| 研究层级 | 台湾侧观察对象 | 大陆侧匹配规则 | 必须控制的变量 |
| --- | --- | --- | --- |
| 1985—2005 产业公司 | 原创单机开发商、代理商、兼营者 | 同年代的单机公司/代理商/网游商 | 定价、市场规模、盗版、发行、外资、跨地区所有权、技术代际 |
| 2000—2015 开发岗位 | 程序/策划/美术/运营等岗位 | 同时段、相近履历和公司类型的岗位 | 角色、学历、年龄、工作制、收入/住房、公司权益与IP限制 |
| 2013—2026 作者团队 | 完成/未完成的具体独立项目 | 相似核心规模、前置能力、品类及平台 | 家庭runway、薪资/储蓄、原型年份、节庆、语言与销售渠道 |
| 2024 固定起点公开队列 | GGJ台湾单一站点或G-EIGHT完整名册 | GGJ 2024深圳南山或同类固定站点 | 入场门槛、作品 vs 团队定义、是否自选报名、国际参与者 |

禁止：以台湾市场2024某个展会100余**参展团队**对照深圳GGJ 16个**公开目录listing**直接算比例。两个是不同抽样框和不同单位。

## 二、固定起点（不从销量榜倒推）

**台湾Frame B1（优先测试）**：2024 Global Game Jam台湾某个在官网有完整 Games目录的站点。先检查官网是否能提供每条永久URL及清晰作品数。暂不预选任何站点，不声称已有分母。与深圳试点对照时，要先核查年龄、城市、线上/线下、主办方资源、提交/删除规则是否可比。

**台湾Frame B2（备份）**：2024 G-EIGHT官方完整参展档/游戏目录。主办方2024官方宣传称「超过100组台湾独立游戏开发团队」；官方年度回顾称「超过130组参展团队及公司，近200款游戏」。两种数值都是**不同总体与单位**：前者为台湾独立开发团队，后者混合创作者与企业，且游戏款数不是开发者人数。2024回顾页面部分计数器呈0，应舍弃这些不稳定UI数字；实际逐项、可去重的原始参展名册尚未取得，`denominator_status: UNKNOWN`。来源：
- G-EIGHT 2024同期官方新闻：https://geight.io/geight-official/g-eight-2024%E5%94%AE%E7%A5%A8%E6%AD%A3%E5%BC%8F%E9%96%8B%E8%B7%91%EF%BC%81%E5%9C%8B%E9%9A%9B%E7%8D%A8%E7%AB%8B%E9%81%8A%E6%88%B2%E8%88%87%E5%8F%B0%E7%81%A3%E5%89%B5%E6%84%8F%E5%8C%AF%E8%81%9A/
- 主办方2024回顾：https://geight.io/en/2024-g-eight-recap/

为所有选入项目保留统一字段：`cohort_id`、`original_listing_url`、`item_type`、`team_duplicate_status`、`selection_rule`、`first_public_trace`、`post_event_release`、`update_visibility`、`career_observability`、`success_or_failure_known`、`UNKNOWN`。未查到发售 ≠ 失败，未找到个人履历 ≠ 没有创作经历。

## 三、人物研究序列：先问题，后名气

1. **《活侠传》原始鸟熊** — 长期私人关系、能力互补、移动弹幕玩法到武侠RPG pivot；优先核两人创业前职业、家庭runway、退出选项、团队外围及2020/2021成立年份口径冲突。作为小团队 `CAPABILITY-COMPOSED` 压力样本。初步原始资料入口：https://game.udn.com/game/story/122090/8098442 、https://2025.tgdf.tw/en/speakers/8 。采访未转为正式Case/Evidence，须先逐条阅读。
2. **《文字游戏》Team9** — 平面/展览/前端/文学/营销的组合是否改变了项目形式和发行选择；明确哪些关键技能其实早已掌握，而非从零开发；核共同创作者贡献与商业支持。入口：https://www.incgmedia.com/all-articles/word-game-interview 、https://2022.tgdf.tw/en/speakers/wenhan_chang_team9 。
3. **《返校》→《还愿》→《九日》赤烛** — 单次成功后重新配置自有资金、众筹、社区资产和战斗研发能力；避免用早期团队规模等同后来的成熟生产。入口：https://shop.redcandlegames.com/zh-TW/projects/ninesols 。
4. **失败/沉默对照** — 与前三者同届的公开GGJ参赛者、G-EIGHT普通参展者、停更但不能确定已放弃的开发者、传统单机工作室失业/转岗者。须从固定名册或同期报道选取，不能只找媒体报道过的知名失败者。

对每位人物，使用 [Creator Life / Decision Audit](../../schemas/creator-life-decision-audit.md) 和 [Capability–Project Fit](../../schemas/capability-project-fit-audit.md)，记录家庭与经济限制、首次独立创作、当时可选职业、本人拥有的能力、首次玩家信号、项目范围变化、失败或退出选项、来源时间效力。

## 四、提前登记的可证伪命题（H，不升级Claim）

- **TW-CN-H01：原创研发的商业回报空间由发行权、代理与渠道分配共同塑造。** 反例方向：台湾同年代仍稳定自研者及大陆在相似渠道制度下成功原创者。
- **TW-CN-H02：更早面向海外市场会改变作者选择，但不必然提高成功率。** 必须有地域收入结构、发行版本、目标语言、实际销售；“台湾本土小”不是因果证据。
- **TW-CN-H03：家庭/教育门控可能早于职业入场，导致公开创作者样本先天选择偏差。** 须尽量构建学生/课程/社团全体起点，而不只采访成功毕业生。
- **TW-CN-H04：非游戏职业的复合能力通过Problem Redefinition形成非常规独立项目。** 反例是同类职业背景的大量未发售/商业失败项目。

大陆镜像入口：[中国013 — 创作者生命周期与资本接口](../china/013-creator-lifecycle-capital-interface-taiwan-mirror.md)。当前仅比较机制，不计算两岸获得资金/公司化/发售概率。

## 五、阻断条件与下一步

- 在 Taiwan cohort 名册完成去重、清楚区分个人/团队/项目及缺失率之前，**不做两岸独立创作者发生率或成功率对比**。
- 在原始合同或开发者本人资料不足前，不凭公司宣传猜出「家庭支持」「IP拥有」「融资控制权」。
- 下一轮优先：①核台湾GGJ2024站点及完整参赛作品目录；②追回1998—2004 MIC原始市场报告以解决统计口径；③正式阅读《活侠传》《文字游戏》同期人物采访，建立个人关键决策时间线及UNKNOWN表。
- 暂不发放新的正式CASE编号；先形成可审计人物evidence intake并完成反例选样。
