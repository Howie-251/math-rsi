# Exactly five degree-eight vertices: remaining actual structure

The branch r8 >= 6 is closed by `../six_conditional/DELTA8_GE6_PROOF.md`. This report concerns the exact remaining case r8=5. Since total degree is 175, the other fifteen vertices all have degree nine. The five degree-eight vertices are the entire degree-eight set; selecting a sixth degree-eight vertex is unavailable.

Their exact five-point inventory is one of the 49 residual orbits in `../five_join/FIVE_REMAINDERS.json`, or an earlier strict certificate or the proved double-pair core lemma already colors H. These 49 inventories are necessary local data, not known realizable counterexamples.

For such an inventory n_T, put C=sum_T binom(|T|,2)n_T and let n0=n_empty. For each external degree-nine vertex y define p_T(y) to count old-slot-T edges containing y, r(y)=sum_{T nonempty} p_T(y), and S(y)=sum_T |T|p_T(y)=sum_{i=1}^5 lambda(i,y). The same actual y satisfies the degree equation p_empty(y)=9-r(y). Exact double counting across all fifteen external vertices gives

    sum_y r(y) = 135 - 5 n0,
    sum_y S(y) = 160 - 2 C.

Consequently, for every nonnegative alpha one may choose one actual y with

    S(y)+alpha r(y) <= floor((160-2C+alpha(135-5n0))/15).

Separate minimizers of S and r cannot be combined. In the present 49-core relation C lies between 14 and 21. Taking alpha=0 guarantees S(y)<=8, or <=7 when C=21. All actual promotions satisfy 0<=p_T<=n_T, p_full-five=0, and p_T<=1 for |T|=4. These are respectively old-slot capacity, five-uniformity, and simplicity of each new five-element trace.

The first generator `domain.py` used these necessary conditions and selected S<=8, quotienting by a simultaneous permutation of the five low labels while fixing y. It stopped after 11 of 49 source cores in 27.13 seconds: 25,691 canonical-prefix labelled promotions and 8,163 orbit representatives. `DOMAIN.json` explicitly records `complete:false`. These are only the processed source cores, not the full labelled domain. No six-lock DP was run on this broad partial domain. Its width justifies stopping this direct route.

A complete new mixed three-lock gate is now available. The old independently verified double certificates rule out every 8/9 pair of codegree at least five (`../../20-new-high/DIAGNOSIS.json` and its replay). Thus for every external y, 1<=lambda(i,y)<=4. For two degree-eight vertices with mutual codegree c in {1,2,3}, let a,b in {1,2,3,4} be their codegrees with y, and let t be their inclusive triple count. The exact inventory is

    n111=t; n110=c-t; n101=a-t; n011=b-t;
    n100=8-c-a+t; n010=8-c-b+t; n001=9-a-b+t;
    n000=10+c+a+b-t.

Only the two degree-eight roles may be interchanged. `mixed_triples/GENERAL_GATE.json` covers all 75 nonnegative types with a<=b and 0<=t<=min(c,a,b). Forty of these types were already evaluated for the selected S<=8 gate and are reused. Forty-seven fixed certificates and one rational joint certificate are strict; 27 remain. The independent no-search replay `general_replay.py` checks the complete 75-type domain and all accepted certificates, with maximum accepted bound 218741000981/218790000000. It takes 0.76 seconds. The complete non-strict relation is:

| c | (a,b) | allowed t |
| --- | --- | --- |
| 1 | (1,2),(1,3),(2,2),(2,3) | 0,1 |
| 2 | (1,1),(1,2) | 0,1 |
| 2 | (2,2),(2,3) | 0,1,2 |
| 2 | (3,3) | 0,1 |
| 3 | (1,1) | 0,1 |
| 3 | (2,2) | 0,1,2 |
| 3 | (3,3) | 0,1 |

In particular every actual external y has all five cross-codegrees at most three: any codegree four would produce a strict mixed triple with any other low vertex. A low-low pair of codegree three forces its two cross-codegrees with y to be equal. A codegree-one low pair cannot both have unit codegree with y. A codegree-two low pair cannot have cross-codegrees 1 and 3. These are global restrictions on the same fifteen outside vertices; they are not extra assumptions.

As a cheap diagnosis, `marginal_pilot.py` enumerates at most 3^5=243 five-dimensional cross-codegree vectors per core, retaining the above pair restrictions, and tests the necessary common marginal equations

    sum_y 1=15,
    sum_y lambda(i,y)=32-sum_{j != i} lambda(i,j), for each i.

All 49 linear relaxations are feasible; each has only 25--63 allowed vectors (see `MARGINAL_PILOT.json` for exact counts). Runtime was 0.039 seconds. This is a failed exclusion test, not an existence certificate or an exact arithmetic proof. No conclusion is drawn from floating-point feasibility. Its purpose is to show that pairwise cross-codegree restrictions and these five aggregate equations alone do not immediately close the branch.

Filtering the already saved partial 8,163 promotion orbits through all ten selected-y mixed triple gates leaves 2,331. This is still a partial domain over eleven source cores and was not sent to a larger DP. Further work should use the full common old-slot distribution over all fifteen actual outside vertices, the inclusive triple totals

    sum_y I_{ijy} = 3 lambda(i,j) - sum_{k in A minus {i,j}} I_{ijk},

or a single valid weighted S+alpha*r budget, before constructing a larger six-lock table. The pairwise marginal relaxation has been tested and should not be repeated unchanged.

Reproduce the newly accepted local gate without LP or position search:

```sh
python3 -B context/propertyb35-paper/round01/middle/twenty-delta8/exact_five_external/mixed_triples/general_replay.py
```
