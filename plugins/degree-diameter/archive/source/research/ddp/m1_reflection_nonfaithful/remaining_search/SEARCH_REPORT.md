# Remaining nonfaithful reflection ranges: complete enumeration

All three authorized branches completed, with **no diameter-5 solution**.
The single worker visited **3,332,186 raw translation tuples**, fully scored
all **3,273,316 legal tuples**, and used **49.79 cumulative CPU seconds**,
including orchestration, within the shared 120-second limit. The branches
ran sequentially in the prescribed order. No restart or additional parameter
range was run.

| Branch | Graph order | Skeletons completed | Raw tuples | Legal tuples | Minimum two-root missing sum | Search child CPU seconds |
|---|---:|---:|---:|---:|---:|---:|
| `(17,24,2)` mixed | 816 | 157 | 771,341 | 771,341 | 48 | 13.306220 |
| `(29,12,12)` mixed | 696 | 47 | 1,146,283 | 1,136,191 | 25 | 16.402410 |
| `(29,12,12)` both | 696 | 2 | 1,414,562 | 1,365,784 | 26 | 20.044099 |

Every count agrees with the existing capacity metadata. All branch terminals
are `COMPLETE_NO_SOLUTION` and certify that their minimum score is global
over the supplied skeletons. Their cursors are `(157,0)`, `(47,0)` and `(2,0)`
respectively, meaning the next skeleton is beyond the complete input and no
assignment is unfinished. The best scores occur in 2, 2 and 4 assignments
respectively; the first best edge list was retained in each case.

## Saved best graphs

| Branch | Quotient `(beta,sigma,tau)` | Translation coordinates | Two-root missing counts | Unordered bad pairs |
|---|---|---|---|---:|
| p17 mixed | `(9,1,10)` | `(b_x,s_x,t_x)=(16,11,12)` | 27, 21 | 9,792 |
| p29 mixed | `(1,3,7)` | `(b_x,s_x,t_x)=(18,2,8)` | 13, 12 | 4,350 |
| p29 both | `(6,1,4)` | `(b_x,d_x,s_x,t_x)=(27,20,3,7)` | 12, 14 | 4,524 |

Their concrete labels under `(x,i)(y,j)=(x+r^i*y,i+j)` are:

- p17 mixed: `A={(0,12),(1,12)}`, `B={(16,9),(9,15)}`,
  `S={(0,0),(11,1),(12,10)}`.
- p29 mixed: `A={(0,6),(1,6)}`, `B={(18,1),(13,11)}`,
  `S={(0,0),(2,3),(8,7)}`.
- p29 both: `A={(0,6),(1,6)}`, `B={(27,6),(20,6)}`,
  `S={(0,0),(3,1),(7,4)}`.

The complete edge lists are `p17_mixed/search.best.edges`,
`p29_mixed/search.best.edges` and `p29_both/search.best.edges`. After all
searches stopped, the independent source agent ran the existing generic
all-source BFS checker once per graph, sequentially. All three are **simple,
connected, 5-regular graphs of diameter 6**. The checks visited all **816,
696 and 696 roots**, respectively, and independently confirmed exactly
**9,792, 4,350 and 4,524 bad unordered pairs**. Results are saved in each
branch's `best.independent_verify.json`. Check times were approximately
0.01608, 0.01119 and 0.01097 seconds. Each checker exit code 1 means failure
of the requested diameter-5 condition, not an execution error.

## Range preservation and legality

The run reuses the unchanged executable and C++ source from the completed
`p13_mixed_search` batch. Its parameter compatibility, including nonfaithful
actions and zero translations, was already checked there. No broad
regression suite was repeated and no new implementation normalization was
introduced.

Before searching, `run_remaining.py` compared each exact skeleton list with
`profile_metadata.json`, checked quotient connectivity, and independently
recomputed the declared legal counts using the closed counting formulas.
It enumerated the full `F_p^3` or `F_p^4` coordinate domain for every listed
skeleton. No zero-coordinate exclusion, extra projective scaling, mixed
side exchange, or residual translation symmetry was applied.

The legal rejection totals were:

- p17 mixed: 0.
- p29 mixed: 3,364 identity internal labels and 6,728 cross-label collisions,
  totaling 10,092. There were no involutory mixed pairs in the range.
- p29 both: 48,778 duplicate reflection pairs and no other rejections.

Those are exactly the stated graph legality constraints. All accepted
assignments were fully scored from the two orbit roots. A left group action
is transitive on each orbit even for a nonfaithful semidirect action, so
two-root coverage is the exact diameter-5 criterion. The independent saved
edge-list checks do not rely on that group argument.

The wrapper maintained one CPU affinity, charged its own CPU time and all
child CPU time against a cumulative 120-second budget, and supplied each
branch only the remaining allowance with a timer margin. Stop-on-zero was
enabled in every branch, so a D5 hit would have saved the complete graph and
halted subsequent branches. No hit or budget boundary occurred.

## Consequence and material

Together with the preceding finite capacity exclusions, these complete
translation enumerations rule out diameter 5 in the normalized two-orbit,
internal-degree-2 / cross-degree-3 families with a two-reflection A for
`(17,24,2)` and `(29,12,12)`. The p17 both branch had already failed capacity
for every skeleton. The analogous `(13,28,5)` family was completed earlier.
This closes the three specified reflection-family ranges, not other groups,
other internal A types, or general degree-diameter constructions.

`scope.json` preserves the exact approved ranges and expected counts.
`terminal.json` combines the branch results and cumulative budget usage.
Each branch retains its run log, per-skeleton complete histograms and counts,
overall summary, best parameters, complete edge list and terminal. The
wrapper and unchanged source/executable are stored in this directory.
All writes stayed here; the capacity records, Wiki and HTML were unchanged.
