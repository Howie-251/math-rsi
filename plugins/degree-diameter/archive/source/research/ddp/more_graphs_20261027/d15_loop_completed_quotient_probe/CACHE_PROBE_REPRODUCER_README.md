`CACHE_PROBE_REPRODUCER.py` is an unexecuted, post-authored reconstruction of the two root exec heredoc computations. It is not a source-code snapshot of those original runs. Saving this file did not run a new probe or recheck any recorded number.

It derives coherent zero ports and zero selfline triangles from the certified affine relation tables, checks the derived selections against the two frozen PREDICTION files, and reads only the existing R3/R4 free-point ball caches. It reproduces the full fixed-set unions and the lexicographic five-triangle subset enumeration, with an exact first-hit or next-unattempted cursor. It does not compute a ball, traverse a graph, solve a model, or generate a graph.

If a separate reproduction is requested later, use an explicit new output directory:

```sh
python research/ddp/more_graphs_20261027/d15_loop_completed_quotient_probe/CACHE_PROBE_REPRODUCER.py --output-dir /tmp/d15-cache-reproduction
```

The output directory must not already exist and must be outside both frozen experiment directories. The script never writes their PREDICTION or RESULT files. Optional `--mode zero` / `--mode triangles` selects one original computation. The default aggregate subset CPU deadline is8 seconds; if reached, the source, tested count and exact next controller subset are recorded. This deadline is a reproduction setting, not a revision of an original runtime.

The actual original results remain in [canonical_zero_port_probe/RESULT.json](canonical_zero_port_probe/RESULT.json) and [selfline_helper9_probe/RESULT.json](selfline_helper9_probe/RESULT.json): zero-port unions missed528/300 targets, while all triangle unions were full but all42504/142506 five-subsets failed. Those numbers are cited from the original records; this reproducer was not executed to validate them.

The subsequent independent-triangle continuation is already terminal: D4 solver UNSAT and D5 UNKNOWN, with no graph. This source-preservation addition starts no new continuation, offset, source or model.
