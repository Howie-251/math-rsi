# An actual 33-point partial ovoid in the existing W(3,7) labeling

The bounded reproduction succeeded. This is an explicit object of the size already published by Cimrakova–Fack in2007, not a new size record, maximum proof, graph or method. No isomorphism identification with the authors' unpublished coordinate list is asserted.

The point ids, sorted in the unchanged400-point order of the parent `PARAMETERS.json`, are

```
20,32,40,42,43,44,52,57,85,119,122,133,147,165,179,199,
230,248,251,260,265,279,295,312,315,322,323,326,337,347,
364,378,394.
```

`ACTUAL_POINTS.json` contains these labels, all33 normalized GF7 coordinate vectors and their33 distinct spread owners. The coordinates are copied from the accepted parent table, rather than independently reordered or reconstructed.

## Construction and cost

The fixed400-point conflict graph was built in memory from the accepted400 isotropic line lists. Its edges encode collinearity. This is the small point compatibility problem authorized for this task; no160050-vertex source edge file was read and no new diameter-three graph was produced. The old22-point set was retained as a valid lower bound and supplied the first initial state.

`find33.cpp` uses the predeclared target33 finite tabu-swap construction with PRNG seed2026110133. It found a conflict-free33-set at the first restart after16 moves, so no further restart, second seed or timer continuation was used. The partial-ovoid search process used0.006378CPU seconds, compilation0.922154, and the wrapper and final selected-set checks approximately0.006915. The reported conservative total, including a0.25-second allowance for earlier short input-discovery commands, is **1.185446749CPU seconds** under the30-second single-worker budget.

`BEST_EVENTS.csv` preserves the actual valid-set improvements; `BEST_POINT_IDS.txt`, source code, frozen input lines and CPU receipts make this one run concrete and reproducible. The failure of a local `pdftotext` lookup is recorded in PRED; nothing was installed and no new web batch was started.

## Selected-set proof

For the coordinate convention already used by the accepted source, define

```
B(x,y)=x0*y2+3*x1*y3-x2*y0-3*x3*y1 modulo7.
```

The stored symplectic Gram matrix gives twice this form. Since2 is nonzero in GF7, these forms have the same zero relation. Only the newly selected528 unordered distinct pairs were evaluated; every value is nonzero. Each pair's point ids and actual residue are saved in `SELECTED_PAIR_PROOF.csv`.

Independently within the same final selected-set check, intersecting the33 ids with each stored isotropic line gives

```
0 selected points: 136 lines
1 selected point:  264 lines
2 or more:          0 lines.
```

Thus the33 projective points are pairwise noncollinear and form a partial ovoid in this actual source geometry. Its distinct spread owners also follow because every spread line is one of these isotropic lines. These are small checks of the new set; the old field axioms,400-point geometry,160050 graph, BFS and Lean were not repeated.

The success-only conclusion is the explicit33-point partial ovoid. A later full-neighborhood clone construction on the original filled160050 source would still need its own authorized production and acceptance. The conditional65/161700 and70/169950 targets are not produced or counted here. `RESULT.json` and `TERMINAL.json` record `PASS_REPRODUCED_PUBLISHED_PARTIAL_OVOID33` with no active process.
