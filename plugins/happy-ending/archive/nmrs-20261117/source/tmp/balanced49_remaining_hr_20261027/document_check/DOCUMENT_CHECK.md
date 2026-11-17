# Document-to-receipt consistency check

Date: 2026-10-27. Scope: documentation and retained receipts only. No proof or
mathematical review, scientific validation, solver/checker invocation, network
acquisition, replay or rerun occurred. This is not an independent review and
does not grant acceptance. The checker also implemented the earlier Joint17
binding and is not independent of that implementation.

Primary document inspected:
`.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_COMMON_ASSIGNMENT_AND_REMAINING_H49_BRANCH_20261027.md`.

The raw result/outcome JSON, corresponding SUMMARY/RESULTS/STAGES/STATUS files
and transport receipts under `tmp/balanced49_remaining_hr_20261027/` were compared
for paths, counts, stages, statuses, quoted hashes and explicit non-execution.
Only this new document_check directory is written by this task; all other
artifacts remain read-only.

## Findings

No substantive inconsistency was found in the completed result statements
already written into the inspected main document. Its nine existing Markdown
file links resolved locally. The main session was concurrently updating the
Closure appendix; its temporary placeholder is intentionally not a finding.
This check does not assess the mathematical correctness of claims such as
common assignment, abstract soundness, or branch implications.

| Stage | Raw evidence | Main-document consistency |
|---|---|---|
| Source acquisition | Partial Prefix verified; Closure not verified; outer exit124; last saved STARTED at `ES7ClosureLiteral.lean:range_request`; no retry | Correctly kept separate from success and final filesystem inventory |
| Prefix | PASS;129 patterns (4/7/118);64/65536 completions;7/118 Good;3198 prefix rules;151801 dictionary names;five controls;wall1.567702838s | Counts, rounded time, Valid/symbolic scope and absent actual Closure CNF match agree |
| Joint17 replay transport | STOPPED_UPLOAD_TIMEOUT_NO_REPLAY;one upload;30932992/38734663 callback bytes;zero verification dispatches/checker calls | Correctly states source upload failure and no completed proof replay |
| Joint17 formula binding | PASS;59479 CNF rows;92886 names;40 catalog states (20 low/20 high among70 ideals);seven controls;wall1.871411712s | Counts, time, authenticated-prefix identity and absent full remote-source/proof verification agree |
| Closure fixed-rule reconstruction | Overall FAIL at mutation_controls;KeyError `core_source_nonempty`;all190932 fixed rules and151801 names completed;three controls rejected, nine unrun | Correct final status to retain in the appendix; completed fixed-row evidence does not turn the whole run into PASS |

Closure group row counts in the SUMMARY agree with the raw result:
base77368, ambient21238, core30987, low1922, counting1561, packet54009,
terminal649, prefix3198. Raw result records `all_rules_Valid=true` and
`all_surviving_atoms_mapped=true`, while `actual_cnf_equality_checked=false`
and `UNSAT_checked=false`. Its missing sourceAttain/sourceForward, low impossible
and counting internalBound fixed-row cases are stated in the SUMMARY; this
check makes no coverage claim about constructors absent from the fixed data.

The replay-stage callback amount alone was not treated as a live remote size.
The separate Joint17 binding receipt subsequently authenticated the existing
read-only remote prefix. Thus the replay outcome's stage-scoped absence of
post-close inventory and the later binding identity are not contradictory.

## Hash comparison

Byte hashes were calculated only to compare document/receipt identities, not
to repeat any scientific check.

- Prefix parser: `19bb1cd473db6b2fd15bf4f06d74658d1d93e4d433f1230a3a395acf11317081`.
- Prefix raw result: `20aaf32b5bdfcdf50a1aefeda310c014e7e336de44c0c5e2fa053cf825b725ba`.
- Prefix ledger: `bba0f718d956a95167d31b7979b5aca5427af04a84bcc530598a725c9ab0a5f5`.
- Joint17 binding parser: `fc2363d334641c644af264ab9d5617d6aaed57dc9237a4c62a5d60a869ef2194`.
- Joint17 binding raw result: `56b3a600e7d5f01bb29f30a1411b19315012c856d10fff774629abdf10ac757f`.
- Closure parser: `7e641a902c61f81c9dfde7e366517b38611b0b12a2768ac6c50cfd2bfea36fc5`.
- Closure raw result: `429dcf100849b06a459570137354d8a69a0b7367a9ef02aad2977142c9a6ecbf`.
- Closure mapped ledger: `0ad49d462a9c48a45c8ec4fedd95e678e4d69d7335983cedb27251daa776e238`.

These match the corresponding recorded parser/result/ledger identities.
The main document's three Joint17 source-chain hashes also exactly match its
raw binding metadata/result: full local Literal `22950a14595f72b93a769261738d029b2aa27d04aa27e1f44fa2dce77775da2a`,
authenticated prefix `7760d1d01c73536ea64ed3c2f587caff67e37ff3531dfbd5b012bfb32fc823a2`,
decoded CNF payload `9a70c9ce1aa47c1a7127a3393a8159c7276c371fb523161b38e838feb6e0b467`.
The source literal start126 and closing-quote offset1490293 also agree.

## Explicit limits

The main document keeps new proof replay, actual Closure CNF equality,
Closure UNSAT, Lean compilation, independent review and acceptance unperformed.
That agrees with the inspected receipts. Historical Through14/Terminal20 PASS
statements remain explicitly historical and do not claim new schema binding.
The main document's mathematical derivations, symbolic seven-point construction,
C49/D29 claims and H49/R30 branch logic were not reviewed in this document task.
