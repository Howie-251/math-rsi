import Aris4Math.ThirtyFour.TwentyOneSevenTriple788Numeric
namespace Aris4Math.ThirtyFour.TwentyOneSevenTriple788
open TwentyOneSevenTriple788Data TwentyOneSevenTriple788Numeric
open Aris4Math.ThirtyThree.MultiLockRecovery (count)

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 21)) (vertices : Fin 3 ↪ Fin 21)
    (i : Case) (counts : ∀ T, count H vertices T=μ i T) : PropertyB H := by
  obtain ⟨valid,nocap,centers,nonneg,avoids,quotas,deduction,strict⟩ := certificates i
  have real : Aris4Math.TypeCounting.RealizesProfile H vertices (positions i) (p i) 34 := by
    rw [p_eq]
    apply LocalProfiles.realizes H vertices (positions i) labels labels_nodup mem_labels (μ i) counts
    rw [← p_eq]; exact valid
  exact SingleLayoutApplication.propertyB_of_single_layout H vertices (positions i) (p i) real
    nocap centers (R i) (α i) (quota i) (loss i) nonneg avoids quotas deduction strict

theorem propertyB_of_data (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (vertices : Fin 3 ↪ Fin 21) (i : Case)
    (hd : ∀ j, H.degree (vertices j)=degree j)
    (ha : H.codegree (vertices 0) (vertices 1)=co i 0)
    (hb : H.codegree (vertices 0) (vertices 2)=co i 1)
    (hc : H.codegree (vertices 1) (vertices 2)=co i 2)
    (ht : Aris4Math.ThirtyThree.TripleProfiles.tripleCodegree H (vertices 0) (vertices 1) (vertices 2)=triple i) : PropertyB H := by
  apply propertyB_of_counts H vertices i
  intro T
  rw [μ_eq_recovered]
  change Aris4Math.ThirtyThree.TripleProfiles.count H vertices T=_
  rw [Aris4Math.ThirtyThree.TripleProfiles.actual_recovered,
    Aris4Math.ThirtyThree.TripleProfiles.triple_count_eq,size,hd 0,hd 1,hd 2,ha,hb,hc,ht]
end Aris4Math.ThirtyFour.TwentyOneSevenTriple788
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenTriple788.propertyB_of_counts
