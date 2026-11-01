# Original-edge Gram constraints in a degree-sequence relaxation

**Current reader entry:** [SIMPLE_CHAIN.md](SIMPLE_CHAIN.md) gives the complete reduced-A1 chain21615→25→1→0. The complete25-profile rerun uses all qi>=2 and actual principal/degree cuts, followed by the proved four-intersection/tau coupling. It needs none of the intermediate low-count Schur arguments, no critical-core theorem and no linear P bound. Its evidence is SIMPLE_CHAIN_RESULT/VERIFY plus SCALAR_T_ONLY. Sections below preserve the earlier stages and their then-current residual counts; they are not the final branch status. The unrestricted m(5)>=36 goal is not claimed complete.

## Outcome

Starting with the frozen25 surviving intersection-moment profiles, the exact degree-prefix DP gives:

|prefix conditions|critical-core condition|profiles remaining|
|---|---|---:|
|independent-set bound only|q2<=29, accepted T33 import|15|
|independent-set bound only|q1<=29, conditional T34-paper import|9|
|uncentered principal trace/rank plus independent-set|q2<=29|6|
|centered principal trace/rank plus both preceding bounds, uniform n4<=8|q2<=29|6|
|same centered bounds using each exact original n4|q2<=29|4|
|same bounds plus actual deleted-edge degree cuts q1<=R,q13<=R-1|q2<=29|4|
|same bounds plus two-deletion prefix and PSD pendant capacity|q2<=29|3|
|same bounds plus low-block rank l+z<=20|q2<=29|3|
|same bounds plus exclusion of the rank-one low20 equality case: l+z<=19|q2<=29|3|
|actual Schur trace/rank forces low<=13 on those three remaining keys|q2<=29|2|
|direct actual coloring excludes every q<=1, applied to the same three keys|q2<=29|**1**|

The two uniform-n4 principal modes leave the same six keys. Their centered calculation left a closest value2722740, only20 above the coloring threshold2722720. Using the exact n4 of each original moment profile removes that key and one more, leaving the four keys in §8; the final Schur-pendant/two-deletion refinement leaves the three keys in §10. It does not establish that any of these six keys or extremal degree sequences is a graph or an H. The conditional q1 result is kept separate and is not used to strengthen the unconditional conclusion.

All optimal values were independently recomputed by a degree-multiplicity DP, distinct from the layer/prefix implementation. All final C-capacity allocations use rational arithmetic. No graph, hypergraph, lock inventory or negative family was generated.

## 1. Actual graph and Gram principal submatrices

H has35 distinct five-edges on21 vertices. Let Gamma have those35 original edges as vertices, with an adjacency exactly when their intersection size is not one. Write e=|E(Gamma)|=595-n1, and sort its degrees as

    34>=q1>=q2>=...>=q35>=0,       sum qi=2e.

The singleton-neighbor count of original edge F is sF=34-qF. The middle path total obeys

    P <= sum_F f(sF),
    f(s) = (s^2 - (5-r)a^2-r(a+1)^2)/2,  s=5a+r, 0<=r<5.

This is the balanced five-group bound on the actual sum of products of singleton attachments, as in the existing shared-middle proof. The current DP only maximizes this degree upper bound.

Let A be the incidence matrix of any N selected original edges, with21 columns. Since its rows all have sum5,

    B=AA^T-J_N = A(I_21-J_21/25)A^T.

The middle matrix is positive definite, so B is PSD and has rank at most21. For an independent set of Gamma, every off-diagonal entry of its B principal submatrix vanishes and the diagonal is4. Thus its size is at most21. For every vertex set L of Gamma,

    e(L) >= max(0,|L|-21).                                        (1)

Indeed deleting at most one chosen endpoint of every edge leaves an independent set of size at least |L|-e(L). No assumption that L is a component is used.

For a set R of r highest-degree vertices, L=V(Gamma) minus R has N=35-r vertices, and

    sum_{i<=r} qi = e + e(R)-e(L)
                   <= e+binom(r,2)-ell(35-r),                     (2)

where initially ell(N)=max(0,N-21). These are necessary conditions on the same original graph, not sufficient graphicality conditions.

## 2. Stronger principal trace/rank lower bounds

The following derivations independently confirm the supplied principal-submatrix formulas. Let

    Q = sum_{unordered selected edge pairs} (|F intersect G|-1)^2.

For the uncentered B above, tr B=4N and tr B^2=16N+2Q. The PSD rank inequality (tr B)^2<=21 tr B^2 gives

    Q >= 8N(N-21)/21.

For original non-one pairs the squared weights at intersection0,2,3,4 are1,1,4,9. Therefore Q<=4e(L)+5n4(L)<=4e(L)+40, using the separately proved original n4<=8. Also Q<=9e(L). Hence one may take

    ell_1(N)=max(0,N-21,
                 ceil(2N(N-21)/21-10),
                 ceil(8N(N-21)/189)).                            (3)

The first three N=34,33,32 lower bounds from the middle term are33,28,24.

For the centered matrix

    B0=AA^T-(25/21)J_N = A(I_21-J_21/21)A^T,

PSD rank is at most20, with diagonal80/21. Its trace/rank inequality gives

    sum_{unordered pairs}(21|F intersect G|-25)^2
        >=160N(N-20).

Subtracting the baseline16 for every unordered pair, the non-one weights become21 times29,13,68,165 for intersections0,2,3,4. Consequently

    21 sum_{Gamma[L] edges} w_j >=152N(N-21),
    1428e(L)+2037n4(L) >=152N(N-21).

The second inequality uses w_j<=68 except at j=4, where the excess is97. The strengthened lower bound is

    ell_2(N)=max(ell_1(N),ceil((152N(N-21)-16296)/1428)).            (4)

The N=34,33,32 bounds are36,31,27. Equations(3),(4) hold for arbitrary original-edge subsets L, not only a component. The original n4<=8 import is global, so replacing every subset's n4(L) by8 safely relaxes rather than strengthens its actual domain. The complementary PSD proof is also recorded by the independent agent in `../a1_incidence_rank_subset_20261020/DERIVATION.md`.

## 3. The two other degree restrictions and their scope

The root-checked exceptional singleton-attachment argument gives at most three original edges with sF=34, equivalently at most three zero degrees qF. This is used in every mode; it is not derived from the independent-set inequality.

The [critical-core lemma](../a1_critical_core_singleton_degree_20261020/CRITICAL_CORE_LEMMA.md) applies accepted T33 to a non-B35-edge H. An inclusion-minimal non-B core has at least34 original edges, each with at least five distinct singleton-intersection neighbors inside that same core. Thus at most one vertex of Gamma has degree greater than29, which is exactly

    q2<=29.                                                       (5)

This does not assume H itself is edge-critical and does not apply A1 degrees to the core. The optional mode q1<=29 requires an at-most34-edge Property-B theorem to force the core to be all of H. It is only a conditional diagnostic here. It was run for the initial prefix bound, retained as such, and is unnecessary for the principal-prefix conclusions.

## 4. Exact DP and complete coverage of its relaxed domain

For each e=72,...,80 occurring in the25 frozen keys, maximize

    sum_{i=1}^{35} f(34-qi)

over integer nonincreasing q satisfying sum qi=2e, at most three zeros, (5), and every one of the35 inequalities(2), with ell chosen from(1),(3),or(4). The conditional initial mode instead imposes q1<=29.

[DP.cpp](DP.cpp) is a layer DP. Its state after i entries is (last,prefix), retaining the largest objective among all prefixes with those values. It appends each integer q between0 and last. The first32 entries are required positive, exactly enforcing at most three zeros in a nonincreasing sequence. From the second entry onward q<=29; in the conditional mode this cap starts at the first entry. Every appended prefix is tested against(2). Prefixes with sum>2e, too little remaining degree capacity last*(35-i), or insufficient remaining degree to make the required positive entries are discarded. The remaining-capacity tests are necessary conditions and cannot remove a complete feasible sequence.

Initialization is the empty prefix with last34 and value0. The final states require prefix2e. Induction on i proves that the recurrence covers every sequence in its declared relaxed domain and retains its maximum objective. All transitions and objective values are integers. Parent pointers reconstruct an attaining sequence; all reconstructed sequences are checked against every declared restriction.

[VERIFY.py](VERIFY.py), [STRONG_VERIFY.py](STRONG_VERIFY.py), and [CENTERED_VERIFY.py](CENTERED_VERIFY.py) do not import the layer recurrence. They descend through possible degree values34,...,0 and choose the multiplicity of each degree, checking each prefix created by that multiplicity. Their state is (next degree, number used, degree sum, number used above29). This independent frequency recursion reproduces all18 initial optima and all9 optima in each stronger mode. It also checks the25 weighted allocations in exact Fraction arithmetic. All three results are PASS.

These are degree-sequence relaxations. They do not test the Erdős–Gallai inequalities, the full Gram matrix, point incidence, or H realizability. This deliberate relaxation is safe for upper bounds and important when interpreting the witnesses below.

## 5. Optimal path bounds and combination with existing bounds

The optimal DP values are:

|e|initial q2<=29|initial conditional q1<=29|uncentered principal|centered principal|
|---:|---:|---:|---:|---:|
|72|13111|13070|13005|12973|
|73|13079|13021|12961|12934|
|74|13049|12974|12917|12912|
|75|13021|12941|12875|12871|
|76|12971|12895|12836|12825|
|77|12935|12850|12810|12785|
|78|12887|12807|12765|12761|
|79|12841|12773|12722|12717|
|80|12809|12729|12680|12675|

For every actual moment key n, the value used for P is

    min(DP(e), T(35,n1,0), (132n1+198)/5).

The previous verified threshold majorant T and new exceptional-degree linear bound are both retained. The latter is not substituted by subtracting a universal amount from the previous objective. Given this P upper bound, fill capacities

    (33n0,26n1+339,24n2,13n3,4n4)

in decreasing event weights(1716,792,330,120,36). If R is the resulting weighted sum, the necessary non-B test is L=R/2+3432n1>=2722720. All quantities are rational. This filtering is complete for the frozen25 keys because every earlier-excluded key remains excluded after a smaller P upper bound.

The final six centered-prefix survivors are:

| (n0,n1,n2,n3,n4) | tau | L | L-2722720 |
|---|---:|---:|---:|
|(34,520,2,32,7)|0|2724060|1340|
|(33,522,2,30,8)|0|2729160|6440|
|(35,519,0,35,6)|1|2722740|20|
|(34,521,0,33,7)|1|2729280|6560|
|(33,523,0,31,8)|1|2734260|11540|
|(34,521,1,31,8)|2|2726256|3536|

## 6. Tight witness and the remaining structural gap

For e=76, the initial, uncentered and centered attaining degree sequences, in multiplicity notation, are respectively

    (34,29,5,4^18,2,1^10,0^3),       objective12971;
    (33,9^11,1^20,0^3),              objective12836;
    (34,10,8^11,2,1^18,0^3),         objective12825.

The final one produces the closest surviving profile (35,519,0,35,6),tau1 above. It has sum152, respects every chosen prefix bound, q2<=29 and exactly three zeros. Its final capacity allocation is saved in CENTERED_RESULT.json.

These witnesses visibly need not be graphic: a vertex of degree34 cannot coexist with an isolated vertex in a simple35-vertex graph. Thus the remaining20 in the final objective is not a realized obstruction or a fractional H. It is an exact gap in the particular relaxed domain. Even the elementary coupling q1<=34-z when there are z isolates is not imposed by the requested state; full graphicality is also not imposed. No additional DP or graph search was started to exploit these omissions.

## 7. Files, reproduction and measured cost

The complete outputs are [RESULT.json](RESULT.json), [STRONG_RESULT.json](STRONG_RESULT.json), and [CENTERED_RESULT.json](CENTERED_RESULT.json), including every attaining sequence and all25 filtered keys. Their independent outputs are [VERIFY.json](VERIFY.json), [STRONG_VERIFY.json](STRONG_VERIFY.json), and [CENTERED_VERIFY.json](CENTERED_VERIFY.json). The frozen input is the previous CAPACITY_FILTER.json, which contains all25 keys rather than a selected sample.

```sh
c++ -std=c++17 -O2 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/DP.cpp -o /tmp/a1_degree_prefix_dp
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/RUN.py
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/VERIFY.py
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/STRONG_RUN.py
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/STRONG_VERIFY.py
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/CENTERED_RUN.py
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/CENTERED_VERIFY.py
```

The generating DP batches cost about0.04,0.02,0.04 CPU seconds. The independent frequency checks cost1.62,1.02,1.22 CPU seconds. Memory for the C++ layer and parent arrays is below1MB; no solver dependency is used. This is deterministic scalar evidence, with same-family/provisional review status. Neither canonical proofs nor navigation/wiki were changed.

## 8. Final refinement: retain each profile's exact n4

There is no need to replace n4(H) by8 when its exact value t is already part of a moment key. Every principal subset has n4(L)<=t. The same derivation therefore strengthens the lower bound to

    ell_t(N)=max(0,N-21,
                 ceil((8N(N-21)-105t)/84),
                 ceil(8N(N-21)/189),
                 ceil((152N(N-21)-2037t)/1428)).

The uncentered term is exactly ceil(2N(N-21)/21-5t/4). This changes no source or H domain and introduces no T34 dependence. The C++ DP takes the optional fifth argument t, default8 to preserve every preceding run. The independent frequency implementation uses the identical mathematical ell_t but its own multiplicity recursion.

All25 frozen profiles use19 distinct(e,t) pairs. In particular the earlier frozen domain includes n4=4 and5 as well as6,7,8; none was discarded on account of an informal parameter list. [PROFILE_N4_RESULT.json](PROFILE_N4_RESULT.json) contains all19 optimal values, every35-entry witness and all25 rational filtering results. [PROFILE_N4_VERIFY.json](PROFILE_N4_VERIFY.json) reports independent frequency-DP PASS for all19 values and all25 allocations. DP batch CPU0.069 seconds; independent check CPU2.59 seconds.

Exactly four profiles remain:

| (n0,n1,n2,n3,n4) | tau | Pbound | L | L-2722720 |
|---|---:|---:|---:|---:|
|(33,522,2,30,8)|0|12934|2729160|6440|
|(34,521,0,33,7)|1|12879|2727300|4580|
|(33,523,0,31,8)|1|12973|2734260|11540|
|(34,521,1,31,8)|2|12912|2726256|3536|

The former margin20 profile had e=76,t=6; its bound decreases from12825 to12792 and it is now excluded. The closest remaining key is the last row, with attaining relaxed degree sequence

    q=(34,8^11,7,1^19,0^3),
    sum q=148, sum f(34-q)=12912,
    C=(0,12453,24,403,32).

Again q1=34 together with three zeros proves that this particular sequence is not graphic. It is only an optimizer of the stated safe relaxation, and the four profiles are not claimed to be feasible graphs or H inputs. The possible additional graphical coupling mentioned in §6 was not imposed.

Reproduce the final refinement after compiling DP.cpp as above:

```sh
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/PROFILE_N4_RUN.py
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/PROFILE_N4_VERIFY.py
```

This concludes the requested scalar filtering; no new lock, original-H or negative-layout search is implied.

## 9. Actual degree sums strengthen the one-edge-deletion cuts

For each original edge F, delete it and consider the remaining34 original edges S. A1 has W=sum_v binom(dv,2)=648. Therefore

    W_S=648-sum_{v in F}(dv-1)=653-sum_{v in F}dv,
    T_S=sum_{unordered pairs in S}(|E intersect J|-1)
       =W_S-binom(34,2)=92-sum_{v in F}dv.

Every original five-edge has degree sum at least6+7+3*8=37, so T_S<=55. The exact centered trace inequality from §2 can equivalently be written

    Q_S-(8/21)T_S >=67184/441.

Writing a_j for its intersection counts and e(S)=a0+a2+a3+a4, the identity

    Q_S=T_S+2e(S)-2a2+4a4

gives Q_S<=T_S+2e(S)+4t. Consequently

    2e(S)+4t >=67184/441-(13/21)*55=52169/441.

The left side is an even integer, so e(S)>=60-2t. Since deleting F removes qF edges of Gamma, qF=E-e(S) and every qF<=R=E-60+2t.

There are exactly23 original edges avoiding both x and p: their two stars have union6+7-lambda(x,p)=12 original edges. Every such F has degree sum at least40 and hence T_S<=52. The analogous right side52988/441 forces e(S)>=61-2t. Thus at least23 degrees qF are at mostR-1, or in sorted form

    q1<=R,       q13<=R-1.

This derivation was independently checked here and by the source agent; it uses the original A1 degrees and no T34-paper assumption. Keeping the actual incident four-intersection degree q4(F) would additionally give qF+2q4(F)<=R (at most R-1 for these23 F), but that edge-colored coupling is not imposed by this degree-only DP.

[DEGREE_CUT_RUN.py](DEGREE_CUT_RUN.py) adds only q1<=R,q13<=R-1, to all25 frozen profiles and all19(e,t) keys. The layer recurrence limits entry i to R-(i>=13). The independent multiplicity recursion disallows degrees aboveR and permits at most12 copies of degreeR. It reproduces all19 optima and all25 allocations: [DEGREE_CUT_VERIFY.json](DEGREE_CUT_VERIFY.json), PASS. Generating batch CPU0.058 seconds; independent check2.95 seconds.

All four previous residual keys remain, with lower objectives:

| (n0,n1,n2,n3,n4) | tau | L | L-2722720 |
|---|---:|---:|---:|
|(33,522,2,30,8)|0|2726340|3620|
|(34,521,0,33,7)|1|2724360|1640|
|(33,523,0,31,8)|1|2730660|7940|
|(34,521,1,31,8)|2|2723256|536|

The last key now has optimal relaxed sequence

    q=(30,9^10,8,1^20,0^3),       Pbound=12862.

Unlike the earlier universal-vertex witnesses, this sequence passes the Erdős–Gallai inequalities. It nevertheless cannot belong to a graph with alpha<=21: the degree30 vertex has only11 possible other degree-at-least-two vertices, hence at least19 degree-one neighbors. These19 leaves together with the three isolates form an independent22-set. This is a precise remaining weakness of replacing alpha<=21 by only its induced-edge prefix consequences. It is not an H counterexample and no further state enlargement was undertaken. In general, if z is the isolate count and k the number of vertices of degree at least two, any degree-q vertex with q>=2 forces an independent set of size at least z+max(0,q-k+1).

All preceding calculation stages remain saved. Reproduction of this last stage after compilation:

```sh
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/DEGREE_CUT_RUN.py
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/DEGREE_CUT_VERIFY.py
```

## 10. Final PSD-pendant capacity and the two-edge-deletion prefix

### 10.1 A common capacity on pendant neighbors

Use the actual uncentered B=AA^T-J with diagonal4. If I is an independent set of Gamma inside the neighborhood of a vertex v, its principal submatrix is4I. The principal block on {v} union I is PSD. Testing the vector (1,-b/4), where bi=|v intersect i|-1, gives

    4-(1/4)sum_i bi^2>=0,       sum_i bi^2<=16.

Every degree-one neighbor of v belongs to such an independent I and each has bi^2>=1, so v has at most16 degree-one neighbors. Let l,z be the numbers of vertices of Gamma of degree one and zero, and k=35-l-z the number with degree at least two. A vertex of maximum degree q>=2 has at most k-1 neighbors of degree at least two and at most16 degree-one neighbors, whence

    qmax <= k+15,       qmax+l+z<=50.                              (8)

This directly uses actual PSD incidence, not just an arbitrary graph's alpha bound. With z<=3 it also implies the earlier independent-leaf consequence qmax+l+2z<=55. Only the stronger(8) was added in this final calculation.

### 10.2 A stronger second prefix

Delete two arbitrary distinct original edges F,G. If mv in{0,1,2} is the number of these two edges through v, the loss from W=648 is

    sum_v [mv*dv-mv(mv+1)/2] >= sum_v mv(dv-3/2).

There are ten removed incidences and each point can occur at most twice. Taking the two cheapest slots at the five smallest original degrees6,7,8,8,8 bounds this loss below by2*37-15=59; allowing the same five points for both edges is a safe relaxation. Thus the remaining33 original edges S have W_S<=589 and T_S=W_S-binom(33,2)<=61.

The centered PSD inequality for N=33 gives

    Q_S-(8/21)T_S >=60192/441.

Using Q_S<=T_S+2e(S)+4t yields

    2e(S)+4t >=60192/441-(13/21)*61=43539/441.

The left side is even, so e(S)>=50-2t. The two deleted graph vertices contain at most one Gamma edge, hence their degree sum is at most E+1-e(S), proving

    q1+q2 <= E-49+2t.                                            (9)

No special intersection type of F,G is assumed; this applies to the actual highest-degree two vertices. Only this second-prefix cut was added, not any three-deletion extension.

### 10.3 Exact final DP and independent coverage

[PENDANT_DP.cpp](PENDANT_DP.cpp) enumerates each possible maximum M from ceil(2E/35) to the established cap R. It fixes the first degree to M, then uses the existing layer recurrence for the remaining34 entries. By(8), at least M-15 entries must have degree at least two, so the recurrence requires qi>=2 whenever i<=M-15. It still enforces qi>=1 through i=32, nonincrease, exact total2E, q2<=29, q13<=R-1, all profile-specific centered principal prefixes, and now(9) at i=2. These conditions are equivalent to the declared degree relaxation, so the maximum over all M covers it completely. No particular saved maximizing sequence is merely deleted after optimization.

[PENDANT_FREQUENCY_VERIFY.cpp](PENDANT_FREQUENCY_VERIFY.cpp) is a distinct memoized recursion by descending degree values and their multiplicities. It tracks the first positive degree M. At the final degree-one step, its number of remaining ones c and zeros z are uniquely determined by the remaining total degree and cardinality, and it tests M+c+z<=50 directly. It checks every created prefix including(9). Thus it imposes the same condition through a different state organization. [PENDANT_VERIFY.py](PENDANT_VERIFY.py) runs it on all19 actual(E,t) keys, checks equality with every primary optimum and checks all25 rational allocations. Result [PENDANT_VERIFY.json](PENDANT_VERIFY.json): **PASS**.

The generating batch used0.072 CPU seconds and independent frequency verification0.421 CPU seconds. Complete output, parent-witness degree sequences and all25 allocations are in [PENDANT_RESULT.json](PENDANT_RESULT.json). The final surviving aggregate keys are exactly:

| (n0,n1,n2,n3,n4) | tau | Pbound | L | L-2722720 |
|---|---:|---:|---:|---:|
|(33,522,2,30,8)|0|12880|2725920|3200|
|(34,521,0,33,7)|1|12824|2724000|1280|
|(33,523,0,31,8)|1|12910|2730480|7760|

The closest final key has E=74,t=7 and optimal relaxed degree sequence q=[28, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], objective12824. Its full sequence is independently checked in the result files.

The former fourth key (34,521,1,31,8),tau2 now has Pbound12850 and L2722536<2722720, so it is rigorously excluded within this complete scalar relaxation. The three survivors are aggregate allocations only, not actual graphs or H realizations. The calculation does not claim that these constraints characterize all possible incidence matrices. All preceding result files remain unchanged.

Reproduction:

```sh
c++ -std=c++17 -O2 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/PENDANT_DP.cpp -o /tmp/a1_pendant_dp
c++ -std=c++17 -O2 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/PENDANT_FREQUENCY_VERIFY.cpp -o /tmp/a1_pendant_frequency
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/PENDANT_RUN.py
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/PENDANT_VERIFY.py
```

No Erdős–Gallai filter, extra r=3 prefix derivation, graph search, lock table, solver, Lean, MCP or navigation edit was used. Review independence remains same-family/provisional.

## 11. Additional actual low-block rank condition

Let L be the set of Gamma vertices of degree zero or one, with |L|=z+l. Its induced graph consists only of isolated vertices and disjoint pairs. The B principal block on L is therefore a direct sum of[4] and matrices[[4,b],[b,4]], where |b|<=3 because original distinct five-edges have intersection at most four. This low block is positive definite.

Eliminate it by a Schur complement. A degree-one pair wholly in L has no original Gamma neighbor in the remaining core. A degree-one vertex attached to the core has exactly one nonzero core entry. Thus elimination modifies only core diagonal entries, preserving every off-diagonal entry of the core block. Edges not wholly within the core number at most l. Since E>=72>l, the core has an edge, so the PSD Schur complement has a nonzero off-diagonal entry and rank at least one. Rank additivity of the Schur complement now gives

    rank B >= (l+z)+1,      l+z<=20,      #{qi>=2}>=15.             (10)

This is stronger than merely PSD or the pendant-neighbor condition. It uses rankB<=21 of the same actual incidence matrix; it is not an arbitrary-graph assertion. The derivation was independently checked here and by the rank-subset source agent.

[LOW_RANK_DP.cpp](LOW_RANK_DP.cpp) adds min qi>=2 for the first max(15,M-15) positions. [LOW_RANK_FREQUENCY_VERIFY.cpp](LOW_RANK_FREQUENCY_VERIFY.cpp) independently rejects final degree-one tails unless at least15 vertices of degree at least two have already been chosen. Both therefore recompute the complete declared sequence domain rather than discarding the previously saved witnesses. Full19(e,t) optima and all25 moment keys are retained in [LOW_RANK_RESULT.json](LOW_RANK_RESULT.json); [LOW_RANK_VERIFY.json](LOW_RANK_VERIFY.json) reports PASS. CPU0.096 seconds for generation and0.412 seconds for independent checking.

Three aggregate keys still remain:

| (n0,n1,n2,n3,n4) | tau | Pbound | L | L-2722720 |
|---|---:|---:|---:|---:|
|(33,522,2,30,8)|0|12878|2725800|3080|
|(34,521,0,33,7)|1|12815|2723460|740|
|(33,523,0,31,8)|1|12906|2730240|7520|

The closest current witness is q=(28,10,9^9,6,2^3,1^17,0^3), E74,t7, objective12815. All three optimizers have l17,z3 and attain the boundary |L|=20. Their possible equality structure has not been added to the DP. In particular, the preserved rank-one Schur core would have to have clique-plus-isolates off-diagonal support. The saved E73/74 witnesses have core edge counts56+p and57+p respectively, where0<=p<=8 counts degree-one pairs, and neither interval contains a possible triangular clique edge count. This diagnoses additional relaxation slack; it does not exclude either entire moment profile. No rank-one equality filter, graphicality filter or new domain was run.

Reproduction:

```sh
c++ -std=c++17 -O2 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/LOW_RANK_DP.cpp -o /tmp/a1_low_rank_dp
c++ -std=c++17 -O2 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/LOW_RANK_FREQUENCY_VERIFY.cpp -o /tmp/a1_low_rank_frequency
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/LOW_RANK_RUN.py
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/LOW_RANK_VERIFY.py
```

All earlier result files are preserved. The conclusion is a necessary aggregate compression with three unexcluded profiles, not a realized non-B input or a proof of the full A1 branch.

## 12. Stable final count cut: low<=19 on the current E range

For the current72<=E<=80, the equality case low=l+z=20 in §11 can also be excluded by a uniform paper argument. The core has15 vertices and its PSD Schur complement has rank one. It is vv^T, so its nonzero off-diagonal support is a clique on a active coordinates; the other15-a coordinates have zero diagonal. Its off-diagonal entries are still the original ones, of absolute value at most3.

An inactive core coordinate has Schur diagonal zero, so the attached degree-one leaves must have squared original entries summing to16. Each nonzero square is1,4,or9. No sum of at most three such squares equals16: with no9 the sum is at most12; with one9 the remaining needed7 is not a sum of at most two1/4; with two9 the sum already exceeds16. Thus each inactive coordinate requires at least four distinct attached leaves.

At most one active coordinate can have Schur diagonal greater than3: two such coordinates would have off-diagonal absolute value equal to the square root of their diagonal product, greater than3. Every other active coordinate therefore needs at least one attached leaf, since no attached leaf would leave its original diagonal4 unchanged. Consequently

    l >=4(15-a)+(a-1)=59-3a.

Since l<=20, a>=13. Let p be the number of degree-one pairs. All noncore Gamma edges number l-p, with p<=floor(l/2). The clique core has binom(a,2) edges, so

    E=binom(a,2)+l-p >=binom(a,2)+ceil(l/2).

If a=13 then l>=20 and E>=78+10=88. If a>=14 the clique alone has at least91 edges. Both contradict E<=80. Hence

    l+z<=19,       #{qi>=2}>=16.

This proof uses no triangle classification, new subgraph enumeration, or critical assumption. It was independently checked here, by the root, and by the principal-rank source agent; no new cross-family acceptance is claimed.

Only this count parameter was changed after §11. [LOW19_DP.cpp](LOW19_DP.cpp) requires qi>=2 for the first max(16,M-15) positions; [LOW19_FREQUENCY_VERIFY.cpp](LOW19_FREQUENCY_VERIFY.cpp) tests at least16 entries already selected at the degree-one tail. All19(E,t) pairs and all25 frozen aggregate keys were recomputed. [LOW19_VERIFY.json](LOW19_VERIFY.json) is PASS against [LOW19_RESULT.json](LOW19_RESULT.json). CPU0.096 seconds generation and0.418 seconds independent verification.

The stable final remaining set is still exactly three aggregate keys:

| (n0,n1,n2,n3,n4) | tau | Pbound | L | L-2722720 |
|---|---:|---:|---:|---:|
|(33,522,2,30,8)|0|12876|2725680|2960|
|(34,521,0,33,7)|1|12812|2723280|560|
|(33,523,0,31,8)|1|12905|2730180|7460|

The closest final witness is q=(28,10,9^9,5,2^4,1^16,0^3), with E74,t7 and objective12812. These are necessary aggregate leftovers, not realized graphs or H classes. The complete optimal degree witnesses are saved with all19 bounds; no further constraint or search was added after this count cut. All earlier outputs are unchanged. Reproduction is the same pair of commands as §11, replacing LOW_RANK by LOW19 and binary low_rank by low19.

## 13. Actual Schur trace/rank: only the three previous keys

Retain the actual low-block elimination of §11. Let h=l+z, core size k=35-h, and let s_v be the sum of squared original B entries from degree-one leaves attached to core vertex v. The Schur complement C has unchanged core off-diagonal entries, diagonal4-s_v/4, rank at most21-h, and s_v<=16 by PSD. Put S=sum s_v and Q=E+3n3+8t, the sum of squared original B entries over all unordered non-one pairs.

An attached leaf contributes a squared entry1,4,or9. Each contribution is at most4 plus an extra5 only for an original four-intersection pair, so

    S<=4h+5t.

The original core squared-entry sum is at mostQ-S, since low-pair contributions are nonnegative. Therefore

    tr C=4k-S/4,
    tr C^2=16k-2S+sum_v(s_v^2)/16+2Q_core
           <=16k+2Q-3S,

where sum s_v^2<=16S. The PSD rank/trace inequality gives the following necessary condition without division by the possible rank:

    F_h(S)=224(35-h)-2(21-h)Q-(7+h)S+S^2/16<=0.

For t<=8, on0<=S<=4h+5t its derivative is at most-(7+h)+(4h+40)/8=-2-h/2<0. Thus an actual input necessarily satisfies F_h(4h+5t)<=0. Its sixteenfold value is the concave quadratic

    -48h^2+(32Q-4032-40t)h+125440-672Q-560t+25t^2.

For the three previously remaining actual moment keys, (Q,t) equals(227,8),(229,7),(229,8). The h=14,20 endpoint values are respectively

    (1376,9056), (1673,9977), (928,8992).

All are positive. Concavity makes every value on14<=h<=20 positive. Since §11 already excludes h>=21, these three keys require h<=13, or at least22 degree-at-least-two vertices. This statement is only applied to these three keys; it is not imposed on any earlier-excluded profile or arbitrary A1 profile with a different Q. The mathematical proof was independently checked by the root, the rank-subset source agent and here.

[TRACE_DP.cpp](TRACE_DP.cpp) changes only the positive-degree-two count to22. [TRACE_FREQUENCY_VERIFY.cpp](TRACE_FREQUENCY_VERIFY.cpp) checks the same count at its final degree-one tail. [TRACE_RUN.py](TRACE_RUN.py) reads the three survivors directly from LOW19_RESULT.json, binds each to its exact(Q,t), and stores the endpoint checks. Only the three(E,t) pairs(73,8),(74,7),(72,8) were computed. [TRACE_VERIFY.py](TRACE_VERIFY.py) independently recomputes every optimum and rational capacity allocation, and evaluates16F directly with Fraction arithmetic rather than the expanded polynomial. [TRACE_VERIFY.json](TRACE_VERIFY.json): PASS.

The new bounds and final status are:

| (n0,n1,n2,n3,n4) | tau | Pbound | L | status |
|---|---:|---:|---:|---|
|(33,522,2,30,8)|0|12855|2724420|unexcluded; margin1700|
|(34,521,0,33,7)|1|12792|2722080|excluded; strict margin640|
|(33,523,0,31,8)|1|12883|2728860|unexcluded; margin6140|

Thus this actual Schur-trace restriction reduces the three aggregate leftovers to two; it does not close the complete branch. All records and witness degree sequences are in [TRACE_RESULT.json](TRACE_RESULT.json). The primary batch cost0.024 CPU seconds and the final independent check0.063 CPU seconds. No other profile, graph/H domain, lock, filter, Lean or model call was added. All old stages are preserved.

```sh
c++ -std=c++17 -O2 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/TRACE_DP.cpp -o /tmp/a1_trace_dp
c++ -std=c++17 -O2 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/TRACE_FREQUENCY_VERIFY.cpp -o /tmp/a1_trace_frequency
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/TRACE_RUN.py
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/TRACE_VERIFY.py
```

## 14. Direct original-H coloring excludes every degree-zero/one event vertex

**General lemma independently checked here.** Let H be a simple five-uniform hypergraph on exactly21 vertices with35 edges and maximum original point degree at most9. If an original edge F has at most one non-one-intersection neighbor, H is two-colorable. No point-pair coverage, A1 role or source state is required.

Color one point v of F red and the other four points blue. Color its16 outside points uniformly with nine red and seven blue. For any original edge meeting F in exactly one point, its monochromatic probability is126/1820 if that point is v, and35/1820 otherwise: these are binom(9,4)/binom(16,4) and binom(7,4)/binom(16,4). The outside choices are not independent; only these marginal probabilities and the union bound are used.

If qF=0 there are34 such singleton edges. Some attachment group has size a<=6. Choose its point v red. Their total bad probability is

    [126a+35(34-a)]/1820 <=1736/1820=434/455<1.

If qF=1, let G be the unique exceptional original edge. There are33 singleton edges. If G is disjoint from F, again choose an attachment group of size at most6. Its singleton contribution is at most1701/1820, and G's monochromatic probability is

    [binom(9,5)+binom(7,5)]/binom(16,5)=147/4368=7/208.

Their sum is1007/1040<1. If |G intersect F|=2,3,or4, choose v in their intersection. G already contains v red and at least one of the other four blue points of F, so is deterministically proper. Exactly a=d_H(v)-2<=7 singleton edges attach at v, since both F,G contain v. Hence their bad sum is at most

    [126*7+35*26]/1820=1792/1820=448/455<1.

In every case F itself is proper. A positive-probability choice makes every other original edge proper, completing the original-H lemma. Simplicity ensures G cannot meet F in all five points. Thus any non-B A1 input must have qF>=2 for all35 original edges. This direct coloring condition is stronger than all the preceding low-count conditions and does not depend on the Schur-trace profile gate.

Following the specified computation scope, only the same three LOW19 residual keys were recomputed with all35 entries at least two. [ALL_TWO_DP.cpp](ALL_TWO_DP.cpp) applies minq=2 at every layer. [ALL_TWO_FREQUENCY_VERIFY.cpp](ALL_TWO_FREQUENCY_VERIFY.cpp) rejects every unfinished tail when it reaches degree one. Both retain the earlier principal prefixes and deleted-edge degree cuts. [ALL_TWO_RUN.py](ALL_TWO_RUN.py) verifies the three rational coloring bounds directly and binds the exact three input keys; the now-unneeded Schur-trace profile assumption is not used by this last run.

The output and independently reproduced optima are:

| (n0,n1,n2,n3,n4) | tau | Pbound | L | status |
|---|---:|---:|---:|---|
|(33,522,2,30,8)|0|12803|2721300|excluded, strict margin1420|
|(34,521,0,33,7)|1|12738|2718840|excluded, strict margin3880|
|(33,523,0,31,8)|1|12827|2725500|unexcluded, margin2780|

The unique remaining aggregate optimizer has q=(28,9^6,8,2^27), sum144, objective12827. It is a degree-sequence witness only, not a hypergraph construction. All3 exact optima and allocations are saved in [ALL_TWO_RESULT.json](ALL_TWO_RESULT.json), and independent verification is [ALL_TWO_VERIFY.json](ALL_TWO_VERIFY.json), PASS. Generation CPU0.032 seconds; independent verification0.085 seconds. Only these3 keys were run; no other role, degree domain, lock inventory or graph/H search was added. Full A1 remains unproved.

```sh
c++ -std=c++17 -O2 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/ALL_TWO_DP.cpp -o /tmp/a1_all_two_dp
c++ -std=c++17 -O2 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/ALL_TWO_FREQUENCY_VERIFY.cpp -o /tmp/a1_all_two_frequency
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/ALL_TWO_RUN.py
python3 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/ALL_TWO_VERIFY.py
```
