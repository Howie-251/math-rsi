# R20 exact-identity novelty comparison — 2026-10-23

Status: primary-source comparison by main agent; independent review unavailable. No R20 acceptance, solver result, or campaign binding changed.

## Proposed claim
For complete rank-3 signotopes with the R20 weak-polygon definition,
N_sig(n,n,n) = N_sig(n,n-1,n)+1, n >= 4.
Primary candidate: .trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md, sections 0.1 and 2–4.3.

## Confirmed source findings
1. Schroeder V1, Proposition 2.1 (paper/geometry.tex:16–38), defines Q_n as the maximum planar set avoiding an (n-1)-cap and convex n-gon, and proves ES(n) <= Q_n+2. It explicitly proves |S| <= Q_n+1 after one root deletion. Since Q_n=N_plane(n,n-1,n) and ES(n)-1=N_plane(n,n,n), this IS the upper direction of the identity in the planar category.
2. paper/main.tex:120 explicitly says the +2 consists of one deleted root plus the conversion from avoiding maximum to forcing threshold. The R20 +1 is not a one-point improvement over that +2.
3. The opposite planar inequality has an elementary extension: take Y in the asymmetric class, choose p to the left and sufficiently below every line through two Y points, making every increasing triple containing p a cap. Any convex n-gon containing p would have a cup side of at most two vertices and hence an n-cap, which would leave an (n-1)-cap in Y. Convex n-gons not containing p were already excluded. Thus |Y|+1 is attainable in the unrestricted avoiding class. This deduction is our comparison argument, not a claim that Schroeder explicitly states or credits this converse.
4. Tóth–Valtr 2005, Theorem 5 proof (p. 564), presents the projective deletion and attributes the bound to their 1998 work. Norin–Yuditsky, Erdos–Szekeres without induction, Theorem 3.1, explicitly states the forcing-threshold implication and attributes it to Tóth–Valtr.
5. Rote, NumPSLA, arXiv:2503.02336v1 (4 March 2025), Appendix B, describes the correspondence between x-sorted abstract configurations with an added extreme pivot and arbitrary oriented abstract order types with a marked hull vertex. Appendix C discusses the alternating orientation predicate; section 1.1 names signotopes among the equivalent frameworks. This is concrete prior machinery for the abstract chart/root operation, not an explicit printed statement of the R20 extremal identity.
6. Baek–Balko, SoCG 2025 section 3, identifies rank-3 signotopes with pseudoline-arrangement configurations and notes that weak polygons are strong polygons for signotopes.

## Assessment
- Planar identity as a new theorem: not a defensible novelty claim; it follows from the published reduction plus elementary extension.
- Exact signotope formula literally printed in the inspected papers: not located. This finite search is not an exhaustive absence proof.
- A new result merely because the word signotope or the equality is absent from Schroeder: not established. The abstract marked-pivot correspondence is an explicit, named prior-work issue.
- Potential remaining contribution: a self-contained proof directly from packet axioms, with an explicit valid-chart construction and weak-polygon invariance, plus useful integration into the SAT proof pipeline. Whether this proof is new and substantial enough for a paper remains to be assessed; it is not currently a confirmed first theorem.
- Recommendation: PROCEED WITH CAUTION for a method/expository lemma and its applications; do not claim first discovery of the planar equality or an improvement over the +2 transfer.
- R20's internal improvement 83 -> 84 via this reduction has operational value, conditional on its preceding bounds. Improvement over an older local recurrence is not by itself improvement over external literature.
- R20 source labels its mathematics unreviewed/unaccepted. This run does not conduct a full proof audit.

## Primary citations
Schroeder companion: https://michaelschroeder.ai/research/ErdosSzekeres/companion
Tóth–Valtr 2005: https://library.slmath.org/books/Book52/files/30toth.pdf
Norin–Yuditsky Theorem 3.1: https://arxiv.org/pdf/1509.03332
Rote versioned source: https://arxiv.org/html/2503.02336v1#A2
Baek–Balko section 3: https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.13/LIPIcs.SoCG.2025.13.html

## Verification and review provenance
Selected original archive files passed ZIP length/CRC32 checks; no Lean or SAT was run. Supplementary retrieval receipt: tmp/schroeder_comparison_20261021/selected_sources/retrieval_receipts_20261023_geometry.json.
One fresh regular Claude review was requested with tools Read,Grep,Glob, semantic model claude-fable-5-1, wire claude-fable-5-1-reversed, configured effort xhigh. Job 553bd45331a24838a8cf46cd603a5093 failed with REVIEW_UNAVAILABLE: CLI failed; receipt b596e82cece84b1181399d06f05921f1. No completed thread, model or effort evidence; no retry or fallback. Review traces: .aris/traces/novelty-check/2026-10-23_r20/.

