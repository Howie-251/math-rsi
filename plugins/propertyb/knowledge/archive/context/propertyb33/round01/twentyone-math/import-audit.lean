import Aris4Math.ThirtyThree.TwentyOne
import Aris4Math.Main

#print Aris4Math.Simple5Hypergraph
#print Aris4Math.Simple5Hypergraph.PairCovering
#print Aris4Math.PropertyB
#check Aris4Math.ThirtyThree.twenty_one_propertyB
#print axioms Aris4Math.ThirtyThree.twenty_one_propertyB
#print axioms Aris4Math.ThirtyThree.TwentyOneTriples.propertyB_of_triple_data
#print axioms Aris4Math.ThirtyThree.TwentyOneDeletion.realized_threshold_deduction
#print axioms Aris4Math.propertyB_of_at_most_thirty_two

/-- The actual 21-vertex reduced branch, restated without a profile, type table,
finite-case membership, probability inequality, or prescribed lock data. -/
theorem twenty_one_original_branch
    (E : Finset (Finset (Fin 21)))
    (hfive : ∀ e ∈ E, e.card = 5) (hcard : E.card = 33)
    (hcover : ∀ x y : Fin 21, x ≠ y → ∃ e ∈ E, x ∈ e ∧ y ∈ e) :
    ∃ c : Fin 21 → Bool, ∀ e ∈ E,
      1 ≤ (e.filter (fun x => c x = true)).card ∧
      (e.filter (fun x => c x = true)).card ≤ 4 :=
  Aris4Math.ThirtyThree.twenty_one_propertyB ⟨E,hfive⟩ hcover hcard

#print axioms twenty_one_original_branch
example : Aris4Math.Target := Aris4Math.propertyB_of_at_most_thirty_two
