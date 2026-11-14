# Q7 v5: actual portable evidence and marked-forest checks

Implemented on 2026-11-14 in the v5 worktree. Source research files were only read/copied; no producer, mathematical Goal, commit, push or publication was started. Main usage is [the selected Q7 archive README](../archive/q7/README.md).

## Changed behavior

The existing `tools/check_forest_rank.py` now accepts `--omitted U...` as an alternative to the unchanged `--root` CLI route. The positional Python call `check(dim, root, holes, forests, columns)` remains available; the new route is `check(dim, None, holes, forests, columns, omitted=U)`.

It derives the record width from the marked pair `(H,U)`, requires nonempty U⊆H, and checks degree 0 on U, 1 on K=V\H and 2 on H\U. It checks all non-omitted components, not just components encountered by visiting K. Each component is an acyclic short-edge path with exactly two K endpoints. Complete-graph columns may contain long/equal-parity edges but must cover exactly K once. The connectivity matrix is reconstructed and independently eliminated; the target remains `2^(|K|/2-1)` from the imported CKN theorem.

The tool does not canonicalize H/U independently. Actual marked transport is retained in the original frozen plan consumers: S3's two target04 uses jointly map the whole six-hole set and its specified three omissions into the exact accepted T63 geometry. The mathematical reference explains transport of the prescribed matching and final cycle as well.

`status=PASS` means the selected input is legal and computation completed. Only `universal_rank_gate_met=true` meets the finite rank premise. The CKN import, nonzero-column argument and forest expansion remain mathematical obligations; this change does not claim a new Q7 theorem.

## Actual executions

All commands below were run from this repository root, with Python `-B` and assertions enabled. Each exited 0. Outputs are in [the v5 evidence directory](../../../development/evolution/v5-q7-20261114/evidence/).

| Run | Actual scope/result | Time |
|---|---|---:|
| Real T63 target04 prefix | 128 forests × 128 columns; all 16,384 bits; rank 16, universal gate false | 0.0764 wall seconds |
| Real T63 target04 complete | 4,096 forests × 4,096 columns; all 16,777,216 bits; 1,311,033 ones; GF(2) rank 4,096; gate true | 80.1396 wall seconds |
| Legacy A10 complete | 1,024 forests × 1,024 columns; all 1,048,576 bits; 158,674 ones; rank 1,024; gate true | 4.6008 wall seconds |
| Old Q3 root interface | original four forests/three columns; rank 2/gate true | recorded in regression JSON |
| New small multi-omission | two short square matchings/all three complete columns; rank 2/gate true | recorded in regression JSON |
| Legal three-omission deficient pool | one legal row; rank 1 < 2, gate false | recorded in regression JSON |
| Invalid certificates | ten malformed/illegal input cases rejected | recorded in regression JSON |
| Relocated frozen S3 | all 18,049 plans; all frozen fields equal except CPU seconds | 1.704028 CPU seconds |
| Relocated frozen S2_STRONG | all 19,718 plans; all frozen fields equal except CPU seconds | 2.682800 CPU seconds |

The 128-prefix measurement justified one complete target04 run; it was not reported as a full-rank result. The other five T63 targets were not rerun. The complete T63 tool run recomputes matrix entries and rank without reading the saved producer matrix, pivots or rank claims. The original matrix and independent rank receipt remain available as frozen evidence. It is a distinct implementation from the original C++ consumer, not a new cross-family mathematical review.

Results: [T63 full](../../../development/evolution/v5-q7-20261114/evidence/t63-target04-full.json), [A10 full](../../../development/evolution/v5-q7-20261114/evidence/a10-legacy-full.json), [contract regressions](../../../development/evolution/v5-q7-20261114/evidence/forest-contract-regression.json), [two relocated frozen consumers](../../../development/evolution/v5-q7-20261114/evidence/q7-relocated-replay.json).

Invalid cases cover U outside H, simultaneous root/U, a forest touching U, duplicate edge, long forest edge, incomplete degree/component coverage, a separate all-hole cycle with correct degree2, repeated column endpoint, wrong column endpoint domain and truncated record. The existing Python `-O` rejection remains. The original A10 archived expected result was not overwritten.

## Source relocation scope

The union of the original key-consumer direct inputs is 178 paths/42,337,645 bytes. They were resolved using the source archive's original SHA bindings, copied to their original preferred relative locations, and then actually rechecked by both unmodified original consumers from this checkout. The original `replay_key_checks.py` and `key_check_inputs.json` bytes are preserved. Full 26MB historical lookup tables are unnecessary when all preferred bound paths exist; this has now been tested in the selected package, rather than inferred from source alone.

Including the named E12/E14/E16 proofs, Q6 corollary, good-root components, primary problem paper, source C++ rank checker and archive-gap notes, selected source content totals **204 files/43,360,734 bytes** at implementation time. [SOURCE_FILES.txt](../archive/q7/SOURCE_FILES.txt) enumerates them. The selected package is self-contained for the two frozen consumers and target04 full rank command, not for every referenced historical theorem or all six T63 rank families. Explicit omissions are in its README. The older Q6 archive was kept intact.

Frozen historical headings and paths remain source evidence, not instructions or current status. Q7, complete E16 and P7 remain open. Original theorem acceptance remains same-family/provisional/sound-modulo-imports where declared. The new finite deterministic executions report their actual coverage without upgrading entire imported proof chains.

## Reproduction commands

The [archive README](../archive/q7/README.md) has copyable commands for the relocated consumers, complete target04 computation and small contract regressions. The unchanged legacy A10 command was:

```sh
python3 -B plugins/hypercube-hamilton/tools/check_forest_rank.py \
  --dim 5 --root 0 --holes 0 1 2 4 8 15 23 27 29 30 \
  --forests plugins/hypercube-hamilton/archive/source/research/six_directions/A10_ORBIT3_UNIVERSAL_rank_selected_forests.bin \
  --columns plugins/hypercube-hamilton/archive/source/research/six_directions/A10_ORBIT3_UNIVERSAL_rank_columns.bin \
  --output /tmp/mathrsi-a10-legacy.json
```

## Final bounded bundle acceptance

Completed on 2026-11-14 after the mathematical runs above, without rerunning any matrix or frozen consumer. `SOURCE_FILES.txt` lists 204 distinct paths; the actual `source/` tree has exactly those 204 regular files, with no missing or unlisted files, totaling 43,360,734 bytes. Direct byte comparison (`filecmp.cmp(..., shallow=False)`) with the received original archive found **zero changed files and zero missing originals**. No new hash framework was introduced.

All 178 preferred paths in the existing frozen direct-input manifest remain present, totaling 42,337,645 bytes. The prior successful relocated execution already exercised their imports and original SHA checks. Target04 forest/columns and its full artifact set are present. No dependency needed for the documented two-consumer replay, target04 rank command or small regression command was found missing. This does not claim complete transitive dependencies for every copied proof: the other five T63 binary sets and older large families remain intentionally omitted as stated in the archive README.

The largest individual new source file is `R7_E16_MU3_CENTRAL_S2_STRONG_FIXED_PLANS.json`, 7,867,113 bytes (about 7.50 MiB); the next is S3 fixed plans, 7,145,775 bytes. Thus none of these selected files crosses GitHub's documented 50 MiB warning or 100 MiB normal-Git block threshold. GitHub's general repository-health/storage recommendations still apply; no push-size or clone-time benchmark is claimed. [Official GitHub file-size documentation](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github), checked 2026-11-14.

Privacy review was restricted to these selected new files. The 204-path inventory contains no credential/settings/environment filename. The 197 text/code/JSON/log files were scanned for obvious private-key blocks, Tencent/AWS credential identifiers, GitHub/API token formats and long credential assignments; there were no candidates. The seven non-text files are the six target04 binary artifacts and the primary problem PDF. Their names and provenance belong to this mathematical evidence set; no unrelated personal project export, account configuration, conversation transcript or credential file was selected. This is a bounded obvious-credential/provenance check, not a claim that arbitrary confidential prose can be automatically ruled out.

`site/public-files.json` was read and contains **no** `archive/q7` source or target04/S3/S2 data entry. `tools/build_public_site.py` copies only that explicit source→destination mapping; the Pages workflow uploads only its `_site` output. Therefore this acceptance confirms the selected 43 MB evidence set is not included in the current public-site export. No public manifest, site file or deployment was changed by this worker. A future maintainer who adds explicit public entries must make that separate publication decision.

The package and implementation evidence are handed back at this point; no further source additions or writes are pending from this worker.
