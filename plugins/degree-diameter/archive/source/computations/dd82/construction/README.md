# Degree 8, diameter 2: construction artifacts

Run from the project root:

```sh
python3 computations/dd82/construction/brown57.py
python3 computations/dd82/construction/verify_edges.py computations/dd82/construction/brown57.edges --out computations/dd82/construction/brown57.verification.json
python3 computations/dd82/construction/triangle_edit_obstruction.py
```

`brown57.edges` begins with `57 224`; every following line is an unordered edge listed once. `brown57.vertices.json` supplies its coordinates. `verify_edges.py` checks simplicity, degrees, and every pair by BFS without importing the generator.

The triangle script checks exact finite premises and enumerates the two minimum covers, producing 4374 necessary seven-edge deletion patterns. It does not construct an extension. The independent coverage diagnostic is:

```sh
g++ -O3 -std=c++17 computations/dd82/construction/r7_domination.cpp -o computations/dd82/construction/r7_domination
computations/dd82/construction/r7_domination computations/dd82/construction/brown57.edges computations/dd82/construction/seven_edge_deletion_patterns.txt computations/dd82/construction/r7_domination.csv
```

The diagnostic's internal wall-time limit is 110 seconds, one CPU. The completed run took about 0.077 seconds and failed the necessary condition on every pattern. A uniform mathematical reason replaces reliance on this enumerative result; see `proofs/dd82/construction/BROWN_EXTENSION_OBSTRUCTION.md`.

`insertion_obstruction.py` is an earlier weaker neighborhood-count check, superseded by the triangle result. `upc_isomorphism.json` stores a bijection to the downloaded public record graph. No graph larger than 57 was found, no global upper bound was established by these computations, and none of these artifacts is a Lean theorem.

## Order63 norm certificate

`python3 computations/dd82/construction/n63_cyclotomic_norms.py` regenerates all63 real cyclotomic polynomials, exact norms and modular nonsquare witnesses using only integer arithmetic. It terminates in under a second on this machine. Only conductor3 has a square norm. The separate original-graph proof is `proofs/dd82/construction/N63_CYCLOTOMIC_SPECTRAL_OBSTRUCTION.md`; the finite data alone do not supply its field and eigenspace bridge. An independent reviewer checked the63 norms by multiplication determinants; the paper proof is reviewed, but the whole upper62 result is not yet in Lean.

## Bounded order58 construction diagnostic

`search58_switches.cpp` starts from Brown57 plus a new vertex joined to its eight degree7 vertices and uses simple degree-preserving two-edge switches. Its objective is exactly the number of unordered pairs without a path of length<=2. Compile with `g++ -O3 -std=c++17 computations/dd82/construction/search58_switches.cpp -o computations/dd82/construction/search58_switches`. Run arguments are `brown57.edges wall_seconds rng_seed output_prefix`, each with the needed path.

Profile budget: one CPU for5 seconds, no subsequent long run authorized by the observed evidence. Seed1 made8,212,021 legal proposals, preserving degree8, and did not improve the starting21 uncovered pairs. Files `search58_profile.*` save the actual run, diagnostic graph and independent BFS. The verifier returns exit1 as expected: all58 vertices have degree8, but21 pairs have distance3. This graph is not a target witness.

The complete local-neighborhood check `python3 computations/dd82/construction/brown58_one_switch.py` enumerates all39,200 legal single switches from that seed. Its minimum score is26, proving that the starting score21 is a strict local minimum for these moves. The saved exact histogram is `brown58_one_switch.json`; runtime about2.54 CPU seconds. This does not rule out longer switch sequences, larger Brown edits, or arbitrary58-point graphs. A new search should change the move neighborhood or use coupled edits, not just repeat this short unchanged trajectory.

## Larger edit obstruction and changed insertion profile

`brown_eight_delete_facts.py` supplies concrete premises for the now reviewed >=9 old-deletion theorem in `BROWN_EIGHT_DELETE_OBSTRUCTION.md`. `brown_r9_eight_iii_facts.py` checks14 full-cover and42 twenty-cover III families plus84 EE alternatives for the narrower `BROWN_R9_EIGHT_III_OBSTRUCTION.md`; the six/seven-III nine-deletion branches remain. Its former6.14million-subset exploratory profile is saved but is unnecessary to the new six-point argument.

`brown_dominating8.py --exclude-polar-lines` obtains and independently verifies an eight-point dominating set distinct from every polar line. This is only a vertex subset. `brown_dominating_repair.py` adds the new vertex there and repairs degrees by greedy edge transfers, giving a regular58 graph with29 uncovered pairs. `search58_switches` now accepts either Brown57 or an explicit regular58 edge list. The five-second profile under `brown_dominating8_nonline/` returned score21; independent BFS and direct edge-set comparison show it is exactly the earlier Brown-plus-hub seed after swapping57 and39. This route has not escaped the established local trap. All positive scores are failed target graphs.

## Bounded A5 construction family

`a5_cayley60.cpp` constructs the60 even permutations onfive letters and checks every inverse-closed8generator set. The15involutions and22inversepairs give600875sets, exactly matching the executed count. The maximum radius-two ball is53; no target graph was found. The saved best60-vertex graph is8regular but has210 distance-three pairs, independently checked by `verify_edges.py`. Results are `a5_cayley60.json` and `a5_cayley60_best.verification.json`; this excludes only the declared construction family computationally, not arbitrary60graphs. Runtime0.0532s onone pinned CPU, with30s outer limit. No learned state or SAT used.

The user has stopped further dedicated known63–65 proof development. Existing order63 data above are retained as past evidence, not an active task.
