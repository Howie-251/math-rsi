import Aris4Math.ThirtyFour.TwentyOneFiveQuadNumeric
import Aris4Math.ThirtyThree.TwentyTwoQuadAssembly

namespace Aris4Math.ThirtyFour.TwentyOneFiveQuad
set_option maxRecDepth 100000
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.ThirtyThree.TripleProfiles (table_pruneZero pruneZero)
open Aris4Math.ThirtyThree.RefinedDeletion
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (highPairSum high_inventory count_le_codegree)
open Aris4Math.ThirtyFour.TwentyOneFiveQuadData

theorem realizes34 (H : Simple5Hypergraph (Fin 21)) (vertices : Fin 4 ↪ Fin 21)
    (i : Case) (hμ : ∀ T, count H vertices T = μ i T)
    (valid : Numeric.validProfile (p i) 34) :
    RealizesProfile H vertices (positions i) (p i) 34 := by
  rw [p_eq] at valid ⊢
  refine ⟨rfl,valid,?_,table_pruneZero _ _ _ (raw_table H vertices (positions i) (μ i) hμ _)⟩
  simp [profile,pruneZero,rawProfile,canonicalType]

theorem propertyB_of_data (H : Simple5Hypergraph (Fin 21))
    (edges34 : H.edges.card=34) (vertices : Fin 4 ↪ Fin 21) (i : Case)
    (hd : ∀ j, H.degree (vertices j) = degree i j)
    (hc : ∀ j, H.codegree (vertices (first j)) (vertices (second j)) = coData i j)
    (ht : ∀ a, count H vertices (highLabels a) = highData i a) : PropertyB H := by
  obtain ⟨valid,strict,bounds⟩ := TwentyOneFiveQuadNumeric.certificates i
  have hm : ∀ T, count H vertices T = μ i T := by
    intro T
    rw [actual_recovered,edges34]
    rw [show (fun j => H.degree (vertices j)) = degree i from funext hd,
      show (fun j => H.codegree (vertices (first j)) (vertices (second j))) = coData i from funext hc,
      show (fun j => count H vertices (highLabels j)) = highData i from funext ht]
    rfl
  have real := realizes34 H vertices i hm valid
  apply ThirtyThree.CustomDeletion.propertyB_of_custom_deletion H vertices (positions i) (p i) real rfl (loss i)
  · intro j _
    obtain ⟨lossEq,nonneg,avoids,quotas,bound⟩ := bounds j
    rw [lossEq]
    exact realized_refined_deduction H vertices (positions i) (p i) real j
      (avoid i j) (alpha i j) (quota i j) (lossAt i j) nonneg avoids quotas bound
  · intro k hk
    have absent : ∀ j : Fin 4, k ≠ (positions i j).val+1 := by
      intro j he
      apply hk
      simp only [p,pruneZero]
      exact List.mem_ofFn.mpr ⟨j,he.symm⟩
    simp [loss,absent 0,absent 1,absent 2,absent 3]
  · exact strict

end Aris4Math.ThirtyFour.TwentyOneFiveQuad
