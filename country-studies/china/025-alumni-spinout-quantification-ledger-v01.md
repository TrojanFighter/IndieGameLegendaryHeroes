# 025 — Alumni → Spinout Quantification Ledger v0.1

- Program: C / 中国国情研究 × Creator Mobility × Creator Class
- Status: **PRELIMINARY LOWER-BOUND LEDGER / DENOMINATOR NOT YET COMPLETE**
- As-of: 2026-10-08
- Parent: [024 — Creator Mobility & Spinout Topology](024-creator-mobility-spinout-topology-noncompete.md)
- Related: [023 — Creator Class Formation](023-creator-class-formation-intergenerational-reproduction.md)
- Rule: **个案存在不等于数量级相同；无法获得senior-alumni分母时，只报已验证下限，不伪造“创业率”。**

## 0. 这份表解决什么

此前常见叙述会混淆四种完全不同的“后代”：

1. `DIRECT SPINOUT`：核心前员工离开母公司，直接创办新工作室；
2. `SERIAL FOUNDER DESCENDANT`：同一个前员工在之后继续创办第二/第三家公司；
3. `ALUMNI LANDING`：前员工进入已有公司并带去知识，但不是创始人；
4. `DESIGN / CULTURAL DESCENDANT`：作品理念受母公司影响，但人员没有直接谱系。

本表只在第1类上做“spinout node”计数；其余单独记录。

因此：
> Looking Glass影响Arkane ≠ Arkane就是Looking Glass spinout。  
> Valve雇佣modder ≠ Valve alumni spinout。  
> 同一个Romero连续开三家公司 ≠ 三个独立“新创始人”样本。

## 1. 统一字段

每个母公司记录：

- `verified_direct_spinout_nodes_lower_bound`
- `unique_alumni_founders_lower_bound`
- `serial_founder_nodes`
- `shipped_first_title`
- `second_title`
- `3y_survival`
- `second_generation_spinout`
- `parent_support`: hostile / neutral / supportive / investor / first-client
- `dominant_reproduction_mode`:
  - spinout
  - alumni landing
  - community→professional
  - publisher/incubator
  - internal entrepreneurship
- `denominator_quality`: none / weak / medium / strong

当前版本不计算：
`spinout_conversion_rate = founders / senior alumni`
因为绝大多数公司尚无可信senior-alumni总数。

## 1.1 Spinout账本不再承担Indie判断

025只回答：
> **母公司是否产生新的产权/创业节点？**

它不再从“founder”直接推导“indie creator”。

详细拆分见：
- [026 — Spinout ≠ Indie](026-spinout-vs-indie-mode-conversion.md)

新增可选字段：
- `spinout_mode`: SCALE-CONTINUITY / AUTHORIAL-STUDIO / INDIE-MODE / INFRASTRUCTURE-CAPITAL-TOOL / UNKNOWN；
- `authorial_divergence`: HIGH / MEDIUM / LOW / UNKNOWN；
- `indie_mode_affinity`: HIGH / MEDIUM / LOW / UNKNOWN；
- `mode_by_phase`: 若工作室随年份/项目改变生产方式，必须按阶段记录。

强制规则：
- founder-owned ≠ indie；
- new genre ≠ new objective function；
- small team ≠ indie；
- premium ≠ indie；
- venture-backed ≠ automatically non-indie；
- 同一studio不可被永久贴一种production-mode标签。

---

# 2. Atari — 高直接spinout、早期级联非常清楚

## 2.1 已验证G1 direct spinouts

### Activision — 1979
- David Crane
- Alan Miller
- Bob Whitehead
- Larry Kaplan
均为Atari程序员/设计人员出走创办。

机制：
- credit + royalty争议；
- 第三方软件公司；
- 首批产品成功。

Sources:
- https://www.gamedeveloper.com/business/atari-the-golden-years----a-history-1978-1981
- https://www.atarimagazines.com/v3n2/levy.php

### Imagic — 1981
Atari contingent至少包括：
- Bill Grubb
- Dennis Koble
- Rob Fulop
- Bob Smith
及其他成员，与Mattel人员共同创办。

Source:
- https://www.atarihq.com/othersec/library/imagic.html

### Videa → Sente — 1981/82
- Howard Delman
- Roger Hector
- Ed Rotberg
均直接从Atari离开后创办Videa。

Sources:
- https://www.gamedeveloper.com/business/atari-the-golden-years----a-history-1978-1981
- https://www.ataricompendium.com/archives/interviews/howard_delman/interview_howard_delman.html

## 2.2 G2 / serial-founder

### Accolade — 1984
Alan Miller、Bob Whitehead：
Atari → Activision → Accolade。

这应算：
- Atari lineage的第二个创业节点；
- 但不是新的unique alumni founders。

Source:
- https://www.ataricompendium.com/archives/interviews/alan_miller/interview_alan_miller.html

### Sterling Silver / Polygames
Dennis Koble等人在Imagic/Sente后继续建立独立开发公司。

Source:
- https://www.ataricompendium.com/archives/interviews/lee_actor/interview_lee_actor.html

## 2.3 v0.1 lower bound

- direct G1 studio nodes: **≥3**
- unique direct alumni founders: **≥11**
- second/serial organizational nodes: **≥2**
- reproductive depth: **≥2 generations**
- dominant mode: **spinout cascade**
- denominator quality: **weak**

### 解释
Atari不是“一个Activision神话”。
在1979–82短时间内至少出现Activision、Imagic、Videa三条直接外生枝条；Activision成功本身又成为后来者可见的职业脚本。

---

# 3. Looking Glass — 思想影响远大于严格direct-spinout数量

## 3.1 已验证direct spinout

### Irrational Games — 1997
- Ken Levine
- Jonathan Chey
- Robert Fermier
均为Looking Glass员工。

Looking Glass在Irrational首个publisher项目失败后又给：
- 小预算；
- 办公空间；
- System Shock 2机会。

Sources:
- https://www.pcgamer.com/the-story-of-irrational-the-studio-that-shut-down-to-rediscover-its-roots/
- https://irrationalgames.ghoststorygames.com/insider/from-the-vault-15-year-anniversary-edition/

### Floodgate Entertainment — 2000
Looking Glass创始人Paul Neurath在LGS关闭后创办；
团队包含多位前Looking Glass员工。

Source:
- https://techcrunch.com/2011/03/18/zynga-buys-mobile-and-video-game-developer-floodgate-entertainment/

## 3.2 不计入direct-spinout但必须记录的扩散

### Harmonix
Harmonix并非由Looking Glass alumni创办；
但Greg LoPiccolo等LGS员工加入后，对Harmonix转向游戏开发和早期设计有显著作用。

Source:
- https://www.vice.com/en/article/the-oral-history-of-guitar-hero/

### OtherSide Entertainment
Paul Neurath在Floodgate / Zynga之后再次创办；
并重新聚集多个Looking Glass alumni。

Source:
- https://en.wikipedia.org/wiki/OtherSide_Entertainment

这属于：
`serial founder / alumni recombination`
而不是新的独立“第二代创始人”样本。

## 3.3 v0.1 lower bound

- direct G1 studio nodes: **≥2**
- unique direct alumni founders: **≥4**
- serial founder nodes: **≥1**
- second-generation spinout: **未充分验证**
- dominant mode: **alumni landing + design diffusion + selective spinout**
- denominator quality: **weak**

### 重要修正
“Looking Glass家谱”常把：
- Irrational
- Arkane
- Harmonix
- Ion Storm
等都画在一棵树上。

严格人员创业谱系却没有这么简单。

因此新增：
# `GENEALOGY INFLATION RISK`

> **媒体把设计影响、合作、人才流入和真正spinout都画成“后代”，会夸大组织再生产率。**

---

# 4. Blizzard — 当前样本中最明显的高密度spinout机器之一

## 4.1 已验证G1节点 lower bound

### ArenaNet — 2000
- Mike O'Brien
- Patrick Wyatt
- Jeff Strain
均来自Blizzard。

Source:
- https://www.gamedeveloper.com/game-platforms/ncsoft-acquires-arenanet

### Flagship Studios — 2003
由多位Blizzard North核心人员创立，包括：
- Bill Roper
- David Brevik
- Max Schaefer
- Erich Schaefer
等。

Source:
- https://www.mobygames.com/company/4165/flagship-studios/

### Carbine Studios — 2005
由一批前Blizzard员工创建。

Source:
- https://www.gamedeveloper.com/business/-i-wildstar-i-developer-carbine-studios-is-no-more

### Bonfire Studios — 2016
前Blizzard CCO / WoW lead designer Rob Pardo创办。

Source:
- https://www.bonfirestudios.com/

### Second Dinner — 2018
Ben Brode、Hamilton Chu等前Hearthstone领导层创办。

Source:
- https://ir.netease.com/static-files/310863ab-3c0a-4bea-a933-6890c6f234be

### Dreamhaven — 2020
Blizzard联合创始人/前CEO Mike Morhaime与大量前Blizzard veteran创办；
下设Moonshot、Secret Door。

Source:
- https://www.dreamhaven.com/news/announcement

### Frost Giant — 2020
Tim Morten、Tim Campbell等Blizzard RTS veteran创办。

Source:
- https://www.windowscentral.com/frost-giant-studios-rts-team-blizzard-entertainment-veterans

### Notorious Studios — 2021
Chris Kaleiki、Doug Frazer等前Blizzard成员创办。

Source:
- https://www.washingtonpost.com/video-games/2022/06/08/asmongold-wow-notorious-blizzard/

### Magic Soup Games — 2023
Jen Oneal、J. Allen Brack、John Donham创办。

Source:
- https://www.gamesradar.com/former-blizzard-co-head-and-president-form-new-inclusive-studio-in-aftermath-of-activision-lawsuit/

## 4.2 G2 / deeper descendants

### ArenaNet → Undead Labs
Jeff Strain：
Blizzard → ArenaNet → Undead Labs。

### ArenaNet / Undead Labs → Possibility Space
Jeff Strain继续创建Possibility Space。

Source:
- https://gameinformer.com/2021/10/13/arenanet-undead-labs-founder-jeff-strain-opens-new-studio

### Blizzard North → Flagship → Runic
Flagship之后，Max/Erich Schaefer等又进入Runic体系。

这显示：
- serial founder depth；
- organizational lineage depth；
都超过一代。

## 4.3 v0.1 lower bound

- verified direct G1 studio nodes: **≥9**
- unique alumni founders: **明显>10，尚未完整去重**
- reproductive depth: **≥3 organizational steps in some lineages**
- shipped-first-title rate: **混合；有Guild Wars / WildStar / Marvel Snap / Stormgate等，也有未发布或失败**
- dominant mode: **spinout + alumni network + founder recombination**
- denominator quality: **weak**

### 当前结论
Blizzard是本轮最需要做正式分母的公司。
因为“能举出9个以上直接节点”已经不是孤例，但仍不能在没有senior-alumni总数时写：
> “Blizzard创业率是X%”。

---

# 5. id Software — 少量核心人物产生高serial-founder密度

## 5.1 已验证G1

### Ion Storm — 1996
John Romero、Tom Hall等创办。

Source:
- https://www.pcgamer.com/the-history-of-ion-storm/

### Crack dot Com
前id程序员Dave Taylor离开后共同创办。

Source anchor:
- https://en.wikipedia.org/wiki/Id_Software

## 5.2 serial-founder网络

Romero / Hall:
- id
→ Ion Storm
→ Monkeystone

Romero later:
→ Romero Games

Mike Wilson:
- id marketing
→ Ion Storm
→ Gathering of Developers
→ later Devolver Digital

因此id lineage特点不是：
> “大量不同员工各自创业”。

更像：
> **少量核心高可见人才反复创业、出版、建新组织。**

## 5.3 v0.1 lower bound

- direct G1 studio nodes: **≥2**
- unique alumni founders: **≥4**
- serial organizational nodes: **≥4**
- dominant mode: **high serial-founder intensity**
- denominator quality: **weak**

---

# 6. Valve — 外向spinout不突出，community→professional非常强

## 6.1 严格direct-spinout已验证

### Stray Bombay — 2019
前Valve writer/designer Chet Faliszek与Kimberly Voll创办。

Sources:
- https://arstechnica.com/gaming/2019/03/former-valve-designer-writer-dishes-on-his-new-co-op-game-studio/
- https://www.gamedeveloper.com/business/chet-faliszek-and-kimberly-voll-form-co-op-game-studio-stray-bombay

目前按严格口径，本轮未验证出与Blizzard同量级的Valve direct game-studio spinout密度。

## 6.2 但Valve的主要再生产模式不同

Valve长期将：
- Counter-Strike
- Dota
- Team Fortress
- Portal等
社区/mod人才吸收到专业生产体系。

因此Valve更适合编码：

# `INBOUND CREATOR ABSORPTION`

而非：
# `OUTBOUND SPINOUT FACTORY`

## 6.3 v0.1 lower bound

- verified direct game-studio spinout nodes: **≥1**
- dominant reproduction mode: **community→professional absorption**
- denominator quality: **weak**

### 方法论价值
若只比较spinout数量，会低估Valve对creator-class reproduction的贡献。
所以Forest Test必须同时保留：
- outward ownership formation；
- inward professionalization。

---

# 7. Tencent — 已有多条强G1，但当前不能计算转化率

## 7.1 莉莉丝 — 2013

王信文、袁帅、张昊：
- 南京大学同学；
- 均曾在腾讯游戏工作；
- 2013离职共同创办莉莉丝。

Sources:
- https://software.nju.edu.cn/yyzj/yyfc/2005j/20200127/i69440.html
- https://ancient.lilith.com/cn/dt_detail_20170103.html

结果：
- shipped；
- 多作持续；
- 公司扩大；
- 后续具备投资/发行能力。

### 反向外部性
公开报道指出《刀塔传奇》成功后，腾讯内部手游组织也受到刺激并调整。

Source:
- https://m.thepaper.cn/newsDetail_forward_30424409

这属于：
# `SPINOUT → INCUMBENT LEARNING`

不仅是新人从大厂学习；
大厂也会从成功spinout反向学习。

## 7.2 游戏科学 — 2014

7名《斗战神》相关腾讯员工离开后成立。

Sources:
- https://www.scmp.com/tech/big-tech/article/3275526/black-myth-wukongs-popularity-brings-unexpected-windfall-fame-low-profile-developer
- https://m.thepaper.cn/newsDetail_forward_30424409

结果：
- 多个手游项目；
- Black Myth: Wukong；
- 形成强studio brand。

## 7.3 身梦科技 — 2023

张哲川带NExT创意工坊部分成员离开后创业。

Source:
- https://www.sohu.com/a/719659296_204824

它是很重要的：
`internal frontier → external spinout`
案例。

## 7.4 AutoGame — 2023

前《和平精英》技术策划张昊阳创业；
已有多轮融资。

Source:
- https://www.taptap.cn/moment/748355307826054818

## 7.5 沈黎新孵化/投资结构 — 2025

前NExT Studios总经理沈黎离开腾讯后做新的游戏投资与孵化机构，
目标包括降低创业者早期风险、在公司盈利后保障创业者控制权。

Source:
- https://www.sohu.com/a/852766962_204824

该节点不是纯studio，
应编码：
`alumni → creator-capital infrastructure`。

## 7.6 v0.1 lower bound

- verified direct creator-owned studio nodes: **≥4**
- verified creator-capital/infrastructure nodes: **≥1**
- unique founder alumni: **≥12**（Game Science 7 + Lilith 3 + others；仍需严格去重）
- reproductive depth: **主要仍是G1，G2待追**
- denominator quality: **none**

### 当前不能说
- “腾讯创业率低/高”
- “腾讯比Blizzard少X倍”

因为腾讯senior game alumni分母巨大且公开不足。

### 当前可以说
> **腾讯已经明确是中国重要的creator-founder训练母体之一；真正未知的是其spinout密度相对于员工规模，以及这些spinout是否继续产生第二代。**

---

# 8. NetEase — 2025–26出现明显“资深制作人出走创业波”

## 8.1 简悦 — 2011
前网易COO詹钟晖（叮当）离职后创办简悦；
之后被大厂收购，2025再次创业做内容驱动买断制游戏。

Source:
- https://www.36kr.com/p/3286565715272581

这说明网易早期已有高层spinout，
且存在：
`serial founder re-entry`。

## 8.2 芥子游戏 / Seed Games — 2025
前《阴阳师》《哈利波特：魔法觉醒》制作人金韬
+ 前网易艺术设计中心负责人易修钦创业；
2026已获数千万美元融资，团队>60人。

Source:
- https://finance.sina.cn/2026-03-17/detail-inhrhpmq5406347.d.html

## 8.3 李凯明新公司 — 2026
前《率土之滨》《无尽的拉格朗日》核心负责人李凯明离开网易创业；
公开报道显示获得米哈游、IDG等投资。

Source:
- https://www.sohu.com/a/1000168387_204728

## 8.4 GreaterThan Group — 2026
前网易游戏全球投资与合作负责人朱原创业建立游戏控股/投资机构，
并吸收部分网易裁撤团队。

Source:
- https://finance.sina.com.cn/stock/aigcy/2026-06-04/doc-iniafrtu9377059.shtml

该节点应编码：
`alumni → capital allocator / studio holding infrastructure`。

## 8.5 v0.1 lower bound

- verified creator-studio / founder nodes: **≥3**
- creator-capital infrastructure: **≥1**
- 2025–26 cohort age: **太新，无法评估ship/second-title**
- dominant current signal: **late-career senior producer spinout wave**
- denominator quality: **none**

### 重要新H
网易可能正进入：
# `LATE INCUMBENT SPINOUT WAVE`

即成熟工业培养十年以上的制作人，
在2025–26开始集中转成owner/founder。

若未来3–5年ship率高，
中国的Mobility-to-Ownership Conversion可能正在发生结构变化。

---

# 9. miHoYo — 公司年轻，但第一批alumni创业节点已经出现

miHoYo 2012才成立，
因此不能与Atari/Blizzard几十年窗口直接比较。

## 9.1 “踢踢” / 《微光之镜》
前miHoYo员工离职后独立开发约4年，
作品进入2022首批恢复发放版号名单，并进行众筹。

Source:
- https://news.yxrb.net/202205/10229660.html

这是：
`employee → solo creator`
而非传统大团队spinout。

## 9.2 鸟鸣啾唧 / HAKU
前《崩坏学园2》制作人曹霞创业，
2025推出《黄金四目》；
产品上线数月后停止服务/团队遇到严重经营困难。

Sources:
- https://www.taptap.cn/moment/648384987548092630
- https://www.taptap.cn/moment/705078054069731958

这是极有价值的失败样本：
> 高履历creator spinout ≠ 市场成功。

## 9.3 梦熵科技 / 贺甲
前miHoYo技术总监贺甲后经腾讯/艺画开天等经历，
2025成立创业公司，
方向包括AI游戏/AI虚拟伴侣。

Source:
- https://www.36kr.com/p/3646227562106759

严格来说它是：
`former-miHoYo lineage startup`，
不是直接离开miHoYo即创业。

## 9.4 余洋新团队 — 2026
前《崩坏：星穹铁道》技术负责人余洋离开后创业，
公开招聘指向UE多人合作PvE英雄射击项目。

Source:
- https://www.sohu.com/a/1025571267_204824

目前尚未ship。

## 9.5 “恶少” / Krene — 2025
前《原神》早期主创离开后做AI游戏创作工具创业，
目标之一是帮助更多小团队/个人创作。

Source:
- https://podcasts.apple.com/cn/podcast/id1729552193?i=1000738998838

应编码：
`alumni → creator-tool infrastructure`，
而非纯游戏studio。

## 9.6 v0.1 lower bound

- verified creator/spinout nodes: **≥4**
- creator-tool infrastructure: **≥1**
- shipped nodes: **至少2**
- failure node: **至少1明确**
- observation window: **短**
- denominator quality: **none**

### 解释
miHoYo现在最大的研究价值不是“创业率”，
而是：
> **第一代Genshin/Honkai核心人员正在从employee reputation向owner/tool-builder转换；未来5年正好可以做前瞻追踪。**

---

# 10. Preliminary Matrix

| Parent | Verified direct/creator spinout lower bound | Reproductive depth | Dominant mode | Current read |
|---|---:|---:|---|---|
| Atari | ≥3 G1 | ≥2 | direct spinout cascade | very early high outward reproduction |
| Looking Glass | ≥2 G1 | unclear | selective spinout + alumni/design diffusion | cultural influence > strict spinout count |
| Blizzard | ≥9 G1 | ≥3 in some lineages | dense spinout + alumni network | strongest apparent spinout machine in current sample |
| id | ≥2 G1; several serial nodes | ≥2 | serial-founder entrepreneurship | concentrated in few highly mobile founders |
| Valve | ≥1 strict G1 | unclear | community→professional absorption | inward reproduction stronger than outward spinout |
| Tencent | ≥4 creator studios + ≥1 infrastructure | mostly G1 | large-incumbent → founder | clearly important parent; denominator missing |
| NetEase | ≥3 creator founders + ≥1 infrastructure | mostly G1 | senior producer late spinout | visible 2025–26 wave, too early for outcomes |
| miHoYo | ≥4 lineage nodes + ≥1 tool node | G1 | creator/solo/tool spinout | young parent; excellent prospective cohort |

**禁止把这张表当排名。**
时间窗口、员工规模、公司年龄、地区和“direct”定义差异极大。

---

# 10.1 Spinout数量不能回答“Indie School”

025当前样本经026修正后，应这样读：

| Parent | Founder/ownership reproduction | Indie-mode inference |
|---|---|---|
| Atari | strong early spinout cascade | independent-production ancestor；不能套现代indie标签 |
| Looking Glass | selective direct spinout + broad influence | authorial exits存在；逐案判断 |
| Blizzard | strong alumni-founder ecology | **不能据此推断高indie conversion** |
| id | serial-founder strong | early independent lineage较强；后续混合 |
| Valve | outward spinout较少 | community→professional强；不是同一指标 |
| Tencent | clear founder school | Lilith等商业创业≠indie；Game Science是阶段性/延迟作者转型 |
| NetEase | visible owner-conversion wave | indie-mode affinity当前大多UNKNOWN |
| miHoYo | heterogeneous exit routes | solo / commercial / tool / creator routes需分开 |

所以：
> **Founder School 和 Indie School 是两个正交问题。**

Blizzard的≥9 G1节点首先证明：
- ownership exit；
- alumni network；
- entrepreneurial recombination。

它不能单独证明：
- small-team authorial production；
- low-burn experimentation；
- capability-shaped projects；
- direct-player market logic。

同理，腾讯出现莉莉丝、游戏科学等高质量spinout，不能合并成“腾讯独游生态”。

# 11. 当前最重要的三个结论

## 11.1 `SPINOUT DENSITY ≠ INFLUENCE DENSITY`

Looking Glass / Valve提示：
- 设计影响可以极大；
- 但direct founder count未必高。

因此“创新扩散”至少有：
- ownership reproduction；
- employment diffusion；
- community professionalization；
- idea diffusion
四条不同路径。

## 11.2 `SERIAL FOUNDER INTENSITY ≠ BROAD CREATOR CLASS`

id / Romero类型提示：
- 同一批极强个人反复开公司，
可以制造很多“公司节点”。

但真正Creator Class更关心：
> **有多少不同的人从employee变owner。**

所以正式比较必须同时报：
- studio nodes；
- unique alumni founders。

## 11.3 中国当前真正可能发生结构变化的是`OWNER CONVERSION WAVE`

腾讯2013–14：
- Lilith
- Game Science

已经证明一轮。

2025–26又出现：
- NExT alumni创业；
- NetEase senior producer集中创业；
- miHoYo第一代核心/技术人员外溢；
- 老制作人转publisher/incubator/capital allocator。

因此现在不能再用2015年的“中国大厂人只会跳槽”静态描述2026。

更准确的研究问题变成：

> **这波owner conversion能否ship、活三年、做第二作，并在2030前产生自己的spinout？**

---

# 12. 下一步：真正计算率之前必须补三类分母

## P0 — Senior Alumni Denominator
对每家公司建立：
- director / lead / principal / senior producer历史名单；
- 离职人数；
- 可观察职业去向。

可能来源：
- credits database；
- LinkedIn/公开简历；
- MobyGames；
-公司开发者档案；
-工商创始人履历。

## P0 — Unique Founder De-duplication
同一人反复创业：
- 算1个unique founder；
- 多个organizational nodes。

否则Romero / Jeff Strain会把“阶层厚度”虚增。

## P0 — Outcome Cohort
每个spinout按成立年份做：
- ship within 5y；
- second title within 10y；
- survive 3y / 5y / 10y；
- acquired / closed；
- second-generation founder count。

只有这样才能把：
`startup formation`
和
`creator-class reproduction`
分开。

---

# 13.1 下一版必须新增两组分母

025原本只准备补：

```text
Spinout Conversion
= founder outcomes / senior-alumni cohort
```

026之后必须再增加：

### `AUTHORIAL-DIVERGENCE RATE`
creator-owned spinout中，有多少真正脱离母公司的objective function？

### `INDIE-MODE CONVERSION RATE`
senior-alumni founder中，有多少进入：
- bounded small-core；
- low fixed burn；
- hands-on creator density；
- capability-shaped project；
- direct player truth；
- governance optionality

的independent-production route？

这样才可能出现真正有意义的对比：

```text
Company A:
high spinout
low indie conversion

Company B:
lower spinout
high indie conversion among exits
```

前者是强创业学校；
后者可能是强作者转换学校。

二者都值得研究，但不是同一种生态。

# 13. 当前最小结论

> **第一版硬账已经足以否定两种偷懒叙述：第一，不能把“某公司思想影响很大”直接当成“它很会生创业公司”；第二，也不能因为中国存在莉莉丝、游戏科学等明星spinout，就默认数量级已经与Blizzard式alumni ecology相当。当前最显著的对照是：Blizzard拥有大量跨二十余年的直接alumni studio节点和多代serial/recombination谱系；Tencent已经明确产生多条高质量G1 spinout，但分母与G2深度仍缺；NetEase和miHoYo则在2025–26出现新的owner-conversion波。下一阶段应从“列公司”转为构建senior-alumni denominator和cohort outcome，从而第一次真正计算Mobility-to-Ownership与Spinout Conversion。**
