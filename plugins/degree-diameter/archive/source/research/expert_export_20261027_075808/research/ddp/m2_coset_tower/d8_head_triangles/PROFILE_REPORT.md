# d8 tower with head triangles: construction and bounded profile

The actual engine, one complete sample, and all **1200** authorized balanced profile inputs are complete. No diameter-5 graph was found. All candidates received real three-root BFS, with the new triangle edges present. No complete-family production or route-formula filtering was started.

## Actual group and graph

Let A=F7²×C3 and encode `(u,v,w)` by `x=u+7*v+49*w`. Addition is componentwise modulo 7,7,3; it is not XOR. Write K coordinates `(b,j)∈F7×Z6`, encoded `b+7*j`, with

    (b,j)(d,l)=(b+4^j*d mod7,j+l mod6),
    (b,j)^-1=(-4^(-j)*b mod7,-j mod6).

K acts by

    (u,v,w) -> (3^(5j)*u+b*3^j*v mod7,3^j*v mod7,w).

The semidirect product uses `(x,k)(y,l)=(x+k(y),kl)` and inverse `(-k^-1(x),k^-1)`. In particular, the inverse negates w modulo 3. All 6174 group inverse identities and 259308 K action-composition identities were checked. The actual tables and encoding are saved in `structure.json`.

H consists of `(b,0)` and has order 7. Right multiplication by H leaves j unchanged. The graph labels are:

| Layer | Label | Count |
|---|---|---:|
| Leaf (x,k) | x+147*k | 6174 |
| Block (x,j) | 6174+x+147*j | 882 |
| Head x | 7056+x | 147 |

Leaf g is joined to g*s for each of seven distinct nonidentity inverse-closed generators, and to its block. A block is joined to its head. For each of the 49 fixed `(u,v)` pairs, the three heads with w=0,1,2 form K3. These are 147 extra head edges. Each leaf has seven leaf neighbours and one block neighbour; each block has seven children and one head; each head has six blocks and two triangle neighbours. The actual graph is therefore 8-regular on **7203** vertices, with **28812** edges.

Left G action preserves all edges, including the head triangles: it applies one affine transformation to `(u,v)` and shifts every w in a triangle equally. It is transitive on each of the three vertex layers. Roots 0,6174,7056 therefore give exact full-graph missing counts, and the unordered count is

    (6174*m_leaf+882*m_block+147*m_head)/2.

The independent mathematical derivation and the complete scope are in `STRUCTURE_SCOPE.md`, which was read in full for this report. No original-head or old-BB formula was silently applied to the modified graph.

## Normalized scope and sampled inputs

At each w, the nonzero field vectors have two K-orbits: the axis `(u,0),u≠0`, of size 6, and the off-axis `v≠0`, of size 42. The new head triangles supply only the two zero-field, nonzero-w head differences. Complete HH coverage therefore forces exactly two cross inverse pairs, one of each field colour, with unique w=1 representatives; the other three generators have w=0 and cover both colours.

The proven simultaneous upper-triangular change of field coordinates, with the associated conjugation of K, normalizes the two w=1 field vectors to `(1,0)` and `(0,1)`. Their K coordinates are still independently arbitrary among 42 choices. The internal three generators form either one inverse pair plus one involution or three involutions.

Actual internal lists, derived using the true group inverse, are:

| Field class | Involutions | Noninvolution inverse pairs |
|---|---:|---:|
| Zero | 1 | 20 |
| Axis | 6 | 123 |
| Off-axis | 42 | 861 |

The five internal allocations, their complete normalized input counts, and the actual bounded sample are:

| Branch | Internal composition | Internal choices | Full choices including cross K coordinates | Profile |
|---|---|---:|---:|---:|
| 0 | Axis pair + off-axis involution | 5166 | 9,112,824 | 300 |
| 1 | Off-axis pair + axis involution | 5166 | 9,112,824 | 300 |
| 2 | Two axis involutions + one off-axis | 630 | 1,111,320 | 200 |
| 3 | One axis involution + two off-axis | 5166 | 9,112,824 | 200 |
| 4 | Axis + off-axis + zero involutions | 252 | 444,528 | 200 |
| Total | | 16380 | **28,894,320** | **1200** |

Only the final column was evaluated. `internal_options.json` preserves the small internal lists, not an enumeration of the full graph family. Each branch was sampled without replacement using Python `random.Random` (MT19937), seed **2026102608**. Its two cross K codes and internal option index were chosen independently and saved. All 1200 actual generator sets are distinct, legal, inverse-closed, and HH-covered. The authoritative explicit list is `profile.inputs.jsonl`; `profile_metadata.json` gives the selection rule.

This balanced allocation is not a uniform statistical sample of the full family. No pass-rate or impossibility conclusion for the unevaluated inputs is inferred. Sample cursor 0 is also the one independently submitted calibration graph; its saved score was reused, so no duplicate sample BFS was performed.

## First actual graph

The first generator set is

    S=[344,839,1526,5406,2,5,3100].

Full coordinates appear in `preflight.parameters.json`, and the entire edge list is `preflight.edges`. Complete BFS from the three orbit roots gives eccentricities `[7,7,7]` and:

| Root layer | Missing leaf | Missing block | Missing head | Total |
|---|---:|---:|---:|---:|
| Leaf | 3361 | 377 | 37 | 3775 |
| Block | 2639 | 406 | 58 | 3103 |
| Head | 1554 | 348 | 0 | 1902 |

The weighted count is **13,161,645** bad unordered pairs. The independent implementation reconstructed every edge exactly, including the 147 head-triangle edges. The generic checker checked all 7203 roots: simple, connected, 8-regular, **diameter 7**, with exactly **13,161,645** bad unordered pairs. See `preflight.independent_check.json` and `preflight.independent_verify.json`. The independent six-mask BB formula also matched all 882 targets individually, with BB missing 406. No second graph was submitted for duplicate calibration.

## Completed profile

Every one of the 1200 candidates received actual three-root depth-five BFS, including the new head triangle edges. Cursor 0 used its already saved complete BFS result; the profile process performed 1199 new evaluations. No old or newly derived route criterion was used to skip any candidate.

| Branch | Minimum LL missing | Minimum BL missing | Minimum BB missing | Minimum head-root missing | Best bad-pair count |
|---|---:|---:|---:|---:|---:|
| 0 | 391 | 329 | 40 | 132 | 1,609,650 |
| 1 | 349 | 196 | 51 | 120 | 1,370,628 |
| 2 | 1070 | 497 | 111 | 144 | 3,900,204 |
| 3 | 838 | 322 | 57 | 30 | 3,082,149 |
| 4 | 1196 | 518 | 117 | 282 | 4,341,645 |

Minima in different columns can occur at different inputs. Global root minima are `[395,286,30]`; all three root-zero counts are zero, and simultaneous head/block coverage is zero. All 1200 BB tests fail, and every LL and BL count is positive. One branch-3 sample covers all LH pairs; otherwise every non-HH pairing type retains a positive missing count in every sample. These are observations about this saved 1200-input profile only.

The best weighted candidate is cursor 358, branch 1:

    S=[1961,5541,938,293,1188,5896,3088],
    root missing=[400,286,132],
    missing by root/target layer=[[368,31,1],[217,54,15],[42,90,0]],
    bad unordered pairs=1370628.

The complete graph is `profile.best.edges`; its score is from actual BFS and the established three-orbit reduction, without a separate full-source check of this second graph. All scores and all nine root/target-layer minima and zero counts are preserved in `profile.results.jsonl` and `profile.branch_summary.json`.

## Budget and terminal scope

Preparation plus compilation took 1.015710 CPU seconds, the first actual sample 0.004533. The profile process took 0.695943 CPU seconds, including 0.297008 for construction and 0.338331 for BFS. The driver-inclusive cumulative charge is **1.732226 CPU seconds**, below the 60-second one-worker budget. The measured process cost is about 0.580 ms per newly evaluated sample, but it does not measure a six-mask BB frontend or predict the full normalized enumeration cost.

The terminal status is `PROFILE_COMPLETE`, cursor **1200**, with no running process and no production started. The independently proved complete 28,894,320-input scope is retained for a later decision; it has not been executed or computationally excluded. The previous d7 zero/one-pair families remain unchanged and were not reopened by this task.

The unique independent sample check used 0.08571051499999999 Python CPU seconds plus 1.831722 checker seconds. Including it, the cumulative recorded charge is **3.6496585149999996 seconds**. All requested sample validation is complete; there is no pending independent check.
