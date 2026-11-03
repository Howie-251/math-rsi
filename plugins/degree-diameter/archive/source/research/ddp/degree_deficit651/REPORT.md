# Complete one-step deficit-moving neighborhood of the saved 651 graph

The input is `research/ddp/matching_single_vertex650/complete.best_filtered.edges`: 651 vertices, 1,627 edges, exactly one degree-four vertex w=650 and all other vertices degree five. Its previously independently verified number of unordered pairs at distance greater than five is 59.

A move chooses x not equal or adjacent to w, chooses y adjacent to x, adds wx and removes xy. Exactly 646 choices of x each have five choices of y, so the entire legal neighborhood has 3,230 distinct moves. The move leaves x at degree five, raises w to degree five, and moves the unique degree-four deficit to y. Simplicity and maximum degree five are preserved.

`enumerate.cpp` evaluated all 3,230 moves in lexicographic (x,y) order using full all-root breadth-first search through radius five. Every unordered pair outside the closed radius-five balls contributes once. There was no early score cutoff, sampled root set, or search beyond this one neighborhood. `complete.moves.tsv` records every move and its exact score.

The actual terminal status is COMPLETE, session 83751 exited with return code 0. The profile used 9.42548 CPU seconds and 9.42763 wall seconds, below the authorized 60 CPU seconds. The first 16 moves took 0.047803 CPU seconds and projected 9.65023 seconds for completion.

| Statistic | Exact result |
|---|---:|
| Legal moves / evaluated | 3,230 / 3,230 |
| Minimum bad pairs | 61 |
| Median bad pairs | 109 |
| Maximum bad pairs | 138 |
| Improving / equal / worsening versus 59 | 0 / 0 / 3,230 |
| Moves attaining minimum | 2 |

The minimizing moves (x,y) are (47,292), (279,34). The first is saved as `complete.best.edges`: add (47,650), remove (47,292), so the deficit is at 292.

`independent_check.py` reads the saved complete edge list afresh. It confirms the exact single-edge addition/deletion, simplicity, connectedness, 650 vertices of degree five, one vertex of degree four, diameter six, and exactly 61 unordered bad pairs. Its full Python BFS took 0.2751 CPU seconds. The ordered distance histogram for distances 0 through 6 is (651,3254,13012,52012,178126,176624,122). Vertex 650 now has seven distance-six partners; the moved degree-four vertex 292 has eight. The check also independently enumerates the complete legal move list and verifies the stored result histogram.

The saved 59-defect input is therefore a strict local minimum for this precise deficit-moving neighborhood. This rules out a non-worsening single move from that graph. It does not rule out longer sequences, other degree-preserving changes, or other graphs. No further search was started.
