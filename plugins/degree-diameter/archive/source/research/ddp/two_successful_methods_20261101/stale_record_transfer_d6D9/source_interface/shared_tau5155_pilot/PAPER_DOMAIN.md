# Paper-only domain and RIGHT-law check for beta5155

2026-11-01. No field powers, words, coefficient forms, endpoint images, graph or BFS were computed here. Read `NEXT_SHARED_TRANSLATION_SCOPE.md`, the older `ANALYSIS_GAUGE_PROOF.md`, and the fixed1512 `field6959_all_embeddings/REPORT.md`. The numerical pilot is the sole driver in this directory.

**Actual scope.** Work only overF6959 with the saved exactorder49 actionβ5155 and phasesa=(1,36,45). The old42-action result fixed generators(1,0),(36,1),(45,1512). Its34 thin rejections and8 radius9 failures do not exclude other sharednormal ratios. The old1512 case forβ5155 is already closed and must be skipped, not relabeled as an untested member. No secondβ orfield is included.

**Complete normal-parameter reduction.** The RIGHT law is

    (j,n)*(a,c)=(j+a,n*β^a+c).

Using the constant coordinate changeY=n+d gives the parameter rule

    c_new=c+(1−β^a)d.

Becauseβ−1≠0, choose d=cA/(β−1) to setcA0. For a word ending atphaseJ, the endpointform increment telescopes to(1−β^J)d, the same constant for every word in that slot. Do not useY=n+β^j*d as a parameter-changing gauge: that map is lefttranslation by(0,d), an automorphism of the RIGHT Cayley graph withc unchanged.

Equivalently, actual group conjugationh*(a,c)*h^(-1), h=(0,d), givesc_new=c+(β^a−1)d and vertex coordinateY=n+(β^j−1)d. This is also a valid gauge and fixesidentity; choosing the opposite sign ford gives exactly the samecA0 section as the constant-coordinate convention. The two valid formulas must not be mixed with the ineffective pureβ^j translation. ThecA0 section is unique under this one-dimensional gauge. Global normal scaling(j,n)→(j,sn), s≠0, is also a group isomorphism and scales all three normals together.

The two remaining normals(b,c) therefore have representatives(1,τ), τ∈F6959, plus infinity(0,1), pluszero(0,0). These q+2=6961 representatives are complete for this fixedβ/phase family under the two stated isomorphisms. Skip the already-refutedτ1512 and the disconnectedzero:6958 new finiteτ plus infinity gives6959 new representatives. No further generator permutation or phase relabeling is silently quotiented out.

Zero has every generator in the49-element phase subgroup and cannot connect the fullgroup. Infinity is not zero and must not be discarded: gA^(-45)*gC=(0,1) there, so it generates the fullnormal additive group together with the phase generator. This is a paper connectivity argument, not a numerical gate or a diameter assertion.

**Correct endpoint-form recurrence.** Represent the normal endpoint fromidentity as L0+L1*τ for the finite branch, or as a dot product with(b,c) to include infinity. When appending a right generator with phasea and normal coefficientvectord, the update is

    L_new=β^a*L_old+d.

A positivegenerator with normalc has inverse(-a,−β^(-a)c), so the reverse update is L_new=β^(-a)*L_old−β^(-a)d_positive. The same formula applies componentwise. The previous69phase convention used additiveβ^currentphase*c and is not this RIGHT law. No zeroing or independent choice of inverse coefficients is valid.

**Why25 phases suffice if all pass.** Let U_j be the complete normal endpoint set of allwords oflength≤9 fromidentity with totalphasej, using the fixed inverseclosedgenerators. Inverting a word reverses its order and inverts each letter; it preserves length and the nonbacktracking property. Since

    (j,n)^(-1)=(-j,−n*β^(-j)),

we have exact set equality U_(-j)=−β^(-j)*U_j. Multiplication by this nonzero scalar is a bijection. Phases0,1,…,24 represent all sign-pairs inZ49, so full6959-point coverage of those25 endpoint sets is equivalent to fullcoverage of all49 phases. In particular, a singlecriticalphase0 pass is only necessary, while a miss in any testedphase already refutes that parameter. Complete identity-ball coverage would give D≤9 for the actual Cayley model by lefttranslation; it does not by itself identify exactD9 or replace the numerical receipt.

The gauge and scaling preserve phase-slot image cardinalities: normal endpoints change by a phase-dependent common affine bijection. The constant-coordinate map moves the chosenidentity root, but the displayed endpointform telescoping identity directly proves fixed-root image cardinality preservation. The equivalent conjugation convention fixesidentity. No invalid normalization, missinginfinity branch or inverse/phase-sign gap was found under these exact conventions. If the bounded evaluation is incomplete it remainsUNKNOWN; this paper check is not a result for any parameter image.

## Paper transport to the inverse action (no second numerical action)

For the same RIGHT convention, φ(j,n)=(-j,n) is a group isomorphism G_r→G_(r^-1): both sides of φ((j,n)*(a,c)) equal(-j-a,n*r^a+c). It sends a positivegenerator(a,c) to(-a,c). Since the Cayley connection set is inverse-closed, choose this image's target inverse as the new positivegenerator; inG_(r^-1) it is(a,−c*r^(-a)).

Starting from positives(1,0),(36,1),(45,τ), global normal scaling by−r^36 then gives

    (1,0), (36,1), (45,τ*r^(-9)).

Thus the complete finiteτ domain for actionr is isomorphic, by a parameter bijection, to the finiteτ domain for actionr^-1. Infinity(0,1) maps to a nonzero infinityvector and renormalizes to infinity; zero stayszero. No numerical value ofr^-1 or secondaction is computed.

The fullr conclusion must include the inheritedτ1512NO and pure-phasezeroNO as well as the6959 new evaluated representatives. In particular, the oldr parameter1512 maps to1512*r^-9, usually not to the old1512 parameter at the inverseaction. It is the *complete* parameter domain, not a mistaken pointwise identification of those two old controls, that permits transport.

The actualbeta5155 pilot rejected every6959 new representative; no graph or BFS was produced. Phase0's2302 survivors showed that newratios repair a necessary old return-fiber gap, but phases1..11 eliminated them all. The numerical result itself tested oneaction only. This paper transport closes the whole normal-translation family at its distinct inverseaction as well, while the remaining40 primitiveactions' freeτ domains remain outside the new result. The older all42 fixedτ1512 exclusions remain valid unchanged. No double experiment count, new independent method or originality assertion follows; no secondbeta is dispatched.
