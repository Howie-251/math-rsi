# Actual T15 marked orbits: fifteen4096-rank certificates

2026-11-01. ARIS proof-writer producer package. PROVABLE AS STATED relative
to the explicit primary rank import and supplied finite certificates;
fresh independent proof-checker acceptance remains required. The original
universal T15 theorem, full ten-hole Q6 and full P6 remain OPEN here.
No old T26/T63 source, accepted ledger or main state was modified.

## Exact theorem and registry

For every registry row below, every arbitrary matching F of K(Q5) with
minority hole0 and exactly the listed five majority holes extends to a
simple30-cycle omitting exactly the listed majority pair. Every edge
outside F is short; original required edges may be long or equal-parity.
A common cube automorphism transports minority,majority,marked omissions
and the entire matching together, including parity reversal. Only these
fifteen marked orbits are claimed, not all T15 geometries.

| Index | Majority holes | Marked omissions | Forests examined | GF2 rank |
|---:|---|---|---:|---:|
| 0 | 1,7,11,14,19 | 1,19 | 17698 | 4096 |
| 1 | 1,7,11,13,14 | 1,7 | 26006 | 4096 |
| 2 | 1,7,11,14,31 | 1,31 | 13798 | 4096 |
| 3 | 7,11,13,14,19 | 13,19 | 18236 | 4096 |
| 4 | 7,11,13,19,31 | 19,31 | 28866 | 4096 |
| 5 | 7,11,13,19,22 | 11,13 | 27366 | 4096 |
| 6 | 1,7,11,14,21 | 1,21 | 20508 | 4096 |
| 7 | 7,11,13,22,26 | 22,26 | 45100 | 4096 |
| 8 | 7,11,13,22,31 | 11,13 | 30887 | 4096 |
| 9 | 7,11,21,26,31 | 7,21 | 26844 | 4096 |
| 10 | 1,2,7,28,31 | 1,2 | 19855 | 4096 |
| 11 | 1,7,11,22,31 | 1,7 | 24859 | 4096 |
| 12 | 1,7,14,26,31 | 1,7 | 21361 | 4096 |
| 13 | 1,7,14,26,31 | 1,14 | 16756 | 4096 |
| 14 | 7,11,21,26,31 | 21,26 | 20592 | 4096 |

## Short-forest and rank proof

Fix one row. Put H={0} union its majority set, U=the two marked omissions,
and K=Q5-H. Thus K has26 vertices and H-U has4 included holes. A selected
forest S has short edges only, omission of U, degree1 at every vertex of K
and degree2 at H-U, and is acyclic. It therefore consists of13 paths,
has17 edges, and has endpoint set precisely K. P(S) pairs its path ends.
For any original matching F on K, a connected labelled alternating
26-cycle F+P(S) expands to a single simple30-cycle on Q5-U. A shared
F/P pair would be an isolated labelled2-cycle, impossible in a connected
26-cycle, so no length-one forest path duplicates an original edge.
Every surviving new edge lies in S and is short.

The imported generic matching-connectivity theorem is
rank_GF(2)(H_26)<=2^(26/2-1)=4096. H_26 is indexed by ALL perfect matchings
of the complete graph on K, with entry1 exactly for one labelled
alternating cycle. Corollary3.5 of Cygan--Kratsch--Nederlof,
*Fast Hamiltonicity checking via bases of perfect matchings*, supplies
the upper bound for every even endpoint count. Primary version and
statement alignment are recorded in A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md.
Only this generic upper bound is imported; no bipartiteness restriction
on required matchings or experimental rank extrapolation is used.

For each registry row the supplied4096 forest pairings restricted to the
supplied4096 valid complete-graph matching columns have full GF(2) rank.
Their complete rows of H_26 are consequently independent and span its
entire row space. Every fixed matching F has a nonzero column: if its
13 edges are(a_i,b_i), pair b_i to a_(i+1) cyclically. This gives another
perfect matching connecting with F. If all selected rows vanished at F,
their entire span and hence every row would vanish there, contradiction.
At least one selected forest connects with every F; expand it as above.
This proves the exact universal matching theorem for the registry row.
The argument applies independently to all15 rows.

No enumeration of every original matching is needed. A deficient or
capped forest search would be OPEN rather than a counterexample. All15
searches reached rank4096 without a cap or deficient termination.

## Explicit finite certificate interface

Each prefix is Q5_T15_RANK_orbit_00 through Q5_T15_RANK_orbit_14. Its
configuration lists six holes and two omissions. Each _forests.bin has
4096 records of34 bytes (17 sorted short edges), each _pairs.bin and
_columns.bin has4096 records of26bytes, and _matrix.bin has4096 rows of
512 bytes with bit j representing connectivity to column j, low-bit-first.
The _pivots.bin and _combos.bin files also have4096 rows of512 bytes:
pivot j's highest set bit is j, and equals the XOR of original matrix
rows selected by combo j. This certifies rank4096 exactly over GF(2), or
an independent checker can recompute elimination from scratch.

Required independent checks are forest edge uniqueness, shortness,
exact omission/degrees, acyclicity and path pairing; column matching
validity on exactly K; all16777216 connectivity bits per registry row;
and rank evidence. The general producer DFS enforces cycles via DSU,
not an independent-cherry assumption. Generation completeness is never
a premise; only the selected4096 legal witnesses per row are needed.

A separate Python producer check for orbit00 recomputes every selected
forest and endpoint pairing, all16777216 matrix bits, and all pivot
combinations. That success validates the producer implementation on
one full certificate, and is not substituted for fresh independent
checking of all15 frozen rows.

## Actual Q6 projection scope

The source domain is the4096 original-record candidate remainder after
Q5_T26_RANK_batch. Its upstream rank/coverage audit is a separate gate;
no decrement is accepted here merely by reading producer residuals.
Within this domain, Q5_T15_RANK_profile.py tries every actual outer cut
containing covered odd target v and rows(a,b)=(3,2),(1,4), with root0.
It tries every legal two-bridge source pair, projects away the outer
coordinate, translates the actual minority to0 and applies common
coordinate permutations to all three marked sets. The profile records
the actual cut, sources and minority/majority/omitted geometry, not just
an unmarked hole type. There are exactly15 marked orbits in this domain.

In row(3,2), choose two even sources from the three Z holes in A. The
B minority is the single Z hole in B, majority is the three W holes in B
plus the two mirrors. In row(1,4), choose two odd sources from four W
holes in A excluding any whose mirror is root0. The B minority is the
single W hole in B, majority is the three Z holes in B plus the mirrors.
The mirrors are exactly the two prescribed majority omissions. Both
A endpoint inputs have balanced FOUR holes, already accepted. The
accepted simultaneous conflict/tag/forest suppression and expansion
construction applies. Required long compressed B edges are permitted
by the rank theorem. Global root and covered target remain prescribed.

A legal mirror is internally covered: original Z-W independence excludes
a hole, the selected free source excludes a crossing port, and the odd-
source restriction excludes root0. No further local T15 geometry test
is imposed for a rank-certified registry row. This is a universal
matching conclusion per eligible original marked geometry.

## Exact producer coverage and old-core alignment

The projection profile lists every candidate4096 record and all actual
witnesses. The rank-certified union covers2346 records, leaving1750:

| v | Input | Covered | OPEN |
|---:|---:|---:|---:|
|1|910|480|430|
|7|1476|846|630|
|31|1710|1020|690|
|Total|4096|2346|1750|

All462 records with no T17 cut are covered. T17 here means an actual
row(3,1) or(0,4); the source-choice exclusions are automatic for these
covered-target rows. The remaining1750 all have at least one such cut,
but no T17 theorem or full ten-hole closure is imported or asserted here.
Greedy coverage uses orbit5 for1764, then orbit0 for462, then orbit10 for120.
Every coverage witness and exact remaining original bytes are saved.
Fresh application review must replay all projections and compare full
remaining byte/set equality, not merely these cardinalities.

Most of these marked geometries do not have an old residual-core ID:
the original geometric diagnostic excluded a same-face condition before
constructing its54-core registry, whereas the accepted conservative
T15 lookup did not accept that unproved shortcut. In particular orbit0,
which covers all462 no-T17 records, is such a previously unaccepted
same-face geometry. It is proved here by its own rank certificate, not
by reusing an unsupported shortcut. Q5_T15_RANK_old_core_alignment.json
records explicit mapping where present: orbit10=core11, orbit12=core26,
orbit13=core34, orbit14=core51. None is silently treated as an old
accepted core. Actual scope is always the explicit marked registry above.

## Dependency and acceptance boundaries

The local rank theorems depend only on the primary generic rank bound
and finite selected forests/columns/matrices. Q6 coverage additionally
uses the accepted uniform transfer, its balanced-four-hole endpoints,
and the upstream T26 candidate residual as a separate acceptance gate.
The DAG is acyclic and no new ten-hole theorem is fed into a local proof.
All15 local certificates and actual coverage are producer-only pending
independent review. Full T15, full ten-hole free/covered Q6, higher-hole
layers and full P6 remain unproved by this package. No main ledger was
updated and no failed search is used as a negative certificate.
