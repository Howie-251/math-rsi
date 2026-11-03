# Non-normal H in the binary AGL(1,7) tower: balanced profile

The six-colour-allocation profile is complete: 200 inputs in each allocation, 1200 legal HH-covered candidates, and actual three-root BFS for every candidate. No diameter-5 graph was found. No production enumeration has started; cursor 1200 is the end of this authorized sample, not a cursor into the 76,384,728-input normalized family.

## Actual construction

Use F8=F2[t]/(t³+t+1), with ζ=t encoded 2, and A=F8². Encode `(u,v)` by `x=u+8v`. Encode K coordinates `(a,b,e)∈Z7×Z3×Z2` by `a+7b+21e`. Multiplication is

    (a,b,e)(c,d,f) = (a+(-1)^e 2^b c mod7, b+d mod3, e+f mod2).

To act on `(u,v)`, first exchange u,v if e=1, then return

    (ζ^a u^(2^b), ζ^(-a) v^(2^b)).

For G=A⋊K, use `(x,k)(y,l)=(x XOR k(y),kl)` and inverse `(k^-1(x),k^-1)`. The code is `x+64*k`. This action has no nonzero vector fixed by all K. H consists of a=0 and has order 6; it is not normal.

Actual labels and edges are:

| Layer | Label | Count |
|---|---|---:|
| Leaf (x,k) | x+64*k | 2688 |
| Block (x,a) | 2688+x+64*a | 448 |
| Head x | 3136+x | 64 |

Right multiplication by H leaves `(x,a)` unchanged. A leaf connects to this block, a block to its head, and leaf g to g*s for six distinct nonidentity inverse-closed generators. The graph has 3200 vertices and 11200 edges and is 7-regular. No alternative normal-H parent labels were used.

The actual group, action, inverses, and right-coset checks are implemented in `prepare_profile.py` and saved in `profile_structure.json`. All involution lists and all vector orbits agree individually with the source agent's pre-existing `STRUCTURE_CHECK.json`; inverse-pair counts agree as well. There are 119 nonidentity involutions and 1284 inverse pairs, including the zero-vector class.

Left G action preserves the graph and is transitive on each layer. Therefore roots 0, 2688, 3136 give exact missing counts for the full graph, weighted by 2688,448,64. The number of unordered pairs at distance greater than 5 is

    (2688*m_leaf + 448*m_block + 64*m_head)/2.

## Scope and input selection

The four nonzero horizontal K-orbits are:

| Name | Size | Involutions | Inverse pairs |
|---|---:|---:|---:|
| O7: uv=1 | 7 | 14 | 140 |
| O14: exactly one coordinate nonzero | 14 | 14 | 287 |
| O21a: uv∈{ζ,ζ²,ζ⁴} | 21 | 42 | 420 |
| O21b: uv∈{ζ³,ζ⁵,ζ⁶} | 21 | 42 | 420 |

Two inverse pairs and two involutions provide four components, so HH requires one component of each colour. For every choice of two involution colours, the other two colours supply the inverse pairs. Each of the six allocations receives 200 distinct component tuples, sampled without replacement using Python `random.Random` (MT19937), fixed seed **2026102607**. All actual indices and generators are preserved in `profile.inputs.jsonl`, making the saved input list authoritative independently of PRNG implementation details. All 1200 generator sets are distinct, legal, and directly checked for HH coverage.

No symmetry normalization was applied. In particular, no division by 6, no arbitrary K conjugation preserving a falsely fixed H, and no claim to cover the complete normalized family is made. The first sampled candidate is the explicit calibration graph and is also profile cursor 0. Its saved result is reused during profiling, so it is not scored a second time.

## Explicit first candidate

The first candidate is

    S=[21,24,1887,2532,1970,2331].

Full coordinates are in `preflight.parameters.json`; the complete graph is `preflight.edges`. Its two involutions have vector coordinates `(5,2)` and `(0,3)` and trivial K components. Actual complete three-root BFS gives eccentricities 6,7,6 and:

| Root layer | Target leaf | Target block | Target head | Total missing |
|---|---:|---:|---:|---:|
| Leaf | 106 | 9 | 5 | 120 |
| Block | 54 | 25 | 3 | 82 |
| Head | 210 | 21 | 0 | 231 |

The weighted count is 187,040 bad unordered pairs. The independent implementation reconstructed all 11200 edges exactly and checked all 3200 roots: simple, connected, 7-regular, diameter 7, 187,040 bad unordered pairs (224 at distance 7). Its masks have sizes 57 and 61, hence BB missing 25; all 448 target memberships agree. See `preflight.independent_check.json` and `preflight.independent_verify.json`. No second independent sample was requested.

## Nonnormal-H BB calibration

The implementation also computes the exact two-mask formula from `../NONNORMAL_BLOCK_CRITERIA.md`. Here K acts on the seven block positions by

    t -> a+(-1)^e 2^b t mod7.

Consequently its translation is T_a, and each nonzero multiplier has a unique H element L_c. For each word of length at most 3, the program accumulates R0 or the uniquely normalized R1, then adds both head-route terms P and Q. It predicts mask M0 at block position 0 and L_c M1 at each nonzero position c.

These masks are **never used to skip a candidate**. Each of the 1200 actual block-root BFS traversals was compared against every one of the 448 predicted target memberships: all 537600 comparisons matched. This is a new calibration of the nonnormal formula, not reuse of the former normal-H formula.

## Results by allocation

Each row contains 200 inputs. Minima in different columns need not occur at the same input. BL counts leaves missed by a block root; LL counts leaves missed by a leaf root. Head counts all target layers.

| Branch | Involution colours | Min LL | Min BL | Min BB | BB-zero inputs | Head-zero inputs | Best bad pairs |
|---|---|---:|---:|---:|---:|---:|---:|
| 0 | O7,O14 | 52 | 36 | 0 | 1 | 4 | 106848 |
| 1 | O7,O21a | 55 | 30 | 0 | 1 | 2 | 113568 |
| 2 | O7,O21b | 77 | 54 | 0 | 2 | 4 | 132160 |
| 3 | O14,O21a | 68 | 36 | 0 | 1 | 5 | 122304 |
| 4 | O14,O21b | 50 | 42 | 0 | 1 | 7 | 94976 |
| 5 | O21a,O21b | 46 | 42 | 2 | 0 | 7 | 104832 |

Global root minima are `[58,39,0]`, and zero counts are `[0,0,29]`. All 1200 LL and BL counts are nonzero. Six candidates achieve complete BB coverage; none of those six achieves complete head-root coverage. No candidate achieves simultaneous complete block-root and head-root coverage. The six actual BB survivors and their scores are retained in `profile.BB_pass.jsonl`.

All nine ordered root/target-layer minima and zero counts are in `profile.branch_summary.json`, alongside each branch's best candidate. Every actual score is in `profile.results.jsonl`; the unfiltered sample does not establish an impossibility theorem or a full-scope pass rate.

The best weighted candidate is cursor 955, branch 4:

    S=[24,1443,2185,2483,467,951],
    root missing=[58,71,35],
    root/target missing=[[50,8,0],[48,18,5],[0,35,0]],
    bad unordered pairs=94976.

Its complete edge list is `profile.best.edges`. This score uses actual BFS and the proven three-orbit reduction; no independent full-source acceptance of this second graph is claimed.

## Cost and terminal state

Preparation and compilation used 1.074039 CPU seconds, the first candidate 0.002125. The following process used 0.299169 CPU seconds for the 1199 new candidates plus reuse of cursor 0: construction took 0.065300 and BFS plus algebraic BB calibration 0.213412. Driver-inclusive recorded cumulative cost is **1.387779 CPU seconds**, below the 60-second one-worker budget.

The measured unfiltered rate is about 0.250 ms per newly evaluated candidate, including actual graph construction, three BFS traversals, and BB membership comparison. It does not measure a standalone optimized BB frontend. No large-family timing claim is inferred from this sample.

The terminal status is `PROFILE_COMPLETE`, cursor 1200, no running process, and no production continuation. `terminal.json` and `profile.terminal.json` preserve the actual counts. The requested first-candidate independent check is complete. Subsequent production, if separately authorized, starts a new enumeration cursor and does not treat this random sample as a prefix.
