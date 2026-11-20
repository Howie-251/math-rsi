# Happy Ending / Erdős–Szekeres & N(m,r,s)

[Current bilingual reader](../../development/homepage-redesign-20261105/site/happy-ending-latest.html) · [2026-11-20 handoff](../../plugins/happy-ending/archive/nmrs-20261120/HANDOFF.md) · [Verification scope](../../plugins/happy-ending/archive/nmrs-20261120/VERIFICATION.md) · [Replay](../../plugins/happy-ending/archive/nmrs-20261120/REPLAY.md) · [Domain methods](../../plugins/happy-ending/skills/mathrsi-happy-ending/references/nmrs-higher-bounds.md)

N(m,r,s) is the maximum population of a complete ordered rank-3 signotope avoiding a blue r-vertex path, a red s-vertex path and weak m: opposite-colour paths on the same actual endpoints with total length at least m+2. Paths count vertices. Write Q_m=N(m,m−1,m) and F_m=N(m,m,m). The R20 chart and reverse-extension manuscript gives F_m=Q_m+1; geometric inclusion adds another one to obtain the planar forcing threshold ES(m)≤F_m+1. The junction-restricted R7 residual D_m is a different capacity from ordinary N(m,m−2,m).

## Current analytical working bounds — 2026-11-20

| m | Q_m | F_m | Planar ES(m) | Source and guarantee |
| --- | ---: | ---: | ---: | --- |
| 7 | ≤75 | ≤76 | ≤77 | Earlier joint replacement and common-root manuscript; historical b25 import retains its recorded scope. |
| 8 | ≤292 | ≤293 | ≤294 | Global same-lock compensation and near-saturation exchange; ordinary 866≤56 is supported by historical fixed-CNF DRAT evidence. |
| 9 | ≤1098 | ≤1099 | ≤1100 | Same-input sector budget with ordinary u=222,t=380. Each bound is 48 below the previous 1146/1147/1148 working chain. |
| 10 | ≤3978 | ≤3979 | ≤3980 | Ordinary-row propagation, an integer obstruction to equality, and the same-input sector budget with u=773,t=1372. |

The new portable checker, its negative control and final repository/site checks are **prepared but unexecuted on Linux** because the authoritative server was unreachable. See VERIFICATION and REPLAY above for the exact pending commands; historical successful receipts are retained separately.

These are **same-session / unreviewed / unaccepted analytical manuscripts**, with no optimality or priority claim. The independent review attempt returned no substantive mathematical opinion. There is no Lean formalization. The new sector-deficit mathematics and corollaries were proposed in the main research session; Sol/high transcribed them and checked text and links. Earlier manuscripts, historical SAT evidence and literature imports keep their own provenance, recorded in the handoff.

## Reusable mathematics and the remaining gap

On one original Q_m input X, define red and blue source sets S,B and their four sectors. For ordinary bounds u,t at the same m, the manuscript constructs two actual induced subdomains I,Y and all penultimate-vertex sets V_q of the last owner of each distinct lock. It proves

$$\delta=u+t-b-p=[u-|I|]+[t-|Y|]+\sum_q(|V_q|-1)+|L\setminus O|\ge0,$$

and combines their shared deficit with ordinary-row slack ρ and slice deficit ε:

$$(m-2)|X|+\rho+\epsilon+(m-3)\delta=(m-1)\binom{2m-7}{m-4}+(m-3)u+(m-2)t.$$

This is a budget on the same actual input. Restricting X requires recomputing all sources, locks and deficits. At 1098 points for m=9, the budget forces δ=0 and at most two unsaturated rows; at the surviving 292-point m=8 types, it forces two actual subdomains to reach 56 and 100 simultaneously. The full all-path family is retained; one representative path does not suffice.

The positive-deficit targets δ8≥6 for every 289-point Q8 input and δ9≥11 for every 1089-point Q9 input remain **open**. They would imply Q8≤288 and Q9≤1088 respectively. The 19-lock m=8 scalar types are excluded by the ordered-interval inequality 5|L|≤z, while remaining scalar types are still unresolved. Fixed-width three-, four- and five-column deficit transport is a separate general-family direction; it does not automatically improve a small-m diagonal bound.

## Evidence layers and earlier contributions

| Material | What it supports | Scope retained |
| --- | --- | --- |
| Historical b25 acceptance and checked E21 25-point colour table | Restricted upper-bound import and a separate abstract lower witness | Same-family/provisional upper acceptance; no geometric realization from the witness; TB-scale proof bodies external. |
| Ordinary 866≤56 and 858≤64 | Historical fixed-CNF UNSAT checks and source/CNF rebuilding evidence | Mathematical reduction to the fixed CNF remains a separate bridge. Ordinary 858≤63 is pending. Large proof bodies are not replayed by the new lightweight checks. |
| Native-trace integer duals C9≤688,D9≤458 and 47,635-row rational witness | Exact finite inequalities and the depth-≤3 LP ceiling | The existing 1146/1147/1148 working assembly and its imports remain available independently of the stronger new analytical chain. |
| Milestone9 115-row certificate and nine-hole vector | Earlier ordinary 866≤61 and exact minimum nine for that row matrix | The vector is a matrix witness, not a 61-point signotope. |
| Schroeder's public octagon omission trees | Attributed 15-file finite arithmetic, used with the project's signotope transfer bridge | Planar ES(8)≤319 is Schroeder's published preprint result; the project's earlier abstract transfer is a separate working argument. |

[2026-11-17 evidence and commands](../../plugins/happy-ending/archive/nmrs-20261117/HANDOFF.md) · [Earlier seven-parameter reader](n7-20261103/START_HERE.html) · [Plugin and checkers](../../plugins/happy-ending/README.md)

The initial b25 and 75/76→77 work used Trellis + standalone ARIS through November 3; the November 5–17 work used Trellis + ARIS + MathRSI v3 and was subsequently integrated into v6 main maintenance. This November 20 incremental handoff preserves those execution attributions and fixed release tags. Packaging, text checks and finite replay do not constitute independent mathematical acceptance.
