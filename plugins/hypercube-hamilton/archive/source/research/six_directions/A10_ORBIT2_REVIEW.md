# A10 second marked orbit: independent proof and certificate review

Date: 2026-11-01. Reviewer: `/root/a10_first_orbit_audit`, a fresh independent
reviewer for the supplied candidate. User-requested GPT-6.1-sol, high;
ARIS proof-checker. `review_independence: same-family`;
`acceptance_status: provisional`.

## Scope and verdict

**PASS, relative to the declared certified Q4 inputs.** All semantic proof
obligations and all 2,366,577 explicit positive cycles pass. The input is
`A10_ORBIT2_REDUCTION.md` with its frozen manifest, canonical domain, and
three positive witness files. This is only the marked coordinate orbit of
size 20 with holes `{0,3,5,6,8,15,23,25,26,28}` and forbidden hole 0.

The quantified theorem is: for every complete-graph matching F on the 32 Q5
vertices with exactly these ten holes, there exists a simple cycle with
vertex set exactly `{1,...,31}` containing every edge of F; every edge of
that cycle outside F has Hamming distance one. Required edges are arbitrary,
including long edges and equal-parity endpoints. Apply the same statement
to each of the 20 coordinate-permuted marked geometries.

This review does not assert full A10 or Q6 P6. After the first 30-geometry
orbit and this 20-geometry orbit, the separate remaining 5-geometry orbit
still needs proof. No production file or main progress ledger is modified.
Same-family provisional assurance does not represent a mathematical gap.

## Dependency and hypothesis accounting

The dependency DAG is acyclic:
Q4 GQ4-avoid + Q4 exact T15 -> four-candidate bridge rule -> no-cycle implies
C closed -> exact C/D matching domain -> coordinate/stabilizer quotient ->
positive cycle witnesses -> all exceptional matchings -> marked orbit.

The imported Q4 statements were inspected directly and their use was checked
in the earlier independent first-orbit review. The current candidate repeats
the bridge derivation, so no conclusion about other Q5 A10 orbits is needed.
Neither full A8 nor any P6 claim is a premise. Q4 existence inputs are
explicit imports; their complete transitive certificates are not re-audited
in this invocation. No probabilistic, asymptotic, or limit-interchange
obligations arise.

F_A,F_B,C_cross partition the original matching; X_A,X_B are crossing endpoint
sets. T consists of crossing A endpoints and two original A holes. P,J,D,Q
are matchings on T, D perfect. C is the fixed covered eight-set, distinct
from C_cross; the later D is the fourteen-vertex complementary set. These
uses of D occur in separate proof steps and are unambiguous from their types.
The two ordinary uses can instead be called D_port and D_vertices if desired;
no inference depends on conflating them. Terminals are endpoints of G
components meeting T, not endpoints of unrelated internal F_B edges.

| Obligation | Independent discharge |
|---|---|
| Original domain | Exactly 22 covered vertices, hence eleven required edges; their lengths and endpoint parities are unrestricted |
| Cut geometry | At bit 16: A holes 5 majority + 1 minority; B holes singleton 23 + minority 25,26,28 |
| All four candidates | M={19,21,22,31} is covered and is both the four mirror set and the face-neighbor set of 23 |
| Short bridges | Their A endpoints are distinct original holes, so new mirror edges cannot duplicate original crossing edges |
| Path forest and roots | Every T vertex has degree one; each possible degree-two B mirror has a bridge to an A leaf |
| Parity and strictness | c even from 2|F_A|+c=10; r=2d-2|P| even; outside terminal gives r>2e, so |J|<d |
| Artificial pairing legality | Root edges use distinct endpoints unused by P; J extends to perfect D_port disjoint from F_A |
| GQ4 application | F_A+D_port holes are three majority and one minority, with specified majority hole 0 still free |
| No premature cycles | Q+D_port is one labelled alternating cycle; restoring any proper subset J gives a forest |
| Compressed matching | Disjoint paths cover all A minus 0 and selected mirrors internally; endpoints are covered nonmirror B vertices |
| T15 obstruction excluded | Original pq edge is explicitly excluded; a newly compressed pq would close Q+J via the prescribed root edge |
| Expansion | Simple cycle, exact omitted vertex, all eleven original edges survive, and every other edge is short |
| Six choices quantified | At most two fixed complementary edges; each candidate belongs to at least two nonfixed choices |
| Closed-set consequence | Port restriction follows from one nonfixed choice, internal-partner restriction separately for every candidate |
| Exact exceptional domain | C and D_vertices partition the covered vertices; a C-closed matching is uniquely a perfect matching on each |
| Stabilizer coverage | All 120 coordinate permutations yield orbit size 20 and full geometry stabilizer of order 6; it preserves C,D_vertices |
| Canonical quotient | First minimize C under S3, then minimize D_vertices under that representative's stabilizer; no two representatives share a full orbit |
| Saved domain exactness | Independent complete set construction of C and D matchings reconstructs every byte of the saved domain |
| Witness coverage and validity | Exact contiguous intervals, matching bytes aligned to domain, exact 31-vertex support, all required edges and short-only added edges |
| Transport and statement match | Stabilizer and coordinate maps preserve arbitrary matching edges, shortness, 0, simplicity, and complete vertex support |

## Analytic adversarial review

Steps 1--3 use the same general sufficient bridge rule as the first-orbit
proof, with independently checked new geometry. The bridge mirrors need not
be internal: a mirror that is an original crossing port produces a valid
T--T path. A mirror's original partner is never assumed to be its mirror.
Long crossings and long internal required edges do not affect the degree
or component arguments.

For strictness, if both obstruction endpoints p,q are rooted terminals,
their roots are distinct and unused by P. A terminal outside {p,q} forces
at least three terminal roots, hence at least four by parity. Otherwise at
least one terminal forces at least two. Thus the prescribed root edge, if
present, still leaves J a proper subset of D_port. Equality is not accepted
as a successful case. The contracted objects must be multigraphs: coincident
Q and D_port edges are separately labelled, including a two-edge cycle
when d=1. A proper subset breaks even that cycle.

An unrelated B--B component of G is a single original F_B edge. A longer
one would pass through a selected mirror, whose bridge leads to an A leaf.
If pq is compressed from two rooted components, their root-to-root path
in Q+P together with the extra edge of J would form a cycle in Q+J. This
excludes the only T15 obstruction before applying that theorem. Compression
and expansion restore all A vertices except 0 and both selected mirrors
exactly once; artificial pairing and compressed edges do not survive as
new long edges in the final cycle.

Under global nonexistence, every nonfixed bridge pair obeys the failure
constraints. A matching on the four candidates can contain two disjoint
fixed obstruction edges, but for any particular candidate x the three
bridge pairs selecting x have complementary edges on the other three
vertices. At most one of those three edges is fixed. Hence every x is
selected in a nonfixed pair. Ports outside M are forbidden by any nonfixed
pair, and internal partners of each x outside M are forbidden by a pair
selecting x. Therefore every other covered B vertex is internally matched
outside M. That set is exactly C={16,17,18,20,24,27,29,30}.

Consequently nonclosed C already gives the desired global cycle by
contraposition. Closed C is exactly the union-of-two-perfect-matchings
domain, not an extra unproved assumption imposed on all F. Its size is
105*135135=14,189,175. The independent positive certificates address all
orbits of this exceptional domain.

The template failures in the final explanatory section are also correct.
For bit 8, each of the four possible three-mirror choices leaves the free
singleton 15 with one available short face neighbor. For bits 1,2,4 the
specified triples similarly leave the original holes 25,26,28 with one
neighbor. A free cycle vertex needs two distinct incident new short edges.
This rules out only those templates and does not rule out the original
global theorem. In particular no T63 input is inferred from a T17 pattern.

## Independent canonical-domain reconstruction

`A10_ORBIT2_REVIEW_check.py` imports no producer and no previous verifier.
It generates every perfect matching using an explicit stack of partial
states, rather than invoking the C++ recursion. It checks uniqueness and
the exact counts 105 on C and 135135 on D_vertices. All six geometry
stabilizers are regenerated from all 120 coordinate permutations. Taking
the minimum image of every C matching gives exactly 23 representatives.

For each C representative its stabilizer G_C is independently found. The
checker takes *every* D matching, computes its least image under G_C, and
forms the exact set of all those minima. It orders that set by the stated
matching enumeration order and reconstructs the actual 22-byte records.
Every reconstructed block is compared with the corresponding frozen bytes;
the final offset must equal the entire file size. This proves no omitted
representative, no repeated representative, no extra record, no changed
matching byte, and the stated order. It does not merely compare weighted
totals or accept a Burnside count as coverage.

All 23 blocks agree. Their C-stabilizer sizes are 1,2,3,6 and their D
canonical counts respectively 135135,67755,45063,22719. Their concatenation
is exactly 2,366,577 records and 52,064,694 bytes, with the manifest hash
`f75459b8203101f4001f34855c80cff46a53cb63ccaff6666b87fb90215129c9`.
Per-block counts and weighted counts independently agree with the producer
count file. As a separate corroboration, fixed-point counts for the six
maps are (105,135135), three copies of (9,375), and two copies of (3,27).
Burnside yields 2,366,577; the full-orbit weighted count is 14,189,175.

The producer source was inspected: its least-unpaired-vertex recursion,
edge normalization, canonical C test, exact representative stabilizer test,
and binary pair order implement precisely the stated quotient. Independence
of the new implementation comes from rebuilding the entire domain through
canonicalized sets and comparing its bytes, rather than trusting this
inspection or the original geometry checker.

## Independent positive-cycle verification

For each of all 2,366,577 records, the checker compares the first 22 bytes
with its indexed frozen input, verifies the remaining 31 bytes are exactly
the distinct vertices 1 through 31, builds cyclic neighbor sets, and checks
every required pair is a cycle edge. It also checks every nonshort cyclic
edge is one of the recorded required edges. This validates long required
edges directly and never demands that required edges be short. Exact chunk
sizes and offsets give contiguous full coverage with no overlap or tail.

| Chunk start | Records | Record bytes |
|---:|---:|---:|
| 0 | 800000 | 53 |
| 800000 | 800000 | 53 |
| 1600000 | 766577 | 53 |

No search is performed, no sample is substituted for full verification,
and no producer summary or root verifier PASS is used as the existence
proof. Each explicit valid cycle itself proves the corresponding positive
instance. The group argument transports these witnesses to every closed-C
matching. The analytic reduction supplies every other matching.

The checker verifies every frozen manifest entry's size/hash, includes the
manifest and direct proof imports in its own hash ledger, and rehashes all
17 declared inputs after checking. It writes only its own review evidence.
Command: `D:\anaconda\python.exe research\six_directions\A10_ORBIT2_REVIEW_check.py`.
Final execution results, input hashes, per-block counts, and per-chunk
positive counts are in `A10_ORBIT2_REVIEW_check.json` and the accompanying
review JSON. The independent process exited with code 0 and status PASS:
all three chunks passed and all 17 input hashes stayed unchanged. Open
FATAL/CRITICAL/MAJOR/MINOR issues: zero. No mathematical fixes or strengthened
hypotheses are needed. Only this marked 20-geometry orbit is closed here;
full A10 and P6 remain OPEN.
