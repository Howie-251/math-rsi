# v5: control proof interfaces and reuse theorems across representations

**v5 is a fixed historical release (`v5` tag), superseded on `main` by [v6](V6_CHANGES.md).** It deepened the five solving stages and hypercube-Hamilton plugin while retaining ten base skills, six domains and fourteen domain skills. Fixed v1–v5 snapshots remain unchanged.

The source is Q7 research run with **MathRSI v3 (local adaptation)**. v5 absorbs its methods and diagnosed failures; it did not produce the historical Q7 results. [Result, methods and open scope](../case-studies/ruskey-savage-q7/README.md) · [Bilingual reader](../development/homepage-redesign-20261105/site/q7.html).

## Three concrete base improvements

| Research situation | Action in the existing workflow |
| --- | --- |
| A proof introduces an auxiliary pairing or other selectable object | Separate the arbitrary original input, the legal auxiliary choices and the actual successor. Choose the auxiliary object to make the next theorem applicable; do not silently require every possible successor to work. |
| A new theorem may already solve inputs represented another way | Before assigning more work, apply it across the task's known legal splits, transports and monotone completions. Preserve the return map to the same original input. Research the intersection of the failed gates. |
| A finite certificate or plan must cover every legal input | Accept either a fixed plan covering every realization of a geometry, or a finite set whose applicable branch is chosen from the actual input. Check all branches, their premises and the final expansion. |

These actions live in [route iteration](../base/skills/mathrsi-route-loop/SKILL.md), [proof development](../base/skills/mathrsi-prove/SKILL.md) and [verification](../base/skills/mathrsi-verify/SKILL.md). The [workflow map](WORKFLOWS.md) and [domain routing](DOMAIN_ROUTING.md) explain the caller/return behavior. “Known legal representations” means the available family with proved return maps; it does not require discovering every possible mathematical equivalence.

Fixed and conditional plans have different valid quantifiers. A fixed plan chooses one plan for a geometry and covers every matching realizing it. A conditional plan set proves that, for each actual matching, at least one of finitely many branches applies. Neither a sample of inputs nor an unconnected local certificate supplies that universal connection.

## A deeper hypercube-Hamilton plugin

The [existing plugin](../plugins/hypercube-hamilton/README.md) gains controlled donor pairings and return bridges, source-fiber and exact compatible-pool counting, and forest certificates with several omitted vertices. These interfaces preserve prescribed original edges through compression and expansion. The matching after compression need not belong to the old P6 input domain; its actual source and available choices matter.

The original **Q6 all-matching theorem** and its imported **at-most-six-direction application** remain available. The new Q7 headline is: **every matching with at least 57 edges in Q7 extends to a Hamilton cycle containing every prescribed edge**. Q7 has 128 vertices. At 56 edges, the μ=2 and μ=4 classes and several μ=3 families are complete. Full Q7, P7 and seven-direction extension remain open. These are results and complete subfamilies, not an arbitrary progress percentage.

## Inherited capabilities

v4's equality-chain recovery, legal exchange and compatible-witness connection remain in place. Subsequent global reassessment and ECC node/computation reuse are also inherited. The new version makes auxiliary control, cross-representation reuse and finite-plan coverage concrete at their existing call sites; it does not claim to have invented the earlier principles again. [v4 release and later maintenance](V4_CHANGES.md).

## Evidence and bounded validation

The [implementation record](../development/evolution/v5-q7-20261114/EVOLUTION.md) and [Hamilton evidence report](../plugins/hypercube-hamilton/evidence/Q7_V5_IMPLEMENTATION.md) own the commands, inputs and exact acceptance scopes. The shared [actual-input reference](../base/skills/mathrsi-prove/references/actual-input-coverage.md) connects the three base actions to real callers.

| Actual v5 maintenance check | Verified scope |
| --- | --- |
| T63 target04, full | Reconstructed all 4,096 × 4,096 = 16,777,216 connectivity bits and obtained GF(2) rank 4,096; 80.14 seconds wall time. |
| Legacy Q6 A10 compatibility | Reconstructed all 1,024 × 1,024 = 1,048,576 bits and obtained rank 1,024 with the existing root interface. |
| Relocated S3 and S2_STRONG consumers | Both PASS from the repository's selected portable inputs: 18,049 and 19,718 plans, respectively. Frozen non-time fields matched. |

These consumers cover overlapping stated families; their counts are not aggregate Q7 coverage. The other five T63 targets were not rerun. The selected finite checks retain the imported rank bridge, nonzero-column argument and expansion obligations; they do not newly accept the entire proof chain.

Presentation validation covers links, the explicitly selected public build, bilingual desktop/mobile rendering and play/replay through v5. Original research provenance remains v3 (local adaptation).

[Implementation/evolution index](../development/README.md) · [Separate maintenance workflow](EVOLUTION_WORKFLOW.md) · [Public publication boundaries](PAGES.md).

## DD follow-up · 2026-11-16

This is later **v5 maintenance on main**, outside the fixed v5 release tag. Two existing degree–diameter pairs improve: **(11,5) reaches 37,632 vertices** and **(12,5) reaches 42,433 vertices**, with maximum degree 11/12 and diameter exactly five. Local increases are +1/+31 from 37,631/42,402. Against the Comellas entries checked on 2026-11-16 (37,631/42,352), gains are separately +1/+81.

The source research ran with local 2026-11-11 main/v4-maintenance plus DD feedback updates. Its results and methods return to v5 main maintenance; they were not produced by the published v5 release. No tag moves or v6 release are involved.

**Base — Consume results before dispatch.** Update current facts from returned evidence before issuing the next task or review, preventing duplicate work and stale-state rollback. This Degree–Diameter feedback extends the existing v5 workflow. Q7 controlled-choice and theorem-reuse actions remain; fixed and conditional plans stay in the detailed capability set. [Current-context reference](../base/skills/mathrsi-research/references/current-context.md).

**DD plugin — Joint completion and verified prefixes.** Use an inclusion-minimal core-blocking set and jointly complete attachments from the full pool of remaining degree ports. Actual bad vertex pairs guide revisions to earlier construction choices; subsequent work consumes only independently verified prefixes. [Joint completion](../plugins/degree-diameter/references/d5-joint-completion.md) · [Verified blocking batches](../plugins/degree-diameter/references/d5-blocking-batches.md).

[DD evolution and implementation record](../development/evolution/v5-dd-20261116/EVOLUTION.md).

Both final graphs were regenerated exactly. D12 preserves the source's edges and checks all 31 new roots; old–old distances inherit the accepted source premise. D11 changes the core and combines the H9 theorem plus literal binding for core–core pairs with complete BFS from all 161 peripheral/new roots. Concrete end-to-end Lean instances and required source final-review obligations remain open.

Earlier (10,4)=2,567 and (16,4)=16,416 remain historical dated comparisons; the live table checked on 2026-11-16 now lists 2,612 and 16,848. This follow-up does not create a new global graph catalogue or Lean-certified count.

[Latest result and methods](../case-studies/degree-diameter/README.md) · [Bilingual reader](../development/homepage-redesign-20261105/site/dd-latest.html) · [Private source package](../plugins/degree-diameter/archive/dd-latest-two-parameters-20261116/).
