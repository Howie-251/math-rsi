# 930-point degree-11 five-pair branch: complete, no diameter-3 graph

The authorized branch is complete. All **8,260,050 marked normalized assignments** in the 38 surviving five-inverse-pair plus one-reflection phase modes were inspected. Of these, 254,536 fail actual-generator legality; all remaining **8,005,514 legal generating sets received a complete single-root BFS**. None has diameter at most 3. The saved best graph has diameter 4 and 55,800 unordered pairs at distance greater than 3.

This closes the five-pair plus one-reflection branch of the specified Cayley group, in combination with the preceding complete phase and symbolic necessary filters. It does **not** close all degree-11 generating sets: 37 four-pair plus three-reflection symbolic modes remain unsearched. Degree 12 was not searched in this production batch.

## Exact range and normalization

The group is `F31 semidirect_3 C30`, with `(x,j)(y,k)=(x+3^j*y,j+k)` and element label `x+31*j`. The scalar 3 has order 30. Five non-involution inverse pairs and one phase-15 reflection give degree 11 after requiring eleven distinct, nonidentity actual group elements.

The complete phase/symbolic analysis is in [REPORT.md](REPORT.md); the necessary equations from fibers having exactly 31 distinct forms are in [D11_TIGHT_LINEAR.md](D11_TIGHT_LINEAR.md). Of the original 40 symbolic five-pair modes, two fail after restricting to the tight-fiber linear kernel. The remaining 38 have the following exact assignment counts:

| Tight-equation rank | Modes | Kernel dimension | Projective assignments per mode | Total |
|---|---:|---:|---:|---:|
| 2 | 10 | 3 | 993 | 9,930 |
| 1 | 20 | 4 | 30,784 | 615,680 |
| 0 | 8 | 5 | 954,305 | 7,634,440 |
| Total | 38 | — | — | 8,260,050 |

For each mode, a component with nontrivial scalar action is first translated to field coordinate zero. If `B` is the saved kernel basis, the remaining original field coordinates are recovered as `X=Bz`. Only **z** is projectively normalized by setting its first nonzero entry to one. The recovered original field coordinates are not normalized a second time. In particular, the checked example `z=(1,0,0)` mapping to original fields `(0,15,25,1,0,0)` is retained. The zero kernel vector lies in a conjugate complement and cannot generate this 930-element group.

Repeated phases remain separate marked components. Actual nonidentity and distinctness tests reject a phase-zero identity or equal/inverse-equal components without discarding legal repeated-phase assignments. Counts are marked inputs, not counts of graph-isomorphism classes.

## Actual computation

The run starts at a new production cursor zero; preceding capacity calculations are not treated as a graph-search prefix. Modes run by descending equation rank and then source cursor; within each mode the projective enumeration uses the first nonzero kernel coordinate followed by the full base-31 tail.

`d11_production.cpp` precomputes exact right multiplication and performs an unrestricted BFS from the group identity for every legal input. Left multiplication is transitive, so this determines the full Cayley graph's connectivity, diameter, and distance distribution. No depth-three early acceptance or approximate score is used.

Final cursor is **8,260,050**, with no next position. The exact per-mode counts and full root-deficit histogram are preserved in `d11_production.terminal.json` and `d11_production.summary.json`. `d11_production.inputs.json` preserves the source modes, anchors and actual kernel bases; `.txt` is the executable input. The run log and metadata preserve the single execution and budget.

## Saved best actual graph

The selection is the minimum root deficit among all legal assignments in this completed branch, not among the unsearched degree-11 modes.

- Source symbolic cursor: 9237; phase representatives: `(1,9,12,12,13)`; reflection phase 15.
- Original field representatives, including the anchored first coordinate: `(0,1,20,4,26,9)`.
- Actual encoded generating set: `31,899,280,667,392,571,376,573,429,544,474`.
- Graph: 930 vertices, 5,115 edges, degree 11; computed connected, diameter 4.
- Root distance histogram at distances 0 through 4: `1,11,110,688,120`.
- Root deficit at radius 3: 120; unordered bad pairs: `930*120/2 = 55,800`.

Only the final selected complete edge table is retained at `d11_production.best.edges`, with parameters and the full single-root spectrum in `d11_production.best.json`. Root completed the unique independent final check: independent reconstruction matched all 5,115 edges, and one generic BFS over all 930 roots confirmed a simple connected 11-regular graph of diameter 4 with 55,800 bad unordered pairs. The ordered distance histogram `930,10230,102300,639840,111600` equals 930 times the production root spectrum. Evidence is saved in `d11_production.best.independent_check.json`; no additional preflight or repeated graph verification was run here.

## Resources and terminal status

- Status: `COMPLETE_NO_SOLUTION` for these 38 modes.
- One worker, no restarts, no extension of the authorized range.
- Production process: **127.749179 CPU seconds**, including 125.542889 CPU seconds in complete BFS.
- New preparation, compilation and production total: **128.733068 CPU seconds**.
- Prior capacity plus tight-linear work, conservatively included: **3.049317963 CPU seconds**.
- Cumulative total before the parent-owned independent final check: **131.782385963 CPU seconds**, within 180 seconds.
- Parent-owned independent reconstruction plus one all-root check: **0.026326115 CPU seconds**.
- Cumulative total including that final check: **131.808712078 CPU seconds**.
- Independent final status: complete; pending actions: none.
