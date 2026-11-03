# Full false-twin58 matching search: one completed episode

This is a construction search on the general eight-by-six matching
cover, with no C7, translation or other group action. It continues parent
run `dd82-v3-f9-c7-20261013-0749`. After preparation and the parent's
same-thread Gemini review, one episode was authorized and completed.
**The best full graph has 24 bad pairs, confirmed by independent BFS;
no target or family exclusion was obtained.**

The existing complete failed seed has 58 vertices, 232 edges, all degrees
eight and 105 bad pairs. Its seven root interfaces are identity by the
proved coordinate gauge; the other 21 S6 interfaces are independent.
The new implementation adapts the complete-graph bitsets and four-endpoint
matching switch from `petersen_all_matchings.cpp`, not its six-Petersen
constraints, objectives or restart mechanism.

One proposal chooses one of the 21 free interfaces and two distinct source
coordinates, then exchanges their targets. These 21·15=315 elementary
moves preserve simplicity, all degrees, every perfect matching, the fixed
scaffold and the root gauge. Transpositions generate each S6 independently,
so this move domain does not freeze an additional interface relation.

The energy is the exact number of uncovered unordered cross-fibre point
pairs among all 28·36=1,008 such pairs. Full-graph adjacency bitsets calculate
one- and two-step reachability; all other point-pair types are automatically
covered by the false-twin construction. A lower energy is always accepted;
an increase Δ is accepted with probability exp(−Δ/T). The proposed single
continuous chain uses `mt19937_64` seed **2026101301** and

\[
T(t)=2.5(0.15/2.5)^{(t\bmod250000)/250000}.
\]

Periodic reheating changes only T: neither the graph nor the RNG is reset.
There are no restarts, new seeds, SAT calls or auxiliary defect objectives.
The proposal sequence and temperature depend on iteration, so the seed,
source and saved discovery iteration specify a replay on the same build.

The prepared sources are
[full_matching58_anneal.cpp](../../../computations/dd82/construction/full_matching58_anneal.cpp)
and [full_matching58_anneal_run.py](../../../computations/dd82/construction/full_matching58_anneal_run.py).
The wrapper separates `prepare` from `run`. Preparation actually compiled
the C++ source and exercised each of the 315 switches on the seed solely
to verify reversibility, degree/gauge preservation, and agreement between
graph reachability and a separately computed permutation-route score.
It did not select an improved neighbour or start an optimization chain.
Compilation used 0.924211 child CPU seconds; the self-check process used
0.005041 child CPU seconds (0.003040 seconds inside C++). Evidence is in
[`preparation.json`](../../../computations/dd82/construction/full_matching58_anneal_run/preparation.json).

The authorized `run` launched once on CPU 1, with a 120 CPU second
process cap, 240 second wall cap and 4 GiB memory cap. The chain stops at
energy zero or after 119 CPU seconds, reserving one second for final files.
Every strict new best saves the complete edge table, all 28 permutations,
seed and discovery iteration. A compact improvement log records the last
switch; the final current graph and RNG state are also retained. The best
full graph is passed to the existing independent all-source BFS program,
which reads only its saved edges and shares no search reachability cache.
All bad pairs are retained by that check. A zero score is only a candidate
until this BFS succeeds. A nonzero best is a failed graph, not a family
exclusion or a certified local optimum.

The actual run completed its CPU budget with 50,232,451 proposals,
2,588,750 accepted moves, including 981,994 accepted increases, and zero
chain restarts. The score improved from 105 to 24; the best was discovered
at iteration 8,582,544 and CPU time 20.330615 seconds. Search child CPU was
119.003882 seconds and wall time 119.576408938 seconds. The final current
state had 32 bad pairs; the saved best remains 24. No second episode,
additional seed or extended budget was used.

The existing independent BFS program read only
[candidate.best.json](../../../computations/dd82/construction/full_matching58_anneal_run/candidate.best.json)
and confirmed 58 vertices, 232 edges, every degree eight, diameter three
and exactly 24 bad pairs. This separate process used 0.031294 CPU seconds
and 0.033675235 wall seconds. All bad pairs are in
[candidate.best.verification.json](../../../computations/dd82/construction/full_matching58_anneal_run/candidate.best.verification.json);
the plain full edge table is
[candidate.best.edges](../../../computations/dd82/construction/full_matching58_anneal_run/candidate.best.edges).
All 28 interface parameters and the seed/discovery iteration are included
in the complete candidate JSON. Every strict earlier best is also saved.

Reading that BFS result, all 24 remaining bad pairs lie between G1={16,…,21}
and G6={46,…,51}; the other 27 fibre pairs are covered. All 21 free
interfaces differ from the initial 105-bad seed, while the seven root
interfaces remain identity. This localization and comparison are in
[best.failure_summary.json](../../../computations/dd82/construction/full_matching58_anneal_run/best.failure_summary.json)
and required no new search or BFS. Exact process resources and launch
parameters are in
[resources.json](../../../computations/dd82/construction/full_matching58_anneal_run/resources.json),
with the complete proposal/acceptance counts in `search.json` and the
improvement log in `improvements.jsonl`. The full general false-twin58
construction problem remains open; this is a heuristic failed candidate.

The requested short diagnosis then read only the actual best edge table.
For the bad block (1,6), every one of the six intermediate-fibre composites
Q_1k Q_k6 is identity (k=0,2,3,4,5,7). Consequently

\[
S=\sum_{k\ne1,6}Q_{1k}Q_{k6}=6I_6,\qquad
Q_{16}=[5,0,4,2,1,3],\qquad
K=\begin{pmatrix}
6&0&0&0&0&1\\
1&6&0&0&0&0\\
0&0&6&0&1&0\\
0&0&1&6&0&0\\
0&1&0&0&6&0\\
0&0&0&1&0&6
\end{pmatrix}.
\]

Each S row has exactly one supported target, with value six; each K row
has two supported targets, with values six and one, and four zero entries.
If only Q16 is replaced by any permutation M, all six composites remain
fixed, so the new block is 6I+M. Its exact bad-pair count is
**24+fix(M)**: a nonfixed row has four zeros and a fixed row five.
Therefore changing Q16 alone cannot improve the graph below 24 bad pairs,
let alone repair it. Some intermediate matching interfaces must change.
This is a conclusion for the other 27 interfaces fixed to this graph,
not an exclusion of the general construction.

The same actual interfaces supply a structural reason to check a common
coordinate symmetry: 20 of the 21 free permutations are fixed-point-free
involutions, and their distinct values comprise all 15 perfect matchings
on six coordinates. The exceptional Q16 is a six-cycle. Checking all 720
coordinate permutations against all 21 free interfaces gives common
centralizer {identity}. Thus there is no nontrivial automorphism induced
by one shared coordinate permutation on all eight fibres while fixing
parents and twins. This is not a computation of the full automorphism
group; in particular the original false-twin swap is still present.

The reproducible diagnosis is
[full_matching58_failure_local.py](../../../computations/dd82/construction/full_matching58_failure_local.py).
It appended the full S/K rows, supports, six route permutations and exact
centralizer to `best.failure_summary.json`, using 0.001833200 CPU seconds
and 0.001832597 wall seconds. It generated no candidate, performed no
optimization or solver call, and did not rerun BFS.

One further requested read-only check tested exactly the induced graph
obtained by deleting {0,8,46,47,48,49,50,51}: twin 0, parent s6 and G6.
The remaining graph has 50 vertices, 175 edges and every degree seven.
Checking all 1,225 unordered pairs gives 175 adjacent pairs with zero
common neighbours and 1,050 nonadjacent pairs with exactly one common
neighbour. Thus this is the degree-seven Moore graph with parameters
(50,7,0,1), the Hoffman–Singleton graph. Its relabelled complete edge set
and original label map are saved in
[best.induced_hs50.json](../../../computations/dd82/construction/full_matching58_anneal_run/best.induced_hs50.json).

This verifies that the actual failed 24-bad graph has returned to a known
induced-HS augmentation core. The existing exclusion in
[HOFFMAN_SINGLETON_AUGMENTATION.md](HOFFMAN_SINGLETON_AUGMENTATION.md)
already rules out a target retaining such an induced HS50; this is failure
localization, not a new exclusion theorem. A subsequent construction must
change the identified induced core rather than merely repair its outside
attachments. No conflict exists with that theorem because this graph has
diameter three and 24 bad pairs.

The one-core check is reproducible in
[full_matching58_induced_core_check.py](../../../computations/dd82/construction/full_matching58_induced_core_check.py)
and appended to `best.failure_summary.json`. It used 0.002526792 CPU seconds
and 0.002946451 wall seconds. It checked only this one induced subgraph,
generated no alternative candidate, and performed no new full-58 BFS or
optimization.
