# T34 paper proof obligations

Scope: the complete finite exact mathematical candidate linked from
`../PAPER_CANDIDATE_MAP.md`. No asymptotic limits occur. This audit is distinct
from the later final Lean/export audit. The original theorem is unchanged.

Typed symbols: V finite set; E finite set of five-element subsets of V;
d:V→N degree; λ on distinct vertex pairs→N codegree; selected labels Fin s;
n_T:N exact edge-trace multiplicity; z_slot:N actual bad unordered-edge-pair
count; layout p:Fin s↪{1,…,v}; γ,β,δ,κ nonnegative rational dual weights.

Dependencies run in this order, with no backwards use of the new theorem:

1. R: original arbitrary finite ≤34 target reduces to <=20 or pair-covered
   21–25, exactly34; completed Lean handles <=20 and 21 degree5.
2. P: actual coloring algorithm failure is covered by the conditional
   random-order A/B/C events; genuine bad pairs remove noncontributors.
3. Q: ordinary total/pure/avoided quotas hold for the actual simple hypergraph.
4. D: exact shared-vector weak dual gives one valid strict layout when its
   repaired rational bound is below one; no assumption on solver optimality.
5. C: each local integer trace catalogue covers all actual selected inputs,
   with degree/edge/pair identities and explicit relabeling transport.
6. N19–N25: actual selections and exhaustive degree/structure cases land in
   strict catalogues, strict projections, or impossible residual structures.
7. T: combine R, P, Q, D, C and all N branches to recover the original coloring.

Micro-claims requiring special attention:

- MC-R: internal pair coverage/point count/exact edge count are derived, not
  left as new original-theorem assumptions.
- MC-D1: all layouts use the same actual z; capacities and unordered/directed
  weights agree; γ sums to one and β≤γ; coefficient deficits pay capacity.
- MC-QW (side diagnostic only): the weighted-overlap inequality is not used
  by any retained strict certificate; it is outside the required dependency DAG.
- MC-C1: promotion/projection visits every actual input, including empty and
  singleton counts; bounded ranges do not assume realizability or miss it.
- MC-C2: all graph/profile relabelings preserve degree roles and certificate
  positions; deleting strict subprofiles is an actual-H coloring argument.
- MC-21: all possible minimum degrees 5/6/7/8 and their count subcases covered.
- MC-22: r6=0,1,2,>=3 complete; actual unit selections discharge every cap.
- MC-23A: min-six weighted exchange, W=6 two-K7 equality and actual extra point.
- MC-23B: r6=1,2 actual common-unit sevens and universal residual graph bound.
- MC-23C: r6=3 U≥8/U7≥2 and all four-high projections.
- MC-23D: r6=4/5 every four-low subset forces unit, same-U triple counts;
  r6>=6 complete extensions and actual degree7/8 choice.
- MC-24: weighted three-class eight-lock selection, temporary negative empty
  restoration, actual eighth low and all deletion witnesses.
- MC-25: q=5/8/9 actual nine-lock selection; true tenth point for each residue;
  universal nine-lock lemma does not assume pair coverage after padding.

For each application the proof source in the map locates its hypotheses and
discharge. The fresh reviewer must report any missing discharge with exact
location, counterexample attempt, downstream impact and smallest valid repair.
