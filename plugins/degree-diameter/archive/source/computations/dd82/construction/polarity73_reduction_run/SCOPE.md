# Polarity73 necessary deletion screen

`screen.py prepare --n 58` and `--n 59` create separate saved
CNF inputs with exactly15 or14 of all73 deletion bits true. No shape,
fiber, seed, symmetry representative, or deletion radius is fixed.

The necessary conditions are: at least8 deleted outer vertices; each
retained outer vertex has a deleted outer neighbor; each retained ambient
degree9 vertex has a deleted H neighbor. Exact neighborhood counters define
`sat[x] iff not D[x] and count_deleted_H_neighbors(x)=degree_H(x)-8`
in both directions. Thus an absolute point uses count0 and every other
point uses count1; deleted points can never be saturated indicators.

For every deleted-center candidate f and every ambient nonadjacent pair
u,v in its neighborhood, the clause `not D[f] or not sat[u] or not sat[v]`
is imposed. This is the proved obstruction to a lost pair whose two
surviving endpoints have no degree deficit. No unproved aggregate linear
bound or runtime prediction is used. No completion edges are variables.

The source reads the preserved `geometry.edges` and `geometry.json`.
It reuses only generic CNF emitter, exact unary recurrence, clause
evaluation and saved-DIMACS checking definitions through the existing
joint-boundary helper module. No historical constructor or main is called.
The direct Python `direct_screen` function evaluates the actual saved H
conditions independently of CNF. Preparation compares every constraint
group and all73 derived sat bits on five explicit deletion assignments,
including the corresponding saved two-fiber example. This is bounded
semantic sanity, not enumeration, a solver call or a target witness.

Each case saves `input.cnf`, `encoding.json`, `variable_map.json` and
`sanity.json`. Existing case inputs are not overwritten. Root owns solver
execution and independent certificate checking. The source implements no
process launcher, solver, new checksum, or old computation.
The case directories are `n58/` and `n59/`; `encoding.json` records
`status: PREPARED_NOT_RUN`, the retained order `n`, and the exact `scope`.

`screen.py decode --n 58 --log PATH` (likewise 59) requires a full
terminal SAT model satisfying every saved clause and the direct screen.
Without `--log`, it reads that case's `solver.log`. A failed model or
direct-screen condition exits nonzero.
It writes `deletion_candidate.json` containing the full deletion D, outer
deletion F, survivors, saturated vertices, retained degrees and deficits,
all original-label retained H edges, every uncovered survivor pair, and
the exact required number of added edges. `retained_H.edges` is the same
induced graph with compact labels; `compact_to_original` preserves labels.

Every decoded object is explicitly **a deletion-screen candidate, not a
target graph or a completed monotone construction**. A SAT screen may still
have no completion. A checked UNSAT input excludes only this necessary
deletion domain at its specified order, conditional on the mathematical
reduction and encoder coverage; UNKNOWN excludes nothing.
