# Evidence Ledger — CASE-026 Brigador / Stellar Jockeys

- Case: `CASE-026`
- Status: ACTIVE
- Last updated: 2026-10-07

本文件记录 Brigador 作为 failure comparator 的来源、支持边界与禁止推论。

## E001 — GDC 2017: `All Systems No: Learning from the Doomed Launch of 'Brigador'`

- Class: P1 — creator postmortem / official conference archive
- Source: Hugh Monahan / Stellar Jockeys, GDC 2017
- URL: https://www.gdcvault.com/play/1023947/All-Systems-No-Learning-from

GDC 官方 overview 明确记录：
- Brigador 于 2016-06-02 正式发售；
- despite two years of touring at conventions and enthusiastic coverage from PC Gamer, Kill Screen, RPS and others，launch 仍几乎没有形成市场反应；
- Steam 当时约 95% positive，媒体评分最高约 90/100；
- Monahan 从 marketing 与 design 两方面复盘；
- session takeaway 明确写作 `good intentions can make for bad decisions` 与 `audience expectations are everything`。

Supports:
- C009 / TC-002: 商业失败不能只归因于执行质量差；选择与 expectation management 可独立失败。
- C010: 有 market activity / press coverage 不等于有效 demand conversion。
- TC-001: selection capability 必须拆 domain，而不是赢家总分。

Boundary:
- GDC overview 不给完整销售曲线、预算和具体每项失误的定量权重。

## E002 — GDC / Game Developer follow-up: launch characterized as failure despite positive reception

- Class: S1/P1 — professional media summarizing creator GDC session
- Source: Game Developer, `Video: Learning from the doomed launch of Brigador`, 2019-06-20
- URL: https://www.gamedeveloper.com/business/video-learning-from-the-doomed-launch-of-i-brigador-i-

Reported:
- 2016 summer launch was effectively a failure;
- game had convention exposure, positive press, and strong Steam/Metacritic reception;
- the talk focuses on what went wrong rather than product quality alone.

Supports E001 framing and independently confirms why this case belongs in a failure audit.

## E003 — 2015 Early Access announcement / production boundary

- Class: P0 — contemporaneous developer announcement
- Source: HughSJ / Stellar Jockeys, `State of the Brigador + Early Access Announcement`, 2015-08-12
- URL: https://www.moddb.com/games/brigador/news/state-of-the-brigador-early-access-announcement

Developer states:
- Early Access planned for October 2015;
- PAX Prime / Megabooth presence;
- team was `just 4 of us`;
- development began around 2011;
- custom tooling and mod support were part of the production strategy;
- EA was expected mainly to flesh out content and polish/react to larger audience input, not radically change the game.

Supports:
- long pre-launch production period;
- four-person core at this stage;
- market access was not zero;
- by EA, core design was perceived by the team as largely settled.

Boundary:
- does not establish total production labor; contractors and later collaborators exist outside the four-person core.

## E004 — 2015 Early Access release: five-year framing and content state

- Class: P0 — contemporaneous developer announcement
- Source: Stellar Jockeys, `Brigador is out on Early Access!`, 2015-10-19
- URL: https://www.moddb.com/games/brigador/news/brigador-is-out-on-early-access

Developer states:
- `After 5 years of work` the game entered EA;
- launch build had 6 playable vehicles, 18 weapons, 3 abilities, 9 maps, one enemy faction;
- players were explicitly asked for feedback;
- game sold via Steam / Humble, with developer encouraging direct/Humble purchase because of revenue share.

Supports:
- multi-year sunk cost existed before 1.0;
- team was already monetizing before 2016 full launch;
- 2016 should not be treated as first public exposure.

## E005 — 2016 Steam pricing/cost statement by Hugh Monahan

- Class: P0 — contemporaneous first-person developer statement
- Source: Hugh Monahan (`Boss Tweed`), Steam Community discussion, 2016-02-23
- URL: https://steamcommunity.com/app/274500/discussions/0/405691491102673468/

Developer states:
- five years including engine development;
- much of the period involved full-time 6–7 day weeks / 8+ hours, with a conservative estimate over 10,000 hours per person across four people;
- no Kickstarter and no publisher; project funded out of pocket;
- custom engine chosen to support fully destructible environments/performance goals;
- $20 price defended on product scope and labor sustainability grounds;
- rough developer math: ~25k copies to compensate time at minimum wage ignoring contractors/other expenses; ~50k when including contractors / reasonable living.

Supports:
- extreme opportunity cost and self-financing;
- development cost strongly informed pricing discourse;
- custom technology was a deliberate product/production choice.

Boundary:
- all dollar/unit break-even numbers are creator estimates, not audited financial statements;
- `10,000 hours per person` is rhetorical/rough, not time-sheet evidence;
- never infer total project budget from these figures.

## E006 — Post-launch Steam discussion: product presentation mis-signaled play experience

- Class: P0 — contemporaneous developer diagnosis after launch
- Source: Hugh Monahan (`Boss Tweed`), Steam Community, June 2016
- URL: https://steamcommunity.com/app/274500/discussions/0/351659808479739760/

Developer diagnosis:
- many people dismissed Brigador as a twin-stick shooter;
- people seeking a twin-stick shooter then encountered something much more mechanically dense;
- presentation/trailers did not match the reality / feel of the game;
- Monahan explicitly compared this unfavorably with trailers such as Crypt of the NecroDancer that communicated play feel better.

Supports:
- strong evidence for `market legibility` / audience-expectation mismatch;
- failure was not simply lack of exposure.

Boundary:
- forum observation is qualitative and does not quantify conversion loss.

## E007 — Creator outreach existed; many keys did not convert into coverage

- Class: P0 — contemporaneous developer/community exchange
- Source: Steam Community, 2016-06-09
- URL: https://steamcommunity.com/app/274500/discussions/0/350533172683406237/

Developer/community statements:
- team worked with Evolve PR to send review/promotional copies;
- a large number of recipients did not produce content;
- Hugh was willing to personally contact suggested creators.

Supports:
- `zero marketing` is false;
- outreach execution existed, but access attempts did not guarantee earned coverage.

## E008 — 2017 developer diagnosis: visibility larger than price

- Class: P0 — first-person developer statement
- Source: Steam Community, `Price and low sales`, 2017-01-06
- URL: https://steamcommunity.com/app/274500/discussions/0/142260895144466898/

Developer states:
- price was a friction point, but visibility was by far the larger issue in his analysis;
- if price were the main cause, 50% discounts should have produced much larger spikes;
- TotalBiscuit and Giant Bomb coverage produced noticeable sales spikes;
- team did not directly pay influencers; PR firm outreach and personal demos often produced no content.

Supports:
- do not reduce case to `price too high`;
- visibility/attention concentration materially affected sales;
- creator amplification had measurable qualitative effect.

Boundary:
- does not provide underlying sales data; magnitude of spikes unknown.

## E009 — Controls/onboarding friction in Hugh Monahan talk summary

- Class: S1 — detailed summary of Hugh Monahan's Full Indie 2016 talk
- Source: Réalités Parallèles, `Learning from Brigador’s mistakes`, 2017-04
- URL: https://realites-paralleles.com/2017/04/en-fullindie-brigador-learnings/

Summary reports:
- Brigador used tank-style controls (`W` = vehicle forward rather than screen-up);
- playtesters could take around 30 minutes to become comfortable, but often liked the controls afterward;
- talk treated controls and expectation management as major issues.

Supports:
- important distinction between long-term mastery satisfaction and first-session conversion friction.

Boundary:
- secondary write-up; exact numbers/wording should not outrank Hugh's direct GDC materials if a transcript becomes available.

## E010 — 2017 Up-Armored changes: accessibility/onboarding correction

- Class: S1 with developer-supplied release information
- Source: PC Gamer, 2017-06-03
- URL: https://www.pcgamer.com/brigador-gets-new-campaign-music-and-discounts-with-the-free-up-armored-edition/

Reported changes:
- new default control schemes intended to improve newcomer accessibility;
- new campaign designed to ease players into mechanics/world;
- major balance, lighting/effects changes;
- localization into multiple languages;
- launch discount around the update.

Supports:
- post-launch team explicitly altered onboarding/presentation/access rather than only adding more core content;
- failure generated a concrete learning loop.

## E011 — Official long-term localization retrospective

- Class: P0/P1 — team production retrospective
- Source: Stellar Jockeys / Steam news, `How We Localized Brigador`
- URL: https://store.steampowered.com/news/app/274500/view/3452600498056903563

Team retrospective:
- Brigador was not originally built with localization in mind;
- engine/UI required retrofitting;
- 2016→2017 Up-Armored period added German, Russian, Japanese, French, Spanish, Brazilian Portuguese, with more later;
- team concludes localization helped reach audiences the English-only game could not reach.

Supports:
- market access can be expanded post-launch through production work, not only promotion;
- localization was a structural reach correction.

Boundary:
- source does not disclose exact incremental revenue by language.

## E012 — Official 2023/2024 retrospective: prototype evolution and company origin

- Class: P0/P1 — developer retrospective
- Source: Stellar Jockeys Steam news archive
- URL: https://store.steampowered.com/oldnews/?appgroupname=Brigador%3A+Up-Armored+Edition&appids=274500&feed=steam_community_announcements&headlines=0

Official retrospective records:
- origins trace to University of Illinois ACM GameBuilders meetings around 2009;
- Hugh Monahan met Dale Kim and Harry Hsiao there;
- the two engineers later built the custom Brigador engine;
- late 2013/early 2014 prototype concepts differed substantially from final gameplay loop;
- 2016 1.0 was not the endpoint; another year of updates led to the Up-Armored form.

Supports:
- capability/team formation predated formal release by years;
- product definition itself evolved over a long period;
- launch failure occurred after a very long search process, which matters for sunk-cost / feedback-loop analysis.

## E013 — Current Steam store / long-tail survival

- Class: P0 — platform listing
- Source: Steam store
- URL: https://store.steampowered.com/app/274500/Brigador/

Current platform facts:
- thousands of English user reviews with very positive aggregate sentiment;
- product remains commercially available years after launch;
- store now presents the game explicitly as an `isometric roguelite of intense tactical combat`, alongside detailed feature language and mod tools.

Supports:
- cult/long-tail persistence;
- current positioning is more explicit than the launch-era twin-stick misread diagnosed by the developer.

Boundary:
- current review count/sentiment cannot be projected backward to 2016 launch demand.

## E014 — 2015 Hugh Monahan direct interview: prototype selection, capability imprint, engine risk

- Class: P1 — direct creator interview during Early Access period
- Source: Hugh Monahan / 80 Level, `Brigador: Three Space Aiming System and a Unique Engine`
- Published: 2015-11-04
- URL: https://80.lv/articles/brigador-three-space-aiming-system-and-a-unique-engine

Direct creator statements:
- Brigador emerged after roughly seven prototypes;
- an earlier 2D four-player arena direction was abandoned when the team realized they did not actually like that kind of game;
- Hugh and Jack explicitly preferred slower, more deliberate action inspired by titles such as Crusader / MechWarrior;
- programmer Dale Kim's Counter-Strike background fed directly into the requirement that aiming be precise and skillful;
- the custom three-space aiming system took months and multiple reticle prototypes;
- the team simultaneously built a custom engine, a new art pipeline and a new core gameplay mechanic;
- Monahan explicitly says doing all of that on a first commercial team project was not something he would recommend;
- before Brigador, he spent roughly six months in the StarCraft II editor exploring what kinds of game problems he actually wanted to build.

Supports:
- C015: project direction was selected through repeated prototyping, taste rejection and team-specific capability input rather than simple genre imitation;
- C003/C011: the shipped product sits on top of prototype and hobbyist prehistory;
- counterpressure: strong fit did not eliminate production risk or later commercial failure.

Boundary:
- this evidence supports `FIT-STRONG`, not the stronger claim that the team optimally matched all capabilities;
- creator retrospective occurs near launch / EA, but some prototype chronology is still recalled after several years.

## E015 — 2016 Hugh Monahan direct interview: kitbash pipeline, narrative peripheralization, launch failure

- Class: P1 — direct creator interview immediately after 1.0 launch
- Source: Michael Riser interview with Hugh Monahan / Goomba Stomp, `Brigador Interview — Hugh Monahan of Stellar Jockeys`
- Published: 2016-07-25
- URL: https://goombastomp.com/brigador-interview-hugh-monahan/

Direct creator statements:
- Hugh handled most design; Jack handled most art; Harry Hsiao and Dale Kim were programmers;
- Jack's Ma.K.-influenced digital-kitbash process shaped both the game's aesthetic and art production pipeline;
- Monahan says that pipeline is the reason one artist could complete the required asset load, with late-project concept-to-engine turnaround sometimes under a day;
- the game deliberately kept traditional linear narrative out of the main interaction loop and moved more worldbuilding into descriptions plus an externally written novel/audiobook;
- soundtrack and novel work were given to specialist collaborators whose instincts matched the project;
- the team simultaneously took on 3-space aiming, destructibility, a new art pipeline and a custom engine;
- after launch, Monahan says the game still struggled for attention and rejects the naive “build it and they will come” assumption.

Supports:
- C015: `Strength Loading + Cost Conversion + Specialist Periphery` are all directly observable;
- CASE-026 becomes a `FIT-STRONG / LAUNCH-FAILED` counterpressure case;
- C010: market cultivation remained necessary even when product identity and internal production fit were strong.

Boundary:
- “under a day” asset turnaround is a creator-reported late-project peak, not average production time;
- this does not establish audited profitability or exact causal weight of fit versus launch failure variables.

## Current evidence-level conclusions

### STRONGLY SUPPORTED

- Brigador had a long, self-funded, high-opportunity-cost development period with a four-person core at EA.
- The final project direction followed multiple prototypes and explicit rejection of a four-player-arena direction the team did not actually want to make.
- Team-specific capability shaped the product: design/taste, precision aiming, custom technology, digital kitbash art production and specialist narrative/music periphery were tightly coupled to the final game form.
- This strong capability–project fit still coexisted with a commercially failed 2016 launch.
- The 2016 launch was treated by its own creator and GDC as a commercial failure despite strong product reception and substantial pre-launch activity.
- `zero marketing` is false: conventions, press, PR, creator outreach, EA, preorder and later influencer spikes all existed.
- The developer explicitly diagnosed a mismatch between product presentation and actual play experience.
- The developer later regarded visibility as more important than price alone.
- Up-Armored materially changed onboarding/control defaults and international reach.

### SUPPORTED WITH BOUNDARY

- tank controls / onboarding imposed a substantial first-session friction cost;
- production sunk cost likely influenced pricing/valuation judgment;
- localization/relaunch materially improved reach and long-tail viability, though exact incremental revenue is not public here.

### UNKNOWN / DO NOT INFER

- audited total budget;
- exact 2016 launch-week sales;
- exact 2016/2017 unit curve;
- exact break-even date;
- relative causal weights of control friction, store presentation, price, release timing, genre niche, visibility and press/influencer conversion;
- whether a different price alone would have made launch successful;
- whether using a commercial engine would have produced a better business outcome.

## Thesis impact

### TC-001 Taste Capital

Brigador is a counterpressure case against treating taste as a scalar. Strong interaction/aesthetic/technical taste coexisted with weak first-launch onboarding and market-legibility decisions.

### TC-002 Execution Failure vs Selection Failure

Brigador is a strong candidate for **selection-domain failure under strong execution**: the team completed difficult technical/art/product work, but the market interface around the product failed to communicate and convert that value efficiently.

### TC-003 AI-era selection scarcity

No direct support. Brigador predates the current AI-production environment; it may only serve as a historical analogy for why increased execution capacity does not eliminate selection problems.
