import Aris4Math.ThirtyFour.TwentyFiveUnitCounts

/-! A failed degree budget needs only a short list of distinct incident blocks.
The list checker never constructs the full pair completion. -/
namespace Aris4Math.ThirtyFour.TwentyFiveDegreeObstruction
open Aris4Math.K6Classification TwentyFiveUnitCounts
variable {n : ℕ}

def blockCheck (listed : List (Finset (Fin n))) (T : Finset (Fin n)) : Bool :=
  listed.contains T || (decide (T.card=2) && listed.all (fun B => decide (¬ T⊆B)))

theorem block_mem (listed : List (Finset (Fin n))) (T : Finset (Fin n))
    (checked : blockCheck listed T=true) : T∈pairCompletion listed.toFinset := by
  simp only [blockCheck,Bool.or_eq_true,Bool.and_eq_true,List.contains_iff,
    decide_eq_true_eq] at checked
  rcases checked with mem | ⟨size,none⟩
  · exact Finset.mem_union_left _ (List.mem_toFinset.mpr mem)
  · apply Finset.mem_union_right
    apply Finset.mem_filter.mpr
    refine ⟨Finset.mem_powersetCard.mpr ⟨Finset.subset_univ _,size⟩,?_⟩
    intro B mem
    exact of_decide_eq_true (List.all_eq_true.mp none B (List.mem_toFinset.mp mem))

theorem not_feasible (degree : Fin n → ℕ) (listed bad : List (Finset (Fin n)))
    (i : Fin n) (nodup : bad.Nodup) (enough : degree i<bad.length)
    (checked : bad.all (fun T => decide (i∈T) && blockCheck listed T)=true) :
    ¬ Feasible 34 degree (pairCompletion listed.toFinset) := by
  intro feasible
  have subset : bad.toFinset⊆(pairCompletion listed.toFinset).filter (fun T => i∈T) := by
    intro T mem
    have h := List.all_eq_true.mp checked T (List.mem_toFinset.mp mem)
    simp only [Bool.and_eq_true] at h
    rcases h with ⟨through,valid⟩
    exact Finset.mem_filter.mpr ⟨block_mem listed T valid,of_decide_eq_true through⟩
  have lower := Finset.card_le_card subset
  rw [List.toFinset_card_of_nodup nodup] at lower
  exact (not_lt_of_ge (le_trans lower (feasible.1 i))) enough

end Aris4Math.ThirtyFour.TwentyFiveDegreeObstruction
