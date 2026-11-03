# Independent finalallpair, source-retraction and every-prefix Walk proof

This statement concerns only the complete literal graph G with16389 vertices and128835 edges and the original literal simple source S with15552 vertices and116316 edges used by the actual fresh verifier. It does not treat a loop-completed relation as an adjacency list or assume a15regular source. The actual source degree distribution is14:648/15:14904; no source-only BFS was run.

## Literal premises actually bound

The original author's headerless adjacency-list file was parsed once, including its full simple row sets and reciprocity. The candidate edge table was parsed once. Every116316 source edge occurs in the candidate exactly, with no added/removed old-old edge. Each of837 new labels15552+j has exactly the complete actual source neighborhood of its ordered source center c_j, including correct degree14 or15. The ordered center recipe is the fixed selected31 controller labels times the27 offsets x0+9*x2+27*x3. The verifier independently constructed this recipe and extracted Ns from the original source rows; it imported no producer neighborhood cache or affine generator.

Every actual new edge was checked for membership in the extracted N_S(c_j), and the complete literal degree plus simplicity establishes equality, not merely inclusion. A source center never belongs to its own simple N. Thus virtualself entries were already deleted at the old center before its N was frozen; they were not reinserted by testing against the clone's new label. Exactly36 centers have degree14 and801 have degree15, yielding12519 newold edges. There are zero newnew edges. All12519 actual old pins are distinct, of load1, and final degrees are14:72/15:4410/16:11907.

## Direct complete finalgraph D4 evidence

Ordinary BFS was executed exactly once for every final vertex0,...,16388, on the actual complete candidate CSR. This includes15552 old-labelled roots and837 new-labelled roots, all in G. Every run reached all16389 final vertices with eccentricity exactly4. Thus every one of268599321 ordered pairs, including diagonal pairs, was actually reached by radius4. No source-diameter publication, symmetry, orbit, translated-root assumption or sample extrapolation is needed as the sole support for old-old D4 in this acceptance.

There was no separate BFS on S, no preliminary837-root batch, and no repeated final root. The complete per-root histograms and prediction comparisons are saved in `ALL16389_FINAL_ROOT_BFS.csv`. An actual distance-four predecessor path, found inside this same batch, is

    0 -- 891 -- 3726 -- 907 -- 1.

It proves that the final graph does not have diameter at most3. The first and last vertices here are old-labelled vertices of G, not a separately tested source root/target.

## Controller projection and the old-R4 prediction

For an old source label v, set q(v)=floor(v/81). For a new clone x_j set q(x_j)=floor(c_j/81). Build the192-vertex loopless undirected controller graph C from **actual source edges between different controller fibers**. Its actual maximum degree was checked to be5. Source edges within one fiber are real edges but project to a holding step. Every candidate edge was separately checked to project either to a C edge or to a holding step;2880 literal candidate edges have holding projections.

Any candidate path of length at most3 projects to at most3 C edges after deleting holding steps. A simple graph of maximum degree5 has a radius3 ball of size at most

    1+5+5*4+5*4^2 = 106.

At least192-106=86 controllers lie outside that projected ball. Each contains81 distinct **old** vertices, so at least6966 old vertices cannot be at candidate distance at most3 from any chosen root. The directly checked final upper bound4 then forces all of them to be at distance exactly4. This proof does not incorrectly demand a graph homomorphism to a loopless C for an intra-fiber edge, and does not count a self-controller target as a new ball vertex.

The new prediction was tested separately for every final root. Actual old distance4 counts range13066..13242, all at least6966. Eccentricity4 and the lower bound had zero failed roots. For every new root its own old center has actual distance2, and all836 other new vertices are at actual distance3 or4, with none at distance at most2. Actual othernew distance3 counts range107..135 and distance4 counts701..729. These numerical ranges and318 full-histogram profiles are outputs, not retrospectively claimed uniform predictions.

## Retraction supplies an independent source upper bound without another BFS

Define pi:G→S by fixing old labels and mapping every clone x_j to c_j. Each old-old edge maps to the identical source edge. Each newold edge x_j-v maps to the actual source edge c_j-v, by complete open-N binding. There is no newnew edge. Therefore pi is an edge-preserving graph map, and the old inclusion is a right inverse.

For any two old vertices, take their actually established length-at-most4 Walk in G and map it by pi. This produces a genuine S Walk of the same length. Thus source D≤4 also follows from the complete finalgraph acceptance by retraction. This does not rerun source BFS and does not use the desired prefix conclusion to prove its own premise. The final all-root test supplies its upper bound directly, then retraction and endpoint replacement supply the structural prefix result.

## Immutable-full-N source-interior Walks for every prefix

Consider any prefix H of completed clone additions, keeping all of S. Old-old pairs have the source Walks just justified. For x_c and an old v different from c, replace the first edge of a source shortest Walk c→v by x_c's identical old-neighbor edge. If v=c, choose any old neighbor u in N_S(c); x_c-u-c has length2. Nonempty N is guaranteed here by minimum source degree14.

For clones x_c,x_d with source centers at distance2,3 or4, replace both endpoints of the corresponding source shortest Walk. If c and d are adjacent, use x_c-d-c-x_d of length3≤4. This handles adjacent source centers without an independence assumption. All interior vertices in every displayed route belong to the original S, so no future clone is needed. The same proof therefore applies to every prefix, rather than inferring a smaller graph's diameter by arbitrary deletion from a tested larger graph.

Every prefix has old pin load at most1; old degree is at most15 and new degree is14 or15, so maximum degree is at most16. Actual final complete degree checks show maximum16 is attained. Disjoint full Ns also explain why different clones have no direct edge or common neighbor, consistent with the separately tested newroot distance3/4 predictions.

This is independent mathematical acceptance of the literal final graph and its prefix mechanism. It is not a Lean proof, new public-priority audit or broad source-family optimality statement. Root owns public comparison, release/counts and subsequent formal/review actions. No root/Wiki/expert/frozen artifact was changed.
