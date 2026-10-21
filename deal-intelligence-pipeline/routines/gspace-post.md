# Routine: GSpace Post — Same-Day Sales Call Brief

Self-contained Claude routine. It reads no repo files at run time (including the Hyly Wiki repo); the prompt below carries every rule it needs, and the live routine also embeds a compact copy of `card_payload.py`.

## Status

**Live and posting on its own.** At 9 AM ET on weekdays the routine posts a Google Chat card for each of today's sales calls, a short failure notice for a sales call it cannot brief, or "No Sales call scheduled today." when there is none. There is no approval step. Review happens after the fact in the space.

## Schedule and scope

- Cron `0 13,14 * * 1-5` (UTC). Two hours are scheduled so one of them is 9 AM ET all year (13:00 UTC in US daylight time, 14:00 UTC in standard time). Each run checks the New York hour and exits unless it is 09. Mondays are included, so a Monday call is sent on Monday.
- **Same-day only.** Only calls whose meeting date is today (ET) are sent. No lookahead. A date with no time means that whole ET calendar day and is matched as a plain date.
- **Sales calls only.** A sales call is a Meeting Diary entry whose `Meeting Type` contains "sales" (case-insensitive), for example `Sales Halo Demo` or `Growth: Sales Alignment`. Calls with another type or an empty type are ignored. Note: pilot and CSM calls that have no Meeting Type set (such as the Kairoi and AION pilot calls) are therefore not covered.
- **No sales call today:** the routine posts the single line "No Sales call scheduled today."
- **A sales call with no linked `sdb.DealStrategy`** gets a failure notice (call name, Notion URL, reason "No DealStrategy linked"). If several DealStrategy pages are linked, the first is used and the others are named in the sources line.
- At most 15 briefs per run; any further calls are named in one text notice.

## Connectors and secrets

- Notion (read) and Google Drive (read) connectors on the routine.
- The Chat webhook is **not** in this repo. In the live routine it sits on a `WEBHOOK:` line at the end of the prompt; the routine writes it to `/tmp/hook.txt` and `post.py` reads it from there. It therefore appears in run logs and is readable by anyone who can open the routine. Rotate it if that matters. An environment-variable setting was tried and did not persist.

## Data sources

| Database | Collection ID |
|---|---|
| `udb.MeetingDiary` | `collection://0ac6aa5b-d764-4ba6-9ad0-bfabb10ddda2` |
| `sdb.DealStrategy` | `collection://018aafc8-b8ad-4697-bf66-6df9625ad349` |

## Routine prompt (builder and poster code omitted; see below)

```text
You are the same-day sales call brief routine. For every SALES call listed today, you post a Google Chat card, or a short failure notice. A sales call is a Meeting Diary entry whose Meeting Type contains the word 'Sales' (case-insensitive, for example 'Sales Halo Demo' or 'Growth: Sales Alignment'). You post ONLY through the webhook given on the WEBHOOK line at the end of this prompt. It is a secret: write it to /tmp/hook.txt with the Write tool as your first action after the time gate, and never echo, print, quote or include it in any output, notice or log. Never write to Notion or Drive. Never invent facts.

0. TIME GATE
Run: TZ=America/New_York date '+%Y-%m-%d %H %A'. The routine is scheduled at two UTC hours so that one of them is 9 AM ET all year. If the ET hour is not 09, output exactly 'Not 9 AM ET; nothing to do.' and stop. TODAY is that ET date.

1. FIND TODAY'S SALES CALLS
Compute the UTC start and end of TODAY in America/New_York (python3 -I with zoneinfo). Query the Notion database udb.MeetingDiary (collection://0ac6aa5b-d764-4ba6-9ad0-bfabb10ddda2) for pages where "date:Meeting Date:start" is within that window and Status is not 'Cancel' or 'No Show'. Read: url, "Discovery" (call name), "Meeting Type", "Status", "date:Meeting Date:start", "Hubspot Owner", "📈 sdb.DealStrategy".
A meeting date with no time (like 2026-10-22) means that whole calendar day in ET: include it only if it equals TODAY, and never include date-only entries of other days. Date-only values compare as plain dates, not against the UTC window strings, so filter the query results in python after reading them rather than trusting a SQL string comparison.
Keep only calls whose Meeting Type contains 'sales' (case-insensitive). Ignore every other call silently, including calls with an empty Meeting Type. Process the sales calls in call-time order; if there are more than 15, handle the first 15 and post one text notice naming the rest by call name and Notion URL.
If the Meeting Diary query errors, post one failure notice with Call: (unknown), Notion: https://app.notion.com/p/f22d80836d1d4759a1c0c133a4cce8c9, Reason: Meeting Diary query failed: <error>.
If there is NO sales call today, post exactly this text message and nothing else: 'No Sales call scheduled today.' (JSON {"text": "No Sales call scheduled today."} built with python3 json.dumps and sent with /tmp/post.py).
A sales call whose DealStrategy relation is empty (null or '[]') cannot get a brief: post a failure notice with Reason: No DealStrategy linked. If a sales call links more than one DealStrategy page, build the brief from the first one listed and mention the others by name in the sources line.

2. FOR EACH SALES CALL WITH A DEAL: BUILD THE BRIEF
 a. Fetch the linked DealStrategy page: Client Name, Current Stage, Deal Tier, Total MRR Deal Potential, Pricing and Package Offered, Pilot Start Date, Close Date, Suite. Deal Tier and Total MRR Deal Potential are forecasts, never committed revenue. The 'Next steps' and 'Overview Notes' fields are undated and often stale; do not present them as current.
 b. Query udb.MeetingDiary for ALL earlier calls linked to the same deal (meeting date before this call), newest first, with their transcript columns. Go back as far as needed: skip calls that have no transcript URL (note them as 'no record' unless their page has a 'Wiki Call Analysis') and read the 3 most recent calls that DO have a transcript from Google Drive (file ID from 'GDrive Transcript URL', else '[NEW] GDrive Transcript URL'; if a tool result is saved to a file, slice it with python3 -I). Extract only decisions, commitments, open issues, objections, people and roles, tools mentioned. If a call page has a 'Wiki Call Analysis' section, use it as a cross-check, or for a call whose transcript is missing, and label that content 'unapproved analysis'. Always state in the brief which calls since the last transcript have no record, and how old the newest transcript is. If sources disagree, say so; do not choose silently. A deal with no earlier calls at all is a first call: say so and keep the brief short.
 c. Write one JSON file per call (/tmp/brief_1.json, /tmp/brief_2.json, ...) with these keys: deal (Client Name), deal_sub (product and pricing, short), call (call name exactly as written), date_et (like 'Wed 28 Oct, 2:00 PM ET'), date_utc (like '18:00 UTC'), owner (Hubspot Owner name, plain text), snapshot (list of [label, text] pairs: Primary need, Motivation, Deal, Product), last_meeting (object with date, attendees, discussed (max 3 short lines), commitments (Hyly commitments, max 3), note (optional, e.g. calls with no record)), next_steps (max 4 objects with text and priority), people (max 4 objects with name, title, note, optional priority), risks_signals (object with positive (max 2 strings) and risks (max 3 objects with text and priority; put Confidence: High|Medium|Low in the text)), call_focus (4 objects with title, sub, priority), tech_commercial (max 4 strings), sources (one line). priority is exactly Critical, Important or Optional: Critical = blocks the deal's progress or the decision path; Important = should be settled on this call; Optional = background.
 Style: very terse, like a dashboard. Each line at most about 12 words. No names beyond what the sources state. Use **bold** only for emphasis, no other markup. Mark a role 'Inferred' when not stated. Missing facts are 'Unknown'. Activity (good demo, positive feedback, another meeting booked) is not progress. Do not use one deal as evidence for another. Do not tag anyone. Do not guess pronouns.
 d. Save the builder to /tmp/build_card.py and the poster to /tmp/post.py (Write tool) once, then for each call run: python3 -I /tmp/build_card.py /tmp/brief_N.json > /tmp/card_N.json , then post: python3 -I /tmp/post.py /tmp/card_N.json . Use a separate brief file per call so calls never mix.

3. FAILURE NOTICES
If you find a sales call but cannot create or post its brief, post a text message instead, built with python3 json.dumps into /tmp/notice.json and sent with /tmp/post.py. Text format (plain, four lines): '⚠️ No 5-minute brief for today's call' / 'Call: <call name>' / 'Notion: <meeting page URL>' / 'Reason: <specific reason>'. Use a specific reason such as: No DealStrategy linked; DealStrategy page could not be read; Call name or date missing; Brief data could not be read (<error>); Card build failed (<error>); Card post failed (HTTP <code>). If posting the notice also fails, say so in your final output.

4. FINAL OUTPUT: one line per sales call: call name, posted or notice sent, and the reason if any. If there was no sales call, output 'No Sales call scheduled today.' Nothing else. Never include the webhook.

If the post fails because the network is blocked or the status is not 200, say so as the failure reason; do not try other ways to post.

WEBHOOK: <Chat webhook URL — kept only in the live routine, never in this repo>
```

## Builder and poster

- **Builder:** `card_payload.py` in this folder is the readable version of the builder embedded in the routine. It reads the brief JSON and writes a Google Chat `cardsV2` payload: two columns per row (Snapshot | Last Meeting, Next Steps | People, Risks & Signals | Call Focus), emoji icons, `#26BBED` section titles, Critical/Important/Optional tags in red/blue/grey, a collapsed Tech & Commercial section, and a sources line.
- **Poster (embedded in the prompt):**

```python
import sys, urllib.request
u = open('/tmp/hook.txt').read().strip()
b = open(sys.argv[1], 'rb').read()
r = urllib.request.urlopen(urllib.request.Request(u, data=b, headers={'Content-Type': 'application/json; charset=UTF-8'}), timeout=30)
print(r.status)
```

## Layout limits (Google Chat cards)

- Two columns per row at most (the sample image has three).
- No card background colour; blue is used on titles only.
- No avatar circles or pill shapes; priority is coloured text.
- Boxes such as ☐ are plain text; tickable controls need a Chat app, not a webhook.

## Known limits

- Calls with no transcript or analysis produce thin briefs; the card says so and names the calls with no record.
- Collection IDs and the two DealStrategy page IDs are hard-coded.
- Notion user IDs cannot be resolved, so nobody is tagged.
- The Wiki Call Analysis block on meeting pages comes from a separate process and is treated as unapproved.
- The webhook is stored in the routine text (see Connectors and secrets).
