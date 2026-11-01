# Twenty vertices, minimum degree eight, exactly five degree-eight vertices

Let H be a simple five-uniform hypergraph on 20 vertices with 35 edges, covering every vertex pair. Suppose its minimum degree is eight and exactly five vertices have degree eight. Then H has Property B. This is a complete paper-proof candidate for this branch; the complementary case of at least six degree-eight vertices is proved in `../six_conditional/DELTA8_GE6_PROOF.md`.

## Actual choice of a degree-eight center and four unit degree-nine neighbors

Let A be the set of the five degree-eight vertices. The other fifteen vertices have degree at least nine, and

    5*8 + 15*9 = 175 = 5*35.

Thus every vertex outside A has degree exactly nine.

The complete five-eight reduction in `../five_join/` applies to this actual set A: unless an earlier strict certificate already gives a coloring, or the separately proved double-pair core lemma in `../rigid_external/CORE_DOUBLE_PAIR_PROOF.md` applies, its exact trace inventory is one of the 49 residual orbits in `../five_join/FIVE_REMAINDERS.json`. The full domain and its independently recovered 23,995 labels and 361 orbits are certified by `../five_join/replay.py`. No sixth degree-eight vertex is assumed in that reduction.

For each of the 49 residual inventories, the pair energy

    C = sum_{i<j in A} lambda(i,j)
      = sum_T binom(|T|,2) mu_T

is at least 14. The exact range on this complete residual list is 14 through 21; `replay_nines.py` also checks this elementary integer statistic. Choose x in A whose internal codegree row c_x=sum_{j in A minus {x}} lambda(x,j) is maximum. Since the five row sums total 2C, we have c_x>=ceil(2C/5)>=6.

The sum of codegrees from x to all other vertices is 4*d(x)=32. Hence its codegree sum to the fifteen degree-nine vertices is 32-c_x<=26. If h9 of those fifteen vertices have codegree exactly one with x, pair coverage gives

    32-c_x >= h9 + 2*(15-h9) = 30-h9.

Therefore h9>=c_x-2>=4. Choose four distinct such neighbors y1,y2,y3,y4. They all have degree nine and satisfy lambda(x,yi)=1. Only this four-neighbor selection is needed. The center has degree eight throughout the following argument.

## Common unit-star representation

Use the general recovery lemma `proofs/propertyb35/UNIT_STAR_RECOVERY.md`. For any selected s of these neighbors, their unique edges through x define one actual partition Pi of the s neighbor labels: labels are in the same block precisely when their unique x-edge is the same. The eight edges through x have exact selected-lock traces

    n_({x} union B)=1 for B in Pi,
    n_{x}=8-|Pi|.

There are exactly 27 noncenter edges. Write I_U for the inclusive number of edges containing all neighbors indexed by nonempty U. Set J_empty=27 and

    J_U = I_U - indicator(U is contained in a block of Pi).

Their exact neighbor traces are uniquely recovered by

    m_T = sum_{U containing T} (-1)^(|U|-|T|) J_U.

All actual m_T are nonnegative. For the selected s<=4 neighbors every block automatically has size at most four, and a block of size four corresponds to the single actual five-edge through x. Thus the simple-five-edge condition on a full selected trace is already enforced by the central block multiplicity one. A noncenter trace on four selected neighbors may have multiplicity greater than one; no unjustified simplicity constraint is imposed on it.

All projections below restrict this same Pi and the same inclusive counts I_U. They are not independently chosen worst-case inventories.

## Two neighbors: the complete necessary relation

The previously certified 9/9 double-lock table excludes pair codegrees 5 through 9; its five exact certificates are in `../../20-new-high/DIAGNOSIS.json` and are also replayed by `replay_nines.py`. The remaining pair codegree c is in {1,2,3,4}. Two unit neighbors can either belong to the same actual central block or to different blocks. Their inclusive triple count with x is consequently one or zero, respectively.

These eight actual three-lock inventories, with degrees (8,9,9), are the `neighbor_degrees=[9,9]` cases in `UNIT_TWO.json`. Three are strictly excluded: c=1 for either block relation, and c=4 in the same block. All are checked against the explicit recovery above in the independent replay. Thus the complete necessary residual rule for every pair of selected unit-nine neighbors is:

* c=2 or c=3, in either central block relation;
* c=4, only in different central blocks.

The center degree is eight, rather than the degree-seven center of earlier unit-star work; these eight profiles were newly evaluated with the present parameters.

## Three neighbors: 242 complete inventories and 24 residual views

For three selected neighbors, use all five set partitions, all three pair codegrees allowed by the preceding rule, and every inclusive neighbor triple count t with 0<=t<=min(c12,c13,c23). Recover the noncenter inventory by the common formula, retaining exactly the nonnegative integer inventories. This is a complete domain of 242 labelled inventories. It is the all-nine part of `THREE_DOMAIN.json`.

The exact fixed certificates in `THREE_DP.json` strictly exclude 214. Four further labelled inventories are strictly excluded by the repaired rational joint certificates in `THREE_JOINT.json`, with source IDs 306, 339, 380 and 424. The remaining 24 labelled inventories are the all-nine part of `THREE_REMAINDERS.json`. There is no asserted coloring certificate for a non-strict entry: those entries are simply retained as necessary views for the next stage.

These are four-lock calculations, including the center. Fixed-position counts have common denominator 16!. Joint certificates use the same actual bad-pair counts across all chosen layouts, with nonnegative rational layout weights summing to one, nonnegative actual quota multipliers, and their verified capacity penalties. The exact multilock counting inequality therefore gives a coloring whenever one of these certificates is strict.

## Four neighbors: all common views are strictly excluded

Return to the four actually chosen unit-nine neighbors. Their Pi is one of the fifteen partitions of four labels. Choose all six pair codegrees subject to the two-neighbor residual rule. For each of the four neighbor triples, restrict Pi and these same pair codegrees and require its inclusive triple count to belong to the corresponding 24-inventory residual relation. If a triple does not satisfy that relation, its actual smaller set of locks already gives a coloring.

Finally choose the inclusive four-neighbor count q between zero and the minimum of the four triple counts. The one common partition Pi and these inclusive counts determine all 27 noncenter edge traces by the displayed Mobius formula. Retain exactly the nonnegative inventories. This recovers every possible actual input, because every parameter and projection is taken from H itself. It does not require that every retained abstract inventory extends to a whole hypergraph.

The complete common domain has 733 labelled inventories and 78 true S4 orbits, with the center fixed. They are the `neighbor_degrees=[9,9,9,9]` parts of `FOUR_DOMAIN.json`. Each labelled inventory stores a single permutation of the four neighbor coordinates taking its representative to that inventory. All 78 representative inventories have strict fixed-position certificates in `FOUR_DP.json`; no joint certificate is needed at this last stage. These are five-lock calculations, including the center, with common denominator 15!. Their exact maximum bound is

    25667/25740 < 1.

Consequently every actual H in this branch either was colored by an earlier strict certificate or yields one of these 78 strict five-lock inventories. In every case the conditionally random permutation has failure expectation strictly below one, giving a proper two-coloring of H.

## Independent domain recovery and fixed replay

`replay_nines.py` is independent of the original recursive recovery and partition enumeration: it generates partitions by restricted growth strings, reconstructs exact traces by the explicit Mobius sum, and directly enumerates the bounded inclusive counts. It obtains the same 242 three-neighbor inventories, the same 24 residual views, and exactly the same 733 labelled four-neighbor inventories. It independently checks that the 78 stored representatives belong to distinct orbits under the full S4 action fixing x, checks all 733 transport permutations, and binds the 78 final fixed certificates to that exact representative set. It also replays the five old strong 9/9 double certificates, all eight new two-neighbor cases, all 242 three-neighbor fixed certificates and the four accepted rational three-neighbor joint certificates. It uses no DP, LP, SciPy or position search.

The full discovery also retained mixed-neighbor exploratory cases. They are not premises of this proof and need not be read or replayed; the final replay filters and covers exactly the degree-nine neighbor branch above. No fifth selected neighbor and no free six-lock promotion table is required.

Run the complete minimal replay from the project root:

```sh
python3 -B context/propertyb35-paper/round01/middle/twenty-delta8/exact_five_unit_star/replay_nines.py
```

`NINES_REPLAY.json` contains the exact counts, accepted maxima and measured runtime. Its acceptance arithmetic consists entirely of integers and exact rational numbers. This establishes the stated twenty-vertex, exact-five-eight branch and makes no claim about the other vertex numbers of the original 35-edge problem.
