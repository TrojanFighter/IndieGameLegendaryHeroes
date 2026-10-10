# 跨模型协作与书稿质量整顿：一轮外部审查及其处置建议

© 2026 洪荒行者。All Rights Reserved.

- Scope: PR #311–#314、Issue #315 的收口；Gunpoint / Kenshi / Zach Barth / early id–DOOM / Limit Theory 五篇 reader prose 的独立诊断；工作流治理审查
- Status: EXTERNAL REVIEW NOTE / NO NEW CLAIM / NOT CANONICAL EVIDENCE
- Author: Reasonix（独立审查会话），提交待作者验收
- Reviewed: 2026-10-10
- Baseline: 审查开始时 `main @ 0f75dd4`、`editorial/chapter-copy-lint-20261009 @ e7b509e`；审查过程中 main 被 pull 前移至 `00945b7`
- Excludes: 私人项目材料；不新增 Case / Evidence / Claim；不修改任何 canonical 事实

本文件是**外部审查意见**，不是事实源。它引用的每个 Case / Evidence / PR 结论，仍以对应文件的最新版原文为准。

---

## 0. 这份审查怎么做的

不是读网页摘要。本轮全部结论来自本地 git 对象与实跑：

| 动作 | 结果 |
|---|---|
| 本地对象比对 | #311–#314 四个 head（`e7b509e` / `74a6f21` / `bd546ca` / `1a64f1d`）本地均可用，因此 diff 是逐行读过的 |
| 文件重叠检查 | `editorial` 与 `main@0f75dd4` 两侧改动文件集合**交集为空** |
| 实跑审计工具 | `reader_evidence_sync_audit.py` 的 #311 版与 #312 版各跑一次，并另写探针统计字段覆盖率 |
| 实跑章节检查 | `chapter_copy_lint.py` 正常跑 + 注入泄漏做负向测试 |
| 直连原始来源 | 拉取 `theamphour.com/332` 的**发言归属转录**（HTTP 200，116KB）逐字核对 #313 / #314 |
| 全库检索 | 对 Limit Theory 的 2022 源码断言做 `rg` 全库核对 |

**审查期间 main 前移**（`0f75dd4` → `00945b7`，见 §1.3）。这本身是本轮要处理的问题类型的一个实例。

---

## 1. 收口

### 1.1 依赖关系（实测）

```text
main @0f75dd4 ──(10 commits, 全部 china/OPEN-QUESTIONS，与本轮文件零重叠)
      │
      └ a0a9830 ── editorial/chapter-copy-lint-20261009 @e7b509e   [#311: 29 commits, 44 files, +1527/-39]
                        ├── chatgpt/record-level-evidence-audit-20261010 @74a6f21   [#312: 3 files, +102/-27]
                        ├── research/zachtronics-primary-transcript-20261010 @bd546ca   [#313: 2 files, +46/-15]
                        │        └── editorial/zach-barth-interruption-candidate-20261010 @1a64f1d   [#314: 1 file, +13/-3]
```

editorial 领先 29 / 落后 10（开始审查时）；main 前移后落后 11。

### 1.2 重复修改

| # | 对象 | 证据 | 后果 |
|---|---|---|---|
| 1 | `tools/reader_evidence_sync_audit.py`、`book/EDITORIAL-GATE.md` | #311 与 #312 同时改 | stacked 正常；但 #312 重写了 #311 写进 Gate 的 "31/65" 段，**合并次序必须 #311 → #312**，否则该段回退 |
| 2 | CASE-012 / E001 | #311 自述与 `codex/gunpoint-life-history-evidence-20261009` 并行改同一份；`7ccdde4` 已吸收其 E001–E008 基线 | 该分支属**已回收未关闭**；同一 E001 有两个来源分支 |
| 3 | CASE-051 | #313 新增 `E011`，而 ledger 已有 `E006` = 同一期节目、同一 URL、同为 P1 | 同一来源被登记两次（见 §1.7） |
| 4 | `cases/CASE-059-slay-the-spire-mega-crit.md` | `main` blob `7857689` vs `origin/research/slay-spire-prestige-pipeline-026` blob `7717775` | **同名 Case 双线演化，内容不同** |

### 1.3 冲突文件

**审查开始时：文本冲突 0。** 但——

- **方向性风险**：main 的 10 个 commit 不在 editorial。「以 editorial 覆盖 main」会直接丢掉它们。**#311 只能 merge / rebase，不得 force。**
- **审查中新增的冲突面**：main 前移到 `00945b7`（`research(education): family-school agency…`），它修改了 `book/chapters/01-goals-are-made-not-found.md` 与 `book/BOOK-ARCHITECTURE.md` —— **这两个文件 editorial 分支也改过**。因此 #311 rebase 到最新 main 时，这两处需要人工确认（改动位置不同，git 多半能自动合并，但不能假设）。
- 这一条同时说明：#315 要求的"先确认基线再动手"在现实中很难维持——审查期间基线就动了。**建议在每次跨模型交付时把基线 commit 写进交接物**（`schemas/evidence-material-refresh.md` 已有此要求，但只在 Lane B 生效）。

### 1.4 尚未合入的有效成果（实测）

- editorial 分支内含：17 份 ledger 的逐字引语回填、`chapter_copy_lint.py`、`reader/`（277 行新 surface）、`EDITORIAL-GATE` 0.6、三个 schema 文件、`workflow-lanes` 跨模型交接章。
- **远程分支 219 个，其中 188 个不在 main**；只有 4 个有开放 PR。抽查确认含 main 中不存在文件的分支：

| 分支 | 新增文件 | 内容 |
|---|---|---|
| `research/yearly-production-capability-map-20261009` | 34 | `cross-industry/industrial-revolutions/` 观测字典 + CSV/SVG |
| `research/slavic-ecology-2026-10-07` | 44 | `country-studies/china/` 队列重构 |
| `chatgpt/jonas-tyroller-longitudinal-case-v2` | 110 | `.github/ISSUE_TEMPLATE/*`（与 main 同名不同版）与纵向 Case |
| `codex/gunpoint-long-life-narrative-20261009` | 5 | Gunpoint / Kenshi / early id 长篇候选稿 |

> 计数注意：`--diff-filter=A` 会**高估**。实测 `cases/CASE-059-…`、`.github/ISSUE_TEMPLATE/1-case-correction.yml`、`book/life-routes/big-company-veteran-to-author-001.md`、`author-corpus/AC-010-…` 都已在 main 中存在。因此清仓必须**逐文件比 blob**，不能按分支名或文件数判定。

### 1.5 PR 处置表

| PR | 处置 | 建议理由 |
|---|---|---|
| **#311** | **修正描述后，按 commit 分组 rebase 到最新 main 再合** | 内容大多是正面证据工作（17 份 ledger 逐字回填、CASE-012 事实修正）。但：①描述称 `book/profiles/kenshi.md`「未改」，实测该文件有 21 行改动——描述与 diff 不一致；②跨三 Lane 混在一条线，评审必须按 commit 走；③`reader/` 建议单独决策（§3.3）。**不要为了减少 PR 数量整支直推。** |
| **#312** | **修正后合并**（必须在 #311 之后） | 分母修正正确（实测 65 → 63）。但统计漏匹配、输出不可追踪（§1.6）。 |
| **#313** | **修正后合并；不要新增 Evidence ID** | 转录经直连核对，事实链成立。但 E011 与 E006 同源，且漏一个解释性节点（§1.7）。 |
| **#314** | **等 #313 定稿；建议 `REVISE_AGAIN`** | 忠实性总体合格，但新增段落偏长，profile 既有结构问题未处理。**不得自动合并。** |
| **#315** | **保留为唯一整合 Issue，更新基线** | 退出条件合理，但「重新核对所有分支」在 188 个未合并分支下不可完成 → 改为「清仓流程 + 抽查最高价值 5 条」。 |

### 1.6 #312 的统计与测试正确性

✅ 正确：分母 `evidence/*.md` 65 vs `CASE-*-source-ledger.md` 63（多出的正是 `README.md` 与 `research-material-ingestion-2026-10.md`）；`--strict` 只对 backlink / year 生效；`EDITORIAL-GATE` 的 31/65 口径纠错准确；3 个单测通过。

❌ **缺陷 1（漏统计）**：`SOURCE_CLASS_RE` 不匹配 markdown 粗体 `- **Class:**`。实测 **18 条记录**被跳过，其中 **15 条声明 P0/P1**。报告的 `P0/P1 records without a detectable long quote` 因此由 375 低估为实际 386（已在修正分支复现）。
样本：`evidence/CASE-016-early-id-software-source-ledger.md` E020–E031。

❌ **缺陷 2（不可追踪）**：只打印 `primary_no_quote[:12]`，按文件名序 ⇒ 报告顶部永远是 CASE-001 起，后面的 Case 永不出现。这不满足 #315 的「reproducible per-Evidence refresh queue identifies actual IDs」。

⚠️ **测试覆盖不足**：3 个单测只覆盖人造 `- Class:` 形状，没有真实 ledger 形状的 fixture，所以上述缺陷测不出来。

> 处理：修正分支见 PR「Audit: count bold `- **Class:**` tiers, and expose the whole queue」。

### 1.7 #313 的原始证据与时间线（已独立核对）

直连 `https://www.theamphour.com/332-an-interview-with-zach-barth-of-zachtronics/`，官网确有**发言归属转录**（`Zach Barth Of Zachtronics:` / `Chris Gammell:` / `Dave Jones:`）。逐条核对：

| #313 断言 | 转录 |
|---|---|
| show notes 把 Ironclad → 关门压缩 | ✅ show notes 原文即 "After Ironclad Tactics didn't go as well as they wanted, they shut down the studio for 1 year" |
| Infinifactory、TIS-100 在暂停**之前** | ✅ "And then we made Infinifactory. We made TIS 100. **At that point**… I got kind of burnt out" |
| "we shut down the studio" | ✅ 逐字存在 |
| "worked there for 10 months" | ✅ 逐字存在 |
| "tired of running the business, but I wasn't tired of making games" | ⚠️ 原文为 "because **I was** tired of running…"，引语起点未回原句边界 |
| 通过 Amplify 时期人脉接触 Alliance | ✅ "one of the writers there ended up at this company, Alliance" |
| 日期 2017-01-20 | ✅ 页面 "Jan 20, 2017"，与 E006 一致 |

**问题 A（登记结构）**：`E011` 与既有 `E006` 同源、同 URL、同为 P1、同期节目 ⇒ 应把新事实节点**并入 E006**，或明确写清 E006/E011 的分工并互相交叉引用。否则同一来源会有两个 ID，引用漂移不可避免。

**问题 B（遗漏一个改变解释的节点）**：转录中 Barth 明确说，去 Valve 之前**又面试了一次 Microsoft 但没成**——"Actually, before that, I interviewed at Microsoft again… I can't go back… But I interviewed at Valve and worked there for 10 months." 这句话才是「为什么是 Valve 而不是回归大厂」的直接证据。E011 与 `CASE-051` §4.5 都没有记录。

**问题 C（静默丢弃）**：#313 改写 `L001` 时删掉了原 S2 lead 的 RPI 节点（"started making games as a student at Rensselar Polytechnic Institute"）。该节点在转录中**没有** Barth 本人对应发言，降级为未核线索是对的，但应当**保留为线索**而非删除。

**问题 D（AGENTS.md §10 缺口）**：`Locator` 写 "around 'we shut down the studio'"，**无 timecode**。需音频或带时间戳版本。

### 1.8 #314 的人物稿事实忠实性

逐条对照转录**全部通过**：约一年暂停 ≠ 十个月 Valve；Infinifactory/TIS-100 在暂停前；Amplify → Alliance；旧游戏继续销售；「不想经营但仍想做游戏」；未虚构售价与控制权。

需修两处：

1. 「他在 2017 年的访谈里回忆，**那段时间**公司一度接近无法继续经营」——转录原文 "Almost went out of business when Iron Cloud Tactics didn't do as well as we thought it would" 是 **Ironclad 时点**的陈述，不是暂停期间。指代应明确。
2. 新增 4 段（约 800 字）偏长，末段「这段经历让『找到适合自己的作品』多了一层含义」是抽象收束，与 profile 既有收束重复。

---

## 2. 五篇的编辑诊断

分类：`资料缺口` / `研究错误` / `章节结构` / `句子表达`。全部给出可定位的段落依据。

### 2.1 Gunpoint（`book/profiles/gunpoint.md`）

- `研究错误` + `资料缺口` — 第 131 行 `Observed: c. 2009–2013` 无证据支撑：ledger 最早记录为 `2010-10-25`，其自己的 STRONGLY SUPPORTED 写 "publicly documented over about three years"。同一缺陷在文内自相矛盾（第 45 行小标题「2010 年，他重新看了一遍 roadmap」）。editorial 分支已把它记为 year drift note（先记不改，做法正确），但**至今未解决**。
- `章节结构` — 第 13–53 行连续四节讲同一件事（评论 → 比较 → 选择 → 删减），且每节都以「这里的…」收束（第 19、29、41、51 行），属 Gate §4 要防的连续「宣布新解释」推进。第 1–9 行把主问题、术语、结论预告一次性说完，读者在第 9 行之前只看到「在 PC Gamer 写游戏评论」。
- `句子表达` — 「品味决定命运」出现在第 1、7、63、75、97、101、103 行共 7 次；第 7 行直接宣布命名，按 Gate §3 应在遇到人之后。
- **应保留**：第 47–53 行 roadmap 审查、第 73 行「首发周销量跨过辞职阈值」、第 89 行「不到一个月便有可移动原型」——具体行动密度是五篇最高。第 65 行主动指出媒体职业带来的网络与可见性，是保留作者判断的正面例子。

### 2.2 Kenshi（`book/profiles/kenshi.md`）

- `研究错误`（已修，但**未进 main**）— main 版第 7、39–41 行把 **Steam Early Access 写成收入起点**。editorial 分支已改（第 7 行改为自营网站 alpha 已足以养活本人并雇 freelancers；小标题改为「玩家付款进入生产，发生过两次」）。**这是 #311 必须尽快合入的核心理由**：错误结论当前仍在 main 上。
- `资料缺口` — editorial 分支已补 CASE-012 的 **E003–E008**，但 `kenshi.md` 第 97–98 行的「研究依据」仍只列 E001、E002。证据层已扩，reader layer 完全没消费。
- `章节结构` — 第 29 行标题「《Kenshi》还有一个麻烦：……」是元评论；同一判断在第 35、67、87 行出现三次。
- `句子表达` — 第 67 行用「生产函数」这一经济学词且置于目录项，与 Gate §5 相悖。
- `人物具体度` — 中等。E003（交出部分工作、模拟系统错误与受众反应）、E004（早期工作周、核心成员与自由职业协作者）是能写出动作的现成素材。

### 2.3 Zach Barth（`book/profiles/zach-barth-zachtronics.md`）

- `章节结构`（本篇最严重）— 7 个 `##` 全是机制／概念式标题，**没有任何一节从具体时刻、处境或选择进入**（Gate §1）。同一结论出现三次以上：开头第 5 行 → 第 53–59 行 → 第 61–65 行整节，再加第 71–79 行三连卡片。「4,000 美元」被讨论 5 次（第 23、25、29、63、73 行）。
- `研究错误`（实为遗漏）— 缺 §1.7 问题 B 的 Microsoft 面试节点。补上后，「2022 关闭」与「2017 暂停」之间出现一条连续线索：他两次尝试回到受雇身份（Microsoft 未成 → Valve 十个月），最后用出售公司换取「不做管理、仍能做游戏」。这改变的是**解释**，不只是细节。
- `句子表达` — 加粗道理句密度高：第 29 行、第 65 行等，属「每节末尾例行拔高」。

### 2.4 early id / DOOM（`book/profiles/early-id-doom.md`）

- `章节结构`（最集中）— 第 217 行出现**一级标题**「# 所以这本书到底应该教一个普通年轻人什么？」，把 Profile 变成全书总论，并再次总结全部案例；直接违反 Gate §7、§11。第 195–215 行的家族／代际大节引入 Bithell、Croshaw、Keith Judge、梁其伟四组**外部反例**，属 Chapter 材料（Gate §7）。收束句在第 99、125、143、147、157、169、191、201、219–227 行，共 8 处以上。
- `句子表达` — 两个「最」式标题并列（第 103 行「DOOM 最不能被写错的一点…」、第 161 行「DOOM 最革命的地方之一…」）；第 211 行直接对读者发问。
- `资料缺口` — 证据层极厚，但 profile 几乎全依赖 Kushner 传记与多年后回顾，缺少同期一手细节。第 39 行使用 Census 分布数据（8.2% / 1.7% / 22.9%）把「天才」还原为分布，非常有力。
- **应作为模板**：第 49–55 行「那个不让 Romero 玩游戏的人，为什么又给他买了电脑？」、第 89–99 行「同样一份 Softdisk 工资，对每个人意味着不同的东西」。

### 2.5 Limit Theory（对照组，结论与预期相反）

- `研究错误`（本轮最重）— 第 135–153 行整节「2022 年，他兑现了另一种承诺」在 **CASE-054 ledger 中没有任何证据**：`rg "2022"` 在 main 与 editorial 两个版本的 ledger 中零命中；E005 只写仓库存在，Published: UNKNOWN。该断言已扩散到三处：`josh-parnell-limit-theory.md` 第 139、183 行、`book/profiles/README.md` 第 35 行、`book/chapters/03-…md` 第 105 行。`book/research-notes/editorial-fidelity-pilot-001.md:100` **已经**把它登记为 `NEEDS_VERIFY / VERIFY_IN_LANE_B`——所以这不是隐藏错误，而是「已登记、未降级、仍以肯定句出现在读者层」。
- `研究错误`（同类）— 第 67 行「2013 年，支持者可以拿到早期可玩原型」在 main 的 ledger 里没有节点，只在 editorial 分支补的 E006 时间线里（"Apr 28 Prototype is Released"）⇒ Profile 依赖尚未合入的证据。
- `句子表达`（两处硬伤）— 第 23 行同句混用姓氏与名：「Parnell 的背景与 **Josh** 后来给自己选择的产品方向有非常直接的联系。」；第 111 行语法不通：「只是当其他人终于加入，原来承诺的整个产品仍然有巨大距离。」
- `章节结构` — 全篇 40 处以上单句成段（第 17、19、35、37、47、49、51、53、59、61、65、79…），节奏由切分而非材料决定（Gate §3）。
- **应保留** — 第 181–191 行「事实范围、成本口径与不可迁移条件」是全库最规范的卡片；第 163 行明确写出 early id / Carmack 作为反例，保留作者的边界判断。

### 2.6 跨篇共性

1. **四篇结尾都在替全书说同一句话**：Gunpoint 第 103 行、Kenshi 第 55 行、Zach 第 65 行、DOOM 第 227 行，都在说「成功只是把你送到下一道题前／不能许诺同样结果」。Gate §7 明文禁止，但四篇全犯 ⇒ **这条规则没有执行机制**。
2. **加粗道理句作为小节结尾**：四篇合计 40+ 处。
3. **除 early-id 两个小节外，全部缺少「具体时刻」开头**；Zach Barth 最严重。
4. **读者层术语不一致**：`chapters/` 已被 lint 清成中文（「来源账本」「案例档案」），`profiles/` 仍写 `CASE-007`、`Evidence Ledger`、`P1`（gunpoint 第 142–153 行）。规则是全书级的，执行只覆盖 chapters。

---

## 3. 工作流是否过度治理

判断标准：**有已发生的重复故障 → 保留；只增加劳动量 → 删。**

### 3.1 应保留（有真实收益证据）

| 规则／工具 | 故障证据 | 实测 |
|---|---|---|
| `tools/chapter_copy_lint.py` | chapters 01/04/06/07 共 4 处后台术语泄漏 | 实跑 `OK (8 chapter files)`；注入 `P0` 后立即 `FAIL` 并给出行号。功能正确、成本近零 |
| `tools/reader_evidence_sync_audit.py`（report-only） | CASE-012 把 Steam 写成收入起点 | 未进 CI；`--strict` 只对 backlink/year 生效，边界正确 |
| `evidence-record-template` 的 `Exact Wording` 必填 | 11 Case 实测 + CASE-012 具体错误 | 正确，但**制造了存量债**：498 条记录中 433 条无长引语 ⇒ 必须继续不进 CI（当前确实没有） |
| `claim-template` 的 Review trigger | 15 个 Claim 中 `VERIFIED` = 0、`REFUTED` = 0 | 真实的不收敛故障 |
| `workflow-lanes` 跨模型交接章 | CASE-012 双线改同一 E001 + 摘要压缩 | 保留；本文件本身就是它的用例 |

### 3.2 应修改（规则互相冲突）

**冲突 1（必须修）**：`chapter_copy_lint` 的禁词表含 `runway`，而 `book/EDITORIAL-GATE.md` §5 明确写「**可以使用**：`runway`、`scope`、`market access`、`capability capital`、`staged commitment`，但第一次出现必须先让普通读者知道它指什么」。同时 `scope` / `market access` 未进禁词表 ⇒ 禁词表没有原则。
已发生的后果：`chapter 02` 的改动正是 REWRITE-PROTOCOL §Pass A 明令禁止的**同义替换式清洗**（「Runway 不只是账户里有多少钱」→「能撑多久，不只看账户里有多少钱」；「也就是runway」被删）。这是在满足正则，不是在修读者问题。
建议：把 `runway` 移出禁词表（`证据增强` / `承诺升级` 是研究后台语言，保留）。

**冲突 2（范围不一致）**：lint 只 glob `book/chapters/*.md`，而 `BOOK-ARCHITECTURE.md` 的原文是「**正文**不出现 P0/P1…」，profiles 里大量存在。要么扩到 profiles 的研究依据节之外，要么把文档口径改成「章节正文」。

**冲突 3（规则重复）**：`EDITORIAL-GATE` 的 §0、§2、§3、§4 与新增 §0.6 讲同一件事（不要为叙事牺牲事实）。0.6 的唯一新意是那句可操作检查（「起点／首次／唯一／才」必须回原文核对）。建议把新意并入 §0，避免同一原则有四个版本。

### 3.3 应质疑（可能只是劳动量）

- **`reader/index.html` + `reader/README.md`（#311 新增，277 行）**：`workflow-lanes` 的 `Change escalation` 第 5 条要求「只有真实用户需要消费时，再做新的 reader surface」；该 README 自己也写「先验证这个阅读形态是否真的比在 GitHub 上一章一章点开更好用，再决定是否需要部署」。**目前没有读者测试记录。** 建议：不合并，或合并但标 `EXPERIMENTAL` 且不进导航。它是仓库第 2 个 UI surface（`explorer/` 已有 1 个），会持续吸收维护注意力。
- **`schemas/evidence-material-refresh.md` 的抓取能力表**：内容有用，但「实测于 2026-10-09」的 403 / 405 / shell 结论是高时效变量，却写成长期 schema。建议加 `Last verified`，过期后降级为 research-note。

### 3.4 结论

「过度治理」的症结**不在 CI 步数**（WORKFLOW.md 9 → 10 项、CI 9 → 10 步；`chapter_copy_lint` 是秒级正则，成本可忽略），而在**规则之间的冲突与重复**：同一原则在 Gate 里有 4 个版本、禁词表与 Gate §5 打架、文档口径与 lint 覆盖范围不一致。

唯一真正会爆炸的工作量债是 `Exact Wording` 必填之于 433 条存量记录。**建议明确写下：不做一次性 backfill，只在触碰某条记录时补。** 否则下一个模型很可能发起全库补引语工程，那既不可能完成，也会稀释 #311 那类有价值的逐字回填。

---

## 4. 交付

### 4.1 优先级整改清单

**P0 — 事实与研究正确性**

1. Limit Theory「2022 源码公开」：补证或降级措辞，**同步三处**（profile 第 139 / 183 行、`book/profiles/README.md` 第 35 行、`book/chapters/03` 第 105 行）。
2. #311 的合入路径：必须 rebase / merge 到最新 main，**不得 force**；注意 `book/chapters/01` 与 `book/BOOK-ARCHITECTURE.md` 因 main 前移而新增的冲突面。
3. #311 的 CASE-012 修正（Kenshi Steam 起点错误）必须尽快进 main。
4. Gunpoint 的 `c. 2009–2013` 与其自身「约三年」表述冲突，取证后二选一。
5. #313 的 E011/E006 同源重复 + 补 Microsoft 面试节点 + 补 timecode。

**P1 — 结构与一致性**

6. profiles 的读者层术语未清理（chapters 已清）。
7. 四篇结尾的「全书总论」与加粗道理句（§2.6）。
8. `chapter_copy_lint` 的 `runway` 冲突。
9. early-id 的家族／代际节迁到 chapter 层。
10. CASE-012 的 E003–E008 未被 profile 消费。

**P2 — 治理与债**

11. 188 个未合并分支的清仓流程（逐文件比 blob，不按分支名）。
12. `reader/` 视图的保留决策。
13. #312 的正则漏匹配与输出可追踪性。

### 4.2 必须交给 GPT 补原始资料的问题

每条给出：目标 / 定位符 / 要带回什么 / 已知可达性。

| # | 目标 | 定位符 | 要带回 | 可达性 |
|---|---|---|---|---|
| 1 | Gunpoint 开发起点 | `pentadact.com` devlog 首篇 / GDC Europe 2013 视频 / IGF 2012 报名页 | 第一版原型有日期的记录 | `pentadact.wordpress.com` **403** |
| 2 | Limit Theory 源码公开 | `github.com/JoshParnell/ltheory`（首个 release / commit）、`ltheory-old` | 公开日期 + 公开范围 | direct |
| 3 | The Amp Hour #332 | 该期音频或带时间戳版本 | 「we shut down the studio」等处 **timecode**；`currently we're four and we've peaked` 的 team-size 原句 | 官网转录 direct（已核）；音频未听 |
| 4 | Alliance 收购 | 2018 年前后官方声明 / 新闻稿 | 收购方全名、日期、是否公开金额 | 未探 |
| 5 | CASE-012 | Siliconera 2015 原采访；4Gamer / GameSkinny 原文 | 自营 alpha 的**原句与售价**；同期团队成员名单 | 部分 blocked / shell |
| 6 | CASE-016 | E020–E031（`- **Class:**` 那批） | 补齐这些 P0/P1 记录的逐字引语 | ledger 内已有 URL |
| 7 | early id | Kushner《DOOM启世录》1993 餐厅道歉段；WIRED 1998 *Legion of Doom* | 可引用的原页原句与页码 | 书需具体页码 |
| 8 | Zach Barth 2015 年财务变动 | `CASE-051` Open Questions 第 2 项 | 原始出处或确认不可获得 | 未探 |

### 4.3 交给 Codex 的文件级写作任务

| ID | 文件 | 基线 | 做什么 | 不许做 |
|---|---|---|---|---|
| T1 | `book/profiles/kenshi.md` | 合 #311 后 | 消费 E003–E008：把「前五六年」扩成 2 个有动作的段落（2017 交出部分工作；2018 早期工作周）；删第 67 行「生产函数」；第 29 行小标题去掉「还有一个麻烦」 | 不补 headcount、不补工资 |
| T2 | `book/profiles/zach-barth-zachtronics.md` | main + #314 | B 稿压成 2 段；补 Microsoft 面试节点（须先由 Lane B 落 E006/E011）；删第 61–65 或第 71–79 之一；给出一个「具体时刻」入口 | 不改 4,000 美元口径；不推断股权 |
| T3 | `book/profiles/josh-parnell-limit-theory.md` | main | 修第 23 行 `Josh`、第 111 行语法；处理第 135–153 行；第 67 行等 E006 合入后再引用 | 不批量合并 40 处单句成段（那是风格清洗） |
| T4 | `book/profiles/gunpoint.md` | main | 合并第 23–31 与 33–41 两节；限制「品味决定命运」的重复 | 不动第 47–53、69–75 行的具体事实段 |
| T5 | `book/profiles/early-id-doom.md` + 目标 chapter | main | 第 195–215 行家族／代际节迁出为 chapter 素材；第 217–227 行改为回到 Romero／团队的 profile 结尾；删 8 处「作者在这里保留的判断」 | 不删 Bithell / Croshaw / Judge 反例本身，只换位置 |
| T6 | `tools/chapter_copy_lint.py` | editorial | 解除 `runway` 禁用并记录理由 | 不放宽 P0/P1/状态词 |
| T7 | `evidence/CASE-051-zachtronics-source-ledger.md` | #313 | E011 并入 E006 或写清分工；补 Microsoft 节点；引语回到原句边界；保留 RPI 线索 | 不声称已听音频 |
| T8 | `tools/reader_evidence_sync_audit.py` | #312 | 支持 `- **Class:**`；`--all` / `--json` 稳定输出；补真实 ledger fixture | 不让它进 CI |
| T9 | `book/profiles/README.md`、`book/chapters/03` | main | 与 T3 同步 Limit Theory 的 2022 措辞 | 不同步虚构日期 |

---

## 5. 本轮边界

- 本文件不新增或改变任何 canonical Case / Evidence / Claim；不合并任何 PR；不改写任何既有 Profile。
- 引用 PR 与 Issue 的编号、标题、base / head 均以 2026-10-10 的 GitHub 实测为准；审查期间 `main` 由 `0f75dd4` 前移至 `00945b7`，涉及 chapter 01 / BOOK-ARCHITECTURE 的合并面需在 rebase 时重新确认。
- §2 的每一条诊断都可由文中给出的文件名、行号或工具输出复现。
- 是否采纳、采纳哪几条，仍由作者裁决。
