# Frozen prediction: the extra degree budget is necessarily saturated

Scope: a simple graph on 64 vertices containing eight specified, disjoint copies of Q3. Write I for their 96 cube edges and E for all remaining edges, and assume maximum E-degree at most 2. Extra edges may join vertices in the same pencil. No symmetry, voltage, permutation, or affine hypothesis is imposed.

Prediction, before the local arithmetic check: if a vertex u has E-degree s at most 1, at most 18s + 36 vertices outside its own pencil can be within distance 3. In particular, s = 1 gives at most 54, whereas there are 56 outside vertices. Hence diameter at most 3 forces every E-degree to equal 2; E is already a spanning 2-factor and the whole graph is 5-regular.

Proposed proof: classify shortest routes by the number of initial cube edges before their first extra edge. For zero, one, and two initial cube edges the respective bounds are 18s, 30, and 6. The key correction to a word count is that Q3 has only three distance-two vertices: the six nonbacktracking words using two different cube flips occur in pairs. Immediate reversals supply no new endpoint.

Planned check: enumerate only the eleven I/E word types of length at most 3 containing E, and the nine ordered pairs of cube flips at one abstract Q3 vertex. Check the first-exit partition and the arithmetic 18 + 30 + 6 = 54. No 64-vertex graph, graph family, BFS, SAT call, or random assignment is to be generated.

Budget: one worker, at most 15 CPU seconds. Stop once the route classification proves or refutes the prediction. Existing UNKNOWN solver outcomes remain UNKNOWN; this task changes only the justification of the degree constraint.

Read scope: current AGENTS.md and NEXT_SESSION.md entry; the q8 K64 cube/external-factor ledger entry; PREDICTION.md in q8_K64_external_factor_sat and q8_cyclic_orbit_sat; expert_review_current/EXPERT_HANDOFF_20261029.md section 4. No other historical family was reopened.
