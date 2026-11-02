# Paused GQ80 overlap derivation: conditional girth-at-least-five obstruction

Status: paper derivation formed before the latest user steering, saved for root review; not independently accepted or promoted to a certified whole-model exclusion. Work on this branch is now paused. No graph, BFS, MILP/SAT, or random experiment was run.

Scope: W(3,3) incidence graph plus a point perfect matching and a line perfect matching. Assume every matching edge joins a noncollinear point pair or disjoint line pair, and the augmented graph has no 4-cycle. These conditions follow if its girth is at least 5. General models with triangles or 4-cycles remain open.

Use the saved exact 1080 cover clauses. Each far matching edge occurs in 17 own-side clauses and 12 opposite-side clauses, so all 40 selected edges give exactly 1160 clause occurrences. If all clauses were covered, total occurrence excess would be R=1160-1080=80.

For any clause, let a be its number of selected own-side matching variables and b its number of selected opposite-side relay variables. Then 0<=a<=2 and 0<=b<=4. The direct-matching clause has only one distinct own variable, which is within this bound. If the clause is covered, a+b>=1 and

    a*b <= (8/5)*(a+b-1).

The maximum ratio is 8/5 at a=2,b=4; the inequality also holds when either factor is zero. Thus total mixed own/relay variable-pair overlap is at most (8/5)R=128.

On the other hand, each of the 160 original incidence edges v--L produces at least one distinct mixed overlap. Let {u,v} be its point-matching edge and {L,M} its line-matching edge. Since both matching edges are far, neither point is incident to both lines and neither line contains both points. A second endpoint incidence would therefore give the forbidden mixed 4-cycle, so v--L is the unique incidence between these two matching edges.

Project u onto M in the GQ: let w be the unique point of M collinear with u, and let N be their line. The mixed 6-cycle is u--v--L--M--w--N--u. If v and w are noncollinear, their point clause contains both selected variables {u,v} (own) and {L,M} (relay). If L and N are disjoint, their line clause contains both selected variables {L,M} (own) and {u,v} (relay).

These two far conditions cannot both fail. Otherwise v is collinear with w and L meets N at z. Since M is disjoint from L, w is not on L; both v and z would be points of L collinear with w. The unique-projection axiom gives v=z, so u and v lie on N, contradicting that their matching edge is far.

Consequently each original incidence yields at least one mixed (clause,own-variable,relay-variable) overlap. Different incidences correspond to different pairs of matching edges because each such pair has at most one endpoint incidence. Hence these are at least 160 distinct overlap triples, contradicting the upper bound 128. Equivalently, mixed overlap forces R>=100 while only R=80 is available.

If root accepts the injection and occurrence counts, this excludes the girth>=5 subclass and shows a D3 construction in the unrestricted model would require a triangle or 4-cycle. It does not settle the unrestricted 41-variable model. The earlier root NB3/C5 budget is not needed for this argument. No further short-cycle classification is undertaken: latest steering concentrates current work on short-path affine-subspace complementarity on the fixed 72-controller.

Evidence: wave11/gq80_paired_matchings/model.json and constraint_schema.json; wave11/gq_commuting_obstruction/REPORT.md. This report records completed reasoning, not a fresh computation or a new graph result.
