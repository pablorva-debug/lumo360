from _blocks import section, cards, compare, prose, HOW_IT_WORKS, four_tests

PAGE = {
    "slug": "automate-phone-screening",
    "footer_label": "Automate Phone Screening",
    "related_blurb": "Keep the conversation, lose the calendar",
    "priority": "0.8",
    "title": "Automate Phone Screening Without Losing the Conversation | Lumo360",
    "description": "Phone screens work because they're conversations, but they don't scale. Lumo360 automates the first call with an adaptive AI interviewer.",
    "og_title": "Automate phone screening without losing the conversation",
    "crumb": "Automate phone screening",
    "kicker": "Automated phone screening",
    "h1": "The phone screen works. <em>It just doesn't scale.</em>",
    "sub": ("A good screening call is a conversation: a question, an answer, a follow-up. That's why recruiters "
            "trust it. Lumo360 keeps the conversation and removes the calendar, so every applicant gets a "
            "first-round call, and your team gets the evidence."),
    "secondary": ("Compare the two", "#compare"),
    "related": ["one-way-video-interview-alternative", "ai-screening-for-recruitment-agencies", "ico-ai-recruitment-questions"],
    "sections": [
        section(
            "problem", "The problem", "Where the screening call breaks down",
            cards(
                ("What works", "Why recruiters rely on it", [
                    "It's a real conversation, so vague answers get a follow-up",
                    "Candidates can ask questions and get a feel for the role",
                    "It's quick to judge basic fit, motivation and communication",
                ], True),
                ("What breaks", "Why it doesn't scale", [
                    "Every call needs a slot in two diaries, and missed calls mean rescheduling",
                    "The same questions, asked fifty times, start to drift",
                    "Notes vary by recruiter and by how late in the day the call was",
                    "Time on early calls is time not spent with shortlisted candidates and clients",
                ]),
            ),
            sub="Nobody needs convincing that screening calls are valuable. The problem is the hours they take.",
            cls="bg-white"),
        section(
            "compare", "Side by side", "Recruiter phone screen vs Lumo360",
            compare("Recruiter phone screen", "Lumo360", [
                ("Format", "A live call with a recruiter",
                 "A spoken conversation with an AI interviewer, much like a phone screen"),
                ("Scheduling", "Find a time, chase no-shows, reschedule",
                 "None. Candidates take it when it suits them"),
                ("Follow-up questions", "Yes, if the recruiter has time", "Yes, based on each answer"),
                ("Consistency", "Depends on the recruiter and the day",
                 "Same competency framework and rubric for every candidate"),
                ("Record of the call", "Recruiter notes", "Full transcript, with every score linked to it"),
                ("Who decides", "The recruiter", "The recruiter, after reviewing the evidence"),
                ("How many you can screen", "As many as the team has hours for", "Every applicant"),
            ]),
            sub="Same purpose, same conversational format. Different limits."),
        section(
            "keep", "Honest fit", "Which calls to keep",
            prose(
                "Automating the first round doesn't mean never picking up the phone. Senior and specialist "
                "roles, candidates you've headhunted, and anyone already shortlisted deserve a person's time.",
                "What Lumo360 takes off your plate is the repetitive first call: the one you make to dozens of "
                "applicants per role to check fit, motivation and core competencies. That's where consistency "
                "matters most, and where recruiter time is spread thinnest.",
            )),
        four_tests(),
        HOW_IT_WORKS,
    ],
    "faqs": [
        ("Can you automate phone screening?",
         "Yes. AI interviewers can now run the first-round screening conversation, asking structured questions "
         "and follow-ups, then give the recruiter a report to review. Lumo360 links every score to the "
         "transcript so the recruiter can check the evidence."),
        ("Do candidates mind an automated screening call?",
         "It depends on how it's done. Candidates react badly to AI interviews that aren't disclosed or where "
         "nobody reviews the result. Tell candidates up front what the interview is and that a person reviews "
         "it. With Lumo360, a recruiter reviews every result."),
        ("Will I still speak to candidates?",
         "Yes. Lumo360 handles the repetitive first call. You still speak to the candidates who make it "
         "through, with more context than a first call would have given you."),
        ("What questions does the AI ask?",
         "Lumo360 builds the interview from your job description as a set of competencies. Your recruiter "
         "reviews and adjusts them before the role goes live, and the AI follows up based on each answer."),
        ("Does the AI decide who progresses?",
         "No. Lumo360 recommends, with the evidence for each score. A recruiter reviews every result before "
         "anyone moves forward."),
    ],
}
