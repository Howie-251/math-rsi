import DegreeDiameter.Portfolio.F3Graph15552FullDegree

namespace DegreeDiameter.Portfolio.F3Graph15552
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000

/-- Type0 can pad any shorter word at the initial controller0. -/
theorem lower_controller_zero_type_zero : controller 0 0 = 0 := rfl

/-- The sole new finite obstruction: the 125 three-type words omit1. -/
theorem lower_no_controller_three : ∀ p q r : Fin 5,
    controller (controller (controller 0 p) q) r ≠ (1 : Fin 192) := by decide +kernel

theorem lower_no_controller_one (p : Fin 5) :
    controller 0 p ≠ (1 : Fin 192) := by
  simpa only [lower_controller_zero_type_zero] using lower_no_controller_three 0 0 p

theorem lower_no_controller_two (p q : Fin 5) :
    controller (controller 0 p) q ≠ (1 : Fin 192) := by
  simpa only [lower_controller_zero_type_zero] using lower_no_controller_three 0 p q

/-- Noise is arbitrary: only the controller projection is used. -/
theorem lower_no_one_step_zero_81 (p : Fin 5) (t : F) :
    forward 0 p t ≠ 81 := by
  intro h
  have hc := congrArg controllerOf h
  simp only [forward,controllerOf_liftAt] at hc
  change controller 0 p = (1 : Fin 192) at hc
  exact lower_no_controller_one p hc

theorem lower_no_two_steps_zero_81 (p q : Fin 5) (t s : F) :
    forward (forward 0 p t) q s ≠ 81 := by
  intro h
  have hc := congrArg controllerOf h
  simp only [forward,controllerOf_liftAt] at hc
  change controller (controller 0 p) q = (1 : Fin 192) at hc
  exact lower_no_controller_two p q hc

theorem lower_no_three_steps_zero_81 (p q r : Fin 5) (t s a : F) :
    forward (forward (forward 0 p t) q s) r a ≠ 81 := by
  intro h
  have hc := congrArg controllerOf h
  simp only [forward,controllerOf_liftAt] at hc
  change controller (controller (controller 0 p) q) r = (1 : Fin 192) at hc
  exact lower_no_controller_three p q r hc

/-- Concrete old labels0 and81 have no true source walk of length at most3.
The reverse-origin adjacency case is already handled by adj_iff_forward. -/
theorem not_diameterAtMost_three : ¬ DiameterAtMost graph 3 := by
  intro h
  obtain ⟨w,hw⟩ := h 0 81
  have hne : (0 : Fin 15552) ≠ 81 := by decide
  obtain ⟨z,hfirst,tail,heq⟩ := SimpleGraph.Walk.exists_eq_cons_of_ne hne w
  rw [heq] at hw
  change tail.length+1 ≤ 3 at hw
  obtain ⟨_,p,t,h1⟩ := (adj_iff_forward 0 z).mp hfirst
  by_cases hz : z = 81
  · exact lower_no_one_step_zero_81 p t (h1.trans hz)
  · obtain ⟨y,hsecond,last,heq₂⟩ := SimpleGraph.Walk.exists_eq_cons_of_ne hz tail
    rw [heq₂] at hw
    change last.length+1+1 ≤ 3 at hw
    obtain ⟨_,q,s,h2⟩ := (adj_iff_forward z y).mp hsecond
    by_cases hzero : last.length = 0
    · have hy : y = 81 := SimpleGraph.Walk.eq_of_length_eq_zero hzero
      apply lower_no_two_steps_zero_81 p q t s
      rw [h1]
      exact h2.trans hy
    · have hone : last.length = 1 := by omega
      have hadj : graph.Adj y 81 := SimpleGraph.Walk.adj_of_length_eq_one hone
      obtain ⟨_,r,a,h3⟩ := (adj_iff_forward y 81).mp hadj
      apply lower_no_three_steps_zero_81 p q r t s a
      rw [h1,h2]
      exact h3

#print axioms not_diameterAtMost_three
end DegreeDiameter.Portfolio.F3Graph15552
