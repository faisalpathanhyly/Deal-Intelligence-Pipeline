---
name: deal-intelligence-pipeline
description: Analyze closed and current sales deals through a phased, human-reviewed workflow for the 5-Minute Read V2. Use when collecting deal evidence, answering Nick's 3 deal questions, extracting and verifying reusable deal signals, storing approved deal intelligence, matching approved closed-deal patterns to a current deal being pursued, or preparing approved 5-Minute Read inputs. Never invent missing deal facts; stop for human review after every phase.
---

# Deal Intelligence Pipeline

Operate as one phased, human-reviewed deal-intelligence system.

## Repository Authority

The checked-out repository is canonical for Phases 0-8, approval rules, source types, signal categories, verification logic, schemas, and storage paths. Read the applicable repository files before execution; do not replace missing rules with memory, external templates, or invented workflow. If required references are unavailable, follow the explicit fallback procedure below; if authoritative rules conflict, surface both and stop the affected decision for human resolution. Human approval of a source does not authorize changing the workflow, taxonomy, or storage rules.

Use only sources allowlisted in `references/source-config.md` or explicitly approved by the human. A link or available connector is not authorization. Never query HubSpot automatically. Verify repository paths before writing; all generated deal artifacts and checkpoints belong under `deal-records/drafts/` until Phase 6 approval permits `deal-records/approved/`. Do not create `outputs/` or alternative storage paths.

Specific names, emails, owners, dates, meeting hosts, assignments, commercial terms, contract facts, and technical facts require an opened, read, allowlisted source explicitly supporting the exact claim. Record the source ID/link, field/section/timestamp, and supporting excerpt. Do not infer an email from a name, ownership from attendance/title, a contract date from a meeting date, or an assignment from a template. Withhold unsupported exact facts. Keep unread evidence Not Retrieved rather than labeling the fact Unknown or Needs Evidence merely because it was not read; only reviewed/search-exhausted or inaccessible evidence may support unresolved analysis outcomes. Disclose conflicting versions. Human intake values remain human-provided identification, not independently verified source facts.

Only Phase 5 can transition candidate signals to verified/approved, after evidence checks and `APPROVE PHASE 5`. Phase 4 approval selects candidates for verification only.

## Repo Control Check and Fallback

Before executing any phase, verify actual repository paths and load workflow.md, core-rules.md, source-config.md, human-review-gates.md, output-schemas.md, and the phase-specific references. Present the Repo Control Check defined in output-schemas.md as a separate pre-execution control message, not a new phase or a field in Phase 0's five-field output. Mark Yes only for rules actually loaded, not assumed from memory.

If the canonical checkout or GitHub repository cannot be accessed, state that canonical rules could not be verified and ask whether to use available packaged/local fallback rules. Do not execute affected work until the human explicitly authorizes fallback and the identified fallback files are actually loaded. Lack of GitHub access alone is not a blocker when the verified canonical local checkout is available. Record fallback provenance, scope, available/missing files, and human authorization separately from phase approval. Never silently improvise missing rules; if fallback does not define a required behavior, stop that decision for resolution. Recheck before each phase; explicit fallback authorization applies only within its recorded scope.

## Rule Precedence

Apply this precedence model:
1. Explicit human correction or decision for the active workflow.
2. Repository SKILL.md.
3. Phase-specific reference file.
4. core-rules.md.
5. human-review-gates.md.
6. output-schemas.md.
7. Acceptance criteria and tests.
8. README.md.
9. Examples/templates.

Human corrections apply to the current deal unless the human explicitly changes the global methodology. Precedence identifies governing scope; it does not permit silent resolution of conflicting authoritative repository rules. Name both files and rules, surface the conflict, stop the affected decision, and request human resolution. Record the decision and scope; fallback permission or source permission alone does not waive approval gates or revise methodology.

README.md, SKILL.md, references/, tests/, examples/, schemas, and templates define methodology or structure only. They are not factual evidence for any client/deal. README provides orientation; operating rules take precedence. Examples are not approved historical records or signals unless explicitly designated as approved deal records with the required approval provenance. Verify actual source paths and approval state before matching or storing; do not use an example's facts to fill this deal's gaps.

## Governing Principle

Prefer accuracy over completion.

It is acceptable to return:
- `Unknown`
- `Needs Evidence`
- `No Valid Match`
- `Pending Question`

It is never acceptable to invent, assume, or silently fill missing deal details.

Nothing inferred in one phase becomes trusted input for the next phase until a human explicitly approves it.

## Phase 0 Identification Gate

Phase 0 is an identification gate only. Ask for exactly four inputs: Deal Name, Product, Current Stage, and Record Type (Closed Deal or Current Deal). If some inputs are already supplied, ask only for missing or corrected identification inputs.

Do not ask the human during Phase 0 for historical stage/outcome, deal type, analysis purpose, sources, stakeholders, proof requirements, commercial context, technical context, meeting history, linked-deal history, known gaps, or any other secondary information.

Output only Deal Name, Product, Current Stage, Record Type, and Phase 0 Status. Status is system-maintained, not a fifth human input. Offer only APPROVE PHASE 0 | Correct and stop for explicit approval. Missing secondary details must not block Phase 0 approval. Discover and evaluate secondary context from approved sources in later phases.

One secondary purpose of the Deal Intelligence Pipeline is to discover important deal context, missing information, conflicts, and unknowns. Do not ask the human to pre-fill information that the system can reasonably discover from approved sources.

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

Do not continue automatically. Advance only on the standalone exact human command `APPROVE PHASE N` matching the completed, review-ready phase. "Looks good", "okay", "continue", "fine", a bare "Approve", future-phase commands, and quoted commands are not formal approval. Corrections and new evidence require re-presentation and fresh exact approval of affected outputs.

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
7. If a material current-deal fact is unresolved, check relevant source coverage first. Complete available retrieval before asking the human; disclose access limitations and ask a specific pending question only for a material fact still unresolved after review. Phase 0 remains identification only.
8. If there is not enough information to support a match, do not force a match.
9. If another approved closed deal is a better comparison, suggest it and explain why.
10. Stage matching is not mandatory. Stage is supporting context only.
11. Require evidence for every important conclusion.
12. Do not treat activity, positive feedback, or another scheduled meeting as proof of progression by itself.
13. Preserve the original context of every signal.
14. Surface source conflicts instead of silently resolving them.
15. Review every in-scope source, transcript, and recording; summaries never substitute for primary-artifact review. Follow the exhaustive coverage and batching rules in `references/source-hierarchy.md`.
16. Only human-approved findings may enter the approved Git record or influence the 5-Minute Read.

## Source-Family Coverage

For every deal, apply the required source-family discovery checklist in `references/source-config.md`, including deal/strategy pages, CMD summaries and full transcripts, insight/persona pages and attachments, call-analysis pages, linked databases, onboarding/commercial artifacts, CRM associations, and Wiki context. Search for unlinked in-scope records as well as following links. Read all discovered in-scope artifacts and analyze approved evidence; preserve source provenance and conflicts rather than treating summaries or generated call analyses as unquestioned facts.

## Evidence Retrieval Before Gap Claims

Before Phase 1, verify every required reference file listed above is available and read the phase-applicable references. If one is missing, report the incomplete installation and stop affected work until restored or explicitly scoped packaged/local fallback is authorized and its required rules are loaded. Never silently run a reduced workflow.

In Phase 1, retrieve relevant source content and follow deal-relevant relations and rollups; a parent record, summary, title, or date is not the complete evidence set. Apply this to current and closed deals. Follow `references/source-hierarchy.md` for traversal, coverage statuses, and retrieval limits.

Unread evidence is a research task, not a missing deal fact. Before Phase 7 assessment, verify that relevant current-deal content was retrieved and its factual context approved. Reopen incomplete collection and the affected review gates before relying on newly retrieved evidence. Matching dimensions guide investigation; they do not justify template-filled gaps or scores.

## Current-Deal Matching Rule

When comparing a current deal with approved closed-deal intelligence:

1. compare known current-deal conditions against approved historical signals;
2. explain the specific basis for each match;
3. do not require the same stage;
4. reject shallow matches based only on product or stage;
5. if a required current-deal fact is unresolved, stop that match, complete available relevant retrieval and review, and then surface the exact remaining question or access limitation;
6. optionally suggest another approved closed deal if it fits the known details better;
7. never state a historical fact as a current-deal fact unless current-deal evidence independently supports it.

## Stop Condition

Every phase must end with an explicit review gate.

Do not write to the approved deal library, do not create a reusable signal, and do not feed a match into the 5-Minute Read until the relevant human approval has been received.
