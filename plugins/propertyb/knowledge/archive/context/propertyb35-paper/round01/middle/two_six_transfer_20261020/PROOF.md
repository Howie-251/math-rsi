# 21 points with exactly two degree-six vertices and zero or one degree-seven vertex

## Statement and scope

Let H consist of 35 distinct five-element edges on 21 vertices and cover every pair of distinct vertices. Suppose exactly two vertices x,y have degree six, all remaining vertices have degree at least seven, and the number a of degree-seven vertices is zero or one. If a=1, additionally suppose lambda(x,y)<=2. Then H has Property B.

The a=0 conclusion does not require the extra restriction on lambda(x,y). This gives complete natural-language candidates for the parent-requested open cases a0/lambda2 and a1/lambda1,2. It does not claim the whole 21-point minimum-degree-six branch, the full 21-point problem, or m(5)>=36. The proof reuses fixed finite local certificates; its deterministic runs and actual mathematical imports are separated below. No Lean or whole-hypergraph search was run.

## 1. The complete nine degree spectra

Assume H is non-B. Write b for its number of degree-eight vertices and e=sum_v max(d(v)-9,0). The total degree 175 gives

    12+7a+8b+9(19-a-b)+e=175,
    e=2a+b-8.

For either degree-six center, pair coverage gives twenty positive codegrees summing to twenty-four, so its repetition excess is exactly four. At most four degree-eight points are nonunit neighbors. The existing six-unit-eight-pool theorem applies to **any** degree-six center, explicitly without global uniqueness. Non-B therefore forces at most five unit-eight neighbors and hence b<=9. Consequently

    8-2a<=b<=9,          0<=e<=2a+1<=3.

Represent the positive excess above nine by a partition of e. The exact degree multiset is

    6,6; a copies of 7; b copies of 8;
    19-a-b degree-nine baselines with that partition added.

This gives two spectra for a=0 and seven for a=1. All partitions are permitted: there are at least nine degree-at-least-nine points and e<=3. Their sums of degree wedges W=sum C(d(v),2), and their final moment results, are listed in Section 5.

The pool theorem and its actual scope are stated in
`../../twentyone-high/unique6_with7/new_structure_20261020/SIX_UNIT8_POOL_PROOF.md`.

## 2. Global codegrees, quadruple intersections and C3

### All point codegrees are at most four

Any degree-six center has codegree at most five by its repetition excess four. The codegree-five direct repair in `../generic_high_degree_pair_gates_20261020/REPORT.md`, Section 5, applies without a uniqueness or other-degree assumption: the star-compatible balanced sample has size 177176, whereas the union bound for the 29 noncenter edges is 29*6006=174174. Thus a non-B H has no codegree five involving either six-degree point.

Every other point has degree in 7,...,12. The total e<=3 implies max(d(u)-9,0)+max(d(v)-9,0)<=3. `PAIR_VERIFY.py` reconstructs the exact double-lock trace counts

    mu0=35-du-dv+c, mu1=du-c, mu2=dv-c, mu3=c

for all seventy such selected-degree inputs with c>=5, and evaluates only the two old fixed layouts (10,21), (21,10), with zero quotas. All seventy are strict, maximum 230293/230945. The computation expands all 35 edge indices and all 1190 ordered distinct pairs using the existing independent falling-factorial injection implementation. These are fixed arithmetic certificates and do not use any degree of an unselected vertex. Hence every actual pair has lambda<=4.

### No four-set is contained in three original edges

If a four-set K containing a degree-six point is in r>=3 edges, those six center edges cover at most r+4(6-r)<=15 vertices outside K. Pair coverage requires all seventeen outside vertices, a contradiction.

If K contains neither degree-six point, all four selected degrees are at least seven and their total excess above nine is at most three. The complete generic four-core inventory in `../generic_quad_core_multiplicity_three_20261020/PROOF.md` covers this input. Its 3805 strict representatives leave only four nonstrict tails, each of degree vector (10,10,10,10) and therefore excess four. Our e<=3 excludes all four tails. The strict representatives use the original pair-coverage nested quotas where needed; they do not assume uniqueness of a degree-six point or any lower bound on unselected degrees.

Thus every four-set lies in at most two original edges.

### Therefore n4<=13

Fix either six-degree center x and delete its six edges. The remaining Hbar has 29 five-edges on twenty points. The complete general six-star count gives at least 164896 compatible 10/10 samples. The general nonunit-graph forest lemma gives rank at least 29-20+2=11. If Hbar's four-intersection graph had forest rank at least four, a common Hunter tree would deduct at least

    4*2002+7*132+17*22=9306

from the 29 bad-event counts. Since 164896-29*6006+9306=28>0, H would be B. Thus its four-intersection forest rank is at most three, and Hbar has at most six four-intersection pairs.

Each x edge has at most one four-intersection neighbor in Hbar: two would form three edges containing its four-point link, already excluded. This contributes at most six cross pairs. Within the six x edges there is at most one four-intersection pair. Two different link pairs with intersection at least three would consume at least six repetitions, contradicting the x-star's exact repetition budget four. Therefore n4<=6+6+1=13.

These are exactly the general star/forest parts of `../generic_quad_core_multiplicity_three_20261020/PROOF.md`, Section 7. Global uniqueness occurs there only in its original actual four-core caller; that caller was replaced above. The star count and forest rank do not depend on it.

### The three-intersection common-middle capacity

The general c14 gate in `../generic_c3_fourteen_gate_20261020/PROOF.md` assumes only selected pointpair codegrees<=4 and selected high excess<=4. Its theorem explicitly imposes no degree-six uniqueness, degree-role or paircover assumption. Applied to our actual H, all lambda<=4 and e<=3 give C3<=13 n3.

## 3. Gamma minimum degree four: exact q3 transfer

Let Gamma have the 35 original edges as vertices, adjacent when their intersection size differs from one. The general 21-point/35-edge q<=2 repair already implies that non-B H has Gamma minimum degree at least three.

Suppose an actual edge F has Gamma degree three. Its three exceptional F traces may be empty or have sizes two, three, four, with repetitions; its other thirty-one edges have singleton traces. The complete existing 3276-label/91-S5-orbit q3 anchor calculation applies without role assumptions. Its full safe sets leave exactly 119 trace/attachment inputs.

`Q3_TRANSFER_VERIFY.py` independently reconstructs those 119 from the saved exact safe thresholds and the complete integer composition domain, then imposes the actual local necessary conditions:

    min F degree>=6, at most two F degree-six points,
    at most a F degree-seven points, F high excess<=2a+1.

It obtains thirteen inputs for a=0 and sixty-nine for a=1; the thirteen are a subset of the sixty-nine. `Q3_FIVE_LOCK_FULL69.py` applies only the same existing fixed sixteen-position menu and zero quotas. Sixty-six of the sixty-nine are strict, each independently expanded and replayed over 35 distinct indices/1190 ordered pairs. The sole newly allowed double-six inventory is

    exceptional traces (0,0,7), singleton counts (7,7,7,5,5),
    F degrees (9,9,9,6,6).

It is strict at positions (4,3,12,2,1), with bound 38361/40040. The three nonstrict tails are precisely the old A, B, C:

|Tail|Exceptional F traces|Singleton counts|F degrees|F excess|
|---|---|---|---|---:|
|A|7,11,28|6,7,7,6,5|9,10,10,9,7|2|
|B|7,25,30|4,7,7,7,6|7,10,10,10,9|3|
|C|7,25,30|5,7,7,6,6|8,10,10,9,9|2|

All three violate e<=1, so none occurs when a=0. If a=1, choose either actual degree-six point x; all F degrees are at least seven, so x is outside F. Put rF=sum_{v in F}(lambda(x,v)-1). Covering F gives five necessary incidences. Every x edge meets F nontrivially because none of the three listed exceptional traces is empty. Thus the six x edges give at least six incidences and rF>=1. If any chosen trace is a triple or quadruple, these six nonempty traces contribute at least eight incidences and rF>=3. If all are singleton, their counts are precisely one of the five vectors 1+e_i.

For A or C, e>=2 and b=6+e>=8. Non-B requires at least b-5>=3 nonunit degree-eight neighbors of x. A has no degree-eight point in F, so at least three such points are outside F; they consume at least three of x's four repetition units, leaving rF<=1. C has exactly one degree-eight point in F, so at least two are outside F, giving rF<=2. Both exclude triples/quadruples. Their actual x stars therefore belong to the five singleton choices each.

For B, e>=3 and hence e=3,b=9. Its F has no degree-eight point. At least four nonunit-eight neighbors outside F consume all four repetitions, leaving rF=0, in contradiction to rF>=1. B is impossible.

The five A and five C singleton-star inventories are a subset of the existing complete47 six-lock certificates. The fixed certificates depend only on their actual 35 six-lock traces; neither requires x to be the only degree-six point. `Q3_TRANSFER_VERIFY.py` separately reconstructs their 35 distinct trace indices and replays all ten by falling-factorial injection arithmetic: all strict, maximum 64/65. Thus both A and C also color the original H. This excludes all q3 cases, proving Gamma minimum degree at least four.

This transfer does not use lambda<=4, n4<=13, or the C3 gate, so there is no circular dependence between this minimum-degree lemma and Section 2.

## 4. Degree-four local gate away from the second low point

The theorem in `../four_nonunit_degree_six_center_20261020/REPORT.md` was originally stated with global uniqueness. Inspecting its actual equations and scripts shows its exact requirement is **local**: F contains a chosen degree-six point, all four other F points have degree at least seven, at most three F points have degree seven, F excess<=4, its internal pair codegrees<=4, and its chosen center's six edges cover all twenty other points. No unselected point's degree is read or used. Thus it applies to every x edge avoiding y, and to every y edge avoiding x.

In the present role all these conditions hold: a<=1, e<=3, Section 2 gives lambda<=4, and pair coverage gives the center-star coverage. Each such edge cannot have Gamma degree four in a non-B H. Section 3 already gave every edge Gamma degree at least four, so all these eligible edges have Gamma degree at least five.

If c=lambda(x,y), there are exactly (6-c)+(6-c)=12-2c distinct eligible edges. The two lists are disjoint because each avoids the other center. By the handshake lemma, with E=|Gamma edges|,

    2E>=4*35+(12-2c), hence E>=76-c.

For c=1 this is E>=75, and for c=2 it is E>=74. This counts actual original edges of the same Gamma; no independent local optimizers are identified with a common H.

## 5. Full moment domain and the remaining sixteen aggregate keys

Use n_j for the number of unordered pairs of distinct original edges intersecting in j vertices. All pointpair codegrees lie in 1,...,4. Define tau=sum_{pointpairs} C(lambda-1,2), so 0<=tau<=140. For W determined by the exact degree spectrum, the three original moments give

    n1=W-280-2tau+3m+8t,
    n2=140+tau-3m-6t,
    n0=735-W+tau-m-3t,       m=n3, t=n4.

The general single-flip repair gives the non-B necessary bound n1>=397. Section 2 gives t<=13. The actual pointpair-row bound gives

    tau>=max(0,4(Delta-10)).

Section 3 implies every original edge has at most thirty singleton-intersection neighbors. With f(s) the balanced five-part cross sum and X=2(595-n1)-140, convexity over thirty-capacity boxes gives the exact safe scalar bound B(n1) from Section 4 of `../a2_a3_min4_cap13_closure_20261020/PROOF.md`; it uses neither a criticality import nor a threshold-graph DP.

The general degree capacities apply unchanged:

    C0<=33n0,
    C1<=35n1-K_d(n1),
    C2<=floor((S6-6)/2)n2=(24+floor(e/2))n2,
    C3<=13n3, C4<=4n4.

Here K_d fills the actual degree capacities C(d,2) from lowest degree upward. S6=54+e because each of the nine complete spectra has at least nine degree-at-least-nine points and at most three positive excesses. This equality is checked independently against each actual degree list.

All Cj share P=sum Cj<=B. Filling capacities in decreasing weights (36,120,330,792,1716) gives the safe maximum of the original two-flip bound

    L=3432n1+(1/2)sum_j w_j Cj.

Whenever L<2722720, the existing two-flip lemma yields a proper coloring of this H.

`MOMENT.py` generates all nine spectra by excess partitions, and all tau/t/m nonnegative moment tuples. The initial necessary moment domain has 761226 keys including their degree spectra. The result below is the maximum L over **all** admissible keys of the corresponding spectrum after t<=13 and the row bound, rather than a sample maximum.

|a|b|Excess partition|W|Maximum L|Remaining keys with L>=2722720|
|---:|---:|---|---:|---:|---:|
|0|8|empty|650|2718744|0|
|0|9|1|651|2719416|0|
|1|6|empty|651|2719416|0|
|1|7|1|652|2724288|1|
|1|8|1+1|653|2725170|3|
|1|8|2|654|2722404|0|
|1|9|1+1+1|654|2729832|6|
|1|9|1+2|655|2728656|3|
|1|9|3|657|2726304|3|

`MOMENT_CHECK.py` independently generates degree spectra by a histogram of degrees ten through twelve, enumerates moments using n1,n3,n4 and a parity condition, and checks the box formula by a separate 35-slot scalar knapsack over all 1051 possible sums. It regenerates all 58 pre-row surviving keys and all 16 post-row keys, with every capacity, greedy allocation and 2L equal to the primary result. It also verifies the complete per-spectrum admissible counts and maximum L values.

All sixteen post-row keys have a=1. Their E=595-n1 distribution is E70:12, E71:3, E72:1. These are necessary aggregate keys, not hypergraph classes. Section 4 forces E>=74 for c<=2, contradicting every one. If a=0 the strict table already contradicts non-B without needing c<=2. Hence the claimed branches have Property B.

## 6. Execution, artifacts and acceptance boundary

The actual deterministic outputs are `PAIR_RESULT.json`, `Q3_FIVE_LOCK_FULL69.json`, `Q3_TRANSFER_RESULT.json`, `MOMENT_RESULT.json`, `MOMENT_CHECK.json`, and `MOMENT_SURVIVORS.json`. Two moment runs plus their checks were used during the small source cleanup; together with all local certificate replays this task used under ten CPU seconds, below the authorized twenty. No local gate source already sent for external review was changed.

The main mathematical imports are the arbitrary-center six-unit-eight-pool theorem, generic q<=2 repair, four-core fixed certificates, general six-star count/forest argument, conditional permutation-to-coloring theorem, and original single/two-flip lemmas. The precise callers have been supplied above. This is a same-family natural-language assembly candidate with actual deterministic verification. Root must still inspect the imports and actual assembly, and record any requested fresh or cross-family review. No external reviewer is represented as having approved this new transfer.

Reproduce the stable local computations in this order:

```sh
python3 context/propertyb35-paper/round01/middle/two_six_transfer_20261020/PAIR_VERIFY.py
python3 context/propertyb35-paper/round01/middle/two_six_transfer_20261020/Q3_TRANSFER_VERIFY.py
python3 context/propertyb35-paper/round01/middle/two_six_transfer_20261020/Q3_FIVE_LOCK_FULL69.py
python3 context/propertyb35-paper/round01/middle/two_six_transfer_20261020/MOMENT.py
python3 context/propertyb35-paper/round01/middle/two_six_transfer_20261020/MOMENT_CHECK.py
```

The q3 transfer script rebuilds its complete input JSON; it also checks the delivered fixed69 certificates. The fixed69 replay may then be rerun independently. The original generic q3 domain and fixed47 source certificates remain unchanged.
