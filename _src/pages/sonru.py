from _blocks import section, cards, compare, prose, disclaimer, brand_disclaimer, HOW_IT_WORKS, four_tests

S = lambda n: f'<sup><a href="#src-{n}">{n}</a></sup>'

PAGE = {
    "slug": "sonru-alternative",
    "footer_label": "Sonru Alternative",
    "related_blurb": "From pre-recorded video to a conversation",
    "title": "Sonru Alternative: Conversational AI Interviews | Lumo360",
    "description": "Comparing Sonru alternatives? Lumo360 replaces recorded video answers with a spoken, adaptive first round and evidence-linked scoring.",
    "og_title": "A Sonru alternative: from recorded video to a conversation",
    "crumb": "Sonru alternative",
    "kicker": "Sonru alternative",
    "h1": "A Sonru alternative that turns recordings into <em>a real conversation.</em>",
    "sub": ("Sonru is one of the longer-established names in video interviewing. If you're reviewing your "
            "screening process, it's worth asking whether recorded answers are still the right first step, or "
            "whether a conversation would tell you more."),
    "secondary": ("See the comparison", "#compare"),
    "related": ["one-way-video-interview-alternative", "launchpad-alternative", "odro-alternative"],
    "sections": [
        section(
            "overview", "At a glance", "Sonru and Lumo360, in brief",
            cards(
                ("Sonru", "Video interviewing", [
                    f"Recorded (one-way) video responses and live video interviews{S(1)}",
                    f"Pre-recorded messages for candidates, plus skills assessment and scoring{S(1)}",
                    f"ATS integration and custom branding{S(1)}",
                    f"Free trial available; prices not published{S(1)}",
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
                ("Interview format", f"Recorded video responses, or live video{S(1)}",
                 "A spoken, adaptive conversation, completed in the candidate's own time"),
                ("Follow-up questions", "Recorded: none. Live: asked by your recruiter",
                 "The AI interviewer asks them, based on each answer"),
                ("What the recruiter reviews", "Video recordings",
                 "A competency-by-competency report, with every score linked to the transcript"),
                ("Where the questions come from", "Questions you set",
                 "Generated from your job description, then reviewed by your recruiter"),
                ("Pricing", f"Not published{S(1)}",
                 "Credits, pay as you go or in bundles; only completed interviews are charged"),
            ], note="Based on public listings checked in October 2026. Public detail on Sonru's current product is limited, so confirm features with Sonru directly."),
            sub="Both remove scheduling from the first round. The difference is whether anyone responds to the answer."),
        section(
            "fit", "Honest fit", "When to stay with recorded video",
            prose(
                "If you specifically want to see candidates on camera at the first stage (for some "
                "presentation-led roles that can matter), a recorded video format still does that job.",
                "For most roles, what you need from the first round is evidence of skills and experience. A "
                "structured conversation with follow-up questions gives you more of that, and candidates "
                "don't have to perform to a camera.",
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
         "Sonru is a video interviewing platform offering recorded video responses and live video interviews, "
         "with skills assessment and scoring."),
        ("How is Lumo360 different from Sonru?",
         "Candidates have a conversation with follow-up questions instead of recording answers to fixed "
         "prompts. Every score links to the transcript, and a recruiter reviews every result."),
        ("How long does switching take?",
         "Lumo360 builds each interview from your job description, so there's no question bank to migrate. The "
         "first screening workflow is typically live within a day."),
    ],
    "sources": [
        '<a href="https://www.capterra.com/p/162157/Sonru/" rel="noopener">Capterra, "Sonru"</a>, product listing, checked October 2026.',
    ],
}
