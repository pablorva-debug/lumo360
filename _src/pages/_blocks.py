"""Reusable section builders for landing pages."""


def section(id, label, title, inner, sub="", cls=""):
    sub_html = f'\n      <p class="section-sub">{sub}</p>' if sub else ""
    cls_attr = f' class="{cls}"' if cls else ""
    return f"""<section{cls_attr} id="{id}">
  <div class="page">
    <div class="section-head">
      <p class="section-label">{label}</p>
      <h2 class="section-title">{title}</h2>{sub_html}
    </div>
{inner}
  </div>
</section>"""


def cards(*cards):
    """cards: (label, heading, [items], good=False)"""
    out = []
    for label, heading, items, *rest in cards:
        good = rest[0] if rest else False
        lis = "\n".join(f"          <li>{i}</li>" for i in items)
        out.append(f"""      <div class="problem-card">
        <p class="pc-label">{label}</p>
        <h3>{heading}</h3>
        <ul class="plist{' good' if good else ''}">
{lis}
        </ul>
      </div>""")
    return '    <div class="problem-grid">\n' + "\n".join(out) + "\n    </div>"


def pull(quote, cite):
    return f"""    <div class="pull">
      <p>{quote}</p>
      <cite>{cite}</cite>
    </div>"""


def compare(left, right, rows, note=""):
    """rows: (dimension, left_text, right_text). Mobile labels come from data attributes."""
    trs = "\n".join(
        f'        <tr><td class="dim">{d}</td><td class="old" data-l="{left}">{l}</td>'
        f'<td class="us" data-l="{right}">{r}</td></tr>'
        for d, l, r in rows)
    note_html = f'\n    <p class="compare-note">{note}</p>' if note else ""
    return f"""    <table class="compare">
      <thead>
        <tr><th scope="col"></th><th scope="col">{left}</th><th scope="col" class="us">{right}</th></tr>
      </thead>
      <tbody>
{trs}
      </tbody>
    </table>{note_html}"""


def checks(items):
    """items: (heading, text)"""
    out = "\n".join(
        f"""      <div class="check">
        <p class="check-num">{i:02d}</p>
        <h3>{h}</h3>
        <p>{t}</p>
      </div>""" for i, (h, t) in enumerate(items, 1))
    return f'    <div class="checks">\n{out}\n    </div>'


def steps(items):
    out = "\n".join(
        f"""      <div class="step-card">
        <p class="step-num">Step {i:02d}</p>
        <h3>{h}</h3>
        <p>{t}</p>
      </div>""" for i, (h, t) in enumerate(items, 1))
    return f'    <div class="steps">\n{out}\n    </div>'


def prose(*paras):
    ps = "\n".join(f"      <p>{p}</p>" for p in paras)
    return f'    <div class="prose">\n{ps}\n    </div>'


def qa(items):
    """items: (ask_label, question, [paras], our_answer)"""
    out = []
    for ask, q, paras, ours in items:
        ps = "\n".join(f"        <p>{p}</p>" for p in paras)
        ours_html = f'\n        <p class="ours"><strong>Lumo360:</strong> {ours}</p>' if ours else ""
        out.append(f"""      <div class="qa-item">
        <p class="ask">{ask}</p>
        <h3>{q}</h3>
{ps}{ours_html}
      </div>""")
    return '    <div class="qa">\n' + "\n".join(out) + "\n    </div>"


def disclaimer(text):
    return f'    <p class="disclaimer">{text}</p>'


# ---------- Shared content used on several pages ----------

HOW_IT_WORKS = section(
    "how", "How Lumo360 works", "From job description to shortlist",
    steps([
        ("Start with the role",
         "Upload the job description. Lumo360 identifies the competencies that matter and turns them into a "
         "structured interview framework. You review and adjust it before going live."),
        ("Candidates have a real conversation",
         "Candidates join when it suits them. The interviewer follows the framework, asks relevant questions "
         "and follows up based on each answer."),
        ("You review the evidence",
         "See how each candidate performed against every competency, with each score linked to the "
         "conversation. Your team decides who moves forward."),
    ]))

FOUR_TESTS_ITEMS = [
    ("It's a conversation, not a recording",
     "If the questions can't change based on what the candidate says, it's still a one-way format, however "
     "clever the scoring."),
    ("Every score points to evidence",
     "You should be able to click from a score to the exact part of the transcript that supports it. If you "
     "can't explain a rejection, you can't defend it."),
    ("A person makes the call",
     "AI should run the first round and recommend. A recruiter should review every result before a candidate "
     "is progressed or rejected."),
    ("Candidates know what's coming",
     "Tell people what the interview is, how it's assessed and that a person reviews it."),
]


def four_tests(sub=None, last_text=None):
    items = list(FOUR_TESTS_ITEMS)
    if last_text:
        items[3] = (items[3][0], last_text)
    return section(
        "checklist", "Our point of view", "Four things to demand from any screening tool",
        checks(items),
        sub=sub or "Whichever tool you choose, including ours, hold it to these four tests.",
        cls="dark")


def brand_disclaimer(brand):
    return (f"{brand} is a trademark of its owner. Lumo360 is not affiliated with {brand}. Details about "
            f"{brand} come from public sources listed below and were checked in October 2026; products change, "
            f"so confirm current features and pricing with {brand} directly.")
