# Chen360: the one-edge subdivision batch

Prediction, saved before execution: subdividing the first primary literal edge
raw{1,141}, normalized{0,140}, gives a new degree2 root360 that reaches every old
vertex within8. This is a low-confidence, falsifiable newroot prediction only;
it does not predict old-old preservation or a complete legal361 graph.

Use only PRIMARY_360_ADJLIST.txt, inherited Chen360/D8. Parse that upper-adjacency
literal once as construction input; require the necessary simple360/540 cubic
format, with raw1..360 mapped to normalized0..359. Do not rerun sourceD8.

For each of the at most540 oldedges, delete{u,v}, add{u,360},{v,360}. Each actual
final candidate has361 vertices,541 edges, olddegrees3 and newdegree2. Test the
predicted edge first, then the remaining edges in lexical order. No symmetry
representatives or presumed edge transitivity are used.

The newroot gate is exactly R7_(G-e)({u,v})=allold, equivalently R7_G({u,v})=allold.
Only a full newroot-R8 pass permits ordinary final-candidate BFS from each of
the360 oldlabels, stopping at its first failed old-old pair. Record each tested
edge's stage and failure. Save first newroot and first old-old shortest paths.
The first old-old failure permits one old-source shortest-path diagnostic for
that exact pair, to identify damage from the removed edge; that is not a
sourceD8 verification.

Stop immediately on the first full hit and save its complete literal/parameters
and allroot statistics for root's fresh acceptance and public baseline gate.
If all540 fail, close only this fixed source's complete single-subdivision
family. Incomplete CPU exhaustion remains UNKNOWN. Do not change source, cuts,
seed, template, or launch another batch automatically.

The sourcecase cap is cumulative20CPU, including prior readgate1.015311471,
preparation, compilation, failures, driver and worker. One numerical worker;
no field/solver/Lean/ARIS/install/hash. Root owns acceptance and global counts.
