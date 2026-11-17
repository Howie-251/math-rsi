# Ordered red-six-block necessary-system probe

This task tests the local projection supplied by the parent: q strictly separated
six-point blocks, each entirely red; every four-point packet has at most one
color change; no blue seven-vertex path; and no red six-vertex path that crosses
blocks. Vertices and all stored paths use zero-based numbering. This report does
not assert the parent's extraction of these blocks from the original eight-parameter
problem. The parent's original-input bridge remains a separate obligation.

## Verified positive witness for the projection

The q=7, n=42 projection is **satisfiable**. Authoritative Linux Kissat returned
SAT in 0.3651 seconds. `dp-q7/colors.json` is a complete coloring.
`dp-q7/model-audit.json` records a direct independent PASS for every CNF clause,
every packet, all seven full-red blocks, absence of blue7, and absence of every
cross-block red6. Maximum forced full-coloring blue/red path lengths are both6.
Thus these necessary conditions do not exclude q7 and do not improve II<=21.

The witness has weak8: blue `[0,1,6,8,25,28]` and red `[0,26,27,28]`, both
with endpoints `[0,28]`; lengths6+4=10. It is not a weak8-free input.
The complete coloring SHA256 is
`0e8f1b8546b18ad2aabbe8ad5bf36b7ef985fba802f373ee10ea603f95aa9983`.

## Compact exact-path CNF and original-object lifting

`solve_dp.py` uses red=true triple variables C and auxiliary path predicates.
B(u,v,l) means that a blue path of exactly l vertices ends in pair u,v.
R(u,v,l,f) additionally tracks whether the red path has crossed a block boundary.
All two-point paths are seeded: blue always, and red with f equal to whether
u and v are in different blocks. A blue triple extends B by one; a red triple
extends R, replacing f by f OR block(v)!=block(w). Blue length7 and red
length6 with f=1 are forbidden. Internal block triples are positive units;
the eight illegal packet bit patterns are excluded directly.

Any actual coloring satisfying the stated local predicates extends to this CNF
by assigning auxiliaries to actual path existence. Conversely, the forward
implications force every actual path predicate by induction, so any CNF model
obeys the blue and crossing-red prohibitions. This covers red paths whose final
pair lies within the last block but whose start lies in an earlier block.
No weak8 restriction is present in this base CNF.

The base has25,256 variables and1,048,264 clauses. `audit_dp.py` independently
reconstructs every variable domain and the full clause stream: PASS.
Base CNF SHA256:
`37d8857b7490ac27f6974000185ba3d784609344a72116929fd7f820140237c5`.
No UNSAT proof claim follows from the SAT-run `proof.drat` auxiliary output.

## Propagation-only experiment

The initial implication set consists of internal red triples, blue triples
with one earlier external vertex and a pair among a block's first3 vertices,
and the mirrored blue triples from a pair among its last3 vertices and a later
external vertex. Each bridge is necessary: a red bridge concatenated with the
three remaining available internal vertices gives a forbidden cross-block R6.

For q=7,6,5,8,10, neither packet propagation nor monochromatic forbidden-path
unit propagation added any literal. `check.py` independently replays all initial
reasons. `check_fixedpoint.py` independently retains every exact reachable
length and external block identity, checks all packet implications and all
potential forbidden-path unit implications, and reports PASS with zero units.
The partial forced blue maximum is4 and red maximum6 in each tested case.
These are fixed-point checks, not satisfiability/exclusion certificates.

| q | vertices | forced triples | generator seconds | fixed-point audit seconds |
|---|---:|---:|---:|---:|
|7|42|896|0.2253|2.1029|
|6|36|660|0.1287|1.3337|
|5|30|460|0.0602|0.4647|
|8|48|1168|0.3915|2.8004|
|10|60|1820|0.9439|7.5953|

## Final bounded weak8 refinement

The parent subsequently authorized one final q7-only refinement: at most20
external solves and90 seconds of cumulative loop time. `cut_weak8.py` preserves
each successive CNF and log. Every cut forbids one explicitly listed same-endpoint
blue/red path pair with total length10. Consequently every weak8-free input
satisfies every generated cut. `audit_cuts.py` checks the explicit path shape,
color realization in its source model, exact cut literals and byte-exact
cumulative CNF bindings. Results are recorded in `weak8-q7/result.json` and the
separate audit log; no unverified termination is an exclusion certificate.

The loop ended inconclusively at90.0569 seconds:14 SAT rounds, followed by the
15th solve timing out on the remaining1.48-second budget. It accumulated1,437
cuts. The independent cut audit passed all1,437 valid path cuts and all15
complete CNF byte bindings. No weak8-free witness and no UNSAT certificate were
obtained. There is no q exclusion or numerical bound improvement from this task.
The last SAT model in round14 still has the66 weak8 witnesses cut for round15.

All complete round CNFs and solver outputs remain preserved on Linux. The local
cut package keeps cuts, per-round metadata and logs; large repetitive round
CNFs and SAT-run proof output stay on Linux. `rebuild_round.py` reconstructs any
round CNF exactly from the fetched base CNF and cumulative cuts, verifies its
recorded SHA256, and writes only a fresh destination.

## Runtime and reproduction

All scientific execution occurred on authoritative Linux under
`/data/ktqiu_hdd/math_agent/reports/n8-common-lock-blocks-20261117` with
`/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B`. Windows only edited,
transferred and unpacked artifacts. No production builder, campaign or running
job was changed. Transport receipts redact connection values.

To reproduce the base witness generation, choose a fresh directory:
`python3 -B solve_dp.py --q 7 --out fresh-dp-q7`.
Run `audit_dp.py fresh-dp-q7` and `check_model.py fresh-dp-q7` on Linux.
For the recorded artifacts, run `check.py q7/trace.json`,
`check_fixedpoint.py q7/trace.json`, `audit_dp.py dp-q7`, and
`check_model.py dp-q7`. The independent model audit uses no SAT auxiliary
reachability variables for its semantic path checks.
