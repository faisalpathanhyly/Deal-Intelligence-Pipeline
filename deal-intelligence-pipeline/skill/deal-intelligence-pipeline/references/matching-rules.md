# Current-Deal Matching Rules

## Purpose

Compare a current deal we are trying to close with the approved closed-deal intelligence library.

The goal is not to predict that the current deal will behave exactly like a closed deal.

The goal is to identify which approved historical patterns may be relevant, what needs validation, and what missing information should be asked for.

## Rule 1 — Stage Matching Is Not Mandatory

Do not require the current deal and closed deal to share the same stage.

Stage is supporting context only.

A different-stage closed deal may still be relevant when the underlying conditions match.

## Rule 2 — Match on Meaningful Conditions

Possible matching dimensions include:
- product;
- requirement;
- stakeholder situation;
- decision structure;
- proof needed;
- technical dependency;
- commercial dependency;
- adoption context;
- risk / blocker;
- progression pattern;
- stage, when useful.

Do not treat product alone or stage alone as sufficient.

## Rule 3 — Explain Why the Match Exists

Every proposed match must include a specific basis.

Good:

`Both deals show an unresolved reporting-proof requirement and unclear expansion decision ownership.`

Weak:

`Both are Halo deals.`

## Rule 4 — Missing Required Detail Stops the Match

If a material current-deal fact is needed to validate the match and is not available:

1. do not force the match;
2. label the item `No Valid Match Yet` or `Needs Current-Deal Detail`;
3. surface the exact pending question;
4. explain why the answer matters.

Example:

`Pending Question: Who owns final expansion approval? This is required to validate the stakeholder-pattern match.`

## Rule 5 — Suggest a Better Closed Deal When Appropriate

If the proposed historical deal does not have enough relevant overlap, but another approved closed deal better matches the current known context:

- suggest the alternative closed deal;
- explain the stronger overlap;
- do not fabricate missing details to preserve the original match.

## Rule 6 — Closed Deals Guide Investigation, Not Current Facts

Closed-deal intelligence may tell the system:
- what to look for;
- what to validate;
- what risk may be worth checking;
- what proof may matter;
- what question to ask.

It may not be used to state a current-deal fact unless current-deal evidence independently supports that fact.

## Rule 7 — Match Confidence

Assign:
- High: multiple meaningful conditions align and current-deal evidence is clear.
- Medium: some meaningful alignment exists but context is incomplete.
- Low: similarity is shallow or depends on important missing facts.

Low-confidence matches should normally remain unapproved and should trigger clarification rather than 5-Minute Read use.

## Rule 8 — Human Approval Is Required

No proposed match may influence the 5-Minute Read until a human approves its relevance.
