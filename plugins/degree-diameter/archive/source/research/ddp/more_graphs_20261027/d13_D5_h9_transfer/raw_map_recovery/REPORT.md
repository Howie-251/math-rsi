# Derivation Package: degree13 raw-map binding

## Target
Test whether classwise pairflips recover the oldauthor13core inside current51417, and give the correct orientation-free Baer13 fallback.

## Status
COHERENT AFTER REFRAMING. The proposed oldcore gauge is impossible. Wholeclassclosure has a sound R4 interface, but its assigned fixed F3-plane degreepool is empty.

## Invariant Object
For every labelled F33397 edge, the number of edges in its core bipartite block is invariant under independent flips within the two endpointclasses.

## Assumptions
Use the already bound actual50554 core, the same17157 splitclasses, savedold50750authorgraph, and inherited Fpolar/core-walk lifting theorem. This note does not reconstruct incidence or assume unchanged colours.

## Notation
Sourcefile tau is an order4 point-line duality on132860 labels. The point involution here is phi(p)=tau[tau[p]], equal to coordinate Frobenius. Never apply source tau once as a pointconjugation. B denotes a13-point Baer; C denotes its fullcurrentclass closure.

## Derivation Strategy
Use blockcardinality first; no search over2^17157 pairflip assignments is necessary. If the oldmap fails, count the exact cost of lifting an entire endpointclass.

## Derivation Map
Old/current edgeblocks -> gauge invariant -> one contradiction. Independently, raw B -> B union phi(B) -> complete currentclasses -> inherited Fwalk lifting -> core R4.

## Main Derivation
The Fedge26--15837 has coreclasses{29,49} and{20913,36638}. Its oldcore block has all four edges. Its currentblock has only29--36638 and49--20913. A pairflip bijects the four potential crosspairs, so it cannot map four oldedges into two currentedges. Thus neither equality nor an oldedge-preserving homomorphism of this fixed oldcore can arise from the allowed classwise flips.

The one finite166425block pass found1345 blocks4->2 and1345 blocks2->4, plus8 changed perfectmatching blocks with unchanged counts. The first witness alone suffices. CPU1.26067943 seconds; zeroBFS and zero poolgeneration here. It does not exclude a different colour-dependent rawH9 realization, which was neither reconstructed nor certified.

For the fallback let j be the number of nonfixed phi-pairs both of whose rawpoints lie in B. Let t be the number of current splitpairs among all pairs hit by B. Then

    C = {pi13(p), pi13(phi(p)) : p in B},
    |C| = 13 - j + t.

Indeed B has13 rawpoints but each doubly hit pair contributes one quotientclass, giving13-j classes; every selected currently splitclass contributes one additional currentvertex. Hence |C|<=13 exactly when t<=j. Every pin must also have actualdegree<13, and anchorcap is13-|C|. The current extras require full actual coverage separately.

C is the fullpreimage of the raw Baer's selected Fclasses. Inherited blocking gives F-radius4 coverage of those classes. Each actualcore quotientedge block is complete or a perfectmatching, so every Fwalk lifts from every currentvertex; its endpoint lands in C. Therefore R4_K(C)=K without any raworientation map.

## Remarks and Interpretation
The root-assigned pool agent separately completed7560Baers x1120savedF3planes (8467200 placements). Its1740 degree-legal wholeclosures have pin counts21:814,22:158,26:768, so none fits13. This is reused evidence from ../baer13_transfer/RESULT.json, CPU0.98348703, noR4. No duplicate pool was run here.

## Boundaries and Non-Claims
No orientation-correct map for nonstable direct13raw pinsets was exported. The gauge obstruction concerns classwise flips of the fixedoldcore. The emptyclosure pool concerns the fixed1120F3defined planes, not all Q9 planes, blocking sets or alternative rawgeometries. No newgraph, diameter measurement, globalWiki edit or hash was produced.

## Open Risks
The broader colour-dependent rawrealization remains unproved, and directnonstable Baer transfer cannot borrow the canonical map without additional binding. Parent has stopped this branch; no such further work is scheduled.
