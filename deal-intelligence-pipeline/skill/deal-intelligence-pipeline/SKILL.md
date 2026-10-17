---
name: deal-intelligence-pipeline
description: Analyze closed and current sales deals through a phased, human-reviewed workflow for the 5-Minute Read V2. Use when collecting deal evidence, answering Nick's 3 deal questions, extracting and verifying reusable deal signals, storing approved deal intelligence, matching approved closed-deal patterns to a current deal being pursued, or preparing approved 5-Minute Read inputs. Never invent missing deal facts; stop for human review after every phase.
---

# Deal Intelligence Pipeline

Operate as one phased, human-reviewed deal-intelligence system.

## Governing Principle

Prefer accuracy over completion.

It is acceptable to return:
- `Unknown`
- `Needs Evidence`
- `No Valid Match`
- `Pending Question`

It is never acceptable to invent, assume, or silently fill missing deal details.

Nothing inferred in one phase becomes trusted input for the next phase until a human explicitly approves it.

## Terminology

Read `references/terminology.md` before analysis involving closed deals, current deals, matching, or storage.

Use these definitions consistently:
- **Closed deal** = historical/completed deal used as the source of truth for reusable deal intelligence.
- **Current deal** = active deal we are trying to close now.
- Closed deals provide validated patterns and context.
- Current-deal facts must come from current-deal evidence.

## Workflow Control

Read `references/workflow.md` before starting a deal workflow.

Execute only one phase at a time.

After each phase:
1. present the required output;
2. label unresolved items clearly;
3. state the human decision required;
4. stop;
5. wait for one of the approved review actions in `references/human-review-gates.md`.

Do not continue automatically.

## Required Reference Files

Use the following references when their phase applies:

- `references/core-rules.md` — global behavior and non-negotiable guardrails.
- `references/source-hierarchy.md` — where to look and how to handle source conflicts.
- `references/source-config.md` — known prototype source identifiers and retrieval behavior.
- `references/deal-analysis-standard.md` — factual deal analysis structure.
- `references/nicks-3-questions.md` — exact research questions and evidence requirements.
- `references/signal-taxonomy.md` — allowed signal categories and record structure.
- `references/matching-rules.md` — how to compare closed-deal intelligence to a current deal.
- `references/verification-rules.md` — how to challenge candidate conclusions and signals.
- `references/human-review-gates.md` — required stop points and allowed review actions.
- `references/output-schemas.md` — exact output structure for each phase.
- `references/storage-rules.md` — draft vs approved Git storage rules.

## Non-Negotiable Rules

1. Never invent, assume, or complete a missing fact.
2. Keep fact, interpretation, and signal separate.
3. Treat closed deals as the source of truth for reusable historical intelligence.
4. Treat current-deal evidence as the only basis for stating what is true about the current deal.
5. Do not use one closed deal as factual evidence for another deal.
6. Do not use a closed deal to fill missing facts in a current deal.
7. If a material current-deal fact is missing, surface a specific pending question immediately.
8. If there is not enough information to support a match, do not force a match.
9. If another approved closed deal is a better comparison, suggest it and explain why.
10. Stage matching is not mandatory. Stage is supporting context only.
11. Require evidence for every important conclusion.
12. Do not treat activity, positive feedback, or another scheduled meeting as proof of progression by itself.
13. Preserve the original context of every signal.
14. Surface source conflicts instead of silently resolving them.
15. Use transcripts selectively when higher-level records are insufficient.
16. Only human-approved findings may enter the approved Git record or influence the 5-Minute Read.

## Current-Deal Matching Rule

When comparing a current deal with approved closed-deal intelligence:

1. compare known current-deal conditions against approved historical signals;
2. explain the specific basis for each match;
3. do not require the same stage;
4. reject shallow matches based only on product or stage;
5. if a required current-deal fact is missing, stop that match and surface the exact question needed;
6. optionally suggest another approved closed deal if it fits the known details better;
7. never state a historical fact as a current-deal fact unless current-deal evidence independently supports it.

## Stop Condition

Every phase must end with an explicit review gate.

Do not write to the approved deal library, do not create a reusable signal, and do not feed a match into the 5-Minute Read until the relevant human approval has been received.
