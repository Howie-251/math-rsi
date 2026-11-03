# Comparison and evidence notes

The case presents a frozen research catalogue of **153 named graph instances in 43 parameter pairs**, with **47 completed concrete-graph Lean instances**. The catalogue includes 103 intermediate prefixes of three D5 extension sequences. Counts describe graphs, parameters and proof records separately.

The main-table entries and the competing degree-13 author package were rechecked online on **2026-11-03**. The D3 comparison calculations retain their original **2026-11-01** audit date. Preparing this case study did not rerun the research or conduct a new exhaustive literature search.

## Main-table improvements

| Maximum degree, diameter | Comellas entry | Our graph | Gain |
| --- | ---: | ---: | ---: |
| (11,5) | 37,628 | 37,631 | +3 |
| (12,5) | 42,342 | 42,402 | +60 |
| (16,4) | 16,384 | 16,416 | +32 |

These are direct comparisons with the [Comellas Degree–Diameter table](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html), not proofs of optimality. The table lists degrees through 16; it supplies no degree-20–26 entries.

Our (13,5) graph has 51,457 vertices, exceeding the table's 51,417 by 40. However, [Ryosuke Mizuno's public construction](https://github.com/rmizuno42/ddp/blob/main/results/degree13-diameter5/README.md) has **88,452** vertices and was added to the author's repository on 2026-10-13. We therefore retain our degree-13 sequence in the catalogue but exclude it from the headline competitive improvements.

## D3: what each comparison number means

“Audited benchmark” means a concrete public construction or a valid instantiation/combination of published methods whose applicability was checked in the research. It does not mean that a paper printed that number as the world's largest graph.

| Degree | Audited benchmark | Our graph | Gain | Benchmark calculation/source |
| --- | ---: | ---: | ---: | --- |
| 20 | 2,791 | 3,840 | +1,049 | Rajiv's degree-19, 2,783-vertex source plus Delorme's cloning guarantee: 2,783 + ceil(2,783 / (19²+1)). |
| 21 | 2,928 | 3,984 | +1,056 | PolarStar: ER₁₃ with a degree-7 IQ supernode, 183 × 16. |
| 22 | 3,294 | 4,192 | +898 | PolarStar: ER₁₃ with a degree-8 IQ supernode, 183 × 18. |
| 23 | 3,549 | 4,336 | +787 | PolarStar: ER₁₆ with a Paley-13 supernode, 273 × 13. |
| 24 | 6,144 | 6,160 | +16 | Public opposite generalized-quadrangle construction for parameters (3,5). |
| 25 | 7,225 | 7,242 | +17 | Public opposite generalized-quadrangle construction for parameters (4,4). |
| 26 | 7,514 | 7,532 | +18 | The 7,225-vertex source plus 289 valid clones; comparison includes this public extension. |

Primary references:

- [Rishabh Rajiv's September 2026 report and data](https://doi.org/10.5281/zenodo.23052995).
- [Lakhotia et al., PolarStar, SPAA 2024, author PDF](https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf): supernode conditions and graph construction.
- [Charles Delorme, Grands Graphes de Degré et Diamètre Donnés, 1985](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf): public product and replication methods.
- [Isham et al., 2026, §3.4.2](https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2): explicit opposite-GQ formulas. The related [Delorme JGT 1985 paper](https://doi.org/10.1002/jgt.3190090304) is credited, but its full text was not obtained in this audit.

The user's earlier 3,250-vertex lead for degree 20 remains unresolved because its source and precise parameters have not been bound. If confirmed for (20,3), our 3,840 vertices would exceed it by **590**, and 2,791 would no longer be the strongest located comparison for that parameter. The high-degree global table also could not be retrieved during the recorded audit. These are the concrete reasons for using “exceeds the audited public constructions/method guarantees,” rather than a universal SOTA claim.

## Higher-degree examples

| Degree (D=3) | Audited benchmark | Our graph | Gain |
| --- | ---: | ---: | ---: |
| 54 | 55,512 | 56,862 | +1,350 |
| 64 | 160,000 | 160,050 | +50 |
| 80 | 327,680 | 327,744 | +64 |
| 98 | 414,050 | 414,132 | +82 |

For degrees 54–59, the benchmark is **52,428 + (Δ−51) × 1,028**, obtained by applying public Delorme methods with a verified 12-vertex controller. This is a project calculation from published methods, not six numerical records quoted from a paper.

For degrees 65–79, the comparison includes the public 33-point partial ovoid in W(7): **160,000 + (Δ−64) × 1,650**. The 33 is a constructed object's size, not the larger upper-bound column in the [Cimráková–Fack paper](https://combinatorialpress.com/article/jcmcc/Volume%20063/vol-063-paper%2012.pdf#page=12).

For the displayed higher q=8 degrees, the comparator is **4,225Δ**, using the [published polarity-product construction and replication](https://arxiv.org/html/2608.27253v2#S7.SS7). The exact public priority of the additional spread-fill and connection-reallocation rules is still open. If the 342,290-vertex filled source and ordinary replication are already public, the degree-98 residual gain falls from 82 to 17; if the same reallocation is already public, its novelty must also be revised. This does not change the graph's validity.

Across the strongest graph at each of the 43 parameters, **3** exceed the listed main-table entries and **37 D3 parameters** exceed their specified audited public-method benchmarks. The other parameters are degree 13 / D5 and degree 35 / D3 (known larger public constructions), and degree 17 / D3 (public-best comparison unresolved). The [43-row comparison CSV](../data/public_comparisons.csv) preserves all of these statuses.

## Validity and reproducibility

The [153-row catalogue](../data/catalog.csv) reports each graph's verification status. All seven degree-20–26 representatives have completed concrete-graph Lean records. This is not a claim that every one of the 153 graphs has Lean, or that a fresh Lean build was run for this case study.

The other 106 cases are covered by their recorded computational/mathematical arguments. In the D5 sequences, each new neighborhood has spare degree and its radius-four balls cover the **current entire graph**, including previously added vertices. Old edges remain. Induction therefore covers all pairs, with the original source's D5 bound as the starting premise. Selected all-root BFS checkpoints and the replay of all 103 additions are in the [source-package verification guide](../reproduce/README.md).

Representative preserved records:

- [(11,5), 37,631: accepted extension sequence](records/d11_D5_n37631_accepted_sequence.json).
- [(12,5), 42,402: accepted extension sequence](records/d12_D5_n42402_accepted_sequence.json).
- [(16,4), 16,416: concrete Lean disposition](records/d16_D4_n16416_ROOT_FULL_LEAN_DISPOSITION.json).
- [(20,3), 3,840: independent all-root check](records/d20_D3_n3840_SUMMARY.json).
- [(21,3), 3,984](records/d21_D3_n3984_SUMMARY.json) and [(22,3), 4,192](records/d22_D3_n4192_SUMMARY.json): independent acceptance.
- [(23,3), 4,336](records/d23_D3_n4336_RESULT.json), [(24,3), 6,160](records/d24_D3_n6160_RESULT.json), [(25,3), 7,242](records/d25_D3_n7242_ROOT_GRAPH_RELEASE.json), and [(26,3), 7,532](records/d26_D3_n7532_ROOT_GRAPH_RELEASE.json): preserved result/release records.
- [(54,3), 56,862: independent acceptance](records/d54_D3_n56862_SUMMARY.json).
- [(98,3), 414,132: release and formalization status](records/d98_D3_n414132_ROOT_GRAPH_RELEASE.json).

The records are historical snapshots, so paths inside them and the original catalogue retain their research-workspace meaning. This compact case includes construction programs and small inputs for **all 153 graphs**, selected verification records, and the chart data. The complete Lean project, all literature readouts and research trajectories remain in the separately delivered full research handoff. Use [reproduce_index.csv](../reproduce/reproduce_index.csv) for portable reconstruction commands from the `reproduce/` directory.

## Attribution and what this case demonstrates

The D5 sources retain credit to Dharunish Yugeswardeenoo and the underlying H(9) work of Rishabh Rajiv. The affine route-chart/controller framework retains credit to Ryosuke Mizuno; the C60 and Schreier controllers retain their Bhakar/f4t4nt source attribution. Generalized quadrangles, spreads, ovoids, opposite products and generic cloning are established tools. The project's deliverables are its explicit compatible choices, neighborhood additions, resulting graph instances, proofs and verification records.

The research preceded this MathRSI integration. This case supplies concrete domain experience for future reuse; it is not a controlled measurement of MathRSI v1, v2, a speedup factor or recursive self-improvement.
