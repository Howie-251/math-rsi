# Two-bridge inverse blocking for four-hole A faces

2026-11-01. ARIS proof-writer candidate. New finite checks pass; a fresh semantic
review is still required. This does not prove complete cores1,4,24 or eight holes.

## Exact claim and imports

Let A and B be coordinate Q4 faces of Q5, with common local labels. An arbitrary
complete-graph matching F has holes {x,r,s,t} in A, all even, and {0,y} in B,
with y odd. The omissions are x_A and y_B. Write F_A,F_B for its internal
restrictions, X_A,X_B for the crossing port sets, C:X_A -> X_B for the arbitrary
original bijection, and c=|X_A|=|X_B|. Thus c is even, 0<=c<=12,
|F_A|=(12-c)/2 and |F_B|=(14-c)/2. Every original edge is retained; all new
edges in the conclusion must be short.

Require r,s,t to be nonzero. Thus every selected bridge pair is disjoint
from the B holes {0,y}; this hypothesis holds for all three geometries
listed below. Without it, a bridge at the free B vertex0 would need a
sixth mode and is outside this lemma.

Import Q4 N14: every arbitrary matching with two same-parity holes extends
to a 15-cycle omitting either specified hole, with short new edges. Import the
finite Q4 tables with holes {0,y,a,b}, omitting {y,a,b} and retaining free0.
Each covers all 10395 matchings and has a positive 13-cycle for every
nonnegative entry. `verify_q4_three_avoided_all.py` checks all 12 canonical
tables, their 168 marked coordinate images, all positive cycles and all
negative degree completions. Its deterministic PASS is not a fresh semantic
review of this document.

For c>=4, choose any pair a,b of r,s,t. Define its negative inverse families
and blockers as below. If for the actual F_B at least one bridge pair has
no negative inverse, or a certified blocking pairing, then a required
30-cycle omitting x_A,y_B exists. For the three geometries in the final table,
this proves every c=10,12 input. For c=4,6,8 it leaves precisely the listed
finite B residual supersets, with every A matching and crossing bijection
still to be treated. No theorem for those residuals is inferred here.

## N14 boundary argument

First take an arbitrary perfect pairing D on X_A union {a,b}. F_A union D
has the same-parity holes x and the remaining retained A hole. N14 gives
a 15-cycle on A-x through this matching. Deleting D produces a spanning
path forest. Its endpoint pairing R has connected union with D: contracting
the paths recovers the original single cycle. D and R are counted as
edge-labelled matchings, including doubled edges in their union.

The two new short bridges are a_Aa_B and b_Ab_B. Depending on their B
positions, use one of the following five disjoint modes.

1. **Distinct internal mates.** Both B vertices are internally matched,
   F_B(a)=k, F_B(b)=l, and k!=b. Delete all D, attach C and the two bridges,
   then add F_B. The only overlaps are a,b, each joined to a distinct
   internally matched vertex outside the boundary. Thus no cycle can form.
   Suppress a,b and all A paths to obtain L with holes {0,y,a,b}.
   The boundary pairing is on X_B union {a,b}. Its union with the
   transported D is connected.

2. **Internally paired bridges.** F_B contains ab. Prescribe ab in D,
   replacing that artificial edge in the N14 circle by
   a_A-a_B-b_B-b_A. Write D' for D-ab, a pairing on X_A.
   Delete D' and attach C. Since c>=4, D' is nonempty, so this is a
   spanning forest. Its quotient Q on X_B has connected union with D'.
   L=(F_B-ab) union Q. The required B edge ab is restored in the expansion.

3. **Only a_B is a port.** Let d=C^{-1}(a_B) and prescribe ad in D.
   Replace this edge by a_A-a_B-d_A, using the short bridge and the
   original crossing. Delete D'=D-ad, attach all other crossings and
   the bridge at b. The boundary is (X_B-{a}) union {b}, of size c.
   D' is nonempty; the replacement circle is therefore cut into paths.
   Add F_B and suppress b. Its internally matched mate lies outside the
   boundary, preventing a cycle. Again L has holes {0,y,a,b}.

4. **Only b_B is a port.** The preceding construction with a,b exchanged.

5. **Both are ports.** Prescribe a C^{-1}(a) and b C^{-1}(b) in D.
   Their four A endpoints are distinct. Replace both prescribed edges
   by the corresponding short-bridge/original-crossing two-edge paths.
   Delete D' on X_A minus those two ports and attach all remaining
   crossings. Its boundary is X_B-{a,b}, of size c-2. Since c>=4,
   D' is nonempty. Its quotient Q has connected union with D'.
   L=F_B union Q.

All boundary pairings are transported through C, with bridge labels added
where indicated. In every mode, the interior of the compressed forest is
exactly (A-x) union {a_B,b_B}, containing seventeen vertices. A positive
13-cycle for L expands to a single simple 30-cycle with exactly the
required support. Path interiors are mutually disjoint and disjoint from
the 13-cycle. All original edges occur in the paths or L; every auxiliary
edge is deleted or expanded, and all surviving new edges are short.

## Complete inverse families

Let L range over every negative six-edge matching in the appropriate
13-cycle table, and put m=(14-c)/2. For a fixed mode the following inverses
produce all negative outputs, grouped by their original internal matching
F_B. Edges are unordered, but each oriented endpoint assignment below is tried.

* Both ports: choose J subset L of size m, F_B=J, Q=L-J.
* Paired bridges: choose J subset L of size m-1, F_B=J+ab, Q=L-J.
* Only a a port: choose oriented edge kq of L and J subset L-kq of
  size m-1. Set F_B=J+bk, Q=L-J-kq+bq. Exchange a,b for the other mode.
* Distinct internal mates, with R pairing a,b: choose oriented edge kl
  of L and J subset L-kl of size m-2. Set F_B=J+ak+bl and
  R=L-J-kl+ab.
* Distinct internal mates, with R not pairing a,b: choose two distinct
  oriented edges kq,lp of L, and J subset L-{kq,lp} of size m-2.
  Set F_B=J+ak+bl and R=L-J-{kq,lp}+aq+bp.

These are exact inverses of path suppression: an untouched F_B edge must
be in J; the internal mates of a,b determine the modified L edge(s).
Conversely each displayed construction is a matching on the required
support and suppresses back to L. No length or parity restriction is
placed on J, F_B, R, Q or C.

For each fixed F_B family the saved blocker D0 is a perfect pairing on
the appropriate boundary whose union with **every** bad output is
disconnected. Pull D0 back to A and choose it as D, or as the remaining
D' after the required prescribed edge(s). N14 supplies an output whose
union with that choice is connected, so the output cannot be negative.
An F_B absent from the inverse list has no negative output in that mode.

`r4_boundary_blocking_probe.py` saves explicit blockers. A missing blocker
is retained as an unresolved input, never used as a negative theorem.
`verify_r4_inverse_blockers.py` independently regenerates the inverse
families by sequential insertion of missing bridge vertices into Q edges,
compares all sets exactly, checks all supports, and checks every positive
blocker by undirected graph traversal. It does not import the inverse
formulas, blocker search or connectivity routine from the producer.

## Current scope

The following normalized A geometries have B holes0,1 and omit the stated
A vertex. A simultaneous coordinate permutation gives any required
three-avoid table image and transports every inverse family and blocker.

| Original core | A holes | A omission | candidate residual B counts c=4,6,8 |
|---|---|---|---|
|1|0,3,5,9|0|210,28,1|
|4|0,3,5,15|0|272,32,1|
|24|3,6,10,15|3|See r4_joint_blocking_check.json|

The c=10,12 lists have no unresolved B inputs. For the first two cores,
the unique c=8 common residual is {(6,7),(10,11),(12,13)}. The joint lists
are intersections across all three bridge pairs, not sums of per-bridge
exception counts. Reproduction and exact files are in
`r4_joint_blocking_check.py/.json` and `r4_inverse_blockers_*_verification.json`.

The proof above intentionally assumes c>=4. At c=2, two occupied bridges
would leave D' empty and an inaccessible closed component. At c=0 the
paired-bridge replacement has the same problem. These boundaries need
separate proofs. Some c=4,6,8 residuals also admit no two-bridge forest
solution, so a different construction, such as four bridges, is required.
