import Aris4Math.TypeCounting
import Aris4Math.LowDegree
import Mathlib.Tactic.IntervalCases

/-! Actual low-degree locks realize the small numerical profiles. -/

namespace Aris4Math.SmallLockProfiles

open TypeCounting

def oneVertex (x : Fin 21) : Fin 1 ↪ Fin 21 :=
  ⟨fun _ => x, fun _ _ _ => Subsingleton.elim _ _⟩

def onePosition : Fin 1 ↪ Fin 21 := oneVertex 10

def profile21 (d : ℕ) : Numeric.Profile :=
  ⟨21, [11], [⟨[], 32-d⟩, ⟨[11], d⟩], none, if d = 7 then [11] else []⟩

theorem profile21_five : profile21 5 = Numeric.v21_d5 := by rfl
theorem profile21_six : profile21 6 = Numeric.v21_d6 := by rfl
theorem profile21_seven : profile21 7 = Numeric.v21_d7 := by rfl

theorem profile21_valid (d : ℕ) (lo : 5 ≤ d) (hi : d ≤ 7) :
    Numeric.validProfile (profile21 d) := by
  interval_cases d
  · exact Numeric.v21_d5_valid
  · exact Numeric.v21_d6_valid
  · exact Numeric.v21_d7_valid

theorem one_type (x : Fin 21) (e : Finset (Fin 21)) :
    positionType (oneVertex x) onePosition e = if x ∈ e then [11] else [] := by
  have hu : (Finset.univ : Finset (Fin 1)) = {0} := by decide
  unfold positionType positionSignature lockSignature
  rw [hu]
  by_cases hx : x ∈ e <;> simp [oneVertex, onePosition, hx]

theorem one_empty_count (H : Simple5Hypergraph (Fin 21)) (x : Fin 21) :
    multiplicity H.edges (positionType (oneVertex x) onePosition) [] =
      H.edges.card - H.degree x := by
  unfold multiplicity fiber
  have he : (H.edges.filter fun e => positionType (oneVertex x) onePosition e = []) =
      H.edges.filter fun e => x ∉ e := by
    ext e
    simp only [Finset.mem_filter, one_type]
    by_cases hx : x ∈ e <;> simp [hx]
  rw [he]
  have h := Finset.filter_card_add_filter_neg_card_eq_card (s := H.edges) (p := fun e => x ∈ e)
  change H.degree x + (H.edges.filter fun e => x ∉ e).card = H.edges.card at h
  omega

theorem one_nonempty_count (H : Simple5Hypergraph (Fin 21)) (x : Fin 21) :
    multiplicity H.edges (positionType (oneVertex x) onePosition) [11] = H.degree x := by
  unfold multiplicity fiber Simple5Hypergraph.degree
  congr 1
  ext e
  simp only [Finset.mem_filter, one_type]
  by_cases hx : x ∈ e <;> simp [hx]

theorem realizes_profile21 (H : Simple5Hypergraph (Fin 21))
    (edges32 : H.edges.card = 32) (x : Fin 21)
    (lo : 5 ≤ H.degree x) (hi : H.degree x ≤ 7) :
    RealizesProfile H (oneVertex x) onePosition (profile21 (H.degree x)) := by
  refine ⟨rfl, profile21_valid _ lo hi, ?_, ?_⟩
  · change ({11} : Finset ℕ) = Finset.univ.image (fun i : Fin 1 => (onePosition i).val + 1)
    decide
  · constructor
    · simp [profile21]
    · intro e he
      simp only [profile21, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false, one_type]
      split_ifs <;> simp
    · intro t ht
      simp only [profile21, List.mem_cons, List.not_mem_nil, or_false] at ht
      rcases ht with rfl | rfl
      · simpa [edges32] using one_empty_count H x
      · exact one_nonempty_count H x

/-- The degree alternative and the complete actual type table are both
derived from H; only its numerical probability bound remains to be applied. -/
theorem exists_realized_profile21 (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32) :
    ∃ x : Fin 21, 5 ≤ H.degree x ∧ H.degree x ≤ 7 ∧
      RealizesProfile H (oneVertex x) onePosition (profile21 (H.degree x)) := by
  obtain ⟨x, lo, hi⟩ := H.exists_degree_five_to_seven_of_twenty_one cover edges32 (by simp)
  exact ⟨x, lo, hi, realizes_profile21 H edges32 x lo hi⟩

end Aris4Math.SmallLockProfiles

#print axioms Aris4Math.SmallLockProfiles.realizes_profile21
#print axioms Aris4Math.SmallLockProfiles.exists_realized_profile21
