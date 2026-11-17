# Position-free 14-through silent-domain probes

Two position-free necessary-condition models have actual SAT witnesses,
independently verified against the saved DIMACS and every physical path:

| Domain | Silent L positions | Silent R positions | Actual blue fours | Result |
|---|---|---|---:|---|
| 17 points, T14+L1+R2 | `{6}` | `{13,15}` | 1 | SAT, independently verified |
| 18 points, T14+L2+R2 | `{1,2}` | `{8,10}` | 9 | SAT, independently verified |

These demonstrate an obstruction to proving nonexistence from the stated
**local necessary conditions alone**. They are not 75-point counterexamples,
do not exhibit ambient red-six anchors for the 14 T labels, do not establish
geometric realizability, and do not refute the parent's stronger analytic
argument. The parent subsequently obtained an analytic exclusion of D37 and
requested controlled closure of this computational subtask. No new search or
budget extension was launched after that instruction.

## Baseline model and coverage

On ordered physical vertices `0,...,n-1`, L and R are disjoint role selections,
with exact populations `(1,2)` for n=17 or `(2,2)` for n=18. All remaining
14 vertices form T. No role position or macro-order was fixed. The reflected
17-point `(2,1)` case is equivalent under order reversal and exchanging L/R;
SAT in the displayed orientation transports to that orientation as well.

The physical coloring satisfies:

1. Every rank-3 four-point packet has at most one color change.
2. No red seven-point path and no blue five-point path occur.
3. No opposite-color same-endpoint paths have vertex-count sum at least nine.
4. Every blue four-point path starts in L and ends in R.

Condition 4 implies that both `T+L` and `T+R` have no blue four. Its source in
the original mathematical caller is
[the t=14 recovery domain](../../.trellis/tasks/10-19-nr7-structure-capacity/research/N7_T15_UNIQUE_BLUE_FOUR_EXCLUSION_20261112.md#74-t14的一个明确开放入口).
All actual ambient through/quiet-point facts are consumed only through these
specified induced-domain consequences. L/R/T labels in a SAT witness are not
asserted to extend to their namesake ambient roles.

There is one physical variable per triple, true meaning red. Two role variables
per vertex select L/R. The remainder is T. Exact small role counts use explicit
subset clauses. Endpoint flags for red-five and red-six existence receive an
implication from every actual candidate path. Red-five flags forbid every
same-endpoint blue four; red-six flags forbid every same-endpoint blue three.
These are the only weak-seven splits left when red seven and blue five are
absent. A canonical assignment sets a flag precisely when some such physical
path exists, so all physical colorings satisfying the model extend to the
auxiliaries. Flags are not used to count exact ambient paths or assert missing
anchors. No production C_r encoding was imported or edited.

## Actual witness content and independent verification

The 17-point witness's only blue four is `(6,9,10,13)`. Its complete physical
color table is `n17-L1-R2-base/colors.tsv`, and its complete independent witness
is `n17-L1-R2-base/independent-witness.json`. It has 240 red six-point paths,
of which 31 are T-internal. Its longest red/blue paths have six/four vertices.

The 18-point witness's complete blue-four list is:

```text
1 3 5 8
1 3 5 10
1 3 8 10
2 3 5 8
2 3 5 10
2 3 8 10
2 4 5 8
2 4 5 10
2 4 8 10
```

It has 237 red-six paths, of which 40 are T-internal. In particular, some blue
fours use an R point internally; the stronger pure-role condition that both
internal vertices must be T is absent from, and not implied by, this baseline.
Its literal colors and complete path enumeration are retained analogously in
`n18-L2-R2-base/`.

`verify.py` imports no generator or solver code. For each actual SAT result it
parses the literal saved DIMACS, requires a complete consistent assignment to
all variables, and checks every clause. It independently reconstructs triple
and role variable numbering, checks every packet, enumerates every increasing
physical subset of at least two vertices as a candidate path, and records all
realized monochromatic paths. It checks every pair of realized red/blue lengths
with each common outer endpoint, including overlapping interiors and all sums
at least nine. Both witnesses passed every check in 1.48155 seconds on Linux.
`independent-verification.json` is the compact receipt; the per-case JSON files
contain every path and every physical color.

## Two stronger bounded probes: unresolved, not exclusions

The parent supplied stronger pure-role consequences during this subtask. They
were placed in separate fresh formulas, preserving both baseline witnesses.

`n17-L1-R2-pure` assumes one pure P0 and two pure Q0 silent points, with the
parent's opposite-direction ambient R5/B4 imports. It adds T-internal B4
interiors, full blue fans for each B4, through bad-source/bad-terminal red fans,
and the specified red-six endpoint restrictions. `probe_pure.py` records the
exact clauses. The 20-second run returned **UNKNOWN**, with solver exit zero
and no outer timeout termination.

`n18-typed-two-missing` uses four free-position pure silent types LA,LN,RA,RN,
one of each, plus T14. LA has the incoming ambient R5 import; RA has the outgoing
ambient R5 import; the corresponding LN/RN imports are missing. It requires
actual blue fours LA-to-RN and LN-to-RA, forbids LA-to-RA, and requires all B4
interiors to lie in T. Only an anchored source LA activates its initial blue fan
and bad-source T-red fan; only an anchored terminal RA activates its terminal
blue fan and bad-terminal T-red fan. Every W-red-six has T endpoints, as supplied
by pure-role membership and opposite-direction B4 hotness with the common
W-endpoint blue-five prohibitions. These are local consequences, not invented
R5/R6 witnesses inside W. `probe_typed18.py` retains the exact model.

The last probe was already running when the parent closed D37 analytically. Its
existing 20-second budget was allowed to finish without extension, producing
**UNKNOWN**, again with exit zero and no outer timeout termination. Neither
stronger formula received an UNSAT result or DRAT acceptance. Their source and
CNF are experimental models; there was no separate complete semantic-CNF audit
for either unresolved formula. No mathematical exclusion is inferred from them.

## Execution, bindings and reproduction

All scientific execution ran on authoritative Linux `ubun`, using
`/opt/anaconda3/envs/forktqiu3/bin/python3.12`, external
`/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat`, and fresh case
directories. The baseline runs took 2.41999 and 3.52252 seconds, both with solver
exit 10. Each enhancement had a 20-second solver budget, a separate process
group and a 30-second outer bound with SIGTERM/SIGKILL and process reaping.
All four jobs finished normally within their outer bounds. No checker was
invoked, since no UNSAT result occurred. A file named `proof.drat` from SAT or
UNKNOWN execution is not a checked UNSAT certificate.

The authoritative root is
`/data/ktqiu_hdd/math_agent/reports/n767-t14-silent-domains-20261112`.
Every case retains the literal CNF, source bindings, spec, original solver
stdout/stderr, raw proof output and result JSON. `manifest.json` binds the final
retained files. `runtime.json` binds the original solver/checker executables;
the enhanced results additionally bind their actual source and base source.

The local `witness-evidence.tar.gz` contains source, all four CNFs, both complete
literal SAT witnesses, logs, summaries and bindings; it intentionally omits raw
`proof.drat` files, which carry no proof acceptance in these runs. The original
raw proof files remain on Linux. The archive is extracted beside this report.

From the extracted complete local model/witness package copied to Linux,
recheck both SAT witnesses without launching a solver:

```bash
/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B verify.py
```

Fresh solve reproduction uses the relevant source in a new directory together
with `probe.py` where imported; existing case directories are create-only.
The role-freedom and actual SAT color tables are the reusable findings. This
subtask did not prove a local nonexistence theorem, modify the parent's proof,
start an external review, or change sealed jobs, production encodings or Goals.
