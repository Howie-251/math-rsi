# The 17-point unique-blue-four obstruction

This is a fresh finite computation on the exact induced domain requested by the
parent task. All 42 order-reflection representatives completed with successful
DRAT verification. The separate literal-DIMACS audit also passed all 42 cases
in 60.4147 seconds, as recorded in `independent-verification.json`.
There was no external mathematical review.

## Exact finite statement

Let an ordered 17-point rank-3 signotope have ordered vertices

`A[p], pi, eta, C[13-p-q], zeta, theta, B[q]`,

where `p,q >= 1`, `p+q <= 13`. Put `T=W\{pi,theta}` (15 physical points).
There is no such coloring satisfying all the following conditions together:

1. Every four-point packet has at most one color change.
2. There is no red seven-point path and no weak seven: opposite-color paths
   with the same outer endpoints and vertex-count sum nine are forbidden.
3. The only blue four-point path is `(pi,eta,zeta,theta)`.
4. `chi(pi,eta,x)=B` for every physical `x>eta` in W, and
   `chi(x,zeta,theta)=B` for every physical `x<zeta` in W.
5. No T-internal blue three-point path starts at eta or ends at zeta.
6. A T-internal red six-point path starts at eta **or** a T-internal red
   six-point path ends at zeta. This is one inclusive disjunction on the same
   coloring; neither disjunct was selected in advance.

The positions are `pi=p`, `eta=p+1`, `zeta=15-q`, `theta=16-q` on vertices
`0,...,16`. Thus both marked pairs are physically adjacent in W. Zero-length
C is allowed. No extra all-T restriction on arbitrary red-six endpoints was
imposed.

## Coverage by order reflection

All 78 ordered pairs `(p,q)` with positive entries and sum at most 13 occur.
The computation uses the 42 pairs with `p<=q`; six are fixed by reflection.
For a pair with `p>q`, the order reversal `x -> 16-x` exchanges the labels

`pi' = 16-theta`, `eta' = 16-zeta`, `zeta' = 16-eta`, `theta' = 16-pi`.

It exchanges A with B, sends `(p,q)` to `(q,p)`, and preserves the colors of
unordered triples. A packet's color sequence reverses, preserving the number
of changes; red/blue paths and their same outer endpoints reverse. The two
blue fans exchange, as do the two forbidden T-blue-three endpoint conditions.
The red-six existence alternative with source eta becomes the alternative
with terminal zeta', and conversely. Thus the **whole disjunction** is invariant.
Every order therefore enters a tested representative without dropping a
branch or changing the shared coloring.

## Encoding and the semantic bridge

There are 680 physical triple variables, with true meaning red, followed by
private existence selectors. All packet clauses are explicit. All seven-point
red paths are forbidden. Every four-point path other than the marked one has
a clause saying at least one of its two consecutive triples is red; the two
consecutive triples of the marked path are blue units.

A blue five-point path would already contain multiple blue four-point paths,
so it is excluded by the unique-four condition. A monochromatic path in a
packet-valid coloring remains monochromatic after deleting internal points:
for four ordered vertices, equality of the first and last packet colors forces
both middle colors to agree, and iteration gives the deletion property.
Consequently every longer red path contains a red seven, and the only remaining
weak-seven splits are red six plus blue three and red five plus blue four.

Every actual red-six path is paired with **every** blue-three candidate with
the same endpoints; interiors may overlap. The unique blue four has outer
endpoints pi,theta, so every red five with those endpoints is forbidden.
The blue fans and forbidden T-blue-three conditions are literal units.
For every T-red-six candidate satisfying at least one endpoint alternative,
a selector implies all its red triples. One clause requires some selector.
Every coloring satisfying the finite statement extends to these selectors by
selecting one actual witness; no converse-only claim is being used to exclude
an unencoded coloring.

`verify_colors.py` imports no generator or solver code. It parses the literal
saved DIMACS bytes, checks the declared variable and clause counts, rejects
duplicates, independently generates every required clause from the mathematical
conditions (in particular enumerating weak paths by fixed endpoint pairs), and
compares the **complete clause sets** and variable count. It independently
reconstructs selector indexing rather than trusting `spec.json`. It also checks
that the actual proof bytes still match each result binding, that drat-trim
returned zero with `s VERIFIED`, and that the CNF digest is unchanged.
For any SAT result it has a separate exhaustive physical-path checker, though
no SAT result arose in this batch.

## Runtime, primary evidence and reproduction

All scientific execution was on authoritative Linux, using Python 3.12 at
`/opt/anaconda3/envs/forktqiu3/bin/python3.12`. The fresh controller used four
threads only to control four external solver/checker jobs. Each external process
had its own process group and outer wall-clock limit; timeout termination waits
for SIGTERM then escalates to SIGKILL and reaps the process. Kissat's own budget
was 90 seconds per case, and drat-trim's budget was 180 seconds per case.

The default solver was
`/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat`; the checker was
`/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim`.
`runtime.json` and `final-bindings.json` bind their actual bytes and both source
files. Each `pNN-qNN/` directory contains `formula.cnf`, `proof.drat`, literal
solver/checker stdout/stderr, `spec.json`, and `result.json` with commands,
exit codes, elapsed times and SHA256 identities. `plan.json` is the full order
list; `summary.json` and `done.json` record actual completion.
`coverage.json` independently checks all 78 ordered parameter pairs, the six
reflection-fixed representatives, solver exit code 20 in every case and checker
exit code zero in every case. `manifest.json` records every retained file's
SHA256 and size before archive transport.

The solve/check controller completed all 42 cases in 104.1204 seconds.
No timeout, unchecked UNSAT, SAT or unattempted representative remained.
The independent audit output records the actual separate audit duration.

The authoritative evidence root is
`/data/ktqiu_hdd/math_agent/reports/n767-t15-unique-blue-four-20261112`.
Its Linux `evidence.tar.gz` preserves all 42 CNF/DRAT cases and the original
audit/report payload: 59,113,838 bytes, SHA256
`868d2e5b496836d87873e6f6a81e052240fc3fac9541a8ddde4687dd7faebe5c`.
Its file listing contains every manifest-bound payload file, and both a fresh
tar listing and gzip integrity check exited zero; see `archive-binding.json`.
The archive was built before that sidecar binding, so the sidecar is outside
the archive.

Two full-directory streaming retrieval attempts exceeded their respective
60-second and 300-second **transport** limits. They did not rerun or interrupt
any scientific job, and no complete 42-case archive is claimed locally.
The local `metadata.tar.gz` contains all 42 proof/formula bindings, their actual
results, the complete independent audit and Linux archive binding. Local
`sample-p01-q12.tar.gz` contains the full original case `p01-q12`, also extracted
to `p01-q12/`, including its actual 4,674,737-byte `formula.cnf` and 22,521-byte
`proof.drat`, all logs and its result record. Every transported sample file's
SHA256 was compared against the original Linux manifest and agreed. These are
transport-integrity checks, not scientific reruns on Windows.

`REPORT.sealed.md` is the original report bound by the Linux manifest; this
local `REPORT.md` adds the final archive/transport distinctions. The original
Linux report and manifest-bound scientific files were not rewritten.

From an extracted **complete Linux archive**, rerun the independent audit on
Linux with:

```bash
/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B verify_colors.py
```

To independently replay an individual certificate, use:

```bash
/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim \
  p01-q12/formula.cnf p01-q12/proof.drat -t 180
```

Fresh solver reproduction uses `probe.py` in an otherwise empty new directory;
the script refuses to overwrite any existing case directory. The local
`transport.ps1` uses the project's established OpenSSH/askpass/known-hosts
control route and makes create-only Linux deployments.

## Connection to the parent research

The original [G.7](../../.trellis/tasks/10-19-nr7-structure-capacity/research/N7_FIRST_TWO_COLUMNS_FORCED_BYPASS_20261112.md#g7-t15的精确恢复入口唯一静默纯点与唯一域内蓝四)
provides the reduction to this 17-point domain, its unique blue four, and
G19a's red-six endpoint disjunction. The physical adjacency of pi,eta and
zeta,theta in this same induced domain is proved in the new
[exclusion manuscript §2.2](../../.trellis/tasks/10-19-nr7-structure-capacity/research/N7_T15_UNIQUE_BLUE_FOUR_EXCLUSION_20261112.md#22-两个禁隙与扩大的红扇),
rather than asserted by the original G.7. The parent also supplies the blue fans
and T-blue-three endpoint prohibitions. This report proves the stated **finite
conditional obstruction**. The parent must retain the proofs of those imports
when concluding anything about the original 75-point t=15 layer. This is neither
a 75-point counterexample nor a claim covering the separate t=14 layer. It uses
no geometric-realizability assumption and no production C_r encoding.

Only this fresh report directory was written. Existing jobs, sealed evidence,
production encodings and all other workers' files were preserved. No new Goal,
external reviewer, model substitution or workflow-maintenance edit occurred.
