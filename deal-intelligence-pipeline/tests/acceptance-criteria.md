# Acceptance Criteria

The prototype passes only if it consistently follows all criteria below.

## Workflow
- Runs one phase at a time.
- Stops after every phase for human review.
- Does not skip directly from raw evidence to signals.
- Does not write approved knowledge before approval.

## Phase 0 Identification Only
- Requests exactly Deal Name, Product, Current Stage, and Record Type (Closed Deal or Current Deal); asks only for missing or corrected identification inputs when others are supplied.
- Do not ask the human during Phase 0 for historical stage/outcome, deal type, analysis purpose, sources, stakeholders, proof requirements, commercial context, technical context, meeting history, linked-deal history, known gaps, or any other secondary information.
- Outputs only Deal Name, Product, Current Stage, Record Type, and system-maintained Phase 0 Status.
- Offers only APPROVE PHASE 0 | Correct and waits for explicit approval before Phase 1.
- Does not block approval for missing secondary context.
- Discovers and evaluates secondary context, missing information, conflicts, and unknowns from approved sources in later phases.
- Preserves this principle: One secondary purpose of the Deal Intelligence Pipeline is to discover important deal context, missing information, conflicts, and unknowns. Do not ask the human to pre-fill information that the system can reasonably discover from approved sources.
- Passes `Minimal Phase 0 Intake` in `test-cases.md`.

## Repository Authority, Approval, and Source Boundaries
- Uses repository Phases 0-8, source allowlist, taxonomy, verification logic, schemas, and storage paths without invention.
- Advances only after the presented current phase receives the standalone exact human command `APPROVE PHASE N`; informal assent, mismatched commands, and quoted commands do not advance.
- Does not query HubSpot or another opt-in/unlisted provider without explicit human source approval; source permission is separate from phase approval.
- Performs Find -> Open -> Read -> Follow linked records -> Extract evidence -> Confirm coverage, including underlying relations of blank rollups.
- Uses Retrieved, Not Retrieved, Inaccessible, Conflicting, and Not Found After Review; never treats unread or blank-template content as missing.
- Checks opened sources for exact names, emails, owners, dates, hosts, assignments, commercial, contract, and technical facts.
- Reads content before excluding a meeting by product/title label.
- Only Phase 5 plus `APPROVE PHASE 5` can promote a candidate signal; earlier selection and later storage cannot verify it.
- Uses verified repository draft/approved paths, never an invented `outputs/` location.

## Repository Controls and Evidence Boundaries
- Performs a Repo Control Check before every phase using actual verified paths; Phase 0 still has only four inputs and five output fields.
- When canonical rules cannot be verified, reports the limitation and waits for explicit packaged/local fallback authorization; loads actual fallback rules and records provenance/scope without improvising.
- Applies the exact precedence in SKILL.md; names both files/rules and stops affected decisions on authoritative conflicts. Deal corrections do not silently change global methodology.
- Investigates duplicate DealStrategy records and conflicting Current Stage/Last Stage using IDs, stage history, edit dates, linked records, and fields.
- Uses source inventory, linked-record and evidence-dimension tables at Gate 1; reviews inaccessible, conflicting, and Not Found After Review items as well as retrieved content.
- Never maps Not Retrieved or empty templates to Missing, Unknown, Needs Current-Deal Detail or Pending Question; asks only after approved searches/linked-record review leave a required fact unresolved.
- Checks raw/transcript support for exact numbers, attribution, wording, reactions, technical/commercial details, and major conclusions; surfaces material summary disagreement.
- Keeps methodology/examples/tests separate from factual deal evidence, verifies paths before reads/matching/writes, and reports missing paths without substitution.
- Gives each assessed Phase 7 dimension its own evidence, checked sources, status, historical signal, basis, confidence, and only eligible unresolved questions.

## Evidence Discipline
- Does not invent missing facts.
- Marks unsupported claims Unknown or Needs Evidence.
- Surfaces source conflicts.
- Uses later-outcome evidence when claiming what moved a deal.
- Does not treat positive activity alone as progression.

## Retrieval and Coverage
- Reads relevant source content in Phase 1 for current and closed deals without performing later-phase interpretation.
- Follows relevant relations, rollups, nested linked records, and meeting bodies; records source IDs, link paths, evidence locations, and retrieval statuses.
- Handles cycles, irrelevant branches, pagination, and access limits explicitly; preserves deal boundaries and reviews every in-scope transcript and recording.
- Distinguishes unread evidence, inaccessible evidence, conflicts, and facts not found after documented review.
- Does not score an unread dimension or label unfinished research as Needs Current-Deal Detail.
- Completes available relevant research before asking humans for discoverable context; maintains source and factual approval gates when reopening collection.
- Passes Linked Evidence Retrieval, Research Gaps Are Not Deal Gaps, and Retrieval Limits and Genuine Unknowns in `test-cases.md`.

## Closed vs Current Deal
- Uses `closed deal` for historical/completed deals.
- Uses `current deal` only for active deals we are trying to close.
- Treats approved closed deals as the source of truth for reusable historical intelligence.
- Does not copy a closed-deal fact into a current deal without current-deal evidence.

## Matching
- Does not require same stage.
- Does not use product or stage alone as a valid match.
- Explains why a proposed match is relevant.
- Stops a match when a required current-deal fact is missing.
- Surfaces a pending question instead of guessing.
- Can suggest another approved closed deal when it better fits the known context.

## Exhaustive Source Review
- Reviews all in-scope artifacts and their full accessible content, including transcripts, recordings, nested links, database results, and authorized CRM records.
- Summaries and excerpts do not replace primary-source review; text review is not claimed as audio/video review.
- Reconciles discovered artifacts against reviewed, partial, unread, blocked, and excluded counts, with concrete scope/duplicate reasons.
- Uses saved batch checkpoints and complete chunk coverage rather than sampling when material is large.
- Continues accessible retrieval without redundant permission requests; only Complete coverage is ready for normal Phase 1 completion approval.
- Reports concrete tool/access blockers and missing required skill references without fabricating capabilities or source authority.

## Source-Family Discovery
- Investigates every family in `source-config.md`, including CMD summaries/transcripts, call analyses, insight attachments, strategy/deal databases, onboarding links, and explicitly human-approved CRM associations.
- Documents unlinked-record searches, filters, pagination, and unsuccessful search scope; does not invent source IDs or account-specific records.
- Tracks child attachments and summary/transcript artifacts separately; unsupported media remains blocked.
- Analyzes approved evidence with primary-source provenance; generated analyses and repeated summaries are not independent factual proof.
- Passes `Source-Family Discovery and Analysis` in `test-cases.md`.

## Coverage Enforcement
- Does not let immediate-question rules bypass available source discovery.
- Gate 1 exposes retrieval readiness and questions blocked by incomplete coverage.
- Verification withholds approval from affected conclusions and signals when material evidence is unread or inaccessible.
- Does not treat source approval as proof that unresolved deal conditions are absent.

## Signals
- Uses only approved taxonomy categories.
- Preserves original deal context and impact.
- Separates candidate signals from approved signals.
- Assigns confidence.
- Requires verification before reuse.

## Human Review
- Provides clear review actions.
- Does not continue without explicit approval.
