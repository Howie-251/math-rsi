# MathRSI two-figure design and review

2026-11-01. The user requested two GPT Image figures, with Gemini 4 composition discussion and repeated inspection after generation. This work changes presentation assets, not the mathematical research or workflow implementation.

## Sources and composition

The source contracts are `docs/WORKFLOWS.md` and `docs/PLUGIN_CONTRACT.md`. Sol checked their contents independently in [FACT_CHECK](FACT_CHECK.md). The first figure explains shared base → domain specialization → task evidence → experience → reviewed core evolution, with domain knowledge returning to plugins. The second expands the five subworkflows and shows shared wiki, embedded ARIS skills, stage-specific plugin calls, and local returns.

Gemini 4 Argon/high discussed composition in two effective SUCCESS responses in the same session. Requests and full responses are saved as `GEMINI_DESIGN_*` and `GEMINI_REFINEMENT_*`. Adopted: common palette, two domain tracks, a separate review/distillation step before v2, wiki above the workflow and plugins below it, and concise stage-aligned interface labels.

Root adjusted the proposals: no OS-style “read-only mount” claim; no historical theorem parameters in an architecture overview; Property B and ECC remain equal-size examples with a small ECC draft marker; v2 is the next iteration rather than an asserted release. The chart summarizes representative paths, rather than drawing every possible workflow transition.

## Actual image inspection and repairs

The built-in GPT Image tool generated both diagrams. Root inspected the rendered images. Sol independently opened both actual PNGs with view_image, and Gemini reported actual image viewing in its third effective response; its complete review is preserved in [GEMINI_VISUAL_RESPONSE](GEMINI_VISUAL_RESPONSE.md). Sol's separate observations and subsequent rechecks are in [VISUAL_REVIEW](VISUAL_REVIEW.md).

The following concrete changes were made with GPT Image editing, retaining the drafts:

1. **Figure 1 specialization:** the initial fork pointed to Property B and its workspace, leaving ECC without its own inlet. It now has a left-side base rail with distinct arrows into both plugins. Root and Sol confirmed this correction on the intermediate image.
2. **Figure 1 feedback destination:** narrowed the dashed grouping boundary to the two plugins, so the returning domain tools visibly enrich the plugins rather than an enclosing group of plugins and workspaces.
3. **Figure 2 spacing:** moved the call/return description into the plugin-panel header and extended the middle dashed connector to align with its peers. The backward proof/route arcs now have clear space.
4. **Figure 2 literature return:** added a Route loop feeder to the existing targeted-literature arrow, alongside Prove. This remains an incremental lookup, not a new problem specification.

The suggestion to add more v2 disclaimers was not adopted: the dashed box and “Next iteration” already express the conceptual next version. The Route loop skill pills remain legible, so no additional redraw for their padding was needed.

Root inspected both final generated images: the corrected arrows, all five stage titles and ARIS names, optional Lean, wiki band, plugin interface, ECC draft marker, and v2 label remain present and readable. Final independent recheck is recorded in VISUAL_REVIEW; Gemini's image review concerned the pre-final versions and is not described as a final-version pass.

## Deliverables

Final assets and all generation/edit prompts are in [figures/mathrsi](../../figures/mathrsi/README.md). Both PNGs are actually 1672 × 941, not the larger preferred resolution mentioned in the prompts. [IMAGE_OUTPUTS](IMAGE_OUTPUTS.json) records actual source paths and dimensions. Images are copied into the repository, not left dependent on the generator cache.

No theorem, Lean build, benchmark, remote publication, or suspended research Goal was executed. The figure reviews assess fidelity and readability, not proof correctness or measured research efficiency.
