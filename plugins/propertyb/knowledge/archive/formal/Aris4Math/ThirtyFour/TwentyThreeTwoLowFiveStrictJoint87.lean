import Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictJoint87Numeric
namespace Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictJoint87
open TwentyThreeTwoLowFiveStrictJoint87Data TwentyThreeTwoLowFiveStrictJoint87Numeric
open Aris4Math.ThirtyThree.MultiLockRecovery (count)
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (counts : ∀ T, count H vertices T=μ T) : PropertyB H := by
  obtain ⟨covers,valid,nocap,centers,gn,mass,bn,bg,dn,avoids,quota_valid⟩ := data_valid
  have real (l) : Aris4Math.TypeCounting.RealizesProfile H vertices (positions l) (p l) 34 := by
    rw [p_eq]
    apply LocalProfiles.realizes H vertices (positions l) labels labels_nodup mem_labels μ counts
    rw [← p_eq]
    exact valid l
  exact MixedLayoutApplication.propertyB_of_mixed_layouts H vertices support μ counts covers
    positions p real nocap centers gamma beta R delta quota gn mass bn bg dn avoids quota_valid strict
end Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictJoint87
#print axioms Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictJoint87.propertyB_of_counts
