# Exact42-vertex port template, prepared CNF, and its uniform obstruction

This is a fixed template, not all42-point graphs. It is not restricted to Cayley graphs. The previous Fano35 splitting family and ordinary-cover exclusions have different vertex sets and connection rules. In particular, adding helper vertices and extra old-port edges breaks the ordinary covering-map model; this42-point graph would not be merely the39-point ordinary3-cover.

## Prepared structural domain

The base points are the13 normalized projective vectors in F3^3. Distinct points are adjacent exactly when their standard dot product is zero. Actual construction gives24 edges, four absolute points of degree3 and nine other points of degree4. Absolute points are mutually nonadjacent. The39 old vertices are(v,s), s in C3. Every oriented base edge u<v has a cyclic shift lambda_uv, and creates edges(u,s)--(v,s+lambda_uv). Opposite orientation uses the negative shift.

A canonical spanning tree has12 edges. Independent relabeling s->s+c_v changes lambda_uv to lambda_uv+c_v-c_u, so tree shifts can all be fixed to0. This loses no graph in the cyclic-lift port family: all12 absolute ports and their helper attachments/old-port pairs are otherwise arbitrary, and that domain is invariant under such relabeling. The other12 shifts remain ternary. No further phase, graph symmetry or attachment is fixed.

The three helpers39,40,41 have fixed path39--40--41. End helpers attach to three old ports each; the middle helper attaches to two. Each of the12 old absolute lifts has exactly one new incident edge. Thus there are eight helper spokes and two remaining old-port matching edges. All assignments satisfying these degree conditions are simple4regular42/84 graphs, but their diameter is not assumed.

There are36 shared shift-selector Boolean variables and102 independent port-edge variables, total138. The102 port edges are all66 unordered pairs of the12 ports plus all36 port-helper pairs. A chord selector is shared by its three lift edges, rather than allowing those edges to vary independently. Potential edges total248:36 fixed old tree edges,108 conditional chord edges,102 port edges and2 fixed helper edges. Every structural assignment selects72 old lift edges and12 additional edges, total84. Its exact labeled domain has3^12=531441 shift assignments and831600 port completions, product441946335600. These numbers describe the domain, not attempted cases.

## Exact existential path encoding

For each unordered pair u,v, Y_uv denotes a selectable claim of distance at most2. A fixed old/helper path of length at most2 can make it a constant true. Otherwise the compiler requires

    Y_uv -> X_uv OR over w of W_uwv,
    W_uwv -> X_uw and X_wv.

For each unordered pair, diameter3 requires

    Y_uv OR over w of Z_uwv,
    Z_uwv -> X_uw and Y_wv.

Identity may be included in closed reachability; the compiler instead omits the redundant w=v term because the direct edge is already in Y_uv. X literals are either true fixed edges, false impossible edges, or the correct shared structural selector. Both Y and every W/Z witness can be true only when a real corresponding path exists. Reverse implications are unnecessary: any actual D3 graph extends to an auxiliary assignment by choosing valid reachability claims and their true witnesses. This proves exact existential equivalence, not merely a sufficient sampled test.

The prepared file has8436 variables and19048 clauses, of which2506 are structural. It was never supplied to a solver. INPUT.json, VARIABLE_MAP.json and REACH2_MAP.json bind every vertex and literal; decode.py would require a full satisfying assignment, check every clause, reconstruct all84 edges, and check actual degrees and all42 roots before exporting a candidate. That decoder was not invoked.

## Uniform external-target obstruction: no SAT is needed

The base coordinates split by the number of nonzero entries: four absolute points A(weight3), six secants S(weight2), and three external points E(weight1). The actual adjacency classes are

    A: three S neighbors,
    S: two A neighbors, one S neighbor, one E neighbor,
    E: two S neighbors and two E neighbors.

Every A/E base pair has exactly one A--S--E two-edge path. ROUTE_CLASS_CERTIFICATE.json binds all12 such paths and their signed shift expressions to the constructed base. Consequently each absolute lift has exactly one old two-step route to a lift over each of the three E base points. A helper spoke to that absolute lift can cover at most three of the nine external old lifts within3 steps.

All nonabsolute old lifts already have degree4. Every absolute old lift has only one free slot. Therefore the only new old neighbors of a helper can be absolute ports, each assigned to at most one new edge. Any length<=3 path from a helper h to an external old point must be

    h -- absolute port -- old secant lift -- old external lift.

Starting with a helper edge leaves only two steps, and an absolute port has no external neighbor. A port joined to h cannot also use an added old-port matching edge, because its unique free slot is already occupied. The other apparent short detours are consequently impossible. Thus helper h needs at least three direct spokes to cover all nine external lifts. With maximum degree4 its internal helper degree is at most1.

For the fixedP3 template, the middle helper has internal degree2 and only two spokes. It can cover at most6 of9 external lifts in3 steps, leaving at least3, uniformly in every shift and port assignment. This is a uniform lower bound, not an ordinary bad-pair count from a chosen graph.

The same argument excludes a stronger template: retain all39 old lift edges and add any three helpers, with any new edges that respect old/new maximumdegree4. Each helper still requires at least three spokes, so their internal graph H has maximum degree1. But D3 would force H to be connected. Indeed, a helper-to-helper path of length2 through one old port would assign two new edges to that port; a length3 path through two old ports would need an old absolute-absolute edge(which does not exist) or a new old-port edge at ports already used by spokes. A path using one intermediate helper and an old port has the same double-spoke violation. Hence no length<=3 route through old vertices connects distinct components of H. On three helpers maximumdegree1 is disconnected, so some helper pair necessarily has distance greater than3 in the full graph, even if the full graph is connected by longer paths.

This is a strict exclusion of the three-helper free-port completion family for this39-lift source, not of arbitrary42-vertex graphs, changed old lift edges, other helper counts or other bases. The original CNF and its preparation data are retained unchanged as a model artifact; no SAT call, voltage enumeration, expanded candidate or graph BFS is required.
