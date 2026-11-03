# d8 binary AGL(1,8) tower: actual construction and bounded profile

The requested structure, one explicit HH-covered sample, and 2000 HH-covered cost-profile candidates are complete. No diameter-5 graph was found. This was a finite sampled path with a fixed allocation of generator colours, **not a complete search of the family**. No production enumeration has started.

## Actual group, labels, and edges

Use F8 = F2[t]/(t³+t+1), polynomial binary 11. A vector is an even-weight 8-bit mask on field coordinates 0,…,7. Encode it by `x=mask>>1`; recover `mask=(x<<1)|parity(x)`. In this encoding vector addition is bitwise XOR.

K is AGL(1,8). Encode the map `t -> a*t XOR b`, with a=1,…,7 and b=0,…,7, by `k=b+8*(a-1)`. Thus

    (a,b)(c,d) = (a*c, a*d XOR b),
    (a,b)^-1 = (a^-1, a^-1*b).

K acts on A by moving each coordinate bit t to a*t XOR b. For the semidirect product G=A⋊K,

    (x,k)(y,l) = (x XOR k(y), k*l),
    (x,k)^-1 = (k^-1(x), k^-1).

The group code is `x+128*k`. The actual tables are in `structure.json`; generator lists, using the actual inverse, are in `generator_lists.json`. All 7168 inverse identities and all K action-composition identities were checked. H consists of b=0 and has order 7. **H is not normal.** No normalization by arbitrary K conjugation was used.

Vertex labels are:

| Layer | Label | Count |
|---|---|---:|
| Leaf (x,k) | x+128*k | 7168 |
| Block (x,b) | 7168+x+128*b | 1024 |
| Head x | 8192+x | 128 |

The right H-coset label is `(x,k(0))=(x,b)`. Each leaf is joined to its block, each block to its head, and leaf g to g*s for the seven generators s∈S. Seven distinct nonidentity inverse-closed generators give seven distinct leaf neighbours. Every block has seven leaf children, every head eight block children. The actual graph has 8320 vertices and 33280 edges and is 8-regular.

Left G action preserves every edge and is transitive on each layer. On blocks it acts by `(z,k):(x,b)->(z XOR k(x),k(b))`; on heads it acts by `x->z XOR k(x)`. Consequently roots 0, 7168, 8192 give exact missing counts for all three orbits. The full number of unordered pairs farther than 5 is

    (7168*m_leaf + 1024*m_block + 128*m_head)/2.

No old normal-H BB formula or quotient-LL substitution is used by the evaluator. It constructs the actual graph and runs three BFS traversals.

## HH colours and tested scope

Two distinct heads can meet within five steps exactly when some generator translation component has their difference in its K orbit. Thus HH coverage is precisely coverage of all five nonzero A-orbits. Actual counts agree with the independent mathematical classification:

| Vector colour | Orbit size | Nonidentity involutions | Noninvolution inverse pairs |
|---|---:|---:|---:|
| Zero | 1 | 7 | 24 |
| All ones | 1 | 8 | 24 |
| Plane of size 4 | 14 | 56 | 364 |
| Weight 2 | 28 | 56 | 756 |
| Weight 6 | 28 | 56 | 756 |
| Nonplane of size 4 | 56 | 56 | 1540 |
| Total | 128 | 239 | 3464 |

The sample and profile use two inverse pairs, respectively of weight 2 and nonplane weight 4, and three involutions, respectively all-ones, plane weight 4, and weight 6. This ensures HH coverage. It does not exhaust the other allocations of two pairs and three involutions, or the one-pair/five-involution and seven-involution patterns.

All component lists are in increasing minimum element-code order. For cursor j=0,…,1999, the five list indices are

    j mod 8,
    (13*j+7) mod 56,
    (23*j+19) mod 56,
    (17*j+31) mod 756,
    (37*j+5) mod 1540.

Each input was checked for seven distinct nonidentity generators, inverse closure, and actual HH coverage. All 2000 generator sets are distinct. This explicit deterministic path is a cost profile, not a random sample or a symmetry-complete enumeration. `profile.inputs.jsonl` and `profile_metadata.json` preserve its exact scope.

## One explicit sample

`preflight.parameters.json` gives all coordinates. The seven group codes are

    [255,263,254,1153,4752,1291,4237].

The three involutions are `(mask,a,b)=(255,1,1),(15,1,2),(252,1,1)`; inverse-pair representatives are `(3,2,1),(23,2,2)`. The other two generators are their actual group inverses.

The complete edge list is `preflight.edges`. Three complete root BFS traversals give eccentricities 6,6,6 and the following missing counts at distance greater than 5:

| Root layer | Target leaf | Target block | Target head | Total |
|---|---:|---:|---:|---:|
| Leaf | 1347 | 197 | 19 | 1563 |
| Block | 1379 | 217 | 28 | 1624 |
| Head | 1064 | 224 | 0 | 1288 |

The weighted bad-pair count is 6,515,712. The independent implementation reconstructed all 33280 edges exactly and checked all 8320 roots: the graph is simple, connected, 8-regular, has diameter 6, and has exactly 6,515,712 bad unordered pairs. See `preflight.independent_check.json` and `preflight.independent_verify.json`. The independent nonnormal-H criterion has |M0|=72 and |M1|=105, giving BB missing 217; it matches all 1024 block targets individually. No other sample was submitted for duplicate full-source calibration.

## Completed profile and cost

All 2000 inputs were legal, all passed HH, and all received actual three-root BFS evaluation. The next cursor is 2000; no further input is authorized or running.

| Metric | Result |
|---|---:|
| Minimum leaf-root missing | 438 |
| Minimum block-root missing | 329 |
| Minimum head-root missing | 56 |
| Leaf/block/head zero counts | 0 / 0 / 0 |
| Simultaneous block+head zero | 0 |
| Minimum BB missing, extracted from saved BFS results | 21 |
| BB-full candidates among these 2000 | 0 |
| Best weighted bad-pair count | 1,802,752 |

These minima need not occur at the same input. The best weighted candidate is cursor 332:

    S=[639,97,508,2344,6034,4025,6618],
    root missing=[438,406,392],
    missing by root/target layer=[[384,47,7],[329,77,0],[392,0,0]].

Its complete graph and parameters are `profile.best.edges` and `profile.best.json`. No independent full-source claim is made for this second graph; its score is from the proven three-orbit reduction and the actual evaluator.

Preparation and compilation took 0.852195 CPU seconds; the explicit sample 0.005313; the 2000-candidate process 1.296870, including 0.545196 for construction and 0.660744 for BFS. The driver-inclusive cumulative charge is **2.156896 CPU seconds**, below the 60-second, one-worker limit. The measured process cost is about 0.648435 ms per candidate, or 648 CPU seconds per million at this unfiltered implementation's measured rate. This is a cost estimate, not authorization or a forecast for a proposed complete scope.

`terminal.json`, `profile.terminal.json`, and `profile.results.jsonl` preserve the terminal status, cursor, and every actual score. No further search, new parameter, old-sample rerun, or production batch was started. The new nonnormal-H BB criterion developed by the parent and mathematical checker was not needed or applied during this profile.

The independent sample check used 0.09702522000000001 Python CPU seconds and 2.452369 checker seconds. Including it, the cumulative recorded charge is 4.70629022 seconds, still below the original limit.
