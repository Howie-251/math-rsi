# MathRSI architecture figures

Two coordinated English diagrams showing the current implementation and its research origins. The v2 redraw uses GPT Image with Gemini design discussion; the [review record](../../development/figures-v2-20261103/REVIEW_DISPOSITION.md) records the actual generation and review scope.

## Figure 1: From ARIS research to the current MathRSI

![ARIS standalone-skill research in Property B and ECC informs unified MathRSI v1; independent DD history informs incremental v2 with meta-evolve and a DD plugin](01-evolution.png)

The v0 stage denotes research with standalone ARIS skills in Property B and ECC. Those experiences informed unified MathRSI v1: five solving subworkflows, the Property B plugin, and an ECC draft. Current v2 incrementally extends that implementation with `mathrsi-meta-evolve`, workflow improvements, and the degree–diameter (DD) plugin. The DD historical archive independently feeds this evolution; its research was not performed using MathRSI v1.

The separate [maintenance workflow](../../docs/EVOLUTION_WORKFLOW.md) consumes research evidence to improve the existing base and plugins. Ordinary solving runs keep their selected version. The fixed `v1` and `v2` tags preserve their snapshots; this figure refresh is documentation on `main`.

## Figure 2: Five solving subworkflows and outer maintenance

![Five adaptive solving subworkflows with embedded ARIS, continuous research wiki, optional Lean, and a separate mathrsi-meta-evolve evidence-to-adoption loop](02-workflows.png)

Prepare, route loop, prove, verify, and handoff reuse embedded ARIS skills and call domain plugins where needed. The research wiki spans all stages. Targeted literature returns, route revision, and proof-repair returns preserve the active obligation; Lean remains optional.

The outer `mathrsi-meta-evolve` workflow classifies research evidence as Base, Plugin, Task, or Defer. Supported Base and Plugin changes proceed through implementation, review, actual use, and adoption. Task state stays in the task wiki; deferred proposals stay in the backlog. Maintenance is separate from solving, rather than an automatic sixth stage after handoff.

## Prompts and review

- Current Figure 1: [v2 redraw prompt](01-evolution-v2.prompt.txt).
- Current Figure 2: [v2 redraw prompt](02-workflows-v2.prompt.txt).
- Current [design discussion and review record](../../development/figures-v2-20261103/REVIEW_DISPOSITION.md).
- Historical Figure 1 prompts: [generation](01-evolution.prompt.txt), [branch correction](01-evolution-edit.prompt.txt), [plugin-group correction](01-evolution-group-edit.prompt.txt).
- Historical Figure 2 prompts: [generation](02-workflows.prompt.txt), [spacing and literature-return correction](02-workflows-edit.prompt.txt).
- Historical [2026-11-01 review and changes](../../development/figures-20261101/REVIEW_DISPOSITION.md).

Underlying executable descriptions: [v2 changes](../../docs/V2_CHANGES.md), [workflow](../../docs/WORKFLOWS.md), [maintenance](../../docs/EVOLUTION_WORKFLOW.md), and [plugin contract](../../docs/PLUGIN_CONTRACT.md).
