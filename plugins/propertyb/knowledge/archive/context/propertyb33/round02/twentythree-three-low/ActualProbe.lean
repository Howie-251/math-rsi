import Aris4Math.ThirtyThree.TwentyFourMatchingHighCatalog

namespace Aris4Math.ThirtyThree.TwentyThreeThreeLowHighCatalog
open scoped BigOperators
open TwentyFourMatchingHighCatalog (largeTypes largeTypes_injective largeTypes_complete)

def pairDegree (e : Fin 3 → ℕ) (b : ℕ) (i j : Fin 5) : ℕ :=
  if ({i,j} : Finset (Fin 5)) = {0,1} then e 0+1 else
  if ({i,j} : Finset (Fin 5)) = {0,2} then e 1+1 else
  if ({i,j} : Finset (Fin 5)) = {1,2} then e 2+1 else
  if ({i,j} : Finset (Fin 5)) = {3,4} then b else 1

def pairSum (h : Fin 16 → ℕ) (i j : Fin 5) : ℕ :=
  ∑ t : Fin 16, if i ∈ largeTypes t ∧ j ∈ largeTypes t then h t else 0

def highValue (h : Fin 16 → ℕ) (T : Finset (Fin 5)) : ℕ :=
  ∑ t : Fin 16, if largeTypes t = T then h t else 0

def Admissible (e : Fin 3 → ℕ) (b : ℕ) (h : Fin 16 → ℕ) : Prop :=
  ∀ i j : Fin 5, i ≠ j → pairSum h i j ≤ pairDegree e b i j


end Aris4Math.ThirtyThree.TwentyThreeThreeLowHighCatalog

namespace Aris4Math.ThirtyThree.TwentyThreeThreeLowComplete
open scoped BigOperators
open Aris4Math.TypeCounting MultiLockRecovery
open TwentyFourMatchingHighCatalog (largeTypes largeTypes_card largeTypes_injective largeTypes_complete)
open TwentyThreeThreeLowHighCatalog

def actualHigh (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23) :
    Fin 16 → ℕ := fun t => count H vertices (largeTypes t)

theorem highValue_at (h : Fin 16 → ℕ) (t : Fin 16) : highValue h (largeTypes t) = h t := by
  simp [highValue,largeTypes_injective.eq_iff]

theorem actual_high_value (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (T : Finset (Fin 5)) (large : 3 ≤ T.card) :
    count H vertices T = highValue (actualHigh H vertices) T := by
  obtain ⟨t,rfl⟩ := largeTypes_complete T large
  rw [highValue_at]
  rfl

theorem actual_admissible (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (e : Fin 3 → ℕ) (b : ℕ)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree e b i j) :
    Admissible e b (actualHigh H vertices) := by
  intro i j ij
  let indices := Finset.univ.filter fun t : Fin 16 => i ∈ largeTypes t ∧ j ∈ largeTypes t
  have image : indices.image largeTypes = supers {i,j} 3 := by
    ext T
    simp only [Finset.mem_image,indices,Finset.mem_filter,Finset.mem_univ,true_and,supers]
    constructor
    · rintro ⟨t,⟨hi,hj⟩,rfl⟩
      exact ⟨by simp only [Finset.insert_subset_iff,Finset.singleton_subset_iff]; exact ⟨hi,hj⟩,
        largeTypes_card t⟩
    · rintro ⟨sub,large⟩
      obtain ⟨t,rfl⟩ := largeTypes_complete T large
      exact ⟨t,⟨sub (by simp),sub (by simp)⟩,rfl⟩
  have sum_eq : pairSum (actualHigh H vertices) i j =
      ∑ T ∈ supers {i,j} 3, count H vertices T := by
    unfold pairSum actualHigh
    rw [← Finset.sum_filter]
    change (∑ t ∈ indices, count H vertices (largeTypes t)) = _
    rw [← image,Finset.sum_image]
    intro a _ b _ eq
    exact largeTypes_injective eq
  rw [sum_eq]
  exact (high_pair_budget H vertices i j ij).trans_eq (pairs i j ij)

private theorem large_has_unit_pair : ∀ t : Fin 16, t ≠ 0 →
    ∃ i ∈ largeTypes t, ∃ j ∈ largeTypes t, i ≠ j ∧
      ({i,j} : Finset (Fin 5)) ≠ {0,1} ∧ ({i,j} : Finset (Fin 5)) ≠ {0,2} ∧
      ({i,j} : Finset (Fin 5)) ≠ {1,2} ∧ ({i,j} : Finset (Fin 5)) ≠ {3,4} := by decide +kernel

theorem actual_rest (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (e : Fin 3 → ℕ) (b : ℕ)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree e b i j)
    (t : Fin 16) (ht : t ≠ 0) : actualHigh H vertices t ≤ 1 := by
  obtain ⟨i,hi,j,hj,ij,n01,n02,n12,n34⟩ := large_has_unit_pair t ht
  have bound := count_le_codegree H vertices (largeTypes t) i j hi hj
  simpa only [pairs i j ij,pairDegree,if_neg n01,if_neg n02,if_neg n12,if_neg n34]
    using bound

theorem actual_first (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (e : Fin 3 → ℕ) (b : ℕ) (he : e 0+e 1 ≤ 2)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree e b i j) :
    actualHigh H vertices 0 ≤ 2 := by
  have h01 := count_le_codegree H vertices (largeTypes 0) 0 1 (by decide) (by decide)
  have h02 := count_le_codegree H vertices (largeTypes 0) 0 2 (by decide) (by decide)
  rw [pairs 0 1 (by decide)] at h01
  rw [pairs 0 2 (by decide)] at h02
  have p01 : pairDegree e b 0 1 = e 0+1 := by rfl
  have p02 : pairDegree e b 0 2 = e 1+1 := by rfl
  rw [p01] at h01
  rw [p02] at h02
  unfold actualHigh
  omega

/-- Relabeling the five locks preserves each actual multiplicity after the
corresponding image of its label subset. -/
theorem count_relabel (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (σ : Fin 5 ≃ Fin 5) (T : Finset (Fin 5)) :
    count H (σ.toEmbedding.trans vertices) T = count H vertices (T.image σ) := by
  have sig (e : Finset (Fin 23)) :
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




end Aris4Math.ThirtyThree.TwentyThreeThreeLowComplete
