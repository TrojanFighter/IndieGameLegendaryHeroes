# 045 — 六年后还有多少人在做游戏：Beginner Friendly Game Jam 2020 固定入口作者性追踪

- Status: **FIXED-ENTRY DENOMINATOR PILOT / COMPLETE 18-SUBMITTER FRAME / PUBLIC AUTHORIAL CONTINUATION ONLY / EMPLOYMENT UNKNOWN**
- Observation cutoff: 2026-10-08
- Routes: OQ-001 Gate / OQ-002 Second Attempt / OQ-003 Silent Failure / OQ-006 Failure Reversibility
- Parent method: [028 媒体选择与分母协议](media-selection-survivorship-and-denominator-protocol-028.md)
- Comparator: [031 Week Sauce 18/18 public-attempt cohort](public-unfeatured-week-sauce-apr-2022-cohort-031.md) / [033 Week Sauce account follow-up](week-sauce-2022-public-creator-followup-033.md)
- Sampling boundary: 本轮从 **2020-06-05 至 2020-06-12 Beginner Friendly Game Jam 的完整 18 条公开提交**出发，先固定分母，再查看 2026 年公开作品痕迹。它可以描述这个特定 online jam 中“后来还能观察到什么”，不能估计所有 beginner、所有独立开发者或任何国家的人群发生率。
- Unit: **primary submitting itch account linked to one baseline submission**；不是 18 位经实名核验且互相独立的自然人。原始条目存在共同作者，后续项目也可能换团队。

## 0. 为什么这组样本比再找十个失败 postmortem 更重要

[044](creator-exit-reentry-economics-044.md) 已经把“失败以后”拆成项目、公司、就业、作者性、家庭压力、残余资本和再入场时间。但 044 的人物是主动寻找的公开 postmortem，天然偏向“有故事、愿意回顾、后来还能被找到”的人。

本轮换一个问题：

> 如果我们**事先不知道后来谁成功、谁还在做、谁消失**，只从一个六年前的完整 beginner jam 名册出发，今天能看到怎样的作者性延续？

Beginner Friendly Game Jam 的官方页记录：
- 开始：2020-06-05 10:00；
- 结束：2020-06-12 10:00；
- 主题：SUPERFAST；
- **18 Entries**；
- 页面与社区明确面向 game-jam / game-dev 新手；但至少一名参与者公开说明自己有商业程序经验、只是刚进入 game dev，因此不能把 18 个账号全部重命名为“零经验新人”。

Sources:
- jam overview: https://itch.io/jam/beginner-friendly
- complete entries: https://itch.io/jam/beginner-friendly/entries
- community / beginner framing: https://itch.io/jam/beginner-friendly/community

与 031 Week Sauce 一样，这不是 2020 年预注册的学术样本，而是 2026 年回顾性选取的**完整小型公开 frame**。选择它的原因是入口完整、规模足以全量核查、时间距今约六年，而不是因为它后来“出了很多成功者”。

## 1. Sampling declaration

```yaml
question: "2020年一个完整的小型 beginner-friendly jam 主提交账号队列，到2026年还能观察到多少后续公开创作？"
target_population: "Beginner Friendly Game Jam 2020 /entries 页面收录的18项公开提交对应的主提交账号；不含报名未提交者"
unit_of_analysis: "project-submission-linked primary itch account"
cohort_entry_event: "baseline submission appears in complete jam entry list"
cohort_window: "2020-06-05..2020-06-12"
t0: "2020-06-12 jam close"
observation_cutoff: "2026-10-08"
sampling_frame: "https://itch.io/jam/beginner-friendly/entries"
selection_rule: "18 entries all included; no filtering by rating, later output, press, commercial result, or biography"
denominator_status: "KNOWN_FOR_PUBLIC_SUBMITTING_ACCOUNTS_ONLY"
denominator_count: 18
identity_boundary: "account != verified natural person; account != stable team membership"
primary_outcome: "public authorial continuation trace after T0"
employment_outcome: "UNKNOWN unless directly public; not inferred from itch activity"
commercial_outcome: "UNKNOWN unless directly evidenced; itch release != sustainable business"
missingness: "deleted/empty profiles, off-platform work, private work, alternate accounts, undated projects, changed teams"
permitted_inference: "within-frame lower bounds on observable later public creation"
forbidden_inference: "career retention, employment recovery, indie success rate, income, national prevalence, reason for silence"
```

## 2. 先定义什么叫“还在做”，避免把主页存在误写成职业持续

本轮使用五档公共痕迹状态：

- `BASELINE_ONLY_VISIBLE`：目前只看到 2020 baseline；**不等于退出**。
- `POST_T0_PUBLIC_CREATION_CONFIRMED`：至少一项作品可证明晚于 2020-06-12。
- `YEAR_2021_PLUS_CONFIRMED`：至少一项公开游戏制作锚点落在 2021 或以后。
- `YEAR_2022_PLUS_CONFIRMED`：至少一项锚点落在 2022 或以后。
- `YEAR_2024_PLUS_CONFIRMED`：至少一项锚点落在 2024 或以后。

这些档位是**最低可证年份**，不是“从 2020 连续做到该年”。例如 2025 有新作，只能证明 2025 那个节点仍有公开作者活动；中间年份可以完全未知。

就业另设：

`EMPLOYMENT_STATUS = UNKNOWN`

除非作者本人或可靠职业来源直接说明。不能因为六年后仍做 jam 就写成“仍在游戏行业”，也不能因为主页空了写成“改行”。

## 3. 18/18 完整回访

| # | 2020 baseline / 主提交账号 | 可证后续 | 本轮编码与边界 |
|---:|---|---|---|
| 01 | Mr. Red LightYear / **CreepaFreaka** | 2020-08 Happy Jam 有《cat vs dogs》 | `POST_T0_CONFIRMED`；只证明两个月后还有公开 jam，不证明长期职业 |
| 02 | Time cuboid / **Not an apple, a stone** | 与 Blueberry Mauro 后续共同制作《Rewinded Sliborg》（Brackeys 2020.2）及 Ludum Dare 49《Unstable Concoction》 | `YEAR_2021_PLUS_CONFIRMED`；当前 creator profile 的作品排序不能替代职业史 |
| 03 | SpeedRun / **HackLord Monster** | 2026 页面仍有新作《Growing On Me》，参加当年 Playgama summer jam | `YEAR_2024_PLUS_CONFIRMED`；多人项目，不能把全部劳动归为 solo |
| 04 | Assassins will not be Illegal / **Blueberry Mauro** | 2021 Ludum Dare 49《Unstable Concoction》，与 Not an apple, a stone 共同署名 | `YEAR_2021_PLUS_CONFIRMED`；合作关系延续可见，经济结果未知 |
| 05 | Stella Universum / **FatiguedFox** | 主页按年份列有 2021、2022 项目；2022-04《Boxed In》有 post-jam devlog | `YEAR_2022_PLUS_CONFIRMED`；主页 2023 栏中部分作品由 Sijil 主署名，不能偷算成 FatiguedFox 自作 |
| 06 | Melon Masher / **Volasf** | 《Infinite Generations》明确写为 RNDGAME2021 | `YEAR_2021_PLUS_CONFIRMED` |
| 07 | Another Slow Speed Running Game / **Brad Make Games** | 2026 Brackeys Game Jam 2026.1《Strange Planets》 | `YEAR_2024_PLUS_CONFIRMED`；项目 credits 显示多人协作 |
| 08 | LvUp++ / **Krazy** | 主页现列《Artfight2025》等多项后续作品 | `YEAR_2024_PLUS_CONFIRMED`；仅以公开作品名/页面确认 2025 活动 |
| 09 | Sonic Jump! / **AmbitiousIndie** | baseline 页面自称“first game I've ever made”；当前另列《Official Phaser Web Game》 | `POST_T0_CONFIRMED`，因为 baseline 自证为第一作；第二页无可靠发布日期，不升级年份档 |
| 10 | Lightspeed / **Aeg** | 后续《Kauri》标为 Weekly Game Jam 166；同届作品有 2020-09 日期锚 | `POST_T0_CONFIRMED`；这是 2020 后续，不证明 2021+ |
| 11 | Adrenaline Rush Racing / **Kara Whelan / KAWGAMING** | 另一可见作《Bounds and Leaps》属于 Game Off 2019，明确早于 baseline | `POST_T0_UNRESOLVED`；不能因主页有“两款”就把 2019 前作误算为 2020 后续 |
| 12 | Flash / **BroocoGamesStudio** | 当前还能看到《Controler SImulator》，但页面无可靠发布日期 | `POST_T0_UNRESOLVED`；作品存在，不擅自推断相对顺序 |
| 13 | Wormhole / **NoCake** | 2020 GMTK Game Jam《System Monitor》，该 jam 晚于六月 baseline | `POST_T0_CONFIRMED` |
| 14 | Super Fast / **Thulkrast** | 当前公开 creator surface 只确认 baseline | `POST_T0_UNRESOLVED`；不是 `CAREER_EXIT` |
| 15 | Sammy Da Snail / **dice099** | 2021-08/09 Metroidvania Month 13《CaveBoy》 | `YEAR_2021_PLUS_CONFIRMED` |
| 16 | Super Plumber / **Tune Polo** | 当前 creator page 无可用作品列表；baseline 仍在 jam 名册 | `POST_T0_UNRESOLVED / PROFILE_EMPTY`；空页不能编码退出 |
| 17 | SCP stupid / **CMRA HEAD** | 当前 creator page 无可用作品列表；baseline 仍在 jam 名册 | `POST_T0_UNRESOLVED / PROFILE_EMPTY` |
| 18 | Super Fast! / **Argle Bargle** | 2024 Do you WANNA Jam?! 的《N.A.N.O》 | `YEAR_2024_PLUS_CONFIRMED`；该项目为多人合作 |

**两条身份警告：**
1. baseline 就已有多人署名，例如 Stella Universum 还署名 Sijil，LvUp++ 还署名 Mia；因此“18 项 = 18 人”的说法从入口就不成立。
2. 后续项目也会换协作者。我们追的是**原主提交账号的公开作者轨迹**，不是固定 18 支团队的组织存活。

## 4. 这一次终于可以报告比例，但比例叫什么决定了它是否诚实

在相同 18-account frame 内：

| 可观察门槛 | 至少确认账号 | frame 内可观察下限 |
|---|---:|---:|
| baseline 后至少一次公开游戏创作痕迹 | **13 / 18** | **72.2%** |
| 2021 年或以后仍有明确公开游戏制作锚点 | **9 / 18** | **50.0%** |
| 2022 年或以后仍有明确公开游戏制作锚点 | **5 / 18** | **27.8%** |
| 2024 年或以后仍有明确公开游戏制作锚点 | **4 / 18** | **22.2%** |
| 本轮没有确认 baseline 后公开 itch 创作 | **5 / 18** | **27.8% unresolved**，**不是退出率** |

这些数值的正确名称是：

> **observable public-authorial-continuation lower bound inside this fixed public-submission frame**

不能改名为：
- beginner game-dev retention rate；
- indie career survival rate；
- 六年后还在游戏行业的比例；
- 第二作成功率；
- 独立开发成功率。

为什么是 **lower bound** 而不是完整发生率：
- 五个 unresolved 账号可能在 Steam、GitHub、别的 itch 账号、公司项目或私人项目继续；
- 公开账号不能证明真实自然人身份连续；
- 后续页面可能删除；
- 已确认者也可能只是在某一年参加一次 jam，并非持续开发；
- frame 本身只收录**已经交出作品的人**，完全看不到想参加却没交、从未入场或只做私人原型的人。

但这仍然比媒体人物样本强一个关键层级：**分母不是由后来谁有故事决定。**

## 5. 结果真正打掉了哪几种错误直觉

### 5.1 “六年前参加 beginner jam 的人大多应该已经消失”不是可以靠直觉宣布的事实

至少 13/18 有某种 baseline 后公开制作，至少 4/18 在 2024–2026 还有明确作品锚点。

这不是说 cohort “留存很好”。它只说明：当我们真的从一个完整入口往后追，而不是只搜出名开发者，**长期留下公开创作痕迹的人并非不可见的零星个案**。

这给 OQ-002 一个新的中间变量：

`AUTHORIAL_PERSISTENCE`

它与：
- `FULLTIME_INDIE`
- `GAME_INDUSTRY_EMPLOYMENT`
- `COMMERCIAL_SUCCESS`
- `SECOND_STEAM_RELEASE`

都不是同义词。

### 5.2 作者性可以长期存在，却完全不告诉我们靠什么生活

Brad Make Games、HackLord Monster、Krazy、Argle Bargle 的较晚公开项目告诉我们“多年后仍在制作”；它们不告诉我们：
- 是学生、业余、自由职业还是全职员工；
- 工资来自哪里；
- 游戏收入多少；
- 是否曾经中断几年；
- 是否想把游戏变成职业。

因此 045 对 044 的补充不是“终于证明失败可逆”，而是：

> **作者性延续比职业经济恢复更容易从公开作品档案观察。**

OQ-006 仍需要另一个具有就业/职业入口的 frame。

### 5.3 一页空白是 censoring，不是人生结论

Tune Polo 与 CMRA HEAD 的当前 creator surface 没有可用作品列表；Thulkrast 目前只见 baseline。

这种数据如果被粗暴二元化，最容易产生“3 人退圈”的假结论。

正确编码是：
`PUBLIC_POST_T0_TRACE_NOT_CONFIRMED`

而不是：
`STOPPED_MAKING_GAMES`
或
`CAREER_EXIT`。

Kara Whelan 则提供另一种错误：主页确有第二款可见作品，但《Bounds and Leaps》明确属于 **Game Off 2019**。如果只数“主页游戏数 > 1”，就会把前作错当后作。

### 5.4 第二次机会不应该只看“第二款商业发行”

这 18 个账号里，大量后续仍然是 jam、小作品、合作作。

对于人生决策研究，这些小项目至少可以承担三类作用：
- 保存作者技能与身份；
- 形成新的合作网络；
- 继续产生作品反馈。

它们是否最终资本化为职业或商业作品，需要另查。不能因为没有 Steam 二作就把这些路径归零。

## 6. 与 Week Sauce 031/033 合起来，我们已经有两个不同年代的小分母

现在仓库至少有两组完整 public-attempt 小队列：

1. **Week Sauce 2022.04**：18 submissions，规则容许分散七个工作日、未完成作品、工作/家庭并存；033 已追到 2026 公开账号状态。
2. **Beginner Friendly Game Jam 2020.06**：18 submissions，短期 beginner-friendly online jam，本篇追到约六年后的公开作者痕迹。

二者都只有 18，且都来自 itch.io，因此**不能把 36 个条目简单拼成一个“普通独游样本 n=36”**：
- entry rules 不同；
- unit 一个先以 submission、一个进一步固定到 primary account；
- 年龄、地区、职业身份未知；
- self-selection 都很强；
- 重复账号/自然人跨 jam 的可能性未系统排除。

它们的价值是方法验证：

> **完整入口 → 全量列名 → 明确保留 UNKNOWN → 再追踪，而不是从媒体结果倒着选人物。**

## 7. 对 OQ-001 / 002 / 003 / 006 的状态影响

### OQ-001｜普通创作者死在哪道 Gate
新增：
`PUBLIC_FIRST/EARLY_JAM → LATER_PUBLIC_AUTHORSHIP`
这一段已经可以在小 frame 里观察。

仍缺：
- 注册但未提交；
- 私人 prototype；
- 全职化；
- 商店页/发售/回本；
- 地区可比队列。

所以它没有被“关闭”。

### OQ-002｜Second Attempt
从：
`SECOND_RELEASE BASELINE + ANECDOTAL EXIT PATHS`

推进到：
`FIXED-ENTRY PUBLIC AUTHORIAL CONTINUATION PILOT`

但这里的“second attempt”包括 jam/小作，不等于第二个商业产品。

下一步真正缺：
- 同一 frame 中哪些人曾把创作职业化；
- 失败/低表现者后续就业；
- 可观察的 full-time → employment / second company 路径。

### OQ-003｜Silent Failure
本轮进一步证明必须把：
`NO PUBLIC TRACE`
当作 missing/censoring state。

五个 unresolved 账号不能塞进 failure bucket。未来若要解析，优先只沿作者自己公开连接的 Steam、GitHub、个人站、credits 等，不做私人身份拼图。

### OQ-006｜Failure Reversibility
只推进了：
`AUTHORIAL_OUTCOME`

几乎没有推进：
`EMPLOYMENT_OUTCOME / SALARY / HOUSEHOLD_RECOVERY / DEBT / GAP`

因此 OQ-006 必须继续保持 PARTIAL。下一个 denominator 不应再选纯作品平台，而应尽量从**职业可观察入口**出发。

## 8. 下一组 cohort 应该怎么选

045 已经完成“六年作者性是否仍可观察”的小型 pilot。继续复制第三个 itch jam 的边际收益开始下降。

下一组优先寻找满足至少两项的入口：
- 有公开 participant/team roster，而不只 winners；
- 能连接公司/职业 credits；
- 时间在 2016–2021，使 T+3/T+5 可观察；
- 有 failed / withdrawn / low-visibility entries；
- 有明确地区或制度背景，便于和中国/台湾/斯拉夫做同口径比较；
- 不依靠主动采访成名者才能被纳入。

候选 frame 类型：
1. 小型 accelerator / incubator 全体 cohort；
2. prototype/grant 全体公开 recipient cohort（若 applicants 不公开，明确只代表 recipients）；
3.公开学生 game showcase 全体项目；
4. 有完整 credits 的小型 studio closure / layoffs cohort；
5. 可追踪 alumni 的公开 development program。

**优先目标从“第三个 jam”切换到“能看到 employment transition 的固定入口”。**

## 9. Reader-layer 可以安全拿走的一句话

> **第一次公开做出游戏以后，真正值得问的不只是“第二款卖了多少”，还包括几年以后这个人是否仍有能力、关系和时间继续留下作品。**

这个 18-account pilot 显示，公开作者性可以比一次具体项目活得久得多；但它也同时提醒：

> **持续做游戏和靠游戏生活，是两件必须分开统计的事。**

这正是人生性价比模型里 `Residual Authorial Options` 不能被 `Income` 或 `Employment` 一列吞掉的原因。

---

## Primary public evidence

Baseline frame:
- Beginner Friendly Game Jam overview: https://itch.io/jam/beginner-friendly
- Complete 18 entries: https://itch.io/jam/beginner-friendly/entries
- Community: https://itch.io/jam/beginner-friendly/community

Selected dated / ordering anchors used for the longitudinal lower bounds:
- CreepaFreaka profile + later Happy Jam frame: https://creepafreaka.itch.io/ · https://itch.io/jam/happy-gamejam
- Blueberry Mauro / Not an apple, a stone — Unstable Concoction, Ludum Dare 49: https://blueberry-mauro.itch.io/unstable-concoction
- FatiguedFox — 2022 Boxed In devlog: https://fatiguedfox.itch.io/boxed-in/devlog/366456/boxed-in-post-jam-update
- Volasf — Infinite Generations / RNDGAME2021: https://volalsf.itch.io/infinite-generations
- Brad Make Games — 2026 profile/feed: https://brad-make-games.itch.io/ · https://itch.io/e/38667978/brad-make-games-published-strange-planets
- Krazy current portfolio incl. Artfight2025: https://ksproduction.itch.io/
- HackLord Monster — Growing On Me / 2026 jam: https://hacklord-monster.itch.io/growing-on-me
- NoCake — System Monitor / GMTK 2020: https://itch.io/jam/gmtk-2020/rate/697840
- dice099 — CaveBoy / Metroidvania Month 13 (2021-08-15..09-15): https://itch.io/jam/metroidvania-month-13
- Argle Bargle — N.A.N.O / Do you WANNA Jam?! 2024: https://itch.io/jam/do-you-wanna-jam-2024/rate/2891359
- Kara Whelan — Bounds and Leaps is Game Off 2019, therefore a pre-baseline control: https://kara-whelan.itch.io/bounds-and-leaps
- BroocoGamesStudio — Controler SImulator exists but page provides no reliable publication date: https://broocogamesstudio.itch.io/controler-simulator
- AmbitiousIndie baseline self-identifies Sonic Jump! as first game: https://ambitiousindie.itch.io/sonic-jump
- AmbitiousIndie second visible project: https://ambitiousindie.itch.io/official-phaser-web-game

No private contact details, identity records, household data, or inferred employment status were collected. Public comments that expose contact information are not reproduced.
