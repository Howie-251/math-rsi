# MathRSI v1 group repository preparation

2026-11-02. The user authorized publishing the complete v1 harness, README, two approved diagrams, and usage instructions to the private group repository `lisresearchgroup/math-rsi`. The remote contained only its initial README commit; that commit was merged into the existing local development history without rewriting either history.

## Delivered entry points

- English `README.md` and `README.zh-CN.md`, with both approved architecture/workflow diagrams.
- `docs/QUICKSTART.md`: clone, separate task workspace, Codex/Claude entry, host-specific ARIS paths, reviewer setup and recovery.
- `examples/proof-repair/`: separate faulty starter and completed reference, exact Python replay, and an agent invocation grounded in the actual prior trial.
- The existing full base/ARIS bundle, Property B knowledge and checkers, four MCP bridge implementations, licenses, and historical development evidence remain included. ECC remains a draft.

The new example preserves the original four-uniform, at-most-seven-edge theorem. Its finite replay checks a false independence assertion and the repaired bound's arithmetic; the full universal proof is written in the reference. Publishing this example does not rerun its historical model reviews or resolve its pending TeX build.

## Gemini collaboration and disposition

Gemini read the existing implementation and proposed the README structure and substantive English draft. Root adopted its three-layer explanation, five-stage table, concrete entry points and figure placement, and shortened the validation section. Root also corrected the draft's overly narrow return-to-route condition: repeated work with no useful information can trigger reconsideration even without an explicit counterexample.

The final review read both READMEs, quickstart, example and its contract/verification references; it reported no substantive publication blocker. Both actual responses selected `gemini-4-argon-high`, effort `high`, status `SUCCESS`, in session `883091cc-2a08-433e-a3a5-a3163258fa05`. This was static documentation review, not a new model-service or mathematical validation run.

- [First request](GEMINI_REQUEST.md), [complete reply](GEMINI_RESPONSE.md), [raw envelope](GEMINI_RAW.json).
- [Final request](GEMINI_FINAL_REQUEST.md), [complete reply](GEMINI_FINAL_RESPONSE.md), [raw envelope](GEMINI_FINAL_RAW.json).

## Independent checkout validation

The tested source is commit `4b08fc114d12fb2ae9939530d2bc3b36d195250f`. A separate temporary clone on the same Mac passed:

- 67 maintained documents and 1,048 local link targets; all 89 relative aliases resolve inside the clone.
- All 207 bundled upstream source files and nine relocated wiki/router/renderer helper commands.
- All 61 offline MCP protocol tests.
- Exact example replay from the clone and an unrelated working directory, the documented starter-copy recipe, and identical starter/reference theorem text.

[Raw commands and results](portable/RESULT.json) and [scope report](portable/REPORT.md) retain the evidence. Subsequent publication bookkeeping adds only review/evidence/navigation records. No original Property B or ECC research Goal was resumed; no new Lean or TeX build was run.

[Inventory audit](INVENTORY_AUDIT.md) found no oversized Git objects, missing declared archived resources, broken aliases, or identified committed credentials. Academic originals retain their own copyrights as described in the repository provenance.
