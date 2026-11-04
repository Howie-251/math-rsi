# Independent audit of canonical A4 completion and gluing

Date: 2026-11-01. Reviewer requested: GPT-6.1-sol, high reasoning.
Review independence: same-family; semantic acceptance: provisional.
Final submission `CANONICAL_A4_CLOSURE.md` was read in full and checked
line by line. Deterministic finite checks: PASS. Mathematical gluing: PASS modulo the
explicit imported Q4 and hole-geometry results below. This does not prove
the full P6 statement at the 8--18-hole levels.

## Scope and independence

The new self-contained checker `CANONICAL_COMPLETION_REVIEW_check.py`
imports no generator, primary checker, or stored exception JSON. It reads
the two binary tables directly. It validates every positive cycle, proves
matching coverage by unique valid involutions and exact cardinality, and
independently enumerates all short complementary perfect matchings for
each negative. It then scans **all 2027025** near-perfect A-side inputs
forward, and enumerates all completions of every candidate stalled partial
forward. Thus the decisive universal endpoint property is checked without
using the producer's inverse-enumeration reasoning.

The checker completed successfully; its detailed output is
`CANONICAL_COMPLETION_REVIEW_check.json`.

## Explicit statement and symbols

Canonical input: an arbitrary complete-graph matching F on Q5, with holes
{0,1,14,22}; the desired simple circle covers every vertex except 1,
contains F, and uses only cube edges outside F. Cut the least significant
coordinate. Local labels x represent 2x+1 in A and 2x in B. Thus A has
hole 0 and B has holes 0,7,11. Write X_A,X_B for distinct crossing-port
sets and c for their common size. F_A,F_B are disjoint internal matchings.
Counting gives 2|F_A|+c=15, so c is positive odd.

For d in X_A, D pairs X_A minus d, and L=F_A+D has holes 0,d. For an
odd y different from d, put k=L(y) and T_y=L-yk+dk, a matching with
holes 0,y. A 14-cycle extending T_y avoids both holes. Delete dk and
append ky to obtain a spanning d--y path P in A minus 0 containing L.
The auxiliary edge dk cannot already be another edge of L: d was free.
Deleting its occurrence in the simple cycle yields a simple path, and y
was absent, so appending it introduces no repetition. This proves exactly
the path property used below.

The submission additionally asserts the converse. It is correct: since y
is an endpoint of a path containing L, its unique incident path edge must
be its prescribed L-edge yk. Remove y from the path and join its remaining
endpoints d,k by dk. These endpoints cannot already be adjacent in this
14-vertex simple path, so this gives a simple 14-cycle with every required
edge of T_y(L), and all other edges short.

## Finite obligations

1. All 135135 matchings for holes 0,1 are covered once. There are 135084
   positive witnesses and 51 negatives, of which 15 contain a half-layer
   and 36 do not.
2. All 135135 matchings for holes 0,7 are covered once. There are 135082
   positive witnesses and 53 negatives, of which 45 contain a half-layer
   and 8 do not.
3. For a negative, every extending 14-cycle would be F plus a disjoint
   short perfect matching, since F already gives degree one everywhere.
   The independent recursive enumeration covers all such short matchings
   and all resulting 2-factors have at least two components. This proves
   negative status rather than trusting a failed Hamilton search.
4. Coordinate permutations take holes 0,1 or 0,7 to 0,y for every odd y.
   The independent checker explicitly transports the mate involutions.
5. There are 15*13!!=2027025 near-perfect inputs (d,L). A direct forward
   scan finds exactly 256 for which neither y=7 nor y=11 works; the option
   y=d is declared unavailable, as required by the construction.
6. A partial F_A with c ports has exactly T=c(c-2)!! completions (d,D).
   For every stalled near-perfect L it contains, count the occurrence of
   F_A as a subset. The partial stalls precisely when this count is T:
   each completion is unique and occurs once in the forward scan.
7. The exact stalled-partial counts for c=1,3,5,7,9,11,13,15 are
   256,210,42,2,0,0,0,0. Their completion counts T are
   1,3,15,105,945,10395,135135,2027025.
8. For c=1 the good-endpoint cardinality distribution is
   {4:210,5:6,6:40}; for c=3 all 210 stalls have four good odd endpoints.
9. Every c=5 or c=7 stall has exactly four good odd endpoints G, disjoint
   from X_A. For each y in G, **every** one of its T completions works.
   This stronger quantifier is essential in choosing d from a B port's
   actual original crossing partner.
10. The two c=7 partials are exactly
    H1={(2,3),(4,5),(8,9),(14,15)} and
    H2={(1,3),(4,6),(8,10),(13,15)}. Every c=5 partial contains exactly one
    of these cores. There are 21 choices of its extra edge per core.

All ten finite obligations PASS deterministically. No conclusion about
Q5 counterexamples is inferred from a Q4 negative.

Every candidate-partial count in the submission's table was independently
checked as well: 256,1372,3048,3596,2366,808,84,1, respectively.

## Safe endpoint transfer: y outside X_B

Choose a good completion and its d--y path P. Delete D, attach every
original crossing edge and the short mirror bridge y_A y_B. Every new
B endpoint is in X_B union {y}, a set of c+1 distinct vertices. The
result is a family of disjoint B-to-B paths whose internal vertices
partition A minus 0. If y belongs to X_A, its D edge was the final edge
of P, and deleting D leaves y isolated. Its original crossing edge and
the new bridge give a two-edge segment through y with distinct endpoints
in B; this is valid and loses no original matching edge. Other deleted
D endpoints receive their original crossing edge; the root d receives
its original crossing edge; an internally covered y receives its bridge.
No component can close because B attachments are distinct degree-one
endpoints. Compression therefore gives a matching R on X_B union {y}.

If y is 7 or 11, F_B+R has holes 0 and the other of 7,11, hence opposite
parity. NC_4 gives a full B circle; expansion gives the required circle.

Otherwise y is an odd non-hole outside X_B and is internally matched by
F_B. Put k=F_B(y), r=R(y). The vertices y,k,r are distinct, k is not a
port and r is a port. Then
L_B=(F_B-yk)+(R-yr)+kr
is a matching with precisely the holes 0,7,11,y. Apply A4_4 avoiding y.
Expand kr into k--y followed by the transferred y--r path, and expand
all other compressed edges. This restores y, F_B's edge ky, and every
A vertex other than 0 exactly once. All retained auxiliary edges are
expanded; the only new crossing bridge is short.

## Occupied endpoint transfer: y in X_B

This case is used only for c=5 or c=7 stalled partials. Pick y in G and
take d to be the actual A endpoint of F's crossing edge incident to y_B.
Because G is disjoint from X_A, y_A is internally covered by F_A, and
d differs from y_A. Pair X_A minus d arbitrarily to obtain D. Universal
availability in obligation 9 yields P for **this** d and D. Since c>=5,
D is nonempty, and no D edge touches either endpoint of P. Deleting D
separates d and y_A into different components: a path has a unique route
between its endpoints and every D edge lies on that route.

Attach the original crossing edges and the mirror bridge y_A y_B.
Only the original d--y_B crossing and the new y_A--y_B bridge share a
B vertex. Their two A segments were distinct, so joining them at y_B
concatenates paths instead of creating a cycle. All other B ends are
the distinct vertices X_B minus {y}. Thus compression is a matching R
on X_B minus {y}, and its disjoint interiors partition (A minus 0)
union {y_B}. F_B+R is a matching with exactly the holes 0,7,11,y. These
are distinct because X_B contains none of B's original holes. All three
nonzero holes are odd. A4_4 gives a B circle avoiding y, and expanding
R restores the internal y_B and all of A minus 0, proving the desired
31-vertex circle. Both edges at y_B are restored, including its original
F edge. The new mirror bridge is distinct from that original edge since
d differs from y_A.

## Complete case partition and imports

If F_A is not stalled, choose y=7 or 11, both outside X_B, and apply
the safe transfer. A stalled c=1 or c=3 partial has at least four good
odd endpoints but at most three B ports, so one is outside X_B. A stalled
c=5 or c=7 partial either has y in G outside X_B, handled safely, or has
G contained in X_B, handled by the occupied transfer. There are no
stalled partials at larger c. The partition includes all positive odd c.

Consequently the canonical A4 family is proved modulo Q4 inputs NC_4,
A4_4 and the finite checks above. Importing R1A from
`A4_SINGLE_GEOMETRY_REDUCTION.md` proves full Q5 A4, conditional only on
its already specified Q5 N14, Q4, and optional-edge-spectrum imports.
These imports were read as explicit inputs and were not silently replaced
by an assumption of A4. There is no circular dependency: the Q4 proofs
precede and do not use Q5 A4; R1A leaves this canonical case open.

The earlier full-six-hole reductions can now discharge their A4 hypothesis.
Their independent acceptance is an import, not a fresh audit of every
six-hole lemma here. The theorem still says nothing new about the
8--18-hole levels, so a conclusion of full P6 would remain unjustified.

The pre-gluing unresolved full-matching counts are independently confirmed
as 42*9*105*120=4762800 at c=5 and
2*binomial(9,3)*15*5040=12700800 at c=7. They are unnecessary for the
proof, since the occupied-endpoint construction covers these families
universally without enumerating all original matchings.

## Final obligation ledger

The following application checks were made against the submitted proof:

| Obligation | Discharge |
|---|---|
| arbitrary original long/same-parity edges | all enumerations use arbitrary pairings; short restrictions apply only to new edges |
| every 3:1 four-hole geometry | imported R1A; canonical proof has no additional restriction on F |
| all crossing counts | counting gives exactly positive odd c<=13; all are covered |
| endpoint target y distinct from root | enforced in the table criterion and every enumerated completion |
| prescribed-root occupied transfer | universal availability, rather than existential availability, established directly |
| A4_4 hole parity and distinctness | holes 0,7,11,y; y odd and outside {0,7,11} in both uses |
| NC_4 hypothesis | exactly two opposite-parity B holes in its use |
| F edges restored | F_A retained in segments; C attached in full; F_B swap edge restored on expansion |
| all vertices once and connectivity | disjoint path interiors and expansion of one simple B circle |
| newly added edges short | local table and Q4 witnesses, plus one mirror bridge; all other auxiliary edges deleted or expanded |
| full six-hole consequence | C6-covered and C6-free explicitly have A4 as their remaining hypothesis, with prior inputs; their cases cover covered and free targets |
| full P6 scope | 8--18-hole obligations explicitly excluded |

The six-hole dependency audit read `SIX_HOLE_FOUR_AUX_REDUCTION.md`,
`SIX_HOLE_MIXED_AND_GEOMETRY.md`, `SIX_HOLE_COVERED_REDUCTION.md`, and
`SIX_HOLE_FREE_REDUCTION.md`. Their dependency arrows run from A4 to K4
and the six-hole transfer theorems; none is invoked to prove A4 here.
Thus the final consequence is a valid discharge of a previously conditional
result, modulo its stated earlier theorems, with no dependency cycle.

Adversarial checks specifically considered c=1 with D empty, a target
isolated by deletion of D, a long original crossing edge at the occupied
target, collisions between mirror bridge and original crossing edge,
and a possible closed component at the shared B port. The hypotheses
above exclude each failure. No fatal, critical, major, or minor issue was
found in the final submission. Verdict: **PASS modulo explicit imports**;
semantic acceptance remains same-family/provisional.
