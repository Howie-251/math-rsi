import DegreeDiameter.Portfolio.F4PlaneBlockClonesFamily
namespace DegreeDiameter.Portfolio.F4PlaneBlockLoadSum23
open F4Graph3840 F4PlaneBlockClones
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

/-- Fixed arithmetic combination r21+r22; preparation only until public execution notice. -/
def layers23 : Fin 31 → Fin 60 := ![1, 4, 11, 14, 18, 20, 22, 22, 23, 24, 25, 29, 31, 32, 33, 34, 35, 40, 43, 45, 46, 47, 48, 49, 50, 54, 56, 56, 57, 58, 59]

theorem capacity23 : ∀ a : Fin 60, Fintype.card (Allowed layers23 a) ≤ 3 := by decide +kernel
#print axioms capacity23
end DegreeDiameter.Portfolio.F4PlaneBlockLoadSum23
