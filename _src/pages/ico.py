from _blocks import section, qa, prose, HOW_IT_WORKS

S = lambda n: f'<sup><a href="#src-{n}">{n}</a></sup>'

# Lines marked [TO CONFIRM] need an answer from the Lumo360 team before publishing.
# _src/check.py fails while any remain.

PAGE = {
    "slug": "ico-ai-recruitment-questions",
    "footer_label": "ICO AI Recruitment Questions",
    "related_blurb": "The six questions the ICO says to ask, answered",
    "priority": "0.8",
    "title": "ICO AI in Recruitment: The 6 Questions to Ask Your Vendor | Lumo360",
    "description": "The ICO's six questions for buying an AI recruitment tool, in plain English, with what a good vendor answer looks like and how Lumo360 answers.",
    "og_title": "The ICO's six questions for AI recruitment tools, answered",
    "crumb": "ICO AI recruitment questions",
    "kicker": "UK compliance guide",
    "h1": "The ICO's six questions for AI recruitment tools, <em>answered in plain English.</em>",
    "sub": ("After auditing AI recruitment tools, the UK Information Commissioner's Office published six "
            "questions organisations should ask before buying one. Here's what each means, what a good "
            "answer looks like, and how Lumo360 answers it."),
    "secondary": ("Go to the questions", "#questions"),
    "related": ["automate-phone-screening", "hirevue-alternative", "ai-screening-for-recruitment-agencies"],
    "sections": [
        section(
            "context", "Background", "Why the ICO is asking",
            prose(
                f"In November 2024 the ICO published the results of audits of AI tools used in sourcing, "
                f"screening and selection. It made almost 300 recommendations to the developers and providers it "
                f"audited{S(1)}, and summarised its expectations in seven recommendations for providers and "
                f"recruiters{S(2)}.",
                f"Some findings were encouraging: many providers monitored their tools for accuracy and bias. "
                f"Others weren't: some tools inferred characteristics such as gender or ethnicity from a "
                f"candidate's name, and some collected more personal information than they needed{S(1)}.",
                f"Alongside the report, the ICO set out six questions to ask before procuring an AI recruitment "
                f"tool{S(3)}. They're a good checklist for any vendor conversation, including one with us.",
            ),
            cls="bg-white"),
        section(
            "questions", "The six questions", "What to ask, and what a good answer looks like",
            qa([
                ("Question 1", "Have you completed a DPIA?", [
                    "A data protection impact assessment identifies the risks of a new kind of processing and how "
                    "you'll reduce them. The ICO expects it early, before processing starts, and updated as the "
                    "tool or your use of it changes.",
                    "<strong>A good vendor answer:</strong> the vendor gives you the information you need to "
                    "complete your DPIA: what data it processes, where, for how long, and what safeguards apply.",
                ], "[TO CONFIRM: what DPIA support Lumo360 provides, e.g. a DPIA information pack or template.]"),
                ("Question 2", "What is your lawful basis for processing personal information?", [
                    "You need a lawful basis under UK GDPR for using candidates' information, and an extra "
                    "condition if any special category data is involved. Both should be documented and appear in "
                    "your privacy notice.",
                    "<strong>A good vendor answer:</strong> the vendor is clear about what data the tool needs, "
                    "and whether it processes or infers any special category data, so you can choose and document "
                    "your basis.",
                ], "Lumo360 assesses candidates against job-related competencies from your job description. "
                   "[TO CONFIRM: that Lumo360 does not collect or infer special category data, such as ethnicity "
                   "or health, from interviews.]"),
                ("Question 3", "Have you documented responsibilities and set clear processing instructions?", [
                    "You need to know who is the controller and who is the processor for each part of the "
                    "processing, with a contract that says so, and written instructions the provider follows.",
                    "<strong>A good vendor answer:</strong> a data processing agreement that sets out roles, "
                    "instructions, sub-processors and what happens to data at the end of the contract.",
                ], "[TO CONFIRM: Lumo360's role (processor, acting on your instructions) and that a data "
                   "processing agreement is available.]"),
                ("Question 4", "Have you checked the provider has mitigated bias?", [
                    "AI can repeat or amplify bias. The ICO expects providers and recruiters to monitor for "
                    "fairness, accuracy and bias, and to act on what they find.",
                    "<strong>A good vendor answer:</strong> a clear explanation of how candidates are assessed, "
                    "what the tool does and doesn't consider, and how bias is tested and monitored over time.",
                ], "Every candidate for a role is assessed against the same structured competency framework and "
                   "rubric, every score links to the evidence in the transcript, and a recruiter reviews every "
                   "result before anyone moves forward. [TO CONFIRM: how Lumo360 tests and monitors scoring for "
                   "bias.]"),
                ("Question 5", "Is the AI tool being used transparently?", [
                    "Candidates should be told that AI is used, how it's used and how it affects them, and how to "
                    "challenge a decision. The ICO points to its guidance on explaining decisions made with AI.",
                    "<strong>A good vendor answer:</strong> you can see and explain how any individual result was "
                    "reached, in terms a candidate would understand.",
                ], "This is what Lumo360 is built around. The full transcript is kept, the reason for each "
                   "question is visible, and every score links to the moments in the conversation that support "
                   "it, so you can explain any result to a candidate."),
                ("Question 6", "How will you limit unnecessary processing?", [
                    "Collect only what you need for the purpose, don't reuse it for something else, and don't keep "
                    "it longer than necessary.",
                    "<strong>A good vendor answer:</strong> a short, specific list of the data collected, a "
                    "retention period you can configure, and a commitment not to use your candidates' data for "
                    "unrelated purposes.",
                ], "[TO CONFIRM: what data Lumo360 collects, default retention period, whether you can change it, "
                   "and whether candidate data is used to train models.]"),
            ]),
            sub="The ICO's questions are quoted as published. The explanations are ours; they aren't legal advice."),
        section(
            "human", "Human oversight", "Why a person should make the call",
            prose(
                "The ICO's recommendations come back repeatedly to fairness and explanation. The simplest "
                "safeguard is also the most effective: AI runs and scores the first round, and a person reviews "
                "the evidence and decides.",
                "In Lumo360, nobody moves forward or is rejected without a recruiter reviewing their result.",
            )),
        HOW_IT_WORKS,
    ],
    "faqs": [
        ("Is it legal to use AI in recruitment in the UK?",
         "Yes, but data protection law applies. The ICO expects organisations to process candidates' information "
         "lawfully, fairly and transparently, to complete a DPIA, and to check that the tool's provider has "
         "mitigated bias. This page summarises the ICO's guidance and isn't legal advice."),
        ("What did the ICO find in its audit of AI recruitment tools?",
         "Some providers monitored accuracy and bias well. Others inferred characteristics such as gender or "
         "ethnicity from candidates' names, or collected more personal information than they needed. The ICO made "
         "almost 300 recommendations to the providers it audited."),
        ("Do I need a DPIA for an AI recruitment tool?",
         "The ICO expects a DPIA to be completed before processing starts, and updated as the tool or the "
         "processing changes."),
        ("What questions should I ask an AI recruitment vendor?",
         "The ICO's six: have you completed a DPIA; what is your lawful basis; have you documented "
         "responsibilities and set clear instructions; has the provider mitigated bias; is the tool used "
         "transparently; and how will you limit unnecessary processing."),
        ("How does Lumo360 support transparency?",
         "Every score links to the transcript moments that support it, the reason for each question is visible, "
         "and a recruiter reviews every result, so any outcome can be explained to the candidate."),
    ],
    "sources": [
        '<a href="https://techmonitor.ai/?p=411592" rel="noopener">Tech Monitor, "ICO publishes 296 recommendations for AI recruitment software providers"</a>, November 2024.',
        '<a href="https://www.aoshearman.com/en/insights/ao-shearman-on-data/uk-ico-makes-recommendations-on-ai-in-recruitment" rel="noopener">A&amp;O Shearman, "UK ICO makes recommendations on AI in recruitment"</a>, November 2024.',
        '<a href="https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2024/11/thinking-of-using-ai-to-assist-recruitment-our-key-data-protection-considerations/" rel="noopener">ICO, "Thinking of using AI to assist recruitment? Our key data protection considerations"</a>, November 2024. See also the ICO\'s <a href="https://ico.org.uk/action-weve-taken/audits-and-overview-reports/ai-tools-in-recruitment/" rel="noopener">AI tools in recruitment audit outcomes report</a>.',
    ],
}
