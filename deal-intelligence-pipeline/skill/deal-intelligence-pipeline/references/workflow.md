# Workflow

Run the workflow sequentially. Never skip a required human review gate.

## Phase 0 — Deal Intake

### Goal
Define exactly what is being analyzed.

### Tasks
- confirm deal name;
- confirm product;
- confirm current stage;
- identify historical stage / outcome if different;
- confirm deal type;
- identify whether the record is a closed deal or a current deal;
- establish the analysis purpose.

### Stage Handling
Stage changes interpretation but is not a mandatory matching criterion.

Examples:
- In Pilot: identify meaningful progression rather than claiming closure.
- Pilot Won: identify what helped the pilot prove enough value.
- Won / Booked: identify what converted evaluation to commitment.
- Retain: identify what created, protected, weakened, or threatened ongoing value.

### Output
Deal Analysis Header.

### Gate
Human confirms identity and analysis context.

---

## Phase 1 — Source Collection

### Goal
Build the evidence set before interpretation.

### Tasks
- locate DealStrategy;
- locate linked Deal where available;
- locate relevant Meeting Diary records;
- locate existing Hyly Wiki Git context;
- identify transcripts linked to important meetings;
- order sources chronologically;
- flag duplicates, irrelevant sources, missing sources, inaccessible sources, and source conflicts;
- identify whether later-outcome evidence exists.

### Rule
Do not answer Nick's questions and do not extract signals in this phase.

### Output
Source Inventory + Chronological Evidence List.

### Gate
Human approves, removes, or adds sources.

---

## Phase 2 — Deal Context Analysis

### Goal
Establish the factual baseline using only approved sources.

### Tasks
Extract:
- product;
- stage / outcome;
- deal type;
- primary requirement;
- scope;
- starting position;
- open decisions;
- blockers;
- proof needed;
- decision structure;
- material technical dependencies;
- material commercial dependencies;
- important events;
- outcome / delta.

Build the timeline:

`Situation -> Important Meeting -> What Changed -> Follow-Up -> Later Outcome`

### Rule
Describe and organize facts. Do not yet convert them into reusable signals.

### Output
Structured Deal Context Record.

### Gate
Human confirms facts and corrections.

---

## Phase 3 — Nick's 3 Questions

### Goal
Answer the three research questions consistently from approved evidence.

Use `nicks-3-questions.md`.

### Output
Three evidence-backed answers with confidence, Dig Factor where relevant, and Brief Catchability where relevant.

### Gate
Human approves, edits, requests more evidence, or marks an answer Unknown.

---

## Phase 4 — Signal Extraction

### Goal
Convert approved findings into standardized candidate signals.

Use `signal-taxonomy.md`.

### Tasks
For each candidate signal capture:
- Signal Type;
- Observed Condition;
- Deal Context;
- Impact;
- Evidence;
- Transferability;
- Confidence.

### Rule
Preserve `Signal -> Deal Context -> Impact`.

### Output
Candidate Signal Records.

### Gate
Human approves which candidates are worth verifying.

---

## Phase 5 — Verification / Critic

### Goal
Challenge candidate conclusions before they become reusable intelligence.

Use `verification-rules.md`.

### Output
Each candidate becomes:
- Approved;
- Needs Evidence;
- Rejected.

### Gate
Human gives final approval to reusable signals.

---

## Phase 6 — Git Storage

### Goal
Create the durable approved deal record.

### Tasks
Store:
- deal-specific context;
- Nick's approved answers;
- approved signals;
- evidence references;
- confidence;
- unresolved Unknowns if they are intentionally retained.

Keep drafts and approved records separate.

### Output
Approved Deal Record ready for Git.

### Gate
Human approves the record before it is treated as trusted library knowledge.

---

## Phase 7 — Current-Deal Matching

### Goal
Compare a current deal we are trying to close with the approved closed-deal intelligence library.

### Tasks
- collect the current deal's known context;
- compare known conditions with approved historical signals;
- explain specific match basis;
- identify missing material current-deal details;
- generate pending questions where needed;
- suggest another approved closed deal if it is a better fit to the known evidence.

### Important
Stage matching is **not mandatory**.

Stage may strengthen or weaken relevance, but a different-stage closed deal may still be useful when the underlying requirement, stakeholder situation, proof need, technical condition, commercial condition, adoption context, blocker, or progression pattern is relevant.

### Output
Current-Deal Match Report.

### Gate
Human approves or rejects each proposed match.

---

## Phase 8 — 5-Minute Read Input

### Goal
Translate only approved current-deal findings and approved relevant closed-deal patterns into 5-Minute Read input.

### Rules
Historical patterns may influence:
- what gets elevated;
- what gets validated;
- what gets questioned;
- what pending questions are surfaced.

Historical patterns may not be presented as current-deal facts without independent current-deal evidence.

### Existing Sections
Refine only the existing sections:
- Snapshot
- Last Meeting
- Next Steps
- People
- Tech & Commercial
- Risks & Signals
- Call Focus
- 30-Second Readiness Check

### Output
5-Minute Read V2 Input Package.

### Gate
Final human review before Sales use.
