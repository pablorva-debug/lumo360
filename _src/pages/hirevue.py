from _blocks import section, cards, compare, prose, disclaimer, brand_disclaimer, HOW_IT_WORKS, four_tests

S = lambda n: f'<sup><a href="#src-{n}">{n}</a></sup>'

PAGE = {
    "slug": "hirevue-alternative",
    "footer_label": "HireVue Alternative",
    "related_blurb": "Transparent scoring without an enterprise contract",
    "title": "HireVue Alternative: Transparent AI Interviews | Lumo360",
    "description": ("Looking for a HireVue alternative? Lumo360 runs conversational first-round interviews where "
                    "every score links to the transcript and a recruiter reviews every result."),
    "og_title": "A HireVue alternative built on transparent scoring",
    "crumb": "HireVue alternative",
    "kicker": "HireVue alternative",
    "h1": "A HireVue alternative where <em>every score shows its working.</em>",
    "sub": ("HireVue is the best-known name in video interviewing and now has its own AI interviewer. If you're "
            "comparing options, the question isn't only whether an AI asks the questions. It's whether you can "
            "see, and defend, how each candidate was scored."),
    "secondary": ("See the comparison", "#compare"),
    "related": ["one-way-video-interview-alternative", "ico-ai-recruitment-questions", "spark-hire-alternative"],
    "sections": [
        section(
            "overview", "At a glance", "HireVue and Lumo360, in brief",
            cards(
                ("HireVue", "An enterprise platform for interviews and assessments", [
                    f"Built around asynchronous (one-way) video interviews, plus pre-hire assessments{S(1)}",
                    f"Acquired Modern Hire in 2023{S(2)} and Hireguide in March 2026, adding conversational hiring technology{S(3)}",
                    f"Now offers a voice-based AI interviewer{S(4)}",
                    f"Doesn't publish prices; packages are quoted{S(1)}",
                    f"Serves large organisations, including around half of the Fortune 100{S(1)}",
                ]),
                ("Lumo360", "Focused on one job: a transparent first round", [
                    "A spoken, adaptive first-round conversation built from your job description",
                    "Every score linked to the transcript moments that support it",
                    "A recruiter reviews every result before anyone moves forward",
                    "Credit-based pricing: pay as you go or in bundles, and only completed interviews are charged",
                    "Typically live within a day, without an implementation project",
                ], True),
            ),
            sub="Two different shapes of product. Which fits depends on what you need the first round to do.",
            cls="bg-white"),
        section(
            "compare", "Side by side", "HireVue vs Lumo360",
            compare("HireVue", "Lumo360", [
                ("Interview format", f"One-way video interviews, plus a voice-based AI interviewer{S(4)}",
                 "Spoken, adaptive conversation that follows up on each answer"),
                ("Assessments", f"Pre-hire assessments available{S(1)}",
                 "Focused on the interview; competencies come from your job description"),
                ("How scores are explained", "Ask HireVue to show you how a specific score was reached",
                 "Every score links to the exact transcript moments behind it"),
                ("Human review", "Ask how recruiters review results before candidates are rejected",
                 "A recruiter reviews every result before anyone moves forward"),
                ("Pricing", f"Not published; quote-based packages{S(1)}",
                 "Credit-based, pay as you go or in bundles; only completed interviews are charged"),
                ("Typical customer", f"Large enterprises{S(1)}", "Agencies and in-house teams of any size"),
            ], note="Based on public information checked in October 2026. Where we couldn't verify how HireVue handles something, we've written the question to ask instead of guessing."),
            sub="Where the two differ, and the questions worth asking in a demo."),
        section(
            "fit", "Honest fit", "When HireVue may be the better choice",
            prose(
                "If you're a large enterprise that wants interviews, psychometric-style assessments and "
                "scheduling from a single long-established supplier, and you have the procurement process for "
                "an annual contract, HireVue is built for that.",
                "If what you need is a fair, explainable first round that your recruiters can trust and "
                "defend, without a long contract or implementation, that's the problem Lumo360 is built to "
                "solve.",
            )),
        four_tests(),
        HOW_IT_WORKS,
        section("note", "About this comparison", "How we wrote this page",
                disclaimer(brand_disclaimer("HireVue")), cls="bg-white"),
    ],
    "faqs": [
        ("What is the best alternative to HireVue?",
         "It depends on what you use HireVue for. For enterprise assessment suites, other enterprise vendors "
         "compete directly. For the first-round interview itself, conversational AI interviewers like Lumo360 "
         "focus on running an adaptive conversation and showing the evidence behind every score."),
        ("Does HireVue have an AI interviewer?",
         "Yes. HireVue acquired Hireguide in March 2026 and offers a voice-based AI interviewer, alongside its "
         "one-way video interviews and assessments."),
        ("How much does HireVue cost?",
         "HireVue doesn't publish its prices. Packages are quoted, so you'll need to ask HireVue directly."),
        ("How is Lumo360 different from HireVue?",
         "Lumo360 is focused on the first-round interview. Every score links to the transcript moments that "
         "support it, a recruiter reviews every result, and pricing is credit-based, so you pay only for "
         "completed interviews."),
        ("Can I switch from HireVue to Lumo360?",
         "Yes. Lumo360 builds each interview from your job description, so there's no question bank to "
         "migrate. The first screening workflow is typically live within a day."),
    ],
    "sources": [
        '<a href="https://www.socialtalent.com/?p=95600" rel="noopener">SocialTalent, "7 best HireVue alternatives in 2026"</a>, July 2026. SocialTalent is a HireVue competitor; we use it only for facts it attributes to HireVue.',
        '<a href="https://www.recruiter.co.uk/news/2023/05/recruitment-solutions-firm-hirevue-acquires-modern-hire" rel="noopener">Recruiter, "Recruitment solutions firm HireVue acquires Modern Hire"</a>, May 2023.',
        '<a href="https://staffingindustry.com/news/global-daily-news/hirevue-acquires-hireguide" rel="noopener">Staffing Industry Analysts, "HireVue acquires Hireguide"</a>, March 2026.',
        '<a href="https://agilebrandguide.com/tag/hirevue/" rel="noopener">Agile Brand Guide, "Hirevue AI Interviewer sets new standard with hiring AI grounded in validated hiring science"</a>, June 2026.',
    ],
}
