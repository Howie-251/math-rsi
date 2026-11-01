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


/-! Check a displayed completion using its listed blocks and all vertex pairs.
This avoids recomputing an entire completion inside each degree or count term. -/
namespace Aris4Math.ThirtyFour.TwentyFiveSparseCompletion
open Aris4Math.K6Classification TwentyFiveDegreeObstruction
variable {n : ℕ}

def Check (big full : List (Finset (Fin n))) : Bool :=
  big.all full.contains && full.all (blockCheck big) &&
    (List.finRange n).all (fun i => (List.finRange n).all (fun j =>
      decide (i=j) || big.any (fun B => decide (i∈B ∧ j∈B)) || full.contains {i,j}))

theorem complete (big full : List (Finset (Fin n))) (checked : Check big full=true) :
    pairCompletion big.toFinset=full.toFinset := by
  simp only [Check,Bool.and_eq_true] at checked
  rcases checked with ⟨⟨includes,valid⟩,pairs⟩
  apply Finset.Subset.antisymm
  · intro T mem
    rcases Finset.mem_union.mp mem with old | fresh
    · apply List.mem_toFinset.mpr
      exact List.contains_iff.mp (List.all_eq_true.mp includes T (List.mem_toFinset.mp old))
    · obtain ⟨pair,free⟩ := Finset.mem_filter.mp fresh
      obtain ⟨i,j,ne,rfl⟩ := Finset.card_eq_two.mp (Finset.mem_powersetCard.mp pair).2
      have hp := List.all_eq_true.mp (List.all_eq_true.mp pairs i (by simp)) j (by simp)
      simp only [Bool.or_eq_true,decide_eq_true_eq,List.contains_iff] at hp
      rcases hp with (eq | covered) | included
      · exact False.elim (ne eq)
      · obtain ⟨B,mem,hB⟩ := List.any_eq_true.mp covered
        have through : i∈B ∧ j∈B := of_decide_eq_true hB
        exact False.elim (free B (List.mem_toFinset.mpr mem) (by simpa only [Finset.insert_subset_iff,Finset.singleton_subset_iff] using through))
      · exact List.mem_toFinset.mpr included
  · intro T mem
    exact block_mem big T (List.all_eq_true.mp valid T (List.mem_toFinset.mp mem))

end Aris4Math.ThirtyFour.TwentyFiveSparseCompletion
namespace SparseCompletionProbe
open Aris4Math.ThirtyFour.TwentyFiveSparseCompletion
set_option maxRecDepth 100000
set_option maxHeartbeats 0
def big : List (Finset (Fin 10)) := [{0,1,2},{0,3,4},{1,3,5},{2,3,6},{4,5,6},{1,4,7},{2,5,7},{0,6,7},{2,4,8},{0,5,8},{1,6,8},{3,7,8}]
def full : List (Finset (Fin 10)) := big ++ [{0,9},{1,9},{2,9},{3,9},{4,9},{5,9},{6,9},{7,9},{8,9}]
set_option profiler true in
theorem checked : Check big full=true := by decide +kernel
#print axioms complete
end SparseCompletionProbe
