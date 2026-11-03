# Controlled success: five helpers cooperate, while the first prefix fails

2026-11-01. The one authorized small Python experiment matches **every
predeclared prediction** in `PREDICTION_AND_SCOPE.md`. It is a mechanism
calibration, with zero portfolio graphs, new parameters or concrete Lean
increments. It is outside the three existing graphs' C review scope.

The exact reproducible recipe is `run_once.py`, with the15 literal adjacency
rows and label conventions in `PARAMETERS.json`. No geometric isomorphism of
this literal relation is assumed or claimed. The sole run used
0.027416 CPU seconds from process resource usage under a5-second CPU limit,
one worker. No field, old graph, geometry, Lean, solver, web, paid review,
hash or extra independent audit was used.

## Literal relation and source

The relation has a_i=i, u_i=5+i and v_i=10+i, i modulo5. It has exactly the
five absolute loops, a_i–u_i, a_i–v_i, the outer u5-cycle and the inner
v-pentagram. All15 adjacency rows have3 entries, the relation is symmetric,
and direct integer multiplication checks

    A^3 = 4A + J

on all225 ordered pairs. Distinct a_i have no edge or common neighbor; their
three-entry closed neighborhoods partition all15 vertices. These are checks
of this literal finite relation, not inherited field claims.

The simple product S has label15x+y and adjacency between distinct labels
exactly when the two coordinate factor adjacencies hold. Only whole-product
self-loops are dropped. The complete table `source_product_n225.edges` has
header225 1000, degree8 on25 absolute-products and degree9 on the other200
vertices. Their25 open8-neighborhoods partition the200 noncenters.

Every entry of A^3 is positive, so any two ordered factor vertices admit a
three-step relation walk. Combining two such walks gives a product
three-walk for every pair of S vertices, with possible whole-vertex loops.
Deleting consecutive repeated vertices removes those loops and gives a
genuine simple-graph walk of length at most3. This establishes the old
source's diameter upper bound without running any old/source-root BFS.

## Joint helper construction and all-pair route coverage

For each i=0..4 add h_i=225+i and the five pins

    h_i -- (a_i,a_j), j=0..4.

Put a K5 on the five helpers. The complete final table is
`graph_d9_D3_n230.edges`, header230 1035. All1000 source edges are retained;
25 pins and10 helper edges are added. Each source center changes degree8 to9,
every other old vertex stays degree9, and each helper has5 pins plus4 helper
neighbors, giving simple9-regularity.

The old-old walks remain. A helper reaches an old absolute-product in its
own row in one step, and any other row in two via that row's helper. Every
noncenter old vertex has a unique absolute-product neighbor c. If c is in
row i, h_i–c–x has length2; otherwise h_i–h_k–c–x has length3. Helpers are
mutually adjacent. Thus the entire joint construction has diameter at most3.

Exactly one ordinary BFS was run for each of all230 final roots. All roots
have eccentricity3 and exactly the predeclared histograms:

|root class|number of roots|distance histogram0,1,2,3|
|---|---:|---|
|helpers|5|(1,9,60,160)|
|old both-absolute or both-nonabsolute pairs|125|(1,9,48,172)|
|old exactly-one-absolute pairs|100|(1,9,46,174)|

`FINAL_ROOT_HISTOGRAMS.tsv` preserves each root separately. The actual
distance3 witness0,7 and all positive third layers establish exact diameter3,
not merely an upper bound. There were no prediction mismatches.

## The controlled one-helper prefix

`prefix_one_helper_n226.edges` contains S and only h_0's five pins, with
header226 1005. One radius3 BFS was run from225, yielding exactly

    (1,5,40,60), total106 reached,120 missed within radius3.

`PREFIX_ROOT_DISTANCES.tsv` records every label's bounded distance; its−1
entries mean beyond the tested radius, not disconnectedness. The prefix
therefore fails diameter3. The final construction cannot be described as a
sequence of valid individual diameter3 additions: its helper edges use the
other new helpers' pins to supply complementary row coverage.

This small example explains how a coordinated batch can succeed while its
first single-point prefix fails. It does not make the q2×q8 source or cap31
feasible, does not override the supported cap27..30 barrier for that other
source, and starts no new parameter or template queue. RESULT/TERMINAL are
complete; root counts, Wiki and frozen artifacts are untouched.
