# Repair an overlapping-edge probability proof

This is a small runnable example of entering MathRSI with a complete candidate, finding a concrete error, repairing the argument, and handing back a readable proof. The exact theorem is:

> For every finite set V and every simple 4-uniform hypergraph H on V with at most seven edges, there exists a map c: V → {red, blue} such that every edge contains both colors.

The input proof incorrectly transfers independence of individual vertex colors to the events that overlapping edges are monochromatic. The theorem remains true. Its repair uses the finite union bound, with probability of a good coloring at least `1 - m/8 >= 1/8`.

## Starter and completed reference

| Path | Purpose |
| --- | --- |
| [starter/REQUEST.md](starter/REQUEST.md) | Task contract to give an agent |
| [starter/PROOF.tex](starter/PROOF.tex) | Deliberately faulty candidate; this is the exercise input |
| [reference/PROOF.md](reference/PROOF.md) | Completed readable mathematical proof |
| [reference/PROOF.tex](reference/PROOF.tex) | Completed TeX proof with unchanged theorem environment |
| [reference/VERIFICATION.md](reference/VERIFICATION.md) | What was checked, historical assurance and remaining dependency |
| [replay.py](replay.py) | Exact standard-library counterexample and repaired-bound arithmetic |

The reference is supplied for reading and comparison. An agent's new run should generate its own audit and handoff in a separate workspace. Do not copy the completed reference into its starter input or pass it to a supposedly blind reviewer.

## Replay the exact arithmetic without an agent

From the clone root:

```bash
python3 examples/proof-repair/replay.py
```

Python 3.9+ is sufficient; no packages, model, network, TeX or Lean are needed. Expected output, with exit code zero:

```text
32 colorings: P(Be)=1/8, P(Bf)=1/8, P(both)=1/16; independence product=1/64
Counterexample to the input's event-independence claim verified.
Union-bound arithmetic checked for m=0,...,7; minimum good-coloring bound=1/8.
The universal theorem is established by reference/PROOF.md, not by this finite replay.
```

The two distinct edges are `{0,1,2,3}` and `{0,1,2,4}`. Both are monochromatic precisely when all five vertices have the same color: two of 32 colorings, giving `1/16`. Independence would give `1/64`. This is a counterexample to an intermediate claim, **not a non-colorable hypergraph** and not an enumeration of the theorem's full domain.

## Run the workflow on fresh starter input

First follow [the quickstart](../../docs/QUICKSTART.md) to clone and choose Codex or Claude Code. From the clone root, create an isolated task directory and copy only the two input files:

```bash
export MATHRSI_ROOT="$(pwd -P)"
export ARIS_REPO="$MATHRSI_ROOT/base"
export TASK_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/mathrsi-proof-repair.XXXXXX")"
cp "$MATHRSI_ROOT/examples/proof-repair/starter/REQUEST.md" "$TASK_ROOT/REQUEST.md"
cp "$MATHRSI_ROOT/examples/proof-repair/starter/PROOF.tex" "$TASK_ROOT/PROOF.tex"
```

Start `codex --add-dir "$TASK_ROOT"` or `claude --add-dir "$TASK_ROOT"` from the clone root. Then give this natural-language request, replacing the placeholders with the actual absolute paths printed by your terminal:

```text
Read <clone>/base/skills/mathrsi-research/SKILL.md and execute REQUEST.md
in <task-directory>. The complete candidate is <task-directory>/PROOF.tex.
Choose the applicable entry from the existing candidate; preserve the original
as ORIGINAL_PROOF.tex before editing. Use the current host's bundled ARIS
skills, with ARIS_REPO=<clone>/base and absolute helpers from that clone.

Use a fresh independent reviewer available in this host for the proof audit,
recording the actual backend and scope. Report same-family review as provisional.
If the required reviewer is unavailable, retain that review as pending; do not
invent a successful call. Do not use examples/proof-repair/reference as reviewer
input. Keep generated work in the task directory and preserve the exact theorem.
Repair any genuine error, execute the applicable verification, and deliver the
full readable proof, actual audit, verification and reproducibility handoff.
No novelty search, new Goal, global service installation or Lean is requested.
```

The expected useful path is `mathrsi-research → mathrsi-verify → proof-checker → mathrsi-handoff`. It need not recreate research preparation or route design for this elementary complete candidate. The request authorizes a bounded exercise, approximately 15 minutes; unavailable dependencies should leave an accurate recovery entry. If your intended route needs MCP setup, configure it first using [REVIEWER_MCP](../../docs/REVIEWER_MCP.md).

On an environment with `pdflatex` and `amsmath`, `amssymb`, `amsthm`, compile a proof from its directory using:

```bash
pdflatex -interaction=nonstopmode -halt-on-error PROOF.tex
```

This checks TeX compilation. Inspect the resulting PDF as a separate display check. Additional audit-report compilation follows the actual checker output and its package requirements; it is not reproduced by this proof-only command.

## What was actually validated

This example is adapted from the [bounded workflow trial](../../development/figure-workflow-check-20261101/trial/TRIAL_REPORT.md). That trial preserved the input theorem, found the independence error through a fresh reviewer, replayed the 32-coloring counterexample, implemented the union-bound repair, consumed two further fresh positive source reviews, and produced a proof and handoff. The reviewers were native Codex agents: **same-family, provisional**. The historical audit recorded mathematical PASS with `workflow_complete=false`.

The historical proof and audit-report TeX compilation attempts returned **127** because `pdflatex` was missing. No successful PDF build or PDF inspection occurred. No Lean, cross-family assurance, full fresh literature/route/research chain, theorem-domain enumeration, or general efficiency evaluation was performed. The trial did not initialize a task wiki for this short exercise. Raw historical records remain in the development directory; this clean example does not duplicate their logs or imply that replaying the arithmetic reruns their reviews.

The reference theorem is supported by the complete elementary proof. The Python replay provides exact evidence for the faulty step and arithmetic, while the universal reasoning is in the proof itself. [Reference verification](reference/VERIFICATION.md) records this distinction and the pending compilation accurately.
