# Complete one-vertex deflation of the 20-bad-pair order-60 candidate

Date: 2026-10-11. This is a new finite construction experiment at order 59,
starting from the saved order-60 twin-HS candidate. It produces complete
graphs outside the equal-ten-point-fiber model, but no diameter-two graph.

For each of the 60 possible deleted vertices v, remove v and all eight
incident edges. Pair its eight neighbors by any perfect matching and add
the four resulting edges. The initial graph is triangle-free, so those
neighbors are independent and every added edge is new. Each surviving
neighbor loses and gains one edge; every other degree stays eight. Thus
every candidate is a simple 59-vertex, 236-edge, eight-regular graph.

There are 7!! = 105 neighbor matchings per deleted vertex. Recursively
pairing the least unpaired vertex with every other unpaired vertex visits
each matching exactly once. All **6,300 construction choices** were checked
by full two-step bitset unions, with no symmetry or random sampling.
Different construction choices are not asserted to give nonisomorphic
graphs.

The minimum is **28 bad vertex pairs**, attained by 60 choices. The full
histogram is retained in `candidate.json`. One minimum deletes original
vertex 41 and adds edges (9,14), (28,42), (38,46), (40,59), in the original
60-vertex labels. The saved graph relabels the remaining vertices in order.
An independent all-source BFS reads its complete edge list and confirms
59 vertices, 236 edges, every degree eight, diameter three and 28 bad pairs.
The retained candidate was also reconstructed from the recorded edits and
compared directly with its edge list.

The enumeration used **0.004001 CPU seconds**, one pinned CPU, with a
10 CPU-second / 4 GiB limit. No annealing, SAT or unchanged earlier search
was run. The complete scope is only this specified one-vertex deflation
neighborhood of the one saved order-60 graph. It excludes neither arbitrary
order-59 graphs nor larger edits of these candidates.

Evidence:

- `computations/dd82/construction/twin60_deflate59.cpp`
- `computations/dd82/construction/twin60_deflate59_run/candidate.json`
- `candidate.best.json`, `candidate.best.edges`,
  `candidate.best.verification.json`, `candidate.failure_analysis.json`,
  and `run.json` in the same directory.

The best deletion removes two old bad pairs, repairs five more, retains
thirteen old bad pairs, and creates fifteen new ones:20−2−5+15=28.
The failure analysis records every one of these pairs in original labels. Any further
repair must account for those newly lost paths as well as the old twin
interface. A separate bounded unrestricted two-edge-switch investigation
is recorded independently when complete.
