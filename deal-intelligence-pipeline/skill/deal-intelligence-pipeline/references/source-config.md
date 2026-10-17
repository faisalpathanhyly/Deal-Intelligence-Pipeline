# Source Configuration

This file records the source locations already identified for the prototype. Use the connected tool available in the Claude environment. Do not assume a connector exists; if a source cannot be accessed, report it as inaccessible and request human help.

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

## Google Drive / Transcript Evidence

Use transcript evidence only when:
- structured meeting notes are insufficient;
- an important fact is ambiguous;
- source summaries conflict;
- stakeholder reaction needs verification;
- exact wording materially affects the conclusion.

## Retrieval Failure Rule

If a configured source cannot be accessed:
1. identify the missing source;
2. explain which phase / conclusion it affects;
3. do not replace it with general knowledge;
4. mark the affected item `Needs Evidence` or `Unknown`;
5. ask the human to provide access, link, file, or clarification.
