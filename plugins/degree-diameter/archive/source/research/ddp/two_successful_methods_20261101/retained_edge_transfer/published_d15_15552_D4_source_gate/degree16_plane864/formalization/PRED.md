# Concrete (16,4)16416 Lean batch

Only the actual fixed I32 × W={x1=0} clone graph is in scope. Source is the already kernel-closed literal F3Graph15552.graph, on Fin15552. New carrier is Fin15552 ⊕ Fin864 with explicit equivalence to Fin16416. New j=27*controllerIndex+offsetIndex, old center uses coefficients (1,9,27) and new label15552+j. Source adjacency deletes virtual self at the old center, inherited unchanged from the source SimpleGraph.

Prediction: reuse Clone16389.recover_stepVec/recover_plane symbolically; independently kernel-check the new 32×5 positive controller-owner equations; then pinOwner_forward gives common-pin uniqueness and load≤1. Generic FullNeighborhoodClones gives degree≤16, genuine Walk≤4 and inherited nonD3 from the unconditional closed source. No old PASS module, field, rank word, coset group or geometry is recompiled.

Budget: one cumulative new batch≤200 CPU seconds, including code preparation, every failed attempt, driver and external small-table binding; one compiler worker, each new module hard≤60 CPU seconds. Four new modules only: F3Graph15552Clone16416Definitions, Inputs, Exact, standaloneAudit. Actual parent import requires no recompilation. Based on old successful analogous Inputs4.154/Exact2.135/Audit2.768 CPU seconds, expected new total is under30 CPU seconds; this is a forecast, not a PASS.

Producer is actually closed: graph_d16_D4_n16416.edges header16416 129240, old116316 edges retained, new12924, centers14:36/15:828. Full independent all-root acceptance is separate and currently pending; producer PASS does not establish that receipt. External typed-label binding will compare ordered literal864roles and independent acceptance when available, without parsing the large graph again or claiming a Lean ASCII parser.

Targets: original unconditional named d16_16416/FinalClaim/final_claim, explicit label equivalence, true SimpleGraph.Walk D4, nonD3, standalone types/body/axioms Audit with only propext, Classical.choice, Quot.sound. Source15552 is a published reproduction and adds no result. No count/state/Wiki/review/ZIP/hash updates in this batch.
