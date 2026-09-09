# Condition B source pack — 01 Schlicht, "Canaries in the column?" (Bank Underground, 6 Aug 2026)

Fidelity key: **[Q]** = text quoted directly from the source by the fetch tool; **[X]** = extract/paraphrase produced by the fetch tool (numbers preserved, wording not guaranteed); **[D]** = dataset, no prose to attach; **[M]** = manual download needed.

For this piece the author's own analysis (composite exposure score × ONS vacancy data) is not reproducible from public prose. The recommended Condition B input is: the literature below **plus** a data appendix built from the piece's own chart notes (`data_appendix_01.txt`), stripped of interpretation.

---

## S1. Brynjolfsson, Chandar & Chen (2026, Aug update) — "Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence" [X]
URL (PDF): https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf
Summary page: https://digitaleconomy.stanford.edu/news/canariesaug26/
Data: ADP payroll microdata through June 2026.

Abstract [Q]: "Using a sample of high-frequency administrative payroll data from ADP covering millions of U.S. workers through June 2026, we document six facts about the labor market following the widespread adoption of generative AI."

Six facts [X, numbers as in source]:
1. No widespread economy-wide job displacement: overall employment in the ADP sample rose ~6% between Nov 2022 and Jun 2026; the most exposed quintile grew ~4%.
2. Employment of 22–25-year-olds in the two most exposed quintiles fell ~11% between Nov 2022 and Jun 2026, while the same age group in the three least-exposed quintiles grew ~10% (21-point divergence). No comparable gap for experienced workers. Young-worker employment in exposed occupations is "19% below where it would be had it kept pace with that of their less-exposed peers."
3. The entry-level divergence has widened steadily since Aug 2025, reaching ~18 points by mid-2026 in occupation-level estimates.
4. Decline operates through reduced hiring, not increased separations: "no evidence that increased separations explain the divergence."
5. Declines concentrate where AI usage substitutes for human tasks; where AI complements workers "employment is flat or rising, especially for experienced workers." Automation exposure coefficient "−0.10 per standard deviation for 22–25 year-olds."
6. "Adjustment is occurring through employment rather than base compensation."
Context sentence [Q]: "between 2023 and 2024, AI performance on software engineering benchmarks surged from 4.4% to 71.7%."

## S2. Lambert & Schindler (2026) — "The Broken Ladder: AI, Remote Work, and Early-Career Hiring" (CAGE WP 808/2026, 1 Jun 2026) [Q/X]
URL: https://warwick.ac.uk/fac/soc/economics/research/centres/cage/publications/workingpapers/2026/the_broken_ladder_ai_remote_work_and_early_career_hiring/
PDF: https://warwick.ac.uk/fac/soc/economics/research/centres/cage/manage/publications/wp808.2026.pdf
SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6787638

Abstract opening [Q]: "Is generative AI replacing junior workers? A growing literature answers yes, citing large declines in early-career hiring concentrated in GenAI-exposed occupations. We argue that this verdict is premature because GenAI exposure is strongly correlated with another post-pandemic shock, working from home (WFH)."
Data [X]: 243 million new-hire records (résumé data) and 407 million online job postings, US/UK/Canada/Australia, 2017–2025; difference-in-differences.
Findings [Q/X]: In single-treatment models a two-SD increase in either WFH or GenAI exposure predicts a ~4–5 pp fall in junior hiring share and ~3 pp fall in postings requiring ≤3 years' experience by 2025. In joint specifications "the WFH effect remains, while the GenAI coefficient attenuates sharply and is often statistically indistinguishable from zero." "at the 6-digit O*NET-SOC occupation level, the WFH exposure measure of Hansen et al. (2023) and the GenAI exposure index of Eloundou et al. (2024) have a Spearman rank correlation of 0.77." "WFH has been shown to raise the cost of supervising and monitoring workers, and can slow on-the-job learning." Actual WFH adoption (firms/regions posting remote roles in 2021–22) "predicts a fall in the junior-share of new hires and the share of job postings requiring 3 years of experience or less." Authors stress results concern junior-vs-senior hiring through 2025, not aggregate GenAI effects.

## S3. Friebel, Huang, Li, Shukla & Zhang (2026) — "Pyramids, Diamonds, and Oscillations: AI and the Structure of Internal Labor Markets" [M]
SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6570519 (rate-limited on fetch)
PDF: https://soumitrashukla.github.io/Pyramids_Diamonds_Oscillations_NBERORG_2026.pdf (blocked to automated fetch; download manually)
As characterised in the piece: a framework in which the junior-heavy pyramid shifts ("oscillates") toward a diamond centred on experienced staff as AI absorbs routine information-processing tasks.

## S4. Felten, Raj & Seamans (2021) — "Occupational, industry, and geographic exposure to artificial intelligence: A novel dataset and its potential uses", Strategic Management Journal 42(12):2195–2217 [X]
Paper (paywalled): https://sms.onlinelibrary.wiley.com/doi/full/10.1002/smj.3286 · SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3822412
Data (open): https://github.com/AIOE-Data/AIOE — AIOE (occupation, SOC), AIIE (industry, NAICS), AIGE (county) scores; built from an application–ability matrix (crowd-sourced relatedness of 10 AI applications to 52 O*NET abilities) aggregated by occupation.

## S5. Felten, Raj & Seamans (2023) — "How will Language Modelers like ChatGPT Affect Occupations and Industries?" (arXiv 2303.01157) [Q]
URL: https://arxiv.org/abs/2303.01157
Abstract: "Recent dramatic increases in AI language modeling capabilities has led to many questions about the effect of these technologies on the economy. In this paper we present a methodology to systematically assess the extent to which occupations, industries and geographies are exposed to advances in AI language modeling capabilities. We find that the top occupations exposed to language modeling include telemarketers and a variety of post-secondary teachers such as English language and literature, foreign language and literature, and history teachers. We find the top industries exposed to advances in language modeling are legal services and securities, commodities, and investments. We also find a positive correlation between wages and exposure to AI language modeling."

## S6. Henseke, Davies, Felstead, Gallie, Green & Zhou (2026) — "How Exposed Are UK Jobs to Generative AI? Developing and Applying a Novel Task-Based Index" (arXiv 2507.22748) [Q]
URL: https://arxiv.org/abs/2507.22748 · HTML: https://arxiv.org/html/2507.22748v2
Abstract opening: "We draw on Eloundou et al. 2024a to develop the Generative AI Susceptibility Index (GAISI), a task-based measure of UK job exposure to large language models (LLMs), such as ChatGPT."
Headline numbers: "By 2023/24, nearly all UK jobs exhibited some exposure, yet only a minority were heavily affected." "94% of jobs have at least some exposure to generative AI"; "only 13% of jobs have ≥50% of tasks" susceptible; "The mean GAISI is 0.40, with values at the 10th and 90th percentile ranging from 0.23 to 0.51."; "25% of tasks are rated as 'directly susceptible' to LLM assistance (E1)"; "Another 27% were indirectly exposed via integration into software, databases and other tools"; "Professional occupations in ICT and research had the highest exposure score, while manual and routine occupations scored the lowest."

## S7. Eloundou, Manning, Mishkin & Rock (2023) — "GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models" (arXiv 2303.10130) [Q]
URL: https://arxiv.org/abs/2303.10130
Abstract: "We investigate the potential implications of large language models (LLMs), such as Generative Pre-trained Transformers (GPTs), on the U.S. labor market, focusing on the increased capabilities arising from LLM-powered software compared to LLMs on their own. Using a new rubric, we assess occupations based on their alignment with LLM capabilities, integrating both human expertise and GPT-4 classifications. Our findings reveal that around 80% of the U.S. workforce could have at least 10% of their work tasks affected by the introduction of LLMs, while approximately 19% of workers may see at least 50% of their tasks impacted. We do not make predictions about the development or adoption timeline of such LLMs. The projected effects span all wage levels, with higher-income jobs potentially facing greater exposure to LLM capabilities and LLM-powered software. Significantly, these impacts are not restricted to industries with higher recent productivity growth. Our analysis suggests that, with access to an LLM, about 15% of all worker tasks in the US could be completed significantly faster at the same level of quality. When incorporating software and tooling built on top of LLMs, this share increases to between 47 and 56% of all tasks. This finding implies that LLM-powered software will have a substantial effect on scaling the economic impacts of the underlying models. We conclude that LLMs such as GPTs exhibit traits of general-purpose technologies, indicating that they could have considerable economic, social, and policy implications."

## S8. Anthropic Economic Index, March 2026 report ("Learning curves") [Q]
URL: https://www.anthropic.com/research/economic-index-march-2026-report · Index home: https://www.anthropic.com/economic-index
Quoted findings: "the top 10 tasks made up 19% of all traffic in February, down from 24% in November"; "About 49% of jobs have seen at least a quarter of their tasks performed using Claude"; "the top 20 countries account for 48% of all per-capita usage, up from 45%"; "average task value...has dropped slightly from $49.3 to $47.9"; "Opus is used 4 percentage points more than average for coding tasks and 7 percentage points less than average for tutoring-related tasks"; "For every additional $10 of hourly wage for a task, the share of conversations using Opus increases by 1.5 percentage points"; "people who have been using Claude for 6 months or more have 10% fewer personal conversations and a 6% higher education level"; "people in this higher-tenure group have a 10% higher success rate in their conversations"; "states would arrive at roughly equal usage per capita in 5–9 years, rather than 2–5". (Used in the piece as one input to the occupational exposure composite.)

## S9–S12. Datasets [D]
- ONS Online Job Adverts (Textkernel series; the earlier Adzuna series at https://www.ons.gov.uk/economy/economicoutputandproductivity/output/datasets/onlinejobadvertestimates was discontinued Oct 2024).
- ONS VACS02 — vacancies by industry: https://www.ons.gov.uk/employmentandlabourmarket/peoplenotinwork/unemployment/datasets/vacanciesbyindustryvacs02
- ONS Business Insights and Conditions Survey (BICS): https://www.ons.gov.uk/businessindustryandtrade/business/businessservices/bulletins/businessinsightsandimpactontheukeconomy/latest
- Bank of England Decision Maker Panel: https://www.bankofengland.co.uk/decision-maker-panel (blocked to automated fetch)
- ONS Annual Population Survey 2022 SIC–SOC employment weights.
