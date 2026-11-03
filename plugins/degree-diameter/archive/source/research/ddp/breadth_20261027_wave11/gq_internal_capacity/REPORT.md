# GQ(q,q) incidence plus internal regular graphs: D3 average-capacity screen

Status: complete mathematical necessary screen. No geometry, candidate graph, random profile, or BFS was generated. This is a generalization of the coverage accounting for the existing q=5,r=2 profile, not a new independent graph mechanism.

**Maximum-degree scope clarification (follow-up):** the regular-parameter table below is not the entire original maximum-degree Goal. The same U bound is valid for arbitrary internal graphs of maximum degree at most r, but regularity parity does not exclude such graphs. In particular q=8,rmax=3 gives 1170 vertices, total degree cap12, U=618>=512, and remains a necessary pass for nonregular choices (each 585-vertex side may have one degree2 vertex and 584 degree3 vertices). The maximum-degree version has four order-improving necessary passes: q3/max1, q5/max2, q7/max3, and q8/max3. None is asserted to exist. See the structural [commuting obstruction](../gq_commuting_obstruction/REPORT.md), which rules out any commuting side in all four, while preserving two noncommuting sides as open.

## Definition and positive routing basis

Let q>=2 be a prime power, and let a generalized quadrangle GQ(q,q) have point set P and line set L. Each side has N=(q+1)(q^2+1) vertices; every vertex has q+1 incidence neighbors. Retain every incidence edge, add an arbitrary simple r-regular graph A on P, and independently an arbitrary simple r-regular graph Q on L. Thus n=2N and Delta=q+1+r. The chosen internal graphs need no symmetry, group action, connectivity, or common cycle structure.

The retained incidence routes guarantee: every opposite-side pair is at distance at most 3; every collinear same-side pair is at distance at most 2; every pair is at distance at most 4. Thus only same-side noncollinear pairs can obstruct D<=3. Every root has exactly q^3 such targets. The following is an obstruction to all choices of the two internal r-regular graphs; a capacity pass is not a construction or a D3 assertion.

## Claim

A necessary condition for D<=3 is

    q^3 <= U(q,r)
         = 2 r q^2 + r q(q+1) + r(r-1) + r(r-1)^2
         = 3 r q^2 + r q + r^2(r-1).

This is an average capacity inequality over all roots on one side. In particular, the second r q^2 term must not be interpreted as a bound at every individual root.

## Proof

Write C(p) for the closed collinearity set of p: p itself and all points collinear with p. Its size is q^2+q+1. For any two distinct points p,u, the intersection C(p) intersect C(u) has size q+1. If p,u are collinear, the common points are precisely their common line, including p and u. If they are noncollinear, each of the q+1 lines through p has exactly one point collinear with u, by the GQ axiom. Consequently |C(u) minus C(p)|=q^2 whenever u!=p. The dual statement holds for lines.

Classify all paths of length at most 3 between points with noncollinear endpoints. The number of incidence edges is even. With two incidence edges there are three possible positions for the one internal edge; with no incidence edges the path is entirely internal.

1. Internal edge first, then two incidence edges (A C). For a fixed root p and each of its r internal neighbors u, the possible far targets belong to C(u) minus C(p), of size q^2. The union therefore has at most r q^2 targets at this root. Direct internal neighbors are already included because C contains its diagonal.

2. Two incidence edges first, then an internal edge (C A). Do not bound this pointwise by r q^2. Instead fix a directed internal edge u->v. The roots p for which u is in C(p) but v is not in C(p) form C(u) minus C(v), which has q^2 elements. Summing over all Nr directed internal edges gives Nr q^2 route endpoint incidences. After collapsing duplicate targets and dividing by N, the mean contribution is at most r q^2. Equivalently, the far ordered pairs supported by C A are the transposes of those supported by A C, so their total counts agree.

3. Incidence, opposite-side internal edge, incidence (B Q B^T). At a fixed root p choose an incident line ell (q+1 choices), then an internal line neighbor m (r choices). If p is on m, no point of m is far from p. Otherwise exactly one point of m is collinear with p and the other q points are far. Hence this term contributes at most r q(q+1) far targets per root.

4. Purely internal paths. Length 1 is already counted in A C. An immediate reversal in length 2 returns to the root; after removing it there are at most r(r-1) nonbacktracking length-2 paths. A length-3 path with an immediate reversal ends at an internal neighbor of the root and is already counted; the remaining paths number at most r(r-1)^2. Distinct paths may still end at the same point or a near point, which can only lower coverage.

These four categories exhaust all possible same-side paths of length at most 3. Sum their endpoint bounds over all N roots. If D<=3, all N q^3 ordered far pairs must be covered. The union bound gives N q^3 <= N U(q,r). The line-side argument is dual. This proves the necessary inequality without imposing a false pointwise bound on C A.

## Regularity parity and complete parameter scope

The range q+1+r<=12 gives q in {2,3,4,5,7,8,9,11} and 0<=r<=11-q: 47 parameter pairs in total. In addition to the capacity condition, a simple r-regular internal graph requires Nr even (and r<N, automatically true here). When q is even, N is odd, so r must be even. There are 36 parity-legal pairs, 35 of them in the active Delta=4..12 range; q=2,r=0 has Delta=3 and is listed only for scope completeness.

Thus q=4,r=1 has no such internal regular graphs at all, besides the numerical capacity failure 52<64. Also q=8,r=3 passes the loose numerical capacity test but is parity-impossible; it must not be listed as a viable 1170-point degree-12 case.

## Comparison with the saved 27-cell portfolio

Baselines are the saved 2026-10-26 snapshot in context/DD_PORTFOLIO_START_20261026/registry/cases.json, not refreshed claims about today's public table. No new lower bound is claimed. RESULT.json contains all 47 parameter pairs, each with comparisons for D=3,4,5 (null outside the active degree range).

Among the 19 strict D3 order-improving parameter pairs, three are parity-impossible. Of the remaining 16, the average-capacity inequality excludes 13. The only three that survive these necessary conditions are:

| q | r | n | Delta | saved D3 lower bound | far targets q^3 | mean upper U | Scope |
|---:|---:|---:|---:|---:|---:|---:|---|
| 3 | 1 | 80 | 5 | 72 | 27 | 30 | Necessary pass only; no graph generated |
| 5 | 2 | 312 | 8 | 253 | 125 | 164 | Existing finite profile failed; not rerun |
| 7 | 3 | 800 | 11 | 715 | 343 | 480 | Necessary pass only; no graph generated |

Notable uniform exclusion: q=7,r=2 would give 800 vertices and degree 10, but U=312<343, so no choices of two internal 2-regular graphs can achieve D3 in this retained-incidence template. Similarly q=8,r=2 has U=404<512; q=9,r=2 has U=508<729.

For D=4 or D=5, retaining incidence gives a positive routing guarantee, but none of the 47 parameter pairs has order greater than the saved lower bound at its resulting degree. These comparisons provide no portfolio improvement for either diameter.

## Existing q=5,r=2 result and stop rule

The existing wave10/gq312_internal_cycles profile tested two fixed starts with a total of 2000 legal internal 2-factor edge switches. Its independent root check found a simple connected degree-8 graph on 312 vertices, actual diameter 4, with 4090 unordered pairs at distance greater than 3. Evidence: research/ddp/breadth_20261027_wave10/gq312_internal_cycles/best.independent_check.json. The original incidence edges and both internal 2-factors were checked there. This finite failure does not exclude all internal 2-factors; the present capacity bound also does not exclude q=5,r=2.

No new internal graph choices have been tried here. The two other necessary passes remain unresolved coverage-design questions. No parameter search or extra starts follow from this screen. Reopening requires an explicit new structural way to cover all far same-side pairs within the retained-incidence template, and a separately bounded construction task; passing U alone is insufficient.

## Full finite table

`legal` means regularity parity permits the internal graph, not that D3 is attainable. `order+` compares n with the saved D3 lower bound. U is an upper bound on mean far-target coverage; a negative margin proves the D3 obstruction independently of whether the order improves a saved bound.

| q | r | n | Delta | legal | savedL(D3) | order+ | q^3 | U | U-q^3 | status |
|---:|---:|---:|---:|:---:|---:|:---:|---:|---:|---:|---|
| 2 | 0 | 30 | 3 | yes | outside | no | 8 | 0 | -8 | OUTSIDE_ACTIVE_DEGREE_RANGE |
| 2 | 1 | 30 | 4 | no | 41 | no | 8 | 14 | 6 | REGULARITY_PARITY_IMPOSSIBLE |
| 2 | 2 | 30 | 5 | yes | 72 | no | 8 | 32 | 24 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 2 | 3 | 30 | 6 | no | 120 | no | 8 | 60 | 52 | REGULARITY_PARITY_IMPOSSIBLE |
| 2 | 4 | 30 | 7 | yes | 170 | no | 8 | 104 | 96 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 2 | 5 | 30 | 8 | no | 253 | no | 8 | 170 | 162 | REGULARITY_PARITY_IMPOSSIBLE |
| 2 | 6 | 30 | 9 | yes | 585 | no | 8 | 264 | 256 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 2 | 7 | 30 | 10 | no | 650 | no | 8 | 392 | 384 | REGULARITY_PARITY_IMPOSSIBLE |
| 2 | 8 | 30 | 11 | yes | 715 | no | 8 | 560 | 552 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 2 | 9 | 30 | 12 | no | 810 | no | 8 | 774 | 766 | REGULARITY_PARITY_IMPOSSIBLE |
| 3 | 0 | 80 | 4 | yes | 41 | yes | 27 | 0 | -27 | D3_AVERAGE_CAPACITY_IMPOSSIBLE |
| 3 | 1 | 80 | 5 | yes | 72 | yes | 27 | 30 | 3 | NECESSARY_PASS_NO_GRAPH_CONSTRUCTED |
| 3 | 2 | 80 | 6 | yes | 120 | no | 27 | 64 | 37 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 3 | 3 | 80 | 7 | yes | 170 | no | 27 | 108 | 81 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 3 | 4 | 80 | 8 | yes | 253 | no | 27 | 168 | 141 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 3 | 5 | 80 | 9 | yes | 585 | no | 27 | 250 | 223 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 3 | 6 | 80 | 10 | yes | 650 | no | 27 | 360 | 333 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 3 | 7 | 80 | 11 | yes | 715 | no | 27 | 504 | 477 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 3 | 8 | 80 | 12 | yes | 810 | no | 27 | 688 | 661 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 4 | 0 | 170 | 5 | yes | 72 | yes | 64 | 0 | -64 | D3_AVERAGE_CAPACITY_IMPOSSIBLE |
| 4 | 1 | 170 | 6 | no | 120 | yes | 64 | 52 | -12 | REGULARITY_PARITY_IMPOSSIBLE |
| 4 | 2 | 170 | 7 | yes | 170 | no | 64 | 108 | 44 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 4 | 3 | 170 | 8 | no | 253 | no | 64 | 174 | 110 | REGULARITY_PARITY_IMPOSSIBLE |
| 4 | 4 | 170 | 9 | yes | 585 | no | 64 | 256 | 192 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 4 | 5 | 170 | 10 | no | 650 | no | 64 | 360 | 296 | REGULARITY_PARITY_IMPOSSIBLE |
| 4 | 6 | 170 | 11 | yes | 715 | no | 64 | 492 | 428 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 4 | 7 | 170 | 12 | no | 810 | no | 64 | 658 | 594 | REGULARITY_PARITY_IMPOSSIBLE |
| 5 | 0 | 312 | 6 | yes | 120 | yes | 125 | 0 | -125 | D3_AVERAGE_CAPACITY_IMPOSSIBLE |
| 5 | 1 | 312 | 7 | yes | 170 | yes | 125 | 80 | -45 | D3_AVERAGE_CAPACITY_IMPOSSIBLE |
| 5 | 2 | 312 | 8 | yes | 253 | yes | 125 | 164 | 39 | NECESSARY_PASS_ALREADY_TESTED_FINITE_PROFILE_FAILED |
| 5 | 3 | 312 | 9 | yes | 585 | no | 125 | 258 | 133 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 5 | 4 | 312 | 10 | yes | 650 | no | 125 | 368 | 243 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 5 | 5 | 312 | 11 | yes | 715 | no | 125 | 500 | 375 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 5 | 6 | 312 | 12 | yes | 810 | no | 125 | 660 | 535 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 7 | 0 | 800 | 8 | yes | 253 | yes | 343 | 0 | -343 | D3_AVERAGE_CAPACITY_IMPOSSIBLE |
| 7 | 1 | 800 | 9 | yes | 585 | yes | 343 | 154 | -189 | D3_AVERAGE_CAPACITY_IMPOSSIBLE |
| 7 | 2 | 800 | 10 | yes | 650 | yes | 343 | 312 | -31 | D3_AVERAGE_CAPACITY_IMPOSSIBLE |
| 7 | 3 | 800 | 11 | yes | 715 | yes | 343 | 480 | 137 | NECESSARY_PASS_NO_GRAPH_CONSTRUCTED |
| 7 | 4 | 800 | 12 | yes | 810 | no | 343 | 664 | 321 | NO_STRICT_D3_ORDER_IMPROVEMENT |
| 8 | 0 | 1170 | 9 | yes | 585 | yes | 512 | 0 | -512 | D3_AVERAGE_CAPACITY_IMPOSSIBLE |
| 8 | 1 | 1170 | 10 | no | 650 | yes | 512 | 200 | -312 | REGULARITY_PARITY_IMPOSSIBLE |
| 8 | 2 | 1170 | 11 | yes | 715 | yes | 512 | 404 | -108 | D3_AVERAGE_CAPACITY_IMPOSSIBLE |
| 8 | 3 | 1170 | 12 | no | 810 | yes | 512 | 618 | 106 | REGULARITY_PARITY_IMPOSSIBLE |
| 9 | 0 | 1640 | 10 | yes | 650 | yes | 729 | 0 | -729 | D3_AVERAGE_CAPACITY_IMPOSSIBLE |
| 9 | 1 | 1640 | 11 | yes | 715 | yes | 729 | 252 | -477 | D3_AVERAGE_CAPACITY_IMPOSSIBLE |
| 9 | 2 | 1640 | 12 | yes | 810 | yes | 729 | 508 | -221 | D3_AVERAGE_CAPACITY_IMPOSSIBLE |
| 11 | 0 | 2928 | 12 | yes | 810 | yes | 1331 | 0 | -1331 | D3_AVERAGE_CAPACITY_IMPOSSIBLE |

## Artifacts and execution

`screen.py` performs only the 47 arithmetic evaluations and comparisons with the saved 27-cell snapshot. `RESULT.json` records all terms, parity conditions, statuses, and D3/D4/D5 comparisons. The arithmetic CPU time was 0.000666 seconds; there were zero graph generations, zero BFS calls, zero search proposals, and zero new lower bounds. No dependency was installed.

## Follow-up: maximum-degree scope and commuting geometry

The original proof extends to internal graphs of maximum degree at most r. The C A total is 2*m_P*q^2 <= N*r*q^2 rather than requiring exactly N*r*q^2; all other terms already use only degree upper bounds. Consequently U is still a necessary average bound. Parity applies only to the exact-regular table, and must not close q8/max3 near-regular choices. Among the 19 strict-order-improving maximum-degree parameter pairs, 15 fail capacity and four pass it; q8/max3 is the extra pass compared with the exact-regular list. RESULT.json now records both scopes separately.

The [commuting obstruction](../gq_commuting_obstruction/REPORT.md) proves that PC=CP merges the two endpoint-route supports. It gives pointwise U_comm=r*q^2+r*q*(q+1)+r*(r-1)+r*(r-1)^2, excluding commuting sides in the three regular survivors with 21<27, 114<125, and 333<343. Commutation also forces regularity via C^2=q^2*I+(q+1)*J; for q8/max3 it forces the commuting side to degree at most2, and the mixed-degree capacity is348<512 even with the other side maximum3. Both actual internal graphs must therefore be noncommuting in each possible over-baseline survivor. This is not an exclusion of all automorphism-derived deduplicated graphs or of the noncommuting families. No new graph search was run.
