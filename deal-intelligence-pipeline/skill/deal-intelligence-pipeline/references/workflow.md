# Workflow

Run the repository-defined Phases 0-8 sequentially. Never add, rename, skip, or combine phases. Advance only after the completed phase is review-ready and the human issues the standalone exact command `APPROVE PHASE N` for it. Informal assent, source authorization, and approval of another phase do not satisfy this gate.

Before each existing phase, run the separate Repo Control Check in `output-schemas.md`. Load applicable rules from verified paths; unavailable rules require restoration or explicitly authorized, loaded fallback under `SKILL.md`. This adds no phase and does not expand Phase 0 intake/output.

## Phase 0 — Deal Intake

### Goal
Identify the deal only.

### Tasks and Rules
Phase 0 is an identification gate only. Ask for exactly four inputs: Deal Name, Product, Current Stage, and Record Type (Closed Deal or Current Deal). If some inputs are already supplied, ask only for missing or corrected identification inputs.

Do not ask the human during Phase 0 for historical stage/outcome, deal type, analysis purpose, sources, stakeholders, proof requirements, commercial context, technical context, meeting history, linked-deal history, known gaps, or any other secondary information.

Output only Deal Name, Product, Current Stage, Record Type, and Phase 0 Status. Status is system-maintained, not a fifth human input. Offer only APPROVE PHASE 0 | Correct and stop for explicit approval. Missing secondary details must not block Phase 0 approval. Discover and evaluate secondary context from approved sources in later phases.

One secondary purpose of the Deal Intelligence Pipeline is to discover important deal context, missing information, conflicts, and unknowns. Do not ask the human to pre-fill information that the system can reasonably discover from approved sources.

### Output
Only the five fields in the Phase 0 schema in `output-schemas.md`.

### Gate
Human reviews identification only: APPROVE PHASE 0 | Correct. Stop and wait for explicit approval before Phase 1.

---

## Phase 1 — Source Collection

### Goal
Build the evidence set before interpretation.

### Retrieval Sequence
Find -> Open -> Read -> Follow linked records -> Extract evidence -> Confirm coverage.

Finding a source is not reviewing it: titles, dates, snippets, and rollup names do not count. Inspect blank rollups and underlying relations before concluding anything is missing. Read meeting content before deciding product relevance; tags/titles alone cannot exclude it. Use only allowlisted or explicitly human-approved sources, then complete research before asking for secondary details.

### Tasks
- apply every family in the `source-config.md` discovery checklist; record searches, filters, pagination, found items, and unsuccessful search scope;
- locate DealStrategy and read its properties and body content;
- locate linked Deal where available;
- locate relevant Meeting Diary records;
- locate existing Hyly Wiki Git context;
- enumerate and fully read every in-scope transcript and review every in-scope recording through supported tools;
- query all in-scope linked database and authorized CRM records directly, including pagination;
- order sources chronologically;
- flag duplicates, irrelevant sources, missing sources, inaccessible sources, and source conflicts;
- identify whether later-outcome evidence exists;
- investigate duplicate DealStrategy records and stage/Last Stage conflicts using identifiers, history, edit dates, linked records, and overlapping fields; document supersession only if supported, otherwise retain the conflict for review;
- retrieve relevant linked-record and meeting content, following relations and rollups using `source-hierarchy.md`;
- record per-source retrieval status, source references, factual excerpts or concise factual summaries, and remaining retrieval work. Titles and dates alone are not collected evidence.

### Rule
Read and collect factual content for both current and closed deals. Do not answer Nick's questions, interpret the facts, score matching dimensions, or extract signals in this phase. Source approval remains required before Phase 2 analysis. Mark unread sources as Not Retrieved and failed retrievals as Inaccessible, not as missing deal facts.

### Output
Source Inventory + Chronological Evidence List.

### Gate
Finish exhaustive retrieval, reconcile artifact counts, and present Complete coverage before requesting normal source approval. Continue available work while coverage is Partial; report concrete blockers and recovery actions when Blocked. Follow batching/checkpoint rules in `source-hierarchy.md`. Human approves, removes, or adds sources; blocked reporting is not completed research.

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

Discover historical stage/outcome, analysis purpose, linked-deal history, and other secondary context from approved sources here and in later applicable phases. Evaluate missing information, conflicts, and unknowns rather than asking the human to pre-fill them during Phase 0.

Stage changes interpretation but is not a mandatory matching criterion. For In Pilot, assess meaningful progression; for Pilot Won, assess proven value; for Won / Booked, assess conversion to commitment; for Retain, assess what created, protected, weakened, or threatened ongoing value.

Build the timeline:

`Situation -> Important Meeting -> What Changed -> Follow-Up -> Later Outcome`

### Rule
Describe and organize facts from every approved source family, including CMD summaries/transcripts, insight pages, and call-analysis pages. Trace generated summaries and analysis to primary evidence where available; retain provenance, useful deal-specific details, and contradictions. Do not treat repeated summaries of the same event as independent corroboration. Do not yet convert facts into reusable signals.

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
Human selects candidates for verification with `APPROVE PHASE 4`; all remain candidates, not verified or approved reusable signals.

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
Only here may evidence-checked candidates become verified/approved reusable signals, after `APPROVE PHASE 5`. Rejected and Needs Evidence candidates do not become verified.

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
- verify current-deal source coverage and approved factual context before any assessment;
- if relevant content remains unread, return to Phase 1 retrieval and Phase 2 context review, stopping at each affected gate before resuming;
- collect the current deal's known context;
- compare known conditions with approved historical signals;
- explain specific match basis;
- identify missing material current-deal details;
- generate pending questions where needed;
- suggest another approved closed deal if it is a better fit to the known evidence.

### Important
Do not score from a template or treat unresearched dimensions as deal gaps. Each assessed dimension needs current-deal evidence or a documented coverage status under `source-hierarchy.md`. `Needs Current-Deal Detail` is reserved for a material fact still unresolved after relevant accessible sources were reviewed. Inaccessible evidence is an access limitation; identify what could not be checked.

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
