# Contributing and submitting changes

[中文原文](../../CONTRIBUTING.md) · [English entry](README.md)

> DRAFT translation; no human translation approval is recorded. English may lag behind the Chinese source. Check the [registry](../manifest.json) and linked source before relying on it.

This repository studies the production conditions of developers and small teams. Prioritize factual corrections, sources, timelines, counterexamples and evidence pointers. Follow the evidence hierarchy and limits on extrapolation in [AGENTS.md](../../AGENTS.md).

## Start work

1. Create a single-task branch from the latest cleaned `origin/main`. Check the full newly introduced history of older branches before merging them.
2. Use a separate conversation for public research, loading only this repository and public sources. Do not continue a conversation that mixes private-project context.
3. Write Case / Evidence / Claim records before summaries or reader-facing prose. Leave unsupported details UNKNOWN and mark interpretations H.
4. Do not import private-project files, conversations, paths, budgets, staffing, plans or designs. Removing names or paraphrasing does not turn them into public sources.

Reusable scope for a research assistant:

> Work only in this public research repository. Use verifiable public sources and its research records. Do not read or map private projects. Record evidence and uncertainty before conclusions. General Transfer sections address unspecified groups of developers and must not guide any private project's current execution.

## Before committing

- Read the actual changes, not only a generated summary. Source important facts and clarify the definitions of amounts, team size and development start dates. Preserve UNKNOWN, H and opposing evidence.
- Check anonymous private information and passages that map a public case into what our own project should do now.
- Stage only files belonging to this task. Review the staged diff and commit message; do not include unrelated research or manuscript edits.
- Install the local hooks described in the [isolation policy](../../docs/public-research-boundary.md) and run `python tools/private_content_guard.py --staged`. Repair missing rules rather than bypassing the check.
- Run checks relevant to the change. For translations run `python tools/translation_lint.py`.
- The local pre-push hook checks newly introduced history. GitHub checks run after uploading and cannot replace local checks.

## PRs and other public surfaces

Use the PR template to state scope, evidence and verification. Manually review PR titles and bodies, Issues, comments, screenshots, attachments and external links; local terminology hooks do not cover these surfaces. Do not publish private rule lists, raw matches, contaminated history backups or raw audit data.

Automated checks are one layer of prevention. Passing a name scan does not establish that anonymous private information is absent. Industry terminology alone is not evidence of a leak.

## Translation and rights

Chinese originals and their Case / Evidence / Claim records remain the research basis. English uses the same IDs and does not create a second facts ledger. Register translation status and source version under the [bilingual policy](../../docs/bilingual-maintenance.md).

Public research, formal manuscripts and third-party materials follow separate rights under [LICENSE-CONTENT](../../LICENSE-CONTENT). Official translations require maintainer authorization. Publication permission for third-party translation submissions must be agreed separately; CC BY-NC-ND does not imply permission to publish derivatives. Submitting a contribution does not automatically authorize use of a contributor's original prose in a future commercial book.
