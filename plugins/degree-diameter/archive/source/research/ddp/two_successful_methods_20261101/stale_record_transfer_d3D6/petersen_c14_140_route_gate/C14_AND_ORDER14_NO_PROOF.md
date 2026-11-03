# Complete Petersen cyclic14 and regular-group14 cover obstruction

This paper connects the actual finite word-capacity gate to the two actual small structure certificates. It does not generate a140-vertex candidate, search C7 assignments, or claim that arbitrary cubic diameter6 graphs are impossible.

## Actual finite inputs and independent reading boundary

The literal Petersen graph, chosen nine-edge spanning tree and six oriented cotree edges are fixed in `INPUT_AND_TREE_GAUGE.json`. `ALL_NB_WORDS_AND_INTEGER_FORMS.json` stores the1900 reduced words of length≤6 generated once, including the empty words. The raw ordered-slot counts are25 for equal base vertices,21 for adjacent vertices and17 for nonadjacent vertices.

After the complete64 binary tree-gauge signatures are tested, the **raw word-capacity** survivors are exactly21 and62. The distinct-mod7-form gate gives the same two survivors, but that stronger abelian form gate is not needed for the proof below or for its nonabelian group corollary. The canonical all-edge-odd signature is43; its actual global minimum is an adjacent slot of size5, while the separately predicted nonadjacent0→2 odd slot has size6. That correction does not affect the two surviving signatures.

The actual small objects are saved under `signature21/` and `signature62/`. Each has20vertices and30edges with vertex label2*u+sheet. `FACES_AND_RETURNS.json` binds the complete seven closed reduced words at every vertex to the empty word and the two orientations of three simple pentagons. Globally there are12 faces; each vertex lies in3 faces and each edge in2. Both `ODD_WHEEL.json` files give central face0 and cyclic rim faces[1,6,8,10,2], with explicit shared old edges for every central/rim and consecutive-rim adjacency. `FACE_CYCLE_MINOR.json` supplies19 spanning-tree edges,11 oriented cotree edges and the twelve integer face-cycle rows; the first eleven have determinant−1.

The paper reviewer read `structure_once.py`, which filters the already saved return words, lifts their literal edges using the specified bits, identifies oriented/reversed pentagons, binds the explicit wheel, and computes the exact integer minor by fraction-free elimination. No old word or signature generator is rerun. `PAPER_STRUCTURE_BINDING_REVIEW.json` separately binds the saved face edges, all280 saved return records, both literal wheels and all24 oriented face-cycle rows. It does not re-enumerate words/faces or recompute the determinant. The new equality/incidence binding cost is0.009237804CPU seconds. Added to the finite owner's3.679050812, the actual recorded case total is3.688288616/5CPU seconds before any root accounting choice; no graph/BFS/C7 assignment is included.

## From all64 signatures to the two small bases

Consider any translation C14-voltage cover of this fixed Petersen graph, with literal opposite voltages on reverse edges. Vertexwise translations gauge the nine spanning-tree voltages to zero. The six remaining voltages have arbitrary components in C14≃C2×C7, so their binary components are one of the64 complete tree-gauge signatures.

For a fixed start vertex and target base vertex, each reduced word produces one lifted target. A requested binary target sheet contains seven possible target fiber labels. It follows that each ordered binary slot must have at least seven reduced words. Every immediate base backtrack lifts to an exact cancellation, so longer unreduced walks of length≤6 add no outputs beyond the saved reduced list. This raw bound rules out62 signatures. It leaves precisely21 and62.

For either survivor, quotient by the C7 fiber gives exactly its actual20-vertex graph H. Any C14 translation cover is in particular a C7-translation cover of that H; its edge voltages may satisfy additional constraints inherited from Petersen, but excluding all C7 voltages on H is stronger.

## The actual odd-wheel contradiction

At any H-vertex, all closed reduced words of length≤6 are the empty word and the three incident face cycles in both orientations. For a C7-translation cover, the reachable return-fiber differences are therefore contained in

{0, ±ω(F1), ±ω(F2), ±ω(F3)}.

Diameter≤6 requires all seven C7 elements at every start fiber point. Each face voltage is nonzero, and the three incident face values represent different classes in F7*/{±1}. This quotient has exactly three classes. Since the voltage group is abelian, a face's value is unchanged by choosing a different starting corner and changes only sign under reversal. Thus one obtains a well-defined global three-coloring of faces, with incident faces at a vertex having all three colors. In particular faces sharing an edge have different colors.

In either actual certificate, face0 is adjacent to all five rim faces1,6,8,10,2, and consecutive rim faces share an edge. The rim must use only the two colors not used by face0. Alternating those two colors around its odd five-cycle is impossible. This contradiction excludes every C7-translation cover of either H with diameter≤6.

Together with the complete raw64-signature gate, **no translation C14-voltage cover of this fixed Petersen graph has diameter≤6**. This is complete within the stated voltage family. It uses no C7 assignment enumeration and no assertion of dodecahedral uniqueness or an isomorphism classification beyond the explicit face certificate.

## Corollary: every regular order14 group-voltage cover

Let G be any group of order14, with a regular G-voltage cover of the same Petersen base. Its Sylow7 subgroup K is unique, since its number divides2 and is1 modulo7. Hence K is normal and cyclic of order7, and G/K≃C2.

The quotient binary voltages obey the same tree gauge and raw64-signature necessary bound: a target quotient coset has seven elements, and one reduced base word yields only one target group element. This step uses raw word counts only, not the mod7 linear-form alias test. Thus the quotient20-base must again be one of the actual21/62 survivors.

The140-vertex cover maps to this H as a regular K-cover. To see explicitly why it is translation-only over H, write a group label over an H-vertex h uniquely as k*t_h, where k∈K and t_h is a chosen representative of its quotient coset. An original right edge voltage α from h to h' sends

k*t_h ↦ k*t_h*α = k*(t_h*α*t_h'^(-1))*t_h'.

The parenthesized element lies in K. Hence, after identifying the cyclic K with C7, each H-edge acts as a translation on its seven-point fiber. The reverse edge has the literal inverse translation. The actual odd-wheel obstruction therefore applies.

Consequently **no regular group-voltage cover by any group of order14 over this fixed Petersen base has diameter≤6**. This includes the cyclic C14 and the dihedral group of order14; the latter is stated by its order to avoid notation conventions. It does not exclude arbitrary S14-permutation covers or all140-vertex cubic graphs. The normal subgroup argument provides a structural corollary, not another numerical domain search.

## Additional actual-H corollary: scalar-affine F7

On either actual H20, allow arbitrary invertible one-dimensional affine edge bijections over F7, with literal inverse maps in the reverse direction. The same complete seven-return-word list holds. If a face holonomy fixes any x, that start fiber point receives the same output from that face word and the empty word, leaving at most six distinct return labels. Diameter≤6 therefore requires every face holonomy to be fixed-point-free.

For x↦a*x+b over F7, a≠1 has the fixed point b/(1-a). Thus every face holonomy has a=1 and b≠0. Its linear part is trivial.

The actual11×11 face-cycle minor has determinant−1. Cotree coordinates identify the graph's integral cycle lattice with Z^11; these eleven face rows are therefore an integer basis. Linear holonomy takes values in the abelian group F7*. Triviality on those face generators makes it trivial on every cycle. Normalize the tree linear parts by vertexwise nonzero scalings; the fundamental-cycle condition then makes every cotree linear part1 as well. The normalized cover is a translation C7 cover of H, already excluded by its odd wheel.

Thus no scalar-affine F7 cover of either of these two actual H20 bases can have diameter≤6. This uses the actual unimodular integer certificate, not just a rational rank claim. It does not classify or exclude all affine/permutation14 covers of Petersen, higher-dimensional affine covers, semilinear maps, or arbitrary seven-permutation covers of H.

## Stop boundary

The cyclic14 and regular-group14 families are closed for this fixed base. The separate scalar-affine F16/Petersen family is closed by `PAPER_AFFINE16_NO_PROOF.md` and its different17-word collision/rank argument. No construction, new parameter, portfolio graph, Lean instance, priority claim or new independent method is counted here. All old failed predictions and intermediate capacity survivors remain as historical evidence. Changing the base, using general permutation covers, or changing the route generation rule is outside these proofs and is not automatically authorized by this closure.
