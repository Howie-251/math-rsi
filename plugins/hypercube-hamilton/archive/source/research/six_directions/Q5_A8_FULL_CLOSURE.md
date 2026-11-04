# Complete Q5 A8: proof assembly

2026-11-01. ARIS proof-writer. Assembly requires final acceptance of every
listed orbit input and a separate independent whole-A8 review. Full P6
is not claimed by this auxiliary theorem.

## Exact theorem

Let F be any matching of K(Q5) whose holes have counts3 and5 in the two
parity classes. For every specified majority-parity hole v there is a cycle
on exactly Q5 minus {v}, containing F, with all edges outside F short.
The required matching may contain arbitrary long and same-parity edges.

## Dependency map and acceptance gate

1. Complete A6 and its already accepted arbitrary-matching scope.
2. A8_PARTIAL_PROOF_PACKAGE.md, with A8_PARTIAL_REVIEW: augmentation and
   every cut with majority-minus-minority count1,2,3.
3. A8_DELTA4_FIRST_ORBIT.md and its final review: first residual orbit.
4. A8_ORBITS2_3_ANALYTIC_CLOSURE.md and its final review: second and third
   residual orbits, using closed matching sets and parity.
5. A8_ORBIT4_FULL_CLOSURE.md and its final review: fourth residual orbit,
   four sufficient cut constructions plus all200475 finite positive inputs.
6. A8_ORBIT5_FULL_CLOSURE.md and its final review: fifth residual orbit,
   four sufficient cut constructions plus all2732625 finite positive inputs.
7. A complete independent geometry cover and disjointness check. Prior
   independent A8 and Q5 higher-hole reviews established the2700-geometry
   domain and exact orbit partition; the assembly review must check that
   every imported orbit theorem has the required marks and quantifiers.

Every final review must be PASS and bind fixed proof/evidence hashes before
the whole-A8 acceptance gate is met. In particular a running certificate
producer, positive samples, or a merely conditional final-orbit draft is
insufficient. Full unrestricted T15 is not an import.

## 1. Short augmentation and normalization

If a minority hole is adjacent to a majority hole other than v, add their
short edge to F. This leaves2:4 holes and keeps v free. Complete A6 supplies
a cycle on exactly Q5-v, preserving F and the added short edge. Thus assume
no such adjacent pair exists.

Translate v to0. The majority holes become even and the minority holes odd,
regardless of their original numerical parity. Write the four other even
holes as Z and the three odd holes as W. Now |Z|=4, |W|=3, and no Z-W
short edge exists. Translation and coordinate permutations preserve all
short edges and transport the full arbitrary-matching domain bijectively.

## 2. Complete geometric partition

There are exactly2700 normalized pairs (Z,W) satisfying these conditions.
Exactly2540 have a coordinate face containing0 whose majority-minus-
minority hole count is1,2,3. The full matching instances of these geometries
are covered by the accepted partial theorem, including zero/one crossings
where applicable and arbitrary long original crossing partners.

The remaining160 pairs are precisely the following disjoint coordinate
orbits. The prescribed omitted hole remains0 in every row.

| Z | W | orbit size | complete proof input |
|---|---|---:|---|
|3,5,6,15|8,25,26|60|first-orbit delta4 theorem|
|3,5,6,15|25,26,28|20|orbits2/3 analytic theorem|
|3,5,15,23|25,26,28|30|orbits2/3 analytic theorem|
|15,23,27,29|1,2,4|30|orbit4 complete theorem|
|15,23,27,29|2,4,8|20|orbit5 complete theorem|

The sizes sum to160. Each imported theorem covers **every** matching on
the complement of its representative hole set, with arbitrary required
edges, and omits exactly0. A coordinate permutation carrying a row to any
other member carries the entire construction and preserves those marks.
Thus the representative theorem proves every realizing matching of every
geometry in its orbit, not merely the finite sample of one matching.

## 3. Completion and boundaries

Short augmentation handles all inputs outside the normalized independent
domain. The partial theorem and five full orbit inputs cover every member
of that domain. Translating back gives the exact theorem for every F and
every specified majority hole v. All new surviving edges are short and
the result is a single31-cycle, by the explicit imported conclusions.

This proves A8 once the acceptance gate above is met. It does not prove
A10, all arbitrary-hole Q5 endpoint statements, or any complete remaining
Q6 hole layer. Previously accepted K8 is not used to prove A8 here, so its
dependence on the partial A8 theorem introduces no circularity.
