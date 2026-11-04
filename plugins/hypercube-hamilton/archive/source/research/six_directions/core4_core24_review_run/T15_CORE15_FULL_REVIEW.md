# Core 15 complete closure: fresh proof review

**PASS — same-family / provisional.** The complete arbitrary-complete-graph-matching claim for the marked core 15 is proved. No open mathematical gap was found. This review does not establish full T15 or the complete eight-hole layer.

Reviewer: `gpt-6.1-sol`, reasoning `high`, fresh assigned reviewer `/root/t15_core15_complete_audit`. The user-requested configuration overrides the proof-checker skill's nominal Astra/ultra setting. Applied instructions: `F:/c4free-hypercube-main/ARIS/skills/skills-codex/proof-checker/SKILL.md`. No cross-family semantic acceptance is claimed.

## Exact reviewed statement

For every matching F covering exactly Q5 minus {0,1,2,13,22,31}, there exists a simple 30-cycle on Q5 minus {1,2} containing F, with every edge outside F a cube edge. All original edges may have arbitrary length and parity. Cube automorphisms transport the marked holes and prescribed omissions together.

The declared main inputs are `T15_CORE15_FULL_CLOSURE.md` and `T15_CORE15_FULL_CLOSURE_VERIFICATION.json`. Input and dependency SHA-256 hashes are recorded in the JSON sidecar. The reviewed proof, manifest, certificates, and global ledgers were not modified. Fresh code, compilations and outputs are isolated in `T15_CORE15_FULL_REVIEW_work/`.

## Obligation and hypothesis ledger

The dependency graph is acyclic: cube normalization + Q4 N14 -> A forests and connected pairing unions; complete balanced positive tables -> admissible B compression; exhaustive B kernels -> small exceptional lists; explicit residual cycles -> the exceptional inputs. Path expansion finishes the theorem. No T15 closure or eight-hole claim is used upstream.

| Obligation | Discharge |
|---|---|
| Normalization | Independently verified old-to-new coordinate destination (0,1,2,4,3), all cube adjacencies, transformed holes {0,1,2,14,21,31}, and fixed omissions 1,2. Under v_A=2v+1, v_B=2v, A holes are {0,10,15}, B holes {0,1,7}; omitted local vertices are 0_A,1_B. |
| Complete original domain | Each face has 13 original covered vertices. Thus c is odd from 1 through 13, internal edge counts are (13-c)/2, and an arbitrary matching decomposes uniquely into A partial matching, B partial matching and crossing bijection. The decomposition counts sum to 25!!, covering all arbitrary matchings, with no length/parity restriction. |
| N14 applications | X_A and chosen A hole z are disjoint and disjoint from F_A. Every D makes seven disjoint edges with exactly two same-even holes 0 and the other retained A hole. N14 omits 0. Fresh direct checks certify all 135135 arbitrary matchings for other hole 3 and all 135135 for other hole 15; coordinate permutations send hole 3 to 10. This supplies precisely every N14 instance used. |
| Forest extraction | D is nonempty and consists of cycle edges. Deleting it from one simple cycle gives only disjoint paths, with endpoint set X_A union {z}; no hidden cyclic component survives. Contracting these paths in the original cycle gives a connected multigraph D union R. |
| Internal bridge mirror, c>=5 | After crossing attachment, z_B has neighbors k=F_B(z) and a transported port q. k is not a port, so k!=q, excluding a suppression loop. The replacement kq and other compressed paths have disjoint interiors and yield a valid six-edge L on the twelve nonholes. Fixed F_B,C recover R uniquely from L. |
| One forbidden output | The bridge-10 table is a coordinate image of the complete (9,2) table. Fresh checking confirms one sentinel row with matching {(2,4),(3,13),(5,15),(6,8),(9,11),(12,14)}; all other rows have directly valid positive cycles. Even proving this sentinel truly negative is unnecessary: at most one output lacks a positive certificate. |
| Artificial matching choice | For each fixed original F_A,F_B,C, invert the lone unsupported L if it is attainable to obtain R0. Choose D=R0 before invoking N14. With c+1>=6 endpoints, D union R0 has at least three components, contradicting the connected union guaranteed for the N14 output. Thus that output is supported. No assumption that the author can prescribe an arbitrary realizable R is used. |
| Occupied bridge mirror, c>=5 | d=C^{-1}(z_B) is an A covered vertex, distinct from hole z. Prescribe zd in D, replace this artificial edge by z_A-z_B-d_A, and delete the nonempty D'. The replacement inserts a new vertex into a single cycle. Deleting D' leaves paths with endpoints X_A minus {d}, transported to X_B minus {z_B}. No loop or detached cycle appears. |
| Occupied quotient choice | Fixed F_B,C recover Q from L because original internal B edges and quotient edges have disjoint endpoint sets. If Q0 is unsupported, choose D'=Q0. Its c-1>=4 endpoints make D' union Q0 disconnected, whereas contraction of the N14 cycle makes the actual D' union Q connected. Hence L is supported. This also covers the boundary case c=5 and c=13 with no internal edges. |
| c=3 abundance | Each bridge has three possible pairings. A singleton realizable set {R0} would contradict N14 with D=R0; thus at least two are realizable for every fixed F_A. All nonexceptional B spectra have at least two admissible pairings on one bridge, so intersection in the same three-element universe is guaranteed for every crossing bijection. |
| Small B kernels | Freshly compiled independent graph traversal checks all 135135 c=1 B inputs and all 1621620 c=3 B/bijection inputs. It traces paths, rejects unvisited closed components including the occupied-bridge loop, and reconstructs L before lookup. Histograms equal the stated complete histograms. Fresh exceptional sets equal the supplied B input files exactly. |
| c=1 occupied bridge edge case | An occupied sole-port bridge would close an isolated A-plus-z_B cycle and is rejected by the kernel. The proof needs only bridges marked admissible by that kernel. It never applies the c>=3 occupied-bridge construction at c=1. |
| Residual coverage | For c=1, twelve B cases times 13*11!! A cases yields 1621620. For c=3, the single B case times choose(13,3)*9!! A cases times all six bijections yields 1621620. Ports and internal vertices partition exactly the thirteen covered B vertices; the input lists are distinct. |
| Certificate correctness | Recompiled `verify_t15_core15_residual.cpp` with assertions enabled and independently ran both complete files. Every reconstructed required edge set agrees byte-for-byte; every cycle has thirty distinct vertices with exactly the stated support, all thirteen original edges and only short remaining edges. Record counts and EOF checks pass. |
| Expansion and auxiliary edges | In either bridge case L edges represent vertex-disjoint paths; the positive table cycle uses each once. Expanding yields support (A-0) union (B-1), hence precisely thirty vertices, and one simple cycle. All D or D' edges are deleted or replaced. Original F_A, F_B and crossing edges are restored. The bridge and surviving nonoriginal A/B edges are short; no artificial edge remains. |
| Existential quantifiers | Choices are allowed to depend on the entire fixed matching. D or D' is chosen from the corresponding unsupported pairing before invoking N14; the connected-union property forces a positive output for every possible N14 cycle for that choice. No future-dependent or uniform-choice assertion is needed. |

## Fresh deterministic verification

The residual verifier was compiled from the reviewed source with `g++ -O3 -std=c++17`; `-DNDEBUG` was not used. Both complete runs returned PASS:

| Crossing count | B exceptional partial inputs | Positive cycles checked | Bytes | SHA-256 |
|---:|---:|---:|---:|---|
| 1 | 12 | 1621620 | 90810720 | ec2c31b708e1f3b4dd493e1f1bf903e82ab7fff7c69902b1d29022c6dd13fcff |
| 3 | 1 | 1621620 | 90810720 | 8d90f33b8c8d3d187e15bff9445034b7e28061e74d49692679969e05ac5e01a2 |

For the B kernel, the isolated source differs from `verify_t15_r3_small_B.cpp` only by restricting its outer core list to `{15}`; its graph algorithm and all input loops are unchanged. Fresh c=1 histogram: {0:12, 1:10503, 2:10395, 3:114225}. The c=3 zero spectrum occurs six times, representing exactly ports {5,10,15} and internal edges {(2,4),(3,13),(6,8),(9,11),(12,14)} under all six bijections. Every other c=3 mask has at least two admissible pairings on a bridge.

The new read-only Python audit independently reconstructs all perfect matching domains, validates all 135135 records across all thirteen balanced tables and all 270270 N14 records, checks every stored positive cycle directly, verifies the bridge coordinate transform, and compares fresh exceptional lists/histograms and certificate hashes with the claimed inputs. Negative sentinel impossibility is not required for this theorem; every other row has been positively certified.

Reproduce from the isolated directory after compiling `residual_check.exe` and `small_B_check.exe`:

```powershell
./residual_check.exe 1 ../t15_core15_c1_B_inputs.txt ../t15_core15_c1_fast.bin | Out-File -Encoding utf8 c1_fresh.json
./residual_check.exe 3 ../t15_core15_c3_B_inputs.txt ../t15_core15_c3_hybrid.bin | Out-File -Encoding utf8 c3_fresh.json
./small_B_check.exe | Out-File -Encoding utf8 small_B_fresh.json
python fresh_inputs.py
```

## Adversarial checks and remaining assurance scope

Checked attempted failure modes: arbitrary long/parity-mixed original edges; nonidentity crossing bijections; occupied mirror producing a loop; c=1 occupied mirror; minimum large crossing c=5; maximum c=13; parallel edges in D union R; artificial edges accidentally retained; repeated compressed edge endpoints; wrong cycle support; missing/trailing binary records; and producer truncation or search caps. None creates a gap in the reviewed argument. Positive certificate verification does not depend on producer pruning, search order or completeness claims.

Definitions remain consistent: R pairs X_A union {z}; Q pairs X_A minus {d}; L is a six-edge matching on the twelve covered B vertices after excluding bridge and omitted vertices. There are no limits, asymptotic constants, integration interchanges or probabilistic assertions. All relevant finite inequalities are endpoint-cardinality bounds and the two-of-three intersection bound, with their boundary hypotheses verified above.

No proof repair was needed. The stated N14 and balanced-table imports are explicit in the source; this review additionally checks their complete positive certificate content as needed here. Semantic acceptance remains provisional because this is a same-family review. The output may support integrating this single marked core, subject to the parent's separate integration process; it does not change parent counts or any global ledger.
