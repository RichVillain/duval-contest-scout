# Update protocol

Goal: keep the admin dashboard current with easy-read, official-source contest data.

## Cadence

Refresh at least weekly. Stamp `meta.verified` with the date you actually checked official pages.

## Sources to open

| Station | Promotions |
| --- | --- |
| WJBT 93.3 The Beat | https://wjbt.iheart.com/promotions/ |
| WSOL V101.5 | https://v1015.iheart.com/promotions/ |
| WKSL 97.9 KISS FM | https://979kissfm.iheart.com/promotions/ |
| WQIK 99.1 | https://991wqik.iheart.com/promotions/ |
| WHJX Hot 106.5 | station contest page / Cox CDN |
| WAPE 95.1 | https://www.wape.com/contests/ |
| WJGL 96.9 The Eagle | station contest page / Cox CDN |
| WEJZ 96.1 | https://www.wejz.com |

Do not invent a ninth station. The registry gap stays empty until an official source names it.

## Contest row format

Inside `data/stations.json`, each contest is:

```json
["Prize title", "tags", "optional note", "optional extra"]
```

Tags (space-separated, lowercase):

- `tickets` — concert / event tickets
- `cash` — money prize
- `online` — enter on the station site or app
- `text` — text-to-enter
- `call` — call-in after the cue

## Rebuild

```bash
python3 scripts/rebuild-data.py
```

Then open `admin/index.html` and confirm:

1. Listing count matches the JSON
2. Cash / tickets / online KPIs look right
3. Play-now cards still make sense
4. iHeart lockout + pickup text is still accurate

## Status language

- **Active** — listed on the verified station page this week
- **Confirm on-air** — keyword, caller number, or studio line is not published
- **Ending soon** — a near date is confirmed in the official copy
- **Unverified** — detail must be checked in current rules

## Do not

- Do not copy old keywords forward
- Do not add pay-to-enter or card-required contests
- Do not auto-dial
- Do not treat social screenshots as official unless the station page matches
