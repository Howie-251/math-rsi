# Prediction: a route-profile barrier on the stronger small-parameter source

2026-11-01, before independent attack or experiment. The q4/G1 replication window27..34 was stopped because the published q2 x q8 polarity product already gives8775 vertices at degree27, and its325 absolute-product vertices can be replicated. That is a public source, not a new graph constructed here. The next useful question is whether the existing spare-degree expansion mechanism can augment THIS source, rather than producing weaker q4 copies.

The prediction below is conditional on the explicit classical polarity-product interface. It is not a claim that every degree27 graph or every small parameter is excluded. No concrete8775 edge file, field/polarity table, BFS, solver or Lean run is requested by this note.

## Published interface and the controlled family

Use the looped polarity quotients A and B of GQ(2,2) and GQ(8,8). They have15 and585 vertices; all adjacency rows, counting a loop once, have3 and9 entries. Their absolute sets O_A,O_B have5 and65 vertices. Distinct absolutes have neither an edge nor a common neighbor, even with the loops retained. The loopless product S is obtained by deleting the self-loops of A tensor B. Published Cor7.9/Lemma7.10 give its order8775, maximum degree27, diameter3. This source interface is inherited from the primary formulas and must be checked in the independent paper attack; it is not a new field-existence assertion.

C=O_A x O_B has325 vertices of degree26; all other8450 vertices have degree27. Distinct C vertices have disjoint open neighborhoods. Each has26 neighbors, so these open neighborhoods partition S minus C.

For integer r>=0 append r full ORIGINAL S-neighborhood clones of every c in C, with no clone--clone edges. Every non-C old vertex now has degree27+r and is saturated at cap Delta=27+r. The free set F consists of the old325 C vertices and all325r clones; each has mandatory degree26 and spare r+1. Retain every source and mandatory clone edge, allow any extra F--F edges, and append any nonempty batch H of new helper vertices with arbitrary internal graph, still at cap Delta.

The prediction is that such an augmentation requires

    650 <= 2*(r+15)^2.

It consequently excludes EVERY nonempty helper batch in this exact family for r=0,1,2,3 (caps27..30), even with additional free--free edges. The r4/cap31 interface is not excluded by this bound and must not be marked impossible or automatically searched.

## A specific hard target class, not a total-bad-pair statistic

Focus on X=(V(A) minus O_A) x O_B: exactly10*65=650 old vertices. These lie outside C and are saturated after uniform copying.

For a free vertex f based at c=(a,b), at most2 of its mandatory neighbors lie in X: the second factor must equal the same absolute b, and the first coordinate is one of the2 nonabsolute neighbors of a. Within two mandatory old steps, at most6 targets in X are available. Indeed the second factor cannot reach a different absolute in at most2 steps, while the first factor's nonabsolute radius2 ball from an absolute has size at most2+2*(3-1)=6. Removing product self-loops cannot increase this count. A clone has exactly the same old-neighbor list as its base, so the same bounds apply to every f in F.

For h in H, let p_h be its actual number of F neighbors and d_h its helper degree. Saturation implies it cannot meet any old non-C vertex, so p_h+d_h<=27+r.

Classify every h-to-X walk of length<=3 by its first step:

* h--f, f in F: mandatory old suffixes reach at most6 X targets. The h--f edge has consumed one of f's r+1 spare slots, leaving at most r added F-peer edges; each such peer has at most2 mandatory X neighbors. Hence at most6+2r targets per actual first pin.
* h--g, g another helper: with only two steps left, X cannot be the next vertex or adjacent to a helper (it is saturated). The only remaining possibility is g--f--x, giving at most2 targets per actual F pin of g. A second helper step cannot finish at X, and an F-peer after g's pin would require four total edges.

This predicts the necessary inequality for every helper:

    650 <= (6+2r)*p_h + 2*sum_{g adjacent h} p_g.

Both overlap and repeated ownership only make this overcount less effective; no unique helper-owner assumption is made. Summing over t=|H|>0 and using the undirected helper graph gives

    650t <= 2*sum_h p_h*(r+3+d_h)
         <= 2*sum_h (27+r-d_h)*(r+3+d_h)
         <= 2*t*(r+15)^2.

The last integer quadratic has its maximum at d_h=12, independent of r. Divide by t. Predicted maxima for r0..4 are450,512,578,648,722. Thus r3 is still strictly short of650, whereas r4 is not ruled out.

## What this would change next

If supported, stop same-cap append attempts on the published8775 source and its complete uniform r1/r2/r3 code-copy variants; do not manufacture a queue of27..30 experiments. Continuing at31 would need a concrete rule coordinating helper pins, helper--helper routes and the degree cost at BOTH ends of free--free edges. This local per-helper upper bound does not guarantee that its favorable r4 numbers can be realized simultaneously.

Omitting or rewiring mandatory edges, nonuniform/incomplete copying, a different center code, a different source or cap, and graphs outside this controlled family remain open. This prediction is not kernel formalization, a new construction, a public priority claim, or part of the three new graphs' existing A/B/C review scope.

An independent paper attack plus at most one tiny scalar check (<=5CPU) should inspect the exact6/2 target counts, source versus looped-factor walks, repeated copies, all allowed extra-edge routes, both-end degree accounting, and the strict r3/cap30 boundary. No source reproduction or large computation is needed.

Primary provenance: [Isham et al.2026v2 Cor7.9/Lemma7.10](https://arxiv.org/html/2608.27253v2#S7.SS4), its absolute-point replication discussion in section7.7, and the completed local audit Q4_NEW_ROLE_REPLICATION_WINDOW27_34_20261101.md. The product and cloning ingredients are published background, not new achievements of this note.
