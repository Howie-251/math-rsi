# General-method discussion: sources and scope

2026-10-21. This is a bounded literature/mathematics discussion requested by the user. The m(5)≥36 Goal remains paused. No new proof search, Lean build, or small-k certificate rerun is part of this discussion.

## Local primary paper

- Cherkashin–Kozik, *A note on random greedy coloring of uniform hypergraphs*, [arXiv:1310.1368v1](https://arxiv.org/abs/1310.1368).
- Existing local PDF: [cherkashin_kozik_2015_random_greedy.pdf](../../ref/cherkashin_kozik_2015_random_greedy.pdf).
- Local `pdfinfo` confirms six pages, 317306 bytes, matching title; `pdftotext -layout` successfully extracted all pages to [CK2013_FULLTEXT.txt](CK2013_FULLTEXT.txt).
- The filename uses the journal year 2015; the downloaded content is the 2013 arXiv version. No duplicate download was needed.

## Published comparison and current-search scope

[Grill–Linzmayer, arXiv:2403.05674v3](https://arxiv.org/html/2403.05674v3), revised 2024-06-20, gives the small-parameter comparison 32, 64, 128, 263, 538 for k=5,…,9. Its introduction states the RS asymptotic lower bound; §2 explicitly notes that its discrete greedy refinement does not change that asymptotic result. These are claims of that primary source, not an exhaustive certification of the worldwide literature on 2026-10-21.

A fresh search also located the authors' [2026 overview chapter](https://link.springer.com/chapter/10.1007/978-3-032-18810-6_9). Only publisher metadata, abstract, and references were accessible; its full text and numerical tables have not been read. The search did not identify a primary paper proving an improved unrestricted asymptotic order. Absence in this bounded search is not a proof that no such result exists.

The collaborator's local manuscripts, their existing replay record, and their general lemmas are distinguished in [SMALL_K_EXTRACTION.md](SMALL_K_EXTRACTION.md). Finite new values do not imply an asymptotic improvement.

## Direct mathematical diagnosis of the CK estimate

Write edge budget \(M=\kappa 2^{k-1}\). CK's sufficient inequality is
\[
\kappa(1-p)^k+\kappa^2p<1.
\]
At the RS scale \(\kappa\asymp\sqrt{k/\log k}\), useful \(p\) has order \(\log k/k\). The first term forces approximately \(kp\gtrsim\log\kappa\); then the second costs order \(\kappa^2\log k/k\). This explains the square-root/log scale **within this estimate**, without claiming a barrier for every analysis of greedy coloring.

Retaining the exact central integral alone gives
\[
\int_{-p/2}^{p/2}(1-4x^2)^{k-1}\,dx=p(1+o(1))
\quad\text{when }p=O(\log k/k),
\]
because the integrand is uniformly between \((1-p^2)^{k-1}\) and 1, and \(kp^2\to0\). Replacing \(M^2\) by \(M(M-1)\) also changes the coefficient only by \(1-o(1)\). Thus these two isolated refinements do not improve the leading asymptotic constant in this particular estimate. A nonvanishing improvement needs an additional uniform gain in the active failure-event bound; present local certificates have not supplied that gain for all sufficiently large k.

This is a scope diagnosis, not an impossibility theorem for locks, shared bad pairs, or the greedy algorithm.
