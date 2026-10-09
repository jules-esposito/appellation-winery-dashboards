#!/usr/bin/env python3
"""Generate every page of the Winery of the Month site from data.py.

Usage:  python3 build.py
Then commit and push. GitHub Pages serves the repo root.
"""
import datetime
import os
import re

from data import PROPERTIES, REDIRECTS, TBD

ROOT = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.date.today()
UPDATED = f"{TODAY:%B} {TODAY.day}, {TODAY.year}"
PENDING_SUB = '<span class="tbd-text">Pending winery submission</span>'

CAL_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>'
GIFT_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 12v9H4v-9"/><path d="M2 7h20v5H2z"/><path d="M12 22V7"/><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"/></svg>'
HANDS_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 8.5 2 15l3 3 3.5-3.5"/><path d="m22 9-3-3-3.5 3.5L19 13z"/><path d="M13 6.5 17.5 11 11 17.5 6.5 13z"/><path d="m9 15 3 3"/></svg>'
CHECK_SVG = '<span class="check"><svg viewBox="0 0 24 24" fill="none" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg></span>'

STATUS_TEXT = {"confirmed": "Confirmed", "pending": "Pending confirmation", "tbd": "To be scheduled"}


def rel(page_dir, target):
    """Relative URL from page_dir (e.g. 'lodi/partnership') to target dir or file."""
    up = "../" * (len(page_dir.split("/")) if page_dir else 0)
    return up + target


def page(page_dir, title, body, *, audience, gate=False):
    css = rel(page_dir, "assets/site.css")
    js = rel(page_dir, "assets/site.js")
    sb = '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>\n' if gate else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="color-scheme" content="light">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<link rel="icon" type="image/png" href="{rel(page_dir, 'assets/logo.png')}">
<link rel="stylesheet" href="{css}">
</head>
<body data-audience="{audience}">
{body}
{sb}<script src="{js}"></script>
</body>
</html>
"""


def header(page_dir, eyebrow, prop, prog, sub, *, crumbs=None, audience=None):
    nav = ""
    if crumbs is not None:
        parts = [f'<a href="{rel(page_dir, href)}">{label}</a>' for label, href in crumbs]
        tag = {"internal": '<span class="audience internal">Internal &middot; Team only</span>',
               "external": '<span class="audience external">Winery facing</span>'}.get(audience, "")
        nav = f'<nav class="topnav"><div>{"<span class=crumb-sep>/</span>".join(parts)}</div>{tag}</nav>\n'
    eb = f'  <p class="property-eyebrow">{eyebrow}</p>\n' if eyebrow else ""
    return f"""{nav}<header>
  <img class="logo" src="{rel(page_dir, 'assets/logo.png')}" alt="Appellation">
{eb}  <h1><span class="prop">{prop}</span><span class="prog">{prog}</span></h1>
{f'  <p class="sub">{sub}</p>' + chr(10) if sub else ''}</header>"""


def footer(*parts):
    return "<footer>" + " &nbsp;&middot;&nbsp; ".join(parts) + "</footer>"


# ------------------------------------------------------------------ schedule

def links_html(links, buttons=False):
    if buttons:
        inner = "".join(f'<a class="wd-btn" href="{l["url"]}" target="_blank" rel="noopener">{l["label"]}</a>' for l in links)
        return f'<div class="wd-btn-group">{inner}</div>'
    return " &middot; ".join(f'<a href="{l["url"]}" target="_blank" rel="noopener">{l["label"]}</a>' for l in links)


def month_card(prop, sched, m):
    year = sched["year"]
    d = m.get("details", {})
    labels = prop["detail_labels"]
    tag = m["quarter"] + (f' &middot; {m["season"]}' if m.get("season") else "")
    if m["winery"]:
        name = f'<div class="featured-name">{m["winery"]}</div>'
    else:
        name = '<div class="featured-name tbd-name">To be announced</div>'
    progs = "\n".join(
        f'          <div><h3>{p["title"]}</h3><ul><li><span class="status-dot {p["status"]}"></span><span>{p["text"]}</span></li></ul></div>'
        for p in m["programs"])

    details = ""
    if m["winery"]:
        web = d.get("website") or []
        web_html = links_html(web) if web else ""
        if d.get("social"):
            web_html = (web_html + " &middot; " if web_html else "") + d["social"]
        fields = [
            f'<div class="wd-field wd-contact" data-w="{m["slug"]}"></div>',
            f'<div class="wd-field"><span class="wd-key">Website / Social</span>{web_html or PENDING_SUB}</div>',
            f'<div class="wd-field"><span class="wd-key">Logo Assets</span>{links_html(d["logo"], True) if d.get("logo") else PENDING_SUB}</div>',
            f'<div class="wd-field"><span class="wd-key">Marketing Photos</span>{links_html(d["photos"], True) if d.get("photos") else PENDING_SUB}</div>',
            f'<div class="wd-field"><span class="wd-key">{labels["nn_wine"]}</span>{d.get("nn_wine") or PENDING_SUB}</div>',
            f'<div class="wd-field"><span class="wd-key">{labels["friday_wine"]}</span>{d.get("friday_wine") or PENDING_SUB}</div>',
        ]
        yappy = ""
        if d.get("yappy"):
            cls, text = d["yappy"]
            yappy = f'\n          <span class="yappy-status {cls}">{text}</span>'
        bio = f'<p>{d["bio"]}</p>' if d.get("bio") else '<p class="tbd-text">Pending winery submission.</p>'
        details = f"""
        <div class="winery-details">
          <div class="wd-label">Winery of the Month Details</div>
          <div class="wd-grid">
            {(chr(10) + '            ').join(fields)}
          </div>{yappy}
          <details class="bio-details"><summary>Winery Bio</summary>{bio}</details>
        </div>"""

    return f"""    <article class="value-card{' is-tbd' if not m['winery'] else ''}" id="{year}-{m['month'].lower()}">
      <div class="card-header">
        <div class="month-title"><div class="icon-wrap">{CAL_SVG}</div><h2>{m['month']} {year}</h2></div>
        <span class="quarter-tag">{tag}</span>
      </div>
      <div class="card-body">
        <div class="featured-row">
          <div>
            <div class="featured-label">{prop['name']} &middot; Winery of the Month</div>
            {name}
          </div>
          <div class="status-badge {m['status']}">{STATUS_TEXT[m['status']]}</div>
        </div>
        <div class="sub-programs">
{progs}
        </div>{details}
      </div>
    </article>"""


def schedule_page(key, prop):
    pd = prop["schedule_path"]
    scheds = prop["schedules"]
    tabs, panels = [], []
    for i, sched in enumerate(scheds):
        year = sched["year"]
        active = " active" if i == 0 else ""
        cards = "\n\n".join(month_card(prop, sched, m) for m in sched["months"])
        dinners = "\n".join(
            f"""      <div class="dinner-card">
        <div class="q-label">{dn['q']} {year}</div>
        <div class="q-winery{' tbd-name' if not dn['winery'] else ''}">{dn['winery'] or 'Not yet assigned'}</div>
        <span class="q-status {dn['status']}">{dn['label']}</span>
      </div>""" for dn in sched["dinners"])
        tabs.append((year, f'  <button class="tab-btn{active}" data-tab="{year}">{year}</button>'))
        panels.append(f"""<div id="tab-{year}" class="tab-panel{active}">
<main>
  <p class="year-range">{sched['range']}</p>
  <div class="legend">
    <span><i class="status-dot confirmed"></i>Confirmed</span>
    <span><i class="status-dot pending"></i>Pending confirmation</span>
    <span><i class="status-dot tbd"></i>To be scheduled</span>
  </div>
  <div class="month-grid">
{cards}
  </div>
  <h2 class="section-title"><span>{year} Quarterly Wine Dinners</span></h2>
  <div class="dinner-grid">
{dinners}
  </div>
</main>
</div>""")
    chips = "\n".join(f'      <div class="chip">{c}</div>' for c in prop["recurring"])
    crumbs = [("All properties", ""), (prop["name"], f"{key}/")]

    body = f"""{header(pd, prop['eyebrow'], prop['name'], 'Winery of the Month', 'Internal Partner Schedule', crumbs=crumbs)}

<div class="tab-nav">
{chr(10).join(t for _, t in sorted(tabs))}
</div>

<div class="authwrap"><div class="authbar" id="authbar">
  <div class="ab-note" id="ab-note">Winery contact details are hidden. Sign in with an approved Appellation email to see them.</div>
  <input id="ab-email" type="email" placeholder="you@appellationhotels.com" autocomplete="email">
  <input id="ab-pass" type="password" placeholder="Password" autocomplete="current-password">
  <button id="ab-signin">Sign in</button>
  <button class="ghost" id="ab-link">Email me a link</button>
  <button class="ghost hidden" id="ab-signout">Sign out</button>
  <div class="ab-msg" id="ab-msg"></div>
</div></div>

{chr(10).join(panels)}

<main class="recurring">
  <h2 class="section-title"><span>Recurring Programming</span></h2>
  <div class="chip-list">
{chips}
  </div>
</main>

{footer(prop['footer'], 'Winery of the Month Program', 'Internal Use', f'Last updated {UPDATED}')}"""
    return pd, page(pd, f"{prop['name']} &middot; Winery of the Month Schedule", body, audience="internal", gate=True)


# --------------------------------------------------------------- partnership

def li(item):
    if isinstance(item, dict):
        return f'<li class="addon-item"><span class="addon-badge">Optional Add-On</span> {item["addon"]}</li>'
    return f"<li>{CHECK_SVG}<span>{item}</span></li>"


def column(cls, icon, kicker, title, sections):
    subs = "\n".join(
        f'          <div class="subsection"><h3>{h}</h3><ul>\n            ' + "\n            ".join(li(i) for i in items) + "\n          </ul></div>"
        for h, items in sections)
    return f"""    <div class="{cls}">
      <div class="value-card">
        <div class="card-header"><div class="icon-wrap">{icon}</div><div class="card-title"><span class="kicker">{kicker}</span>{title}</div></div>
        <div class="card-body">
{subs}
        </div>
      </div>
    </div>"""


def partnership_page(key, prop):
    p = prop["partnership"]
    pd = p["path"]
    c = p["contact"]
    title_line = f'\n    <div class="contact-title">{c["title"]}</div>' if c.get("title") else ""
    body = f"""{header(pd, prop['eyebrow'], prop['name'], 'Winery of the Month', p['sub'])}
<div class="tab-nav">
  <button class="tab-btn active" data-tab="details">Partnership Details</button>
  <button class="tab-btn" data-tab="submit">Submit Information</button>
</div>

<div id="tab-details" class="tab-panel active partner">
<div class="intro">{p['intro']}</div>
<div class="winery-field">
  <label>{prop['name']} &middot; Winery of the Month</label>
  <div class="field-line"></div>
</div>
<main>
  <div class="columns">
{column('provides-col', GIFT_SVG, 'What You Receive', p['provides_title'], p['provides'])}
{column('commits-col', HANDS_SVG, 'What You Provide', 'Winery Partnership Commitment', p['commits'])}
  </div>
  <div class="closing">
    <div class="contact-name">{c['name']}</div>{title_line}
    <div class="contact-email"><a href="mailto:{c['email']}">{c['email']}</a></div>
  </div>
</main>
</div>

<div id="tab-submit" class="tab-panel">
  <div class="submit-wrap">
    <h2>Submit Your Information</h2>
    <p>{p['submit_text']}</p>
    <a class="submit-btn" href="{prop['form_url']}" target="_blank" rel="noopener">Submit Info</a>
  </div>
</div>

{footer(prop['footer'], 'Winery of the Month Program', 'Partner Reference')}"""
    return pd, page(pd, f"{prop['name']} &middot; Winery of the Month Partnership", body, audience="external")


# ------------------------------------------------------------ landing + hub

def landing_page(key, prop):
    pd = key
    body = f"""{header(pd, prop['eyebrow'], prop['name'], 'Winery of the Month', '', crumbs=[('All properties', '')])}
<main class="choice">
  <a class="choice-btn" href="{rel(pd, prop['schedule_path'] + '/')}">Internal</a>
  <a class="choice-btn external" href="{rel(pd, prop['partnership']['path'] + '/')}">External</a>
</main>"""
    return pd, page(pd, f"{prop['name']} &middot; Winery of the Month", body, audience="internal")


def hub_page():
    blocks = []
    for key, prop in PROPERTIES.items():
        blocks.append(f"""    <div>
      <a class="card property-card" href="{key}/">
        <h3>{prop['name']}</h3>
        <p>Internal and External Dashboards</p>
        <span class="go">Open {prop['name'].replace('Appellation ', '')} &rarr;</span>
      </a>
    </div>""")
    body = f"""{header('', None, 'Appellation Hotels', 'Winery of the Month', 'Partner dashboards by property')}
<main>
  <section class="group">
    <p class="group-label">Choose a property</p>
    <div class="cards">
{chr(10).join(blocks)}
    </div>
  </section>
</main>
{footer('Appellation Hotels', 'Winery of the Month Program', 'Internal Use')}"""
    return "", page("", "Appellation &middot; Winery of the Month", body, audience="internal")


def redirect_page(src, dest):
    path, _, frag = dest.partition("#")
    url = rel(src, path + "/")
    hash_js = f'"#{frag}"' if frag else "location.hash"
    href = url + (f"#{frag}" if frag else "")
    return src, f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="robots" content="noindex, nofollow">
<title>Moved</title>
<meta http-equiv="refresh" content="0; url={href}">
<link rel="canonical" href="{url}">
<script>location.replace("{url}" + location.search + {hash_js});</script>
</head><body style="font-family:Arial,sans-serif;background:#FAF7F2;color:#2B2A28;padding:40px">
This page has moved. <a href="{href}" style="color:#5C6B41">Continue</a>.
</body></html>
"""

def write(page_dir, html):
    if "—" in html or "&mdash;" in html:
        raise SystemExit(f"Em dash found in {page_dir or 'index'}; remove it from data.py.")
    path = os.path.join(ROOT, page_dir, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  wrote /{page_dir + '/' if page_dir else ''}")


SITE_URL = "https://jules-esposito.github.io/appellation-winery-dashboards/"
TRELLIS_OUT = os.path.join(os.path.dirname(ROOT), "Trellis board", "winery-of-the-month.html")


def trellis_hub():
    """Self-contained copy of the hub for the Trellis board: inline CSS and logo, absolute links."""
    import base64
    _, html = hub_page()
    css = open(os.path.join(ROOT, "assets", "site.css"), encoding="utf-8").read()
    logo = base64.b64encode(open(os.path.join(ROOT, "assets", "logo.png"), "rb").read()).decode()
    html = html.replace('<link rel="stylesheet" href="assets/site.css">', f"<style>\n{css}\n</style>")
    html = html.replace('<link rel="icon" type="image/png" href="assets/logo.png">\n', "")
    html = html.replace('src="assets/logo.png"', f'src="data:image/png;base64,{logo}"')
    html = html.replace('<script src="assets/site.js"></script>\n', "")
    for key in PROPERTIES:
        html = html.replace(f'href="{key}/"', f'href="{SITE_URL}{key}/" target="_top"')
    assert "assets/" not in html, "relative asset left in Trellis hub"
    os.makedirs(os.path.dirname(TRELLIS_OUT), exist_ok=True)
    with open(TRELLIS_OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  wrote Trellis board file: {TRELLIS_OUT}")


def main():
    out = [hub_page()]
    for key, prop in PROPERTIES.items():
        out.append(landing_page(key, prop))
        out.append(partnership_page(key, prop))
        out.append(schedule_page(key, prop))
    out.extend(redirect_page(src, dest) for src, dest in REDIRECTS.items())
    for pd, html in out:
        write(pd, html)
    trellis_hub()


if __name__ == "__main__":
    main()
