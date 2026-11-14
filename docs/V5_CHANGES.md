# v5: control proof interfaces and reuse theorems across representations

**v5 is the current workflow on `main`.** It deepens the existing five solving stages and hypercube-Hamilton plugin, retaining ten base skills, six domains and fourteen domain skills. Clone `main` or [download its ZIP](https://github.com/lisresearchgroup/math-rsi/archive/refs/heads/main.zip), then record the exact commit. Fixed v1–v4 snapshots remain unchanged.

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

The [implementation record](../development/evolution/v5-q7-20261114/EVOLUTION.md) and [Hamilton evidence report](../plugins/hypercube-hamilton/evidence/Q7_V5_IMPLEMENTATION.md) own the commands, inputs and exact acceptance scopes. The shared [actual-input reference](https://github.com/lisresearchgroup/math-rsi/blob/main/base/skills/mathrsi-prove/references/actual-input-coverage.md) connects the three base actions to real callers.

| Actual v5 maintenance check | Verified scope |
| --- | --- |
| T63 target04, full | Reconstructed all 4,096 × 4,096 = 16,777,216 connectivity bits and obtained GF(2) rank 4,096; 80.14 seconds wall time. |
| Legacy Q6 A10 compatibility | Reconstructed all 1,024 × 1,024 = 1,048,576 bits and obtained rank 1,024 with the existing root interface. |
| Relocated S3 and S2_STRONG consumers | Both PASS from the repository's selected portable inputs: 18,049 and 19,718 plans, respectively. Frozen non-time fields matched. |

These consumers cover overlapping stated families; their counts are not aggregate Q7 coverage. The other five T63 targets were not rerun. The selected finite checks retain the imported rank bridge, nonzero-column argument and expansion obligations; they do not newly accept the entire proof chain.

Presentation validation covers links, the explicitly selected public build, bilingual desktop/mobile rendering and play/replay through v5. Original research provenance remains v3 (local adaptation).

[Implementation/evolution index](../development/README.md) · [Separate maintenance workflow](EVOLUTION_WORKFLOW.md) · [Public publication boundaries](PAGES.md).
