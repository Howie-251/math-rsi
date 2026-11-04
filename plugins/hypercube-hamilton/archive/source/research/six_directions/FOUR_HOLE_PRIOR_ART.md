# Four-hole residual: focused primary-source audit

Date: 2026-11-01. Bounded literature check; not a novelty certification or proof of P6. Target: a 30-edge matching of Q6 with holes u,z even and w,t odd, where z is adjacent to neither w nor t. Local N3 therefore does not apply by short-edge completion.

## Exact available statements

**Alahmadi et al., Theorem 4 (2015):** for d≥2, a pairing P of Qd and two cube edges e1,e2 outside P incident with one vertex, there is a cube perfect matching P′ containing at least one of e1,e2 such that P∪P′ is a Hamilton cycle. Here “pairing” permits a perfect matching of the complete graph K(Qd), not merely cube edges. The theorem does not prescribe path endpoints and does not promise both extra edges. The discussion after its proof exhibits pairings with multiple individually forbidden extra edges. [Original publication, §6](https://dmtcs.episciences.org/2105/pdf).

**Gregor–Novotný–Škrekovski, Theorem 2 (2018):** d≥5, opposite-parity x,y, perfect P in B(Qd), xy∉P. A Hamilton x–y extension exists exactly when (P−{xP(x),yP(y)})∪{P(x)P(y)} contains no half-layer. It supplies no additional edge requirement. [Original paper](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i2p56/pdf/).

**Fink–Mütze, Theorems 11–12:** Theorem 11 replaces B(Qd) by K(Qd) in that fixed-end characterization. Theorem 12 says a perfect matching of K(Qd−{x,y}), with x,y opposite and d≥5, extends to a cycle avoiding x,y exactly when it contains no half-layer. Theorem 8 instead concerns a cycle avoiding one vertex; the cycle need not span the remaining vertices. These statements allow same-parity artificial matching edges, but do not prescribe an additional nonmatching edge in a fixed-end path. [Author manuscript, pp.3–4](https://tmuetze.de/papers/match.pdf).

## Concrete consequence for the current four-hole case

The following is our deduction, not a theorem stated in the sources. Assume M uses at least two directions. Set P=M∪{zt}, a perfect matching on V(Q6)−{u,w}. Since zt is long, a half-layer in P would be wholly contained in M. A short matching containing a whole direction-i half-layer uses only direction i: that half-layer saturates one of the two sets defined by parity outside coordinate i, and the induced cube edges inside its complement also have direction i. Thus P has no half-layer.

Theorem 12 yields a 62-vertex cycle through P avoiding u,w. Deleting the artificial edge zt gives a Hamilton z–t path of Q6−{u,w} containing all of M. Swapping w,t gives the analogous z–w path avoiding u,t. This does **not** give the required spanning u–v path; precisely the missing short edges from z to w,t obstruct the immediate endpoint splice. The one-direction case is already covered by the known five-direction result.

## What was not found and why nearby results do not finish it

- No checked primary source states a four-hole dense-matching theorem that delivers arbitrary prescribed opposite-parity target v from uncovered u. This records the bounded search outcome, not nonexistence of such a theorem.
- Perfect-matching fixed-end extension is equivalent to a cycle extension with one added closing edge. Asking additionally for a specified nonmatching path edge imposes another constraint; neither the two-incident-edge cycle theorem nor the fixed-end theorem alone establishes their conjunction.
- The 2025 small-matching preprint advertises |M|≤3n−13; at n=6 this is five edges, far below thirty. It cannot close this residual case. [Authors' arXiv submission](https://arxiv.org/abs/2506.21432).
- Unconstrained paired spanning-path-cover results do not preserve the thirty forced matching edges. The local two-pair cover derived from Fink is useful, but converting it to a prescribed u–v Hamilton path still needs a valid connector or edge-placement argument.

## N3 attribution boundary

The local near-perfect-completion theorem is presented as a derivation from cited results. The searches for “near-perfect”, “almost perfect”, “four uncovered vertices”, and fixed-end matching extensions did not locate its exact statement. This is insufficient to assert novelty. Retain the current non-novelty disclaimer and cite its actual input theorems.

No source above proves full P6. This note changes no proof acceptance status.
