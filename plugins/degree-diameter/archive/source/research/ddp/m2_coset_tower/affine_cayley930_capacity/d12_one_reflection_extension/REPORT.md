# Fixed degree-11 best, one-reflection extension

All 30 authorized extensions were evaluated and none has diameter 3. The fixed original generating set was not changed: for each x in F31 except 9, the reflection `(x,15)` was added to the degree-11 best in the parent directory. This is the complete finite extension of that single saved graph; no other degree-11 candidates or generator replacements were inspected.

The group is `F31 semidirect_3 C30`, multiplication `(x,j)(y,k)=(x+3^j*y,j+k)`, label `x+31*j`. Since `3^15=-1 mod31`, all 31 elements `(x,15)` are involutions. The original set contains exactly `(9,15)` among them. Every other addition therefore produces twelve distinct nonidentity inverse-closed generators and a 930-vertex, 5,580-edge, 12-regular Cayley graph.

Each of the 30 graphs received a complete BFS from the group identity. Left translation is vertex-transitive, so this gives the exact diameter and all-root distance spectrum by multiplication by 930. Individual actual generating sets, root deficits and complete root distance histograms are saved in `results.jsonl`.

The minimum root deficit is **67**, obtained by adding **(20,15)** (encoded 485). The saved best is connected with **diameter 4** and **31,155 unordered pairs beyond distance 3**, compared with 55,800 before the extension. Its complete root histogram is `{'0': 1, '1': 12, '2': 130, '3': 720, '4': 67}`. Full parameters are in `best.json` and the complete graph is in `best.edges`.

The program `run.py` ran once on one worker, completing all 30 inputs in **0.032439263 CPU seconds**, below the 5-second limit. Final cursor has no next input, status `COMPLETE_NO_SOLUTION`. The degree-12 family outside these 30 fixed-base extensions remains open. The parent completed the unique independent final check: all 5,580 reconstructed edges matched; one generic BFS over all 930 roots confirmed simplicity, connectedness, degree 12, diameter 4, and 31,155 bad unordered pairs. The ordered distance histogram is `930,11160,120900,669600,62310`, exactly 930 times the production root spectrum. Evidence is in `best.independent_check.json`. The independent check cost 0.027869488 CPU seconds; total construction plus independent checking is **0.060308751 CPU seconds**. No pending actions remain and no repeated graph check was run here.

| Added reflection x | Root deficit beyond radius 3 | Diameter |
|---:|---:|---:|
| 0 | 77 | 4 |
| 1 | 83 | 4 |
| 2 | 83 | 4 |
| 3 | 83 | 4 |
| 4 | 73 | 4 |
| 5 | 74 | 4 |
| 6 | 94 | 4 |
| 7 | 82 | 4 |
| 8 | 80 | 4 |
| 10 | 92 | 4 |
| 11 | 91 | 4 |
| 12 | 80 | 4 |
| 13 | 69 | 4 |
| 14 | 73 | 4 |
| 15 | 79 | 4 |
| 16 | 85 | 4 |
| 17 | 89 | 4 |
| 18 | 77 | 4 |
| 19 | 89 | 4 |
| 20 | 67 | 4 |
| 21 | 97 | 4 |
| 22 | 83 | 4 |
| 23 | 82 | 4 |
| 24 | 82 | 4 |
| 25 | 79 | 4 |
| 26 | 92 | 4 |
| 27 | 85 | 4 |
| 28 | 74 | 4 |
| 29 | 70 | 4 |
| 30 | 76 | 4 |
