# C60/F4: the unique-route matching obstruction does not close the domain

The sole prescribed short-word gate completed successfully: PID2147374,
0.051644238 CPU seconds, exit0, within the five-second hard limit. No graph,
graph BFS, field matrix enumeration or alternate controller was used.

There are4800 nonbacktracking three-words. Exactly1260 ordered endpoint pairs
have controller distance3 and a unique such word. The1980 count in the F7
route summary also includes pairs having a shorter route, and cannot all be
used to force rank3. We explicitly exclude length0,1,2 endpoints here.

For a unique word u–a–b–v, let e=a→b have port p and reverse port r. Let i be
the reverse incoming port at a, and j the outgoing port at b. For local
directions L and inverse-consistent edge charts, applying the inverse of the
last chart reduces the three noise vectors to

\[
T_e L_{a,i},\quad L_{b,r},\quad L_{b,j}.
\]

If their rank is below3, one affine image of size at most16 cannot cover the
64 target coordinates. Hence this turn must have rank3, for arbitrary source
coordinate and arbitrary affine offsets.

At each vertex assume a shared five-direction arc: every triple is linearly
independent. In the two-dimensional quotient at e, each side supplies four
different points of PG(1,4), which has five points. There must be at least
three coincident pairs, and they form a matching between the four incoming
and four outgoing alternatives. All those bad cells must avoid the forced
cells above.

The literal300 directed edges give:

| Forced cells per edge | Number of directed edges |
|---:|---:|
|2|40|
|3|120|
|4|40|
|5|20|
|7|80|

Every edge's unforced cells contain a matching of size4. Thus the prediction
that one edge already forbids three bad cells is refuted. This result leaves
the edge-dependent chart/local arc-frame domain open; it does not establish
projective realizability or D3.

If both the five directions and matrices are global by port, the forced
unions for ports0..4 have sizes11,11,7,7,11, with complementary maximum
matching sizes3,3,4,4,3. These unions also pass the necessary gate, but are
not restrictions one may impose on arbitrary edge-dependent charts.

## A precise next small interface (not executed)

Fix one explicit five-point conic over F4, label its directions by the five
ports, and derive the five quotient coordinate systems. For each port test
the60 elements of PGL(2,4) against its saved forced-cell union. Couple inverse
ports by inverse maps; for the self-inverse port require a genuine linear
involution lift, rather than just a freely chosen projectivity. This is a
small projective compatibility test, not a GL(3) matrix search. Testing one
conic labeling does not by itself classify all labeled local frames.

The self-inverse port already has a useful exact restriction. Its forced
union leaves only cells(0,0),(0,1),(1,0),(1,1),(3,3), while row2 is entirely
forced. Therefore a feasible projectivity has exactly three bad cells. In
the five-point projective line with omitted point *, it must interchange
2 with *, fix3, and either fix0,1 or swap0,1. The former would fix three
projective points and hence be identity, which contradicts2↔*. Thus the
only possible permutation is **(0 1)(2 *) with3 fixed**. Whether it is a
projectivity for the chosen quotient coordinates remains to be checked.

Even projective compatibility would only satisfy necessary unique-route
conditions. Actual rank-deficient multi-route unions and adjacent/same-fiber
coverage still need a specified chart rule and an exact common-coverage
check. No field graph is authorized or produced by this report.

Evidence: RESULT.json; FORCED_TURNS.json includes every edge and its forced
cells with endpoint witnesses; UNIQUE_DISTANCE3_PATHS.json stores all1260
literal paths. PREDICTION.md preserves the falsified prediction.
