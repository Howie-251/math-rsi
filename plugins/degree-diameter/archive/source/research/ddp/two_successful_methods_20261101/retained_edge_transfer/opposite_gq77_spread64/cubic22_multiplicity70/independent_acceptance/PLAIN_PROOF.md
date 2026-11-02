# Literal A70 acceptance and the immutable-neighborhood clone argument

This scope is the single166650-vertex A70 candidate. Its source is the original accepted160050-vertex64-regular graph G, with5121600 edges, in `../../graph_d64_D3_n160050.edges` relative to this directory. The161150-vertex65-degree graph is not read or used. No producer code, producer `CENTERS`, cached neighborhoods, or producer passed flags are used.

The source's accepted literal/formula binding is inherited from `../../independent_acceptance/SUMMARY.json`. Its already closed concrete Lean theorem is inherited from `../../formalization/FINAL_COMPILE_RESULT.json`: `DegreeDiameter.Portfolio.OppositeGQ77Spread.concrete_order_degree_and_exact_D3`, with no user hypotheses. This new task does not reconstruct the GQ, recompile its Lean modules, or run any old BFS root. The fresh literal source read itself checks the source header, all proper strictly sorted distinct source edges, and degree64 at every source vertex.

## Exact new graph definition

Let P be the explicit point order

    [57,119,165,251,265,347,399,71,133,179,216,279,312,364,
     85,147,193,230,293,326,378,1].

Let S be the original50 spread labels, read in their original order from the source `PARAMETERS.json`; they are never sorted. For b=50i+j, define the1100 distinct base centers c_b=400P[i]+S[j]. For copy r=0,...,5, define k=1100r+b and x_k=160050+k. Thus copy order is outermost, and point order then original spread order are inside it.

For each base center, the fresh source scan independently recovers the full open neighborhood N_G(c_b), by accumulating every incident source edge. Each recovered set has64 distinct old vertices. For every one of the6600 new labels, the new graph must connect exactly to N_G(c_(k mod1100)). This is the immutable original source neighborhood, including any original source bonus vertex actually present there. It is never a neighborhood in an intermediate clone graph.

The candidate scan checks every edge's endpoints and strict lexicographic order. Its old-old subsequence is compared entry for entry against a fresh stream of the original source body, with both bodies exhausted exactly. Each new edge is checked for membership in its independently recovered base neighborhood. Every new label has64 distinct incident old edges, so membership plus cardinality establishes full equality for all six repetitions of every base center. Any new-new edge is rejected.

## Diameter lemma, including repeated and adjacent centers

Suppose G has diameter at most3 and each selected center has positive degree. Form H by preserving every edge of G and adding arbitrary distinct clone vertices x_k, with x_k adjacent exactly to the old source set N_G(c_k), and with no new-new edges. Centers may repeat and may be adjacent. Then H has diameter at most3.

Old-old pairs retain a source walk of length at most3. For an old v different from c_k, choose a shortest G path c_k-a-...-v of length1,2,or3. Replacing its first vertex by x_k produces an H walk of the same length, because a is an original neighbor of c_k. For v=c_k, positive source degree gives an old a in N_G(c_k), and x_k-a-c_k has length2.

For two distinct clone vertices x_k,x_l:

- If c_k=c_l, any original source neighbor a gives x_k-a-x_l of length2. This explicitly handles all pairs of the six copies at the same base center.
- If c_k and c_l are adjacent, x_k-c_l-c_k-x_l has length3. Both outer edges are legal clone edges to original source neighbors, and the middle edge is a source edge.
- If the centers have source distance2, a source path c_k-a-c_l gives x_k-a-x_l of length2.
- If the centers have source distance3, a source path c_k-a-b-c_l gives x_k-a-b-x_l of length3.

Equal vertices use the zero-length walk. These cases cover every pair. No independence of the distinct base centers is assumed.

Every nontrivial route in this proof uses only the one or two clone endpoints being connected and old original-source vertices. Consequently the same proof applies to **every prefix** consisting of G plus new labels160050,...,160050+t-1, for0<=t<=6600. No prefix route borrows a future clone. This is a mathematical all-pairs and all-prefix proof once the complete literal binding above is established; it does not depend on performing old-root or prefix BFS.

## Degree and exact diameter

For each old v, the source scan counts base_load(v), the number of distinct base neighborhoods containing v. The final candidate separately counts every incident new edge, and binds that literal count to6*base_load(v) for each individual old vertex. Since G is64-regular, its final degree is64 plus that count; each clone has degree64. Prefix loads are at most final loads and therefore obey the same degree cap70.

The actual fresh read establishes1100 distinct base centers with64 source neighbors each, base_load at most1, and **231 source edges between distinct base centers**. The final literal graph has **166650 vertices and5544000 edges**, including every one of the5121600 source edges and exactly422400 clone edges. It has no new-new edge. Every old vertex was checked separately:89650 have final load0 and70400 have final load6. The actual degree histogram is **64:96250,70:70400**. Thus all finite premises of the preceding proof are actual checked facts for the literal candidate.

The source diameter-at-most3 theorem, the exact full-neighborhood clone binding, and the lemma prove final and prefix diameter at most3. A graph of maximum degree70 and diameter at most2 has order at most

    1 + 70 + 70*69 = 4901.

All these graphs have at least160050 vertices, so they cannot have diameter at most2. In particular, the final candidate has exact diameter3. The new concrete Lean instance is a separate task; this independent acceptance performs no Lean compilation.

## Falsifiable histogram prediction and actual measurement

`PRED.json` was written before the candidate was read. It predicts all6600 new-root distance histograms, including their class counts:132 roots with(1,64,3191,163394) and6468 roots with(1,64,3254,163331), in distance0/1/2/3 order. The five additional same-center copies belong to distance2. For a root's class, the independent source neighborhood is checked for an original source bonus neighbor in labels160000,...,160049: presence predicts the first histogram, absence predicts the second. The source class sizes and every root's predicted and measured histogram are checked, not only its reached count.

The BFS implementation is an ordinary FIFO queue over the parsed candidate adjacency, through radius3. It assigns distances on first discovery. Vertices at distance3 need not be expanded, because the checked obligation is that every candidate vertex has already been reached within radius3. No route cache, producer neighborhood, bitset reachability, or old-root BFS is used. The fixed budget is90 CPU seconds, single worker, including the one compile and all BFS. The first10 roots are the pilot; a forecast exceeding the remaining budget permits only the pilot and is reported without extending the timer.

The actual10-root pilot cost0.035732 CPU seconds and forecast25.703978 CPU seconds for the whole validator, so it allowed the full fixed scope. **All6600 new roots were actually run, and0 old roots were run**. Every root reached all166650 vertices and every root matched its predicted histogram class. The actual distribution is exactly **132 roots with(1,64,3191,163394),6468 roots with(1,64,3254,163331)**. Thus the same-center+5 prediction and the class counts both passed; this is stronger than checking only reachability.

The actual internal validator total was25.270636 CPU seconds:0.565332 for source parsing and independent neighborhoods,1.551543 for the complete candidate binding,23.094774 for BFS, plus small internal overhead. Actual child resource receipts record1.028157 CPU seconds for the one compile and25.278185 for validation. The measured acceptance-process total including compile, driver preparation, CSV aggregation, and inherited source-receipt reading is **26.343279409 CPU seconds /90**, one worker, with no budget extension. All actual finite counts, histogram classes, pilot forecast, and complete measured CPU receipts are recorded in `SUMMARY.json`, `RESULT.json`, `RESULT.md`, `TERMINAL.json`, and `NEW_ROOT_BFS.csv`. No solver, installation, download, hash calculation, or Lean compilation was performed.
