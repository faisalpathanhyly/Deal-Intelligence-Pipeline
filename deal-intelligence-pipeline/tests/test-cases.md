# Test Cases

## Test 1 — Missing Decision-Maker

### Input Condition
Current deal contains product, proof requirement, and technical context, but no final decision owner.

### Expected Behavior
- Do not infer a decision-maker from title or from a closed deal.
- Return a Pending Question asking who owns the final decision.
- If decision ownership is required for the proposed match, return No Valid Match Yet for that match.

### Failure
System names a likely decision-maker without evidence.

---

## Test 2 — Different Stage, Strong Signal Match

### Input Condition
Closed deal is Retain. Current deal is In Pilot. Both show a documented internal BI environment and the same proof requirement.

### Expected Behavior
- Do not reject the comparison just because stages differ.
- Explain the relevant shared conditions.
- Include stage as context, not as a mandatory filter.

### Failure
System refuses to compare because stages are different.

---

## Test 3 — Same Product, Weak Match

### Input Condition
Both deals use Halo, but no meaningful overlap in stakeholders, proof, technical condition, commercial condition, adoption, blocker, or progression pattern.

### Expected Behavior
- Do not call this a valid match.
- Explain that product alone is insufficient.

### Failure
System matches the deals only because both are Halo.

---

## Test 4 — Another Closed Deal Is Better

### Input Condition
Proposed closed deal lacks the relevant stakeholder and technical context. Another approved closed deal matches the known current-deal details more closely.

### Expected Behavior
- Do not force the original comparison.
- Suggest the better closed deal.
- Explain why it has stronger overlap.

### Failure
System invents missing details to preserve the original match.

---

## Test 5 — Positive Meeting Without Outcome

### Input Condition
Meeting notes say the client liked the demo. No later commitment, decision, stage movement, rollout action, or measurable next step is documented.

### Expected Behavior
- Do not answer Q1 with `the demo moved the deal`.
- Return Unknown or Needs Evidence for movement.

### Failure
System treats positive feedback as proven progression.

---

## Test 6 — Source Conflict

### Input Condition
DealStrategy identifies Person A as decision-maker. A later meeting says Person B now owns approval.

### Expected Behavior
- Surface the conflict.
- Note that the later source may represent a stakeholder change.
- Ask for human review if the distinction affects analysis.

### Failure
System silently chooses one source.

---

## Test 7 — Signal Context Changes Meaning

### Input Condition
Two closed deals both have internal BI. In one it acts as a competitor; in the other it is an integration opportunity.

### Expected Behavior
- Store two context-specific signals.
- Do not create universal rule `internal BI = risk`.

### Failure
System collapses both into the same generic rule.

---

## Test 8 — Human Gate Enforcement

### Input Condition
Phase 2 output has been generated but not approved.

### Expected Behavior
- Stop.
- Do not answer Nick's 3 questions yet.

### Failure
System continues automatically into Phase 3.
