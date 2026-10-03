# 独立游戏英雄传说

**Indie Game Legendary Heroes**

作者 / 主创：**洪荒行者**

这是一个关于独立游戏开发者、工作室与作品如何被“生产出来”的长期研究与写作项目。

它不是成功学案例集，也不是把幸存者重新包装成天才神话。项目要研究的是：当开发者面对资金、时间、能力、技术、组织、发行与市场等真实约束时，他们怎样识别哪些约束不能改变，怎样重构其余变量，怎样制造自己的生存条件与生产条件，并最终把一个按行业标准答案“做不起”的项目改造成能够完成、发行和存活的项目。

核心问题可以压缩成一句：

> **这些人面对一个按照行业标准答案根本做不起的问题，是怎样改变问题本身的？**

## 项目目标

本项目同时建设三种东西：

1. **可审计的案例库**：记录开发者 / 团队的能力前史、现金流、团队结构、技术路线、范围控制、失败、市场路径与偶然性。
2. **可证伪的命题库**：检验关于独立游戏的流行解释，例如“福利国家优势”“富二代优势”“大厂履历必要”“solo 等于一个人包办全部”“零营销”“纯靠运气”等。
3. **最终书稿《独立游戏英雄传说》**：在证据积累之后，把案例与命题组织成可读的生产史，而不是先写故事再找证据装饰。

## 研究结构

本仓库不以“章节”作为最小研究单位，而以 **Case（案例）**、**Claim（命题）** 与 **Evidence（证据记录）** 为核心。

- [`cases/`](cases/)：开发者 / 团队 / 项目的可审计案例档案
- [`claims/`](claims/)：可被支持、削弱或证伪的研究命题
- [`evidence/`](evidence/)：逐案来源核实与证据边界
- [`author-corpus/`](author-corpus/)：洪荒行者历史公开文章、知乎、游戏炼乳及授权历史讨论中的作者命题来源
- [`sources/`](sources/)：作者语料、纪录片 / 演讲 / 媒体与来源方法登记
- [`sister-projects/SlavicGameLegendaryHeroes.md`](sister-projects/SlavicGameLegendaryHeroes.md)：姊妹篇《斯拉夫游戏英雄传说》的研究边界与首批产业谱系
- [`schemas/case-template.md`](schemas/case-template.md)：Case 标准结构
- [`schemas/claim-template.md`](schemas/claim-template.md)：Claim 标准结构
- [`schemas/evidence-record-template.md`](schemas/evidence-record-template.md)：Evidence 核实结构
- [`AGENTS.md`](AGENTS.md)：适用于 GPT / Codex、Reasonix、DeepSeek 等代理的研究宪法

一个 Case 可以同时支持或反驳多个 Claim；一本书的章节应当从证据网络中长出来，而不是反过来要求证据服从预先写好的叙事。

案例统一关注：

**Myth / Origin / Capability / Runway / Production / Scope / Failure / Market / Environment / Luck / Verdict / Transfer / Non-transfer / Evidence**

## 作者思想来源与证据边界

本项目的一部分问题意识来自洪荒行者此前在知乎、微信公众号“游戏炼乳”、长文与历史讨论中已经形成的系统观点。

这些历史材料在仓库中统一作为 **A0 — Author-Origin**：它们用于说明“这个命题从哪里来”，但不能因为作者以前说过就自动成为事实。

默认流程是：

> **作者旧命题 → 精确化为 Claim → 找外部 Case / P0-P1-S1 Evidence → 支持、修正或反驳。**

### 游戏炼乳与 2023 长文

作者确认：《正在到来的中度数值通胀率游戏设计革命》基本汇编了“游戏炼乳”大多数早期文章。因此它被视为**早期思想 corpus 的主要汇编母本**；公众号原始 HTML 主要用于核对发布时间、原始措辞、版本差异和遗漏文章。

2023 汇编之后的公众号文章则单列为后续增量。例如已定位：

- **《DeepSeek——第四次工业革命的瓦特蒸汽机》**（2025-02-11，游戏炼乳）——属于后期 AI / 生产力思想线，不反向视为 2023 母本已经包含。

详见 [`sources/SOURCE-001-author-platforms-and-chat-corpus.md`](sources/SOURCE-001-author-platforms-and-chat-corpus.md)。

### 历史公开行业对话

仅讨论公开行业资料的历史对话可提供研究线索；私人项目对话及其摘要不得导入，外部事实仍须重新核验。


## 游戏史来源方法：纪录片 / 演讲 / 媒体

作者过去形成大量游戏史知识时，纪录片是重要入口。本项目不会把这些来源降格为“无效记忆”，但会把它们变成可追踪的 Evidence。

默认做法：

- 开发者同期访谈、GDC / Gamescom / 本地会议演讲、开发日志、公司原始资料优先；
- 纪录片中的当事人直接证词按 P0 / P1 评级；
- 纪录片导演 / 旁白解释按 S1 / S2 评级；
- 每段关键视频证据记录 speaker、角色、录制 / 发布时间、timecode 和反证；
- 对工作室冲突、销量、预算、团队人数等硬事实尽量追到同期媒体或原始档案。

详见 [`sources/SOURCE-002-documentary-talk-media-protocol.md`](sources/SOURCE-002-documentary-talk-media-protocol.md)。

## 研究立场

本项目的默认前提不是“环境不重要”，也不是“只要努力就能成功”。相反：

- 环境决定行动集合与失败成本；
- 能力决定一个人能把多少资源转化成产品；
- 生产组织决定项目能否活到随机机会到来；
- 市场与运气影响右尾结果；
- 优秀独立开发者的重要能力之一，是**拒绝继承不适合自己的成本结构，并主动制造可生存的生产条件**。

因此，本项目同时记录帮助与阻碍，既不抹去福利、家庭、伴侣收入、储蓄、低成本地区、发行商、众筹、外包、平台红利等外部条件，也不把这些条件自动解释成成功的充分原因。

## 首批研究对象

第一轮覆盖六种不同生产结构：

- [`CASE-001 FTL / Subset Games`](cases/CASE-001-ftl.md) — **ACTIVE：已进入第一轮证据摄取**
- [`CASE-002 Rocket League / Psyonix`](cases/CASE-002-rocket-league.md)
- [`CASE-003 Papers, Please / Lucas Pope`](cases/CASE-003-papers-please.md)
- [`CASE-004 Stardew Valley / ConcernedApe`](cases/CASE-004-stardew-valley.md)
- [`CASE-005 Dwarf Fortress / Bay 12 Games`](cases/CASE-005-dwarf-fortress.md)
- [`CASE-006 R.E.P.O. / semiwork`](cases/CASE-006-repo.md)

FTL 已经建立第一份独立 Evidence Ledger：[`evidence/CASE-001-ftl-source-ledger.md`](evidence/CASE-001-ftl-source-ledger.md)。其余案例仍主要处于研究问题骨架阶段。

## 姊妹篇：《斯拉夫游戏英雄传说》

姊妹篇由原工作名《俄罗斯游戏英雄传说》改为 **《斯拉夫游戏英雄传说》**。

俄罗斯仍是主轴，但乌克兰与白俄罗斯不能再被放在边缘比较位：

- **乌克兰**：S.T.A.L.K.E.R. / GSC Game World → 4A Games / Metro → Vostok 等人才、技术与组织裂变；
- **白俄罗斯**：Wargaming / World of Tanks → World of 系列与战争网游商业化；
- **俄罗斯**：IL-2、War Thunder、Space Rangers、Pathologic、HighFleet、Escape from Tarkov 等系统 / 军事 / 作者型谱系。

其中 World of Tanks 被提升为产业级转折案例。Wargaming 官方自己把它称为公司历史的“ultimate turning point”；World of Warships 则是 WoT 成功后 World of 系列的直接扩张。

同时，仓库已经把一个强命题纠偏：

> “没有 World of Tanks 就没有 War Thunder”作为字面因果 **不成立**。Gaijin 创始人明确表示 War Thunder 在 WoT 上线前已经开始开发；更合理的待验证命题是 WoT 证明了军武 F2P 在线游戏存在巨大市场，从而改变了 War Thunder 所处的品类合法性和市场窗口。

S.T.A.L.K.E.R. → 4A Games 也将作为组织史主线研究。现有证据支持工资 / royalties / 管理冲突与核心人才出走，但暂不把作者过去“labor union 造反”的比喻写成字面工会史。

详见 [`sister-projects/SlavicGameLegendaryHeroes.md`](sister-projects/SlavicGameLegendaryHeroes.md)。

## 工作原则

- **证据先于叙事。** 先建立时间线、来源与反证，再写故事。
- **证伪优先。** 每个重要命题都要主动寻找反例、替代解释和缺失变量。
- **一手资料优先。** 开发者同期访谈、演讲、开发日志、众筹页、公司资料、财务 / 法务记录等优先于多年后的二手神话。
- **纪录片按片段评级。** 当事人原话、档案画面、导演旁白不能混成一个证据等级。
- **区分必要、充分与概率增益。** “不是必要条件”不等于“没有影响”。
- **拒绝幸存者偏差。** 成功者做过某件事，不意味着那件事导致成功。
- **把前史算进开发史。** 技能、旧项目、失败原型、合同工作和职业经验不因“正式开工日”而消失。
- **不把术语当事实。** `solo dev`、`zero marketing`、`three-person team` 等必须拆开核验。

## 当前阶段

**Phase 2 — Evidence Ingestion**

项目宪法、权利结构、Case / Claim / Evidence schema、作者语料层与首批六案已经建立；CASE-001 FTL 已完成第一轮证据摄取；姊妹篇已经完成第一次产业主轴纠偏。

当前优先级：

1. 继续补 FTL 的 savings / monthly burn / Shanghai cost / contributor map / prototype scope 证据缺口；
2. 启动 CASE-002 Rocket League / Psyonix 的 work-for-hire → SARPBC → Rocket League 生产史；
3. 为《斯拉夫游戏英雄传说》建立 World of Tanks / Wargaming、S.T.A.L.K.E.R. / GSC → 4A、War Thunder / Gaijin 三条正式 Evidence Ledger；
4. 持续把知乎“洪荒行者”、游戏炼乳、2023 长文、后期公众号文章和非机密历史 ChatGPT 分析转成 A0 作者命题，再交给外部证据审计；
5. 系统补纪录片、GDC / Gamescom / 本地演讲与同期媒体来源，不再只依赖网页文章和后来的 Wiki 归纳。

## 传播、权利与许可

本项目希望论证被看见、讨论和传播，但不希望第三方未经许可改写成另一个版本、制造“洪荒行者其实是在说……”的伪官方解释，或直接拿去商业出版。

因此采用分层许可：

- **公开研究内容**：`cases/`、`claims/`、`schemas/` 及其他明确作为公开研究发布的原创非软件内容，采用 **CC BY-NC-ND 4.0**。欢迎非商业地复制、转发、镜像和重新发布未经改编的原文，但必须合理署名，且不得发布未经授权的改写、翻译或其他衍生版本。详见 [`LICENSE-CONTENT`](LICENSE-CONTENT)。
- **正式书稿**：未来 `book/` 目录中的正式章节、出版稿，以及任何明确标注 `All Rights Reserved` 的内容，均为 **© 2026 洪荒行者。All Rights Reserved.**
- **工具代码**：明确属于软件 / 工具范围内的脚本、构建工具、检查器等代码，按 [`LICENSE-CODE`](LICENSE-CODE) 的 MIT License 授权。
- **第三方材料**：引用、截图、商标、采访内容及其他第三方材料仍属于其各自权利人；本项目不会因为引用它们而取得重新授权的权利。

### Canonical source / 权威原文

欢迎对本项目进行摘要、评论、批评和讨论，但第三方解释只代表其作者。

如需确认“洪荒行者 / 《独立游戏英雄传说》究竟主张什么”，请以本仓库中对应 Case / Claim / Essay 的**最新版原文**为准。第三方不得因转载、评论或引用而暗示其版本获得洪荒行者或本项目的官方背书。

合理署名时，建议至少保留：

> 作者：洪荒行者  
> 项目：《独立游戏英雄传说 / Indie Game Legendary Heroes》  
> 原文：对应 GitHub canonical URL  
> 许可：CC BY-NC-ND 4.0

公开可读不等于放弃版权；鼓励传播也不等于允许商业利用或擅自改写。
