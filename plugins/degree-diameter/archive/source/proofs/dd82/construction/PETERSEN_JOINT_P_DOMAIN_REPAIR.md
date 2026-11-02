# Complete local Petersen choices still require compatible cross coverage

Date: 2026-10-12. One bounded matching repair reached **six nonempty
complete Petersen domains** while retaining \(F=0\). Choosing one actual
Petersen graph from each domain produced a complete 60-vertex,
240-edge, eight-regular graph, independently checked to have **307 bad
pairs**. One new unrestricted internal completion input was checked
UNSAT. Its failure has a short explicit explanation: the unique allowed
Petersen graph in fiber 3 forces four internal neighbors at vertex 1.

This completes the authorized repair chain. No further local score,
matching repair, or solver input was added after the failure.

## The complete-P construction mechanism

The input was the actual
[286-pair skeleton](../../../computations/dd82/construction/petersen_tight_row_repair_run/candidate.json).
Its five empty local domains were established by the complete
[allowed-Petersen diagnostic](PETERSEN_ALLOWED_PETERSEN_DOMAINS.md).

For each matching skeleton, form the allowed graph \(H_i\) by the proved
tight-row forbidden-edge rule. This episode minimized

\[
R=\sum_{i=0}^5\min_{P\in\mathcal P_{\rm all}}|E(P)\setminus E(H_i)|,
\]

where \(\mathcal P_{\rm all}\) contains all 30,240 labeled Petersen graphs.
The previous fixed-route condition \(F=0\) was a hard invariant.
Initially the six distances were \((1,2,0,1,1,2)\), so \(R=7\).

The full 45-bit catalog is generated once using the existing exact
transversal. For each encountered allowed graph, the program scans this
catalog to obtain the exact minimum and a complete Petersen minimizer.
Results are cached by the actual 45-bit allowed edge set. A scan can stop
at its first zero because zero is the exact minimum. At the final state,
each of the six full catalogs is scanned completely to count its domain.

A move swaps two images of one external matching. Only decreasing or
equal \(R\) moves are retained, using the existing deterministic level
search with no random restart. The declared limits were fifteen CPU
seconds, a 14.7-second internal stop, and 500 total stored states. Every
stored state on the returned path includes six actual complete Petersen
minimizers, rather than only six allowed graphs.

## Actual endpoint and complete graph

The single episode reached \(R=0\) in seven matching switches, six
strictly improving and one neutral. It checked 2,274 switches, expanded
seven states and stored twelve states. The endpoint has

\[
F=K=R=0,\qquad
(|\mathcal P_0|,\ldots,|\mathcal P_5|)=(4,4,121,1,3,2).
\]

There are 24 tight rows. The changed external interfaces are
\(01,04,05,15,24\). All six chosen internal graphs differ from the
source graph's internal graphs. Every path state was reconstructed in
Python; its external switch and \(F=0\) were checked, and its saved
internal masks were directly verified to have Petersen's degree and
common-neighbor properties. Their forbidden-edge count agrees with the
recorded score.

The complete endpoint's independent BFS found 60 vertices, 240 edges,
degree eight everywhere, diameter three and **307 bad pairs**. The saved
route energy is 352. The full graph, exact old-to-new edits, internal
edges by fiber, fifteen matching permutations and all bad pairs are
retained. It is not a target graph or an improvement of the old bad-pair
objective. What succeeded was the more specific construction step: six
complete internal Petersen choices simultaneously fit all tight-row
prohibitions of the same external skeleton.

## One new exact completion input

After \(R=0\) had been reached and the full graph had been checked, the
authorized new CNF allowed every one of the six internal graphs to vary.
It fixed only this endpoint's fifteen external matching interfaces.
There were no fixed internal edges or symmetry-breaking clauses.

The exact encoding uses 270 internal-edge variables, 9,720 exact-degree
clauses, 720 triangle prohibitions, 3,780 four-cycle prohibitions and 762
binary cross-coverage clauses: **14,982 clauses** in total. Its
candidate-preservation argument is unchanged from
[the exact internal completion encoding](PETERSEN_FIXED_ROUTE_REPAIR_AND_INTERNAL_COMPLETION.md).
Inserting the actual chosen internal graphs falsifies exactly the 307
coverage clauses corresponding to the saved BFS's 307 bad pairs.

The sole new CaDiCaL call returned UNSAT. Its 1,263-byte LRAT proof passed
one independent `lrat-trim --no-trim` check on the exact saved CNF. The
180-CPU-second, one-CPU, 8-GiB memory and 768-MiB proof limits were retained;
the actual solver CPU use was 0.009637 seconds.

## Explicit incompatibility of the nonempty local domains

The complete final catalog scan gives exactly one Petersen graph in
\(H_3\). Its fifteen edges are

\[
\begin{gathered}
30\!-!35,30\!-!37,30\!-!39,31\!-!34,31\!-!37,31\!-!38,\\
32\!-!35,32\!-!36,32\!-!38,33\!-!34,33\!-!36,33\!-!39,\\
34\!-!35,36\!-!37,38\!-!39.
\end{gathered}
\]

Every target with this external skeleton must therefore use this same
\(P_3\). In particular,

\[
N_{P_3}(33)=\{34,36,39\},\qquad
N_{P_3}(32)=\{35,36,38\}.
\]

Four actual binary cross-coverage clauses now force an impossible set of
internal edges in fiber 0:

| Cross pair | Required fiber-0 edge | Alternative fiber-3 edge, absent in the unique \(P_3\) | CNF clause |
|---|---|---|---:|
| \((1,38)\) | \(1\sim0\) | \(33\sim38\) | 14,332 |
| \((1,30)\) | \(1\sim4\) | \(33\sim30\) | 14,328 |
| \((1,37)\) | \(1\sim5\) | \(33\sim37\) | 14,331 |
| \((9,33)\) | \(1\sim9\) | \(32\sim33\) | 14,369 |

None of these four pairs has a fixed external route. For source 1 into
fiber 3 the five fixed endpoints, including multiplicity, are
\(33,35,31,35,32\); for source 9 they are
\(32,30,39,31,34\). The full intermediate vertex labels are recorded in
the witness file. These lists exclude the corresponding targets in the
table, leaving exactly the two internal alternatives shown.

The unique \(P_3\) makes the second alternative false in each row, forcing

\[
N_{P_0}(1)\supseteq\{0,4,5,9\},
\]

contrary to internal degree three. The other four internal fibers cannot
alter any route in this argument: their matching-to-matching paths are
already fixed, and a length-two path through such a fiber uses no internal
edge there.

This is a joint cross-fiber incompatibility despite every separate
Petersen domain being nonempty. Its extraction only read the completed
domain count, saved complete \(P_3\), actual matching edges and four saved
coverage clauses. It performed no new catalog scan, graph search or
solver call. The conclusion concerns this specific external skeleton;
it does not exclude arbitrary six-Petersen graphs.

## Files and measured resources

- [Repair source](../../../computations/dd82/construction/petersen_joint_p_domain_repair.cpp)
  and [launcher](../../../computations/dd82/construction/petersen_joint_p_domain_repair_run.py).
- [Exact path, all selected internal masks and domain counts](../../../computations/dd82/construction/petersen_joint_p_domain_repair_run/search.json),
  [resource record](../../../computations/dd82/construction/petersen_joint_p_domain_repair_run/resources.json).
- [Complete candidate and edits](../../../computations/dd82/construction/petersen_joint_p_domain_repair_run/candidate.json),
  [edge list](../../../computations/dd82/construction/petersen_joint_p_domain_repair_run/candidate.edges),
  [independent BFS and all bad pairs](../../../computations/dd82/construction/petersen_joint_p_domain_repair_run/candidate.verification.json),
  [all block diagnostics](../../../computations/dd82/construction/petersen_joint_p_domain_repair_run/candidate.diagnostic.json),
  [tight-row constraints](../../../computations/dd82/construction/petersen_joint_p_domain_repair_run/tight_row_constraints.json).
- [New completion encoder](../../../computations/dd82/construction/petersen_joint_p_domain_repair_completion.py),
  [encoding map](../../../computations/dd82/construction/petersen_joint_p_domain_repair_completion_run/encoding.json),
  [CNF](../../../computations/dd82/construction/petersen_joint_p_domain_repair_completion_run/input.cnf),
  [result](../../../computations/dd82/construction/petersen_joint_p_domain_repair_completion_run/result.json),
  [LRAT](../../../computations/dd82/construction/petersen_joint_p_domain_repair_completion_run/proof.lrat),
  [checker log](../../../computations/dd82/construction/petersen_joint_p_domain_repair_completion_run/certificate_check.log).
- [Four-clause witness extractor](../../../computations/dd82/construction/petersen_joint_p_domain_repair_conflict.py)
  and [actual witness](../../../computations/dd82/construction/petersen_joint_p_domain_repair_run/specific_conflict.json).

| Operation | CPU seconds | Wall seconds |
|---|---:|---:|
| One repair child, including the catalog | 0.090874 | 0.115431204 |
| Independent graph BFS child | 0.032317 | Included below |
| Repair launcher and path reconstruction | 0.022365745 | 0.172399905 including children |
| New CNF preparation | 0.037361319 | 0.040324528 |
| Sole new SAT call | 0.009637 | 0.079197880 |
| Sole independent LRAT check | 0.003515 | 0.004885573 |
| Read-only concrete conflict extraction | 0.002691524 | 0.003741469 |

The repair cached 2,212 actual allowed graphs and performed 61,811,328
catalog distance popcounts. All processes are finished. No shared wiki
or global checkpoint was edited, and this repair chain is stopped.
