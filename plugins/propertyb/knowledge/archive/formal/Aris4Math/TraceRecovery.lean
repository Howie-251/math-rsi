import Aris4Math.K6Traces
import Aris4Math.TypeCounting

/-! General trace recovery for any number of equally-degreed locks.
This is used by the four-lock numerical bridge. -/

open scoped BigOperators

namespace Aris4Math.TraceRecovery

open K6Traces K6Classification

variable {V : Type*} [DecidableEq V] {n : Nat}

/-- Label a block in an arbitrary finite lock set. -/
def labelBlock (W : Finset V) (label : ↥W ≃ Fin n) (B : Finset V) : Finset (Fin n) :=
  (onGround W B).map label.toEmbedding

@[simp] theorem mem_labelBlock (W : Finset V) (label : ↥W ≃ Fin n)
    (B : Finset V) (i : Fin n) :
    i ∈ labelBlock W label B ↔ (label.symm i).val ∈ B := by
  simp [labelBlock, Finset.mem_map_equiv]

theorem labelBlock_card (W : Finset V) (label : ↥W ≃ Fin n)
    (B : Finset V) (inside : B ⊆ W) : (labelBlock W label B).card = B.card := by
  simpa [labelBlock] using onGround_card W B inside

/-- Actual lock vertices, indexed by an arbitrary finite label set. -/
def lockVertices (W : Finset V) (label : ↥W ≃ Fin n) : Fin n ↪ V :=
  label.symm.toEmbedding.trans (Function.Embedding.subtype (fun x => x ∈ W))

/-- The exact subset of lock labels carried by an actual edge. -/
abbrev lockedLabels {ι : Type*} [Fintype ι] [DecidableEq ι]
    (vertices : ι ↪ V) (e : Finset V) : Finset ι := TypeCounting.lockSignature vertices e

@[simp] theorem mem_lockedLabels {ι : Type*} [Fintype ι] [DecidableEq ι]
    (vertices : ι ↪ V) (e : Finset V) (i : ι) :
    i ∈ lockedLabels vertices e ↔ vertices i ∈ e := by simp [lockedLabels, TypeCounting.lockSignature]

/-- Convert a label subset back into the actual vertex subset. -/
def unlabel (W : Finset V) (label : ↥W ≃ Fin n) (T : Finset (Fin n)) : Finset V :=
  T.map (lockVertices W label)

omit [DecidableEq V] in
theorem unlabel_subset (W : Finset V) (label : ↥W ≃ Fin n) (T : Finset (Fin n)) :
    unlabel W label T ⊆ W := by
  intro x hx
  obtain ⟨i, _, rfl⟩ := Finset.mem_map.mp hx
  exact (label.symm i).property

omit [DecidableEq V] in
@[simp] theorem unlabel_card (W : Finset V) (label : ↥W ≃ Fin n) (T : Finset (Fin n)) :
    (unlabel W label T).card = T.card := Finset.card_map _

@[simp] theorem label_unlabel (W : Finset V) (label : ↥W ≃ Fin n) (T : Finset (Fin n)) :
    labelBlock W label (unlabel W label T) = T := by
  ext i
  rw [mem_labelBlock]
  change lockVertices W label i ∈ T.map (lockVertices W label) ↔ i ∈ T
  exact Finset.mem_map' _

theorem labelBlock_injective (W : Finset V) (label : ↥W ≃ Fin n)
    {B C : Finset V} (hB : B ⊆ W) (hC : C ⊆ W)
    (same : labelBlock W label B = labelBlock W label C) : B = C := by
  apply onGround_injective W hB hC
  exact Finset.map_injective label.toEmbedding same

theorem labels_eq_iff_trace (W : Finset V) (label : ↥W ≃ Fin n)
    (e : Finset V) (T : Finset (Fin n)) :
    lockedLabels (lockVertices W label) e = T ↔ e ∩ W = unlabel W label T := by
  have hl : labelBlock W label (e ∩ W) = lockedLabels (lockVertices W label) e := by
    ext i
    simp [lockVertices]
  constructor
  · intro h
    apply labelBlock_injective W label Finset.inter_subset_right (unlabel_subset W label T)
    rw [hl, h, label_unlabel]
  · intro h
    rw [← hl, h, label_unlabel]

/-- Actual edge-fiber count equals the already-defined exact trace multiplicity. -/
theorem labeled_fiber_card (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin n) (T : Finset (Fin n)) :
    (H.edges.filter (fun e => lockedLabels (lockVertices W label) e = T)).card =
      H.typeCount W (unlabel W label T) := by
  unfold Simple5Hypergraph.typeCount
  congr 1
  apply Finset.filter_congr
  intro e _
  exact labels_eq_iff_trace W label e T

/-- The generic type-count formula forced by a full block family, fixed lock
degree, and total edge count. Subtraction is justified by the exact count lemmas. -/
def recoveredCount (edges degree : Nat) (blocks : Finset (Finset (Fin n)))
    (T : Finset (Fin n)) : Nat :=
  if T = ∅ then
    edges - blocks.card - ∑ i : Fin n, (degree - (blocks.filter (fun B => i ∈ B)).card)
  else if T.card = 1 then
    ∑ i ∈ T, (degree - (blocks.filter (fun B => i ∈ B)).card)
  else if T ∈ blocks then 1 else 0

theorem labeled_blocks_card (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin n) :
    ((H.multiTraces W).image (labelBlock W label)).card = (H.multiTraces W).card := by
  apply Finset.card_image_of_injOn
  intro B hB C hC h
  exact labelBlock_injective W label (H.multiTraces_subset W hB) (H.multiTraces_subset W hC) h

theorem labeled_incidence_card (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin n) (i : Fin n) :
    (((H.multiTraces W).image (labelBlock W label)).filter (fun B => i ∈ B)).card =
      ((H.multiTraces W).filter (fun B => lockVertices W label i ∈ B)).card := by
  rw [Finset.filter_image]
  have eq : (H.multiTraces W).filter (fun B => i ∈ labelBlock W label B) =
      (H.multiTraces W).filter (fun B => lockVertices W label i ∈ B) := by
    apply Finset.filter_congr
    intro B _
    exact mem_labelBlock W label B i
  rw [eq]
  apply Finset.card_image_of_injOn
  intro B hB C hC h
  exact labelBlock_injective W label
    (H.multiTraces_subset W (Finset.mem_filter.mp hB).1)
    (H.multiTraces_subset W (Finset.mem_filter.mp hC).1) h

theorem labeled_singleton_count (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin n) (unit : H.UnitCodegrees W) (degree : Nat)
    (degrees : ∀ x ∈ W, H.degree x = degree) (i : Fin n) :
    H.typeCount W (unlabel W label {i}) =
      degree - (((H.multiTraces W).image (labelBlock W label)).filter (fun B => i ∈ B)).card := by
  rw [labeled_incidence_card]
  have h := H.singleton_typeCount_eq W unit (label.symm i).property
  rw [degrees _ (label.symm i).property] at h
  simpa [unlabel, lockVertices] using h

theorem singleton_sum_labels (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin n) :
    (∑ x ∈ W, H.typeCount W {x}) = ∑ i : Fin n, H.typeCount W (unlabel W label {i}) := by
  apply Finset.sum_bij (fun x hx => label ⟨x, hx⟩) (fun _ _ => Finset.mem_univ _)
  · intro x hx y hy eq
    exact congrArg Subtype.val (label.injective eq)
  · intro i _
    exact ⟨(label.symm i).val, (label.symm i).property, label.apply_symm_apply i⟩
  · intro x hx
    simp [unlabel, lockVertices]

theorem unlabel_mem_blocks (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin n) (T : Finset (Fin n)) :
    unlabel W label T ∈ H.multiTraces W ↔
      T ∈ (H.multiTraces W).image (labelBlock W label) := by
  constructor
  · intro h
    exact Finset.mem_image.mpr ⟨unlabel W label T, h, label_unlabel W label T⟩
  · intro h
    obtain ⟨B, hB, eq⟩ := Finset.mem_image.mp h
    have same : B = unlabel W label T := labelBlock_injective W label
      (H.multiTraces_subset W hB) (unlabel_subset W label T)
      (eq.trans (label_unlabel W label T).symm)
    exact same ▸ hB

/-- Derive every exact type count of the actual hypergraph from its full
labeled block family. Empty, singleton, and large types are all proved here. -/
theorem actual_recovered_count (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin n) (unit : H.UnitCodegrees W) (degree : Nat)
    (degrees : ∀ x ∈ W, H.degree x = degree) (T : Finset (Fin n)) :
    (H.edges.filter (fun e => lockedLabels (lockVertices W label) e = T)).card =
      recoveredCount H.edges.card degree ((H.multiTraces W).image (labelBlock W label)) T := by
  rw [labeled_fiber_card]
  by_cases empty : T = ∅
  · subst T
    simp only [recoveredCount, unlabel, Finset.map_empty]
    rw [H.empty_typeCount_eq W unit, singleton_sum_labels H W label, labeled_blocks_card]
    congr 1
    apply Finset.sum_congr rfl
    intro i _
    exact labeled_singleton_count H W label unit degree degrees i
  by_cases one : T.card = 1
  · obtain ⟨i, rfl⟩ := Finset.card_eq_one.mp one
    simpa [recoveredCount] using labeled_singleton_count H W label unit degree degrees i
  · have large : 2 ≤ (unlabel W label T).card := by
      rw [unlabel_card]
      have pos : 0 < T.card := Finset.card_pos.mpr (Finset.nonempty_iff_ne_empty.mpr empty)
      omega
    rw [H.typeCount_large W _ unit large]
    simp only [unlabel_mem_blocks, recoveredCount, if_neg empty, if_neg one]


theorem labelBlock_inter (W : Finset V) (label : ↥W ≃ Fin n) (B C : Finset V) :
    labelBlock W label (B ∩ C) = labelBlock W label B ∩ labelBlock W label C := by
  ext i
  simp

theorem label_largeBlocks (W : Finset V) (label : ↥W ≃ Fin n) (blocks : Finset (Finset V))
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
    (unit : H.UnitCodegrees W) (label : ↥W ≃ Fin n) :
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


end Aris4Math.TraceRecovery

#print axioms Aris4Math.TraceRecovery.actual_recovered_count
