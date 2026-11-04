# Independent ARIS review: fifteen new conditional T17 inputs and actual safe application

**PASS for both gates**, modulo the explicit primary rank and accepted
general-transfer/source imports. The fifteen exact local iff classifications
are proved for all arbitrary complete-graph required matchings. Their actual
safe application covers 1046 of the accepted 1281 covered-target records,
leaving exactly **235**, all at target31. Complete twelve-hole Q6, complete
higher layers and full P6 remain OPEN.

Reviewer `/root/higher_q5_nearbalanced_review`, user-selected GPT-6.1-sol /
high, independently checks the producer `a8_bridge_inputs_audit` package
under ARIS proof-checker. Review independence is same-family; acceptance
is provisional. No producer, frozen input/output or accepted state was
modified.

Proof SHA256:
`a636edd4891b1c2a90336e7e2496fe0f2458f193df5cb501255b6533d30b6cf0`.
Application SHA256:
`4357c065ec297de2ab57ba5f2973aadb1987cc5b37935597ccd7e47222f62075`.
Manifest SHA256:
`0c40fc7c8d25f67aa4cc4e79698e2c7477b95b5d38ebf2f7a123a6c29c3d3534`.
All160 declared frozen file hashes match before and after the audit;
declared sizes and all certificate format lengths are checked.

## Gate 1: exact local iff theorem

The exact new indices are97,113,177,178,179,180,181,182,234,239,240,241,
281,282,283 in TWELVE_EXTRA_FORCED_summary.json and the matching prefixes.
For each row H={0} union its specified seven majority holes J, U={1,2,4},
K=Q5 minus H, p=8,q=16. For EVERY perfect matching F of the COMPLETE graph
on K, a simple29-cycle on exactly Q5 minus U containing F and adding only
short edges exists **if and only if pq is absent from F**. Required edges
may be long or same-parity. A common cube automorphism transports the hole
set, omissions, forced included hole, pair and entire matching together.

The full theorem tables were parsed independently and compared with the
exact summary, config and per-prefix metadata. Every K has24 vertices;
K'=K minus {p,q} has22. The unique included hole with exactly two available
short neighbors outside U is0, with neighbors8 and16, both covered.
Coordinate-permutation orbit comparison finds no new row in any of the old
seven accepted forced-T17 marked classes. Since both old and new singleton
minority normalize to0, any common cube automorphism between them fixes0
and is a coordinate permutation. Thus no unexamined translation can supply
a missing old-class match. These new certificates are necessary evidence.

| ID | Local proof obligation and discharge |
|---|---|
| L01 | A permitted cycle must have degree2 at hole0, and only short edges may be added there because no required edge meets a hole. Its only retained short neighbors are p,q, so p--0--q is forced. If F contains pq these form an isolated triangle, incompatible with the required29-vertex single cycle. Necessity is analytic, not a deficient-rank inference. |
| L02 | Every supplied S has seventeen distinct short edges, degree0 at U, degree1 at all24 covered terminals, degree2 at the five included holes and no cycle. Hence it has exactly twelve path components on all29 retained vertices. Its actual complete endpoint pairing is independently derived. |
| L03 | The component through0 is exactly p--0--q: both physical edges occur, 0 has degree2, p,q degree1. The derived full pairing contains pq. Delete that exact pair and require exact agreement with the saved reduced perfect matching P' on K'. Every reduced matching column uses all22 K' terminals exactly once. |
| L04 | If F excludes pq, write F(p)=a,F(q)=b. Matching validity makes p,q,a,b distinct. Replacing pa,qb by ab gives an arbitrary perfect matching F' on K'. Contracting the labelled path a--p--q--b shows F+P is connected exactly when F'+P' is connected. Long/same-parity ab is allowed. Common matching pairs remain labelled two-edge components, rather than being collapsed to a single simple edge. |
| L05 | Every reduced connectivity bit is recomputed, and fifteen new GF(2) eliminations give rank1024. The generic rank bound1024 on H22 makes the1024 selected complete rows span its full row space. Every arbitrary F' column is nonzero by cyclically linking its eleven oriented edges; otherwise all selected rows vanishing would force all rows to vanish. Thus some selected P' connects to EVERY F'. The finite columns witness rank, not a restriction on quantified F. |
| L06 | Undo the contraction and expand the forest paths. Connectedness and exact degrees give one cycle on Q5 minus U containing F. A common physical F/S edge would be a length-one forest path and shared endpoint pair, yielding an isolated labelled two-edge component on24 endpoints; this cannot occur in a connected union. The deliberately fixed pq is already excluded from F. Therefore the expanded cycle is simple and every added edge is short, proving sufficiency with exactly the same F domain as necessity. |

The [primary accepted manuscript of Cygan--Kratsch--Nederlof](https://pure.tue.nl/ws/portalfiles/portal/99596886/1211.1506.pdf)
was directly inspected in this independent audit series. Its abstract
defines H_t on all complete-graph perfect matchings. Theorem3.4 and
Corollary3.5 on PDF page9 give rank_GF2(H_t)=2^(t/2-1) for every even t>=2.
At t=22 this is1024. No bipartite restriction or extrapolation from a
smaller certified matrix is introduced.

Fresh TWELVE_EXTRA_FORCED_REVIEW_rank.cpp uses DSU to validate every
physical forest and reconstruct its full pairing. It checks the exact
fixed cherry, removes pq and validates all reduced pairings/columns. For
each matrix bit it contracts eleven reduced row-pairs and adds actual
column edges; ten successful unions mean connected. It compares all bits
with the frozen matrix and performs new increasing-column Gaussian
elimination on the independently recomputed rows.

| Independent local check | Total |
|---|---:|
| Exact conditional inputs |15|
| Short forests, full/reduced pairings |15360|
| Reduced arbitrary matching columns |15360|
| Recomputed connectivity bits |15728640|
| Independent GF(2) eliminations |15|
| Rank of each1024x1024 reduced matrix |1024|

The checker exits0 and reports PASS. Producer pivots/combos are hash-bound
but not rank evidence. The original1024x2048 full-endpoint matrices,
extraction-column indices and producer author checker are not trusted or
executed as proof. The reduced certificates stand on their own. Search
exhaustiveness is unnecessary, and no unrestricted T17 is inferred.

## Gate 2: complete actual safe application

The exact source gate is final TWELVE_EXTRA_TYPES_REVIEW.json PASS,
SHA256 `d3acfe0680d227a60c7fac1f3bcef8dc22ed22d94298a0e72852428888dfad43`.
Its three accepted residual hashes match the unchanged source files with
0/504/777 original eleven-byte records. The accepted general safe-transfer
gate HIGHER_FORCED_CHERRY_REVIEW.json and its bound proof are explicit
imports. No desired complete twelve-hole result is a premise.

| ID | Actual application obligation and discharge |
|---|---|
| A01 | Every source has sorted distinct nonzero even Z5 and odd W6, root0 free, covered odd target and Z--W independence. Each actual target-facing cut is classified. Even row(4,2) takes3 Z sources; odd row(1,5) takes3 W sources excluding root's mirror. Covered v is not a hole source. Source sets and actual mirrors are checked, and mirrors exclude all original holes/root. |
| A02 | Both rows leave2 holes of each parity in completed A. Its free even root and prescribed covered odd target, including a crossing target, satisfy the accepted arbitrary-complete-graph endpoint theorem. All sources are originally free; shortness precludes a mirror being a crossing port. Independence and root exclusion make every mirror internally B-covered for every realizing original short matching. |
| A03 | Actual B minority/majority holes are Z intersect B and W intersect B plus Y in even consumption, or W intersect B and Z intersect B plus Y in odd consumption. Exactly the three mirrors Y are omitted. Delete only the outer coordinate and move minority,majority,omissions and obstruction pair under one common cube map. Each actual pair is covered, outside holes and has the parity of Y. |
| A04 | Root0 is in B precisely when v has outer-cut bit1, and then projects to0. Reject exactly when this actual0 belongs to the ACTUAL transported pair. For root in A exclusion is automatic. Source count3, independent nonroot holes, legal sources, arbitrary-matching endpoint input and same-parity covered pair discharge all generic single-cherry hypotheses. Its controlled completion/spare-gap proof ensures the ACTUAL compressed L lacks pq; original M_B lacking a same-parity edge is not substituted for that argument. |
| A05 | For c=0 use the explicit five-direction Q6 endpoint import. Otherwise the accepted tagged forest and simultaneous mirror suppression apply, including target-port boundaries. Apply the new local classification to the now-obstruction-free arbitrary L, expand all paths, and delete the tag. Every original edge, all vertices and prescribed root/target are restored, and all surviving new physical edges are short. Cut/source data are geometric while completion choices may depend on M, preserving the EVERY-realizing-short-M quantifier. |
| A06 | The independent all-cut/all-source predicate equals selected-witness membership for every original target/index. Copying nonhit original records unchanged in order proves the exact complement; no overlapping coverage decrement or matching-realizability exclusion is used. |

The independent Python application checker builds1160 marked lookup keys
from the exact new fifteen rows, with coordinate orbits generated by
adjacent swaps. Minority normalization is unique. It tests ALL six actual
cuts and ALL legal source triples for every source, evaluating20330 legal
projections. Every one of the 1046 frozen witnesses (32 bytes each) is decoded and
replayed against independently generated candidates: local ID, cut,
original-label source mask, actual M/J/U/obstruction masks and actual root
exclusion must all agree. Unique in-range indices and exact per-record
predicate/witness equality exclude stray or duplicate witnesses.

All three independent complementary byte strings equal the frozen raw
outputs, preserving original order:

| Covered target | Accepted input | Safe subset | Exact remaining |
|---:|---:|---:|---:|
|1|0|0|0|
|7|504|504|0|
|31|777|542|235|
|Total|1281|1046|235|

Fourteen of the fifteen local rows occur among chosen witnesses; index113
is unused. No minimal-registry conclusion is asserted. The nonempty v31
residual SHA256 is
`a84bde6025aac56f976bcf1a1c3367251b4ce9723c152e509102132cadd73124`.

## Supplemental geometry, independently checked

The application checker separately generates the coordinate-permutation
group fixing root0 and each normalized target. Adjacent swaps within the
target's1-coordinate class and0-coordinate class generate its full
stabilizer; BFS orbits and lexicographic canonical representatives are
computed independently. It also counts original target neighbors outside
the hole set, without finding or assuming an actual matching.

The original1281 source records form41 such marked coordinate orbits.
Their available original-target-neighbor counts are1:984,4:50,5:208,6:39;
all984 one-candidate cases belong to the already accepted safe subset.
W=N(0) occurs12 times at v7 and285 times at v31. The final235 records all
have target31 and W={1,2,4,8,16,32}=N(0); they form exactly6 marked
coordinate orbits and have available-neighbor counts5:205 and6:30.
Canonical orbit representatives and counts agree with the frozen profile.

These are finite GEOMETRIC facts only. A one-candidate neighborhood forces
the target mate if an original matching exists; it does not prove that
matching exists. W=N(0) and the six-orbit classification do not exclude
realizability or establish an extension. No remaining matching-existence
claim or negative Hamilton certificate is accepted here.

## Reproduction, counterexample pressure and final scope

Run TWELVE_EXTRA_FORCED_REVIEW_prepare.py with D:/anaconda/python.exe.
Compile the fresh rank C++ with D:/mingw64/bin/g++.exe -std=c++17 -O3,
run it with this directory as argument and save stdout to the reviewer
rank JSON. Run TWELVE_EXTRA_FORCED_REVIEW_application.py. The verifier
checks all160 frozen hashes again after computation; final reporting
requires both independent checker gates PASS.

Counterexample pressure covers a hidden third neighbor of0, a wrong fixed
cherry, an incorrect full/reduced pair, all-hole forest cycle, invalid
column support, common labelled pairs, degenerate contraction, finite
columns mistaken for universal F, the wrong field/rank domain, old-seven
unmarked substitution, source into root, canonical instead of actual
obstruction, independently transported omissions, covered target-port
isolation, and equal-count/different-residual sets. Explicit degree,
graph, marked transport and complete finite checks exclude these failures.
No limiting, asymptotic or probabilistic assertion enters the argument.

All twelve mathematical obligations pass with zero open issues. Set
local_15_forced_inputs_proved=true and
remaining_covered_target_geometries=235. The local DAG is primary rank plus
new reduced certificates -> exact iff statements; these plus accepted
generic safe transfer and accepted1281 source -> exact1046 sufficient
class. There is no circular dependency on desired twelve-hole closure.
Full T17, complete twelve-hole Q6, higher complete layers and full P6
remain unproved by this package. Semantic assurance remains
same-family/provisional relative to the named imports.
