# Sixteen-point bidirectional certification witness

2026-11-17. The fixed construction was supplied analytically by the parent
agent; this module constructed its complete coloring and audited it on the
authoritative Linux server. This is a same-session computational audit, with no
independent review and no change to any global capacity claim.

## Fixed object and verified result

The ordered blocks are A={0,1,2,3}, B={4,5,6,7}, C={8,9,10,11},
D={12,13,14,15}. Every triple within a block is blue; every triple meeting
three different blocks is red. Low pairs are all A-pairs, all B-pairs except
{4,5}, and {10,11}; every other same-block pair is high. A triple whose first
two points form a same-block pair is red exactly when that pair is low. A
triple whose last two points form a same-block pair is red exactly when that
pair is high.

The complete 560-triple table is `fixed16_colors.json`. All 1,820 four-point
packets are legal. Every vertex subset of sizes 2 through 16 was checked for
both path colors. The consecutive-triple and all-triples definitions agreed
everywhere. A separate start-fixed endpoint DP agreed with every reachable
path length. There is no R7, B6, or weak7. The longest red and blue paths have
lengths 6 and 4 respectively. There are 576 R6 paths and 1,296 R5 paths.

Using exactly the two-sided definitions in section 10 of
`N7_74_NINE_POINT_FORK_CUT_EXCLUSION_20261117.md`, the full sets are

```
H+ = {0,1,2,3,4,5,6}
H- = {9,10,11,12,13,14,15}.
```

These entire sets are physically disjoint. They contain the red fours
`(0,1,4,5)` and `(10,11,14,15)` respectively.

## Physically disjoint full certification packages

For i in {4,5}, the forward package uses

```
P_i = (0,1,i,8,12,13)       actual R6
F_i = (i,6,8,12,13)         actual R5 starting at P_i[third].
```

Their certified prefix triples cover the whole forward red four. Their
complete physical support is `{0,1,4,5,6,8,12,13}`.

For j in {10,11}, the reverse package uses

```
P_j = (2,3,7,j,14,15)       actual R6
F_j = (2,3,7,9,j)           actual R5 ending at P_j[fourth].
```

Their certified suffix triples cover the whole reverse red four. Their
complete physical support is `{2,3,7,9,10,11,14,15}`. These two eight-point
supports are disjoint and partition the entire sixteen-point object. All
listed paths and certification identities were directly checked.

## Exact physical transversal numbers

Each direction has 17,280 actual ordered (R6,R5) certification pairs. The
audit deduplicates their physical unions, then enumerates physical label
subsets in increasing size. All minimum covers and every distinct support
are retained in `fixed16_audit.json`.

| Family | Exact transversal number |
|---|---:|
| All actual R6 paths | 3 |
| Forward fork supports | 2 |
| Reverse fork supports | 2 |
| Union of both fork families | 3 |
| All R4 inside H+ | 1 |
| All R4 inside H- | 1 |

The two individual fork costs therefore do not add to the joint cost in this
example. The example certifies small-scale coexistence, including disjoint
complete witness packages; it supplies no 74-point model and no obstruction
to such a model.

## Raw evidence and reproduction

`audit_fixed.py` is self-contained and independent of production builders.
`fixed16_packets.json`, `fixed16_paths.json`, `fixed16_forks.json`, and
`fixed16_audit.json` retain the exhaustive raw data. `fixed16.log` and
`fixed16_run.json` retain Linux output and transport metadata. The executed
source SHA256 was
`c926f5270acaf4ae3bd78f70cf511b7daba468ba4ff3c71bdf45191d429e7d06`.

On Linux, copy the source into a fresh output directory (the program uses
exclusive creation), then run:

```bash
timeout -s TERM -k 5s 100s \
  /opt/anaconda3/envs/forktqiu3/bin/python3.12 -B audit_fixed.py
```

The first exploratory `search.py` run considered 20,000 deterministic random
recursive join models: 3,783 passed the two path caps, seven had red fours in
both certification sets, and all seven failed weak7. This negative exploratory
result has only that finite sampled scope; the analytically supplied fixed
sixteen-point construction closes the requested existence obligation.

`sat_probe.py` was written and uploaded before receiving the analytic model,
but never executed. Total solver invocations: zero. No old runtime, production
encoding, sealed CNF/proof, running job, or external-review session was changed.
