# Two n=62 programs

These programs attack the four rooted templates that remained open after the
previous `n=62` run:

- `08_triangle_pairs`
- `09_star_pairs`
- `10_path4_pairs`
- `11_path3_plus_pair`

They use the same exact rooted model: vertices `0,...,8` are fixed as the
root and its eight neighbours, and only the graph induced by the 53 second-layer
vertices is unknown.

## 1. Exact SMS/SAT queue

`n62_sms_solver.py` builds a smaller exact CNF for one template or one old
cube. Degree, root-to-second-layer coverage, and local defect bounds are in
CNF. The bundled `smsg-n62` binary enforces the remaining distance-two
condition directly and performs dynamic graph-isomorphism rejection.

The 55-core launcher distributes all 66 maximum-depth leaves left by the old
run:

```bash
cd /inspire/hdd/global_user/mahaitong-240108120090/mathagent
nohup bash degree_diameter_sat/run55/start_n62_sms_55cpu.sh \
  > n62_sms_launcher.log 2>&1 &
echo $!
```

The default per-leaf budget is six hours. It can be changed, for example:

```bash
N62_TASK_TIMEOUT=43200 N62_WORKERS=55 \
  bash degree_diameter_sat/run55/start_n62_sms_55cpu.sh
```

If the old sidecar is stored elsewhere, set `N62_SIDECAR_RUN` to its directory.
The launcher writes a timestamped directory under
`degree_diameter_sat/results/n62_sms_specialized/`.

Progress is recorded in `progress.json`; final aggregate results are in
`summary.json`. Every leaf has its own `tasks/<task-id>/queue.log`, `sms.log`,
and `result.json`. Re-running with the same `N62_OUTPUT_DIR` reuses completed
SAT/UNSAT leaves.

For a one-leaf test:

```bash
python3 degree_diameter_sat/n62_sms_solver.py \
  --template 09_star_pairs \
  --cube-json degree_diameter_sat/results/n62_all_templates/cube_sidecar/20260815T170431Z/roots/09_star_pairs/root_0016.json \
  --output-dir /tmp/n62_one_leaf \
  --timeout-seconds 60
```

## 2. Degree-preserving construction search

`n62_switch_search.py` is an AlphaMoore-style complementary search. Each state
has the exact required degree sequence, and every move is a degree-preserving
2-switch. Its hard energy is the number of uncovered distance-two pairs plus
the exact local-budget violations. Energy zero triggers the independent full
62-vertex verifier before a graph is reported.

Run 55 independent trajectories on the second machine:

```bash
cd /inspire/hdd/global_user/mahaitong-240108120090/mathagent
nohup bash degree_diameter_sat/run55/start_n62_switch_55cpu.sh \
  > n62_switch_launcher.log 2>&1 &
echo $!
```

The default search time is six hours per worker. For a 24-hour run:

```bash
N62_SEARCH_SECONDS=86400 N62_WORKERS=55 \
  bash degree_diameter_sat/run55/start_n62_switch_55cpu.sh
```

Worker checkpoints are written under
`degree_diameter_sat/results/n62_switch_search/<run-id>/workers/`. A verified
construction creates `FOUND` and `candidate_worker_*.edges`. A nonzero best
energy is search progress, not evidence of nonexistence.

## Interpretation

- A verified zero-energy construction proves that an order-62 graph exists.
- Closing all 66 exact leaves as UNSAT proves the four remaining rooted
  templates impossible; together with the eight previously closed templates,
  this closes order 62 under the proved rooted classification.
- `UNKNOWN` means only that the assigned time expired. Such leaves can be
  resumed with a larger budget or split again.
