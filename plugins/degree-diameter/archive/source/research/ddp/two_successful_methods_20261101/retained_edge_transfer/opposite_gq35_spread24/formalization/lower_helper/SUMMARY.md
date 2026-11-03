# Generic lower-diameter helper: PASS

Source: `formal/DegreeDiameter/Portfolio/OppositeGQ35SpreadLowerGeneric.lean`.
Export: `DegreeDiameter.Portfolio.OppositeGQSpread.diameter_two_card_le`.

For finite nonempty `V`, a simple graph `G`, and `forward : V → Fin k → V`
covering every neighbor, `DiameterAtMost G 2` implies
`Fintype.card V ≤ 1 + k + k * k`. No concrete graph property is assumed or
certified by this module beyond these explicit generic hypotheses.

The proof fixes a root, enumerates root/one-step/two-step endpoints by
`(Unit ⊕ Fin k) ⊕ (Fin k × Fin k)`, splits each actual walk of length at most two,
and applies `Fintype.card_le_of_surjective`.

One actual directLean 4.24.0 compilation, `-j1`, exit 0; CPU 1.994863 seconds;
60 CPU-second invocation limit and 120 CPU-second overall auxiliary budget.
The same successful compilation printed the complete theorem type and transitive
axioms: `propext`, `Classical.choice`, `Quot.sound`. No repeated PASS build.
The exact command, working directory, explicit LEAN_PATH, timings, and log path
are in COMPILE_RESULT.json. `compile.py 1` reproduces this single module build.

Only this Lean module and its own lower_helper receipts were changed. No graph
file or producer mathematical data was read during this helper task; no BFS,
solver, Lean installation, lake command, native_decide, new axiom, hash, checksum,
or external review was used. The earlier literal graph acceptance remains a
separate, saved result. Main graph proof integration belongs to the main formal
agent, which has received the exact stable interface and successful build result.
