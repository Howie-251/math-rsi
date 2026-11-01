import Aris4Math.TypeCounting
import Aris4Math.LowDegree
import Mathlib.Tactic.IntervalCases
import Aris4Math.ThirtyThree.TwentyOneDeletion

/-! Actual low-degree locks realize the small numerical profiles. -/

namespace Aris4Math.ThirtyFour.NineteenSingle

open TypeCounting

def oneVertex (x : Fin 19) : Fin 1 ↪ Fin 19 :=
  ⟨fun _ => x, fun _ _ _ => Subsingleton.elim _ _⟩

def onePosition : Fin 1 ↪ Fin 19 := oneVertex 9

def profile19 (d : ℕ) : Numeric.Profile :=
  ⟨19, [10], [⟨[], 34-d⟩, ⟨[10], d⟩], none, [10]⟩

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem certificates : ∀ d : Fin 8, 5 ≤ d.val →
    Numeric.validProfile (profile19 d.val) 34 ∧ Numeric.totalBound (profile19 d.val) < 1 ∧
    0 ≤ ThirtyThree.TwentyOneDeletion.threshold (profile19 d.val) 10 ∧
    Numeric.deduction (profile19 d.val) 10 ≤
      (((4*d.val-18+2)/3 : ℕ) : ℚ) * ThirtyThree.TwentyOneDeletion.threshold (profile19 d.val) 10 -
        ThirtyThree.TwentyOneDeletion.penaltySum (profile19 d.val) 10
          (ThirtyThree.TwentyOneDeletion.threshold (profile19 d.val) 10) := by
  unfold Numeric.validProfile
  decide +kernel

theorem profile19_valid (d : ℕ) (lo : 5 ≤ d) (hi : d ≤ 7) :
    Numeric.validProfile (profile19 d) 34 :=
  (certificates ⟨d,by omega⟩ lo).1

theorem one_type (x : Fin 19) (e : Finset (Fin 19)) :
    positionType (oneVertex x) onePosition e = if x ∈ e then [10] else [] := by
  have hu : (Finset.univ : Finset (Fin 1)) = {0} := by decide
  unfold positionType positionSignature lockSignature
  rw [hu]
  by_cases hx : x ∈ e <;> simp [oneVertex, onePosition, hx]

theorem one_empty_count (H : Simple5Hypergraph (Fin 19)) (x : Fin 19) :
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

theorem one_nonempty_count (H : Simple5Hypergraph (Fin 19)) (x : Fin 19) :
    multiplicity H.edges (positionType (oneVertex x) onePosition) [10] = H.degree x := by
  unfold multiplicity fiber Simple5Hypergraph.degree
  congr 1
  ext e
  simp only [Finset.mem_filter, one_type]
  by_cases hx : x ∈ e <;> simp [hx]

theorem realizes_profile19 (H : Simple5Hypergraph (Fin 19))
    (edges34 : H.edges.card = 34) (x : Fin 19)
    (lo : 5 ≤ H.degree x) (hi : H.degree x ≤ 7) :
    RealizesProfile H (oneVertex x) onePosition (profile19 (H.degree x)) 34 := by
  refine ⟨rfl, profile19_valid _ lo hi, ?_, ?_⟩
  · change ({10} : Finset ℕ) = Finset.univ.image (fun i : Fin 1 => (onePosition i).val + 1)
    decide
  · constructor
    · simp [profile19]
    · intro e he
      simp only [profile19, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false, one_type]
      split_ifs <;> simp
    · intro t ht
      simp only [profile19, List.mem_cons, List.not_mem_nil, or_false] at ht
      rcases ht with rfl | rfl
      · simpa [edges34] using one_empty_count H x
      · exact one_nonempty_count H x

theorem propertyB_of_degree_five_to_seven (H : Simple5Hypergraph (Fin 19))
    (cover : H.PairCovering) (edges34 : H.edges.card = 34) (x : Fin 19)
    (lo : 5 ≤ H.degree x) (hi : H.degree x ≤ 7) : PropertyB H := by
  have real := realizes_profile19 H edges34 x lo hi
  obtain ⟨_,strict,nonneg,bound⟩ := certificates ⟨H.degree x,by omega⟩ lo
  apply ProfileApplication.propertyB_of_corrected_profile H
    (oneVertex x) onePosition (profile19 (H.degree x)) real rfl
  · intro j _
    have hk : (onePosition j).val + 1 = 10 := by rfl
    rw [hk]
    apply ThirtyThree.TwentyOneDeletion.realized_threshold_deduction H cover
      (oneVertex x) onePosition (profile19 (H.degree x)) real j 10
      ((4*H.degree x-18+2)/3) _ _ hk
    · exact le_rfl
    · exact nonneg
    · exact bound
  · exact strict

end Aris4Math.ThirtyFour.NineteenSingle
#print axioms Aris4Math.ThirtyFour.NineteenSingle.propertyB_of_degree_five_to_seven
