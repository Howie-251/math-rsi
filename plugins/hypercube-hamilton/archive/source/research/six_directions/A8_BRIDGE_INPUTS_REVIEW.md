# A8 bridge inputs: fresh independent review

Date: 2026-11-01. Review agent: `/root/a8_bridge_inputs_audit`.
Requested reviewer setting: GPT-6.1-sol, high. Method: ARIS proof-checker,
with the user-authorized scope and named outputs. Assurance:
`review_independence: same-family`; `acceptance_status: provisional`.

## Verdict and scope

**PASS for the exact Q4 T63 classification. PASS for both stated sufficient
bridge criteria, relative to their explicitly imported Q4 theorems.** No
mathematical gap was found within these statements. Full A8 and the original
full Q6 question remain OPEN. This report neither audits nor promotes a
universal residual-orbit closure.

| Audited obligation | Verdict | Qualification |
|---|---|---|
| T63 marked-geometry normalization | PASS | Seven disjoint orbits cover all 560 even-parity geometries; odd parity follows by translation |
| T63 arbitrary matching domain | PASS | All 945 matchings per representative checked exactly once |
| T63 positive sufficiency | PASS | 6405 explicit simple 13-cycles checked independently |
| T63 negative necessity and completeness | PASS | All 210 negatives satisfy the proved degree obstruction; no search-failure premise |
| General bridge graph and proper-subset argument | PASS | Explicit path/endpoint and multigraph reasoning below |
| Double-bridge criterion | PASS relative to imports | GQ4-avoid and Q4 T15; fixed original obstruction remains excluded |
| Three-bridge criterion | PASS relative to imports | GQ4-avoid and the independently checked T63 |
| Fourth residual geometry, two-cut reduction | PASS | At least one cut has no fixed obstruction; the remaining small-crossing cases stay open |
| Every residual arbitrary matching satisfies some criterion | OPEN / not claimed | No exhaustive matching coverage for these Q5 criteria |
| Full A8 / full Q6 | OPEN / not proved | Neither follows from these local results |

The reviewed theorem-bearing sources are `A8_Q4_T63_CLASSIFICATION.md`,
`A8_DOUBLE_BRIDGE_SUFFICIENT.md`, and `A8_THREE_BRIDGE_SUFFICIENT.md`.
The report JSON pins SHA-256 hashes for these, the source definitions/import
statements actually read, the producer verifier/output inspected, manifest,
and all seven binary certificates. No production file or main ledger was
modified. The new independent checker writes only review evidence.

## Dependency and assumption ledger

The new dependency DAG is acyclic:

* T63: degree argument + complete marked-geometry coverage + positive cycle
  witnesses; it uses no Q5 extension theorem and no T15 theorem.
* Double bridge: residual assumption (I) + graph/forest lemma + GQ4-avoid +
  Q4 T15 classification.
* Three bridges: residual assumption (I) + graph/forest lemma + GQ4-avoid +
  T63. The two-cut reduction uses only this sufficient theorem and the
  incompatibility of two edges sharing vertex 24 in a matching.

The imported statements were read in `Q4_GENERAL_AUGMENTATION.md` and
`Q4_T15_CLASSIFICATION.md`. Their base certificate packages are not re-audited
here. Thus the bridge verdicts are expressly relative to these imports,
not fresh certification of all their transitive dependencies.

Symbols have consistent types: `F_A,F_B,C` are disjoint parts of the original
matching; `X_A,X_B` are its crossing endpoint sets; `H_A,H_B` are original
holes; `T` is a set of distinct A vertices; `P,J,D,S` are matchings on T,
with D perfect; `G` is the uncompressed graph; L is the final matching on B.
S and D must be treated as separately labelled edges when their endpoints
coincide. In particular the two-edge cycle at d=1 is a multigraph cycle.
No probabilistic, asymptotic, or interchange obligations arise.

## Independent finite verification of T63

The new checker `A8_BRIDGE_INPUTS_REVIEW_check.py` does not import the
producer or execute its search/verifier. It independently generates all
perfect matchings of the ten covered vertices and checks each decoded
matching for membership and uniqueness. Its orbit implementation permutes
bits and then translates, separately from the producer's transform code.
The exact union is compared with directly generated pairs (H,U).

| H | U | Orbit | Positive | Analytic negative |
|---|---|---:|---:|---:|
| 0,3,5,6,9,10 | 0,3,5 | 96 | 945 | 0 |
| 0,3,5,6,9,10 | 0,5,6 | 96 | 840 | 105 |
| 0,3,5,6,9,10 | 0,5,9 | 96 | 945 | 0 |
| 0,3,5,6,9,10 | 0,5,10 | 96 | 945 | 0 |
| 0,3,5,6,9,10 | 5,6,9 | 96 | 945 | 0 |
| 0,3,5,10,12,15 | 0,3,5 | 32 | 840 | 105 |
| 0,3,5,10,12,15 | 0,3,12 | 48 | 945 | 0 |

The output is `A8_BRIDGE_INPUTS_REVIEW_check.json`: 560 even geometries,
560 translated odd geometries, 6615 representative matching records,
6405 positive cycles, 210 analytic negatives. Every binary is exactly
945*29 bytes. No records are duplicated or omitted. For each positive record
the checker verifies 13 distinct vertices equal to Q4 minus U, the two
cyclic neighbors at every vertex, preservation of every required edge,
and shortness of every edge outside the required matching. Long edges and
same-parity required edges are permitted throughout.

For each negative, an opposite-parity covered vertex a has exactly one
short neighbor b outside U and the matching contains ab. The second cycle
edge incident to a would have to be a new short edge, but no distinct such
edge exists. This proves impossibility analytically. The only obstruction
edges in the two negative-bearing files are 4--12 and 1--9 respectively;
each occurs for exactly 7!!=105 matchings. Positive records have no such
obstruction. The necessity argument and the positive certificate cover
together establish the iff, independently of search completeness.

The parity-preserving group has 8*24 automorphisms. Its seven disjoint
orbits have sizes 96,96,96,96,96,32,48 summing to 560. Translation by an odd
vertex handles the opposite parity without changing adjacency, arbitrary
required edges, U, or the obstruction. This discharges the WLOG and
quantifier obligations for every arbitrary matching and every marked U.

## Bridge graph, compression, and obstruction control

For k=2 or 3 bridges let W be their distinct B mirrors. The added bridges
are new short edges: their A endpoints are distinct original holes. They
cannot duplicate edges of the original matching, even when a mirror is a
crossing port. Every vertex of T has degree one in G; each mirror has
degree two (one original required edge and its bridge); all other covered
B vertices have degree one. Original B holes are isolated. A cycle of G
would have to pass through a mirror, hence through its adjacent A leaf,
which is impossible. This proof does not assume original crossings are
short, that the two mirrors are unpaired, or that mirrors are internal
rather than ports.

A nontrivial G component has either two T endpoints, one T endpoint and
one B terminal, or two B endpoints. The first components define a matching
P on T; each contains a mirror, so |P|<=k. Terminal components have unique,
distinct roots, disjoint from endpoints of P. A two-B-endpoint component
is a single edge of F_B: a longer path would require an internal mirror,
whose bridge goes to an A leaf. This also settles the case where both
potential obstruction endpoints lie in the same G component: then their
edge is already an original F_B edge and is excluded by the fixed-edge
condition. Roots are never ambiguously assigned to a component with two
terminals and a T endpoint.

Since J is a matching on T, it extends to a perfect matching D. The strict
inequality d>|J| makes J a proper subset. Delete D from the GQ4-avoid
cycle K on A-v. Since D is a nonempty matching, all remaining components
are nonempty paths with endpoint set T; their contraction is S. S+D is
one alternating cycle, including the parallel-edge d=1 case. Restoring
any proper subset of its D edges cannot create a cycle. Hence S+J, and
in particular S+P, are forests.

Expanding S and attaching G therefore produces disjoint paths with
endpoints precisely the covered nonmirror vertices of B. Every A-v
vertex and every mirror is an interior vertex of exactly one such path;
every required edge belongs to exactly one path (or is a single-edge
path). Compression gives a genuine loop-free matching L. Its holes are
exactly H_B union W. There are no duplicated endpoints, lost components,
or suppressed original holes.

If two covered candidate obstruction endpoints are both terminals, their
distinct roots u,r are unused by P. Adding ur to J is therefore legal.
If compression paired those endpoints, S+P would contain a u--r path.
Together with the separately labelled ur edge it would form a cycle in
S+J, contradicting the proper-subset argument. This remains valid if the
path is one edge, when the forbidden cycle has two parallel edges. If
one endpoint is not a terminal, its component is a single original
F_B edge, so excluding the fixed obstruction suffices. These are all
possibilities; original edges may be arbitrary long edges.

The final B cycle contains L and omits exactly W. Replace each compressed
edge by its stored path, including single-edge paths when appropriate.
The paths have disjoint interiors and endpoints, and the omitted mirrors
occur only inside them. Thus the result is one simple cycle with exactly
Q5-v as vertex set, containing all F_A,F_B,C. Artificial D edges have
been removed, compressed edges have been expanded, original long edges
are retained, and every other introduced edge is short.

## Double-bridge hypothesis discharge

The hypotheses imply |H_B|=4 and |H_A|=4. The two mirrors have the same
parity by assumption 3; t,s have the opposite parity. If t,s are minority
holes, the A counts are (majority,minority)=(2,2), hence delta=0. If t,s
are majority holes, the counts are (4,0), hence delta=4. In both cases
removing t,s leaves precisely two majority holes including v. Consequently
F_A+D satisfies GQ4-avoid, c is even, and d=(c+2)/2. This T15 criterion
does not assert all possible delta-four cuts have its 1+5 B-hole pattern.

The singleton B hole a is original: mirrors belong to the five-hole
parity class. If both mirrors neighbor a, its other neighbors p,q are
not original holes. They have the mirrors' parity; residual (I) excludes
their being original holes, since a is in B and therefore is not v.
They are also distinct from the mirrors. Q4 T15's obstruction is exactly
pq in L. If a mirror is not adjacent to a, the obstruction is already
geometrically impossible. Otherwise pq not in F_B is explicitly required;
it cannot be dropped even for large c. The root-pair argument above
excludes newly compressed pq. All T15 hypotheses are now discharged.
Here |P|<=2, |J|<=3, so c>=6 implies d>=4>|J|, subject to the fixed-edge
condition. Smaller c are included whenever the actual strict criterion
holds; no claim is made when it fails.

## Three-bridge hypothesis discharge and fourth-orbit boundary

For delta=-1 as stated, A has two majority and three minority holes;
B has three majority holes. Each minority bridge mirror has majority
parity and is covered by residual (I). Then c is odd, d=(c+3)/2, and
F_A+D has exactly the two majority holes in A, including v. The GQ4-avoid
application is valid. L has six majority holes, with W the three avoided
holes, so T63 applies.

An opposite-parity vertex has a unique remaining neighbor outside W
exactly when it neighbors all three mirrors. There is at most one such
vertex: two distinct Q4 vertices have at most two common neighbors.
If it exists, a is a covered nonmirror vertex; its fourth neighbor b is
not a mirror. If b is an original hole, ab cannot lie in L. Otherwise
both endpoints are covered nonmirror vertices, the explicit fixed-edge
exclusion and root-pair argument eliminate ab. Thus every possible T63
obstruction, including one introduced by compression, is excluded.
Here |J|<=4; c>=7 yields d>=5>|J| whenever the required original-edge
exclusion holds. The criterion also covers any smaller-c instance that
actually satisfies the strict inequality.

The independent checker verifies the fourth residual geometry directly:
at bit 8 the mirrors are 9,10,12 with a=8,b=24; at bit 16 they are
17,18,20 with a=16,b=24. Both A faces have the stated 2+3 hole counts.
The two fixed edges 8--24 and 16--24 cannot both belong to a matching.
Therefore at least one cut has no fixed obstruction. If such a cut has
c>=7, the theorem applies. If both sufficient tests fail, at least one
cut has no fixed obstruction and c<=5 (c is odd). This does not imply
the other cut has no fixed obstruction, or that the small-c cut satisfies
d>|J|, or that the full orbit is closed. Those cases remain OPEN.

## Adversarial edge cases and reproduction

Checked structurally: arbitrary long original edges; mirror ports;
two mirrors paired by an original edge; obstruction endpoints in one
G component; obstruction endpoints in distinct terminal components;
an obstruction endpoint that is an original hole; no common neighbor;
d=1 and parallel contracted edges; and equality |J|=d. No counterexample
to a stated criterion was found. Equality was deliberately not accepted:
restoring all deleted edges can close a component. A fixed original
obstruction edge cannot be removed through root prescriptions.

Run `D:\anaconda\python.exe research\six_directions\A8_BRIDGE_INPUTS_REVIEW_check.py`
from the workspace. It is deterministic and verifies that all input
hashes stay unchanged during the run. Its output and this audit JSON
record the exact reviewed input bytes. Semantic acceptance remains
same-family/provisional; the deterministic certificate checks passed.
