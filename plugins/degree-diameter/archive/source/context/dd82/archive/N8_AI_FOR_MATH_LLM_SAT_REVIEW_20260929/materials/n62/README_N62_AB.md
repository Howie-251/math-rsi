# n=62 theory-reduced A+B SAT front end

This front end implements Section 7 of `N62_SAT_HANDOFF_FOR_CODEX.md`.
It starts from the seven exhaustive rooted templates in
`n62_root_templates_theory.json`; it does not encode an unrooted raw graph.

For each template, the 1,378 possible edges inside `Y={9,...,61}` are the
primary graph variables. Auxiliary variables encode the entries of
`B=A^2+A-7I-J`, exact row sum 3, the one-triangle-per-vertex constraint,
the simple/double-B branch conditions, and the template-local restrictions.

## Files

- `n62_ab_cnf.py`: generate the seven CNFs and their variable maps.
- `n62_ab_make_cubes.py`: make the deterministic 7 x 8 depth-three split.
- `n62_ab_verify.py`: reconstruct and independently check any SAT graph.
- `run55/run_n62_ab_cube_queue.py`: solve the 56 leaves in parallel.
- `run55/start_n62_ab_12h_55cpu.sh`: ready-to-run 55-core pilot.
- `run55/show_n62_ab_progress.py`: compact progress report.

## Run on a 55-core instance

From `degree_diameter_sat`:

```bash
nohup bash run55/start_n62_ab_12h_55cpu.sh > n62_ab_12h.log 2>&1 &
```

The default pilot uses 55 workers, an 11-hour per-leaf timeout, and a
12-hour overall wall limit. Override these with `N62_WORKERS`,
`N62_TASK_TIMEOUT`, and `N62_WALL_TIMEOUT`.

Check progress with:

```bash
python3 run55/show_n62_ab_progress.py
```

The first run generates about 210 MB of base CNFs. Each active worker makes
a temporary augmented CNF and removes it when its solver exits.

## Interpretation

A `SAT_VERIFIED` result is a genuine 62-vertex graph after exact independent
checking. `UNSAT` is a solver-level result for one leaf. Closing all 56 leaves
as raw UNSAT excludes all seven theoretical templates, but a publication-grade
computational proof still requires proof-producing reruns and proof checking.

The five double-B instances refine old rooted branches that were already
reported raw UNSAT. The two simple-B instances give a stronger coordinate
system for the old unresolved simple-B region; old semantic cubes cannot be
reused without an explicit rerooting map.
