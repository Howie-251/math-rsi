# Native trace certificates: 988 at most 688 and actual D9 at most 458

2026-11-16. Actual authoritative Linux LP execution and a separate exact
integer checker both succeeded. This is a same-session finite-certificate
candidate, not an independently reviewed acceptance.

## Final working upper bounds

The complete bounded run queue and its separate exact replays are finished.
The strongest successful native certificates are:

| Actual caller | States | Complete matrix rows | Positive certificate rows | Integer holes | Population bound |
| --- | ---: | ---: | ---: | ---: | ---: |
| ordinary 988, depth2 | 924 | 90891 | 883 | 236 | **688** |
| true D9 residual, depth3 | 582 | 47635 | 532 | 124 | **458** |

Both certificates use **only native trace rows after ordinary coordinate
erasure**. There are no public cycle rows and no imported numerical whole-slice
capacities in this generic matrix. They therefore do not require the new
cyclic packet bridge, 977's 222 bound, 968's 185 bound, or public finite trees.

For D9 the mother is the 792 five-subsets of `[12]`; the actual allowed
universe is exactly `12 in W => 11 in W`, of size 582. For every original
trace K, the demand is reduced by **exactly** `|K outside U|` before summing
its surviving variables. The independent check regenerates the original
trace and checks this deduction. The D9 certificate's total weighted credit
for those fixed forbidden states is 17140072.

With Lambda=1000000, the exact integer quantities are:

| Caller | Weighted RHS D | Overload P | D-P | Strict comparison |
| --- | ---: | ---: | ---: | --- |
| 988 | 235971972 | 299 | 235971673 | >235 Lambda |
| D9 | 123539526 | 165 | 123539361 | >123 Lambda |

The universal arithmetic is `D <= sum l_W h_W <= Lambda H+P`, where
`P=sum max(0,l_W-Lambda)` and each actual h_W is 0 or 1. Hence the certified
numbers of holes are 236 and 124. The maximum column load is 1000003 in each
case. Floating LP objectives do not enter these conclusions.

Thus the existing actual R7/R20 interfaces give

`N_sig(9,8,8)<=688`, `D9<=458`,

`N_sig(9,8,9)<=688+458=1146`, `N_sig(9,9,9)<=1147`, **ES(9)<=1148**.

## Self-contained replay, with no optimizer or large matrix

The complete selected q/p parameters, included/excluded coordinate sets,
legal-state IDs, adjusted demands, positive weights and all integer column
loads are stored in these compact files:

* [ordinary 688 certificate](run-988-d2/compact-certificate.json), 196592 bytes;
* [true residual 458 certificate](run-d9-d3/compact-certificate.json), 115339 bytes.

On Linux, standard-library Python suffices; neither SciPy, `rows.json`, an
optimizer nor a network source is required:

```bash
python3 compact_certificate_final.py --check run-988-d2/compact-certificate.json
python3 compact_certificate_final.py --check run-d9-d3/compact-certificate.json
```

The [final standalone checker](compact_certificate_final.py), SHA-256
`9cddf343da72b51a34b7b0d70a7e41b4f6c67ac6d7deecec99b606763abb1af1`,
checks the exact caller parameters, reconstructs every original row from its
q/p difference cells and both legal chains, lifts the fixed-coordinate map,
recounts forbidden states, matches the surviving support, and sums all loads.
Both pack-and-check and a subsequent separate standalone check actually
returned PASS, exit0, for each file. Raw logs are
[988 standalone](run-988-d2/standalone-check.log) and
[D9 standalone](run-d9-d3/standalone-check.log), with their same-name `.exit`
receipts. The compact-file hashes are respectively
`5872dda9c68e83696f42d5e45edb41294647fd0546ab1752a17b25e0ab17bec8`
and `ccee0f65beba7f72709ee4e9cc77a5d71faddc9fb3c270f365544b91d40a5638`.

Generator `residual_lp.py` is frozen at SHA-256
`73d5acace0e342c063de62a932c5e75f0c5525bb7dce4daba4f285c75ac73478`.
Separate matrix-based checker `verify_residual.py` is frozen at
`2c26e376c3e833c214a0ffea4738277b5be3d247027f7ebb22ba65c6a586414c`.
Their 988/D9 row hashes are
`8db0b05bc50d14dde5f65fca11e5639ef89b54cc7de5b6078d9013cf79855b53`
and `9239dfaa4febb076726af4eaea7fd07c6fcff2a242ce2ab3270acbdada8f8829`.
Primary result files are [988](run-988-d2/result.json) and
[D9](run-d9-d3/result.json); complete sources and all small execution receipts
are local in this directory. Large matrices remain on the authoritative Linux
server and are not needed to replay the compact proof.

## Exact stopping point and unsuccessful profiles

For L=12,m=9, fixing f ordinary coordinates gives trace demand 4-f. Depth3
therefore includes every positive-demand native full trace in every ordinary
fixed-coordinate slice of these two mothers. This is a precise row-family
claim, not a claim to cover all possible weak-nine witnesses.

For D9 depth3, [fractional-grid.json](run-d9-d3/fractional-grid.json) is a
verified **fractional** feasible point, total `123539833/1000000 <=124`.
The independent [grid replay](run-d9-d3/fractional-verify.log) checked all
47635 inequalities with integer arithmetic; minimum row slack was 3 units.
Together with the integer dual lower bound above 123, this proves the ceiling
of this complete native LP is exactly 124. Further copies of the same row
family cannot give 125 via LP alone. This vector is not an actual input or
an integral occupancy; integer branching or new path constraints may improve.

988 depth3 generated 288011 rows but HiGHS returned status1/time limit,
`fun=null`, after 245.36 seconds. The Python process itself exited zero;
the attempted checker then exited one because no certificate existed. There
is **no depth3 proof or completed-LP optimum**, and no complete-framework
fractional stopping claim for 988. Its successful depth2 certificate remains
the bound 688. No longer solve or automatic retry was started.

D8 depth2 succeeded but certified only 24 holes/130 states, weaker than the
existing autonomous 126 and the public-finite/packet-migration 124. It changes
neither of those bounds. Its raw artifacts are in `run-d8-d2/`; it is not
silently called an improvement. No 757 optimization was run in this directory.

The returned final small-evidence archive `closure-evidence.tgz` has matching
Linux/Windows SHA-256
`d07f0b462f8bff21d9206124553ef2b9dead74169cb94c59da83c31e130c44e6`.
There was no scientific execution on Windows and no change to sealed jobs.

The root's new deep independent-review request returned `isError=true` and
`REVIEW_UNAVAILABLE: neutral task ownership envelope required`; no jobId or
review text was produced. Requested model was `claude-fable-5-1-reversed`,
requested tools Read,Grep,Glob. This pre-start rejection is distinct from the
earlier archived CLI exit1/zero-read failures. It supplies no mathematical
review. The user subsequently authorized exactly one corrected read-only
request. JobId `c8362c2a79ea45b699a3b953a2de2c98` reached failed; its actual
[receipt](../../../.aris/review-state/claude-review-deep/evidence/5ec834a4404d429999eb00a76e34025c.json)
was read: CLI exit1, zero tool calls, empty review body,
`review_complete=false`, `acceptance_status=unaccepted`, backend/effort
unverifiable. No further retry occurred. These are integer-certificate-checked
**working upper bounds**, not independently accepted results.

## Earlier 691 certificate, preserved as a successful baseline

For every actual `N_sig(9,8,8)` input, the 6 by 6 state catalogue has 924 states.
Every full antimonotone boundary trace, also after ordered coordinate erasure,
has at most eight occupied states by the same-end hereditary trace proof in
[EIGHT-MOVE section 2](../EIGHT-MOVE.md). The inverse coordinate maps are given
in [README](README.md); a state is a six-subset of `[12]` and all states of a
slice use the same fixed included/excluded coordinates.

The generator enumerated 60,687 distinct constraints. Its nonzero certificate
uses **783 trace constraints only**. It uses none of the whole-slice 30-, 82-
or 25-hole numerical imports present as optional strengthening in that LP.
Thus this particular proof depends only on legitimate coordinate erasure,
the same-end trace lemma, and exact integer arithmetic. It does not depend on
the public cyclic data, the new signotope cyclic packet bridge, NINE29's 222
bound, or TRANSFER-NEXT's 185 bound.

Let the 783 positive integer row weights be those in
[certificate.json](run-native-v2/certificate.json). For every one of the 924
states compute its integer load l_W. The separately implemented
`verify_cert.py` regenerated the support of every selected row from q,p,
tested its actual difference cells and its two legal chains, and obtained:

| Exact quantity | Value |
| --- | ---: |
| Weighted row RHS D | 232590437 |
| Scale Lambda | 1000000 |
| Maximum state load | 1000003 |
| Overload penalty P=sum max(0,l_W-Lambda) | 201 |
| D-P | 232590236 |

If H denotes the number of actual missing states, their indicators are 0 or 1,
so `D <= sum l_W h_W <= Lambda H+P`. As

`232590236 > 232 * 1000000`,

we obtain **H>=233**, and hence

`N_sig(9,8,8) <= 924-233 = 691`.

Combining this ordinary capacity with the already completed actual residual
bound `D9<=463` from [NINE30-MOVE](../NINE30-MOVE.md), the same R7/R20 interfaces
give `N_sig(9,8,9)<=1154`, `N_sig(9,9,9)<=1155`, and the planar forcing
threshold **ES(9)<=1156**. This calculation keeps the residual's actual
junction restriction; it does not replace D9 by an ordinary rectangle.

## Actual bindings and receipts

The native v2 generator hash is
`8d25cbcf18232c84aee5a7f9393491bcfc710facd6bf3fadd346e528d5d7e4bd`.
The generated complete row catalogue hash is
`bd41e0a38be7a9aa3911c309b6893cdf9ad99b7411bdb0256e7b56ce78e7f5d0`.
The independent checker source hash is
`93d77d5fc5560a5c006d988ce29ae7df538b48f1f3366b314d453daa02e0ae7a`.

The parent authorized exact single-file delivery and the seven worker used
its existing authenticated connection to transmit those frozen bytes to the
same authoritative Linux host. Both remote hashes were matched before run.
The original Python3.12/no-SciPy failure was preserved; the successful run
used the existing same-host `/opt/anaconda3/envs/forktqiu/bin/python3`.

Primary local receipts are [result.json](run-native-v2/result.json),
[run log](run-native-v2.log), [run exit](run-native-v2.exit),
[independent check log](verify-cert.log), and [check exit](verify-cert.exit).
The raw 7.7MB `rows.json` remains at the same directory on Linux:
`/data/ktqiu_hdd/math_agent/reports/n79-overlap-20261116/direct-cycle-lp/run-native-v2/rows.json`.
The selected metadata is reproducibly regenerated by the frozen source; its
full support and exact arithmetic were read and checked on Linux.

The returned small evidence archive is
`../octagon-source-replay/lp-min-evidence.tgz`, SHA-256
`9c068693e9ae8b9cb748e5e4cc15576743ec5cebdf0c3b6ff647f5a38422c44f`,
matched on Linux and Windows. No mathematical code or solver ran on Windows.
