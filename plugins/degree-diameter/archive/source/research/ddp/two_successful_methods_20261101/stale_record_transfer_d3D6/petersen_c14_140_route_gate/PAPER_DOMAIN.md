# Paper domain review: Petersen translation covers of length at most six

This paper task performs no word count,64-signature enumeration, cover generation, source BFS, field check, solver, Lean or review. The separate finite gate owns all actual counts and survivors. The proposed raw counts25(diagonal),21(adjacent),17(nonadjacent) are derived predictions until bound by its actual result.

## Complete translation parameter domain

The literal base is the connected Petersen graph: outer0..4 form a5-cycle, inner5+i join by step2, with the five spokes i—(5+i). It has10vertices and15edges. The chosen spanning tree has outer path01,12,23,34 and all five spokes, hence9edges. The six cotree edges, each oriented smaller-to-larger, are(0,4),(5,7),(5,8),(6,8),(6,9),(7,9).

For additive voltage group A, an edge u→v with voltage α_uv lifts(u,x) to(v,x+α_uv), and its reverse has voltage−α_uv. Relabel the fiber at u by y=x+g(u). The new voltage is α'_uv=α_uv+g(v)−g(u). Choosing g recursively along the rooted spanning tree makes every tree voltage zero. The six remaining voltages are arbitrary. This gauge is a bijection of each fiber and preserves all distances and endpoint coverage. Consequently it covers all translation-only A-covers of this fixed base, including disconnected ones; it does not parametrize arbitrary edge permutations or affine maps with nonidentity linear part.

For A=C14, the Chinese remainder map x↦(x mod2,x mod7) is an additive group isomorphism C14≃C2×C7. Each of the six gauged variables therefore has one binary component and one independent mod7 component. The64 binary signatures exhaust this gauge domain. No sign,connectedness or scalar normalization should be silently added.

The canonical bipartite double-cover class is the all-edge-odd cochain before gauge. In the chosen tree gauge, its cotree signature is1+depth(u)+depth(v) mod2, equivalently the parity of that fundamental cycle. It need not be the six-entry all-ones signature. Since the Petersen base is nonbipartite, no conclusion about that one canonical parity class automatically applies to the other signatures.

## Why nonbacktracking words are the right finite objects

A base immediate backtrack traverses an edge and its prescribed inverse, so its lift returns to the identical global vertex. It can be erased without changing voltage or endpoints. Hence any lifted route of length≤6 has a nonbacktracking base word of length≤6 with the same endpoints and voltage; include the empty word for return-to-same-controller slots. This is an exact reduction for the translation model, not a use of the original base diameter as a cover-diameter certificate.

In tree gauge each word voltage is an integer linear form in the six variables. For a fixed mod2 signature, compute the word's parity from the integer coefficients reduced modulo2. Independently reduce its coefficients modulo7 to obtain the mod7 form. Mod7 reduction does not itself determine parity because7 is odd. Different base words can have identical forms, and different forms can evaluate to the same value at a particular choice of the six mod7 variables.

For every ordered base pair and each prescribed parity ε, the target fiber contains exactly seven points. At least seven distinct mod7 forms in that slot is therefore necessary. Raw word count≥7 is weaker. Even distinct-form count≥7 for every slot does not exhibit one simultaneous assignment whose evaluated images cover all seven values in every slot; any surviving signature remains only a necessary-gate survivor.

For the canonical all-edge-odd class, word parity is path-length parity plus endpoint gauge shifts. A measured nonadjacent parity slot with only six words, or six distinct forms, suffices to close that single class. It cannot be used to guess that every other signature fails. This paper does not assert the predicted six without the finite result.

## Inverse words and the separate160-vertex obstruction

For any nonempty closed nonbacktracking word w, reversal with every dart inverted gives another closed nonbacktracking word w^-1 based at the same vertex. They cannot coincide as literal words: an odd-length fixed word would have a self-inverse central dart, impossible in a loopless base; an even-length fixed word would have an immediate reversal at its middle. Thus the nonempty closed words split into inverse pairs.

In a translation-only cover with voltage group F2^4, w and w^-1 have equal voltage, since−v=v. If the actual return count is25 including the empty word, the24 nonempty words give at most12images and the empty word contributes at most one more. Thus at most13 of the16 return-fiber points can be reached within six steps. Once the gate actually binds that count, this strictly excludes a160-vertex diameter≤6 F2^4-translation cover of this fixed Petersen base. It does not exclude C16 translations, arbitrary16-permutation covers, or general affine16-covers, where inverse closed maps can send a fixed fiber point to different points.

For C14, inverse word voltages are v and−v, usually distinct. The same13-image argument is invalid. At a return slot the images are closed under negation. To cover all14 values one must cover both self-inverse elements0 and7. The empty word supplies0; a closed word of odd binary parity must evaluate to0 modulo7 to supply7. This is an evaluation constraint, not a requirement that its formal coefficient vector be zero. All other values can occur in opposite pairs. It is useful only after actual word/slot binding and does not identify a unique dodecahedral or other branch.

## Scope boundary

No flaw was found in the six-variable tree gauge or the64-signature CRT domain. The finite owner must report actual raw counts and stronger distinct-form slot capacities separately, along with every survivor. There is no paper basis here to label all survivors dodecahedral, to infer short-face identities without the corresponding literal branch, or to claim a140-vertex graph from a capacity gate. This task stops at that interface and the conditional exponent-two obstruction.
