# -*- coding: utf-8 -*-
"""Generate the Jacksonville NC Fence Company static site."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://www.jacksonvillencfence.com"
NAME = "Jacksonville NC Fence Company"
PHONE = "(910) 519-2447"
TEL = "+19105192447"
TALLY = (
    "https://tally.so/embed/xX6B0y?alignLeft=1&hideTitle=1"
    "&transparentBackground=1&dynamicHeight=1&source=Jacksonville+NC+Fence+Company"
)

SERVICES = [
    ("services.html", "All services"),
    ("vinyl-fence.html", "Vinyl fencing"),
    ("wood-fence.html", "Wood fencing"),
    ("chain-link-fence.html", "Chain-link fencing"),
    ("aluminum-fence.html", "Aluminum fencing"),
    ("farm-fence.html", "Farm fencing"),
    ("commercial-fencing.html", "Commercial fencing"),
]
FOOTER_SERVICES = [s for s in SERVICES if s[0] != "services.html"]

LOCATIONS = [
    ("fence-company-swansboro-nc.html", "Swansboro"),
    ("fence-company-richlands-nc.html", "Richlands"),
    ("fence-company-holly-ridge-nc.html", "Holly Ridge"),
    ("fence-company-sneads-ferry-nc.html", "Sneads Ferry"),
    ("fence-company-hubert-nc.html", "Hubert"),
    ("fence-company-piney-green-nc.html", "Piney Green"),
    ("fence-company-midway-park-nc.html", "Midway Park"),
    ("fence-company-onslow-county-nc.html", "Onslow County"),
]

PHONE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
MENU_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg>'


def canonical(path):
    if path in ("", "index.html"):
        return SITE + "/"
    return SITE + "/" + path


def quote_btn(current):
    href = "#quote" if current == "index.html" else "contact.html#quote"
    return f'<a class="btn btn-primary" href="{href}">Get a free quote</a>'


def call_btn(cls="btn btn-ghost"):
    return f'<a class="{cls}" href="tel:{TEL}">{PHONE_SVG}{PHONE}</a>'


def tally_block():
    return f'''<div class="quote-card" id="quote">
      <h2>Get a free quote</h2>
      <p class="quote-note">Tell us the town, the fence type, and roughly how much line you need.</p>
      <iframe data-tally-src="{TALLY}" loading="lazy" width="100%" height="552" frameborder="0" marginheight="0" marginwidth="0" title="Get a free quote"></iframe>
    </div>'''


def crumbs(items):
    parts = ['<a href="index.html">Home</a>']
    for href, label in items[:-1]:
        parts.append(f'<a href="{href}">{label}</a>')
    parts.append(items[-1][1])
    inner = " / ".join(parts)
    return f'<p class="crumbs">{inner}</p>'


def faq_cards(items):
    blocks = []
    for q, a in items:
        blocks.append(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>')
    return '<div class="faq-grid">' + "".join(blocks) + "</div>"


def header(current):
    def link(href, label):
        cur = ' aria-current="page"' if href == current else ""
        return f'<a href="{href}"{cur}>{label}</a>'

    svc_links = "".join(link(h, l) for h, l in SERVICES)
    loc_links = link("service-areas.html", "All service areas") + "".join(
        link(h, l) for h, l in LOCATIONS
    )
    quote_href = "#quote" if current == "index.html" else "contact.html#quote"
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="topbar">
    <div class="container topbar-inner">
      <span>Free estimates in Jacksonville and Onslow County</span>
      <a href="tel:{TEL}">{PHONE}</a>
    </div>
  </div>
  <div class="container header-inner">
    <a class="logo-link" href="index.html" aria-label="{NAME} home"><img src="logo.svg" alt="{NAME}" width="280" height="60"></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">{MENU_SVG}</button>
    <nav class="nav" id="site-nav" aria-label="Primary">
      {link("index.html", "Home")}
      <details>
        <summary>Services</summary>
        <div class="nav-panel">{svc_links}</div>
      </details>
      <details>
        <summary>Service area</summary>
        <div class="nav-panel">{loc_links}</div>
      </details>
      {link("faq.html", "FAQ")}
      {link("about.html", "About")}
      {link("contact.html", "Contact")}
    </nav>
    <div class="header-actions">
      {call_btn()}
      <a class="btn btn-primary" href="{quote_href}">Get a free quote</a>
    </div>
  </div>
</header>'''


def footer():
    services = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in FOOTER_SERVICES)
    return f'''<footer class="site-footer">
  <div class="footer-accent"></div>
  <div class="container footer-grid">
    <div>
      <h2>Company</h2>
      <img src="logo.svg" alt="" width="280" height="60">
      <p style="margin-top:0.9rem">Fence installation and repair for homes, farms, and commercial lots in Jacksonville, NC and nearby Onslow County.</p>
      <a class="footer-phone" href="tel:{TEL}">{PHONE}</a>
      <ul style="margin-top:0.8rem">
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>
    <div>
      <h2>Services</h2>
      <ul>{services}</ul>
    </div>
    <div>
      <h2>Quick links</h2>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="services.html">Services</a></li>
        <li><a href="faq.html">FAQ</a></li>
        <li><a href="service-areas.html">Service areas</a></li>
        <li><a href="privacy.html">Privacy</a></li>
        <li><a href="sitemap.xml">Sitemap</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer-base">
    <p>© 2026 {NAME}.</p>
    <p><a href="sitemap.xml">XML sitemap</a> · <a href="robots.txt">robots.txt</a></p>
  </div>
</footer>
<nav class="callbar" aria-label="Call or request a quote">
  <a class="btn btn-ink" href="tel:{TEL}">{PHONE_SVG}Call</a>
  <a class="btn btn-primary" href="contact.html#quote">Free quote</a>
</nav>'''


TALLY_SCRIPT = '''<script>var d=document,w="https://tally.so/widgets/embed.js",v=function(){"undefined"!=typeof Tally?Tally.loadEmbeds():d.querySelectorAll("iframe[data-tally-src]:not([src])").forEach((function(e){e.src=e.dataset.tallySrc}))};if("undefined"!=typeof Tally)v();else if(d.querySelector('script[src="'+w+'"]')==null){var s=d.createElement("script");s.src=w,s.onload=v,s.onerror=v,d.body.appendChild(s);}</script>'''


def layout(filename, title, description, body, graph, og_image="/images/wood-privacy.jpg"):
    url = canonical(filename)
    schema = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="{NAME}">
  <meta property="og:image" content="{SITE}{og_image}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
  <script type="application/ld+json">{schema}</script>
</head>
<body>
{header(filename)}
<main id="main">
{body}
</main>
{footer()}
<script src="main.js"></script>
{TALLY_SCRIPT}
</body>
</html>
'''
    (ROOT / filename).write_text(html, encoding="utf-8")
    print("wrote", filename)


def business_node():
    areas = [
        {"@type": "City", "name": "Jacksonville, NC"},
        {"@type": "AdministrativeArea", "name": "Onslow County, NC"},
    ]
    for _, name in LOCATIONS:
        if name == "Onslow County":
            continue
        areas.append({"@type": "City", "name": f"{name}, NC"})
    catalog = []
    for i, (href, label) in enumerate(FOOTER_SERVICES, start=1):
        catalog.append({
            "@type": "Offer",
            "itemOffered": {
                "@type": "Service",
                "@id": canonical(href) + "#service",
                "name": label + " in Jacksonville, NC",
                "url": canonical(href),
                "provider": {"@id": SITE + "/#business"},
            },
        })
    return {
        "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
        "@id": SITE + "/#business",
        "name": NAME,
        "url": SITE + "/",
        "telephone": "+1-910-519-2447",
        "image": SITE + "/images/wood-privacy.jpg",
        "logo": SITE + "/logo.svg",
        "description": "Fence installation and repair for homes, farms, and commercial lots in Jacksonville, North Carolina and nearby Onslow County. Service-area business with no public storefront.",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Jacksonville",
            "addressRegion": "NC",
            "addressCountry": "US",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": 34.7540524, "longitude": -77.4302414},
        "areaServed": [
            {
                "@type": "GeoCircle",
                "name": "About 25 miles around Jacksonville, North Carolina",
                "geoMidpoint": {"@type": "GeoCoordinates", "latitude": 34.7540524, "longitude": -77.4302414},
                "geoRadius": 40234,
            },
            *areas,
        ],
        "knowsAbout": [
            "Wood fence installation",
            "Vinyl fence installation",
            "Chain-link fence installation",
            "Aluminum fence installation",
            "Farm fencing",
            "Commercial fencing",
            "Fence repair",
            "Sandy coastal soil fence posts",
            "Onslow County fence rules",
            "City of Jacksonville NC fence height limits",
        ],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Fence installation and repair",
            "itemListElement": catalog,
        },
        "potentialAction": {
            "@type": "CommunicateAction",
            "name": "Request a fence estimate",
            "target": SITE + "/contact.html",
        },
    }


def webpage(filename, name, description, main_id):
    return {
        "@type": "WebPage",
        "@id": canonical(filename) + "#webpage",
        "url": canonical(filename),
        "name": name,
        "description": description,
        "isPartOf": {"@id": SITE + "/#website"},
        "about": {"@id": main_id},
        "publisher": {"@id": SITE + "/#business"},
        "inLanguage": "en-US",
    }


def website_node():
    return {
        "@type": "WebSite",
        "@id": SITE + "/#website",
        "url": SITE + "/",
        "name": NAME,
        "publisher": {"@id": SITE + "/#business"},
        "inLanguage": "en-US",
    }


def crumbs_schema(filename, trail):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    for i, (href, label) in enumerate(trail, start=2):
        items.append({"@type": "ListItem", "position": i, "name": label, "item": canonical(href) if href else canonical(filename)})
    return {"@type": "BreadcrumbList", "@id": canonical(filename) + "#breadcrumb", "itemListElement": items}


def faq_schema(filename, items):
    return {
        "@type": "FAQPage",
        "@id": canonical(filename) + "#faq",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ],
    }


HOME_FAQS = [
    (
        "How much does a fence cost in Jacksonville, NC?",
        "The price follows the line we measure: length, height, material, gates, and whether an old fence has to come out. Sandy soil, a slope, tree roots, and a long carry from the street change the labor. We do not publish a per-foot menu. The estimate comes from the property.",
    ),
    (
        "Can you install a fence in the sandy soil around Onslow County?",
        "Yes. Most lots from Jacksonville out toward the river sit on coastal-plain sand, and some low yards hold water after a hard rain. Posts go in concrete, deep enough to stay put, with the mix crowned so water does not pool at the post. If a stretch stays soft or saturated, we say so before we set it.",
    ),
    (
        "Do you offer wood, vinyl, chain link, aluminum, and farm fencing?",
        "Yes. Wood and vinyl cover privacy and picket work. Chain link covers yards, dogs, and commercial perimeters. Aluminum covers open ornamental lines and pools. Farm fencing covers rail, wire, pipe-and-cable, and electric for animals on larger parcels. Repair work is part of the same call.",
    ),
    (
        "Do I need a permit to put up a fence in Jacksonville or Onslow County?",
        "Inside the City of Jacksonville, published standards limit a residential front-yard fence to 4 feet and a side or rear fence to 6 feet, and the fence cannot sit in an easement, a sidewalk, or the right-of-way. In unincorporated Onslow County, the county says a zoning permit is not required for a fence. An HOA can be stricter than either one. Confirm the rule for your parcel before posts go in.",
    ),
    (
        "Can you repair a storm-damaged fence, or does the whole line have to come out?",
        "If the posts are still sound, we replace the panels, rails, or gate that failed and leave the rest. If the posts have rotted or pulled out of the sand, new boards on those posts will lean again, and that stretch should be rebuilt. We will tell you which it is after we see the line.",
    ),
]


def home():
    cards = [
        ("vinyl-fence.html", "images/vinyl-privacy.jpg", "White vinyl fence with a scalloped top along a grassy yard", "Vinyl fencing", "Privacy, picket, and ranch-rail vinyl for a straight line without a yearly stain. A practical fit for humid Onslow County summers."),
        ("wood-fence.html", "images/wood-privacy.jpg", "Wood privacy fence with vertical boards and square posts", "Wood fencing", "Privacy, picket, and shadowbox wood you can stain to the house. Posts are set in concrete for sandy coastal-plain soil."),
        ("chain-link-fence.html", "images/chain-link.jpg", "Galvanized chain-link fence running beside a walk", "Chain-link fencing", "Galvanized and vinyl-coated chain link for yards, dogs, and work lots. A screen can be added where you need a visual break."),
        ("aluminum-fence.html", "images/aluminum.jpg", "Black ornamental aluminum fence behind a trimmed hedge", "Aluminum fencing", "Open aluminum for front yards, pools, and sloped lines. It stays straight in humidity and does not need paint."),
        ("farm-fence.html", "images/farm-rail.jpg", "Split-rail wood fence along a grassy field", "Farm fencing", "Split rail, woven wire, pipe-and-cable, and electric fence for horses, cattle, and acreage around rural Onslow County."),
        ("commercial-fencing.html", "images/chain-link-run.jpg", "Long run of chain-link fence along a paved walk", "Commercial fencing", "Heavier chain link, vehicle gates, and screens for yards and job sites. Built to a commercial spec, not a backyard panel."),
    ]
    card_html = []
    for href, img, alt, title, text in cards:
        card_html.append(f'''<a class="service-card" href="{href}">
        <span class="media"><img src="{img}" alt="{alt}" width="925" height="615" loading="lazy"></span>
        <span class="body"><h3>{title}</h3><p>{text}</p><span class="more">View service</span></span>
      </a>''')
    gallery = [
        ("images/wood-privacy.jpg", "Wood privacy fence with vertical boards"),
        ("images/vinyl-privacy.jpg", "White vinyl fence along a lawn"),
        ("images/vinyl-picket.jpg", "Black vinyl picket fence in front of a garden"),
        ("images/chain-link.jpg", "Chain-link fence with metal posts"),
        ("images/aluminum.jpg", "Black aluminum fence with vertical pickets"),
        ("images/farm-rail.jpg", "Split-rail fence in a grassy field"),
    ]
    ghtml = "".join(
        f'<figure><img src="{src}" alt="{alt}" loading="lazy"></figure>' for src, alt in gallery
    )
    chips = "".join(f'<li><a href="{h}">{n}</a></li>' for h, n in LOCATIONS)
    desc = "Jacksonville NC Fence Company installs and repairs wood, vinyl, chain-link, aluminum, and farm fencing in Jacksonville and Onslow County. Call (910) 519-2447."
    body = f'''<section class="hero">
  <div class="hero-media"><img src="images/wood-privacy.jpg" alt="Wood privacy fence with vertical boards and square posts" width="926" height="615" fetchpriority="high"></div>
  <div class="hero-shade"></div>
  <div class="container hero-grid">
    <div>
      <p class="eyebrow">Jacksonville, North Carolina</p>
      <h1>Fence company in Jacksonville, NC</h1>
      <p class="lede">Wood, vinyl, chain-link, aluminum, and farm fencing for houses and commercial lots. New lines, replacements, repairs, and gates are quoted from the property.</p>
      <div class="hero-actions">
        {call_btn("btn btn-primary btn-lg")}
        <a class="btn btn-ghost btn-lg" href="contact.html#quote">Request an estimate</a>
      </div>
      <ul class="hero-points">
        <li>Homes, farms, and commercial lots</li>
        <li>Posts set for coastal-plain sand</li>
        <li>Free on-site estimates</li>
      </ul>
    </div>
    {tally_block()}
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="kicker">Materials and work</p>
      <h2>Fence services in Jacksonville</h2>
      <p>Start with the job. A backyard screen, a pool barrier, a dog run, and a pasture line are not the same fence.</p>
    </div>
    <div class="card-grid services">{"".join(card_html)}</div>
  </div>
</section>
<section class="band">
  <div class="container section">
    <div class="section-head">
      <p class="kicker">Styles</p>
      <h2>Fences we install</h2>
      <p>Privacy, vinyl, chain link, aluminum, and rail from the crew that walks the line in Jacksonville and Onslow County.</p>
    </div>
    <div class="gallery">{ghtml}</div>
  </div>
</section>
<section class="section soft">
  <div class="container split-2">
    <div>
      <h2>Houses</h2>
      <p>Backyard privacy, pet runs, pool barriers, and property-line replacements. Most in-town jobs are a 6-foot wood or vinyl line on the side and rear, with a gate that fits the mower. Front yards inside the city stay at the 4-foot limit.</p>
      <a class="more" href="wood-fence.html">Wood fencing</a>
    </div>
    <div>
      <h2>Lots and acreage</h2>
      <p>A storage yard needs heavier chain link and a vehicle gate. A pasture in Richlands or Hubert needs wire or rail sized for the animals, not a backyard panel. Tell us how the ground is used and we will spec the line for that use.</p>
      <a class="more" href="commercial-fencing.html">Commercial fencing</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="container split-2">
    <div>
      <h2>How a fence job is quoted</h2>
      <ol class="steps">
        <li><span class="num">1</span><span><strong>Name the job.</strong> Screen, contain animals, mark a line, or secure a lot. That choice picks the material faster than a photo.</span></li>
        <li><span class="num">2</span><span><strong>Walk the ground.</strong> Sand, standing water, slope, trees, and the distance from the driveway all change the posts and the labor.</span></li>
        <li><span class="num">3</span><span><strong>Count the openings.</strong> A fence with the wrong gate is a daily problem. Walk gates and drive gates are priced as their own pieces.</span></li>
        <li><span class="num">4</span><span><strong>Repair or replace.</strong> Sound posts can take new panels. Posts that have failed in the sand cannot. We say which one you have.</span></li>
      </ol>
    </div>
    <div class="panel">
      <h2>Repairs and gates</h2>
      <p>Leaning posts, missing boards, and sagging gates are a large share of the calls after a storm. If the rest of the line is sound, we repair the failed section. If the posts have let go, we will tell you to rebuild that run.</p>
      <p>Gates are hung on posts sized for the opening, with hardware that can carry the weight. A walk gate and a drive gate are different builds.</p>
      <a class="more" href="contact.html#quote">Request an estimate</a>
    </div>
  </div>
</section>
<section class="band">
  <div class="container section">
    <h2>Service area</h2>
    <p>We work in Jacksonville and nearby communities, roughly a 25-mile drive. Each town puts a different demand on the fence: salt air near the water, HOA rules in subdivisions, and longer farm lines inland.</p>
    <ul class="chips">{chips}</ul>
    <p style="margin-top:1rem"><a href="service-areas.html" style="color:white">All service areas</a></p>
  </div>
</section>
<section class="section">
  <div class="container">
    <h2>Questions before you call</h2>
    <div style="margin-top:1.2rem">{faq_cards(HOME_FAQS)}</div>
    <p style="margin-top:1rem"><a href="faq.html">More fence questions</a></p>
  </div>
</section>
<section class="cta-band">
  <div class="container cta-inner">
    <div>
      <h2>Ready to walk the line?</h2>
      <p>Call {PHONE} or send the lot details. Estimates are free.</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-primary btn-lg" href="#quote">Get a free quote</a>
      {call_btn("btn btn-ink btn-lg")}
    </div>
  </div>
</section>'''
    graph = [
        business_node(),
        website_node(),
        webpage("index.html", "Fence company in Jacksonville, NC", desc, SITE + "/#business"),
        faq_schema("index.html", HOME_FAQS),
    ]
    layout("index.html", "Fence Company in Jacksonville, NC | Jacksonville NC Fence Company", desc, body, graph)


def steps(items):
    lis = []
    for i, (title, text) in enumerate(items, start=1):
        lis.append(f'<li><span class="num">{i}</span><span><strong>{title}</strong> {text}</span></li>')
    return '<ol class="steps">' + "".join(lis) + "</ol>"


def factors(items):
    blocks = []
    for title, text in items:
        blocks.append(f'<article class="factor"><h3>{title}</h3><p>{text}</p></article>')
    return '<div class="factor-grid">' + "".join(blocks) + "</div>"


def related(links):
    bits = " · ".join(f'<a href="{h}">{l}</a>' for h, l in links)
    return f'<p style="margin-top:1rem">Related: {bits}</p>'


def service_layout(s):
    filename = s["file"]
    desc = s["description"]
    faqs = s["faqs"]
    body = f'''<section class="page-hero">
  <div class="container">
    {crumbs([("services.html", "Services"), (filename, s["crumb"])])}
    <h1>{s["h1"]}</h1>
    <p class="lede">{s["intro"]}</p>
    <div class="hero-actions">
      {call_btn("btn btn-primary btn-lg")}
      <a class="btn btn-ghost btn-lg" href="contact.html#quote">Get a free quote</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="container split">
    <div class="split-media"><img src="{s["image"]}" alt="{s["alt"]}" width="925" height="615"></div>
    <div class="prose">
      <h2>When this fence is the right job</h2>
      <p>{s["when"]}</p>
    </div>
  </div>
</section>
<section class="section soft">
  <div class="container prose">
    <h2>How the work goes</h2>
    {steps(s["process"])}
    <div style="margin-top:1.2rem">{s["after"]}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <h2>What changes the estimate</h2>
      <p>We price the line on your lot. These are the pieces that move the number.</p>
    </div>
    {factors(s["factors"])}
  </div>
</section>
<section class="section soft">
  <div class="container">
    <h2>Questions about {s["faq_label"]}</h2>
    <div style="margin-top:1.2rem">{faq_cards(faqs)}</div>
    {related(s["related"])}
  </div>
</section>
<section class="cta-band">
  <div class="container cta-inner">
    <div>
      <h2>Get an estimate for this fence</h2>
      <p>Call {PHONE} or send the town, the approximate length, and the gate count.</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-primary btn-lg" href="contact.html#quote">Get a free quote</a>
      {call_btn("btn btn-ink btn-lg")}
    </div>
  </div>
</section>'''
    graph = [
        business_node(),
        webpage(filename, s["h1"], desc, canonical(filename) + "#service"),
        {
            "@type": "Service",
            "@id": canonical(filename) + "#service",
            "name": s["h1"],
            "description": desc,
            "url": canonical(filename),
            "provider": {"@id": SITE + "/#business"},
            "areaServed": {"@type": "AdministrativeArea", "name": "Onslow County, NC"},
            "serviceType": s["crumb"],
        },
        crumbs_schema(filename, [("services.html", "Services"), (filename, s["crumb"])]),
        faq_schema(filename, faqs),
    ]
    layout(filename, s["title"], desc, body, graph, og_image="/" + s["image"])


SERVICES_DATA = [
    {
        "file": "wood-fence.html",
        "title": "Wood Fence Installation in Jacksonville, NC",
        "description": "Wood privacy, picket, and shadowbox fences in Jacksonville, NC. Posts set in concrete for sandy soil. Call (910) 519-2447 for a free estimate.",
        "h1": "Wood fence installation in Jacksonville, NC",
        "crumb": "Wood fencing",
        "faq_label": "wood fencing",
        "image": "images/wood-privacy.jpg",
        "alt": "Wood privacy fence with vertical boards, rails, and square posts",
        "intro": "Privacy, picket, and shadowbox wood for Jacksonville yards that want a solid screen and a fence you can stain to the house. We measure the line, set the posts for sand, and price the gates separately.",
        "when": "Choose wood when the job is a backyard screen, a stained match to the house, or a repair on a wood line that still has sound posts. Inside the City of Jacksonville, side and rear residential fences are limited to 6 feet, and front-yard fences are limited to 4 feet. A tall privacy fence belongs behind the front wall of the house.",
        "process": [
            ("Walk the line.", "We note the slope, trees, sprinklers, gates, and who owns the property line."),
            ("Check the rule.", "City height limits, county easements, and any HOA color or material sheet come before the lumber order."),
            ("Set the posts.", "Posts go in concrete, crowned at the top, deep enough for coastal-plain sand."),
            ("Hang the fence and the gate.", "Rails, boards, and a gate that latches without dragging on the ground."),
            ("Walk it with you.", "We point out what to stain and which boards sit closest to sprinklers."),
        ],
        "after": "<p>A privacy style sets the boards tight so the yard is screened. Shadowbox staggers boards on both faces so neighbors on each side see a finished side and a little air can pass. Picket is the shorter open fence for a front yard. The style is part of the quote, because board count and both-side nailing change the material.</p>",
        "factors": [
            ("Length and height", "A 6-foot privacy run uses more board than a 4-foot picket on the same line."),
            ("Style", "Privacy, shadowbox, and picket do not share a board count or a rail layout."),
            ("Gates", "Each walk gate and drive gate is its own frame, posts, and hardware."),
            ("Tear-out", "Hauling off an old fence, including posts in concrete, is a separate piece of the job."),
            ("Ground", "Slope, roots, and soft spots add time. A flat side yard does not price like a ditch line."),
            ("Access", "A long carry from the street, or a backyard with no gate yet, takes more labor."),
        ],
        "faqs": [
            ("How long does a wood fence hold up in Jacksonville humidity?", "Humidity and summer rain are what age a bare board. A finish renewed before the wood cracks is what keeps a privacy fence in service. Shade, sprinklers, and how often you stain it matter more than a catalog year-count, so we do not promise a lifespan."),
            ("Can you repair part of a wood fence instead of replacing the line?", "Yes, when the posts are still solid. We can replace rails, boards, or a gate and leave the sound sections. If a post has rotted at the ground, new boards on that post will lean again. We say which it is after we see the line."),
            ("What is the difference between privacy, shadowbox, and picket?", "Privacy boards sit tight and screen the yard. Shadowbox staggers boards on both sides of the rail so each neighbor sees a finished face. Picket is a shorter, open fence used where a front yard has a lower height limit."),
            ("Do wood posts need concrete in Onslow County sand?", "Yes on a residential line. Coastal-plain sand does not grip a post the way clay does. We set posts in concrete and crown the top so water does not sit against the wood."),
            ("Will a solid wood fence handle wind off the coast?", "A solid fence catches wind. On an open lot we space posts for that load instead of stretching a tall run between too few posts. Shadowbox lets some air through and is sometimes the better build on an exposed side line."),
        ],
        "related": [("vinyl-fence.html", "Vinyl fencing"), ("aluminum-fence.html", "Aluminum fencing"), ("farm-fence.html", "Farm fencing")],
    },
    {
        "file": "vinyl-fence.html",
        "title": "Vinyl Fence Installation in Jacksonville, NC",
        "description": "Vinyl privacy, picket, and ranch-rail fences in Jacksonville, NC. Low upkeep for humid Onslow County yards. Call (910) 519-2447.",
        "h1": "Vinyl fence installation in Jacksonville, NC",
        "crumb": "Vinyl fencing",
        "faq_label": "vinyl fencing",
        "image": "images/vinyl-privacy.jpg",
        "alt": "White vinyl fence with decorative tops along a lawn",
        "intro": "Vinyl privacy, picket, and ranch rail for homeowners who want a straight fence without a stain schedule. We match the style to the yard, the HOA sheet, and the slope before any panels are ordered.",
        "when": "Vinyl fits a yard where painting is the chore you want off the list. It is a common privacy fence in Jacksonville subdivisions and a common ranch-rail edge on a larger lot. It is a poor swap onto old wood posts. A vinyl line gets its own posts.",
        "process": [
            ("Confirm style and color.", "Privacy, picket, or ranch rail, in the color the house or the HOA already named."),
            ("Read the grade.", "Racked panels follow a slope. Stepped panels leave a gap under each section. We pick one before ordering."),
            ("Set vinyl posts.", "Posts are set in concrete on layout, not bolted to whatever wood is already in the ground."),
            ("Assemble panels and gates.", "Rails, pickets or privacy boards, and gates hung so the latch meets the strike."),
            ("Check the line.", "We look for gaps at the grade, racked sections that bind, and gates that drag."),
        ],
        "after": "<p>Privacy panels screen a patio or a neighbor. Picket and ranch rail stay open, which suits a front yard under the city’s 4-foot front-yard limit or a pasture edge you are marking more than hiding. Dark colors absorb more sun. If the HOA allows white, tan, or black, we talk through which face of the yard sits in full afternoon light.</p>",
        "factors": [
            ("Style", "Privacy panels, picket, and two-, three-, or four-rail ranch styles do not share a price."),
            ("Height", "A 6-foot privacy line is a different product from a 4-foot front-yard picket."),
            ("Color", "Standard whites are easier to source than a matched accent color. We order what was approved."),
            ("Grade", "A yard that falls toward a swale needs racked or stepped sections. Flat ground does not."),
            ("Gates and tear-out", "Gate count and removal of the old fence are separate from the panel price."),
            ("Carry", "Panels are bulky. A backyard with no access from the driveway takes more time."),
        ],
        "faqs": [
            ("Does vinyl make sense in Onslow County heat?", "Vinyl does not need stain, and it does not rot the way bare wood does. Dark colors run hotter in full sun. We look at the color an HOA allows and which side of the yard takes the afternoon light before you order."),
            ("Can vinyl follow a sloped yard?", "Some systems rack and some have to be stepped. A lot that falls toward a ditch needs that choice made before the material is ordered. Stepped panels leave a triangular gap. Racked panels follow the grade."),
            ("Is vinyl only a privacy fence?", "No. Full privacy panels screen a backyard. Picket and ranch rail are open styles for front yards and for lines where you are marking a boundary more than hiding the yard."),
            ("Can you put vinyl panels on my old wood posts?", "Usually no. A vinyl system is built for its own posts, and the old wood posts are often the part that failed. A vinyl replacement is a new post layout, not a board swap."),
            ("What changes the price of a vinyl fence?", "Length, height, style, gate count, and whether the old fence comes out. Slope, roots, and a long carry from the driveway add labor. We price the line we measure."),
        ],
        "related": [("wood-fence.html", "Wood fencing"), ("aluminum-fence.html", "Aluminum fencing"), ("commercial-fencing.html", "Commercial fencing")],
    },
    {
        "file": "chain-link-fence.html",
        "title": "Chain-Link Fence Installation in Jacksonville, NC",
        "description": "Chain-link fence installation in Jacksonville, NC for yards, dogs, and commercial lots. Galvanized and vinyl-coated. Call (910) 519-2447.",
        "h1": "Chain-link fence installation in Jacksonville, NC",
        "crumb": "Chain-link fencing",
        "faq_label": "chain-link fencing",
        "image": "images/chain-link.jpg",
        "alt": "Galvanized chain-link fence with metal line posts",
        "intro": "Chain link for residential yards, dog runs, and commercial perimeters. Galvanized is the basic fabric. Vinyl-coated fabric is the better spec where salt air reaches the lot.",
        "when": "Use chain link when you need a boundary, a dog run, or a secure lot and you do not need a solid screen. It is the wrong product if the goal is to block the neighbor’s view, unless a windscreen is added and the frame is built for that wind load. Commercial fabric and terminal posts are heavier than a backyard kit.",
        "process": [
            ("Mark the line and the openings.", "Corners, ends, and gates are laid out before any post is set."),
            ("Set terminal posts.", "End, corner, and gate posts go in concrete. They carry the tension."),
            ("Set line posts and rail.", "The framework goes in, then the fabric is stretched and tied."),
            ("Hang the gates.", "Gates sit on posts sized for the opening, not on a light line post."),
            ("Add coating or screen if it is part of the job.", "Vinyl-coated fabric or a privacy screen is decided up front, not bolted on a frame that cannot hold it."),
        ],
        "after": "<p>Residential chain link is a common side-yard and dog fence in Jacksonville. Closer to Sneads Ferry, Swansboro, and the New River, salt air shortens the life of bare steel, so a vinyl-coated fabric is worth specifying. Inland, toward Richlands, galvanized is usually enough. A privacy screen turns the fence into a sail. That is a commercial-grade conversation, not a slat pack on a light frame.</p>",
        "factors": [
            ("Height and gauge", "A 4-foot residential run and a taller commercial fabric are different steel."),
            ("Coating", "Galvanized and vinyl-coated fabric do not cost the same, and the coast pushes the choice."),
            ("Framework", "Terminal posts, rail, and tension wire are what keep the fabric from sagging."),
            ("Gates", "A walk gate is simple. A double drive gate needs posts that can carry it."),
            ("Screen", "Privacy slats or a windscreen add material and a wind load the posts must hold."),
            ("Ground", "Soft sand, roots, and a slope change post depth and how the fabric is stretched."),
        ],
        "faqs": [
            ("Is chain link only for commercial lots?", "No. It is a common residential fence for dogs, side yards, and people who want a boundary without a solid wall. Commercial work uses a heavier framework, taller fabric, and gates sized for trucks."),
            ("Can you add privacy to chain link?", "A screen can block the view. It also catches wind, so the posts and rails have to be up to that load. A screen on a light residential frame is a different job than a screen on a commercial line."),
            ("Which coating holds up near the coast?", "Bare galvanized is the basic product. Closer to Sneads Ferry, Swansboro, and the river, vinyl-coated fabric resists corrosion longer. Inland Richlands and much of Jacksonville can use galvanized when salt exposure is low."),
            ("How is a chain-link install sequenced?", "We mark the line, set terminal posts in concrete, add line posts and rail, then stretch the fabric and tie it off. Gates hang on posts sized for the opening."),
            ("Can chain link sit on the property line?", "In Jacksonville, a fence may sit on the line if it stays out of easements, sidewalks, and the right-of-way. In unincorporated Onslow County a zoning permit is not required and the ordinance does not set a fence location. The line still has to be yours. A survey beats a guess."),
        ],
        "related": [("commercial-fencing.html", "Commercial fencing"), ("farm-fence.html", "Farm fencing"), ("aluminum-fence.html", "Aluminum fencing")],
    },
    {
        "file": "aluminum-fence.html",
        "title": "Aluminum Fence Installation in Jacksonville, NC",
        "description": "Ornamental aluminum fences and gates in Jacksonville, NC for front yards, pools, and slopes. Call (910) 519-2447 for an estimate.",
        "h1": "Aluminum fence installation in Jacksonville, NC",
        "crumb": "Aluminum fencing",
        "faq_label": "aluminum fencing",
        "image": "images/aluminum.jpg",
        "alt": "Black ornamental aluminum fence with vertical pickets behind a hedge",
        "intro": "Ornamental aluminum for front yards, pool barriers, and lines that need to follow a slope. It stays open, so it is the fence you choose when you want the yard marked and still visible.",
        "when": "Aluminum is the right call for a 4-foot front yard inside the City of Jacksonville, a pool you need to see through, or a sloped side line where panels can rack. It is the wrong call when the job is a privacy screen. Wood or vinyl does that work. Aluminum also handles pool chemicals and humidity better than bare steel.",
        "process": [
            ("Pick the height for the yard.", "Front-yard limits and pool-barrier rules decide the height before style does."),
            ("Choose a finish.", "Black, bronze, white, khaki, and green, in gloss or satin, matched to the house or the HOA."),
            ("Lay out posts for the grade.", "Racked sections follow a mild slope. A steep drop may step."),
            ("Set posts and hang panels.", "Posts in concrete, panels and gates fastened so the latch meets."),
            ("Check pool gates when that is the job.", "A pool opening has to close and latch the way the inspector expects."),
        ],
        "after": "<p>Finishes we install most often are black, bronze, white, khaki, and green. Satin reads flatter in the sun. Gloss reads sharper. We order the color that was approved, because aluminum is not a stain-it-later material. On a pool, Onslow County requires a barrier at least 4 feet high around water 24 inches deep or more. Latch and gate hardware still have to match the code the building department is using that season.</p>",
        "factors": [
            ("Height and style", "A 4-foot open front fence and a taller pool style are different layouts."),
            ("Finish", "Standard black is easier to schedule than a less common color."),
            ("Grade", "Racking a panel down a slope takes layout time a flat run does not."),
            ("Gates", "A pool gate with self-closing hardware is a different piece from a simple walk gate."),
            ("Linear feet", "Ornamental fence is priced on the measured line, including corners."),
            ("Tear-out", "Removing an old rusted steel fence is part of the quote when it is in the way."),
        ],
        "faqs": [
            ("Is aluminum the same as wrought iron?", "No. Aluminum is the light ornamental fence that does not rust the way steel does. It is the usual choice for pools and front yards. Steel needs a different maintenance plan, especially in salt air."),
            ("Can aluminum be a pool fence?", "It is a common pool barrier because you can see through it and it handles chlorine better than steel. Onslow County requires a barrier at least 4 feet high around a pool or spa that holds 24 inches of water or more. Gate hardware still has to match the code the inspector is using."),
            ("What finishes can you install?", "The finishes we install most often are black, bronze, white, khaki, and green, in gloss or satin. We match the color to the house and to any HOA sheet before the material is ordered."),
            ("Will aluminum work on a slope?", "Ornamental aluminum can rack to follow a mild grade, which is why it fits a yard that is not flat. A steep drop may still need a stepped layout. We decide that on the lot."),
            ("Can aluminum give me backyard privacy?", "Not by itself. It is an open fence. If the job is a screen from the neighbor, wood or vinyl privacy is the product. Aluminum fits front yards, pools, and places where a shorter open fence is what the city allows."),
            ("Do city height limits affect an aluminum fence?", "Inside Jacksonville, a fence in front of the house is limited to 4 feet, and side or rear residential fences are limited to 6 feet. A 4-foot aluminum fence is a common way to mark a front yard inside that rule."),
        ],
        "related": [("vinyl-fence.html", "Vinyl fencing"), ("wood-fence.html", "Wood fencing"), ("chain-link-fence.html", "Chain-link fencing")],
    },
    {
        "file": "farm-fence.html",
        "title": "Farm Fence Installation in Jacksonville, NC",
        "description": "Farm and acreage fencing near Jacksonville, NC: split rail, woven wire, pipe-and-cable, and electric for horses and cattle. Call (910) 519-2447.",
        "h1": "Farm fence installation near Jacksonville, NC",
        "crumb": "Farm fencing",
        "faq_label": "farm fencing",
        "image": "images/farm-rail.jpg",
        "alt": "Split-rail fence running through a grassy field",
        "intro": "Rail, woven wire, pipe-and-cable, and electric fence for horses, cattle, and other animals on acreage around Jacksonville. The animal decides the fence. A backyard privacy panel does not.",
        "when": "This is the page for a pasture, a garden you need to keep deer or livestock out of, or a long property line in Richlands, Hubert, or rural Onslow County. A horse needs a fence it can see. Cattle can be held with wire or electric. Split rail marks a line and looks right, and it holds animals only when the right wire is added.",
        "process": [
            ("Name the animals.", "Horses, cattle, goats, and a garden perimeter are different fences."),
            ("Walk the corners and gates.", "Brace corners and the openings for a truck or a tractor carry the line."),
            ("Clear the path.", "Brush on the line comes out before wire goes up. We include that when it is part of the job."),
            ("Set posts and hang the fence.", "Depth follows the soil. Soft, wet ground gets a different post plan than a firm field."),
            ("Check gates and energizers.", "Electric fence is tested. Gates are hung so a truck can actually use them."),
        ],
        "after": "<p>Pipe-and-cable is a horse fence owners ask for because the rail is visible and the cable gives. Woven wire and high-tensile electric are the practical cattle options. Barbed wire is a cattle tool, not a horse fence, and on a house lot Onslow County wants barbed or electric wire on the interior side of the property and marked when it sits close to a line. A bona fide farm is treated differently. We sort that out for the parcel.</p>",
        "factors": [
            ("Length", "Acreage lines are priced on the run, and corners add bracing."),
            ("Animal", "A horse fence and a cattle fence do not share posts, wire, or spacing."),
            ("Gates", "A 12-foot farm gate is a different piece from a backyard walk gate."),
            ("Clearing", "Fence in the woods costs more than fence in an open field."),
            ("Ground", "Wet spots and sand change post depth and how many posts we set."),
            ("Power", "An electric line needs an energizer, ground rods, and a place to put them."),
        ],
        "faqs": [
            ("What fence fits horses versus cattle?", "Horses need a fence they can see and that will not cut them: pipe-and-cable, rail, or a no-climb mesh with a visible top. Cattle can be held with woven wire, barbed wire, or high-tensile electric. A horse should not live on a cattle barbed-wire line."),
            ("Is split rail enough to hold animals?", "Split rail marks a line and suits a pasture edge. It does not hold a determined horse or a small goat unless wire is added. We say which animals the style will actually contain."),
            ("Do farm fences need a permit in Onslow County?", "The county does not require a zoning permit for a fence, and bona fide farms are treated differently from a house lot on electric and barbed wire. Inside a town, ask before you build. Easements and the right-of-way are still off limits."),
            ("Can you mix a privacy fence by the house with wire on the back acreage?", "Yes. That is a common layout in Hubert and Richlands: wood or vinyl around the yard, and a farm fence on the longer field lines. They are two materials and two prices."),
            ("What changes a farm-fence estimate the most?", "Length, then corners, gates for trucks, brush that has to come off the line, and soft ground. A long wire run is not priced like a backyard."),
        ],
        "related": [("chain-link-fence.html", "Chain-link fencing"), ("wood-fence.html", "Wood fencing"), ("commercial-fencing.html", "Commercial fencing")],
    },
    {
        "file": "commercial-fencing.html",
        "title": "Commercial Fencing in Jacksonville, NC",
        "description": "Commercial chain-link, gates, and screens for lots and job sites in Jacksonville, NC. Quoted to the use of the property. Call (910) 519-2447.",
        "h1": "Commercial fencing in Jacksonville, NC",
        "crumb": "Commercial fencing",
        "faq_label": "commercial fencing",
        "image": "images/chain-link-run.jpg",
        "alt": "Long chain-link fence running along a paved walk",
        "intro": "Heavier chain link, vehicle gates, and screens for storage yards, churches, shops, and job sites in Jacksonville. A commercial lot gets a commercial spec. It does not get a backyard panel kit.",
        "when": "Call this in when trucks need a gate, the lot has to be closed after hours, or a property manager handed you a height and a fabric gauge. Inside the City of Jacksonville, nonresidential fences are allowed up to 8 feet under the published city standard. Screening around trash areas has its own material rules, and chain link with slats is not the screen those areas are supposed to use.",
        "process": [
            ("Learn the use.", "A church lot, a contractor yard, and a short-term job site are different fences."),
            ("Read any spec.", "If a general contractor or property manager has a gauge, height, or gate width, send it with the form."),
            ("Lay out gates for the vehicles that use them.", "The opening is measured for the truck, not for a catalog gate."),
            ("Set a framework that can hold the fabric.", "Terminal posts and rails are sized for the height and for any screen or wire on top."),
            ("Leave a line that latches.", "We check gates, drops, and anything that would block a drive aisle."),
        ],
        "after": "<p>Barbed wire and razor wire are commercial add-ons only where the parcel and the local rule allow them. On a residential lot, Onslow County requires barbed wire on the interior side. We do not put that material on a quote until the rule for that address is clear. Privacy screen is available on a frame built for the wind. Temporary job-site fence is available when you can tell us how long it has to stand.</p>",
        "factors": [
            ("Height and gauge", "Commercial fabric and an 8-foot line are not priced like a 4-foot yard fence."),
            ("Gates", "Vehicle gates, cantilever or swing, move the number more than the fabric does."),
            ("Top treatments", "Barbed wire or a screen is extra material and extra post strength."),
            ("Spec", "A written spec from a GC can require fittings a simple yard does not."),
            ("Access and concrete", "Existing pavement, utilities, and a live driveway change how posts go in."),
            ("Duration", "A temporary line and a permanent line are planned differently."),
        ],
        "faqs": [
            ("How is a commercial fence different from a backyard fence?", "The posts, fabric, and gates are sized for the use. A storage yard or a job site does not get a residential panel kit. Vehicle gates need posts and hinges that can carry a truck opening."),
            ("Do you install barbed wire or a privacy screen?", "Where the property and the local rules allow it, a commercial chain-link line can take a privacy screen or barbed wire. We confirm the rule for the parcel before that material goes on the quote."),
            ("Can you fence a job site for a short period?", "Temporary chain link is a normal request. Tell us how long it has to stand and whether it has to move. A temporary line still has to stay out of a sidewalk and a drive aisle."),
            ("What should I have ready for a commercial estimate?", "The address, how the lot is used, the gate width vehicles need, and any spec from a property manager or contractor. A site plan helps. We still look at the ground before we lock a number."),
            ("How tall can a commercial fence be in Jacksonville?", "Nonresidential fences in the city are allowed up to 8 feet under the published city standard. Trash-area screening has its own rules. We match the fence to the use and the standard for that parcel."),
        ],
        "related": [("chain-link-fence.html", "Chain-link fencing"), ("aluminum-fence.html", "Aluminum fencing"), ("farm-fence.html", "Farm fencing")],
    },
]


BLURBS = {
    "vinyl-fence.html": "Privacy, picket, and ranch-rail vinyl for a straight line without a yearly stain. A practical fit for humid Onslow County summers.",
    "wood-fence.html": "Privacy, picket, and shadowbox wood you can stain to the house. Posts are set in concrete for sandy coastal-plain soil.",
    "chain-link-fence.html": "Galvanized and vinyl-coated chain link for yards, dogs, and work lots. A screen can be added where you need a visual break.",
    "aluminum-fence.html": "Open aluminum for front yards, pools, and sloped lines. It stays straight in humidity and does not need paint.",
    "farm-fence.html": "Split rail, woven wire, pipe-and-cable, and electric fence for horses, cattle, and acreage around rural Onslow County.",
    "commercial-fencing.html": "Heavier chain link, vehicle gates, and screens for yards and job sites. Built to a commercial spec, not a backyard panel.",
}


def services_page():
    cards = []
    data_by_file = {s["file"]: s for s in SERVICES_DATA}
    for href, label in FOOTER_SERVICES:
        s = data_by_file[href]
        cards.append(f'''<a class="service-card" href="{href}">
        <span class="media"><img src="{s["image"]}" alt="{s["alt"]}" loading="lazy"></span>
        <span class="body"><h3>{label}</h3><p>{BLURBS[href]}</p><span class="more">View service</span></span>
      </a>''')
    desc = "Wood, vinyl, chain-link, aluminum, farm, and commercial fence installation in Jacksonville, NC. Compare services and call (910) 519-2447."
    body = f'''<section class="page-hero">
  <div class="container">
    {crumbs([("services.html", "Services")])}
    <h1>Fence services in Jacksonville, NC</h1>
    <p class="lede">Six ways to fence a property in Onslow County. Pick the material that matches the job, then open the page for process, cost factors, and the questions owners actually ask.</p>
    <div class="hero-actions">{call_btn("btn btn-primary btn-lg")} <a class="btn btn-ghost btn-lg" href="contact.html#quote">Get a free quote</a></div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="card-grid services">{"".join(cards)}</div>
  </div>
</section>'''
    graph = [business_node(), webpage("services.html", "Fence services in Jacksonville, NC", desc, SITE + "/#business"), crumbs_schema("services.html", [("services.html", "Services")])]
    layout("services.html", "Fence Services in Jacksonville, NC | Jacksonville NC Fence Company", desc, body, graph)


FAQ_PAGE = HOME_FAQS + [
    (
        "How do I get ready for a fence estimate?",
        "Know the town, about how many sides of the yard you want fenced, and whether a gate has to fit a mower, a car, or a truck. Photos of the line and of any leaning section help. We still need to see the ground before the number is final.",
    ),
    (
        "Can you add a gate to a fence that is already standing?",
        "Yes, when the posts on either side of the opening can carry a gate. A gate hung on a light line post will sag. If those posts are soft, we replace them as part of the gate, then hang hardware sized for the leaf.",
    ),
    (
        "What if my HOA has fence rules?",
        "Send the written standard before we order material. Many subdivisions around Piney Green, Western Boulevard, and Holly Ridge specify height, color, and whether the finished side faces the neighbor. We build to that sheet. We do not guess it.",
    ),
    (
        "Do you fence rental houses near Camp Lejeune?",
        "We fence off-base houses when the owner, or a tenant with the owner’s written permission, asks us to. We do not install on Camp Lejeune or New River. A landlord who wants the line back in a certain condition should say so in the request.",
    ),
    (
        "Which fence holds up better near salt air?",
        "Vinyl, aluminum, and vinyl-coated chain link handle salt better than bare steel or an unstained wood line. Lots in Sneads Ferry and Swansboro feel that more than a yard in Richlands. We pick the coating for how close the lot sits to the water.",
    ),
]


def faq_page():
    desc = "Fence cost, permits, sandy soil, HOA rules, and storm repairs in Jacksonville, NC. Answers from Jacksonville NC Fence Company. Call (910) 519-2447."
    body = f'''<section class="page-hero">
  <div class="container">
    {crumbs([("faq.html", "FAQ")])}
    <h1>Fence questions in Jacksonville, NC</h1>
    <p class="lede">Straight answers on price, permits, soil, and repairs. If your lot does not fit these, call {PHONE} and describe the line.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    {faq_cards(FAQ_PAGE)}
    <div class="cta-actions" style="margin-top:1.5rem">
      <a class="btn btn-primary" href="contact.html#quote">Get a free quote</a>
      {call_btn("btn btn-ink")}
    </div>
  </div>
</section>'''
    graph = [business_node(), webpage("faq.html", "Fence questions in Jacksonville, NC", desc, canonical("faq.html") + "#faq"), faq_schema("faq.html", FAQ_PAGE), crumbs_schema("faq.html", [("faq.html", "FAQ")])]
    layout("faq.html", "Fence FAQ | Jacksonville NC Fence Company", desc, body, graph)


def about_page():
    desc = "Jacksonville NC Fence Company installs and repairs wood, vinyl, chain-link, aluminum, and farm fences in Jacksonville and Onslow County. Call (910) 519-2447."
    body = f'''<section class="page-hero">
  <div class="container">
    {crumbs([("about.html", "About")])}
    <h1>About Jacksonville NC Fence Company</h1>
    <p class="lede">A local fence crew for houses, farms, and commercial lots in Jacksonville and nearby Onslow County. Our installers do the work. The estimate comes from a look at the line, not from a national form.</p>
    <div class="hero-actions">{call_btn("btn btn-primary btn-lg")} <a class="btn btn-ghost btn-lg" href="contact.html#quote">Get a free quote</a></div>
  </div>
</section>
<section class="section">
  <div class="container split">
    <div class="split-media"><img src="images/vinyl-picket.jpg" alt="Black vinyl picket fence along a garden" width="925" height="615"></div>
    <div class="prose">
      <h2>What we take on</h2>
      <p>Wood, vinyl, chain link, aluminum, and farm fence, plus repairs and gates. A privacy screen in town, a pool barrier, a dog run, and a pasture line are all work we price. We do not install on Camp Lejeune or New River. Off-base houses are fine when the owner has approved the fence.</p>
      <p>There is no public storefront. You call, we come to the property, and you get a number for that line.</p>
    </div>
  </div>
</section>
<section class="section soft">
  <div class="container prose">
    <h2>How we work a Jacksonville lot</h2>
    <p>Coastal-plain sand, summer storms, and salt air closer to the water are the conditions that decide the posts and the coating. Inside the city, front-yard fences stop at 4 feet and side or rear residential fences stop at 6 feet. In unincorporated Onslow County, a zoning permit is not required for a fence, and the fence still has to stay off easements. HOA rules can be tighter than both.</p>
    <p>If the posts on an old line are sound, we repair. If they have failed, we say so. The materials we install are the ones on the <a href="services.html">services</a> pages, matched to the job rather than to a single “best” product.</p>
    <p><a href="service-areas.html">See the towns we serve</a> or <a href="contact.html">request an estimate</a>.</p>
  </div>
</section>'''
    graph = [business_node(), webpage("about.html", "About Jacksonville NC Fence Company", desc, SITE + "/#business"), crumbs_schema("about.html", [("about.html", "About")])]
    layout("about.html", "About Jacksonville NC Fence Company", desc, body, graph)


def contact_page():
    desc = "Request a free fence estimate in Jacksonville, NC. Call (910) 519-2447 or send the town, fence type, and approximate length."
    body = f'''<section class="page-hero">
  <div class="container">
    {crumbs([("contact.html", "Contact")])}
    <h1>Request a fence estimate</h1>
    <p class="lede">Call {PHONE} or use the form. Estimates are free. We are a service-area company in Jacksonville, with no public storefront to visit.</p>
    <div class="hero-actions">{call_btn("btn btn-primary btn-lg")}</div>
  </div>
</section>
<section class="section">
  <div class="container contact-layout">
    <div class="prose">
      <h2>What to include</h2>
      <p>The town, the fence type if you know it, about how much line you need, and whether an old fence has to come out. A gate for a mower and a gate for a truck are different. Photos help.</p>
      <p>If an HOA has a written fence rule, mention that in the form so we do not order the wrong height or color.</p>
      <div class="map-frame">
        <iframe title="Map of Jacksonville, North Carolina" src="https://maps.google.com/maps?q=34.7540524,-77.4302414&amp;z=11&amp;output=embed" loading="lazy"></iframe>
        <p class="map-caption">Service area centered on Jacksonville, NC. This pin marks the city, not a storefront.</p>
      </div>
    </div>
    {tally_block()}
  </div>
</section>'''
    graph = [business_node(), webpage("contact.html", "Request a fence estimate", desc, SITE + "/#business"), crumbs_schema("contact.html", [("contact.html", "Contact")])]
    layout("contact.html", "Contact Jacksonville NC Fence Company", desc, body, graph)


LOC_DATA = [
    {
        "file": "fence-company-swansboro-nc.html",
        "name": "Swansboro",
        "title": "Fence Company in Swansboro, NC",
        "description": "Fence installation in Swansboro, NC for salt air, small lots, and tight side yards. Vinyl, aluminum, and coated chain link. Call (910) 519-2447.",
        "intro": "Swansboro lots are often smaller than inland Onslow parcels, and the air off Bogue Sound is harder on bare steel. A fence here is planned for salt, tight side yards, and whatever height the town allows on that street.",
        "detail": "Wood still works when it will be stained and the posts are in concrete. Vinyl and aluminum ask less of you next to the water. Vinyl-coated chain link is the chain-link spec we lean toward this close to the sound. Corner lots need a fence that stays out of the sight line for drivers. We measure the opening for the gate before we order it, because a side yard in town rarely has extra room.",
        "points": [
            ("Salt and coatings", "Aluminum, vinyl, and coated chain link are the materials we specify first on lots that take spray and humidity off the water."),
            ("Tight lines", "Short side yards mean the gate width and the post layout have to be exact. There is not much room to adjust after the concrete is in."),
            ("Town rules", "Confirm Swansboro’s height and setback for your street, especially on a corner. We do not copy a Jacksonville city limit onto a Swansboro lot."),
        ],
        "services": [("aluminum-fence.html", "Aluminum fencing"), ("vinyl-fence.html", "Vinyl fencing"), ("chain-link-fence.html", "Chain-link fencing")],
        "faqs": [
            ("Can you install a fence close to Bogue Sound?", "Yes, on private lots. We look at soft ground and standing water before posts go in, and we spec coatings that handle salt better than bare steel."),
            ("Is a wood privacy fence a bad idea in Swansboro?", "It is a fine screen if you will stain it and the posts are set in concrete. If you do not want that upkeep, vinyl privacy is the closer match."),
            ("Do Jacksonville’s 4-foot and 6-foot limits apply here?", "Those numbers are the City of Jacksonville standard. Swansboro is its own town. Bring the local rule, or we will confirm it before we order a height."),
        ],
    },
    {
        "file": "fence-company-richlands-nc.html",
        "name": "Richlands",
        "title": "Fence Company in Richlands, NC",
        "description": "Farm, wood, and chain-link fencing in Richlands, NC for larger lots and acreage northwest of Jacksonville. Call (910) 519-2447.",
        "intro": "Richlands sits inland of Jacksonville, with larger lots and more pasture than the neighborhoods along the river. Fence work here is often a long line: field wire, rail, or a privacy screen around the house and a different fence on the back acreage.",
        "detail": "Salt is less of a factor than it is in Sneads Ferry, so galvanized chain link and wood are common and sensible. The soil is still coastal-plain sand in many fields, and posts still go in concrete. A mile of wire is quoted on corners, gates for trucks, and brush, not on a backyard per-foot habit. Inside the town, ask about local height rules. Outside town limits, Onslow County does not require a fence zoning permit.",
        "points": [
            ("Longer runs", "Acreage changes the quote. Corners, braces, and farm gates matter more than picket style."),
            ("Two fences, one property", "A wood or vinyl yard around the house and wire on the field is a normal Richlands layout."),
            ("Less salt, same sand", "Coatings can be simpler than on the coast. Post depth still has to suit sand."),
        ],
        "services": [("farm-fence.html", "Farm fencing"), ("wood-fence.html", "Wood fencing"), ("chain-link-fence.html", "Chain-link fencing")],
        "faqs": [
            ("Do you build horse and cattle fence in Richlands?", "Yes. Horses get a visible fence such as pipe-and-cable or rail. Cattle can use woven wire or electric. We do not put horses on barbed wire."),
            ("Can the house yard and the field be different fences?", "Yes. They are quoted as two materials. The privacy line stops where the pasture fence starts."),
            ("Is a county permit required outside Richlands town limits?", "Onslow County says a zoning permit is not required for a fence. Stay off easements and the right-of-way, and check with the town if the lot is inside town limits."),
        ],
    },
    {
        "file": "fence-company-holly-ridge-nc.html",
        "name": "Holly Ridge",
        "title": "Fence Company in Holly Ridge, NC",
        "description": "Wood, vinyl, and aluminum fences for Holly Ridge, NC subdivisions and house lots. HOA colors and sandy soil included. Call (910) 519-2447.",
        "intro": "Holly Ridge house lots are a mix of newer subdivisions and older parcels between Jacksonville and the beaches. The fence question is usually an HOA color, a 6-foot rear privacy line, and posts that will hold in sand.",
        "detail": "We ask for the written HOA rule before ordering white vinyl, stained wood, or a black aluminum front fence. Front yards and corner sight lines are where those rules bite. The ground is still sandy, and a new subdivision lot can hide irrigation lines along the fence path. Flag those before we dig. This is residential work first: wood, vinyl, and aluminum, with chain link where a dog run or a side yard does not need a solid screen.",
        "points": [
            ("HOA sheets", "Height, color, and which side faces the neighbor should be in writing before material is ordered."),
            ("New-lot utilities", "Irrigation and shallow utilities are common on fresh subdivisions. We need them marked."),
            ("Privacy on the rear line", "Most of the screen goes on the side and rear. The front stays within whatever the town and the HOA allow."),
        ],
        "services": [("wood-fence.html", "Wood fencing"), ("vinyl-fence.html", "Vinyl fencing"), ("aluminum-fence.html", "Aluminum fencing")],
        "faqs": [
            ("Can you match an HOA fence color in Holly Ridge?", "If the HOA names a color or a material, we order that. Send the sheet with the estimate request so the quote uses the right product."),
            ("Is chain link allowed in Holly Ridge subdivisions?", "Some allow it on the rear line and some do not. The covenants decide. We will not guess from the fence next door."),
            ("Do posts in newer Holly Ridge yards need concrete?", "Yes. The soil is sandy. Concrete and a crowned top are how a post stays put after rain."),
        ],
    },
    {
        "file": "fence-company-sneads-ferry-nc.html",
        "name": "Sneads Ferry",
        "title": "Fence Company in Sneads Ferry, NC",
        "description": "Fencing in Sneads Ferry, NC for salt air, low lots, and soft ground near the New River Inlet. Call (910) 519-2447.",
        "intro": "Sneads Ferry fences deal with salt off the inlet and with low ground that stays soft after rain. The material and the post plan come from those two conditions, not from a catalog photo.",
        "detail": "Vinyl-coated chain link, vinyl privacy, and aluminum are the specs that avoid a rust problem you would see sooner here than in Richlands. We do not set posts in standing water and hope. If a corner of the lot holds water, we say so and move the plan, or we wait for drier ground. Year-round houses and houses that sit empty part of the year both need a gate that latches without someone on site to adjust it every week.",
        "points": [
            ("Salt first", "Coated chain link, vinyl, and aluminum are the default conversation this close to the inlet."),
            ("Soft ground", "A post in saturated sand will move. We check that before concrete goes in the hole."),
            ("Empty-house gates", "Gates are hung and latched so the fence still works when you are not there to lift a sagging leaf."),
        ],
        "services": [("vinyl-fence.html", "Vinyl fencing"), ("aluminum-fence.html", "Aluminum fencing"), ("chain-link-fence.html", "Chain-link fencing")],
        "faqs": [
            ("Will a galvanized chain-link fence rust in Sneads Ferry?", "Bare galvanized steel ages faster next to the inlet. Vinyl-coated fabric is the chain-link spec we recommend on these lots."),
            ("Can you set posts in a yard that floods?", "Not in standing water. We look at the low spots first. A line can often move a few feet onto firmer ground. If it cannot, we wait or we change the plan."),
            ("Is a solid privacy fence a problem in the wind here?", "A solid fence catches wind off open water. Post spacing has to match that. On a very exposed edge, a style that lets some air through can be the sturdier build."),
        ],
    },
    {
        "file": "fence-company-hubert-nc.html",
        "name": "Hubert",
        "title": "Fence Company in Hubert, NC",
        "description": "Fence installation in Hubert, NC for acreage, dogs, and horses between Jacksonville and Swansboro. Call (910) 519-2447.",
        "intro": "Hubert properties are often bigger than a Jacksonville subdivision lot. The usual job is a privacy fence near the house and a longer wire or rail line on the rest of the parcel.",
        "detail": "County rules apply on most of these unincorporated lots: Onslow County does not require a zoning permit for a fence, and electric or barbed wire on a house lot belongs on the interior side. Dogs are the reason for a lot of the yard fencing. Horses show up on the larger tracts and need a fence they can see. We quote the yard and the field as separate runs so you can build one now and the other later.",
        "points": [
            ("Yard plus field", "Wood or vinyl by the house, farm fence on the long line. Two quotes, one visit."),
            ("Dogs and horses", "A dog run and a horse pasture are not the same height, mesh, or gate."),
            ("County lots", "No county fence permit, and the fence still stays off easements and the road right-of-way."),
        ],
        "services": [("farm-fence.html", "Farm fencing"), ("wood-fence.html", "Wood fencing"), ("chain-link-fence.html", "Chain-link fencing")],
        "faqs": [
            ("Can you fence just the house yard in Hubert and leave the field for later?", "Yes. We lay out both if you want, and you can build the yard line first. The field quote stays its own number."),
            ("What do you use for dogs on a larger Hubert lot?", "Chain link or a wood privacy line around the yard the dog actually uses. Fencing the whole acreage in privacy board is rarely the useful spend."),
            ("Are Hubert fences under city of Jacksonville rules?", "Hubert is unincorporated Onslow County, so the city’s 4-foot and 6-foot limits are not the default. County fence rules and any subdivision covenants are what we follow."),
        ],
    },
    {
        "file": "fence-company-piney-green-nc.html",
        "name": "Piney Green",
        "title": "Fence Company in Piney Green, NC",
        "description": "Residential fence installation in Piney Green, NC. Short lot lines, HOA rules, and neighbor boundaries. Call (910) 519-2447.",
        "intro": "Piney Green is dense residential ground inside the Jacksonville area. Fences here are short lines between close neighbors, with HOA rules and utility easements along the back of a lot.",
        "detail": "A 6-foot wood or vinyl privacy fence on the side and rear is the common request, and it has to respect the city’s height limits when the lot is inside the city. The finished side, the color, and the gate for a mower are the details that cause callbacks if they are guessed. We want the property corners known. A fence built on a neighbor’s side of an unseen pin is a problem we will not create. Easements along the rear, especially drainage, are left open.",
        "points": [
            ("Short, exact lines", "There is little extra footage. The layout has to match the pins you actually have."),
            ("HOA and city height", "Front yards stay low. Side and rear privacy stays within the city 6-foot residential limit where that rule applies."),
            ("Mower gates", "A gate that is an inch too narrow becomes the complaint. We measure the machine you need to push through."),
        ],
        "services": [("wood-fence.html", "Wood fencing"), ("vinyl-fence.html", "Vinyl fencing"), ("aluminum-fence.html", "Aluminum fencing")],
        "faqs": [
            ("Can you put a privacy fence on the property line in Piney Green?", "In the City of Jacksonville a fence may sit on the line if it stays out of easements and the right-of-way. Know where the pins are. We recommend telling the neighbor before the posts go in."),
            ("What if the rear line is a drainage easement?", "We do not set posts in an easement. The fence moves onto the buildable part of the lot, even if that gives up a few feet of yard."),
            ("Will you match the neighbor’s fence style?", "We can come close on board width and color when you want that. An HOA sheet outranks the fence next door if the two disagree."),
        ],
    },
    {
        "file": "fence-company-midway-park-nc.html",
        "name": "Midway Park",
        "title": "Fence Company in Midway Park, NC",
        "description": "Off-base fence installation in Midway Park, NC for pets, privacy, and rental houses near Camp Lejeune. Call (910) 519-2447.",
        "intro": "Midway Park work is off-base housing along the corridor toward Camp Lejeune. The jobs are practical: pet containment, a privacy line on a modest yard, and repairs after a storm. We do not install inside the base gate.",
        "detail": "Many houses are rentals. We need the owner’s approval, or a tenant who has it in writing, before we set posts. A landlord who wants the fence removed later should say that up front so the spec matches. Yards are often smaller than Hubert acreage, so chain link, wood privacy, and vinyl are the materials that fit. Timelines around a move are easier when the line is simple and the gate count is low.",
        "points": [
            ("Off base only", "We fence private houses in Midway Park. Base housing and the installation itself are outside this work."),
            ("Owner approval", "Rental fences start with written permission from the owner."),
            ("Useful, not decorative", "Pet runs, privacy on the rear line, and gate repairs are the calls we get most."),
        ],
        "services": [("wood-fence.html", "Wood fencing"), ("vinyl-fence.html", "Vinyl fencing"), ("chain-link-fence.html", "Chain-link fencing")],
        "faqs": [
            ("Can you install a fence on Camp Lejeune?", "No. Our work in this area is on off-base private property in and around Midway Park."),
            ("I rent. Can I still get a fence?", "Only with the owner’s written permission. Send that with the request so the estimate is for a job we are allowed to do."),
            ("What fence makes sense for a dog in a small Midway Park yard?", "Chain link or a short wood or vinyl run around the part of the yard the dog uses. A full privacy line is there if you also want the screen. The gate latch matters as much as the height."),
        ],
    },
    {
        "file": "fence-company-onslow-county-nc.html",
        "name": "Onslow County",
        "title": "Fence Company in Onslow County, NC",
        "description": "Fence installation across Onslow County, NC. City and county rules, sandy soil, farms, and house lots. Call (910) 519-2447.",
        "intro": "Onslow County is the service area, and the fence rules change when you cross from the City of Jacksonville into unincorporated county or into another town. The soil and the weather are the part that stays the same: sand, humidity, and storms.",
        "detail": "Inside Jacksonville, residential front-yard fences are limited to 4 feet and side or rear fences to 6 feet, and nonresidential fences may go to 8 feet. In unincorporated county, a zoning permit is not required for a fence, the ordinance does not set a standard fence location, and electric or barbed wire on a house lot stays on the interior and is marked if it is close to a property line. Pools and spas that hold 24 inches of water or more need a barrier at least 4 feet high. HOA rules can be tighter than both the city and the county. We build to the rule that applies to the parcel in front of us.",
        "points": [
            ("City versus county", "Jacksonville height limits are not the county rule. We do not swap them."),
            ("One soil, many lots", "Sand and soft ground show up from Piney Green to Sneads Ferry. Posts go in concrete."),
            ("Match the use", "A Piney Green privacy fence, a Richlands pasture, and a Jacksonville commercial yard are three different specs."),
        ],
        "services": [("services.html", "All services"), ("farm-fence.html", "Farm fencing"), ("commercial-fencing.html", "Commercial fencing")],
        "faqs": [
            ("Do I need a fence permit in unincorporated Onslow County?", "The county says a zoning permit is not required for a fence. Keep it off easements and the right-of-way. Talk to the neighbor if you plan to build on the line. Towns inside the county can have their own height rules."),
            ("What are the City of Jacksonville fence heights?", "Published city standards limit residential fences to 4 feet in the front yard and 6 feet on the side and rear, and nonresidential fences to 8 feet. Nothing may block a sidewalk, sit in an easement, or break a corner sight line."),
            ("Which fence belongs on a county acreage lot?", "Farm fence on the long lines, and wood, vinyl, or chain link around the house yard if you want a screen or a dog run. See the farm page for horses versus cattle."),
        ],
    },
]


def location_pages():
    for loc in LOC_DATA:
        filename = loc["file"]
        desc = loc["description"]
        points = "".join(
            f'<article class="factor"><h3>{t}</h3><p>{p}</p></article>' for t, p in loc["points"]
        )
        svc = "".join(f'<li><a href="{h}">{label}</a></li>' for h, label in loc["services"])
        others = "".join(
            f'<li><a href="{h}">{n}</a></li>' for h, n in LOCATIONS if h != filename
        )
        body = f'''<section class="page-hero">
  <div class="container">
    {crumbs([("service-areas.html", "Service areas"), (filename, loc["name"])])}
    <h1>Fence company in {loc["name"]}, NC</h1>
    <p class="lede">{loc["intro"]}</p>
    <div class="hero-actions">{call_btn("btn btn-primary btn-lg")} <a class="btn btn-ghost btn-lg" href="contact.html#quote">Get a free quote</a></div>
  </div>
</section>
<section class="section">
  <div class="container prose">
    <h2>What fence work looks like here</h2>
    <p>{loc["detail"]}</p>
    <div style="margin-top:1.2rem">{factors(loc["points"])}</div>
  </div>
</section>
<section class="section soft">
  <div class="container">
    <h2>Services that fit {loc["name"]}</h2>
    <ul class="chips light-chips" style="margin-top:1rem">{svc}</ul>
    <div style="margin-top:1.6rem">{faq_cards(loc["faqs"])}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <h2>Nearby areas</h2>
    <ul class="chips light-chips">{others}</ul>
    <p style="margin-top:1rem"><a href="service-areas.html">Full service area</a></p>
  </div>
</section>
<section class="cta-band">
  <div class="container cta-inner">
    <div>
      <h2>Estimate for a {loc["name"]} fence</h2>
      <p>Call {PHONE} or send the lot details. Say you are in {loc["name"]} so we plan the drive.</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-primary btn-lg" href="contact.html#quote">Get a free quote</a>
      {call_btn("btn btn-ink btn-lg")}
    </div>
  </div>
</section>'''
        graph = [
            business_node(),
            webpage(filename, f"Fence company in {loc['name']}, NC", desc, canonical(filename) + "#place"),
            {
                "@type": "City" if loc["name"] != "Onslow County" else "AdministrativeArea",
                "@id": canonical(filename) + "#place",
                "name": loc["name"] + ", NC",
                "containedInPlace": {"@type": "State", "name": "North Carolina"},
            },
            faq_schema(filename, loc["faqs"]),
            crumbs_schema(filename, [("service-areas.html", "Service areas"), (filename, loc["name"])]),
        ]
        layout(filename, loc["title"] + " | Jacksonville NC Fence Company", desc, body, graph)


def service_areas_page():
    desc = "Jacksonville NC Fence Company serves Jacksonville, Swansboro, Richlands, Holly Ridge, Sneads Ferry, Hubert, Piney Green, Midway Park, and Onslow County."
    cards = []
    for loc in LOC_DATA:
        cards.append(f'''<a class="service-card" href="{loc["file"]}">
        <span class="body"><h3>{loc["name"]}</h3><p>{loc["intro"]}</p><span class="more">Fence notes for {loc["name"]}</span></span>
      </a>''')
    body = f'''<section class="page-hero">
  <div class="container">
    {crumbs([("service-areas.html", "Service areas")])}
    <h1>Fence service area around Jacksonville, NC</h1>
    <p class="lede">We install and repair fences within about 25 miles of Jacksonville. The towns below are not copies of each other. Salt, lot size, farm lines, and city rules change the fence.</p>
    <div class="hero-actions">{call_btn("btn btn-primary btn-lg")}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="card-grid services">{"".join(cards)}</div>
    <div class="map-frame">
      <iframe title="Map of the Jacksonville, North Carolina service area" src="https://maps.google.com/maps?q=Jacksonville,+NC&amp;z=10&amp;output=embed" loading="lazy"></iframe>
      <p class="map-caption">Service-area map centered on Jacksonville. We do not have a public storefront.</p>
    </div>
  </div>
</section>'''
    graph = [business_node(), webpage("service-areas.html", "Fence service area around Jacksonville, NC", desc, SITE + "/#business"), crumbs_schema("service-areas.html", [("service-areas.html", "Service areas")])]
    layout("service-areas.html", "Fence Service Areas near Jacksonville, NC", desc, body, graph)


def privacy_page():
    desc = "How Jacksonville NC Fence Company uses the information you send with a fence estimate request."
    body = f'''<section class="page-hero">
  <div class="container">
    {crumbs([("privacy.html", "Privacy")])}
    <h1>Privacy</h1>
    <p class="lede">What we do with the details you send when you ask for a fence estimate.</p>
  </div>
</section>
<section class="section">
  <div class="container prose">
    <p>The quote form on this site is provided by Tally. When you submit it, we receive your name, phone number, email, and whatever you wrote about the job, along with a source field that tells us the lead came from {NAME}.</p>
    <p>We use that information to reply about a fence estimate and to schedule a look at the property. We do not sell the form contents. Phone calls to {PHONE} are answered for the same purpose.</p>
    <p>If you want your request deleted, call or write and say so. Do not send payment information through the form.</p>
  </div>
</section>'''
    graph = [business_node(), webpage("privacy.html", "Privacy", desc, SITE + "/#business"), crumbs_schema("privacy.html", [("privacy.html", "Privacy")])]
    layout("privacy.html", "Privacy | Jacksonville NC Fence Company", desc, body, graph)


def sitemap():
    paths = ["index.html", "services.html", "about.html", "contact.html", "faq.html", "service-areas.html", "privacy.html"]
    paths += [s["file"] for s in SERVICES_DATA]
    paths += [loc["file"] for loc in LOC_DATA]
    urls = []
    for p in paths:
        loc = canonical(p)
        urls.append(f"  <url><loc>{loc}</loc></url>")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: https://www.jacksonvillencfence.com/sitemap.xml\n",
        encoding="utf-8",
    )
    print("wrote sitemap", len(paths))


def main():
    home()
    services_page()
    for s in SERVICES_DATA:
        service_layout(s)
    faq_page()
    about_page()
    contact_page()
    service_areas_page()
    location_pages()
    privacy_page()
    sitemap()


if __name__ == "__main__":
    main()
