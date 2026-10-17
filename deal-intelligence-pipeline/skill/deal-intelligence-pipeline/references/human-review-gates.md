# Human Review Gates

Every phase must stop for human review.

## Allowed Review Actions

### Approve
Accept the phase output and permit the next phase.

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
Confirm deal identity, stage context, product, and analysis purpose.

### Gate 1 — Source Collection
Confirm the source inventory and remove incorrect sources or add missing sources.

### Gate 2 — Deal Context
Confirm facts, timeline, stakeholders, proof requirements, and dependencies.

### Gate 3 — Nick's 3 Questions
Confirm the evidence-backed conclusions or mark them Unknown / Needs Evidence.

### Gate 4 — Candidate Signals
Approve which candidate signals should be verified.

### Gate 5 — Verification
Approve which verified signals become reusable intelligence.

### Gate 6 — Git Storage
Approve the final deal record before it is treated as trusted Git knowledge.

### Gate 7 — Current-Deal Matching
Approve or reject each proposed closed-deal match.

### Gate 8 — 5-Minute Read Input
Final review before any intelligence is used by Sales.

## Stop Language

At the end of each phase, state:

`Human Review Required`

Then list the available decisions relevant to that phase.

Do not continue until the human explicitly responds.
