# Complete T15 core8: candidate proof package

Date: 2026-11-01. ARIS proof-writer. Fresh independent overall proof review is required before integration. This file concerns one marked core only.

## Claim

Let $F$ be any matching of $K(Q_5)$ whose holes are $\{0,1,2,7,13,31\}$. There is a simple cycle with vertex set $Q_5-\{1,2\}$ containing every edge of $F$, with every other edge a cube edge. This includes every cube-automorphic image of the marked geometry. No length or parity restriction is placed on the original matching edges.

## Status

PROVABLE AS STATED, conditional on the explicitly retained previously audited Q4 N14 and complete balanced-table imports, and the finite verification records identified below. This is a complete candidate package, not a fresh independent semantic acceptance. No assertion of full T15, the complete eight-hole layer, or P6 is made.

## Assumptions

1. Q4 N14 in its arbitrary complete-graph matching scope: any matching with two holes of the same parity extends to a simple 15-cycle omitting either designated hole, using short new edges.
2. The complete audited balanced Q4 tables. For holes $\{0,7,z,1\}$ and omissions $z,1$, the bridge $z=3$ table has exactly three negatives, and $z=15$ has exactly ten. Every other matching on the twelve covered vertices has a certified fourteen-vertex cycle. See `T15_BALANCED_BRIDGE_REVIEW.md/.json`.

No search-exhaustion assertion is used as a theorem. All new finite obligations are proved by complete inverse accounting or positive certificates.

## Notation

Swap global coordinates zero and one. The original holes become $H=\{0,1,2,7,14,31\}$ and the prescribed omissions remain $\{1,2\}$. This is a proof device, undone at the end. Split along global coordinate zero and label vertices $v_A=2v+1$ and $v_B=2v$. Face $A$ has holes $\{0,3,15\}$ and omits $0_A$; face $B$ has holes $\{0,7,1\}$ and omits $1_B$. The four retained original holes in global labels are $\{0,7,14,31\}$.

Write $F_A,F_B$ for internal matchings, $X_A,X_B$ for crossing ports, $C:X_A\to X_B$ for the original arbitrary crossing bijection, and $c=|X_A|=|X_B|$. Both faces have thirteen original covered vertices. Thus $c\in\{1,3,5,7,9,11,13\}$ and each internal matching has $m=(13-c)/2$ edges. A bridge is the short new edge $z_Az_B$ for $z\in\{3,15\}$.

## Proof Strategy

Use N14 for every chosen artificial boundary matching. Its connectedness condition allows complete negative-output families to be blocked by saved explicit pairings. This closes all larger crossing counts except one fixed five-port B skeleton. The complete small-crossing B spectra reduce $c=1,3$ to twenty-two and ten fixed B inputs respectively. Positive cycle certificates close every complete input in all three residual families.

## Dependency Map

1. N14 gives spanning A forests and connectedness with an arbitrary artificial pairing.
2. Audited balanced tables classify the resulting B matching after path compression.
3. `verify_t15_core8_blockers.py` reconstructs every inverse family and checks each explicit blocker by graph traversal.
4. `verify_t15_core8_B.cpp` reconstructs the complete small-crossing spectra by graph tracing from the raw balanced tables.
5. `verify_t15_core8_residual.cpp` proves exact full-input coverage and validates every saved positive residual cycle, without search or the producer's enumeration order.
6. `verify_t15_core8_full_closure.py` checks all reductions, counts, input lists, geometry, import hashes, and certificate hashes.

No T15 theorem, eight-hole result, P6 result, or core8 conclusion is used upstream.

## Proof

### Step 1. Arbitrary boundary pairing and path expansion

Choose $z\in\{3,15\}$ and write $w$ for the other retained A hole. Put $E=X_A\cup\{z\}$. For every perfect matching $D$ on $E$, $F_A\cup D$ has exactly the two even local holes $0,w$. N14 gives a simple 15-cycle on $A-0$ containing that matching. Delete $D$. Its nonempty, vertex-disjoint edges break the cycle into a spanning path forest. The induced endpoint pairing $R$ is a perfect matching on $E$, and $D\cup R$ is connected, because contracting the paths recovers the original single cycle. Every surviving edge outside $F_A$ is short.

If $z_B$ is internal, attach the original crossings and the short bridge. The transported endpoint pairing has boundary $X_B\cup\{z_B\}$. Let $k=F_B(z)$ and let $q$ be the transported partner of $z$. Here $k$ is internally covered and $q$ is a port, so $k\ne q$. Suppress $z_B$ to replace the original edge $kz$ and the path ending at $z_B$ by $kq$. The result is a six-edge matching $L$ with holes $\{0,7,z,1\}$. This operation is invertible for fixed $F_B,C$.

If $z_B$ is occupied and $c\ge3$, let $d=C^{-1}(z_B)$ and prescribe $zd\in D$. Write $D=\{zd\}\cup D'$. Replace $zd$ in the N14 cycle by $z_Az_Bd_A$, using the new short bridge and the original crossing. Delete the nonempty matching $D'$ and attach the remaining original crossings. The result is a spanning path forest with interiors $(A-0)\cup\{z_B\}$ and boundary $X_B-\{z_B\}$. Its compressed pairing $Q$ has connected union with the transported $D'$, and $L=F_B\cup Q$ is a matching with the same four holes.

Whenever $L$ is positive in its balanced table, expand each compressed edge in its fourteen-vertex cycle. Path interiors are pairwise disjoint and disjoint from those fourteen B vertices. The expansion adds the fifteen vertices of $A-0$ and $z_B$, producing a simple thirty-vertex cycle. It preserves every original edge, including the suppressed original $kz$, every original crossing and every long original edge. All artificial $D$ edges have been deleted; every compressed edge is expanded; all remaining new edges are short.

### Step 2. Complete inverse families and explicit blockers

For each bridge $z$, let $L$ run over its exact negative table entries.

For occupied mode, every negative output is $L=F_B\cup Q$. Enumerate each $m$-edge subset $J\subseteq L$ and set $F_B=J$, $Q=L-J$.

For internal mode, choose every oriented edge $kq$ of $L$ and every $(m-1)$-edge subset $J\subseteq L-\{kq\}$. Set

$$F_B=J\cup\{zk\},\qquad R_B=(L-J-\{kq\})\cup\{zq\}.$$

These are both directions of the inverses in Step 1. For a fixed actual $F_B$, the resulting family contains all possible negative boundary pairings. If $F_B$ does not occur in the inverse list, it has no negative output. No restriction on its edge lengths or on any A matching is used. The arbitrary crossing bijection only relabels boundary vertices and preserves connectedness.

`r3_boundary_blocking_3_1.json` and `r3_boundary_blocking_15_1.json` save these complete families and explicit blocking pairings. `verify_t15_core8_blockers.py` independently rebuilds every family from the raw negative tables, checks exact set equality, checks all matching supports, and uses graph traversal to verify that each saved blocker has disconnected union with every forbidden output. Its output is `t15_core8_blockers_verification.json`.

For bridge $3$, the complete family counts in internal/occupied modes are $312/43$ at $c=5$, $264/52$ at $c=7$, $100/33$ at $c=9$, $12/10$ at $c=11$, and occupied $1$ at $c=13$. All have explicit blockers except one occupied $c=5$ family.

For bridge $15$, the corresponding counts are $1080/146$, $856/180$, $240/107$, $12/24$, and occupied $1$. All have explicit blockers except two occupied $c=5$ families. There is no internal mode at $c=13$.

Pull the applicable blocker back through $C$ and use it as $D$ in internal mode, or as $D'$ in occupied mode. Every forbidden output has disconnected union with it, whereas Step 1 supplies an output with connected union. Hence the supplied output is positive. This proves every $c\ge7$ case and every $c=5$ input with an internal bridge. For $c=5$ with both bridges occupied, the two null-family sets have exactly one common matching:

$$J=\{(2,4),(5,6),(9,11),(10,13)\}.$$

Its port set is $S=\{3,8,12,14,15\}$. This intersection is verified exactly, not inferred from a failed blocker search. Every other $c=5$ input has a blocker on at least one bridge. The remaining $F_B=J$ inputs are handled in Step 5.

### Step 3. Small-crossing spectra, including occupied mirrors

For $c=3$, each bridge has four A endpoints and three possible endpoint pairings. At least two are realizable: if only $R_0$ were realizable, choose $D=R_0$ in Step 1; its two doubled edges would give two connected components, contradicting connectedness. For $c=1$ the sole two-endpoint pairing is realizable by N14.

For a fixed B input and crossing bijection, transport A ports to their B partners and the bridge endpoint to $z_B$. Add these compressed edges to $F_B$ as a multigraph. Reject a self-loop or any closed component. Otherwise trace the paths between degree-one endpoints and compress them to $L$, testing it against the balanced table. This defines B-admissibility on the same original A endpoint pairings. In particular, at an occupied mirror two endpoint labels become the same B vertex; the graph test, rather than an assumption of distinct boundary labels, handles this. For occupied $c=1$ the sole pairing can form a loop and is then rejected.

`verify_t15_core8_B.cpp` independently traces this multigraph and extracts negative sets from the thirteen audited raw tables and their coordinate images. It checks all $135135$ one-crossing B inputs, and all $\binom{13}{3}9!!\cdot3!=1621620$ three-crossing B/bijection inputs. Its full histograms equal the saved producer histograms.

At $c=1$, exactly twenty-two B inputs have neither bridge admissible. At $c=3$, exactly ten B partial matchings, each with all six bijections, have zero admissible pairing on both bridges; every other B/bijection input has at least two admissible pairings on some bridge. Its two-of-three admissible set intersects the at-least-two realizable A set, closing that input by Step 1.

The ten exceptional B partial matchings are exactly

$$F_B=J\cup\{e\},\qquad e\in\binom{S}{2},$$

with ports $S-V(e)$. This equality is checked directly from the complete independent exception list. It also identifies the relation between the $c=3$ and $c=5$ residuals, without assuming that proving one automatically proves the other.

### Step 4. Exact residual input domains

The saved inputs are `t15_core8_c1_B_inputs.txt`, `t15_core8_c3_B_inputs.txt`, and `t15_core8_c5_B_inputs.txt`. Each begins with its number of B cases; each row contains its $c$ ports and its $(13-c)/2$ internal edges. For $c=1,3$ the lists equal the independently regenerated exceptions, with no duplicate B input. For $c=5$ the sole row is $J$ with ports $S$.

For each fixed B case, the A side has

$$\binom{13}{c}(12-c)!!$$

partial matchings, and there are exactly $c!$ crossing bijections. Consequently the complete residual domains have sizes:

| $c$ | B cases | A partial matchings | Bijections | Full inputs |
|---:|---:|---:|---:|---:|
|1|22|135135|1|2972970|
|3|10|270270|6|16216200|
|5|1|135135|120|16216200|

These are complete domains, with every original internal pairing and arbitrary crossing partner represented. They total $35405370$ original matchings.

### Step 5. Positive certificates and independent coverage verification

`t15_core8_residual.cpp` constructs one explicit positive cycle for each residual input. It treats each original matching edge as an indivisible block and the four retained holes as singleton blocks. It joins these blocks only by short edges. Precomputed bitsets and a memo table accelerate the search; the proof uses only the saved positive cycles.

Each certificate record is exactly 56 bytes: thirteen original matching edges, followed by thirty cycle vertices. The three binary files are `t15_core8_c1_residual.bin`, `t15_core8_c3_residual.bin`, and `t15_core8_c5_residual.bin`.

The separate verifier `verify_t15_core8_residual.cpp` performs no search and does not reproduce the producer's enumeration order. From each record it validates that the required edges form a matching covering exactly $Q_5-H$, with the prescribed B case and exactly $c$ crossings. It computes an independent dense input index: the A port subset has a combinadic rank, the remaining A perfect matching is ranked recursively by the partner of its least unused vertex, and the crossing bijection has a permutation rank. Combining these ranks with the B case index gives a bijection onto the domain in Step 4. A bitmap rejects repeated indices; exact record count and an entirely filled bitmap prove no omission.

For each record the verifier also checks thirty distinct cycle vertices with support exactly $Q_5-\{1,2\}$, all thirteen original edges present, and Hamming distance one for every other edge. It checks exact EOF with no incomplete or trailing record. The three verification reports are `t15_core8_c<c>_residual_verification.json`.

All $35405370$ residual inputs have positive certificates, with zero UNKNOWN and zero exhausted inputs. Their exact byte sizes are $166486320$, $908107200$, and $908107200$, respectively, totaling $1982700720$ bytes. Counts, file sizes and SHA256 hashes are recorded in `T15_CORE8_FULL_CLOSURE_VERIFICATION.json` by the aggregate checker. No finite node cap contributes a negative or universal assertion: each accepted input has its own fully checked positive cycle.

### Step 6. Conclusion

Step 2 closes all larger crossing counts except the single five-port B skeleton, which Step 5 closes. Steps 3--5 close every one- and three-crossing input. These cases exhaust every possible odd crossing count. Undo the global coordinate swap and transport by arbitrary cube automorphisms to obtain the original marked claim. All original edges survive and all new edges are short. ∎

## Reproduction

From this directory, compile with `g++ -O3 -std=c++17`; `-march=native` is optional for the producer. Run the producer as `t15_core8_residual.exe <c> t15_core8_c<c>_B_inputs.txt t15_core8_c<c>_residual.bin t15_core8_c<c>_residual_failures.txt` for $c=1,3,5$, saving its JSON stdout. Run the verifier as `verify_t15_core8_residual.exe <c> t15_core8_c<c>_B_inputs.txt t15_core8_c<c>_residual.bin`, saving each verification JSON. Run `verify_t15_core8_B.exe` for the B spectra, `python verify_t15_core8_blockers.py` for all inverse blockers, and `python verify_t15_core8_full_closure.py` for the aggregate package.

Initial bounded pilots checked $10000$ inputs in each residual family, all positive. After bitset optimization a $100000$-input three-crossing pilot took about 1.55 seconds on the local environment; full enumeration was chosen using this measured cost, rather than an unbounded blind run. Pilot data are not used to establish universal coverage.

## Corrections or Missing Assumptions

None beyond the explicitly retained N14 and audited balanced-table imports. The ten three-crossing B exceptions and the common five-crossing B exception are handled as full positive-certificate domains, not discarded because both bridges fail.

## Open Risks

A fresh independent overall proof audit is required before integrating this one core into parent counts. This candidate package does not establish the other T15 cores, full T15, the complete eight-hole layer, or P6. Previously audited core23 files and global proof status were not changed.
