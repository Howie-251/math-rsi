import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion832 : pairCompletion (big 832)=full 832 := by
  have same : big 832=([{0,2,3,6},{1,4,5,6},{2,4,7},{3,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,6},{1,4,5,6},{2,4,7},{3,5,7},{6,7,8}] [{0,1},{1,2},{1,3},{0,4},{3,4},{0,5},{2,5},{0,2,3,6},{1,4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered832 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 832) T=TwentyFiveEightLow.Case832.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case832.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 832)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case832.support T pos))
  · decide +kernel
theorem completion833 : pairCompletion (big 833)=full 833 := by
  have same : big 833=([{0,1,2,3,6},{4,5,6},{2,4,7},{3,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,6},{4,5,6},{2,4,7},{3,5,7},{6,7,8}] [{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{0,1,2,3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered833 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 833) T=TwentyFiveEightLow.Case833.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case833.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 833)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case833.support T pos))
  · decide +kernel
theorem completion834 : pairCompletion (big 834)=full 834 := by
  have same : big 834=([{0,1,4,6},{2,3,5,6},{4,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,6},{2,3,5,6},{4,5,7},{6,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,4},{3,4},{0,5},{1,5},{0,1,4,6},{2,3,5,6},{0,7},{1,7},{2,7},{3,7},{4,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered834 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 834) T=TwentyFiveEightLow.Case834.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case834.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 834)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case834.support T pos))
  · decide +kernel
theorem completion835 : pairCompletion (big 835)=full 835 := by
  have same : big 835=([{0,1,2,5,6},{3,4,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5,6},{3,4,5,7},{6,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,6},{4,6},{0,1,2,5,6},{0,7},{1,7},{2,7},{3,4,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered835 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 835) T=TwentyFiveEightLow.Case835.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case835.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 835)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case835.support T pos))
  · decide +kernel
theorem completion836 : pairCompletion (big 836)=full 836 := by
  have same : big 836=([{0,1,6,7},{2,3,6,8},{4,5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6,7},{2,3,6,8},{4,5,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{0,5},{1,5},{2,5},{3,5},{4,6},{5,6},{2,7},{3,7},{0,1,6,7},{0,8},{1,8},{2,3,6,8},{4,5,7,8}]=true
  decide +kernel

theorem recovered836 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 836) T=TwentyFiveEightLow.Case836.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case836.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 836)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case836.support T pos))
  · decide +kernel
theorem completion837 : pairCompletion (big 837)=full 837 := by
  have same : big 837=([{0,1,5,6},{2,3,5,7},{4,6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5,6},{2,3,5,7},{4,6,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{4,5},{2,6},{3,6},{0,1,5,6},{0,7},{1,7},{2,3,5,7},{0,8},{1,8},{2,8},{3,8},{5,8},{4,6,7,8}]=true
  decide +kernel

theorem recovered837 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 837) T=TwentyFiveEightLow.Case837.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case837.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 837)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case837.support T pos))
  · decide +kernel
theorem completion838 : pairCompletion (big 838)=full 838 := by
  have same : big 838=([{0,1,2,3,8},{4,5,6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,8},{4,5,6,7,8}] [{0,4},{1,4},{2,4},{3,4},{0,5},{1,5},{2,5},{3,5},{0,6},{1,6},{2,6},{3,6},{0,7},{1,7},{2,7},{3,7},{0,1,2,3,8},{4,5,6,7,8}]=true
  decide +kernel

theorem recovered838 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 838) T=TwentyFiveEightLow.Case838.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case838.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 838)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case838.support T pos))
  · decide +kernel
theorem completion839 : pairCompletion (big 839)=full 839 := by
  have same : big 839=([{0,1,2,3,7},{4,5,6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,7},{4,5,6,7,8}] [{0,4},{1,4},{2,4},{3,4},{0,5},{1,5},{2,5},{3,5},{0,6},{1,6},{2,6},{3,6},{0,1,2,3,7},{0,8},{1,8},{2,8},{3,8},{4,5,6,7,8}]=true
  decide +kernel

theorem recovered839 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 839) T=TwentyFiveEightLow.Case839.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case839.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 839)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case839.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
