import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion64 : pairCompletion (big 64)=full 64 := by
  have same : big 64=([{0,1,2},{0,3,4},{2,3,6},{4,5,6},{2,4,7},{3,5,7},{1,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,4},{2,3,6},{4,5,6},{2,4,7},{3,5,7},{1,5,8},{6,7,8}] [{0,1,2},{1,3},{1,4},{0,3,4},{0,5},{2,5},{0,6},{1,6},{2,3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,8},{2,8},{3,8},{4,8},{1,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered64 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 64) T=TwentyFiveEightLow.Case64.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case64.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 64)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case64.support T pos))
  · decide +kernel
theorem completion65 : pairCompletion (big 65)=full 65 := by
  have same : big 65=([{0,2,3},{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,6,8},{1,7,8}] [{0,1},{1,2},{1,3},{0,2,3},{0,4},{0,5},{1,4,5},{1,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{6,7},{2,8},{3,8},{4,8},{5,8},{0,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered65 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 65) T=TwentyFiveEightLow.Case65.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case65.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 65)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case65.support T pos))
  · decide +kernel
theorem completion66 : pairCompletion (big 66)=full 66 := by
  have same : big 66=([{0,1,3},{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}] [{0,2},{1,2},{0,1,3},{2,4},{3,4},{1,5},{3,5},{0,4,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{2,3,7},{5,6,7},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered66 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 66) T=TwentyFiveEightLow.Case66.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case66.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 66)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case66.support T pos))
  · decide +kernel
theorem completion67 : pairCompletion (big 67)=full 67 := by
  have same : big 67=([{0,1,3},{0,4,5},{1,4,6},{2,5,7},{3,6,7},{2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{0,4,5},{1,4,6},{2,5,7},{3,6,7},{2,3,8},{5,6,8},{4,7,8}] [{0,2},{1,2},{0,1,3},{2,4},{3,4},{1,5},{3,5},{0,4,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,8},{1,8},{2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered67 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 67) T=TwentyFiveEightLow.Case67.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case67.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 67)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case67.support T pos))
  · decide +kernel
theorem completion68 : pairCompletion (big 68)=full 68 := by
  have same : big 68=([{0,1,3},{0,4,5},{2,3,6},{2,4,7},{5,6,7},{1,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{0,4,5},{2,3,6},{2,4,7},{5,6,7},{1,5,8},{4,6,8},{3,7,8}] [{0,2},{1,2},{0,1,3},{1,4},{3,4},{2,5},{3,5},{0,4,5},{0,6},{1,6},{2,3,6},{0,7},{1,7},{2,4,7},{5,6,7},{0,8},{2,8},{1,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered68 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 68) T=TwentyFiveEightLow.Case68.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case68.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 68)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case68.support T pos))
  · decide +kernel
theorem completion69 : pairCompletion (big 69)=full 69 := by
  have same : big 69=([{0,1,3},{0,4,5},{2,3,6},{3,5,7},{4,6,7},{1,4,8},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{0,4,5},{2,3,6},{3,5,7},{4,6,7},{1,4,8},{5,6,8},{2,7,8}] [{0,2},{1,2},{0,1,3},{2,4},{3,4},{1,5},{2,5},{0,4,5},{0,6},{1,6},{2,3,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{3,8},{1,4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered69 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 69) T=TwentyFiveEightLow.Case69.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case69.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 69)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case69.support T pos))
  · decide +kernel
theorem completion70 : pairCompletion (big 70)=full 70 := by
  have same : big 70=([{0,1,3},{2,3,5},{2,4,6},{4,5,7},{3,6,7},{0,4,8},{5,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{2,3,5},{2,4,6},{4,5,7},{3,6,7},{0,4,8},{5,6,8},{1,7,8}] [{0,2},{1,2},{0,1,3},{1,4},{3,4},{0,5},{1,5},{2,3,5},{0,6},{1,6},{2,4,6},{0,7},{2,7},{4,5,7},{3,6,7},{2,8},{3,8},{0,4,8},{5,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered70 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 70) T=TwentyFiveEightLow.Case70.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case70.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 70)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case70.support T pos))
  · decide +kernel
theorem completion71 : pairCompletion (big 71)=full 71 := by
  have same : big 71=([{0,3,4},{1,3,5},{2,4,6},{4,5,7},{3,6,7},{0,1,8},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{2,4,6},{4,5,7},{3,6,7},{0,1,8},{5,6,8},{2,7,8}] [{0,2},{1,2},{2,3},{1,4},{0,3,4},{0,5},{2,5},{1,3,5},{0,6},{1,6},{2,4,6},{0,7},{1,7},{4,5,7},{3,6,7},{0,1,8},{3,8},{4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered71 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 71) T=TwentyFiveEightLow.Case71.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case71.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 71)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case71.support T pos))
  · decide +kernel
theorem completion72 : pairCompletion (big 72)=full 72 := by
  have same : big 72=([{0,1,2},{0,3,4},{1,3,5},{2,4,6},{4,5,7},{3,6,7},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,4},{1,3,5},{2,4,6},{4,5,7},{3,6,7},{5,6,8},{2,7,8}] [{0,1,2},{2,3},{1,4},{0,3,4},{0,5},{2,5},{1,3,5},{0,6},{1,6},{2,4,6},{0,7},{1,7},{4,5,7},{3,6,7},{0,8},{1,8},{3,8},{4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered72 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 72) T=TwentyFiveEightLow.Case72.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case72.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 72)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case72.support T pos))
  · decide +kernel
theorem completion73 : pairCompletion (big 73)=full 73 := by
  have same : big 73=([{0,2,4},{0,3,5},{1,2,6},{4,5,6},{3,4,7},{2,5,7},{1,3,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4},{0,3,5},{1,2,6},{4,5,6},{3,4,7},{2,5,7},{1,3,8},{6,7,8}] [{0,1},{2,3},{1,4},{0,2,4},{1,5},{0,3,5},{0,6},{1,2,6},{3,6},{4,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{0,8},{2,8},{1,3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered73 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 73) T=TwentyFiveEightLow.Case73.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case73.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 73)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case73.support T pos))
  · decide +kernel
theorem completion74 : pairCompletion (big 74)=full 74 := by
  have same : big 74=([{0,2,3},{2,4,5},{0,4,6},{3,5,6},{3,4,7},{1,5,7},{1,2,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{2,4,5},{0,4,6},{3,5,6},{3,4,7},{1,5,7},{1,2,8},{6,7,8}] [{0,1},{1,3},{0,2,3},{1,4},{0,5},{2,4,5},{1,6},{2,6},{0,4,6},{3,5,6},{0,7},{2,7},{3,4,7},{1,5,7},{0,8},{1,2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered74 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 74) T=TwentyFiveEightLow.Case74.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case74.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 74)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case74.support T pos))
  · decide +kernel
theorem completion75 : pairCompletion (big 75)=full 75 := by
  have same : big 75=([{0,1,3},{0,4,5},{1,4,6},{2,5,7},{3,6,7},{3,5,8},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{0,4,5},{1,4,6},{2,5,7},{3,6,7},{3,5,8},{2,6,8},{4,7,8}] [{0,2},{1,2},{0,1,3},{2,3},{2,4},{3,4},{1,5},{0,4,5},{0,6},{1,4,6},{5,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered75 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 75) T=TwentyFiveEightLow.Case75.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case75.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 75)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case75.support T pos))
  · decide +kernel
theorem completion76 : pairCompletion (big 76)=full 76 := by
  have same : big 76=([{0,1,3},{0,4,5},{2,4,6},{3,4,7},{5,6,7},{1,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{0,4,5},{2,4,6},{3,4,7},{5,6,7},{1,5,8},{3,6,8},{2,7,8}] [{0,2},{1,2},{0,1,3},{2,3},{1,4},{2,5},{3,5},{0,4,5},{0,6},{1,6},{2,4,6},{0,7},{1,7},{3,4,7},{5,6,7},{0,8},{4,8},{1,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered76 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 76) T=TwentyFiveEightLow.Case76.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case76.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 76)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case76.support T pos))
  · decide +kernel
theorem completion77 : pairCompletion (big 77)=full 77 := by
  have same : big 77=([{0,1,3},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,4,8},{1,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,4,8},{1,5,8},{6,7,8}] [{0,2},{1,2},{0,1,3},{2,3},{1,4},{0,5},{4,5},{0,6},{1,6},{2,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{2,8},{3,8},{0,4,8},{1,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered77 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 77) T=TwentyFiveEightLow.Case77.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case77.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 77)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case77.support T pos))
  · decide +kernel
theorem completion78 : pairCompletion (big 78)=full 78 := by
  have same : big 78=([{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{0,1,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{0,1,8},{5,6,8},{4,7,8}] [{0,2},{1,2},{2,3},{1,4},{0,3,4},{0,5},{1,3,5},{4,5},{0,6},{1,6},{2,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered78 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 78) T=TwentyFiveEightLow.Case78.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case78.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 78)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case78.support T pos))
  · decide +kernel
theorem completion79 : pairCompletion (big 79)=full 79 := by
  have same : big 79=([{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] [{0,1,2},{2,3},{1,4},{0,3,4},{0,5},{1,3,5},{4,5},{0,6},{1,6},{2,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered79 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 79) T=TwentyFiveEightLow.Case79.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case79.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 79)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case79.support T pos))
  · decide +kernel
theorem completion80 : pairCompletion (big 80)=full 80 := by
  have same : big 80=([{0,2,3},{0,4,5},{1,2,6},{3,4,6},{2,4,7},{3,5,7},{5,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{0,4,5},{1,2,6},{3,4,6},{2,4,7},{3,5,7},{5,6,8},{1,7,8}] [{0,1},{1,3},{0,2,3},{1,4},{1,5},{2,5},{0,4,5},{0,6},{1,2,6},{3,4,6},{0,7},{2,4,7},{3,5,7},{6,7},{0,8},{2,8},{3,8},{4,8},{5,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered80 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 80) T=TwentyFiveEightLow.Case80.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case80.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 80)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case80.support T pos))
  · decide +kernel
theorem completion81 : pairCompletion (big 81)=full 81 := by
  have same : big 81=([{0,1,3},{2,4,5},{0,4,6},{1,5,7},{3,6,7},{3,5,8},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{2,4,5},{0,4,6},{1,5,7},{3,6,7},{3,5,8},{2,6,8},{4,7,8}] [{0,2},{1,2},{0,1,3},{2,3},{1,4},{3,4},{0,5},{2,4,5},{1,6},{0,4,6},{5,6},{0,7},{2,7},{1,5,7},{3,6,7},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered81 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 81) T=TwentyFiveEightLow.Case81.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case81.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 81)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case81.support T pos))
  · decide +kernel
theorem completion82 : pairCompletion (big 82)=full 82 := by
  have same : big 82=([{0,1,3},{0,4,5},{2,4,6},{2,5,7},{3,6,7},{3,5,8},{1,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{0,4,5},{2,4,6},{2,5,7},{3,6,7},{3,5,8},{1,6,8},{4,7,8}] [{0,2},{1,2},{0,1,3},{2,3},{1,4},{3,4},{1,5},{0,4,5},{0,6},{2,4,6},{5,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,8},{2,8},{3,5,8},{1,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered82 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 82) T=TwentyFiveEightLow.Case82.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case82.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 82)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case82.support T pos))
  · decide +kernel
theorem completion83 : pairCompletion (big 83)=full 83 := by
  have same : big 83=([{0,1,3},{0,4,5},{2,4,6},{3,4,7},{5,6,7},{2,5,8},{3,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{0,4,5},{2,4,6},{3,4,7},{5,6,7},{2,5,8},{3,6,8},{1,7,8}] [{0,2},{1,2},{0,1,3},{2,3},{1,4},{1,5},{3,5},{0,4,5},{0,6},{1,6},{2,4,6},{0,7},{2,7},{3,4,7},{5,6,7},{0,8},{4,8},{2,5,8},{3,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered83 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 83) T=TwentyFiveEightLow.Case83.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case83.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 83)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case83.support T pos))
  · decide +kernel
theorem completion84 : pairCompletion (big 84)=full 84 := by
  have same : big 84=([{0,1,3},{2,4,5},{0,4,6},{3,4,7},{5,6,7},{1,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{2,4,5},{0,4,6},{3,4,7},{5,6,7},{1,5,8},{3,6,8},{2,7,8}] [{0,2},{1,2},{0,1,3},{2,3},{1,4},{0,5},{3,5},{2,4,5},{1,6},{2,6},{0,4,6},{0,7},{1,7},{3,4,7},{5,6,7},{0,8},{4,8},{1,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered84 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 84) T=TwentyFiveEightLow.Case84.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case84.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 84)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case84.support T pos))
  · decide +kernel
theorem completion85 : pairCompletion (big 85)=full 85 := by
  have same : big 85=([{0,1,3},{0,4,6},{3,5,6},{3,4,7},{2,5,7},{2,4,8},{1,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{0,4,6},{3,5,6},{3,4,7},{2,5,7},{2,4,8},{1,5,8},{6,7,8}] [{0,2},{1,2},{0,1,3},{2,3},{1,4},{0,5},{4,5},{1,6},{2,6},{0,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{0,8},{3,8},{2,4,8},{1,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered85 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 85) T=TwentyFiveEightLow.Case85.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case85.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 85)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case85.support T pos))
  · decide +kernel
theorem completion86 : pairCompletion (big 86)=full 86 := by
  have same : big 86=([{0,3,4},{2,3,5},{1,5,6},{2,4,7},{3,6,7},{0,1,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{2,3,5},{1,5,6},{2,4,7},{3,6,7},{0,1,8},{4,6,8},{5,7,8}] [{0,2},{1,2},{1,3},{1,4},{0,3,4},{0,5},{2,3,5},{4,5},{0,6},{2,6},{1,5,6},{0,7},{1,7},{2,4,7},{3,6,7},{0,1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered86 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 86) T=TwentyFiveEightLow.Case86.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case86.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 86)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case86.support T pos))
  · decide +kernel
theorem completion87 : pairCompletion (big 87)=full 87 := by
  have same : big 87=([{0,1,2},{0,3,4},{2,3,5},{1,5,6},{2,4,7},{3,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,4},{2,3,5},{1,5,6},{2,4,7},{3,6,7},{4,6,8},{5,7,8}] [{0,1,2},{1,3},{1,4},{0,3,4},{0,5},{2,3,5},{4,5},{0,6},{2,6},{1,5,6},{0,7},{1,7},{2,4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered87 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 87) T=TwentyFiveEightLow.Case87.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case87.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 87)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case87.support T pos))
  · decide +kernel
theorem completion88 : pairCompletion (big 88)=full 88 := by
  have same : big 88=([{1,2,3},{0,2,4},{0,3,5},{4,5,6},{3,4,7},{2,6,7},{1,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3},{0,2,4},{0,3,5},{4,5,6},{3,4,7},{2,6,7},{1,6,8},{5,7,8}] [{0,1},{1,2,3},{1,4},{0,2,4},{1,5},{2,5},{0,3,5},{0,6},{3,6},{4,5,6},{0,7},{1,7},{3,4,7},{2,6,7},{0,8},{2,8},{3,8},{4,8},{1,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered88 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 88) T=TwentyFiveEightLow.Case88.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case88.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 88)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case88.support T pos))
  · decide +kernel
theorem completion89 : pairCompletion (big 89)=full 89 := by
  have same : big 89=([{1,2,4},{0,2,5},{3,4,5},{0,3,6},{2,3,7},{4,6,7},{5,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,4},{0,2,5},{3,4,5},{0,3,6},{2,3,7},{4,6,7},{5,6,8},{1,7,8}] [{0,1},{1,3},{0,4},{1,2,4},{1,5},{0,2,5},{3,4,5},{1,6},{2,6},{0,3,6},{0,7},{2,3,7},{5,7},{4,6,7},{0,8},{2,8},{3,8},{4,8},{5,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered89 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 89) T=TwentyFiveEightLow.Case89.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case89.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 89)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case89.support T pos))
  · decide +kernel
theorem completion90 : pairCompletion (big 90)=full 90 := by
  have same : big 90=([{0,1,3},{2,4,5},{0,4,6},{1,5,7},{3,6,7},{2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{2,4,5},{0,4,6},{1,5,7},{3,6,7},{2,3,8},{5,6,8},{4,7,8}] [{0,2},{1,2},{0,1,3},{1,4},{3,4},{0,5},{3,5},{2,4,5},{1,6},{2,6},{0,4,6},{0,7},{2,7},{1,5,7},{3,6,7},{0,8},{1,8},{2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered90 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 90) T=TwentyFiveEightLow.Case90.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case90.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 90)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case90.support T pos))
  · decide +kernel
theorem completion91 : pairCompletion (big 91)=full 91 := by
  have same : big 91=([{0,1,3},{2,4,5},{0,4,6},{2,3,7},{5,6,7},{1,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{2,4,5},{0,4,6},{2,3,7},{5,6,7},{1,5,8},{3,6,8},{4,7,8}] [{0,2},{1,2},{0,1,3},{1,4},{3,4},{0,5},{3,5},{2,4,5},{1,6},{2,6},{0,4,6},{0,7},{1,7},{2,3,7},{5,6,7},{0,8},{2,8},{1,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered91 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 91) T=TwentyFiveEightLow.Case91.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case91.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 91)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case91.support T pos))
  · decide +kernel
theorem completion92 : pairCompletion (big 92)=full 92 := by
  have same : big 92=([{0,1,3},{0,4,5},{2,3,6},{3,5,7},{4,6,7},{2,4,8},{5,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{0,4,5},{2,3,6},{3,5,7},{4,6,7},{2,4,8},{5,6,8},{1,7,8}] [{0,2},{1,2},{0,1,3},{1,4},{3,4},{1,5},{2,5},{0,4,5},{0,6},{1,6},{2,3,6},{0,7},{2,7},{3,5,7},{4,6,7},{0,8},{3,8},{2,4,8},{5,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered92 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 92) T=TwentyFiveEightLow.Case92.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case92.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 92)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case92.support T pos))
  · decide +kernel
theorem completion93 : pairCompletion (big 93)=full 93 := by
  have same : big 93=([{2,3,4},{0,3,5},{1,4,6},{4,5,7},{3,6,7},{0,1,8},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{0,3,5},{1,4,6},{4,5,7},{3,6,7},{0,1,8},{5,6,8},{2,7,8}] [{0,2},{1,2},{1,3},{0,4},{2,3,4},{1,5},{2,5},{0,3,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{4,5,7},{3,6,7},{0,1,8},{3,8},{4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered93 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 93) T=TwentyFiveEightLow.Case93.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case93.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 93)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case93.support T pos))
  · decide +kernel
theorem completion94 : pairCompletion (big 94)=full 94 := by
  have same : big 94=([{0,1,2},{2,3,4},{0,3,5},{1,4,6},{4,5,7},{3,6,7},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{2,3,4},{0,3,5},{1,4,6},{4,5,7},{3,6,7},{5,6,8},{2,7,8}] [{0,1,2},{1,3},{0,4},{2,3,4},{1,5},{2,5},{0,3,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{4,5,7},{3,6,7},{0,8},{1,8},{3,8},{4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered94 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 94) T=TwentyFiveEightLow.Case94.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case94.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 94)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case94.support T pos))
  · decide +kernel
theorem completion95 : pairCompletion (big 95)=full 95 := by
  have same : big 95=([{0,3,4},{1,2,5},{0,2,6},{4,5,6},{2,4,7},{3,5,7},{1,3,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,2,5},{0,2,6},{4,5,6},{2,4,7},{3,5,7},{1,3,8},{6,7,8}] [{0,1},{2,3},{1,4},{0,3,4},{0,5},{1,2,5},{1,6},{0,2,6},{3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,8},{2,8},{1,3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered95 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 95) T=TwentyFiveEightLow.Case95.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case95.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 95)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case95.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
