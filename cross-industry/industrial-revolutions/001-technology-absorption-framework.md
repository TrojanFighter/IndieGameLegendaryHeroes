# 001 — Technology Absorption Framework

- Status: WORKING FRAMEWORK
- Purpose: 统一记录“技术出现 → 真正改变产业”的时间差。
- Boundary: 不用于生成私人项目设计方案；只研究公开历史与产业吸收。

## 1. Technology Availability ≠ Technology Absorption

“某技术已经存在”至少可能指四种完全不同的状态：

| 层级 | 定义 | 典型问题 |
|---|---|---|
| Frontier availability | 少数实验室/顶尖团队能做到 | 成本、可靠性、人才是否不可承受？ |
| Professional diffusion | 资金充足的专业组织能稳定采购/使用 | 是否需要专门团队与重资产？ |
| Small-team / indie diffusion | 小公司、独立开发者可以合理负担 | 是否出现通用工具、托管服务、标准接口？ |
| Mass availability | 普通用户/创作者把它视为默认基础设施 | 竞争优势是否已从“拥有技术”转移到“怎么用”？ |

因此写“某年技术已经成熟”必须说明是哪一级。

## 2. 六阶段吸收链

### A. Invention

原理或装置第一次成立。

研究问题：
- 是实验室 demo 还是可重复装置？
- 发明者解决了什么具体问题？
- 同时存在哪些替代技术？

### B. Engineering maturity

研究：
- reliability；
- yield；
- maintenance；
- manufacturability；
- tooling；
- skill bottleneck。

技术有用但“难伺候”时，往往还没有真正进入大规模生产。

### C. Economic viability

最重要的问题不是 benchmark，而是：

> **它是否跨过某个真实业务的成本/收益线？**

记录：
- capital cost；
- operating cost；
- energy / compute / labour requirement；
- lifetime；
- switching cost；
- incumbent alternative。

### D. Diffusion

研究：
- 谁先采用；
- 哪个行业先采用；
- 哪些基础设施与标准使它扩散；
- 人才培养是否跟上；
- 地区扩散是否显著滞后。

### E. Complementary fit

很多技术真正的价值要等另一套东西出现：

- 新工厂布局；
- 新供应链；
- 新交通网络；
- 新军事 doctrine；
- 新平台；
- 新商业模式；
- 新分发渠道；
- 新监管/标准。

所以“killer application”应理解为**技术 × 场景 × 组织**的匹配，而不是宿命论。

### F. Absorption / organizational redesign

组织是否真正围绕新技术重新设计自己？

如果只是：
- 买了新机器；
- 保持旧流程；
- 保持旧岗位；
- 保持旧 KPI；

就可能出现长时间 productivity lag。

## 3. 强制时间字段

每个重要技术尽量记录：

- Frontier date
- First robust engineering date
- First economically convincing use
- Professional diffusion range
- Small-team diffusion range
- Mass diffusion range
- First high-profile complementary-fit cases

不知道就写 UNKNOWN，不用“差不多在某年代”伪精确。

## 4. 技术机会窗口

对于人物/公司案例，建立：

| 当时可用技术 | 相比上一代降低的约束 | 仍然昂贵/困难的部分 | 当事人是否明确识别 | 实际 artifact | 同时代对照 |
|---|---|---|---|---|---|

真正需要解释的是：

> **同一时代很多人都能接触技术，为什么少数人率先把它组合成新产品？**

## 5. 失败与冷板凳

特别追踪：

- 发明后多年低利用；
- 技术先进但没有需求；
- 技术有需求但成本线未过；
- 组织采用却没有重构流程；
- 错误 killer app；
- 战争/危机/供应链变化突然改变 relative advantage；
- 替代技术反超；
- 先行者失败、后来者成功。

冷板凳不是“技术没价值”的同义词，也不是“历史终将证明它”的保证。

## 6. 与游戏产业分代的接口

游戏技术史不只按硬件规格分代，而按“开发者可行解空间”分代。

至少同时记录：
- compute / memory / storage；
- input / display；
- networking / backend；
- engine / middleware / authoring tools；
- distribution / payment；
- mod / UGC substrate；
- creator discovery；
- financing / Early Access / crowdfunding；
- AI / agentic tools。

详见 [003](003-game-industry-technology-regimes.md)。

## 7. 禁止推论

- frontier demo = industry adoption；
- benchmark improvement = useful product；
- cheaper tool = no skill bottleneck；
- AI assistance = complete autonomous production；
- one successful use case = general-purpose proof；
- later dominance = original inventor already understood final use。
