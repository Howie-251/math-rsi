import Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictBlock4Numeric
namespace Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictBlock4
open TwentyThreeTwoLowFiveStrictBlock4Data TwentyThreeTwoLowFiveStrictBlock4Numeric
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
end Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictBlock4
#print axioms Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictBlock4.propertyB_of_counts
