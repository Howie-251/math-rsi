# C5 single-matching coverage factors and the capacity prediction

This is a paper audit of the newly authorized finite capacity interface. It evaluates no matrix, word, matching, bitset or candidate. All actual action/permutation/block data belong to the numeric owner.

## What each block mask must mean

The original exact same-side far-pair formula needs at most one noncancellable matching edge on a length≤3 route: MII,IIM orIMI. Three same-side matching steps reduce to one; other two-matching/one-incidence arrangements end on the opposite side. Thus an individual selected matching edge is by itself a witness to each far clause it covers; it does not need another selected edge of the other matching.

Once a literal common incidence-preserving C5 action is bound, every matching block consists of five edges forming one invariant orbit. If any of those edges witnesses a representative far clause, invariance gives a witness for every member of its five-pair orbit. Build one bit for each of the216 far-clause orbits, and set a block's bit exactly when one or more of its individual edges occurs in that representative's positive41-edge clause. Repeated occurrences of a block are one positive OR bit, not independent choices.

A point-matching block contributes own-route witnesses to point-far clauses **and** opposite-relay witnesses to line-far clauses. Its mask must include both contributions in the same216-bit universe. A line block has the dual mixed contribution. It would be incorrect to use only the108 clauses on the block's own side when computing the joint capacity bound.

A complete invariant perfect matching on either side selects four orbit-pair blocks. Its exact coverage contribution is the bitwise OR of those four block masks. It has no hidden contribution requiring two of its blocks simultaneously, because every reduced far route uses only one matching edge. For any two valid side matchings P,Q, all required far pairs are covered exactly when

mask(P) OR mask(Q) = FULL216.

The mixed pairs and old near same-side pairs remain covered by incidence paths. Therefore this equation plus the orbit-degree conditions is sufficient as well as necessary for D≤3 in this unrestricted C5-invariant paired model. No triangle-free or rectangle condition is implicitly imposed.

## Completeness of the single-side enumeration

The eight free5-orbits cannot match internally: an equivariant involutive shift on a5-orbit would satisfy2r=0 and hence r=0, a loop. Every perfect matching pairs the eight orbits, with five independent shifts for each of the four pairs. Thus the entire single-side domain is7*5*3*1 times5^4=65625 matchings. Enumerating each unordered orbit-pairing once and every shift tuple is complete, assuming the literal block and reverse-shift binding is correct. Point and line sides must both be treated; equal combinatorial parameters alone do not justify assuming their actual coverage maxima are equal.

## Valid and invalid conclusions from the capacity sum

Let mP=max_P popcount(mask(P)) and mQ=max_Q popcount(mask(Q)), over all65625 valid single-side matchings on each side, retaining every collinear/concurrent block. Then for every joint pair,

popcount(mask(P) OR mask(Q)) ≤ popcount(mask(P))+popcount(mask(Q)) ≤mP+mQ.

If mP+mQ<216, this strictly excludes every completion in this fixed common-C5 family. No billions-pair join, graph or BFS is needed for that conclusion. The count is in orbit clauses, not raw edge routes; all these clause orbits have the same length five.

If mP+mQ≥216, the capacity-alone prediction is refuted or insufficient. It is not a graph, and it is not a proof that any two matchings are complementary. One may inspect the two stored argmax matchings: if their OR is FULL216, they provide an actual binary matching witness whose graph still needs the separately required production/fresh acceptance. If that one OR is not full, it proves nothing negative about other pairs. A later exact coupling model or join would require a separately justified/authorized task; no automatic continuation follows.

The valid i_x+3j_x≤3 cuts from `PAPER_INTERFACE.md` are not prerequisites for this capacity test. Omitting such consequences only makes the side domains larger and the upper bound weaker, so it cannot invalidate a negative capacity bound. They must not be imported with missing hypotheses or incorrectly deduplicated linear coefficients.

## Conjugacy scope, if a complete fixed-subgroup NO is obtained

Sp4(F3) has order51840 with a single factor5. Every order-five subgroup in this group is a Sylow5 subgroup, and all are conjugate by a symplectic collineation. If a matching pair were invariant under some common order-five subgroup, conjugating both matchings and the geometry would carry it to a matching pair invariant under a fixed chosen subgroup, preserving incidences and diameter.

Consequently a complete NO for the fixed C5 family would also exclude paired matchings having **any common C5 subgroup inside the actual symplectic group**. This does not say arbitrary matchings are WLOG invariant, does not treat two different unmatched symmetry subgroups as a common one, and does not classify broader permutation symmetries. This is a paper transport, not an additional enumeration. No conclusion is asserted before the actual finite capacity or coupling result exists.
