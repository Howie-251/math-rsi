import Aris4Math.ThirtyThree.Nineteen

#print Aris4Math.Simple5Hypergraph
#print Aris4Math.PropertyB
#check Aris4Math.ThirtyThree.Nineteen.nineteen_propertyB
#print axioms Aris4Math.ThirtyThree.Nineteen.nineteen_sum_value
#print axioms Aris4Math.ThirtyThree.Nineteen.nineteen_propertyB

/-- Independently restated nineteen-point branch: arbitrary distinct five-element
edges and at most 33 edges, with no point-covering or profile assumptions. -/
theorem nineteen_original_statement
    (E : Finset (Finset (Fin 19)))
    (hfive : ∀ e ∈ E, e.card = 5) (hcard : E.card ≤ 33) :
    ∃ c : Fin 19 → Bool, ∀ e ∈ E,
      1 ≤ (e.filter (fun x => c x = true)).card ∧
      (e.filter (fun x => c x = true)).card ≤ 4 :=
  Aris4Math.ThirtyThree.Nineteen.nineteen_propertyB ⟨E, hfive⟩ hcard

#print axioms nineteen_original_statement
