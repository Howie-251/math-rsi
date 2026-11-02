# One old-old repair edge: endpoint route prediction

Use the actual public106/582 max11,D2 source, not the old Brown91 source.
The earlier minimal4-matching rule is closed by its saved forcing certificate.
The user now explicitly authorizes modifying old edges. This batch changes
the rule to5 deleted matching edges, one added old-old nonedge, and one new
degree10 point. Final target remains107/588 with all old degrees11.

For each of the21 saved minimal candidate edges a-b and each directional
forced critical target k in K={7,23,46,59}, choose repair edge a-k. Delete
a-b and k-l, where l ranges over its actual source neighbors and the two
edges are disjoint and avoid T={34,54}. Add a-k. In this rule a,k use their
freed slots for the repair and are NOT neighbors of the prospective newpoint.

Falsifiable prediction: at least one such anchor preserves the two-step
coverage from BOTH a and k to all106 old vertices. The addition must repair
the specifically predicted missing pair(a,k). If an endpoint still misses
any old vertex, the remaining three deletions and a newpoint not adjacent
to that endpoint cannot repair it. Save a concrete counterexample per anchor.

For the independently suggested anchor(64,0,7), predict that every allowed
l fails: the old pair64--5 had only common neighbor0; the added64--7 cannot
replace it because7 is not adjacent5. This is a route-class prediction,
not a count of total bad pairs.

Whole-case cumulative20CPU budget includes the previously measured source
preparation and minimal4 attempt costs, all preparation and this batch. One
process, no solver/BFS, no new graph/field/Lean or old-source distance rerun.
Enumerate this anchor domain once. A passing anchor is only a necessary
interface; no complete107 graph is claimed without its remaining obligations.
