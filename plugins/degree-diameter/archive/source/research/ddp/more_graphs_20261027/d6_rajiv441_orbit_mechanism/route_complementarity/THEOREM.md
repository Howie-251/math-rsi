# Diameter4 forces a cross-distance5 incidence geometry

Consider a finite nonempty simple incidence graph with points P and lines L, every line containing s+1points and every point on t+1lines, s,t>=1. Use the exact recovered441operator: A is the point set; B and C are distinct copies of flags(p,l),p incidentl. Add

- A_a--B(p,l) when a is in l other than p;
- B(p,l)--C(q,m) when p is in m other than q and l!=m;
- a clique among C(p,l) with fixed p and varying incident l.

No other edges are present. The degrees are d_A=d_B=s(t+1), d_C=t(s+1), and the order is N=v(2t+3), where v=|P|. These formulas use the actual fixed-point C panel, not the refuted fixed-triad panel.

## The cross-distance implication

If the operator has diameter at most4, every point a and every line m have incidence-graph distance at most5. Choose any q in m and consider a shortest A_a--C(q,m) path. Because A only meets B, B meets A/C, and C meets B/its fixed-point panel, the possible part sequences of lengths at most4 are precisely

    ABC, ABCC, ABCCC, ABABC, ABCBC.

Each projects to an incidence walk ending at the target line m:

- ABC, with B(p,l), gives a-l-p-m, length3.
- ABCC or ABCCC has the same C point q along its C steps, giving a-l-p-n-q-m, length5, where n is its first C line.
- ABABC, with middle A_b and second B(r,n), gives a-l-b-n-r-m, length5.
- ABCBC, with first/second B marks p,r and middle C line n, gives a-l-p-n-r-m, length5.

Repeated vertices only shorten a walk and cause no problem. Thus point-to-line distance is at most5. Any same-side pair then has distance at most6, by appending one incidence edge to a suitable cross-side route. Hence the incidence graph has diameter at most6. No generalized-polygon or girth assumption was used.

Fix any line. Its point layers at distances1,3,5 have sizes at most

    s+1, (s+1)st, (s+1)s²t².

Every point occurs in those layers, so

    v <= (s+1)(1+st+s²t²),
    N <= (s+1)(1+st+s²t²)(2t+3).                 (1)

This is a necessary condition only. Cycles and repeated routes can reduce the layers, never increase them. Dually, the line count is at most(t+1)(1+st+s²t²), consistent with v(t+1)=|L|(s+1).

For a larger(v_3) configuration,s=t=2, this gives v<=63 and N<=441. The known source attains441, so changing to another larger trivalent incidence configuration cannot improve(6,4) while retaining this operator.

## The marked-flag bottleneck

Assume only that the incidence graph has no4- or6-cycles. For an incident pair p in m, every length-at-most4 A_p--C(p,m) path must be ABCBC. In an ABC path the two distinct points p and the B mark lie in two distinct common lines, creating a4-cycle. This also eliminates ABCC and ABCCC because their C mark stays p. An ABABC path either reduces to that case or creates a4- or6-incidence cycle.

Write an ABCBC path as

    A_p--B(u,l)--C(v,n)--B(w,k)--C(p,m).

If u!=w, the incidence walk p-l-u-n-w-m-p is a4- or6-cycle after the adjacency exclusions. Thus u=w. The absence of4-cycles forces l=m. The BC conditions require n and k to be two distinct lines through u, each different from m. Choose u in m other than p in s ways, n through u other than m in t ways, the middle C mark v in n other than u in s ways, and k through u other than m,n in t-1ways. Therefore the exact number of four-step routes is

    s² t(t-1).                                  (2)

In particular t=1 leaves no such route, despite point/line Moore feasibility. For the original s=t=2 source this gives8 marked-flag four-routes: the three-line pencil is an essential resource.

## Removing the sole raw bound exception

Among integer s,t with max{s(t+1),t(s+1)}<=12, the only raw bound(1) above a current D4 threshold is(s,t)=(2,1): Delta4 and N<=105, just above104.

If this tuple improved104, then N=5v>104 and v<=21, so v=21 and equality holds in the cross-distance bound. From every line the three point layers must attain3+6+12=21. A4-cycle identifies forward branches from two first-layer points; a6-cycle identifies a third-layer point reached from two branches. Either makes the bound strict. Hence equality forbids4/6 incidence cycles. Equation(2) then gives zero A_p--C(p,m) paths within4, a contradiction. No uniqueness classification of the Heawood geometry is needed.

Thus v<=20. Incidence balance2v=3|L| forces v divisible by3, so actually v<=18 and N<=90 for this tuple if the operator has D<=4. The105 raw exception is fully removed.

## Original A-A route compression

The point two-section of the source is recovered by the two A neighbors of each B vertex: it is6regular on63points with189edges. Its63triads correspond to the recovered incidence lines. Given the established source D4, the trivalent incidence graph attains the diameter6 bipartite Moore count126 and hence the generalized-hexagon(2,2) distance counts.

A pair of points opposite in that incidence geometry is not covered by ABABA; that would give a point two-section path of length2. Its four-step source paths are exactly ABCBA. A geodesic point path a-p-r-b with middle triad m={p,r,q} compresses to

    A_a--B(p,l_first)--C(q,m)--B(r,l_last)--A_b.

The three incidence geodesics between opposite points give exactly three such routes. The source point distance layers are1,6,24,32, so1008 unordered A pairs use this opposite-pair mechanism. C-panel edges cannot appear in any A-A path of length at most4. Fixed-point C panels can matter for other orbit pairs; the marked-flag routes above instead use three incidence lines and the BC rule, with no C-C edge. Thus an A-A coverage check alone cannot certify the full operator. No source441 all-root BFS or alternative C panel was run here.

## Scope of the family decision

PARAMETER_BOUNDS.json enumerates all17 nondegenerate integer tuples with canonical maximum degree at most12. After the marked-flag exception, none has an upper bound above a current D4 saved threshold for degree caps4..12. Zero s or t produces isolated operator vertices and gives no connected diameter4 exception.

The result is for the complete uniform flag operator as defined above. It does not cover changed BC predicates, trimmed panels, removed or added orbitals, nonuniform incidence structures, vertex splitting or general degree-diameter graphs. It is a paper proof, not a Lean or external-review claim. No new candidate or solver is needed to finish this mechanism decision.
