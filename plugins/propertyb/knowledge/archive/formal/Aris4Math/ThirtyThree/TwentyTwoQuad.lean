import Aris4Math.ThirtyThree.TwentyTwoQuadData

namespace Aris4Math.ThirtyThree.TwentyTwoQuad

open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.QuadProfiles Aris4Math.ThirtyThree.TwentyTwoQuadData
open Aris4Math.ThirtyThree.PureLink

theorem propertyB_of_data (H : Simple5Hypergraph (Fin 22))
    (cover : H.PairCovering) (edges33 : H.edges.card=33)
    (vertices : Fin 4 ↪ Fin 22) (i : Fin 20)
    (hd : ∀ j,H.degree (vertices j)=7)
    (hc : ∀ a : Fin 6,H.codegree (vertices (first a)) (vertices (second a))=co (kindOf i) a)
    (hh : ∀ a : Fin 5,count H vertices (highLabels a)=high i a) : PropertyB H := by
  obtain ⟨hv,hs,hbounds⟩ := certificates i
  have hm : ∀ T,count H vertices T=counts i T := by
    intro T
    rw [actual_recovered,edges33]
    simp only [hd,hc,hh,counts]
  have real : RealizesProfile H vertices (positions i) (p i) 33 := by
    rw [p_eq] at hv ⊢
    exact realizes_profile H vertices (positions i) (counts i) hm _ hv
  apply CustomDeletion.propertyB_of_custom_deletion H vertices (positions i) (p i) real rfl (loss i)
  · intro j _
    obtain ⟨hcn,hdn,hfinite⟩ := hbounds j
    apply TwentyTwoPureDeletion.realized_dual_deduction H cover vertices (positions i) (p i)
      real j _ 3 ((4*counts i {j}+2-18)/3) (counts i {j}) (c i j) (d i j) _ rfl
    · simp [hd]
    · exact hm {j}
    · exact le_rfl
    · exact hcn
    · exact hdn
    · exact hfinite
  · intro k hk
    have hne : ∀ j : Fin 4,k ≠ (positions i j).val+1 := by
      intro j heq
      apply hk
      rw [heq]
      change _ ∈ List.ofFn (fun j => (positions i j).val+1)
      exact List.mem_ofFn.mpr ⟨j,rfl⟩
    simp only [loss,if_neg (hne 0),if_neg (hne 1),if_neg (hne 2),if_neg (hne 3)]
  · exact hs

end Aris4Math.ThirtyThree.TwentyTwoQuad

#print axioms Aris4Math.ThirtyThree.TwentyTwoQuad.propertyB_of_data
