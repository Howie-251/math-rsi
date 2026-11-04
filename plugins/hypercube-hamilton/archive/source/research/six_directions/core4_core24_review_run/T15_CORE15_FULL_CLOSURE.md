# Complete T15 core 15

Date: 2026-11-01. ARIS proof-writer. Candidate complete proof for one marked core, with independently checked finite inputs. Fresh overall review is required before integration. Full T15 and the complete eight-hole layer are not asserted.

## Claim

For every matching $F$ of $K(Q_5)$ with holes $\{0,1,2,13,22,31\}$, there is a simple cycle on $Q_5-\{1,2\}$ containing every edge of $F$, with every new edge a cube edge. The claim includes all cube-automorphic images of this marked geometry. Original matching edges may have arbitrary lengths and parity types.

## Status

PROVABLE AS STATED, conditional on the previously audited Q4 N14 and balanced-table imports stated below. The complete finite input manifest is `T15_CORE15_FULL_CLOSURE_VERIFICATION.json`. Fresh overall semantic review remains pending.

## Assumptions

1. Q4 N14 in its arbitrary complete-graph matching scope: every matching with two same-parity holes extends to a 15-cycle omitting either specified hole and using short added edges.
2. The complete independently audited balanced Q4 tables, each covering all $10395$ matchings on twelve covered vertices. See `T15_BALANCED_BRIDGE_REVIEW.md/.json`.
3. The independent small-crossing B enumeration in `T15_R3_SMALL_CROSSING_PROGRESS.md` and `t15_r3_small_verification.json`.

## Notation and normalized geometry

Swap global coordinates three and four. The old-to-new destination map is $(0,1,2,4,3)$. It sends the original holes to $\{0,1,2,14,21,31\}$ and fixes the prescribed omissions $1,2$.

In these normalized global labels write $v_A=2v+1$ and $v_B=2v$. Thus face $A$ has holes $\{0,10,15\}$ and omits $0_A$; face $B$ has holes $\{0,7,1\}$ and omits $1_B$. The retained global free vertices are $0,21,31,14$.

Write $F_A,F_B$ for the internal matching edges, $X_A,X_B$ for the port sets, and $C:X_A\to X_B$ for the arbitrary original crossing bijection. Let $c=|C|$. Both faces have thirteen originally covered vertices, so $c$ is odd, $1\le c\le13$, and each internal matching has $(13-c)/2$ edges.

For the large-crossing argument always choose bridge $z=10$. The balanced table with holes $\{0,7,10,1\}$ and omissions $10,1$ has exactly one negative matching:

$$L_0=\{(2,4),(3,13),(5,15),(6,8),(9,11),(12,14)\}.$$

`verify_t15_core15_table.py` independently reads the audited raw table, applies the coordinate permutations that produce this geometry, checks their consistency, and verifies this unique negative. Its report is `t15_core15_table_verification.json`.

## Proof Strategy

N14 applies for every artificially chosen endpoint matching. The induced forest pairing must have connected union with that chosen matching. For each fixed B input there is at most one forbidden compressed output for bridge 10. Choosing the artificial matching equal to its forbidden endpoint pairing makes that union disconnected, forcing a positive output. This covers every $c\ge5$. The independently checked B kernels cover all small-crossing inputs except twelve one-crossing and one three-crossing B partial matching. Complete positive cycles close all those residual inputs.

## Dependency Map

1. N14 supplies the A forests and compatibility with every prescribed artificial matching.
2. The balanced table has one exact forbidden output for bridge 10.
3. The small-crossing independent enumeration supplies complete exceptional B lists.
4. New residual certificates and `verify_t15_core15_residual.cpp` cover every complete matching over those exceptional inputs.

## Proof

### Step 1. Artificial boundary matchings and N14

Let $z\in\{10,15\}$, and put $E=X_A\cup\{z\}$. For every perfect matching $D$ on $E$, the matching $F_A\cup D$ has exactly the two even local holes $0$ and the other retained A hole. N14 gives a 15-cycle on $A-0$ containing it. Delete $D$. The remainder is a spanning path forest whose endpoint pairing is a perfect matching $R$ on $E$.

The multigraph $D\cup R$ is connected: compression of those paths in the original single cycle gives exactly that multigraph. Every artificial edge is deleted, so every remaining edge outside the original matching is short.

### Step 2. The bridge mirror is internal

Suppose $z_B\notin X_B$. Attach the original crossings and the short bridge $z_Az_B$. Let $k=F_B(z)$, and let $q$ be the transported partner of $z_B$ in the forest pairing. Suppress $z_B$, replacing its two incident edges by $kq$. Since $k$ is internally covered and $q$ is a crossing port, they are distinct. The result is a matching $L$ with holes $\{0,7,z,1\}$.

For fixed $F_B$ and $C$, this map from $R$ to $L$ is injective. The edge incident to $k$ in $L$ determines $q$; splitting it through $z_B$, removing the other fixed B edges, and undoing $C$ recovers $R$. Thus bridge $z=10$ has at most one forbidden pairing $R_0$ for every fixed input.

When $c\ge5$, $|E|=c+1\ge6$. If there is a forbidden $R_0$, choose $D=R_0$ in Step 1. Its union with $R_0$ has $(c+1)/2$ separate two-vertex components, so the connected output pairing cannot be $R_0$. If no forbidden output exists, choose any $D$. In either case $L$ is positive.

### Step 3. The bridge mirror is occupied

Suppose $z_B\in X_B$, and set $d=C^{-1}(z_B)$. Because $z$ is an A hole, $d\ne z$. Prescribe $zd$ in $D$, writing $D=\{zd\}\cup D'$ for any matching $D'$ on $X_A-\{d\}$.

In the N14 cycle replace the artificial edge $z_Ad_A$ by the path $z_Az_Bd_A$, using the new short bridge and the original crossing incident to $z_B$. Delete $D'$ and attach all remaining original crossings. For $c\ge3$ the nonempty set $D'$ breaks the cycle into a forest whose interiors cover $(A-0)\cup\{z_B\}$ and whose endpoints are $X_B-\{z_B\}$.

Let $Q$ be the endpoint pairing, pulled back to $X_A-\{d\}$. Its union with $D'$ is connected by compression in the original cycle after replacing $zd$. Its B output is $L=F_B\cup C(Q)$, with holes $\{0,7,z,1\}$. For fixed $F_B,C$ the map from $Q$ to $L$ is injective, since the fixed internal edges and port-pairing edges have disjoint endpoint sets.

For bridge 10 there is at most one forbidden quotient $Q_0$. When $c\ge5$, the quotient boundary has $c-1\ge4$ vertices. If a forbidden quotient exists, choose $D'=Q_0$. Their union has at least two components, so Step 3 cannot produce that forbidden quotient. With none forbidden, choose any $D'$. Thus $L$ is positive.

A positive output in Step 2 or Step 3 has a fourteen-vertex cycle in the audited table. Expand its compressed paths. This adds all fifteen A vertices and $z_B$, gives exactly the required thirty-vertex support, and restores every original matching edge. Disjoint path interiors preserve simplicity; all surviving new edges are short. These steps cover every $c\ge5$.

### Step 4. Three crossings outside the exceptional B input

Each bridge has four endpoint vertices and exactly three possible pairings. At least two pairings are realizable by an A forest: if only $R_0$ were realizable, choosing $D=R_0$ in Step 1 would contradict connectedness.

The independent core-15 B kernel checks all $\binom{13}{3}9!!=270270$ B partial matchings and all six crossing bijections. Except for one B partial matching, every resulting spectrum allows at least two pairings on at least one bridge. These intersect its at least two realizable A pairings, giving a positive output and expanded cycle. The independent checker and producer agree on the entire B spectrum histogram.

The unique exceptional B input is

$$X_B=\{5,10,15\},\qquad F_B=\{(2,4),(3,13),(6,8),(9,11),(12,14)\}.$$

It has zero admissible pairing on both bridges for each crossing bijection. Its $270270$ possible A partial matchings and six arbitrary crossing bijections leave precisely $1621620$ complete residual inputs.

### Step 5. One crossing outside the twelve exceptional B inputs

For one crossing, each bridge has a unique endpoint pairing, which Step 1 realizes. The independent B kernel checks every $13\cdot11!!=135135$ partial matching. Exactly twelve B inputs have neither bridge admissible. They are listed in `t15_r3_small_core15_c1_B_exceptions.txt`; their exact equality with `t15_core15_c1_B_inputs.txt` is checked in the final manifest program.

All other one-crossing inputs therefore have an expanded positive cycle. For each exceptional B input there are $13\cdot11!!=135135$ A partial matchings, leaving exactly $12\cdot135135=1621620$ complete residual inputs.

### Step 6. Complete positive residual certificates

The generic producers `t15_core15_residual_fast.cpp` and `t15_core15_residual_hybrid.cpp` support both crossing counts and every crossing bijection. The hybrid version first tries bounded alternative search orders and then falls back to the full search; the independent checker does not depend on this heuristic. It enumerates the A port subsets in increasing order, all perfect matchings on their remaining covered A vertices, each exceptional B input, and all permutations of its ports. Original matching edges are kept as indivisible blocks during its search. The four retained globally free vertices are singleton blocks.

It emits $1621620$ positive certificates for each crossing count, with zero UNKNOWN and zero exhausted input. The two binary certificate files are `t15_core15_c1_fast.bin` and `t15_core15_c3_hybrid.bin`. Each record stores thirteen required edges followed by thirty cycle vertices, totaling 56 bytes.

`verify_t15_core15_residual.cpp` performs no search. It independently enumerates every expected A port subset, every remaining A matching, and every crossing bijection over each exact exceptional B input. It checks exact equality of the recorded required edges with that reconstructed input; thirty distinct cycle vertices with support exactly $Q_5-\{1,2\}$; presence of all thirteen original matching edges; and Hamming distance one of every other cycle edge. It requires exactly $1621620$ records for each crossing count and rejects trailing bytes.

Both complete independent checks pass, covering $3243240$ original residual matchings. The manifest `T15_CORE15_FULL_CLOSURE_VERIFICATION.json` records the counts, exact binary sizes and SHA-256 values. Correctness depends on these direct certificate checks, not on the producer's search pruning or node cap.

Steps 2--6 exhaust every odd crossing count. Undoing the coordinate swap proves the original marked geometry; cube automorphisms preserve the entire conclusion and give its orbit. ∎

## Reproduction

Compile `t15_core15_residual_fast.cpp` and `verify_t15_core15_residual.cpp` with `g++ -O3 -std=c++17`. Then run for each crossing count $c\in\{1,3\}$:

```powershell
./t15_core15_residual_fast.exe 1 t15_core15_c1_B_inputs.txt t15_core15_c1_fast.bin t15_core15_c1_fast_failures.txt | Out-File -Encoding utf8 t15_core15_c1_fast.json
./verify_t15_core15_residual.exe 1 t15_core15_c1_B_inputs.txt t15_core15_c1_fast.bin | Out-File -Encoding utf8 t15_core15_c1_residual_verification.json
```

For three crossings, compile and use `t15_core15_residual_hybrid.cpp`, argument `3`, and the `t15_core15_c3_hybrid` output prefix; use the corresponding three-crossing B inputs and verifier paths. Finally execute `python verify_t15_core15_table.py` and `python verify_t15_core15_full_closure.py`.

## Corrections or Missing Assumptions

None beyond the explicitly stated imported theorems and audited tables. The large-crossing proof uses a single forbidden output and has no general boundary-blocking lemma or additional finite-basis dependency.

## Open Risks

Fresh overall semantic and finite-input review is required before updating integrated core or parent counts. This package does not claim full T15 or the complete eight-hole layer.
