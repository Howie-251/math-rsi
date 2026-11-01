# Reduced A1: the simplified complete arithmetic chain

## Statement and scope

Let H be a simple five-uniform hypergraph on21 vertices with35 edges and full point-pair coverage. Its actual A1 roles are x6,p7,nine degree8,ten degree9; exactly four degree8 points have codegree two with x, and x has codegree one with all other points. The following chain excludes a non-B H with these roles, using the listed actual-H repair imports and complete exact degree-prefix evidence.

The final chain is

    21615 complete integer moment profiles
       ->25 profiles under the threshold-only path budget
       ->one profile under the actual min-degree-two Gram-prefix budget
       ->zero by the actual four-intersection/tau coupling.

The original-H implications are stated below. This is the reduced-A1 branch, not the unrestricted m(5)>=36 theorem. The new combined assembly has deterministic evidence and same-family/provisional verification; this document does not broaden the recorded scope of any cross-family review.

## 1. Original-H consequences before arithmetic

Assume for contradiction that H is not two-colorable.

- The existing A1 strong-pair reduction gives every point-pair codegree at most four. The relevant import is [TWENTYONE_HIGH_FOUR_CORE_LOW.md](../../../../../proofs/propertyb35/TWENTYONE_HIGH_FOUR_CORE_LOW.md), with its original degree-role reduction.
- [TWENTYONE_A1_STRONG_FOREST_RANK.md](../../../../../proofs/propertyb35/TWENTYONE_A1_STRONG_FOREST_RANK.md) gives original n4<=8. More specifically, after deleting x and its six edges, the29-edge Hbar four-intersection graph has forest rank at most two, and there are at most five cross-star four-intersection pairs and none within the x-star. This import uses the uniform balanced-star count and returns a proper original-H coloring whenever its Hunter threshold is exceeded.
- [TWENTYONE_LOW_NONUNIT_DEGREE_REPAIR.md](../../../../../proofs/propertyb35/TWENTYONE_LOW_NONUNIT_DEGREE_REPAIR.md) gives minimum degree at least two in the graph Gamma on the35 original edge indices joined by non-one intersections. It applies directly since A1 has maximum original degree nine. Its sample fixes one red/four blue points of an original edge, and chooses nine red/seven blue among the other16 points; its three strict failure bounds are434/455,1007/1040,448/455. No critical-core assumption is involved.
- [GLOBAL_PRIVATE_PAIR_REPAIR.md](../../../../../proofs/propertyb35/GLOBAL_PRIVATE_PAIR_REPAIR.md) gives n1>=397. The actual A1 link quotas give n1<=546, as recorded in [GLOBAL_TWO_FLIP_SHARED_MIDDLE.md](../../../../../proofs/propertyb35/GLOBAL_TWO_FLIP_SHARED_MIDDLE.md), §6: singleton attachments at x,p,each8,each9 are bounded respectively by13,17,24,30.

Here n_j counts unordered pairs of distinct original edges with intersection j. Define

    tau=sum_{unordered point pairs} binom(lambda-1,2).

Point-pair coverage and lambda<=4 give0<=tau<=140, since sum(lambda-1)=350-210=140 and binom(lambda-1,2)<=lambda-1 in this range. The degree spectrum gives sum j*n_j=sum_v binom(dv,2)=648. Double counting common point pairs gives sum binom(j,2)*n_j=140+tau. Together with sum n_j=595, these identities are equivalent to

    n0=87+tau-n3-3n4,
    n1=368-2tau+3n3+8n4,
    n2=140+tau-3n3-6n4.                                        (1)

Thus every actual non-B H maps into the finite domain

    0<=tau<=140, 0<=n4<=8,
    n_j>=0, 397<=n1<=546,
    n3>=0 with (1).

This domain has exactly21615 integer keys. No graph or H realizability is assumed for a key.

## 2. Same-H shared middle budget

For every original middle edge F, let t_Fg count the other original edges meeting F exactly at g, and put sF=sum_g t_Fg. Define

    P=sum_F sum_{g<h in F} t_Fg*t_Fh.

For an unordered pair of original outer edges of intersection j, let its common-middle count use distinct singleton attachments, and sum these counts as Cj. The exact original-H identity is sum_j Cj=P. If f is the balanced five-group maximum

    f(s)=(s^2-(5-r)a^2-r(a+1)^2)/2,     s=5a+r, 0<=r<5,

then P<=sum_F f(sF), and sum_F sF=2n1. The singleton-intersection graph has35 vertices, n1 edges and degree sequence(sF). The convex threshold-graph majorant proved in GLOBAL_TWO_FLIP_SHARED_MIDDLE therefore gives

    P<=T(35,n1,0),
    T(n,m,r)=max(f(r)+T(n-1,m,r),
                f(n-1+r)+T(n-1,m-n+1,r+1)),                   (2)

with T(0,0,r)=0 and invalid graph sizes excluded.

Use the same-H common-middle capacities

    C0<=33n0, C1<=26n1+339, C2<=24n2, C3<=13n3, C4<=4n4.     (3)

The shared C1 bound and other basic caps are in the two-flip/shared-middle proofs. The strengthened C3 cap is the accepted [THREE_INTERSECTION_MIDDLE_NEAR_SATURATION.md](../../../../../proofs/propertyb35/THREE_INTERSECTION_MIDDLE_NEAR_SATURATION.md):14 common middles of a three-intersection outer pair give an actual original-H coloring. All exclusive points meet its degree hypotheses automatically in A1; a hypothetical six-degree exclusive point contradicts the required cross-row lower bound immediately.

Let R=sum_j (36,120,330,792,1716)_j*Cj. The original-H two-flip theorem gives Property B whenever

    L=R/2+3432n1 <2722720.                                    (4)

To upper-bound R, fill(3) from the highest weight downward, with the shared total capacity(2). This is an exact rational relaxation of the actual common-middle counts. It does not choose different H or different middle edges for different constraints.

[SCALAR_T_ONLY.py](SCALAR_T_ONLY.py) loops the complete21615 keys of §1, uses only P<=T and(3), and tests(4). It leaves exactly25 keys, identical as a set to the frozen25. **No linear P upper bound is used**: neither the former +594 nor +198 constant is needed in this first step. [SCALAR_T_ONLY.json](SCALAR_T_ONLY.json) records21615/25, no extra/missing keys, CPU0.197 seconds. The independent complete rescan is also in SIMPLE_CHAIN_VERIFY.py.

## 3. Actual degree-prefix domain for each of the25 keys

Put E=595-n1 and sort the actual Gamma degrees q1>=...>=q35. Minimum degree two gives qi>=2. Every q is at most34, their sum is2E, and the actual singleton degree is sF=34-qF. Hence

    P<=sum_i f(34-qi).                                       (5)

For any N original edges, incidence Gram principal submatrices give the following lower bound on the number of their non-one pairs, using t=n4(H):

    ell_t(N)=max(0,N-21,
       ceil((8N(N-21)-105t)/84),
       ceil(8N(N-21)/189),
       ceil((152N(N-21)-2037t)/1428)).                        (6)

The independent-set part uses B=AA^T-J=A(I21-J21/25)A^T, PSD rank<=21. Its rank/trace bound gives Q>=8N(N-21)/21, with Q<=4e+5t and Q<=9e. The centered matrix A(I21-J21/21)A^T has rank<=20 and yields1428e+2037n4(S)>=152N(N-21). These derive(6) on every actual original-edge subset, not merely a component or an abstract graph.

Deleting the r highest-degree vertices leaves N=35-r, so exact edge counting gives

    sum_{i<=r}qi <=E+binom(r,2)-ell_t(35-r),   r=1,...,35.    (7)

The original A1 degree sums strengthen some constraints. Let R0=E-60+2t. Deleting any one original edge F gives T_S=92-sum_{v in F}dv<=55. Centered Gram plus Q_S<=T_S+2e(S)+4t gives the even-integer bound e(S)>=60-2t. Thus q1<=R0. Exactly23 edges avoid x,p and have degree sum at least40, strengthening their bounds by one. Consequently

    q1<=R0,        q13<=R0-1.                                (8)

Deleting two original edges loses at least59 from W648 (ten removed incidences, at most two at each point, cheapest original degrees6,7,8,8,8). Therefore their remaining33-edge T_S<=61, centered Gram gives e(S)>=50-2t, and

    q1+q2<=E-49+2t.                                         (9)

The full proofs and independent exact arithmetic are in [the principal-subset derivation](../a1_incidence_rank_subset_20261020/DERIVATION.md), §§1–3.3, and this directory's REPORT §§1–2,9–10. They are actual incidence constraints, not graph realizability assertions.

All25 keys have E<=80,t<=8. Equation(9) gives q1+q2<=47. Nonincrease implies q2<=23, so the q2<=29 check retained in the program is redundant. **No T33/T34 critical-core theorem is an external premise of this simplified chain.** The program's zero-count and pendant checks are also redundant when all qi>=2: l=z=0 and qmax<=34<50. None of the old low<=20, low<=19 or profile-specific low<=13 Schur arguments is used.

## 4. Complete exact DP and independent check

For each of the19 distinct(E,t) keys among these25 profiles, maximize(5) over integer nonincreasing sequences satisfying qi>=2, sum2E, (7),(8),(9). This relaxes graphicality and is safe for an actual Gamma upper bound.

[SIMPLE_CHAIN_DP.cpp](SIMPLE_CHAIN_DP.cpp) fixes the first degree M over all possible values from ceil(2E/35) to min(34,R0). After i entries it keeps the maximum objective for the state(last degree,prefix sum). An appended q ranges from2 to the previous degree, is capped by(8), and its prefix must satisfy(7) and the stronger(9) at i=2. The final prefix equals2E. Each append adds f(34-q). Induction shows that every declared degree sequence is retained at its state and every final state represents a sequence in the declared relaxation. Parent pointers provide an attaining sequence for every bound.

[SIMPLE_CHAIN_FREQUENCY_VERIFY.cpp](SIMPLE_CHAIN_FREQUENCY_VERIFY.cpp) independently recurses through degree values34 down to2 and their multiplicities, checking each created prefix. It rejects an unfinished cardinality when degree one is reached. It uses different state organization and independently matches every one of the19 optimal integers. [SIMPLE_CHAIN_VERIFY.py](SIMPLE_CHAIN_VERIFY.py) also regenerates the full21615 moment domain with P<=T only, checks its25-key set exactly, verifies all19 cache-key identities and all25 Fraction allocations.

The final P upper bound for a profile is simply

    min(DP(E,t),T(35,n1,0)).                                (10)

No linear P bound enters. Its greedy use in(3),(4) leaves exactly one aggregate key:

    (n0,n1,n2,n3,n4)=(33,523,0,31,8), tau=1,
    DP(E72,t8)=12827, L=2725500.

Every other one of the25 keys has a strict coloring bound(4). Full data and degree witnesses are [SIMPLE_CHAIN_RESULT.json](SIMPLE_CHAIN_RESULT.json). The primary full19-key batch cost0.082 CPU seconds; independent frequency/moment checks cost0.592 CPU seconds. [SIMPLE_CHAIN_VERIFY.json](SIMPLE_CHAIN_VERIFY.json) reports PASS with domain counts21615,25,1,0. The final zero uses the separately proved actual-H coupling below, not a claim that degree sequences alone are infeasible.

## 5. Actual coupling excludes the final key and returns the original conclusion

Use [TWENTYONE_A1_QUAD_TAU_COUPLING.md](../../../../../proofs/propertyb35/TWENTYONE_A1_QUAD_TAU_COUPLING.md). For completeness, its short actual step is as follows. The final key has n4=8. The strong forest import bounds Hbar four-intersection rank by two, hence Hbar has at most three four-intersection pairs. The other original pairs give at most five across the x-star and none inside it. Equality n4=8 therefore forces exactly three Hbar four-intersection graph edges. A simple graph of rank at most two with three edges must be a triangle.

There are thus three distinct original Hbar five-edges pairwise intersecting in four points. Two four-subsets inside the first five-set overlap in at least three points, so the triple intersection has at least three actual vertices. Their three distinct point pairs each belong to all three original edges, have lambda>=3, and each contributes at least one to tau. Thus tau>=3, contradicting the final key's tau=1.

The non-B assumption is impossible. Every import producing a strict probability bound has an explicit coloring of the same original H; otherwise the necessary statistics cannot coexist. This proves the reduced-A1 Property-B conclusion through21615→25→1→0, without any low-count Schur exploratory branch, critical-core import, linear P bound, whole-H enumeration or new lock table. The unrestricted35-edge problem has other branches and is not asserted complete here.
