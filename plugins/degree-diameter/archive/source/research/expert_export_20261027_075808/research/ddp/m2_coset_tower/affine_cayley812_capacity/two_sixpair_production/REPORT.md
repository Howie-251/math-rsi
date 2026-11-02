# Two 812-point degree-12 six-pair modes: complete, no D3

The two authorized modes are complete: **1,465,082 marked normalized inputs**, of which **1,414,562 legal generating sets each received a complete single-root BFS**. No graph of diameter at most 3 was found. The unique saved minimum-deficit graph has diameter 4 and **15,022 unordered pairs beyond distance 3**.

This result covers only the phase modes `(3,4,4,6,7,11)` and `(5,7,9,10,12,12)` in `F29 semidirect_2 C28`. The other 8,611 symbolic-surviving modes were not searched. In particular, having selected the two highest minimum-symbolic-capacity six-pair modes does not exclude other modes with smaller symbolic capacity.

## Complete range and actual checks

The full normalization and legality proof is in [SCOPE.md](SCOPE.md). The first component has nontrivial action, allowing common field translation to set its coordinate to zero. The remaining five coordinates are projectivized once by their first nonzero entry. Thus each mode has `(29^5−1)/28=732,541` marked inputs. The reused basis machinery is explicitly the identity matrix with no additional linear constraints.

In each mode the single repeated phase gives one duplicate-pair hyperplane, containing `(29^4−1)/28=25,260` projective inputs. The complete program counts exactly match this independently derived count:

| Pair phases | Marked inputs | Illegal actual generators | Legal sets / complete BFS | Minimum root deficit |
|---|---:|---:|---:|---:|
| `[3,4,4,6,7,11]` | 732,541 | 25,260 | 707,281 | 41 |
| `[5,7,9,10,12,12]` | 732,541 | 25,260 | 707,281 | 37 |
| Total | 1,465,082 | 50,520 | 1,414,562 | 37 |

All actual twelve elements are checked for nonidentity and distinctness and supplied in exact inverse pairs. Each legal candidate receives an unrestricted BFS until its entire reachable component is processed. By Cayley left-translation symmetry this determines connectivity, diameter, and the all-vertex distance spectrum. Neither symbolic pass counts nor truncated BFS results are reported as fully checked graphs.

The run starts at production cursor zero, independent of the earlier capacity calculations. Final cursor is **1,465,082**, next position is null, status `COMPLETE_NO_SOLUTION`. Input phases and coordinates, the identity parameter basis, per-mode totals, and the complete root-deficit histogram are preserved in `production.inputs.json`, `production.terminal.json`, and `terminal.json`. `production.cpp` and `run.py` preserve the actual implementation; `production.log` preserves the unique run.

## Saved best

The saved minimum-deficit graph is from the second mode, source symbolic cursor 36744:

- Pair phases: `(5,7,9,10,12,12)`.
- Actual representative field coordinates: `(0,1,10,13,10,6)`.
- Element encoding: `x+29*j`; scalar action `2^j` modulo 29.
- Twelve generators: `145,667,204,621,271,552,303,527,358,475,354,488`.
- Graph: **812 vertices, 4,872 edges, degree 12**, computed connected and diameter 4.
- Complete root spectrum at distances 0 through 4: **1,12,129,633,37**.
- Radius-three root deficit: 37, yielding `812*37/2 = 15,022` bad unordered pairs.

`production.best.edges` is the only retained complete best edge table, and `production.best.json` contains its parameters, spectrum and selection scope. No additional candidate, preflight graph, or repeated final BFS was run here. Root completed the unique independent final check: all 4,872 independently reconstructed edges match. One generic BFS over all 812 roots confirmed simplicity, connectedness, degree 12, diameter 4 and 15,022 bad unordered pairs. The ordered spectrum is `812,9744,104748,513996,30044`, exactly 812 times the production root spectrum. Evidence is in `production.best.independent_check.json`.

## Resources

One worker completed the scope without restarting. The process used **19.060879 CPU seconds**, including **18.553777 CPU seconds** in complete BFS. Preparation and compilation used **1.029782 CPU seconds**; total recorded preparation, compilation and production was **20.095262 CPU seconds**, below the 120-second budget. Wall time was 20.115744 seconds.

No extra phase mode or other group was started. The parent-owned independent final check used **0.022022259 CPU seconds**; the total including that check is **20.117284259 CPU seconds**. Pending actions: none.
