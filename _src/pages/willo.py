from _blocks import section, cards, compare, prose, disclaimer, brand_disclaimer

S = lambda n: f'<sup><a href="#src-{n}">{n}</a></sup>'

PAGE = {
    "slug": "willo-alternative",
    "footer_label": "Willo Alternative",
    "related_blurb": "Flexible async screening versus an adaptive conversation",
    "title": "Willo Alternative: Adaptive AI Interviews | Lumo360",
    "description": "Comparing Willo alternatives? See how Willo's asynchronous screening and pay-per-role pricing compare with Lumo360's spoken, adaptive first-round interview.",
    "og_title": "A Willo alternative: an adaptive conversation, not clips",
    "crumb": "Willo alternative",
    "kicker": "Willo alternative",
    "h1": "A Willo alternative built on <em>conversation, not clips.</em>",
    "sub": ("Willo is a flexible asynchronous screening platform with a wide integration list, identity checks "
            "and AI summaries. Lumo360 makes a narrower bet: the interview itself should be a conversation that "
            "responds to each candidate, with every score tied to evidence."),
    "secondary": ("See the comparison", "#compare"),
    "related": ["one-way-video-interview-alternative", "spark-hire-alternative", "ico-ai-recruitment-questions"],
    "sections": [
        section(
            "overview", "At a glance", "Willo and Lumo360, in brief",
            cards(
                ("Willo", "Asynchronous screening with AI assistance", [
                    f"Candidates answer in their own time, on any device; questions can be video, written, file upload or multiple choice{S(1)}",
                    f"Willo Intelligence adds transcripts, summaries, benchmarks and role-specific insights, and is described as supporting human decisions{S(1)}",
                    f"Identity and right-to-work checks are available, and Willo says it is ISO 27001 certified and offers 18+ languages{S(1)}",
                    f"Lists 50+ native integrations, including Greenhouse, Lever, Workday and Workable{S(1)}",
                    f"Willo Lite is £49 per live role with no contract; Enterprise starts at £2,999 a year{S(2)}",
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
                ("Interview format", f"Asynchronous: video, written, file upload or multiple choice{S(1)}",
                 "A spoken, adaptive conversation, completed in the candidate's own time"),
                ("Follow-up questions", f"Lists follow-up questions among Willo Intelligence features{S(2)}. Ask whether the AI asks them of the candidate, or suggests them to your team",
                 "The interviewer asks them of the candidate, based on each answer"),
                ("AI's role", f"Transcribes, summarises and benchmarks responses{S(1)}",
                 "Runs the conversation, then scores each competency with linked evidence"),
                ("Compliance and checks", f"ISO 27001, identity and right-to-work checks{S(1)}",
                 "Ask us about your security and verification requirements"),
                ("Pricing", f"Per live role on Lite (up to 150 assessed candidates per role), or an annual Enterprise contract{S(2)}",
                 "Credits, pay as you go or in bundles; only completed interviews are charged"),
            ], note="Based on public information checked in October 2026."),
            sub="Both remove scheduling. The difference is whether the questions respond to the candidate."),
        section(
            "fit", "Honest fit", "When Willo may be the better choice",
            prose(
                "If you need candidates to answer a standard set of questions in whichever format suits them, in "
                "many languages, with identity or right-to-work checks and a long integration list, Willo is "
                "well suited. Its per-role pricing is also hard to beat on cost if recorded answers give you "
                "enough to decide on.",
                "If you want the first round to work like a real screening call, where a vague answer gets a "
                "follow-up, and your reviewers to see the evidence behind each score, a conversational interview "
                "gives you more to decide on. Read how a "
                "<a href=\"/automate-phone-screening\">phone screen can be automated</a> without losing the "
                "conversation.",
            )),
        section("note", "About this comparison", "How we wrote this page",
                disclaimer(brand_disclaimer("Willo")), cls="bg-white"),
    ],
    "faqs": [
        ("What is the best alternative to Willo?",
         "If you want the interview itself to adapt to each candidate, look at conversational AI interviewers. "
         "Lumo360 runs a spoken first-round conversation with follow-up questions and links every score to the "
         "transcript."),
        ("Does Willo use AI?",
         "Yes. Willo Intelligence provides transcripts, summaries, benchmarks and role-specific insights, and "
         "Willo describes it as supporting human hiring decisions rather than replacing them."),
        ("How much does Willo cost?",
         "Willo's pricing page lists Willo Lite at £49 per live role with no contract, and Willo Enterprise "
         "from £2,999 a year on a one-year term. Check Willo's pricing page for current figures."),
        ("How is Lumo360 different from Willo?",
         "In Lumo360 the AI runs the interview as a spoken conversation, asking follow-up questions based on "
         "each answer, rather than summarising recorded responses. Every score links to the transcript, and a "
         "recruiter reviews every result."),
        ("Can candidates still interview in their own time?",
         "Yes. Like Willo, Lumo360 needs no scheduling. Candidates complete the conversation when it suits "
         "them."),
    ],
    "sources": [
        '<a href="https://www.willo.video/" rel="noopener">Willo, company website</a>, checked October 2026. Performance figures on that site are Willo\'s own claims; we have not verified them.',
        '<a href="https://www.willo.video/pricing" rel="noopener">Willo, pricing page</a>, checked October 2026. Prices in pounds sterling.',
    ],
}
