# Full A8 endpoint and ten-hole consequences: independent review

2026-11-01. Fresh reviewer `/root/a8_bridge_inputs_audit`, requested
GPT-6.1-sol/high. ARIS proof-checker method within the authorized scope.
Assurance: **same-family / provisional**.

**PASS relative to the explicitly accepted imports.** Full balanced-eight-hole
Q5 endpoints follow for arbitrary complete-graph matchings and every
opposite-parity target, free or covered. The six stated ten-hole cut rules
apply without a partial-A8 admissibility test. Independently filtering the
accepted 91225-record covered-target residual domain proves exactly 37003
additional geometries covered and **54222 geometries still OPEN**.
This does not establish full ten-hole P6, A10, the higher Q6 layers or full P6.

## Fixed input boundary and accepted dependencies

The theorem-bearing input is `Q5_A8_ENDPOINT_AND_TEN_CONSEQUENCES.md`.
The producer script and its output are read and hashed for comparison but
are not executed or imported by the new checker. The fixed full-A8 import
is the final PASS in `Q5_A8_FULL_REVIEW.json`, SHA-256
`625a3c3ac4db6742a23e3e6a9291c87b5ab8588da691445a0426cce07da5bf47`.
Its current source is `Q5_A8_FULL_CLOSURE.md`, SHA-256
`a4109945b5e6e4d1316e5acd18640687d7d5c6e9c287f2c3e0f91bdb2f681e75`.
This import permits arbitrary long and equal-parity required edges and
every specified majority hole in either numerical parity orientation.

K6's arbitrary-matching balanced-six-hole cycle theorem is read in
`A6_AND_EIGHT_FREE_CLOSED.md` and accepted through `A6_CLOSURE_REVIEW`.
K8 and its exact arbitrary-matching cycle conclusion are bound through
`Q5_K8_REVIEW`. The accepted ten-hole six-row transfer and its fixed
91225 residual domain are imported from `TEN_HOLE_COVERED_PARTIAL_REVIEW`.
The actual transfer statement, row formulas, endpoint completion and
tag/forest/suppression proof were read, including
`HIGHER_HOLE_UNIFIED_TRANSFER.md`.

The checker verifies PASS for all five direct theorem/review gates and
checks their recorded theorem/direct-import source hashes against current
bytes. It separately binds the three original independent residual binaries
to their hashes in the accepted ten-hole review. Large previously accepted
matching-certificate suites are not rerun. All these bindings and the new
comparison files are pinned in the review JSON; no production proof or
main state was modified.

The dependency DAG is acyclic: accepted A8 + K6 -> full balanced-eight-hole
local endpoints; endpoints + accepted K8/forest transfer -> six sufficient
Q6 cut classes; accepted old domain + independent six-cut replay -> exact
new coverage accounting. No new ten-hole theorem is fed back into A8.

## Endpoint theorem: all quantifiers and artificial edges

Let F be any K(Q5) matching with four holes in each parity class. Fix any
free root r and any opposite-parity vertex y. No adjacency of r and y is
assumed. No restriction is imposed on F's original edges or the parity
of a covered y's mate.

If y is free, r and y are distinct free vertices. Adding the auxiliary
edge ry gives a matching with three holes per parity. K6 gives a full
32-vertex cycle containing F and ry, even if ry is long. Deleting exactly
ry leaves one Hamilton r--y path. Every surviving edge outside F was a
new short edge of that cycle; the only auxiliary required edge disappears.

If y is covered, let h be its unique F-mate. The three vertices r,y,h
are distinct because r is free. The edge swap
`F' = (F minus {yh}) union {hr}` is a matching: h has just been freed,
r was free, and all other required edges are disjoint. Its holes are
exactly `(old holes minus {r}) union {y}`. Removing a hole of r's parity
and adding one of y's parity gives counts 3:5, with y in the majority.
These facts do not depend on h's parity or on hr being short.

The accepted full A8 cycle on exactly Q5-y contains F', hence contains
hr. Deleting hr gives a single r--h path containing every vertex except
y. Appending the original edge hy at h adds exactly the missing vertex
and gives the Hamilton r--y path. All original edges other than hy were
retained in F'; hy is restored; the auxiliary hr is removed. Every other
new edge is short. Thus the conclusion holds for every mate h, every
matching F and both root parities. If h was an artificial completion mate
in a later application, the same argument restores that required edge
of the completed matching before the transfer deletes its completion.

Taking y to be a short neighbor of r closes the Hamilton path by ry to
a full cycle. Since r is free, ry is a new short edge, and a 32-vertex
r--y path cannot already contain an edge between its endpoints. This
cycle consequence agrees with the previously accepted K8 theorem; it
is not used circularly to prove its endpoint premise.

## Six rows and hypothesis discharge

The global domain is a short 27-edge Q6 matching, normalized free even
root u=0 and covered odd target v. Z is the four other even holes and W
the five odd holes. When Z--W contains a short edge, the accepted full
eight-hole endpoint theorem justifies augmentation; otherwise Z union W
is independent. Root--W adjacency is allowed. For a cut with v in A,
write a=|Z intersect A|, b=|W intersect A|; c=0 remains covered by the
accepted five-direction theorem. For positive c the exact six sufficient
rows are:

| (a,b) | A local input | B local input and marked omission |
|---|---|---|
| (0,1) | Accepted balanced-two-hole endpoint theorem | K8 full cycle, balanced 4+4 holes |
| (1,1) | Accepted balanced-two-hole endpoint theorem | Full A8: minority Z intersect B, majority (W intersect B) union {y}, omit the even-source mirror y |
| (0,2) | Accepted balanced-two-hole endpoint theorem | Full A8 reversed: minority W intersect B, majority (Z intersect B) union {y}, omit the odd-source mirror y |
| (3,4) | New full balanced-eight-hole endpoint theorem | Accepted balanced-two-hole B cycle |
| (4,4) | New full balanced-eight-hole endpoint theorem | N14: two odd B holes, omit the even-source mirror |
| (3,5) | New full balanced-eight-hole endpoint theorem | N14 reversed: two even B holes, omit the odd-source mirror |

Every displayed A8 input has exactly 3+5 holes, with its specified omitted
vertex in the majority class. Complete A8 therefore replaces the former
partial-admissibility check for all marked geometries. The last three
rows now use the full 4+4 endpoint theorem directly, although the old
uniform theorem's smaller endpoint import had b<=3 or a<=2. Those bounds
served the old local import only; the already audited six-row completion
and forest proof explicitly permits these new rows.

Even bridge sources are original free even holes, whose odd mirrors cannot
be u and cannot be original holes by independence. In the odd-source rows,
there are respectively two or five original odd source holes. At most one
mirrors to u, and covered v is not a hole source. Thus a legal source
always exists. Each legal mirror is internally B-covered: its original
free mirror prevents a crossing edge, independence prevents another hole,
and the root-mirror exclusion removes u. These conditions are unchanged.

In the last three rows the completed A matching has exactly 4+4 holes.
If u is in A take r=u; otherwise use the accepted even-port choice, or
the even source in row (4,4). The port surplus supplies the needed root.
The target v stays covered by an internal original edge or its completion
edge at an odd port; it cannot equal an even root or an original free
bridge source. This discharges the endpoint theorem even when the actual
mate is an artificial completion partner. The resulting path contains
every completion edge before D is deleted.

All other steps remain the accepted construction: remove D, attach original
crossings and the optional short bridge, add the tag between the global
endpoints, compress the forest, suppress the internally covered mirror
conflict, apply the exact B cycle theorem, expand every path, and remove
the tag. Distinct terminals, an original pendant mate outside transferred
endpoints, and the already audited D-empty/tag boundaries prevent closed
components. No artificial completion, compressed or tagged edge survives.
The final global path preserves M and its prescribed u,v endpoints with
all new edges short. This is a universal matching statement per eligible
geometry, not evidence from a sampled matching.

## Independent full residual and witness replay

The new checker is `Q5_A8_CONSEQUENCES_REVIEW_check.py`, and its evidence
is `Q5_A8_CONSEQUENCES_REVIEW_check.json`. It does not execute or import
`ten_covered_after_full_A8.py`. The previously accepted domain is fixed as
three independent nine-byte-record binaries. Each is rehashed against
the accepted review and parsed with exact record count, uniqueness,
sorted original labels, parity, root/target exclusion, and Z--W independence.
No matching-feasibility or root-adjacency filter is added.

For every one of the 91225 original records the checker constructs all
six actual coordinate faces containing v and directly intersects each
face with Z,W. This differs from the producer's XOR count expression.
It collects all valid cuts rather than accepting a supplied chosen cut.
For bridge rows it also independently checks existence of eligible source
holes and that their mirrors are covered and distinct from the root.

The independently obtained covered-index set is compared to all 37003
producer witnesses. Every witness is unique, refers to exactly that
covered set, and its actual cut/counts are independently valid. The
producer's first-successful-cut convention is also checked. For every
uncovered record, its original nine bytes are retained in original input
order. The complete concatenation equals the producer's remaining file
byte for byte; unique record sets also agree exactly with the complement
of the covered-index set. Thus there are no omitted, duplicated or
relabelled inputs in either branch.

| Covered target v | Accepted input | Newly covered | Still OPEN |
|---:|---:|---:|---:|
| 1 | 26880 | 9960 | 16920 |
| 7 | 29955 | 12933 | 17022 |
| 31 | 34390 | 14110 | 20280 |
| Total | 91225 | 37003 | 54222 |

First-successful-cut row counts provide an additional witness checksum:

| Row | v=1 | v=7 | v=31 |
|---|---:|---:|---:|
| (0,1) | 0 | 0 | 0 |
| (1,1) | 3200 | 3336 | 3680 |
| (0,2) | 300 | 258 | 500 |
| (3,4) | 5810 | 8238 | 8790 |
| (4,4) | 90 | 270 | 270 |
| (3,5) | 560 | 831 | 870 |

Row (0,1) is valid but contributes zero additional records because K8
already covered it in the earlier accepted filtering. The other counts
are counts of normalized hole geometries in these fixed domains, not
numbers of matching instances or orbit counts. Coordinate/root
normalization and the earlier full 145248180-geometry census remain
explicit accepted imports; they are not claimed as rerun here.

## Verdict, counterexample attempts and limits

All new obligations pass: endpoint legality and shortness, all six row
applications, exact accepted input binding, every actual-cut witness,
both complete residual byte and set comparisons, and final hash stability.
Adversarial cases checked include an opposite-parity target that is free;
a covered target whose mate has the root's parity; long auxiliary edges;
an artificial target mate; a root represented by an even source; a bridge
that would mirror to u; a target crossing port; D empty; and a local bound
accidentally retained from the old endpoint import. The explicit matching
swap, source choices and accepted forest proof resolve them. No new gap
or counterexample was found within the stated scope.

Reproduce with `D:\anaconda\python.exe research\six_directions\Q5_A8_CONSEQUENCES_REVIEW_check.py`.
The report JSON binds all compared inputs and accepted direct dependencies.
Deterministic checks passed; semantic acceptance is same-family/provisional
relative to those imports. The remaining 54222 covered-target geometries
still require universal proofs for their realizing matchings. They are
open obligations rather than counterexamples. No full ten-hole, A10,
complete 12--18-hole layer, full Q6 or full P6 conclusion is accepted here.
