# Fixed (4,6) 760-source flag/layer absorption: source and candidates ready

The fresh Comellas main table on 2026-10-27 still lists 760 at (4,6),
without bold optimality markup. Its exact cell is saved in
SOURCE_PROFILE.json and the fetched HTML in main_table_fresh.html.
The current method ledger and experiment notes have no exact 760 or
author deg4/dia6 source entry. No old closed profile was restarted.

The actual primary source is Nishant Bhakar's
[degree-diameter-graphs repository](https://github.com/f4t4nt/degree-diameter-graphs/tree/main/graphs/deg4/dia6).
README.author.md, source760.author.edges.txt, construction.author.json,
and verification.author.txt preserve the small author files. The
construction JSON selects an explicit edge list. The author's verifier
reports diameter 6, with zero unreachable or too-distant pairs. This
source diameter certificate is reused; no source BFS was run here.

The literal has 760 vertices and 1520 distinct edges, and every vertex
has degree 4. The type ranges stated by the author agree with the data:
364 point vertices 0..363, 364 line vertices 364..727, and 32 inserted
vertices 728..759. There are 1424 retained point–line incidences, 64
base–layer edges, and 32 layer edges. Each layer vertex has one point,
one line, and two layer neighbors. The layer cycles have lengths 8,8,16.
Restoring the 32 subdivided flags and removing the layer gives a
728-vertex, 1456-edge, 4-regular bipartite incidence literal. These
checks recover the required flag recipe without rebuilding H(3).

The author's description identifies the original incidence geometry
as the generalized hexagon H(3) and the flag set as two 16-flag orbits
under a Sylow 2-subgroup in an involution centralizer. Preparation does
not recover or use the individual group permutations or orbit labels.
RECIPE_BINDING.json records the actual 32 point–line flags and layer
cycles needed for this experiment.

PREDICTION.json was saved before source profiling or candidate
evaluation: some retained original flag and some layer edge can be
jointly absorbed into one new vertex while retaining diameter 6.
The complete frozen list is all 1424 current base edges times all 32
current layer edges, with the base edge sorted lexicographically in
the outer loop and layer edge in the inner loop. All 45568 pairs have
four distinct endpoints. Each proposed graph has 761 vertices, 1522
edges and degree exactly 4: delete both edges and join new vertex 760
to their four endpoints.

PROOF.md establishes the complete validation rule. Source R5 of the
four endpoints is exactly the new-root coverage condition. All
potentially damaged old–old pairs have at least one endpoint in their
source R2 neighborhood; BFS from this root set plus the new vertex
therefore checks all pairs, using at most 69 roots. The producer must
use each candidate's actual modified adjacency. These roots are not
a sample, and passing the new-root gate alone is insufficient.

Preparation used 0.099 CPU seconds, with zero source BFS, candidate
BFS, geometry rebuilds or candidate route tests. The explicit input
list and normalized source are frozen.json and source760.header.edges;
prepare.py reproduces them. The separate producer is
/root/expert_brief_evidence and owns its execution terminal. No
761-vertex graph or new lower bound is claimed by source preparation.

This fixed scope excludes arbitrary additional rewiring, alternative
flag sets, two base-edge cuts, or two layer-edge cuts. Failure of the
frozen list would not exclude general order-761 (4,6) graphs. No global
Wiki, HTML, delivery archive, old D2 task or unrelated chart was changed.
