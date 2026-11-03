# F5 complementary-triples finite positive control

The frozen local prediction is SUPPORTED. The single worker checked all four directed-port maps, their actual inverse binding, all36 central turns (all rank3), and the full six-plane pencil for all125 source coordinates at every port. Each of the24 planes has25 points, pairwise intersections within a pencil have5 points, and each pencil union has125. Total500 translated-pencil checks passed.

Worker PID 1109648, CPU 0.059301383 seconds. The process completed; no graph, old/source BFS, new word enumeration, matrix search, or solver was run.

## Exact matrices over F5

port0 -> reverseport1: [[0, 2, 4], [1, 0, 0], [0, 1, 3]]
port1 -> reverseport0: [[0, 1, 0], [4, 0, 3], [2, 0, 1]]
port2 -> reverseport3: [[2, 3, 1], [0, 4, 1], [1, 0, 1]]
port3 -> reverseport2: [[2, 1, 2], [3, 3, 4], [3, 4, 4]]

Each matrix sends its outgoing direction exactly to the direction at the reverse port. Ports1/3 are the computed inverses of ports0/2. The second pair was obtained by a frame permutation followed by scalar normalization, not independent reverse choices.

## Why every edge can use these maps simultaneously

The actual stored controller has the same inverse-port convention on all120 darts, which the worker checked. Assign matrix T_p to every dart with port p. The reverse dart has port inv(p), and its matrix is exactly T_p^-1. Edge-local equations are therefore satisfied for all60 undirected edges at once.

The neighborhood is a line relation, not an action of a group presentation. Products of matrices around a controller cycle need not equal identity. A three-step nonbacktracking path has image rank equal to rank[T_middle*l_i, l_q, l_j], after factoring out an invertible final matrix. Since all36 local turn cases pass, there is no extra shared-edge rank condition left for different words. This is the precise reason the local result is not merely an unimplemented PGL existence claim.

## Conditional whole-graph certificate, without generating that graph

Read-only binding to the existing actual controller verified30 vertices, degree4, no loops or repeated controller neighbors, inverse ports at all120 darts. The worker read the previously saved NB3 integer table, rather than recomputing its words: all780 nonadjacent/equal ordered pairs have a route (minimum count1). The120 adjacent ordered pairs use the six-plane pencil.

Thus the explicitly specified relation on30 times F5^3 would be simple20-regular of order3750, with D<=3 for every source coordinate. Moore(20,2)=401<3750 would give exactD3. This is a mathematical construction certificate; an actual3750-vertex edge list has not been generated or independently checked here.

## Bound sources

Local source/controller package:
research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json
research/ddp/breadth_20261027_wave4/mizuno_d3_source/controller_structure.json
research/ddp/breadth_20261027_wave4/mizuno_d3_source/PROOF_ja.md
research/ddp/breadth_20261027_wave4/mizuno_d3_source/bfs_certificate.json

Primary author proof:
https://raw.githubusercontent.com/rmizuno42/ddp/main/results/degree16-diameter3/certificate/PROOF_ja.md

Published source edge file identified in that proof (not downloaded or parsed in this task):
https://raw.githubusercontent.com/rmizuno42/ddp/main/results/degree16-diameter3/certificate/graph_d16_D3_n1920.edges

The source is the published1920 F4 graph. No claim is made that our F5 matrices reconstruct its edges; only the source controller, port convention and cached route existence are reused.

## Scope and unresolved comparison

This check proves the four-port local complement/pencil rule over exactly F5 and its compatibility with the fixed source30 controller. It does not prove new-record status, classify all (20,3) graphs, require every viable affine construction to have full-rank individual routes, or exclude multiword unions at q3/q4.

Fresh Comellas main table ends at degree16; no primary degree20/D3 comparison has been bound. The source author states a specific F4 construction, not an arbitrary-q theorem or novelty of projective pencils. Complete graph generation is paused until a worthwhile comparison is established. No q/controller scan is queued.
