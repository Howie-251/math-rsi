# MathRSI v2 figure refresh — 2026-11-03

The two README figures were redrawn with the built-in GPT Image tool after a concrete layout discussion with Gemini 4 Argon (High). The final images are 1586 × 992 pixels. Original generated files remain in the tool output directory; the repository contains the final PNG copies.

## Adopted design

Figure 1 now shows v0 → v1 → v2. The pre-harness ARIS research in Property B and ECC informs the unified v1. The independent historical degree–diameter archive and existing v1 implementation enter mathrsi-meta-evolve, which produces base and plugin updates for v2. ECC remains marked draft. The v2 card represents the implemented version.

Figure 2 retains the five solving subworkflows, embedded ARIS skills, shared research wiki, plugin interfaces, literature return, route revision, proof repair, and optional Lean. A separate outer mathrsi-meta-evolve band classifies evidence. Base / Plugin changes enter modification and review/use before the next version; Task-specific / Defer remains in the wiki or backlog.

Root simplified Gemini's proposed bridge into a spacious bottom evidence-to-upgrade path in Figure 1. Figure 2 keeps “Lean when useful”; the draft phrase “Direct Lean or full audit” was not used because those are not mutually exclusive. Extra defensive text and duplicate boxes were omitted.

## Actual review

Root inspected both generated images directly: English spelling, diagram arrows, current version labels, DD provenance, ECC draft labels, separation of solving and maintenance, and readable text. Both were usable without a further image edit.

Gemini continued the original design session and reported directly reading both saved PNGs with view_file. Its final response found no factual, spelling, arrow, or readability issue and recommended adoption. This review concerns the figures, not a new validation of the mathematical results or a performance experiment.

- Requested and returned model: gemini-4-argon-high
- Returned effort: high; source cli_selected_model_variant
- Design and final responses: SUCCESS
- Session: a7294485-a2dd-48e8-8d99-146f66002c6c

## Sources

- [Figure 1 generation prompt](../../figures/mathrsi/01-evolution-v2.prompt.txt)
- [Figure 2 generation prompt](../../figures/mathrsi/02-workflows-v2.prompt.txt)
- [Design request](GEMINI_DESIGN_REQUEST.md), [raw response](GEMINI_DESIGN_RAW.json), [readable response](GEMINI_DESIGN_RESPONSE.md)
- [Final check request](GEMINI_FINAL_REQUEST.md), [raw response](GEMINI_FINAL_RAW.json), [readable response](GEMINI_FINAL_RESPONSE.md)
- [Generated output paths and dimensions](IMAGE_OUTPUTS.json)
- [Implemented v2 changes](../../docs/V2_CHANGES.md)

Only current documentation and figures are refreshed. The fixed v1 and v2 Git tags retain their original snapshots.

