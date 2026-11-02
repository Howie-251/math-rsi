# Selected actual small candidate:17/2016, before generation

The one exact controller packing test returned optimum6 in373 nodes,
0.001421773 CPU seconds, supporting the saved maximum6 prediction.
Its actual controller centers are I=[0,3,5,7,9,16], with disjoint open
neighborhoods covering24 controller layers. The7-capacity envelope was
not attained. Stop the controller-only packing search here.

Select only this one candidate, not the1936 fallback and not an18/19 ladder.
For i=0..5 and a,b in F4, clone the complete original neighborhood of

    c(i,a,b)=64*I[i]+a+4*b+16*(a XOR b).
    new(i,a,b)=1920+16*i+4*a+b.

All96 centers lie in the common transversal plane. Every center has16
source neighbors. Each selected controller layer uses every old vertex
in each of its four neighboring layers exactly once. Thus all1536 pins
are distinct, and each has final degree17. The other384 old vertices and
96 new vertices have degree16. Predicted n2016, m16896, histogram
{16:480,17:1536}; no old edge removed and no new-new edge.

Every pair of DISTINCT new vertices is predicted to have distance EXACTLY3:
disjoint full neighborhoods forbid length2, while full-N endpoint Walk
replacement in the actual D3 source supplies length3. Each new vertex is
distance2 from its old center. These are specific route predictions to be
checked independently, not just a total failed-pair count.

The old1920 raw edge table was not located locally; materialize it once
from the already accepted literal edge-local recipe so the new graph can
have an actual complete edge table and physical source binding. Do not run
the author's full main, source BFS, inverse/rank/pencil/field tests or hashes.
One producer worker, whole production CPU<=15s. Return source and candidate
edge tables,96 ordered centers/neighborhoods, PARAMETERS/RESULT/TERMINAL
and genuine all-pair/prefix proof. Fresh independent budget<=30s after
production: parse each small table once, verify full old body and all96
complete neighborhoods/load/degree, then ordinary BFS from just96 NEW
roots. Compare all new-new distances and new-center distances with the
predictions. Zero old-root BFS. No solver/Lean/seed/timer reset.

The primary Comellas table currently stops at degree16 and cannot be read
as a degree17 row.1920 is only the located degree-monotone guarantee;
current global17 threshold and exact priority remain UNKNOWN. A small
complete legal graph is useful evidence for the combined mechanism,
but cannot be called a record on that basis. Check cached admissible
general-family bounds before any long source Lean investment. Source1920
is a published reproduction and must not increment the named portfolio.
The new2016 candidate is not accepted or counted until independent results.
