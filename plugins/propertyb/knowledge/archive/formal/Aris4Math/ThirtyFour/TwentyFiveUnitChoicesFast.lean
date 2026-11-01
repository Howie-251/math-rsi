import Aris4Math.ThirtyFour.TwentyFiveUnitExtension

namespace Aris4Math.ThirtyFour.TwentyFiveUnitChoicesFast
open TwentyFiveUnitExtension

/-- The same recursion, with the compatibility decision confined to the
already selected blocks instead of the ambient powerset. -/
def choicesFast {n : ℕ} (candidates : List (Finset (Fin n)))
    (chosen : Finset (Finset (Fin n))) : List (Finset (Finset (Fin n))) :=
  match candidates with
  | [] => [chosen]
  | T :: rest =>
    letI : Decidable (∀ U ∈ chosen, T ≠ U → Disjoint T U) :=
      Finset.decidableDforallFinset
    choicesFast rest chosen ++
      if ∀ U ∈ chosen, T ≠ U → Disjoint T U then
        choicesFast rest (insert T chosen) else []

theorem choicesFast_eq {n : ℕ} (candidates : List (Finset (Fin n)))
    (chosen : Finset (Finset (Fin n))) :
    choicesFast candidates chosen = choices candidates chosen := by
  induction candidates generalizing chosen with
  | nil => rfl
  | cons T rest ih =>
    simp only [choicesFast, choices, ih]

end Aris4Math.ThirtyFour.TwentyFiveUnitChoicesFast
