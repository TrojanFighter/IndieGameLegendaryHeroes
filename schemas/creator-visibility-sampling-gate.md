# Creator Visibility / Sampling Gate — 不把著名开发者当总体样本

- Status: RESEARCH METHODOLOGY / COMPARISON GATE
- Last verified: 2026-10-07
- Primary research: [media-selection-survivorship-and-denominator-protocol-028.md](../book/research-notes/media-selection-survivorship-and-denominator-protocol-028.md)
- Applies to: *every* cohort-level education / company / country / outcome / indie career-rate inference.

## 0. Separate two research modes

### Mechanism / biography mode (existing Case corpus)

Can answer: **What happened to this person? Under what constraints? What decision produced what observable downstream change?**

Can use reported founders, GDC talks, postmortems, interviews, success and failure. Requires dated facts and rival explanations.

**Cannot** answer: rates, distributions, representative typicality, country-level comparisons, employee exit probability, share retaining independent authorship.

### Population / cohort mode (new requirement)

Can only answer relative frequency when a population, sampling frame, inclusion window, missingness, outcome definitions and coverage are explicit.

A celebrity archive is not a probability sample. Mixing more failures into that archive does not turn it into one.

## 1. Before a comparative claim, fill this sample declaration

```yaml
question: "The comparative claim being tested"
target_population: "People/projects the statement is supposed to describe"
unit_of_analysis: "person | project | studio"
cohort_entry_event: "e.g. hired in 2017, entered jam 2019, Kickstarter campaign launched 2020"
geography_and_year_window: "explicit start and stop"
sampling_frame: "how EVERY eligible person/project could be enumerated"
inclusion_exclusion_rules: "pre-registered, not adapted to famous outcomes"
denominator_status: "KNOWN | PARTIAL | UNKNOWN"
denominator_count: "integer or UNKNOWN"
visible_entries: "integer or UNKNOWN"
visibility_reasons: "media | press | public project | school record | employer roster | other"
missingness: "unobserved employment | private project | lost archives | language | censorship | self-selection | etc."
outcome_definitions: "no public work / private unknown / public prototype / abandoned / shipped / revenue unknown / successful"
followup_window_and_censoring: "when we stop observing an attempt"
rival_explanations: "job role | prior taste | runway | tools | publication constraints | audience selection"
permitted_inference: "what exactly this frame can justify"
forbidden_inference: "what it cannot tell us"
```

If `denominator_status=UNKNOWN`: **no frequencies, probability, majority/minority, 'more often than other country', or confidence based on Case count**.

Do not turn `NO PUBLIC ARTIFACT OBSERVED` into `NO AUTHORSHIP`.

## 2. Source visibility tiers (descriptive, not quality ranking)

- `MEDIA_FEATURED`: GDC/postmortem, press interviews, platform promotion, widely reported case.
- `PUBLIC_UNFEATURED`: public itch/jam/Steam/KS/forum trace without meaningful biographical press.
- `INSTITUTIONAL_FRAME`: roster, archived cohort, structured public entrant register.
- `PRIVATE/UNKNOWN`: potential population members with no trace available for ethical public research.

Visibility tiers affect *who got into our source set*, not which participant is creatively better.

## 3. Why a famous failure isn't automatically a counterfactual

An excellent and publicized commercial failure (CASE-048 The Magic Circle; CASE-054 Limit Theory) can falsify a claim like “author ownership guarantees success”.

It **cannot** estimate how common failures are in the source industry. Nor does a visible failure have the same probability of interview as an unlaunched project.

A real denominator requires failures *and* all other eligible attempts under the same observation rule.

## 4. What counts as a usable first pilot

A useful pilot can be very small, but:
1. pick **one** platform/event/time slice before examining winners;
2. enumerate **all eligible entries** or document exactly why enumeration failed;
3. use uniform attempts to identify public project traces and career history;
4. record no-trace / employment-unobserved and attrition honestly;
5. only then choose a few **mechanism** cases, including public but unfeatured projects;
6. report limits. If career histories mostly unknown, the pilot does not support ex-big-company conclusions.

Example of a feasible frame: public game jam roster including all submitted games for one dated jam. This can study later public-shipping trails among roster entries, **not** whether most Tencent/Amazon employees retain authorial identity.

## 5. Writing / lint boundary

This is an **editorial and study-design gate**, not automatic fill-in: machine metadata remains canonical for cases/claims, and no personal facts may be fabricated to satisfy a ratio.

Any reader chapter claiming a social-level comparative result must link a filled sampling declaration or state explicitly:
> “The archive is a purposive set of publicly discoverable cases, not a population sample; no prevalence estimate is possible.”

Related foundational methodological references:
- Widner (2022), *Descriptive Accuracy in Interview-Based Case Studies*: https://www.cambridge.org/core/books/case-for-case-studies/descriptive-accuracy-in-interviewbased-case-studies/5A2722EFDEF1F485BD28EE1FE47543E7
- *The BMJ* (2023), collider selection: https://www.bmj.com/content/381/bmj.p1135
- GDC State of the Game Industry (2026), respondent survey not employee population denominator: https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/
