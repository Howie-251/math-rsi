# Complete left-H-equivariant matching domain and factored cross gate

This is a paper extension of the same actual684 two-orbit source question. No shift, parameter pair, endpoint set, graph or BFS is evaluated here. It does not authorize a full-family finite run. The shared-t gate is owned by the separate numeric task.

## Complete matching domain

Use host vertices(h,σ), h∈H342 and σ∈{0,1}, with the actual common free left action L_k(h,σ)=(k*h,σ). Let f be an H-equivariant bijection from the copy0 vertex set to the copy1 vertex set. Write

f(e,σ)=(tσ,πσ).

Equivariance forces f(h,σ)=L_h f(e,σ)=(h*tσ,πσ). Each source orbit maps bijectively onto the indicated target orbit because right multiplication by tσ is a bijection. If both source orbits had the same target orbit, f would not be injective or surjective. Therefore π is a permutation of the two source types.

Conversely, every π∈S2 and arbitrary independent t0,t1∈H define an equivariant bijection by this formula. Its values at(e,0),(e,1) recover all parameters uniquely. Thus the complete domain of equivariant perfect matchings is precisely

(π,t0,t1)∈S2×H×H,

of size2·342²=233928. This is all matchings commuting with the specified left-H action, not all permutations of684 vertices. The old shared-shift family is only the subdomain π=id,t0=t1.

The cross edges are the undirected matching

(h,σ,0)—(h*tσ,πσ,1).

The reverse crossing at(g,κ,1) uses σ=π^(-1)κ and sends it to(g*tσ^(-1),σ,0). There is **no** requirement t1=t0^(-1), even if π swaps the two types. The reverse operation is f^(-1) on the other copy, not a second forward application of f. There is also no requirement that π or f be an automorphism of the original host; they define a new matching between two copies.

## Degree and the swap case

Every global vertex has exactly one cross partner. The two source copies remain unchanged and disjoint, so any such matching gives a simple8-regular1368-vertex graph if the inherited host is simple7-regular. This holds for both π=id and the type swap. In particular swapping source types across copies does not delete or relabel any edge inside either old copy; all within-copy diameter-four routes remain available.

For any cross-copy pair, cross immediately and then use an old source walk of length≤4. Hence every proposed graph has diameter≤5. A cross-copy walk of length≤4 has one or three crossings. With three crossings it has at most one old edge, so two crossings are consecutive and cancel as f followed by f^(-1), irrespective of the intervening source types. Thus only one-cross paths are needed for an exact diameter-four cross test.

## Factored endpoint sets

Keep the actual typed old-walk endpoint sets A_{τσ}^{≤a} from `PAPER_INTERFACE.md`; identity is included at length0 only when the two types agree. For a proposed old-leg meeting typeσ, a route starting from(e,τ,0), crossing once and ending in target typeρ has endpoint

u*tσ*v,

with u∈A_{τσ}^{≤a}, v∈A_{πσ,ρ}^{≤b}, and a+b≤3. Define the precomputable set

C_{τσρ}(t,κ)
 = union over a,b≥0, a+b≤3 of A_{τσ}^{≤a} *t* A_{κρ}^{≤b}.

For fixed(π,t0,t1), the exact condition for every target of each ordered type pair(τ,ρ) to be within4 is

C_{τ,0,ρ}(t0,π0) union C_{τ,1,ρ}(t1,π1) = H.

All four ordered pairs(τ,ρ) must pass. The sets are independent of the other meeting type's parameter, so they can be computed once for the individual t and post-cross typeκ. With any fixed enumeration of H, each C is a342-bit integer and each final slot condition is one bitwise OR compared with the all-H mask. This is a complete factorization of this domain, not an approximation based on individual helper/pin coverage.

The common left-H action commutes with every f(h,σ)=(h*tσ,πσ), so arbitrary cross pairs still reduce to the two starting roots(e,τ,copy0), τ=0,1. Undirected distance covers the reverse-copy direction. Type swap does not restore a one-orbit transitivity assumption.

If all four slot unions are full, the graph has diameter≤4 and hence exact diameter4 by the degree8/diameter3 Moore bound457<1368. If a slot fails, some cross distance is at least5, while the universal upper bound is5, so the candidate has exact diameter5. These facts do not require separately generating or running a BFS on every matching.

## Optional automorphism prune and scope

For a general matching map f, being an old-host automorphism is an extra property, not part of the domain definition. With the actual right-voltage convention its exact connection-set condition is

tσ^(-1) S_{σρ} tρ = S_{πσ,πρ}

for all old ordered source-type pairs. If this holds, relabel copy1 by f^(-1) and obtain the Cartesian prism of the host with K2, of diameter5. For the old shared identity-type case this reduces to simultaneously normalizing all four S-sets. It would be incorrect to apply that narrower normalization criterion as a general domain restriction, or to assume arbitrary right shifts are automorphisms.

The complete domain and factorization above are supported on paper. The initial same684 shared-t finite gate may provide feedback, but its failure alone would not exclude independent t0,t1 or swapped π. No full233928-family gate, candidate graph, source check, solver, field arithmetic or BFS is run by this note. A later exact finite gate, if separately authorized, must preserve all parameters and all four slots; a complete negative result would close only this fixed-host left-H-equivariant matching family, not arbitrary matchings or general(8,4) graphs.
