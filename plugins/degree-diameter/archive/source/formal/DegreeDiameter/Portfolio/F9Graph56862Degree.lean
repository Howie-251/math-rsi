import DegreeDiameter.Portfolio.F9Graph56862Routes
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_ports_injective : ∀ (a : Fin 78) (p q : Fin 6),
    controller a p = controller a q → p = q := by decide +kernel
theorem direction_noise_injective : ∀ (p : Fin 6) (s t : F),
    s • direction p = t • direction p → s = t := by decide +kernel
theorem forward_parameters_injective (u : Fin 56862) :
    Function.Injective (fun pt : Fin 6 × F => forward u pt.1 pt.2) := by
  rintro ⟨p,t⟩ ⟨q,s⟩ h
  have hp := congrArg controllerOf h
  simp only [forward,controllerOf_liftAt] at hp
  have hpq := controller_ports_injective (controllerOf u) p q hp
  cases hpq
  have hf := congrArg (fun v => decodeVec (fiberOf v)) h
  simp only [forward,fiberOf_liftAt,fiberStep,decodeVec_encodeVec,stepVec] at hf
  exact Prod.ext rfl (direction_noise_injective (inversePort p) t s (add_left_cancel hf))
theorem degree_fifty_four (u : Fin 56862) : graph.degree u = 54 := by
  rw [← SimpleGraph.card_neighborFinset_eq_degree,neighborFinset_eq_forward,
    Finset.card_image_of_injective _ (forward_parameters_injective u)]
  decide
#print axioms degree_fifty_four
end DegreeDiameter.Portfolio.F9Graph56862
