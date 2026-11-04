# Complete T15 core 0: independent proof review

Verdict: **PASS, same-family / provisional**, for the complete core-0 theorem in `T15_CORE0_FULL_CLOSURE.md`, with the explicitly imported audited Q4 N14 theorem and exact balanced tables. No mathematical issue was found. All new finite checks and the full residual cycle certificate check passed. This does not establish full T15, the eight-hole layer, or P6.

Reviewer: `gpt-6.1-sol`, reasoning `high`, fresh context `fork_turns=none`, agent `/root/t15_core0_complete_audit`. These are the requested actual review settings; no Astra/ultra or cross-family review is claimed. Applied skill: `F:/c4free-hypercube-main/ARIS/skills/skills-codex/proof-checker/SKILL.md`. The assignment overrides the nominal skill model and output filenames. No main proof, global state, wiki, or claim ledger was edited.

## Exact statement and typed symbols

For every matching F covering exactly Q5 minus {0,1,2,7,11,13}, there exists a simple cycle with vertex set Q5 minus {1,2}, containing F, with every edge outside F short. Transporting the entire marked configuration by any cube automorphism gives the corresponding statement. Original edges have no parity or length restriction.

After deleting coordinate 1, A is the one-face and B the zero-face, each locally Q4. A holes are {0,3,5}; B holes are {0,7,1}. The cycle omits 0_A and 1_B. F_A,F_B are internal matchings; C:X_A→X_B is a bijection of crossing ports; c is their common cardinality. z∈{3,5} is a bridge label and w the other label. D and R are perfect matchings on E=X_A∪{z}. In the occupied case d=C^{-1}(z_B), D={zd}∪D', and Q is a perfect matching on X_A minus {d}. L is always a six-edge matching on B minus {0,7,1,z}. Compressed edges carry their original path interiors throughout expansion.

The coordinate calculation is direct: global A holes 2,7,11 delete to 0,3,5; global B holes 0,1,13 delete to 0,1,7. Each face has thirteen covered vertices, so 13-c=2|F_A|=2|F_B|. Thus c∈{1,3,5,7,9,11,13}; there is no zero-crossing case.

## Imported inputs

I read `Q4_CORE_AND_A4_SPLIT.md`, `T15_BALANCED_BRIDGE_REVIEW.md/.json`, and the two requested proof dependencies in full. The N14 scope is arbitrary complete-graph matchings with two same-parity holes, omitting either prescribed hole. The earlier audit independently checked all 270270 base certificates and all thirteen complete balanced tables, including positive cycles, negative infeasibility, full matching coverage, and transformed negative-family agreement.

As explicitly authorized, I import those finite base results rather than rerun their 405405 records. I independently rehash both N14 binary files, all thirteen balanced binary files, and the imported audit Markdown against that audit's declared hashes; all agree. Only the (3,1) balanced geometry and its coordinate image (5,1) are mathematically needed here. Swapping coordinates 1 and 2 fixes 0,7,1 and takes 3 to 5, so it transports the complete table and its three negatives without any hypothesis change.

No producer PASS, search exhaustion, or previous candidate proof is accepted as evidence for any new finite obligation below.

## Dependency DAG and hypothesis ledger

The DAG is acyclic: imported N14 → A forests and connected boundary pairings; new disconnection lemma → exclusion for large boundary sets; imported balanced tables → positive B cycles and exact negative sets; new c5 inverse exhaustion or complete c1/c3 B enumeration → a permissible compression; path expansion or residual positive certificates → the 30-cycle. No T15 conclusion, eight-hole conclusion, or P6 assertion occurs upstream.

| ID | Obligation and discharge |
|---|---|
| MC1 | F_A∪D is a genuine seven-edge matching: its supports are disjoint, E has c+1 vertices, and its only holes are 0,w. Both holes have even local parity. Hence N14 applies for **every** D and omits 0. |
| MC2 | Deleting nonempty D from a simple cycle leaves only paths, endpoints E, and all fifteen A vertices. The matching property prevents two deleted edges from sharing a vertex. Compressing these paths in the original cycle proves R∪D connected, with common edges interpreted with multiplicity when necessary. |
| MC3 | Internal mirror: z_B has original mate k outside X_B∪{z}. The R path incident to z_B has other endpoint q∈X_B, hence q≠k. Suppression makes edge kq and creates neither a loop nor a closed component. All remaining F_B edges have disjoint support from the port paths. |
| MC4 | Internal injectivity: k is fixed. The partner q of k in L uniquely determines the suppressed path; expand kq to kz,zq, remove the fixed F_B edges and pull the ports back through C. Thus distinct R cannot give the same L; at most three R are negative. |
| MC5 | Occupied mirror: d is an A covered port while z is an A hole, so d≠z. For c≥3 there is nonempty D'. Replacing the original cycle edge zd by z_A,z_B,d_A gives one simple sixteen-vertex cycle, because z_B is new to it. Deleting D' leaves paths, never a cyclic component. Their endpoint set after other crossing attachments is X_B minus {z_B}. |
| MC6 | Occupied connectedness: restoring D' closes exactly that same single cycle. Compressing the surviving paths therefore gives connected Q∪D'. This is a statement about the quotient paths of the modified cycle, not an assumption that Q can be prescribed. F_B is supported off the endpoints, so Q→L=F_B∪Q_B is injective. At most three Q are forbidden. |
| MC7 | Large boundary exclusion: choose D (internal) or D' (occupied) **before** invoking N14, to disconnect every forbidden output. N14 supplies some output whose union with that selected auxiliary pairing is connected, so that output is not forbidden. No swap from ∀D∃R to ∃R∀D occurs. |
| MC8 | Internal c≥5 has |E|=c+1≥6; occupied c≥7 has |X_A minus {d}|=c-1≥6. Both sets have even size and the at-most-three-matchings lemma applies. This covers every c≥7 and all internal-mirror c=5 inputs. |
| MC9 | Remaining c=5: if a compression for bridge z is negative, its L is one of the exact three negatives. Its four-edge F_B is obtained by retaining four L edges. The other two edges cover precisely X_B minus {z}. Requiring the other bridge w to be a port enumerates every possible bad (X_B,F_B) for this bridge. Independent inverse lists have 15 entries each and empty intersection. Hence at least one bridge has no negative compression, for every A matching and C. Any D' then suffices. |
| MC10 | c=3: the three R possibilities on E form a three-element universe. If the realizable set were {R0}, choosing D=R0 in N14 would give disconnected R0∪D, a contradiction. The realizable set is nonempty and therefore has at least two elements for each bridge. Complete B enumeration proves some bridge has at least two good pairings; these two sets intersect. |
| MC11 | c=1: N14 realizes the unique two-endpoint pairing. Complete B enumeration finds precisely the six inputs printed in the dependency. Exact equality with the six residual input records was independently checked, including distinctness and full disjoint matching support. |
| MC12 | For each residual B input there are thirteen A port choices and 11!!=10395 A internal matchings. The freshly compiled independent verifier enumerates all of them and checks exactly 810810 binary records, their exact required edges, thirty distinct vertices, exact omitted set {1,2}, all thirteen required edges, every other edge short, and EOF. All pass. |
| MC13 | Expansion replaces each required compressed matching edge by its stored simple path, with disjoint interiors. The B cycle has fourteen vertices and omits z,1; expansion adds fifteen A vertices and z_B, giving thirty vertices and omitting exactly 0_A,1_B. All artificial edges disappear, every original edge survives, and every remaining new edge is short. This also holds for c=13, when F_A,F_B are empty. |

## New independent finite verification

The new `T15_CORE0_FULL_independent_check.py` imports no producer or earlier checker module. It independently generates matching sets, uses disjoint-set connectivity, parses raw balanced records, and enumerates the inverse candidates by retaining four negative-table edges (the producer instead removes two). Its complete results are in `T15_CORE0_FULL_independent_check.json`.

The finite disconnection basis checks the matching lists are exactly all perfect matchings, without duplicates; verifies the normalized first matching; verifies all 225 or 11025 ordered-pair cells and the range of every witness; and independently checks all three witness unions disconnected. N=6 has 15 perfect matchings; N=8 has 105. Equality and repetition cases are included. Normalization is lossless because any bijection taking R1 to the consecutive pairing preserves all union connectivity. Collections of size one or two can repeat a member, and the empty collection is immediate.

For every even N≥10, the analytic proof is complete: choose e1∈R1, then e2∈R2 avoiding its two vertices (at most two R2 edges excluded), then e3∈R3 avoiding the four chosen vertices (at most four edges excluded). Each matching has at least five edges. Complete these disjoint edges arbitrarily on the remaining even vertex set. Each selected shared edge is a two-vertex component of D∪Ri, and N>2. This proves the infinite part with no computational extrapolation.

The c5 check verifies the raw (3,1) file has exactly all 10395 distinct matchings on the proper support, isolates exactly three negative records, constructs the complete (5,1) family by the explicit bit permutation, and saves both fifteen-entry inverse lists. Their intersection is empty.

The B graph checker was read line by line and freshly recompiled with `g++ -O3 -std=c++17`, with assertions enabled. The saved `T15_CORE0_FULL_B_check.cpp` is the existing independent graph-path checker with only the core loop restricted to 0 and exception output paths changed to this audit's prefix. It reads all thirteen original binary tables, transforms their negative lists, constructs the multigraph including parallel edges and loops, traverses degree-one paths, and rejects any unvisited closed component. It does not reuse the producer suppression formula or producer prepared negative lists.

| Re-executed finite domain | Count | Result |
|---|---:|---|
| c1 B partial matchings | 135135 | Exactly six zero masks; other masks 1:10425, 2:10425, 3:114279 |
| c3 B partial matchings × partner orders | 270270×6=1621620 | No zero mask; every observed mask has at least two good pairings for one bridge |
| c1 complete residual Q5 inputs | 6×13×10395=810810 | Every positive cycle certificate passes |

The residual checker source `verify_t15_r3_small_core0_c1_residual.cpp` was likewise read and freshly compiled to `T15_CORE0_FULL_residual_check.exe`; its output is `T15_CORE0_FULL_residual_check.json`. It enumerates expected inputs itself, rather than checking only records supplied by the search. Its required-edge count check is sound because the certified cycle is simple and each of the thirteen distinct required undirected edges can occur at most once. The certificate SHA256 is `4764b5f4d0252e5bcfc1a09c87c79a8c86bd1c1c56d88a31b72b323d3c5902b6`.

The residual global labels 2v+1 for A and 2v for B move the deleted coordinate into bit 0. This is a coordinate permutation of Q5, preserving all short adjacencies and arbitrary prescribed edges. In these labels the original holes are {0,1,2,7,11,14} and omitted vertices {1,2}; applying the inverse permutation gives exactly the theorem's geometry and omissions.

## Counterexample and closure pass

I checked empty/repeated forbidden families, maximal c=13, zero internal matching, both bridge-port statuses, c1 occupied loops, and disconnected or parallel-edge B components. The quantifier audit explicitly rejects prescribing an arbitrary R; only N14's ∀D∃R connected response is used. No asymptotic estimates, limit interchanges, measure-theoretic arguments, or hidden constants occur.

An additional deterministic counterexample pass fixes canonical D containing zd=01 and enumerates **all** R for boundary sizes 4,6,8,10,12,14. For each connected R∪D it independently forms the occupied quotient by suppressing z,d and checks Q∪D' connected. The connected counts are respectively 2,8,48,384,3840,46080; zero failures. Relabeling D justifies the canonical choice; this pass supplements, rather than replaces, MC6's graph proof.

The crossing cases partition the entire domain. Every N14 application discharges the same-parity-hole and arbitrary-matching hypotheses; every balanced-table application has exactly the declared six-edge support; every expansion discharges disjointness and support. No issue or scope-changing fix remains. The semantic acceptance is provisional within the same model family, with the N14/table imports explicitly retained; the new finite checks are deterministic and reproducible.
