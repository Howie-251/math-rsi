import Aris4Math.ThirtyFour.TwentyFiveEightLowTenthInventoryBatch0
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowTenthInventory
open TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
export TwentyFiveEightLowTenthInventoryData (big blockLabels full)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem completion : ∀ c,pairCompletion (big c)=full c := by
  intro c
  fin_cases c
  · exact completion0
  · exact completion1
  · exact completion2
  · exact completion3
  · exact completion4
  · exact completion5
  · exact completion6
  · exact completion7
  · exact completion8
  · exact completion9
  · exact completion10
  · exact completion11
  · exact completion12
  · exact completion13
  · exact completion14
  · exact completion15
  · exact completion16
  · exact completion17
  · exact completion18
  · exact completion19
theorem recovered (c : Fin 20) (T : Finset (Fin 10)) :
  inventory 34 (standard 8) (pairCompletion (big c)) T=TwentyFiveEightLowTenth.μ c T := by
  fin_cases c
  · rw [completion0]; exact recovered0 T
  · rw [completion1]; exact recovered1 T
  · rw [completion2]; exact recovered2 T
  · rw [completion3]; exact recovered3 T
  · rw [completion4]; exact recovered4 T
  · rw [completion5]; exact recovered5 T
  · rw [completion6]; exact recovered6 T
  · rw [completion7]; exact recovered7 T
  · rw [completion8]; exact recovered8 T
  · rw [completion9]; exact recovered9 T
  · rw [completion10]; exact recovered10 T
  · rw [completion11]; exact recovered11 T
  · rw [completion12]; exact recovered12 T
  · rw [completion13]; exact recovered13 T
  · rw [completion14]; exact recovered14 T
  · rw [completion15]; exact recovered15 T
  · rw [completion16]; exact recovered16 T
  · rw [completion17]; exact recovered17 T
  · rw [completion18]; exact recovered18 T
  · rw [completion19]; exact recovered19 T
end Aris4Math.ThirtyFour.TwentyFiveEightLowTenthInventory
