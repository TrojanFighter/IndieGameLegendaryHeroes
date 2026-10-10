# 第六篇阅读改造：事实锁与结构剪辑

状态：AUTHOR_REVIEW_PENDING。Lane C；真实读者测试 NOT TESTED。本记录先于候选正文建立。

## 写入预检与基线

- 精确目标：`TrojanFighter/IndieGameLegendaryHeroes`，公开行业案例的跨人物专题。
- 最新 main：`44cc729e1e4ab6e127cd31a6b730bb52823119c2`；分支：`codex/chapter06-editorial-pilot-20261009`。
- 原稿：[`06-you-do-not-need-a-standard-studio.md`](../chapters/06-you-do-not-need-a-standard-studio.md)，blob `436914e480d542b9d6db999abe36ba627da359ef`。
- 本轮只新增本笔记与一份完整专题候选；不覆盖正式 Chapter，不改 [LR-004](../life-routes/project-thesis-capability-gap-004.md)，不改 Case/Evidence/Claim/Schema/metadata。
- 原稿可从 baseline commit/blob 恢复。候选经独立史实回读后交单独 PR，作者验收前不合并。
- 历史事实 Owner 为 CASE-007/042/048/050/056 及各自 Ledger；其研究状态不由本轮编辑改变。用公开资料独立写作，无其他项目内部材料、私人执行建议或匿名私人信息。
- 主线之外的既有比较消费 CASE-060/054/047/057/026 及各自 Ledger，具体锁定见下表；C015 仍为 SUPPORTED，不将适配方法写成商业成功条件。

## Narrative Packet

本篇是跨人物专题。主问题为：同样说“做不出来”，为什么有人寻找共同作者，有人删掉制作义务，有人购买现成材料，而合适的团队仍可能难以持续？

Roset 的视觉设想与技术伙伴形成作品；Francis 在工资支持的业余制作中重划范围；Wehle 在职业与育儿约束中借用素材。三者不排成成功步骤，也不把职业标签当成选择的原因。Playdead 用成功后的关系变动检验“互补就能长期共存”；Question 用成品的商业不足检验“能力匹配就能养活团队”。

采用比较随笔：先让 Roset/Francis 的相反选择相遇，再让 Wehle 的整合劳动改变“自己做”的定义，随后转入合作的时间成本与市场边界。两种失败压力来自不同问题，不将治理冲突和销量不足混成一项。

要保存的作者判断：扩大能力集合与缩减产品义务均有价值；岗位名不能定义瓶颈；共同作者带来共同权力；学习、购买和融资都要说明服务什么作品任务；制作可行与市场可持续分别核验。保持锋芒，但不重复同一套课堂总结。

禁止补写相遇现场、谈判对白、焦虑或信任的心理描写、家庭照护分工、资金分配和人物过错。作品题材、协作者、工资和家庭责任保留其已有口径。

## 正文生成前 Fact Lock

| 人物/动作 | Canonical 依据 | 口径与未核部分 |
| --- | --- | --- |
| Roset 职业插画经历、先有颜色恢复设想；Mendoza/Cuevas 有 AAA 程序经验；作品先于公司 | [CASE-050](../../cases/CASE-050-nomada-gris-neva.md)；[Ledger](../../evidence/CASE-050-nomada-gris-neva-source-ledger.md) E001–E003 | 2019 发售后回忆与 2018 发售前访谈分开；具体股份、创始人资金 UNKNOWN |
| 三人做 demo、向 Gamescom 发行商展示 | CASE-050 E002 | 已登记事实，可用于填充叙述；不加六个月经费、合同条款或“因为展会所以成功” |
| Francis 长期评论、发现 GameMaker/原型、2010 删脚本演出；艺术与音乐协作、工资与首发周辞职阈值 | [CASE-007](../../cases/CASE-007-gunpoint.md)；[Ledger](../../evidence/CASE-007-gunpoint-source-ledger.md) E001/E002/E004/E006/E008 | 2010 当时记录、2014 方法归纳分开；删昂贵外壳是作者分析，不是所有决定共享当时路线图；收入/预算 UNKNOWN |
| Wehle 职业技术美术、前作约两年、2016 在职育儿、偏好短简单范围、授权素材/脚本、环境叙事 UX 强项 | [CASE-042](../../cases/CASE-042-the-first-tree.md)；[Ledger](../../evidence/CASE-042-the-first-tree-source-ledger.md) E002/E003/E005 | 前作约两年来自可能更新的本人作品页，不能当逐日开发日志；家庭预算、照护分工未知 |
| Jensen 愿景与 Patti 公司建设分工；2016 退出、2017 冲突报道及其人生/项目时间安排说法 | [CASE-056](../../cases/CASE-056-playdead-founder-governance.md)；[Ledger](../../evidence/CASE-056-playdead-founder-governance-source-ledger.md) E001–E003/E005–E007 | 不是未完成第二作，不裁定责任；股权、法律因果和可避免冲突的条款未知 |
| Question 三位核心的职业前史变成玩法/题材；Shin 不同阶段加入；2016 商业不足，2018 选择合作恐怖 | [CASE-048](../../cases/CASE-048-the-magic-circle.md)；[Ledger](../../evidence/CASE-048-the-magic-circle-source-ledger.md) E001–E005/E008–E010 | 三位核心不是全部 contributors、不是从第一天同为全职；无营销预算不是无营销；销量不等于终身财务；后作盈利未知 |
| Croteam 沿用引擎/Editor、补叙事专长及谜题测试；Limit Theory 取消时游戏远未功能完成 | CASE-060 Ledger E002–E004；CASE-054 [Ledger](../../evidence/CASE-054-limit-theory-source-ledger.md) E006/E007 | 只比较学习与产品距离；不单归因自研引擎；未加入新的效率、成本或反事实成功判断 |
| The Witness 前作收入与建筑/景观专长；thatgamecompany 公司股权融资扩展发行能力 | CASE-047 Ledger E001/E003–E005；CASE-057 Ledger E001/E005/E006 | 资本口径不混同；不推特定权益、创意否决或融资导致全部延期 |
| Brigador 展会、报道、EA、商业不足与展示错配 | CASE-026 Ledger E001/E004/E006 | 开发者定性诊断，不确定全部因果；有市场活动不等于有效转化 |

H/作者分析不升级成 Claim；没有新 Signal 或外部报道事实直接入稿。观察年代与 2026 可用性分开，历史渠道和生活成本不默认仍有效。

## Structural Cut：原章逐节职责与去向

N=人物行动，A=作者分析，D=决策建议，R=研究边界。用于发现阅读断点，不设比例。

| 原章段落组 | 用途 | 候选操作及观点去向 |
| --- | --- | --- |
| 开头 + Roset 技术伙伴 | N/A/R | 合并起点，补入已有 E002 的 demo 与发行商展示；删除未发生的“自学全套/先做好再画图”展开，保留视觉意图与共同作者判断 |
| Francis 遇到不同问题 | N/A/R | 与 Roset 并置，保留 2010 删改和协作者；补已有首发周辞职时间，避免裸辞叙事 |
| 原型不漂亮的三种诊断 | D | 正文用短比较保留“岗位名不是瓶颈”判断；细表链接 LR-004 第一/二关与虚构双人示例，原稿可回查，不新增路线教程 |
| 自己学不免费：Wehle/Croteam/Limit Theory | N/A/D/R | 主线集中 Wehle 的前作、在职育儿、外部材料；学习有成本的原观点保留；Croteam/Limit Theory 连同学习评价句转为候选末尾延伸比较 |
| 共同创始人/Playdead | N/A/D/R | 保留完成两作后仍分裂的反压力；删假设等五年谈判问答，权力与长期责任保留；方法链接 LR-004 COMPOSE |
| 有钱招人：Witness/thatgamecompany | N/A/D/R | 放入候选末尾“延伸对照”，保留资本来源、长期组织义务及融资非验证判断；不消除而是从主线让出篇幅 |
| 最冷酷反例：Question/Brigador | N/A/R | Question 推进到下一作方向，商业不足不写成解散；Brigador 与定性归因边界链接延伸对照 |
| 怎样判断合作 + 先确认再承诺 | D/A | 取消第二次岗位诊断，结尾保留能力与作品相互调整、长期承诺必须核具体任务；方法只链接 LR-004 |
| 时效卡 + 继续读 + 来源 | R/D | 保留观察年份/历史条件/状态；主线五组事实回链，旁支给现有 Case/Route 链接 |

没有搬写或修改 LR-004。现有路线已包含 S0–S4 证据门、能力核心与可验收外围、六种动作、生产/市场两次检查和虚构视觉诊断。原章三种视觉问题与路线示例不完全逐字相同，候选保留其共同判断；若作者希望保留三分表，可继续保留原稿或另审路线，不谎称全量迁移已完成。

## 网上原稿核验记录

访问日期 2026-10-09；这些是编辑读源记录，不修改 Ledger 的来源等级。

- David Wehle，[So Many Projects, So Little Time](https://www.gamedeveloper.com/business/so-many-projects-so-little-time)，2016-07-06，正文完整读。用于 E005 已登记的在职、育儿、范围与材料选择；未新增每日工作、报价、家庭分工或当代授权建议。
- Ryan Lambie，[Interview: BioShock 2 director Jordan Thomas on The Blackout Club](https://filmstories.co.uk/gaming/interview-bioshock-2-director-jordan-thomas-on-the-blackout-club/)，2018-11-26，访谈正文完整读。只消费 E008 的后续方向，未引入新的团队数、试玩现场及预测；引言年代不替代 canonical 前史。
- Christian Nutt，[Hanging in Limbo](https://www.gamedeveloper.com/business/hanging-in-limbo)，2012-02-24，已读开头及作品/公司关系段，未声称完整读完长访谈。用 E002/E003 交叉核工作职责；新增删减比例与制作轶事不入稿。
- Alex Wawro，[Road to the IGF: Question's The Magic Circle](https://www.gamedeveloper.com/business/road-to-the-igf-question-s-i-the-magic-circle-i-)，2016-01-15，已读背景、工具、制作时长与题材起点段；未声称完整阅读。E001 的角色及加入阶段可回查；新增技术、外包轶事不入稿。
- Enerio Dima，AnaitGames，2019-08-02，[Nomada founders interview](https://www.anaitgames.com/entrevistas/celsius-2019-entrevista-conrad-roset-roger-mendoza-adrian-cuevas) 本轮访问超时，不能称重新读过；保留 E001 的既有证据身份，不靠搜索摘要填充。demo 补叙用另项已登记 E002。
- Nintenderos，[Hablamos con Conrad Roset](https://www.nintenderos.com/2018/09/entrevista-hablamos-con-conrad-roset-director-creativo-de-gris-sobre-la-industria-del-videojuego-el-origen-y-las-inspiraciones-de-este-titulo-y-mucho-mas/)，访谈正文完整读。当前页标 `Publicado 07/09/2018`，与 E002 登记的 `2018-09-25` 不同；不静默改 Ledger，候选仅写 2018 年。辞职谓词紧随两位程序员，故候选不笼统写三人都辞职。访谈还说 Gamescom “三年前”，不直接推算demo年份，具体时间线交 Lane B。画作起点、音乐协作等未登记新细节不引入本轮。

## 三遍编辑与回读计划

Delete：先移出重复决策教程和第三轮总结，再处理句子。Restore Person：保留劳动与合作的实际安排，用已登记前作/demo/转型填叙述断处。Rhythm：五条路径彼此提出问题，不依次重复“背景—结论—限制—建议”。

作者验收始终独立；不以模型意见、篇幅减少或禁词数量作为通过标准。

## 原稿与候选的 Fidelity Readback

完整候选见 [Chapter 06 阅读稿](chapter06-narrative-candidate-2026-10-09.md)。A 为上述 baseline 下的正式原章，B 为该候选；本轮做明示版本的编辑比较，未假装匿名盲测。原章没有被删除或替换，逐节删移关系见 Structural Cut。

| 项目 | 状态 | 回读重点 |
| --- | --- | --- |
| 人物与署名 | PRESERVED | Roset/Mendoza/Cuevas、Francis艺术音乐协作、Wehle外部材料、Jensen/Patti分工、Question三人职责；核心不等于完整贡献者 |
| 时间与知识 | PRESERVED | 2010 Francis开发记录与2014方法归纳分开；2013首发周后退出职业；Roset2018/2019访谈分别归属；Patti2016退出与2017冲突报道分开 |
| 新增叙事填充 | PRESERVED | GRIS demo/Gamescom → CASE-050 E002；Wehle前作/约两年 → CASE-042 E003；Shin兼职到全职 → CASE-048 E001；均已在 canonical corpus，不产生新史实 |
| 数字口径 | PRESERVED | Wehle约两年是前作制作，不是 The First Tree；没有增加预算/工时/人数/销量；三位核心不写成第一天全职或总人力 |
| 否定、情态、因果 | PRESERVED | 不承诺小作品/素材/合作成功；无营销预算仍与实际活动分开；前作/方法不隔离出唯一成功原因；商业短缺不是立即解散 |
| 未知与争议 | PRESERVED | demo资金、股份、家庭预算、工资阈值、Patti责任/法律、Question后作盈利未知保留；不替双方归责 |
| 作者观点与 H | PRESERVED | 能力集合/制作义务、判断与整合、学习到成品的距离、共同权力、融资非需求验证、市场与制作两次检查分别保留；均为有边界的作者分析 |
| 时效 | PRESERVED | 主线给观察年份、历史条件及2026状态；DURABLE仅指治理与核验问题，不给当前品类/渠道推荐；延伸对照可回原章时效卡 |
| 引语与权利 | PRESERVED | 新增正文独立中文转述，无虚构对白与长引语；保留作者原有判断语句，书稿继续 All Rights Reserved |
| 未核来源 | NEEDS_VERIFY | AnaitGames重访超时不作成功核验；Nintenderos页面与登记日期不同、demo相对年份待核，候选不填具体月日/年份且删除笼统辞职归责；合同、家庭、财务仍需 Lane B |

独立 AI 编辑于2026-10-09对照原章、候选、主线与旁支Ledger，确认Wehle约两年属于前作，Shin阶段、无预算/市场活动、Patti归责与Question后作财务边界保留。提出两项提交前修正：GRIS时效表可能暗定demo年份；“保留撤回空间”的原观点弱化。已分别改成demo具体年份待核，并在结尾恢复投入无效时撤回、改变合作方式或改作品的检查。除此未发现必须阻断的事实 REGRESSION。审读为非盲AI编辑意见，未重新打开外链，不构成真人测试或作者验收。

## 六维 A/B 编辑比较

| 维度 | 候选相对原稿的变化与限制 |
| --- | --- |
| 人物具体性 | demo、前作、加入阶段补上实际动作；不靠表情或内心填故事；五组人物仍只是专题窗口，不替代完整传记 |
| 连贯度 | Roset的共创直接遇见Francis的删减，Wehle改变“自己做”的含义，Playdead/Question分别压力测试长期合作与市场；省去中途虚构招聘教程 |
| 作者观点 | 主要判断在过程之后落地；学习/资本/Brigador下沉仍明确可读，原文也可查。作者需确认延伸对照的压缩是否降低锋芒 |
| 节奏 | 少一次“列问题—逐项建议—总结”的循环；章节长度服务比较，不以字数减少定优劣；五段例子是否仍太像依次摘要待读者判断 |
| 继续阅读意愿 | 编辑预期后半的两种压力能改变前半理解，但真实读者测试 NOT TESTED；无人类完成率、跳读或偏好数据 |
| 忠实性 | 已锁事实保持，并保留时代/未知边界；新增的是既有档案的叙述空间，不是外部新事实或新的研究结论 |

作者仍需判断：三种视觉障碍是否应保留原三分表；学习、融资的旁支是否值得重新放回主线；结尾是否足以保留作者原有批判；五组人物是否真正构成比较，而非只是较短的串讲。

## 交付状态与后续

暂定 AUTHOR_REVIEW_PENDING。Gunpoint #283 与 DOOM #284 当前均 OPEN、无作者 reviews，不能据此宣布其候选已进入 main。第六篇继续独立提交，不能把主分支填充目标缩为“若干 PR 已绿灯”。正式替换与合并仍需对应稿件的作者验收。

`python tools/reader_layer_lint.py` 通过；新增内容、提交消息与PR描述已做公开/跨库边界语义审阅。暂存/提交/推送接受本库现有私人内容hooks，远端结果见PR；没有为研究/schema/metadata未改的内容重复跑无关测试。

本轮完成后可让作者同时比较三份试验的不同叙述方式；当前不适合全库自动套用，也不另建新 Gate。正文替换、main合并与真人阅读效果仍未完成。
