# Independent review: fifteen actual marked T15 rank certificates

Verdict: **PASS for the fifteen stated marked Q5 theorems and their exact application to the accepted 4,096-record domain.** Review independence is `same-family`; semantic acceptance is `provisional`. The explicit user route, relayed by the parent, specifies GPT-6.1-sol with high reasoning and overrides the skill's default model. Reviewer: `/root/t15_rank_batch_review`. ARIS proof-checker was read at `F:\c4free-hypercube-main\ARIS\skills\skills-codex\proof-checker\SKILL.md`.

This review does not prove full T15, full ten-hole Q6, a T17 theorem, or P6. Producer files and main state were not edited. The optional T63 union below is a separate exact set calculation using a prior accepted review, not another local theorem proved in this audit.

## Frozen scope and proof obligations

The declared input is `Q5_T15_RANK_BATCH_PROOF.md`, the frozen manifest, every manifest entry, and the accepted dependency reviews identified in the JSON. All manifest SHA256 values and file sizes were independently checked. The fifteen Markdown registry rows were parsed and compared to the certificate configurations, the summary geometry and examined counts. The registry has minority 0, five odd majority holes and two distinct marked majority omissions. The relevant cube action transports minority, majority, omissions and matching together, allowing parity reversal.

| Obligation | Discharge |
|---|---|
| Exact local geometry and support | All fifteen configurations checked; pairwise marked orbits are distinct under the full cube action. |
| Every selected forest is legal | Independently checked all 61,440 forests: 17 distinct short edges, omissions unused, degree 1 at the 26 complement vertices, degree 2 at the four included holes, no cycle, and exact endpoint pairing. |
| Every matching column is legal | Independently checked all 61,440 columns: exactly one occurrence of each of the 26 complement vertices, paired consecutively; no parity restriction. |
| Every matrix entry is correct | Recomputed all 251,658,240 bits using connectivity after contracting the 13 forest endpoint pairs; compared every byte, including low-bit-first convention. |
| Rank is 4,096 over GF(2) | Independent forward Gaussian elimination of every recomputed matrix gives 4,096 for each of fifteen matrices. Producer pivots/combos are hashed but are not used as rank evidence. |
| Generic rank upper bound is applicable | Primary theorem explicitly applies to all complete-graph perfect matchings and all even endpoint counts; t=26 yields 2^12=4,096. |
| Universal matching conclusion | Full-rank selected restrictions give independent complete rows; the imported upper bound makes them a basis. Every complete matching column is nonzero, so some selected forest connects. |
| Expand to a simple 30-cycle | Disjoint path interiors, exact degree conditions and connected alternating endpoint cycle give one simple cycle; a common matching/forest edge would create an isolated labelled two-cycle and is therefore impossible. |
| Actual Q6 hypothesis discharge | All six cuts and legal two-source choices replayed independently for rows (3,2)/(1,4), using accepted uniform transfer and balanced-four-hole A endpoint input. |
| Exact domain and subtraction | Accepted T26 reviewer bytes/hashes verified, every producer witness checked, complete orbit coverage compared, and residual bytes and sets checked exactly. |

## Primary source alignment and local reasoning

The [primary author manuscript](https://pure.tue.nl/ws/portalfiles/portal/99596886/1211.1506.pdf) was opened directly during this review. Its abstract defines H_t on all perfect matchings of K_t; Theorem 3.4 and Corollary 3.5 on printed page 9 state the GF(2) factorization and rank 2^(t/2-1) for every even t >= 2. This directly discharges the t=26 upper bound; bipartite matching restrictions are absent. The A10 source note's emphasized t=22 use describes its earlier application, not a restriction on the generic corollary. No finite rank extrapolation is used.

For each selected S, the checked degrees and acyclicity give 30 vertices and 17 edges, hence 13 path components, all with their two endpoints in K. Their pairings are rows of this exact H_26. An invertible 4,096-column restriction implies that the 4,096 full rows are independent. The primary upper bound then implies that they span the full row space. For arbitrary F with edges (a_i,b_i), the pairing of b_i with a_(i+1), indices modulo 13, is a legal matching giving a single alternating cycle, so the F column is nonzero. If every selected row vanished there, every row would vanish there, a contradiction. Expand a connecting selected pairing along S to obtain the required cycle on Q5 minus the two marked omissions, containing F. All added edges belong to S and are short.

Counterexample candidates examined: shared F/S edge (excluded by connectedness on 26 endpoints); a hidden all-hole cycle (excluded by DSU acyclicity); an interior endpoint or missing covered vertex (excluded by degrees); same-parity/long F edges (allowed in K_26 and untouched by the proof); an unlisted marked geometry or independently moved omission pair (excluded by exact common automorphism lookup); and a deficient finite search extrapolated to universality (not used; each certified rank reaches the imported upper bound). None yields an unresolved proof gap.

## Independent certificate implementation

`Q5_T15_RANK_BATCH_REVIEW_check.cpp` explicitly instantiates the already reviewed independent T63/T26 certificate checker, after inspection of its logic, with forest bytes 34 and omission count 2. Endpoint count 26, 13 components, 4,096 rows, 512 matrix bytes and 64 GF(2) words remain appropriate. It does not import producer code. Its forest DSU checks cycle-freedom; its matrix DSU contracts endpoint pairs and tests connectivity; its rank implementation performs fresh elimination and never reads producer combos or pivots. It was compiled with `D:\mingw64\bin\g++.exe -O3 -std=c++17` and run successfully on every frozen prefix. The per-prefix results are saved in `Q5_T15_RANK_BATCH_REVIEW_certificates.log`.

`Q5_T15_RANK_BATCH_REVIEW_check.py` is a separate reviewer application implementation, run with `D:\anaconda\python.exe`. No producer profile/coverage function is imported or executed. It builds a 39,360-element lookup of actual marked geometries from each reviewed registry representative under all coordinate permutations and translations. Repeated symmetries are permitted within a single orbit, but overlap between distinct registry indices is rejected.

## Actual application and exact remainder

The domain is precisely `Q5_T26_RANK_BATCH_REVIEW_remaining_v{1,7,31}.bin`, with hash equality to its accepted review evidence and byte equality to the producer's domain checked. Each nine-byte record has four distinct nonzero even Z vertices and five distinct odd W vertices, with Z-W independence and covered odd target v. The reviewer enumerates all six cuts containing v, counts actual (a,b), and enumerates every two-source subset for the two stated rows. Row (3,2) consumes two even Z sources; row (1,4) consumes two odd W sources and excludes the mirror of root 0. Each actual mirror pair is distinct, internally covered for every realizing matching, and excludes root and original holes. Sources are free and hence cannot be crossing ports. Projection deletes the actual outer coordinate, and a single common cube automorphism matches all three marked sets to a reviewed certificate.

For c>0 the previously accepted uniform transfer discharges the simultaneous tag/conflict suppression and expansion. Both branches leave balanced four holes for the A endpoint theorem; the B compressed matching may have long or equal-parity edges, which the local theorem permits. For c=0 the previously accepted five-direction endpoint import applies. Neither branch assumes a fixed crossing matching realization or imports a higher-hole predecessor theorem. The application remains relative to the exact imports already accepted in `HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json`.

All **8,160** profile witnesses were checked against independently regenerated actual cuts, source pairs and marked projections. For every input record the complete set of attainable registry indices agrees with the producer profile. All **2,346** selected coverage witnesses were also checked. Independent witnesses, including a common permutation and translation, are saved separately. No bare producer count is treated as evidence.

| Target | Accepted input | T15 covered | T15 remaining |
|---:|---:|---:|---:|
| 1 | 910 | 480 | 430 |
| 7 | 1,476 | 846 | 630 |
| 31 | 1,710 | 1,020 | 690 |
| Total | 4,096 | **2,346** | **1,750** |

Reviewer residual files use prefix `Q5_T15_RANK_BATCH_REVIEW_remaining_`. They agree with producer residuals in full byte order and exact set difference, not only cardinality. All 462 records without a (3,1)/(0,4) cut are covered; every remaining record has such a cut. Having such a cut does not establish a T17 theorem.

Old-core alignment was independently recomputed from coordinate permutations of marked omitted/included sets against the original 54-core registry. The non-null mappings are exactly orbit 10 -> core 11, orbit 12 -> core 26, orbit 13 -> core 34 and orbit 14 -> core 51. For all other eleven orbits the historical same-face predicate is true, matching the producer alignment. This explains their absence from that diagnostic registry; it does not supply a proof. All eleven were instead checked with their own new full-rank certificates. In particular orbit 0 covers all 462 no-T17 records and was not silently imported as an old accepted core.

## Separate optional exact T15/T63 union

The existing `Q5_T63_RANK_REVIEW.json` has PASS; all its declared input hashes and evidence hashes were rechecked before using its residual sets. Its seven local rank theorems and 1,743-record application are prior accepted dependencies, not re-proved here. The independent current T15 residual set was intersected with each exact accepted T63 residual set, preserving accepted source record order. No T17 package or unreviewed source enters this operation.

| Target | T15 covered | T63 covered | Union covered | Union remaining |
|---:|---:|---:|---:|---:|
| 1 | 480 | 330 | 630 | 280 |
| 7 | 846 | 693 | 1,197 | 279 |
| 31 | 1,020 | 720 | 1,380 | 330 |
| Total | 2,346 | 1,743 | **3,207** | **889** |

The overlap is 882; T63 removes 861 additional records from the newly reviewed T15 remainder. Exact union residual files use prefix `Q5_T15_T63_RANK_UNION_REVIEW_remaining_`, with hashes in the JSON/check evidence. This union calculation is PASS relative to the accepted T63 review. The 889 remaining records are OPEN, not counterexamples.

## Acceptance boundary and dependency graph

Primary generic rank theorem + independently checked finite local certificates -> fifteen local universal matching theorems. Accepted T26 exact residual domain + those local theorems + accepted uniform transfer and lower local endpoint imports -> exact T15 coverage. Optional accepted T63 exact residuals + T15 residuals -> exact union. There is no cycle back from a claimed ten-hole result into a local certificate. No new fatal, critical or major issue remains within this scope. Full T15, full T63, T17, full ten-hole Q6 and P6 remain OPEN. No producer, ledger, or main state mutation was performed.
