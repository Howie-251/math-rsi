import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion32 : pairCompletion (big 32)=full 32 := by
  have same : big 32=([{0,1,2},{0,3,5},{1,5,6},{4,5,7},{3,6,7},{4,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,5},{1,5,6},{4,5,7},{3,6,7},{4,6,8},{2,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{2,5},{0,3,5},{0,6},{2,6},{1,5,6},{0,7},{1,7},{4,5,7},{3,6,7},{0,8},{1,8},{3,8},{5,8},{4,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered32 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 32) T=TwentyFiveEightLow.Case32.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case32.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 32)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case32.support T pos))
  · decide +kernel
theorem completion33 : pairCompletion (big 33)=full 33 := by
  have same : big 33=([{0,1,5},{0,3,6},{4,5,6},{2,4,7},{3,5,7},{1,2,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{0,3,6},{4,5,6},{2,4,7},{3,5,7},{1,2,8},{6,7,8}] [{0,2},{1,3},{2,3},{0,4},{1,4},{3,4},{0,1,5},{2,5},{1,6},{2,6},{0,3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,8},{1,2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered33 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 33) T=TwentyFiveEightLow.Case33.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case33.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 33)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case33.support T pos))
  · decide +kernel
theorem completion34 : pairCompletion (big 34)=full 34 := by
  have same : big 34=([{0,1,5},{0,2,6},{4,5,6},{2,5,7},{3,6,7},{1,3,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{0,2,6},{4,5,6},{2,5,7},{3,6,7},{1,3,8},{4,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,1,5},{3,5},{1,6},{0,2,6},{4,5,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,8},{2,8},{1,3,8},{5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered34 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 34) T=TwentyFiveEightLow.Case34.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case34.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 34)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case34.support T pos))
  · decide +kernel
theorem completion35 : pairCompletion (big 35)=full 35 := by
  have same : big 35=([{0,1,5},{2,3,6},{4,5,6},{2,5,7},{1,6,7},{0,4,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{2,3,6},{4,5,6},{2,5,7},{1,6,7},{0,4,8},{3,7,8}] [{0,2},{1,2},{0,3},{1,3},{1,4},{2,4},{3,4},{0,1,5},{3,5},{0,6},{2,3,6},{4,5,6},{0,7},{4,7},{2,5,7},{1,6,7},{1,8},{2,8},{0,4,8},{5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered35 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 35) T=TwentyFiveEightLow.Case35.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case35.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 35)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case35.support T pos))
  · decide +kernel
theorem completion36 : pairCompletion (big 36)=full 36 := by
  have same : big 36=([{0,1,2},{0,3,6},{4,5,7},{1,6,7},{3,4,8},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,6},{4,5,7},{1,6,7},{3,4,8},{5,6,8},{2,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,5},{2,6},{0,3,6},{4,6},{0,7},{3,7},{4,5,7},{1,6,7},{0,8},{1,8},{3,4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered36 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 36) T=TwentyFiveEightLow.Case36.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case36.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 36)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case36.support T pos))
  · decide +kernel
theorem completion37 : pairCompletion (big 37)=full 37 := by
  have same : big 37=([{0,1,2},{0,3,6},{3,4,7},{5,6,7},{4,5,8},{1,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,6},{3,4,7},{5,6,7},{4,5,8},{1,6,8},{2,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,5},{2,6},{0,3,6},{4,6},{0,7},{1,7},{3,4,7},{5,6,7},{0,8},{3,8},{4,5,8},{1,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered37 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 37) T=TwentyFiveEightLow.Case37.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case37.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 37)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case37.support T pos))
  · decide +kernel
theorem completion38 : pairCompletion (big 38)=full 38 := by
  have same : big 38=([{0,1,2},{3,5,6},{3,4,7},{1,6,7},{0,4,8},{2,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{3,5,6},{3,4,7},{1,6,7},{0,4,8},{2,6,8},{5,7,8}] [{0,1,2},{0,3},{1,3},{2,3},{1,4},{2,4},{0,5},{1,5},{2,5},{4,5},{0,6},{4,6},{3,5,6},{0,7},{2,7},{3,4,7},{1,6,7},{1,8},{3,8},{0,4,8},{2,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered38 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 38) T=TwentyFiveEightLow.Case38.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case38.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 38)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case38.support T pos))
  · decide +kernel
theorem completion39 : pairCompletion (big 39)=full 39 := by
  have same : big 39=([{0,1,2},{0,3,5},{3,4,6},{1,5,7},{2,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,5},{3,4,6},{1,5,7},{2,6,7},{5,6,8},{4,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{1,4},{2,4},{2,5},{0,3,5},{4,5},{0,6},{1,6},{3,4,6},{0,7},{3,7},{1,5,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered39 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 39) T=TwentyFiveEightLow.Case39.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case39.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 39)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case39.support T pos))
  · decide +kernel
theorem completion40 : pairCompletion (big 40)=full 40 := by
  have same : big 40=([{0,1,2},{0,3,5},{1,5,6},{4,5,7},{2,6,7},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,5},{1,5,6},{4,5,7},{2,6,7},{4,6,8},{3,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{2,5},{0,3,5},{0,6},{3,6},{1,5,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered40 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 40) T=TwentyFiveEightLow.Case40.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case40.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 40)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case40.support T pos))
  · decide +kernel
theorem completion41 : pairCompletion (big 41)=full 41 := by
  have same : big 41=([{0,1,2},{3,4,5},{0,5,6},{1,5,7},{3,6,7},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{3,4,5},{0,5,6},{1,5,7},{3,6,7},{2,6,8},{4,7,8}] [{0,1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{2,5},{3,4,5},{1,6},{4,6},{0,5,6},{0,7},{2,7},{1,5,7},{3,6,7},{0,8},{1,8},{3,8},{5,8},{2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered41 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 41) T=TwentyFiveEightLow.Case41.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case41.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 41)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case41.support T pos))
  · decide +kernel
theorem completion42 : pairCompletion (big 42)=full 42 := by
  have same : big 42=([{0,2,5},{0,1,6},{3,5,6},{1,3,7},{4,5,7},{2,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,5},{0,1,6},{3,5,6},{1,3,7},{4,5,7},{2,4,8},{6,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{1,5},{0,2,5},{0,1,6},{2,6},{4,6},{3,5,6},{0,7},{2,7},{1,3,7},{4,5,7},{0,8},{1,8},{3,8},{2,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered42 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 42) T=TwentyFiveEightLow.Case42.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case42.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 42)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case42.support T pos))
  · decide +kernel
theorem completion43 : pairCompletion (big 43)=full 43 := by
  have same : big 43=([{0,1,5},{0,2,6},{3,5,6},{1,3,7},{4,5,7},{2,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{0,2,6},{3,5,6},{1,3,7},{4,5,7},{2,4,8},{6,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{0,1,5},{2,5},{1,6},{0,2,6},{4,6},{3,5,6},{0,7},{2,7},{1,3,7},{4,5,7},{0,8},{1,8},{3,8},{2,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered43 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 43) T=TwentyFiveEightLow.Case43.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case43.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 43)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case43.support T pos))
  · decide +kernel
theorem completion44 : pairCompletion (big 44)=full 44 := by
  have same : big 44=([{0,1,5},{0,2,6},{3,5,6},{4,5,7},{1,6,7},{3,4,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{0,2,6},{3,5,6},{4,5,7},{1,6,7},{3,4,8},{2,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,1,5},{2,5},{0,2,6},{4,6},{3,5,6},{0,7},{3,7},{4,5,7},{1,6,7},{0,8},{1,8},{3,4,8},{5,8},{6,8},{2,7,8}]=true
  decide +kernel

theorem recovered44 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 44) T=TwentyFiveEightLow.Case44.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case44.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 44)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case44.support T pos))
  · decide +kernel
theorem completion45 : pairCompletion (big 45)=full 45 := by
  have same : big 45=([{0,1,2},{1,4,6},{3,5,6},{3,4,7},{2,5,7},{0,3,8},{2,4,8},{1,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{1,4,6},{3,5,6},{3,4,7},{2,5,7},{0,3,8},{2,4,8},{1,5,8},{6,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{0,5},{4,5},{0,6},{2,6},{1,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{0,3,8},{2,4,8},{1,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered45 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 45) T=TwentyFiveEightLow.Case45.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case45.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 45)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case45.support T pos))
  · decide +kernel
theorem completion46 : pairCompletion (big 46)=full 46 := by
  have same : big 46=([{0,1,2},{1,4,5},{3,4,6},{0,3,7},{2,5,7},{1,6,7},{3,5,8},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{1,4,5},{3,4,6},{0,3,7},{2,5,7},{1,6,7},{3,5,8},{2,6,8},{4,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{2,4},{0,5},{1,4,5},{0,6},{3,4,6},{5,6},{0,3,7},{2,5,7},{1,6,7},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered46 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 46) T=TwentyFiveEightLow.Case46.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case46.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 46)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case46.support T pos))
  · decide +kernel
theorem completion47 : pairCompletion (big 47)=full 47 := by
  have same : big 47=([{0,1,2},{1,4,5},{3,4,6},{0,3,7},{2,4,7},{5,6,7},{3,5,8},{2,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{1,4,5},{3,4,6},{0,3,7},{2,4,7},{5,6,7},{3,5,8},{2,6,8},{1,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{0,5},{2,5},{1,4,5},{0,6},{1,6},{3,4,6},{0,3,7},{2,4,7},{5,6,7},{0,8},{4,8},{3,5,8},{2,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered47 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 47) T=TwentyFiveEightLow.Case47.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case47.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 47)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case47.support T pos))
  · decide +kernel
theorem completion48 : pairCompletion (big 48)=full 48 := by
  have same : big 48=([{0,1,2},{1,3,5},{2,4,6},{2,3,7},{1,4,7},{5,6,7},{4,5,8},{3,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{1,3,5},{2,4,6},{2,3,7},{1,4,7},{5,6,7},{4,5,8},{3,6,8},{0,7,8}] [{0,1,2},{0,3},{0,4},{3,4},{0,5},{2,5},{1,3,5},{0,6},{1,6},{2,4,6},{2,3,7},{1,4,7},{5,6,7},{1,8},{2,8},{4,5,8},{3,6,8},{0,7,8}]=true
  decide +kernel

theorem recovered48 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 48) T=TwentyFiveEightLow.Case48.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case48.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 48)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case48.support T pos))
  · decide +kernel
theorem completion49 : pairCompletion (big 49)=full 49 := by
  have same : big 49=([{2,3,4},{1,3,5},{1,4,6},{0,1,7},{2,5,7},{3,6,7},{0,2,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{1,3,5},{1,4,6},{0,1,7},{2,5,7},{3,6,7},{0,2,8},{5,6,8},{4,7,8}] [{1,2},{0,3},{0,4},{2,3,4},{0,5},{1,3,5},{4,5},{0,6},{2,6},{1,4,6},{0,1,7},{2,5,7},{3,6,7},{1,8},{0,2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered49 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 49) T=TwentyFiveEightLow.Case49.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case49.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 49)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case49.support T pos))
  · decide +kernel
theorem completion50 : pairCompletion (big 50)=full 50 := by
  have same : big 50=([{0,2,4},{1,3,4},{1,2,5},{0,3,6},{0,1,7},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4},{1,3,4},{1,2,5},{0,3,6},{0,1,7},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] [{2,3},{0,2,4},{1,3,4},{0,5},{1,2,5},{4,5},{1,6},{0,3,6},{4,6},{0,1,7},{3,5,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered50 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 50) T=TwentyFiveEightLow.Case50.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case50.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 50)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case50.support T pos))
  · decide +kernel
theorem completion51 : pairCompletion (big 51)=full 51 := by
  have same : big 51=([{0,1,2},{3,4,6},{3,5,7},{0,6,7},{4,5,8},{1,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{3,4,6},{3,5,7},{0,6,7},{4,5,8},{1,6,8},{2,7,8}] [{0,1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{2,6},{3,4,6},{5,6},{1,7},{4,7},{3,5,7},{0,6,7},{0,8},{3,8},{4,5,8},{1,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered51 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 51) T=TwentyFiveEightLow.Case51.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case51.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 51)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case51.support T pos))
  · decide +kernel
theorem completion52 : pairCompletion (big 52)=full 52 := by
  have same : big 52=([{0,1,2},{3,4,5},{0,5,6},{1,5,7},{2,6,7},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{3,4,5},{0,5,6},{1,5,7},{2,6,7},{3,6,8},{4,7,8}] [{0,1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{2,5},{3,4,5},{1,6},{4,6},{0,5,6},{0,7},{3,7},{1,5,7},{2,6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered52 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 52) T=TwentyFiveEightLow.Case52.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case52.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 52)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case52.support T pos))
  · decide +kernel
theorem completion53 : pairCompletion (big 53)=full 53 := by
  have same : big 53=([{0,1,5},{0,2,6},{3,5,6},{1,2,7},{4,5,7},{3,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{0,2,6},{3,5,6},{1,2,7},{4,5,7},{3,4,8},{6,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,1,5},{2,5},{1,6},{0,2,6},{4,6},{3,5,6},{0,7},{1,2,7},{3,7},{4,5,7},{0,8},{1,8},{2,8},{3,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered53 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 53) T=TwentyFiveEightLow.Case53.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case53.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 53)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case53.support T pos))
  · decide +kernel
theorem completion54 : pairCompletion (big 54)=full 54 := by
  have same : big 54=([{0,1,3},{0,2,4},{1,2,7},{3,5,7},{4,6,7},{5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{0,2,4},{1,2,7},{3,5,7},{4,6,7},{5,6,8}] [{0,1,3},{2,3},{1,4},{0,2,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{0,7},{1,2,7},{3,5,7},{4,6,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,6,8},{7,8}]=true
  decide +kernel

theorem recovered54 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 54) T=TwentyFiveEightLow.Case54.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case54.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 54)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case54.support T pos))
  · decide +kernel
theorem completion55 : pairCompletion (big 55)=full 55 := by
  have same : big 55=([{0,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,1,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,1,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{1,4},{1,5},{0,4,5},{0,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{1,6,7},{0,1,8},{2,8},{3,8},{4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered55 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 55) T=TwentyFiveEightLow.Case55.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case55.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 55)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case55.support T pos))
  · decide +kernel
theorem completion56 : pairCompletion (big 56)=full 56 := by
  have same : big 56=([{0,1,2},{3,5,7},{4,6,7},{0,3,8},{1,4,8},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{3,5,7},{4,6,7},{0,3,8},{1,4,8},{5,6,8},{2,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,3,8},{1,4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered56 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 56) T=TwentyFiveEightLow.Case56.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case56.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 56)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case56.support T pos))
  · decide +kernel
theorem completion57 : pairCompletion (big 57)=full 57 := by
  have same : big 57=([{0,1,2},{0,3,7},{1,4,7},{5,6,7},{3,5,8},{4,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,7},{1,4,7},{5,6,7},{3,5,8},{4,6,8},{2,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{0,3,7},{1,4,7},{5,6,7},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered57 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 57) T=TwentyFiveEightLow.Case57.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case57.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 57)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case57.support T pos))
  · decide +kernel
theorem completion58 : pairCompletion (big 58)=full 58 := by
  have same : big 58=([{0,1,2},{3,4,6},{0,3,7},{1,5,7},{2,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{3,4,6},{0,3,7},{1,5,7},{2,6,7},{5,6,8},{4,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{2,5},{3,5},{4,5},{0,6},{1,6},{3,4,6},{0,3,7},{1,5,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered58 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 58) T=TwentyFiveEightLow.Case58.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case58.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 58)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case58.support T pos))
  · decide +kernel
theorem completion59 : pairCompletion (big 59)=full 59 := by
  have same : big 59=([{0,1,2},{3,4,6},{0,3,7},{4,5,7},{1,6,7},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{3,4,6},{0,3,7},{4,5,7},{1,6,7},{5,6,8},{2,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,5},{0,6},{2,6},{3,4,6},{0,3,7},{4,5,7},{1,6,7},{0,8},{1,8},{3,8},{4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered59 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 59) T=TwentyFiveEightLow.Case59.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case59.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 59)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case59.support T pos))
  · decide +kernel
theorem completion60 : pairCompletion (big 60)=full 60 := by
  have same : big 60=([{0,2,6},{1,3,6},{0,1,7},{2,4,7},{3,5,7},{4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,6},{1,3,6},{0,1,7},{2,4,7},{3,5,7},{4,5,8},{6,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{0,2,6},{1,3,6},{4,6},{5,6},{0,1,7},{2,4,7},{3,5,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered60 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 60) T=TwentyFiveEightLow.Case60.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case60.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 60)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case60.support T pos))
  · decide +kernel
theorem completion61 : pairCompletion (big 61)=full 61 := by
  have same : big 61=([{0,1,6},{2,3,6},{0,2,7},{1,4,7},{5,6,7},{4,5,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{2,3,6},{0,2,7},{1,4,7},{5,6,7},{4,5,8},{3,7,8}] [{1,2},{0,3},{1,3},{0,4},{2,4},{3,4},{0,5},{1,5},{2,5},{3,5},{0,1,6},{2,3,6},{4,6},{0,2,7},{1,4,7},{5,6,7},{0,8},{1,8},{2,8},{4,5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered61 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 61) T=TwentyFiveEightLow.Case61.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case61.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 61)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case61.support T pos))
  · decide +kernel
theorem completion62 : pairCompletion (big 62)=full 62 := by
  have same : big 62=([{0,1,3},{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] [{1,2},{0,1,3},{2,3},{1,4},{0,2,4},{3,4},{0,5},{2,5},{0,6},{2,6},{1,5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered62 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 62) T=TwentyFiveEightLow.Case62.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case62.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 62)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case62.support T pos))
  · decide +kernel
theorem completion63 : pairCompletion (big 63)=full 63 := by
  have same : big 63=([{0,1,3},{1,4,5},{3,4,6},{3,5,7},{2,6,7},{0,2,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{1,4,5},{3,4,6},{3,5,7},{2,6,7},{0,2,8},{5,6,8},{4,7,8}] [{1,2},{0,1,3},{2,3},{0,4},{2,4},{0,5},{2,5},{1,4,5},{0,6},{1,6},{3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{1,8},{0,2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered63 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 63) T=TwentyFiveEightLow.Case63.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case63.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 63)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case63.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
