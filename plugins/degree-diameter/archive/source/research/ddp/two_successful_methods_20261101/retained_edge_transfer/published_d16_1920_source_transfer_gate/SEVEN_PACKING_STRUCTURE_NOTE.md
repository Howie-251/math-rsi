# Seven open-neighborhood centres: necessary structure, paper analysis

2026-11-01. This note concerns only the actual 30-vertex, degree-four controller in `research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json`, read through its `controller` field. It proves the proposed necessary seven-centre shape and a stronger local reconstruction interface. **It does not claim an independent complete exclusion of seven centres.** Root has separately completed the exact packing computation: optimum six, witness `[0,3,5,7,9,16]`, 373 nodes, reported CPU 0.001421773 seconds. That actual result is recorded in `CONTROLLER_PACKING_RESULT.json` and `CONTROLLER_PACKING_TERMINAL.json`; no enumeration was repeated here.

The analysis below uses open neighborhoods, not closed balls. Its scope is a whole-controller-fibre plane packing. It is not an upper bound for arbitrary point-level lift codes or different controllers.

## The literal two factors

The triangle factor, with names used below, is

| Triangle | Vertices | External-cycle indices met |
|---|---|---|
| T0 | 0,2,18 | 0,1,3 |
| T1 | 1,3,17 | 1,2,5 |
| T2 | 4,8,10 | 2,3,5 |
| T3 | 5,15,29 | 2,3,4 |
| T4 | 6,21,22 | 0,2,4 |
| T5 | 7,13,25 | 1,3,4 |
| T6 | 9,14,19 | 0,3,5 |
| T7 | 11,16,26 | 1,4,5 |
| T8 | 12,23,28 | 0,1,2 |
| T9 | 20,24,27 | 0,4,5 |

The remaining edges form the six cycles, in cyclic order:

```
C0 = (0,20,28,22,9)
C1 = (1,13,23,11,2)
C2 = (3,21,8,12,5)
C3 = (4,25,14,29,18)
C4 = (6,15,27,7,16)
C5 = (10,19,26,17,24)
```

Each cycle meets five distinct triangles. The displayed incidence triples also show that any two cycles meet exactly two common triangle blocks. These are literal properties read from this controller, not consequences of factor sizes alone.

## 1. Three external edges plus one isolated centre are necessary

Suppose S has seven centres and their open neighborhoods are pairwise disjoint. Each center has four neighbors, so the neighborhood union has size 28 and exactly two vertices are uncovered.

Every vertex has at most one neighbor in S. In particular the induced graph on S has maximum degree one. Two centres cannot lie in one triangle: they would have its third vertex as a common neighbor. Thus an induced edge on S must belong to the external five-cycle factor, and S occupies seven distinct triangles.

If the induced matching has e edges, precisely 7−2e centres are isolated in S. Each isolated centre lies outside the neighborhood union. Hence 7−2e≤2 and e≤3, forcing e=3 and exactly one isolated centre.

In a five-cycle two selected nonadjacent vertices have a common cycle neighbor, while three selected vertices either contain such a pair or violate induced maximum degree one. Thus a cycle contains at most two centres, and two must be adjacent. The three matching edges therefore lie in three different cycles, the isolated centre lies in a fourth cycle, and two cycles are empty. This proves the proposed shape.

## 2. Exactly where the second uncovered vertex must occur

Let E and F be the two empty cycles. Together they touch 5+5−2=8 triangle blocks. Every vertex in either empty cycle has no external selected neighbor. It is covered if and only if its triangle contains a centre.

There are only seven selected triangles. Consequently at least one vertex in E∪F is uncovered. The isolated centre already accounts for the other uncovered vertex, so there is **exactly one** uncovered vertex in E∪F and none elsewhere.

Both triangles shared by E and F must be selected: an unselected shared triangle would contribute two uncovered vertices, already too many alongside the isolated centre. Of the six triangle blocks touching exactly one of E,F, exactly five are selected and one is unselected. Both triangle blocks avoiding E and F are unselected.

It would be incorrect simply to demand that all vertices in both empty cycles be covered, then infer the false immediate contradiction eight selected triangles > seven. The allowed second uncovered vertex matters.

## 3. A stronger local interface in the four occupied cycles

Let Z denote the three unselected triangle blocks. In an occupied cycle:

* A noncentre in a selected triangle is already covered by its triangle centre, so it cannot have any selected external neighbor.
* A vertex in Z has no selected triangle neighbor. It must have one selected external neighbor, because the only uncovered vertices have already been located: the isolated centre and one vertex in E∪F.
* A paired centre has exactly one selected external neighbor; the isolated centre has none.

If a cycle contains a selected edge, its external neighborhood union consists of the two centres and two additional vertices. Those two additional vertices are exactly its vertices in Z. If a cycle contains the singleton, its two external neighbors are exactly its vertices in Z. Therefore **each of the four occupied cycles meets Z in exactly two vertices**.

In either case those two Z vertices have distance two around their five-cycle. Label them v0,v2 in cyclic order v0,v1,v2,v3,v4. There are only two locally compatible choices:

```
singleton: {v1}, the unique common external neighbor of the Z pair;
edge:     {v3,v4}, the other adjacent pair avoiding Z.
```

An adjacent Z pair permits neither choice. Globally exactly one occupied cycle must use the singleton choice and the other three the edge choice. Their seven selected vertices must lie in seven distinct triangle blocks, exactly the complement of Z. This final transport between cycle positions and triangle blocks is an additional compatibility condition; a cardinality count alone does not supply it.

## 4. Reduction to two Z possibilities per empty-cycle pair

Fix E,F. The two triangle blocks avoiding both have cycle-index triples contained in the other four indices. They are distinct three-subsets of those four indices, hence share two indices A,B and have respective remaining indices C,D. Across the four occupied cycles, these two unselected triangles contribute counts (2,2,1,1) on A,B,C,D.

The third unselected triangle must touch one empty cycle and two occupied cycles. The preceding exactly-two condition forces it to touch C and D, not A or B. The literal pair-incidence-two property supplies just two such triangle blocks. Thus each fixed empty-cycle pair has at most two candidate choices of Z, followed by the local singleton/edge rule above and the remaining global distinct-triangle check.

This is a proved necessary finite interface. This paper task did not go through all empty-cycle pairs or prove that the final global check fails in every case. Root's already completed exact 373-node computation supplies the actual optimum-six conclusion, independently of finishing this hand classification. No further enumeration, solver or validation is needed for the present decision.

## Scope and decision

The capacity upper bound seven is not geometrically neutral: saturation would force a near-perfect partition jointly compatible with both factors, including the exact Z profiles above. Root's actual optimum six now closes that whole-controller open-neighborhood plane model. It does not close fractional or point-level constructions, different fibre subsets, or arbitrary extensions of the 1920-vertex lift. This note is not a new graph, Lean result, external-review verdict, or a new Wiki method.

No packing enumeration, rank computation, BFS, solver, field experiment or paid review was run for this analysis. Only the saved controller was read and this paper note written; root-owned files and frozen packages were not changed.
