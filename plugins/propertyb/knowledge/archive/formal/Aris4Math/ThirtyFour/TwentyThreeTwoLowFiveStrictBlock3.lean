import Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictBlock3Numeric
namespace Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictBlock3
open TwentyThreeTwoLowFiveStrictBlock3Data TwentyThreeTwoLowFiveStrictBlock3Numeric
open Aris4Math.ThirtyThree.MultiLockRecovery (count)
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (i : Case) (counts : ∀ T, count H vertices T=μ i T) : PropertyB H := by
  obtain ⟨valid,nocap,centers,nonneg,avoids,quotas,deduction,strict⟩ := certificates i
  have real : Aris4Math.TypeCounting.RealizesProfile H vertices (positions i) (p i) 34 := by
    rw [p_eq]
    apply LocalProfiles.realizes H vertices (positions i) labels labels_nodup mem_labels (μ i) counts
    rw [← p_eq]; exact valid
  exact SingleLayoutApplication.propertyB_of_single_layout H vertices (positions i) (p i) real
    nocap centers (R i) (α i) (quota i) (loss i) nonneg avoids quotas deduction strict
end Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictBlock3
#print axioms Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictBlock3.propertyB_of_counts
