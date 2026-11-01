import Aris4Math.ThirtyThree.TwentyFourMatchingHighCatalog

/-! The actual five-low matching configuration is connected to the complete
local high-type classification and the strict bare probability certificate. -/
namespace Aris4Math.ThirtyThree.TwentyFourFiveMatchingComplete
open scoped BigOperators
open Aris4Math.TypeCounting MultiLockRecovery
open TwentyFourFiveMatching TwentyFourMatchingHighCatalog

private theorem large_has_unit_pair : ∀ T : Finset (Fin 5), 3 ≤ T.card →
    ∃ i ∈ T, ∃ j ∈ T, i ≠ j ∧ pairDegree i j = 1 := by decide +kernel

theorem large_count_le_one (H : Simple5Hypergraph (Fin 24)) (vertices : Fin 5 ↪ Fin 24)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree i j)
    (T : Finset (Fin 5)) (large : 3 ≤ T.card) : count H vertices T ≤ 1 := by
  obtain ⟨i,hi,j,hj,ij,unit⟩ := large_has_unit_pair T large
  have bound := count_le_codegree H vertices T i j hi hj
  simpa only [pairs i j ij,unit] using bound

def actualBits (H : Simple5Hypergraph (Fin 24)) (vertices : Fin 5 ↪ Fin 24) :
    Fin 16 → Bool := fun a => decide (count H vertices (largeTypes a) = 1)

theorem actual_bit_count (H : Simple5Hypergraph (Fin 24)) (vertices : Fin 5 ↪ Fin 24)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree i j)
    (a : Fin 16) :
    (if actualBits H vertices a then 1 else 0) = count H vertices (largeTypes a) := by
  have bound := large_count_le_one H vertices pairs (largeTypes a) (largeTypes_card a)
  by_cases hc : count H vertices (largeTypes a) = 1
  · simp [actualBits,hc]
  · have hz : count H vertices (largeTypes a) = 0 := by omega
    simp [actualBits,hz]

theorem highValue_at (h : Fin 16 → Bool) (a : Fin 16) :
    highValue h (largeTypes a) = if h a then 1 else 0 := by
  have eq : (∃ b : Fin 16, largeTypes b = largeTypes a ∧ h b = true) ↔ h a = true := by
    constructor
    · rintro ⟨b,eq,hb⟩
      have ba := largeTypes_injective eq
      simpa only [ba] using hb
    · intro ha
      exact ⟨a,rfl,ha⟩
  simp only [highValue,eq]

theorem actual_high_value (H : Simple5Hypergraph (Fin 24)) (vertices : Fin 5 ↪ Fin 24)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree i j)
    (T : Finset (Fin 5)) (large : 3 ≤ T.card) :
    count H vertices T = highValue (actualBits H vertices) T := by
  obtain ⟨a,rfl⟩ := largeTypes_complete T large
  rw [highValue_at]
  exact (actual_bit_count H vertices pairs a).symm

theorem actual_admissible (H : Simple5Hypergraph (Fin 24)) (vertices : Fin 5 ↪ Fin 24)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree i j) :
    Admissible (actualBits H vertices) := by
  intro i j ij
  let indices := Finset.univ.filter fun a : Fin 16 => i ∈ largeTypes a ∧ j ∈ largeTypes a
  have image : indices.image largeTypes = supers {i,j} 3 := by
    ext T
    simp only [Finset.mem_image,indices,Finset.mem_filter,Finset.mem_univ,true_and,supers]
    constructor
    · rintro ⟨a,⟨hi,hj⟩,rfl⟩
      exact ⟨by simp only [Finset.insert_subset_iff,Finset.singleton_subset_iff]; exact ⟨hi,hj⟩,
        largeTypes_card a⟩
    · rintro ⟨sub,large⟩
      obtain ⟨a,rfl⟩ := largeTypes_complete T large
      exact ⟨a,⟨sub (by simp),sub (by simp)⟩,rfl⟩
  have sum_eq : pairSum (actualBits H vertices) i j =
      ∑ T ∈ supers {i,j} 3, count H vertices T := by
    unfold pairSum
    simp_rw [actual_bit_count H vertices pairs]
    rw [← Finset.sum_filter]
    change (∑ a ∈ indices, count H vertices (largeTypes a)) = _
    rw [← image,Finset.sum_image]
    intro a _ b _ eq
    exact largeTypes_injective eq
  rw [sum_eq]
  exact (high_pair_budget H vertices i j ij).trans_eq (pairs i j ij)

/-- Relabeling the five locks preserves each actual multiplicity after the
corresponding image of its label subset. -/
theorem count_relabel (H : Simple5Hypergraph (Fin 24)) (vertices : Fin 5 ↪ Fin 24)
    (σ : Fin 5 ≃ Fin 5) (T : Finset (Fin 5)) :
    count H (σ.toEmbedding.trans vertices) T = count H vertices (T.image σ) := by
  have sig (e : Finset (Fin 24)) :
      (lockSignature (σ.toEmbedding.trans vertices) e).image σ = lockSignature vertices e := by
    ext j
    constructor
    · intro hj
      obtain ⟨i,hi,rfl⟩ := Finset.mem_image.mp hj
      exact (mem_lockSignature vertices e (σ i)).mpr
        ((mem_lockSignature (σ.toEmbedding.trans vertices) e i).mp hi)
    · intro hj
      apply Finset.mem_image.mpr
      refine ⟨σ.symm j,?_,σ.apply_symm_apply j⟩
      apply (mem_lockSignature (σ.toEmbedding.trans vertices) e (σ.symm j)).mpr
      simpa using (mem_lockSignature vertices e j).mp hj
  unfold count multiplicity fiber
  congr 1
  apply Finset.filter_congr
  intro e _
  constructor
  · intro hs
    exact (sig e).symm.trans (congrArg (fun S : Finset (Fin 5) => S.image σ) hs)
  · intro hs
    apply Finset.image_injective σ.injective
    exact (sig e).trans hs

/-- Complete five-matching branch: every datum is obtained from the actual
hypergraph, including Boolean high types, classification, relabeling, and all
remaining type multiplicities. -/
theorem propertyB_of_five_matching (H : Simple5Hypergraph (Fin 24))
    (edges33 : H.edges.card = 33) (selected : TwentyFourSelection.FiveMatchingLocks H) :
    PropertyB H := by
  obtain ⟨vertices,degrees,pairs⟩ := exists_labeled H selected
  obtain ⟨k,σ,preserve,large⟩ := classify (actualBits H vertices)
    (actual_admissible H vertices pairs)
  let newVertices := σ.toEmbedding.trans vertices
  apply propertyB_of_large H edges33 newVertices (fun i => degrees (σ i))
    (fun i j ij => (pairs (σ i) (σ j) (σ.injective.ne ij)).trans (preserve i j)) k
  intro T hT
  rw [show newVertices = σ.toEmbedding.trans vertices from rfl,count_relabel]
  rw [actual_high_value H vertices pairs (T.image σ)
    (by simpa only [Finset.card_image_of_injective _ σ.injective] using hT)]
  exact large T hT

end Aris4Math.ThirtyThree.TwentyFourFiveMatchingComplete
#print axioms Aris4Math.ThirtyThree.TwentyFourFiveMatchingComplete.propertyB_of_five_matching
