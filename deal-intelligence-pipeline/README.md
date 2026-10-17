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
- **Transcripts / Google Drive**: deeper evidence when summaries are insufficient.
- **Existing Hyly Wiki Git context**: account and deal context already stored in the Wiki.
- **Human reviewer**: approves sources, facts, Nick's answers, candidate signals, verification, storage, and current-deal matches.
- **5-Minute Read V2**: consumes only approved current-deal information and approved relevant closed-deal patterns.

## Workflow

`Phase 0 Deal Intake -> Phase 1 Source Collection -> Phase 2 Deal Context Analysis -> Phase 3 Nick's 3 Questions -> Phase 4 Signal Extraction -> Phase 5 Verification / Critic -> Phase 6 Git Storage -> Phase 7 Current-Deal Matching -> Phase 8 5-Minute Read Input`

Every phase ends in a mandatory human review gate.
