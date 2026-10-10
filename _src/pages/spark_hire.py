from _blocks import section, cards, compare, prose, disclaimer, brand_disclaimer, HOW_IT_WORKS, four_tests

S = lambda n: f'<sup><a href="#src-{n}">{n}</a></sup>'

PAGE = {
    "slug": "spark-hire-alternative",
    "footer_label": "Spark Hire Alternative",
    "related_blurb": "Flat subscription versus pay per completed interview",
    "title": "Spark Hire Alternative: Pay Per Interview, Not Per Month",
    "description": "Comparing Spark Hire alternatives? See how a flat monthly subscription compares with Lumo360's pay-per-completed-interview model and spoken, adaptive first round.",
    "og_title": "A Spark Hire alternative: pay per completed interview",
    "crumb": "Spark Hire alternative",
    "kicker": "Spark Hire alternative",
    "h1": "A Spark Hire alternative that <em>listens and follows up.</em>",
    "sub": ("Spark Hire is a long-running one-way video tool that has grown into an applicant tracking system. "
            "Lumo360 is narrower: a spoken first-round interview that adapts to each candidate, priced per "
            "completed interview rather than per month. Which suits you depends on your hiring pattern as much "
            "as on features."),
    "secondary": ("See the comparison", "#compare"),
    "related": ["one-way-video-interview-alternative", "willo-alternative", "hirevue-alternative"],
    "sections": [
        section(
            "overview", "At a glance", "Spark Hire and Lumo360, in brief",
            cards(
                ("Spark Hire", "Video interviewing plus an ATS", [
                    f"Core product is one-way video, where candidates record answers to set questions; its video plans also include live interviews{S(1)}",
                    f"Video interview plans start at $299 a month, or $249 a month billed annually; the plans include unlimited interviews{S(1)}",
                    f"Its Recruit ATS starts at $335 a month, billed annually, and adds AI video review and transcription{S(1)}",
                    f"Lists integrations with more than 100 providers across job boards, assessments and HRIS{S(2)}",
                ]),
                ("Lumo360", "A conversation instead of a recording", [
                    "A spoken, adaptive first-round conversation built from your job description",
                    "Follow-up questions based on each candidate's answers",
                    "Every score linked to the transcript moments that support it",
                    "A recruiter reviews every result before anyone moves forward",
                    "No subscription: 1 credit assesses a CV, 10 credits run a full interview",
                ], True),
            ),
            cls="bg-white"),
        section(
            "compare", "Side by side", "Spark Hire vs Lumo360",
            compare("Spark Hire", "Lumo360", [
                ("Interview format", f"One-way video; live video on the interview plans{S(1)}",
                 "A spoken, adaptive conversation; keep your usual video tool for later rounds"),
                ("Follow-up questions", "Candidates answer the questions you set",
                 "The interviewer probes deeper based on each answer"),
                ("What the recruiter reviews", f"Recorded answers, with transcription and AI video review on the ATS plans{S(1)}",
                 "A competency-by-competency report, with every score linked to the transcript"),
                ("Beyond the interview", f"Applicant tracking, scheduling, assessments and reference checks{S(1)}{S(2)}",
                 "Focused on the first-round interview and CV assessment"),
                ("Cost model", f"Monthly or annual subscription; interviews are unlimited{S(1)}",
                 "Per completed interview; a free 25-credit trial; bundles from 500 credits"),
            ], note="Based on public information checked in October 2026."),
            sub="Both let candidates interview in their own time. The difference is what happens while they talk, and how you pay."),
        section(
            "cost", "Cost model", "Subscription or pay-per-interview?",
            prose(
                "A flat subscription favours steady, high interview volume: the more you run, the lower the cost "
                "per interview. Pay-per-interview favours uneven hiring, where a quiet month shouldn't cost the "
                "same as a busy one.",
                "On Lumo360 a full interview is 10 credits, which is £5.00 on pay as you go and £4.00 on the "
                "Growth bundle (2,000 credits for £800). In our "
                "<a href=\"/story-tech-scaleup.html\">tech scale-up case study</a>, a two-person talent team "
                "screened for twelve open roles across a quarter for £672. If you run very large numbers of "
                "recorded interviews every month, a flat subscription can still work out cheaper per interview. "
                "The question is whether a recording tells you as much as a conversation does.",
            ),
            sub="We've used only our published prices, and Spark Hire's, which are quoted in US dollars, so compare them against your own volumes."),
        section(
            "fit", "Honest fit", "When Spark Hire may be the better choice",
            prose(
                "If you want video interviews, applicant tracking, scheduling and reference checks from one "
                "supplier on a single subscription, and your hiring is steady enough to use it every month, "
                "Spark Hire covers those.",
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
         "If you like the convenience of Spark Hire but want more than recorded answers, look at conversational "
         "AI interviewers. Lumo360 runs a spoken, adaptive first-round conversation and links every score to "
         "the transcript."),
        ("Is Spark Hire a one-way video interview tool?",
         "One-way video is Spark Hire's core product. Its video interview plans also include live video "
         "interviews, and it sells an applicant tracking system and a behavioural assessment."),
        ("How much does Spark Hire cost?",
         "Spark Hire's pricing page lists video interview plans from $299 a month, or $249 a month billed "
         "annually, and ATS plans from $335 a month billed annually. Prices vary with company size, so check "
         "its pricing page for current figures."),
        ("How is Lumo360 different from Spark Hire?",
         "Candidates have a conversation instead of recording answers to fixed prompts. The interviewer follows "
         "up on what they say, every score links to the transcript, and a recruiter reviews every result. "
         "Pricing is per completed interview rather than a subscription."),
        ("Do I still need a video tool for later rounds?",
         "Yes. Lumo360 handles the first round. Most teams keep their usual video call tool for interviews with "
         "the hiring manager."),
    ],
    "sources": [
        '<a href="https://www.sparkhire.com/pricing" rel="noopener">Spark Hire, pricing page</a>, checked October 2026. Prices in US dollars, excluding sales tax.',
        '<a href="https://www.sparkhire.com/" rel="noopener">Spark Hire, company website</a>, checked October 2026.',
    ],
}
