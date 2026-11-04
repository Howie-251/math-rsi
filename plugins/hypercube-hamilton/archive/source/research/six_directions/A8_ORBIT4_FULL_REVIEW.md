# Fourth A8 residual orbit: independent full-closure review

2026-11-01. Fresh reviewer `/root/a8_bridge_inputs_audit`, requested
GPT-6.1-sol/high. ARIS proof-checker method within the authorized scope.
`review_independence: same-family`; `acceptance_status: provisional`.

**PASS, relative to the stated Q4 imports and audited bridge criteria.**
The proof establishes the exact theorem for holes
`{0,1,2,4,15,23,27,29}`, omitted vertex `0`, and every arbitrary matching
of the other 24 vertices. The coordinate-permutation orbit has exactly
30 marked hole geometries. No new mathematical gap was found. Full A8,
full P6 and the original full Q6 question remain OPEN.

## Scope and dependencies

The reviewed assembly is `A8_ORBIT4_FULL_CLOSURE.md`. Its dependency DAG is
GQ4-avoid + exact Q4 T15/T63 classifications -> previously audited bridge
sufficient criteria -> four-cut coverage condition; independently, finite
allowed graphs -> complete matching domain -> explicit positive cycles.
These two branches jointly imply this orbit theorem. The earlier bridge
review and the exact current bytes of its theorem sources are pinned in
the JSON. The diagnostic typed spectrum is not used as an assumption.
No Q5 A8 conclusion or higher-layer theorem is imported.

The new independent checker is `A8_ORBIT4_FULL_REVIEW_check.py`, with evidence
in `A8_ORBIT4_FULL_REVIEW_check.json`. It imports neither the producer nor
the existing verifier. It reconstructs templates from the holes, rebuilds
all 16 allowed graphs, recursively enumerates matchings without memoized
producer counts, checks exact input-set equality and all positive cycles,
and generates the coordinate orbit. Both the semantic statements and the
binary input bytes have SHA-256 pins in the review JSON. Source hashes
were checked unchanged at the end. Production sources and the main state
were not modified.

| Obligation | Verdict | Evidence |
|---|---|---|
| Four valid face templates and actual marked Q4 obstructions | PASS | Direct reconstruction from H and face neighbors |
| Every uncovered input lies in the restricted graph family | PASS | Even terminal count and a terminal outside the OB pair |
| Sixteen disjoint mask domains | PASS | Exact mask, required-edge disjointness, explicit unset-edge absence |
| All empty domains | PASS | Four fixed-edge conflicts; nine odd-component obstructions |
| Complete finite domain | PASS | Independent set enumeration; 200475 distinct full matchings |
| Positive witnesses | PASS | All 200475 simple 31-cycles checked directly |
| Coordinate transfer | PASS | 30 images under all 120 coordinate permutations, all fixing 0 |
| Full A8 / P6 / original full Q6 | OPEN | Outside this theorem's scope |

## Four-cut hypotheses and exact Q4 obstruction identities

All holes have the required 5-even/3-odd pattern. Each nonzero even hole
15,23,27,29 has no short edge to any of 1,2,4, so the residual
nonadjacency hypothesis holds. Face A is the zero face and always contains
0. The following facts were independently derived rather than accepted
from the typed signatures:

| Bit | Minority A bridge sources | B mirrors Y | Singleton/common B vertex | Other neighbor(s) | Fixed OB edge |
|---:|---|---|---:|---|---|
| 2 | 1,4 | 3,6 | 2 | 10,18 | 10--18 |
| 4 | 1,2 | 5,6 | 4 | 12,20 | 12--20 |
| 8 | 1,2,4 | 9,10,12 | 8 | 24 | 8--24 |
| 16 | 1,2,4 | 17,18,20 | 16 | 24 | 16--24 |

For bits 2 and 4, A has two majority and two minority holes. Removing the
two chosen minority sources leaves two majority holes including 0. B has
one minority and three majority original holes; the two covered mirrors
produce the required 1+5 T15 pattern. The singleton's four in-face
neighbors are exactly the two omitted mirrors and the displayed pair.
For bits 8 and 16, A has two majority and three minority holes; deleting
the three sources again leaves two majority holes including 0. B has
three majority holes and the covered mirrors make the T63 six-hole
pattern. The displayed common neighbor is unique and its fourth neighbor
is 24. Thus these are the actual marked Q4 obstruction edges, not merely
unmarked geometric types. Every mirror and every obstruction endpoint
is originally covered. Original matching edges remain arbitrary.

## Coverage necessity without the diagnostic spectrum

Fix a template and suppose its fixed obstruction edge pq is absent from
the original matching. Put S=Y union {p,q}. If an original crossing edge
has its B endpoint outside S, that endpoint is a covered nonmirror
degree-one vertex of G and is a terminal rooted in T. If an internal
mirror's original mate lies outside S, that mate is a covered nonmirror
degree-one vertex of G, again a terminal rooted through the mirror's
bridge. In either case it is a terminal outside {p,q}. This uses no
assumption that an original edge is short.

The graph lemma gives R=|T|-2|P| rooted terminals. Here |T| is even:
the two double-bridge cuts have even c and |T|=c+2, while the triple-bridge
cuts have odd c and |T|=c+3. Thus R is even. Let e be 1 if both p and q
are rooted terminals, and 0 otherwise. For e=0 the additional terminal
gives R>=2>0; for e=1 it gives R>=4>2. Consequently
|T|/2>|P|+e, exactly the audited strict sufficient criterion. The root
edge, when needed, is a matching edge disjoint from P. The original fixed
edge is absent by the explicit premise, so its exclusion hypothesis also
holds. Therefore violation of either restricted condition proves this
matching extendable by that template.

Taking the contrapositive for all four templates proves that every input
not already covered satisfies each required restricted condition unless
its fixed edge is present. This is a necessary coverage condition only;
no converse is needed. In particular the restricted finite family may
contain inputs also solvable by a template. Certifying the entire family
still completes the proof. No Hamilton-search failure or diagnostic
classification is used to infer coverage.

## Exact 16-domain enumeration and empty-domain certificates

An input's mask is determined uniquely by which four actual fixed edges
it contains. For a set bit its edge is required. For an unset bit that
edge is explicitly forbidden, crossing B endpoints must lie in S, and
internal B edges meeting Y must remain inside S. All other edges are
allowed, including long and same-parity edges. These are exactly the
graph conditions used by the independent reconstruction. Every required
edge is also checked against all other applicable restrictions before its
endpoints are removed. Domains cannot overlap because their actual fixed
edge masks differ.

Masks 12,13,14,15 require both 8--24 and 16--24, contradicting that F is
a matching. For every other empty branch the rebuilt residual graph has
an odd connected component with no allowed outgoing edge. A perfect
matching would have to match that odd component internally, which is
impossible. One small explicit component per empty branch is:

| Mask | Odd component |
|---:|---|
| 0 | {7} |
| 1 | {28,30,31} |
| 2 | {26,30,31} |
| 4 | {22,30,31} |
| 5 | {21,22,28,30,31} |
| 6 | {19,22,26,30,31} |
| 8 | {14,30,31} |
| 9 | {13,14,28,30,31} |
| 10 | {11,14,26,30,31} |

The checker records all odd components and checks closure under every
allowed adjacency. Thus these are analytic empty-domain certificates,
not unexplained zero search counts.

The other three domains are independently enumerated by taking the least
remaining vertex, pairing it with each allowed remaining neighbor and
recursing. Every perfect matching has exactly one branch at each step,
so the recursion is exhaustive and duplicate-free. It imports no producer
code and reuses no producer counting cache. At each leaf the canonical
24-byte full matching must occur in the input-record set and is removed;
the set must be empty at the end. Every initial input record is also
checked to be a distinct canonical matching covering precisely Q5-H.

| Mask | Full original arbitrary matchings |
|---:|---:|
| 3 | 2025 |
| 7 | 99225 |
| 11 | 99225 |
| Total | 200475 |

Input binary size is 200475*24=4811400 bytes. Exact set equality, fixed
presences and unset absences all passed. This is complete domain
verification, not sampling or acceptance of a reported producer count.

## Positive cycle verification, expansion, and orbit transfer

The certificate binary has 200475*55=11026125 bytes. Every record's first
24 bytes equal the corresponding full matching input. Its remaining 31
bytes list each vertex 1 through 31 exactly once. The checker verifies
every required edge occurs between cyclic neighbors and every cyclic
edge outside the matching has XOR in {1,2,4,8,16}, including the closing
edge. Thus every record directly specifies one connected simple cycle
on Q5-0 containing all twelve original edges. Every finite-remainder
input has a positive witness; search exhaustion and producer unknown
counters play no role.

Inputs outside that remainder are covered by an audited bridge criterion,
whose forest/compression/expansion proof retains all original required
edges and restores every omitted mirror and every A-0 vertex. This closes
the logical union of the analytic and finite branches without assuming
that the finite branch is all possible arbitrary matchings.

All 120 coordinate permutations fix omitted vertex 0, preserve shortness,
and act on the entire arbitrary matching. Their images of H give exactly
30 distinct hole geometries. Hence the exact representative theorem
transports to the full fourth residual marked orbit. On the previously
reported accounting of 100 remaining geometries in four orbits, this
removes 30 and leaves 70 in three orbits. That accounting update is not a
proof of the other orbits or of full A8/P6/Q6.

## Checks and limitations

Adversarial checks addressed overlapping fixed edges; original long and
same-parity edges; mirrors that are crossing ports or are paired to each
other; e=0 versus e=1 and the parity needed for a strict inequality;
obstructions created by compression; distinct roots; unchanged omitted
vertex; forbidden-edge absences in every unset mask; duplicate/missing
records; and cycle closing-edge shortness. No mathematical counterexample
or open obligation was found within the exact theorem and its explicit
imports. The transitive Q4 import packages are not all re-audited here.

Reproduce with `D:\anaconda\python.exe research\six_directions\A8_ORBIT4_FULL_REVIEW_check.py`.
Deterministic matching/cycle checks passed. Semantic acceptance remains
same-family/provisional relative to the declared imports. No production
proof, main state, or original task-scope theorem was changed by this review.
