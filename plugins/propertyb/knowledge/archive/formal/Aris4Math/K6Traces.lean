import Aris4Math.K6Classification
import Aris4Math.Traces

/-! Transport the analytic six-point classification to actual lock traces.
The ground set, blocks, and exact-label equivalence are all derived from H.
-/

namespace Aris4Math.K6Traces

open BlockClassification K6Classification

variable {V : Type*} [DecidableEq V]

/-- Regard a block as a subset of its finite ground type. -/
def onGround (W B : Finset V) : Finset ↥W := B.subtype (fun x => x ∈ W)

@[simp] theorem mem_onGround (W B : Finset V) (x : W) :
    x ∈ onGround W B ↔ x.val ∈ B := Finset.mem_subtype

theorem onGround_card (W B : Finset V) (inside : B ⊆ W) :
    (onGround W B).card = B.card := by
  rw [onGround, Finset.card_subtype, Finset.filter_eq_self.mpr inside]

theorem onGround_injective (W : Finset V) {B C : Finset V}
    (hB : B ⊆ W) (hC : C ⊆ W) (same : onGround W B = onGround W C) : B = C := by
  have hb := Finset.subtype_map_of_mem hB
  have hc := Finset.subtype_map_of_mem hC
  exact hb.symm.trans ((congrArg (fun D => D.map (Function.Embedding.subtype (fun x => x ∈ W))) same).trans hc)

theorem onGround_inter (W B C : Finset V) :
    onGround W (B ∩ C) = onGround W B ∩ onGround W C := by
  ext x
  simp

/-- Taking exact size classes commutes with passing to the finite ground type. -/
theorem ground_filter (W : Finset V) (blocks : Finset (Finset V))
    (inside : ∀ B ∈ blocks, B ⊆ W) (p : Nat → Prop) [DecidablePred p] :
    (blocks.image (onGround W)).filter (fun B => p B.card) =
      (blocks.filter (fun B => p B.card)).image (onGround W) := by
  rw [Finset.filter_image]
  congr 1
  apply Finset.filter_congr
  intro B hB
  rw [onGround_card W B (inside B hB)]

/-- Size classes retain their exact count: subtype transport does not merge blocks. -/
theorem ground_filter_card (W : Finset V) (blocks : Finset (Finset V))
    (inside : ∀ B ∈ blocks, B ⊆ W) (p : Nat → Prop) [DecidablePred p] :
    ((blocks.image (onGround W)).filter (fun B => p B.card)).card =
      (blocks.filter (fun B => p B.card)).card := by
  rw [ground_filter W blocks inside p]
  apply Finset.card_image_of_injOn
  intro B hB C hC heq
  exact onGround_injective W (inside B (Finset.mem_filter.mp hB).1)
    (inside C (Finset.mem_filter.mp hC).1) heq

theorem ground_linear (W : Finset V) (blocks : Finset (Finset V))
    (inside : ∀ B ∈ blocks, B ⊆ W) (linear : Linear blocks) :
    Linear (blocks.image (onGround W)) := by
  intro D hD E hE hne
  obtain ⟨B, hB, rfl⟩ := Finset.mem_image.mp hD
  obtain ⟨C, hC, rfl⟩ := Finset.mem_image.mp hE
  rw [← onGround_inter, onGround_card W (B ∩ C)
    (Finset.Subset.trans Finset.inter_subset_left (inside B hB))]
  exact linear B hB C hC (fun h => hne (congrArg (onGround W) h))

theorem ground_good (W : Finset V) (blocks : Finset (Finset V))
    (inside : ∀ B ∈ blocks, B ⊆ W) (good : ¬ Avoidance.TwoTripleShape blocks) :
    ¬ Avoidance.TwoTripleShape (blocks.image (onGround W)) := by
  intro bad
  apply good
  constructor
  · intro B hB
    have small := bad.1 (onGround W B) (Finset.mem_image.mpr ⟨B, hB, rfl⟩)
    rwa [onGround_card W B (inside B hB)] at small
  · have count := bad.2
    rwa [ground_filter_card W blocks inside (fun n => n = 3)] at count

/-- The large-block image after labeling the actual finite ground set. -/
def labelBlock (W : Finset V) (label : ↥W ≃ Fin 6) (B : Finset V) : Finset (Fin 6) :=
  (onGround W B).map label.toEmbedding

@[simp] theorem mem_labelBlock (W : Finset V) (label : ↥W ≃ Fin 6)
    (B : Finset V) (i : Fin 6) :
    i ∈ labelBlock W label B ↔ (label.symm i).val ∈ B := by
  simp [labelBlock, Finset.mem_map_equiv]

theorem labelBlock_card (W : Finset V) (label : ↥W ≃ Fin 6)
    (B : Finset V) (inside : B ⊆ W) : (labelBlock W label B).card = B.card := by
  simpa [labelBlock] using onGround_card W B inside

theorem labelBlock_inter (W : Finset V) (label : ↥W ≃ Fin 6) (B C : Finset V) :
    labelBlock W label (B ∩ C) = labelBlock W label B ∩ labelBlock W label C := by
  ext i
  simp

theorem label_largeBlocks (W : Finset V) (label : ↥W ≃ Fin 6) (blocks : Finset (Finset V))
    (inside : ∀ B ∈ blocks, B ⊆ W) :
    largeBlocks (blocks.image (labelBlock W label)) =
      (largeBlocks blocks).image (labelBlock W label) := by
  rw [largeBlocks, Finset.filter_image]
  congr 1
  apply Finset.filter_congr
  intro B hB
  rw [labelBlock_card W label B (inside B hB)]

/-- Labeled actual multipoint traces are completely determined by their
labeled large traces, including every uncovered two-element block. -/
theorem labeled_traces_recovered (H : Simple5Hypergraph V) (W : Finset V)
    (unit : H.UnitCodegrees W) (label : ↥W ≃ Fin 6) :
    (H.multiTraces W).image (labelBlock W label) =
      pairCompletion ((largeBlocks (H.multiTraces W)).image (labelBlock W label)) := by
  rw [← label_largeBlocks W label (H.multiTraces W) (fun _ hB => H.multiTraces_subset W hB)]
  apply recover_pairs
  · intro B hB
    obtain ⟨C, hC, rfl⟩ := Finset.mem_image.mp hB
    rw [labelBlock_card W label C (H.multiTraces_subset W hC)]
    exact ((H.mem_multiTraces W C).mp hC).2
  · intro B hB C hC ne
    obtain ⟨D, hD, rfl⟩ := Finset.mem_image.mp hB
    obtain ⟨E, hE, rfl⟩ := Finset.mem_image.mp hC
    rw [← labelBlock_inter, labelBlock_card W label (D ∩ E)
      (Finset.Subset.trans Finset.inter_subset_left (H.multiTraces_subset W hD))]
    exact H.multiTraces_inter_card_le_one W unit hD hE
      (fun h => ne (congrArg (labelBlock W label) h))
  · intro P cardP
    obtain ⟨i, j, ne, rfl⟩ := Finset.card_eq_two.mp cardP
    have hne : (label.symm i).val ≠ (label.symm j).val := by
      intro eq
      exact ne (label.symm.injective (Subtype.ext eq))
    obtain ⟨B, ⟨hB, hi, hj⟩, _⟩ := H.existsUnique_multiTrace_pair W unit
      (label.symm i).property (label.symm j).property hne
    refine ⟨labelBlock W label B, Finset.mem_image.mpr ⟨B, hB, rfl⟩, ?_⟩
    simp only [Finset.insert_subset_iff, Finset.singleton_subset_iff, mem_labelBlock]
    exact ⟨hi, hj⟩

/-- Six-point classification with the exact finite set as domain, so unused
vertices outside the locks do not enter any classification assumption. -/
theorem classify_on_set (W : Finset V) (blocks : Finset (Finset V))
    (six : W.card = 6) (inside : ∀ B ∈ blocks, B ⊆ W)
    (at_most_five : ∀ B ∈ blocks, B.card ≤ 5) (linear : Linear blocks)
    (good : ¬ Avoidance.TwoTripleShape blocks) :
    ∃ k : Fin 9, k ≠ 2 ∧ k ≠ 3 ∧ ∃ label : ↥W ≃ Fin 6,
      (largeBlocks blocks).image (labelBlock W label) = representative k := by
  have small : ∀ B ∈ blocks.image (onGround W), B.card ≤ 5 := by
    intro B hB
    obtain ⟨C, hC, rfl⟩ := Finset.mem_image.mp hB
    rw [onGround_card W C (inside C hC)]
    exact at_most_five C hC
  obtain ⟨k, hk2, hk3, label, hlabel⟩ := classify_good_six
    (by simpa using six : Fintype.card ↥W = 6) (blocks.image (onGround W)) small
    (ground_linear W blocks inside linear) (ground_good W blocks inside good)
  refine ⟨k, hk2, hk3, label, ?_⟩
  change ((blocks.image (onGround W)).filter (fun B => 3 ≤ B.card)).image _ = _ at hlabel
  rw [ground_filter W blocks inside (fun n => 3 ≤ n), Finset.image_image] at hlabel
  exact hlabel

/-- Every actual 25-vertex finite goal instance has six degree-six locks and
a concrete label equivalence to one of the seven admissible representatives. -/
theorem exists_labeled_six_good_locks [Fintype V] (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (edges32 : H.edges.card = 32)
    (vertices25 : Fintype.card V = 25) :
    ∃ W : Finset V, W.card = 6 ∧ (∀ x ∈ W, H.degree x = 6) ∧ H.UnitCodegrees W ∧
      ∃ k : Fin 9, k ≠ 2 ∧ k ≠ 3 ∧ ∃ label : ↥W ≃ Fin 6,
        (largeBlocks (H.multiTraces W)).image (labelBlock W label) = representative k := by
  obtain ⟨W, six, degrees, unit, good⟩ := H.exists_six_good_locks cover edges32 vertices25
  obtain ⟨k, hk2, hk3, label, hl⟩ := classify_on_set W (H.multiTraces W) six
    (fun _ hB => H.multiTraces_subset W hB) (fun _ hB => H.multiTraces_card_le_five W hB)
    (fun _ hB _ hC hne => H.multiTraces_inter_card_le_one W unit hB hC hne) good
  exact ⟨W, six, degrees, unit, k, hk2, hk3, label, hl⟩

/-- The actual hypergraph bridge with the full representative family, not just
its large blocks. This is ready for exact trace multiplicity recovery. -/
theorem exists_full_labeled_six_good_locks [Fintype V] (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (edges32 : H.edges.card = 32)
    (vertices25 : Fintype.card V = 25) :
    ∃ W : Finset V, W.card = 6 ∧ (∀ x ∈ W, H.degree x = 6) ∧ H.UnitCodegrees W ∧
      ∃ k : Fin 9, k ≠ 2 ∧ k ≠ 3 ∧ ∃ label : ↥W ≃ Fin 6,
        (H.multiTraces W).image (labelBlock W label) = fullRepresentative k := by
  obtain ⟨W, six, degrees, unit, k, hk2, hk3, label, hl⟩ :=
    exists_labeled_six_good_locks H cover edges32 vertices25
  refine ⟨W, six, degrees, unit, k, hk2, hk3, label, ?_⟩
  rw [labeled_traces_recovered H W unit label, hl]
  rfl

end Aris4Math.K6Traces

#print axioms Aris4Math.K6Traces.classify_on_set
#print axioms Aris4Math.K6Traces.exists_labeled_six_good_locks
#print axioms Aris4Math.K6Traces.labeled_traces_recovered
#print axioms Aris4Math.K6Traces.exists_full_labeled_six_good_locks
