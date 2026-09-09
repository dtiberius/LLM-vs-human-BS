# Condition B source packs

One folder per corpus piece. Each has a `sources_NN.md` index (citation, URL, what was retrieved and at what fidelity) and, where the piece's own analysis is the evidence, a `data_appendix_NN.txt` restating its numbers with the interpretation stripped out.

## Fidelity labels

| Label | Meaning |
|---|---|
| **[V]** | Full text retrieved verbatim (the IFOW case studies; the two papers' Methods/Results sections) |
| **[Q]** | Sentences quoted directly from the source by the fetch tool — abstracts and numbered findings |
| **[X]** | Extract produced by the fetch tool; numbers preserved, wording not guaranteed |
| **[R]** | Reconstructed from the corpus piece itself (used only for 05) |
| **[D]** | Dataset — no prose; link given, download by hand |
| **[M]** | Paywalled or blocked to automated fetch — link given, download by hand |
| **[C]** | Citation only (background literature the piece names but does not draw numbers from) |

Everything was retrieved through the cloud fetch tool, which passes pages through a summarising model. Where it was asked to quote and did, the text is marked [Q]; where it visibly paraphrased, [X]. Before publishing any quotation from a [Q]/[X] file, check it against the linked original.

## Viability verdict per piece

| # | Piece | Condition B input | Verdict |
|---|---|---|---|
| 01 | Bank Underground, Schlicht | 8 literature sources (5 [Q], 2 [X], 1 [M]) + data appendix from chart notes | Viable. Friebel et al. needs a manual download. |
| 02 | Bank Underground, Batten | 7 literature sources (4 [Q], 1 [X], 2 [M]) + data appendix | Viable. Bresnahan & Trajtenberg and Crafts are paywalled (abstract-level only). |
| 03 | EPI, Gould & Fast | 8 sources incl. the two earlier posts in the series (all [Q]/[X]) + data appendix (figure tables) | Viable, strong. |
| 04 | **ONS, AI in UK businesses (replacement)** | 12 figure CSVs [D] or data appendix; 4 external sources [Q] | Viable, strong. Replaces St. Louis Fed post (retired). |
| 05 | CIPD, Crowley | Survey figures reconstructed [R] + sibling article [Q] + Labour Market Outlook [Q] + IFOW case studies | Viable but thin — Condition B overlaps Condition C. Report with caveat or swap. |
| 06 | IFOW | All eight case studies verbatim [V] + report page + literature citations [C] | Viable, strongest in the set. |
| 07 | Frontiers, Zhu et al. | Paper's own Methods + Results verbatim [V] + references | Viable, cleanest design. |
| 08 | PLOS ONE, Zhang et al. | Paper's own Methods + Results verbatim [V] + references | Viable; check contamination (Jan 2026). |

## Manual downloads still needed (four links)
- Friebel et al. (2026) PDF — https://soumitrashukla.github.io/Pyramids_Diamonds_Oscillations_NBERORG_2026.pdf
- Crafts (2021) via Sussex repository — https://sussex.figshare.com/articles/journal_contribution/Artificial_Intelligence_as_a_general-purpose_technology_an_historical_perspective/23482037
- Bresnahan & Trajtenberg (1992 NBER WP 4148, open precursor) — https://www.nber.org/papers/w4148
- ONS figure CSVs for piece 04 — links in `04_ons/sources_04.md`

## Design note
For pieces whose contribution is the author's own analysis (01, 02, 03, 04), Condition B gives the model the cited literature plus the piece's numbers stripped of interpretation. This tests whether the model, given the same evidence, commits to the same kind of claims — which is the H1/H3 question — rather than whether it can reproduce an ONS Secure Research Service regression, which it cannot. Say this explicitly in the write-up.
