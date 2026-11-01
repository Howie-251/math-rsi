import Aris4Math.ThirtyFour.TwentyThreeTwoLowFourNumeric
namespace Aris4Math.ThirtyFour.TwentyThreeTwoLowFour
open TwentyThreeTwoLowFourData TwentyThreeTwoLowFourNumeric
open Aris4Math.ThirtyThree.MultiLockRecovery (count)
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 4 ↪ Fin 23)
    (i : Case) (counts : ∀ T, count H vertices T=μ i T) : PropertyB H := by
  obtain ⟨valid,nocap,centers,nonneg,avoids,quotas,deduction,strict⟩ := certificates i
  have real : Aris4Math.TypeCounting.RealizesProfile H vertices (positions i) (p i) 34 := by
    rw [p_eq]
    apply LocalProfiles.realizes H vertices (positions i) labels labels_nodup mem_labels (μ i) counts
    rw [← p_eq]; exact valid
  exact SingleLayoutApplication.propertyB_of_single_layout H vertices (positions i) (p i) real
    nocap centers (R i) (α i) (quota i) (loss i) nonneg avoids quotas deduction strict
theorem propertyB_of_data (H : Simple5Hypergraph (Fin 23)) (size : H.edges.card=34)
    (vertices : Fin 4 ↪ Fin 23) (i : Case)
    (hd : ∀ j, H.degree (vertices j)=degree j)
    (hc : ∀ j, H.codegree (vertices (Aris4Math.ThirtyThree.QuadProfiles.first j))
      (vertices (Aris4Math.ThirtyThree.QuadProfiles.second j))=co i j)
    (ht : ∀ j, count H vertices (Aris4Math.ThirtyThree.QuadProfiles.highLabels j)=high i j) : PropertyB H := by
  apply propertyB_of_counts H vertices i
  intro T
  rw [μ_eq_recovered]
  change Aris4Math.ThirtyThree.QuadProfiles.count H vertices T=_
  rw [Aris4Math.ThirtyThree.QuadProfiles.actual_recovered,size]
  rw [show (fun j=>H.degree (vertices j))=degree from funext hd,
    show (fun j=>H.codegree (vertices (Aris4Math.ThirtyThree.QuadProfiles.first j))
      (vertices (Aris4Math.ThirtyThree.QuadProfiles.second j)))=co i from funext hc,
    show (fun j=>Aris4Math.ThirtyThree.QuadProfiles.count H vertices (Aris4Math.ThirtyThree.QuadProfiles.highLabels j))=high i from funext ht]
end Aris4Math.ThirtyFour.TwentyThreeTwoLowFour
#print axioms Aris4Math.ThirtyFour.TwentyThreeTwoLowFour.propertyB_of_counts
#print axioms Aris4Math.ThirtyFour.TwentyThreeTwoLowFour.propertyB_of_data
