# Exact optimum10 for open-neighborhood packing in the fixedC78 controller

The input is the one accepted78×6controller table, read from `../../PARAMETERS.json`. The independent implementation also rebuilds that same table from the three-baseZ26 rules and parameters(2,6,17,5,10), then compares all468entries. No other controller or parameter is searched.

## Actual witness

The maximum packing found is

    U=[31,32,44,45,59,60,61,72,73,74].

Its ten literal open neighborhoods contain60distinct vertices. Every one of the45pair intersections is empty; the actual six targets perselected vertex are recorded in `SELECTED_OPEN_NEIGHBORHOODS.tsv`, and all45intersection counts are in `PAIR_INTERSECTION_CERTIFICATE.tsv`. The sorted covered and18uncovered targets are stored in `SEARCH_RESULT.json`.

Adjacent selected vertices were allowed, as the task requires. Indeed the selected induced graph is5K2, with edges

    (31,44),(32,45),(59,72),(60,73),(61,74).

Thus this is not an ordinary independent-set calculation. It is a packing of open neighborhoods.

## Paper upper bound12

Six disjoint targets perselected vertex gives6|U|≤78, hence |U|≤13. If equality13held, the13open neighborhoods would partition the entire78-vertex controller. Each selected vertex would then have exactly one selected neighbor. The graph induced on13selected vertices would be1regular, contradicting the handshaking lemma. Therefore |U|≤12. This argument uses the78-vertex simple6-regular input and makes no independence assumption.

## Why the exact search closes the stronger upper bound10

Define a compatibility graph on the same78vertices by makingu,vcompatible exactly whenu≠v and N(u)∩N(v)=∅. A clique in that graph is exactly an open-neighborhood packing in the original controller, in both directions. The code represents these sets with unsigned128-bit integers.

The branch-and-bound state is a clique `current` and a candidate setPwhose members are compatible with every vertex in that clique. To branch onv, appendv and recurse onP∩compatible(v); then removevfromP before considering subsequent branches. This is exhaustive over allcliques that can improve the current incumbent: each possibleextension is assigned to the branch containing its last vertex in the fixed coloring order.

At each node, greedy coloring partitionsPinto independent color classes of the compatibility graph. The `color_sort` output lists complete color classes in increasing color order. Before branching on itsithvertex in reverse order, the remainingPcontains only the prefix throughi, so a clique extension has size at most the recorded color number for that prefix. If current-size plus that number cannot exceed the incumbent, every remaining branch at that node can be discarded. The separate cardinality prune |current|+|P|≤incumbent is also valid. No heuristic score is treated as a bound.

The initial incumbent was the given7-set[0,1,7,9,15,18,24], whose actual neighborhood intersections were checked before use. Search stopped only after its entire improvement tree closed. It did not reach the optional attained-upper-bound12stop and did not time out. The terminal result is `TRUE_OPTIMUM_COMPLETE_TREE`, with646nodes,646greedy-coloring calls and644cardinality/color bound prunes. The final incumbent10and exhaustion prove an exact optimum of10for this fixed controller.

The bound is scoped to complete open-neighborhood packing in this specificC78controller. It is not a bound on arbitrary fiber-coordinate pin sets, nonrectangular point-level packings, other controllers or the degree/diameter problem itself. The previous base0bound7was not used as a global upper bound. No oldm34range was rerun.

## Execution and handoff

One compiler and one exact-search process were run, single worker. Total measured executable batch CPU was0.757685026seconds including input-header preparation, compilation, search and driver aggregation, below20CPU. Search's own measured CPU was0.001823seconds. The entire executable batch terminated; there is no UNKNOWN, pending search or automatic timer continuation.

This scope generated no fibergraph and did not read any large graph edgefile, run BFS/Lean/oldF9finite checks, use a solver, install software or compute hashes. The result supplies the actual ten controller layers and their60disjoint target layers for the existing plane interface. Any selection of a new complete graph, copy multiplicity or degree window remains a separate concrete root decision.
