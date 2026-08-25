# Appellation Healdsburg — Winery of the Month dashboards

Static site served by GitHub Pages. No build step, no dependencies.

| Path | Audience | Notes |
|---|---|---|
| `index.html` | internal | Landing page linking both dashboards |
| `schedule/index.html` | internal | 2026 partner schedule, August through December. Winery contact details stay hidden until sign in |
| `partnership/index.html` | winery facing | What Appellation provides vs. what the winery commits to, plus the ClickUp intake form |

## Contact details are not in this repo

Winery contact names, emails and phone numbers live in Supabase, table `public.winery_contacts`,
project `vkxjggeuicfrmenqdskl`. Row level security allows `select` only when the signed in email is
active in `public.viewer_allowlist`, checked by `private.is_allowed_viewer()`. That is the same gate
`cpc-eom-dashboard` uses.

The Supabase key embedded in `schedule/index.html` is a publishable key and reads nothing on its own.
Never put a `service_role` key in these files.

To grant someone access, add them to the allowlist and make sure they have a Supabase auth user:

```sql
insert into public.viewer_allowlist (email, active) values ('name@appellationhotels.com', true);
```

The sign in bar accepts a password or a one time email link.

## Editing

Edit the HTML and commit. Pages redeploys on every push to `main`.

Schedule source data comes from ClickUp: workspace `9014048227`, space "Appellation Marketing",
folder "Healdsburg", list "Winery of the Month" (`901418123665`). The winery intake form is
`https://forms.clickup.com/9014048227/f/8cmexf3-4694/T38F7WBXB4CP6O7K2R`.

`robots.txt` and a `noindex` tag on both dashboards keep the site out of search results.
