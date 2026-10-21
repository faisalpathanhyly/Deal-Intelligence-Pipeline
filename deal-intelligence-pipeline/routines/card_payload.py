"""Build a Google Chat card (cardsV2) from one meeting object produced by the
gspace-post routine.

Reads one JSON object on stdin and writes the card payload to stdout. It does
not send anything and holds no secrets.

Input shape:
  {"deal": str, "call": str, "date_et": str, "date_utc": str, "owner": str,
   "sections": [{"title": str, "lines": [str, ...]}]}
"""
import html
import json
import re
import sys


def fmt(line):
    # Escape first, then turn **bold** into the one tag Chat cards need.
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(line, quote=False))


def section(title, lines):
    return {
        "header": title,
        "widgets": [{"textParagraph": {"text": "<br>".join(fmt(x) for x in lines)}}],
    }


def build(m):
    for key in ("deal", "call", "date_et", "date_utc", "owner", "sections"):
        if not m.get(key):
            raise ValueError("missing field: " + key)
    top = {
        "widgets": [
            {"decoratedText": {"topLabel": "Date", "text": f"{m['date_et']} ({m['date_utc']})"}},
            {"decoratedText": {"topLabel": "Call owner", "text": m["owner"]}},
            {"decoratedText": {"topLabel": "Deal", "text": m["deal"]}},
        ]
    }
    card_id = re.sub(r"[^a-z0-9]+", "-", m["call"].lower()).strip("-")[:60]
    return {
        "cardsV2": [
            {
                "cardId": card_id,
                "card": {
                    "header": {
                        "title": "5-Minute Pre-Call View - " + m["deal"],
                        "subtitle": m["call"],
                    },
                    "sections": [top] + [section(s["title"], s["lines"]) for s in m["sections"]],
                },
            }
        ]
    }


if __name__ == "__main__":
    json.dump(build(json.load(sys.stdin)), sys.stdout)
