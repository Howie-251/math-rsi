import Aris4Math.ThirtyFour.TwentyFiveDegreeObstruction

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
