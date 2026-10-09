from _blocks import section, cards, compare, prose, disclaimer, brand_disclaimer, HOW_IT_WORKS, four_tests

S = lambda n: f'<sup><a href="#src-{n}">{n}</a></sup>'

PAGE = {
    "slug": "launchpad-alternative",
    "footer_label": "LaunchPad Alternative",
    "related_blurb": "Volume screening that still feels human",
    "title": "LaunchPad Recruits Alternative: Conversational AI Interviews | Lumo360",
    "description": ("Comparing LaunchPad alternatives for volume hiring? Lumo360 screens every applicant with a "
                    "spoken, adaptive conversation and links every score to the transcript."),
    "og_title": "A LaunchPad alternative for volume screening",
    "crumb": "LaunchPad alternative",
    "kicker": "LaunchPad Recruits alternative",
    "h1": "A LaunchPad alternative for volume hiring that <em>still feels human.</em>",
    "sub": ("LaunchPad is a video assessment platform built for high-volume recruitment teams. Lumo360 tackles "
            "the same volume problem differently: every applicant gets a structured conversation that adapts to "
            "their answers, and your team gets evidence rather than recordings."),
    "secondary": ("See the comparison", "#compare"),
    "related": ["one-way-video-interview-alternative", "sonru-alternative", "automate-phone-screening"],
    "sections": [
        section(
            "overview", "At a glance", "LaunchPad and Lumo360, in brief",
            cards(
                ("LaunchPad", "Video assessment for volume recruitment", [
                    f"A video assessment solution with question pre-selection, interview recording, sharing and review{S(1)}",
                    f"Live video interviews and candidate practice sessions{S(1)}",
                    f"Designed for volume in-house recruitment teams{S(1)}",
                    f"Prices not published{S(1)}",
                ]),
                ("Lumo360", "Conversational screening at volume", [
                    "A spoken, adaptive first-round conversation with every applicant",
                    "Built from your job description, reviewed by your recruiter before going live",
                    "Every score linked to the transcript moments that support it",
                    "A recruiter reviews every result before anyone moves forward",
                    "Credit-based pricing: pay only for completed interviews",
                ], True),
            ),
            cls="bg-white"),
        section(
            "compare", "Side by side", "LaunchPad vs Lumo360",
            compare("LaunchPad", "Lumo360", [
                ("Interview format", f"Recorded video assessment, plus live video{S(1)}",
                 "A spoken, adaptive conversation, completed in the candidate's own time"),
                ("Follow-up questions", "Recorded: questions are pre-selected",
                 "The AI interviewer follows up based on each answer"),
                ("What the recruiter reviews", f"Recordings, shared and reviewed by the team{S(1)}",
                 "A competency-by-competency report, with every score linked to the transcript"),
                ("Built for", f"Volume in-house recruitment teams{S(1)}",
                 "Agencies and in-house teams, from a handful of roles to high volume"),
                ("Pricing", f"Not published{S(1)}",
                 "Credits, pay as you go or in bundles; only completed interviews are charged"),
            ], note="Based on public listings checked in October 2026. Public detail on LaunchPad's current product is limited, so confirm features with LaunchPad directly."),
            sub="Volume needs consistency. The question is whether recordings or conversations give you better evidence."),
        section(
            "fit", "Honest fit", "When LaunchPad may be the better choice",
            prose(
                "If your process depends on seeing candidates on video at the first stage, and your team is "
                "set up to review recordings at volume, a video assessment platform fits that.",
                "If reviewing recordings is the bottleneck, a conversational interview that produces a scored, "
                "evidence-linked report for each candidate cuts the watching, without cutting the depth.",
            )),
        four_tests(),
        HOW_IT_WORKS,
        section("note", "About this comparison", "How we wrote this page",
                disclaimer(brand_disclaimer("LaunchPad")), cls="bg-white"),
    ],
    "faqs": [
        ("What is the best alternative to LaunchPad Recruits?",
         "For high-volume first-round screening, conversational AI interviewers like Lumo360 interview every "
         "applicant and give recruiters an evidence-linked report instead of recordings to watch."),
        ("What does LaunchPad do?",
         "LaunchPad is a video assessment platform with pre-selected interview questions, recording, sharing "
         "and review, plus live video interviews. It's aimed at volume in-house recruitment teams."),
        ("How is Lumo360 different from LaunchPad?",
         "Candidates have a spoken conversation with follow-up questions instead of recording answers. Every "
         "score links to the transcript, and a recruiter reviews every result."),
        ("Can Lumo360 handle high volumes?",
         "Yes. There's no scheduling, so you can invite every applicant at once and each completes the "
         "conversation when it suits them. Every candidate is assessed against the same framework."),
    ],
    "sources": [
        '<a href="https://www.capterra.com/p/162695/LaunchPad-RECRUITS/" rel="noopener">Capterra, "LaunchPad Recruiting Platform"</a>, product listing, checked October 2026.',
    ],
}
