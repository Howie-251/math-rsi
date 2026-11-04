# MathRSI v3 README figures

Two new English diagrams replace the historical v2 images as the primary README illustrations. The earlier PNGs and fixed v1/v2/v3 tags remain unchanged. This is a documentation refresh, preceding the separately planned results website.

## What the figures explain

[Evolution](../../figures/mathrsi/01-evolution-v3.png) uses two aligned tracks: the shared base becomes stronger, while domain knowledge expands and deepens. It shows v0 basic research tools, v1's five adaptive subworkflows, v2's introduction of `mathrsi-meta-evolve` and evidence-transfer improvements, and the current v3's four proof-handling improvements and six domains. ECC is upgraded in place. A separate evidence-to-maintenance path returns changes to both tracks; historical research is not presented as a controlled version benchmark.

[Execution](../../figures/mathrsi/02-workflows-v3.png) starts with a problem or existing workspace, recognizes the object and goal, selects an applicable plugin or base alone, and enters the current evidence stage. Root exchanges work with scoped parallel authors and cross-model adversarial reviewers, then dispatches the current stage. The five solving stages each have a bidirectional connection to the task wiki: retrieve relevant records, use lemmas and failures, write new evidence, and read back for later reuse. Plugins supply methods to the shared stage interface. Maintenance is visually separate from solving.

The numbered stages retain their existing meanings and actual skill names. Reviewer objections drive discussion and revisions; the Verify stage retains proof checking and optional Lean. Plugin source archives supply reusable knowledge; current task results belong to the task workspace. Detailed scopes and executable operations remain in the linked skills and documents rather than being compressed into tiny diagram footnotes.

## Design discussion and applied refinements

Gemini 4 read the current README, routing, main skill and wiki operations and proposed the two-track evolution matrix and explicit coordination/wiki layers. Root retained that structure, shortened the copy and avoided the draft's redundant connectors and warning text. Gemini's stated word totals and aspect-ratio shorthand were not used as measured layout facts.

Both initial images were generated with the built-in GPT Image tool. Root inspected the images and found that Figure 1 should locate the introduction of meta-evolve in v2, while Figure 2 needed an explicit Root-to-stages dispatch path and a plugin-method connection that served all five stages rather than only Handoff. Gemini inspected the two initial PNGs and independently agreed with these changes.

One targeted GPT Image edit per figure implemented the refinements. Figure 1 adds “Adds mathrsi-meta-evolve” in the v2 base cell. Figure 2 adds a shared dispatch rail, connects it to Root and all five stages, connects domain methods to that rail, and relocates the plugin-selection connection to Recognize & route. Root visually inspected the final edited images, including the preserved five wiki read/write connectors, six plugin names, feedback paths and separate maintenance. Gemini's visual response covers the pre-edit images; the final edited PNG inspection is Root's.

## Actual discussion and generation record

- Reviewer: requested and returned `gemini-4-argon-high`, effort `high`, source `cli_selected_model_variant`; both design and visual calls returned `SUCCESS`.
- Native session: `a51c0181-806d-47c8-9565-7592b76a096d`.
- [Design request](GEMINI_DESIGN_REQUEST.md), [raw response](GEMINI_DESIGN_RAW.json), [readable response](GEMINI_DESIGN_RESPONSE.md).
- [Visual request](GEMINI_VISUAL_REQUEST.md), [raw response](GEMINI_VISUAL_RAW.json), [readable response](GEMINI_VISUAL_RESPONSE.md).
- [Figure 1 generation](../../figures/mathrsi/01-evolution-v3.prompt.txt) and [refinement](../../figures/mathrsi/01-evolution-v3-edit.prompt.txt).
- [Figure 2 generation](../../figures/mathrsi/02-workflows-v3.prompt.txt) and [refinement](../../figures/mathrsi/02-workflows-v3-edit.prompt.txt).
- [Output provenance and dimensions](IMAGE_OUTPUTS.json).

These are figure design and implementation-alignment checks, not new mathematical validation or harness performance measurements. No mathematical Goal or source project was resumed.

## Integration

Both English and Chinese READMEs display the current evolution and execution figures while retaining collapsed historical v2 images. The figures README separates current prompts from old edits. The v3 changes page and project AGENTS.md record the update. Shared base skills, plugin mathematics and Python tools are unchanged.

Repository link check: `python3 tools/check_links.py` checked 119 maintained documents and 1,764 local targets, with zero missing targets. `git diff --check` passed. Both final PNG dimensions were read from the saved files and recorded in IMAGE_OUTPUTS.json.

## Implementation references

- [Main workflow and wiki operations](../../base/skills/mathrsi-research/SKILL.md).
- [Domain recognition, selection and return](../../docs/DOMAIN_ROUTING.md).
- [Five-stage wiki read/write contract](../../docs/WORKSPACE.md#7-五阶段的-wiki-读取与写回).
- [v2 changes](../../docs/V2_CHANGES.md) and [v3 changes](../../docs/V3_CHANGES.md).
- [Separate maintenance workflow](../../base/skills/mathrsi-meta-evolve/SKILL.md).
