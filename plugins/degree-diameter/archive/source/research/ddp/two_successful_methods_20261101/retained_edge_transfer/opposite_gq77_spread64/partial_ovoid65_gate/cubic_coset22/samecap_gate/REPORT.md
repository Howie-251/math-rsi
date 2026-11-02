# Fixed current161150 graph: same-cap65 full-neighborhood gate

The previously unknown question was whether any center in the accepted
161150-vertex graph could support one further clone adjacent to its complete
current open neighborhood, while retaining every edge, diameter at most3 and
maximum degree65. The accepted source is the frozen160050-vertex64-regular
opposite-GQ/spread graph; its1100 already accepted clones use O22 times the
original50 spread lines. No other source, field, seed or pin rule is tested.

`PRED.json` was written before the single finite run. It predicted that O22
is maximal and that every current center is blocked by an already saturated
neighbor. The prediction is confirmed. The actual compatible outside-point
list and actual compatible current-center list are both empty, rather than
a greedy extension attempt. This is a strict exclusion of this fixed operation,
not an exclusion of arbitrary pin sets or cooperative additions.

The one worker used **1.558927914 CPU seconds**, below the30CPU bound. It
opened only the frozen small geometry/center tables, never either large edge
table. It performed no BFS, Lean compilation, solver call or graph generation.
The geometry, original160050 literal binding, and accepted161150 clone binding
are inherited. The finite result is derived from the explicit neighborhood
recipe, not from an imported passed-status flag. An independent subagent
supplied the same structural derivation using paper algebra and the small
source files, without running a second numeric check.

For the reduced nonzero-scalar version of the alternating form, put

    B(x,y)=x0*y2+3*x1*y3-x2*y0-3*x3*y1 mod7.

The accepted point set is p_t^k=(1,t,t^3+k,-t^2), for k in K={0,2,4},
t in F7, together with infinity=(0,0,1,0). Pairing two finite points gives
(t-s)^3+(l-k). Cubes are0,1,6 and the distinct offset differences are2,3,4,5;
pairing any finite point with infinity is1. Thus it is a partial ovoid.

For any projective point x=(a,b,c,d), a=0 implies B(x,infinity)=0. Otherwise
normalize a=1, write t=b+u, and set A=3*(b^2+d), D=2*b^3+3*b*d+c. Then

    B(x,p_t^k)=u^3-A*u-D+k.

The image J_A={u^3-A*u:u in F7} is {0,1,6} if A=0,
{0,1,3,4,6} if A is1,2 or4, and {0,2,3,4,5} if A is3,5 or6.
For A=0, J_A+K=F7. Otherwise |J_A|=5, so it intersects the three-element
set D-K in the seven-element field. In every case some O22 point is
orthogonal to x. Therefore every point outside O22 is collinear with O22:
O22 is maximal under adding points. This does not assert that22 is the
maximum size of a partial ovoid.

The finite400point check gives the following counts. For an O22 point the
count includes its self pairing; each of those22 counts is1.

| Number of O22 points orthogonal to a point | All400 points | Outside378 points |
| --- | ---: | ---: |
| 1 | 85 | 63 |
| 2 | 42 | 42 |
| 3 | 119 | 119 |
| 4 | 98 | 98 |
| 5 | 21 | 21 |
| 6 | 14 | 14 |
| 7 | 21 | 21 |

All400 actual coordinates and counts are saved in `POINT_COLLINEARITY.json`;
the seven small image calculations are in `MAXIMALITY_RESIDUES.json`.
There is no outside point with count0.

Write s(p) for the unique original spread line containing p, and b_j for
the original bonus of spread line s_j. In the160050 source, the neighborhood
of a product vertex c=(p,l) is exactly

    {(q,m):q in l,m through p,(q,m)!=c}
    plus {b_owner(p)} if p lies on l.

The bonus neighborhood is all64 flags (q,m) with q on its spread line and
m through q. The original1100 clones use these complete source neighborhoods,
with no new-new edges. Their disjoint pin sets make exactly70400 source
vertices saturated at degree65; all other vertices currently have degree64.

There are176 GQ lines meeting O22. An original product (q,m) is saturated
exactly when m meets O22, except for the22 products (o,s(o)), o in O22.
Indeed m meets at most one O22 point o, and the unique spread containing q
selects the unique clone center (o,s(q)); the sole failure is its removed raw
self-pair q=o,m=s(o). At that flag its source neighborhood substitutes the
actual bonus b_owner(o). Thus the saturated products are precisely
400*176-22=70378, together with22 saturated bonuses. This explicit exception
is retained throughout; no assertion treats a raw self-pair as an edge.

For each product center (p,l), define r(p) to be the number of lines through
p meeting O22. It is8 if p lies in O22 and otherwise equals the number of
O22 points collinear with p, so maximality gives r(p)>=1. Let E be1 exactly
when l meets O22 at o and p lies on s(o). Let A_self be1 exactly when p lies
on l and the product (p,l) is saturated. Let F be1 exactly when p lies on l
and the bonus b_owner(p) is saturated. The exact number of saturated current
neighbors of (p,l) is

    8*r(p) - E - A_self + F.

The first subtraction removes the special unsaturated product (o,s(o)) if
it is in the raw rectangle; the second removes an actual saturated self-pair;
the final term accounts for the actual source bonus. Its possible extra
current clone neighbor has degree64 and contributes0 to this count.
If E=A_self=1, then p is on the spread s(o), so s(p)=s(o) meets O22 and F=1.
Consequently the displayed number is always at least8*r(p)-1, hence at least7.
This proves that every one of the160000 product centers is blocked, including
all original flags, self/bonus exceptions, and centers of current degree65.
The finite scan computes each actual full current neighborhood and checks this
formula at all160000 products. Its minimum is exactly7, attained112times.

For an original bonus b_j whose spread line does not meet O22, every O22 point
has one projected point on that spread line. Counting the resulting saturated
flags gives exactly22 saturated neighbors. There are28 such bonuses. If its
spread line contains o in O22, the point o contributes7 saturated flags after
the special flag is removed; the other seven spread points contribute7 flags
from o and21 from the remaining O22 points, for exactly35. There are22 such
bonuses. A possible extra current clone neighbor again has degree64. Hence all
50 original bonuses are blocked. Each of the1100 new clones has its own64
source pins as neighbors, all of which became saturated by that clone itself.
Thus all1100 clone centers are blocked too.

| Current center class | Centers checked | Minimum saturated neighbors | Exact special counts |
| --- | ---: | ---: | --- |
| Original product | 160000 | 7 | Full count histogram in RESULT.json |
| Original bonus | 50 | 22 | 28 have22;22 have35 |
| New clone | 1100 | 64 | All1100 have64 |

The finite recipe scan covers all161150 vertices and reconstructs the accepted
degree histogram64:90750,65:70400. A same-cap65 full-neighborhood clone would
need its current center degree at most65 and every neighbor degree at most64.
Every center satisfies the first condition, but each has saturated neighbors,
so **zero current centers satisfy both**. Complete neighborhood/degree records
for representative minimum blockers are in `MINIMUM_BLOCKER_WITNESSES.json`;
`ACTUAL_COMPATIBLE_CENTERS.json` is the actual empty list. No further point was
added and no continuous greedy process was run.

The next choice is therefore to stop this fixed graph/full-current-neighborhood/
same-cap65 operation. Any further retained-edge filling at cap65 must establish
a different actual pin-cover interface. Arbitrary pins, cooperative helpers,
edge changes, and other sources remain outside this exclusion; no new search
in any of those scopes was started. `RESULT.json` and `TERMINAL.json` record
the exact result, CPU and completed local state.
