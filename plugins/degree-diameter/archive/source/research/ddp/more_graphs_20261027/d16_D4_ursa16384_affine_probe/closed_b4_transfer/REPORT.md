# Closed-b⁴ fixed GF(4) transfer: all 974 necessary tests fail

The original 650 assignments and the separately frozen 324-assignment
even-phase control were both completed. There were zero necessary
passers, zero strong full-rank certificates, zero untested assignments
and zero UNKNOWN results. No candidate graph was generated and no BFS
was performed.

All assignments retain the cached four global GF(4) relations and
base permutations alpha=(0 1 2 3), beta=(0 1 3 2). Their voltages are
va=(0,x,y,0), vb=(-1,0,0,1), with each x,y tried exactly once modulo m.
The full original order m17 then m19 was preserved; m18 was appended
as a distinct even-phase control before any evaluation. The two
prediction files record this scope change explicitly.

| Frozen group | Assignments | Simple controller | Repeated ports retained | Necessary passers | No unique rank-3 slot |
|---|---:|---:|---:|---:|---:|
| Original m17/19 | 650 | 614 | 36 | 0 | 126 |
| Separate m18 control | 324 | 306 | 18 | 0 | 61 |

There was no simple-controller filter: all 974 assignments were
retained. Parallel or repeated controller ports do not automatically
make the deduplicated lift illegal; the exact word-union necessary
test remains valid for them. The port inverse binding 0↔3,1↔2 was
inherited from the actual interface, and the controller transitions
were checked against that binding for every assignment.

The new structural rule achieved its intended local guarantee.
The voltage sum around b⁴ is zero at every base and sheet. Cached
words1111 and2222 have rank4. They therefore cover the entire same
fiber, for every fiber source vector, independently of singularity
of the individual canonical matrices. Every evaluated zero-source
self fiber was also checked full by the actual cached union.

For each assignment, all four source bases with fiber0 were tested.
Every test used the exact union of all 341 word images of length at
most4, including nonreduced/backtracking words, assigned to actual
controller endpoints. All assignments already fail at source base0;
the other three bases were nevertheless evaluated as frozen. A missing
point in this union is a genuine necessary route obstruction. It is
not a failed rank4-only sufficient certificate, and it is not an
all-graph unordered bad-pair count.

Closing b⁴ eliminates the previous same-fiber shortage but does not
produce a full graph. The original full-cover prediction was refuted.
The even-phase prediction had the narrower outcome it asked for:
61even assignments have no unique rank3-only slot, yet all still have
other complete-union gaps. The same happens for126odd assignments.
Thus the absence of a unique deficient route is not enough to imply
coverage. No conclusion about all affine offsets, other controllers,
other moduli or arbitrary (16,4) graphs follows.

RESULT.json and terminal.json summarize the two groups separately.
ROWS.json preserves every literal parameter tuple, all four source
inventories, missing-controller counts, first missing fiber IDs and
unique-rank3 flags. The algebraic evaluator used 0.776093 CPU seconds
before final serialization, with zero source parses, word-image
recomputations, graph generation or BFS. The fixed 974 scope is closed
and stopped: no more phase moduli, voltages, offsets or samples are
scheduled.
