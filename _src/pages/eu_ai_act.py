from _blocks import section, checks, prose, qa, disclaimer, HOW_IT_WORKS

S = lambda n: f'<sup><a href="#src-{n}">{n}</a></sup>'

PAGE = {
    "slug": "eu-ai-act-recruitment",
    "footer_label": "EU AI Act for Recruiters",
    "related_blurb": "What the EU AI Act means for AI hiring tools, and when",
    "priority": "0.8",
    "title": "EU AI Act for Recruiters: What It Means for AI Hiring Tools",
    "description": ("AI that screens or evaluates candidates is high-risk under the EU AI Act. What already "
                    "applies, what moved to December 2027, and what employers and vendors must do."),
    "og_title": "The EU AI Act and AI in recruitment, in plain English",
    "crumb": "EU AI Act for recruiters",
    "kicker": "EU compliance guide",
    "h1": "The EU AI Act and AI in recruitment, <em>in plain English.</em>",
    "sub": ("AI used to screen or evaluate job candidates is classed as high-risk under the EU AI Act. The main "
            "obligations now apply from 2 December 2027, after the Digital Omnibus moved the original August "
            "2026 date. Some rules already apply today. Here is what each one means for an employer using an "
            "AI hiring tool."),
    "secondary": ("See the timeline", "#timeline"),
    "related": ["ico-ai-recruitment-questions", "one-way-video-interview-alternative", "hirevue-alternative"],
    "sections": [
        section(
            "timeline", "Timeline", "Which rules apply, and from when",
            checks([
                ("2 February 2025: banned practices and AI literacy",
                 f"Prohibited AI practices apply, including emotion recognition in the workplace{S(1)}. "
                 f"Employers and vendors must also support AI literacy among staff who use AI; the Digital "
                 f"Omnibus softened this to a duty to support literacy rather than guarantee a set level{S(2)}."),
                ("2 August 2026: telling people they're talking to an AI",
                 f"Transparency rules in Article 50 apply. An AI system that interacts directly with people must "
                 f"make sure they are \"informed that they are interacting with an AI system\"{S(3)}. The "
                 f"Omnibus did not change these obligations{S(4)}."),
                ("2 December 2027: high-risk obligations for recruitment AI",
                 f"Obligations for high-risk systems listed in Annex III, which includes employment, now apply "
                 f"from this date. It was originally 2 August 2026, and was moved by Regulation (EU) 2026/1744, "
                 f"in force since 27 July 2026{S(2)}{S(5)}."),
                ("Until then: prepare, don't wait",
                 "The extra time is for standards and guidance to catch up, not a reason to pause. Contracts "
                 "you sign now will very likely still be running in December 2027."),
            ]),
            sub="The Digital Omnibus delayed the high-risk rules. It did not remove them.",
            cls="dark"),
        section(
            "high-risk", "Classification", "Is your recruitment tool high-risk?",
            prose(
                f"Almost certainly, if it screens or evaluates candidates. Annex III of the Act lists "
                f"\"AI systems intended to be used for the recruitment or selection of natural persons, in "
                f"particular to place targeted job advertisements, to analyse and filter job applications, and "
                f"to evaluate candidates\"{S(6)}.",
                f"There is a narrow exception for systems that don't pose a significant risk, such as tools that "
                f"only do a narrow procedural task or preparatory work{S(7)}. But it doesn't apply to profiling: "
                f"an Annex III system that profiles people \"shall always be considered to be high-risk\"{S(7)}. "
                f"A tool that scores candidates on competencies is hard to fit into the exception.",
                f"The Act also reaches beyond the EU. It covers providers and deployers based outside the EU "
                f"\"where the output produced by the AI system is used in the Union\"{S(8)}, so a UK employer "
                f"hiring for EU roles, or a UK vendor selling to EU employers, can be in scope.",
            )),
        section(
            "emotion", "Already in force", "No emotion recognition in interviews",
            prose(
                f"Since 2 February 2025, it has been prohibited to use AI \"to infer emotions of a natural person "
                f"in the areas of workplace and education institutions\", except for medical or safety reasons{S(1)}. "
                f"Commission guidelines read \"workplace\" broadly, covering the relationship from recruitment to "
                f"dismissal{S(1)}.",
                f"In practice, an interview tool that reads facial expressions or tone of voice to judge whether a "
                f"candidate is nervous, enthusiastic or honest is a serious risk. Breaches of the prohibitions "
                f"carry the Act's highest fines: up to €35 million or 7% of worldwide annual turnover, whichever is "
                f"higher; for SMEs, whichever is lower{S(9)}.",
            ),
            cls="bg-white"),
        section(
            "employers", "Deployer duties", "What employers using AI hiring tools must do",
            checks([
                ("Use it as the vendor intends",
                 f"Take appropriate technical and organisational measures to use the system in line with the "
                 f"provider's instructions for use{S(10)}."),
                ("Put a qualified person in charge",
                 f"Assign human oversight to people with \"the necessary competence, training and authority\"{S(10)}."),
                ("Monitor it, and keep the logs",
                 f"Monitor the system, report risks to the provider and authorities, and keep the logs it "
                 f"generates for at least six months{S(10)}."),
                ("Tell candidates and workers",
                 f"Inform people that they are subject to a high-risk system used to make or assist decisions "
                 f"about them, and inform workers' representatives before using one in the workplace{S(10)}."),
                ("Run a data protection impact assessment",
                 f"Use the information the provider must supply to carry out your DPIA under data protection law{S(10)}."),
                ("Be ready to explain a decision",
                 f"People affected by a decision based on a high-risk system's output can ask for \"clear and "
                 f"meaningful explanations of the role of the AI system\" and the main elements of the decision{S(11)}."),
            ]),
            sub=f"These are the deployer obligations in Article 26, plus the right to explanation in Article 86. Breaches can lead to fines of up to €15 million or 3% of worldwide turnover{S(9)}.",
            cls="dark"),
        section(
            "vendor", "Due diligence", "Questions to ask your AI hiring vendor now",
            qa([
                ("Classification", "Do you treat your product as a high-risk AI system?",
                 ["If a tool screens or evaluates candidates and the vendor says it isn't high-risk, ask them to "
                  "explain why in writing."], ""),
                ("Emotion inference", "Does the tool infer emotions, from video, voice or text?",
                 ["Ask directly, and get the answer in the contract. This has been prohibited at work since "
                  "February 2025."], ""),
                ("Explanations", "Can a recruiter see why a candidate got a particular score?",
                 ["You will need this to meet the right to explanation, and to answer a rejected candidate's "
                  "question fairly."],
                 "Every score links to the transcript moments that support it, so a recruiter can show the evidence behind it."),
                ("Human oversight", "Does a person review every result before a candidate is rejected?",
                 ["Oversight has to be real: a named, trained person with the authority to overrule the system."],
                 "A recruiter reviews every result before anyone moves forward or is rejected."),
                ("Disclosure", "How are candidates told they are speaking to an AI?",
                 ["From August 2026 this is required by Article 50, and candidates react badly when they find out "
                  "later."], ""),
                ("Records", "What logs and documents will you give us, and for how long?",
                 ["You need logs for at least six months, and enough information from the vendor to complete your "
                  "DPIA."], ""),
            ]),
            sub="Our own answers are included where we can give them today. For the rest, ask us for our current position."),
        section(
            "uk", "UK employers", "If you only hire in the UK",
            prose(
                "The EU AI Act doesn't apply to UK-only hiring. UK GDPR and the Information Commissioner's Office "
                "set the rules instead, and the ICO has published its own six questions for buyers of AI "
                "recruitment tools.",
                "Read our <a href=\"/ico-ai-recruitment-questions\">guide to the ICO's six questions</a>. If you "
                "hire into EU roles as well, plan for both.",
            ),
            cls="bg-white"),
        HOW_IT_WORKS,
        section("note", "About this guide", "What this guide is, and isn't",
                disclaimer("This guide summarises Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744, "
                           "checked in October 2026. It is general information, not legal advice. Guidance and "
                           "standards are still being published, so take advice on your own situation."),
                cls="bg-white"),
    ],
    "faqs": [
        ("Is AI recruitment software high-risk under the EU AI Act?",
         "Yes, in most cases. Annex III lists AI used for recruitment or selection, including analysing and "
         "filtering applications and evaluating candidates, as high-risk. A narrow exception exists, but it never "
         "applies to systems that profile people."),
        ("When do the EU AI Act rules for recruitment apply?",
         "The high-risk obligations apply from 2 December 2027, moved from 2 August 2026 by the Digital Omnibus "
         "(Regulation (EU) 2026/1744). The ban on emotion recognition at work has applied since 2 February 2025, "
         "and the duty to tell people they are interacting with an AI applies from 2 August 2026."),
        ("Can AI interviews analyse candidates' emotions?",
         "No. Since 2 February 2025 the EU AI Act prohibits using AI to infer emotions in the workplace, which "
         "Commission guidance says includes recruitment, except for medical or safety reasons."),
        ("Does the EU AI Act apply to UK companies?",
         "It can. The Act covers providers and deployers outside the EU where the AI system's output is used in "
         "the EU, for example a UK company hiring for roles in the EU. UK-only hiring is covered by UK GDPR and "
         "ICO guidance instead."),
        ("Do candidates have to be told an AI is involved?",
         "Yes. From 2 August 2026 people must be told when they are interacting directly with an AI system, and "
         "from December 2027 employers must inform candidates that a high-risk AI system is being used in "
         "decisions about them."),
    ],
    "sources": [
        '<a href="https://legalblogs.wolterskluwer.com/global-workplace-law-and-policy/the-prohibition-of-ai-emotion-recognition-technologies-in-the-workplace-under-the-ai-act/" rel="noopener">Wolters Kluwer Global Workplace Law &amp; Policy, "The prohibition of AI emotion recognition technologies in the workplace under the AI Act"</a>, on Article 5(1)(f) and the Commission guidelines.',
        '<a href="https://www.cuatrecasas.com/en/global/intellectual-property/art/digital-omnibus-ai-has-been-published" rel="noopener">Cuatrecasas, "Digital Omnibus on AI has been published"</a>, July 2026.',
        '<a href="https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50" rel="noopener">European Commission AI Act Service Desk, Article 50</a>.',
        '<a href="https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/" rel="noopener">Gibson Dunn, "EU AI Act Omnibus agreement: postponed high-risk deadlines and other key changes"</a>, May 2026.',
        '<a href="https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng" rel="noopener">Regulation (EU) 2026/1744 of 8 July 2026 (Digital Omnibus on AI)</a>, EUR-Lex.',
        '<a href="https://www.euaiact.com/annex/3" rel="noopener">EU AI Act, Annex III, point 4(a)</a>.',
        '<a href="https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6" rel="noopener">European Commission AI Act Service Desk, Article 6</a>.',
        '<a href="https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-2" rel="noopener">European Commission AI Act Service Desk, Article 2</a>.',
        '<a href="https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-99" rel="noopener">European Commission AI Act Service Desk, Article 99</a>.',
        '<a href="https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26" rel="noopener">European Commission AI Act Service Desk, Article 26</a>.',
        '<a href="https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-86" rel="noopener">European Commission AI Act Service Desk, Article 86</a>.',
    ],
}
