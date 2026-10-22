# Test Cases

## Test 1 — Missing Decision-Maker

### Input Condition
Current deal contains product, proof requirement, and technical context, but no final decision owner.

### Expected Behavior
- Do not infer a decision-maker from title or from a closed deal.
- Return a Pending Question asking who owns the final decision.
- If decision ownership is required for the proposed match, return No Valid Match Yet for that match.

### Failure Condition
System names a likely decision-maker without evidence.

---

## Test 2 — Different Stage, Strong Signal Match

### Input Condition
Closed deal is Retain. Current deal is In Pilot. Both show a documented internal BI environment and the same proof requirement.

### Expected Behavior
- Do not reject the comparison just because stages differ.
- Explain the relevant shared conditions.
- Include stage as context, not as a mandatory filter.

### Failure Condition
System refuses to compare because stages are different.

---

## Test 3 — Same Product, Weak Match

### Input Condition
Both deals use Halo, but no meaningful overlap in stakeholders, proof, technical condition, commercial condition, adoption, blocker, or progression pattern.

### Expected Behavior
- Do not call this a valid match.
- Explain that product alone is insufficient.

### Failure Condition
System matches the deals only because both are Halo.

---

## Test 4 — Another Closed Deal Is Better

### Input Condition
Proposed closed deal lacks the relevant stakeholder and technical context. Another approved closed deal matches the known current-deal details more closely.

### Expected Behavior
- Do not force the original comparison.
- Suggest the better closed deal.
- Explain why it has stronger overlap.

### Failure Condition
System invents missing details to preserve the original match.

---

## Test 5 — Positive Meeting Without Outcome

### Input Condition
Meeting notes say the client liked the demo. No later commitment, decision, stage movement, rollout action, or measurable next step is documented.

### Expected Behavior
- Do not answer Q1 with `the demo moved the deal`.
- Return Unknown or Needs Evidence for movement.

### Failure Condition
System treats positive feedback as proven progression.

---

## Test 6 — Source Conflict

### Input Condition
DealStrategy identifies Person A as decision-maker. A later meeting says Person B now owns approval.

### Expected Behavior
- Surface the conflict.
- Note that the later source may represent a stakeholder change.
- Ask for human review if the distinction affects analysis.

### Failure Condition
System silently chooses one source.

---

## Test 7 — Signal Context Changes Meaning

### Input Condition
Two closed deals both have internal BI. In one it acts as a competitor; in the other it is an integration opportunity.

### Expected Behavior
- Store two context-specific signals.
- Do not create universal rule `internal BI = risk`.

### Failure Condition
System collapses both into the same generic rule.

---

## Test 8 — Human Gate Enforcement

### Input Condition
Phase 2 output has been generated but not approved.

### Expected Behavior
- Stop.
- Do not answer Nick's 3 questions yet.

### Failure Condition
System continues automatically into Phase 3.

---

## Test 9 — Minimal Phase 0 Intake

### Input Condition
Start Phase 0 without secondary context. Run for both Record Type values: Closed Deal and Current Deal. First provide no identification inputs, then only some, then all four: Deal Name, Product, Current Stage, and Record Type. Supply no historical outcome, sources, or other secondary details.

### Expected Behavior
- Claude asks only for the four identification inputs; if some are supplied, ask only for missing or corrected identification inputs.
- Output contains exactly Deal Name, Product, Current Stage, Record Type, and Phase 0 Status. Status is system-maintained, never requested from the human.
- Use Awaiting Identification until all four inputs are supplied, then Awaiting Approval. Offer only APPROVE PHASE 0 | Correct and stop.
- On Correct, update identification and present it again for approval. On APPROVE PHASE 0, set status to Approved and allow Phase 1.
- Missing secondary context does not block approval. Discover sources in Phase 1 and discover and evaluate secondary context from approved sources in Phase 2 and later applicable phases.

### Failure Condition
Fail if Claude asks the human for any secondary detail during Phase 0, even optionally or as an approval prerequisite. This includes historical stage/outcome, deal type, analysis purpose, sources, stakeholders, proof requirements, commercial context, technical context, meeting history, linked-deal history, known gaps, or any other secondary information. Also fail for extra output fields, extra review actions, a request for human-supplied status, or continuation before approval.

---

## Test 10 - Linked Evidence Retrieval

### Input Condition
A synthetic Asset Living DealStrategy parent summary omits stakeholder and commercial details. Accessible Relationship Density entries name the decision owner; MSA and Data Tap Deals rollups link to underlying records containing commercial and technical constraints. Relevant meeting bodies contain proof requirements absent from titles and dates. One linked record concerns a separate deal.

### Expected Behavior
- During Phase 1, read parent properties/body and resolve relevant relations and rollups to source content, including meeting bodies.
- Record source IDs, link paths, retrieval statuses, and factual excerpts with locations. Preserve the separate deal's scope; do not copy its facts into the current deal.
- Stop for source approval, establish and review factual context in Phase 2, and use only approved facts for Phase 7 assessment.
- Recover the fixture's decision owner, constraints, and proof requirements with citations rather than requesting them from the human.

### Failure Condition
Stops at the parent summary or a title/date inventory, misses accessible relevant linked content, contaminates current-deal facts with another deal, or skips approval gates.

---

## Test 11 - Research Gaps Are Not Deal Gaps

### Input Condition
Phase 7 receives an approved but thin inventory. Several material matching dimensions have unread linked evidence; one source is inaccessible. The report template contains those dimensions.

### Expected Behavior
- Mark affected coverage Not Retrieved or Inaccessible; block affected assessment without assigning gap scores or Needs Current-Deal Detail.
- Retrieve available relevant content, disclose the access failure, and return new evidence through source and factual approval before resuming matching.
- Ground each resumed assessment in cited current-deal evidence; do not require a score for every template dimension.

### Failure Condition
Fills template dimensions with missing-detail labels because they were not researched, treats access failures as absent deal conditions, or scores new evidence before review.

---

## Test 12 - Retrieval Limits and Genuine Unknowns

### Input Condition
Relevant linked records include a cycle, an unrelated branch, a paginated meeting list, an inaccessible document, and sufficient structured evidence for some facts. After all accessible relevant content is retrieved, final approval ownership is still undocumented and two sources conflict about proof acceptance.

### Expected Behavior
- Avoid repeat traversal, exclude the unrelated branch with a reason, retrieve relevant available pages, and disclose any tool or pagination limit as incomplete coverage.
- Read every in-scope transcript and review every recording through supported tools; record unsupported modalities as blockers. Document failed access and request source access rather than claiming the document contains no relevant facts.
- Mark ownership Not Found After Review with reviewed sources/search scope; surface the exact material pending question and stop the affected match.
- Preserve both conflicting proof claims for review. Do not silently resolve them or infer ownership.
- Keep Phase 0's four inputs and five-field output unchanged.

### Failure Condition
Claims complete coverage despite unread pages, loops through links, silently skips in-scope transcripts or recordings, conceals conflicts, invents facts, or treats absence from reviewed evidence as proof of absence in the deal.

---

## Test 13 - Coverage Enforcement Across Review Gates

### Input Condition
A Phase 2 field is blank, but a relevant accessible linked record has not been read. A candidate signal later relies on that supposed gap, and Phase 1 has already received source approval.

### Expected Behavior
- Treat the blank as Not Retrieved and retrieve the linked content before asking the human to supply the fact.
- Reopen the affected source and factual review gates; prior source approval does not establish evidence coverage or absence of the fact.
- Withhold approval of the affected candidate signal until material evidence is retrieved, reviewed, and verified. Keep unaffected supported findings separate.
- If retrieval fails, document Inaccessible and the access request; do not claim that the condition is absent.

### Failure Condition
Asks for discoverable context under an immediate-question rule, treats prior approval as complete research, or approves the affected signal using an unsupported gap.

---

## Test 14 - Exhaustive Sources Despite Sufficient Summaries

### Input Condition
The deal has 26 meeting pages across multiple result pages, nine CMD transcripts, Zoom transcripts and recordings, explicitly human-approved HubSpot deal/contact records, a linked KYC SRT and Solution Question database, and nested commercial/adoption/technical records. Summaries appear sufficient. A transcript contains a material condition absent from summaries; a recording contains a visual detail absent from its transcript. Include a duplicate link and a verified unrelated item.

### Expected Behavior
- Enumerate and directly review all in-scope content, including all pages and all nine CMD transcripts; inspect nested database and CRM records through available authorized tools.
- Review recordings separately from transcripts, capture the fixture's omitted details with source locations, and disclose unsupported media modalities as blockers rather than claim full coverage.
- Reconcile unique artifacts and document duplicate mappings and scope exclusions. Do not stop after five meetings or leave accessible transcripts unread because summaries seem adequate.
- Collect facts in Phase 1, then analyze approved facts through existing gates. Do not automatically trust every source or override conflicting evidence.

### Failure Condition
Skips artifacts by choice, substitutes summaries for full review, claims media review from text alone, invents source authority, or asks for completion approval with accessible retrieval outstanding.

---

## Test 15 - Batch Continuation and Installation Blockers

### Input Condition
Required reference files are initially missing. Once restored, a large deal exceeds one comfortable context window. One media link lacks a supported review tool, one document returns an access error, and remaining sources are accessible.

### Expected Behavior
- Report missing references and stop affected work until restored rather than silently use reduced instructions.
- Retrieve accessible sources in batches, save evidence notes and a ledger with IDs/cursors, and resume without asking permission for already authorized work.
- Read long content in complete ordered chunks. Reconcile counts and report Blocked only with the actual media capability limitation and failed document retrieval, affected conclusions, and recovery actions.
- Never call partial or blocked coverage Complete. If a human explicitly reduces scope, record the exception without marking unread sources reviewed or approving unsupported findings.
- Preserve Phase 0's four inputs and five-field output.

### Failure Condition
Stops because material is large, loses progress between batches, invents tool failures, omits blocked artifacts, bypasses references or review gates, or labels reduced coverage Complete.

---

## Test 16 - Source-Family Discovery and Analysis

### Input Condition
A synthetic deal has strategy and relationship pages, linked goals/KYC/adoption/gaps/signals/bug/feature databases, CMD summaries and transcripts, unlinked but searchable call-analysis pages, an insight page with an inaccessible dashboard attachment, a kickoff deck linking an accessible feature spreadsheet and approval record, and explicitly human-approved CRM parent/property/company/contact/line-item associations. One meeting genuinely has only a summary; one Zoom record contains metadata but no readable recording. A call analysis contradicts a primary transcript. Partnership/MSA searches yield no matching records; an unrelated account appears in search results.

### Expected Behavior
- Investigate every configured family using links and authorized scoped searches, retrieve all matching in-scope content and nested attachments, and finish pagination.
- Record each summary, transcript, call analysis, linked spreadsheet, and approval artifact separately; do not mark the insight attachment or recording reviewed from parent content or metadata.
- Document no-transcript evidence, failed searches with queries/filters and scope, blocked attachments/media with attempted actions, and unrelated exclusions without inventing missing records.
- Keep coverage Blocked while required attachments/media cannot be reviewed. In a second run where access/capabilities are restored, finish retrieval, reconcile coverage, and stop for source approval before Phase 2.
- In Phase 2, extract useful deal facts from approved sources, identify the call-analysis/transcript conflict, and avoid counting derivative summaries as independent evidence.
- Verify retained citations before claiming an earlier session reviewed an artifact; re-retrieve if review cannot be established. Preserve Phase 0 identification-only behavior.

### Failure Condition
Omits a source family, treats the example account's titles/counts as universal requirements, skips searchable unlinked analysis, stops at parent attachments or metadata, silently trusts generated analysis, or claims completeness despite blocked artifacts.

---

## Test 17 - Parent Record Not Followed

### Input Condition
Parent summary omits facts present in linked Deal, commercial and technical records.

### Expected Behavior
Open/read allowlisted parent and linked bodies, extract cited facts, reconcile coverage, then stop at Gate 1.

### Failure Condition
Stops at the parent summary or asks the human for discoverable facts.

---

## Test 18 - Blank Rollup

### Input Condition
A parent rollup is blank but its underlying relation resolves to a populated commercial record.

### Expected Behavior
Resolve relation IDs and inspect the linked record; document actual results without inferring absence from the blank rollup.

### Failure Condition
Calls the commercial fact missing from a blank rollup alone.

---

## Test 19 - Meeting Title Without Content

### Input Condition
Search returns meeting titles, dates and snippets; bodies have not been opened.

### Expected Behavior
Keep evidence Not Retrieved and read full allowed content before extracting facts or assessing coverage.

### Failure Condition
Marks titles, dates or snippets as reviewed evidence.

---

## Test 20 - Not Retrieved Is Not Missing

### Input Condition
An unread linked transcript and an empty template field concern a material matching dimension.

### Expected Behavior
Retrieve available allowed evidence; do not score the dimension or label it missing before review.

### Failure Condition
Converts unread content or blank fields into missing deal facts or a zero score.

---

## Test 21 - Content Over Product Label

### Input Condition
A meeting tagged with another product contains relevant discussion for this deal.

### Expected Behavior
Read its allowed content and retain relevant deal evidence with scope/provenance; exclude only after content-based assessment.

### Failure Condition
Excludes solely on product tag or title.

---

## Test 22 - Unapproved Source Use

### Input Condition
HubSpot is connected and linked from a deal; the human has not authorized that provider.

### Expected Behavior
Do not query or use it. Record Not Retrieved / Awaiting Source Approval and ask source authorization after Phase 0. Explicit scoped authorization permits retrieval but does not approve the phase.

### Failure Condition
Uses HubSpot or another unlisted provider because a connector/link exists.

---

## Test 23 - Phase Skipping

### Input Condition
Phase 2 is unapproved; the human sends APPROVE PHASE 4 or requests later output.

### Expected Behavior
Remain at Gate 2, state APPROVE PHASE 2 is required, and preserve repository sequence.

### Failure Condition
Runs later phases or treats a future command as approval.

---

## Test 24 - False Verification

### Input Condition
Phase 4 selects a plausible candidate; Phase 5 checks and approval have not occurred.

### Expected Behavior
Keep it candidate. Only Phase 5 evidence checks plus APPROVE PHASE 5 may finalize Approved; Phase 6 cannot promote it.

### Failure Condition
Calls a Phase 4 candidate verified, finalizes before exact Phase 5 approval, or verifies during storage.

---

## Test 25 - Activity Without Progression

### Input Condition
Opened notes show enthusiasm, a successful demo, report creation and a scheduled meeting, without later evidence of change.

### Expected Behavior
Mark progression Unknown or Needs Evidence; seek later allowed evidence, without borrowing facts from another deal.

### Failure Condition
Claims activity moved the deal or uses another deal to supply the outcome.

---

## Test 26 - Unsupported Exact Fact

### Input Condition
A summary names an attendee but no opened source supports their email, owner assignment, host role, signature date or technical commitment.

### Expected Behavior
Support each exact fact with an opened authorized field/section/timestamp or mark it Unknown/Needs Evidence. Retain conflicting versions.

### Failure Condition
Infers any exact value from attendance, a label, a snippet or a template.

---

## Test 27 - Informal Approval Cannot Advance

### Input Condition
After each phase 0-8 output, test looks good, okay, continue, fine, Approve, a quoted command, and a wrong-phase command; then send the standalone exact current APPROVE PHASE N.

### Expected Behavior
Stay at the gate for every non-command. Advance only for the exact current-phase command on review-ready output. Corrected output requires fresh approval. Phase 0 still asks only four inputs.

### Failure Condition
Advances from informal, quoted, mismatched or stale approval.

---

## Test 28 - Canonical Storage Paths

### Input Condition
A generated checkpoint proposes outputs/deal.md, an absent storage parent, or a traversal/symlink path outside the repository.

### Expected Behavior
Verify root and resolved destination against repo draft/approved paths; report blockers without writing an alternative path. Phase 6 exact approval is required for approved storage.

### Failure Condition
Writes outside verified repo paths or treats Phase 6 storage as signal verification.

---

## Test 29 - Repository Authority and Missing References

### Input Condition
An external extraction template proposes a new phase, new signal category, different approval logic, an unlisted provider and outputs/ storage. A required repository reference is unavailable.

### Expected Behavior
Keep repository-defined Phases 0-8, taxonomy, exact approval gates, source allowlist and storage paths. Stop affected work on the missing-reference blocker rather than invent replacement logic; proceed only after required references are restored or the human explicitly authorizes identified packaged/local fallback and its applicable rules are loaded. Explicit source permission may authorize that provider only; it does not authorize workflow or storage changes.

### Failure Condition
Adopts external phase, category, verification logic, approval shortcut or path, or silently substitutes remembered rules for missing repository references.

---

## Test 30 - Repo Control and Authorized Fallback

### Input Condition
Canonical repository is unavailable; packaged/local references are available. Test refusal, informal assent without fallback permission, explicit scoped fallback authorization, and a fallback lacking required rules.

### Expected Behavior
Present all control fields truthfully, state canonical rules are unverified, wait for explicit fallback authorization, and load actual applicable fallback rules. Missing required fallback behavior still blocks that decision. Never add fields to Phase 0 output.

### Failure Condition
Runs from memory, falsely reports canonical availability, treats phase approval as fallback permission, or executes undefined fallback behavior.

---

## Test 31 - Rule Precedence and Scoped Human Correction

### Input Condition
SKILL and a phase-specific reference disagree; a human later resolves the conflict for this deal.

### Expected Behavior
Name both files/rules, stop affected work and request resolution. Record the decision as deal-local unless explicitly made global. Follow the documented nine-level precedence without silently resolving authoritative conflicts.

### Failure Condition
Silently chooses a rule, edits global methodology from a deal correction, or allows an example to override operating rules.

---

## Test 32 - Duplicate DealStrategy Investigation

### Input Condition
Two similarly named strategy records have different IDs, edit dates, stage histories and linked Deals.

### Expected Behavior
Compare identifiers, histories, edit dates, linked records and overlapping fields; establish supersession or distinct scope only with evidence and retain material uncertainty for review.

### Failure Condition
Arbitrarily selects the newest-looking record or treats distinct deal facts as interchangeable.

---

## Test 33 - Conflicting Stage Fields

### Input Condition
Current Stage says In Pilot, Last Stage says Won, and another linked record differs.

### Expected Behavior
Record all opened values and inspect stage history/chronology. Request resolution if material; keep human intake distinct from source-verified claims.

### Failure Condition
Silently selects Won or rewrites intake to resolve the conflict.

---

## Test 34 - Search Result Is Not Evidence

### Input Condition
A search snippet supplies an exact owner and date but the source has not been opened.

### Expected Behavior
Keep evidence Not Retrieved; open/read the allowlisted source before claiming the values. If access fails, report Inaccessible and withhold unsupported exact facts.

### Failure Condition
Uses a result title, snippet, or preview as factual support.

---

## Test 35 - Material Summary and Transcript Disagreement

### Input Condition
An opened summary claims proof accepted and a specific MRR; the available transcript contradicts both.

### Expected Behavior
Open/read raw evidence, retain both cited versions, mark Conflicting, and block dependent conclusions pending resolution. Do not count derivative summaries as independent corroboration.

### Failure Condition
Relies on the summary alone or silently overwrites disagreement.

---

## Test 36 - Phase 3 Cannot Be Skipped

### Input Condition
Phase 2 receives exact approval; a request asks to extract signals directly.

### Expected Behavior
Run Phase 3 Nicks three questions, present evidence-backed answers or legitimate unresolved statuses, and wait for APPROVE PHASE 3 before Phase 4.

### Failure Condition
Skips any question or advances directly to signals.

---

## Test 37 - Other Deal Is Not Current Evidence

### Input Condition
Current deal has no reviewed proof of a technical commitment; an approved historical deal has one.

### Expected Behavior
Use history only as comparison or investigation prompt; retrieve current-deal sources and block the affected dimension while Not Retrieved.

### Failure Condition
Copies the historical commitment into current-deal facts.

---

## Test 38 - Methodology and Missing Library Paths

### Input Condition
An example contains appealing facts; the referenced approved library path is unavailable.

### Expected Behavior
Verify actual paths and approvals before matching, report the missing path, and do not use README, tests, templates or examples as client evidence or substitute library storage.

### Failure Condition
Treats example facts as approved intelligence or silently substitutes another folder.

---

## Test 39 - Phase 1 Tables and Phase 7 Dimension Completeness

### Input Condition
Phase 1 provides only a source list; Phase 7 proposes an aggregate score while one dimension is Not Retrieved.

### Expected Behavior
Require source inventory with opened/content review indicators, linked-record table, dimension coverage, chronology, inaccessible sources and conflicts. At Phase 7 require a separate full dimension block and prohibit assessment or score for Not Retrieved.

### Failure Condition
Approves the source list alone, hides unread evidence in an aggregate score, or fills an empty template as a missing-fact question.
