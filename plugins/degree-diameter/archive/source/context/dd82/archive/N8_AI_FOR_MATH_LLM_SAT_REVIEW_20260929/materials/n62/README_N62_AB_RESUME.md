# n=62 A+B canonical resume

This queue continues the interrupted n=62 A+B computation without restarting
the old 56-leaf pilot. The old run finished 45/56 leaves. Its three remaining
double-B leaves are already covered by the earlier raw-UNSAT results for rooted
classes 02--04, so the default queue spends all CPU time on the genuinely open
`S_DISJOINT` region.

The default manifest contains 80 symmetry-canonical, pairwise disjoint tasks.
They cover the eight unfinished `S_DISJOINT` pilot leaves. This is enough to
feed 55 workers while assigning exactly one solver to each cube. A timed-out
cube is split into disjoint children; it is not restarted as several portfolio
copies of the same formula.

For a self-contained rerun of all 11 interrupted leaves, including the
mathematically redundant double-B tail, set `N62_RESUME_TEMPLATES=all`. That
scope has 126 canonical tasks and uses a separate state directory.

## Start or resume on the 55-core machine

From `degree_diameter_sat` run:

```bash
bash run55/start_n62_ab_resume_7d_55cpu.sh
```

The launcher uses `nohup`, writes a PID and timestamped launcher log, and then
returns. Its defaults are:

- solver: `solvers/satcomp2025/AE_kissat2025_MAB/kissat`;
- workers: 55;
- active queue budget: 7 days;
- canonical-root probe: 1 hour;
- descendant slices: 2, 4, 8, 16, 32, then at most 48 hours;
- adaptive split depth: at most 8 levels;
- scratch directory: `/tmp/n62_ab_resume_canonical_v1_s_disjoint`.

The increasing slice schedule is deliberate. Easy roots close immediately;
when only a few hard roots remain, each is stopped before its children are
queued, then split into two complementary cubes. This grows enough distinct
work to keep the 55 workers occupied while allowing deeper cubes long runs.

Persistent state is fixed at:

```text
results/n62_ab_resume/canonical_v1/s_disjoint
```

Running the same command after a machine shutdown reads that directory,
retains closed cubes, and queues only unresolved work. Kissat itself does not
serialize an in-memory CDCL state: a solver process that was killed restarts
its current cube, while all completed cubes and the exact partition survive.
Machine downtime is not solver work and is not counted as active queue time.

Check progress with:

```bash
python3 run55/show_n62_ab_resume_progress.py
```

The report distinguishes canonical roots already closed by raw UNSAT from
queued/running descendants and displays active time, live solvers, and counts
by template and depth. The launcher refuses to start a second queue while the
PID recorded for this scope is still alive.

Useful overrides include:

```bash
N62_WORKERS=55 N62_WALL_TIMEOUT=604800 \
  bash run55/start_n62_ab_resume_7d_55cpu.sh

N62_RESUME_TEMPLATES=all \
  bash run55/start_n62_ab_resume_7d_55cpu.sh
```

Do not restart `start_n62_ab_12h_55cpu.sh`: it rebuilds the earlier 56-leaf
pilot and repeats the 45 leaves already closed. The new queue is a
solver-level search. `UNSAT` becomes a certified result only after a later
proof-producing rerun and proof checking.
