# Proof Package: r3 small-crossing kernels

Date: 2026-11-01. ARIS proof-writer. This file supplies the complete small-crossing pieces for core 0; it does not claim full T15 or the complete eight-hole layer.

## Claim

Consider an arbitrary complete-graph matching on two adjacent four-dimensional cube faces. In the common local labels, its uncovered vertices are $\{0,3,5\}$ in face $A$ and $\{0,7,1\}$ in face $B$. The prescribed omitted vertices are $0_A$ and $1_B$. If the matching has exactly $c\in\{1,3\}$ crossing edges, it extends to a simple cycle on the other thirty vertices using only short new edges. This is the core-0 profile.

The $c=3$ conclusion also holds for the profiles called cores 5 and 23 below. For the remaining profiles, only the explicitly stated finite reduction is proved here.

## Status

PROVABLE AS STATED for the preceding claim, conditional on the previously imported Q4 N14 theorem and the independently audited complete balanced four-hole tables. Independent checking performed in this work is recorded in `t15_r3_small_verification.json` (PASS). A fresh overall proof review remains appropriate before integration.

## Assumptions

- Q4 N14: every arbitrary complete-graph matching with two holes of the same parity extends to a 15-cycle omitting either specified hole, with short new edges.
- The audited complete Q4 tables for holes $\{0,7,z,y\}$, omitting $z,y$, are exact. Each contains all $11!!=10395$ matchings on the other twelve vertices. See `T15_BALANCED_BRIDGE_REVIEW.md/.json` and `q4_balanced_two_avoided_*_*.bin`.
- The common local labeling preserves short edges and mirrors across the cut. No restriction is imposed on crossing partners or on the lengths of original matching edges.

## Notation

Let $x$ be the omitted $A$ hole, let $r,s$ be its two retained holes, and let $y$ be the omitted $B$ hole. Write $F_A,F_B$ for the two internal matchings, $X_A,X_B$ for their crossing ports, and $C:X_A\to X_B$ for the arbitrary crossing bijection. Both faces have thirteen originally covered vertices. The retained $B$ holes are $0,7$. For a bridge $z\in\{r,s\}$, define $E_z=X_A\cup\{z\}$.

An $A$ pairing is a perfect matching on $E_z$ obtained by compressing the path components of a spanning path forest on $A-x$ that contains $F_A$ and uses short added edges. No cyclic component is permitted in that forest.

## Proof Strategy

For $c=3$, every bridge has at least two realizable $A$ pairings among the three possible pairings. A complete independent finite enumeration shows that every core-0 $B$ input has a bridge permitting at least two of these pairings. The two sets intersect. For $c=1$, the same construction leaves exactly six $B$ inputs; all $6\cdot135135=810810$ complete residual inputs have explicit independently verified thirty-vertex cycles.

## Dependency Map

1. N14 supplies the $A$ path forests and the two-of-three pairing lemma.
2. The audited balanced tables decide which compressed $B$ matchings have the required fourteen-vertex cycle.
3. `verify_t15_r3_small_B.cpp` independently enumerates every $B$ input and reconstructs each compression as a graph.
4. `verify_t15_r3_small_core0_c1_residual.cpp` independently checks both exhaustive residual-input coverage and every saved positive cycle.

## Proof

### Step 1. Pairing abundance for three crossings

Fix a bridge $z$ and suppose $c=3$. There are exactly three perfect matchings on the four vertices of $E_z$. For any such artificial matching $D$, the matching $F_A\cup D$ has precisely the two same-parity holes $x$ and the other retained $A$ hole. N14 gives a 15-cycle omitting $x$. Deleting the two edges of $D$ produces two paths spanning $A-x$, whose endpoint pairing is some $R$ on $E_z$.

The pairing $R$ cannot equal $D$: if equal, restoring the two artificial edges would close each path separately, yielding two components instead of the N14 cycle. If the realizable pairing set were a singleton $\{R_0\}$, applying N14 with $D=R_0$ would contradict this fact. Consequently every bridge has at least two realizable pairings. This argument avoids dependence on the producer's exhaustive $A$ spectra.

For $c=1$, the endpoint set has two vertices and its unique pairing is realized by deleting the single artificial edge supplied to N14.

### Step 2. Exact meaning of an admissible B pairing

Map each endpoint $a\in X_A$ to $C(a)\in X_B$ and map endpoint $z\in E_z$ to the mirror $z_B$. Regard each pair of $R$ as the compression of its corresponding $A$ path with the attached original crossings and the new short bridge $z_Az_B$. Unite these compressed edges with $F_B$ to obtain a multigraph $J$ on $B-\{0,7,y\}$.

Every vertex of $J$ except $z_B$ has degree one and $z_B$ has degree two. Reject a pairing if $J$ contains a closed component, including a loop at $z_B$. Otherwise its path components compress to a perfect matching $L$ on $B-\{0,7,y,z\}$. Its six pairs contain all original $B$ edges not incident to $z$, and the original edge incident to $z$, if present, is recovered by expanding the corresponding path.

Call $R$ admissible if this $L$ is positive in the audited balanced table. Expanding its fourteen-vertex cycle restores all fifteen $A-x$ vertices and $z_B$, giving a simple thirty-vertex cycle. All original matching edges survive; all added edges are short. Distinct path interiors ensure that expansion preserves simplicity.

### Step 3. Complete independent B enumeration

The producer `t15_r3_small_spectra.cpp` enumerates the $B$ partial matchings, all crossing bijections, and all one or three pairings for each of the two bridges. Its implementation explicitly suppresses the degree-two vertex.

The independent checker `verify_t15_r3_small_B.cpp` reads the thirteen original binary tables directly, transforms their exact negative lists under the six coordinate permutations fixing coordinate 3, and covers all 49 marked balanced geometries. It does not read the producer's prepared negative list. It then builds the multigraph $J$, traces all paths from degree-one endpoints, rejects any unvisited closed component, and looks up the resulting endpoint matching. Thus it does not reuse the producer's suppression procedure.

For $c=1$ it checks all $13\cdot11!!=135135$ internal partial matchings. For $c=3$ it checks all $\binom{13}{3}9!!=270270$ internal partial matchings and all $3!=6$ crossing bijections, totaling $1621620$ inputs per profile. The bit positions for $c=3$ are the three pairings $01|23$, $02|13$, $03|12$ on the ordered ports followed by the bridge endpoint, first for $r$ and then for $s$.

`verify_t15_r3_small_results.py` checks exact equality of the complete independent and producer $B$ spectrum histograms. It also checks that each nonzero three-crossing spectrum permits at least two pairings for at least one bridge. For core 0 there are no zero three-crossing spectra. Step 1 and the elementary fact that two subsets of size at least two of a three-element set intersect now prove the entire core-0 $c=3$ case.

### Step 4. Complete core-0 one-crossing reduction

For $c=1$, the unique $A$ pairing works whenever either bridge's corresponding $B$ pairing is admissible. The complete independent enumeration identifies exactly six $B$ inputs with neither bridge admissible. These are saved in `t15_r3_small_core0_c1_B_exceptions.txt`; their equality with the residual search inputs `t15_r3_small_core0_c1_B_inputs.txt` is independently asserted by `verify_t15_r3_small_results.py`.

The six exceptional inputs, each showing its sole port followed by its six internal edges, are:

```text
3 : 2-4 5-6 8-10 9-13 11-12 14-15
3 : 2-4 5-6 8-14 9-13 10-15 11-12
3 : 2-4 5-6 8-15 9-13 10-14 11-12
5 : 2-4 3-6 8-12 9-11 10-13 14-15
5 : 2-4 3-6 8-14 9-11 10-13 12-15
5 : 2-4 3-6 8-15 9-11 10-13 12-14
```

The $A$ crossing port has thirteen possibilities, and the other twelve covered $A$ vertices have $11!!=10395$ internal matchings. Thus these six inputs leave exactly $6\cdot13\cdot10395=810810$ original Q5 matchings.

### Step 5. Positive certificates for every residual matching

Use global labels $2v+1$ for $v_A$ and $2v$ for $v_B$. The omitted vertices are globally $1,2$, and the four retained free vertices are $0,7,11,14$. This label map is a cube isomorphism. Each residual input has thirteen required edges: six internal edges on each face and its sole crossing edge.

`t15_r3_small_core0_c1_residual.cpp` exhaustively emits a certificate for every residual input. The search treats each required edge as an indivisible block and links oriented blocks using short edges. Its finite node cap is irrelevant to acceptance because all inputs succeed: the result is $810810$ positive, zero UNKNOWN, zero exhausted negatives. The maximum visited-node count for any input is $9359$, below the cap of $2000000$.

The independent verifier reconstructs each expected input by independently enumerating all ports and all pairings of the other twelve vertices. Each 56-byte record contains its thirteen required edges followed by thirty cycle vertices. The verifier checks exact equality of the recorded required edges with the independently reconstructed input, uniqueness and exact support of the cycle vertices, presence of all thirteen required edges, and Hamming distance one of every other cycle edge. It asserts exactly $810810$ records and no trailing bytes. These checks pass.

The binary certificate file is `t15_r3_small_core0_c1_residual.bin`, size 45,405,360 bytes, SHA-256 `4764b5f4d0252e5bcfc1a09c87c79a8c86bd1c1c56d88a31b72b323d3c5902b6`.

Steps 1--5 prove both small-crossing cases claimed for core 0. ∎

## Additional finite kernels

The same independent enumeration was completed on all seven requested profiles. In the table, the exceptional count is the number of $B$ partial matchings with zero admissible pairing on both bridges. For three crossings every such partial matching fails for all six crossing bijections; every other input has at least two good pairings on one bridge.

| Core | $x;r,s$ in $A$ | $y$ in $B$ | $c=1$ exceptional B | $c=3$ exceptional B |
|---:|:---|---:|---:|---:|
|0|$0;3,5$|$1$|6|0|
|5|$0;3,6$|$1$|5|0|
|8|$0;3,15$|$1$|22|10|
|15|$0;10,15$|$1$|12|1|
|23|$9;3,5$|$8$|20|0|
|26|$9;3,15$|$8$|82|24|
|27|$9;6,15$|$8$|82|24|

Hence cores 5 and 23 also have complete $c=3$ proofs by Steps 1--3. The full exact exceptional B lists are saved as `t15_r3_small_core<K>_c<C>_B_exceptions.txt`. Those residuals for other cores are not claimed solved here.

## Reproduction

From this directory, compile the three C++ executables with `g++ -O3 -std=c++17` and run:

```powershell
./verify_t15_r3_small_B.exe | Out-File -Encoding utf8 t15_r3_small_B_independent.json
./verify_t15_r3_small_core0_c1_residual.exe t15_r3_small_core0_c1_B_inputs.txt t15_r3_small_core0_c1_residual.bin | Out-File -Encoding utf8 t15_r3_small_core0_c1_residual_verification.json
python verify_t15_r3_small_results.py
```

The producer for any listed profile is `t15_r3_small_spectra.exe <core> <c> <prefix>`. The residual certificate producer takes the exceptional B input path, binary output path, and failure log path as its three arguments.

## Corrections or Missing Assumptions

None for the stated small-crossing claim. This file deliberately does not assert the larger-crossing cases or full T15.

## Open Risks

- The N14 import and the balanced-table audit are external dependencies explicitly retained in the claim.
- Core normalization and integration into the eight-hole parent count require separate review; this package proves the displayed common-label profiles.
- Other cores' exceptional B residuals remain open within this package.
