# Appellation · Winery of the Month dashboards

Live: https://jules-esposito.github.io/appellation-winery-dashboards/

## Pages

| Page | Path | Audience |
|---|---|---|
| Hub, both properties | `/` | Internal |
| Healdsburg landing | `/healdsburg/` | Internal |
| Healdsburg schedules (2027 and 2026 tabs) | `/healdsburg/schedule/` | Internal |
| Healdsburg partnership | `/healdsburg/partnership/` | Winery facing |
| Lodi landing | `/lodi/` | Internal |
| Lodi schedule (2027 tab) | `/lodi/schedule/` | Internal |
| Lodi partnership | `/lodi/partnership/` | Winery facing |

Old links redirect: `/schedule/` and `/healdsburg/schedule-2026/` open the Healdsburg 2026 tab, `/healdsburg/schedule-2027/` the 2027 tab, `/lodi/schedule-2027/` the Lodi page, `/partnership/` the Healdsburg partnership page. Add `#2026` to a schedule URL to open that year.

Winery-facing pages carry no links to internal pages. Send wineries only the partnership URL.

## Editing

1. Change content in `data.py` (wineries, statuses, dates, partnership terms, contacts).
2. Run `python3 build.py`. It regenerates every `index.html` and refuses to write if an em dash slips in.
3. Commit and push. GitHub Pages redeploys in 1 to 3 minutes.

Do not hand-edit generated `index.html` files; the next build overwrites them.
`ameyalli-preview/` is a separate page and is not touched by the build.

## Shared files

- `assets/site.css`: the one stylesheet
- `assets/site.js`: tabs, copy-link buttons, contact gate
- `assets/logo.png`: white Appellation brandmark

## Contact gate

Contact names, emails and phones are not in this repo. They live in Supabase project `vkxjggeuicfrmenqdskl`, table `public.winery_contacts` (`slug`, `contact_name`, `contact_email`, `contact_phone`), readable only by emails active in `public.viewer_allowlist`. Each month card's `slug` in `data.py` matches a row. Missing rows show "Not on file yet" after sign-in.

Grant a viewer (they also need a Supabase auth user):

```sql
insert into public.viewer_allowlist (email, active) values ('name@appellationhotels.com', true);
```

Free-tier Supabase projects pause after a week without activity. If sign-in stops working, restore the project from the Supabase dashboard.
