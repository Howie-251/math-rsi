# Complete T15 core 24

Date: 2026-11-01. ARIS proof-writer. Candidate complete-core proof, with explicit finite certificates and independent checks. Fresh overall semantic review is required before integration. Full T15 and the whole eight-hole layer are not asserted here.

## Claim

Every arbitrary matching $F$ of $K(Q_5)$ with holes $\{0,1,7,14,22,31\}$ extends to a simple cycle on $Q_5-\{1,7\}$ containing every edge of $F$, with all new edges short. This includes the entire marked cube-automorphism orbit. Original matching edges may have arbitrary lengths and parity types.

## Status and imports

PROVABLE AS STATED, conditional on the imported Q4 N14 theorem and the audited Q4 finite tables below. The manifest is `T15_CORE24_FULL_CLOSURE_VERIFICATION.json`; the full package awaits fresh overall review.

1. Q4 N14 for arbitrary complete-graph matchings with two same-parity holes, omitting either specified hole.
2. Audited three-avoided Q4 tables: holes $\{0,1,a,b\}$, omissions $1,a,b$, each containing all $10395$ matchings and positive thirteen-vertex cycles. See `R4_DOUBLE_BRIDGE_REVIEW.md/.json` and the imported table audits there.
3. The five-mode inverse-blocking theorem `R4_DOUBLE_BRIDGE_BLOCKING.md`, with its independent complete inverse-family and blocker audit `R4_DOUBLE_BRIDGE_REVIEW.json` (PASS, provisional same-family review). It proves the large-crossing reduction stated below, not the remaining residual cases.
4. Eighteen eleven-cycle tables for this core's four-bridge choices. Their positive cycles and exact input domains are checked in `r4_parent_fourbridge_preparation.json`. Only positive certificates are used by the four-bridge construction.

## Geometry and notation

Swap global coordinates zero and one. This maps the original holes to $\{0,2,7,13,21,31\}$ and the omissions to $2,7$. Write normalized labels as $v_A=2v+1$ and $v_B=2v$. Then A has holes $\{3,6,10,15\}$ and omits $3_A$; B has holes $\{0,1\}$ and omits $1_B$. The retained free global vertices are $0,13,21,31$.

Write $F_A,F_B$ for internal matchings, $X_A,X_B$ for their ports, and $C:X_A\to X_B$ for the arbitrary crossing bijection. The crossing count $c$ is even, $0\le c\le12$; the internal edge counts are $(12-c)/2$ in A and $(14-c)/2$ in B. A ports may include local vertex zero, which is originally covered in A.

## Strategy and dependency map

For $c\ge4$, the audited five-mode two-bridge inverse argument closes all but explicit joint B residuals. Every complete input over these residuals is solved by an independently checked four-bridge forest. A separate exact small spectrum closes all two-crossing inputs except 786 B partial matchings, and the same four-bridge check closes every input over these too. At zero crossings, N14 gives a uniform A path; only 255 B matchings remain, and explicit independently verified thirty-cycles cover their entire product with A matchings.

Thus the dependencies are N14 and audited tables; the five-mode reduction; exact small-spectrum input completeness; the four-bridge forest expansion; and positive residual cycle verification. No unknown search result is used as a universal certificate.

## Proof

### Step 1. The audited two-bridge reduction for $c\ge4$

Choose two bridge labels $a,b$ among $6,10,15$. Add an arbitrary auxiliary pairing $D$ on $X_A\cup\{a,b\}$ to $F_A$. N14 gives a 15-cycle on $A-3$. Deleting $D$ leaves an A forest whose endpoint pairing has connected union with $D$.

The five distinct B situations are: distinct internal mates; internally paired bridges; only the first mirror occupied; only the second occupied; both occupied. In the latter four modes prescribe and replace the corresponding auxiliary edge or edges before deleting the remaining auxiliary pairing. As proved and audited in `R4_DOUBLE_BRIDGE_BLOCKING.md`, each permitted quotient pairing has connected union with its chosen remaining auxiliary pairing, and a positive thirteen-cycle in B expands to the required thirty-cycle.

The complete inverse lists account for every possible negative B output for each fixed $F_B$. Every saved blocking pairing disconnects all bad outputs. N14's connected output is therefore positive. An input absent from the inverse list has no negative output. Intersecting unresolved families over all three retained-hole bridge pairs leaves precisely 312, 34, and 1 B internal matchings for $c=4,6,8$, respectively, and none for $c=10,12$. These exact joint lists are in `r4_joint_blocking_check.json` and the core24 B input files.

### Step 2. Four bridges and their finite positive test

Set $J=\{(5,7),(9,11),(12,14)\}$, with the first endpoints even and second endpoints odd. Choose a retained-hole bridge pair $a,b$, two distinct edges of J, and an even endpoint $p$ of one and the odd endpoint $q$ of the other, in either order. There are $3\cdot3\cdot2=18$ choices. Let $u$ be the third retained A hole and let $S=\{a,b,p,q\}$.

Enumerate every short-edge set H on $A-3$ having degree two at $u$, zero at $p,q$, and one at every other vertex. This enumeration chooses the two distinct neighbors of $u$ and then every short perfect matching on the remaining eligible vertices. Reject H if it overlaps a required $F_A$ edge or if $F_A\cup H$ has a cyclic component.

Its boundary has one crossing endpoint incidence for every A port and one bridge endpoint incidence for every member of S. A vertex in $\{p,q\}\cap X_A$ has two endpoint incidences at the same isolated A vertex; this is a zero-length path, not a deleted vertex. The implementation preserves both incidences as distinct indexed endpoints. Every other component is a path with two endpoint incidences. Thus this correctly represents all fifteen A vertices, including zero-length components when needed.

Attach all original crossings, the four short bridges at S, and $F_B$. Reject a cyclic component. Suppressing the interiors, including the four B bridge mirrors, gives a perfect matching L on the ten covered vertices of $B-\{0,1,a,b,p,q\}$; the retained free vertex zero is not part of L.

If L has a saved positive eleven-cycle in the corresponding five-avoided table, expand the compressed paths. Their interiors are exactly the fifteen A vertices and four B bridge mirrors. Their disjointness and acyclicity preserve simplicity, and $11+15+4=30$ gives the exact required support. Every original matching edge lies in a compressed path or in L and is restored. Every surviving added edge is short. This proves the soundness of each accepted four-bridge test.

### Step 3. Complete four-bridge coverage of the large-crossing residuals

`r4_joint_fourbridge_parent.cpp` enumerates every A port subset and every matching on the remaining originally covered A vertices, every joint residual B internal matching, and all $c!$ crossing bijections. Its core24 branch uses omission 3 and permits A port zero. It computes the endpoint spectra of all H from Step 2 and accepts only a saved positive B table record.

`verify_r4_joint_fourbridge_generic.cpp` independently checks degree bounds, duplicate edges, acyclicity and components using explicit graph traversal rather than the producer's union-find. It independently enumerates the complete original input domain and checks exact agreement with the saved residual input list. Its full verification reports are the `r4_joint_fourbridge_core24_c<C>_verification.json` files.

| $c$ | A partial matchings | B residuals | crossing bijections | complete inputs | remaining residuals |
|---:|---:|---:|---:|---:|---:|
|4|51975|312|24|389188800|0|
|6|13860|34|720|339292800|0|
|8|1485|1|40320|59875200|0|

Each original input is accepted by at least one sound test from Step 2. Together with Step 1, this closes every crossing count at least four.

### Step 4. The two-crossing spectrum and its exact residual domain

There are $\binom{12}{2}9!!=62370$ A partial matchings and $\binom{14}{2}11!!=945945$ B partial matchings. Each of the three retained-hole bridge pairs has four endpoint incidences and three possible pairings, giving a nine-bit spectrum on each face. All A spectra are obtained by complete short-degree-factor enumeration and cycle rejection. Each B bit records successful suppression to an exact positive thirteen-cycle table entry.

`t15_core24_c2_types.cpp` saves the signature and complete original matching for every partial input. `verify_t15_core24_c2_types.cpp` independently reconstructs every signature using graph components, checks uniqueness and full cardinalities of both original input lists, and compares both crossing orientations. The A matching encoding includes the nibble at vertex zero, avoiding ambiguity when zero is a port or matching endpoint.

The independent check proves that every disjoint A/B spectrum pair has B spectrum zero. Exactly 786 B partial matchings have zero spectrum. Both crossing orientations fail for every A partial input over these B matchings, giving precisely $786\cdot2\cdot62370=98045640$ complete residual inputs. There are no additional nonzero-spectrum B failures.

The B list is `r4_joint_fourbridge_core24_B2.txt`; its exact equality with the zero-spectrum list is checked by the manifest program. The complete four-bridge producer and graph verifier from Steps 2--3 check all $98045640$ residual inputs and leave none. Hence every two-crossing matching has the required cycle.

### Step 5. Zero crossings: a uniform A path and complete B reduction

For any retained-hole bridge pair $a,b$, add the single auxiliary edge $ab$ to $F_A$. It leaves the same-parity holes 3 and the third retained A hole. N14 gives a 15-cycle on $A-3$; deleting $ab$ gives a spanning path between a and b, uniformly for every A matching.

If $F_B$ contains $ab$, attaching both bridges closes a component and that bridge pair is rejected. Otherwise let $k=F_B(a)$ and $l=F_B(b)$. They are distinct and outside the bridge pair. Suppress the resulting path from k through the two B mirrors and all A vertices to l, replacing $ak,bl$ by $kl$. This gives a six-edge matching L with holes $\{0,1,a,b\}$. Any positive thirteen-cycle for L expands to the required thirty-cycle.

`verify_t15_core24_c0_B.py` independently enumerates all $13!!=135135$ B matchings, tests all three bridge pairs by this exact suppression, and identifies exactly 255 exceptional B matchings. It independently regenerates all $11!!=10395$ A matchings and every original input over those B matchings, checking exact equality with the entire saved residual byte stream. Thus the residual domain has exactly $255\cdot10395=2650725$ inputs; its completeness is not inferred merely from its file size.

### Step 6. Complete positive certificates for zero-crossing residuals

`t15_core24_raw_residual.cpp` produces a thirty-cycle for every saved zero-crossing residual input. The result is $2650725$ positive records, zero UNKNOWN and zero exhausted input. Each record contains the thirteen required edges followed by thirty cycle vertices.

`verify_t15_core24_raw_residual.cpp` performs no search. It compares every required edge byte with the independently regenerated original input stream, checks distinct required endpoints and the exact original hole set, checks thirty distinct cycle vertices with support exactly $Q_5-\{2,7\}$, and verifies all thirteen original edges and shortness of every other cycle edge. It asserts the complete record count and rejects trailing bytes. All records pass. File sizes and SHA-256 values appear in the manifest.

The even crossing counts zero through twelve are now exhausted. Undo the global coordinate swap to prove the original marked claim; cube automorphisms preserve the entire conclusion and yield its orbit. ∎

## Reproduction and exact finite evidence

The principal evidence files are:

- `t15_core24_c0_B_verification.json` and `t15_core24_c0_residual_verification.json` for zero crossings.
- `t15_core24_c2_types_verification.json` for the independent complete small spectrum.
- `r4_joint_fourbridge_core24_c2/4/6/8.json` and the corresponding `_verification.json` files for four-bridge coverage.
- `R4_DOUBLE_BRIDGE_REVIEW.json` and `r4_joint_blocking_check.json` for the imported five-mode reduction.
- `r4_parent_fourbridge_preparation.json` for the actual positive eleven-cycle tables.

Run `python verify_t15_core24_full_closure.py` to rebuild the complete finite manifest after the documented executable checks. Compile C++ sources with `g++ -O3 -march=native -std=c++17`. The four-bridge producer and checker use interfaces `exe 24 c`; the raw residual producer takes input26, output56 and failure-log paths, and its verifier additionally takes the expected count.

## Open risks

A fresh overall semantic and finite-input audit is required before integrating this core into parent counts. The imported two-bridge theorem currently has provisional same-family acceptance. This package makes no full T15 or full eight-hole claim.
