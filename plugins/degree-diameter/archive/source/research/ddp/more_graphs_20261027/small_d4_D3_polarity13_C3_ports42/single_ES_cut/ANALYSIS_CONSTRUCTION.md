# Single E-S cut: valid positive lemma and encoding, but a uniform old-old obstruction

The degree accounting, voltage gauge, c-root guarantee and exact reachability encoding are **VALID**. Nevertheless this fixed single-cut family cannot have D3: the old cross-E fibre obstruction below survives every voltage and port assignment. This is a paper exclusion, not a solver UNSAT. No SAT call, graph assignment, BFS or word enumeration is executed by this review.

## The exact prepared subfamily

Start with the same C3 lift of the loopless13-point F3 dot-product polarity graph. The old classes are12 absolute ports A,18 secant lifts S and9 external lifts E. Choose the base E-S edge(0,7), force it into the gauge tree, and delete only its sheet-zero lift e-s=[0,21]. The other two lifts of that base edge are retained.

Add helpers a=39,b=40,c=41 with edges a-b-c. Add e-a, and connect c to all three lifts[24,25,26] of the fixed absolute base point T=8, which is not adjacent to base S=7. The released S endpoint s is paired to exactly one of[27,28,29], the lifts of the other absolute base point nonadjacent to S. Helpers a and b each take two further absolute spokes, from the nine ports outside T. The remaining four absolute ports form two old-old matching edges.

This is the concrete subfamily bound by [INPUT.json](INPUT.json). In particular, it is not all single-edge cuts, all choices of T, or all legal released-S neighbors. The nonadjacent-base restriction is sufficient to avoid an already existing S-A edge; other unused sheet pairs over adjacent bases are not included by this model.

There are14 freed old slots: the original12 A ports plus e and s. Eight helper spokes and three new old-old edges use8+6=14 slots. There are71 retained old edges, two internal helper edges, eight spokes and three old-old edges, giving84 edges on42 vertices. Every vertex has degree4. The fixed T ports and e already use their added slot; the nine remaining A ports and released s have exact-one new-port constraints. Helpers a,b each have two conditional A spokes, while c has its three fixed T spokes.

## The gauge and c's full-root guarantee are sound

The original connected13-point base has24 edges. A spanning tree containing the cut base edge has12 edges; its voltages can all be made zero by independent fibre relabelling. Fix the root-fibre translation so the selected deleted lift has sheet zero at e. Since its base edge is in the tree, the other endpoint then also has sheet zero. The twelve chord trits remain free.

This gauge preserves the fixed base edge and T, maps the singled-out e-a edge to the declared label, and preserves the full T fibre as a set. All remaining allowed A-port pair/spoke domains and the three S-pair options are permuted within their base fibres. It is lossless within this fixed geometric rule, not an assertion that every one-cut42-vertex extension belongs to it.

The loopless polarity base has diameter at most2: the perpendicular lines of two nonadjacent projective points meet in a common neighbor. T is adjacent to neither endpoint E nor S of the cut base edge. Hence no base path of length at most2 starting at T can use that edge: such a path would need its first edge to reach one of those endpoints. In particular, T's unique two-step route to the cut E uses the paired secant S', as the prepared certificate records.

For any old target base point, choose a length<=2 base path from T. It avoids the cut base edge. Lifting that path is a bijection between the starting T sheets and target sheets. Since c is attached to all three T sheets, every one of the39 old targets is within3 steps of c, for every voltage assignment. The other helpers have fixed paths c-b and c-b-a. Thus c has full radius3 coverage of all42 vertices independently of the remaining ports. [C_FULL_FIBER_GUARANTEE.json](C_FULL_FIBER_GUARANTEE.json) records the cut-avoiding base paths without enumerating voltages.

This is a radius3 fact, not a radius2 fact. It neither permits all Y2(c,v) flags to be true nor proves old-old or a/b coverage.

## What the changed E budget really establishes

For b, two A spokes supply at most six E endpoints through b-A-S-E: at most two per external base fibre. The fixed b-a-e route supplies e, and its extension through e's two E neighbors supplies one endpoint in each other E base fibre. These three buddy endpoints plus the six A-route endpoints make the old upper bound exactly nine instead of six.

To cover all E targets, the three endpoints in each external base fibre must actually be distinct, and neither relevant A-route may have been destroyed by the cut. This is a meaningful capacity improvement but is only a b-root condition. The old no-cut theorem is not applicable: e can now attach directly to a helper and s to a new A port, violating its saturated-E/S premises. A separate old-old obstruction must still be checked.

## Prepared code remains an exact graph model

The inspected [compile.py](compile.py) imports only the previous CNF helper class, without running the old builder. It uses one selector for all three edges of a chosen chord shift, retains35 fixed tree-lift edges after the cut, and adds the six fixed new edges described above. The57 port selectors consist of36 A-pair choices, three released-S choices and18 a/b spokes. Together with36 shift selectors, the structural model has93 variables and682 clauses.

The structural conditions select71 old plus13 new edges. [MODEL_STATS.json](MODEL_STATS.json) reports206 potential edges,41 fixed edges,6403 total variables and13226 clauses; these are a prepared model, not a chosen42-vertex graph.

The generic two-stage reachability encoding is retained. A Y2 flag implies a real direct edge or a sound two-edge conjunction. A three-route conjunction implies its first selected edge and a sound Y2 suffix. These dependencies are acyclic and cannot invent a path. Conversely any genuine D<=3 structural assignment extends by its actual radius2 flags and enabled conjunctions. Only fixed paths of length<=2 are made constant Y2=true. The c radius3 lemma is not used to strengthen a Y2 flag, and all diameter pair obligations are retained in the generic encoding.

The inspected [decode.py](decode.py) checks all clauses and reconstructs edges only from structural potential-edge literals. Reachability auxiliaries never become graph edges. A later SAT witness would trigger its full42-root check, but no such witness or graph is produced here.

## Decisive cross-E obstruction

Let the three external base points be E0,E1,E4. They induce a triangle, whose C3 lift is the unchanged nine-vertex E subgraph. Consider a simple path of length at most3 between vertices over different E base points.

If it leaves the E subgraph, a two-step E-S-E path must return to the same actual E vertex, since each S lift has at most one E neighbor. The analogous E-a-E path also returns to e, the only E neighbor of a. Neither gives a new simple path.

For a three-step path with both intermediate vertices outside E, each intermediate endpoint next to E is either S or a. An S-S edge is only the old paired-secant edge, whose two S bases have the same E base neighbor. It therefore cannot connect different E base fibres. There is no S-a edge. Paths through A cannot end with A-E, and a-b cannot end at E because b has no E neighbor. The new s-A edge does not change any of these facts.

If exactly one intermediate vertex is in E, the remaining E-S-E or E-a-E excursion is just a backtrack, reducing to an already counted pure-E edge. These cases exhaust simple paths of length<=3 that leave E.

Thus all short paths between different E base fibres lie entirely in the triangle lift. Such a path has only two possible target-sheet images: the direct edge, or the two-edge route via the third E base point. A nonbacktracking three-edge triangle walk returns to the starting base, while a three-edge walk with backtracking reduces to the direct edge. At most two of the three vertices in the other E fibre can therefore be reached.

This argument is independent of the other eleven chord trits, every port choice, and the c-root guarantee. It proves D>3 for every structural assignment in the prepared family.

In the actual tree gauge, the E0-E1 and E0-E4 voltages are zero. Write tau for the E1-E4 chord voltage. From root0=(E0,0), the E1-fibre images within3 steps are contained in {0,-tau}. If tau is0 or1, old vertex4=(E1,1) is missing; if tau is2, old vertex5=(E1,2) is missing. This is a symbolic old-old counterexample, not a generated graph or a measured larger diameter.

## Terminal scope

The c-positive lemma and exact CNF are compatible with the failure: one new root can reach every old vertex in3 steps while some old-old pair still needs more than3. The family is strictly excluded by the cross-E argument; SAT remains unexecuted, rather than UNKNOWN or raw solver UNSAT.

The conclusion concerns this fixed E-S base cut, deleted lift, T, e-a connection, P3, and released-S/A matching rule. It does not exclude arbitrary42-vertex graphs, other one-cut completion rules, or additional changes creating new short cross-E routes. The original no-cut exclusion remains valid and separate. No automatic second cut, new helper pattern, voltage sweep, or solver call is proposed by this review.
