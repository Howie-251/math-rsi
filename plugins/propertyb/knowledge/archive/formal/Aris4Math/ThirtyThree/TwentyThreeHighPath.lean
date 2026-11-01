import Aris4Math.ThirtyThree.TwentyThreeHighPathCatalog
import Aris4Math.ThirtyThree.TwentyThreeHighSelection
import Aris4Math.ThirtyThree.TwentyThreeHighQuad

/-! Actual P3(+K2) classification, quota deletion, and original coloring. -/
namespace Aris4Math.ThirtyThree.TwentyThreeHighPath

open scoped BigOperators
open Aris4Math.TypeCounting MultiLockRecovery
open TwentyThreeHighPathData TwentyThreeHighPathCatalog

theorem large_has_unit_pair : ∀ e : Fin 2, ∀ T : Finset (Fin 5), 3 ≤ T.card →
    ∃ i ∈ T, ∃ j ∈ T, i ≠ j ∧ pairDegree e i j = 1 := by decide +kernel

theorem large_count_le_one (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (e : Fin 2) (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree e i j)
    (T : Finset (Fin 5)) (large : 3 ≤ T.card) : count H vertices T ≤ 1 := by
  obtain ⟨i,hi,j,hj,ij,unit⟩ := large_has_unit_pair e T large
  have bound := count_le_codegree H vertices T i j hi hj
  simpa only [pairs i j ij,unit] using bound

def actualBits (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23) :
    Fin 16 → Bool := fun a => decide (count H vertices (largeTypes a) = 1)

theorem actual_bit_count (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (e : Fin 2) (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree e i j)
    (a : Fin 16) :
    (if actualBits H vertices a then 1 else 0) = count H vertices (largeTypes a) := by
  have bound := large_count_le_one H vertices e pairs (largeTypes a) (largeTypes_card a)
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

theorem actual_high_value (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (e : Fin 2) (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree e i j)
    (T : Finset (Fin 5)) (large : 3 ≤ T.card) :
    count H vertices T = highValue (actualBits H vertices) T := by
  obtain ⟨a,rfl⟩ := largeTypes_complete T large
  rw [highValue_at]
  exact (actual_bit_count H vertices e pairs a).symm

theorem actual_admissible (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (e : Fin 2) (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree e i j) :
    Admissible e (actualBits H vertices) := by
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
    simp_rw [actual_bit_count H vertices e pairs]
    rw [← Finset.sum_filter]
    change (∑ a ∈ indices, count H vertices (largeTypes a)) = _
    rw [←image,Finset.sum_image]
    intro a _ b _ eq
    exact largeTypes_injective eq
  rw [sum_eq]
  exact (high_pair_budget H vertices i j ij).trans_eq (pairs i j ij)

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 23))
    (vertices : Fin 5 ↪ Fin 23) (k : Fin 115)
    (actual : ∀ T, count H vertices T = counts k T) : PropertyB H := by
  obtain ⟨valid,strict,bounds⟩ := certificates k
  have real := FiveProfiles.realizes_profile H vertices (positions k) (counts k) actual
    (List.ofFn fun j => (positions k j).val+1) (by simpa only [←p_eq] using valid)
  rw [←p_eq] at real
  apply RefinedDeletion.propertyB_of_refined_deletion H vertices (positions k) (p k) real rfl
    (loss k) (avoided k) (multipliers k) (quotas k)
  · intro j _
    exact (bounds j).1
  · intro j _
    exact (bounds j).2.1
  · intro j _
    exact (bounds j).2.2.1
  · intro j _
    exact (bounds j).2.2.2
  · intro x hx
    have ne (j : Fin 5) : x ≠ (positions k j).val+1 := by
      intro eq
      apply hx
      rw [eq]
      change _ ∈ List.ofFn (fun j => (positions k j).val+1)
      exact List.mem_ofFn.mpr ⟨j,rfl⟩
    simp only [loss,if_neg (ne 0),if_neg (ne 1),if_neg (ne 2),if_neg (ne 3),if_neg (ne 4)]
  · exact strict

/-- Classification is applied to the actual large traces before all smaller
multiplicities are recovered from degrees and pair codegrees. -/
theorem propertyB_of_labeled_path (H : Simple5Hypergraph (Fin 23)) (edges33 : H.edges.card = 33)
    (vertices : Fin 5 ↪ Fin 23) (e : Fin 2) (degrees : ∀ i, H.degree (vertices i) = 7)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree e i j) :
    PropertyB H := by
  obtain ⟨k,ek,bits⟩ := covers e (actualBits H vertices) (actual_admissible H vertices e pairs)
  have hlow : ∀ T, T.card ≤ 2 → upperCount H vertices T = lowData (extra k) T := by
    apply upper_eq_of_low_data H vertices (lowData (extra k))
    · simp [lowData,edges33]
    · intro i
      simp [lowData,degrees]
    · intro i j ij
      rw [pairs i j ij,ek]
      simp [lowData,pairDegree,ij]
  have high (T : Finset (Fin 5)) (large : 3 ≤ T.card) : count H vertices T = counts k T := by
    rw [actual_high_value H vertices e pairs T large,funext bits]
    exact catalog_counts k T large
  apply propertyB_of_counts H vertices k
  intro T
  exact (actual_recovered H vertices (lowData (extra k)) (counts k) hlow high T).trans
    (recovery_formula k T)

theorem pairDegree_comm (e : Fin 2) (i j : Fin 5) : pairDegree e i j = pairDegree e j i := by
  unfold pairDegree
  rw [Finset.pair_comm i j]

set_option maxHeartbeats 1000000 in
/-- Extend a genuine induced three-vertex path and discharge its complete
five-lock classification, including both possibilities for the new pair. -/
theorem propertyB_of_path (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges33 : H.edges.card = 33) (many : 19 ≤ (TwentyThreeSelection.sevenVertices H).card)
    (upper : ∀ x, H.degree x = 7 → ∀ y, H.degree y = 7 → x ≠ y → H.codegree x y ≤ 2)
    (x y z : Fin 23) (dx : H.degree x = 7) (dy : H.degree y = 7) (dz : H.degree z = 7)
    (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z)
    (cxy : H.codegree x y = 2) (cxz : H.codegree x z = 1)
    (cyz : H.codegree y z = 2) : PropertyB H := by
  obtain ⟨f,inj,degrees,c01,c12,c02,others⟩ :=
    TwentyThreeHighSelection.exists_five_high_of_path H cover (by decide) many
      x y z dx dy dz xy xz yz cxy cxz cyz
  have f34 : f 3 ≠ f 4 := fun eq => by have := inj eq; contradiction
  have lower := H.one_le_codegree cover f34
  have bound := upper (f 3) (degrees 3) (f 4) (degrees 4) f34
  let e : Fin 2 := ⟨H.codegree (f 3) (f 4)-1,by omega⟩
  have c34 : H.codegree (f 3) (f 4) = e.val+1 := by dsimp [e]; omega
  have forward (i j : Fin 5) (ij : i < j) : H.codegree (f i) (f j) = pairDegree e i j := by
    fin_cases i <;> fin_cases j <;> simp only [Fin.lt_def] at ij <;> norm_num at ij <;>
      norm_num [pairDegree] <;> first
      | exact c01 | exact c12 | exact c02 | exact c34
      | exact others _ _ (by decide) (by decide)
  let vertices : Fin 5 ↪ Fin 23 := ⟨f,inj⟩
  apply propertyB_of_labeled_path H edges33 vertices e degrees
  intro i j ij
  rcases lt_or_gt_of_ne ij with h | h
  · exact forward i j h
  · change H.codegree (f i) (f j) = _
    rw [H.codegree_comm, forward j i h, pairDegree_comm]

end Aris4Math.ThirtyThree.TwentyThreeHighPath
