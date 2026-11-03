# Complete Petersen domains of the actual tight-row allowed graphs

Date: 2026-10-12. All 30,240 distinct labeled Petersen graphs were tested
against each of twelve actual allowed graphs. Every surviving mask is
saved; all twelve domains are complete. No repair, SAT, or repeated BFS
was part of this diagnostic.

Here \(H_i\) is the allowed internal graph obtained from all tight external
rows, as proved in
[the tight-row report](PETERSEN_TIGHT_ROW_DEGREE_OBSTRUCTION.md).
The domain is

\[
\mathcal P_i=\{P:\ P\text{ is a labeled Petersen graph},\ E(P)\subseteq E(H_i)\}.
\]

| Actual matching skeleton | \(F\) | \(K\) | Domain sizes for fibers 0–5 |
|---|---:|---:|---|
| New 286-bad-pair graph | 0 | 0 | **0, 0, 1, 0, 0, 0** |
| Original twenty-bad-pair graph | 40 | 0 | **12, 12, 12, 12, 44, 44** |

For the new skeleton, the minimum number of forbidden edges used by a
Petersen copy in each fiber is

\[
(1,2,0,1,1,2),\qquad \text{sum }7.
\]

These are exact minima over the entire catalog, not lower bounds from
individual vertex degrees. For each fiber the data save one closest
complete Petersen copy, its forbidden edges, and the number of copies
attaining the minimum. The unique allowed copy in fiber 2 is also saved
explicitly. None of the new graph's six original internal graphs belongs
to its current domain, including fiber 2, whose sole survivor is different.

In contrast, all six original internal Petersen graphs of the twenty-pair
seed belong to their domains. That seed already meets the local complete-P
requirements, but fails \(F=0\): its 4-to-5 and 5-to-4 rows have four
coincident intermediate matching routes. No choice from its nonempty
domains can repair this immutable external failure. There is therefore
no reason to enumerate products of those old internal domains.

## Concrete reasons for the five empty new domains

The following arguments use the actual allowed-neighbor lists saved in
the input data, in original global labels. They explain the empty domains
without treating minimum allowed degree as sufficient.

- **Fiber 0.** Vertex 6 has exactly the allowed neighbors \(1,2,4\), so
  these three edges are forced. In a Petersen completion, put
  \(A=\{1,2,4\}\) and \(R=\{0,3,5,7,8,9\}\). Every vertex of \(R\)
  has exactly one neighbor in \(A\), and \(R\) induces a six-cycle:
  radius two around 6 exhausts the ten vertices, and girth five prevents
  repeated second neighbors or a shorter cycle component. Vertex 8 has
  only \(0,3\) available inside \(R\), while vertex 5 has only \(3,9\).
  Hence the six-cycle must be \(0,8,3,5,9,7,0\). The two children of
  vertex 2 must be opposite on this cycle, to avoid a triangle or
  four-cycle through 2. Its only available children are \(3,5,9\), three
  consecutive cycle vertices, containing no opposite pair. Contradiction.
- **Fiber 1.** Vertices 14 and 19 each have exactly the allowed neighbors
  \(12,15,18\). Their forced edges give the four-cycle
  \(14,12,19,15,14\).
- **Fiber 3.** Vertex 37 forces neighbors \(32,33,38\); vertex 39 forces
  \(30,33,36\). The latter star forbids \(30\sim36\). The allowed
  neighbors of 30 are \(32,36,38,39\), so 30 must use \(32,38,39\).
  This forces the four-cycle \(37,32,30,38,37\).
- **Fiber 4.** Vertex 45 forces \(40,44,47\). Triangle-freeness then
  forbids \(40\sim44\) and \(40\sim47\). But 40's complete allowed
  list is \(43,44,45,47\), leaving it at most two neighbors.
- **Fiber 5.** Vertices 51,53,54,58 have exactly the allowed lists
  \(\{50,52,56\}\), \(\{50,52,54\}\), \(\{50,53,57\}\),
  \(\{50,55,56\}\). Their four forced incidences at 50 contradict
  internal degree three. This last obstruction does not require girth.

The only nonempty new domain, fiber 2, contains the following fifteen
edges:

\[
\begin{gathered}
20\!-!23,20\!-!24,20\!-!27,21\!-!24,21\!-!25,21\!-!28,\\
22\!-!23,22\!-!28,22\!-!29,23\!-!25,24\!-!29,\\
25\!-!26,26\!-!27,26\!-!29,27\!-!28.
\end{gathered}
\]

## Complete enumeration and next constructive mechanism

The catalog generator is the already used exact transversal from
`petersen_internal_reassembly.cpp`: fix the image of vertex 0, order the
images of its three neighbors, and break the remaining order-two
stabilizer by \(p(2)<p(6)\). It generates
\(9!/(3!\,2)=30240\) labeled copies, checking distinctness with an ordered
set. Each domain then tests precisely \(E(P)\setminus E(H_i)=\varnothing\).
The twelve full scans make 362,880 containment checks.

The concrete next mechanism is to retain \(F=0\) while changing external
matchings and minimizing

\[
R=\sum_i\min_{P\in\mathcal P_{\rm all}}|E(P)\setminus E(H_i)|.
\]

The current value is seven. This objective chooses a **complete internal
Petersen graph** in every fiber; it does not merely remove one vertex's
degree deficit. A state can be expanded immediately using its six actual
minimizers. At \(R=0\), all six local complete graphs satisfy every tight
row prohibition. Their joint cross-fiber coverage must still be checked;
local nonempty domains do not imply a target. The parent has authorized
one subsequent bounded episode under this mechanism, recorded separately.

## Files and resources

- [Enumerator](../../../computations/dd82/construction/petersen_allowed_petersen_domains.cpp)
  and [launcher](../../../computations/dd82/construction/petersen_allowed_petersen_domains_run.py).
- [Actual allowed graphs and every tight row](../../../computations/dd82/construction/petersen_allowed_petersen_domains_run/input_graphs.json).
- [All twelve complete domains and closest copies](../../../computations/dd82/construction/petersen_allowed_petersen_domains_run/domains.json).
  Masks are 45-bit edge sets using the saved lexicographic local edge
  index; they are graph encodings, not hashes.
- [Resources and summaries](../../../computations/dd82/construction/petersen_allowed_petersen_domains_run/resources.json).

The enumeration used 0.016001 child CPU seconds and 0.033493273 wall
seconds. Preparation and result processing used 0.020201581 parent CPU
seconds; total wall time was 0.054405563 seconds. The diagnostic had a
five-CPU-second bound and completed all twelve domains. No graph search,
solver, or BFS replay was run.
