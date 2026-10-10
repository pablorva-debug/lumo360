from _blocks import section, cards, compare, steps, prose, disclaimer, brand_disclaimer, HOW_IT_WORKS, four_tests

S = lambda n: f'<sup><a href="#src-{n}">{n}</a></sup>'

PAGE = {
    "slug": "sonru-alternative",
    "footer_label": "Sonru Alternative",
    "related_blurb": "What changes when you move on from recorded video",
    "title": "Sonru Alternative: Moving From Recorded Video | Lumo360",
    "description": "Thinking about moving on from Sonru? See what changes for candidates, recruiters and reporting when you replace recorded answers with an adaptive interview.",
    "og_title": "A Sonru alternative: what changes when you move on from recorded video",
    "crumb": "Sonru alternative",
    "kicker": "Sonru alternative",
    "h1": "A Sonru alternative that turns recordings into <em>a real conversation.</em>",
    "sub": ("Sonru has been running video interviews since 2007. If you're reviewing your screening process, "
            "the practical question is what you would gain and what would change for candidates, recruiters and "
            "reporting if the first round became a conversation instead of a recording."),
    "secondary": ("See the comparison", "#compare"),
    "related": ["one-way-video-interview-alternative", "ico-ai-recruitment-questions", "willo-alternative"],
    "sections": [
        section(
            "overview", "At a glance", "Sonru and Lumo360, in brief",
            cards(
                ("Sonru", "Established one-way video interviewing", [
                    f"Candidates record answers on their own schedule, with screening questions to filter on your criteria{S(1)}",
                    f"Says it has operated since 2007 and offers 24/7 candidate support{S(1)}",
                    f"Questions can be written in any language{S(1)}",
                    f"Names DHL Express and EE as case studies; claims up to 80% less early-stage screening time (Sonru's own figure){S(1)}",
                    f"Prices are not published on its site{S(1)}",
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
            "compare", "Side by side", "Sonru vs Lumo360",
            compare("Sonru", "Lumo360", [
                ("Interview format", f"Recorded video responses{S(1)}",
                 "A spoken, adaptive conversation, completed in the candidate's own time"),
                ("Follow-up questions", "Candidates answer the set questions; there is no one on the other end",
                 "The AI interviewer asks them, based on each answer"),
                ("What the recruiter reviews", "Video recordings, one candidate at a time",
                 "A competency-by-competency report, with every score linked to the transcript"),
                ("Where the questions come from", "Questions you set",
                 "Generated from your job description, then reviewed by your recruiter"),
                ("Pricing", f"Not published{S(1)}",
                 "Published: credits, pay as you go or in bundles; only completed interviews are charged"),
            ], note="Based on public information checked in October 2026. Sonru's site gives limited product detail, so confirm current features with Sonru directly."),
            sub="Both remove scheduling from the first round. The difference is whether anyone responds to the answer."),
        section(
            "switching", "If you move", "What changes when you switch",
            steps([
                ("For candidates",
                 "They join a spoken conversation instead of recording to a camera. It still happens in their own "
                 "time, and it takes the same kind of effort, but they are answered as they go."),
                ("For recruiters",
                 "You stop watching recordings. You read a scored report per candidate and open the transcript "
                 "where you want to check the evidence."),
                ("For your content",
                 "There is no question set to rebuild. Lumo360 generates the framework from the job description, "
                 "and your team reviews and adjusts it before it goes live."),
            ]),
            sub="A first workflow is typically live within a day. Existing recordings stay in Sonru, so check what you need to keep and for how long."),
        section(
            "fit", "Honest fit", "When to stay with recorded video",
            prose(
                "If seeing candidates on camera at the first stage matters for your roles, such as "
                "presentation-led positions, recorded video still does that job. If you need established "
                "multilingual question setup and round-the-clock candidate support, Sonru lists both.",
                "For most roles, what you need from the first round is evidence of skills and experience. A "
                "structured conversation with follow-up questions gives you more of that, and candidates don't "
                "have to perform to a camera. See how it compares across the "
                "<a href=\"/one-way-video-interview-alternative\">one-way video category</a>.",
            )),
        four_tests(),
        HOW_IT_WORKS,
        section("note", "About this comparison", "How we wrote this page",
                disclaimer(brand_disclaimer("Sonru")), cls="bg-white"),
    ],
    "faqs": [
        ("What is the best alternative to Sonru?",
         "If you're moving on from recorded video interviews, look at conversational AI interviewers. Lumo360 "
         "runs a spoken, adaptive first-round conversation and links every score to the transcript."),
        ("What does Sonru do?",
         "Sonru is a video interviewing platform. Candidates record answers to screening questions on their own "
         "schedule, and Sonru says it has operated since 2007."),
        ("How is Lumo360 different from Sonru?",
         "Candidates have a conversation with follow-up questions instead of recording answers to fixed "
         "prompts. Every score links to the transcript, and a recruiter reviews every result."),
        ("How long does switching take?",
         "Lumo360 builds each interview from your job description, so there is no question bank to migrate. The "
         "first screening workflow is typically live within a day."),
        ("What happens to my existing Sonru recordings?",
         "They stay with Sonru. Before you switch, check with Sonru how long recordings are kept and how you can "
         "export them, particularly if you need them for audit."),
    ],
    "sources": [
        '<a href="https://www.sonru.com/" rel="noopener">Sonru, company website</a>, checked October 2026. Performance figures and client names on that site are Sonru\'s own claims; we have not verified them.',
    ],
}
