# The one-six, one-eight branch on25 points

Let H be a simple five-uniform hypergraph on25 points, with35 edges, covering every pair. Assume exactly one point z has degree6, exactly one point t has degree8, and the other23 points have degree7. Then H has Property B.

This proof uses the previously established mixed single-K5 theorem (`MIXED_ONE_SIX_K5.md`), the complete marked seven-unit gate (`MIXED_ONE_SIX_UNIT7.md`), and the complete eight-unit one-six gate (`MIXED_ONE_SIX_UNIT8.md`). Each gate has its own independent exact replay. The present step supplies the remaining minimum-empty private-pair argument; it does not assert the entire25-point branch with more than one six-degree point.

## Actual choice of the seven-unit set and private pair

Write w(u,v)=λ(u,v)−1. Pair coverage and five-uniformity give weighted rows0 at z,8 at t, and4 at every degree-seven point. In particular z is unit to every other point.

If five seven-degree points form a positive-weight K5 component, the mixed single-K5 theorem applies. Otherwise the support graph on the23 seven-degree points has maximum degree4 and no K5 component; Brooks's theorem supplies six mutually unit seven-degree points. Add z to obtain a seven-unit set I of the stated degree pattern.

Choose I among all such sets to minimize its empty trace multiplicity. In a non-B candidate the complete marked seven-unit gate leaves only core0 (empty8), core16 with z at the intersection of two triples (empty6), or core19 with z inside its unique triple (empty7). The core0 minimum is impossible by the incidence contradiction40≤28 proved in `MIXED_ONE_SIX_UNIT7.md`. Hence I has one of the following inventories, after relabeling z=6:

* Core16: large traces C1={2,3,6}, C2={4,5,6}, singleton multiplicities1 at0,1 and2 at2,…,6, empty multiplicity6; all unused lock pairs occur once.
* Core19: large trace C={4,5,6}, singleton multiplicities1 at0,…,3 and at6,2 at4,5, empty multiplicity7; all unused lock pairs occur once.

There are17 seven-degree points outside I. Every such x has w_I(x)=Σ_{i∈I}w(x,i)≥1; otherwise I∪{x} gives eight unit locks of one six and seven sevens, ruled out by the strict eight-lock gate. Put b=w_I(t), and let h count those external seven-degree points with w_I(x)=1. Summing the six seven-degree weighted rows in I gives

24−b ≥ h+2(17−h),  hence h≥10+b≥10.

Each of these h private points has a unique partner i∈I with λ(x,i)=2, and i≠z. There are only six eligible partners, so two distinct private seven-degree points x,y have the same partner i. If λ(x,y)=1 then (I\{i})∪{x,y} is an eight-unit set with one six and seven sevens, again impossible. Their weighted rows also give1+(λ(x,y)−1)≤4. Thus

2≤λ(x,y)≤4.

This selects the actual nine locked points I∪{x,y}. The unique eight-degree point is unlocked; neither private point is t. No third external point is selected.

## Sharp single-star necessities from the minimum

Let μ_T be the actual I-trace inventory. For a private seven-degree x let p_T be the number of its edges with I-trace T. Then Σ_T p_T=7 and Σ_{T∋j}p_T=2 for j=i and1 for every other lock j. In particular x lies in at most one old triple: in core16 both old triples contain z and λ(x,z)=1.

Write r=p_empty, s=p_{i}, and q_out=Σ_{|T|=2,i∉T}p_T. Replacing i by x preserves the unit set and low mark. Its new empty count is μ_empty−r+μ_i−s. The private incidence equations give

r+s = 1+q_out+Σ_{|T|=3}(2−1_{i∈T})p_T.

Four rooted cases cover every possible partner, using permutations that fix z and preserve the core inventory.

| Core/root | Minimum-empty necessity | Additional sharp necessity |
|---|---|---|
|16, i=0 outside both triples|no old triple, q_out=0|none|
|16, i=2 in C1\{z}|a_other=0, q_out+a_own≤1|if a_own=0,q_out=1, its pair trace is {z,0} or {z,1}|
|19, i=0 outside C|a=0,q_out=0|none|
|19, i=4 in C\{z}|a+q_out≤1|if a=0,q_out=1, its pair trace is {z,j} with j∈{0,1,2,3}|

Here a_own,p_C and a_other are the corresponding0/1 triple incidences. To prove the sharp column, consider the only nontrivial case q_out=1 with no own-triple incidence. The exchange removes the old own triple and creates one new triple from that unique pair trace. In core16 the new empty count is6, so the exchanged marked gate must again be core16 and both surviving triples must contain z. In core19 it is7, so the new unique triple must contain z; a core19 triple avoiding z is already strictly colorable. The unique pair trace must therefore contain z. The displayed available pairs are exactly those not already consumed by an old triple. If q_out=a_own=0, core16 may move to core19 at empty7, and core19 may move to core0 at empty8; these exchanges are allowed, without claiming they preserve the minimum.

## Complete small local domain and strict gate

A private star is a partition of the eight lock incidences (one incidence at each point plus a second at i) into nonempty old trace slots. A slot T is used at most μ_T times. The empty incidence count is7 minus the number of chosen nonempty slots and must lie between0 and μ_empty. This is a complete description of the necessary single-star domain: every actual x gives such a partition. Applying the preceding sharp necessities leaves the following small domains.

| Core/root | Stars before necessities | Retained stars | Root automorphisms | First-star orbits | Nine-lock representatives | Maximum raw bound |
|---|---:|---:|---:|---:|---:|---|
|16, i=0|169|21|8|8|515|3873/4004|
|16, i=2|161|29|4|13|1112|1973/2002|
|19, i=0|231|21|12|8|163|553/572|
|19, i=4|227|43|24|7|279|7863/8008|

For two retained stars p,r put q_T equal to the number of common edges in old slot T. Their full nine-lock inventory is obtained by the four exact cells

μ_T−p_T−r_T+q_T,  p_T−q_T,  r_T−q_T,  q_T,

according as neither, only x, only y, or both external points are present. For each T the complete q range is max(0,p_T+r_T−μ_T)≤q_T≤min(p_T,r_T). Retain Σq_T∈{2,3,4} and traces of size at most5. These are necessary conditions on the actual two stars and their actual shared edges, so the resulting domain is an outer approximation of every selected actual pair. No independence between stars is assumed.

The generator first quotients a star by all permutations fixing z,i and preserving μ; after fixing it, it quotients the joint inventory by its stabilizer. All four groups are explicitly exhausted. They preserve the degree-six mark and the partner; the two new points remain ordered. This leaves2069 representative inputs. Every input has35 total edges, degrees6 at z and7 at the other eight locks, unit codegrees within I, codegree2 from i to x,y, unit codegrees from the other locks to x,y, and λ(x,y)∈{2,3,4}.

The exact raw permutation ABC bound is strictly below1 for every representative. There are16 unlocked vertices and the common integer coefficient denominator is16!. The certificate uses only fixed layouts and raw C: no center quota, marked-point degree surrogate, or subtracted pair correction is required. The largest of all2069 bounds is1973/2002<1. Hence the actual selected pair has a colorable nine-lock input, contradicting the assumption that H is non-B. This proves the stated r=1 theorem.

## Computation and independent scope

`MIXED_ONE_SIX_MINIMUM_STARS.py/json` exhausts the4140 partitions of eight labeled incidences and verifies the analytic necessities by actually reconstructing every exchanged seven-lock inventory. It takes0.10 seconds. `MIXED_ONE_SIX_MINIMUM_PAIRS.py/json` exhausts all shared-slot choices and performs the exact mark/partner-preserving quotient, taking0.30 seconds.

Only eight residual representative inputs were optimized by DP, two per root (2.89 seconds). Their layouts, along with previously available a7 layouts and the x/y interchange, cover the complete2069-input domain in2.70 seconds. Thus the finite proof is the2069 concrete layouts in `MIXED_ONE_SIX_MINIMUM_PAIR_CERTIFICATE.json`, not an assertion that an optimizer eventually succeeds.

`MIXED_ONE_SIX_MINIMUM_PAIR_REPLAY.py/json` independently reconstructs each star by recursion on the first uncovered lock incidence, without the partition generator or its sharp-filter implementation. Instead it rebuilds the exchanged marked inventory and tests exactly the already-proved residual gate plus minimum-empty value. It enumerates every ordered pair without quotienting, reconstructs every nonnegative shared-slot split, and checks that the exact automorphic images of the certificate representatives cover precisely this full labeled domain. It also recomputes every raw rational ABC bound directly from binomial coefficients, importing no probability/DP/quota/coefficient code. The replay passed in46.18 seconds: the four unquotiented domains have3021,3796,1050,4850 inputs respectively (12717 in total), exactly the full certificate images, and all2069 direct rational bounds are strict.

The complete unit-seven and unit-eight catalogues and the raw permutation repair criterion remain explicit previously proved inputs. No whole hypergraph is enumerated. This result closes the degree pattern6,8,7×23; degree patterns with at least two six-degree points are outside this theorem.
