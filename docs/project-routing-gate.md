# Project Routing Gate / 跨项目写入边界

**Owner：Lane A / Library Operations。适用所有 GPT、Codex、其他 Agent 与人工 PR。**

本协议解决已发生的错误：研究讨论与另一个项目的“教育、创新、决策、游戏设计、流程治理”等主题重叠，Agent 却依据旧上下文或近期记忆选择了错误的 Git 仓库。本协议只控制**写入去向**，不替代 [research authority map](../schemas/research-authority-map.md) 或 [public/private boundary](public-research-boundary.md)。

## 1. 唯一写入目标

```text
Target repository: TrojanFighter/IndieGameLegendaryHeroes
Publication: public research / book
Default branch: main (protected)
Changes: named topic branch → PR → required checks → author/maintainer acceptance
```

`main` 是已发布的研究基线，不意味着所有 Case 都已经 VERIFIED。用户要求“录入 / 写入 / 合并”时，**优先使用当前对话明确指定的项目与仓库**；不能仅凭最近另一项目的工作记忆、熟悉的关键词，改变目标仓库。

**允许作为本仓库内容：**

- 可由独立公开来源支撑的行业、开发者、教育/创作者、技术、公司、制度及跨国比较研究；
- 符合本仓库 `PROGRAM-MAP.md` 的中国、斯拉夫、独立游戏、跨行业理论研究；
- Case / Evidence / Claim / Signal / Author-Origin / 研究笔记 / 公开书稿以及各自的审计；
- 为本仓库独立整理、不含另一项目内部事实的通用治理方法。

**禁止作为本仓库内容：**

- 另一项目的未公开设计、世界观、玩法、内部工作流、制作任务、预算、融资、谈判、私人人员资料；
- 为另一个具体项目量身订制的策略、建议、里程碑或执行清单，即使删除项目名也不允许；
- 未经授权的私人聊天、文件、屏幕内容、原始 signal 身份资料；
- 任何仅因为“当前讨论过”“AI 曾给出过”就自动晋级的事实。

通用行业词（例如市场接入、作品范围、创新、技术、教育）**不是私有污染的充分证据**。应检查内容的实际对象、证据 Owner、直接用途和可识别性，不能靠禁词删除合法研究。

## 2. Write Preflight / 写入前五问

在任何 `create_file / update_file / delete_file / commit / PR` 前，Agent 先在其任务计划或 PR 中明确回答：

1. **Repository identity：** 当前 Git remote 或 connector 的精确 `owner/repo` 是什么？是否与本次对话指令一致？
2. **Workstream：** 这是 Lane A（库治理）、B（案例/课题研究）还是 C（书稿）？话题为什么属于**本库**，而不是因为关键词相似被路由过来？
3. **Canonical owner：** 这条事实或判断的主档在哪里？有没有已存在的入口？是否属于外部输入而非已采纳事实？
4. **Write perimeter：** 本次明确允许修改哪些文件、哪些内容不改？是否会跨库复制未经公开授权的信息？
5. **Review / reversible exit：** 是否从最新 `main` 开分支、经过 PR 与必要检查、保留回退路径？用户是否明确批准了当前目标？

如果第 1、2、4 问不能确定：**暂停写入并记录路由歧义**；可以继续只读检索，但不能先往“似乎相关”的仓库提交再等待用户纠错。

### Cross-project method reuse

另一个项目的流程经验可能有用，但必须：

- 在新仓库中**独立表述成一般方法**，不能复制私人项目实例、目录、角色、参数或决策历史；
- 尊重新仓库现有 status / schema / owners，不把另一项目的规范性词汇硬套进来；
- 通过本仓库自己的 Lane A PR 验证，且不把来源项目的内部文件或名称写进公共仓库；
- **借鉴方法 ≠ 搬运内容 ≠ 获得另一个项目的修改授权**。

## 3. 发现疑似串库后的精确回退

**先审计，后回退；不得“按关键词全部删除”，也不得重写公开历史掩盖问题。**

1. 核验正确仓库与错误目标仓库的访问权限、最新 default branch 及相关时段的 PR/commits。
2. 以 source conversation / PR purpose / commit diff / file path 为证据，形成**私下维护**的逐文件清单：时间、SHA、路径、误入内容、是否被后续正确修改。
3. 分为：
   - `WRONG_DESTINATION`：本应进别库的内容、在本库无独立 Owner/用途；
   - `VALID_ADAPTATION`：已经独立转译并得到作者批准的通用方法；
   - `IN_SCOPE`：本库正常研究或正式设计/编辑内容；
   - `NEEDS_REVIEW`：不能仅凭关键词判定的混合文档。
4. 对 `WRONG_DESTINATION` 在**实际受影响仓库**开单独修复分支与 PR。纯误写且提交独立，可 revert 整 commit；混合提交必须只撤错误 hunk，并复核前后引用、索引和派生文件。
5. 保留 `VALID_ADAPTATION` 与 `IN_SCOPE`。任何可能影响正式已批准内容的删除，都要作者审阅 diff 后再合并。
6. 若涉及可能公开泄露的私人材料，按项目私有内容安全流程处置；普通 Git revert **不等于**从 Git 历史和缓存中擦除敏感内容。不要把私人对象名称或命中原文复制到公共 issue、PR 和 CI 日志。
7. 验证受影响文档、CI、关系索引，逐项报告“已回退 / 仍待审 / 无法访问”。**无文件和差异证据时，不得宣称已经清理干净。**

**重要边界：**公开研究仓库只能控制自己的内容与提交；即使另一仓库确实存在误写，也必须在该仓库的权限与 PR 流程中独立修复。修改这里的 routing rule **不等于**完成另一仓库的回退。

## 4. PR 与审计交接

对可能跨项目的话题，PR 应回答：

- 本次写入目标仓库已核对；
- 话题的领域归属和公共来源已核对；
- 没有从私人项目导入事实或执行计划；
- 改动文件与 canonical owner 明确；
- 跨库借鉴如有发生，仅为**独立的通用方法**，不是数据复制或修改对方仓库；
- 如发现先前错误，修复 PR 引用**本仓库可公开的**直接 diff，私有污染证据仍保留于受限位置。

本协议与 `private-content-guard` 协同：守卫提供自动拦截，项目路由需要人/Agent 做语义判断；两个检查均不能单独替代另一个。
