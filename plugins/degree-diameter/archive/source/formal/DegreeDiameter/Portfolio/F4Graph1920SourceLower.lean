import DegreeDiameter.Portfolio.F4Graph1920Routes
namespace DegreeDiameter.Portfolio.F4Graph1920
open F4Graph3840
theorem zero_ne_192 : (0 : Fin 1920)≠192 := by decide
theorem no_controller_one : ∀p:Fin 4,controller 0 p≠(3:Fin 30) := by decide +kernel
theorem no_controller_two : ∀p q:Fin 4,controller (controller 0 p) q≠(3:Fin 30) := by decide +kernel
theorem no_one_step_zero_192 : ∀(p:Fin 4)(t:F),forward 0 p t≠192 := by
  intro p t h
  have hc := congrArg controllerOf h
  simp only [forward,controllerOf_liftAt] at hc
  change controller 0 p=(3:Fin 30) at hc
  exact no_controller_one p hc
theorem no_two_steps_zero_192 : ∀(p q:Fin 4)(t s:F),forward (forward 0 p t) q s≠192 := by
  intro p q t s h
  have hc := congrArg controllerOf h
  simp only [forward,controllerOf_liftAt] at hc
  change controller (controller 0 p) q=(3:Fin 30) at hc
  exact no_controller_two p q hc
theorem not_diameterAtMost_two : ¬DiameterAtMost graph 2 := by
  intro h
  obtain ⟨w,hw⟩ := h 0 192
  obtain ⟨z,hfirst,tail,heq⟩ := SimpleGraph.Walk.exists_eq_cons_of_ne zero_ne_192 w
  rw [heq] at hw
  change tail.length+1≤2 at hw
  obtain ⟨p,t,h1⟩ := (adj_iff_forward 0 z).mp hfirst
  by_cases hzero : tail.length=0
  · have hz : z=192 := SimpleGraph.Walk.eq_of_length_eq_zero hzero
    exact no_one_step_zero_192 p t (h1.trans hz)
  · have hone : tail.length=1 := by omega
    have hadj : graph.Adj z 192 := SimpleGraph.Walk.adj_of_length_eq_one hone
    obtain ⟨q,s,h2⟩ := (adj_iff_forward z 192).mp hadj
    apply no_two_steps_zero_192 p q t s
    rw [h1]
    exact h2
#print axioms not_diameterAtMost_two
end DegreeDiameter.Portfolio.F4Graph1920
