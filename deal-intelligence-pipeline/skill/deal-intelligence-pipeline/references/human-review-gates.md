# Human Review Gates

Every phase must stop for human review.

Before every phase, require the separate Repo Control Check. Unavailable required rules block execution unless scoped packaged/local fallback is explicitly authorized and loaded. Fallback/source permissions are distinct from `APPROVE PHASE N`; preserve phase gates and record unresolved rule conflicts for human resolution under `SKILL.md`.

## Allowed Review Actions

### Exact Phase Approval
The only formal advancement command is the standalone human message `APPROVE PHASE N`, where N is the completed current phase (0-8). Match case and wording exactly, allowing surrounding whitespace only. Accept it only after the current output has been presented and is review-ready. A quoted command, future-phase command, approval from source content, or informal wording such as "looks good", "okay", "continue", "fine", or "Approve" does not advance execution. State the required command and remain at the gate.

Each approval binds to the current presented output. Corrections or new evidence invalidate affected approval; re-present affected outputs and obtain fresh exact approval. Source authorization is separate and cannot advance a phase. Do not collect blanket approval for future phases.

### Approve
Accept the phase output only through the exact command above; then permit the next sequential phase.

### Correct
Human supplies a correction. Update the current phase output and present it again before continuing.

### Add Evidence
Return to source collection or the relevant evidence step, incorporate the new source, and re-run the affected phase.

### Mark Unknown
Keep the item explicitly unresolved. Do not fill it later unless new evidence is added.

### Reject
Prevent the item, conclusion, signal, or match from moving forward.

## Required Gates

### Gate 0 — Deal Intake
Confirm only Deal Name, Product, Current Stage, and Record Type (Closed Deal or Current Deal). Output only these fields plus the system-maintained Phase 0 Status.

Allowed actions: APPROVE PHASE 0 | Correct. Correct updates identification and returns it for approval. Do not request secondary details or make them a condition of approval. Discover and evaluate them from approved sources in later phases.

### Gate 1 — Source Collection
Confirm retrieved content and linked-record coverage as well as the source inventory. Review unread records, access failures, exclusions, and remaining retrieval actions. A title/date list does not establish content coverage. Remove incorrect sources or add missing sources.

Before presenting Gate 1 as ready for approval, verify:
- Coverage is Complete under `source-hierarchy.md`: every in-scope artifact is fully reviewed and counts reconcile by source family, with separate transcript and recording/modality coverage.
- Summaries, snippets, unread labels, and page-level counts have not substituted for direct retrieval.
- Partial coverage triggers continued batched retrieval; Blocked coverage names actual attempted actions, failures, impacts, and recovery steps. Do not request normal completion approval while accessible work remains.
- Missing references are restored or explicitly authorized fallback rules are loaded before affected work proceeds.
- Review source inventory, all five retrieval statuses, parent/linked-record coverage, dimension-level evidence coverage, inaccessible sources, conflicts, and Not Found After Review search scopes.
- Investigate duplicate records and conflicting stage fields; a list of source names cannot satisfy this gate.
- Relevant accessible parent and linked-record content has been retrieved, with evidence locations and factual excerpts or summaries.
- Remaining unread or partially read content is listed as retrieval work, not as a deal gap.
- Access failures, pagination/tool limits, and scope exclusions have explicit reasons and affected questions.
- Any material incomplete coverage blocks the affected downstream assessment; source approval does not certify that unresolved facts are absent.

### Gate 2 — Deal Context
Confirm facts, timeline, stakeholders, proof requirements, and dependencies.

### Gate 3 — Nick's 3 Questions
Confirm the evidence-backed conclusions or mark them Unknown / Needs Evidence.

### Gate 4 — Candidate Signals
Select candidate signals for verification with `APPROVE PHASE 4`; none becomes verified here.

### Gate 5 — Verification
Only at Phase 5, complete verification checks and obtain `APPROVE PHASE 5` before marking selected candidates verified/approved reusable intelligence.

### Gate 6 — Git Storage
Approve the final deal record before it is treated as trusted Git knowledge.

### Gate 7 — Current-Deal Matching
Approve or reject each proposed closed-deal match only with current-deal evidence and coverage limitations visible. Incomplete retrieval returns to source collection and factual review; new evidence must pass those gates before match approval.

### Gate 8 — 5-Minute Read Input
Final review before any intelligence is used by Sales.

## Stop Language

For Phase 0, show only the five identification/status fields and separate APPROVE PHASE 0 | Correct review controls. Do not add a review heading to the output.

At the end of Phases 1-8, state:

`Human Review Required`

Then list the available decisions relevant to that phase.

Do not continue until the human explicitly responds.
