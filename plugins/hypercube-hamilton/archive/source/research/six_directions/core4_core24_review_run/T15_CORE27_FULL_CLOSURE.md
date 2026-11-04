# T15 core27 candidate proof package

Date: 2026-11-01. ARIS proof-writer. All three residual domains now have complete positive certificates and independent coverage verification. A fresh overall semantic audit is required before integration. No global state or previously reviewed core8/core23 artifact is changed.

## Claim

For every matching $F$ of $K(Q_5)$ with holes $\{0,1,7,26,28,31\}$, there is a simple cycle on exactly $Q_5-\{1,7\}$ containing $F$, whose other edges are short. Original matching edges and crossing bijections are arbitrary. Every cube-automorphic image of this marked geometry is included.

## Status

PROVABLE AS STATED, conditional only on the explicitly retained audited N14 and balanced-table imports. All new finite proof obligations, including every complete residual input, have passed independent checks. This remains a candidate proof pending fresh overall semantic review. Full T15, the full eight-hole layer, and P6 remain outside scope.

## Assumptions

1. Q4 N14, at arbitrary complete-graph matching scope: two same-parity holes permit a simple 15-cycle omitting either specified hole, with short new edges.
2. Complete balanced Q4 tables from `T15_BALANCED_BRIDGE_REVIEW.md/.json`. The $(3,8)$ table has ten exact negatives and $10385$ positives, and $(15,8)$ has fifty negatives and $10345$ positives, each among all $10395$ complete-graph matchings on the twelve covered vertices. Coordinate permutations transport the full tables.

No search exhaustion is used as a negative certificate.

## Notation

Apply the old-to-new global coordinate destination map $(4,0,1,2,3)$. The holes become $H=\{0,13,14,16,19,31\}$ and the omissions become $\{16,19\}$. Label the two faces by $v_A=2v+1$ and $v_B=2v$. Face A has local holes $\{9,6,15\}$ and omits $9_A$; B has holes $\{0,7,8\}$ and omits $8_B$. The retained globally free vertices are $\{0,13,14,31\}$.

Write internal matchings $F_A,F_B$, port sets $X_A,X_B$, and original crossing bijection $C:X_A\to X_B$. Let $c=|C|$ and $m=(13-c)/2$. Both faces have thirteen originally covered vertices, so $c$ is odd from one to thirteen. A bridge is the short edge $z_Az_B$, where $z\in\{6,15\}$.

## Proof Strategy

Apply N14 with an arbitrarily chosen artificial boundary matching. Block all negative output pairings using complete inverse families and explicit disconnection certificates. Bridge 6 closes all $c\ge7$ inputs and all but two B inputs at $c=5$. Complete small-crossing B spectra leave eighty-two B inputs at $c=1$ and twenty-four B inputs at $c=3$. Prove all full residual inputs by positive cycle certificates.

## Dependency Map

N14 gives A forests and connectedness with each chosen artificial pairing. Balanced tables classify their compressed B matchings. Complete inverse enumeration and explicit blockers close larger crossings. Complete B spectra give exact small-crossing residuals. Full positive certificates close the residual domains. No T15, eight-hole, P6, or core27 conclusion is used upstream.

## Proof

### Step 1. N14 boundary pairing and expansion

Fix $z$ and let $w$ be the other retained A hole. Set $E=X_A\cup\{z\}$. For every perfect matching $D$ on $E$, $F_A\cup D$ is a seven-edge matching with exactly the two local even holes $9,w$. N14 gives a simple cycle on $A-9$ containing it. Delete $D$. Since its edges are nonempty and vertex-disjoint, the result is a spanning path forest. Its endpoint pairing $R$ satisfies that $D\cup R$ is connected: contraction of the paths recovers the original single cycle. All surviving edges outside $F_A$ are short.

If $z_B$ is internal, attach all original crossings and the short bridge. Let $k=F_B(z)$ and let $q$ be the transported partner of $z$. Since $k$ is internally covered and $q$ is a port, $k\ne q$. Suppress $z_B$ to replace its incident path and $kz$ by $kq$. The resulting matching $L$ has holes $\{0,7,z,8\}$. This operation is invertible for fixed $F_B,C$.

If $z_B$ is occupied and $c\ge3$, let $d=C^{-1}(z_B)$ and prescribe $zd\in D$, with $D=\{zd\}\cup D'$. Replace $zd$ in the N14 cycle by $z_Az_Bd_A$, using the bridge and the original crossing. Delete the nonempty $D'$ and attach the other original crossings. This gives a path forest with interiors $(A-9)\cup\{z_B\}$ and boundary $X_B-\{z_B\}$. Its pairing $Q$ has connected union with the transported $D'$. The compressed matching is $L=F_B\cup Q$.

For positive $L$, replace its compressed edges in the balanced fourteen-vertex B cycle by the recorded forest paths. The paths have mutually disjoint interiors disjoint from those fourteen vertices. Expansion adds fifteen A vertices and $z_B$, giving a simple thirty-vertex cycle. Every original edge survives, including a suppressed original $kz$ and all crossings; artificial D edges are deleted, compressed edges are expanded, and all remaining added edges are short.

### Step 2. Complete bridge-6 blockers

The local destination permutation $(1,2,0,3)$ fixes B holes $0,7,8$ and sends bridge 3 to 6. It transports the full negative table and boundary data. This only transports a B kernel; it does not identify the entire A geometry with core23.

For each negative $L$, occupied-mode inverses choose every $m$-edge subset $J\subseteq L$ and set $F_B=J$, $Q=L-J$. Internal-mode inverses choose every oriented edge $kq$ of $L$ and every $(m-1)$-edge subset $J\subseteq L-\{kq\}$, and set

$$F_B=J\cup\{6k\},\qquad R_B=(L-J-\{kq\})\cup\{6q\}.$$

These formulas invert Step 1 in both directions, so no negative endpoint pairing can be missed for any fixed actual $F_B$. An absent $F_B$ has no negative output. Arbitrary $C$ merely relabels the boundary and preserves connectedness; no A matching or edge-length restriction is used to discard an output.

`verify_t15_core27_blockers.py` independently extracts the ten negative raw $(3,8)$ entries, transports them, rebuilds all inverse families, compares exact sets with `r3_boundary_blocking_6_8.json`, validates supports, and checks every explicit blocker against every forbidden pairing by graph traversal. The checked counts are:

| $c$ | internal families/blockers | occupied families/blockers |
|---:|---:|---:|
|5|1080/1080|146/144|
|7|856/856|180/180|
|9|240/240|107/107|
|11|12/12|24/24|
|13|impossible|1/1|

All $2644$ explicit blockers pass. Pull back a blocker through $C$ and choose it as $D$ or $D'$ in Step 1. Every forbidden output has disconnected union with it, whereas N14 provides an output with connected union. That output is therefore positive. The order of quantifiers is preserved: choose the artificial pairing from the actual B data, then obtain some A forest from N14.

Only two occupied $c=5$ B inputs remain:

$$\{(1,2),(3,5),(10,13),(12,14)\},\qquad
\{(1,4),(3,5),(10,14),(11,12)\}.$$

Their ports are $\{4,6,9,11,15\}$ and $\{2,6,9,13,15\}$. Each unblocked four-endpoint family contains all three possible pairings, checked directly. Both have bridge 15 occupied too. They are retained in Step 5; no bridge-15 blocker table or failed-search inference is needed.

### Step 3. Complete small-crossing kernels

For $c=3$, a bridge has three pairings on $X_A\cup\{z\}$. At least two are realizable: if only $R_0$ were realizable, applying N14 with $D=R_0$ would give two disconnected doubled edges rather than a connected union. For $c=1$, its unique pairing is realized by N14.

Transport each candidate A pairing into B and add it to $F_B$ as a multigraph. Reject a self-loop or closed component; otherwise trace paths from degree-one endpoints and compress to $L$. B-admissibility means this $L$ is positive. This definition explicitly handles occupied mirrors, including the rejected self-loop for occupied $c=1$; its pairings remain the original A pairings, not the smaller occupied quotient pairing set.

`verify_t15_core27_B.cpp` reads the thirteen raw audited tables and their coordinate images and reconstructs these graphs. It checks all $135135$ one-crossing B inputs and all $\binom{13}{3}9!!\cdot3!=1621620$ three-crossing B/bijection inputs. Full independent histograms match the producer's.

Exactly eighty-two B inputs fail both bridges at $c=1$. Exactly twenty-four B partial matchings, with all six bijections each, have zero admissible pairing at $c=3$. Every other three-crossing input has at least two admissible pairings at some bridge, intersecting its at-least-two realizable A pairings in the same three-element set. That intersection and Step 1 close every such input.

### Step 4. Exact remaining finite domains

`t15_core27_c1_B_inputs.txt`, `t15_core27_c3_B_inputs.txt`, and `t15_core27_c5_B_inputs.txt` have respectively 82, 24, and 2 B inputs. The first two equal the complete independently regenerated exception lists; the last is exactly the two unblocked inputs in Step 2. Input supports and absence of duplicate rows are checked.

For each fixed B input there are $\binom{13}{c}(12-c)!!$ A partial matchings and $c!$ crossing bijections. Thus the exact residual sizes are:

| $c$ | B inputs | A partial matchings | Bijections | Complete inputs |
|---:|---:|---:|---:|---:|
|1|82|135135|1|11081070|
|3|24|270270|6|38918880|
|5|2|135135|120|32432400|

Their total is $82432350$ original matchings, including A port zero wherever it occurs.

### Step 5. Complete positive certificates and independent verifier

The generic producer `t15_residual_fast.cpp`, with geometry arguments $9,6,15,8$, treats thirteen original matching edges as indivisible blocks and the retained holes $0,13,14,31$ as singleton blocks. It links blocks by short edges. A positive record consists of thirteen required edges followed by thirty cycle vertices, totaling 56 bytes. Search caps are irrelevant to acceptance; every input must have a positive cycle.

The separate search-free verifier `verify_t15_residual_rank.cpp` checks that each required matching covers exactly $Q_5-H$, has the specified B input and $c$ crossings, and derives an independent dense index. It uses the A port subset's combinadic rank, the internal matching's recursive least-partner rank, the B input index, and the crossing bijection's permutation rank. A bitmap rejects duplicates and must be entirely filled. This proves coverage without reproducing the producer's enumeration order.

Every cycle is checked for thirty distinct vertices on exactly $Q_5-\{16,19\}$, inclusion of all thirteen original edges, and Hamming distance one of every other edge. Exact record count and EOF exclude missing, partial, or extra records. All $82432350$ complete residual inputs have positive cycles, zero UNKNOWN and zero exhausted inputs; all three independent rank-bitmap verifications pass. The complete binary size is $4616211600$ bytes across `t15_core27_c1_residual.bin`, `t15_core27_c3_residual.bin`, and `t15_core27_c5_residual.bin`. The aggregate checker `verify_t15_core27_full_closure.py` requires all expected positive records, no UNKNOWN/exhausted input, exact independently verified coverage, reduction-list equality, import-hash equality, and geometry checks before emitting `T15_CORE27_FULL_CLOSURE_VERIFICATION.json`.

Steps 2–5 therefore cover every odd crossing count. Undo the global coordinate permutation and transport by cube automorphisms to conclude the original claim with all original edges retained and only short new edges. ∎

## Reproduction

Compile `t15_residual_fast.cpp` and `verify_t15_residual_rank.cpp` with `g++ -O3 -std=c++17`; `-march=native` is optional for the producer. For each $c=1,3,5$, use `t15_residual_fast.exe <c> t15_core27_c<c>_B_inputs.txt t15_core27_c<c>_residual.bin t15_core27_c<c>_residual_failures.txt 0 9 6 15 8`. Zero requests the full domain. Verify with `verify_t15_residual_rank.exe <c> t15_core27_c<c>_B_inputs.txt t15_core27_c<c>_residual.bin 9 6 15 8`. Save JSON stdout to the corresponding residual and verification JSON files. Run the B graph checker, blocker checker, and aggregate checker as named above.

The bounded pilots each covered $100000$ inputs, all positive and no UNKNOWN, taking approximately 1.4–1.6 seconds locally. Full enumeration was chosen from this measured cost. Pilot success does not establish universal coverage.

## Corrections or Missing Assumptions

Only the explicitly retained N14 and balanced imports are intended as assumptions. All failed-bridge cases remain in the exact finite positive-certificate domains.

## Open Risks

The full finite package has passed. A fresh overall semantic review is required before integration; no independent overall acceptance is claimed here. Full T15, the full eight-hole layer, and P6 remain unproved by this package.
