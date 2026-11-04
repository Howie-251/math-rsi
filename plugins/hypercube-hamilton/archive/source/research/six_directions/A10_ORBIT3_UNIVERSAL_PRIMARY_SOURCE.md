# Imported matching-connectivity rank bound

Marek Cygan, Stefan Kratsch, Jesper Nederlof, *Fast Hamiltonicity checking
via bases of perfect matchings*, Journal of the ACM 65(3), Article 12,
2018. DOI: [10.1145/3148227](https://doi.org/10.1145/3148227).

Primary author accepted manuscript: [TU Eindhoven repository PDF](https://pure.tue.nl/ws/portalfiles/portal/99596886/1211.1506.pdf).
The repository PDF identifies itself as the accepted manuscript of the
published paper; browsed 2026-11-01. Preprint identifier:
[arXiv:1211.1506](https://arxiv.org/abs/1211.1506).

The paper defines H_t on *all perfect matchings of the complete graph* on
t labelled vertices: the entry is one exactly when their union is a
Hamiltonian cycle. There is no bipartiteness restriction on matchings.
For t=2 the double-labelled edge is interpreted as a two-edge cycle.

Definition 3.1 is on printed page 8 (zero-based PDF page 8). Starting from
X(2,empty)={01}, extend a matching M on t-2 vertices by a bit:
bit 1 adds the edge (t-2,t-1); bit 0 replaces the edge (t-3,alpha_M(t-3))
by (t-2,alpha_M(t-3)) and (t-3,t-1). Thus X_t has 2^(t/2-1) columns.

Theorem 3.4 and Corollary 3.5, printed page 9 (zero-based PDF page 9),
give a GF(2) factorization through X_t and rank(H_t)=2^(t/2-1) for every
even t>=2. **Only the upper bound rank(H_22)<=1024 is imported in the
new proof.** The appendix proof starts at printed page 37; the main
proof does not substitute a small-case experiment for that imported theorem.

No other assertion of the original research problem is imported here.
