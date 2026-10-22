# Source Configuration

This file records the source locations already identified for the prototype. Use the connected tool available in the Claude environment. Do not assume a connector exists; if a source cannot be accessed, report it as inaccessible and request human help.

## Source Allowlist and Authorization

The baseline allowlist consists of the configured Notion DealStrategy, Deals, and Meeting Diary sources; deal-scoped Notion pages/databases in the checklist below; existing Hyly Wiki Git context; and linked CMD, Zoom, or Google Drive transcripts, summaries, recordings, and attachments for those deal sources. Checklist names describe allowed families, not invented IDs or authority to access unrelated systems. Before opening a link, confirm its provider/family and deal scope are allowlisted and authorized. Unknown external providers and other unlisted source types require explicit human approval before access or use.

HubSpot and all other CRM providers are NOT baseline-allowlisted. Their checklist row applies only after the human explicitly approves that named provider and deal scope. Do not query them merely because a connector, association, or link exists. Record each additional source approval, scope, and human wording in the ledger; source approval does not approve a phase. Pending authorization is Not Retrieved with reason Awaiting Source Approval, not Inaccessible or a missing deal fact. Ask for source authorization after Phase 0; never add secondary intake questions.

External spreadsheets are not automatically authorized by a page link. Only deal-scoped Google Drive artifacts explicitly covered by the baseline allowlist below may be opened without additional source approval; Salesforce, other CRM systems, other spreadsheet providers, unrelated repositories, and all unlisted systems remain opt-in. State the unapproved provider and proposed scope, ask whether to add it, and do not use its content before approval. Methodology/example files in this repository are not deal evidence.

## Notion — DealStrategy

Known data source:

`collection://018aafc8-b8ad-4697-bf66-6df9625ad349`

Use to locate records such as:

`Asset Living.Halo.DS`

Primary purpose:
- strategic objective;
- current stage;
- deal drivers;
- risks;
- relationship context;
- next steps;
- linked Deal / meetings where present.

## Notion — Deals

Known data source:

`collection://69301d72-5cef-49a0-82b5-a5b9f0046446`

Primary purpose:
- linked commercial deal;
- historical stage / outcome;
- close / booking information;
- pricing / MRR when present;
- account-level vs property-level deal context.

## Notion — Meeting Diary

Known data source:

`collection://0ac6aa5b-d764-4ba6-9ad0-bfabb10ddda2`

Primary purpose:
- chronological meeting history;
- pre-meeting context;
- meeting outcomes;
- later follow-up evidence;
- links to transcript / source material where present.

## Existing Hyly Wiki Git Context

Use the existing client / deal knowledge structure available to the user or connected repository.

Known conceptual structure from the current workflow includes:
- `raw/` — raw meeting evidence / transcript material;
- `meetings/` — structured meeting summaries;
- `overview.md` — accumulated account history;
- `brief.md` — current condensed Command Center brief;
- contacts — people / roles / relationship context;
- themes — recurring needs, objections, pain points, feature requests.

Do not assume an exact file exists until it is found in the repository.

## Transcripts and Recordings

Retrieve every in-scope CMD, Zoom, Google Drive, and other linked transcript; review every in-scope recording through available authorized media tools. Read complete content rather than summaries or search snippets. Track transcript, audio, and video review separately. Unsupported media capabilities must be disclosed as blockers under `source-hierarchy.md`.

## CRM, Linked Databases, and Other Artifacts

Only after explicit human approval of HubSpot and the deal scope, query its deal and contact records. For baseline-allowlisted Notion sources, query KYC SRT and Solution Question database entries, and other linked databases directly. Follow linked MSA, Data Tap Deals, Client Adoption, Outreach Calendar, Bugs and Feature Requests, strategy, kickoff, persona, insights, decision-making, gaps, and signals records. These names are discovery examples, not assumed collection IDs or proof that an integration exists. Resolve actual IDs and associations through authorized tools; do not invent source locations or designate source-of-truth precedence without supporting configuration. Surface contradictory commercial dates with provenance for human review.

## Required Source-Family Discovery Checklist

For every deal, investigate each family below using actual links, configured sources, and authorized account/product/deal searches. Read every in-scope item found, not a representative sample. The reference deal illustrates source families, not mandatory account-specific titles, dates, row counts, or collection IDs. These families are a minimum discovery checklist, not a limit on following additional in-scope evidence.

| Source Family | Discover and Review |
|---|---|
| Deal and strategy pages | DealStrategy, linked commercial deals, CSM/relationship strategy, partnership strategy, strategy goals/SMART goals, and decision-making pages. |
| Deal databases | Gate QA/KYC/SRT and Solution Questions, Client Adoption, Outreach Calendar, Halo Gaps, Signals, Feature Requests, PM Bugs, and relevant related entries across all result pages. |
| Insight and persona pages | Account insights, Halo Persona and related analysis, dashboards, ownership briefs, and every in-scope attachment or embedded file. |
| CMD transcripts and summaries | Every meeting summary and its corresponding full transcript, including discovery, demo, pilot, launch, kickoff, training, check-in, and commercial/legal discussions where present. Read both artifacts; reconcile disagreements. |
| Call-analysis pages | All account/deal call-analysis pages and their linked evidence. Treat generated analysis as interpretation until checked against primary meeting/transcript evidence. |
| Meeting and recording records | Meeting Diary, discovery/demo records, Zoom metadata, transcripts, and recordings, with separate actual-content and metadata coverage. |
| Onboarding and commercial artifacts | Kickoff decks, linked spreadsheets/live-feature lists, approval records, MRR/commercial boards, MSA records, Data Tap records, and their underlying evidence. |
| Connected CRM (opt-in only) | Only after explicit human approval of provider and deal scope: HubSpot parent and associated property deals, company/contact records, line items, and relevant associations. Verify account/product/deal identity; do not assume every associated record describes this deal. |
| Existing Wiki and additional links | Existing account/deal Git context and any other in-scope links discovered during retrieval. |

Search for unlinked family records as well as following links; record source locations, queries/filters, pagination, result counts, and inspected IDs in the Phase 1 ledger. A failed name search is not proof that a family or artifact does not exist. Complete available linked-ID resolution and authorized alternate searches before requesting a missing link. Do not query unrelated accounts merely to expand source coverage.

If an artifact has no transcript, a page is blank, or a search finds no matching record, report exactly that evidence with search scope or inspected location. Do not invent the artifact or equate missing transcript with reviewed recording. A deck, insight page, or persona page is not fully reviewed while its in-scope attachments, spreadsheets, dashboards, or approval links remain unread. Record each child artifact separately. Verify retained source IDs and evidence locations before claiming that material was read in an earlier session; otherwise retrieve it again.

## Relation and Rollup Retrieval

The configured collections are starting points. Follow relevant linked records discovered in their properties and bodies, including Relationship Density, MSA, Data Tap Deals, and meeting links when present. Resolve rollups to underlying records and retrieve relevant content using available authorized tools. Do not assume these names identify configured collections or invent their IDs. Apply traversal and coverage rules in `source-hierarchy.md`.

## Retrieval Failure Rule

If a configured source cannot be accessed:
1. identify the missing source;
2. explain which phase / conclusion it affects;
3. do not replace it with general knowledge;
4. mark the affected item `Needs Evidence` or `Unknown`;
5. ask the human to provide access, link, file, or clarification.
