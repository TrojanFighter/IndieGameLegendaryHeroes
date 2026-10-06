# CASE-054 Evidence Ledger — Josh Parnell / Limit Theory

- Last verified: 2026-10-07
- Status: ACTIVE
- Case: [CASE-054](../cases/CASE-054-limit-theory-fit-trap.md)

## E001 — Kickstarter campaign

- Source class: P0 — contemporaneous crowdfunding campaign.
- Title: Limit Theory: An Infinite, Procedural Space Game.
- Author / Institution: Josh Parnell / Kickstarter.
- Published: 2012-11-20.
- Accessed: 2026-10-07.
- URL: https://www.kickstarter.com/projects/joshparnell/limit-theory-an-infinite-procedural-space-game/description
- Claim use: campaign framing as RPG + RTS + sandbox space exploration in an infinite procedural universe; $50,000 goal; $187,865 pledged by 5,449 backers; establishes capital and initial product-obligation surface.
- Confidence: VERY HIGH.
- Boundary: pledged gross is not net development budget; stretch-goal / delivery details require separate capture.

## E002 — 2012 direct creator interview

- Source class: P0 — contemporaneous direct interview during Kickstarter.
- Title: Limit Theory Q&A: Limitless Procedural Good Timiness.
- Author / Institution: Brian Rubin / Space Game Junkie, interviewing Josh Parnell.
- Published: 2012-11-26.
- Accessed: 2026-10-07.
- URL: https://www.spacegamejunkie.com/featured/limit-theory-qa-limitless-procedural-good-timiness/
- Claim use: creator describes target as combining Freelancer accessibility, X3 depth/dynamism and Elite procedurality; useful for original design thesis before later development drift.
- Confidence: HIGH.
- Boundary: promotional Kickstarter-period interview; ambition statements are not feasibility evidence.

## E003 — Official FAQ: custom-engine rationale

- Source class: P0 — creator / project official FAQ.
- Title: Limit Theory — FAQ.
- Author / Institution: Limit Theory / Josh Parnell.
- Published: UNKNOWN.
- Accessed: 2026-10-07.
- URL: https://ltheory.com/faq.html
- Claim use: states a custom C/Lua/OpenGL engine was written from scratch; rationale includes intimate control for procedural generation and explicit enthusiasm for game-engine / graphics-engine design; also describes Lua-heavy moddability.
- Confidence: VERY HIGH.
- Boundary: current archived/live FAQ reflects later-generation stack, not necessarily the exact 2012 architecture; enthusiasm supports capability-attraction hypothesis but does not prove any specific engine task was wasteful.

## E004 — March 2014 development update

- Source class: P0 — contemporaneous creator development update.
- Title: Development Update #15: March 2014.
- Author / Institution: Josh Parnell / Kickstarter.
- Published: 2014-04-03.
- Accessed: 2026-10-07.
- URL: https://www.kickstarter.com/projects/joshparnell/limit-theory-an-infinite-procedural-space-game/posts/798579
- Claim use: records real order-based market/economy, macro AI, NPC job selection, NPC project-management and operational-strategy systems; documents simulation obligation expanding in active development.
- Confidence: VERY HIGH.
- Boundary: feature depth may be part of original thesis; evidence does not by itself classify it as harmful feature creep.

## E005 — Official source repositories: two technology generations

- Source class: P0 — creator-released source repositories.
- Title: Limit Theory Old / Limit Theory.
- Author / Institution: Josh Parnell / GitHub.
- Published: UNKNOWN.
- Accessed: 2026-10-07.
- URL: https://github.com/JoshParnell/ltheory-old
- Claim use: old repository explicitly identifies 2012–2015 C++ implementation containing Limit Theory Engine and Limit Theory Scripting Language; current repository identifies itself as second-generation game code after migration to C and Lua.
- Confidence: VERY HIGH.
- Boundary: repositories prove generation migration and architecture, not that migration was a bad decision; detailed causes require devlog evidence.

## E006 — Official project news timeline

- Source class: P0 — official project news archive.
- Title: Limit Theory — News.
- Author / Institution: Limit Theory / Josh Parnell and project team.
- Published: UNKNOWN.
- Accessed: 2026-10-07.
- URL: https://ltheory.com/news.html
- Claim use: Feb 2017 says severe performance roadblocks took roughly two years to acquire enough knowledge to begin fixing; July 2017 adds Adam and Sean programmers; Nov 2017 adds Lindsey programmer/artist; Jan 2018 PAX demo simulates 2000+ ships/projectiles/full AI and says engine work paid off, while content implementation and then gameplay are still described as next.
- Confidence: VERY HIGH.
- Boundary: official progress reporting has promotional incentives; contributor employment/compensation remains unverified.

## E007 — Cancellation update

- Source class: P0 — creator-authored final project update.
- Title: The End.
- Author / Institution: Josh Parnell / Kickstarter.
- Published: 2018-09-28.
- Accessed: 2026-10-07.
- URL: https://www.kickstarter.com/projects/joshparnell/limit-theory-an-infinite-procedural-space-game/posts/2270873
- Claim use: after six years Josh reports spending beyond initial investment and most personal savings, exhaustion, repeated underestimation of work, project frighteningly far from feature completion, source not a working game with large half-refactored/half-complete areas, and engine substantially more solid than Lua game code.
- Confidence: VERY HIGH.
- Boundary: emotionally extreme cancellation moment; use as direct factual/accounting testimony but do not reduce failure to mental health or infer that every technical investment was unnecessary.

## E008 — Professional background / capability prior

- Source class: P1 — creator-maintained professional profile.
- Title: Josh Parnell — professional profile.
- Author / Institution: Josh Parnell / LinkedIn.
- Published: UNKNOWN.
- Accessed: 2026-10-07.
- URL: https://www.linkedin.com/in/joshparnell
- Claim use: identifies real-time rendering / engine programming specialization; Stanford 2010–2013 CS with computer-graphics concentration; left after Limit Theory Kickstarter funding; supports pre-existing engineering-capability classification.
- Confidence: HIGH.
- Boundary: current retrospective career profile; use contemporaneous sources for project-state claims.

## Current evidence-level conclusions

### STRONGLY SUPPORTED
- Limit Theory was an extremely broad RPG/RTS/sandbox procedural-space thesis before production matured.
- Josh entered with unusually strong graphics / engine capability.
- custom technology was a deliberate choice and engine/graphics design was itself an explicit interest.
- the project accumulated custom engine, scripting, procedural, economy, AI, UI and performance infrastructure.
- development moved across at least two major implementation generations.
- performance problems consumed a very long period; late 2017/2018 engine work achieved impressive local results.
- in January 2018 content implementation / gameplay closure was still framed as next despite engine success.
- in September 2018 the project was still far from feature completion and the engine was materially more mature than the game code.

### SUPPORTED WITH BOUNDARY
- Limit Theory is a strong FIT-TRAP sample: engineering capability created real local value while also furnishing an effectively unbounded investment surface whose maturity diverged from shippable-game maturity.
- the project is better interpreted as multi-causal `FIT-TRAP + overscope + long-cycle solo concentration + rewrite/performance debt + human-cost exhaustion` than as a single-cause engine mistake.

### UNKNOWN / DO NOT INFER
- every engine rewrite was unnecessary;
- commercial engine use would have saved the project;
- exact allocation of development time between engine/tooling/gameplay/content;
- exact annual burn / salaries;
- complete contributor employment status;
- exact causal share of technical perfectionism versus original oversized scope;
- whether Kickstarter overfunding materially expanded promised scope;
- whether community praise for technical demos reinforced engineering overinvestment.
