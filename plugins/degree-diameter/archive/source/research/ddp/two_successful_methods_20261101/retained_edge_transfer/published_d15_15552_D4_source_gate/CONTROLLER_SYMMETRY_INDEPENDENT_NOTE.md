# Independent controller-symmetry transfer for the actual15552 source

This paper-only note reads the newly saved CONTROLLER_SYMMETRY_PRED/RESULT and the actual F3Graph15552Definitions interface. It continues the existing clone-owner analysis without recomputing the centralizer, graph distances, field/rank facts, a solver result or any Lean compilation. It writes no source or root-owned plan/state/Wiki file.

## Actual finite result being inherited

The root result reports a complete forced-propagation test of192 possible images of controller0:24 accepted port-preserving permutations,168 rejected images, with each accepted map's960 commutation equations checked by that experiment. The resulting action has8 orbits, each of size24, with representatives

    reps = [0,1,2,3,9,10,16,35].

These are numerical structural results from the actual new root experiment, not independent checks rerun here. The source is not transitive under this action: type0 fixes controller0 but not controller1, and more generally the8 orbits remain distinct. Nothing below infers full transitivity or permits one row0 certificate to replace all eight representative rows.

The actual definitions are essential: B_p, v_p and c_p depend only on the GLOBAL type p∈Fin5, while controller(a,p) is the192×5 table. A local arc-position label whose associated matrix changes with a would not suffice. Current global type indexing matches the five matrix/direction/constant tables in F3Graph15552Definitions and the recovered literal source. This is not the older edge-local120-matrix F4 source.

## Why a controller centralizer really lifts

Let h be a permutation of the192 controllers satisfying

    h(controller(a,p)) = controller(h(a),p)             (C)

for every a,p. Write a source vertex as liftAt(a,encodeVec(x)), x∈F3^4, and define

    H(liftAt(a,encodeVec(x))) = liftAt(h(a),encodeVec(x)).

Its inverse applies h^(-1) to the controller and leaves x unchanged. The literal decomposition liftAt_parts and encode/decode identities show these are inverse functions on Fin15552. No translation or source-fiber orbit assumption is involved.

Because stepVec(p,t,x)=B_p x+c_p+t v_p has no a-dependence, (C) gives

    H(forward(u,p,t)) = forward(H(u),p,t).              (F)

This uses no invertibility of the singular B_p maps, no matrix ranks, no degree regularity and no field automorphism. Both disjuncts of the actual definition

    Adj(u,v) iff u≠v and
       ((∃p,t, forward(u,p,t)=v) or (∃p,t, forward(v,p,t)=u))

are preserved by (F). The inverse permutation also satisfies (C): applying h to controller(h^(-1)(a),p) and using (C) yields controller(a,p); injectivity of h then gives the inverse commutation equation. Applying the same argument to H^(-1) proves the reverse implication of Adj preservation. Therefore H is an actual SIMPLE-source graph automorphism, rather than merely a forward-relation homomorphism.

Virtualself deletion causes no gap. H is injective, so H(u)=H(v) iff u=v. A completed output is deleted exactly when its entire old global label equals the input; after H the same equality holds, and unequal labels stay unequal. A real same-controller/different-coordinate edge stays real; a virtual stay stays deleted. The degree14/15 distinction is transported, not replaced by an assumption of15regularity. Constants could even be nonzero provided they still depend only on p; the current five constants are0.

## Correct complete-row transfer

Use the FULL property

    RowBound(a) := for every x∈Fin81 and every v∈Fin15552,
      there is a genuine source Walk from liftAt(a,x) to v of length≤4.

Suppose RowBound(r) is proved and h(r)=a. Given an arbitrary x and target v, invoke RowBound(r) with target H^(-1)(v). Map that actual Walk through H. Its start is H(liftAt(r,x))=liftAt(a,x), its target is v, and mapping preserves Walk length. This proves RowBound(a). The target quantifier must cover every target controller AND every fiber coordinate before transfer; the targets are not restricted to orbit representatives or to h-images of a preselected subset.

The same mechanism can transfer a single certified pair(a,b) to pairs(h(a),h(b)), but that weaker pair transport is NOT a full-row proof. The existing two successful representative pilot pairs(0,0) and(0,33) consequently do not prove row0, nor its orbit. Even a completed row0 only supplies the24 controllers in its own orbit. One still needs complete RowBound for each of the eight actual representatives0,1,2,3,9,10,16,35 (or another proven representative in each orbit).

Those rows must themselves use genuine completed-route-to-simple-Walk theorems and all-coordinate covers. A zero-fiber sample, rank-only sufficient-word test or stored numeric BFS summary cannot silently replace those theorem premises. The source already has independent mathematical D4 acceptance via finalgraph retraction; the issue here is compressing an unconditional kernel proof, not revalidating that graph by another route.

## A small positive certificate instead of24×960 checks

The desired final Lean proof does not need a theorem identifying the entire automorphism group or reenacting the192-image centralizer search. It needs enough actual generators to reach every controller from the chosen representative in its orbit.

1. Root selects2 or3 literal generator permutations from the already found24, together with inverse data or an equivalent concrete bijectivity proof. For EACH generator prove its960 equations(C). Do not assume the chosen count works before actual generator/coverage data exists.
2. Prove once, generically, that identity, composition and inverse of port-preserving controller equivalences preserve(C). Composition follows from h(k(C(a,p)))=h(C(k(a),p))=C(h(k(a)),p); the inverse argument was given above.
3. Evaluate a finite list of generator symbols as a composed controller equivalence. Prove its commutation and lifted graph-isomorphism laws by induction on the word, using those generic lemmas. Either freeze positive words, or include inverse symbols and use the generic inverse theorem; record the convention.
4. Store one repIndex(a):Fin8 and one generator word coverWord(a) for each of the192 target controllers, with the192 POSITIVE equations

       eval(coverWord(a))(reps[repIndex(a)]) = a.

   These equations are the coverage certificate. Avoid checking a full24×960 commuting table again,192 independent source route rows, or all pairwise generator products. Each word denotes a bijection, so its inverse is available for pulling back arbitrary targets in the row-transfer lemma.
5. Combine the eight complete representative-row theorems with the192 coverage equations and the generic Walk map lemma to obtain the entire source D≤4 theorem.

A useful evaluation convention is eval([])=id and eval(g::w)=eval(w)∘generator(g), so applying a word follows its written order from left to right. A right-fold convention is equally valid if the actual coverage words use it; mismatching the convention is a realistic finite-input error. Endpoint coverage alone is not a substitute for generator commutation or bijectivity.

For r actual generators the only new commutation obligations are r×960 (1920 for two or2880 for three), plus small permutation/inverse identities and192 endpoint equations; a generic theorem supplies all compositions. The root may already have numerical checks for all24 maps, but those old checked entries do not become kernel assumptions. Proving the generator identities and coverage equations closes the necessary formal bridge without trusting an external receipt. Full centralizer order24 need not be proved again: even a smaller generated subgroup is enough if its actual positive coverage equations hold.

Actual follow-up received and read: `CONTROLLER_SYMMETRY_GENERATORS_PRED.md` and `CONTROLLER_SYMMETRY_GENERATORS_RESULT.json` now contain the concrete compression. Root reused the already found24 maps and their small composition table; no single map generated all24, while the first successful pair has group indices[1,4], images of0 equal to[5,17]. Their positive words generate the24 maps with maximum word length5. The saved192(rep,word) entries cover every actual controller; root reports all192 coverage bindings checked,0.017433091 CPU seconds within2. This independent note inherits that actual finite result without recomputing it. Thus the concrete intended formal certificate is now TWO generators with1920 commutation equations plus192 coverage equations and generic composition. It is no longer merely a proposed2-or3-generator compression. The external JSON is data for future concrete kernel equations, not a user-certificate axiom or evidence that source/clone FinalClaim is already proved.

## Scope limitations and owner interaction

The lift is a source15552 automorphism. The selected31 clone-center layers I need not be invariant under h. Therefore H is not automatically an automorphism of the16389 graph, cannot transfer its clone labels or justify dropping selected-center load cases, and does not imply that fullN copies have equal distance histograms. The already written CLONE_PIN_OWNER_NOTE gives an independent explicit owner formula for the fixed I/W roles; the symmetry transfer does not alter that formula or the virtualself deletion convention.

A full source theorem proved from eight rows can subsequently feed the generic immutable-full-N source-interior Walk theorem, together with the separate degree/load/label proof, to close the particular clone target. That is a dependency structure, not an assertion that the current two-pair/row pilot or this paper note has already closed source or clone FinalClaim. No graph, parameter, concrete Lean count, external-review approval or global-priority status is incremented here.

Conclusion: the proposed source automorphism and COMPLETE-row orbit transfer are mathematically valid for the actual global-type definitions. The remaining substantive kernel work is eight full representative-row covers plus the now concrete two-generator/192-coverage certificate, not merely the two successful pair pilots. Port-changing or coordinate-changing automorphisms, larger symmetry groups and reducing the eight representatives further are outside this note and are not ruled out by the24-map centralizer result.

Preparation CPU: 0.009357227000000001 seconds for this note-write process; initial read-only small-result inspection measured0.012241820 CPU seconds. No numerical symmetry or graph experiment was rerun.
