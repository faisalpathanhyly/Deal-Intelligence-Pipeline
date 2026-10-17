# Git Storage Rules

## Purpose

Use Git as the deal-intelligence brain and durable storage layer for the prototype.

The repository must clearly separate unapproved analysis from trusted approved intelligence.

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

Do not move or represent a record as approved until the human explicitly approves Phase 6.

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
