# Field-centred CRT control for the actual C54 source

Use the actual LEFT law on normalZ24681 and phaseC54. Normal factors are C3,C19,F433, with action orders2,9,54. Preserve the whole small factorC57 and its action47; this is a3078-state controller, not a C162 controller.

Conjugating by `(C,phase0)` sends `(n,j)` to `(n+(1-r^j)*C,j)`. Choose C=20577, with residues0mod57 and226mod433. Since the source involution field coordinate is414=-19 and r27=-1 inF433, its new field coordinate is `-19+2*226=0`. This is a source-group isomorphism and changes no controller coordinate. The positive field residues become `[324,8,42]`. Multiplying the field by143, while multiplying normal57 by1, gives `[1,278,377]=[1,-155,-56]`. Its full old scalar is U=11401, characterized by U=1mod57 and143mod433.

Thus the complete source coordinate map is

`F(n,j)=(U*(n+(1-788^j)*20577) mod24681,j)`.

The source involution's small normal coordinate remains19, so the normalized full involution is8227, not zero. The chosen normal control is precisely small57 residues `[10,2,2]`, field residues `[1,-155,-56]`, and phases `[33,2,16]`; involution smallnormal19/field0/phase27. The centred integers are frozen explicitly: replacing them by other F433 representatives gives an equivalent old source but a different target transfer.

The baseline threshold is exact: `1332774=54*57*433`, so retaining phase54 and normal57 needs q>433. The next eligible integer487 is prime and is1mod54. F487 has phi(54)=18 exact-order54 actions. No target root was computed. For each such rho, set the full action by CRT r=47mod57,r=rho mod487. Then r54=1; its field27power is-1, and its small27power is20mod57. The target full normals are `[7306,19325,22346]` and hnormal9253, obtained by CRT from the frozen source coordinates. True inverses must use `(-r^(-j)*n,-j)` in this new group, not copied source inverse normal values.

Every such recipe is simple7regular because its phases `[33,2,16,21,52,38,27]` are distinct and h is an involution. Connectivity can also be proved without source or target BFS. In the small57 quotient, r33=11, r2=43, r27=20. The commutator of g1 and g2 has normal `10*(1-43)+2*(11-1)=-1mod57`, generating C57, while phases2 and27 generate C54. Hence the fixed projected generators generate the3078-element quotient.

The commutator of h with g1 is zero on the small factor: `19*(1-11)+10*(20-1)=0mod57`. In the target field hnormal=0, g1normal=1, and rho27=-1, so the same commutator is-2 inF487. It therefore generates the full pure field kernel. Containing that kernel and surjecting onto the small quotient proves that every proposed embedding is connected.

These degree/connectivity statements do not imply diameter9. A Cayley graph's complete identity-root distances would determine its global diameter by left translations, but no target distances, words or field images were evaluated. The proposed scope is exactly one field487, this fixed CRT controller/vector/phase frame, and all18 exact-order54 embeddings if later authorized. It is not an automatic nextfield or free-vector search.
