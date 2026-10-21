"""Build a Google Chat card (cardsV2) in the grid layout from one brief object
produced by the gspace-post routine.

Usage: python3 -I card_payload.py brief.json > card.json
It sends nothing and holds no secrets.

Input keys: deal, deal_sub, call, date_et, date_utc, owner,
  snapshot [[label, text]], last_meeting {date, attendees, discussed[],
  commitments[], note?}, next_steps [{text, priority}], people [{name, title,
  note, priority?}], risks_signals {positive[], risks [{text, priority}]},
  call_focus [{title, sub, priority}], tech_commercial [str], sources str.
priority is Critical, Important or Optional.
"""
import html
import json
import re
import sys

COL = {"Critical": "#C62828", "Important": "#3949AB", "Optional": "#757575"}
BLUE = "#26BBED"


def esc(s):
    # Escape first, then turn **bold** into the one tag Chat cards need.
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(s, quote=False))


def fnt(color, text):
    return f'<font color="{color}">{text}</font>'


def pill(p):
    return " " + fnt(COL[p], f"<b>[{p}]</b>") if p in COL else ""


def box(icon, title, lines, tag=""):
    head = fnt(BLUE, f"<b>{icon} {esc(title)}</b>") + pill(tag)
    return {"textParagraph": {"text": head + "<br>" + "<br>".join(lines)}}


def col(widget):
    return {"horizontalSizeStyle": "FILL_AVAILABLE_SPACE", "horizontalAlignment": "START",
            "verticalAlignment": "TOP", "widgets": [widget]}


def row(a, b):
    return {"columns": {"columnItems": [col(a), col(b)]}}


def bul(items):
    return ["• " + esc(i) for i in items]


def build(m):
    for key in ("deal", "call", "date_et", "date_utc", "owner"):
        if not m.get(key):
            raise ValueError("missing field: " + key)
    snap = box("📄", "Snapshot", [f"<b>{esc(k)}:</b> {esc(v)}" for k, v in m["snapshot"]], "Important")
    lm = m["last_meeting"]
    last = box("📅", "Last Meeting - " + lm["date"],
               [f"<b>Attendees:</b> {esc(lm['attendees'])}", "<b>Discussed:</b>"] + bul(lm["discussed"])
               + ["<b>Hyly commitments:</b>" + pill("Important")] + bul(lm["commitments"])
               + ([f"<i>{esc(lm['note'])}</i>"] if lm.get("note") else []))
    steps = box("✅", "Next Steps", ["☐ " + esc(x["text"]) + pill(x["priority"]) for x in m["next_steps"]])
    people = box("👥", "People", [f"<b>{esc(p['name'])}</b>{pill(p.get('priority', ''))}<br>{esc(p['title'])}. "
                                  f"<i>{esc(p['note'])}</i>" for p in m["people"]])
    rs = m["risks_signals"]
    risks = box("📊", "Risks & Signals",
                [fnt("#2E7D32", "<b>↗ Positive Signals</b>")] + bul(rs["positive"])
                + [fnt("#C62828", "<b>▲ Risks</b>")]
                + ["• " + esc(r["text"]) + pill(r["priority"]) for r in rs["risks"]])
    focus = box("🎯", "Call Focus", [f"<b>{i}. {esc(f['title'])}</b>{pill(f['priority'])}<br><i>{esc(f['sub'])}</i>"
                                      for i, f in enumerate(m["call_focus"], 1)])
    top = {"widgets": [row(
        {"textParagraph": {"text": fnt(BLUE, f"<b>🏢 {esc(m['deal'])}</b>") + "<br>" + esc(m["deal_sub"])}},
        {"textParagraph": {"text": fnt(BLUE, f"<b>🕑 {esc(m['date_et'])}</b>")
                           + f"<br>{m['date_utc']} | Owner: {esc(m['owner'])}"}})]}
    grid = {"widgets": [row(snap, last), {"divider": {}}, row(steps, people), {"divider": {}}, row(risks, focus)]}
    tech = {"header": "🗂 Tech & Commercial (optional)", "collapsible": True, "uncollapsibleWidgetsCount": 0,
            "widgets": [{"textParagraph": {"text": "<br>".join(bul(m["tech_commercial"]))}}]}
    src = {"widgets": [{"textParagraph": {"text": f"<i>{esc(m['sources'])}</i>"}}]}
    card_id = re.sub(r"[^a-z0-9]+", "-", m["call"].lower()).strip("-")[:60]
    return {"cardsV2": [{"cardId": card_id, "card": {
        "header": {"title": "5-Minute Pre-Call View - " + m["deal"], "subtitle": m["call"]},
        "sections": [top, grid, tech, src]}}]}


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        json.dump(build(json.load(f)), sys.stdout, ensure_ascii=False)
