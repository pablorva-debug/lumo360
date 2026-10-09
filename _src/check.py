#!/usr/bin/env python3
"""Pre-publish checks for the landing pages. Run after build.py:  python3 _src/check.py

Fails if any page still has [TO CONFIRM] placeholders, broken internal links,
footnote references without a matching source, or missing SEO basics.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "_src"))
from build import load_pages  # noqa: E402

problems = []
pages = load_pages()
slugs = {p["slug"] for p in pages}

for p in pages:
    f = ROOT / f'{p["slug"]}.html'
    s = f.read_text()
    name = f.name
    for m in re.findall(r"\[TO CONFIRM[^\]]*\]", s):
        problems.append(f"{name}: placeholder {m[:90]}")
    for href in re.findall(r'href="(/[^"#]*)', s):
        target = href.strip("/")
        if target and target not in slugs and not (ROOT / target).exists():
            problems.append(f"{name}: broken internal link {href}")
    refs = set(re.findall(r'href="#(src-\d+)"', s))
    ids = set(re.findall(r'id="(src-\d+)"', s))
    for r in sorted(refs - ids):
        problems.append(f"{name}: footnote {r} has no source")
    if len(p["title"]) > 70:
        problems.append(f"{name}: title is {len(p['title'])} chars (aim for 70 or fewer)")
    if not 70 <= len(p["description"]) <= 165:
        problems.append(f"{name}: meta description is {len(p['description'])} chars (aim for 70-165)")
    if s.count("<h1") != 1:
        problems.append(f"{name}: expected exactly one h1")

for line in problems:
    print("•", line)
print(f"\n{len(pages)} pages checked, {len(problems)} issue(s).")
sys.exit(1 if problems else 0)
