# Rajiv19 source: exact pin providers and a closed geometric-line rule

The source is Rajiv's public September2026 fibre extension Γ(11;X,X′;K),
with1331 points and1452 lines, n2783, m25773. Points have degree18 and one
spare slot at cap19; all lines have degree19. The public source's diameter3
and Theorem1 are inherited. No old source-diameter BFS is rerun, and this
source reproduction is not a new graph result.

## Exact bridge to the author definition

The retrieved small witness gives X={2,4,5,6,7,9}, X′={1,3,8,10} over F11,
and242 undirected gadget edges on121 labels a*11+l. Their gadget degree is4,
all gadget edges are between distinct pencils; the complete class graph K
adds the4 pencil edges and is8regular.

`prepare.py` constructs all normalized affine PG points and all isotropic
lines not through ∞ directly. For each direction(1,k), h,l∈F11, the line is

    {(h,0,1,k)} ∪ {(l+h*z,1,z,k*z−h):z∈F11},

with projective normalization of every representative. For the last
direction(0,1), the line is

    {(h,0,0,1)} ∪ {(l+h*z,1,h,z):z∈F11}.

Each is the span of its displayed infinity point and the z=0 point; their
alternating product is0. The1452 distinct lines give all q²(q+1) isotropic
lines avoiding ∞. Sorting the normalized affine points, and sorting these
line sets by their sorted tuples, is exactly the author's `fibre_build`
point/line ordering. The12 lines M through ∞ are sorted identically; within
each M, intersections m are sorted, the same lexicographically least base
line is chosen for each pencil, then β(a,l)=z_l(base), exactly as the source.

This is a mathematical bridge to the author's generator definition, not a
claim of bytewise comparison with its unrequested large shipped adjacency
file. No foreign verifier entry point is executed. SOURCE_GEOMETRY.json saves
the complete point labels, original β line labels and pencil/base tables.
The source is generated once, in `source_d19_D3_n2783.edges`.

## Exact radius2 line provider of a point

A point r is incident with one line β_i(v_i(r)) in each class i. Its source
radius2 line targets in that class are precisely

    P(v_i(r)) ∪ N_gadget(v_i(r)),

where P(v) is the entire11line pencil containing v. Indeed its own incidence
line supplies v; point-fibre moves X followed by incidence supply the6
X-translates within that pencil; incidence followed by pencil edges X′ gives
the4 remaining translates. These are all11 pencil lines since X and X′
partition F11*. The only other routes are incidence then one of the4 gadget
edges. Thus each point gives exactly15 line targets per class,180 overall.
All1331 point provider formulas were compared exactly with the generated
adjacency's two-step unions and agreed. These are radius2 provider checks,
not a diameter3 BFS from every source root.

## Controlled comparison: orbit versus a geometric line

First take S_orbit={(a,1,0,0):a∈F11}. For any point(A,1,B,C), the alternating
form against the a-th pin is a−A, so the a=A pin is collinear with it (or is
the same point). Therefore all1331 point targets are covered in radius2.
In each line class, the11 incidence lines form one entire pencil, and gadget
boundaries give the remaining line coverage. Actual coverage is600/1452 line
targets, leaving852. This supports the point-coverage prediction, but leaves
a large line-only cover problem. No orbit+8 model was run or excluded.

The stronger controlled rule takes the11 affine points of one isotropic
W-line L0, using author class0 and β_0(0) for the concrete check. A point whose
unique collinear point on L0 lies in the affine part is within2 by incidence.
Otherwise it shares a transvection orbit with exactly one affine L0 point.
Since |X|=6>11/2, X+X=F11, so two point-fibre moves suffice. All1331 point
targets are again covered.

In the class containing L0, all11 pins are incident with L0, and their exact
line coverage is its full pencil plus the4 gadget neighbors of its Kvertex:
15 of121 lines. In any other class, their pencil indices are all distinct
(otherwise three lines/points give a forbidden W(11) triangle). They therefore
hit all11 pencils and cover every121 lines in that class. Actual source data
confirms1346/1452 total line targets, with only106 missing, all in class0.

## Complete reduction of every Wline-base-plus8 rule

There are at most8 more pointpins after spending11 on L0. In its exceptional
class each extra point supplies one provider P(v)∪N_gadget(v). Conversely,
every Kvertex v can be lifted to any of the11 affine points of its line;
different lines of this same class have no common affine point, so selected
distinct Kvertices lift to distinct available pointpins. Every other class
and every point target were already covered by L0.

Consequently every such19pin construction, over every possible base line and
class, is equivalent to selecting at most9 Kvertices whose providers cover
all121 Ktargets: one selected vertex supplies the11 base points and each of
the other8 supplies one extra point. Since each provider has size15,
8 providers cover at most120<121, so exactly9 distinct Kvertices are required.
The class copies use the same K, so no class/base seed search is needed.

## Exact capacity obstruction, with no solver

Nine selected Kvertices occupy at most9 of11 pencils. Choose any2 unoccupied
pencils A,B. Their22 vertices are not supplied by any selected full pencil,
so they must all be reached by gadget edges from the9 selected Kvertices.
For each of the55 possible pairs, compute each outside vertex's number of
gadget neighbors in A∪B and sum the9 largest contributions. This optimistic
sum permits duplicates of covered targets and ignores selected-pencil
conflicts, hence is a valid upper bound.

For54 pairs this bound is at most21, strictly below22. The only surviving
optimistic pair is A=3,B=9, where the bound is22. Thus there cannot be3 or more
unoccupied pencils, since among them there would be an already excluded pair.
There are exactly2 unoccupied pencils, namely3 and9, and one selected vertex
in each of the other9 pencils.

Now maximize the gadget contribution separately inside those9 selected
pencils. In their order0,1,2,4,5,6,7,8,10 the exact maxima are

    1,2,2,3,3,2,3,2,3,

whose sum is21<22. Even counting all overlaps favorably,22 omitted targets
cannot be covered. This closes the sole optimistic survivor, hence all
Wline-base11-plus8 pointpin rules. ALL_BASE_CAPACITY_FINAL.json saves all55
integer bounds, all nine final group bounds and their actual maximizing
vertices. `check_capacity.py` reproduces the tiny arithmetic without loading
or regenerating the source.

No MILP, SAT or other solver is required; the one30CPU solver authorization
was not used. Preprocessing measured0.182630432CPU; final capacity checking
0.002568460CPU. No new2784 graph or speculative pin set was generated.

## Scope and decision

Stop every one-Wline-plus8 variant, across all base lines and classes; do not
replace it by repeated base/seed scans. The11point base really does repair all
point targets and all other line classes, but the remaining class requires
mutually incompatible pencil and gadget coverage. This is a concrete failure
of simultaneous coverage, not only failure to find good pins.

Arbitrary19point pin covers, the original transvection-orbit-plus8 rule,
different sources and cooperative multiple-new-vertex mechanisms remain
open and were not searched. General source extension impossibility, new
public records, global optimality and additional Lean results are not claimed.

The obstruction also persists if other old-old edges are added within cap19:
each selected pointpin uses its only spare slot on the new vertex, while
every old line is already saturated. Therefore no added old-old edge can
change a two-step route from a selected pin to an old line. This observation
does not extend the exclusion to rewiring that deletes original edges.
