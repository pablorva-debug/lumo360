from _blocks import section, cards, compare, prose, disclaimer, brand_disclaimer, HOW_IT_WORKS, four_tests

S = lambda n: f'<sup><a href="#src-{n}">{n}</a></sup>'

PAGE = {
    "slug": "odro-alternative",
    "footer_label": "Odro Alternative",
    "related_blurb": "Keep live video, automate the first round",
    "title": "Odro Alternative for Agency First-Round Screening | Lumo360",
    "description": "Looking at Odro alternatives? Lumo360 automates the first-round screen with an adaptive conversation, so live video is saved for the shortlist.",
    "og_title": "An Odro alternative for the first round",
    "crumb": "Odro alternative",
    "kicker": "Odro alternative",
    "h1": "Keep live video for the shortlist. <em>Let the first round run itself.</em>",
    "sub": ("Odro is built for recruiters who interview by video, live or one-way. Lumo360 tackles the step "
            "before: a spoken, adaptive first-round conversation with every applicant, so your consultants only "
            "spend live time on candidates with evidence behind them."),
    "secondary": ("See the comparison", "#compare"),
    "related": ["ai-screening-for-recruitment-agencies", "one-way-video-interview-alternative", "sonru-alternative"],
    "sections": [
        section(
            "overview", "At a glance", "Odro and Lumo360, in brief",
            cards(
                ("Odro", "Video interviewing and engagement for recruiters", [
                    f"Live video, one-way and panel interviews{S(1)}",
                    f"Personalised video outreach and candidate practice sessions{S(1)}",
                    f"Integrates with Bullhorn, Access Vincere Evo, Microsoft Teams and Paiger{S(1)}",
                    f"Used by recruitment agencies and in-house teams{S(1)}",
                ]),
                ("Lumo360", "Automates the first-round screen", [
                    "A spoken, adaptive conversation with every applicant, built from the job description",
                    "Follow-up questions based on each candidate's answers",
                    "Every score linked to the transcript moments that support it",
                    "A consultant reviews every result before anyone moves forward",
                    "Credit-based pricing: pay only for completed interviews",
                ], True),
            ),
            cls="bg-white"),
        section(
            "compare", "Side by side", "Odro vs Lumo360",
            compare("Odro", "Lumo360", [
                ("Main job", f"Video interviews between recruiters and candidates, live or one-way{S(1)}",
                 "Running the first-round screen without a recruiter on the call"),
                ("Recruiter time per candidate", "A live call, or watching a one-way recording",
                 "Reading a scored report, with the transcript a click away"),
                ("Follow-up questions", "Live: the recruiter asks them. One-way: none",
                 "The AI interviewer asks them, based on each answer"),
                ("Consistency", "Depends on the recruiter running the call",
                 "Same competency framework and rubric for every candidate"),
                ("Integrations", f"Bullhorn, Vincere, Microsoft Teams, Paiger{S(1)}",
                 "Ask us about your ATS"),
            ], note="Based on public information checked in October 2026."),
            sub="These tools can work together: Lumo360 for the first round, live video for the shortlist."),
        section(
            "fit", "Honest fit", "Replace, or use alongside?",
            prose(
                "If most of your interviewing is live (consultants meeting candidates, or clients meeting "
                "shortlists), keep a live video tool. Lumo360 doesn't replace that.",
                "Where Lumo360 helps is the stage before: the dozens or hundreds of applicants per vacancy who "
                "each need a first conversation. Screen them all consistently, then spend live time on the "
                "candidates the evidence supports.",
            )),
        four_tests(),
        HOW_IT_WORKS,
        section("note", "About this comparison", "How we wrote this page",
                disclaimer(brand_disclaimer("Odro")), cls="bg-white"),
    ],
    "faqs": [
        ("What is the best alternative to Odro?",
         "It depends which part of Odro you use. For live video interviews, most video-call tools will do. For "
         "first-round screening at volume, a conversational AI interviewer like Lumo360 screens every applicant "
         "without a consultant on the call."),
        ("Does Lumo360 do live video interviews?",
         "No. Lumo360 runs the first-round screen as a spoken conversation with an AI interviewer. Keep your "
         "usual video tool for live interviews with consultants and clients."),
        ("Is Lumo360 built for recruitment agencies?",
         "Yes. It's designed so an agency can screen every applicant to a vacancy consistently, then share an "
         "evidence-backed shortlist with the client."),
        ("Does Lumo360 integrate with Bullhorn or Vincere?",
         "Ask us about your applicant tracking system when you book a demo."),
        ("Who decides which candidates go forward?",
         "Your consultant. Lumo360 recommends, with the evidence for each score, and a person reviews every "
         "result."),
    ],
    "sources": [
        '<a href="https://www.capterra.com/p/185590/Odro/" rel="noopener">Capterra, "Odro"</a>, product listing and reviews, checked October 2026.',
    ],
}
