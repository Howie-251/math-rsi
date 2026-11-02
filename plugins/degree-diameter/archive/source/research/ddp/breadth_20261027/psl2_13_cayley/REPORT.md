# PSL(2,13): completed twelve-start Cayley construction profile

This new matrix-group entry completed its authorized finite trial without a diameter-three graph. It constructs actual 1092-vertex, 12-regular simple undirected graphs, rather than a symbolic projection. The saved best has 140 vertices outside the identity root's radius-three ball. By the proven transitive left group action this corresponds to 76440 bad unordered pairs. The parent's unique independent final saved-edge verification checks all1092 roots and confirms a connected simple twelve-regular graph of exact diameter four; see best.independent_check.json. No claim about the entire group family or a new lower bound is made.

## Construction and parameter choice

Vertices are SL(2,F13)/{+I,-I}; determinant-one matrices number 2184 and give 1092 canonical classes. A matrix (a,b;c,d) has code a+13b+169c+2197d. The representative has the smaller code of M and -M, and identity is reindexed zero. Multiplication is ordinary matrix multiplication modulo13, followed by this canonicalization. The inverse is (d,-b;-c,a), canonicalized. The implementation obtains 91 nonidentity involutions and 500 unordered noninvolution inverse pairs.

For twelve distinct nonidentity generators S closed under inversion, edges are g--g*s. This gives degree12 and 6552 undirected edges. Left multiplication preserves every edge and is transitive, so identity-root radius-three coverage is exact for this diameter target. Order1092 exceeds the saved (12,3) lower bound810 if an actual diameter-three set is found. This arithmetic alone does not establish existence or make the choice optimal.

## Exact finite trial

Seed20261027130 chooses four fresh starts for each composition: six inverse pairs; five inverse pairs plus two involutions; four inverse pairs plus four involutions. Each of the twelve starts has three descent segments. A segment considers all legal replacements in each occupied pair or involution coordinate and takes strict score improvements, up to twelve moves. Between segments, two sequential legal coordinate replacements are applied using seed20261027131; they are not guaranteed to select distinct coordinate slots. No composition conversion, added group, automatic restart, or extra start was used.

All twelve starts and thirty-six segments finished, with154 complete coordinate neighborhoods,118 accepted strict moves,24 two-replacement perturbations, and405530 exact identity-root radius-three evaluations. The first formal start misses266 radius-three targets; the best visited state misses140. These are evaluations and not a distinct-graph count. The entire group family remains open.

## Calibration and saved graph

Python directly expands the first production candidate from matrix tuples, checking all13104 directed adjacencies for simplicity, degree and reversibility, then computes its1092-entry radius-three distance vector. C++ independently builds its matrix product table and compares every entry of that first distance vector. The first score is reused. first_python_check.json and first_cpp_check.json preserve the result.

best.edges is the one saved complete6552-edge graph. best.json records its generators, matrix codes, score and graph parameters; group_definition.json fixes the full vertex labeling. The best uses four noninvolution inverse pairs plus four involutions. Its generator indices are [316,698,394,451,315,822,57,697,725,408,1037,671]. Their matrix codes are [5295,10259,6308,7048,5286,11880,914,10244,10617,6498,14671,9915]. No separate all-source final BFS was run by this producer.

## Cost and terminal state

The single worker completed normally. Preparation including compilation and Python calibration used1.245910 CPU seconds; production used4.839690 CPU seconds; the driver measured6.088338 CPU seconds and6.099718 wall seconds total, below the90 CPU-second budget. No process remains running and there were zero restarts. terminal.json is COMPLETE_12_START_PROFILE_NO_D3 with pending=[] after the parent's completed independent final check. That separate verification used1.072493630 CPU seconds and is not included in the production-driver total. The completed input scope will not be extended here.
