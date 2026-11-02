import DegreeDiameter.Portfolio.F9Graph56862Routes
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 10000
set_option maxHeartbeats 20000000
theorem zero_ne_target : (0 : Fin 56862) ≠ 729 := by decide

theorem no_controller_one : ∀ p : Fin 6, controller 0 p ≠ 1 := by decide +kernel
theorem no_controller_two : ∀ p q : Fin 6, controller (controller 0 p) q ≠ 1 := by decide +kernel
theorem no_one_step_zero_target : ∀ (p : Fin 6) (t : F), forward 0 p t ≠ 729 := by
  intro p t h
  have hc := congrArg controllerOf h
  simp only [forward,controllerOf_liftAt] at hc
  exact no_controller_one p hc
theorem no_two_steps_zero_target : ∀ (p q : Fin 6) (t s : F),
    forward (forward 0 p t) q s ≠ 729 := by
  intro p q t s h
  have hc := congrArg controllerOf h
  simp only [forward,controllerOf_liftAt] at hc
  exact no_controller_two p q hc

theorem not_diameterAtMost_two : ¬ DiameterAtMost graph 2 := by
  intro h
  obtain ⟨w, hw⟩ := h 0 729
  obtain ⟨z, hfirst, tail, heq⟩ := SimpleGraph.Walk.exists_eq_cons_of_ne zero_ne_target w
  rw [heq] at hw
  change tail.length + 1 ≤ 2 at hw
  obtain ⟨p, t, h1⟩ := (adj_iff_forward 0 z).mp hfirst
  by_cases hzero : tail.length = 0
  · have hz : z = 729 := SimpleGraph.Walk.eq_of_length_eq_zero hzero
    exact no_one_step_zero_target p t (h1.trans hz)
  · have hone : tail.length = 1 := by omega
    have hadj : graph.Adj z 729 := SimpleGraph.Walk.adj_of_length_eq_one hone
    obtain ⟨q, s, h2⟩ := (adj_iff_forward z 729).mp hadj
    apply no_two_steps_zero_target p q t s
    rw [h1]
    exact h2


#print axioms not_diameterAtMost_two
end DegreeDiameter.Portfolio.F9Graph56862
