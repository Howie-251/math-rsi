# v4: recover equality structure and deepen two existing plugins

**[v4](https://github.com/lisresearchgroup/math-rsi/tree/v4) is the preserved v4 harness release; [v5](V5_CHANGES.md) is the current workflow on `main`.** Fixed v1/v2/v3 snapshots are unchanged. This increment retains **10 base skills, six domains and 14 domain skills**; it strengthens existing workflows and plugins rather than increasing their count. The [maintenance record](../development/evolution/v4-20261108/EVOLUTION.md) owns implementation and acceptance status.

## Subsequent v4 maintenance on `main`: global reassessment

The fixed `v4` tag preserves the release described below. This subsequent increment belongs to v4 maintenance on `main`; it is not contained in that tag, does not move any tag and is not v5. The base remains ten skills across five solving stages, with six domains and fourteen domain skills.

Every dispatch batch and result return checks progress against the original problem’s bottleneck. Global reassessment is mandatory after two consecutive batches at the same bottleneck without a decision-changing gain, when local results accumulate without improving the critical connection, full-domain coverage or end-to-end cost, or when a preset checkpoint or expansion budget is reached. By default two independent read-only agents examine (1) the original-target connection and route and (2) total cost and alternatives; a third resolves material disagreement when needed.

A mathematically valid reduction is assessed separately for usefulness. Fewer parent objects can still leave a larger extension space; proving a new representation's own internal lemmas does not by itself reduce the original gap. Compare the outstanding obligations, callable tools and total completion cost before and after. Without a task-specific checkpoint, reassess after three substantive batches on the same route; an already assessed finite completion plan keeps its own boundaries.

Root consumes their actual findings and executes a bounded continuation, missing connection, new representation, route transfer, assembly or scope closure. After triggering, do not expand the old route before that decision; preserve evidence and useful running computations. Record the next trigger in the existing report and `NEXT_SESSION`, without a parallel ledger or automatic Goal pause. Necessary full-domain computation that is feasible and closes an original obligation continues; short proofs do not acquire ceremonial reviews. The [shared execution contract](../base/skills/mathrsi-research/references/global-reassessment.md) owns the detailed caller/return behavior. This maintenance does not establish a measured speedup.

The [maintenance record](../development/evolution/v4-global-reassessment-20261108/EVOLUTION.md) links Gemini's design and implementation review, two independent historical decision exercises, the actual caller integrations and documentation/browser checks.

## Subsequent v4 maintenance on `main`: ECC node research

[PR #19](https://github.com/lisresearchgroup/math-rsi/pull/19) adds a Markdown execution protocol to the existing ECC plugin. It is subsequent v4 maintenance on `main`, outside the fixed `v4` tag. It adds no base skill or mathematical result.

Before advancing, resuming, changing methods or dispatching work, `mathrsi-ecc` matches the actual object, target and coverage to a stable `node_id` and records a `task_id`. Existing exclusions prune covered work; unfinished tasks resume from real checkpoints. Changing basis or algorithm keeps the mathematical node. Shared computations have one task and multiple consumers; uncertain membership first becomes a scope-check task. Existing task records and the research wiki carry these decisions.

`ecc-certificate` checks the precise local result and its connection to the caller. Closing a parent additionally requires coverage of its full domain, all necessary child evidence and valid dependencies; completed tasks alone do not close it. The base global-reassessment protocol retains priority when choosing the next route.

- [Node protocol](../plugins/ecc/skills/mathrsi-ecc/references/node-research.md): object identity, coverage, dispatch and result return.
- [Minimal work package](../plugins/ecc/skills/mathrsi-ecc/examples/node-work-package.md): reusable node/task fields and acceptance conditions.
- [72/36 branch example](../plugins/ecc/skills/mathrsi-ecc/examples/node-research.md): algebraic branches, uncovered remainders and shared extension work; a teaching example, not a new solution.
- [Validation record](../plugins/ecc/evidence/NODE_RESEARCH_VALIDATION.md): link and manual execution-path checks, plus a small algebraic replay; no original-problem scan or Goal was started.

## A stronger shared base

When a proof misses an integer threshold by one, the existing [route-loop](../base/skills/mathrsi-route-loop/SKILL.md), [prove](../base/skills/mathrsi-prove/SKILL.md) and [verify](../base/skills/mathrsi-verify/SKILL.md) now connect three actions:

1. Follow the same inequality chain back through its nonnegative slack terms. Identify which equalities must hold simultaneously on the same mathematical object.
2. Use those constraints to make a legal equal-size replacement and any required augmentation. Verify the resulting object meets the applicable capacity theorem’s other premises; exceeding that capacity then forces an actual witness.
3. Require that witness to carry the endpoints and marked data needed at the original caller, then reconnect the conclusion to the original input.

The new behavior is the connected use of equality structure, legal replacement and compatible witnesses at a tight integer threshold. Common objects, counterexample feedback, marked transformations and evidence inheritance already existed; they are retained rather than counted again as new capabilities. Domain lemmas and numerical thresholds remain in their plugins. The [executable proof reference](../base/skills/mathrsi-prove/references/critical-equality.md) supplies the trigger, actual objects, legal-operation checks and return paths.

## Deeper Happy Ending methods

The existing [Happy Ending research skill](../plugins/happy-ending/skills/mathrsi-happy-ending/SKILL.md) and [certificate skill](../plugins/happy-ending/skills/happy-ending-certificate/SKILL.md) consume the new 75/76/77 proof chain and its failure examples. The manuscripts claim `N(7,6,7) ≤ 75`, `N(7,7,7) ≤ 76` and `ES(7) ≤ 77`. Their structural arguments retain their **same-session / unreviewed / unaccepted** status; absorbing a method does not accept the underlying theorem.

The domain supplies the cup/cap and matching interpretation of the base actions: recover simultaneous equality constraints, make legal replacements, use capacity to force witnesses, and check that their endpoint roles fit the intended extension. Concrete counterexamples delimit tempting stronger claims. The [equality-and-exchange reference](../plugins/happy-ending/skills/mathrsi-happy-ending/references/equality-exchange.md) gives the actual same-root construction and distinguishes the conditional ≤74 subclasses from the still-open unconditional strengthening. This deepens the existing plugin rather than creating a second Happy Ending workflow.

## Deeper degree–diameter methods

The existing [degree–diameter plugin](../plugins/degree-diameter/README.md) gains the concrete `(10,4)` extension method and portable finite-edit replay. Delete a matching of five edges from a saturated 10-regular graph and connect a new vertex to the ten endpoints; use old-only switches where needed and diagnose failed vertex pairs across the whole graph. Preserving degrees alone does not establish the diameter. The [saturated-insertion and replay reference](../plugins/degree-diameter/references/saturated-insertion-and-replay.md) gives the move assumptions, distance obligations, concrete failure return and portable invocation.

The resulting graph has **2,567 vertices, 12,835 edges, degree 10 and exact diameter 4**. It improves the Comellas table entry of 2,566 checked 2026-11-05. It was constructed in a **v2 + DD run with the PR #7 handoff repair**, not with v4. The published 2,557 seed, local 2,566 predecessor and dated public 2,566 comparison have different roles.

Replay reconstructs the ten accepted orders 2,558–2,567 from a seed and literal edits; it does not rerun discovery, BFS or Lean. Preserved all-roots BFS and Lean final-assembly receipts retain their original scopes. External formal C review remains incomplete, and the portable package does not contain the full rebuildable Lean project. Catalogue totals are 163 graph instances / 44 parameter pairs / 49 completed concrete-graph Lean instances, including accepted intermediate graphs; these are not 163 new records.

## Implementation and bounded use

The [Happy Ending implementation record](../development/evolution/v4-20261108/HAPPY_ENDING.md) records two successful bounded commands. The new [strategy-example checker](../plugins/happy-ending/tools/check_strategy_examples.py) checks the fixed 11-point and 10-point counterexamples directly from triple colors: 3,049 increasing vertex subsets and 540 four-point packets. The 11-point example has private paths for each external point without the required cross-side compatibility; the 10-point example admits each new point separately but creates an actual forbidden path when both are added. These results reject the corresponding unconditional strategy claims; they do not verify the full 75/76 proof chain. See the [actual strategy results](../development/evolution/v4-20261108/usage/happy-ending/strategy-examples.json).

The existing lower-25 checker was also rerun successfully: 2,300 triples, 12,650 packets, all 300 endpoint pairs and the 35-downset catalogue, with `e = m = 9`. This checks one abstract lower witness, not a new upper bound or planar realizability. See the [actual lower-witness result](../development/evolution/v4-20261108/usage/happy-ending/lower25.json). No full structural-proof independent review, original 55-cell CNF/certificate replay, Lean build or geometry check was performed. New structural manuscripts remain **same-session / unreviewed / unaccepted**; the missing TB certificate/checker is not supplied by these bounded checks.

The [DD implementation record](../development/evolution/v4-20261108/DD.md) records a successful invocation of the bundled replay for all ten graphs. Current literal checks passed order, edge count, label legality, simplicity and degree 10 for every output. This use did not run BFS or Lean, or repeat comparison with the accepted original edge files. See its [actual results](../development/evolution/v4-20261108/usage/dd/RESULT.json).

Actual changed files, commands, readback and review dispositions are recorded in the [v4 maintenance directory](../development/evolution/v4-20261108/EVOLUTION.md). Documentation validation and its limits are recorded in [DOCS.md](../development/evolution/v4-20261108/DOCS.md). This release does not resume historical mathematical Goals, relabel results as v4 runs, or establish an equal-budget performance gain.

Earlier changes remain available in [v3](V3_CHANGES.md) and [v2](V2_CHANGES.md). Existing v3 overview figures describe that release; they are not v4 implementation diagrams.
