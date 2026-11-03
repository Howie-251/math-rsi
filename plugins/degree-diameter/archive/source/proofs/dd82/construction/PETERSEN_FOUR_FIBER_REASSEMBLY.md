# A synchronous four-fiber reassembly with an exact route partition

Date: 2026-10-12. This experiment changes an interface in the shared
forty-vertex core and simultaneously reconstructs two routes between the
former twin fibers. It is distinct from the earlier experiment fixing the
entire forty-vertex core, the fixed-root SAT input, and the single-switch
annealing searches. Its one exact assembly call returned **RAW_UNSAT** in
0.027937 CPU seconds. No solver proof was written or checked. The subsequent
short boundary-rigidity argument below proves the impossibility of changing
the core matching in this scope, independently of that solver result. This
does not exclude all six-Petersen graphs.

## The new finite assembly problem

Start from the saved twenty-bad-pair graph, with Petersen fibers
\(F_0,\ldots,F_5\). Release all six matching interfaces induced by the four
fibers \(\{0,1,4,5\}\):

\[
01,\quad04,\quad05,\quad14,\quad15,\quad45.
\]

Each released matching is an arbitrary permutation, independently of the
others. Keep the other nine matchings and all six internal Petersen graphs
fixed. Require \(M_{01}\) to differ from its original value. This last
requirement defines the new construction scope; it is not asserted as a
necessary condition on every possible six-Petersen target.

The former five-interface repair fixed \(01\), and the former nine-interface
repair kept all six matchings inside \(F_0\cup\cdots\cup F_3\). Neither was
this six-interface problem. There is no random restart or graph-neighborhood
optimization in the present experiment.

## The pair budget forces an exact partition

Use row-source matching matrices. In the original seed all four routes
from \(F_4\) through \(F_a\) to \(F_5\), \(a=0,1,2,3\), give the same
permutation \(\Phi\). In actual vertex labels its images of 40,...,49 are

\[
(55,50,51,56,58,57,54,52,59,53).
\]

The present scope keeps the two routes through fibers 2 and 3 fixed. Write
\(Q_0=M_{40}M_{05}\) and \(Q_1=M_{41}M_{15}\). Let \(P_i\) be the
Petersen adjacency matrix in fiber \(i\). The complete 4-to-5 route matrix is

\[
C_{45}=M_{45}+P_4M_{45}+M_{45}P_5+Q_0+Q_1+2\Phi.
\]

Every row has eleven route slots. If all ten targets are covered, exactly
one target in each row receives a second route and all others receive one.
The two copies of \(\Phi\) already use that repetition. Consequently every
target in this assembly scope necessarily satisfies

\[
\boxed{M_{45}+P_4M_{45}+M_{45}P_5+Q_0+Q_1=J-\Phi.}\tag{1}
\]

In particular \(Q_0,Q_1\) both avoid \(\Phi\) at every row, and they avoid
each other at every row. All seven direct/internal routes are disjoint and
avoid these three permutation images. This is an exact joint assembly
condition, not a heuristic score.

In the notation of
[the pair-cycle budget](PETERSEN_PAIR_CYCLE_BUDGET.md), the two unchanged
channels already contribute \(c_{45\mid23}=10\). Every additional
four-fiber contribution is nonnegative, while a target requires
\(c_{45}=r_{45}\le10\). Thus this scope forces
\(c_{45}=r_{45}=10\), with \(q_{45}=t_{45}=a_{45}=0\), and all the other
\(c_{45\mid ab}\) zero. Equation (1) is the entrywise version of this
budget. More generally, retaining three of the original identical channels
would already give \(c_{45}\ge30\), making completion impossible. At least
two of the four actual route permutations must therefore be reconstructed;
altering \(M_{45}\) or a core interface \(M_{ab}\) alone does not change
these four routes.

## An actual complete seed realizing the new partition

Keep the original \(M_{45}\) temporarily. Its seven direct/internal
targets in each row are distinct and avoid \(\Phi\). The remaining matrix

\[
R=J-\Phi-M_{45}-P_4M_{45}-M_{45}P_5
\]

is a simple two-regular bipartite graph. A deterministic perfect matching
\(Q_0\) in it leaves a second perfect matching \(Q_1=R-Q_0\).
Retain the original \(M_{40},M_{41}\), and define \(M_{05},M_{15}\) by
\(M_{4a}M_{a5}=Q_a\). Finally transpose the images of vertices 0 and 1 in
the original \(M_{01}\). This changes the old core while preserving every
required degree and matching. There is no optimization in these choices.

The expanded seed has 60 vertices, 240 edges, and degree eight everywhere.
It replaces 22 edges by 22 edges. Independent BFS finds **97 bad pairs**,
all at distance three. Its total pair energy is 118. Crucially the 4--5
block now has zero bad pairs and zero energy, with route multiplicities
\(1^{90},2^{10}\), whereas its old energy was 50. None of the six graphs
obtained by omitting a fiber is HS50. Thus this seed does break both old
HS cores and solves the intended local route obligation, but it is a
failed full construction: the deficit has moved to other blocks.

| Block(s) | Bad pairs per block | Energy per block |
|---|---:|---:|
| 01 | 8 | 8 |
| 02,03,12,13 | 2 | 2 |
| 04,14 | 2 | 3 |
| 05 | 28 | 35 |
| 15 | 19 | 25 |
| 25,35 | 15 | 18 |
| 23,24,34,45 | 0 | 0 |

The seed edge list, exact edit trace, all 97 BFS witnesses, and every block
route histogram are saved. No nonzero bad-pair count is a successful target.

## Exact encoding and the single bounded call

There are 600 edge variables, one for each possible edge of each released
matching. Exactly-one row and column constraints impose a perfect matching
in each interface. A single clause excludes retaining all ten original
\(01\) edges.

For every unordered vertex pair without a fixed direct edge or fixed
two-edge route, a coverage clause is formed from every possible direct or
two-edge route. A route with one fixed edge contributes its other edge
variable. A route with two variable edges contributes a cached variable
defined by an equivalence to their conjunction. This encoding uses the
actual fixed edge set and covers all types of vertex pairs; it does not
assume an HS completion.

Equation (1) is then imposed explicitly. For each \((u,v)\in F_4\times F_5\)
there are 27 possible variable route indicators: one direct edge, six
routes using an internal Petersen edge, and twenty routes through fibers
0 and 1. For \(v=\Phi(u)\), every indicator is false. Otherwise exactly
one is true. Matching constraints ensure each middle fiber contributes
exactly one actual route per row, so these are precisely the entries of
(1). They preserve every target in the stated six-interface scope.

The actual input has 10,600 variables and 68,121 clauses, including 10,000
route-conjunction variables, 650 coverage clauses, and 32,550 additional
clauses while installing the exact 4--5 partition (including newly needed
conjunction definitions). CaDiCaL, pinned to one CPU and limited to 45 CPU
seconds and 4 GiB, returned exit code 20 after 0.027937 child CPU seconds
and 0.135808334 wall seconds. It was a construction call without a proof
file; therefore the status remains **RAW_UNSAT**. No second call or proof
replay was started.

Preparation consumed 0.102207979 parent CPU seconds and 0.030948 independent
BFS child CPU seconds, with 0.156777978 wall seconds. All calls finished.
The experiment does not establish a lower bound or close the general
six-Petersen model. It identifies the exact simultaneous two-channel
obligation, produces a graph satisfying that obligation, and records the
failure of the specified joint assembly input to yield a full target. The
following analytic argument subsequently explains this failure.

## Boundary rigidity forces the old core matching

**Proposition.** In the stated six-interface assembly domain, covering just
the vertex pairs from \(F_0\) to \(F_2\cup F_3\) already forces
\(M_{01}\) to equal its original value. Consequently the imposed genuine
core change is impossible, without using (1), the SAT result, or any
unexamined matching enumeration.

**Proof.** For a vertex \(v\) in fiber 1, 4, or 5, define its *boundary
signature* to be its ordered pair of neighbors in \(F_2,F_3\). All these
neighbors are fixed in this assembly domain. Since the interfaces are
perfect matchings, each fiber's ten signatures form the graph of a
bijection between the two boundary fibers. Let \(\Sigma\) be the curve
for fiber 1 and \(\Pi\) the curve for fiber 4.

The original twin relation makes the fiber-5 signature curve equal to
\(\Pi\). Also \(\Sigma\cap\Pi=\varnothing\): otherwise a pair of boundary
vertices would have a common neighbor in both fibers 1 and 4, giving a
four-cycle inside the original HS50 obtained by omitting fiber 5.

Fix \(u\in F_0\). In each boundary fiber the fixed direct and two-edge
routes give exactly eight distinct targets: one direct route, three using
an internal edge of \(F_0\), three using an internal edge of the target
fiber, and one via the other boundary fiber. These eight routes belong to
the original HS50. Its two additional routes via fibers 1 and 4 are
distinct and fill the two missing targets.

Write the signature of the original fiber-4 neighbor as
\(p=(a,c)\in\Pi\), and that of the original fiber-1 neighbor as
\(q=(b,d)\in\Sigma\). Thus \(a\ne b,c\ne d\), and the still-missing
boundary targets are \(\{a,b\}\) in fiber 2 and \(\{c,d\}\) in fiber 3.
In a new assembly, let the signatures of the three new neighbors of \(u\)
in fibers 1,4,5 be respectively

\[
Q\in\Sigma,\qquad R,S\in\Pi.
\]

These three routes must cover both missing targets in each coordinate.
Suppose \(Q\ne q\). Because \(\Sigma\) is a bijection curve and contains
\((b,d)\), the first coordinate of \(Q\) cannot be \(b\), and its second
coordinate cannot be \(d\). Therefore \(R,S\) must supply first coordinate
\(b\) and second coordinate \(d\). They cannot do this with the same
point, because \((b,d)=q\notin\Pi\). Hence both points are used, one for
each coordinate. Neither can be \(p=(a,c)\), because \(a\ne b,c\ne d\).
As \(\Pi\) is also a bijection curve, neither can then supply first
coordinate \(a\) or second coordinate \(c\). Both remaining targets must
be supplied by \(Q\), forcing \(Q=(a,c)=p\), contrary to
\(\Sigma\cap\Pi=\varnothing\).

Thus \(Q=q\). A vertex's boundary signature is injective within its fiber,
so the fiber-1 neighbor of \(u\) is the original one. This holds for every
\(u\in F_0\), proving the proposition. Moreover, now \(Q=q\) covers neither
\(a\) nor \(c\); at least one of \(R,S\) must be the original twin
signature \(p\). \(\square\)

This proof uses only the double-HS seed relations and fixed boundary
interfaces, so the same statement holds for any chosen core pair
\(a,b\in\{0,1,2,3\}\): retaining the other nine interfaces while releasing
the six on \(\{a,b,4,5\}\) forces the old \(M_{ab}\), provided boundary
coverage is required. This is a relabeling of the proof, not a claim of six
additional solver runs. It gives a concrete next-construction requirement:
to change \(01\), one must also alter at least one of

\[
02,03,12,13,23,24,25,34,35
\]

or leave the fixed Petersen-fiber model. Reconstructing just the chosen
four-fiber module cannot change its old core interface while maintaining
the necessary boundary coverage. This is stronger failure localization
than the raw solver status and does not turn the failed 97-pair seed into
a valid construction.

The [small actual-row witness source](../../../computations/dd82/construction/petersen_four_fiber_boundary_witness.py)
read the saved graph and checked the two signature curves, their
disjointness, and all ten eight-route rows directly. Its
[output](../../../computations/dd82/construction/petersen_four_fiber_reassembly_run/boundary_rigidity.json)
contains every signature and fixed route count. It took 0.000730616 CPU
seconds, without a SAT call, matching search, or BFS replay. The proof
above supplies the universal implication; these actual-row checks only
verify the labeling-specific input identities.

Artifacts:

- [Source](../../../computations/dd82/construction/petersen_four_fiber_reassembly.py).
- [Complete seed and edits](../../../computations/dd82/construction/petersen_four_fiber_reassembly_run/seed.json),
  [edge list](../../../computations/dd82/construction/petersen_four_fiber_reassembly_run/seed.edges),
  [independent BFS](../../../computations/dd82/construction/petersen_four_fiber_reassembly_run/seed.verification.json),
  [block diagnostics](../../../computations/dd82/construction/petersen_four_fiber_reassembly_run/seed.diagnostic.json).
- [Encoding and variable map](../../../computations/dd82/construction/petersen_four_fiber_reassembly_run/encoding.json),
  [actual CNF](../../../computations/dd82/construction/petersen_four_fiber_reassembly_run/input.cnf),
  [solver result](../../../computations/dd82/construction/petersen_four_fiber_reassembly_run/result.json),
  [solver log](../../../computations/dd82/construction/petersen_four_fiber_reassembly_run/solver.log).
