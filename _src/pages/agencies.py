from _blocks import section, cards, compare, prose, checks, HOW_IT_WORKS, four_tests

PAGE = {
    "slug": "ai-screening-for-recruitment-agencies",
    "footer_label": "AI Screening for Recruitment Agencies",
    "related_blurb": "Screen every applicant, send clients the evidence",
    "priority": "0.8",
    "title": "AI Candidate Screening for Recruitment Agencies | Lumo360",
    "description": "AI first-round interviews for recruitment agencies: screen every applicant, send clients evidence-backed shortlists, pay per completed interview.",
    "og_title": "AI candidate screening for recruitment agencies",
    "crumb": "AI screening for recruitment agencies",
    "kicker": "For recruitment agencies",
    "h1": "Screen every applicant. <em>Send clients the evidence.</em>",
    "sub": ("Agencies win on speed and on the quality of the shortlist. Lumo360 gives every applicant a "
            "structured first-round conversation, so your consultants spend their time on the candidates and "
            "clients that matter, with evidence to back every recommendation."),
    "secondary": ("How agencies use it", "#workflow"),
    "related": ["automate-phone-screening", "odro-alternative", "one-way-video-interview-alternative"],
    "sections": [
        section(
            "problem", "The problem", "The first round is where consultant time disappears",
            cards(
                ("Today", "Calls, voicemails and notes", [
                    "Every live vacancy brings a wave of applicants who each need a first call",
                    "Consultants lose hours to scheduling, voicemail and rescheduling",
                    "Screening quality varies by consultant, which clients notice",
                    "Good candidates go cold while they wait for a call back",
                ]),
                ("With Lumo360", "Every applicant screened, consistently", [
                    "Every applicant can be invited straight away and take part when it suits them",
                    "The same competency framework is used for every candidate on a role",
                    "Consultants review scored reports instead of making first calls",
                    "Shortlists come with evidence your client can read for themselves",
                ], True),
            ),
            cls="bg-white"),
        section(
            "workflow", "How agencies use it", "From new vacancy to client shortlist",
            checks([
                ("Load the client's job description",
                 "Lumo360 turns it into a structured set of competencies. Your consultant reviews and adjusts "
                 "them, so the screen reflects what the client actually wants."),
                ("Invite every applicant",
                 "Candidates take a spoken, conversational first round in their own time. The interviewer "
                 "follows up on vague answers, as a good consultant would."),
                ("Review the evidence",
                 "Each candidate gets a competency-by-competency report, with every score linked to the "
                 "transcript. Your consultant decides who goes forward."),
                ("Send a stronger shortlist",
                 "Share candidates with the reasoning attached, so the client sees why each one is on the "
                 "list."),
            ]),
            sub="Lumo360 fits around how agencies already work: one vacancy, many applicants, one client to impress.",
            cls="dark"),
        section(
            "pricing", "Pricing that fits agency volumes", "Pay for interviews, not seats",
            prose(
                "Agency volume is uneven: busy one month, quiet the next. Lumo360 uses credits, so you can pay "
                "as you go or buy a bundle at a lower price per credit.",
                "Credits are reserved when a candidate is invited and only charged when the interview is "
                "completed. No-shows don't cost you anything.",
            )),
        section(
            "compare", "Side by side", "Consultant screening call vs Lumo360",
            compare("Consultant call", "Lumo360", [
                ("Who runs the first round", "A consultant, one call at a time", "An AI interviewer, for every applicant"),
                ("Scheduling", "Diary slots, voicemail, reschedules", "None"),
                ("Consistency across consultants", "Varies", "Same framework and rubric for every candidate"),
                ("What the client sees", "Your summary", "Your summary, plus the evidence behind it"),
                ("Who decides", "The consultant", "The consultant, after reviewing the evidence"),
            ])),
        HOW_IT_WORKS,
    ],
    "faqs": [
        ("How do recruitment agencies use AI for candidate screening?",
         "The most common use is the first-round screen: an AI interviewer has a structured conversation with "
         "every applicant, and consultants review the results instead of making every first call themselves."),
        ("Will clients accept AI-screened shortlists?",
         "Clients care about the quality of the shortlist and the reasoning behind it. Lumo360 links every "
         "score to the transcript, so you can show a client exactly why a candidate was put forward, and a "
         "consultant reviews every result."),
        ("How is Lumo360 priced for agencies?",
         "With credits. Pay as you go, or buy a bundle at a lower price per credit. You're only charged for "
         "interviews candidates complete."),
        ("Does it replace our consultants?",
         "No. It replaces the repetitive first call. Consultants still decide who goes forward, and spend more "
         "of their time with shortlisted candidates and clients."),
        ("What do candidates experience?",
         "A structured, spoken conversation, much like a phone screen, which they complete when it suits them, "
         "with nothing to schedule."),
    ],
}
