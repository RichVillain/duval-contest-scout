#!/usr/bin/env python3
"""Rebuild listings.json + scout-data.js from stations.json + meta.json."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def main() -> None:
    stations = json.loads((DATA / "stations.json").read_text())
    meta = json.loads((DATA / "meta.json").read_text())
    rows = []
    for s in stations:
        for i, c in enumerate(s.get("contests") or []):
            title = c[0] if c else ""
            tags = (c[1] if len(c) > 1 else "").lower()
            extras = c[2:] if len(c) > 2 else []
            rows.append(
                {
                    "id": f"{s['call']}-{i+1}",
                    "stationCall": s["call"],
                    "stationName": s["name"],
                    "frequency": s["frequency"],
                    "audience": s["audience"],
                    "owner": s["owner"],
                    "format": s.get("format"),
                    "title": title,
                    "tags": tags,
                    "cash": "cash" in tags,
                    "tickets": "ticket" in tags,
                    "online": "online" in tags,
                    "text": "text" in tags,
                    "notes": extras,
                    "contestsUrl": s.get("contestsUrl"),
                    "phone": s.get("phone"),
                    "textLine": s.get("text"),
                }
            )
    meta["listingCount"] = len(rows)
    meta["stationPages"] = sum(1 for s in stations if s.get("audience") != "unresolved")
    meta["registryGap"] = sum(1 for s in stations if s.get("audience") == "unresolved")
    (DATA / "meta.json").write_text(json.dumps(meta, indent=2) + "\n")
    (DATA / "listings.json").write_text(json.dumps(rows, indent=2) + "\n")
    payload = {"meta": meta, "stations": stations, "listings": rows}
    (DATA / "scout-data.js").write_text(
        "window.SCOUT_DATA = " + json.dumps(payload) + ";\n"
    )
    print(f"rebuilt {len(rows)} listings across {meta['stationPages']} stations")


if __name__ == "__main__":
    main()
