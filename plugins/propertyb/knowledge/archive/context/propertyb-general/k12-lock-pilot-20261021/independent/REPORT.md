# Independent k=12, M=4660 certificate check

Status: **PASS within the scopes below**. This is a same-family independent implementation check; the structural existence/selection lemmas are outside this arithmetic task.

## Complete parameter-domain reconstruction

`check.py` imports no author scanner or certificate module. It independently rederived the pair-cover minimum-degree constraint and balanced-coloring necessary constraint over every integer 23≤v≤55920, obtaining exactly v=93,…,782. For every surviving v it checked the simple-hypergraph edge capacity `C(v,12)≥4660`; the saved candidate list and selected-mode row list match exactly and have no duplicate or omitted v.

For each selected mode it independently generated every parameter tuple. In the two-lock stage it searched for B directly by the defining strict integer inequality, rather than using the author's quotient expression. In the three-lock stage it scanned **every D from d0 through M**, then checked that the saved D is the least feasible value and that the saved Z and strict difference are exact. It checked all saved degree ranges and worst-profile membership.

| Mode | v range | Independently regenerated profiles |
|---|---|---:|
| Zero locks | 93–511 | 419 |
| One lock | 512–564 | 2929 |
| Two locks | 565–648 | 87807 |
| Three locks | 649–782 | 600274 |
| Total | 93–782 | 691429 |

All domain assertions passed. Full per-v details: `DOMAIN_CHECK.json`.

## Independent probability arithmetic

`check.py` rewrites the endpoint probabilities, ordered critical-pair probabilities, and greedy minimum compulsory bad-pair deletion in Python `Fraction`. The unlocked formula includes its separate global overlap deduction. No floating point participates in a decision. It recomputed **31 profiles** covering each mode's saved global maximum, both sides of every mode transition, outer endpoints, degree-range upper endpoints, and both separate/triple three-lock incidence types (including low and high degree extrema at the sampled three-lock vertices). Every exact U is at most the saved per-v fixed-point upper bound, and that bound is strictly below one. Full exact rational numerators and denominators: `RESULT.json`.

`integer01.py` additionally rewrites and replays **all 3348 zero/one-lock profiles**, using Python arbitrary-size integers and denominator **10^20**, distinct from the author's 2^52. Upper probabilities round up and deletion probabilities round down. Every profile is strictly below one; each independent per-v maximum is at most the author's saved maximum. This complete partial replay took 1.690 seconds. Full per-v arithmetic results: `INTEGER01.json`.

The remaining two/three-lock probability values were **not** all recomputed by this second implementation. Their complete domains were independently reconstructed, and the stated boundary profiles received exact Fraction replay. This report does not claim a complete second arithmetic replay of all 691429 profiles, nor does it establish the structural selection lemmas by computation.

## Reproduction

From the project root:

```sh
python3 context/propertyb-general/k12-lock-pilot-20261021/independent/check.py
python3 context/propertyb-general/k12-lock-pilot-20261021/independent/integer01.py
```

The second command imports only the independent `check.py` and repeats its short boundary replay. Logs: `run.log`, `integer01.log`. This review did not launch Lean, Goal, MCP, or any v2 operation and did not modify author files.
