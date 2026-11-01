# Two-flip repair with a common middle-edge wedge budget

This note strengthens [global two-flip path repair](GLOBAL_TWO_FLIP_PATH_REPAIR.md) by charging all paths through the same original middle edge together. Its A1 consequences are necessary counterexample structure, not a proof that the whole A1 branch is colorable.

## 1. Exact path identity and its normalization

Let H be a simple five-uniform hypergraph with M distinct original edges. For an original middle edge F and g∈F, define

    t(F,g)=#{G∈H:G∩F={g}},       s(F)=Σ_{g∈F}t(F,g).

For distinct unordered outer edges {G,J}, a valid middle F has F∩G={g}, F∩J={h}, g≠h. Let Cj count such (unordered outer pair, original middle) flags with |G∩J|=j, and let nj count unordered original edge pairs intersecting in j points. Then, exactly,

    P:=Σ_{j=0}^4 Cj =Σ_{F∈H}Σ_{g<h∈F}t(F,g)t(F,h),
    Σ_F s(F)=2n1,                  0≤s(F)≤M−1.              (1)

Indeed, selecting g<h and one outer edge in each of the two singleton-intersection groups gives two distinct outer edges and a unique middle flag. Conversely every flag gives exactly that choice. The middle cannot equal an outer edge, since their intersection is one point; distinct attachment points also prevent the two outer edges being equal. The second identity counts each unordered singleton-intersection pair twice, once with each endpoint edge as middle.

There is no extra factor two in P. The ordered path random variable Z of the two-flip theorem has both orientations of the outer pair, and therefore

    EZ=2Σ_j Cj rj.                                           (2)

This is a common budget on the actual original edges; different outer pairs cannot each be assigned their largest number of middle edges independently.

## 2. A general 35-edge wedge bound

For fixed s and five nonnegative integer group sizes summing to s, the maximum pair sum is

    f(s)=[s²−(5−r)a²−r(a+1)²]/2,    s=5a+r, 0≤r<5.         (3)

Moving one unit from a group at least two larger than another decreases the sum of squares; hence the balanced groups maximize the pair sum. In particular f(34)=462. For s≤33, Cauchy gives f(s)≤2s²/5≤66s/5; for s=34,

    f(34)=66·34/5+66/5.

Thus, writing N34=#{F:s(F)=34}, any 35-edge five-uniform input satisfies

    P≤(132/5)n1+(66/5)N34.                                 (4)

Without further structure, one also has P≤462n1/17: for s≤33, f(s)/s≤66/5<231/17, while f(34)/34=231/17; apply (1). Neither bound assumes a maximum original vertex degree.

## 3. Reduced A1: at most nine exceptional middle edges

Now assume the actual reduced A1 role on21 points and35 edges: one six-degree point x, one seven-degree point p, nine eight-degree points, and ten nine-degree points V. The pair xp is unit, and every xv with v∈V is unit; all other points outside x,p have degree8 or9. These actual unit relations are used below; the degree sequence alone is insufficient for this step.

Let ej(F) be the number of other original edges intersecting F in j points. The same H gives

    m(F):=Σ_{v∈F}(dv−1)=s(F)+2e2(F)+3e3(F)+4e4(F),
    e0(F)+s(F)+e2(F)+e3(F)+e4(F)=34.                         (5)

Consequently s(F)=34 implies m(F)=34, or Σ_{v∈F}dv=39. An edge avoiding x,p has degree sum at least40, so cannot be exceptional.

There are five x-only edges, six p-only edges, and the unique xp edge. Let v0 be the number of V points on the xp edge, so 0≤v0≤3, and put S=10−v0. Since each xv is unit, the V incidences on the five x-only edges sum exactly S. Since p must cover every V point, the six p-only edges have at least S V incidences.

An x-only edge has degree sum38+v, where v is its number of V points, so it is eligible for s=34 only when v=1. If k of the five x-only edges are eligible, then S≤k+4(5−k), hence k≤floor((20−S)/3). A p-only edge has degree sum39+v, so eligibility requires v=0. If l of the six p-only edges are eligible, then S≤4(6−l), hence l≤6−ceil(S/4). The xp edge has degree sum37+v0, so eligibility requires v0=2.

The resulting upper bounds on N34, for v0=0,1,2,3, are respectively

    6, 6, 9, 8.

Therefore every actual reduced A1 input satisfies the joint capacity

    N34≤9,       P≤(132n1+594)/5.                           (6)

This proof neither enumerates H nor chooses separate private or middle edges for different paths.

## 4. The degree-three outer intersection cap can be made strict

Assume in addition Δ≤9 and all point-pair codegrees at most4, as supplied in the remaining A1 role by the [complete strong-pair imports](../../context/propertyb35-paper/round01/middle/high_edge_intersection_repair_20261020/REPORT.md#2-共同概率判据及强共度进口).

For outer edges G,J intersecting in three points, put A=G\J and B=J\G, each of size two. The usual degree budget gives c(G,J)≤16. If equality holds, every point of A and B has degree9 and all eight of its edges other than its own outer edge must be valid middle edges. Thus there are exactly16 original middle edges, each meeting A and B once, and no other edge meets A∪B except G,J and these middle edges.

There are four cross point pairs in A×B, each of codegree at most4; their middle-edge counts sum16, so each has codegree exactly4. The two within-side pairs occur only in G and J respectively. Consequently the four-lock exact inventory on A∪B is forced:

    μ0=17; μA=μB=1; μ{a,b}=4 for every a∈A,b∈B;
    all other nonempty traces zero.                        (7)

A single fixed certificate at lock positions(8,9,20,21), using the [conditional permutation criterion](../PROBABILITY_LEMMAS.md), gives

    Σ min(Ak,Bk,Ck−lk)=250309/437580<1.

The certificate and an independent expansion into35 original edge indices and1190 ordered distinct edge pairs are saved in SATURATION.json and SATURATION.py in the evidence directory below. There is no unknown inventory in (7). Hence equality16 supplies a proper coloring of the actual H. A non-B input in this role must therefore satisfy

    C3≤15n3.                                               (8)

Retaining C3≤16n3 gives the unconditional intermediate calculation in §5 before this one-profile repair import; the strict improvement (8) is separately identifiable.

## 5. A joint weighted upper bound and the resulting A1 inequality

Use D=352716 and the 21/22-point path numerators

    r=(36,120,330,792,1716).

For nonnegative Cj and any α≥0,

    R:=Σ_j rj Cj ≤ αP+Σ_j(rj−α)_+ Uj                      (9)

whenever Cj≤Uj. This follows by subtracting αΣCj and discarding only negative coefficients.

Take α=120. The j0 term is negative and the j1 term is zero; hence no independent C0 or C1 capacity is needed:

    R≤120P+210C2+672C3+1596C4.

If any three-intersection outer pair has16 middle edges, §4 already supplies a proper coloring. Otherwise use C2≤24n2, (8), and C4≤4n4. The last bound follows because a valid middle for a four-intersection outer pair must contain its two singleton-difference points, whose codegree is at most4. Combining with (6),

    R/2+3432n1
    ≤5016n1+2520n2+5040n3+3192n4+7128=:L15.               (10)

The exact two-flip repair criterion is R/2+3432n1<2722720. Thus L15<2722720 suffices for an original proper coloring; every non-B reduced-A1 input must have L15≥2722720.

Point-pair coverage supplies

    n1=368−2τ+3n3+8n4,
    n2=140+τ−3n3−6n4,
    n0=87+τ−n3−3n4,
    τ=Σ_{u<v} C(λuv−1,2)≥0.

Substitution in (10) yields

    L15=2205816+12528n3+28200n4−7512τ.

All three variable coefficients are divisible by24. Therefore a non-B input necessarily satisfies

    522n3+1175n4−313τ≥21538.                              (11)

In particular n3+n4≥19; if n4=0, then n3≥42. With only C3≤16n3, the same argument gives the weaker intermediate inequality

    536n3+1175n4−313τ≥21538.                              (12)

This intermediate inequality already strengthens the previous independently allocated middle capacities throughout the A1 moment domain. Specifically, if Lold is the shared-C1 expression in GLOBAL_TWO_FLIP_PATH_REPAIR §6.3, then the α120 expression before (8), denoted L16, obeys

    L16−Lold=−15598−353τ−1729n2−1161n3<0.

The α36 version with the same nine-exception wedge budget is also uniformly weaker:

    L16−L36=−(19250+196τ+5012n2+3024n3)/5<0.

After applying (8), L15=L16−336n3. Thus the improvement is not confined to one favorable abstract intersection distribution.

## 6. With the separate bound n4≤11: what follows and what remains

The separate [A1 balanced-star forest theorem](TWENTYONE_A1_BALANCED_STAR_FOREST.md) supplies n4≤11 in the remaining non-B role, with the repair imports recorded there. That new structural ingredient is root-checked; its newer designated cross-family review is separate. The wedge proof above does not depend on how that bound is established.

Even the intermediate (12) gives n3≥17 and n3+n4≥28. Combining it with n2≥0 gives the exact relation403τ≤10426+309n4, hence τ≤34. The constant is10426.

The stronger (11) gives

    139τ≤2822+131n4,

and therefore τ≤30 when n4≤11. These are source-free actual counterexample constraints, not a coloring theorem for every input satisfying the residual bounds.

A cheap, more stringent common-graph relaxation still survives; it is included to state the exact stopping point rather than claim a contradiction from unrealizable aggregate numbers.

### A scalar singleton-graph majorant

Construct the simple graph on the35 original H-edge indices, adjacent exactly at singleton intersection. Its degrees are s(F), and it has n1 graph edges. By (3), P≤Σ_F f(s(F)); the integer function f has nondecreasing increments f(s+1)−f(s)=s−floor(s/5).

For any simple graph with a fixed edge count, a maximizer of this convex degree sum can be chosen with nested neighborhoods, hence a threshold graph. To see this without an external extremal import, choose a maximizer with lexicographically maximal sorted degree vector. If du≤dv and u has a neighbor w≠v not adjacent to v, move uw to vw. Convexity does not decrease the objective and the sorted degree vector strictly increases, a contradiction. Thus N(u)\{v}⊆N(v)\{u}. If the minimum degree is positive, this nesting makes a maximum-degree vertex universal; otherwise there is an isolated vertex. Removal preserves the nesting, proving the recursive threshold representation.

Define T(n,m,r) as the largest Σf(final degree) for an n-vertex threshold graph with m remaining edges and an offset r already-universal removed vertices. Then

    T(n,m,r)=max{ f(r)+T(n−1,m,r),
                   f(n−1+r)+T(n−1,m−n+1,r+1) },

with T(0,0,r)=0 and invalid edge counts excluded. Therefore

    P≤min{T(35,n1,0),(132n1+594)/5}.                       (13)

This is a degree-sum upper bound on the singleton graph, not a generation of hypergraphs. Only24506 small integer states are used for the required n1 range.

For the numerical diagnostic, use397≤n1≤546. The lower bound is the one-flip repair criterion. For the upper bound, let ℓv count singleton-intersection pairs meeting exactly at v. The six-star A1 repetition budget gives ℓx≤13. The [already-closed four-intersection kernels through p](../../context/propertyb35-paper/round01/middle/high_edge_intersection_repair_20261020/REPORT.md) give ℓp≤17: its link cover has surplus8, its nonempty pair intersections have size at most2, so at least4 of its21 edge pairs are not singleton. Ordinary link-cover quotas give ℓv≤24 for degree8 and≤30 for degree9. Summing gives n1≤13+17+9·24+10·30=546.

For each integer moment profile with0≤τ≤140,0≤n4≤11,nj≥0 and397≤n1≤546, bound the five Cj simultaneously by (13) and

    C≤(33n0,26n1+339,24n2,15n3,4n4).

Fill the highest r-weight first to maximize R under these capacities; all arithmetic is exact. This complete, deliberately relaxed scalar domain has29733 profiles and219 survivors. It forces n3≥21 and n3+n4≥32 within these combined necessary conditions, but does not eliminate all profiles.

For example,

    (n0,n1,n2,n3,n4)=(33,519,11,21,11), τ=0,
    Pupper=13074,
    (C0,C1,C2,C3,C4)=(0,12451,264,315,44)

satisfies the retained bounds and gives R/2+3432n1=2734320≥2722720. These numbers are a feasible aggregate obstruction to this relaxation, not an actual H. The C2,C3,C4 bounds and total P are saturated, while C1 has slack. Thus improving only the previous shared-C1 price cannot remove this witness; further common support for high-intersection outer pairs or the attachment-colored singleton graph is missing.

## 7. Exact evidence and scope

Evidence directory:

    context/propertyb35-paper/round01/middle/a1_middle_wedge_capacity_20261020/

CHECK.py uses exact integer/Fraction arithmetic for the wedge inequalities, all nine-exception constants, both price choices, coefficient identities and the saved residual witness. It also compares the threshold recurrence with independent direct threshold-string construction through nine vertices. CHECK.json is PASS.

SATURATION.py/json record the single forced inventory (7), its strict fixed certificate and independent35-index replay. GRAPH_PILOT.py/json retain all219 surviving exact moment/C-capacity profiles and the scalar T values. Earlier n4≤13 and C3≤16 diagnostics remain separate historical outputs; they are not the final domain. A final scalar diagnostic run takes about0.27 CPU seconds, the equality-profile certificate about0.014, and the arithmetic check about0.044; no H search, new q2 inventory table, Lean, MCP or navigation edit is used.

The analytic inequalities (1)–(12) apply to the stated actual H. The conditional n4≤11 corollaries have the precise separate import identified above. The219 surviving aggregates are not asserted realizable, and no infeasibility assertion or global A1 completion is made. New designated cross-family acceptance is recorded separately by the main project.
