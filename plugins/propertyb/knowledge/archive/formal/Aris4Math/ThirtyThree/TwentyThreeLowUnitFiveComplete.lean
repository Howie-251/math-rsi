import Aris4Math.ThirtyThree.TwentyThreeLowUnitFiveCatalog
import Aris4Math.ThirtyThree.TwentyThreeDefectSelection
import Aris4Math.ThirtyThree.TwentyThreeHighPair

/-! Actual one-low, all-unit branch with a seven-degree pair of codegree ≥3. -/
namespace Aris4Math.ThirtyThree.TwentyThreeLowUnitFiveComplete
open scoped BigOperators
open Aris4Math.TypeCounting MultiLockRecovery
open TwentyThreeTwoLowHighCatalog (pairDegree Admissible)
open TwentyFourMatchingHighCatalog (largeTypes largeTypes_card largeTypes_injective
  largeTypes_complete highValue pairSum)
open TwentyThreeLowUnitFiveCatalog (low)

private theorem large_has_unit_pair : ∀ T : Finset (Fin 5), 3 ≤ T.card →
    ∃ i ∈ T, ∃ j ∈ T, i ≠ j ∧ ({i,j} : Finset (Fin 5)) ≠ {0,1} ∧
      ({i,j} : Finset (Fin 5)) ≠ {2,3} := by decide +kernel

theorem large_count_le_one (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (a b : ℕ)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree a b i j)
    (T : Finset (Fin 5)) (large : 3 ≤ T.card) : count H vertices T ≤ 1 := by
  obtain ⟨i,hi,j,hj,ij,not01,not23⟩ := large_has_unit_pair T large
  have unit : pairDegree a b i j = 1 := by simp [pairDegree,not01,not23]
  have bound := count_le_codegree H vertices T i j hi hj
  simpa only [pairs i j ij,unit] using bound

def actualBits (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23) :
    Fin 16 → Bool := fun a => decide (count H vertices (largeTypes a) = 1)

theorem actual_bit_count (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (a b : ℕ)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree a b i j)
    (t : Fin 16) :
    (if actualBits H vertices t then 1 else 0) = count H vertices (largeTypes t) := by
  have bound := large_count_le_one H vertices a b pairs (largeTypes t) (largeTypes_card t)
  by_cases hc : count H vertices (largeTypes t) = 1
  · simp [actualBits,hc]
  · have hz : count H vertices (largeTypes t) = 0 := by omega
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

theorem actual_high_value (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (a b : ℕ)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree a b i j)
    (T : Finset (Fin 5)) (large : 3 ≤ T.card) :
    count H vertices T = highValue (actualBits H vertices) T := by
  obtain ⟨t,rfl⟩ := largeTypes_complete T large
  rw [highValue_at]
  exact (actual_bit_count H vertices a b pairs t).symm

theorem actual_admissible (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (a b : ℕ)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree a b i j) :
    Admissible a b (actualBits H vertices) := by
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
    simp_rw [actual_bit_count H vertices a b pairs]
    rw [← Finset.sum_filter]
    change (∑ a ∈ indices, count H vertices (largeTypes a)) = _
    rw [← image,Finset.sum_image]
    intro a _ b _ eq
    exact largeTypes_injective eq
  rw [sum_eq]
  exact (high_pair_budget H vertices i j ij).trans_eq (pairs i j ij)

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


theorem propertyB_of_locks (H : Simple5Hypergraph (Fin 23))
    (edges33 : H.edges.card = 33) (vertices : Fin 5 ↪ Fin 23) (a : ℕ)
    (ha : 1 ≤ a ∧ a ≤ 3)
    (degrees : ∀ i, H.degree (vertices i) = if i=4 then 6 else 7)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree a 3 i j) :
    PropertyB H := by
  have hlow : ∀ T, T.card ≤ 2 → upperCount H vertices T = low a T := by
    apply upper_eq_of_low_data
    · simp [low,edges33]
    · intro i
      rw [degrees]
      fin_cases i <;> simp [low]
    · intro i j ij
      rw [pairs i j ij]
      simp [low,pairDegree,ij]
  have high : ∀ T, 3 ≤ T.card → count H vertices T = highValue (actualBits H vertices) T :=
    actual_high_value H vertices a 3 pairs
  have recovered (T : Finset (Fin 5)) :=
    actual_recovered H vertices (low a) (highValue (actualBits H vertices)) hlow high T
  obtain ⟨k,σ,chosen⟩ := TwentyThreeLowUnitFiveCatalog.classify a (actualBits H vertices) ha
    (actual_admissible H vertices a 3 pairs)
  apply TwentyThreeLowUnitFiveBare.propertyB_of_counts H (σ.toEmbedding.trans vertices) k
  intro T
  rw [count_relabel,recovered]
  exact chosen T

def reorder : Fin 5 → Fin 5 := ![3,4,1,2,0]
theorem reorder_injective : Function.Injective reorder := by decide +kernel

private theorem pairDegree_comm (a b : ℕ) (i j : Fin 5) :
    pairDegree a b i j = pairDegree a b j i := by
  simp only [pairDegree,Finset.pair_comm i j]

set_option maxHeartbeats 1000000 in
/-- The selected five locks are reordered so the low vertex is label4. -/
theorem propertyB_of_high_three (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (many : 17 ≤ (TwentyThreeSelection.sevenVertices H).card)
    (x y z : Fin 23) (dx : H.degree x = 6) (dy : H.degree y = 7) (dz : H.degree z = 7)
    (unit : ∀ a, H.degree a = 7 → H.codegree x a = 1)
    (yz : y ≠ z) (cyz : H.codegree y z = 3) : PropertyB H := by
  obtain ⟨f,inj,fx,degrees,c12,others⟩ :=
    TwentyThreeDefectSelection.exists_mixed_five_of_high_three H cover (by decide) many
      x y z dx dy dz unit yz cyz
  have ne34 : f 3 ≠ f 4 := inj.ne (by decide)
  have d3 : H.degree (f 3) = 7 := by simpa using degrees 3
  have d4 : H.degree (f 4) = 7 := by simpa using degrees 4
  by_cases high : 4 ≤ H.codegree (f 3) (f 4)
  · exact TwentyThreeHighPair.propertyB_of_high_pair H edges33 (f 3) (f 4) ne34 d3 d4 high
  let a := H.codegree (f 3) (f 4)
  have ha : 1 ≤ a ∧ a ≤ 3 := ⟨H.one_le_codegree cover ne34,by dsimp [a]; omega⟩
  let g := f ∘ reorder
  let vertices : Fin 5 ↪ Fin 23 := ⟨g,inj.comp reorder_injective⟩
  have ds (i : Fin 5) : H.degree (vertices i) = if i=4 then 6 else 7 := by
    change H.degree (f (reorder i)) = _
    rw [degrees]
    fin_cases i <;> rfl
  have co (i j : Fin 5) (ij : i < j) :
      H.codegree (vertices i) (vertices j) = pairDegree a 3 i j := by
    have u01 := others 0 1 (by decide) (by decide) (by decide)
    have u02 := others 0 2 (by decide) (by decide) (by decide)
    have u03 := others 0 3 (by decide) (by decide) (by decide)
    have u04 := others 0 4 (by decide) (by decide) (by decide)
    have u13 := others 1 3 (by decide) (by decide) (by decide)
    have u14 := others 1 4 (by decide) (by decide) (by decide)
    have u23 := others 2 3 (by decide) (by decide) (by decide)
    have u24 := others 2 4 (by decide) (by decide) (by decide)
    have v01 := (H.codegree_comm (f 1) (f 0)).trans u01
    have v02 := (H.codegree_comm (f 2) (f 0)).trans u02
    have v03 := (H.codegree_comm (f 3) (f 0)).trans u03
    have v04 := (H.codegree_comm (f 4) (f 0)).trans u04
    have v13 := (H.codegree_comm (f 3) (f 1)).trans u13
    have v14 := (H.codegree_comm (f 4) (f 1)).trans u14
    have v23 := (H.codegree_comm (f 3) (f 2)).trans u23
    have v24 := (H.codegree_comm (f 4) (f 2)).trans u24
    fin_cases i <;> fin_cases j <;> simp only [Fin.lt_def] at ij <;> norm_num at ij <;>
      norm_num [vertices,g,Function.comp_def,reorder,pairDegree] <;> first
      | rfl | exact c12 | exact v01 | exact v02 | exact v03 | exact v04
      | exact v13 | exact v14 | exact v23 | exact v24
  apply propertyB_of_locks H edges33 vertices a ha ds
  intro i j ij
  rcases lt_or_gt_of_ne ij with h | h
  · exact co i j h
  · rw [H.codegree_comm,co j i h,pairDegree_comm]

theorem propertyB_of_high_pair (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (many : 17 ≤ (TwentyThreeSelection.sevenVertices H).card)
    (x y z : Fin 23) (dx : H.degree x = 6) (dy : H.degree y = 7) (dz : H.degree z = 7)
    (unit : ∀ a, H.degree a = 7 → H.codegree x a = 1)
    (yz : y ≠ z) (cyz : 3 ≤ H.codegree y z) : PropertyB H := by
  by_cases high : 4 ≤ H.codegree y z
  · exact TwentyThreeHighPair.propertyB_of_high_pair H edges33 y z yz dy dz high
  · exact propertyB_of_high_three H cover edges33 many x y z dx dy dz unit yz (by omega)

end Aris4Math.ThirtyThree.TwentyThreeLowUnitFiveComplete
#print axioms Aris4Math.ThirtyThree.TwentyThreeLowUnitFiveComplete.propertyB_of_high_pair
