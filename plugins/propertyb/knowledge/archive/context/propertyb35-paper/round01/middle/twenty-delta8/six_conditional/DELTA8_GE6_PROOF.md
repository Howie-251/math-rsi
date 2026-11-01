# Twenty vertices, minimum degree eight, at least six degree-eight vertices

This is a complete paper-proof candidate for this branch. It does not assert that the case of exactly five degree-eight vertices is covered.

Let H be a simple five-uniform hypergraph with 20 vertices and exactly 35 edges, covering every vertex pair, and let its minimum degree be eight. Assume that at least six vertices have degree eight. Then H has Property B.

For any ordered list L of s distinct vertices, write n_T for the number of edges whose intersection with L has exactly the index set T. These are actual nonnegative integer multiplicities. Their sum is 35 and the sum over T containing any index is eight. All projections below are formed by summing these same n_T over deleted coordinates; they are not separately selected hypothetical inventories. Reordering L permutes all subsets by the same permutation and preserves every counting certificate.

We use the previously established exact multilock counting inequality, including the actual same-center bad-edge-pair quotas. For fixed positions of s locks, the common denominator is (20-s)!, and the verified numerator bounds the expected number of failures. A numerator strictly below that denominator gives a proper coloring by the permutation argument. A joint certificate uses several positions and orders for the same inventory and the same actual bad-pair variables, with nonnegative rational weights of total one, nonnegative quota multipliers and the verified capacity penalties. Thus the joint bounds also apply to the original H. No independence of the two free sides or of different layouts is assumed.

The complete old double and triple tables are `../../20-new-high/DIAGNOSIS.json`, with their fixed replay in that directory. Degree-eight pairs of codegree at least five are excluded by the double table. A codegree-four pair with any third degree-eight vertex is excluded by the triple table. There are at least six degree-eight vertices, so every pair among them has codegree in {1,2,3}. After identifying the simultaneous permutation of the three lock labels, the only triple parameters not strictly excluded are:

| Sorted pair codegrees | Inclusive triple count |
| --- | --- |
| 111 | 0,1 |
| 112 | 0,1 |
| 113 | 0,1 |
| 122 | 0,1 |
| 123 | 0 |
| 222 | 0,1,2 |
| 223 | 0,1,2 |
| 233 | 0,1 |
| 333 | 0,1,2,3 |

For four actual degree-eight vertices, choose all six pair counts in {1,2,3}, all four inclusive triple counts admitted by this table, and their inclusive four-count q. Inclusion-exclusion gives n_4=q, n_3=t-q, n_2=c-sum(t)+q, n_1=8-sum(c)+sum(t)-q and n_empty=3+sum(c)-sum(t)+q, with each sum restricted to supersets or incident subsets of the indicated trace. Retain exactly the nonnegative inventories. This gives 4,878 labelled inventories and 385 true S4 orbits. The complete fixed and joint certificates strictly exclude 341 orbits, leaving 44 orbits and 461 labelled inventories. See `../four_projection/DOMAIN.json`, `FOUR_DP.json`, `FOUR_JOINT.json`, `FOUR_REMAINDERS.json` and the independent `replay.py`. Its accepted strict maximum is 54991457/55000000.

For five actual degree-eight vertices, every four-coordinate projection must be one of those 461 labelled residuals. This is a simultaneous necessary condition, since otherwise that actual four-tuple already supplies a proper coloring. To recover the five-point inventory, join two four-point residuals over their same three-point exact inventory n_T. If a_T and b_T count edges from old slot T containing each of the new points, the number q_T containing both must satisfy

    max(0,a_T+b_T-n_T) <= q_T <= min(a_T,b_T).

The four new exact slots are n_T-a_T-b_T+q_T, a_T-q_T, b_T-q_T, q_T. Their total inclusive new-pair count is between one and three. The exact full-five trace is at most one, by simplicity. Check the three further four-coordinate projections against the same residual relation. The unique inventory with n_empty=15 and n_T=2 on each two-point trace is excluded by the separate general lemma `../rigid_external/CORE_DOUBLE_PAIR_PROOF.md`; that lemma applies with any minimum-eight external degrees, not only an exact 8^5 9^15 spectrum. The remaining domain has 23,995 labelled inventories and 361 true S5 orbits. Fixed and joint certificates leave 49 orbits, comprising 1,505 labelled inventories. Their independently recovered domain, transports and certificates are in `../five_join/`; its accepted strict maximum is 5004/5005.

Now choose six actual degree-eight vertices. Each of the six five-coordinate projections is in the same 1,505-inventory residual relation, or the proof is already complete. Recover the six-point inventory by joining two such five-point inventories over their common four-point exact inventory n_T (T ranges over the subsets of four old coordinates). Define a_T,b_T,q_T exactly as above, with the same interval bounds. Also require:

* 1 <= sum_T q_T <= 3, the inclusive codegree of the two new points;
* q_{1234}=0, since a five-edge cannot contain six selected vertices;
* q_T <= 1 when |T|=3, since then T together with the two new vertices is an actual five-element edge;
* each of the four further five-coordinate projections is in the same 1,505-inventory relation.

The seed views already guarantee the other exact five-trace simplicity bounds. These conditions are necessary for every actual H, and the displayed four-slot reconstruction recovers its exact inventory without loss. `domain.py` exhausts the bounded intervals, obtaining 35,915 labelled inventories in 136 true S6 orbits. It stores, for every labelled inventory, a single permutation of all six coordinates transporting its representative to that inventory. Thus this is a genuine quotient by simultaneous label permutations.

`SIX_DP.json` contains a fixed certificate for every one of the 136 representatives. Exactly 134 are strict. The remaining representatives 7 and 54 have strict joint certificates in `SIX_JOINT.json`, with bounds 37743591/38500000 and 687500747/715000143, respectively. The largest bound used across all 136 cases is 3002/3003. Consequently every possible actual six-point inventory gives a proper coloring of H.

The independent replay uses a different domain recovery: it directly promotes one sixth point from each of the 49 five-point representatives, applies the actual slot capacities, degree-eight marginal, pair bounds, full-six exclusion, full-five simplicity, and all five new projections, and then takes the full S6 closure. It recovers exactly the same 35,915 labelled inventories and 136 orbits, checks all 35,915 stored transports, and re-evaluates all 136 fixed certificates and both rational joint certificates without running a DP, an LP or a position search. Its 2,620,608 recursive states and 1,294,260 promotion leaves finish in 26.49 seconds on this run. `REPLAY.json` records PASS and the exact maximum above.

Reproduce the fixed evidence from the project root:

```sh
python3 -B context/propertyb35-paper/round01/middle/twenty-delta8/six_conditional/replay.py
```

New discovery work reused the 18 already verified pilot profiles. The other fixed profiles took 4.92 seconds. The two joint certificates took 3.19 seconds including cached fixed loading. The original bounded two-view domain construction took 17.52 seconds. All arithmetic acceptance uses exact rational numbers and arbitrary-size integers; floating-point LP output serves only to propose the separately repaired and replayed rational witnesses.
