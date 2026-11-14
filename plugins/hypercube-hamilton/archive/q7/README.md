# Q7 selected original sources and portable checks

This directory contains original Q7 proof sources, the frozen direct inputs for two E16 checks, and the complete T63 target04 certificate. It is a selected, runnable evidence package, **not the complete 22.577 GiB research archive**. Q7 remains open. The complete E14 result covers every original short matching with at least 57 edges; E16 is only partially closed.

The sources were copied without editing their bytes from the November 12 Q7 archive received on November 14. Their old Windows paths, historical status headings and references remain historical source text. `source/archive_inventory/key_check_inputs.json` retains the original SHA bindings; the original replay loader resolves those logical paths to the frozen files in this checkout. No model calls, network, producer search or author-machine directory is needed for the following two checks.

## Replay the two frozen finite consumers

From the repository root, Python 3.11 or newer, standard library only:

```sh
python3 -B plugins/hypercube-hamilton/archive/q7/source/archive_inventory/replay_key_checks.py
```

Add `--check S3` or `--check S2_STRONG` to run one. The original entry point and checker bytes are unchanged. It reads the two complete finite branches, checks the input bindings and compares every result field with the frozen independent output except current CPU seconds. It prints JSON and does not overwrite original results. To retain a run, redirect stdout to a new file in your workspace.

Both consumers were actually run from this checkout: S3 checks all 18,049 fixed plans, S2_STRONG all 19,718; both returned PASS. These are complete **conditional subfamilies**, not all E16 inputs. The latter includes 6,328 cases that use another actual cut to enter S3, so the counts cannot be added into an E16 completion percentage. Details and actual results are in [the implementation record](../../evidence/Q7_V5_IMPLEMENTATION.md).

The two direct-input sets contain 157 and 150 files, their union 178 paths and 42,337,645 bytes. The full historical inventory tables are omitted: every preferred path needed by these two consumers is present and its required SHA is checked. Extra proof sources and the original replay entry/manifest are also included. See [the copied-file list](SOURCE_FILES.txt).

## Recompute the real T63 target04 rank with the extended tool

The existing plugin tool now supports an explicit omitted subset U of holes H. The old `--root` single-omission command remains valid. From the repository root:

```sh
python3 -B plugins/hypercube-hamilton/tools/check_forest_rank.py \
  --dim 5 --omitted 0 5 20 --holes 0 3 5 10 15 20 \
  --forests plugins/hypercube-hamilton/archive/q7/source/research/seven_directions_continuation/R7_MU3_T63_TARGET04_RANK/target04_forests.bin \
  --columns plugins/hypercube-hamilton/archive/q7/source/research/seven_directions_continuation/R7_MU3_T63_TARGET04_RANK/target04_columns.bin \
  --output /tmp/mathrsi-t63-target04.json
```

This command actually checks all 4,096 forests and 4,096 arbitrary complete-graph matching columns, recomputes all 16,777,216 connectivity bits and does GF(2) elimination. The recorded execution took 80.14 seconds on the development machine, obtained rank 4,096 and `universal_rank_gate_met=true`. It does not trust the producer's saved matrix/rank. Other machines may take longer.

The degrees must be zero on U, one on K=V\H and two on H\U. The tool checks every non-omitted component, its two K endpoints, short/unique edges, acyclicity, exact column endpoint domain, and the CKN target `2^(|K|/2-1)`. H and U are supplied together; the tool does not separately canonicalize them. The frozen S3 consumer separately checks the actual joint marked transport into target04 for both uses, including full holes and omitted marks.

The CKN complete matching-connectivity rank upper bound is a literature import. Full selected rank plus a nonzero column for every arbitrary prescribed matching gives the universal forest interface; path expansion and matching preservation are mathematical obligations, explained in the [original T63 proof](source/research/seven_directions_continuation/R7_MU3_T63_NEW_RANK.md) and [joint review](source/research/seven_directions_continuation/R7_MU3_CONTROLLED_AND_T63_REVIEW.md). A legal input with rank below target returns `status=PASS` and **`universal_rank_gate_met=false`**; it does not prove the original theorem false or certify the universal interface.

Small interface/regression checks (including the unchanged positional root route and invalid certificate rejection) run with:

```sh
python3 -B plugins/hypercube-hamilton/tools/regress_forest_rank.py \
  --output /tmp/mathrsi-forest-regression.json
```

## What is and is not included

The main original sources are in `source/research/seven_directions_continuation/`: E14 assembly/review; E16 mu=2 and mu=4 closure/review; controlled donor/return and full-matching expansion; S3/S2_STRONG proofs, consumers, frozen finite data and results; current remainder. The selected E12 sources, good-root component argument, six-direction corollary and primary problem paper are also present. [Q7 methods](../../skills/mathrsi-hypercube-hamilton/references/q7-methods.md) explains how to consume them.

Target04's entire listed artifact set is present, including original matrix, compressed pairs, pivots, combinations, config and logs. The old [independent C++ consumer](source/research/six_directions/Q5_T63_RANK_REVIEW_check.cpp) is preserved as source; the portable Python command above needs no C++ compiler or Windows executable.

The other five new T63 target binary sets, most old Q5/Q6 rank families, large source forest/search streams, complete historical inventories/trajectories and all 23 GB of older data are **not** included. Reading a copied review or PASS receipt does not rerun these imports. The two frozen consumers import those accepted local theorems; this package does not claim complete transitive re-verification of E14, E16 or Q7. The existing older Q6 plugin archive remains separate and unchanged.

Original provenance/status qualifications remain `same-family`, `provisional`, `sound-modulo-imports`, without upgrading to Lean or independent peer review. The original [historical binding-gap note](source/archive_inventory/HISTORICAL_BINDING_GAPS.md) and [eight unresolved bindings](source/archive_inventory/unresolved_bindings.jsonl) are retained for context; their presence is not a claim to have packaged the rest of the full historical archive.

These large evidence inputs belong in repository/evidence distribution, not the browser site's asset tree. Nothing here publishes them to Pages or starts a mathematical research run.
