# Fixed7532 diagonal-filler reallocation

This fixed graph keeps all90525 edges of the accepted7242-vertex source H.
Let U be its original7225-vertex opposite-incidence graph, F the17 original
fillers, and C=O17 x spread17 the frozen289 ordered centers. Every clone now
uses the open N_U(c), and a new hub7531 meets every original filler. Relative
to the accepted7531 literal file, exactly the17 incident-flag clone/filler
edges are removed and the17 hub/filler edges inserted. Actual diagonal owners
are the original spread indices, not ovoid indices.

The old JSON raw Cartesian row has25 entries even on a flag, including that
center itself. Its true open U-neighborhood removes the center: diagonal clone
degree24, off-diagonal clone degree25. The producer bound every resulting clone
adjacency to this exact filtered row. The graph has7532 vertices and
90525+(17*24+272*25)+17=97750 edges. Its measured histogram is
{17:1,24:17,25:289,26:7225}, with maximum degree26.

## Diameter routes, using old-source interiors

The inherited GQ projection property proves U has diameter at most3. For
u=(p,l),v=(q,m), take projections r in l on a line k through q, and s in m on
a line n through p. The incidence-valid sequence
u,(r,n),(s,k),v has length3; remove consecutive equal vertices to obtain a true
Walk. Every U vertex has a neighbor (raw degree24 or25). Thus the already proved
FullNeighborhoodClones Walk argument applies to U and any prefix of these
modified clones. It covers all U/clone pairs, including adjacent centers; no
center-independence assumption is used.

Pairs contained in H keep their old source paths. For a filler f_j and clone
of c, take a shortest H-path from f_j to c. If it ends through an old U vertex,
replace c by the clone. The only problematic direct source adjacency is a
diagonal flag c=(p,S_j) incident to this same filler. Choose another line m
through p, m!=S_j. The flag (p,m) lies both in the filler pinset and in N_U(c),
so f_j,(p,m),clone(c) has length2. For a different filler, a shortest length3
path cannot end through the center's own filler: that would require one flag
belonging to two distinct original filler pinsets, impossible for a spread.
If c is nonflag it has no filler neighbor at all. These cases exhaust every
filler/clone pair and use no other clone as an interior vertex.

The hub reaches each filler in1 and each old flag in2 through its owning
filler. For a nonflag old u=(p,l), projection gives a flag x=(q,m) with
q in l and p,q in m; x is an old U-neighbor of u and has an owning filler.
Thus hub,filler(x),x,u has length3. Each clone likewise has an old flag in
N_U(c): use projection for nonflag c, and another point/line on the incident
flag for diagonal c. The same3route reaches that clone. The producer supplies
289 explicit hub/filler/flag/clone Walk rows, without BFS.

Together these give diameter at most3. An actual old-U pair[0,21] is a
nonedge and has no common neighbor in the produced graph; the two small
neighbor lists are saved in NON_D2_OLD_U_WITNESS.json. This direct intersection
check used no BFS. Independently, n7532 exceeds the cap26 diameter-two Moore
bound677. Hence the resulting diameter is exactly3.

## Prefix and scope

Prefixes start from H and append modified raw-U-neighborhood clones, then the
hub. All routes above use H/U interiors plus the specified endpoints; no
future clone is required. Degree only increases to the displayed final bounds.
This does not delete edges from a supposed immutable7531 prefix. It changes
the generation rule by omitting17 full-H clone pins while preserving H, so it
does not contradict the previous mandatory-full-N_H augmentation obstruction.

Production used0.195131966 CPU/20, one input parse, no compilation, BFS, field,
geometry, Lean, solver or hashing. This draft is the producer's argument, not a
Lean proof or independent acceptance receipt. The separate fresh agent owns
the actual290 new-root BFS and literal delta check. No root counts, reports,
progress/recovery files or old frozen packages were changed here.
