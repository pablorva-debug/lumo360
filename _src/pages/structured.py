from _blocks import section, cards, compare, checks, steps, prose

S = lambda n: f'<sup><a href="#src-{n}">{n}</a></sup>'

PAGE = {
    "slug": "structured-interviews",
    "footer_label": "Structured Interview Guide",
    "related_blurb": "Competencies, questions and a scoring rubric, step by step",
    "priority": "0.8",
    "title": "Structured Interviews: Competencies, Questions and Scoring Rubrics",
    "description": ("How to run a structured interview: turn a job description into competencies, write "
                    "behavioural questions and follow-ups, and score against an anchored rubric."),
    "og_title": "How to build a structured interview, from job description to scoring rubric",
    "crumb": "Structured interview guide",
    "kicker": "Hiring guide",
    "h1": "How to build a structured interview, <em>from job description to rubric.</em>",
    "sub": ("Structured interviews are the best single predictor of job performance in the most recent large "
            "review of selection research. Every candidate answers the same job-related questions and is "
            "scored against the same rubric. This guide shows how to build one, step by step."),
    "secondary": ("Jump to the steps", "#build"),
    "related": ["automate-phone-screening", "one-way-video-interview-alternative", "eu-ai-act-recruitment"],
    "sections": [
        section(
            "why", "The evidence", "Why structure beats a conversation that wanders",
            prose(
                f"In 2022, Sackett and colleagues re-ran the best-known estimates of how well hiring methods "
                f"predict job performance. Structured interviews came out on top, with a mean validity of .42, "
                f"ahead of job knowledge tests (.40), work samples (.33) and cognitive ability tests (.31){S(1)}.",
                f"Unstructured interviews, where each interviewer asks whatever comes to mind, came out at about "
                f".19, less than half the structured figure{S(2)}. They feel informative, but much of what they "
                f"measure is the interviewer's impression rather than the candidate's ability.",
                f"Structure helps candidates too. Google reports that candidates rated structured interviews as "
                f"fairer, that rejected candidates who had one were 35% happier than those who didn't, and that "
                f"ready-made questions and rubrics saved interviewers an average of 40 minutes per interview{S(3)}.",
            ),
            cls="bg-white"),
        section(
            "parts", "The essentials", "What makes an interview structured",
            checks([
                ("Competencies from the job",
                 "Decide what the role needs before meeting anyone, and assess only that. Everything else in the "
                 "interview hangs off this list."),
                ("The same core questions",
                 f"Every candidate gets the same questions, each tied to a competency. Google's guidance adds "
                 f"planned follow-ups that probe how the candidate reached their answer{S(3)}."),
                ("An anchored rubric",
                 f"Each competency has a scale with examples of what a poor, borderline, solid and outstanding "
                 f"answer looks like, so two interviewers mean the same thing by a 3{S(3)}."),
                ("Evidence, then a decision",
                 f"Record what the candidate actually said, score each competency on its own, and only then make "
                 f"an overall call. Notes let someone else check the score later{S(3)}."),
            ]),
            sub="Remove any one of these and the interview drifts back towards gut feel.",
            cls="dark"),
        section(
            "build", "Step by step", "Build one from a job description",
            steps([
                ("Pick four to six competencies",
                 "Read the job description and pull out the skills and behaviours that separate good performers "
                 "from average ones. Fewer, sharper competencies beat a long list nobody can assess in 30 minutes."),
                ("Define each one in observable terms",
                 "\"Good communicator\" is a label. \"Explains a complex issue so a non-specialist can act on it\" "
                 "is something you can hear in an answer."),
                ("Write the questions and follow-ups",
                 "One or two questions per competency: behavioural (\"Tell me about a time...\") or situational "
                 "(\"Imagine that...\"). Add follow-ups that ask what the candidate did, why, and what happened."),
                ("Write the rubric before you interview",
                 "For each competency, describe what a 1, 2, 3 and 4 answer contains. Writing anchors after the "
                 "interview lets the strongest impression set the bar."),
                ("Review it with the hiring manager",
                 "Agree the competencies and the rubric before the role goes live. Disagreements about what the "
                 "job needs surface here, not after the third interview."),
                ("Score competencies separately, then decide",
                 "Score each competency against its anchors with the evidence in front of you. Then make the "
                 "overall decision, and write down why."),
            ]),
            sub="The four-to-six range and the 1–4 scale are our recommendations; adjust them to the role."),
        section(
            "example", "Worked example", "One competency, from definition to score",
            prose(
                "<strong>Role:</strong> customer success manager. <strong>Competency:</strong> handling a "
                "difficult stakeholder. <strong>Definition:</strong> keeps a strained relationship productive "
                "while protecting the outcome the customer needs.",
                "<strong>Question:</strong> \"Tell me about a time a customer was unhappy with something you "
                "couldn't change. What did you do?\" <strong>Follow-ups:</strong> \"What did you say first?\" "
                "\"What did you offer instead?\" \"What happened to the account afterwards?\"",
            ) + "\n" + compare("Weak answer (1–2)", "Strong answer (3–4)", [
                ("The situation", "Vague or generic: \"customers are often difficult\"",
                 "A specific customer, a specific problem, and why it mattered to them"),
                ("What they did", "Talks about what \"we\" did, or what the policy was",
                 "Describes their own actions and the reasoning behind them"),
                ("The outcome", "No result, or one they can't connect to their actions",
                 "A concrete result, such as a renewal, a recovered relationship or a changed process"),
                ("Reflection", "None, or blames the customer",
                 "What they would do differently, or what they took into the next account"),
            ], note="An anchored rubric like this lets two interviewers reach the same score from the same answer."),
            cls="bg-white"),
        section(
            "mistakes", "Common mistakes", "Where structured interviews go wrong",
            cards(
                ("Design", "Mistakes before the interview", [
                    "Too many competencies, so none is assessed properly",
                    "Competencies copied from a generic framework, not this role",
                    "Questions that test interview polish rather than the competency",
                    "No rubric, or one written after meeting the candidates",
                ]),
                ("Delivery", "Mistakes during and after", [
                    "Skipping questions for candidates who \"obviously\" have it",
                    "Scoring from memory at the end of the day",
                    "Letting one strong answer lift every other score",
                    "Deciding first, then filling in the scores to match",
                ]),
            )),
        section(
            "ai", "Where AI fits", "Running structured first rounds at volume",
            prose(
                "The hard part of structure is doing it every time, for every applicant, when there are hundreds "
                "of them. That is the gap Lumo360 is built for.",
                "Lumo360 turns your job description into a competency framework, which your team reviews and "
                "adjusts before the role goes live. Every candidate then has a spoken first-round conversation "
                "built on the same framework and rubric. Follow-up questions adapt to each answer, but stay "
                "within the competency being assessed. Each score links to the transcript moments behind it, and "
                "a recruiter reviews every result before anyone moves forward.",
                "See what this looks like for <a href=\"/automate-phone-screening\">automating the first phone "
                "screen</a>, or how it compares with <a href=\"/one-way-video-interview-alternative\">one-way "
                "video interviews</a>.",
            ),
            cls="bg-white"),
    ],
    "faqs": [
        ("What is a structured interview?",
         "An interview where every candidate for a role is asked the same job-related questions and scored "
         "against the same rubric, with the competencies and scoring decided before any interview takes place."),
        ("Are structured interviews better than unstructured ones?",
         "Yes. A 2022 review of selection research by Sackett and colleagues put the mean validity of structured "
         "interviews at .42, the highest of the methods reviewed. Unstructured interviews came out at about .19."),
        ("What is a competency-based interview?",
         "A structured interview built around the competencies the role needs, usually using behavioural "
         "questions that ask candidates to describe what they actually did in past situations."),
        ("How many competencies should an interview assess?",
         "We recommend four to six for a first-round interview. More than that and there isn't time to gather "
         "real evidence on each one."),
        ("Can you follow up on answers in a structured interview?",
         "Yes. Good structured interviews include follow-up questions that probe the candidate's reasoning. "
         "What stays fixed is the competencies, the core questions and the rubric."),
    ],
    "sources": [
        '<a href="https://www.siop.org/tip-article/is-cognitive-ability-the-best-predictor-of-job-performance" rel="noopener">SIOP, "Is cognitive ability the best predictor of job performance?"</a>, summarising Sackett, P. R., Zhang, C., Berry, C. M., &amp; Lievens, F. (2022), <em>Journal of Applied Psychology</em>, 107, 2040–2068.',
        '<a href="https://kitalent.com/research/interviewing-for-skills-and-identity/chapter-2-evidence-not-impressions" rel="noopener">KiTalent, "Evidence, not impressions"</a>, reporting the Sackett et al. (2022) estimate for unstructured interviews.',
        '<a href="https://rework.withgoogle.com/intl/en/guides/a-guide-to-structured-interviewing-for-better-hiring-practices" rel="noopener">Google re:Work, "A guide to structured interviewing for better hiring practices"</a>.',
    ],
}
