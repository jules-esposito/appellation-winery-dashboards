# Appellation Winery of the Month: all site content lives here.
# Edit this file, then run `python3 build.py` to regenerate every page.
#
# Status values: "confirmed", "pending", "tbd".
# Text may contain HTML entities (&amp;, &middot;). Never use em dashes.
# Yappy chip classes: "yes", "maybe", "pending".
# "slug" ties a month to its row in Supabase public.winery_contacts.

CONFIRMED, PENDING, TBD = "confirmed", "pending", "tbd"


def link(label, url):
    return {"label": label, "url": url}


def prog(title, text, status=CONFIRMED):
    return {"title": title, "status": status, "text": text}


# ---------------------------------------------------------------- HEALDSBURG

HB_NN = prog("Neighbor Night", "Wednesdays, weekly")


def hb_month(month, quarter, winery, slug, yappy, *extra, status=CONFIRMED, website=None, note=None):
    programs = [prog("Yappy Hour", yappy), HB_NN, *extra]
    if note:
        programs.append(prog("Note", note, TBD))
    return {
        "month": month, "quarter": quarter, "winery": winery, "slug": slug,
        "status": status, "programs": programs,
        "details": {"website": website or []},
    }


HB_2027 = [
    hb_month("January", "Q1", "Innumero Wines", "innumero", "January 7",
             website=[link("innumerowines.com", "https://www.innumerowines.com")],
             note="Smaller production"),
    hb_month("February", "Q1", "Red Stitch", "red-stitch", "February 4",
             website=[link("redstitchwine.com", "https://www.redstitchwine.com")]),
    hb_month("March", "Q1", "Marine Layer Wines", "marine-layer", "March 4",
             note="Pigs and Pinot"),
    hb_month("April", "Q2", "CIRQ | CHEV", "michael-browne", "April 1",
             prog("Quarterly Wine Dinner", "Q2 CIRQ | CHEV &middot; <span class=\"tbd-text\">date pending</span>"),
             website=[link("cirq.com", "https://cirq.com"), link("chevwines.com", "https://chevwines.com")]),
    hb_month("May", "Q2", "Brandon Gregory", "brandon-gregory", "May 6"),
    hb_month("June", "Q2", "Jackson Family Wines", "stonestreet", "June 3"),
    hb_month("July", "Q3", "The Setting Wines", "the-setting", "July 1"),
    hb_month("August", "Q3", "Bricoleur Vineyards", "bricoleur", "August 5",
             prog("Quarterly Wine Dinner", "Q3 Bricoleur &middot; <span class=\"tbd-text\">pending confirmation</span>", PENDING)),
    hb_month("September", "Q3", "Mauritson Wines", "mauritson", "September 2",
             note="Project Zin"),
    hb_month("October", "Q4", "Knights Bridge Winery", "knights-bridge", "October 7",
             website=[link("knightsbridgewinery.com", "https://knightsbridgewinery.com")]),
    hb_month("November", "Q4", "Dutcher Crossing Winery", "dutcher-crossing", "November 4"),
    hb_month("December", "Q4", "Grail by Dan Kosta", "kosta", "December 2",
             prog("Quarterly Wine Dinner", "Q4 Grail by Dan Kosta &middot; <span class=\"tbd-text\">pending confirmation</span>", PENDING),
             website=[link("grailbydankosta.com", "https://grailbydankosta.com")]),
]

HB_2027_DINNERS = [
    {"q": "Q1", "winery": None, "status": TBD, "label": "To be scheduled"},
    {"q": "Q2", "winery": "CIRQ | CHEV", "status": CONFIRMED, "label": "April"},
    {"q": "Q3", "winery": "Bricoleur Vineyards", "status": PENDING, "label": "August &middot; Pending"},
    {"q": "Q4", "winery": "Grail by Dan Kosta", "status": PENDING, "label": "December &middot; Pending"},
]

PENDING_YAPPY_HOST = "<span class=\"tbd-text\">host pending confirmation</span>"

HB_2026 = [
    {
        "month": "August", "quarter": "Q3", "winery": "Kosta", "slug": "kosta", "status": CONFIRMED,
        "programs": [prog("Yappy Hour", "August 6 &middot; " + PENDING_YAPPY_HOST, PENDING)],
        "details": {
            "website": [link("grailbydankosta.com", "https://grailbydankosta.com")],
            "social": "@dankostawines",
            "logo": [link("Logo Assets", "https://netorg10522870.sharepoint.com/:f:/s/CompanyPortal/IgAmNSa7BtVWSJcu5cLfiIsLAVSjhKC5Tyx4B-SHlar6gEI?e=KeIgIn")],
            "photos": [link("Marketing Photos", "https://netorg10522870.sharepoint.com/:f:/s/CompanyPortal/IgCbUFT6grbeT5QcvdxjX_WqAQgCOFh2jMY2xNiv8VlT4W8?e=M0TyKY")],
            "nn_wine": "<span class=\"tbd-text\">(Need Guidance Please)</span>",
            "friday_wine": "Grail by Dan Kosta Campbell Ranch Pinot Noir, 2022",
            "yappy": ("pending", "Yappy Hour: Pending response"),
            "bio": "Grail by Dan Kosta is a quest for exceptional Pinot Noir and Chardonnay, guided by Dan's reputation for producing world-class quality. Success has not happened overnight, but rather through many seasons of working with the elusive grape, understanding the nuances of terroir, and cultivating relationships that lead us to the pinnacle enjoyment of not only the wine, but also the people and the process. After many years of preparation, we are ready to share these timeless bottles with you.",
        },
    },
    {
        "month": "September", "quarter": "Q3", "winery": "Knights Bridge", "slug": "knights-bridge", "status": CONFIRMED,
        "programs": [
            prog("Yappy Hour", "September 3 &middot; " + PENDING_YAPPY_HOST, PENDING),
            prog("Quarterly Wine Dinner", "Knights Bridge &middot; <span class=\"tbd-text\">date pending confirmation</span>", PENDING),
        ],
        "details": {
            "website": [link("knightsbridgewinery.com", "https://knightsbridgewinery.com")],
            "social": "@knightsbridgewinery",
            "logo": [link("Logo Assets", "https://knightsbridgewinery.com/trade-media/knights-bridge/")],
            "photos": [link("Marketing Photos", "https://knightsbridgewinery.com/trade-media/knights-bridge/")],
            "nn_wine": "2024 Knights Bridge Pont de Chevalier Sauvignon Blanc &middot; $17/bottle",
            "friday_wine": "2021 Knights Bridge Pont de Chevalier Chardonnay",
            "yappy": ("pending", "Yappy Hour: Pending response"),
            "bio": "Knights Bridge Winery was founded with a singular purpose: to produce exceptional wines from an extraordinary place, inspired by the wild beauty of Knights Valley and the grandeur of Mt. St. Helena. The organically farmed, 100% estate-grown vineyard spans 80 planted acres on the rocky western slopes of the Mayacamas Mountains. Winemaker Derek Baljeu, a UC Davis graduate in Viticulture and Enology, crafts wines that are balanced, refined, and built to age.",
        },
    },
    {
        "month": "October", "quarter": "Q4", "winery": "Michael Browne", "slug": "michael-browne", "status": CONFIRMED,
        "programs": [prog("Yappy Hour", "October 1 &middot; Michael Browne")],
        "details": {
            "website": [link("cirq.com", "https://cirq.com"), link("chevwines.com", "https://chevwines.com")],
            "social": "@cirqestate &middot; @chev_wines",
            "logo": [link("Logo Assets", "https://drive.google.com/drive/folders/1owou_RFwIf0UKWmfSRtQzbKIdI9vx51k?usp=drive_link")],
            "photos": [link("Marketing Photos", "https://drive.google.com/drive/folders/15SUElfVo-wvY3KhLVoPEzO--ls9ZzQ40?usp=sharing")],
            "nn_wine": "2022 CHEV Chardonnay, Russian River Valley &middot; $20/bottle",
            "friday_wine": "2023 CHEV Pinot Noir, Russian River Valley",
            "yappy": ("yes", "Yappy Hour: Yes, participating"),
            "bio": "Perched atop a private hilltop in the Russian River Valley, CIRQ | CHEV Estate by Sarah and Michael Browne brings together exceptional wines, genuine hospitality, and meaningful moments. Renowned vintner and Kosta Browne co-founder Michael Browne launched CIRQ in 2009, focused on crafting extraordinary Pinot Noir from the Russian River Valley's finest vineyard sites. CHEV followed as a tribute to timeless craftsmanship.",
        },
    },
    {
        "month": "November", "quarter": "Q4", "winery": "Rochioli", "slug": "rochioli", "status": CONFIRMED,
        "programs": [
            prog("Yappy Hour", "November 5 &middot; Rochioli"),
            prog("Quarterly Wine Dinner", "Rochioli &middot; <span class=\"tbd-text\">date pending confirmation</span>", PENDING),
        ],
        "details": {
            "website": [link("rochioliwinery.com", "https://rochioliwinery.com")],
            "social": "@rochioliwinery",
            "logo": [link("Logo Assets", "https://www.dropbox.com/scl/fo/2wdgq215j5c7p4ev70ded/APW1HRQ7pgcaGzChS89ez1w?rlkey=jcfwer5a0qorlfj89jl2dzh6x&st=cbew3ili&dl=0")],
            "photos": [link("Marketing Photos", "https://www.dropbox.com/scl/fo/2wdgq215j5c7p4ev70ded/APW1HRQ7pgcaGzChS89ez1w?rlkey=jcfwer5a0qorlfj89jl2dzh6x&st=cbew3ili&dl=0")],
            "nn_wine": "2024 Estate Chardonnay / 2024 Estate Pinot Noir &middot; $20/bottle",
            "friday_wine": "2024 Estate Chardonnay / 2024 Estate Pinot Noir",
            "yappy": ("maybe", "Yappy Hour: Maybe another time"),
            "bio": "With four generations of dedication to the land, Rochioli Vineyards & Winery has earned a reputation as one of Sonoma County's finest wineries. Our family crafts renowned, terroir-driven wines built on a foundation of superb fruit, with a focus on Pinot Noir, Chardonnay, and Sauvignon Blanc. This commitment to quality is unwavering and is our promise to everyone who uncorks a bottle of our wine.",
        },
    },
    {
        "month": "December", "quarter": "Q4", "winery": "Stonestreet", "slug": "stonestreet", "status": CONFIRMED,
        "programs": [prog("Yappy Hour", "December 3 &middot; Jackson Family Wines")],
        "details": {
            "website": [link("stonestreetwines.com", "https://www.stonestreetwines.com")],
            "logo": [link("Logo Assets", "https://jfw.widen.net/s/wtw8fjmd5j/sts-logo---blue")],
            "photos": [
                link("Marketing Photos 1", "https://jfw.widen.net/s/ttgzpmdg6j/ewp2019_stonestreet_rockfall-7221_extended-cmyk"),
                link("Marketing Photos 2", "https://jfw.widen.net/s/b9dh927jnq/st_winemaker_25_mbattey_9-2025"),
                link("Marketing Photos 3", "https://jfw.widen.net/s/5ft6hjqxpt/ewp2019_stonestreet-2250"),
                link("Marketing Photos 4", "https://jfw.widen.net/s/8fpnmlkq5s/stonestreet-may2024-226"),
            ],
            "nn_wine": "2017 Bear Point Vineyard Cabernet Sauvignon &middot; $20/bottle",
            "friday_wine": "2022 Estate Chardonnay",
            "yappy": ("yes", "Yappy Hour: Yes, participating"),
            "bio": "Stonestreet Estate Vineyards is the story of a family's vision to defy the limits of California winegrowing. Jess Stonestreet Jackson and Barbara Banke established the estate in 1995, and their son Christopher Jackson and his wife Ariel continue the legacy. Stonestreet is one of the most expansive and multi-faceted mountain vineyards in the world, producing a distinctive collection of single vineyard wines focused on powerful Cabernet Sauvignon and soulful Chardonnay.",
        },
    },
]

HB_2026_DINNERS = [
    {"q": "Q3", "winery": "Knights Bridge", "status": PENDING, "label": "September &middot; Date pending"},
    {"q": "Q4", "winery": "Rochioli", "status": PENDING, "label": "November &middot; Date pending"},
]

# ---------------------------------------------------------------- LODI

LO_NN = prog("Neighbor Nights", "Sundays and Mondays")
LO_FRI = prog("Friday Wine Reception", "Fridays, 4 to 5 pm")


def lo_month(month, quarter, winery, slug, *extra, status=CONFIRMED, season=None, note=None):
    programs = [LO_NN, LO_FRI, *extra]
    if note:
        programs.append(prog("Note", note, TBD))
    return {
        "month": month, "quarter": quarter, "season": season, "winery": winery, "slug": slug,
        "status": status if winery else TBD, "programs": programs, "details": {},
    }


LO_2027 = [
    lo_month("January", "Q1", "Mikami Vineyards", "mikami", season="Slow Season"),
    lo_month("February", "Q1", "Block 21 Winery", "block-21"),
    lo_month("March", "Q1", "LangeTwins", "langetwins"),
    lo_month("April", "Q2", "Flowers", "flowers",
             prog("Quarterly Wine Dinner", "Q2 Terre Rouge &middot; <span class=\"tbd-text\">date pending</span>"),
             status=PENDING),
    lo_month("May", "Q2", "Markus Wine Co.", "markus", season="Summer", note="American Fare"),
    lo_month("June", "Q2", "Harney Lane Winery", "harney-lane"),
    lo_month("July", "Q3", "Acquiesce Winery", "acquiesce"),
    lo_month("August", "Q3", "Perlegos Family Wine Co.", "perlegos",
             prog("Quarterly Wine Dinner", "Q3 Perlegos &middot; <span class=\"tbd-text\">date pending</span>"),
             season="Harvest"),
    lo_month("September", "Q3", "Oak Farm Vineyards", "oak-farm"),
    lo_month("October", "Q4", None, None),
    lo_month("November", "Q4", None, None, season="Holidays"),
    lo_month("December", "Q4", None, None,
             prog("Quarterly Wine Dinner", "Q4 Harney Lane &middot; <span class=\"tbd-text\">date pending</span>")),
]

LO_2027_DINNERS = [
    {"q": "Q1", "winery": None, "status": TBD, "label": "To be scheduled"},
    {"q": "Q2", "winery": "Terre Rouge", "status": CONFIRMED, "label": "April"},
    {"q": "Q3", "winery": "Perlegos Family Wine Co.", "status": CONFIRMED, "label": "August"},
    {"q": "Q4", "winery": "Harney Lane Winery", "status": CONFIRMED, "label": "December"},
]

# ---------------------------------------------------------------- PROPERTIES

PROPERTIES = {
    "healdsburg": {
        "name": "Appellation Healdsburg",
        "eyebrow": "Appellation Healdsburg &nbsp;&middot;&nbsp; Sonoma County",
        "footer": "Appellation Healdsburg",
        "detail_labels": {"nn_wine": "Neighbor Night Wines", "friday_wine": "Friday Pour Wine"},
        "recurring": ["Neighbor Night &middot; Wednesdays", "Friday Lobby Pours &middot; Weekly", "Yappy Hour &middot; First Thursday"],
        "form_url": "https://forms.clickup.com/9014048227/f/8cmexf3-4694/T38F7WBXB4CP6O7K2R",
        "schedule_path": "healdsburg/schedule",
        "schedules": [
            {"year": 2027, "path": "healdsburg/schedule-2027", "range": "January&ndash;December 2027",
             "months": HB_2027, "dinners": HB_2027_DINNERS,
             "blurb": "Twelve months of featured wineries, Yappy Hour dates, and quarterly wine dinners."},
            {"year": 2026, "path": "healdsburg/schedule-2026", "range": "August&ndash;December 2026",
             "months": HB_2026, "dinners": HB_2026_DINNERS,
             "blurb": "August through December. Assets, featured wines, and winery bios as submitted."},
        ],
        "partnership": {
            "path": "healdsburg/partnership",
            "sub": "Featured Winery Partnership",
            "intro": "Appellation Healdsburg is rooted in relationships with the legendary and emerging producers who define Sonoma County's character. As Winery of the Month, your story is woven into the guest experience for a full month, across our restaurant, our lobby, and our community. What follows is what the partnership provides, and what we ask of your winery in return.",
            "provides_title": "Appellation Provides",
            "provides": [
                ("Prominent Exposure", [
                    "Featured Winery of the Month page on the Folia wine list",
                    "Dedicated landing page on the Appellation Healdsburg website as the month's featured winery partner",
                    "Inclusion in Appellation Healdsburg email marketing campaigns throughout the month",
                    "One collaborative social post or reel, produced by the Appellation team and shared from both accounts",
                ]),
                ("Immersive Guest Experiences", [
                    "Exclusive Welcome Pour Experience served to every arriving hotel guest throughout the month, paired with a signature Sonoma Taste bite",
                    "Opportunity to provide branded winery materials for an immersive Front Desk Welcome Experience throughout the partnership",
                ]),
                ("Programming &amp; Events", [
                    "Exclusive winery partner for Neighbor Night, held every Wednesday of the month, with a by-the-glass and by-the-bottle offering at a featured promotional price",
                    "Friday Lobby Wine Pours hosted weekly by your winery throughout the month, with preference for a winemaker or principal to be present",
                    "Opportunity to host an Atelier Cellar Session: a ticketed, twelve-seat maximum tasting menu dinner curated around your wines by Chefs Reed and Charlie Palmer",
                    {"addon": "Yappy Hour: option and preference for your winery to take part, held the first Thursday of every month."},
                ]),
            ],
            "commits": [
                ("Wine Support", [
                    "Provide 6&ndash;8 cases of wine throughout the partnership (final quantity based on projected hotel occupancy)",
                    "Offer two featured SKUs at preferred pricing (less than $20/bottle) to support by-the-glass pours at Neighbor Night (every Wednesday). No winery representative is needed to pour",
                ]),
                ("Guest Experience", [
                    "Provide decor and materials that reflect your winery's story to outfit the Front Desk experience; our team will help finalize the plan",
                    "Provide an exclusive tasting experience for Appellation guests (e.g., two-for-one tasting, complimentary tasting upgrade, library tasting)",
                ]),
                ("Marketing Commitments", [
                    "One dedicated in-feed social post or reel from your winery's channels",
                    "One dedicated email campaign at the start of the month, featuring the wine and the month's programming (wine dinners, Yappy Hour, and similar)",
                    {"addon": "One additional dedicated email campaign tied to a specific program, such as a wine dinner."},
                ]),
                ("Winery Participation", [
                    "Friday Lobby Wine Pours are hosted weekly by your winery, with preference for a winemaker or principal to be present",
                    "Collaborate with the Appellation team by providing marketing assets, photography, brand information, and event details to support promotional efforts",
                    "Market involvement with Appellation Healdsburg: being a featured winery of the month, participating in Yappy Hour and Neighbor Night, and similar programming",
                    {"addon": "Yappy Hour: if your winery chooses to take part, you will be responsible for donating two cases (two SKUs) of wine and having someone on hand to pour."},
                ]),
            ],
            "contact": {"name": "Tess Housholder", "title": "Sommelier, Appellation Healdsburg", "email": "tess.housholder@appellationhotels.com"},
            "submit_text": "Use the form below to share marketing assets, photography, brand information, and event details for your Appellation Healdsburg Winery of the Month partnership.",
        },
    },
    "lodi": {
        "name": "Appellation Lodi",
        "eyebrow": "Appellation Lodi &nbsp;&middot;&nbsp; Wine &amp; Roses",
        "footer": "Appellation Lodi &nbsp;&middot;&nbsp; Wine &amp; Roses",
        "detail_labels": {"nn_wine": "By the Glass Wines", "friday_wine": "Friday Reception Wine"},
        "recurring": ["Neighbor Nights &middot; Sundays and Mondays", "Friday Wine Reception &middot; 4 to 5 pm", "Three wines by the glass per partner", "American Fare &middot; May 2027"],
        "form_url": "https://forms.clickup.com/9014048227/f/8cmexf3-4974/FULVFIN59G0BM1XJEO",
        "schedule_path": "lodi/schedule",
        "schedules": [
            {"year": 2027, "path": "lodi/schedule-2027", "range": "January&ndash;December 2027",
             "months": LO_2027, "dinners": LO_2027_DINNERS,
             "blurb": "Twelve months of featured wineries, season notes, and quarterly wine dinners."},
        ],
        "partnership": {
            "path": "lodi/partnership",
            "sub": "Featured Winery Partnership &nbsp;&middot;&nbsp; 2027 Program",
            "intro": "Appellation Lodi is rooted in relationships with the multi-generational growers and independent producers who give the Lodi appellation its character. As Winery of the Month, your story is woven into the guest experience for a full month, across Americana House and beyond.",
            "provides_title": "Appellation Lodi Provides",
            "provides": [
                ("Prominent Exposure", [
                    "Featured Winery of the Month page on the Americana House wine list",
                    "Dedicated landing page on the Appellation Lodi website as the month's featured winery partner",
                    "Inclusion in Appellation Lodi email marketing campaigns throughout the month",
                    "One collaborative social post or reel, produced by the Appellation team and shared from both accounts",
                ]),
                ("Programming &amp; Events", [
                    "Exclusive winery partner for Neighbor Nights, held Sundays and Mondays, with three by-the-glass offerings",
                    "Friday Wine Reception pours, hosted weekly from 4 to 5 pm",
                ]),
            ],
            "commits": [
                ("Wine Support", ["Offer three wines to be poured by the glass"]),
                ("Guest Experience", [
                    "Provide an exclusive tasting experience for Appellation guests (e.g., two-for-one tasting, complimentary tasting upgrade, library tasting)",
                ]),
                ("Marketing Commitments", [
                    "One dedicated in-feed social post or reel from your winery's channels",
                    "One dedicated email campaign at the start of the month, featuring the wine and the month's programming",
                ]),
                ("Winery Participation", [
                    "Friday Reception Wine Pours are hosted weekly by your winery from 4 to 5 pm, with preference for a winemaker or principal to be present",
                    "Collaborate with the Appellation team by providing marketing assets, photography, brand information, and event details to support promotional efforts",
                    "Market involvement with Appellation Lodi, being a featured winery of the month, participating in Neighbor Nights and similar programming",
                ]),
            ],
            "contact": {"name": "Victoria Klein", "title": None, "email": "victoriak@winerose.com"},
            "submit_text": "Use the form below to share marketing assets, photography, brand information, and event details for your Appellation Lodi Winery of the Month partnership.",
        },
    },
}

# Old URLs that must keep working. Each becomes a redirect page.
REDIRECTS = {
    "schedule": "healdsburg/schedule#2026",
    "partnership": "healdsburg/partnership",
    "healdsburg/schedule-2027": "healdsburg/schedule#2027",
    "healdsburg/schedule-2026": "healdsburg/schedule#2026",
    "lodi/schedule-2027": "lodi/schedule#2027",
}
