# Eight unit locks with two six-degree points

Let H be a simple five-uniform hypergraph on25 points, with35 edges and every pair covered. If H contains eight pairwise unit points, exactly two of degree6 and six of degree7, then H has Property B. There is no additional degree assumption on the seventeen unlocked points.

## Complete marked trace domain

Write μ_T for the actual multiplicity of each lock trace. A trace of size at least2 occurs once, and the traces partition the28 lock pairs into cliques. The previously complete unit-eight catalogue has65 uncolored families of size-at-least-three traces. Add every unused pair as a size-two trace to obtain B. Put h_i=7−|{T∈B:i∈T}|. For the unordered pair L of low labels the actual singleton and empty multiplicities are

μ_i=h_i−1_{i∈L},   μ_empty=37−|B|−Σ_i h_i.

They follow from the eight degree equations and the total35 edges. All65 families and all28 low pairs were reconsidered before discarding negative multiplicities. The complete feasible domain has64 uncolored families,1566 marked inputs and531 orbits under permutations preserving the unordered pair L. The all-pair family0 is infeasible because it would require a negative low singleton.

The shift by two empty edges is necessary. Previously negative all-seven empty multiplicities become feasible:

| Old empty | Source identifiers | New empty |
|---|---|---|
|−2|11,12,14,27,58|0|
|−1|1,23,30,36,51|1|

Each of these ten families has all28 feasible low markings. No restriction to the old55 all-seven feasible families, or59 one-low families, is used.

## Strict raw gate

Every1566 marked input has a concrete fixed-position raw ABC certificate. For a layout of the eight locks in25 positions, uniformly permute the other17 vertices. The bound is the usual sum over positions of min(A_k,B_k,C_k), with C_k the raw ordered opposite-side edge-pair upper bound. All bounds are strictly below1, with maximum

3093/3094 < 1.

The standard strict permutation repair criterion therefore yields a proper two-coloring for every actual H under the stated lock hypothesis. No center quota or pair deduction is used in the final certificate.

The bounded screen used18 consecutive layouts and nine previously available one-low layouts, choosing a layout per marked orbit and transporting it only through low-set-preserving permutations. It covered1436 labels. The remaining130 labels formed35 orbits, each covered by one eight-lock subset-DP layout. Search took1.55 seconds for the complete screen and6.17 seconds for these35 residual orbits. No extra lock or external-point trace classification was introduced.

## Actual r=2 consequence without a seven-degree K5 component

Suppose H has exactly two six-degree points and all other degrees at least7. Since the total degree is175, its degree spectrum is either6²,9,7²² or6²,8²,7²¹. For each six-degree point z, pair coverage and five-uniformity give Σ_{v≠z}(λ(z,v)−1)=4·6−24=0. Thus both low points are unit to all points.

On the22 or21 seven-degree points consider the positive-weight support graph for w(u,v)=λ(u,v)−1. Each seven-degree weighted row is4, hence the ordinary graph has maximum degree4. If it contained a K5, all internal weights would be1 and would exhaust all five rows, giving a seven-degree K5 component with zero exterior weight. In the absence of such a component, Brooks's theorem gives a four-coloring of the seven-degree graph. A color class has at least ceil(21/4)=6 points. Adding the two globally unit six-degree points gives the required actual eight-unit lock set. The strict gate proves Property B.

This closes both r=2 spectra **when there is no seven-degree K5 component**. The branch with such a component still requires a mixed single-G argument with three or four special external points; it is not covered by the present theorem or the earlier r=1 single-G proof.

## Reproduction and independent verification

`MIXED_TWO_SIX_UNIT8_SCREEN.py/json` preserves all65 families,1566 marked inputs,531 exact colored orbits, the newly feasible families and the bounded screen. `MIXED_TWO_SIX_UNIT8_PILOT.py/json` contains35 residual-orbit layouts and their exact bounds. `MIXED_TWO_SIX_UNIT8_CERTIFICATE.py/json` gives one concrete raw layout for every marked input.

`MIXED_TWO_SIX_UNIT8_REPLAY.py/json` independently restores the domain from all65 source families, verifies the35-edge total, both low degrees, the six high degrees and all28 unit codegrees, and recomputes every rational raw ABC bound with binomial coefficients. It imports no domain generator, canonical transporter, DP, quota or probability-coefficient implementation. The independent replay passed in27.13 seconds for all1566 marked inputs, with exactly the domain and maximum stated above. The imported complete catalogue remains `context/propertyb34/round01/high-math/UNIT_CATALOGUE_8.json`, with its prior completeness proof.
