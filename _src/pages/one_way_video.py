from _blocks import section, cards, pull, compare, prose, HOW_IT_WORKS, four_tests

PAGE = {
    "slug": "one-way-video-interview-alternative",
    "footer_label": "One-Way Video Interview Alternative",
    "related_blurb": "Why candidates want a conversation, not a camera",
    "priority": "0.8",
    "title": "One-Way Video Interview Alternative: Conversational AI | Lumo360",
    "description": "Candidates find one-way video interviews one-sided. Lumo360 runs a spoken, adaptive first round, with every score traceable to the transcript.",
    "og_title": "The one-way video interview alternative: a real conversation",
    "crumb": "One-way video interview alternative",
    "kicker": "One-way video interview alternative",
    "h1": "Swap the one-way video for <em>a real conversation.</em>",
    "sub": ("One-way video interviews ask candidates to perform to a camera while nobody listens. Lumo360 runs a "
            "spoken first-round interview that listens, asks follow-up questions, and shows your team the "
            "evidence behind every score."),
    "secondary": ("Compare the two formats", "#compare"),
    "related": ["phone-screen-alternative", "hirevue-alternative", "ai-screening-for-recruitment-agencies"],
    "sections": [
        section(
            "problem", "The problem", "Why hiring teams are moving on from one-way video",
            cards(
                ("What candidates say", "It feels like recording a podcast for nobody", [
                    'Preparing, rehearsing and re-recording takes far longer than a normal interview<sup><a href="#src-1">1</a></sup>',
                    'There\'s no one to clarify a question, and no chance to ask their own<sup><a href="#src-1">1</a></sup>',
                    'Recording alone on camera is stressful, and puts people without a quiet, polished setup at a disadvantage<sup><a href="#src-1">1</a></sup>',
                    'They worry about who watches the footage, and whether software is judging their tone and body language<sup><a href="#src-1">1</a></sup>',
                ]),
                ("What recruiters get", "Hours of footage, and a fixed script", [
                    "Someone still has to watch the videos, so the time saved on scheduling goes on screening instead",
                    "Candidates answer the same fixed prompts with no follow-up, so vague answers stay vague",
                    'Recordings reward on-camera polish, which most roles don\'t need<sup><a href="#src-1">1</a></sup>',
                    'Seeing faces this early invites the very bias structured screening is meant to remove<sup><a href="#src-1">1</a></sup>',
                ]),
            ) + "\n" + pull(
                "“Candidates aren't walking away from AI. They're walking from bad experiences caused by bad AI.”",
                'Greenhouse, quoted in Fortune\'s coverage of its 2026 candidate survey, in which around 38% of job '
                'seekers said they had withdrawn from a hiring process because it included an AI interview'
                '<sup><a href="#src-2">2</a></sup>'),
            sub=("One-way video solved a real problem: nobody has to schedule a call. But it shifted the effort "
                 "onto candidates and the watching onto recruiters, and both sides have noticed."),
            cls="bg-white"),
        section(
            "compare", "Side by side", "One-way video vs a conversational interview",
            compare("One-way video", "Lumo360 conversation", [
                ("What the candidate does", "Records answers to a fixed list of prompts on camera",
                 "Takes part in a structured, spoken conversation, much like a phone screen"),
                ("Follow-up questions", "None. Every candidate gets the same prompts, whatever they say",
                 "The interviewer probes deeper based on each answer, within a fixed framework"),
                ("Where the questions come from", "A question bank someone has to write and maintain",
                 "Generated from your job description as a set of competencies, which your recruiter reviews before the role goes live"),
                ("Scheduling", "None needed", "None needed"),
                ("What the recruiter reviews", "Each video, end to end",
                 "A competency-by-competency report, with the full transcript a click away"),
                ("How scores are explained", "Reviewer notes, or a score from software that doesn't show its working",
                 "Every score is linked to the transcript moments that support it"),
                ("Consistency", "Same questions, but judgement varies from reviewer to reviewer",
                 "Same competency framework and rubric applied to every candidate"),
                ("Who decides", "A recruiter",
                 "A recruiter. Lumo360 recommends; a person reviews every result before anyone moves forward"),
            ], note="One-way video tools differ, and some now add AI features. This compares the formats, not any one product."),
            sub="Both formats let candidates interview in their own time. What changes is whether anyone is listening."),
        four_tests(
            sub=("Whichever tool you choose, including ours, hold it to these four tests. If a vendor can't meet "
                 "them, you're swapping one problem for another."),
            last_text=('In Gartner\'s research, only 31% of candidates who had an AI interview knew about it in '
                       'advance.<sup><a href="#src-3">3</a></sup> Tell people what the interview is, how it\'s '
                       'assessed and that a person reviews it.')),
        HOW_IT_WORKS,
        section(
            "switching", "Switching", "Already using a one-way video platform?",
            prose(
                "You don't need to migrate a question bank. Lumo360 builds each interview from the job "
                "description, so switching starts with the next role you open, not a project plan.",
                "We suggest running both formats side by side on one role and comparing the shortlists. Setup is "
                "quick: the first screening workflow is typically live within a day.",
            ),
            cls="bg-white"),
    ],
    "faqs": [
        ("What is a one-way video interview?",
         "A one-way video interview (also called an asynchronous or pre-recorded video interview) asks candidates "
         "to record answers to a fixed set of questions on camera, with no interviewer present. The recruiter "
         "watches the recordings later."),
        ("What is the best alternative to a one-way video interview?",
         "A conversational interview: one where someone, or something, listens to the answer and asks a relevant "
         "follow-up. Recruiter phone screens do this well but don't scale. Conversational AI interviews like "
         "Lumo360 run a structured, spoken conversation with every applicant, then give the recruiter an "
         "evidence-backed report to review."),
        ("Can candidates still complete it in their own time?",
         "Yes. Like one-way video, there is nothing to schedule. Candidates complete a Lumo360 interview when it "
         "suits them. The difference is that it feels like a structured phone-style conversation rather than "
         "recording answers to a camera."),
        ("Does the AI decide who gets hired?",
         "No. Lumo360 runs the first-round conversation and recommends, with the evidence for each score. A "
         "recruiter reviews every result before any candidate moves forward."),
        ("How long does it take to switch from a one-way video tool?",
         "Lumo360 builds the interview from your job description, so there is no question bank to migrate. The "
         "first screening workflow is typically live within a day."),
    ],
    "sources": [
        '<a href="https://www.askamanager.org/2025/03/whats-the-deal-with-one-way-recorded-video-interviews.html" rel="noopener">Ask a Manager, "What\'s the deal with one-way recorded video interviews?"</a>, March 2025, and reader responses.',
        '<a href="https://fortune.com/2026/05/04/4-in-10-job-candidates-bailed-hiring-rounds-required-ai-interview/" rel="noopener">Fortune, "Nearly 4 in 10 job candidates have bailed on a hiring round because it required an AI interview"</a>, 4 May 2026, reporting Greenhouse survey data.',
        '<a href="https://www.recruitingnewsnetwork.com/posts/human-touch-vs-ai-navigating-the-new-hiring-landscape" rel="noopener">Recruiting News Network, "Human touch vs AI: navigating the new hiring landscape"</a>, January 2026, citing Gartner\'s 3Q25 candidate survey.',
    ],
}
