# Paper interface: two copies of the actual two-orbit684 host

This is a read-only conditional construction interface, not a generated1368-vertex graph or a test of shifts. No host/source BFS, endpoint enumeration, group/field verification, solver, cover construction, Lean or external review is run here. The separate source owner binds the published recipe and earlier scopes.

## Source correction and precise convention

The initial idea treated the684-vertex degree7/diameter4 host as a Cayley graph on a group of order684. That premise is not supported by the actual primary entry. The cached primary `research/ddp/m1_sources/desc_g4.html#74`, lines174–177, describes a two-vertex voltage lift over H=C38⋊_23 C9, with two orbits and no vertex transitivity. The earlier672 graph is the Cayley source mentioned nearby; it must not be confused with684.

For the actual684 recipe, old vertices are(h,τ), h∈H, τ∈{0,1}. An old edge has the form(h,τ)—(h*s,σ), s∈S_{τσ}, using the actual connection sets in the recovered recipe. The source owner's reported labels are342*τ+9*a+b for h=(a,b), with group product(a,b)(c,d)=(a+23^b*c mod38,b+d mod9). This paper takes the actual old simple graph and its degree7/diameter4 as inputs; it neither reconstructs nor verifies them. The read-only `HISTORY_SOURCE_GATE.json` now binds Michel de Messieres' published684-vertex/2394-edge source, communicated2026-10-05, to `research/ddp/m1_sources/684_recovered_construction.json` and the read-only generator `recover_684.py`; the inherited cached source validity is not rerun. Reverse connection sets use the literal group inverses, as required by the undirected source.

The corrected proposed matching uses one shared t∈H:

(h,τ,copy0) ↔ (h*t,τ,copy1).

It preserves the old source type τ and joins distinct copies. It is not the discarded one-root Cayley684 formula, not a type-swapping matching, not separate shifts for the two types, and not an arbitrary permutation matching.

## Actual connection-set and older-scope binding

The separate source owner read the literal right-multiplication generator, without executing it. Its actual sets are

```text
S00 = {(4,4),(8,5),(25,3),(29,6)}
S01 = {(2,2),(2,6),(24,3)}
S10 = {(26,7),(24,3),(2,6)}
S11 = {(10,1),(23,6),(26,8),(29,3)}
```

Each source vertex has four within-type and three other-type neighbors. These values and the right-product convention, not a hypothetical order684 group, define the proposed endpoint sets. The source-interface read gate reports1.5/5CPU conservative read/preparation charge and no same-fixed-host/shared-t342 strict NO located. This is a bounded local-history conclusion, not a claim that nobody has studied the model.

Earlier complete NO scopes are different: the684→685 one-vertex split, a p43/order774 free-projective host change, and deleting one of the source's three original cross matchings to reduce degree. They do not exclude adding the one inter-copy shared-shift matching. Exact references and inherited boundaries are preserved in `HISTORY_SOURCE_GATE.json`; this paper does not repeat any of those computations.

## Simplicity and degree

Take two disjoint copies of the original host and retain all their old edges. Right multiplication by t is a bijection of H, so the displayed edges form a perfect matching of the two684-point copies. Each old vertex receives exactly one cross-copy neighbor. All cross edges join different copies and therefore neither create loops nor duplicate a host edge. If the inherited source is7-regular, the resulting graph is simple8-regular on1368 vertices. With the inherited2394 source edges per copy, its edge count would be2·2394+684=5472. This remains a prediction for the proposed graph, not a produced file.

## Why one-cross paths are sufficient for a diameter-four test

A path from copy0 to copy1 has an odd number of matching crossings. At length≤4 it has either one crossing or three. In the three-cross case there is at most one host edge among the four steps, so two matching crossings must be consecutive. Since the matching's reverse is its literal inverse, those consecutive crossings return to the identical global vertex and can be erased. Thus every cross-copy walk of length≤4 has a one-cross walk of length≤4 with the same endpoints.

This does not assume right multiplication by t is a host automorphism. It uses only that each global vertex has one matching partner and the cross edges are undirected. It also does not extend automatically to a larger length bound where three crossings could be separated by host edges.

## Exact four typed endpoint conditions

For ℓ≥0 define A_{τσ}^{≤ℓ}⊆H as all group endpoint products of old-host walks of length≤ℓ from(e,τ) to a vertex of typeσ. These are typed old walks using the actual S-sets. At length zero the set is{e} if τ=σ and is empty otherwise.

Starting at(e,τ,copy0), a one-cross route with ℓ old steps first reaches(u,σ,copy0), where u∈A_{τσ}^{≤ℓ}. It crosses to(u*t,σ,copy1), then m old steps reach(u*t*v,ρ,copy1), where v∈A_{σρ}^{≤m}. Its length isℓ+1+m. Consequently every cross-copy target of typeρ is within4 exactly when

H = union over σ∈{0,1}, ℓ,m≥0, ℓ+m≤3 of
    A_{τσ}^{≤ℓ} * t * A_{σρ}^{≤m}.

This equality is required for **all four ordered type pairs(τ,ρ)**. One may equivalently use m=3−ℓ and ℓ=0..3 because the A-sets use the ≤ convention. Endpoint products must retain the type of the joining point σ; replacing these typed sets by an untyped Cayley ball loses information and is unjustified for this source.

Left multiplication L_k:(h,τ,copyi)↦(k*h,τ,copyi) preserves old edges and the matching, since(k*h)*t=k*(h*t). It acts freely and transitively on each fixed source-type/copy orbit. Therefore an arbitrary cross-copy pair(h,τ,0),(g,ρ,1) is reduced to(e,τ,0),(h^(-1)*g,ρ,1). Two starting representatives(e,0,0) and(e,1,0) suffice; there is no justified reduction to a single type. The reverse direction from copy1 to copy0 is already covered by symmetry of undirected distance.

Within each copy, all old host paths remain and have length≤4. Thus the four equalities above are necessary and sufficient for diameter≤4 of this fixed shared-shift graph. If they hold, its diameter is exactly4: the maximum-degree8 Moore bound for diameter3 is1+8+56+392=457<1368. If they fail, the graph has diameter exactly5: from any vertex one can cross immediately and then use a source walk of length≤4, so all distances are≤5.

## Which shifts are known to fail without testing

For t=e the graph is the Cartesian prism of the host with K2. Its cross-copy routes are one matching edge plus an old path; it has diameter5 because the host has diameter4. Equivalently the endpoint union reduces to the original radius-three ball. The degree7 rooted bound is1+7+42+252=302<684, so radius3 cannot cover the old host.

More generally, if R_t:(h,τ)↦(h*t,τ) is an automorphism of the host, relabel copy1 by R_t^(-1). The matching becomes the identity matching and both host copies remain unchanged as graphs. Again the graph is a prism and has diameter5.

With the stated right-voltage convention, R_t preserves each old connection relation exactly when

t^(-1) S_{τσ} t = S_{τσ}

for all four ordered source-type pairs. This follows by comparing(h*t)^(-1)*(h*s*t)=t^(-1)*s*t. Left multiplication is always a host automorphism; right multiplication is an automorphism only under the displayed connection-set condition. In particular a central t satisfies it, but arbitrary t must not be assumed to do so. If all actual S-sets were invariant under all conjugations, the whole shared-right-shift family would collapse to prisms; this paper does not assert or test that additional property.

## Decision boundary

The initial conditional Cayley formula was algebraically valid for a different one-orbit Cayley host, but the actual684 source does not meet that premise. The corrected two-orbit shared-shift interface above is the precise next question. No t has been tested, no endpoint union or candidate graph has been computed, and no source/path validity is rechecked here. A possible future finite gate must use the actual recovered S_{τσ}, both start types and all four endpoint conditions, while inheriting any genuinely matching earlier closed scope. Success would be a fixed1368/degree8/diameter4 candidate rule, not an already accepted graph or a priority claim. Failure for this rule would not exclude general(8,4) graphs, other matchings or other hosts.
