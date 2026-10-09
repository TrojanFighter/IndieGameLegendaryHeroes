# Cross-model narrative trial — 实验记录（Kenshi，第 1 关）

> 本文件是审阅记录，**不属于候选正文**，也不属于正式书稿或 canonical 档案。按 PR #292 任务书 §五保留模型身份与元数据。

- **试验：** PR #292 第 1 关（Kenshi），独立片段试写。
- **作者模型 A：** Reasonix agent。**底层模型标识：UNKNOWN**（本次环境未确认确切模型版本，不虚构 provider/版本对比）。
- **日期：** 2026-10-09（任务书日期）。
- **提示词版本：** PR #292 §四 提示词原文直接使用；未新增 Humanizer、禁词表、模式评分或模板校对 Gate。
- **事实包锁定（快照）：**
  - `cases/CASE-012-kenshi.md`、`evidence/CASE-012-kenshi-source-ledger.md` @ `693b3de29b75f0c30e61c3cdbbdaebe16b72b583`（PR #288 head）。
  - 本地基线：`main` @ `be84e31`。
  - 原始来源：GameSkinny 2017（E003）、Siliconera 2015（E001）、Lo-Fi Games Fact Sheet（E002）、Reddit r/IAmA 2019（E007）。
- **候选正文文件：** `cross-model-narrative-trial-2026-10-09-kenshi-candidate-a.md`。
- **正文字数：** 914 汉字（含标点非空白 1135），落在 800–1300 区间。
- **是否阅读其他模型候选稿：** **否。** 未读 PR #283 / #284 / #285 / #289 的任何候选段落，未读 `book/profiles/kenshi.md` 或本库任何成篇人物稿；未模仿既有 Profile 结构。
- **是否真人盲评：** **否 — `NOT TESTED`。**
- **是否宣称达出版质量：** **否。** 本候选仅供作者与其他模型匿名比较。

## Fact Lock（事实锁，非正文）

- **佣兵事件：** Chris Hunt 2017 访谈口述，游戏内模拟 bug 的连锁示例，**不是现实事件**；只保留 Hunt 描述的行为链（民宅误判 → 屋主动手 → 守卫介入 → 同伙卷入 → 全镇混战），不补旁观者动作、对白或情绪。
- **单人期：** 前五六年全职 solo + 最低工资夜班保安（E001，2015 时点口径）。**不写“一人十年”。**
- **职业前史：** 二十出头做游戏程序员，厌恶小 cash-cow 项目；2008 年离职（E002）。
- **收入顺序：** 2013 Greenlight 前自家网站 alpha 销售已支持本人与 freelancers；Steam Early Access 收入用于组队（E001 + E002）。不倒写为“Steam 才带来全部玩家收入”。
- **回忆时点：** “十八岁才弄明白做游戏”属 2019 AMA 回忆（E007）；“C++ / 自拼引擎”属 2017 回忆（E003）。
- **UNKNOWN（未写）：** 家庭与住房、精确储蓄与夜班排班、逐年 headcount、EA 收入金额与销量时间线、完整 contributor perimeter。

## 遗留 / 待裁决

- 结果状态待作者盲读后判定：`KEEP_EXISTING` / `REVISE` / `SELECT_AS_PILOT`。
- 独立事实审稿（可由其他模型或 Lane B 执行）尚未进行；本记录不构成事实通过。

## 修订稿 v2（作者模型 A）

- **文件：** `cross-model-narrative-trial-2026-10-09-kenshi-candidate-a-rev2.md`。
- **修订依据（v1 编辑自评）：** ①两节起手同为“格言式总括 + 展开”，节拍重复；②“公开销售之后”一段缺真实摩擦，整体过于平滑；③结尾仍有“不是……而是……”式归纳。
- **处理：** 小节 1 改为事实起手（“Kenshi 的前五六年……”），小节 2 改为人物动作起手（“第一个进来的程序员叫 Sam……”）；补入 Ledger E004 / E005 / E006 已核的摩擦材料（Early Access 稳定性压力、更新间隔期的玩家不信任、引擎老化、长 bug 清单与评论、自压工资）；结尾以具体事实收束，不再替读者归纳。
- **正文字数：** 958 汉字（含标点非空白 1206），与 v1 均在 800–1300 区间。
- **是否真人盲测：** 否 — `NOT TESTED`。
- **版本保留：** v1 与 v2 并存，供作者（及另一模型版本）比较；不覆盖、不删改 v1。

## 修订稿 v3（针对 Lane A 指出的漂移，作者模型 A 自我修正）

- **文件：** `cross-model-narrative-trial-2026-10-09-kenshi-candidate-a-rev3.md`。
- **触发：** PR #294 `book/EDITORIAL-CROSS-MODEL-ROLLOUT-2026-10-09.md` §1 与 §6 对 A v2 的评审——“口述的模拟系统 Bug 被添入动作／时间细节；Hunt 认为混乱是开发问题的态度可能在翻译中被改变”，以及“先复核……动词、Hunt 引语立场、bug 时点与薪水时间范围”。
- **修正条目（逐条对照原始来源）：**
  1. 开场动作贴回 E003 原文动词链，删除“推门”“吓了一跳”“抄起家伙”“随后赶到”等原文未给的细节；
  2. 正文补回 Hunt 的立场——他把模拟世界的混乱称作“最大的问题”（`The biggest problem is the sheer chaos of a simulated world.`），不再只当作轻快轶事；
  3. 删除把佣兵 bug 放进“挂上去卖之后”的时序暗示（E003 未给时点）；
  4. “Steam 上线 Early Access 之前”改回 E001 的锚点“通过 Steam Greenlight 之前”；
  5. “压得他不想看”改回 E006 的 `could be discouraging`（去具体心理）；
  6. 薪水句限定为“2018 年那次采访”，去掉“一直”这一无依据的时间范围。
- **正文字数：** 938 汉字（含标点非空白 1192）。
- **性质与边界：** 这是 writer 自我修正，**不替代独立 fact-checker**；不得据此宣称漂移已全部修复或通过。仍需 Lane B／独立审稿逐句回读。
- **版本保留：** v1 / v2 / v3 三版并存，供作者与独立模型 B 比较；不覆盖、不删改前两版。
