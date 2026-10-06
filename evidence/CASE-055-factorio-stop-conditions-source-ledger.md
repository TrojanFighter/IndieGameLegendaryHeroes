# CASE-055 Evidence Ledger — Wube / Factorio

- Last verified: 2026-10-07
- Status: ACTIVE
- Case: [CASE-055](../cases/CASE-055-factorio-stop-conditions.md)

## E001 — Original project announcement

- Source class: P0 — contemporaneous official project blog.
- Title: Here we are.
- Author / Institution: Tomas / Factorio.
- Published: 2012-10-24.
- Accessed: 2026-10-07.
- URL: https://www.factorio.com/blog/post/here-we-are
- Claim use: project began from Michal Kovařík's ideas for a game he wanted to play but could not find; three-person Prague team; early factory / automation thesis already present.
- Confidence: VERY HIGH.
- Boundary: official origin narrative; does not by itself prove later scope discipline.

## E002 — Public demo and early playable loop

- Source class: P0 — contemporaneous official project blog.
- Title: The demo is out.
- Author / Institution: Tomas / Factorio.
- Published: 2012-12-31.
- Accessed: 2026-10-07.
- URL: https://www.factorio.com/blog/post/demo-is-out
- Claim use: public demo plus alpha/freeplay/map editor existed before crowdfunding completion; establishes early playable-product feedback rather than technology-only development.
- Confidence: VERY HIGH.
- Boundary: demo completeness and player population not quantified here.

## E003 — Alpha access becomes market/feedback mechanism

- Source class: P0 — contemporaneous official project blog.
- Title: Getting the Alpha.
- Author / Institution: Tomas / Factorio.
- Published: 2013-02-13.
- Accessed: 2026-10-07.
- URL: https://direct.factorio.com/blog/post/getting-the-alpha
- Claim use: team says immediate alpha access for backers significantly improved crowdfunding prospects and created an active community giving feedback.
- Confidence: VERY HIGH.
- Boundary: creator assessment of campaign effect, not a controlled causal estimate.

## E004 — Founder and team capability background

- Source class: P0 — official team retrospective.
- Title: Friday Facts #300 — Special edition.
- Author / Institution: Factorio Team / Wube.
- Published: 2019-06-21.
- Accessed: 2026-10-07.
- URL: https://www.factorio.com/blog/post/fff-300
- Claim use: Kovařík reports programming since childhood, strong attraction to simulation/optimization, 4.5 years professional programming before Factorio; Kozelek describes informatics/programming background; later developers describe performance/networking/modding specializations; establishes unusually engineering-heavy capability vector.
- Confidence: VERY HIGH.
- Boundary: retrospective self-description; specific early decisions should rely on contemporaneous posts where possible.

## E005 — Multiplayer architecture failure and rewrite

- Source class: P0 — contemporaneous official development log.
- Title: Friday Facts #147 — Multiplayer rewrite.
- Author / Institution: kovarex / Wube.
- Published: 2016-07-15.
- Accessed: 2026-10-07.
- URL: https://www.factorio.com/blog/post/fff-147
- Claim use: team identifies concrete P2P/server hybrid problems, admits earlier architecture had serious complexity/latency tradeoffs, and performs a substantial rewrite to solve real online-play failures.
- Confidence: VERY HIGH.
- Boundary: rewrite cost not fully quantified; does not show every architecture decision was optimal.

## E006 — Multiplayer rewrite delivers large local technical success

- Source class: P0 — contemporaneous official development log.
- Title: Friday Facts #156 — Massive Multiplayer.
- Author / Institution: Tomas / Wube.
- Published: 2016-09-16.
- Accessed: 2026-10-07.
- URL: https://www.factorio.com/blog/post/fff-156
- Claim use: multiplayer rewrite and network optimization are reported to support hundreds of players, far beyond the initial hoped-for ~50.
- Confidence: VERY HIGH.
- Boundary: event/server/network conditions matter; this is a capability-success checkpoint, not an argument that such scale was product-essential.

## E007 — Explicit technical stop condition

- Source class: P0 — contemporaneous official development log.
- Title: Friday Facts #157 — We are able to eat paper, but we don't do it.
- Author / Institution: kovarex / Wube.
- Published: 2016-09-23.
- Accessed: 2026-10-07.
- URL: https://www.factorio.com/blog/post/fff-157
- Claim use: after reaching ~350 players and considering 400/1000, team explicitly asks whether more optimization improves gameplay or is merely an internal race; states Factorio is not an MMO, ~200-player support is enough, and shifts attention to general factory simulation optimizations that benefit single-player as well.
- Confidence: VERY HIGH.
- Boundary: “200 enough” is project-specific, not a universal multiplayer threshold.

## E008 — Feature deletion because value did not justify maintenance cost

- Source class: P0 — contemporaneous official development log.
- Title: Friday Facts #222 — Christmas avalanche.
- Author / Institution: kovarex / Wube.
- Published: 2017-12-22.
- Accessed: 2026-10-07.
- URL: https://www.factorio.com/blog/post/fff-222
- Claim use: team abolishes fluid-wagon tank separation partly because the problem already has a trivial solution and the mechanic would continue to cost code/UI/bug maintenance; explicitly frames development as priorities because everything has a cost.
- Confidence: VERY HIGH.
- Boundary: one mechanic does not prove universal scope discipline.

## E009 — Major-feature wrap-up before 1.0

- Source class: P0 — official release post.
- Title: Factorio version 0.16 — Now stable.
- Author / Institution: Factorio Team / Wube.
- Published: 2018-03-29.
- Accessed: 2026-10-07.
- URL: https://www.factorio.com/blog/post/016-stable
- Claim use: official goal of 0.16 is to wrap up addition of major features and focus on final steps toward 1.0.
- Confidence: VERY HIGH.
- Boundary: actual path to 1.0 remained long; stated goal is not proof of immediate closure.

## E010 — Public deadline as closure governance

- Source class: P0 — contemporaneous official development log.
- Title: Friday Facts #321 — Countdown.
- Author / Institution: kovarex, Klonan / Wube.
- Published: 2019-11-15.
- Accessed: 2026-10-07.
- URL: https://www.factorio.com/blog/post/fff-321
- Claim use: team says “done when it is done” could make Factorio development continue effectively forever; publicly fixes a 1.0 date so work must focus on the most important remaining items.
- Confidence: VERY HIGH.
- Boundary: deadline effectiveness is case-specific and supported here by later shipment, not a universal process rule.

## E011 — 1.0 descoping

- Source class: P0 — contemporaneous official development log.
- Title: Friday Facts #349 — The 1.0 plan.
- Author / Institution: Klonan, Rseding, Boskid / Wube.
- Published: 2020-05-29.
- Accessed: 2026-10-07.
- URL: https://www.factorio.com/blog/post/fff-349
- Claim use: team reports cancellation of the new campaign, postponement of fluid improvements, cuts to GUI rewrite, and states this descoping helps make an earlier release possible; final weeks shift to finalization and marketing.
- Confidence: VERY HIGH.
- Boundary: individual features were cut/postponed for independent reasons; do not claim Cyberpunk directly caused those cuts.

## E012 — Post-1.0 prototype complexity pruning

- Source class: P0 — official expansion development log.
- Title: Friday Facts #387 — Swimming in lava.
- Author / Institution: Factorio Team / Wube.
- Published: 2023-11-10.
- Accessed: 2026-10-07.
- URL: https://www.factorio.com/blog/post/fff-387
- Claim use: Space Age prototype originally contained more intermediate items/mechanics; team removed several because in the full game they only slowed progression or created complexity without enough distinct value.
- Confidence: VERY HIGH.
- Boundary: expansion design context differs from base-game production; use as longitudinal reinforcement, not causal proof of 2012–2020 success.

## E013 — 2026 explicit scope ceiling / end of active gameplay development

- Source class: P0 — current official development plan.
- Title: Friday Facts #440 — 2.1 plan.
- Author / Institution: Klonan / Wube.
- Published: 2026-05-29.
- Accessed: 2026-10-07.
- URL: https://www.factorio.com/blog/post/fff-440
- Claim use: Wube states 2.1 has no new planets, enemies, research trees or resource chains, is primarily QoL/fixes/polish/modding improvements, and is envisioned as the last major update before long-term support.
- Confidence: VERY HIGH.
- Boundary: future plans can change; as of access date this is official intent, not completed future history.

## E014 — Official development timeline / team origin

- Source class: P0 — official press kit.
- Title: Factorio Press Kit.
- Author / Institution: Wube Software.
- Published: UNKNOWN.
- Accessed: 2026-10-07.
- URL: https://www.factorio.com/press-kit
- Claim use: development began May 2012; successful crowdfunding February 2013; Wube founded September 2014; Steam February 2016; 1.0 August 2020; original core described as a tiny programmer-led garage company.
- Confidence: VERY HIGH.
- Boundary: current retrospective summary; contemporaneous posts take precedence for disputed dates/details.

## Current evidence-level conclusions

### STRONGLY SUPPORTED
- Factorio emerged from a programmer-heavy founding core and a systems/automation product thesis.
- Wube repeatedly invested in deep engine/simulation/network/performance work rather than avoiding technical complexity.
- multiplayer rewrite produced technical capability far beyond initial scale expectations.
- the team then explicitly stopped chasing further multiplayer scale because it no longer matched the product goal.
- Wube has removed implemented mechanics when unique player value did not justify ongoing code/UI/bug cost.
- the team publicly recognized that unlimited polishing could prevent closure and imposed a 1.0 deadline.
- 1.0 was enabled partly by explicit cancellation/postponement/cutting of major work.
- similar complexity-pruning language persisted in Space Age and the 2026 2.1 plan.

### SUPPORTED WITH BOUNDARY
- Factorio is a strong success-side counterpoint to Limit Theory for the narrower mechanism “technical capability + product-facing stop conditions.”
- the relevant distinction is not custom technology vs commercial engine, but whether technical progress closes core player/product obligations and whether teams can declare “enough.”
- early playable/paid-alpha feedback plausibly constrained technical work toward an existing product, but it cannot be treated as a sufficient cause of success.

### UNKNOWN / DO NOT INFER
- exact counterfactual outcome if Wube had used a commercial engine;
- exact person-hours saved by any individual optimization or cut feature;
- whether every major technical investment had positive ROI;
- whether public deadlines would work equally well for other teams;
- whether Factorio's unusually patient paying community is reproducible;
- exact ownership/equity structure of Wube across the full period;
- whether all later scope discipline came from one consistent formal internal process.
