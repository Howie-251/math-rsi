# One degree-six point: seven guaranteed unit locks and a complete eight-lock gate

Let H be a simple five-uniform hypergraph on25 points, with35 edges, every pair covered, one point z of degree6, one point t of degree8, and the remaining23 points of degree7. Put w(x,y)=λ(x,y)−1. The weighted rows are0 at z,8 at t, and4 at each seven-degree point; in particular z is unit to every other point.

Assume no five seven-degree points form a positive-weight K5 component. On the23 seven-degree points the ordinary support graph has maximum degree4. A K5 in this induced graph would already exhaust all five weighted rows: its ten weights would be1 and there could be no positive exterior weight, including a weight toward t. Thus the induced graph has no K5 component. Brooks's theorem colors it with four colors (the odd-cycle exception also uses at most four). One color contains at least ceil(23/4)=6 points. Adjoining z guarantees **seven pairwise unit locks, one of degree6 and six of degree7**.

The preceding graph information alone cannot guarantee eight. The replay file constructs an abstract weighted graph with rows8,4×23,0, no seven-point K5 component, and independence number exactly7. Its24 nonisolated vertices are covered by six K4 blocks. This is a sharpness example for the graph argument, without a claimed hypergraph realization.

## Conditional eight-lock theorem

If H has eight pairwise unit points, exactly one of degree6 and seven of degree7, then H has Property B.

For completeness, write the actual lock traces as multiplicities n_T. Every trace of size at least2 has multiplicity1, and those traces partition all28 lock pairs into cliques. After the traces of size at least3 are specified, every unused pair is a size-two trace. The previously complete unit-eight catalogue contains65 uncolored large-trace families; its completeness does not depend on M or degrees. For a fixed family let B be the full size-at-least-two traces and h_i=7−|{T∈B:i∈T}|. If ℓ is the degree-six mark, then

n_{i}=h_i−1_{i=ℓ},   n_empty=36−|B|−Σ_i h_i.

These equalities follow from the eight actual degree equations and Σ_T n_T=35. All65 families and all eight marks were reconsidered; only nonnegative multiplicities were retained. The complete domain is59 uncolored families and436 marked inputs, or197 orbits under permutations preserving the low-degree mark. Five families with old all-seven empty multiplicity−1 become feasible: source identifiers1,23,30,36,51. Thus the old55-family feasible domain is insufficient here.

Each of the436 inputs has a fixed-position raw ABC certificate. The raw bound is the usual sum over25 positions of min(A_k,B_k,C_k), with all17 unlocked vertices uniformly permuted; C_k is the ordered opposite-side bad-edge-pair upper bound. Only actual trace multiplicities enter. All bounds are strictly below1, and their maximum is

269355/272272 < 1.

This is the standard strict permutation repair criterion, so every actual input has Property B. No center quota or improved pair deduction is needed for these final certificates.

The bounded search first used18 consecutive layouts and transported them by exact mark-preserving isomorphisms; this covered414 marked inputs. The22 residual labels comprised nine colored orbits. One eight-lock subset DP witness per residual orbit covered all remaining labels. Transport only permutes the lock points and their positions, preserving the degree-six point. The final certificate lists a concrete layout for every labeled input, so its independent replay does not trust the transporter or DP.

## Reproduction and exact scope

`MIXED_ONE_SIX_UNIT8_CERTIFICATE.json` gives436 inputs and strict layouts. `MIXED_ONE_SIX_UNIT8_REPLAY.py` independently reconstructs the full domain from all65 catalogue families, checks35 edges, the marked6/7 degrees and unit pair equations, and recomputes every rational ABC sum using only binomial coefficients. It imports no DP, original domain generator, quota code or position coefficient implementation. Its replay passed in6.72 seconds. The original screen and nine-orbit witness search took3.56 and1.60 seconds respectively.

The imported classification is `context/propertyb34/round01/high-math/UNIT_CATALOGUE_8.json`, with `complete=true`; this local result retains that complete-catalogue dependency. The files ending `_SCREEN`, `_PILOT`, `_CERTIFICATE`, and `_REPLAY` preserve the domain, search witnesses, final certificates, and independent check separately.

The actual Brooks caller guarantees seven locks. The eight-lock theorem is a complete conditional gate; it does not by itself prove that an eight-lock set exists or close the r=1 branch. Together they permit restricting a remaining non-B candidate without a seven-degree K5 component to maximum6/7 unit-set size exactly7 (with z included).
