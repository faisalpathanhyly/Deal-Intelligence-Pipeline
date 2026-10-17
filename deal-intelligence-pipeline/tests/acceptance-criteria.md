# Acceptance Criteria

The prototype passes only if it consistently follows all criteria below.

## Workflow
- Runs one phase at a time.
- Stops after every phase for human review.
- Does not skip directly from raw evidence to signals.
- Does not write approved knowledge before approval.

## Evidence Discipline
- Does not invent missing facts.
- Marks unsupported claims Unknown or Needs Evidence.
- Surfaces source conflicts.
- Uses later-outcome evidence when claiming what moved a deal.
- Does not treat positive activity alone as progression.

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

## Signals
- Uses only approved taxonomy categories.
- Preserves original deal context and impact.
- Separates candidate signals from approved signals.
- Assigns confidence.
- Requires verification before reuse.

## Human Review
- Provides clear review actions.
- Does not continue without explicit approval.
