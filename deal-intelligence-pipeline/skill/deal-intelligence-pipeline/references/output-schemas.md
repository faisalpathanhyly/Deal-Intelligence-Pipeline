# Output Schemas

Use these schemas to keep outputs consistent.

## Phase 0 — Deal Analysis Header

```markdown
# Deal Analysis Header
- Deal:
- Product:
- Deal Type:
- Current Stage:
- Historical Stage / Outcome:
- Record Type: Closed Deal | Current Deal
- Analysis Purpose:
- Known Gaps:

## Human Review Required
Approve | Correct | Add Evidence | Mark Unknown | Reject
```

## Phase 1 — Source Inventory

```markdown
# Source Inventory

| Source | Date | Type | Relevant? | Purpose | Status |
|---|---|---|---|---|---|

## Missing / Conflicting Sources
- ...

## Chronological Evidence List
1. ...
2. ...

## Human Review Required
Approve sources | Remove source | Add Evidence | Mark Unknown
```

## Phase 2 — Deal Context Record

```markdown
# Deal Context Record

## Deal Context
- Product:
- Stage / Outcome:
- Deal Type:
- Primary Requirement:
- Scope:

## Starting Position
...

## Decision Structure
- Champion:
- Decision-Maker:
- Gatekeeper:
- Technical Validator:
- Operational Stakeholder:
- Missing / Weakened Stakeholder:

## Proof Needed
...

## Technical Dependencies
...

## Commercial Dependencies
...

## Timeline
| Situation | Important Meeting | What Changed | Follow-Up | Later Outcome |
|---|---|---|---|---|

## Unknown / Needs Evidence
...

## Human Review Required
Approve | Correct | Add Evidence | Mark Unknown
```

## Phase 3 — Nick's 3 Questions

```markdown
# Nick's 3 Questions

## Q1 — What actually moved it?
- Answer:
- Supporting Evidence:
- Later-Outcome Evidence:
- Confidence:

## Q2 — What did the rep know going in?
- Critical Pre-Call Context:
- Why It Mattered:
- Source:
- Dig Factor:
- Confidence:

## Q3 — Why did it stall, and would a brief have caught it?
- Stall Symptom:
- Underlying Reason:
- Supporting Evidence:
- Earlier Warning Signs:
- Brief Catchability:
- Confidence:

## Human Review Required
Approve | Correct | Add Evidence | Mark Unknown | Reject
```

## Phase 4 — Candidate Signal Record

```markdown
# Candidate Signals

## Signal [N]
- Signal Type:
- Observed Condition:
- Deal Context:
- Impact in This Deal:
- Evidence:
- Transferability:
- Confidence:
- Open Questions:

## Human Review Required
Approve candidate | Correct | Add Evidence | Reject
```

## Phase 5 — Verified Signal Set

```markdown
# Verified Signal Set

| Signal | Verification Status | Evidence Check | Contradictions | Confidence | Verifier Note |
|---|---|---|---|---|---|

## Human Review Required
Approve reusable signal | Needs Evidence | Reject
```

## Phase 6 — Approved Deal Record

```markdown
# Approved Deal Record — [Deal]

## Deal Context
...

## Starting Position
...

## Timeline
...

## Nick's 3 Questions
...

## Decision Structure
...

## Proof Needed
...

## Technical Dependency
...

## Commercial Dependency
...

## Stall Reason
...

## Outcome / Delta
...

## Approved Signals
...

## Evidence References
...

## Confidence
...

## Unresolved Unknowns
...
```

## Phase 7 — Current-Deal Match Report

```markdown
# Current-Deal Match Report

## Current Deal
- Deal:
- Known Context:
- Missing Material Context:

## Proposed Match [N]
- Closed Deal:
- Approved Historical Signal:
- Current-Deal Evidence:
- Match Basis:
- Stage Context:
- Why It May Matter:
- Match Confidence:
- Missing Information:
- Pending Question:
- Alternative Closed Deal, if better:

## No-Match Cases
- Reason no valid match can be made yet:
- Evidence needed:

## Human Review Required
Approve match | Reject match | Ask Pending Question | Suggest Another Closed Deal
```

## Phase 8 — 5-Minute Read V2 Input Package

```markdown
# 5-Minute Read V2 Input Package

## Snapshot
...

## Last Meeting
...

## Next Steps
...

## People
...

## Tech & Commercial
...

## Risks & Signals
...

## Call Focus
...

## 30-Second Readiness Check
...

## Pending Questions
...

## Approved Historical Pattern Influence
- Pattern:
- How it changed prioritization / questioning:
- Current-deal evidence supporting its relevance:

## Final Human Review Required
Approve for Sales use | Correct | Remove Item | Ask Pending Question
```
