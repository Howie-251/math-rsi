# A complete one-six seven-unit gate and the new minimum-empty core

Use the actual r=1 hypotheses of `MIXED_ONE_SIX_UNIT8.md`:25 points,35 simple five-edges, pair coverage, unique degree-six point z, unique degree-eight point t, and23 degree-seven points. A seven-unit lock set I is required to contain z and six seven-degree points. Such a set is guaranteed after the seven-degree K5 branch is excluded.

The complete unit-seven catalogue has22 uncolored large-trace families. Reconstruct every unused pair as one size-two trace. If B is the full set of traces of size at least2 and h_i=7−|{T∈B:i∈T}|, then the actual marked inventory is n_i=h_i−1_{i=z} and n_empty=36−|B|−Σh_i. All22 families and all seven low marks are feasible:154 labeled inputs,54 low-mark-preserving orbits. The degree-eight point is unlocked; no assumption about its individual trace distribution is used by the raw bound.

Nineteen consecutive layouts, transported by exact permutations preserving the low mark, cover115 labeled inputs. Fourteen remaining colored orbits were tested by the seven-lock subset DP, taking1.21 seconds. Eleven become raw ABC strict. The final raw fixed-layout gate covers143 of154 labeled inputs, maximum1325/1326. Exactly these three colored orbits remain without a strict certificate:

| Source core | Large traces | Position of z | Low marks in source labeling | Empty multiplicity | Best tested raw bound |
|---|---|---|---|---|---|
|0|none|arbitrary|0,…,6|8|1465/1428|
|16|{2,3,6}, {4,5,6}|their intersection|6|6|10927/10608|
|19|{4,5,6}|inside the triple|4,5,6|7|25241/24752|

The former all-seven core21 is strict here; so is core19 with z outside its triple (5197/5304). The new core16 cannot be discarded when selecting I to minimize empty multiplicity.

## A structural consequence: core0 is impossible at the minimum

In a putative non-B input, select I among all seven-unit sets of the stated degree pattern to minimize n_empty. The strict gate implies I has one of the preceding three forms. Suppose its minimum equals8, hence I has core0.

For x outside I define w_I(x)=Σ_{i∈I}(λ(x,i)−1), and put b=w_I(t). Since only the six seven-degree lock points contribute positive weighted rows, Σ_{x outside I}w_I(x)=24. Every one of the17 external seven-degree points has w_I(x)≥1: otherwise it extends I to an eight-unit set of one six and seven sevens, which the complete eight-lock gate makes colorable. If h of these17 points have w_I(x)=1, then

24−b ≥ h+2(17−h),  hence h≥10+b.

Such a private x has a unique partner i with λ(x,i)=2; the partner is a seven-degree point because z is globally unit. Replace i by x. This produces another seven-unit set containing z. Let r_x be the number of edges through x disjoint from I, and s_xi the number whose I-trace is exactly {i}. The new empty multiplicity is

8−r_x+n_{i}−s_xi = 9−r_x−s_xi.

It is at least8 by minimality. The gate leaves only empty values6,7,8 in a non-B graph, so it is also at most8. Therefore r_x+s_xi=1 and r_x≤1.

For a nonprivate external seven-degree point, let p,q,r count its incidences with single, pair, empty I-traces. Core0 has no larger trace. The equations p+q+r=7 and p+2q=7+w_I(x) give2r+p+w_I(x)=7; thus r≤2. For t the same equations have degree8 and give2r_t+p_t+b=9, so r_t≤floor((9−b)/2). Count incidences of all18 external points with the eight empty-trace edges:

40 = Σ_{x outside I}r_x ≤ h+2(17−h)+floor((9−b)/2)
   =34−h+floor((9−b)/2) ≤24−b+floor((9−b)/2) ≤28,

a contradiction. Thus a minimum-empty lock set in a non-B candidate is either core16 with z at the common point of its two triples (empty6), or core19 with z inside its triple (empty7).

## Precise next structural boundary

The exchange formula remains valid for every private seven-degree x and its partner i≠z: at a minimum, r_x+s_xi≤n_i. In core19 this gives the same numerical single-slot budgets1 outside the triple and2 inside. However the low mark must lie inside the triple, and core16 must first be handled before one can require the minimum to be7. In core16 the budgets are1 for i∈{0,1} and2 for i∈{2,3,4,5}; z is not an eligible partner.

Also write B_i for the private seven-degree points with partner i. If x,y∈B_i had λ(x,y)=1, replacing i by x,y would give eight unit locks of one six and seven sevens, contrary to the strict gate. Hence λ(x,y)≥2 inside B_i. Since each seven-degree weighted row is4 and w(x,i)=1, |B_i|≤4. Equality4 would exhaust all five rows in the K5 on {i}∪B_i, giving a seven-degree K5 component already handled by the mixed single-G theorem. Thus |B_i|≤3. In core16, either a triple-member partner has at least two private points, or h≤3+3+1+1+1+1=10. In the latter case h≥10+b forces b=0, h=10, the two non-triple partners each have three private points, and each of the four triple-member partners has one. This is a structural alternative, without an enumerated extension domain.

A further direct consequence, useful without a new table: if a private seven-degree x lies in a triple-trace edge, its partner i must belong to that same triple and be different from z. Indeed put a=1 for that triple and let q be its pair-trace incidence count. The degree and lock-incidence equations give r_x=q+1. If the partner is outside this triple then s_xi=2−q_i, where q_i≤q, so r_x+s_xi≥3, greater than either available budget1 or2. If the partner is in the triple then s_xi=1−q_i; its budget2 forces q_i=q. Thus all pair-trace edges through x also contain its partner. This observation does not require a classification of the remaining stars.

## Independent verification

`MIXED_ONE_SIX_UNIT7_CERTIFICATE.json` lists the143 strict raw layouts. `MIXED_ONE_SIX_UNIT7_REPLAY.py` rebuilds the full154-input domain from all22 catalogue families and independently checks each strict rational ABC bound; it uses no DP, transporter, quota code or original domain implementation. It passed in1.49 seconds, with exactly the11 labels in the three residual orbits above. The imported22-family classification remains explicit.

No double-private-star domain has been generated. The unresolved problem is now the two stated minimum-empty cores, with the complete eight-unit gate and the actual private-count inequality available. The local gate and the core0 descent do not alone close the r=1 branch.
