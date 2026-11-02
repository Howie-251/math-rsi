import DegreeDiameter.Portfolio.F5Graph3750Diameter

namespace DegreeDiameter.Portfolio.F5Graph3750
set_option maxRecDepth 10000
set_option maxHeartbeats 20000000

theorem zero_ne_six : (0 : Fin 3750) ≠ 6 := by decide

theorem no_one_step_zero_six : ∀ (p : Fin 4) (t : Fin 5), forward 0 p t ≠ 6 := by decide

/-- Only 4*4*5*5=400 two-edge generated routes; no intermediate-vertex sweep. -/
theorem no_two_steps_zero_six : ∀ (p q : Fin 4) (t s : Fin 5),
    forward (forward 0 p t) q s ≠ 6 := by decide

theorem not_diameterAtMost_two : ¬ DiameterAtMost graph 2 := by
  intro h
  obtain ⟨w, hw⟩ := h 0 6
  obtain ⟨z, hfirst, tail, heq⟩ := SimpleGraph.Walk.exists_eq_cons_of_ne zero_ne_six w
  rw [heq] at hw
  change tail.length + 1 ≤ 2 at hw
  obtain ⟨p, t, h1⟩ := (adj_iff_forward 0 z).mp hfirst
  by_cases hzero : tail.length = 0
  · have hz : z = 6 := SimpleGraph.Walk.eq_of_length_eq_zero hzero
    exact no_one_step_zero_six p t (h1.trans hz)
  · have hone : tail.length = 1 := by omega
    have hadj : graph.Adj z 6 := SimpleGraph.Walk.adj_of_length_eq_one hone
    obtain ⟨q, s, h2⟩ := (adj_iff_forward z 6).mp hadj
    apply no_two_steps_zero_six p q t s
    rw [h1]
    exact h2

theorem concrete_order_degree_and_D3 :
    Fintype.card (Fin 3750) = 3750 ∧
      (∀ u, graph.degree u ≤ 20) ∧ DiameterAtMost graph 3 := by
  exact ⟨Fintype.card_fin _, degree_le_twenty, diameterAtMost_three⟩

theorem diameter_exact_three_in_project_definition :
    DiameterAtMost graph 3 ∧ ¬ DiameterAtMost graph 2 :=
  ⟨diameterAtMost_three, not_diameterAtMost_two⟩

#print axioms concrete_order_degree_and_D3
#print axioms diameter_exact_three_in_project_definition
end DegreeDiameter.Portfolio.F5Graph3750
