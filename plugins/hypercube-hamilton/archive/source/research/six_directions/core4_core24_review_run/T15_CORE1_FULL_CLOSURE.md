# Proof Package: full T15 core1

Date: 2026-11-01. ARIS proof-writer. New proof package only; global state and previously audited documents are not modified.

## Claim

Every arbitrary complete-graph matching $F$ on $V(Q_5)$ with holes $\{0,1,2,7,11,19\}$ extends to a simple thirty-cycle on $V(Q_5)\setminus\{1,2\}$, using only short additional hypercube edges. Every cube-automorphic image of this marked geometry is included.

## Status

**PROVABLE AS STATED**, relative to the explicitly listed imported N14 theorem and checked finite tables/blockers. All new finite domains and direct positive certificates below have separately implemented checks reporting PASS. Fresh-context semantic audit remains pending. No full T15, full eight-hole, or P6 conclusion is asserted in this document.

## Assumptions and notation

Cut coordinate zero and label the one-face A by $a\mapsto2a+1$, the zero-face B by $b\mapsto2b$. A has holes $\{0,3,5,9\}$, omits0; B has holes $\{0,1\}$, omits1. Denote original internal matchings by $F_A,F_B$, original crossings by $C$, their port sets by $X_A,X_B$, and their cardinality by $c$. Each matching edge may have arbitrary length and parity. A short edge differs in exactly one coordinate.

A has twelve originally covered vertices and B fourteen, so $c$ is even and $0\le c\le12$. The internal edge counts are $(12-c)/2$ and $(14-c)/2$. The crossing bijection is arbitrary.

## Proof strategy and dependency map

1. Q4 N14 in its arbitrary-complete-graph scope, imported from the existing Q4 proof package.
2. The audited Q4 three-avoided tables: omit $1,s,t$ for two retained A holes $s,t$. Each contains every $10395$ six-edge matching with free vertex0; the three core1 pair geometries are coordinate images of $(3,5,1)$, with33 negatives each.
3. `R4_DOUBLE_BRIDGE_BLOCKING.md` and `r4_inverse_blockers_3_5_1_verification.json`: exact five-mode inverse families and checked positive boundary blockers for $c\ge4$.
4. The new independently checked eighteen Q4 five-avoided tables, each containing all945 five-edge matchings, recorded in `q4_five_avoided_jpair_verification.json`.
5. Complete two- and four-bridge finite classifications and directly checked residual positive certificates described below.

## Proof

### Step1. Zero crossings

Choose $s,t$ from $\{3,5,9\}$ and let $u$ be the remaining retained hole. Add the artificial edge $st$ to $F_A$. N14, with equal-parity holes $0,u$, gives a fifteen-cycle omitting0. Delete $st$ to get a spanning A path from $s$ to $t$ preserving $F_A$.

If $F_B(s)\ne t$, write $k=F_B(s),l=F_B(t)$ and suppress the two bridge vertices in B:
$$L=F_B-\{sk,tl\}+\{kl\}.$$
This is a six-edge matching with holes $0,1,s,t$. A positive thirteen-cycle omitting $1,s,t$ expands the edge $kl$ through $k,s_B,s_A$, the A path, $t_A,t_B,l$ to give the required thirty-cycle. This restores the original B edges and uses only short new bridges.

`verify_t15_core1_c0_B.py` independently enumerates all135135 B matchings and the three suppressions. Precisely105 B matchings have no positive suppression, including rejection of an existing edge $st$. The saved residual input file contains all10395 A matchings for each of these B matchings. All1091475 full inputs have direct positive certificates, checked for exact input edges, required holes, thirty distinct vertices, exact support, all thirteen required edges and shortness of every other edge by `verify_t15_core1_route_c0_residual.cpp`. The residual B list is separately regenerated, not inferred from failed search.

### Step2. Two crossings

For each bridge pair $s,t$ and remaining hole $u$, the short part $N$ of an A path forest has degree two at $u$ and degree one at every other vertex of A except omitted0. Enumerate it by choosing two distinct short neighbors of $u$, then every short perfect matching on the remaining twelve vertices. There are116 patterns per $u$.

Discard a pattern that repeats an original A edge or creates a cycle. The surviving graph $F_A\cup N$ is a spanning forest of two paths, with endpoints the two original ports and $s,t$. The three pairings of these four endpoints give three bits for each of three bridge pairs. Enumerate all62370 A internal partial matchings and record their available nine-bit spectra.

For each of all945945 B internal partial matchings, test all three pairings for each bridge pair. Map A ports to the ordered B ports, attach the two bridges, include $F_B$, reject any closed component and suppress the degree-two bridge vertices and the abstract A stubs. Mark a bit admissible when the resulting six-edge matching lies outside its exact negative table. A common A/B bit expands a thirteen-cycle to the required thirty-cycle. Reversing the crossing bijection exchanges the two port-to-bridge pairings and preserves the port-pair/bridge-pair option.

`t15_core1_c2_types.cpp` produces all input spectra by path walking. `verify_t15_core1_c2_types.cpp` independently recomputes each spectrum by disjoint-set components, checks input uniqueness and exact domain counts, and tests every spectrum pair in both orientations. Every nonzero B spectrum works for every A input in both orientations. Exactly420 unordered B inputs have zero spectrum, leaving52390800 full inputs. Step4 closes every one of these.

### Step3. The remaining large-crossing B lists

Apply the five-mode double-bridge theorem in `R4_DOUBLE_BRIDGE_BLOCKING.md`, for all three choices from retained holes3,5,9. Its hypotheses hold: all four A holes are even; the retained holes are nonzero and distinct from the B holes0,1. It handles distinct internal mates, internally paired bridge mirrors, one occupied mirror in either orientation, and both occupied mirrors. The prescribed artificial edges in the occupied and paired modes are removed or replaced by the original B path as specified there; no artificial edge remains in the final cycle.

For a fixed B matching, every reported positive auxiliary blocker disconnects every bad output pairing. N14 supplies an output connected with the chosen auxiliary pairing, hence a positive output. This argument pulls every pairing through the actual arbitrary crossing bijection. A missing blocker is retained as unresolved and is never treated as a negative theorem.

`verify_t15_core1_joint_B.py` transports the completely checked canonical inverse families by coordinate permutations fixing1, intersects their three unresolved B sets, and compares the resulting exact sets with every supplied B input file. The resulting common unresolved counts are:

| $c$ | B inputs requiring another construction |
|---:|---:|
|4|210|
|6|28|
|8|1|
|10|0|
|12|0|

Thus all $c=10,12$ inputs are already closed. For $c=4,6,8$, only the displayed B lists require Step4. This reduction depends only on B and applies to every A matching and every original crossing bijection.

### Step4. Four-bridge transfer

Let $J=\{(6,7),(10,11),(12,13)\}$. Choose two retained holes $s,t\in\{3,5,9\}$ and let $u$ be the third. Choose an even endpoint $z$ of one J edge and an odd endpoint $w$ of a different J edge. This gives18 bridge sets
$$S=\{s,t,z,w\}.$$
All bridge labels are distinct, avoid0,1, and lie in the support of the required cycle. Each $u$ is distinct from every bridge label.

Enumerate every short A graph $N$ having degree two at $u$, degree zero at $0,z,w$, and degree one at every other A vertex. Choose the two short edges at $u$, then every short perfect matching on all remaining vertices after deleting $0,u,z,w$ and the selected neighbors. This is a complete degree enumeration.

If $F_A\cup N$ is simple and acyclic, it provides a pairing R of the abstract external endpoints consisting of the $c$ original crossing stubs and four bridge stubs. Endpoints at the same A vertex are kept as distinct stubs. In particular, if $z$ or $w$ is an original A port, that A vertex is isolated in $F_A\cup N$ and its original-crossing stub is paired directly to its bridge stub. The isolated vertex is retained as an interior vertex during expansion.

Map each original-crossing stub through its actual partner in B, attach the four short bridges, and add $F_B$. If the resulting multigraph H has a cycle component, reject this choice. This includes a bridge equal to an original crossing: they form a two-cycle and cannot be merged as one edge. Both the producer's union-find and the independent checker's duplicate-edge/graph traversal reject this case.

For an accepted choice every A vertex except0 and every B bridge vertex has degree two, every other covered B vertex has degree one, and retained free $0_B$ has degree zero. H therefore consists of five nontrivial paths and the isolated free vertex. Compress its paths to a matching L on the ten B vertices outside $\{0,1\}\cup S$. A positive eleven-cycle on $B\setminus(\{1\}\cup S)$ containing L expands through those five paths to a thirty-cycle. Expansion restores fifteen A vertices and four B bridge vertices, adding nineteen vertices to the eleven-cycle. All original edges survive, and all new edges are short.

The eighteen five-avoided tables provide exact positive eleven-cycles for all positive L entries. Their positive witnesses and negative degree completions were independently checked in `q4_five_avoided_jpair_verification.json`. The proof needs only the positive witnesses; a negative entry merely rejects this particular choice.

### Step5. Complete four-bridge coverage and direct residuals

`t15_core1_joint_fourbridge_spectra.cpp` enumerates every A partial matching in the indicated crossing class, computes all its realizable external pairings for each of the eighteen bridge choices, and tests every B input from Steps2--3 in all $c!$ port orders. This covers every original crossing bijection: order the A ports once and list their B mates in that order.

The separately implemented `verify_t15_core1_joint_fourbridge.cpp` replaces union-find with fixed-degree adjacency lists and breadth-first component traversal. It rejects duplicate edges, excessive degrees and every cycle component. It independently rebuilds the A pairing spectra and repeats the complete finite domain. Every uncovered input is compared byte-for-byte with the saved residual list; premature end and trailing data are rejected. Thus the exact residual lists, not merely their sizes, are independently verified.

| $c$ | A partial matchings | B matchings | All A/B/port-order inputs | Residuals |
|---:|---:|---:|---:|---:|
|2|62370|420|52390800|0|
|4|51975|210|261954000|1575|
|6|13860|28|279417600|6300|
|8|1485|1|59875200|2520|

Every row reports PASS in `t15_core1_joint_fourbridge_c*_verification.json`. Every residual in the last three rows has a direct thirty-cycle certificate; `verify_t15_core1_joint_residual.cpp` checks exact original matching edges, exact holes, support, vertex uniqueness, all thirteen required edges, closing adjacency, and shortness of every added edge. All10395 positive residual certificates pass, with zero exhausted or node-limited inputs. Together with Step1, there are1101870 independently checked direct witnesses.

The only possible crossing counts are $0,2,4,6,8,10,12$. Steps1--5 exhaust all of them and preserve every original matching edge. The claim follows.

## Corrections or missing assumptions

No weakening of the core1 claim is made. Imported N14 and the finite matching tables must retain their arbitrary complete-graph scope. This proof requires no assertion that the discarded bridge choices fail globally.

## Open risks and reproducibility

- Fresh-context semantic audit remains pending.
- The core1 finite manifest must list fixed proof inputs and checker outputs; dynamic global coverage ledgers are not proof dependencies.
- Compile C++ with `g++ -O3 -std=c++17` and run from `research/six_directions`.
- Other cores and the final eight-hole geometry integration remain separate obligations.
