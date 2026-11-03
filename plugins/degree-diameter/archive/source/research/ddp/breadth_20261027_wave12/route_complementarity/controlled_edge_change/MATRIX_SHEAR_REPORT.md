# Coupled output shear: one linear prediction preserves every original tight route

Status: one prescribed candidate checked at the route-linear level. Target AACA rank4 and all468 cached unique4 ranks4 are confirmed. No expanded graph, whole-graph score, BFS, matrix grid, or solver was used. Root receives this frozen prediction before generating its one controlled graph.

## Why this variable change follows the observed failure

The single b-only change on0->18 repaired AACA but changed the reverse branch vector8->9, damaging37<->63. A sequential second-edge repair moved the deficit; even the complete225 assignments on those two fixed matrices could not preserve all tight routes. The new test changes the connection rule: transform the matrix and branch vector together on just the first edge, so the desired forward direction changes while the original reverse branch is retained.

Let S toggle output bit1 by output bit0. In vector codes, S(1)=3 and S(8)=8, and S is its own inverse. With original A-matrix columns[2,4,8,1] and branch b1, the fixed candidate is

    T' = S*T,      columns[2,4,8,3],
    b' = S*b = 3,
    T'^-1 = T^-1*S, columns[9,1,2,4],
    T'^-1*b' = T^-1*b = 8.

All143 other edge relations, and every offset0, remain exactly at cachedbest68. This is one matrix/vector change selected algebraically; no matrix family was scanned.

## Frozen numerical predictions

Target0->10 has AACA path0-18-37-64-10. Its columns become

    [14,9,7,1], rank3 -> [10,9,7,1], rank4.

Thus AACA alone is predicted to reach all16 target coordinates for each of16 source coordinates: all256 ordered fiber pairs for this controller slot have distance at most4.

All468 cached unique4 controller slots retain rank4, so their predicted missing fiber-pair count is0. In particular:

| tight slot | path | columns after shear | rank |
|---|---|---|---:|
| 37->63 | 37-18-0-36-63 | [7,2,15,11] | 4 |
| 63->37 | 63-36-0-18-37 | [14,12,6,1] | 4 |

The first list is exactly the original forward list. For the DDCC route37->63, its first D step supplies vector8. The changed reverse matrix is T^-1*S, and S fixes8; the new reverse branch is also8. Therefore the two affected prefix columns remain as before, and the two final C steps produce the original four columns. The reverse route has changed columns but retains full rank.

These predictions cover the target and the468 necessary tight slots. They do not claim whole-graph D4: other controller pairs combine several route images and still need exact expanded-graph measurement.

## It changes the connection, rather than renaming vertex18 coordinates

Applying S as a complete coordinate gauge at vertex18 would transform every one of its four port relations. This candidate modifies only port0<->18. For example, the other A-port18->37 remains y=A*x+lambda*1. A full vertex18 gauge would instead give y=A*S*x+lambda*1. At input x=1 these have target sets{2,3} and{6,7}, respectively, which are distinct. The retained other ports therefore rule out interpreting the candidate as that full gauge.

One can also see the changed loop connection in the branch-zero linear actions along the controller A-cycle

    0-18-37-60-6-24-43-57-3-21-40-54-0.

Its original A^12 action is the identity. With only the first matrix replaced, its linear action is A^11*S*A=A^3*S*A, with columns[1,2,4,9], which is nonidentity. This is an explanation of the controlled matrix connection, not a whole-graph route or distance certificate.

## Evidence, cost, and next check

matrix_shear_prediction.json freezes all candidate parameters, target columns, all468 original/modified route records, zero damage, and scope. analyze_shear.py reproduces the single route-linear calculation. Candidate count1, matrix-grid count0, graphs0, whole-graph scores0, BFS0, solvers0, new lower bounds0. CPU time was 0.008000 seconds under a hard1-CPU-second process limit.

The former fixed-T b-only repair rule failed in the two prescribed local slices. This coupled T/b rule passes the exact tight-rank test and now merits the single controlled expanded graph. Root will generate that graph once and compare the frozen predictions, then use the remaining coverage result to decide the next rule. No other edge, shear, offset, or seed is automatically added.


## Actual controlled graph result — root check completed

The preceding sections preserve the prediction as frozen before measurement. Root has now generated and checked exactly this one shear graph from its complete edge table; reuse matrix_prediction_check.json and matrix_shear_distances.u8.bin. This report update performed no graph generation or BFS.

The graph is simple, connected,8-regular on1152 vertices with4608 edges. The all1152-root check found actual diameter5 and12800 unordered pairs at distance greater than4. Its target0->10 has0 missing pairs among all256, and tight_slot_missing is empty. Thus both frozen linear predictions matched exactly: the target was repaired and all468 original tight slots were preserved.

The bad-pair comparison is:

| graph | actual diameter | unordered pairs at distance>4 |
|---|---:|---:|
| original cachedbest68 | 5 | 12384 |
| first edge b-only change | 5 | 13424 |
| this coupled T/b shear | 5 | 12800 |

The coupled shear removes624 bad pairs compared with the b-only graph, but has416 more than the original source. The test supports the specific rule that changing T and b together can preserve the reverse branch and avoid the identified tight-route damage. It does not show a global coverage improvement over the original graph or produce a new lower bound.

The outstanding explanation is a concrete off-target coverage loss created by this change. Another assigned agent is examining a specific newly damaged controller slot; that explanation is not yet available in this report. No cause is inferred from the total bad-pair count alone, and the generic statement that tight ranks do not settle every route union is not counted as a new result. The next connection rule should respond to that actual counterexample and protect its multi-route coverage. No additional candidate, matrix grid, template, or repeated BFS is started here.
