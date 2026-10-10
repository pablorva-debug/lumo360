from _blocks import section, cards, compare, steps, prose, disclaimer, brand_disclaimer

S = lambda n: f'<sup><a href="#src-{n}">{n}</a></sup>'

PAGE = {
    "slug": "odro-alternative",
    "footer_label": "Odro Alternative",
    "related_blurb": "Keep live video for the shortlist, automate the first round",
    "title": "Odro Alternative for Recruitment Agencies | Lumo360",
    "description": "Looking at Odro alternatives? See how an adaptive first-round interview fits an agency workflow, so live video is saved for the shortlist your clients see.",
    "og_title": "An Odro alternative for agency first-round screening",
    "crumb": "Odro alternative",
    "kicker": "Odro alternative",
    "h1": "Keep live video for the shortlist. <em>Let the first round run itself.</em>",
    "sub": ("Odro is video interviewing and engagement technology built for recruiters. Lumo360 covers the stage "
            "before it: a spoken, adaptive first-round conversation with every applicant, so your consultants "
            "spend live time only on candidates with evidence behind them."),
    "secondary": ("See the comparison", "#compare"),
    "related": ["ai-screening-for-recruitment-agencies", "one-way-video-interview-alternative", "launchpad-alternative"],
    "sections": [
        section(
            "overview", "At a glance", "Odro and Lumo360, in brief",
            cards(
                ("Odro", "Video interviewing and engagement for recruiters", [
                    f"Offers asynchronous and two-way video interviewing, digital shortlisting and video messaging{S(1)}",
                    f"Third-party listings add panel interviews, pre-recorded messages, candidate practice sessions and session recording{S(2)}",
                    f"Lists integrations including Bullhorn, Vincere, Paiger and Microsoft Teams{S(2)}",
                    f"In 2021 Hays announced a multi-year partnership giving over 1,800 UK and Ireland recruiters access to it{S(1)}",
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
                ("Consistency across consultants", "Depends on who runs each call",
                 "The same competency framework and rubric for every candidate"),
                ("Agency systems", f"Lists Bullhorn, Vincere and Paiger integrations{S(2)}",
                 "Ask us about your ATS or CRM"),
            ], note="Based on public information checked in October 2026."),
            sub="These tools can work together: Lumo360 for the first round, live video for the shortlist."),
        section(
            "workflow", "Agency workflow", "Where each tool fits in a vacancy",
            steps([
                ("Applicants arrive",
                 "A job advert can bring dozens or hundreds of applicants. Lumo360 gives every one of them the "
                 "same first conversation, built from the client's job description."),
                ("Consultants read a report",
                 "Each consultant reviews a scored, evidence-linked report instead of making screening calls. "
                 "They decide who moves forward."),
                ("Live video for the shortlist",
                 "Use Odro or your usual video tool for the interviews that need a person, and for presenting "
                 "candidates to the client."),
            ]),
            sub="See the full agency picture in our guide to <a href=\"/ai-screening-for-recruitment-agencies\">AI candidate screening for recruitment agencies</a>."),
        section(
            "fit", "Honest fit", "Replace, or use alongside?",
            prose(
                "If most of your interviewing is live, with consultants meeting candidates and clients meeting "
                "shortlists, keep a live video tool. Lumo360 doesn't replace that.",
                "Where Lumo360 helps is the stage before: the applicants per vacancy who each need a first "
                "conversation. Screen them all consistently, then spend live time on the ones who earned it.",
            )),
        section("note", "About this comparison", "How we wrote this page",
                disclaimer(brand_disclaimer("Odro") + " When we checked in October 2026, odro.com did not show a product page, so details here come from the third-party sources below, dated as shown. Please confirm Odro's current status and features before making a decision."), cls="bg-white"),
    ],
    "faqs": [
        ("What is the best alternative to Odro?",
         "If your problem is first-round screening volume, a conversational AI interviewer such as Lumo360 "
         "automates the first call. If you need live video with clients, a video interviewing tool is still "
         "the right fit, and the two work together."),
        ("What does Odro do?",
         "Odro is video interviewing and engagement technology for recruiters, offering asynchronous and "
         "two-way video interviews, digital shortlisting and video messaging."),
        ("How is Lumo360 different from Odro?",
         "Lumo360 automates the first-round screen with a spoken, adaptive conversation. Every score links to "
         "the transcript, and a consultant reviews every result. Live video is saved for the shortlist."),
        ("Can recruitment agencies use Lumo360 for client shortlists?",
         "Yes. Agencies use it to screen every applicant and send clients evidence-backed shortlists. See our "
         "<a href=\"/ai-screening-for-recruitment-agencies\">guide for recruitment agencies</a>."),
    ],
    "sources": [
        '<a href="https://www.privateequitywire.co.uk/bgf-backed-odro-secures-hays-deal/" rel="noopener">Private Equity Wire, "BGF-backed Odro secures Hays deal"</a>, August 2021.',
        '<a href="https://www.capterra.com/p/185590/Odro/" rel="noopener">Capterra, "Odro"</a>, product listing, checked October 2026.',
    ],
}
