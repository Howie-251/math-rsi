# Opposite forbidden parities force intersecting optional-edge unions

Date: 2026-11-01. ARIS proof-writer draft; independent audit pending.
This is a four-dimensional gluing input, not the full Q5 T15 theorem.

## Exact claim

On one labeled Q4, let L have exactly two same-parity holes, one specified
as forbidden vertex a. Let R have either two same-parity holes including
its forbidden vertex b, or four holes with parity counts 1:3 and b in
the majority class. Assume a and b have opposite parities.
Both matchings are arbitrary matchings of K(Q4), not necessarily short.

There is a short edge e outside BOTH matchings and extending 15-cycles
C_L on Q4-a and C_R on Q4-b, each containing its matching and e, and
having all new edges short.

Equivalently, their optional-new-edge unions intersect. The two cycles
may be chosen independently after choosing the common edge. No simultaneous
prescription of a whole optional-edge union in a single cycle is asserted.

## Dependencies and normalization

Translate a to 0, so b is odd. Coordinate permutations reduce the other
hole of L to 3 or 15. The same two-hole normalization applies to R when
it has two holes. Four-hole R with a short edge between its minority hole
and a nonforbidden majority hole reduces by adding that edge to a two-hole
instance, still avoiding b.

For remaining four-hole R, translate the minority hole to 0. Its two
nonforbidden majority holes have weight three, so permute them to 7,11.
The remaining forbidden majority hole has representatives 1,4,13. This
classification was checked on all marked geometries in
`A6_FINITE_INPUTS_REVIEW.md`; it uses no Q5 theorem.

## Positive certificates, not exact spectrum assumptions

The files `q4_n14_rich_3.bin`, `q4_n14_rich_15.bin` list every matching
with the corresponding two holes 0,p, avoiding 0. Each has 135135 records.
The files `q4_a4_rich_1.bin`, `_4.bin`, `_13.bin` list every matching
with holes 0,7,11,v, avoiding v. Each has 10395 records.
Each record stores the sixteen mate bytes (255 denotes a hole), a one-byte
cycle count, and that many explicit 15-vertex cycles. Define the stored
union U to be the union of all their edges outside the required matching.
It is a subset of the true optional-edge union.

`verify_q4_rich_spectrum_gluing.py` verifies matching rank coverage,
each cycle's exact vertices, every required edge and every new short edge.
It checks all 301455 records and 1634808 positive cycles. Every stored
union has at least 15 edges. Call a stored union high if it has at least
18 edges, and low otherwise. The low records are exactly:

- holes 0,3: 6 records, each with stored union size 16;
- holes 0,15: 36 records, each with stored union size 15;
- four-hole representative v=4: 20 records;
- four-hole representatives v=1,13: no low records.

These statements concern stored, witnessed unions. An exact upper bound
on the true spectrum is not required. The producer may have explored all
cycles on a low record, but this proof never relies on that exhaustiveness.

If either matching has a high witnessed union and the other has a union
of size at least 15, intersection follows from 18+15>32, since Q4 has
32 edges. It remains to compare the finite low candidates.

## Complete coverage of low candidates

Expand the two-hole low records under all coordinate permutations. This
gives 72 distinct candidate matchings with forbidden vertex 0. For the
second face, also translate by each odd vertex; there are 576 distinct
two-hole candidates with odd forbidden vertex. If different transported
certificates describe the same matching and forbidden vertex, take the
union of their stored unions. This is still a witnessed subset of the
true optional-edge union, so is valid for improving the bound.

For a four-hole R admitting an added short edge f, set P=R+f. If P is high,
R is high as well: every witnessed new edge for P is a new edge for R.
If P is low, R is obtained by deleting f from one of the transported
two-hole low candidates. The same witnessed cycles show the union
U(P) union {f} is available for R. Enumerate removal of every SHORT
required edge from every such low P. This includes each potentially low
adjacent-reducible R; it may also include R that has another high completion,
which is harmless. Repeated R candidates can again merge their unions.

For nonadjacent four-hole R, transport the 20 low representative records
under all 384 Q4 automorphisms and retain odd forbidden vertices. Combine
these candidates with those obtained by edge removal. After merging
and discarding unions already of size at least 18, 4128 four-hole
candidates remain. All have witnessed unions of size at least 15.

No matching outside these lists can lack a high certificate: the two-hole
tables, the four-hole residual tables, and the adjacent augmentation
exhaust all input possibilities. In particular the procedure never assumes
that a low table entry has a mathematically small exact spectrum.

## Finite intersection and conclusion

The verifier compares every one of the 72 first-face low candidates
with all 576 second-face two-hole candidates and all 4128 second-face
four-hole candidates. In every pair the witnessed unions intersect;
the minimum intersection size is three in each comparison. Thus the
low-low cases hold as well. This proves the exact claim.

## Five-dimensional consequences

Consider a matching F of K(Q5) with two prescribed omitted holes of the
same GLOBAL parity. Split into Q4 faces A,B separating the omitted holes.
Suppose either each face has exactly two holes of that parity (the
T44_5 split case), or one face has two holes of that parity and the other
has 1:3 holes with that parity the majority (the T15 split case).

The crossing count c is even. If c>0, pair A ports into D and use the
appropriate Q4 avoided cycle on A. Delete D, attach original crossings,
and compress paths onto B ports. The B matching has exactly its original
holes; its avoided-cycle theorem supplies the second cycle, and expansion
gives one 30-vertex circle omitting the two prescribed holes.

If c=0, the faces' required matchings are independent. On identifying
the two faces by short bridges, their omitted vertices have opposite
LOCAL parities because their GLOBAL parities agree. The present theorem
supplies corresponding optional edges in the two avoided cycles. Delete
those edges and add the two short bridges joining corresponding endpoints.
The result is a single 30-vertex circle. Required edges are never removed,
and the new bridges are short. This closes the zero-crossing case as well.

Thus these two geometric split conditions suffice for ALL original
matchings, regardless of crossing count. Other T44_5/T15 geometries and
full Q6 P6 are not asserted here.
