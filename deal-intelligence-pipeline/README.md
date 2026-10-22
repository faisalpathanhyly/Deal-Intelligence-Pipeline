# Deal Intelligence Pipeline

Prototype repository for a phased, human-reviewed deal-intelligence system that supports the 5-Minute Read V2.

## Objective

Build one repeatable pipeline that can:

1. collect approved deal evidence;
2. establish deal context;
3. answer Nick's 3 questions;
4. convert approved findings into reusable signals;
5. verify those signals;
6. store only approved deal intelligence in Git;
7. compare approved closed-deal intelligence against a current deal we are trying to close; and
8. prepare approved inputs for the 5-Minute Read V2.

The prototype is designed for Claude Skill / Claude Project testing. A Dark Factory is a later operationalization option after the workflow, rules, schemas, and review gates are stable.

## Repository Authority and Execution Contract

The checked-out repository is canonical for Phases 0-8, approval rules, source types, signal categories, verification logic, schemas, and storage paths. Read the applicable repository files before execution; do not replace missing rules with memory, external templates, or invented workflow. If references are unavailable, use only the explicitly authorized fallback procedure below; if authoritative rules conflict, report both and stop the affected decision. Human approval of a source does not authorize changing the workflow, taxonomy, or storage rules.

Phase 0 requests only Deal Name, Product, Current Stage, and Record Type. Phase 1 follows Find -> Open -> Read -> Follow linked records -> Extract evidence -> Confirm coverage. Discovery labels are not reviewed evidence. Use the allowlist in `source-config.md`; HubSpot requires explicit human source approval. Every phase ends with the exact command `APPROVE PHASE N` for that completed phase; informal assent never advances execution. Phase 5 alone can verify candidate signals, and Phase 6 approval controls approved storage. Generated deal records use only verified `deal-records/drafts/` and `deal-records/approved/` paths.

## Rule Loading, Fallback, and Precedence

Before executing any phase, verify actual repository paths and load workflow.md, core-rules.md, source-config.md, human-review-gates.md, output-schemas.md, and the phase-specific references. Present the Repo Control Check defined in output-schemas.md as a separate pre-execution control message, not a new phase or a field in Phase 0's five-field output. Mark Yes only for rules actually loaded, not assumed from memory.

If the canonical checkout or GitHub repository cannot be accessed, state that canonical rules could not be verified and ask whether to use available packaged/local fallback rules. Do not execute affected work until the human explicitly authorizes fallback and the identified fallback files are actually loaded. Lack of GitHub access alone is not a blocker when the verified canonical local checkout is available. Record fallback provenance, scope, available/missing files, and human authorization separately from phase approval. Never silently improvise missing rules; if fallback does not define a required behavior, stop that decision for resolution. Recheck before each phase; explicit fallback authorization applies only within its recorded scope.

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

## Core Principle

**Accuracy over completion.** It is acceptable to return `Unknown`, `Needs Evidence`, `No Valid Match`, or a `Pending Question`. It is not acceptable to invent information in order to complete a phase.

Nothing inferred in one phase becomes trusted input for the next phase until a human reviews and approves it.

## Terminology

- **Closed deal**: a completed / historical deal whose approved evidence and verified signals form the reusable intelligence library.
- **Current deal**: an active deal we are trying to close now.
- **Closed-deal source of truth**: the approved historical evidence and verified deal intelligence used to understand what mattered in previous deals.
- **Current-deal evidence**: the only basis for stating what is true about the current deal.
- **Signal**: an evidence-backed pattern that preserves its original deal context and impact.
- **Pending question**: a specific question surfaced when a material current-deal fact is missing and is needed to validate a conclusion or match.

## Repository Structure

```text
deal-intelligence-pipeline/
├── README.md
├── skill/
│   └── deal-intelligence-pipeline/
│       ├── SKILL.md
│       ├── agents/
│       │   └── openai.yaml
│       └── references/
│           ├── terminology.md
│           ├── workflow.md
│           ├── core-rules.md
│           ├── source-hierarchy.md
│           ├── source-config.md
│           ├── deal-analysis-standard.md
│           ├── nicks-3-questions.md
│           ├── signal-taxonomy.md
│           ├── matching-rules.md
│           ├── verification-rules.md
│           ├── human-review-gates.md
│           ├── output-schemas.md
│           └── storage-rules.md
├── deal-records/
│   ├── drafts/
│   └── approved/
├── examples/
│   └── example-approved-deal.md
└── tests/
    ├── acceptance-criteria.md
    └── test-cases.md
```

## System Roles

- **Claude Skill / Project**: executes the phased workflow and enforces rules.
- **Git repo**: deal-intelligence brain and storage layer.
- **Notion DealStrategy**: strategic baseline for a deal.
- **Linked Deal**: commercial / historical context when available.
- **Notion Meeting Diary**: chronological meeting evidence.
- **Transcripts / Google Drive**: review all in-scope allowlisted evidence; summaries do not substitute for original content.
- **Existing Hyly Wiki Git context**: account and deal context already stored in the Wiki.
- **Human reviewer**: approves sources, facts, Nick's answers, candidate signals, verification, storage, and current-deal matches.
- **5-Minute Read V2**: consumes only approved current-deal information and approved relevant closed-deal patterns.

## Workflow

`Phase 0 Deal Intake -> Phase 1 Source Collection -> Phase 2 Deal Context Analysis -> Phase 3 Nick's 3 Questions -> Phase 4 Signal Extraction -> Phase 5 Verification / Critic -> Phase 6 Git Storage -> Phase 7 Current-Deal Matching -> Phase 8 5-Minute Read Input`

Every phase ends in a mandatory human review gate.

## Routines

- `routines/gspace-post.md`: a self-contained Claude routine. At 6 PM IST on weekdays it reads the Notion Meeting Diary for today's calls (Meeting Type contains "Sales", or blank with a deal linked), builds a 5-Minute Pre-Call View from the DealStrategy page and the latest Wiki Call Analysis block of the deal (falling back to Drive transcripts), and posts it to a Google Chat space as a card; if it cannot build a brief it posts the call name, Notion link and reason instead, and if there is no sales call it posts "No Sales call scheduled today." `routines/card_payload.py` is the readable card builder. It reads nothing else from this repo and does not need the Hyly Wiki repo. The Chat webhook is stored only in the live routine, never in this repo.
