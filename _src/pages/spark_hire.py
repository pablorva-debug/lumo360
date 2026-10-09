from _blocks import section, cards, compare, prose, disclaimer, brand_disclaimer, HOW_IT_WORKS, four_tests

S = lambda n: f'<sup><a href="#src-{n}">{n}</a></sup>'

PAGE = {
    "slug": "spark-hire-alternative",
    "footer_label": "Spark Hire Alternative",
    "related_blurb": "From recorded answers to a real conversation",
    "title": "Spark Hire Alternative: Conversational AI Interviews | Lumo360",
    "description": "Comparing Spark Hire alternatives? Lumo360 replaces recorded one-way answers with a spoken, adaptive first round and evidence-linked scores.",
    "og_title": "A Spark Hire alternative: from recorded answers to a conversation",
    "crumb": "Spark Hire alternative",
    "kicker": "Spark Hire alternative",
    "h1": "A Spark Hire alternative that <em>listens and follows up.</em>",
    "sub": ("Spark Hire made one-way video interviews easy to run. Lumo360 takes the next step: instead of "
            "recording answers to fixed prompts, candidates have a structured conversation that adapts to "
            "what they say, and your team gets the evidence behind every score."),
    "secondary": ("See the comparison", "#compare"),
    "related": ["one-way-video-interview-alternative", "willo-alternative", "hirevue-alternative"],
    "sections": [
        section(
            "overview", "At a glance", "Spark Hire and Lumo360, in brief",
            cards(
                ("Spark Hire", "One-way video, live video and an ATS", [
                    f"Core product is one-way video interviewing, where candidates record answers to set questions{S(1)}",
                    f"Also offers live video interviews and behavioural assessments{S(1)}",
                    f"Its Recruit ATS adds AI resume review{S(1)}",
                    f"Interview plans reported from $299 a month, or $249 a month billed annually{S(1)}",
                ]),
                ("Lumo360", "A conversation instead of a recording", [
                    "A spoken, adaptive first-round conversation built from your job description",
                    "Follow-up questions based on each candidate's answers",
                    "Every score linked to the transcript moments that support it",
                    "A recruiter reviews every result before anyone moves forward",
                    "Credit-based pricing: pay only for completed interviews",
                ], True),
            ),
            cls="bg-white"),
        section(
            "compare", "Side by side", "Spark Hire vs Lumo360",
            compare("Spark Hire", "Lumo360", [
                ("Interview format", f"One-way video, with live video for later rounds{S(1)}",
                 "Spoken, adaptive conversation; use your usual video tool for later rounds"),
                ("Follow-up questions", "Candidates answer the questions you set",
                 "The interviewer probes deeper based on each answer"),
                ("What the recruiter reviews", f"Recorded answers, with transcription{S(1)}",
                 "A competency-by-competency report, with every score linked to the transcript"),
                ("Where the questions come from", "Questions you write or pick",
                 "Generated from your job description, then reviewed by your recruiter"),
                ("Pricing", f"Monthly or annual subscription{S(1)}",
                 "Credits, pay as you go or in bundles; only completed interviews are charged"),
            ], note="Based on public information checked in October 2026."),
            sub="Both let candidates interview in their own time. The difference is what happens while they talk."),
        section(
            "fit", "Honest fit", "When Spark Hire may be the better choice",
            prose(
                "If you want one-way video, live interviews and an applicant tracking system from one supplier "
                "on a single subscription, Spark Hire covers all three.",
                "If your problem is the first round itself (too many applicants, too little signal, and "
                "candidates who dislike recording themselves), a conversational interview gives you more to go "
                "on, with less to watch.",
            )),
        four_tests(),
        HOW_IT_WORKS,
        section("note", "About this comparison", "How we wrote this page",
                disclaimer(brand_disclaimer("Spark Hire")), cls="bg-white"),
    ],
    "faqs": [
        ("What is the best alternative to Spark Hire?",
         "If you like Spark Hire's convenience but want more than recorded answers, look at conversational AI "
         "interviewers. Lumo360 runs a spoken, adaptive first-round conversation and links every score to the "
         "transcript."),
        ("Is Spark Hire a one-way video interview tool?",
         "One-way video is Spark Hire's core product. It also offers live video interviews, assessments and an "
         "applicant tracking system."),
        ("How much does Spark Hire cost?",
         "Third-party reports in 2026 put Spark Hire's interview plan at about $299 a month, or $249 a month "
         "billed annually. Check Spark Hire's pricing page for current figures."),
        ("How is Lumo360 different from Spark Hire?",
         "Candidates have a conversation instead of recording answers. The interviewer follows up on what they "
         "say, and every score links to the transcript moments that support it. A recruiter reviews every "
         "result."),
        ("Do I still need a video tool for later rounds?",
         "Yes. Lumo360 handles the first round. Most teams keep their usual video call tool for interviews with "
         "the hiring manager."),
    ],
    "sources": [
        '<a href="https://hiretruffle.com/blog/spark-hire-pricing" rel="noopener">Truffle, "Spark Hire pricing in 2026"</a>, June 2026, citing Spark Hire\'s pricing page. Truffle is a Spark Hire competitor.',
    ],
}
