import Aris4Math.ThirtyFour.TwentyFiveCoefficientPilot
import Aris4Math.ThirtyFour.CachedIntegerRows
import Aris4Math.ThirtyFour.CachedCoefficients16Scaled

namespace Aris4Math.ThirtyFour.TwentyFiveCoefficientPilotInteger
open scoped BigOperators
open CachedRows CachedIntegerRows TwentyFiveCoefficientPilot
open Aris4Math.ThirtyThree.MultiLockRecovery
set_option maxRecDepth 100000
set_option maxHeartbeats 0

def denominator : ℕ := CachedCoefficients16Scaled.denominator

def aInt (k : Fin 25) (last : Bool) : Fin 6 → ℤ :=
  CachedCoefficients16Scaled.edgeTable
    (CachedCoefficients16.index (locked k) (if last then leftSlots k else rightSlots k))
def cInt (k : Fin 25) : Fin 6 → Fin 6 → ℤ :=
  CachedCoefficients16Scaled.pairTable (CachedCoefficients16.index (locked k) (leftSlots k))

theorem aCoeff_scaled (k : Fin 25) (last : Bool) (r : Fin 6) :
    aCoeff computed (k.val+1) last r = (aInt k last r : ℚ)/denominator := by
  rw [aCoeff_eq]
  exact CachedCoefficients16Scaled.edgeTable_eq _ _
theorem cCoeff_scaled (k : Fin 25) (r q : Fin 6) :
    cCoeff computed (k.val+1) r q = (cInt k r q : ℚ)/denominator := by
  rw [cCoeff_eq]
  exact CachedCoefficients16Scaled.pairTable_eq _ _ _

theorem integer_value : (∑ k : Fin 25,
    min (rowA computed (k.val+1) true (aInt k true))
      (min (rowA computed (k.val+1) false (aInt k false))
        (rowC computed (k.val+1) (cInt k)))) = 20921164185600 := by
  decide +kernel

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (vertices : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H vertices T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H vertices positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,p_eq_computed]
    have nodup : ∀ t ∈ computed.types,t.locks.Nodup := by
      intro t ht
      have valid' := valid
      rw [p_eq_computed] at valid'
      have h := List.all_eq_true.mp valid'.2.2.2.2.1 t ht
      simp only [Bool.and_eq_true,decide_eq_true_eq] at h
      exact h.1.1.1.1.1
    simp_rw [cachedA_scaled computed _ _ _ (denominator : ℚ) (aCoeff_scaled _ _),
      cachedC_scaled computed _ _ (denominator : ℚ) nodup (cCoeff_scaled _)]
    apply strict_of_integer _ _ _ denominator (by decide +kernel)
    rw [integer_value]
    decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveCoefficientPilotInteger
#print axioms Aris4Math.ThirtyFour.TwentyFiveCoefficientPilotInteger.propertyB_of_counts
