import Aris4Math.ThirtyFour.TwentyFiveUnit9Data

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

namespace Aris4Math.ThirtyFour
open TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
example : rows0.map Row.selected = TwentyFiveUnitChoicesFast.choicesFast (candidates 0) ∅ := by decide +kernel
end Aris4Math.ThirtyFour
