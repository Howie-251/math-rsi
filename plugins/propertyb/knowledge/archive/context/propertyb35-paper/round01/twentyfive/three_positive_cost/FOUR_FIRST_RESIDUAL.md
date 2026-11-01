# First four-positive count residual: actual degree budget removes it

The authorized bounded screen stopped at its first nonstrict input, after77 of23393 marked states, in0.016 seconds. The first76 states satisfy its strict necessary-count test; they have not been promoted to a completed four-positive gate. The remaining23316 states were not processed. The residual is not an actual H. Its genuine additional obstruction can be excluded using the common blue degree budget.

The four positive sets are

A_1={0,1,2,10}, A_2={3,4,9,10},

A_3={5,6,9,10}, A_4={7,8,9,10},

with forbidden singleton points F={9,10}. Their repeated-positive-incidence surplus is5. The free positive parts are four disjoint sets of sizes3,2,2,2 on U={0,…,8}. There are exactly24 minimal transversals, each of size4. Each point of U has positive multiplicity1.

The weak cost-only model really can block all of them: use two negative singletons F and use each of the24 transversals itself as a negative four-set, then duplicate two four-sets to get28 indexed negative sets. This satisfies9n_1+4n_2+n_3≤24 and3n_1+2n_2+n_3≤8, but it is merely a signed-set construction. It violates the actual common vertex-degree budget.

To exclude **every** blocker at this positive state, let p,t count the useful negative pairs and triples, those contained in at least one of the24 candidates. Discarding other negatives only weakens the two budgets. Here n_1≥2, so

4p+t≤6, 2p+t≤2.

Thus the only possibilities are(p,t)=(0,0),(0,1),(0,2),(1,0). A pair covers at most6 of the24 candidates, and a triple covers at most3. A negative four-set covers at most one, so at least

24−6p−3t

useful negative four-sets are required. All useful negative sets are subsets of U. Their total indexed incidence on U is at least

2p+3t+4(24−6p−3t).

For the four possible(p,t) this is96,87,78,74, respectively. Positive edges and negative edges are different original edges: positives contain the chosen center g, negatives avoid it. Consequently

Σ_(x∈U)d(x) ≥9+74=83.

For the actual24-point35-edge minimum-degree-seven branch, total excess is5·35−7·24=7. Therefore every nine-point subset has degree sum at most7·9+7=70, contradiction. The bound can be strengthened to70−(d(r)−7) for these blue points, but that is unnecessary here. Equivalently, this residual would require at least20 excess on U, exceeding the entire actual budget7.

The useful-negative counting argument does not require their edges to have freely assignable G-traces or their incidence maxima to be simultaneously attainable. It upper-bounds their coverage independently, so it is a valid outer relaxation and the resulting contradiction remains sound.

`FOUR_RESIDUAL_CHECK.py/json` independently generates all four-subsets of U, verifies the24 candidate transversals, checks that none has a proper transversal subset, computes the exact maximum pair/triple coverages6 and3, and replays all four feasible small-blocker count choices. It imports no screen or profile code and uses only the standard library. This is an exact local proof of this one residual, not a full m4 classification.

The stopped screen is `FOUR_SCREEN.py/json`. Its complete candidate domain has798 distinct-positive Venn families under surplus≤5 and23393 F-cell markings, but the actual processed scope remains77 states. Continuing it with the new degree filter would constitute a new stronger test, not a completed result already obtained here.
