# CASE-044 Evidence Ledger — Garry Newman / Garry's Mod → Rust → s&box

- Last verified: 2026-10-07
- Status: ACTIVE
- Case: [CASE-044](../cases/CASE-044-garry-newman-sbox.md)

## E001 — PC Gamer 15-year Garry's Mod direct interview
- Source class: P1/S1 — direct interview with Garry Newman and Valve's Erik Johnson.
- Title: How a 'total accident' led to Garry's Mod's funniest feature and 15 years of twisted success.
- Author / Institution: Christopher Livingston / PC Gamer.
- Published: 2019-12-24.
- Accessed: 2026-10-07.
- URL: https://www.pcgamer.com/garrys-mod-interview/
- Claim use: free-mod origin, Valve commercial approach, paid version as development incentive, Steam update infrastructure, community feedback competence, GMod longevity.
- Confidence: HIGH.
- Boundary: retrospective 15 years later; sales numbers are creator-reported.

Direct quotes (verbatim, page re-read 2026-10-09):

Origin of the name:
- "You know, I think I kind of actually stole the name, it wasn't my idea to name stuff after myself. At the time there was another mod called JBMod, made by a guy that went by 'jb55.' So it made sense that my take on that mod would be called Garry's Mod—because I went by the name 'garry'. I probably wouldn't have named it called Garry's Mod if I knew where it would end up."

Scale, as stated by the creator:
- "It sells about 1.5m copies a year, and it's sold just over 15m copies total. Which is kind of pleasing since it's also 15 years old. Plus you know, money."

The paid version, and why it mattered:
- "It was about a year before we started selling it. I was emailing [Valve] to ask about something else and they mentioned that they think it'd sell well. I was like, yeah right, what a dumb idea, it's already free—why would anyone pay for it?"
- "I don't think I ever contemplated charging more. It was free and now it's not, the price had to be low enough to people that they'd just be like... yeah sure why not. It's important to remember that before Steam pretty much no-one bought games on the PC. Everything was pirated."
- "I think Garry's Mod would have died 15 years ago if we didn't sell it. It gave us a reason to continue development. Besides that Steam obviously allowed us to update the game much easier."

Announcing Steam, and how small Steam was then:
- "I can't remember much of it—it was actually one of the most embarrassing things that has ever happened to me. We'd been working on it in secret for a few months and the community were getting quite worried. They had got used to weekly updates before that. So we decided to announce that we were going to be on Steam and everything was going to be okay. This wasn't like announcing that you're gonna be on Steam nowadays, this was when there were about 3 games on Steam."

Accidental feature origin (ragdoll posing):
- "A total accident. I was trying to pose ragdolls, but not by freezing their joints. I was trying to make it so they would move like the atmosphere was really thick, so they'd stay in place. … I used the wrong values and it locked one of their bones in place. I made a quick pose—I think it was Kleiner giving birth. I was really excited—I immediately knew the fun everyone was going to have with this."

Valve's side (Erik Johnson):
- "It was the early days of getting Steam built, and it was pretty clear that Garry's Mod had a big (and growing) audience. Our philosophy back then was the same as it is today, which is that we wanted a platform that connected the people who created valuable content with the people that consumed it."
- "We've always been impressed by Garry's ability to iterate on the game and roll feedback from his community into the game so well. It's a more difficult process than it sounds."

Handing the game over; declining to pre-announce:
- "I haven't personally worked on it for about three years. Rubat and Willox have done a really good job of taking it off my plate. I found that it got to a place where anything I tried to change I got yelled at by the community for breaking something else."
- "There's actually a ton of things I want to do, but I don't like to talk about it too much. If you talk about stuff you want to do you don't end up doing it, because you feel like you already did it. You get all the positive feedback from it."

s&box state as of 2019 (the 2026 release is E003–E007):
- "We did a lot of experimentation with s&box on UE4. It's actually quite far along but we decided to pause it for now. We're hoping you'll hear more about it next year—if not it's probably dead forever."

Valve rejected him as an applicant:
- "Yeah I applied for a job, I think it was before Garry's Mod went on sale. Or might have been just after. … I had a phone interview and I don't think it took them long to realise that I didn't know shit. I didn't get offered a position. In retrospect it's a good thing."

Boundary additions:
- These are 15-year retrospective statements; sales figures are creator-stated and not audited.
- "Would have died 15 years ago if we didn't sell it" is a counterfactual, not an observed outcome.
- The post-2019 s&box pause prediction did not hold: the project shipped in 2026 (E003), so the 2019 remark is a dated forecast.

## E002 — Rust direct interview
- Source class: P1/S1 — direct creator interview.
- Title: Garry Newman interview: on Rust and player freedom.
- Author / Institution: PC Gamer.
- Published: 2013-12-13.
- Accessed: 2026-10-07.
- URL: https://www.pcgamer.com/rust-interview/
- Claim use: confirms Facepunch's explicit DayZ inspiration and transition from GMod lineage into survival multiplayer.
- Confidence: HIGH.
- Boundary: design-origin testimony, not complete production history.

Direct quotes (verbatim, page re-read 2026-10-09):

Design origin (DayZ → player-created world):
- "We love DayZ and we wanted to make a game like it. So we did. We quickly realized that we couldn't create an explorable world as well done as DayZ so we came up with the idea of having the player create the world. This was the seed that spawned Rust. We really loved the idea of players starting with nothing, and having no goals but to exist in the world."

Refusing a morality system:
- "So one thing that was suggested was making 'bandits'. Making people turn evil, get a negative score if they attack other players. We hate that. People should be nice to each other because they get a nice feeling from being nice. There shouldn't be a system hanging around forcing people to be good. It removes a lot of gameplay fun."

Stated method:
- "To be totally honest we haven't played any of the others. With Rust we're making the game we want to play. We're being ruthless with the development, being careful to test each theory instead of just dismissing it as a bad idea."

Two player-behaviour anecdotes:
- "During early development we accidentally left a small white static cube out miles away from anywhere. There was a French server we joined and they'd built a huge shrine around it in a big circle, like a crop circle."
- "It's a weird thing. When any player can kill you easily - and they don't, it's like the biggest compliment ever. They become good friends. You go to bed, and lie there and think to yourself 'that was a nice guy, I hope I run into him again.'"

Boundary addition:
- 2013 Early Access-period interview: ambition and design rationale are creator testimony, not a record of what shipped.

## E003 — s&box Release
- Source class: P0 — contemporaneous official developer log.
- Title: Release.
- Author / Institution: Garry Newman / s&box.
- Published: 2026-04-28.
- Accessed: 2026-10-07.
- URL: https://sbox.game/news/release-26-04-28/
- Claim use: multiple years / false starts / engines; explicit refusal to make merely Garry's Mod on Source 2; acknowledges discovery/AI challenges at v1.
- Confidence: VERY HIGH.
- Boundary: creator framing of its own development.

## E004 — s&box Post Release
- Source class: P0 — contemporaneous official postmortem.
- Title: Post Release.
- Author / Institution: Garry Newman, Matt / s&box.
- Published: 2026-04-29.
- Accessed: 2026-10-07.
- URL: https://sbox.game/news/post-release/9qtcxbc94hvf.jsp
- Claim use: month-profit statement, mixed-review state, unexpected backend stress, AI slop/performance/"This Isn't Garry's Mod" complaints, no-frontpage-push strategy.
- Confidence: VERY HIGH.
- Boundary: day-one state; not final commercial verdict.

## E005 — Review/discovery update
- Source class: P0 — official developer log.
- Title: Update 26.05.13.
- Author / Institution: Garry Newman et al. / s&box.
- Published: 2026-05-13.
- Accessed: 2026-10-07.
- URL: https://sbox.game/news/update-26-05-13
- Claim use: review tags feeding discovery, AI-thumbnail discouragement, reported complaint shares, performance work.
- Confidence: HIGH.
- Boundary: internal telemetry is developer-reported; categories may evolve.

## E006 — Welcome-screen / positioning correction
- Source class: P0 — official developer log.
- Title: Update 26.05.20.
- Author / Institution: s&box.
- Published: 2026-05-20.
- Accessed: 2026-10-07.
- URL: https://sbox.game/news/update-26-05-20
- Claim use: Newman states the team explained itself better to developers than gamers and adds onboarding to clarify product identity.
- Confidence: VERY HIGH.
- Boundary: intervention intent; downstream effect still to measure.

## E007 — Discovery redesign
- Source class: P0 — official developer log.
- Title: Update 26.09.01.
- Author / Institution: s&box.
- Published: 2026-09-01.
- Accessed: 2026-10-07.
- URL: https://sbox.game/news/update-26-09-01
- Claim use: old discovery surfaced same 31 games / ~1.2% coverage; redesigned personalized discovery reported ~70% coverage.
- Confidence: HIGH.
- Boundary: internal metrics and current-state architecture; future efficacy unknown.
