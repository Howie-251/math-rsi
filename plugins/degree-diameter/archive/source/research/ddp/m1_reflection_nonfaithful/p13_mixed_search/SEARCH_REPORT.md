# Complete `(13,28,5)` mixed reflection enumeration

The prescribed **48 quotient skeletons and all 105,456 translation tuples
were completed**, with no diameter-5 solution. All tuples were legal. Search
CPU time was **1.669478 seconds** as measured by the child-process resource
counter, within the 30-second limit; exactly one worker ran. The per-skeleton
records and overall terminal have no unfinished cursor (`next_skeleton_id=48`,
`next_assignment_index=0`). No `(17,24,2)` or `(29,12,12)` search was launched.

The best two-root missing sum is **29**, attained by two enumerated tuples.
The first saved best has:

- quotient `(beta,sigma,tau)=(1,5,17)`;
- variables `(b_x,s_x,t_x)=(9,8,5)`;
- `A={(0,14),(1,14)}`;
- `B={(9,1),(6,27)}`;
- `S={(0,0),(8,5),(5,17)}`;
- orbit-root missing counts **18 and 11** beyond distance 5;
- **5,278 unordered bad pairs**, since each orbit has 364 vertices.

An independent agent ran the existing generic checker on the complete edge
list. It confirmed **728 vertices, 1,820 edges, simple connected 5-regular,
diameter 6 and 5,278 unordered bad pairs**, by BFS from **all 728 vertices**.
The checker reported 0.01058 seconds and returned exit code 1, meaning that
the graph fails the requested diameter-5 condition, not an execution error.
The result is saved as `best.independent_verify.json`.

## Implementation and preflight

`search_reflections.cpp` is an unchanged copy of the already regressed F41
program. It already accepts p, m and r at runtime. Its group check requires
`r^m=1` and `r^(m/2)=-1`, not a faithful action. It allocates multiplication,
adjacency and BFS vectors from `q=p*m` and `n=2*q`; the unsigned-short vertex
bound 65,535 safely contains n=728. Fewer than 211,000 BFS stamps are used, so
the unsigned stamp range is also sufficient. No parameterization change was
needed.

The full enumeration visits every code `0..13^3-1` and decodes its three
base-13 digits as `(b_x,s_x,t_x)`. Zero coordinates are included. No further
projective normalization, residual reflection symmetry, or side swap is
applied. All 48 skeletons have nonzero B quotient and three distinct cross
quotients, so every tuple is legal; the observed count agrees exactly with
the capacity metadata.

Before production, exactly two explicit assignments at quotient `(1,1,6)`
were expanded by the C++ code and separately by direct Python group
multiplication. Their full edge sets matched. Each C++ two-root score and
diameter then agreed with the existing independent generic checker, which
parses the saved edge list and runs BFS from all 728 vertices:

| `(b_x,s_x,t_x)` | Two-root missing counts | Diameter | Unordered bad pairs |
|---|---|---:|---:|
| `(0,0,0)` | 412, 424 | 8 | 152,152 |
| `(4,7,12)` | 72, 64 | 6 | 24,752 |

The generic checker's bad-pair semantics are unordered pairs with distance
greater than 5, including unreachable pairs; both preflight graphs were
connected and 5-regular. This was a small parameter compatibility check, not
a repeated regression suite. Compilation used 1.175459 CPU seconds and the
two preflight cases plus independent checks used 0.034272 CPU seconds.

## Scope of the negative result

The preceding capacity diagnosis already excluded the other 255 of 303
canonical mixed skeletons for this parameter group. Completing every legal
translation assignment on the remaining 48 therefore excludes diameter 5
throughout this normalized mixed family. The both-reflection branch for the
same group was previously excluded by quotient walk capacity alone. These
are finite family results; they do not establish a general degree-diameter
upper bound.

Saved files include the unchanged C++ source and local executable,
`run_profile.py`, `preflight.json` and its two complete edge lists,
`production.log`, `complete_mixed.skeleton_results.jsonl` with every
skeleton's histogram and count, `complete_mixed.summary.json`,
`complete_mixed.best.json`, `complete_mixed.best.edges`, and `terminal.json`.
All writes for this batch are inside this directory. The capacity records,
Wiki and HTML were not modified.
