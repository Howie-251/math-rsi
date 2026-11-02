# Three four-generator subsets all have exact diameter11

The fixed three-case experiment is complete, with zero D10hits,
zero untested cases and zero UNKNOWN results. Every actual graph
constructed in memory is simple, connected and4-regular, with20400
vertices and40800edges. Each exact global diameter is11, exceeding
the target10. No new lower bound resulted.

The three inverse pairs are P0=(850,16575),P1=(4183,17412), and
P2=(13044,18426), named by the images of0under the recovered actual
permutations. Each case uses the four permutations in two pairs and
adds the undirected edges v—pi_s(v). These are left-Cayley edges;
they were not assumed to be old source edges in its original labels.

| Selected pairs | Reached from0 | Exact globalD | Root targets beyond10 | First such target |
|---|---:|---:|---:|---:|
| P0,P1 | 20400 | 11 | 31 | 437 |
| P0,P2 | 20400 | 11 | 392 | 851 |
| P1,P2 | 20400 | 11 | 16 | 3287 |

Each row used one complete ordinary BFS from0. The source group
Gamma is already proved regular on the old labels. Identify each
label with its unique group element g via g(0). The new edge rule is
g—s*g. For any h in Gamma, abstract right multiplication g→g*h maps
this edge to g*h—s*g*h, another new edge, and acts transitively.
Thus the new graph is vertex-transitive. All rows are connected, so
the measured0eccentricity equals the global diameter. No all-source
distance sweep is needed for this conclusion.

The displayed beyond10counts are single-root target counts. If an
ordinary global unordered count is wanted, transitivity gives
n*k/2:316200,3998400and163200, respectively. They are exact derived
counts by the stated symmetry proof, not a separately run all-pairs
BFS or one shared aggregate across the three graphs.

RESULT.json contains all distance histograms and literal pair IDs;
run.py reproduces each graph directly from the saved six permutation
files. Failed graphs were not exported as new record artifacts. Total
recorded CPU was0.111369seconds, with three candidate-root BFS runs,
zero original-source D7checks and zero source downloads. The original
at-least-one-D10prediction is refuted on exactly these three subsets.
This finite family is closed and stopped; no generator was replaced,
retuned, or selected according to the smaller residual count.
