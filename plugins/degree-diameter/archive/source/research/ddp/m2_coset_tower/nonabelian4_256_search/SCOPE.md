# Prepared fixed-group four-orbit search

Root selected **Q64 only** after the capacity comparison and authorized one bounded actual run. D64 will not be run. The actual execution status is recorded in `run.json` and `terminal.json` when those files exist.

The selected group has elements `(x,s)`, with `x` in Z32 and `s` in C2, encoded `x+32s`. Its product is

`(x,s)(y,t) = (x + (-1)^s y + c s t mod32, s xor t)`,

where `c=0` for D64 and `c=16` for Q64. The inverse is `(-x,0)` for `s=0`, and `(x+c,1)` for `s=1`. In particular, Q64 odd elements are not treated as reflections. The search constructs the product and inverse tables from this one selected definition.

The fixed base has four vertices and multiplicities `(01,02,03,12,13,23)=(3,3,2,2,3,3)`. In edge-array order these classes have IDs `0..2,3..5,6..7,8..9,10..12,13..15`. Tree edges `[0,3,6]` have identity voltage. The 13 free edges in phase-bit order are `[1,2,4,5,7,8,9,10,11,12,13,14,15]`. There are no loops. The only additional simplicity condition is that parallel edges have distinct actual group voltages.

Vertices are `(i,g)`, labeled `64i+g`. A base edge `i<j` with voltage `h` gives all edges `(i,g)--(j,gh)`. Thus each candidate has 256 vertices and 1,024 edges and is simple 8-regular; a reverse traversal multiplies by the true inverse of `h`. For each `a` in the group, left multiplication `(i,g) -> (i,ag)` is an automorphism, since `a(gh)=(ag)h`. Four complete BFS roots `0,64,128,192` therefore determine all eccentricities and all radius-3 deficits, including disconnected candidates. If their deficits are `m_i`, the exact number of bad unordered vertex pairs is `64 sum(m_i)/2`. This uses the actual group action, not a commutative voltage assumption.

The planned bounded procedure uses 64 fixed random starts, at most nine segments per start, and at most 30 strict coordinate moves per segment. At each move it evaluates every legal alternative among all 63 other group values on each free edge, then takes a best strict improvement. Capacity phase restrictions select the initial starts only; moves and legal two-coordinate kicks can change phase and are not capacity-filtered. There is no normalization in the x direction, no scalar quotient, no old seed, and no reduction of a graph from another modulus. Completing this procedure does not exhaust all voltage assignments.

The driver requires two parent-selected inputs before it does any preparation:

- `group_definition.json`: fields `name` (`D64` or `Q64`) and `twist` (respectively 0 or 16), with optional source description.
- `start_policy.json`: `group_name`, exact `edge_u`, `edge_v`, `tree_edge_indices`, `free_edge_indices`, and an ordered list `initial_phase_codes` of length 64. Bit k gives the phase of free edge k. Capacity-source and selection-policy descriptions should be retained in this file. This explicit interface avoids silently interpreting a capacity table with another edge order.

The capacity input is `../nonabelian4_256_capacity/q64/survivors.json`. Of its 324 masks with minimum capacity 52, start 0 uses mask 1205. The remaining 63 masks are sampled without replacement from the other masks in increasing order using `Random(20261027064).sample`. The exact ordered 64 masks are saved in `start_policy.json`. `python3 run.py` generates each start's x coordinates using the separate fixed seed 20261027066, respecting its chosen phase code and parallel-edge legality. It saves every start and independently builds the first formal candidate in Python. Its 1,024-edge adjacency and all four full distance arrays are compared pointwise with the first C++ evaluation, whose score is reused in the search. There is no separate all-source preflight. The parent owns the single final all-256-root check of the saved best graph.

The total single-worker CPU budget is 180 seconds including preparation, compilation, the formal first-start calibration, and search. The driver subtracts preparation and a two-second shutdown reserve from the C++ limit. The C++ process saves the exact current position, current state, staged best neighbor, and random-engine state if its budget is reached; it does not restart automatically. A D3 score stops immediately with the complete graph saved. Run, progress, best, and terminal files describe only actual execution when it is authorized.
