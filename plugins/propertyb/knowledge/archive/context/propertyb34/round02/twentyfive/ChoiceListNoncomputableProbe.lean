import Aris4Math.ThirtyFour.TwentyFiveUnitExtension

namespace Aris4Math.ThirtyFour.TwentyFiveChoiceList
variable {n : ℕ}

/-- Evaluate the disjointness guard only on the currently selected blocks. -/
def choices (candidates : List (Finset (Fin n))) (chosen : Finset (Finset (Fin n))) :
    List (Finset (Finset (Fin n))) :=
  match candidates with
  | [] => [chosen]
  | T :: rest => choices rest chosen ++
      if chosen.toList.all (fun U => decide (T ≠ U → Disjoint T U))
      then choices rest (insert T chosen) else []

theorem choices_eq (candidates : List (Finset (Fin n)))
    (chosen : Finset (Finset (Fin n))) :
    choices candidates chosen=TwentyFiveUnitExtension.choices candidates chosen := by
  induction candidates generalizing chosen with
  | nil => rfl
  | cons T rest ih =>
    simp only [choices,TwentyFiveUnitExtension.choices,ih]
    have guard : chosen.toList.all (fun U => decide (T ≠ U → Disjoint T U))=true ↔
        ∀ U ∈ chosen, T ≠ U → Disjoint T U := by
      simp only [List.all_eq_true,Finset.mem_toList,decide_eq_true_eq]
    by_cases h : ∀ U ∈ chosen, T ≠ U → Disjoint T U
    · simp only [h,guard.mpr h,if_pos,true_iff]
    · have nh : ¬ chosen.toList.all (fun U => decide (T ≠ U → Disjoint T U))=true :=
        fun hh => h (guard.mp hh)
      simp only [h,nh,if_neg]
end Aris4Math.ThirtyFour.TwentyFiveChoiceList
#print axioms Aris4Math.ThirtyFour.TwentyFiveChoiceList.choices_eq
