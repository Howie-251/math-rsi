# Complete C31 four-orbit degree-six capacity

All **47** connected degree-six four-vertex pseudographs were completed.
**25** pass the necessary D3 capacity test: **3 without loops and 22
with loops**. CPU time was **0.107312288 seconds**, wall time
0.109252401 seconds; terminal status is COMPLETE. There were zero actual
voltage assignments, lifted graphs, and BFS roots.

The complete labeled enumeration has 670 degree solutions, of which
142 are disconnected. The 528 connected solutions form 47 S4 orbits.
Every type has twelve undirected edges and nine free coordinates after
fixing a nonloop spanning tree. Raw and gauge coefficient counts agree
in every one of the 752 endpoint slots.

The best base is **K4 with two edges per pair (222)**. Its capacities
are **55 on the diagonal and 44 off the diagonal**, correcting the
tentative diagonal 61. The six immediate two-edge returns counted in
61 all give the identity and must be removed. The exact matrix is:

    55 44 44 44
    44 55 44 44
    44 44 55 44
    44 44 44 55

Each root has 187 reduced walks, and all of their forms are different
within their endpoint slots. Minimum capacity 44 exceeds the required
fiber size 31, but this is only a necessary condition. A future legal
assignment must make all sixteen evaluated sets equal F31.

| Total loops | Base types | Capacity passes | Best minimum |
|---:|---:|---:|---:|
| 0 | 6 | 3 | 44 |
| 1 | 4 | 3 | 35 |
| 2 | 10 | 5 | 37 |
| 3 | 7 | 5 | 35 |
| 4 | 10 | 5 | 35 |
| 5 | 4 | 2 | 31 |
| 6 | 4 | 2 | 35 |
| 7 | 1 | 0 | 24 |
| 8 | 1 | 0 | 26 |

Leading bases, ordered by minimum capacity then total capacity:

| ID | Loops | Cross counts 01,02,03,12,13,23 | Minimum | Total |
|---:|---|---|---:|---:|
| 5 | 0,0,0,0 | 2,2,2,2,2,2 | 44 | 748 |
| 4 | 0,0,0,0 | 1,2,3,3,2,1 | 42 | 736 |
| 13 | 0,0,1,1 | 2,1,3,3,1,0 | 37 | 704 |
| 3 | 0,0,0,0 | 1,1,4,4,1,1 | 37 | 700 |
| 9 | 0,0,0,1 | 2,2,2,3,1,1 | 35 | 736 |

Compared with the previous 172-point degree-seven family, this changes
the degree, field, number of edges, and all coverage requirements. It
has nine free gauge variables instead of eleven and 187 short words
per root instead of 302. It could exceed the saved (6,3) baseline 120
with a 124-point D3 lift. The capacity calculation supplies no such
lift and does not imply a better chance of finding one: its worst-slot
ratio 44/31 is lower than the old 322 ratio 68/43.

Files:

- [DERIVATION_PACKAGE.md](DERIVATION_PACKAGE.md): full degree enumeration,
  loop/gauge treatment, 55/44 paper count, and exact coverage conditions.
- [results.json](results.json), [all_bases.jsonl](all_bases.jsonl): summary
  and all 47 base records.
- [survivors.json](survivors.json), [top_bases.json](top_bases.json),
  [top_loop_bases.json](top_loop_bases.json): passing and ranked bases.
- [topology_222.json](topology_222.json): the best base's edge arrays,
  spanning tree, nine free coordinates, and capacities; no voltages.
- [enumerate_capacity.py](enumerate_capacity.py), [terminal.json](terminal.json):
  deterministic computation and final completion scope.

Reproduction: `python3 enumerate_capacity.py` from this directory.
No actual search is started by this report.
