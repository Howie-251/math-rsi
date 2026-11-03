# A forced edge excludes the actual refined order58 deletion set

2026-10-18. Scope: all monotone degree-eight diameter-two completions of the
single saved deletion set from `refined/n58/deletion_candidate.json`.
This is not an exclusion of the full polarity73 family or of arbitrary order58.
The refined screen's arbitrary choice values are not assumed.

Let H be the surviving induced graph in the saved 73-point geometry, after
deleting

    {8,16,21,22,23,27,28,31,51,52,54,56,63,64,69}.

For a survivor x, write δ(x)=8−deg_H(x). Every target of order above57
is eight-regular by the inherited regularity theorem. Monotonicity retains
every H edge, so δ is precisely the number of new incident edges.

Direct extraction from the saved ambient edge list gives:

| x | N_H(x) | δ(x) |
| --- | --- | --- |
| 0 | {65,66,67,68,70,71,72} | 1 |
| 1 | {9,17,25,33,41,49,57} | 1 |
| 2 | {5,13,29,37,45,53,61} | 1 |
| 5 | {2,10,18,26,34,42,50,58} | 0 |
| 61 | {2,15,19,30,32,45,49,60} | 0 |

The pairs {0,5} and {0,61} have neither an H edge nor an H common neighbor.
Vertices5 and61 are saturated and cannot acquire any new neighbor. Hence
the unique new neighbor of0 must lie in N_H(5)∩N_H(61)={2}. Every completion
therefore contains the added edge {0,2}. This conclusion follows from H,
not from the particular SAT assignment.

Let H'=H+{0,2}. Vertices0 and2 are now saturated, so their final neighborhoods
are fixed as

    N(0)={2,65,66,67,68,70,71,72},
    N(2)={0,5,13,29,37,45,53,61}.

These sets are disjoint. Vertex1 still has deficit1, and has neither adjacency
nor a common neighbor with0 or2 in H'. Its only new neighbor must therefore
lie in both fixed neighborhoods, an impossibility. Thus this entire fixed-D
monotone completion problem is impossible. No full completion SAT run is
needed for this candidate.

## What the observed failure teaches

The refined screen correctly accounts for vertices already saturated in H,
but not all consequences of vertices becoming saturated after forced new
edges. A locally compatible set of unit-neighbor choices can therefore pass
the screen without a simultaneous completion. Merely reporting the chosen
model's capacity overflow at vertex72 would not prove this conclusion,
because other choices were allowed. The forced-edge argument above does.

Next decisions should consider complete simultaneous completion or a justified
generation change, rather than an indefinite chain of progressively weaker
partial screens. The 59-point refined screen returned UNKNOWN within its
single short profile, so it has no candidate or exclusion.

## Actual evidence

- `computations/dd82/construction/polarity73_reduction_run/refined/n58/result.json`:
  18325 variables,73630 clauses; SAT, CPU0.963712s/wall1.134302s, complete model
  and direct-predicate checks passed; no proof output, no target graph.
- `refined/n59/result.json`: 18267 variables,73399 clauses; UNKNOWN, CPU27.996050s/
  wall28.192344s, exit0 at solver soft limit; no proof output, no exclusion.
- `refined/analyze_fixed_candidate.py` and n58 `forced_completion_analysis.json`
  recompute only H from D and propagate mathematically forced edges. Its
  additional forced edge43–53 is unnecessary to the displayed short proof.
- `refined/CODE_REVIEW.md` records the scoped same-family source review.
  This manuscript is a paper/computation-extraction argument, not a Lean proof.
  Any further review status must be read from its actual receipt, not inferred.
