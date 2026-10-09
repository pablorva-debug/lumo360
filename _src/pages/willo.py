from _blocks import section, cards, compare, prose, disclaimer, brand_disclaimer, HOW_IT_WORKS, four_tests

S = lambda n: f'<sup><a href="#src-{n}">{n}</a></sup>'

PAGE = {
    "slug": "willo-alternative",
    "footer_label": "Willo Alternative",
    "related_blurb": "Async answers vs an adaptive conversation",
    "title": "Willo Alternative: Conversational AI Interviews | Lumo360",
    "description": "Comparing Willo alternatives? Lumo360 runs a spoken first round that follows up on each answer, with every score linked to the transcript.",
    "og_title": "A Willo alternative: from async answers to a conversation",
    "crumb": "Willo alternative",
    "kicker": "Willo alternative",
    "h1": "A Willo alternative built on <em>conversation, not clips.</em>",
    "sub": ("Willo is a flexible asynchronous interviewing platform, with AI summaries on top. Lumo360 works "
            "differently: the interview itself is a conversation that adapts to each candidate, so there's more "
            "to assess, and every score shows its evidence."),
    "secondary": ("See the comparison", "#compare"),
    "related": ["one-way-video-interview-alternative", "spark-hire-alternative", "odro-alternative"],
    "sections": [
        section(
            "overview", "At a glance", "Willo and Lumo360, in brief",
            cards(
                ("Willo", "Asynchronous interviewing with AI assistance", [
                    f"An asynchronous interviewing platform: candidates answer in their own time{S(1)}",
                    f"Questions can be answered by video, audio only or text, in one interview{S(1)}",
                    f"Its Intelligence AI transcribes, summarises responses and identifies key skills{S(1)}",
                    f"Its Real Talk feature flags answers that may be AI-generated or scripted{S(1)}",
                    f"Plans reported from $279 a month{S(1)}",
                ]),
                ("Lumo360", "An interviewer, not just a recorder", [
                    "A spoken first-round conversation built from your job description",
                    "Follow-up questions based on what each candidate says",
                    "Every score linked to the transcript moments that support it",
                    "A recruiter reviews every result before anyone moves forward",
                    "Credit-based pricing: pay only for completed interviews",
                ], True),
            ),
            cls="bg-white"),
        section(
            "compare", "Side by side", "Willo vs Lumo360",
            compare("Willo", "Lumo360", [
                ("Interview format", f"Asynchronous answers by video, audio or text{S(1)}",
                 "A spoken, adaptive conversation, completed in the candidate's own time"),
                ("Follow-up questions", "Ask Willo whether follow-ups adapt to each answer",
                 "The interviewer probes deeper based on each answer"),
                ("AI's role", f"Transcribes, summarises and highlights skills{S(1)}",
                 "Runs the conversation, then scores each competency with linked evidence"),
                ("Scripted or AI-written answers", f"Flagged by its Real Talk feature{S(1)}",
                 "Follow-up questions make rehearsed answers harder to rely on"),
                ("Pricing", f"Monthly plans, reported from $279 a month{S(1)}",
                 "Credits, pay as you go or in bundles; only completed interviews are charged"),
            ], note="Based on public information checked in October 2026."),
            sub="Both remove scheduling. The difference is whether the questions respond to the candidate."),
        section(
            "fit", "Honest fit", "When Willo may be the better choice",
            prose(
                "If you want candidates to answer a fixed set of questions in whatever format suits them "
                "(video, audio or text) and you're happy reviewing summarised responses, Willo is well suited.",
                "If you want the first round to work like a real screening call, where weak or vague answers "
                "get a follow-up, a conversational interview gives you stronger evidence to decide on.",
            )),
        four_tests(),
        HOW_IT_WORKS,
        section("note", "About this comparison", "How we wrote this page",
                disclaimer(brand_disclaimer("Willo")), cls="bg-white"),
    ],
    "faqs": [
        ("What is the best alternative to Willo?",
         "If you want the interview itself to adapt to each candidate, look at conversational AI interviewers. "
         "Lumo360 runs a spoken first-round conversation with follow-up questions and links every score to the "
         "transcript."),
        ("Does Willo use AI?",
         "Yes. Willo's Intelligence AI transcribes and summarises responses and identifies key skills, and its "
         "Real Talk feature flags answers that may be AI-generated or scripted."),
        ("How much does Willo cost?",
         "Third-party listings in 2026 report plans from $279 a month. Check Willo's pricing page for current "
         "figures."),
        ("How is Lumo360 different from Willo?",
         "In Lumo360 the AI runs the interview as a conversation, asking follow-up questions based on each "
         "answer, rather than summarising recorded responses. Every score links to the transcript, and a "
         "recruiter reviews every result."),
        ("Can candidates still interview in their own time?",
         "Yes. Like Willo, Lumo360 needs no scheduling. Candidates complete the conversation when it suits "
         "them."),
    ],
    "sources": [
        '<a href="https://softwarefinder.com/hr/willo" rel="noopener">Software Finder, "Willo"</a>, updated June 2026.',
    ],
}
