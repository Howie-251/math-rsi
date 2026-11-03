# Fixed K4 / Z20 six-matching controller gate

Before execution, 2026-11-01 UTC.

Prediction: the concrete K4-deck construction may admit an 80-vertex controller with the complete NB3 source interface for the already passed r6/F9 local charts. The outcome is an exact finite-domain witness, an exhausted-domain STOP, or budget-limited UNKNOWN; failure does not imply a general controller obstruction.

Vertices are `(i,z)`, `0<=i<4`, `z in Z20`, with label `20*i+z`. For every `i<j`, add the zero edge `(i,z)~(j,z)` and shifted edge `(i,z)~(j,z+g_ij)`. Set `g_01=1`; independently enumerate `(g_02,g_03,g_12,g_13,g_23)` in lexicographic order in `{1,...,19}^5`, exactly 2,476,099 assignments. Fixing a unit anchor is a restricted family over the composite ring Z20, not a WLOG reduction of all six-shift controllers.

Port `k-1` is the zero matching `i -> i xor k`, and port `k+2` is the shifted matching on the same base one-factor, for `k=1,2,3`. All six ports are self-inverse. A lower-base to higher-base shifted step adds `g_ij`; the reverse subtracts it. Zero and shifted edges differ because every shift is nonzero, so each assignment gives a simple 6-regular controller with 80 vertices and 240 edges. Every deck contains a K4, giving a triangle at every vertex.

For each of four base roots `(i,0)`, precompute all 150 port words `(p1,p2,p3)` with `p2 != p1` and `p3 != p2`, their target bases and six integer shift coefficients. For each assignment and each target base, form the complete 20-bit endpoint-residue set. It must contain every residue for equal base, and every residue except `0` and the signed `g_ij` for different bases. This checks all 296 required translation classes, equivalently 5,920 ordered same/nonadjacent vertex pairs. Adjacent pairs are delegated to the passed full pencil. The first failed class rejects an assignment; the first completely passing assignment stops the search.

One worker, total budget 30 CPU seconds including C++ compilation, search and certificate generation. No fiber graph, old graph, BFS, solver, Lean, installation, hashes, alternate modulus, seed or timer continuation. On success preserve literal controller edges, port table, shifts, all ordered-pair NB3 witnesses, triangles, and word-based diameter evidence. The candidate lift would have 80*729=58,320 vertices and degree 54, pending root production decision and independent acceptance. No accepted count or Wiki changes are made here.
