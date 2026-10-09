#!/usr/bin/env python3
"""Builds the Lumo360 SEO landing pages.

Each page's content lives in _src/pages/<name>.py as a PAGE dict.
Run from the repo root:  python3 _src/build.py

It writes <slug>.html for every page, refreshes the footer link list in
index.html (between the footer-links markers) and rewrites sitemap.xml.
_src/ is excluded from the deployed site by .assetsignore.
"""
import html
import importlib.util
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES_DIR = ROOT / "_src" / "pages"
sys.path.insert(0, str(PAGES_DIR))  # lets page files import _blocks
SITE = "https://lumo360.io"
FORM_ENDPOINT = "https://formspree.io/f/mzdyknoz"
LASTMOD = "2026-10-09"

# Order controls the footer link list on every page.
ORDER = [
    "one_way_video",
    "phone_screen",
    "agencies",
    "ico",
    "hirevue",
    "spark_hire",
    "willo",
    "odro",
    "sonru",
    "launchpad",
]


def load_pages():
    pages = []
    for name in ORDER:
        path = PAGES_DIR / f"{name}.py"
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        pages.append(mod.PAGE)
    return pages


def esc(s):
    return html.escape(s, quote=True)


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


LOGO = """<svg aria-hidden="true" width="{size}" height="{size}" viewBox="0 0 44 44" fill="none">
        <circle cx="22" cy="22" r="16" stroke="{c1}" stroke-width="2.5" stroke-dasharray="84 16" stroke-dashoffset="4" stroke-linecap="round"/>
        <circle cx="22" cy="22" r="9" stroke="{c2}" stroke-width="2" stroke-dasharray="44 12" stroke-dashoffset="-8" stroke-linecap="round"/>
        <circle cx="22" cy="22" r="2.5" fill="{c2}"/>
      </svg>"""

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 44 44'%3E"
           "%3Ccircle cx='22' cy='22' r='16' stroke='%231A3252' stroke-width='2.5' stroke-dasharray='84 16' "
           "stroke-dashoffset='4' stroke-linecap='round' fill='none'/%3E%3Ccircle cx='22' cy='22' r='9' "
           "stroke='%232060A8' stroke-width='2' stroke-dasharray='44 12' stroke-dashoffset='-8' "
           "stroke-linecap='round' fill='none'/%3E%3Ccircle cx='22' cy='22' r='2.5' fill='%232060A8'/%3E%3C/svg%3E")


def footer_links_html(pages, indent="      "):
    lines = [f'{indent}<a href="/">Home</a>']
    for p in pages:
        lines.append(f'{indent}<a href="/{p["slug"]}">{esc(p["footer_label"])}</a>')
    return "\n".join(lines)


def faq_schema(faqs):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in faqs
        ],
    }, indent=2, ensure_ascii=False)


def breadcrumb_schema(p):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Lumo360", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": p["crumb"], "item": f'{SITE}/{p["slug"]}'},
        ],
    }, indent=2, ensure_ascii=False)


def faq_html(faqs):
    items = "\n".join(
        f"""      <details>
        <summary>{esc(q)}</summary>
        <p>{a}</p>
      </details>""" for q, a in faqs)
    return f"""<section id="faq">
  <div class="page">
    <div class="section-head">
      <p class="section-label">FAQ</p>
      <h2 class="section-title">Common questions</h2>
    </div>
    <div class="faq">
{items}
    </div>
  </div>
</section>"""


def related_html(page, pages):
    picks = [p for p in pages if p["slug"] in page.get("related", [])]
    if not picks:
        return ""
    cards = "\n".join(
        f'      <a href="/{p["slug"]}">{esc(p["footer_label"])}<span>{esc(p["related_blurb"])}</span></a>'
        for p in picks)
    return f"""<section class="bg-white" id="related">
  <div class="page">
    <div class="section-head">
      <p class="section-label">Keep reading</p>
      <h2 class="section-title">Related guides</h2>
    </div>
    <div class="related">
{cards}
    </div>
  </div>
</section>"""


def sources_html(sources):
    if not sources:
        return ""
    items = "\n".join(f'      <li id="src-{i}">{s}</li>' for i, s in enumerate(sources, 1))
    return f"""<div class="sources">
  <div class="page">
    <h2>Sources</h2>
    <ol>
{items}
    </ol>
  </div>
</div>"""


def render(p, pages):
    url = f'{SITE}/{p["slug"]}'
    sections = "\n\n".join(p["sections"])
    cta = p.get("cta", {})
    cta_title = cta.get("title", "Give candidates a conversation.<br>Give your team <em>the evidence.</em>")
    cta_sub = cta.get("sub", "See a Lumo360 interview and the report it produces, using one of your own job descriptions.")
    secondary = p.get("secondary")
    secondary_html = (f'\n      <a href="{secondary[1]}" class="btn-secondary">{esc(secondary[0])}</a>'
                      if secondary else "")
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- Generated by _src/build.py from _src/pages/. Edit the source, not this file. -->
<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["description"])}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{url}">
<link rel="icon" type="image/svg+xml" href="{FAVICON}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(p["og_title"])}">
<meta property="og:description" content="{esc(p["description"])}">
<meta property="og:image" content="{SITE}/og-image.jpg">
<meta property="og:locale" content="en_GB">
<meta property="og:site_name" content="Lumo360">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(p["og_title"])}">
<meta name="twitter:description" content="{esc(p["description"])}">
<meta name="twitter:image" content="{SITE}/og-image.jpg">
<script type="application/ld+json">
{breadcrumb_schema(p)}
</script>
<script type="application/ld+json">
{faq_schema(p["faqs"])}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,300;1,9..40,400&family=Archivo:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/landing.css">
</head>
<body>

<nav class="nav">
  <div class="page">
    <a href="/" class="nav-left" aria-label="Lumo360 home">
      {LOGO.format(size=30, c1="#1A3252", c2="#2060A8")}
      <span class="nav-wordmark">Lumo<span>360</span></span>
    </a>
    <ul class="nav-links" id="nav-links">
      <li><a href="/#problem">Why Lumo360</a></li>
      <li><a href="/#how">How it works</a></li>
      <li><a href="/#trust">Trust</a></li>
      <li><a href="/#faq">FAQ</a></li>
    </ul>
    <div style="display:flex; align-items:center; gap:8px;">
      <a href="#demo" class="nav-cta js-demo">Book a demo</a>
      <button class="nav-toggle" id="nav-toggle" aria-label="Toggle menu" aria-expanded="false"><span></span></button>
    </div>
  </div>
</nav>

<header class="hero">
  <div class="page">
    <p class="crumbs"><a href="/">Lumo360</a> &nbsp;/&nbsp; {esc(p["crumb"])}</p>
    <p class="hero-kicker">{esc(p["kicker"])}</p>
    <h1>{p["h1"]}</h1>
    <p class="hero-sub">{p["sub"]}</p>
    <div class="hero-actions">
      <a href="#demo" class="btn-primary js-demo">Book a demo <span aria-hidden="true">→</span></a>{secondary_html}
    </div>
  </div>
</header>

<main>

{sections}

{faq_html(p["faqs"])}

{related_html(p, pages)}

<section id="demo-cta">
  <div class="page">
    <div class="cta-block">
      <h2 class="section-title">{cta_title}</h2>
      <p class="cta-sub">{cta_sub}</p>
      <a href="#demo" class="btn-primary-light js-demo">Book a demo <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

{sources_html(p.get("sources", []))}

</main>

<footer class="footer">
  <div class="page">
    <nav class="footer-links" aria-label="Footer">
{footer_links_html(pages)}
    </nav>
    <div class="footer-row">
      <div class="footer-left">
        {LOGO.format(size=18, c1="#B0B8C4", c2="#B0B8C4")}
        <span class="footer-copy">Screening Intelligence · Lumo360</span>
      </div>
      <span class="footer-tagline">Designed for people. Built for trust.</span>
      <span class="footer-copy">© 2026 Lumo360. All rights reserved.</span>
    </div>
  </div>
</footer>

<div id="demo-modal" role="dialog" aria-modal="true" aria-labelledby="demo-title">
  <div class="modal-backdrop" id="demo-backdrop"></div>
  <div class="modal-card">
    <h3 id="demo-title">Book a demo</h3>
    <p>Drop your email and we'll be in touch to find a time that works for you.</p>
    <div id="demo-form">
      <input id="demo-email" type="email" placeholder="your@email.com" autocomplete="email" aria-label="Work email">
      <button class="btn-primary" id="demo-submit" type="button">Request my demo →</button>
      <p id="demo-error">Please enter a valid email address.</p>
    </div>
    <div id="demo-success">
      <p style="font-size:15px;font-weight:600;color:var(--ink-900);margin:20px 0 6px;">You're on the list!</p>
      <p>We'll be in touch very soon.</p>
    </div>
    <button class="modal-close" id="demo-close" type="button" aria-label="Close">✕</button>
  </div>
</div>

<script>
  // Page identifier sent with demo requests so you can see which landing page converts
  const PAGE_SOURCE = '{p["slug"]}';

  const modal = document.getElementById('demo-modal');
  function openDemo(e) {{
    if (e) e.preventDefault();
    modal.style.display = 'flex';
    document.getElementById('demo-success').style.display = 'none';
    document.getElementById('demo-form').style.display = 'block';
    document.getElementById('demo-error').style.display = 'none';
    document.getElementById('demo-email').focus();
  }}
  function closeDemo() {{ modal.style.display = 'none'; }}
  function submitDemo() {{
    const email = document.getElementById('demo-email').value.trim();
    const err = document.getElementById('demo-error');
    if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)) {{
      err.textContent = 'Please enter a valid email address.';
      err.style.display = 'block';
      return;
    }}
    fetch('{FORM_ENDPOINT}', {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/json', 'Accept': 'application/json' }},
      body: JSON.stringify({{ email, source: PAGE_SOURCE, _subject: 'Lumo360 demo request (' + PAGE_SOURCE + ')' }})
    }})
    .then(res => {{ if (!res.ok) throw new Error(); return res.json(); }})
    .then(() => {{
      document.getElementById('demo-form').style.display = 'none';
      document.getElementById('demo-success').style.display = 'block';
    }})
    .catch(() => {{
      err.textContent = 'Something went wrong. Please try again.';
      err.style.display = 'block';
    }});
  }}
  document.querySelectorAll('.js-demo').forEach(el => el.addEventListener('click', openDemo));
  document.getElementById('demo-backdrop').addEventListener('click', closeDemo);
  document.getElementById('demo-close').addEventListener('click', closeDemo);
  document.getElementById('demo-submit').addEventListener('click', submitDemo);
  document.getElementById('demo-email').addEventListener('keydown', e => {{ if (e.key === 'Enter') submitDemo(); }});
  document.addEventListener('keydown', e => {{ if (e.key === 'Escape') closeDemo(); }});

  const navToggle = document.getElementById('nav-toggle');
  const navLinks = document.getElementById('nav-links');
  navToggle.addEventListener('click', () => {{
    const open = navLinks.classList.toggle('open');
    navToggle.classList.toggle('open', open);
    navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  }});
</script>
</body>
</html>
"""


def update_index(pages):
    path = ROOT / "index.html"
    s = path.read_text()
    start, end = "<!-- footer-links:start -->", "<!-- footer-links:end -->"
    block = f"{start}\n{footer_links_html(pages)}\n      {end}"
    s2 = re.sub(re.escape(start) + r".*?" + re.escape(end), lambda m: block, s, flags=re.S)
    if s2 == s and start not in s:
        raise SystemExit("index.html is missing the footer-links markers")
    path.write_text(s2)


def write_sitemap(pages):
    urls = [(SITE + "/", "2026-09-05", "1.0")] + [
        (f'{SITE}/{p["slug"]}', LASTMOD, p.get("priority", "0.7")) for p in pages]
    body = "\n".join(
        f"""  <url>
    <loc>{u}</loc>
    <lastmod>{d}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{pr}</priority>
  </url>""" for u, d, pr in urls)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n')


def main():
    pages = load_pages()
    for p in pages:
        (ROOT / f'{p["slug"]}.html').write_text(render(p, pages))
        print("wrote", p["slug"] + ".html")
    update_index(pages)
    write_sitemap(pages)
    print("updated index.html footer and sitemap.xml")


if __name__ == "__main__":
    main()
