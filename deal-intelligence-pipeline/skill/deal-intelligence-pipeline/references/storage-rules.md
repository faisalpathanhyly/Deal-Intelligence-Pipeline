# Git Storage Rules

## Purpose

Use Git as the deal-intelligence brain and durable storage layer for the prototype.

The repository must clearly separate unapproved analysis from trusted approved intelligence.

## Canonical Paths and Write Verification

Use only repository-defined `deal-records/drafts/` for unapproved artifacts, source ledgers, checkpoints, and evidence notes, and `deal-records/approved/` for Phase 6-approved records. Do not invent `outputs/`, alternate roots, or external checkpoint stores.

Before every write, verify the actual repository root and destination parent, normalize/resolve the full path (including symlink/junction targets), and confirm it remains inside the intended repository storage area. Validate a safe normalized deal filename; reject absolute or traversal-based input. Check for existing files and preserve unrelated content. Verify the configured storage parent exists; if absent or unverifiable, report the path blocker rather than silently create an alternative layout. No generated deal files before `APPROVE PHASE 0`.

## Path Checks Before Reads and Matching

Verify actual repository root and referenced file/directory paths before reading, matching, or storing as well as before writing. A documentation mention is not proof of existence. Report missing configured paths and do not silently substitute or invent `final/`, `completed/`, `approved-output/`, `analysis/`, `outputs/`, or another location. New records may use a new safe filename only within a verified existing draft/approved parent, with the required approval state.

README, SKILL, references, tests, schemas, templates, and examples are methodology, not deal evidence. Verify library record provenance and Phase 5/6 approvals; an example file is not a trusted historical match merely because its path exists.

## Storage Areas

### Draft Records
Store unapproved work under:

`deal-records/drafts/`

Drafts may contain:
- source inventory;
- factual analysis awaiting review;
- unanswered Nick questions;
- candidate signals;
- verification notes;
- unresolved conflicts;
- pending questions.

A draft is never a trusted source for matching.

### Approved Records
Store human-approved deal intelligence under:

`deal-records/approved/`

Approved records may be used for:
- closed-deal pattern retrieval;
- current-deal matching;
- future 5-Minute Read inputs.

## Approval Boundary

Do not move or represent a record as approved until the human issues `APPROVE PHASE 6` for the presented record. Only signals verified and approved at Phase 5 may be represented as approved signals in it.

Do not silently copy candidate signals into the approved library.

## Record Naming

Use a stable deal-based filename.

Recommended pattern:

`<normalized-deal-name>.md`

Example pattern only:

`asset-living-halo.md`

Do not create a file for a deal until the deal identity has been confirmed in Phase 0.

## Record Contents

An approved record should include:
- Deal Context;
- Starting Position;
- Timeline;
- Nick's 3 approved answers;
- Decision Structure;
- Proof Needed;
- Technical Dependency;
- Commercial Dependency;
- Stall Reason;
- Outcome / Delta;
- Approved Signals;
- Evidence References;
- Confidence;
- intentionally unresolved Unknowns.

## Evidence Traceability

Every major approved claim should retain a reference to the source that supports it.

Do not store unsupported paraphrases without evidence reference when a source is available.

## Current Prototype vs Hyly Wiki Production Repo

This prototype repo is the working deal-intelligence store for developing and testing the methodology.

The team does not currently own the Hyly Wiki repo. Requirements for production incorporation into Hyly Wiki are expected to be handed to the appropriate owner for incorporation rather than assuming this prototype can directly change that production repository.
