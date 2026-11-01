# Fresh search for the exact five-uniform bound — 2026-10-06

**No original source proving \(m(5)\ge33\), and no non-two-colourable five-uniform hypergraph with at most 32 edges, was located in this search.** The strongest numerical lower bound directly checked remains \(m(5)\ge32\) in Grill–Linzmayer, arXiv:2403.05674v3, Theorem 1 (p.7); their Table 1 (p.6) gives the established upper bound 51. The [current arXiv record](https://arxiv.org/abs/2403.05674) still lists v3, submitted 2024-06-20, with v1 on 2024-03-08 and v2 on 2024-03-20. This is a bounded literature-search conclusion, not proof that nobody has obtained an unindexed result.

ARIS research-lit and novelty-check were read and used for this shard. Root owns final novelty synthesis, independent review, deduplication and wiki ingestion. This shard made no changes to the wiki or proof status. The [JSON report](search_latest_bounds_20261006.json) contains all **44 web queries**, canonical IDs, primary URLs, dates and read depth.

## Newer sources and unresolved access

| Source | Verified content and scope | Consequence |
|---|---|---|
| Grill–Linzmayer, *An Overview of Property B*, Springer, 2026-05-28, pp.173–181, DOI 10.1007/978-3-032-18810-6_9 | Publisher metadata, abstract and bibliography | **Full chapter not acquired**; no inference about its numerical tables |
| Linzmayer–Grill, *Some upper bounds for property B for small values of n by heuristic search* (2024) | Reference 16 of the 2026 chapter; no venue, DOI or accessible manuscript | **Numerical results unverified**; no independent edge list located |
| Grill, *Some Upper Bounds for Property B*, Sum(m)it280, 2024-07-08 | Official abstract, printed p.22 / PDF p.24; joint work with Linzmayer | Heuristic search announced for small uniformity/vertex counts, but abstract gives no numerical bound |
| Linzmayer, *Die probabilistische Methode in der Kombinatorik*, TU Wien thesis (2018) | §10.2.1 pp.74–77 and Appendix A p.80 | Reports \(m(5,11)=m(5,12)=66\), gives two 66-edge lists; no 32-edge witness |
| Akhmejanova–Longbrake, *Fractional hypergraph coloring*, arXiv:2504.12430, **v2 2026-06-07** | Latest PDF pp.1–4, all result statements, bibliography | Does not provide ordinary \(m(5)\ge33\) |
| Gao, *Peeling Hypergraphs: A Structural Sufficient Condition for Property B*, Zenodo (record 2026-07-22; PDF 2026-07-23) | Nine-page manuscript read for scope; no full independent proof audit | Different sufficient condition; no numerical \(m(5)\) claim |

The [Springer chapter](https://link.springer.com/chapter/10.1007/978-3-032-18810-6_9) is a real 2026 publication; its PDF endpoint returned HTML. The heuristic-search citation is evidence of reported work, not of a 32-edge counterexample. The related [official conference abstract](https://conferences.renyi.hu/uploads/Abstract_Booklet_Summit280_%289%29.pdf) also gives no numeric bound. Exact identity of the cited manuscript and conference presentation is not assumed.

The [2018 thesis](https://repositum.tuwien.at/handle/20.500.12708/3487), previously inaccessible locally, was downloaded from the official repository. Chapter 10 describes simulated annealing with bitset representations of partitions. It establishes that researchers have pursued computational counterexample searches. The two 66-edge lists were inspected but not independently executed in this shard.

## Forward citation and recent-paper checks

OpenAlex title search resolved the 2024 lower-bound paper to **W4392736645**. Its forward-citation response returned one work, *Fractional Hypergraph Coloring* (SSRN DOI 10.2139/ssrn.5349457), deduplicated with arXiv:2504.12430. One indexed result does not mean only one citing work exists. SSRN lists 2025-07-12; arXiv v1 is 2025-04-16 and current v2 is 2026-06-07. The downloaded v2 has **13 physical pages**, although the arXiv comments field says ten pages.

In [v2](https://arxiv.org/pdf/2504.12430v2), Theorem 1 requires \(b\ge2\), excluding ordinary two-colouring \((a,b)=(2,1)\). Proposition 1 requires \(a>3\). Theorem 2 is asymptotic and supplies no explicit small-\(n\) witness. Theorem 3 allows \((n,a,b)=(5,2,1)\), but then \(a'=\lfloor2(5-1)/5\rfloor=1\), so its threshold is only \(|E|\le1\). Its displayed results do not give the target 32-edge statement.

The [Gao manuscript](https://zenodo.org/records/21475089) gives a sufficient condition requiring every edge, in a suitable order, to introduce at least one new vertex. A peeling five-uniform hypergraph with 32 edges consequently needs at least \(5+31=36\) nonisolated vertices. This inference directly from Definition 1.1 shows the condition does not itself handle the project's reduced 19–25-vertex classes. It is not accepted here as a replacement proof route.

Other recent primary abstracts checked:

- [Carenini, *The Scaling Window of Random k-SAT*, ECCC TR26-145 / arXiv:2609.26222](https://eccc.weizmann.ac.il/report/2026/145/): random threshold windows, not a finite universal extremal bound.
- [Pálvölgyi, *Note on polychromatic coloring of hereditary hypergraph families II*, arXiv:2604.24412](https://arxiv.org/abs/2604.24412), 2026-04-27: separates polychromatic three-colouring from two-colourability of heavy restrictions; different target.
- [Janzer–Portier, *Nearly tight bounds for MaxCut in hypergraphs*, arXiv:2511.08501](https://arxiv.org/abs/2511.08501), 2025-11-11: asymptotic excess-cut bounds; no exact 32-edge theorem stated in the abstract.

Baumgartner-style forcing papers using “Property B” were excluded as a homonymous subject. Wikipedia and OEIS A392185 still display the older lower bound 29 and are not used to overrule the 2024 primary theorem. Root separately checked the GitHub formal-conjectures issue/PR and public AI research reports.

## Coverage and limits

The 44 web formulations cover exact \(m(5)\) with 32/33, five-uniform and 5-uniform wording, non-two-colourable / non-2-colorable variants, lower/upper bounds, counterexample and erratum terms, exact titles, author names, heuristic-search slides, 2025/2026 and an explicit **2026-04-06 to 2026-10-06** interval. Primary pages include arXiv, TU Wien, Springer, ECCC, Zenodo and official conference records. No matching erratum or disproof of the 2024 lower-bound paper appeared in these searched results.

Both fresh ARIS arXiv helper calls used the configured ARIS_REPO and failed with **HTTP 429** after internal attempts. Their saved JSON files explicitly record failure, not zero matches. Semantic Scholar's citation call also returned 429. OpenAlex's direct arXiv URL resolver returned 404; title resolution and the forward-citation query succeeded. Date-filtered web searches supplied recent-paper coverage. Earlier successful same-day API files are historical evidence of those earlier queries, not relabelled fresh successes.

The outstanding literature gaps are the **2026 chapter full text** and the **2024 heuristic upper-bound manuscript/results**. No exhaustive absence or definitive novelty claim is made.

## New local materials and actual read coverage

| PDF | Pages | Read here |
|---|---:|---|
| [linzmayer_2018_probabilistische_methode.pdf](../ref/linzmayer_2018_probabilistische_methode.pdf) | 93 | Title/abstract/contents; §8 pp.57–59; Chapter 10 pp.71–78; conclusion p.79; Appendix A p.80. Other chapters/C code not fully read |
| [summit280_2024_abstract_booklet.pdf](../ref/summit280_2024_abstract_booklet.pdf) | 64 | Only relevant abstract: printed p.22 / physical p.24 |
| [gao_2026_peeling_hypergraphs.pdf](../ref/gao_2026_peeling_hypergraphs.pdf) | 9 | Full manuscript for claim scope; no independent proof audit |
| [akhmejanova_longbrake_2025_fractional_hypergraph_coloring.pdf](../ref/akhmejanova_longbrake_2025_fractional_hypergraph_coloring.pdf) | 13 | Current v2 pp.1–4 and bibliography; v1 introduction/results read separately via primary HTML |

Each has a unique extracted-text file under context/extracted/. Accepted downloads were checked for the PDF signature; page counts are from local PDFs. Full canonical URLs and retrieval evidence are in the JSON report.

