from _blocks import section, cards, compare, checks, prose, disclaimer, brand_disclaimer

S = lambda n: f'<sup><a href="#src-{n}">{n}</a></sup>'

PAGE = {
    "slug": "launchpad-alternative",
    "footer_label": "LaunchPad Recruits Alternative",
    "related_blurb": "Graduate and volume screening that still feels human",
    "title": "LaunchPad Recruits Alternative for High-Volume Hiring",
    "description": "Comparing LaunchPad Recruits alternatives for graduate and high-volume hiring? See how an adaptive first-round interview handles thousands of applicants.",
    "og_title": "A LaunchPad Recruits alternative for high-volume and graduate hiring",
    "crumb": "LaunchPad Recruits alternative",
    "kicker": "LaunchPad Recruits alternative",
    "h1": "A LaunchPad alternative for volume hiring that <em>still feels human.</em>",
    "sub": ("LaunchPad Recruits built its name on video interviews for graduate and high-volume hiring, and is now "
            "part of Harver. If you're reviewing how your team screens a thousand applicants for ninety places, "
            "the question is how much signal each first round gives you."),
    "secondary": ("See the comparison", "#compare"),
    "related": ["automate-phone-screening", "one-way-video-interview-alternative", "odro-alternative"],
    "sections": [
        section(
            "overview", "At a glance", "LaunchPad and Lumo360, in brief",
            cards(
                ("LaunchPad Recruits", "Video interviewing for in-house volume hiring", [
                    f"Launched in the UK in 2012 as a video interviewing service; candidates answer questions on video{S(1)}",
                    f"Listed as designed for in-house recruitment teams with high hiring volume{S(2)}",
                    f"Third-party listings include skills assessment and scoring, live video, a question library and session recording{S(2)}",
                    f"Now part of Harver, a volume-hiring and assessment platform; launchpadrecruits.com redirected to harver.com when we checked{S(3)}",
                    f"No public price listed{S(2)}",
                ]),
                ("Lumo360", "A spoken first round at any volume", [
                    "A spoken, adaptive first-round conversation built from your job description",
                    "Follow-up questions based on each candidate's answers",
                    "Every score linked to the transcript moments that support it",
                    "A recruiter reviews every result before anyone moves forward",
                    "Credit-based pricing: pay only for completed interviews",
                ], True),
            ),
            cls="bg-white"),
        section(
            "compare", "Side by side", "LaunchPad vs Lumo360",
            compare("LaunchPad Recruits", "Lumo360", [
                ("Interview format", f"Candidates answer set questions on video{S(1)}",
                 "A spoken, adaptive conversation, completed in the candidate's own time"),
                ("Follow-up questions", "Candidates answer the questions you set",
                 "The interviewer probes deeper based on each answer"),
                ("Reviewing at volume", "Reviewers watch or skim candidate recordings",
                 "A scored report per candidate, with the transcript a click away"),
                ("Part of a wider platform", f"Now part of Harver's assessment and volume-hiring suite{S(3)}",
                 "Focused on the first-round interview"),
                ("Pricing", f"Not published{S(2)}",
                 "Published: credits, pay as you go or in bundles; only completed interviews are charged"),
            ], note="Based on public information checked in October 2026. LaunchPad's own site now redirects to Harver, so confirm what is still sold under the LaunchPad name."),
            sub="Both are built for the first round when applicant numbers outrun the team."),
        section(
            "volume", "Volume in practice", "What a high-volume first round looks like",
            checks([
                ("1,000 applicants, 90 places",
                 "In our <a href=\"/story-graduate-scheme.html\">graduate scheme case study</a>, a three-person "
                 "talent team screened around 1,000 applicants for 90 places: 3,500 credits, £1,400 on Growth bundles."),
                ("300 roles in six weeks",
                 "In our <a href=\"/story-seasonal-hiring.html\">seasonal hiring case study</a>, a customer "
                 "operations team screened about 2,400 applicants for 300 roles with scorecards in under 24 hours."),
                ("Same questions, every candidate",
                 "Each role gets one competency framework, reviewed by the hiring team, so candidates are compared "
                 "on the same evidence, not on who was screened first."),
                ("People make the decisions",
                 "The AI runs the conversation and recommends. A recruiter reviews every result before anyone "
                 "moves forward or is rejected."),
            ]),
            cls="bg-white"),
        section(
            "fit", "Honest fit", "When a video-first tool may be the better choice",
            prose(
                "If your graduate process depends on seeing candidates on camera early, or you want video "
                "interviewing as part of a wider assessment suite, a platform such as Harver may suit you.",
                "If your priority is a fair, consistent first conversation with everyone, and evidence your "
                "team can open and check, that is what Lumo360 is built for. Compare it with "
                "<a href=\"/automate-phone-screening\">automating the phone screen</a>, which many volume teams "
                "are trying to replace.",
            )),
        section("note", "About this comparison", "How we wrote this page",
                disclaimer(brand_disclaimer("LaunchPad Recruits")), cls="bg-white"),
    ],
    "faqs": [
        ("What is the best alternative to LaunchPad Recruits?",
         "For high-volume and graduate screening, look at conversational AI interviewers. Lumo360 runs a "
         "spoken, adaptive first round with every applicant and links every score to the transcript."),
        ("Is LaunchPad Recruits now part of Harver?",
         "Third-party listings say so, and launchpadrecruits.com redirected to harver.com when we checked in "
         "October 2026. Confirm with Harver what is currently sold under the LaunchPad name."),
        ("How is Lumo360 different from LaunchPad?",
         "Candidates have a spoken conversation that follows up on their answers instead of recording answers "
         "to set questions. Every score links to the transcript, and a recruiter reviews every result."),
        ("Can Lumo360 handle graduate schemes and seasonal hiring?",
         "Yes. See our case studies on a graduate intake of around 1,000 applicants and a seasonal campaign of "
         "about 2,400 applicants."),
    ],
    "sources": [
        '<a href="https://www.recruiter.co.uk/node/18413" rel="noopener">Recruiter, "Product launch: Lift-off for Launchpad Recruits"</a>, 2012.',
        '<a href="https://www.capterra.com/p/162695/LaunchPad-RECRUITS/" rel="noopener">Capterra, "LaunchPad Recruits"</a>, product listing, checked October 2026.',
        '<a href="https://www.cielotalent.com/recruiting-technology-navigator/launchpad/" rel="noopener">Cielo, "LaunchPad Recruits"</a>, technology navigator, and <a href="https://harver.com/" rel="noopener">Harver</a>, checked October 2026.',
    ],
}
