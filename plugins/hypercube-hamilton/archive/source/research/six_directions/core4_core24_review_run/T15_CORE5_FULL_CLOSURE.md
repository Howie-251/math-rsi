# Complete T15 core 5

Date: 2026-11-01. ARIS proof-writer. Complete candidate proof for one marked core; fresh independent overall review pending. Full T15 and the full eight-hole layer remain unproved by this package.

## Claim

Let $F$ be any matching of $K(Q_5)$ whose holes are $\{0,1,2,7,13,14\}$. There is a simple cycle on $Q_5-\{1,2\}$ containing every edge of $F$, with every new edge a cube edge. All cube-automorphic images of this marked geometry are included. Original matching edges may have arbitrary length and parity.

## Status

PROVABLE AS STATED, with the explicitly retained previously audited N14 and balanced-table imports below. The new finite checks, including every residual positive cycle, pass. A fresh review of this complete package is requested before integration.

## Assumptions

1. Q4 N14: every arbitrary complete-graph matching with two holes of the same parity extends to a 15-cycle omitting either specified hole, using short new edges.
2. The audited complete balanced Q4 tables, each covering all $10395$ complete-graph matchings on twelve covered vertices. See `T15_BALANCED_BRIDGE_REVIEW.md/.json`.
3. The already independently checked small-crossing kernels in `T15_R3_SMALL_CROSSING_PROGRESS.md` and `t15_r3_small_verification.json`. Their core-5 statements are independently checked exhaustive $B$ computations, rather than an assumed full T15 result.

## Notation and normalized geometry

Cut coordinate zero. A vertex $v_A$ has global label $2v+1$ and a vertex $v_B$ has global label $2v$. Thus $A$ has holes $\{0,3,6\}$ and omits $0_A$; $B$ has holes $\{0,7,1\}$ and omits $1_B$. These are exactly the displayed original global holes and omissions; no additional normalization is assumed.

Write $F_A,F_B$ for the internal matching edges, $X_A,X_B$ for the crossing ports, $C:X_A\to X_B$ for the arbitrary original crossing bijection, and $c=|C|$. Each face has thirteen originally covered vertices. Therefore $c$ is odd, $1\le c\le13$, and each internal matching has $(13-c)/2$ edges.

We use the bridge label $z=6$ except in the already checked small-crossing kernels, which permit either $z=3$ or $z=6$. The complete balanced table for holes $\{0,7,6,1\}$, omitting $6,1$, has exactly two negative matchings. It is the coordinate image of `q4_balanced_two_avoided_3_4.bin`. The table for bridge $3$ has three negative matchings.

## Proof Strategy

N14 supplies a boundary pairing compatible with every artificially chosen boundary matching. A boundary matching can be deliberately chosen to exclude a small forbidden set. Two forbidden pairings on at least six boundary vertices can be excluded by an elementary shared-edge argument. Only $c=1,3$, and an occupied bridge at $c=5$, require additional finite inputs. The three-crossing kernel is already complete. Five one-crossing exceptional $B$ inputs are closed by $675675$ independently verified explicit cycles. The occupied five-crossing inverse kernel has at most one forbidden quotient for every fixed $B$ input.

## Dependency Map

1. N14 gives every needed $A$ forest and the connectedness of its induced boundary pairing with the chosen artificial pairing.
2. The exact balanced tables classify the compressed $B$ matchings.
3. The two-pairing exclusion lemma below closes every $c\ge7$ and the internal-bridge case at $c=5$; it has no finite computational dependency.
4. `verify_t15_core5_c5_inverse.py` checks the thirty nonempty inverse cases for an occupied bridge at $c=5$ directly from the audited raw tables.
5. The independently checked core-5 $c=3$ kernel and the new one-crossing residual certificates close the remaining cases.

## Proof

### Step 1. Boundary pairings supplied by N14

Fix $z\in\{3,6\}$ and put $E=X_A\cup\{z\}$. For every perfect matching $D$ on $E$, the matching $F_A\cup D$ has exactly the two same-parity holes $0$ and the other retained $A$ hole. N14 supplies a 15-cycle on $A-0$ containing that matching. Delete all edges of $D$. This gives a spanning path forest whose endpoints are $E$ and whose endpoint pairing is a perfect matching $R$ on $E$.

The multigraph $D\cup R$ is connected: compressing the forest paths in the original single cycle produces that multigraph. Every non-original edge surviving in the forest is short. The path interiors are disjoint and exhaust the other vertices of $A-0$.

### Step 2. An internal bridge mirror

Suppose $z_B\notin X_B$. Attach the original crossings and the short bridge $z_Az_B$ to the forest. Its endpoint pairing is transported to $X_B\cup\{z_B\}$. Let $k=F_B(z)$ and let $q$ be the transported partner of $z_B$. Suppress $z_B$, replacing the two incident edges by $kq$.

The vertex $k$ is internally covered whereas $q$ is a crossing port, so they are distinct. The resulting $L$ is a matching on $B-\{0,7,1,z\}$. For fixed $F_B$ and $C$, the map $R\mapsto L$ is injective: replace the edge of $L$ incident to $k$ by the two-edge path through $z_B$, remove the other fixed internal edges, and pull endpoint labels back through $C$. Hence at most two boundary pairings $R$ are bad when $z=6$.

If $L$ is positive, expand its fourteen-vertex cycle by restoring the suppressed paths. This restores $z_B$ and all fifteen $A-0$ vertices, yielding one simple thirty-vertex cycle. Every original matching edge is restored, all artificial edges are gone, and every new edge is short.

### Step 3. An occupied bridge mirror

Suppose $z_B\in X_B$, and write $d=C^{-1}(z_B)$. Since $z$ is an $A$ hole, $d\ne z$. Prescribe the edge $zd$ in $D$ and write $D=\{zd\}\cup D'$, where $D'$ is any perfect matching on $X_A-\{d\}$.

In the N14 cycle replace the artificial edge $z_Ad_A$ by the path $z_Az_Bd_A$. This uses the new short bridge and the original crossing incident to $z_B$. Delete $D'$ and attach every other original crossing. When $c\ge3$, the nonempty set $D'$ breaks the cycle into a forest whose interiors cover $(A-0)\cup\{z_B\}$ and whose endpoints are $X_B-\{z_B\}$.

Let $Q$ be the endpoint pairing, pulled back to $X_A-\{d\}$. Then $D'\cup Q$ is connected, by compressing these forest paths in the cycle before deletion of $D'$. The matching $L=F_B\cup C(Q)$ has holes $\{0,7,1,z\}$. For fixed $F_B,C$, its dependence on $Q$ is injective, because $F_B$ covers precisely the internally covered vertices and the quotient pairing covers precisely the remaining ports. Thus at most two $Q$ are bad for bridge $6$. Any positive $L$ expands to the required thirty-vertex cycle.

### Step 4. Excluding two bad pairings on at least six vertices

Let $V$ have even size $N\ge6$, and let at most two perfect matchings $R_1,R_2$ be forbidden. With no forbidden matching, choose any perfect matching $D$. With one forbidden matching, choose one of its edges and extend it to $D$. Then $D\cup R_1$ has an isolated two-vertex component.

With two forbidden matchings, choose an edge $e_1$ of $R_1$. At most two edges of $R_2$ meet its endpoints. Since $R_2$ has at least three edges, it has an edge $e_2$ disjoint from $e_1$. Extend the two disjoint edges to a perfect matching $D$. For each $i$, the shared edge $e_i$ is an isolated two-vertex component of $D\cup R_i$. Because $N>2$, both unions are disconnected. This proves the exclusion lemma without a computational basis or a third-matching lemma.

### Step 5. Every $c\ge7$, and an internal mirror at $c=5$

Always choose bridge $z=6$. If its mirror is internal and $c\ge5$, the boundary set has $c+1\ge6$ vertices. Step 2 gives at most two forbidden $R$. Choose $D$ by Step 4 to disconnect it from each forbidden $R$. Step 1 must produce a connected union, so its output is not forbidden. It therefore gives a positive $L$ and the required expanded cycle.

If its mirror is occupied and $c\ge7$, the quotient boundary has $c-1\ge6$ vertices. Step 3 gives at most two forbidden $Q$. Choose $D'$ by Step 4, and then apply Step 3. Connectedness again excludes every forbidden output. This closes all crossing counts at least seven.

### Step 6. The occupied mirror at $c=5$

Here $F_B$ has four edges, and the quotient $Q$ is one of the three perfect matchings on four port vertices. A negative $L=F_B\cup C(Q)$ must be one of the two exact negatives of the bridge-6 table. Conversely, every such decomposition is obtained by choosing two of the six edges of a negative $L$ as $C(Q)$ and keeping the other four as $F_B$. There are only $2\binom62=30$ choices before deduplication.

The independent program `verify_t15_core5_c5_inverse.py` reads the audited raw table, applies all relevant coordinate permutations and checks their consistency, verifies that exactly two negatives occur, generates all thirty inverse inputs, and then explicitly checks all three quotient pairings on each resulting four-port boundary. It finds thirty distinct $B$ partial matchings, each with exactly one negative quotient. The full cases and the PASS report are in `t15_core5_c5_inverse_verification.json`. This independently confirms the earlier producer `t15_r3_c5_negative_kernels.py/.json` for the bridge used here.

For any fixed $F_B,C$, there is consequently at most one bad quotient $Q_0$ on $X_A-\{d\}$. If there is none, choose any $D'$. Otherwise choose $D'=Q_0$. The multigraph $D'\cup Q_0$ has two components, since it consists of two duplicated matching edges on four vertices. Step 3 supplies an output $Q$ with $D'\cup Q$ connected; therefore $Q\ne Q_0$, and $L$ is positive. This closes the occupied case at five crossings.

### Step 7. Three crossings

The independently checked core-5 profile in `T15_R3_SMALL_CROSSING_PROGRESS.md` has $270270$ possible $B$ partial matchings and six arbitrary crossing bijections, for $1621620$ inputs. Its complete $B$ spectrum has no zero case, and every spectrum has a bridge allowing at least two of the three pairings on its four endpoints. The independent graph-compression checker and producer agree on the entire histogram, as recorded in `t15_r3_small_verification.json`.

For each bridge, N14 implies at least two realizable $A$ pairings: if only one pairing $R_0$ were realizable, applying Step 1 with $D=R_0$ would give the disconnected union of a pairing with itself, contradicting connectedness. Thus the realizable and admissible sets intersect on the bridge selected by the $B$ kernel. Their common pairing expands to the required cycle. This closes all three-crossing inputs without enumerating the $A$ matchings as a proof dependency.

### Step 8. One crossing and the five exceptional B inputs

For one crossing, each bridge has a unique endpoint pairing, and Step 1 realizes it. The complete independent $B$ enumeration in the small-crossing package checks all $135135$ partial matchings. Exactly five have neither bridge admissible. The five exceptional inputs, with sole port followed by six internal edges, are:

```text
3 : 2-4 5-6 8-10 9-11 12-14 13-15
3 : 2-4 5-6 8-12 9-13 10-14 11-15
6 : 2-4 3-5 8-12 9-11 10-13 14-15
6 : 2-4 3-5 8-14 9-11 10-13 12-15
6 : 2-4 3-5 8-15 9-11 10-13 12-14
```

They are saved independently as `t15_r3_small_core5_c1_B_exceptions.txt`, and the search uses the exactly equal list `t15_core5_c1_B_inputs.txt`. Every other one-crossing input is already solved by its admissible bridge.

For each exceptional $B$ input, the $A$ crossing port has thirteen possibilities and the other twelve covered vertices have $11!!=10395$ internal matchings. Thus exactly $5\cdot13\cdot10395=675675$ complete residual matchings remain.

### Step 9. Independently checked cycles for every one-crossing residual

`t15_core5_c1_residual.cpp` enumerates every residual matching and emits its thirteen required edges followed by a thirty-vertex cycle. The saved result has $675675$ positives and no unknown or exhausted input.

`verify_t15_core5_c1_residual.cpp` performs no search. It independently enumerates every expected residual input and checks exact agreement with the required edges recorded in each 56-byte record. It verifies thirty distinct cycle vertices with support exactly $Q_5-\{1,2\}$, presence of every original required edge, and Hamming distance one of every other cycle edge. It asserts exactly $675675$ records and rejects trailing bytes. All these checks pass. See `t15_core5_c1_residual_verification.json` and the combined `T15_CORE5_FULL_CLOSURE_VERIFICATION.json` for the exact binary size and SHA-256.

The free retained vertices in these global labels are $0,7,13,14$, which the producer leaves as singleton blocks. All thirteen original matching edges are preserved as indivisible blocks during the search. The independent verifier checks the resulting cycles directly, so correctness does not depend on trusting the search strategy.

The odd crossing counts $1,3,5,7,9,11,13$ have now all been exhausted. The required thirty-vertex cycle exists for every matching in the displayed core-5 geometry. Cube automorphisms preserve matching incidence, prescribed holes, cycle simplicity and shortness of new edges, proving the claimed orbit statement. ∎

## Reproduction

Compile the two new C++ programs with `g++ -O3 -std=c++17`, then run:

```powershell
./t15_core5_c1_residual.exe t15_core5_c1_B_inputs.txt t15_core5_c1_residual.bin t15_core5_c1_residual_failures.txt | Out-File -Encoding utf8 t15_core5_c1_residual.json
./verify_t15_core5_c1_residual.exe t15_core5_c1_B_inputs.txt t15_core5_c1_residual.bin | Out-File -Encoding utf8 t15_core5_c1_residual_verification.json
python verify_t15_core5_c5_inverse.py
python verify_t15_core5_full_closure.py
```

The small-crossing B verifier and its reproduction commands are documented in `T15_R3_SMALL_CROSSING_PROGRESS.md`. Previously submitted proof and checker files were not edited to produce this package.

## Corrections or Missing Assumptions

None beyond the explicitly stated N14 and audited balanced-table imports. The two-pairing exclusion proof avoids any dependence on the separate three-pairing finite lemma.

## Open Risks

The new complete-core proof should receive a fresh semantic and finite-input audit before being promoted to integrated status. This file does not itself update parent orbit counts or claim a full eight-hole theorem.
