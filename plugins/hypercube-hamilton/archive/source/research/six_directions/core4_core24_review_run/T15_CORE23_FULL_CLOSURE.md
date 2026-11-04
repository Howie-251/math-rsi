# Complete T15 core 23

Date: 2026-11-01. ARIS proof-writer. Complete candidate proof for one marked core. Fresh overall independent review remains required before integration. Full T15 and the full eight-hole layer are not asserted.

## Claim

Let $F$ be any matching of $K(Q_5)$ with holes $\{0,1,7,14,22,26\}$. There is a simple cycle on $Q_5-\{1,7\}$ containing every edge of $F$, whose new edges are cube edges. The claim includes every cube-automorphic image of this marked geometry. There is no restriction on the lengths or parity types of original matching edges.

## Status

PROVABLE AS STATED, conditional on the explicitly retained previously audited N14 and balanced-table imports. All new finite kernels and positive residual certificates have independent checkers. This is a candidate complete-core package awaiting a fresh overall proof audit.

## Assumptions

1. Q4 N14, in its arbitrary complete-graph matching scope: two same-parity holes permit a 15-cycle omitting either specified hole, with short added edges.
2. The complete independently audited balanced Q4 tables, each covering all $10395$ matchings on twelve vertices. The bridge geometry used here has holes $\{0,7,3,8\}$, omitting $3,8$, and exactly ten negatives. See `T15_BALANCED_BRIDGE_REVIEW.md/.json`.
3. The independently checked small-crossing $B$ kernels in `T15_R3_SMALL_CROSSING_PROGRESS.md` and `t15_r3_small_verification.json`.

## Notation and normalized geometry

Permute the original five coordinates by the old-to-new destination map $(4,1,0,2,3)$. This sends the original holes to $\{0,7,11,14,16,19\}$ and the prescribed omissions to $16,19$. In these global labels, write $v_A=2v+1$ and $v_B=2v$. Face $A$ has holes $\{9,3,5\}$ and omits $9_A$; face $B$ has holes $\{0,7,8\}$ and omits $8_B$. The four retained globally free vertices are $0,7,11,14$.

Let $F_A,F_B$ be the internal matchings, let $X_A,X_B$ be the port sets, and let $C:X_A\to X_B$ be the arbitrary original crossing bijection. Write $c=|C|$ and $m=(13-c)/2$. Both faces have thirteen originally covered vertices, so $c$ is odd and lies between one and thirteen.

For $z\in\{3,5\}$ the new short edge $z_Az_B$ is called the bridge. A negative output is an exact negative entry of the audited balanced table with holes $\{0,7,z,8\}$ and omissions $z,8$.

## Proof Strategy

Apply N14 after adding any chosen artificial matching on the boundary endpoints. Its resulting path pairing must have connected union with the chosen artificial matching. Exact inverse enumeration from the ten negative $B$ outputs gives every possible forbidden endpoint-pairing family. Explicit saved boundary matchings disconnect all forbidden outputs, forcing N14 to produce a positive output. Two five-crossing occupied cases require switching bridge. The three-crossing case is already uniformly closed by its independently checked kernel. Twenty one-crossing exceptional $B$ inputs are closed by complete positive-cycle certificates.

## Dependency Map

1. N14 gives the $A$ forests and the crucial connectedness with every chosen artificial pairing.
2. The audited balanced table classifies their compressed $B$ outputs.
3. `r3_boundary_blocking_3_8.json` supplies finite inverse families and explicit blockers.
4. `verify_t15_core23_blockers.py` independently verifies the completeness of every family and every explicit blocker, using ordinary graph traversal.
5. The small-crossing independent kernel closes $c=3$ and reduces $c=1$ to twenty $B$ inputs.
6. `verify_t15_core23_c1_residual.cpp` independently checks every complete residual input and its saved cycle.

## Proof

### Step 1. N14 with an arbitrary artificial boundary matching

Choose $z\in\{3,5\}$ and let $E=X_A\cup\{z\}$. For any perfect matching $D$ on $E$, the matching $F_A\cup D$ has the two even local holes $9$ and the other retained $A$ hole. N14 gives a 15-cycle on $A-9$ containing it. Delete $D$. The remainder is a spanning path forest on $A-9$, containing $F_A$, whose endpoint pairing is a perfect matching $R$ on $E$.

Compressing its paths in the original single cycle proves that $D\cup R$ is connected. All auxiliary edges $D$ have been deleted, so every surviving edge outside the original matching is short.

If $z_B$ is internal in $F_B$, attach all original crossings and the short bridge. Transport the forest endpoints to $X_B\cup\{z_B\}$. Put $k=F_B(z)$, and let $q$ be the transported partner of $z_B$. Suppressing $z_B$ replaces its two incident edges by $kq$. Because $k$ is internally covered and $q$ is a port, they are distinct. The resulting matching $L$ has holes $\{0,7,z,8\}$. Inverting this operation recovers the endpoint pairing uniquely for fixed $F_B,C$.

If $z_B$ is a port, let $d=C^{-1}(z_B)$ and prescribe $zd$ in $D$. Write $D=\{zd\}\cup D'$ on the remaining port set $X_A-\{d\}$. Replace the artificial edge $zd$ in the N14 cycle by the two-edge path $z_Az_Bd_A$, using the short bridge and the original crossing. Delete $D'$ and attach the other original crossings. When $c\ge3$, the nonempty set $D'$ breaks the cycle into a spanning path forest. Its interiors cover $(A-9)\cup\{z_B\}$, and its endpoint set is $X_B-\{z_B\}$.

Write $Q$ for its endpoint pairing in $B$ labels. It has connected union with the transported $D'$, because compression of its paths recovers the same single cycle. Its compressed output is $L=F_B\cup Q$, with holes $\{0,7,z,8\}$.

In either case a positive $L$ has a fourteen-vertex cycle in the audited table. Expanding the compressed paths adds the fifteen $A-9$ vertices and $z_B$, giving a simple thirty-vertex cycle. Expansion preserves all original edges, and every surviving added edge is short. The path interiors are disjoint, so simplicity is preserved.

### Step 2. Complete inverse families for a fixed B matching

First use bridge $z=3$. Let $L$ range over all ten exact negative matchings in its table.

For an occupied bridge, every negative decomposition is $L=F_B\cup Q$. Thus, for the given internal edge count $m$, select any $m$ edges $J$ of $L$. Set $F_B=J$ and $Q=L-J$. This enumerates every bad quotient family for every fixed internal matching. There is no edge-length restriction on $J$.

For an internal bridge, write $k=F_B(z)$ and let $q=L(k)$. The edge $kq$ belongs to $L$. The remaining $m-1$ internal edges form a subset $J\subseteq L-\{kq\}$. Conversely every choice of an oriented edge $kq$ of $L$ and such a subset gives

$$F_B=J\cup\{zk\},\qquad R_B=(L-J-\{kq\})\cup\{zq\}.$$

Here $R_B$ is the transported forest endpoint pairing on $X_B\cup\{z\}$. This is exactly the inverse of the suppression in Step 1. Hence all forbidden outputs are enumerated, and none are discarded according to a heuristic about an $A$ matching.

If a fixed actual $F_B$ is absent from an inverse list, it admits no negative output in that mode. If it occurs, the list contains its full forbidden output family. The arbitrary crossing bijection simply relabels the boundary; it changes neither completeness nor connectedness.

### Step 3. Independent verification of the saved blockers

`verify_t15_core23_blockers.py` reads the audited raw `q4_balanced_two_avoided_3_8.bin`, verifies its size and extracts exactly ten negative matchings. It independently constructs all families in Step 2 for every odd $c\ge5$. It checks exact equality with all saved families and bad-output sets in `r3_boundary_blocking_3_8.json`, checks matching validity and the precise boundary support, and checks every explicit blocking pairing by ordinary graph traversal of its union with every forbidden output. It does not call the producer's pairing search or its alternating-permutation connectivity test.

The resulting complete counts are:

| $c$ | mode | inverse families | explicit blockers | unblocked families |
|---:|:---|---:|---:|---:|
|5|internal|1080|1080|0|
|5|occupied|146|144|2|
|7|internal|856|856|0|
|7|occupied|180|180|0|
|9|internal|240|240|0|
|9|occupied|107|107|0|
|11|internal|12|12|0|
|11|occupied|24|24|0|
|13|occupied|1|1|0|

There is no internal case when $c=13$, because then every covered $B$ vertex is a port. All $2644$ explicit blockers pass. The two unblocked four-vertex families each contain all three possible pairings; the checker verifies this fact directly. The exact PASS report is `t15_core23_blockers_verification.json`.

For an internal actual input, pull its saved blocking pairing on $X_B\cup\{z\}$ back through the crossing bijection, with $z_B$ sent to $z_A$, and choose this as $D$. Its union with every forbidden $R$ is disconnected. Step 1 supplies an $R$ with connected union, so that output cannot be forbidden. For an occupied input choose the transported saved blocker as $D'$ and apply the same argument to $Q$. This proves every $c\ge7$ input and every internal bridge case at $c=5$.

### Step 4. The occupied five-crossing exceptions

The only unblocked bridge-3 internal matchings at $c=5$ are

$$\{(1,4),(5,6),(9,14),(10,11)\},\qquad\{(2,4),(5,6),(9,11),(10,13)\}.$$

Each ordered-looking pair denotes its unordered edge. The same exact machine-readable edge lists are in `t15_core23_blockers_verification.json`.

Swap local coordinates one and two. This fixes $0,7,8,9$ and swaps the retained $A$ holes $3,5$. Thus it preserves the entire marked core and converts the bridge-3 result to the bridge-5 result. The transformed exceptional $F_B$ sets are disjoint from the original two sets. The independent checker explicitly verifies this empty intersection and exact agreement with the core-23 part of `t15_r3_c5_negative_kernels.json`.

For an actual five-crossing input, if either bridge is internal, Step 3 applies after this symmetry if necessary. If both bridges are occupied, the same $F_B$ cannot belong to both unblocked lists, so at least one bridge has a certified blocker. Choose it and apply Step 3. This closes all five-crossing inputs.

### Step 5. Three crossings

For any bridge, its four endpoint vertices have exactly three possible pairings. At least two pairings are realizable by an $A$ forest from N14: if only $R_0$ were realizable, choosing $D=R_0$ in Step 1 would force the disconnected union of a matching with itself, contradicting connectedness.

The independent small-crossing check for core 23 enumerates all $\binom{13}{3}9!!=270270$ possible $B$ partial matchings and all six crossing bijections, totaling $1621620$ inputs. Every input has a bridge allowing at least two of the three pairings. There are no zero spectra, and the complete independent and producer histograms agree. See `t15_r3_small_verification.json`.

Two subsets of size at least two of a three-element set intersect. Choosing a common realizable and admissible pairing on the indicated bridge gives a positive $L$ and the expanded cycle from Step 1. This closes all three-crossing inputs without dependence on enumerating $A$ partial matchings.

### Step 6. One crossing and complete positive residual certificates

For one crossing the endpoint pairing at each bridge is unique, and N14 realizes it. The independent small-crossing $B$ checker enumerates all $13\cdot11!!=135135$ partial matchings. Exactly twenty have neither bridge admissible. They are saved in `t15_r3_small_core23_c1_B_exceptions.txt`; the certificate input list `t15_core23_c1_B_inputs.txt` is checked to be exactly equal to it.

For each exceptional $B$ input, the $A$ port has thirteen choices in $\{0,\ldots,15\}-\{9,3,5\}$, including vertex zero. The other twelve covered vertices have $11!!=10395$ internal matchings. Thus precisely $20\cdot13\cdot10395=2702700$ complete residual inputs remain.

`t15_core23_c1_residual.cpp` enumerates these inputs, keeps every original matching edge as an indivisible block, and saves a positive cycle for each input. There are no UNKNOWN or exhausted residual inputs.

`verify_t15_core23_c1_residual.cpp` performs no search. It independently reconstructs every expected residual input, including port zero, and checks its exact equality with the thirteen required edges recorded in each 56-byte certificate. It verifies thirty distinct cycle vertices, support exactly $Q_5-\{16,19\}$, presence of all original matching edges, and Hamming distance one for every other cycle edge. It requires exactly $2702700$ records and no trailing bytes. The independent verification passes for all records. See `t15_core23_c1_residual_verification.json` and `T15_CORE23_FULL_CLOSURE_VERIFICATION.json` for counts, exact byte size and SHA-256.

Every one-crossing input outside the twenty exceptions already has an admissible bridge, so this exhausts the one-crossing case. Together with Steps 3--5, every possible odd crossing count is covered. Undoing the coordinate permutation proves the original marked claim, and cube automorphisms give its full orbit. ∎

## Reproduction

Compile the two new C++ sources with `g++ -O3 -std=c++17`, then run from this directory:

```powershell
python verify_t15_core23_blockers.py
./t15_core23_c1_residual.exe t15_core23_c1_B_inputs.txt t15_core23_c1_residual.bin t15_core23_c1_residual_failures.txt | Out-File -Encoding utf8 t15_core23_c1_residual.json
./verify_t15_core23_c1_residual.exe t15_core23_c1_B_inputs.txt t15_core23_c1_residual.bin | Out-File -Encoding utf8 t15_core23_c1_residual_verification.json
python verify_t15_core23_full_closure.py
```

## Corrections or Missing Assumptions

None beyond the explicitly stated N14 and audited balanced-table imports. The proof uses complete inverse families and positive blockers, not a failed search as a universal certificate.

## Open Risks

A fresh overall semantic and finite-input review is required before integrating this core into parent counts. This package leaves all other T15 cores and the overall eight-hole theorem outside its claim.
