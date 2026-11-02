# The saved 97-pair matching skeleton cannot be completed internally

Date: 2026-10-12. Allowing **all six internal Petersen graphs to change**
does not repair the fifteen external matchings of the saved 97-bad-pair
construction. A direct route-count witness rules out even arbitrary cubic
internal graphs. The proposed 180-CPU-second SAT call was cancelled before
CNF generation; there was no solver call.

For a source vertex \(u\in F_i\) and target fiber \(F_j\), the fixed
external matchings supply five route slots: the direct matching and one
two-edge route through each of the other four fibers. Let \(b_{ij}(u)\)
be the number of distinct targets in these five slots. An arbitrary
internal cubic graph in \(F_i\) supplies three additional slots, and an
arbitrary internal cubic graph in \(F_j\) supplies three. These are all
possible routes of length at most two. Therefore

\[
\#\{v\in F_j:d(u,v)>2\}\ \ge\ \max(0,4-b_{ij}(u)).
\]

In particular, every target requires \(b_{ij}(u)\ge4\), independently of
the choice of **all six** internal graphs. This strictly strengthens the
earlier [fixed-\(P_2\) row obstruction](PETERSEN_INTERNAL_REASSEMBLY.md).

## Explicit immutable witness

Read the external edges of the
[complete source](../../../computations/dd82/construction/petersen_four_fiber_reassembly_run/seed.json).
For vertex 29 and target fiber \(F_5=\{50,\ldots,59\}\), the five paths are

\[
29-51,\quad29-1-51,\quad29-19-55,\quad29-31-55,\quad29-42-55.
\]

They reach only 51 and 55. The six internal-route slots can add at most six
targets, so at least two targets remain uncovered regardless of every
internal graph. The shorter row \(0\to F_5\) also has only three fixed
targets, with multiplicities \(53^2,56^2,59\), and already suffices.

All 300 directed cross-fiber rows were read directly from the saved edge
list. Their fixed surplus \(5-b_{ij}(u)\) has distribution

\[
0:108,\qquad1:167,\qquad2:24,\qquad3:1.
\]

Thus 25 rows fail the necessary condition. Summing the unavoidable missing
targets over rows gives a lower bound for each directed block. For an
unordered block, take the larger of its two directional bounds, then sum
over the fifteen blocks. This proves at least **17 bad unordered pairs**
for every cubic internal completion of this particular matching skeleton.
The bound is not claimed sharp.

## Scope and evidence

The external matching skeleton is fixed, but no internal adjacency is
fixed in this argument. The result is not an exclusion of arbitrary
six-Petersen graphs. Any successful continuation from this skeleton must
change external matching edges contributing to the deficient rows.

- [Reproducible extractor](../../../computations/dd82/construction/petersen_all_internal_obstruction.py).
- [Every fixed row and its actual paths](../../../computations/dd82/construction/petersen_all_internal_completion_run/fixed_routes.json).
- [All failing rows, block bounds, and strongest witness](../../../computations/dd82/construction/petersen_all_internal_completion_run/obstruction.json).
- [Resources](../../../computations/dd82/construction/petersen_all_internal_completion_run/resources.json): 0.013380256 CPU seconds, 0.014785625 wall seconds.

No graph enumeration, new BFS, CNF, or solver was needed. The previously
saved [independent source BFS](../../../computations/dd82/construction/petersen_four_fiber_reassembly_run/seed.verification.json)
already records its 60 vertices, 240 edges, degree eight, and 97 bad pairs;
it was not repeated.
