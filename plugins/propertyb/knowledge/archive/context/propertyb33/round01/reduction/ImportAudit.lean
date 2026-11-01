import Aris4Math.ThirtyThree.Reduction

/- Independent consumer of the new reduction module. -/

#print Aris4Math.Target33
#print Aris4Math.ThirtyThree.FiniteGoal
#check Aris4Math.ThirtyThree.exists_nineteen_to_twenty_five_counterexample
#check Aris4Math.ThirtyThree.propertyB_of_vertices_le_eighteen
#check Aris4Math.ThirtyThree.card_le_twenty_five
#print axioms Aris4Math.ThirtyThree.exists_nineteen_to_twenty_five_counterexample
#print axioms Aris4Math.ThirtyThree.target_of_finite_goal
#print axioms Aris4Math.ThirtyThree.target_iff_finite_goal

universe u

example
    (cases : ∀ n : ℕ, 19 ≤ n → n ≤ 25 →
      ∀ H : Aris4Math.Simple5Hypergraph (Fin n),
        H.edges.card = 33 → H.PairCovering → Aris4Math.PropertyB H)
    (V : Type u) [Fintype V] (H : Aris4Math.Simple5Hypergraph V)
    (edges : H.edges.card ≤ 33) :
    ∃ color : V → Bool, ∀ edge ∈ H.edges,
      1 ≤ (edge.filter (fun x => color x = true)).card ∧
      (edge.filter (fun x => color x = true)).card ≤ 4 :=
  Aris4Math.ThirtyThree.target_of_finite_goal cases V H edges

example (n : ℕ) (H : Aris4Math.Simple5Hypergraph (Fin n))
    (vertices : n ≤ 18) (edges : H.edges.card ≤ 33) :
    Aris4Math.PropertyB H :=
  Aris4Math.ThirtyThree.propertyB_of_vertices_le_eighteen vertices H edges
