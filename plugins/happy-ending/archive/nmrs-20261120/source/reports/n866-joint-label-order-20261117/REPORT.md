<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# Shared-label inclusion model: a checked nine-hole milestone

2026-11-17. The first three adaptive eight-hole batches produced 11 checked
kernel rows and their true transposes. Together with the original 93 rows,
the resulting **115-row necessary matrix has exact minimum nine holes**.
The at-most-eight exclusion has an actual successful external proof check;
a nine-hole vector is independently verified against every row. Via the
original ordinary-866 state/label interface this gives the candidate upper
bound `N_sig(8,6,6) <= 61`. It does not yet give eleven/twelve holes or a new
global eight-parameter endpoint. Mathematical bridge assurance and independent
external acceptance are unchanged.

The immutable standalone package is [milestone9](../../../../nmrs-20261117/source/reports/n866-joint-label-order-20261117/milestone9/README.md), with
actual [verification](../../../../nmrs-20261117/source/reports/n866-joint-label-order-20261117/milestone9/verification.json). Its Linux/local archive
SHA256 is `33ee393ee26594b805f18d4ea8803ef4a5c5ac382ec2b45a9b29c9c23fd1dad7`;
the 40-file manifest SHA256 is
`89ba7c1450145a00a2c97d8257091d67864426768b0d7b9c3624f8b8f6ff3f2e`.
Higher-budget experiments are bound separately under `appendix9plus/` and do
not change this package.

## Actual input and a necessary model covering every occupancy budget

The universe is all 70 Ferrers ideals in the 4 by 4 grid, encoded by four-subsets
W of [8] with column heights `(w4-4,w3-3,w2-2,w1-1)`. A hole variable h_i is true
exactly when that state is not occupied. Every strict inclusion A contained in B
has **one shared cell label**, chosen from B minus A. The same choice appears
in every triple using that actual pair. Every inclusion triple A<B<C has one
color variable. A blue triple requires x(label(B,C))>x(label(A,B)); a red triple
requires the analogous strict y increase. These requirements are gated by the
three states being occupied. Every occupied four-point inclusion chain also
has a legal one-change packet.

The same original actual input supplies all these quantities: inclusion fixes
chronology, because the reverse actual pair would need a label in the empty
reverse ideal difference. Actual ambient pair labels belong to the appropriate
directed differences; they are retained, not recomputed independently per
triple. The original complete triple coloring supplies the shared colors and
packets. Missing states can be assigned arbitrary unused labels/colors.

Two forward DP layers retain the **same actual source** and then the same
actual endpoint. Four-point monochromatic inclusion chains force
`R4(source,last_pair,color)`; extending with the same shared triple color forces
`R5(source,end,color)`. The model prohibits both colors of R5 for the same
source and endpoint. Their two five-point paths would be weak eight. DP
implications are forward only, which is sufficient: every real path must
activate its state; assigning the DP states exactly by real path existence
extends any actual input. Their interpretation does not require arbitrary
auxiliary states to be true.

The model is a necessary projection. It does not impose chronological order or
all packets among incomparable states, and a satisfying assignment would not
by itself be a complete signotope. An UNSAT proof, however, excludes every
actual input mapped into that specified occupied domain.

The full model has 1694 comparable pairs, 8434 candidate cells, 21238 inclusion
triples, and 163982 four-point chains. It has **69208 variables and 2165442
clauses**. `audit.py` independently regenerated every clause and all variable
interfaces and returned PASS for all 2165442 rows. The base CNF SHA256 is
`6ac37a76af080e68b1342c6679004a39a40e943e421f4fc688017227a251251d`.

All scientific execution was on Linux `ubun` under
`<private-artifact-root>`, with
`<private-python-runtime>`. Every solve used the controlled
external default `<private-artifact-root>`.
Checks used the existing external
`<private-artifact-root>`.

## Initial probes and extraction of genuinely universal rows

The previous explicit eight-hole vector was checked UNSAT in the full model
(Kissat 1.77 seconds; actual checker VERIFIED in 4.33 seconds). Its extracted
93-clause core needed only 22 negative occupation assumptions. A second actual
check of that small core succeeded. Its new cover row needs one hole in those
22 states; it is not limited to that original eight-hole mask.

Four initial all-budget solves, with at-most-eight/nine/ten/eleven counters,
each reached its controlled 20-second limit. Their actual status remains
UNKNOWN. The later independently checked cover-matrix argument settles the
eight-hole bound without rewriting these old timeout results. No full-model
nine/ten/eleven exclusion is inferred from those runs.

Adaptive CEGAR then selected occupied domains from the growing cover matrix.
Each solve fixed only the selected occupied states, with **negative hole
units**; the omitted states were not fixed to be holes, and no hole-budget
unit was added. Thus every extracted occupation-only core becomes an
unconditional necessary cover row. The proof is rechecked on the small core,
and its nonoccupation clauses are independently matched to the original base.
The final standalone verifier goes further: it checks each such clause
directly against the cell-label, packet and actual common-end path semantics.

| Batch | Checked new masks | Kernel support sizes | Rows after true transposes |
| --- | ---: | --- | ---: |
| Initial fixed eight-hole vector | 1 | 22 | 95 |
| Eight-hole batch 1 | 4 | 13,20,36,13 | 103 |
| Eight-hole batch 2 | 4 | 13,19,13,25 | 111 |
| Eight-hole batch 3 | 2 | 24,13 | 115 |

All these fixed-domain solves and their small-core checks actually succeeded.
No repeated transpose orbit was counted as a new candidate. Search no-goods
were used only to diversify candidates; they are absent from the mathematical
row pool and the final budget certificate.

True grid transpose is the only symmetry used. On codes it is
`W*={9-v : v in [8] minus W}`, with pair coordinates exchanged and colors
swapped. It preserves actual time and the admissible interface. No unverified
reverse-order operation is used.

## Independent reconstruction of the nine-hole milestone

`milestone9/verify.py` is standalone with Python and an existing drat-trim.
Its actual Linux run returned PASS in 3.02 seconds. It reconstructed:

* The original 63 cycle supports from 6930 nonvacuous six-order checks.
* All 30 shared-pivot rows from 84 actual pivot-cell branches.
* Every semantic clause of all 11 occupation-only kernel CNFs, every small
  proof, and each true-transposed cover support.
* The complete final 115-row matrix, exact at-most-eight threshold counter,
  final proof binding, and explicit nine-hole cover.

The final budget CNF has **664 variables and 1295 clauses**, SHA256
`132667ca6bda843535941a6a8c82cdfb6a5d6bad2e843a4caa770047564a3a62`.
Default Kissat returned UNSAT in 1.57 seconds; drat-trim returned zero and
**s VERIFIED** in 1.12 seconds. Its 2069915-byte proof SHA256 is
`b95ca8d9b4a8c93b6537de33f6b3541f11b8ee2f3bd33cea5543cccb6045259a`.

The exact nine-hole cover is

```
1238 1458 1468 1568 2347 2357 2367 3567 4567
```

It is a feasible matrix vector, not an actual 61-point construction. Combined
with the checked at-most-eight exclusion, it proves that this **115-row matrix**
has exact minimum nine.

Reproduce from the sealed directory on Linux:

```bash
python3 verify.py --directory . --checker /path/to/drat-trim
```

## Three distinct shared-label claims

The 13-state certificate included in the sealed milestone uses **one actual
pair** `1247 -> 1258` whose cell domain is `{(1,4),(2,2)}`. Each branch unit
refutes the same 52-clause occupation core. Its proof has three additions:
reject the first cell, reject the second, then the empty clause. It is a
single-pair/two-cell certificate, not a two-pair theorem.

The separate `two-pair/` certificate uses **two different actual pairs**:

```
P: 1268 -> 1468, cells (3,1) or (3,2)
Q: 1457 -> 2467, cells (2,3) or (4,1).
```

On the common 53-clause core, P alone leaves both branches unresolved by unit
propagation; Q alone leaves its first branch unresolved. All four P/Q cell
combinations unit-refute. The checked seven-line proof adds the four binary
rejections `not(P_i and Q_j)`, then the two `not P_i` units, then the empty
clause. The actual checker returned VERIFIED. This is genuinely joint in the
stated UP sense; no claim is made that its support or proof is globally
minimum. It was the best proof-line/core-size pair found in a completed scan
of 23 exported cores and 462 eligible pair-pairs.

Finally, the full model simultaneously shares labels over all 1694 comparable
pairs. Its meaning and coverage are broader than either small certificate.

## Transport scope and observed rigidity

For any checked core on source ideals I_i, distinct target ideals J_i inherit
the row when every required comparable pair stays strict and
`J_j minus J_i` is contained in `I_j minus I_i`. Pull every target actual label
back to the same grid cell of its source domain, retain the same actual triple
colors, and interpret common-end DP variables by actual paths. Every semantic
clause and occupied assumption then holds, contradicting the checked core.
This argument uses a **single common mapping** and shared pair labels.

The finite uniform-cell-forcing/transpose orbits of the first five kernels
were completely enumerated. Every orbit had only its source and true
transpose. A separate exact CSP for each of the two first 13-state kernels
was rigid: arc consistency left each target variable at its original state,
so the unique difference-shrinking embedding is identity. A relaxed version
using only comparisons actually present in those proofs and shrinking domains
only on used label pairs was also rigid. These are precisely scoped negative
transport results; arbitrary pair-cell remappings were not implemented.

## Higher-budget work and recovery

The sealed nine-hole milestone is final and untouched. Subsequent work is
finalized in [APPENDIX9PLUS.md](APPENDIX9PLUS.md): a frozen 215-row pool and a
separate final 271-row transport merge, each with a verified nine-hole survivor.
Their exact matrix minimum remains nine. No higher budget is folded silently
into the 115-row claim. The original full CNFs, timeout proof prefixes and
solver logs remain on Linux; the small proof chains and standalone packages
are returned locally.

An early `cases-audit.json` classified interleaved clause groups by cumulative
counts. That optional group breakdown was inaccurate; its file/occupation
binding checks were sound. The sealed verifier's **per-clause semantic**
classification supersedes that breakdown. No mathematical conclusion relies
on the early group counts.
