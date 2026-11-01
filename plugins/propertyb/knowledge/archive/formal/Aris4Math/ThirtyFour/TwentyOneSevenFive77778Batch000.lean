import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch000Numeric
namespace Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch000
open TwentyOneSevenFive77778Batch000Data TwentyOneSevenFive77778Batch000Numeric
open Aris4Math.ThirtyThree.MultiLockRecovery (count)

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 21)) (vertices : Fin 5 ↪ Fin 21)
    (i : Case) (counts : ∀ T, count H vertices T=μ i T) : PropertyB H := by
  obtain ⟨valid,nocap,centers,nonneg,avoids,quotas,deduction,strict⟩ := certificates i
  have real : Aris4Math.TypeCounting.RealizesProfile H vertices (positions i) (p i) 34 := by
    rw [p_eq]
    apply LocalProfiles.realizes H vertices (positions i) labels labels_nodup mem_labels (μ i) counts
    rw [← p_eq]; exact valid
  exact SingleLayoutApplication.propertyB_of_single_layout H vertices (positions i) (p i) real
    nocap centers (R i) (α i) (quota i) (loss i) nonneg avoids quotas deduction strict

theorem propertyB_of_low_high (H : Simple5Hypergraph (Fin 21))
    (vertices : Fin 5 ↪ Fin 21) (i : Case)
    (low : ∀ T,T.card≤2→Aris4Math.ThirtyThree.MultiLockRecovery.upperCount H vertices T=upper i T)
    (high : ∀ T,3≤T.card→count H vertices T=μ i T) : PropertyB H := by
  apply propertyB_of_counts H vertices i
  intro T
  rw [μ_eq_recovered]
  exact Aris4Math.ThirtyThree.MultiLockRecovery.actual_recovered H vertices (upper i) (μ i) low high T
end Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch000
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch000.propertyB_of_counts
