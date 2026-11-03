> Actual closure: the two structure/wheel/integer-minor certificates are now present and bound. See `C14_AND_ORDER14_NO_PROOF.md` for the complete cyclic14 and regular-group14 proof, plus the actual-H affine7 corollary. The conditional prediction below remains historical.

# Conditional odd-wheel obstruction; no survivor classification assumed

This is a pure paper attack within the same route-capacity gate. It does not enumerate the64 binary signatures, identify any actual parity survivor, or certify a20-vertex graph or its face list. The premises below must be bound to the finite owner's actual objects before the conclusion is applied.

## Translation statement

Let H be a loopless20-vertex base. Assume that at each vertex v, the complete list of closed nonbacktracking words of length≤6 consists of exactly seven words: the empty word and the two orientations of the three incident pentagonal faces. Assume these are genuine literal face cycles, consistent under cyclic rotation and reversal, rather than merely seven arbitrary return words. Suppose the actual face-incidence certificate contains six distinct faces F,g0,g1,g2,g3,g4 such that F is adjacent to all gi and gi is adjacent to g(i+1 mod5), where adjacency means sharing an edge (sharing the appropriate vertex would already suffice).

In an additive C7 voltage cover, immediate base backtracks lift to exact cancellations. Every route returning to the same base vertex within6 therefore has the voltage of one of the seven listed reduced words. Its reachable return-fiber labels are precisely contained in

{0, ±ω(F1), ±ω(F2), ±ω(F3)}.

Diameter≤6 requires all seven fiber labels to occur, at every vertex. Hence every face voltage is nonzero and the three incident unoriented values [ω]={ω,−ω} are distinct. The set F7* modulo sign has three classes. Since voltage addition is abelian, a face voltage is independent of its chosen starting corner and changes only sign under reversal; thus this gives one well-defined global three-color assignment to the faces. Adjacent faces share an incident vertex and must have different colors.

The central face F uses one color. Each gi must use one of the other two colors, while consecutive gi must have different colors. An odd five-cycle cannot be colored with two colors: alternation around the cycle makes the closing edge monochromatic. Contradiction. Therefore this particular H has no diameter≤6 C7-translation cover, for any voltage assignment. The count is tight, so a zero face voltage or a repeated sign-class is already a direct failure rather than an escape from the coloring argument.

No assertion that there are twelve faces, that H is dodecahedral, or that the six-face wheel exists is inferred solely from the raw count seven. Those are separate finite bindings. No cycle-basis premise is needed for this translation statement; literal face consistency and the odd wheel suffice.

## Conditional use for C14 over the Petersen base

For a fixed binary signature σ, use H with vertices(u,ε) and transitions(u,ε)→(v,ε+σ_uv). Under C14≃C2×C7, every Petersen C14-translation cover is a C7-translation cover of this H, with edge mod7 voltages inherited from the Petersen edges. Excluding all C7 assignments on H is stronger than excluding only that inherited assignment family, so the implication is valid.

To close the whole Petersen C14 family by this argument, every surviving binary signature must either be excluded by the finite distinct-form gate or be bound to an H satisfying the premises above. A wheel for one H does not exclude another signature. Raw word capacities and distinct-mod7-form capacities remain different statements. This note does not claim two survivors, only dodecahedral survivors, or an actual140-vertex graph.

## Optional one-dimensional affine7 corollary

Assume in addition that the actual oriented face cycles generate H's integral cycle lattice. A cellular sphere face certificate suffices, or one may supply a primitive/unimodular cotree-cycle certificate; mere rational spanning is not the same premise.

Allow arbitrary invertible one-dimensional affine edge maps x↦a x+b over F7, with literal inverse maps on reversed edges. The same reduction to seven return words holds. If any face holonomy g fixes some x, that fiber point receives the same output from the empty word and g; at most six return labels then remain, violating diameter≤6. Thus every face holonomy has no fixed point. For an affine map a≠1, x=b/(1−a) is a fixed point. Hence every face holonomy must have a=1 and b≠0.

The linear parts lie in the abelian group F7*. Having trivial product around each integral face generator makes the linear holonomy trivial on every cycle. A vertexwise nonzero scaling can then gauge every edge linear part to1: first normalize a spanning tree, then the trivial fundamental-cycle products force the cotree parts to1. The entire affine cover becomes a translation cover by a fiberwise bijection, so the previous odd-wheel obstruction applies.

Without the integral cycle-generation binding, face translations alone do not justify one global face-voltage coloring: changing the starting corner may conjugate and rescale a translation. That is the precise gap the extra premise removes. The corollary does not extend to higher-dimensional affine covers, general permutations of seven symbols, or arbitrary affine/permutation14-covers. Fixed-point-free higher-dimensional affine maps need not have identity linear part, and general fixed-point-free permutations need not be translations.

## Current evidence boundary

This conditional proof is supported; no logical counterexample was found under its explicit premises. It is not yet an actual survivor classification or whole-family finite conclusion. Await the finite owner's actual signature list,20-base/face words, and wheel. Any optional affine conclusion additionally awaits the integer-cycle-generation certificate. No graph, word/signature enumeration, field computation, BFS, solver, Lean, external review or numerical batch was run by this paper task.


## Actual finite gate handoff (read-only)

The finite owner's completed `RESULT.json` and `ALL64_SIGNATURE_RESULTS.json` now report raw and distinct-mod7-form survivors exactly21 and62 in the fixed tree coordinates. Their bits are[1,0,1,0,1,0] and[0,1,1,1,1,1]. Both report a tight seven-word slot(0,0,0). This paragraph only reads the saved result; it does not regenerate words or classify either20-layer base. The actual20-base/faces/odd-wheel certificates have not yet been generated in this gate, so the conditional obstruction is not yet applied to all C14 covers. In particular, root0 tightness alone does not establish the required face description at every vertex.
