import DegreeDiameter.Portfolio.F9PlaneClone55Exact
open DegreeDiameter.Portfolio
set_option pp.explicit true in
#print DiameterAtMost
#print F9PlaneClone55.clonePair
#print F9PlaneClone55.parameters
#print F9PlaneClone55.plane
#print F9PlaneClone55.center
#print F9PlaneClone55.graph
#print FullNeighborhoodClones.graph
#print F9PlaneClone55.label
#check F9PlaneClone55.clone_label
#check F9PlaneClone55.center_source_label
#check F9PlaneClone55.label_old
#check F9PlaneClone55.label_new
#check F9PlaneClone55.pinInverse_basis
#check F9PlaneClone55.pinInverse_left
#check F9PlaneClone55.common_pin_index_unique
#check F9PlaneClone55.load_le_one
#check F9PlaneClone55.source_no_isolated
#check F9PlaneClone55.old_walk_bound_iff
#check F9PlaneClone55.concrete_order_degree_and_exact_D3
#print F9PlaneClone55.concrete_order_degree_and_exact_D3
#print F9PlaneClone55.FinalClaim
#print axioms F9PlaneClone55.load_le_one
#print axioms F9PlaneClone55.concrete_order_degree_and_exact_D3
#print axioms F9PlaneClone55.final_claim
set_option eval.pp false in
#eval ("CLONE55_ORDERED_BINDING", (List.finRange 81).map (fun i =>
  [i.val,(F9PlaneClone55.center i).val,(F9PlaneClone55.label (.inr i)).val]))
