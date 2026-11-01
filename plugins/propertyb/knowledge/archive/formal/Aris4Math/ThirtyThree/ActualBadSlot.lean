import Aris4Math.ThirtyThree.MultiLockRecovery
import Aris4Math.ThirtyThree.CustomDeletion

/-! Record a real bad edge pair in its finite type slot before choosing lock
positions. The slot capacity and deleted weight are both derived from H. -/

namespace Aris4Math.ThirtyThree.ActualBadSlot

open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates
open Aris4Math.ThirtyThree.MultiLockRecovery

variable {n v : ℕ}

def Admissible (μ : Finset (Fin n) → ℕ) (j : Fin n)
    (T U : Finset (Fin n)) : Prop :=
  T ∩ U = {j} ∧ 0 < μ T ∧ 0 < μ U ∧ (T = U → 2 ≤ μ T)

instance (μ : Finset (Fin n) → ℕ) (j : Fin n) (T U : Finset (Fin n)) :
    Decidable (Admissible μ j T U) := by unfold Admissible; infer_instance

theorem actual_admissible (H : Simple5Hypergraph (Fin v))
    (vertices : Fin n ↪ Fin v) (j : Fin n)
    (unit : ∀ i, i ≠ j → H.codegree (vertices j) (vertices i) = 1)
    {E F : Finset (Fin v)} (bad : ({E,F} : Finset (Finset (Fin v))) ∈
      H.badLinkPairs (vertices j)) :
    Admissible (count H vertices) j (lockSignature vertices E) (lockSignature vertices F) := by
  have sub := badPair_subset H (vertices j) {E,F} bad
  have he := Finset.mem_filter.mp (sub (Finset.mem_insert_self _ _))
  have hf := Finset.mem_filter.mp (sub (Finset.mem_insert_of_mem (Finset.mem_singleton_self _)))
  have paircard := badPair_card H (vertices j) {E,F} bad
  have ef : E ≠ F := by intro h; simp [h] at paircard
  refine ⟨?_, ?_, ?_, ?_⟩
  · ext i
    simp only [Finset.mem_inter, mem_lockSignature, Finset.mem_singleton]
    constructor
    · intro h
      by_contra ij
      exact ef (H.edge_unique_of_codegree_one (unit i ij)
        he.1 hf.1 he.2 h.1 hf.2 h.2)
    · intro h
      subst i
      exact ⟨he.2,hf.2⟩
  · exact Finset.card_pos.mpr ⟨E,Finset.mem_filter.mpr ⟨he.1,rfl⟩⟩
  · exact Finset.card_pos.mpr ⟨F,Finset.mem_filter.mpr ⟨hf.1,rfl⟩⟩
  · intro same
    have inside : ({E,F} : Finset (Finset (Fin v))) ⊆
        fiber H.edges (lockSignature vertices) (lockSignature vertices E) := by
      intro e hm
      rcases Finset.mem_insert.mp hm with h | h
      · subst e
        exact Finset.mem_filter.mpr ⟨he.1,rfl⟩
      · have h := Finset.mem_singleton.mp h
        subst e
        exact Finset.mem_filter.mpr ⟨hf.1,same.symm⟩
    have bound := Finset.card_le_card inside
    simpa only [paircard] using bound

/-- A position-independent finite input extracted from a genuine bad pair. -/
theorem exists_actual_slot (H : Simple5Hypergraph (Fin v))
    (vertices : Fin n ↪ Fin v) (j : Fin n)
    (unit : ∀ i, i ≠ j → H.codegree (vertices j) (vertices i) = 1)
    (existsBad : (H.badLinkPairs (vertices j)).Nonempty) :
    ∃ T U E F, ({E,F} : Finset (Finset (Fin v))) ∈ H.badLinkPairs (vertices j) ∧
      lockSignature vertices E = T ∧ lockSignature vertices F = U ∧
      Admissible (count H vertices) j T U := by
  obtain ⟨p,hp⟩ := existsBad
  obtain ⟨E,F,_,rfl⟩ := Finset.card_eq_two.mp (badPair_card H (vertices j) p hp)
  exact ⟨_,_,E,F,hp,rfl,rfl,actual_admissible H vertices j unit hp⟩

theorem signature_disjoint (vertices : Fin n ↪ Fin v) (E : Finset (Fin v))
    (R : Finset (Fin n)) :
    Disjoint (lockSignature vertices E) R ↔ Disjoint E (R.image vertices) := by
  rw [Finset.disjoint_left, Finset.disjoint_left]
  constructor
  · intro h x hx hr
    obtain ⟨i,hi,rfl⟩ := Finset.mem_image.mp hr
    exact h (by simpa using hx) hi
  · intro h i hi hr
    exact h (by simpa using hi) (Finset.mem_image.mpr ⟨i,hr,rfl⟩)

theorem slot_avoids_of_pair_avoids (vertices : Fin n ↪ Fin v)
    (E F : Finset (Fin v)) (R : Finset (Fin n))
    (avoid : ∃ e ∈ ({E,F} : Finset (Finset (Fin v))), Disjoint e (R.image vertices)) :
    Disjoint (lockSignature vertices E) R ∨ Disjoint (lockSignature vertices F) R := by
  obtain ⟨e,he,ha⟩ := avoid
  rcases Finset.mem_insert.mp he with h | h
  · subst e
    exact Or.inl ((signature_disjoint vertices E R).mpr ha)
  · have h := Finset.mem_singleton.mp h
    subst e
    exact Or.inr ((signature_disjoint vertices F R).mpr ha)

/-- Once the actual slot is fixed, its two ordered weights may be deleted at
any subsequently selected lock positions. Other actual bad pairs are nonnegative. -/
theorem slot_weight_lower (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin n ↪ Fin v) (p : Numeric.Profile) (j : Fin n)
    (E F : Finset (Fin v)) (T U : Finset (Fin n))
    (bad : ({E,F} : Finset (Finset (Fin v))) ∈ H.badLinkPairs (vertices j))
    (hE : lockSignature vertices E = T) (hF : lockSignature vertices F = U) :
    Numeric.pairWeight p ⟨canonicalType positions T,0⟩ ⟨canonicalType positions U,0⟩
        ((positions j).val+1) +
      Numeric.pairWeight p ⟨canonicalType positions U,0⟩ ⟨canonicalType positions T,0⟩
        ((positions j).val+1) ≤
      ∑ d ∈ directedBadPairs H (vertices j),
        typeWeight p (positionType vertices positions) ((positions j).val+1) d := by
  have hc := badPair_card H (vertices j) {E,F} bad
  have ef : E ≠ F := by intro h; simp [h] at hc
  have typeE : positionType vertices positions E = canonicalType positions T := by
    change canonicalType positions (lockSignature vertices E) = _
    rw [hE]
  have typeF : positionType vertices positions F = canonicalType positions U := by
    change canonicalType positions (lockSignature vertices F) = _
    rw [hF]
  rw [directed_bad_sum]
  have h := Finset.single_le_sum
    (f := fun q => unorderedWeight
      (typeWeight p (positionType vertices positions) ((positions j).val+1)) q)
    (fun q _ => Finset.sum_nonneg fun d _ =>
      Aris4Math.ProfileProbability.numeric_pairWeight_nonneg _ _ _ _) bad
  dsimp only at h
  rw [unorderedWeight_pair _ E F ef] at h
  simpa only [typeWeight,typeE,typeF] using h

end Aris4Math.ThirtyThree.ActualBadSlot

#print axioms Aris4Math.ThirtyThree.ActualBadSlot.exists_actual_slot
#print axioms Aris4Math.ThirtyThree.ActualBadSlot.slot_weight_lower
