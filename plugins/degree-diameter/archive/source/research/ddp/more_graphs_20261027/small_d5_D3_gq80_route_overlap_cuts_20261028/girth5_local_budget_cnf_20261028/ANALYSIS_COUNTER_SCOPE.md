# Local-budget counter: existentially exact and edge-safe

Verdict: **VALID**. The sequential-unary clauses encode at-most-three exactly under existential quantification of their auxiliary variables. The actual worker allocates disjoint auxiliary blocks after the1080 edge variables and never decodes them as graph edges. This review reads the new code and producer calibration evidence only; it runs no solver, truth-assignment calibration, BFS, graph, or old geometry audit.

The base is the complete35720-clause girth>=5 GQ80 CNF. Its [scope proof](../girth5_cnf_20261028/ANALYSIS_GIRTH_SCOPE.md) already establishes the pointwise route budget. For every point or line root x, let a_x count selected own-side matching edges entirely inside its12 old collinear neighbors. The26 old-far targets other than its matching mate need own-first, own-last, or opposite-relay routes, whose capacities give

    26 <= 8 + (12-2*a_x) + 12,
    a_x <= 3.

There are54 eligible noncollinear matching variables in each such near set. This is a necessary condition on every integer model of the existing girth5+D3 formula, not a new restriction on feasible target graphs. It is not asserted for all girth5 graphs without the D3 requirement.

## Exact meaning of one counter

For input bits x_1,...,x_n, [counter_encoding.py](counter_encoding.py) allocates three flags s_i,j for each i=1..n and j=1,2,3. Their IDs are

    s_i,j = first_aux + 3*(i-1) + (j-1).

It writes the implications x_i=>s_i,1, s_(i-1),j=>s_i,j, and x_i AND s_(i-1),(j-1)=>s_i,j for j=2,3. Flags with j>i are forced false. For i>=2 the overflow clause forbids x_i AND s_(i-1),3.

If a prefix has at least j true inputs, these implications force s_i,j true, by induction on i. In particular, before a fourth true input the flag s_(i-1),3 is already true, so the fourth input violates the overflow clause. Thus no auxiliary assignment can satisfy a counter whose input has weight above3.

Conversely, for an input assignment of weight at most3, set s_i,j true exactly when its first i inputs contain at least j true values. This satisfies all input, carry, promotion, boundary-false, and overflow clauses. Hence such an input always has an auxiliary extension. Therefore

    exists auxiliary flags satisfying Counter(x,s)
        iff sum_i x_i <= 3.

The flags need not have unique values in every satisfying assignment. Their one-way implications are sufficient because the property required is existential equivalence, not unique counter reconstruction.

For n=54, there are162 auxiliaries and375 clauses:54 input implications,159 carry implications,106 promotions,53 overflow clauses, and three impossible-threshold units. The producer's [COUNTER_CALIBRATION.json](COUNTER_CALIBRATION.json) reports all510 input assignments for n=1..8 passing, plus seven deterministic54-input controls covering zero through three true values, four early/dispersed or late true values, and all inputs true. Legal inputs were checked with the constructive prefix assignment, and overflowing inputs by unit-propagation contradiction. These checks use no external solver. This review does not rerun them; the general proof above supplies the arbitrary-n justification.

## The whole formula preserves the integer graph family

Let Phi(E) be the original girth5+D3 CNF on the1080 edge bits. Let X_r be each root's54 relevant edge bits and S_r its fresh counter flags. The new formula is

    Phi(E) AND all_r Counter(X_r,S_r).

If the new formula is satisfied, its unchanged base clauses imply Phi(E). If Phi(E) is satisfied, the previously proved route budget gives weight(X_r)<=3 for all80 roots. The canonical prefix assignment above extends each counter, and the auxiliary blocks are disjoint, so the extensions coexist. Consequently

    exists all counter auxiliaries: new_formula(E,S)
        iff Phi(E).

Thus every original feasible girth5/D3 graph is preserved. The added clauses can change propagation and search behavior, but neither select a special matching nor create a smaller integer graph class. No implication to the unrestricted GQ80 family or arbitrary(5,3) graphs follows from this encoding change.

## Actual IDs, row inputs, and SAT decoding

The actual [worker.py](worker.py) retains the prior dense edge mapping1..1080. For each of the80 roots, it takes precisely those allowed own-side matching records whose two endpoints lie in the cached near12 set. It asserts54 distinct input IDs. No old geometry is regenerated for this step.

The first counter starts at1081; each subsequent block starts at the previous last_aux+1. The80 blocks occupy1081..14040, with12960 auxiliaries in total. There are30000 added counter clauses, giving65720 clauses and14040 total variables. [COUNTERS.json](COUNTERS.json) records per-root inputs and ranges; [MODEL_STATS.json](MODEL_STATS.json) records these totals.

The SAT parser accepts and checks all14040 variable values and all65720 clauses. Graph reconstruction, however, iterates only over the inherited1080 edge records. Each selected record is mapped back through original_variable_id, and the line-side vertex IDs receive the original offset40. The selected_edge_DIMACS_variables output likewise contains only edge records. Auxiliary truth values are never interpreted as selected edges, matching endpoints, or graph vertices.

The worker rechecks original matching degrees and coverage clauses, rectangle constraints, all80 a_x counts, and the resulting graph's degree and absence of triangles/four-cycles before exporting a candidate. There is no missing+1 or auxiliary remapping bug in the inspected code.

## Terminal interpretation

The producer reports the single authorized call ended UNKNOWN with no candidate or graph BFS; the actual outcome is retained in [RESULT.json](RESULT.json). That outcome neither refutes the girth5 template nor the unrestricted GQ80 family or parameter. Raw solver UNSAT without a checked proof would also remain uncertified. A future SAT witness would be only a candidate until the parent's one independent complete80-root graph check.

This paper adds no solver call, calibration run, graph, independent method, or new geometric premise. The evidence belongs to the existing GQ80 mechanism's same girth5-family strengthening window. No additional encoding, time extension, or template is proposed here.
