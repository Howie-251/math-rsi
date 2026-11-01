import Aris4Math.ThirtyFour.TwentyThreeTraceShape

namespace Aris4Math.ThirtyFour.TwentyThreeSixLowClassifiedProbe
abbrev Residue := Fin 1
def residualCounts (_ : Residue) : Finset (Fin 6) → ℕ := fun T => if T=∅ then 11 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else 0
end Aris4Math.ThirtyFour.TwentyThreeSixLowClassifiedProbe

/-! Complete ≥7 degree-six branch at 23 vertices. All local classifications
are internally derived from the original H; the final contradiction counts
original edges across seven deletions, preserving trace multiplicity. -/
namespace Aris4Math.ThirtyFour.TwentyThreeManyLowComplete
open scoped BigOperators
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery
open TwentyThreeSevenLowCounting

private theorem residue_small : ∀ r : TwentyThreeSixLowClassifiedProbe.Residue,
    ∀ T : Finset (Fin 6), 0 < TwentyThreeSixLowClassifiedProbe.residualCounts r T → T.card≤3 := by
  decide +kernel

private theorem residue_triples : ∀ r : TwentyThreeSixLowClassifiedProbe.Residue,
    (∑ T ∈ Finset.univ.filter (fun T : Finset (Fin 6) => T.card=3),
      TwentyThreeSixLowClassifiedProbe.residualCounts r T)=2 := by decide +kernel

/-- Exact actual counts imply the required original-edge trace statement. -/
theorem shape_of_residue (H : Simple5Hypergraph (Fin 23)) (f : Fin 6 ↪ Fin 23)
    (r : TwentyThreeSixLowClassifiedProbe.Residue)
    (actual : ∀ T, count H f T=TwentyThreeSixLowClassifiedProbe.residualCounts r T) :
    TwoTripleTraceShape H (Finset.univ.image f) :=
  TwentyThreeTraceShape.shape_of_counts H f _ (residue_small r) (residue_triples r) actual

variable (checkedClassifier : ∀ (H : Simple5Hypergraph (Fin 23)), H.PairCovering →
    H.edges.card=34 → ∀ (f : Fin 6 ↪ Fin 23),
    (∀ i, H.degree (f i)=6) → ¬ PropertyB H →
    ∃ r : TwentyThreeSixLowClassifiedProbe.Residue, ∃ σ : Equiv.Perm (Fin 6),
      ∀ T, count H (σ.toEmbedding.trans f) T=TwentyThreeSixLowClassifiedProbe.residualCounts r T)
include checkedClassifier

/-- All six-subsets of the actual low vertex set have the unique residual
shape if H is noncolorable. The finite local domain is no longer a premise. -/
theorem six_subset_shape (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (notB : ¬ PropertyB H)
    (S : Finset (Fin 23)) (sub : S ⊆ H.sixVertices) (six : S.card=6) :
    TwoTripleTraceShape H S := by
  let equiv : ↥S ≃ Fin 6 := Fintype.equivFinOfCardEq (by simpa using six)
  let f : Fin 6 ↪ Fin 23 :=
    ⟨fun i => (equiv.symm i).val,Subtype.val_injective.comp equiv.symm.injective⟩
  have inside (i : Fin 6) : f i ∈ S := (equiv.symm i).property
  have degrees (i : Fin 6) : H.degree (f i)=6 :=
    (Finset.mem_filter.mp (sub (inside i))).2
  obtain ⟨r,σ,actual⟩ := checkedClassifier H cover edges f degrees notB
  let g := σ.toEmbedding.trans f
  have range : Finset.univ.image g = S := by
    apply Finset.eq_of_subset_of_card_le
    · intro x hx
      obtain ⟨i,_,rfl⟩ := Finset.mem_image.mp hx
      exact inside (σ i)
    · rw [Finset.card_image_of_injective _ g.injective,six]
      simp
  rw [← range]
  exact shape_of_residue H g r actual

/-- No certificate or classifier hypothesis is left in the actual branch. -/
theorem propertyB (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (many : 7 ≤ H.sixVertices.card) : PropertyB H := by
  apply propertyB_of_six_low_classification H many
  intro notB S sub six
  exact six_subset_shape checkedClassifier H cover edges notB S sub six

end Aris4Math.ThirtyFour.TwentyThreeManyLowComplete
#print axioms Aris4Math.ThirtyFour.TwentyThreeManyLowComplete.propertyB
