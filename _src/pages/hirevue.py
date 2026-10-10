from _blocks import section, cards, compare, checks, prose, disclaimer, brand_disclaimer

S = lambda n: f'<sup><a href="#src-{n}">{n}</a></sup>'

PAGE = {
    "slug": "hirevue-alternative",
    "footer_label": "HireVue Alternative",
    "related_blurb": "Explainable first-round screening without an enterprise suite",
    "title": "HireVue Alternative: Explainable AI First-Round Interviews",
    "description": ("Comparing HireVue alternatives? Lumo360 runs a spoken, adaptive first-round interview where "
                    "every score links to the transcript and a recruiter reviews every result."),
    "og_title": "A HireVue alternative built around explainable first-round scoring",
    "crumb": "HireVue alternative",
    "kicker": "HireVue alternative",
    "h1": "A HireVue alternative where <em>every score shows its working.</em>",
    "sub": ("HireVue is a broad enterprise hiring suite that now includes a voice-based AI interviewer. If you "
            "only need the first-round interview, the useful question isn't which vendor has more modules. It's "
            "whether your recruiters can trace each result back to what the candidate said."),
    "secondary": ("See the comparison", "#compare"),
    "related": ["one-way-video-interview-alternative", "ico-ai-recruitment-questions", "launchpad-alternative"],
    "sections": [
        section(
            "overview", "At a glance", "A suite versus a single job done well",
            cards(
                ("HireVue", "An enterprise suite for interviewing and assessment", [
                    f"Products include live interviewing with a note-taking co-pilot, assessments (skills tests and game-based) and a voice-based AI Interviewer{S(1)}",
                    f"Lists integrations with more than 45 applicant tracking systems{S(1)}",
                    f"Publishes an AI explainability statement and says it runs fairness studies on its models{S(1)}",
                    f"Says around 40% of the Fortune 100 are customers; prices are not published and are quoted on request{S(1)}",
                    f"Grew through acquisition: Modern Hire in 2023{S(2)} and Hireguide in March 2026{S(3)}",
                ]),
                ("Lumo360", "One job: a transparent first round", [
                    "A spoken, adaptive first-round conversation built from your job description",
                    "Every score linked to the transcript moments that support it",
                    "A recruiter reviews every result before anyone moves forward",
                    "Credit-based pricing, published on the site, and only completed interviews are charged",
                    "Typically live within a day, without an implementation project",
                ], True),
            ),
            sub="HireVue's own materials emphasise explainability, so the real difference is scope and buying model, not whether either vendor cares about it.",
            cls="bg-white"),
        section(
            "compare", "Side by side", "HireVue vs Lumo360",
            compare("HireVue", "Lumo360", [
                ("Scope", f"Interviewing, assessments, scheduling and a voice AI Interviewer across the hiring funnel{S(1)}",
                 "The first-round interview, from job description to scored report"),
                ("Candidate experience", f"A voice-based AI Interviewer{S(4)}. Ask how it handles follow-up questions",
                 "A spoken conversation that follows up on each answer"),
                ("Explaining a result", f"Publishes an AI explainability statement{S(1)}. Ask how one candidate's result is traced to their answers",
                 "Every score links to the transcript moments behind it"),
                ("Human oversight", "Ask how recruiters review results before candidates are progressed or rejected",
                 "A recruiter reviews every result before anyone moves forward"),
                ("Pricing", f"Not published; quote-based{S(1)}",
                 "Published: pay as you go, or in bundles, from a free 25-credit trial"),
                ("Typical buyer", f"Large enterprises{S(1)}", "Agencies and in-house teams of any size"),
            ], note="Based on public information checked in October 2026. Where we couldn't verify how HireVue handles something, we've written the question to ask instead of guessing."),
            sub="Where the two differ, and where to look harder in a demo."),
        section(
            "demo-questions", "Due diligence", "Four questions to ask in any AI interview demo",
            checks([
                ("Show me one rejected candidate",
                 "Ask the vendor to take one low-scoring candidate and walk from the score to the exact answer that "
                 "caused it. If that takes a data scientist, a recruiter won't manage it either."),
                ("Where does a person step in?",
                 "Find out whether a recruiter reviews every result, or only a sample. Under UK GDPR, solely "
                 "automated decisions with significant effects carry extra obligations."),
                ("What changes when we run a new role?",
                 "Ask how interview content is created for a role you haven't hired for before, and who reviews it."),
                ("What does it cost at our volume?",
                 "Get a written price for your real applicant numbers, including implementation and any minimum term."),
            ]),
            sub="These apply to Lumo360 too. Our own answers are in the ICO guide linked below.",
            cls="bg-white"),
        section(
            "fit", "Honest fit", "When HireVue may be the better choice",
            prose(
                "If you're a large enterprise that wants interviewing, assessments and ATS integrations from one "
                "long-established supplier, and you already run an annual procurement process, HireVue is built "
                "for that and has the scale to match.",
                "If you want the first-round conversation done well, with published pricing and a short setup, "
                "and you would rather add other tools later than buy a suite now, that is what Lumo360 is for. "
                "Our <a href=\"/ico-ai-recruitment-questions\">guide to the ICO's six questions</a> sets out how "
                "to test any vendor, ours included.",
            )),
        section("note", "About this comparison", "How we wrote this page",
                disclaimer(brand_disclaimer("HireVue")), cls="bg-white"),
    ],
    "faqs": [
        ("What is the best alternative to HireVue?",
         "It depends on what you use HireVue for. For a full assessment suite, other enterprise vendors compete "
         "directly. For the first-round interview itself, conversational AI interviewers such as Lumo360 focus "
         "on an adaptive conversation and on showing the evidence behind every score."),
        ("Does HireVue have an AI interviewer?",
         "Yes. HireVue offers a voice-based AI Interviewer, and acquired Hireguide in March 2026."),
        ("How much does HireVue cost?",
         "HireVue doesn't publish prices on its website; packages are quoted on request, so you will need to ask "
         "HireVue directly."),
        ("How is Lumo360 different from HireVue?",
         "Lumo360 does one thing, the first-round interview. Every score links to the transcript moments that "
         "support it, a recruiter reviews every result, and pricing is published and credit-based, so you pay "
         "only for completed interviews."),
        ("Can I switch from HireVue to Lumo360?",
         "For the first round, yes. Lumo360 builds each interview from your job description, so there is no "
         "question bank to migrate, and the first screening workflow is typically live within a day. If you "
         "also use HireVue for assessments, you can keep those separate."),
    ],
    "sources": [
        '<a href="https://www.hirevue.com/" rel="noopener">HireVue, company website</a>, checked October 2026. Customer and performance figures on that site are HireVue\'s own claims; we have not verified them.',
        '<a href="https://www.recruiter.co.uk/news/2023/05/recruitment-solutions-firm-hirevue-acquires-modern-hire" rel="noopener">Recruiter, "Recruitment solutions firm HireVue acquires Modern Hire"</a>, May 2023.',
        '<a href="https://staffingindustry.com/news/global-daily-news/hirevue-acquires-hireguide" rel="noopener">Staffing Industry Analysts, "HireVue acquires Hireguide"</a>, March 2026.',
        '<a href="https://agilebrandguide.com/tag/hirevue/" rel="noopener">Agile Brand Guide, "Hirevue AI Interviewer sets new standard with hiring AI grounded in validated hiring science"</a>, June 2026.',
    ],
}
