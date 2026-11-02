# Verification and reproducibility

The theorem is unchanged: every finite simple 4-uniform hypergraph with at most seven edges has a coloring in which each edge contains both colors. `PROOF.md` gives the full analytic argument; `PROOF.tex` is its TeX form. The theorem environment in the supplied TeX input and repaired TeX is identical.

The repaired proof uses the pointwise inequality between the indicator of a union and the sum of event indicators. Averaging yields the finite union bound; each bad edge has probability 1/8, so the probability of a good coloring is at least `1-m/8 >= 1/8 > 0`. The finite coloring space is nonempty even when V is empty, and the empty edge family is included. No disjointness, vertex-count bound, balancing condition or changed edge budget is introduced.

## Deterministic replay

From the clone root:

```bash
python3 examples/proof-repair/replay.py
```

The standard-library script counts all 32 colorings of a specific five-vertex set. For edges `{0,1,2,3}` and `{0,1,2,4}`, it obtains marginal bad-event probabilities 1/8 and joint probability 1/16, unequal to their product 1/64. It also checks exact rational positivity of `1-m/8` for all integer budgets 0 through 7. These checks establish the concrete error and repaired-bound arithmetic. The analytic proof supplies the universal quantifier over all finite hypergraphs.

## Historical audit and its limits

The [original trial report](../../../development/figure-workflow-check-20261101/trial/TRIAL_REPORT.md) and its [verification record](../../../development/figure-workflow-check-20261101/trial/VERIFICATION.md) retain the actual audit evidence. An initial fresh native Codex reviewer found the error; after the repair, a fresh full re-review and a separate fresh blind source review returned positive assessments. These are **same-family/provisional** model reviews. The original audit recorded mathematical PASS while explicitly setting `workflow_complete=false`.

The proof and audit-report compilation attempts in that trial returned **127**, because the environment lacked `pdflatex`. No successful TeX build or PDF inspection was performed. The trial did not execute Lean, cross-family review, full new-research preparation/route discovery, all-hypergraph enumeration or an efficiency benchmark. This published reference is an adaptation of that completed mathematical repair, not a fresh audit invocation.

## Compile when TeX is available

In this reference directory, with `pdflatex` and `amsmath`, `amssymb`, `amsthm` installed:

```bash
pdflatex -interaction=nonstopmode -halt-on-error PROOF.tex
```

Keep the actual log and inspect the resulting PDF. A successful future compilation resolves the proof-PDF dependency in that environment. It does not rerun a mathematical audit or compile the historical audit report. The Markdown proof is readable without TeX.

For a new agent exercise, copy only `starter/REQUEST.md` and `starter/PROOF.tex` into a fresh workspace, then generate and retain your own audit, verification and handoff there. Keep original input, revised source, review provenance and any pending actions separate. There is no active reviewer or Goal associated with this reference output.
