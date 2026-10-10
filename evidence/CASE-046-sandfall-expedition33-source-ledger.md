# CASE-046 Evidence Ledger — Sandfall / Clair Obscur: Expedition 33

- Last verified: 2026-10-07
- Status: ACTIVE
- Case: [CASE-046](../cases/CASE-046-sandfall-expedition33.md)

## E001 — 2021 Project W direct interview
- Source class: P0/P1 — early-development direct founder interview.
- Title: Pitch & Produce | PROJECT W: Sandfall Interactive Studios Develops Ambitious RPG Game with Real-time Tools.
- Author / Institution: Reallusion Magazine; interviewee Guillaume Broche.
- Published: 2021-06-09.
- Accessed: 2026-10-07.
- URL: https://magazine.reallusion.com/2021/06/09/pitch-produce-project-w-sandfall-interactive-studios-develops-ambitious-rpg-game-with-real-time-tools/
- Claim use: Ubisoft 4+ years, co-founding with another Ubisoft dev, team of 8 planning 15, loss of AAA specialization, creator personally covering character work, use of Character Creator/ActorCore/Rokoko.
- Confidence: VERY HIGH.
- Boundary: vendor feature story; direct quotes are useful but tool benefits are presented in promotional context.

## E002 — Unreal 2025 production interview
- Source class: P0/P1 — direct technical interview.
- Title: Inside the development journey of Clair Obscur: Expedition 33.
- Author / Institution: Epic Games / Unreal Engine; interviewee Tom Guillermin.
- Published: 2025-03-27.
- Accessed: 2026-10-07.
- URL: https://www.unrealengine.com/developer-interviews/inside-the-development-journey-of-clair-obscur-expedition-33
- Claim use: core team <30, 25 Montpellier + 5 Paris, five-year development window, early combat prototypes, UE5 feature leverage.
- Confidence: VERY HIGH.
- Boundary: engine-vendor interview; claims about Unreal benefits have promotional incentive.

## E003 — Unreal 2025 post-success workflow interview
- Source class: P0/P1 — direct technical interview.
- Title: Clair Obscur: Expedition 33: autonomy, creativity, and community key to Sandfall Interactive’s success.
- Author / Institution: Epic Games / Unreal Engine; interviewee Tom Guillermin.
- Published: 2025-12-02.
- Accessed: 2026-10-07.
- URL: https://www.unrealengine.com/developer-interviews/clair-obscur-expedition-33-autonomy-creativity-and-community-key-to-sandfall-interactives-success
- Claim use: Blueprint cross-discipline autonomy, Sequencer coordination, 3–5 environment artists, World Partition / Nanite as labor-saving workflow.
- Confidence: HIGH.
- Boundary: retrospective success framing and vendor incentives.

## E004 — Sandfall official studio page
- Source class: P0 — official studio statement.
- Title: Sandfall Interactive.
- Author / Institution: Sandfall Interactive.
- Published: UNKNOWN (dynamic).
- Accessed: 2026-10-07.
- URL: https://www.sandfall.co/
- Claim use: founded 2020; small-team pipeline thesis; Kepler listed as publisher.
- Confidence: HIGH.
- Boundary: current corporate self-description.

## E005 — Sandfall official team page
- Source class: P0 — official current team roster.
- Title: Team | Sandfall Interactive.
- Author / Institution: Sandfall Interactive.
- Published: UNKNOWN (dynamic).
- Accessed: 2026-10-07.
- URL: https://www.sandfall.co/team
- Claim use: current internal role structure and named disciplines.
- Confidence: HIGH.
- Boundary: current roster does not equal historical peak or all contributors.

## E006 — MobyGames credits
- Source class: S1 — structured shipped-game credits transcription.
- Title: Clair Obscur: Expedition 33 credits (Windows, 2025).
- Author / Institution: MobyGames.
- Published: UNKNOWN (2025 shipped-game credits).
- Accessed: 2026-10-07.
- URL: https://www.mobygames.com/game/241065/clair-obscur-expedition-33/credits/windows/
- Claim use: ~438 people / 429 professional roles / 530 credits; demonstrates broad external production perimeter including voice, performance, production partners and testing.
- Confidence: MEDIUM-HIGH.
- Boundary: credit count != full-time headcount or person-months; deduplication and exact employer mapping require deeper audit.

## E007 — Kepler official product page
- Source class: P0 — publisher product page.
- Title: Clair Obscur: Expedition 33.
- Author / Institution: Kepler Interactive.
- Published: UNKNOWN (dynamic).
- Accessed: 2026-10-07.
- URL: https://www.kepler-interactive.com/games/clair-obscur-expedition-33
- Claim use: confirms Sandfall as developer and Kepler publisher.
- Confidence: HIGH.
- Boundary: does not disclose financing / ownership / recoup terms.

## E008 — Sandfall official release chronology
- Source class: P0 — official studio post.
- Title: Clair Obscur: Expedition 33 was released on April 24, 2025.
- Author / Institution: Sandfall Interactive.
- Published: 2025-06-11.
- Accessed: 2026-10-07.
- URL: https://www.sandfall.co/post/clair-obscur-expedition-33-was-released-on-april-24-2025
- Claim use: confirms 2025-04-24 release and >5-year development framing.
- Confidence: HIGH.
- Boundary: post-success studio narrative.

## Fetch status — re-read attempt 2026-10-09

Attempted to re-read the primary sources. Results:

- `unrealengine.com` (E002, E003): **403** to direct fetch; the archive.org copy returns a JavaScript shell — 249KB of markup containing 6 paragraphs of text, no interview body. Not recoverable this way.
- `magazine.reallusion.com` (E001): **403** direct; archive.org returned **429** at the time of the attempt.
- `sandfall.co` (E004, E005, E008): reachable, but renders client-side (614KB of markup, 7 paragraphs of text).
- `mobygames.com` (E006) and `kepler-interactive.com` (E007): not attempted; both are structured listings rather than narrative sources.

Consequence: **E001–E003 carry the narrative and none of them could be re-read.** Their summaries therefore remain unverified against their originals, and this Case could not be enriched by the method that worked for CASE-004, CASE-015, CASE-017, CASE-041 and CASE-044. This is a source-access failure, not a finding that the Case is thin on purpose.

What would work instead:

- a browser-captured archive copy (the pages need JavaScript to render);
- a print or syndicated reprint of the Epic/Unreal interviews;
- a Chinese- or French-language interview with the developers that quotes them directly;
- and, for E001, the Reallusion page retried at some later time, since only rate-limiting blocked it.
