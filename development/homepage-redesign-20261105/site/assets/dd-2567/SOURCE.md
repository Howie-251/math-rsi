# PR11: offline source materials for the 2,567-vertex graph

Original PR: https://github.com/lisresearchgroup/math-rsi/pull/11

Frozen commit: `7bd5a0cf34db9454cb0badf79c8622fb5fb7b833`.

Files below retain their original repository paths and contents. Start with [the ten-graph construction README](case-studies/degree-diameter/reproduce/d10_d4/README.md), [execution version](case-studies/degree-diameter/evidence/execution_version.md), or [the exact five-cut diagram](case-studies/degree-diameter/assets/construction_d10_d4.svg). The original [English case text](case-studies/degree-diameter/CASE_STUDY_EN.txt) and [Chinese case text](case-studies/degree-diameter/CASE_STUDY.txt) provide context.

This is a small source excerpt, not the entire case-study website or research workspace. Original navigation to materials outside this excerpt is retained and may require the repository. The complete Lean project and dependencies are not included. Original verification receipts record historical all-root BFS and completed kernel/import results; final external formal C review remains incomplete.

The research used MathRSI v2 plus the degree–diameter plugin and PR7 handoff repair. Publication used later main/v3. Inclusion as v4Preview feedback does not change execution attribution or imply v4 release.

## Deterministic replay

From `case-studies/degree-diameter/reproduce/` run:

```sh
python3 d10_d4/reproduce.py --all --output-dir /path/to/rebuilt_d10_d4
```

This standard-library script applies saved finite edits to the compressed 2,557-vertex source. It does not run search, BFS, or Lean. The present packaging check stores generated outputs and its result outside this asset directory, under `reviews/dd-v4-20261107/intake/replay-check/`. That check confirms deterministic reconstruction and expected sizes; the historical publication receipt separately records complete edge-set comparisons against accepted originals.

[MANIFEST.json](MANIFEST.json) lists the original source paths. [LICENSE](LICENSE) is preserved from the same commit.
