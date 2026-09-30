# Duval Contest Scout

Jacksonville / Duval County radio contest intelligence.

Public scout + admin dashboard, sourced from the Muse artifact
[Duval Contest Scout](https://muse.ai/s/duval-contest-scout-zy66xaxl99xpxwxv)
(verified **Sept 28, 2026**) and packaged for weekly updates.

Built for Kimani Dudley. Private repo.

## Open locally

No build step. Open either file in a browser:

- Public radar: [`public/index.html`](public/index.html)
- Admin dashboard: [`admin/index.html`](admin/index.html)
- Original Muse capture: [`public/muse-original.html`](public/muse-original.html)

Both live pages read [`data/scout-data.js`](data/scout-data.js).

## What is in here

| Path | Purpose |
| --- | --- |
| `data/stations.json` | Weekly source of truth — stations + contests |
| `data/listings.json` | Flattened easy-read contest rows |
| `data/meta.json` | Verified stamp, pickup rules, scam shield |
| `data/scout-data.js` | Same payload embedded for file:// use |
| `public/index.html` | Easy-read public radar |
| `admin/index.html` | Admin dashboard: KPIs, filters, play cards, local track |
| `UPDATE-PROTOCOL.md` | How to keep the dashboard current |

## Snapshot (verified Sept 28, 2026)

- **61** verified listings
- **8** station pages + **1** open registry slot
- Filters: All · Black Radio · Mainstream · Cash · Tickets · Enter Online
- iHeart cluster pickup: 8000 Belfort Pkwy, Jacksonville, FL 32256
- 30-day household lockout across the iHeart Jacksonville cluster (90 days if prize > $100)

## Scam shield

Real radio contests never require card data to enter. Never pay. Never enter credit-card information.

## Weekly update

Edit `data/stations.json`, then run:

```bash
python3 scripts/rebuild-data.py
```

That regenerates listings + `scout-data.js`. Commit. Open admin to confirm counts.

See [UPDATE-PROTOCOL.md](UPDATE-PROTOCOL.md).
