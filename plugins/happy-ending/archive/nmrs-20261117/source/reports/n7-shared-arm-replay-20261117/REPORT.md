# Exact shared-arm replay on the fixed sixteen-point input

2026-11-17. All scientific computation ran on the authoritative Linux server
`ubun`, using `/opt/anaconda3/envs/forktqiu/bin/python3.10`, in the fresh directory
`/data/ktqiu_hdd/math_agent/reports/n7-shared-arm-replay-20261117`.
The source was the unchanged complete coloring
`/data/ktqiu_hdd/math_agent/tmp/n7_bidirectional_four_20261117/fixed16_colors.json`.
Its copied bytes are retained as `input16.json`, SHA256
`5b9076e588f11d5d0d878056705b7afb145d8601ddb2e14c3c5b335409c4e279`.
This is a finite calibration of the proposed arm structure, not a general
74-point result or an independent external acceptance.

## Complete arms, middle pairs and closure

The physical blocks are A={0,1,2,3}, B={4,5,6,7}, C={8,9,10,11},
D={12,13,14,15}. The replay rechecked all 560 triple entries and all 1820
packets, then enumerated every actual red six as an all-red-triples subset.
It found exactly 576 paths and 16 actual middle pairs, precisely B times C.
The entire path family is

```
choose(A,2) x B x C x choose(D,2).
```

For every actual middle pair (k,h), the replay constructed

```
Ldomain(k,h) = {z<k : color(z,k,h)=red}
Rdomain(k,h) = {z>h : color(k,h,z)=red}.
```

Its left comparison graph has edges (a,b) in Ldomain exactly when
`color(a,b,k)=red`; the right graph has edges (p,t) in Rdomain exactly when
`color(h,p,t)=red`. Each graph was compared against the **complete** actual
four-point red arms with that middle pair, including all triples of each arm.
They agreed on every middle pair. The Cartesian product of both arm families
was red in every case, and its complete union equaled the complete enumerated
R6 family, with neither missing nor extra paths.

| Quantity | Exact value |
| --- | ---: |
| Actual R6 | 576 |
| Actual middle pairs | 16 |
| Left arms, summed over all middle pairs | 96 |
| Right arms, summed over all middle pairs | 96 |
| Distinct physical left edges | 6 |
| Distinct physical right edges | 6 |

For each fixed k, every left domain was checked pairwise for inclusion
comparability; the right mirror was checked for every fixed h. All passed.
In this particular model, domains at a fixed root are equal as the opposite
middle endpoint varies. Thus it tests exact deduplication and compression,
but supplies no example with strictly different domains at one root.
The six distinct left edges form K4 on A; the six right edges form K4 on D.

`first16/paths.json` retains every R6, `arms.json` every domain and complete
arm list, and `nesting.json` every fixed-root group and chosen maximum domain.

## All minimum physical cuts and D+sigma reconstruction

Complete physical-subset enumeration found minimum transversal size three.
All 137 subsets of sizes zero, one and two fail. All three-point transversals
are exactly these eight:

```
0,1,2       0,1,3       0,2,3       1,2,3
12,13,14    12,13,15    12,14,15    13,14,15
```

All-left graph VC cost is three, all-right graph VC cost is three, and the
joint physical R6 transversal cost is three. These are overlapping physical
costs; the two one-sided values are not added.

For a concrete certificate choose T={0,1,2}. The original actual middle-label
set is M=B union C={4,...,11}, so the prescribed D0=T intersect M is empty.
Choose sigma(k,h)=left at every one of the 16 surviving middle pairs. For each
of the four left roots k, compress its four selected middle pairs to one
maximum-domain representative. Each resulting comparison graph is the same
K4 on A. Their **physical union** is just one K4, and T covers it with cost
three. Every red six has an A-pair, so T hits every actual path. The right
mirror uses any three vertices of D. In both cases a two-point cover is
impossible, because it leaves an A-pair and a D-pair as well as an available
B and C point, hence an actual red six avoiding it.

The replay repeats this reconstruction for all eight minimum T. It computes
D0=T intersect M first, filters **all original complete red sixes** to X minus
D0, recomputes active middle pairs and both complete arms from the surviving
input, and then chooses sigma only for these surviving middle pairs. It checks
that every selected arm is covered by T minus D0, that taking a maximum domain
at each root preserves the physical graph union exactly, and that the exact
VC minimum plus |D0| equals three. All certificates are in
`first16/recoveries.json`; `cuts.json` contains all minimum covers and all
three-point transversals.

All eight minimum T avoid M, so **D0 is empty in every minimum certificate**.
Consequently this finite model does not stress the nonempty-D0 case, including
middle pairs that become inactive after an arm vertex is deleted. The code
recomputes them correctly from the filtered full path family, but that branch
was not exercised by these minimum witnesses. No general conclusion about
nonempty-D0 instances follows from this run.

## Independent implementation replay and optional 25-point calibration

`check_replay.py` separately rebuilt all red sixes using consecutive triples,
checked that each is all-triples red, recovered complete arms by actual path
projections, checked two-wing products, exhaustively recomputed the graph and
physical minima, and replayed all eight exported D0+sigma certificates against
the original coloring. `check16.json` is PASS, exit zero. It is a separate
finite implementation, not an external reviewer or a new theorem-acceptance
event. The original generator completed in 0.099165 seconds, exit zero, under
an external 90-second timeout. No solver was invoked.

An existing complete 25-point fixture was easily available at
`/data/ktqiu_hdd/math_agent/tmp/n7_path_transversal_probe_20261105/Y25_colors.json`.
Its unchanged bytes are `input25.json`, SHA256
`70fb9df483f1947c256f933a7df6d7b900c01d49825ed10aa88eff438fd138d3`.
`calibrate25.py` checked its 2300 triples, all 12650 packets and every six-point
subset. There are **zero** actual red sixes. Therefore there are no active
middle pairs and all three transversal costs are zero, with the empty set as
unique minimum. `calibration25.json` records this 0.186188-second Linux run,
exit zero. This is only an empty-family calibration, not a second nontrivial
arm/nesting example.

## Raw evidence and reproduction

The complete returned `evidence.tgz` has identical Linux/local SHA256
`817c786d5b3ce08c8131320c8f4545f3c3bc35aef4e2b7b2bede3d93321288d6`.
It includes both exact input files, every 16-point path/arm/nesting/cut/recovery
artifact, generator log and exit, separate check stdout/stderr/exit, optional
25-point calibration stdout/stderr/exit, and `source-input-sha256.txt`.
Transport and actual commands are in `receipts/`. The three source scripts
are alongside this report. Windows performed only edits, transfers, byte hashes
and archive unpacking. No job remains running; old evidence and production
builders/CNFs/proofs were not changed.

On Linux, using fresh output names:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 90 \
 /opt/anaconda3/envs/forktqiu/bin/python3.10 replay.py \
 --input input16.json --out replay16
/opt/anaconda3/envs/forktqiu/bin/python3.10 check_replay.py input16.json replay16
/opt/anaconda3/envs/forktqiu/bin/python3.10 calibrate25.py input25.json
```

The caller receives a complete successful 16-point structural replay and
explicit minimum-cut reconstruction. Extending it to arbitrary critical
74-point inputs, nontrivial nesting, or nonempty-D0 arm loss remains a separate
mathematical obligation.
