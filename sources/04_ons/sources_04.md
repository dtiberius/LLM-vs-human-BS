# Condition B source pack — 04 (REPLACEMENT) ONS Macroeconomic Insights team, "Artificial intelligence in UK businesses: 2023 to 2026" (20 Jul 2026)

Replaces the St. Louis Fed Eighth District survey post (retired to `corpus/retired/`). Reason: that post's only substantive source was its own unpublished survey, so Condition B would have collapsed into Condition C. The ONS article is built on public BICS data (per-figure CSV downloads), cites five retrievable external works, and is a UK official-statistics analysis your audience recognises. Corpus text: `corpus/04_ons_ai_in_uk_businesses_2023_2026.txt` (sections 1–5, ~3,000 words; consider trimming to sections 1, 3 and 4 for length parity).

Fidelity key: **[Q]** quoted by the fetch tool; **[X]** extract; **[D]** dataset — download by hand (the ONS generator endpoint refuses automated fetches).

Recommended Condition B input: the twelve figure CSVs (S1) **or**, if you don't want to download them, `data_appendix_04.txt` (every number in the article, interpretation removed), plus S2–S6.

---

## S1. ONS Business Insights and Conditions Survey, Wave 159 (5–28 Jun 2026) and Opinions and Lifestyle Survey (6 May–28 Jun 2026) — per-figure data [D]
Dataset release (2 Jul 2026): https://www.ons.gov.uk/economy/economicoutputandproductivity/output/datasets/businessinsightsandimpactontheukeconomy
Figure CSVs (append `&format=xls` for Excel):
- Fig 1 AI use over time: https://www.ons.gov.uk/generator?uri=/businessindustryandtrade/business/businessservices/articles/artificialintelligenceinukbusinesses/2023to2026/808491a0&format=csv
- Fig 2 technologies per business: .../2023to2026/7296b513&format=csv
- Fig 3 by industry: .../2023to2026/5376501d&format=csv
- Fig 4 business vs employee use: .../2023to2026/b6b793e1&format=csv
- Fig 5 purpose by size band: .../2023to2026/069669a5&format=csv
- Fig 6 adoption method by industry: .../2023to2026/1783dc4d&format=csv
- Fig 7 headcount impact by size band: .../2023to2026/5796c494&format=csv
- Fig 8 headcount impact by purpose: .../2023to2026/4ea0c381&format=csv
- Fig 9 roles affected by AI type: .../2023to2026/fc8b4fc2&format=csv
- Fig 10 barriers by size band (interactive): https://www.ons.gov.uk/visualisations/dvc3591/fig10/index.html
- Fig 11 skills approach by barrier status: .../2023to2026/a96989e6&format=csv
- Fig 12 skills approach by size band: .../2023to2026/3ca5c8d8&format=csv
(Replace `...` with `https://www.ons.gov.uk/generator?uri=/businessindustryandtrade/business/businessservices/articles/artificialintelligenceinukbusinesses`.)

## S2. Bick, Blandin, Deming, Fuchs-Schündeln & Jessen (2026) — "Mind the Gap: AI Adoption in Europe and the U.S.", NBER WP 34995 (Mar 2026) [Q]
URL: https://www.nber.org/papers/w34995 · St. Louis Fed summary (30 Mar 2026): https://www.stlouisfed.org/on-the-economy/2026/mar/mind-gap-ai-adoption-europe-us · IZA DP 18521: https://docs.iza.org/dp18521.pdf
Abstract: "This paper combines international evidence from worker and firm surveys conducted in 2025 and 2026 to document large gaps in AI adoption, both between the US and Europe and across European countries. Cross-country differences in worker demographics and firm composition account for an important share of these gaps. AI adoption, within and across countries, is also closely linked to firm personnel management practices and whether firms actively encourage AI use by workers. Micro-level evidence suggests that AI generates meaningful time savings for many workers. At the macro level, in recent years industries with higher AI adoption rates have experienced faster productivity growth. While we do not establish causality, this relationship is statistically significant and similar in magnitude in Europe and the US. We do not find clear evidence that industry-level AI adoption is associated with employment changes. We discuss limitations of existing data and outline priorities for future data collection to better assess the productivity and labor market effects of AI."
Summary-post numbers [Q]: "43.0% of U.S. workers reported using AI for their jobs in January-February 2026"; "36.3% in the U.K."; "25.6% in Italy"; "32% across the European countries we surveyed"; "5.2% of all U.S. work hours in early 2026 were spent using AI"; EU firms "the share of firms using at least one AI technology averaged 20%"; "U.S. adoption was between 18% and 68% higher than in any of these individual European countries."

## S3. Yotzov, Barrero, Bloom, Bunn, Davis et al. (2026) — "Firm Data on AI", NBER WP 34836 (Feb 2026) [Q]
URL: https://www.nber.org/papers/w34836 · PDF: https://www.nber.org/system/files/working_papers/w34836/w34836.pdf
Abstract: "We survey nearly 6,000 senior business executives at US, UK, German, and Australian firms to develop new evidence on AI adoption and its effects on jobs, productivity, and output. Specifically, we ask executives about AI usage, its effects at their own firms over the past three years and, looking ahead, what they anticipate over the next three years. We find four main results. First, 69% of firms actively use AI, with higher usage rates at younger and more productive firms. Second, more than two thirds of executives regularly use AI, but their usage rate averages only 1.5 hours a week. Third, executives report little own-firm impact of AI over the last 3 years, with nine-in-ten reporting no impact on employment or productivity. Fourth, these same executives predict sizable effects over the next 3 years, predicting that AI will boost productivity at their firms by an average of 1.4%, raise output 0.8%, and cut employment 0.7%. In contrast, employees anticipate that AI will raise employment 0.5% at their firms in the next 3 years, highlighting an expectations gap between employers and employees."
(The ONS article quotes the country breakdown: ~78% of US firms and ~71% of UK firms using at least one AI technology.)

## S4. DSIT (updated 13 Feb 2026) — "AI Adoption Research" (3,500 business interviews, 12 Feb–2 May 2025; 100 qualitative interviews Mar–May 2025) [Q]
URL: https://www.gov.uk/government/publications/ai-adoption-research/ai-adoption-research
"1 in 6 businesses currently use AI, but most businesses currently have no active plans to adopt AI."; "Natural language processing and text generation are the most common uses, with 85% of AI adopters currently using AI for these purposes."; "Among AI adopters, 30% of staff currently use AI, on average."; "Just over half of organisations already using AI feel ready to further scale up their use, only a third of those planning to use AI feel ready to implement it."; "Lack of identified need and limited AI skills are the most commonly cited barriers to AI adoption, but ethical concerns are deemed more significant."; "Most businesses using AI report an increase in workforce productivity."; "Most business have not yet experienced a change in revenue." Adoption: using 16%, planning 5%, neither 80%; staff expected to use AI in 1–2 years: 43%.

## S5. ONS (24 Mar 2025) — "Management practices and the adoption of technology and artificial intelligence in UK firms: 2023" [Q]
URL: https://www.ons.gov.uk/economy/economicoutputandproductivity/productivitymeasures/articles/managementpracticesandtheadoptionoftechnologyandartificialintelligenceinukfirms2023/2025-03-24
"In 2023, artificial intelligence (AI) was adopted by 9% of firms while cloud-based computing systems and applications were adopted by 69% of firms in the UK."; "While 88% of firms in the top decile of management practice scores adopted at least one of AI, cloud-based computing systems and applications, robotics, specialised software or specialised equipment, only 51% of firms in the bottom decile did so."; "The most common barriers to AI adoption reported by firms in 2023 were difficulty identifying activities or business use cases (39%), cost (21%) and level of AI expertise and skills (16%)."; "Technology adopters were associated with 19% higher turnover per worker, after controlling for management practice scores and firm characteristics."; "Firms with higher management practice scores were more likely to follow through in adopting AI in 2024, given that they planned to adopt AI in 2023."

## S6. Department for Business and Trade (4 Jun 2026) — "UK Innovation Survey 2025: report" [C]
URL: https://www.gov.uk/government/statistics/uk-innovation-survey-2025-report/uk-innovation-survey-2025-report
Cited by ONS for "innovative businesses are more likely to use AI"; the fetch of section 9 found no AI sentences, so the supporting figure sits elsewhere in the report — check before relying on it.

## S7. Bank of England Decision Maker Panel, January 2026 [C]
URL: https://www.bankofengland.co.uk/decision-maker-panel/2026/january-2026 (survey 9–23 Jan 2026, 2,064 responses). ONS cites it for "for most firms, the use of AI has had no material impact on the number of employees over the past three years"; the January page text retrieved carried no AI section, so the AI results are probably in the accompanying data/charts — verify by hand.

## S8. US Census Business Trends and Outlook Survey; Eurostat ICT usage in enterprises [C]
Mentioned as comparators only.
