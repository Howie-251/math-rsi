# Independent attack: arbitrary free-edge additions after uniform saturation

2026-11-01. **The new necessary bound is supported by the complete paper route
classification below.** The old fixed-free-adjacency route formula does not
survive: a single degree-legal k2 peer-clone gadget gives an actual new3route.
Its degree cost is precisely included in the new bound. The one new tiny test
used0.033554806 CPU/5, two13-vertex helper BFS runs, and no q8 graph, field,
geometry, projection, old toy, solver, Lean or external-review execution.

## Exact assumptions and the saturation reduction

Let H be a finite delta-regular simple host and C a center set whose open
neighborhoods are pairwise disjoint, with union V(H) minus D. Assume D is a
subset of C, every D vertex is isolated in H[C], and C_off=C minus D induces a
perfect matching T. Write M=|C_off|. Form exactly k>=1 full original-N_H(c)
clones for every c in C, with cap Delta=delta+k. Retain every source and
mandatory clone edge. Add any edges among existing vertices and any edges
involving a finite nonempty set B of new vertices, while keeping the same cap.
All graphs and additions are simple.

Put U=V(H) minus D and F=D together with all existing clones. Each u in U
belongs to exactly one center neighborhood, hence receives exactly k mandatory
clone edges. Its degree is already delta+k=Delta. No genuinely new edge can
touch U; in particular every old C_off center is saturated. Every f in F has
exactly delta mandatory neighbors, all in U. Initially there are no F-F edges:
D has no center neighbor, clones only meet original neighborhoods, and no
center neighborhood contains D. Thus every added F-F or B-F edge spends one
of f's at most k extra slots. A new helper has neighbors only in F or B.

For h in B let p_h=|N(h) intersect F| and d_h=|N(h) intersect B|. Then

    p_h+d_h = degree(h) <= Delta.

No uniqueness of class owners or pins is assumed. Multiple helpers may use
the same class or different copies of it; every actual pin edge still pays
degree at both endpoints.

## Exhaustive classification of helper-to-old-C_off walks of length at most3

Fix h in B and c in C_off. There is no edge from any helper directly to c,
because c is saturated. Classify a possible nonempty walk by its first step.
Backtracking or repeated vertices create no omitted type in this classification.

### First step h-f with f in F

Only two more edges are available.

If f is a clone of base a in C_off, its mandatory direct old C_off neighbor is
T(a), the only neighbor of a inside C. A mandatory two-step suffix f-u-c,
with u an old source vertex, requires

    u in N_H(a) intersect N_H(c).

Disjoint center neighborhoods force c=a. Therefore all mandatory source
suffixes from this f reach at most the two targets a and T(a). If f is an old
D vertex, the same intersection argument rules out any two-step source suffix
to C_off, and D has no direct C_off neighbor. A clone based in D likewise
has no such C_off source suffix. Using the upper bound2 uniformly is safe.

An added first suffix edge f-f' with f' in F leaves only f'-c. Since c is
saturated, that last edge must be mandatory. Every f' has at most one direct
old C_off neighbor: a clone of an off-center a' can reach only T(a'), and old
D vertices or D-based clones reach none. Thus each F-peer edge adds at most
one target. An added suffix edge f-g with g in B adds none, because g-c is
forbidden. There is no new edge from f to U.

The particular h-f edge already uses one of f's k extra slots. Consequently

    added_F_peer_degree(f) <= k-1,
    targets reachable with first edge h-f <= 2+(k-1)=k+1.

Other B-neighbors of f consume further slots; repeated targets and D pins only
decrease useful coverage. This argument permits arbitrary edges throughout F.
It does not silently assume the old fixed-adjacency condition.

### First step h-g with g in B

With two steps left, g cannot go through U because helpers have no U neighbors.
A second helper cannot take the last edge to saturated c. Thus the only
possible suffix is g-f-c with f in F, and each actual F-pin of g has at most
one direct old C_off target. This first-step type covers at most p_g targets.
Using a peer edge after g-f would require four total edges, not three.

The two first-step types cover every walk of length at most3 to C_off. Hence
diameter at most3 of the final augmentation requires, for every h in B,

    M <= (k+1)p_h + sum_{g in N_B(h)} p_g.                 (1)

This is a union upper bound, not an exact center-coverage equivalence. All
overlaps make its right side larger and cannot invalidate necessity.

## The summed degree obstruction

Let t=|B|>0. The induced helper graph is undirected, so double-counting the
second term of (1) gives

    Mt <= sum_h p_h(k+1+d_h)
       <= sum_h (Delta-d_h)(k+1+d_h).

For any integer d,

    4(Delta-d)(k+1+d)
      = (Delta+k+1)^2 - (2d-(Delta-k-1))^2.

Each summand is therefore at most floor((Delta+k+1)^2/4). Dividing by t yields

    M <= floor((Delta+k+1)^2/4)
      = floor((delta+2k+1)^2/4).                          (2)

The unrestricted quadratic vertex is d=(delta-1)/2. Restricting d to actual
helper graph degrees or enforcing global F-slot consistency can only lower
capacity, so neither restriction is needed for this necessary upper bound.
Equality or failure of (2) to exclude a parameter is not an existence result.

The condition t>0 matters: this does not forbid adding edges solely among F
while retaining the same vertex set. It forbids an increase in order in the
stated cap ranges, even when such free-edge changes accompany the new vertices.

## The targeted counterexample to the obsolete route formula

Take H to be matching edges0-1 and2-3, delta1, C=all4 old vertices and D=empty.
Its center open neighborhoods are disjoint and cover H, and T(c)=c xor1.
With k2, add two full-N clones/class and cap Delta3. Label clone(c,r)=4+2c+r
and the new helper h=12. Add h-4 and the peer edge4-8.

All13 vertex degrees are at most3. Without the peer edge, h reaches old
targets{0,1} within3. With it, the actual walk

    h12 -> clone_0(4) -> clone_2(8) -> old3=T(2)

has length3, and the reachable old target set becomes{0,1,3}. The old fixed
adjacency condition h in S_c union N_B[S_T(c)] misses c=3: h owns only class0
and the helper graph has no edge. Thus that old exact-route lemma genuinely
cannot be reused here. The new first-pin bound is tight for this local witness:
three targets=k+1. Old2 remains at distance4, so no whole-graph D3 claim is made.

Using the same two extra edges with k1 makes the first pin degree3 while its
cap is2. It is not a legal k1 counterexample. The test checks actual adjacency,
all vertex degrees, and helper-to-old distances in both k2 configurations.
No optional auxiliary exhaustive enumeration or previous toy was executed.

## Consequences and limits

|source|delta|M|excluded uniform k|maximum excluded cap|bound there|first unexcluded k/cap|bound there|
|---|---:|---:|---|---:|---:|---|---:|
|balanced|81|4160|1..23|104|4096|24 /105|4225|
|Payne|80|4032|1..22|102|3906|23 /103|4032|

For balanced, (2) is M<=(k+41)^2; for Payne it is
M<=(k+40)(k+41). Thus the accepted k1 degree82 graph cannot gain any new
vertices at cap82 by keeping every existing edge, even if arbitrary edges
among its currently free vertices are added. This is a statement about this
fixed edge-preserving augmentation interface, not a bound on global N(82,3).

Allowing F-F edges enlarges the augmentation model, so these excluded k ranges
are smaller than those in the earlier fixed-F-adjacency note. Nothing here
excludes nonuniform cloning, deleting or modifying mandatory edges, changing
the source/code, constructing jointly before saturation, or using a higher cap.
It does not automatically apply to P33 or F9 U10, whose old free complement
is not a subset of the center code. No q8 or other complete graph was generated.

The current three-target remote C review concerns only the original80/81/82
graph claims. This new paper lemma has not thereby acquired external-review,
Lean, novelty or global-record status. No root counts or frozen artifacts were
changed. RESULT/TERMINAL and the small executable Python witness are saved next
to this note; all processes are terminal.
