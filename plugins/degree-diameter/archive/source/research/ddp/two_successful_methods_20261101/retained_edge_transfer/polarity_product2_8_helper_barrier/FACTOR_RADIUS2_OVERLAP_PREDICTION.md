# Prediction: eight absolute pins cannot cover every nonabsolute B target

2026-11-01, before the new paper attack or the small support experiment.
The supported cap31 condition only forces some helper to own at least eight
different based classes in one A row. It does not say that eight pins repair
that row. The specific next question is how much the old two-step routes of
those eight B absolutes necessarily repeat.

Let M be the symmetric looped point-polarity adjacency of a genuine
GQ(q,q), q=2 or 8 here. Every row has q+1 entries and there are q^2+1
absolute vertices O. Distinct absolutes have no edge/common neighbor.
For b in O let T_b be the nonabsolute vertices reached in at most two
factor steps. Predict

    |T_b|=q(q+1),    |T_b intersect T_c|=q+1 for b!=c.

Reason to test: the GQ projection axiom gives the exact matrix identity
M^3=2q M+J. For an incident point/line endpoint pair there are 2q+1
three-step incidence walks; for a nonincident pair projection gives one.
Thus M^4=2q M^2+(q+1)J. GQ incidence has no4-cycle, so off-diagonal
entries of M^2 are 0 or1. In an absolute row the only absolute entry of
M^2 is its own diagonal q+1; its nonabsolute support contains immediate
neighbors too, because its absolute loop pads their one-step walks.
The row sum and the off-diagonal absolute-absolute M^4 entries give the
two predicted support counts.

For t distinct absolutes with 1<=t<=q, let m_x count how many T_b contain
the nonabsolute x. Since binom(m_x,2)<=t*(m_x-1)/2 on the union, predict

    |union T_b| <= (q+1)*((q-1)*t+1).

At q=8,t=8 the union is at most513 of520 nonabsolute B vertices, hence
at least7 are missed. At q=2,t=2 the union is exactly9 of10. Therefore
an eight-class A row still needs an external helper/F-peer route to at
least one unowned based class. This strengthens a local route obligation;
it does NOT exclude cap31 or require every helper to have nine pins in a row.

The bounded test is the existing literal15-row q2 factor, reconstructed
directly from its saved recipe without rerunning the225/230 graphs. Enumerate
its five absolute supports and their ten pairs once. For every subset of
the five absolutes, compute the exact set of additional based classes whose
mandatory one-step pairs are needed to cover the nonabsolute complement.
Predicted external-class counts as a function of distinct own classes are
5,4,1,0,0,0 for t=0..5. Repeated copies do not change these supports.
Return explicit missed vertices and required classes, not just union sizes.
One Python run <=2CPU, no BFS/graph/field/solver/Lean/source generation,
and no portfolio/parameter/Lean increment. No q8 finite table or8775 graph
is assumed to be available.

If supported, a future cap31 generator must track repeated routes and the
remaining required classes for each helper: an eight-pin row is not a
finished row. If refuted, save the counterexample and remove the invalid
support inference before any controller search. This analysis is outside
the existing three-graph final-C scope.
