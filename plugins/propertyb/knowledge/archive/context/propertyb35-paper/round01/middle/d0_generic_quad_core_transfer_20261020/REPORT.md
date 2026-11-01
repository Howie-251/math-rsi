# D0 repeat-star quadruple cores: a role-independent transfer

## Result and exact scope

Let H be a simple five-uniform hypergraph on21 vertices with35 edges and full point-pair coverage. Let x have degree6. Suppose three distinct points b1,b2,b3 have degrees in{7,8}, satisfy λ(x,bi)=2, and have their three mutual codegrees at most4. If two distinct original edges contain{x,b1,b2,b3}, then H is two-colorable.

This is a conditional, role-independent four-lock theorem. It needs neither a unique six-degree point, a unique seven-degree point, λ(x,p)=1, nor degrees or roles of the other17 vertices. It does not import the stronger7/8 codegree cap3. The old A1 four-core proof's §3 depends only on these selected degrees, the three center codegrees, the three remaining codegree caps, simplicity,35 edges,21 points and point-pair coverage. Its use of A1 roles was to guarantee that selected data, not an additional ingredient in the36 certificates.

All four degree vectors pass their complete36-inventory domains:

|Selected degree vector|Complete labeled inventories|Maximum exact bound|
|---|---:|---:|
|(6,8,8,8)|36|11676/12155|
|(6,7,8,8)|36|2331/2431|
|(6,7,7,8)|36|23269/24310|
|(6,7,7,7)|36|23269/24310|

Every maximum is strictly less than1. The original(6,8,8,8) maximum is recovered exactly. Independent complete input reconstruction and fixed-certificate replay is PASS for all144 inventories.

## Actual H to the complete36 inventories

Label x,b1,b2,b3 by bits0,1,2,3. The two distinguished original edges already use both incidences allowed by each λ(x,bi)=2. Therefore the exact full trace has multiplicity2, the exact singleton{x} has multiplicity4, and every other trace containing x has multiplicity0. This follows from the same actual six edges through x; it is not a freely chosen completion.

For the29 original edges avoiding x, let a,b,c be the inclusive numbers through b1b2,b1b3,b2b3 respectively, and let t count those through all three points. The original mutual pair caps give0≤a,b,c≤2 and0≤t≤min(a,b,c). With di=d_H(bi), all exact nonzero-possible counts are forced:

\[
\mu_{15}=2,\quad\mu_1=4,
\]
\[
\mu_2=d_1-2-a-b+t,\quad
\mu_4=d_2-2-a-c+t,\quad
\mu_8=d_3-2-b-c+t,
\]
\[
\mu_6=a-t,\quad\mu_{10}=b-t,\quad\mu_{12}=c-t,
\quad\mu_{14}=t,
\]
\[
\mu_0=35-d_1-d_2-d_3+a+b+c-t.
\]

There are exactlyΣ_{a,b,c=0}^2(min(a,b,c)+1)=27+8+1=36 parameter choices. Each is nonnegative for di∈{7,8}, sums to35 and has the specified degrees. We keep all36 even if an additional restriction of a particular actual branch would exclude some of them. The three b-labels can be permuted to put their degrees in nondecreasing order, yielding exactly the four jobs above; no whole-H automorphism is required.

## Probability theorem, genuine cover deductions, and original coloring

Use the [conditional permutation probability theorem](../../../../../proofs/PROBABILITY_LEMMAS.md). For each inventory, RESULT.json stores four distinct selected positions and an exact bound

\[
\mathcal B=\sum_{k=1}^{21}\min(A_k,B_k,C_k-\ell_k)<1.
\]

The remaining17 original vertices are uniformly permuted without replacement. Every coefficient refers to the same actual35 original edge indices. The C terms retain distinct ordered original-edge pairs; traces with equal masks do not identify the edges.

The deductions use only point-pair coverage at the selected locks. For selected degree d, its four-set link covers the other20 points, so at least ceil((4d−20)/3) distinct unordered link pairs meet outside their center. This is2,3,4 for degree6,7,8. The pure-singleton quota is max(0,ceil((4μ_single−17)/3)). Pure slots are used first, and then only unused slots contribute to the remaining total quota. Same-trace and different-trace capacities are respectively C(μ_T,2) and μ_T μ_U; the cost of an unordered pair is its two directed event weights. Taking the cheapest available nonnegative weights gives a valid lower bound on the actual impossible-pair deduction, with no duplicate charging of the same original pair.

These conditions are entirely selected-degree and cover data. In particular the quotas do not use the old A1 partition into p,B,U,V9, and no assumption is made that free-point edges or choices are independent.

A strict bound supplies an actual permutation outside the greedy-failure event. Starting with all points red, process that permutation and turn the current point blue when it is the last point of an edge still all red. The probability theorem ensures every original edge contains both colors outside the critical event. Thus the certificate returns a proper coloring of H itself, completing the conditional theorem.

## Independent verification

[PILOT.py](PILOT.py) enumerates exact a,b,c,t data and discovers each layout with the existing subset-position dynamic program. It independently replays A/B/C injection probabilities while recording the nested quota certificates. [RESULT.json](RESULT.json) stores all144 complete keys, layouts,21 rows and exact deductions; measured CPU2.187053 seconds.

[VERIFY.py](VERIFY.py) does not import PILOT or the position solver. It first checks that the saved job set is exactly the mathematical four-vector set. It chooses the inclusive codegrees λ(x,bi)=2 and λ(bi,bj)∈{2,3,4}; inclusive triples through x all equal2, the non-x inclusive triple ranges from2 to the minimum mutual pair count, and the fourfold count is2. General four-point Möbius inversion recovers each exact trace. For each job the resulting full36 keys equal the saved domain and case keys exactly.

The independent fixed replay expands each case into35 distinct original edge indices and recomputes21 injection rows,1190 ordered distinct original pairs and all nested deductions. Every saved exact rational bound is equal to the recomputed bound, and all144 are strict. [VERIFY.json](VERIFY.json) records PASS. This is a finite necessary-local-domain proof, not an enumeration or existence assertion for H. Mathematical checking here remains same-family/provisional; new cross-family review is separate.

## D0 star interface and the old18-domain payoff

Assume the actual D0 center x has exactly four repeated neighbors, each occurring in two of its six link four-sets, all other16 neighbors occurring once; suppose each repeated neighbor has degree7 or8 and their mutual pair codegrees are at most4. Represent a repeated neighbor by the unordered pair of link indices that contain it. This is a loopless four-edge multigraph on six block labels.

Three parallel graph edges mean that two original x-edges share x and three repeated neighbors. The theorem just proved colors H in every possible7/8 assignment on those three points. Four parallel edges would make the two original five-edges identical and is already excluded by simplicity. Hence a non-B D0 source has edge multiplicity at most2.

Its star therefore lies in exactly the same previously classified domain as the A1 repeat-star:15 possible block pairs, four chosen with repetition, multiplicity at most2. The old count is2835 labeled multisets and18 S6-orbits, with no other shape excluded. The private points fill the4−degree(block) remaining places; their role is determined by the actual star, not by their full-H degrees. All graph degrees are automatically at most4.

Consequently the **star-only** balanced-color event and its old18-orbit counts transfer: its minimum is164896 out of C(20,10)=184756, as in [the existing star count](../../../../../proofs/propertyb35/TWENTYONE_A1_BALANCED_STAR_FOREST.md). This step transports only the common star domain/count. It does not automatically transport the A1-specific degree moments, forest/rank estimates for the29 noncenter edges, or the full A1 theorem to A2/A3. The actual D0 degree and strong-pair premises must be supplied by their own branch reductions.

The separate old [multiplicity-three four-core theorem](../../../../../proofs/propertyb35/TWENTYONE_HIGH_FOUR_CORE_MULTIPLICITY_THREE.md) already has a role-independent statement for four8/9 points. It is not needed to exclude the present parallel3 configuration: these are two original edges sharing x and three repeated points, so the full four-trace count here is exactly2.
