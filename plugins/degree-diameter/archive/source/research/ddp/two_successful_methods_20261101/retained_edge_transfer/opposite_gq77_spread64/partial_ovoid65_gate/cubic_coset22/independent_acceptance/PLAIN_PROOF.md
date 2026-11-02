# Independent mathematical acceptance of the literal 161150-vertex graph

The actual complete candidate was read afresh after the root reported that the file was closed. The validator does not import producer code, producer neighborhood caches, producer passed flags, or `CENTERS.json`. The independent input consists of the explicit ordered point IDs in the task and the original ordered spread labels read from the accepted source `PARAMETERS.json`; the spread order is preserved. Every source neighborhood below is computed by reading the literal immutable source edge file itself.

The source graph G has vertex set {0,...,160049}. Its accepted literal file is `../../../graph_d64_D3_n160050.edges`, relative to this directory. The source independent acceptance and closed concrete Lean result are inherited: `../../../independent_acceptance/SUMMARY.json` and `../../../formalization/FINAL_COMPILE_RESULT.json`. The latter records the unconditional theorem `DegreeDiameter.Portfolio.OppositeGQ77Spread.concrete_order_degree_and_exact_D3`, with no user hypotheses and only the standard three axioms. This acceptance does not reconstruct the source GQ, recompile Lean, or rerun source roots. Its fresh source parse checks 160050 vertices, 5121600 sorted distinct proper edges, and degree64 at every vertex.

For i=50a+j, the old center is

    c_i = 400 * P[a] + S[j],    0 <= a < 22, 0 <= j < 50,

where P is exactly

    [57,119,165,251,265,347,399,71,133,179,216,279,312,364,
     85,147,193,230,293,326,378,1],

and S is the unsorted original spread order in `INDEPENDENT_INPUTS.json`. All 1100 centers are distinct. The new vertex is x_i=160050+i. Its intended neighborhood is the full open neighborhood N_G(c_i), in this immutable G, including any of G's original 50 bonus vertices that actually occur there.

The validator independently accumulates every N_G(c_i) from the source edge body, checks each has 64 distinct vertices, and checks every new candidate edge belongs to the corresponding set. Each new vertex has exactly 64 incident edges and the candidate is simple, so this is equality of sets, not a subset check. The candidate's old-old edge subsequence equals the source edge body entry for entry and exhausts it. The candidate contains no new-new edge. These checks establish the exact graph H used in the following argument.

## General full-neighborhood clone lemma

Let G be a simple graph of diameter at most3, with every chosen center of positive degree. Preserve all edges of G and add arbitrary distinct new vertices x_i, each adjacent exactly to the old vertices N_G(c_i), with no new-new edges. Then the resulting graph H has diameter at most3. The centers need not form an independent set and may even repeat.

For two old vertices, retain their old G walk of length at most3. For a new x_i and old v different from c_i, take a shortest G path

    c_i - a_1 - ... - v.

Its length is1,2,or3; replacing its initial c_i by x_i gives an H walk of the same length because a_1 is an old neighbor of c_i. For v=c_i, choose any a in N_G(c_i); then x_i-a-c_i has length2.

For two different new vertices x_i,x_j, split according to the source distance between their centers:

- If c_i=c_j, a common old neighbor a gives x_i-a-x_j of length2.
- If c_i and c_j are adjacent, use x_i-c_j-c_i-x_j of length3. All three edges are legitimate: the two outer edges are clone edges to original source neighbors and the middle edge is an original source edge.
- If the source distance is2, a source path c_i-a-c_j gives x_i-a-x_j of length2.
- If the source distance is3, a source path c_i-a-b-c_j gives x_i-a-b-x_j of length3.

The equal-vertex cases have length0. These cases cover every pair, so H has diameter at most3. In particular, the adjacent-center case cannot be replaced by an independence assumption. The actual fresh source parse found **231 source edges among these 1100 centers**, and the adjacent-center route above handles all of them.

## Degree, cardinality, and exact diameter

For every old vertex v, independently count

    load(v) = number of i for which v belongs to N_G(c_i).

The source parse gives load0 for89650 old vertices and load1 for70400 old vertices; no old vertex has larger load. The candidate scan separately counts incident clone edges at every old vertex and checks equality with that vertex's source-derived load. Since G is 64-regular, the old degrees in H are exactly64+load(v); every new degree is64. Thus the actual candidate has 161150 vertices and 5192000 edges, with degree histogram 64:90750 and 65:70400, maximum degree65. Exactly5121600 old edges are retained and70400 edges are added.

Applying the lemma to the accepted source diameter-at-most3 theorem gives a genuine all-pairs diameter-at-most3 proof for this exact literal H. It does not infer all-pairs diameter from a sample of BFS roots.

A graph of maximum degree65 and diameter at most2 can have at most

    1 + 65 + 65*64 = 4226

vertices, by counting the root, first neighbors, and at most64 further neighbors per first neighbor. Even the cruder bound1+65+65^2=4291 is smaller than161150. Hence H is not diameter at most2, and its diameter is exactly3.

## Actual queue-BFS and measured cost

The separate literal check performs ordinary FIFO queue BFS from each of the **1100 new vertices**, through radius3, using only the parsed candidate adjacency. Once a vertex has distance3 its neighbors need not be expanded, because the checked obligation is that every vertex is already reached within radius3. No source geometry, cached route, bitset reachability, or producer neighborhood is used in BFS. Every run reaches all161150 vertices. **No old root is run.**

The first10 new roots cost0.034380 CPU seconds; the pilot estimated5.859821 CPU seconds for the whole validator, so all1100 were allowed within the fixed120 CPU-second single-worker budget. The actual BFS histograms are in `NEW_ROOT_BFS.csv`:22 roots have(1,64,3186,157899), and1078 roots have(1,64,3249,157836), in distance0/1/2/3 order. This exact distribution is also recorded in `SUMMARY.json`, `RESULT.json`, and `TERMINAL.json`.

The whole validator used5.763262 internal CPU seconds, including3.679689 for BFS. Actual child resource accounting gives0.975500 CPU seconds for the one compile and5.767770 for validation. The measured compile+validation+driver total is6.747941293 CPU seconds; separately measured result aggregation and source-receipt reading add0.005828474 CPU seconds, for**6.753769767 CPU seconds /120**. Input-table preparation is included in the driver measurement. This task runs no solver, installation, download, hash calculation, or Lean compilation. The candidate's new concrete Lean proof is outside this independent mathematical acceptance.
