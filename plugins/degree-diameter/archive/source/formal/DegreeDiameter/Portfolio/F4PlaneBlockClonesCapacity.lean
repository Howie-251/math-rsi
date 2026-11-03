import DegreeDiameter.Portfolio.F4PlaneBlockClonesDefinitions
namespace DegreeDiameter.Portfolio.F4PlaneBlockClones
open F4Graph3840
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

abbrev Allowed {K : Nat} (layers : Fin K → Fin 60) (a : Fin 60) :=
  {b : Fin K // ∃ p : Fin 5, controller a p = layers b}

theorem capacity21 : ∀ a : Fin 60, Fintype.card (Allowed layers21 a) ≤ 1 := by decide +kernel

theorem capacity22 : ∀ a : Fin 60, Fintype.card (Allowed layers22 a) ≤ 2 := by decide +kernel

#print axioms capacity21
#print axioms capacity22
end DegreeDiameter.Portfolio.F4PlaneBlockClones
