# Creator Life / Decision Audit 024：P0 人生条件回填与第一版决策对照

- Status: RESEARCH NOTE / SECOND-WAVE BACKFILL
- Last verified: 2026-10-07
- Schema: `../../schemas/creator-life-decision-audit.md`
- Coverage: `../../metadata/creator-life-audit-coverage.json`
- Prior wave: `creator-life-decision-audit-backfill-023.md`

## 0. 本轮完成什么

023 建立统一字段并回填第一批 16 个 Case。

024 按既定 P0 清单继续补 12 个高价值 Case：

- CASE-003 Papers, Please
- CASE-012 Kenshi
- CASE-016 early id / Commander Keen → DOOM
- CASE-020 Into the Breach
- CASE-035 Factorio / Wube
- CASE-036 Manor Lords
- CASE-043 Everything
- CASE-049 Outer Wilds
- CASE-050 Nomada / GRIS → Neva
- CASE-053 Kenny Sun
- CASE-055 Factorio stop conditions
- CASE-056 Playdead founder governance

截至本轮：

- 56 个 Case 全部进入覆盖率索引；
- 28 个 Case 已显式拥有 Creator Life / Decision Audit section；
- 其中 16 个 `SUBSTANTIAL`；
- 10 个 `PARTIAL`；
- 2 个虽已显式审计，但仍为 `PENDING`，因为来源不足；
- 其余 28 个仍待后续逐案回填。

这里的“覆盖”不是成熟度，也不是成功率。

---

# 一、第一条成熟决策线：不要先买“独立开发者身份”

Papers, Please、Gunpoint、Manor Lords、Kenshi 形成四种不同的 runway 结构。

## Papers, Please

```text
AAA career capital
→ leave / bounded author project
→ public beta / Greenlight
→ evidence improves
→ add three months polish
→ if needed, return to employment
```

核心资产：
> **re-employment reversibility**

## Gunpoint

```text
salary job
→ nights/weekends
→ prototype
→ testers/devlog
→ sales threshold
→ only then quit
```

核心资产：
> **salary-funded optionality**

## Manor Lords

```text
video freelance
→ hobby development
→ Patreon / MegaGrant
→ buy back full-time focus
→ selectively hire specialists
→ publisher market perimeter
```

核心资产：
> **convert non-dilutive / community capital into author time before permanent payroll**

## Kenshi

```text
minimum-wage night shift
→ long solo systems build
→ playable / Early Access
→ player revenue
→ hire team
```

核心资产：
> **recurring low-status cashflow can be runway**

但代价极高：
- 极长时间；
- 双重劳动；
- 体力 / opportunity cost；
- scope risk。

因此不能浪漫化。

---

# 二、第二条成熟决策线：有钱以后，不一定应该扩公司

Into the Breach 是当前最干净的反例之一。

FTL 成功以后，Subset Games 有能力：

- 雇更多人；
- 公开更早；
- 融更多资；
- 做 FTL 续作。

他们却把成功主要兑换成：

- 时间；
- 不公开的自由；
- 大量扔掉工作；
- 低固定 burn；
- 低 stakeholder surface。

所以：

> **Capital can buy more capability.**
>
> 但它也可以购买：
>
> **more time to say no.**

这应成为 “有前作成功 / 有融资” reader route 的固定问题：

> 你真正缺的是更多 hands，还是更多未承诺时间？

---

# 三、第三条成熟决策线：强技术不是风险，失去停止条件才是风险

## Limit Theory

```text
strong engine capability
→ more engine / procedural obligations
→ local technical success
→ product closure stays far away
→ cancellation
```

## Factorio

```text
strong simulation capability
→ playable product
→ paying users
→ technical improvement
→ ask "is this still improving the game?"
→ explicit enough
→ redirect to closure
```

CASE-055 提供的关键不是“Factorio 写底层写对了”。

而是：

### Technical Stop Condition

- multiplayer 做到约 200 人 good connection，停止追更大数字；
- 已有简单替代解的 mechanic 可以删除；
- “done when done” 被团队自己否定；
- 1.0 前取消/推迟 campaign、fluid、GUI 等大项；
- release obligation 高于内部无限 polish。

因此：

> **Capability Capture Risk 的反面不是“少做技术”。**
>
> 而是：
>
> **给技术 frontier 一个由 player value / maintenance / release closure 定义的终止函数。**

---

# 四、第四条成熟决策线：能力可以通过四种方式进入项目

现在 C015 / Life Audit 已经能区分：

## 1. Capability-Shaped
改项目，让它适合已有的人。

例：
- The First Tree
- Gunpoint
- Papers, Please

## 2. Capability-Composed
找共同作者，让 founding capability set 发生变化。

例：
- Nomada / GRIS
- Playdead

成本不是普通工资，而是：
- equity；
- authorship；
- control；
- time-horizon negotiation；
- exit cost。

Playdead 提醒：

> **互补 founder 真实有效，也真实昂贵。**

## 3. Capability-Expanded
已有 thesis / evidence，再用资本买缺失能力。

例：
- Outer Wilds
- Manor Lords
- The Witness

关键问题：

> 什么钱，以什么 governance price，买什么能力？

## 4. Capability-Accreted
通过连续作品把自己变成另一种创作者。

例：
- Kenny Sun

```text
Flash/public artifacts
→ jam/commercial shipping
→ Harmonix gameplay programming
→ weekend indie catalog
→ indie income threshold
→ publisher-expanded solo
→ specialist team lead
```

所以“你现在是什么岗位”不再等于“你以后只能做什么”。

---

# 五、第五条成熟决策线：家庭风险和项目风险必须分账

现有 Case 已能构成三类：

## A. 个人现金风险高
- Everything：self-funded / debt risk；
- Limit Theory：Kickstarter + personal savings erosion；
- 中国 022 household cases。

## B. 个人现金风险被职业收入压低
- Gunpoint；
- The First Tree；
- Manor Lords early phase；
- Kenny Sun pre-2018。

## C. 项目风险很高，但个人 founder-cash risk 不是同一层
- Duckov；
- Gunfire Reborn；
- NExT / SYNCED；
- Outer Wilds institutional path。

以后必须禁止：

> “这项目只有 5/8/10 人，所以个人创业风险也低。”

团队规模回答的是 production question。

household cash exposure 回答的是 life-risk question。

---

# 六、第一版 Reader Life-Risk 对照

| 你的现实处境 | 最优先读 | 先防什么 |
|---|---|---|
| 有稳定工资，想做自己的项目 | Gunpoint / The First Tree | 不要把“独立身份”误当第一 milestone |
| 有成熟职业能力，准备短期离职试一作 | Papers, Please | 给实验设置时间边界和再就业路径 |
| 只能接零工 / 自由职业维持 | Manor Lords | 先买回连续开发时间，再买 permanent payroll |
| 现金少但可以长期低收入生存 | Kenshi | 不要浪漫化多年双重劳动与超大 scope |
| 第一作已经成功 | Into the Breach | 不要自动把 success 兑换成 headcount |
| 技术极强 | Factorio + Limit Theory | 给 technical frontier 设 product stop condition |
| 视觉作者，不会完整做游戏 | GRIS / Everything | 决定是找 cofounder、长期 programmer dyad，还是买 specialist capacity |
| 学生 / early-career，有很强 prototype | Outer Wilds | 先形成 thesis/evidence，再让资本扩 capability |
| 多年程序/generalist，想升级成主创 | Kenny Sun | 用连续 shipping 移动 capability frontier，不必一次完成身份跃迁 |
| 找互补 cofounder | GRIS + Playdead | 不只审能力互补，也审 equity / authorship / time horizon |
| 有公司工资的小核心 | Duckov / Gunfire / NExT | 不要把 corporate perimeter 当作“5人独立就能复制” |

---

# 七、现在“该不该辞职”可以被拆成一个更严谨的问题

不再问：

> 你够不够勇敢？

而问：

1. 现在是否已经有 playable artifact？
2. 是否有陌生人 feedback？
3. 是否已有 market signal？
4. 没辞职时，最大 bottleneck 真的是时间吗？
5. 辞职后买来的连续时间是否能关闭关键 uncertainty？
6. household monthly burn 是多少？
7. runway 结束时是否有明确 stop condition？
8. 失败后能否回原职业？
9. 是否有人依赖你的收入？
10. 你是在用 savings 买 evidence，还是买“我终于是独立开发者”的身份？

只有这些问题得到回答后，辞职才是 production decision。

---

# 八、下一批不再叫 P0

P0 读者路径核心 Case 已补齐。

后续进入 P1：

- Rocket League
- R.E.P.O.
- Project Wingman
- Minecraft
- Among Us
- Jonas Tyroller
- Landfall
- Darkwood
- Tripwire
- House House

优先目标不再是把所有 56 Case 机械填完。

而是补三种比较：

1. **work-for-hire / day job / previous revenue / grant / publisher** 不同 runway 的真实 trade-off；
2. **solo → team** 在什么时候是 evidence-following scaling，什么时候只是提前加 burn；
3. **failure residue** 是否真的给下一作留下 capability / network / code / audience。

完成后，才值得开始把 Life Audit 输出成真正 reader-facing 的互动决策入口。
