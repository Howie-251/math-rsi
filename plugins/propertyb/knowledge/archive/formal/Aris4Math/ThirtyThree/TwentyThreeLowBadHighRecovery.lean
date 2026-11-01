import Aris4Math.ThirtyThree.TwentyThreeLowBadHighData
namespace Aris4Math.ThirtyThree.TwentyThreeLowBadHighComplete
open MultiLockRecovery TwentyThreeLowBadHighData

def low (c : Config) (T : Finset (Fin 5)) : ℕ :=
  if T = ∅ then 33 else if T.card = 1 then (if 0 ∈ T then 6 else 7) else
  if T = {0,1} then lowCodegree c else if T = {2,3} then highCodegree c else 1

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem recovery_formula : ∀ c T, recovered (low c) (counts c) T = counts c T := by
  intro c
  fin_cases c <;> decide +kernel

end Aris4Math.ThirtyThree.TwentyThreeLowBadHighComplete
