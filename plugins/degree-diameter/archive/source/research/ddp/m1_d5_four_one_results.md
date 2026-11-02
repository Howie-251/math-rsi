# Degree 5, diameter 5: completed 4+1 inverse-pair families

All four authorized finite families were completed without a diameter-5 graph. The independent all-root checks confirm that the best saved graph in each family has diameter 6. These results concern the specified two-orbit 4+1 construction with two noninvolutory inverse pairs on each side; they do not exclude other allocations, involution branches, groups, or arbitrary graphs.

## Construction and exact reduction

Use `G=F_p ⋊ C_m`, with multiplication `(x,i)(y,j)=(x+r^i y,i+j)`. Vertices are `(0,g),(1,g)`. The positive generator coordinate order is **`(a,c,b,d)`**. Internal sets are `A={a,a^-1,c,c^-1}` and `B={b,b^-1,d,d^-1}`, and `(0,g)` is joined to `(1,g)` by the only cross edge. Legality requires four distinct nonidentity internal neighbors on each side. Thus every generator is nonidentity and noninvolutory, `a` differs from both `c` and `c^-1`, and `b` differs from both `d` and `d^-1`. Equal quotient residues alone do not imply an illegal collision.

A single original cross voltage `s0` can be normalized to identity by changing the second fiber coordinate; its internal set becomes `s0 B s0^-1`. Once the cross set is identity, a common group automorphism on both sides preserves it. Conjugation by `(u,0)` adds `u*(1-r^i)` to the translation of a generator with quotient residue `i`. At a fixed quotient skeleton generating `C_m`, this vector is nonzero. Set its first nonzero coordinate to zero by conjugation, then scale the remaining three coordinates so their first nonzero value is one. This gives `p^2+p+1` nonzero projective representatives. The excluded zero class generates a subgroup contained in a conjugate of `C_m`, so its lift cannot be connected. The root's quotient skeleton files account for generator inversion, exchanges within a side, exchange of the sides, and compatible quotient units. There is no cross-anchor choice in 4+1.

Left multiplication by any element of `G` preserves every edge and is transitive on each side. Hence complete depth-5 BFS at `(0,e)` and `(1,e)` exactly decides diameter at most 5. For missing counts `s0,s1`, the number of bad unordered vertex pairs is `|G|*(s0+s1)/2`.

## Completed counts and minima

| `(p,m,r)` | Vertices | Skeletons | Projective representatives | Legal fully scored | Illegal | Minimum `s0+s1` | Best bad pairs |
|---|---:|---:|---:|---:|---:|---:|---:|
| `(13,27,3)` | 702 | 605 | 110715 | 106140 | 4575 | 32 | 5616 |
| `(109,3,45)` | 654 | 5 | 59955 | 58212 | 1743 | 124 | 20274 |
| `(41,8,3)` | 656 | 99 | 170577 | 80870 | 89707 | 41 | 6724 |
| `(37,9,7)` | 666 | 114 | 160398 | 154107 | 6291 | 4 | 666 |

All **823 skeletons**, **501645 projective representatives**, and **399329 legal candidates** were completed. The **823 zero classes** were excluded separately. The illegal categories, with priority identity, then nonidentity involution, then same-side inverse-pair collision, totaled 9179, 85104, and 8033. The involution count occurs entirely for `m=8`; the generator residue 4 is rejected for every translation.

Every legal candidate was fully scored. The recorded minimum is therefore global over the input finite family, not just a lower bound from early rejection. The batch used a single CPU sequentially and ended normally in **5.640123 child CPU seconds**, about **5.690 wall seconds**, within the cumulative 120-second limit. No additional groups, trajectories, or budget extensions were used.

## Exact best graphs

All arrays below use `(a,c,b,d)` order.

| `(p,m,r)` | Quotient residues | Translation values | Root missing counts |
|---|---|---|---|
| `(13,27,3)` | `(1,2,7,10)` | `(0,1,9,7)` | `(16,16)` |
| `(109,3,45)` | `(0,1,0,1)` | `(1,0,9,6)` | `(63,61)` |
| `(41,8,3)` | `(1,2,3,3)` | `(0,1,21,5)` | `(26,15)` |
| `(37,9,7)` | `(0,1,4,4)` | `(1,0,21,15)` | `(3,1)` |

The existing independent verifier parsed each saved full edge list and performed unrestricted BFS from every vertex. All four are simple, connected, 5-regular, and have diameter exactly 6. The full bad-pair counts equal the table. In particular the 666-vertex graph with only four representative misses is still not a successful diameter-5 construction.

## Implementation checks

The separate `search_4plus1.cpp` keeps the original 2+3 source and evidence unchanged. An independent Python generator inserts forward positive-generator edges as unordered pairs, thereby obtaining inverse edges without using the C++ inverse table.

For `F_7 ⋊ C_3` and `F_5 ⋊ C_4`, the regression checked 295 projective representatives across seven test skeletons. All raw translation vectors were independently normalized: every zero class had `p` vectors and every nonzero projective class had `p*(p-1)`. Legality by actual degrees and loops agreed with the algebraic rejection categories. For all 186 legal small graphs, independent BFS from every vertex agreed with the C++ score histogram; the C++ saved edge lists exactly matched the independent generator. These include identity, involution, and inverse-pair collision rejections. The separately specified positive control `a=(0,1),c=(1,0),b=(1,1),d=(2,0)` over `F_7 ⋊ C_3` has 42 vertices, degree 5, and diameter 3.

A negative control used the authorized old group `13,27,3` at quotient skeleton `(1,4,2,4)`. All 183 projective representatives were legal; independent graph generation and two-root BFS matched the entire C++ score histogram, whose minimum was 90. Its best edge list also passed an independent full 702-root check with diameter 6 and 15795 bad pairs. Thus both acceptance and failure paths were exercised before the production batch.

## Evidence and reproduction

All code and data are in `computations/ddp/m1/d5_four_one/`:

- `search_4plus1.cpp` / `search_4plus1`: independent 4+1 implementation.
- `check_implementation.py`, `regression/check.json`: the stated implementation controls, with exact histograms and negative-control all-root check alongside.
- `batch.json`, `*.skeletons.txt`: root-generated quotient representatives and orbit-closure metadata.
- `run_batch.py`, `batch_results.json`: cumulative one-CPU 120-second execution and actual terminal results.
- Per-case prefix `pP_mM_rR.search`: `.summary.json`, `.skeleton_results.jsonl`, `.best.json`, `.best.edges`, `.best.independent_bfs.json`, and `.log`.

The executable takes `P M R SKELETONS SECONDS OUTPUT_PREFIX`, and stops on a successful graph. The optional final argument `full` is used only for small regression so positive controls can have complete histograms. Production calls omitted it. Every per-skeleton completion and count was reconciled with its summary. No process remains active.
