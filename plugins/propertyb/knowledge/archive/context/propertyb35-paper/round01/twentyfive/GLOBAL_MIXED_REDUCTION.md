# Global mixed-degree reduction: a uniform criterion and a real obstruction

The completed r=1 and r=2 proofs do not justify a monotone reduction of all higher-r cases to the two-low eight-unit gate. There is an explicit obstruction inside the actual25-point,35-edge hypergraph class, already when r=3. Two useful conclusions are nevertheless available: a parameterized positive reduction to the existing gate, and a single new eight-unit interface that would cover all r=3,4 no-K5 cases at once.

Throughout, H is simple and five-uniform, has25 points and35 edges, covers every pair, and has minimum degree6. Let L be its r six-degree points, S its s seven-degree points, and A its h higher-degree points. The degree sum gives

s=25−r−h,   Σ_{v∈A}(d(v)−7)=r,   1≤h≤r

when r>0. Every low point is unit to all points. On S the positive-weight graph F for w=λ−1 has weighted rows at most4 and ordinary maximum degree4. A K5 in F exhausts the five weighted rows, so is a complete component with all weights1 and no exterior weight in the full graph.

## 1. A parameterized positive reduction to the already-proved q=2 gate

**Proposition.** If r≥2 and α(F)≥6, H has Property B. More explicitly, let c be the number of K5 components in F. If

c+ceil((s−5c)/4) ≥6,

then H has Property B. Equivalently, the displayed sufficient condition is s−c≥21.

**Proof.** Six independent points of F are six seven-degree points with all mutual codegrees1. Add any two points of L. The resulting eight points are pairwise unit, with degrees6²,7⁶, and `MIXED_TWO_SIX_UNIT8.md` applies regardless of the individual degrees of the unlocked points. For the explicit estimate, select one point from each of the c K5 components. Delete those components, and apply Brooks's four-color theorem to the rest; the odd-cycle exception also uses at most four colors. A largest color class supplies at least ceil((s−5c)/4) additional independent points. There are no edges to the deleted components. ∎

In particular, with no seven-degree K5, every case with r+h≤4 reduces directly to the existing gate. This includes the no-K5 r=3 spectrum6³,10,7²¹. It does not include all r=3 spectra. A remaining non-B candidate must have α(F)≤5, hence s−c≤20. This criterion is uniform in r; it does not depend on a new private-star table.

## 2. Universal q=2 lock reselection is false in the actual class

Points are (x,y)∈F5², encoded5x+y. Start with the30 standard affine lines: the five vertical lines and y=mx+b for m,b∈F5. Add the following five non-line edges:

| Edge | Example A | Example B |
|---|---|---|
|E1|{0,2,3,4,5}|{0,3,4,5,6}|
|E2|{0,6,7,8,9}|{0,7,8,9,10}|
|E3|{0,10,11,12,13}|{1,11,12,13,14}|
|E4|{1,14,15,16,17}|{1,2,15,16,17}|
|E5|{1,18,19,20,21}|{2,18,19,20,21}|

These are two explicit simple35-edge pair-covering five-uniform hypergraphs, not abstract degree or graph models. Their six-degree points are22,23,24.

* Example A has degrees6³,9,8,7²⁰. Its seven-degree graph is five disjoint K4 components: the four seven-degree points in each extra edge.
* Example B has degrees6³,8³,7¹⁹. Its seven-degree graph is four K4 components and one K3 component: the latter is{15,16,17} in E4.

The extra edges have pairwise intersections only at higher-degree points. Thus the asserted seven-degree components follow directly, and there is no seven-degree K5. Their independence numbers are exactly5: select one point from each complete component, and no independent set can select more than one from any component. Consequently neither actual H contains eight unit locks with exactly two six-degree and six seven-degree points. No choice of a minimum-empty unit set can create a sixth seven-degree independent point in either example.

Both H are properly colored by the explicit red set

{1,2,3,4,5,6,10,14,15,19,20,21}.

Thus these examples do not challenge Property B. They show that any universal reduction to the q=2 gate must alter the mathematical interface or edge constraints; it cannot consist solely of choosing different locks in the unchanged H.

`GLOBAL_MIXED_REDUCTION_CHECK.py/json` lists all35 edges of each H and verifies simplicity, every degree, pair coverage, all low-point unit equations, the exact support components, the unit sets below and the displayed proper colorings. Only these two H are checked. Runtime0.23 seconds.

## 3. Degree virtualization is algebraically valid but raw-bound inheritance fails

There is a genuine parameterized compression at the level of trace inventories. For a fixed eight-unit clique family B, set

b=35−|B|−Σ_i(7−inc_B(i)).

This is the all-seven empty count before low labels are imposed. The already complete65-family catalogue has b≥−2; its families with b=−2 are exactly11,12,14,27,58. For q≥2 low marks, the actual empty count is b+q≥q−2. Raising any q−2 low singleton counts by1 and reducing empty by q−2 produces a nonnegative virtual inventory with exactly two low marks, all the same large traces, the same35-edge total and all unit pair equations. Therefore all q≥2 eight-lock domains use the same previously known clique families; a new q does not require a new clique-family classification.

This virtual inventory is a numerical relaxation, without an operation on the actual H that preserves its coloring problem. In particular, one cannot simply reuse its strict raw certificate. Example B supplies a concrete failure. Its actual unit set is

I=(22,23,24,3,7,11,15,18),

with three low locks in the first three coordinates. Virtually raise the first low coordinate by replacing one empty trace with its singleton. The q=2 certificate transported to positions

(22,25,12,24,15,20,21,23)

has raw bound108973/123760<1 on that virtual inventory. On the unchanged actual q=3 inventory the identical layout has raw bound74785/74256>1. Both values are recomputed from the actual35 edges. Thus the proposed fixed-layout monotonicity under singleton→empty transfer is false. The script checks all three possible one-low virtual raises of this actual input; the selected q=2 witnesses all cease to be strict, but this does not exclude other layouts from working on q=3.

The obstruction is exact: shifting a singleton to empty changes free-pivot event sizes and quadratic raw C terms; the sum of pointwise minima has no automatic monotonicity. A future uniform comparison must prove a new inequality, not identify the two inventories.

## 4. One new eight-unit gate would cover r=3 and r=4 together

The most economical next mathematical obligation is a single conditional theorem:

**Gate(8,3).** A25-point,35-edge pair-covering simple five-uniform H with eight pairwise unit locks, three of degree6 and five of degree7, has Property B; unlocked degrees are unrestricted.

This is an unproved obligation here. It requires only the existing65 clique families with three low labels, actual singleton subtraction at each mark and empty shift+3. The preceding virtual-inventory proposition identifies its family domain with the same previously classified families, but does not prove the required probability bound.

If Gate(8,3) is established, it has the following complete actual caller without new r-specific star classifications. Assume no seven-degree K5 component. Brooks gives at least ceil(s/4) seven-degree unit points. Whenever r≥3 and s≥17, select five of these and three low points. Since s=25−r−h, the single condition r+h≤8 suffices. In particular:

* r=3 has h≤3, hence s≥19 and the caller always works;
* r=4 has h≤4, hence s≥17 and the caller always works.

So one Gate(8,3) would close all r=3 and r=4 no-K5 spectra at once, and also every higher-r no-K5 case satisfying r+h≤8. This is a local gate attached to a global degree/graph argument, rather than one fresh star domain per degree spectrum. The branch with a seven-degree K5 remains a separate single-G obligation; Gate(8,3) alone does not close it.

No q=3 table or extra-point domain has been generated in this analysis. A bounded fixed-layout profile for this one conditional interface would have a clear mathematical payoff and a fixed stopping point if analytic comparison does not emerge.

## 5. Single entry for the completed r=2 branch

**Theorem (r=2).** Every H satisfying the standing assumptions and having exactly two six-degree points has Property B.

The degree surplus is2, so the spectrum is either6²,9,7²² or6²,8²,7²¹. If no seven-degree K5 component exists, Brooks yields at least six independent seven-degree points because s≥21; adjoining the two low points invokes the complete q=2 eight-unit gate. If a seven-degree K5 component exists, its rows force a group with internal λ2 and exterior λ1. Spectrum6²,9,7²² is covered by `MIXED_TWO_SIX_K5_A.md`; spectrum6²,8²,7²¹ by `MIXED_TWO_SIX_K5_B.md`. Those two proofs explicitly include inventories12 and25, the possibility that both global D=1 points are eight-degree, and the full8/8 slot domain with row8 bound, so no all-seven or unique-special black box is being substituted. ∎

The exact evidence is1566 independent q=2 gate inputs (maximum3093/3094),42 new Case A forced inputs (maximum37491/38896), and116 new Case B forced inputs (maximum20773/20995), together with their stated earlier single-G selection and certificate dependencies. Each has a complete independent domain/ABC replay. This is the paper-level r=2 result submitted to the root agent; designated cross-model review remains separate.
