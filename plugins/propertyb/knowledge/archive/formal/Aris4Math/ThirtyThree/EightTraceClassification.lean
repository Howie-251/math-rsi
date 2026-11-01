import Aris4Math.ThirtyThree.EightClassification
import Aris4Math.TraceRecovery

/-! Apply the complete eight-point classification to actual hypergraph traces.
The final family includes every pair block, recovered from unit codegrees. -/

namespace Aris4Math.ThirtyThree.EightTraceClassification

open Aris4Math.TraceRecovery Aris4Math.BlockClassification
open Aris4Math.K6Classification
open Aris4Math.ThirtyThree.EightClassification

variable {V : Type*} [DecidableEq V]

theorem labelBlock_trans (S : Finset V) (label : ↥S ≃ Fin 8)
    (e : Fin 8 ≃ Fin 8) (B : Finset V) :
    labelBlock S (label.trans e) B = (labelBlock S label B).map e.toEmbedding := by
  ext i
  simp only [mem_labelBlock, Finset.mem_map_equiv]
  rfl

/-- Classify the actual subsets, retaining a concrete label equivalence with
domain exactly the chosen eight vertices. -/
theorem classify_on_set (S : Finset V) (T : Finset (Finset V))
    (eight : S.card = 8) (inside : ∀ B ∈ T, B ⊆ S)
    (three : ∀ B ∈ T, B.card = 3) (linear : Linear T)
    (covers : ∀ x ∈ S, ∃ B ∈ T, x ∈ B) (many : 5 ≤ T.card) :
    ∃ k : Fin 14, ∃ label : ↥S ≃ Fin 8,
      T.image (labelBlock S label) = representative8 k := by
  let label : ↥S ≃ Fin 8 := Fintype.equivOfCardEq (by simpa using eight)
  let U := T.image (labelBlock S label)
  have threeU : ∀ B ∈ U, B.card = 3 := by
    intro B hB
    obtain ⟨C,hC,rfl⟩ := Finset.mem_image.mp hB
    rw [labelBlock_card S label C (inside C hC)]
    exact three C hC
  have linearU : Linear U := by
    intro B hB C hC ne
    obtain ⟨D,hD,rfl⟩ := Finset.mem_image.mp hB
    obtain ⟨E,hE,rfl⟩ := Finset.mem_image.mp hC
    rw [← labelBlock_inter, labelBlock_card S label (D ∩ E)
      (Finset.inter_subset_left.trans (inside D hD))]
    exact linear D hD E hE (fun h => ne (congrArg (labelBlock S label) h))
  have coversU : ∀ i : Fin 8, ∃ B ∈ U, i ∈ B := by
    intro i
    obtain ⟨B,hB,hi⟩ := covers (label.symm i).val (label.symm i).property
    exact ⟨labelBlock S label B, Finset.mem_image.mpr ⟨B,hB,rfl⟩,
      (mem_labelBlock S label B i).mpr hi⟩
  have manyU : 5 ≤ U.card := by
    have eq : U.card = T.card := by
      apply Finset.card_image_of_injOn
      intro B hB C hC h
      exact labelBlock_injective S label (inside B hB) (inside C hC) h
    rw [eq]
    exact many
  obtain ⟨k,e,mapped⟩ := classify_eight U threeU linearU coversU manyU
  refine ⟨k,label.trans e,?_⟩
  rw [show T.image (labelBlock S (label.trans e)) =
      U.image (fun B => B.map e.toEmbedding) by
    dsimp [U]
    rw [Finset.image_image]
    apply Finset.image_congr
    intro B _
    exact labelBlock_trans S label e B]
  exact mapped

/-- Full family recovery from an actual eight-lock set. These are the precise
structural hypotheses supplied by TwentyFiveStructure; no realization or
numeric certificate is assumed. -/
theorem exists_full_labeled_eight (H : Simple5Hypergraph V) (S : Finset V)
    (eight : S.card = 8) (unit : H.UnitCodegrees S)
    (small : ∀ B ∈ H.multiTraces S, B.card ≤ 3)
    (many : 5 ≤ ((H.multiTraces S).filter fun B => B.card = 3).card)
    (covers : ∀ x ∈ S, ∃ B ∈ H.multiTraces S, B.card = 3 ∧ x ∈ B) :
    ∃ k : Fin 14, ∃ label : ↥S ≃ Fin 8,
      (H.multiTraces S).image (labelBlock S label) = pairCompletion (representative8 k) := by
  let T := (H.multiTraces S).filter fun B => B.card = 3
  have inside : ∀ B ∈ T, B ⊆ S := by
    intro B hB
    exact H.multiTraces_subset S (Finset.mem_filter.mp hB).1
  have three : ∀ B ∈ T, B.card = 3 := by
    intro B hB
    exact (Finset.mem_filter.mp hB).2
  have linear : Linear T := by
    intro B hB C hC ne
    exact H.multiTraces_inter_card_le_one S unit
      (Finset.mem_filter.mp hB).1 (Finset.mem_filter.mp hC).1 ne
  have covered : ∀ x ∈ S, ∃ B ∈ T, x ∈ B := by
    intro x hx
    obtain ⟨B,hB,three,hxB⟩ := covers x hx
    exact ⟨B,Finset.mem_filter.mpr ⟨hB,three⟩,hxB⟩
  obtain ⟨k,label,mapped⟩ := classify_on_set S T eight inside three linear covered many
  have large_eq : largeBlocks (H.multiTraces S) = T := by
    apply Finset.filter_congr
    intro B hB
    have upper := small B hB
    omega
  refine ⟨k,label,?_⟩
  rw [labeled_traces_recovered H S unit label, large_eq, mapped]

end Aris4Math.ThirtyThree.EightTraceClassification

#print axioms Aris4Math.ThirtyThree.EightTraceClassification.exists_full_labeled_eight
