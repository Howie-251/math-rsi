import DegreeDiameter.Portfolio.H9CrossKernel
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Finite.Card

namespace DegreeDiameter.Portfolio.H9CrossStar
open H9CrossRouting H9CrossKernel
variable {K : Type*} [Field K] [Finite K]

/-- This finite cardinal bound uses the proved coordinate injection, not rank. -/
theorem kernel_card_le (p : Vec7 K) (hp : p ≠ 0) (hn : norm p = 0) :
    Nat.card (Kernel p) ≤ Nat.card K ^ 3 := by
  classical
  letI : Fintype K := Fintype.ofFinite K
  letI : Fintype (Kernel p) := Fintype.ofFinite (Kernel p)
  obtain ⟨f, hf⟩ := null_kernel_injects_three p hp hn
  simpa only [Nat.card_eq_fintype_card, Fintype.card_fun, Fintype.card_fin]
    using Fintype.card_le_of_injective f hf

/-- The 729 distinct star vectors exhaust the cross kernel over a field of order 9.
The concrete 91 projective points times eight nonzero scalars plus zero still
need to be bound to an actual injective input s. -/
theorem star729_surjective (hK : Nat.card K = 9)
    (p : Vec7 K) (hp : p ≠ 0) (hn : norm p = 0)
    (s : Fin 729 → Kernel p) (hs : Function.Injective s) :
    Function.Surjective s := by
  classical
  letI : Fintype K := Fintype.ofFinite K
  letI : Fintype (Kernel p) := Fintype.ofFinite (Kernel p)
  have hu : Fintype.card (Kernel p) ≤ 729 := by
    have h := kernel_card_le p hp hn
    rw [hK] at h
    simpa only [Nat.card_eq_fintype_card] using h
  by_contra hnotsurj
  have hl : 729 < Fintype.card (Kernel p) := by
    simpa only [Fintype.card_fin] using
      Fintype.card_lt_of_injective_not_surjective s hs hnotsurj
  exact (not_lt_of_ge hu) hl

end DegreeDiameter.Portfolio.H9CrossStar

#print axioms DegreeDiameter.Portfolio.H9CrossStar.kernel_card_le
#print axioms DegreeDiameter.Portfolio.H9CrossStar.star729_surjective
