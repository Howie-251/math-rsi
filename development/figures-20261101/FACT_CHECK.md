# Figure facts — 2026-11-01

Checked against `AGENTS.md`, `README.md`, `docs/WORKFLOWS.md`, and `docs/PLUGIN_CONTRACT.md`. Suggested English labels below are descriptions, not new product/version claims.

## Figure 1: shared base, domain plugins, reviewed improvement

Use **“mathrsi-base-v1”** for the requested conceptual starting version; **“Mathematical problem”**, **“Select domain methods”**, **“Property B plugin”**, and **“ECC plugin · draft”** for domain selection. The base supplies general research workflow and complete bundled ARIS capabilities; plugins supply domain knowledge, methods, diagnostics, and checkers. The task workspace owns the problem specification, proofs, wiki, evidence, and recovery state.

Accurate feedback labels: **“Research experience” → “Proposed improvements” → “Separate review and evaluation” → “mathrsi-base-v2 · conceptual next version”**. Domain knowledge can also feed a separately maintained plugin update. A research run does not directly rewrite base or acceptance criteria. Do not depict v2 as released or RSI gains as measured.

## Figure 2: five subworkflows inside the base

| English label / actual skill | Responsibility and returned result | Main ARIS skills / domain entry |
|---|---|---|
| **Prepare problem & literature** / `mathrsi-prepare` | Recover or clarify; search alternate names, citations, counterexamples and errata; read key imports; fix the exact target. Return specification and usable literature. | `research-lit`, `research-wiki`, `wiki-enrich`; Property B `propertyb-literature`. Internally: `specify → survey → specify`. |
| **Iterate solution routes** / `mathrsi-route-loop` | Propose a route; challenge across models; run informative probes; implement revisions and re-review. Return an actionable route, open assumptions, and first proof tasks. | Mathematical adaptation of `auto-review-loop`, using `research-review`; Property B `propertyb-bound-lab` diagnosis. |
| **Advance the proof** / `mathrsi-prove` | Derive, prove, construct or compute; reclaim results and connect them to the actual original input. Return a candidate proof, witness, or precise gap. | `formula-derivation`, `proof-writer`, targeted `research-review`; Property B `propertyb-bound-lab` execution. |
| **Assemble & verify** / `mathrsi-verify` | Assemble when needed; check applicable coverage, exact arithmetic and proof obligations; repair and recheck; use Lean when appropriate. Return scoped verification and remaining obligations. | `proof-writer` via `mathrsi-assemble`, `proof-checker`, optional `lean-formalize`; Property B `propertyb-certificate`. |
| **Deliver & preserve knowledge** / `mathrsi-handoff` | Prepare readable proof, reproduction materials, requested HTML/package, wiki and recovery entry. Return an accurate handoff, including unfinished work when applicable. | `render-html` when requested; `research-wiki`; plugin supplies domain reproduction details. |

**“mathrsi-research · select entry, consume results, decide next”** is the orchestrator. **“Wiki & evidence throughout”** is a cross-cutting label. ARIS names above are selected capabilities, not an exhaustive list or mandatory stack.

## Return points and specific traps

- Plugins return **“Result + conditions + scope + evidence + remaining gap”** to their current caller. The single parent orchestrator starts the next sibling stage once. No recursive duplicate final-verification loop.
- New literature questions return to targeted survey, then to the same route/proof obligation. Local verification returns to its proof caller; substantive mathematical gaps return to prove; a failed core route returns to route-loop.
- Entry is flexible: a full proof can start at verify; an existing route or short proof can start at prove. A five-step mandatory waterfall would be misleading.
- Property B is the rebuilt substantive plugin. ECC is a retained **unaccepted draft**, not an equally validated implementation or default-discovered plugin.
- Model agreement, a checker exit code, local PASS, and a generated package are not interchangeable with the original theorem being proved. Lean is optional; route readiness is not theorem truth.
- Repository layering is an architectural contract, not OS permission isolation. Historical source snapshots do not authorize resuming old research.
