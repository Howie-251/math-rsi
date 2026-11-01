# Derivation Package: 23 points with exactly two degree-six vertices

## Target

Prove Property B for a finite simple pair-covering 5-uniform hypergraph H with 23 vertices, 33 edges, and exactly two vertices of degree six. This is the r=2 branch of the established T33 minimum-counterexample reduction.

## Status

COHERENT AS STATED: complete conditional mathematical candidate, with exact numerical witnesses and independent A/B/C replay. Not yet implemented in Lean or reviewed across model families.

## Invariant Object

The sum over permutation positions of min(A_k,B_k,C_k−D_k), where A/B are the edge-last/edge-first union bounds, C is the ordered unique-intersection pair bound, and D is a justified loss from real bad link pairs. A strict value below one produces a Property-B coloring using the existing permutation lemma.

## Assumptions

- H is simple, 5-uniform, pair-covering, has 23 vertices and 33 edges.
- Exactly two vertices have degree six. Every other vertex has degree at least seven, as given by pair coverage.
- Existing strict two-lock bounds exclude any pair of degree-seven vertices with codegree at least four. Their certified values for codegrees 4,5,6,7 are respectively 282379/293930, 131581/146965, 34907/41990, 1738/2261; see `../TWENTY_THREE_MANY_SEVENS.md` and `../TWENTYTHREE_HIGH_PAIRS.json`.

## Notation

The degree-six vertices are x_0,x_1. Let L be the degree-seven vertices and t=|L|. Write λ(u,v) for codegree. A pair is bad when its codegree is at least two. Five selected locks use bits 0,...,4; a mask B denotes the exact intersection of an actual edge with those locks, and n_B is its multiplicity.

## Derivation Strategy

Choose all degree-six vertices. Their small codegree excess leaves enough degree-seven points with unit codegree to both. Select three such points with at most one bad pair. The resulting complete local domain has only two disjoint possibly nonunit pairs. Every actual type input is among 412 labelled integer patterns, reduced computationally to 208 representatives; all have exact strict bounds.

## Derivation Map

1. Total degree 165 gives at least 15 degree-seven vertices.
2. Degree-six codegree excess equals two, so each low vertex has at most two bad neighbors.
3. At least 11 degree-seven points have unit codegree to both low vertices.
4. Among these points choose three whose bad graph has at most one edge.
5. Enumerate all actual five-lock traces using exact pair and degree equations.
6. Apply exact permutation weights and real link-subfamily losses, producing a strict upper bound for every input.

## Main Derivation

### 1. Degree and selection propositions

Let u=21−t be the number of remaining vertices of degree at least eight. Then

165 ≥ 2·6+7t+8(21−t)=180−t,

so t≥15. For each low vertex x,

Σ_{y≠x}(λ(x,y)−1)=4·6−22=2.

Thus at most two vertices have nonunit codegree with x, and every pair involving x has codegree at most three. Remove from L all nonunit neighbors of either low vertex. The remaining pool P has size at least t−4≥11.

For a seven-degree vertex y,

Σ_{z≠y}(λ(y,z)−1)=4·7−22=6,

so it has at most six bad neighbors. Fix any y_4 in P. Among the other at least ten members of P, at least four have unit codegree with y_4. Choose any two of those, y_2,y_3. Each has unit codegree to y_4. Their mutual codegree b is in {1,2,3}, unless the already certified high-pair branch applies.

The low pair has codegree a in {1,2,3}. All six low-high pairs are unit. The selected locks therefore have degrees (6,6,7,7,7), pair codegrees a on 01 and b on 23, and unit codegree on the other eight pairs.

### 2. Complete local-domain proposition

Each set of at least three locks contains a unit-codegree pair: the only nonunit pairs 01 and 23 are disjoint. Consequently n_B≤1 for every |B|≥3. There are exactly 16 such masks among five locks; their entire domain is {0,1}^16.

For each (a,b)∈{1,2,3}² and every choice of those 16 bits, define

n_{ij}=λ_{ij}−Σ_{B⊃{i,j}, |B|≥3} n_B,

n_i=d_i−Σ_{B∋i, |B|≥2}n_B,

n_∅=33−Σ_{B≠∅}n_B.

Discard exactly those patterns with any negative entry. These are identities for the actual type counts of H, so every real input is retained. The nine (a,b) patterns have respectively 32,41,43,41,51,53,43,53,55 labelled type inputs, totaling 412. Degree-preserving and codegree-preserving relabelings reduce these to 208 representatives. A Lean implementation may use all 412 labelled inputs directly and avoid proving the orbit reduction.

### 3. Real bad-link losses

At each lock i the full four-uniform link lives on 22 vertices, giving at least ceil((4d_i−22)/3) unordered bad pairs: one for degree six and two for degree seven. The pure-singleton link subfamily lies on 18 free vertices, giving at least max(0,ceil((4n_i−18)/3)) bad pairs. These are nested quotas; their losses are allocated jointly, so no pair is subtracted twice.

For four representatives, strengthen this using every avoided-lock subfamily. If R is a subset of the other locks, let F_R be the center-incident edges that avoid R. Its four-point links lie on 22−|R| vertices, giving

q_R=max(0,ceil((4|F_R|−(22−|R|))/3)).

For each unordered type slot j with capacity c_j and both-direction permutation weight w_j, a nonnegative multiplier α_R certifies the loss lower bound

Σ_R α_R q_R − Σ_j c_j max(0,Σ_{R: slot j avoids R} α_R−w_j).

This follows by multiplying the real quota inequalities and using 0≤b_j≤c_j for actual bad-pair counts b_j. Numerical LP is only used to propose α; the displayed expression and strict bounds are checked with exact Fractions.

### 4. Exact strict witnesses

`TWO_LOW_THREE_HIGH.json` supplies 204 strict witnesses from pure/total quotas. Its four remaining groups 56,57,58,64 are replaced by `TWO_LOW_THREE_HIGH_REFINEMENT.json`, giving respective values

203/208, 342725/350064, 233/234, 21460/21879.

The largest bound over the selected 208 winners is 7292/7293<1. Thus every possible actual local input has a strictly positive probability of successful coloring.

## Remarks and Interpretation

This branch needs only five locks and no whole-hypergraph enumeration. The finite search enumerates exact local trace data whose completeness is supplied by the pair equations above.

## Boundaries and Non-Claims

- This file covers exactly r=2, conditional on the established minimum-counterexample reduction and permutation counting lemmas.
- This is not a declaration that the whole T33 target has been proved.
- Exact local checks alone do not establish coverage; the selection and trace reconstruction propositions above are necessary.
- The representative orbit reduction is computational here; formalization can avoid it using the full 412 labelled inputs.

## Open Risks

The candidate needs Lean connections for actual selection, exact trace reconstruction, link-subfamily quotas, and the finite inequalities. No mathematical gap is currently identified within the stated conditional branch.

## Evidence

- Scripts: `computations/propertyb33/round01/r123-child/two_low_three_high.py`, `two_low_refine.py`, `audit_two_low.py`.
- `TWO_LOW_INDEPENDENT.json`: 208 strict winners, 4784 independently recomputed position rows, four exact dual replays, no LP called in the audit.
- A/B/C are independently computed by expanding all 33 edge stubs and counting labelled injections, rather than reusing the binomial weight implementation.
- All four saved duals were reconstructed from their nonnegative multipliers, actual local counts, and unordered slot capacities; main terms, capacity penalties, and final losses agree exactly.
