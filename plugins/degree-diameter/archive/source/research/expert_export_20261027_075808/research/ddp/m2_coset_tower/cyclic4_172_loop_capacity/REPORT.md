# Complete loop-base capacity enumeration

All **91** connected seven-regular four-vertex multigraphs, with loops
counted twice in the degree, were completed. **52** pass the necessary
three-step C43 linear-form capacity test; **48 of those contain loops**.
No voltage assignments or lifted graphs were searched, and no BFS was run.

Measured enumeration and capacity CPU was **0.310231033 seconds**; wall
time was 0.312724128 seconds. The process exited 0 with status COMPLETE,
well within the single-worker 60 CPU-second allocation.

The degree enumeration has 1270 labeled solutions, of which 48 are
disconnected. The remaining 1222 solutions form 91 S4 orbits. All orbit
sizes were checked against the labeled occurrence counts. Every root has
302 reduced walks of length at most three, including repeated same-way
loop traversal. In all 1456 endpoint slots, the count of distinct full
14-variable forms equals the count after the three tree coordinates
are removed.

| Total loops | Base types | Capacity passes | Best minimum capacity |
|---:|---:|---:|---:|
| 0 | 7 | 4 | 68 |
| 1 | 5 | 5 | 59 |
| 2 | 14 | 10 | 61 |
| 3 | 11 | 8 | 57 |
| 4 | 17 | 11 | 61 |
| 5 | 11 | 6 | 49 |
| 6 | 11 | 5 | 51 |
| 7 | 6 | 1 | 43 |
| 8 | 5 | 2 | 49 |
| 9 | 2 | 0 | 17 |
| 10 | 1 | 0 | 2 |
| 11 | 1 | 0 | 17 |

Some leading loop bases are below. Cross multiplicities are ordered
01,02,03,12,13,23. Ranking uses minimum capacity and then total capacity;
it does not predict actual voltage feasibility.

| ID | Loops l0,l1,l2,l3 | Cross multiplicities | Minimum | Total over 16 slots |
|---:|---|---|---:|---:|
| 21 | 0,0,1,1 | 3,2,2,2,2,1 | 61 | 1178 |
| 67 | 1,1,1,1 | 1,1,3,3,1,1 | 61 | 1132 |
| 11 | 0,0,0,1 | 2,3,2,3,2,1 | 59 | 1184 |
| 17 | 0,0,1,1 | 2,1,4,4,1,0 | 59 | 1100 |
| 10 | 0,0,0,1 | 2,2,3,4,1,1 | 57 | 1162 |
| 46 | 0,1,1,1 | 2,2,3,2,1,1 | 57 | 1162 |

The previous loop-free balanced 322 base remains the maximum of this
capacity ranking, with minimum 68 and total 1196. ID 21 changes it by
replacing two of the 2--3 matchings with one loop at each endpoint. This
raises the 2--3 capacity to 85 but reduces the two affected self-orbit
capacities to 61. It changes the available short words without improving
the weakest symbolic margin. The exact remaining condition is that
every slot's evaluated forms cover F43 simultaneously.

Full definitions, completeness argument, gauge proof, exact set-matrix
coverage condition, and the comparison in matched labels are in
[DERIVATION_PACKAGE.md](DERIVATION_PACKAGE.md).

Machine-readable output:

- [results.json](results.json): summary, all loop-count strata, old 322
  and best loop base, measured timing, and actual completion scope.
- [all_bases.jsonl](all_bases.jsonl): all 91 representatives, edge arrays,
  spanning tree/free indices, raw walk counts, and full/gauged capacities.
- [survivors.json](survivors.json): all 52 passing base representatives.
- [top_loop_bases.json](top_loop_bases.json): the twelve leading loop bases.
- [topology_candidate_21.json](topology_candidate_21.json): a direct
  construction interface for the highest-ranked loop base; no voltages.
- [enumerate_capacity.py](enumerate_capacity.py): deterministic producer.
- [terminal.json](terminal.json): COMPLETE, not running, zero graphs/BFS.

Reproduce from this directory with `python3 enumerate_capacity.py`.
This report closes only the requested capacity calculation; no graph
record or existence claim follows from a passing base.
