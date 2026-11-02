# Every simple four-uniform hypergraph with at most seven edges is two-colorable

**Theorem.** Let V be any finite set and let E be a set of four-element subsets of V with m=|E|<=7. There is a coloring c:V→{0,1} taking both values on every edge.

**Proof.** Give the finite set Ω={0,1}^V the uniform distribution. This is the experiment that independently assigns each vertex a fair color. For an edge e, let B_e be the event that all four vertices of e receive the same color. Exactly two of the sixteen equally likely colorings of e are constant, so P(B_e)=1/8.

For each coloring, the indicator of the union of the B_e is at most the sum of their indicators. Averaging over Ω gives

P(⋃_{e∈E} B_e) <= Σ_{e∈E} P(B_e) = m/8.

Consequently the probability that every edge has both colors is

P(⋂_{e∈E} B_eᶜ) = 1-P(⋃_{e∈E} B_e) >= 1-m/8 >= 1/8 > 0.

A positive-probability subset of the finite coloring space is nonempty. Any coloring in it has the required property. ∎

This is a readable transcription of the canonical repaired PROOF.tex. The argument includes E empty; Ω has one element when V is empty.
