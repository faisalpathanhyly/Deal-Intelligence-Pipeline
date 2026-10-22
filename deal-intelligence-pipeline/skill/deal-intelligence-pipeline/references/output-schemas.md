# Output Schemas

Use these repository schemas; do not invent fields that change phase scope. Each phase gate requires the standalone exact human command `APPROVE PHASE N`; non-approval actions never advance a phase. Phase 0 still contains only its five fields and separate approval/correction controls.

For Phases 1-8, include an approval record with Phase, Presented Output Revision, Required Command, and Actual Human Approval (or Pending). Record only actual commands, never infer approval from informal assent. This record belongs in the phase draft, not in Phase 0's five-field output.

The control block and phase schemas below are separate messages. Do not merge the control fields into deal output.

## Repo Control Check (Before Each Phase)

Present this separately before phase execution. It is an execution control, not a tenth phase, deal intake, or a field in Phase 0 output.

```markdown
Repo Control Check
- Repository available: Yes / No
- Workflow loaded: Yes / No
- Core rules loaded: Yes / No
- Phase-specific rules loaded: Yes / No
- Source configuration loaded: Yes / No
- Human review gate loaded: Yes / No
- Output schema loaded: Yes / No
- Active phase: Phase N
```

Keep actual file paths/revision and any failure in the control record. If canonical rules cannot be verified, state that limitation and stop pending explicit fallback authorization. Record fallback files/provenance, missing rules, scope, and authorization separately; do not mark Repository available Yes solely because fallback exists. Required fallback rules must actually be loaded before execution.

## Phase 0 — Deal Analysis Header

Phase 0 is identification only. Request exactly the four identification inputs below, asking only for missing or corrected inputs when others are supplied. Do not request or output secondary details; discover and evaluate them from approved sources in later phases.

```markdown
- Deal Name:
- Product:
- Current Stage:
- Record Type: Closed Deal | Current Deal
- Phase 0 Status: Awaiting Identification | Awaiting Approval | Approved
```

Derive Phase 0 Status: Awaiting Identification while any identification input is missing, Awaiting Approval when all four are supplied or corrected, and Approved only after `APPROVE PHASE 0`. Status is not a human input; missing secondary context does not affect it.

Present review controls separately from the five-field output: APPROVE PHASE 0 | Correct. No other Phase 0 output fields or actions are allowed.

## Phase 1 — Source Inventory

```markdown
# Source Inventory

| Source | Type | Linked From | Retrieved? | Content Reviewed? | Relevant Evidence | Status |
|---|---|---|---|---|---|---|

Source includes stable ID/link; Relevant Evidence includes opened field/section/timestamp and excerpt. Retain date, purpose, scope reason, reviewed chunks, and remaining action in the associated ledger.

## Linked Records
| Parent Source | Linked Record | Relation Type | Reviewed? | Relevance |
|---|---|---|---|---|

## Evidence Coverage
| Dimension | Sources Reviewed | Evidence Found? | Coverage Status |
|---|---|---|---|

Use Stakeholder, Proof / Value, Technical, Commercial, Adoption, and Risk / Blocker where applicable. Coverage Status uses the five evidence statuses; dimensions organize evidence and do not create signals in Phase 1.

## Conflicts
- Opened sources, incompatible claims, duplicate/stage history investigation, and required human decision:

## Missing / Inaccessible Sources
- Source, attempted action, retrieval status, search scope, limitation, and next action:

## Source Authorization
| Provider / Source Family | Baseline Allowlist Entry or Explicit Human Approval / Scope | Authorization Pending? |
|---|---|---|

Use Retrieved | Not Retrieved | Inaccessible | Conflicting | Not Found After Review for evidence status. Pending source authorization stays Not Retrieved with its reason. Do not mislabel unread evidence as missing. Put exclusions and duplicate mappings in separate fields.

## Coverage Limitations
- Relevant unread or partially read records, access failures, pagination/tool limits, and affected questions:

## Coverage Review
- Coverage Status: Complete | Partial | Blocked
- Documented Deal Scope:
- Discovery / Pagination Exhausted: Yes | No
- Required References Available: Yes | No

| Source Family | Discovered Unique | Fully Reviewed | Partially Reviewed | Not Retrieved | Blocked | Excluded |
|---|---|---|---|---|---|---|

## Source-Family Discovery Checklist
| Family from source-config.md | Links / Locations and Queries / Filters Checked | Pagination Exhausted? | Matching Artifact IDs | No-Match Search Scope / Blocker | Remaining Action |
|---|---|---|---|---|---|

Populate every family even when no matching record is found. No matching result documents the search performed; it does not prove absence. Track nested attachments and each summary/transcript/call-analysis artifact separately in the inventory.

## Artifact and Modality Coverage
| Artifact ID / Link | Canonical ID / Duplicate Of | Text / Audio / Video | Sections / Time Range Reviewed | Full Content Reviewed? | Tool Attempt / Failure | Remaining Action |
|---|---|---|---|---|---|---|

## Checkpoint
- Ledger / Evidence Notes Location:
- Remaining IDs and Page / Chunk Cursor:
- Exact Resume Action:

## Limitations
- Relevant accessible retrieval complete: Yes | No
- Material questions blocked by incomplete retrieval or access:
- Source scope exclusions and reasons:
- Next retrieval / access action:

## Missing / Conflicting Sources
- ...

## Chronological Evidence List
1. ...
2. ...

## Human Review Required
APPROVE PHASE 1 | Remove source | Add Evidence | Mark Unknown
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
APPROVE PHASE 2 | Correct | Add Evidence | Mark Unknown
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
APPROVE PHASE 3 | Correct | Add Evidence | Mark Unknown | Reject
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
APPROVE PHASE 4 | Correct | Add Evidence | Reject
```

## Phase 5 — Verified Signal Set

```markdown
# Verified Signal Set

| Signal | Verification Status | Evidence Check | Contradictions | Confidence | Verifier Note |
|---|---|---|---|---|---|

## Human Review Required
APPROVE PHASE 5 | Needs Evidence | Reject
```

For Phase 5, record candidate ID, opened-source checks, contradictions, later-outcome check, verification outcome, and exact human approval. Approved is final only after `APPROVE PHASE 5`; other phases cannot supply this transition.

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

Phase 6 review command: `APPROVE PHASE 6`. Store only in paths verified under `storage-rules.md`.

## Phase 7 — Current-Deal Match Report

```markdown
# Current-Deal Match Report

## Current Deal
- Deal:
- Known Context:
- Missing Material Context:

## Proposed Match [N] / Dimension [D]
- Dimension:
- Sources Checked:
- Coverage Status:
- Historical Signal:
- Closed Deal:
- Approved Historical Signal:
- Current-Deal Evidence:
- Evidence Status per Matching Dimension:
- Opened Source + Field / Section / Timestamp:
- Match Basis:
- Stage Context:
- Why It May Matter:
- Match Confidence:
- Missing Information:
- Pending Question:
- Alternative Closed Deal, if better:

## Evidence Coverage for Assessed Dimensions
| Dimension / Material Question | Coverage Status | Current-Deal Evidence / Sources Reviewed | Retrieval Limitation / Remaining Action |
|---|---|---|---|

Repeat the dimension block for every assessed dimension; do not hide a Not Retrieved dimension in an aggregate score. Pending Question is allowed only after searched sources/linked records leave a required fact Not Found After Review, Inaccessible, or materially Conflicting.

Use Retrieved, Conflicting, Not Retrieved, Inaccessible, or Not Found After Review. Unread or inaccessible evidence blocks the affected assessment; it is not a deal-gap score. Document search scope for Not Found After Review. Do not fill dimensions from the template without research.

## No-Match Cases
- Reason no valid match can be made yet:
- Evidence needed:

## Human Review Required
APPROVE PHASE 7 | Reject match | Ask Pending Question | Suggest Another Closed Deal
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
APPROVE PHASE 8 | Correct | Remove Item | Ask Pending Question
```
