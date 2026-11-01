import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion320 : pairCompletion (big 320)=full 320 := by
  have same : big 320=([{0,1,2,3},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{1,4,5,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{1,4,5,8}] [{0,1,2,3},{0,4},{0,5},{0,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{1,6,7},{0,8},{2,8},{3,8},{1,4,5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered320 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 320) T=TwentyFiveEightLow.Case320.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case320.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 320)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case320.support T pos))
  · decide +kernel
theorem completion321 : pairCompletion (big 321)=full 321 := by
  have same : big 321=([{0,2,3,4},{1,5,6,7},{2,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{1,5,6,7},{2,5,8},{3,6,8},{4,7,8}] [{0,1},{1,2},{1,3},{1,4},{0,2,3,4},{0,5},{3,5},{4,5},{0,6},{2,6},{4,6},{0,7},{2,7},{3,7},{1,5,6,7},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered321 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 321) T=TwentyFiveEightLow.Case321.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case321.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 321)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case321.support T pos))
  · decide +kernel
theorem completion322 : pairCompletion (big 322)=full 322 := by
  have same : big 322=([{0,2,3,6},{2,4,7},{3,5,7},{1,4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,6},{2,4,7},{3,5,7},{1,4,5,8},{6,7,8}] [{0,1},{1,2},{1,3},{0,4},{3,4},{0,5},{2,5},{1,6},{0,2,3,6},{4,6},{5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,8},{2,8},{3,8},{1,4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered322 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 322) T=TwentyFiveEightLow.Case322.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case322.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 322)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case322.support T pos))
  · decide +kernel
theorem completion323 : pairCompletion (big 323)=full 323 := by
  have same : big 323=([{0,1,2,3},{1,4,7},{2,5,7},{3,6,7},{4,5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{1,4,7},{2,5,7},{3,6,7},{4,5,6,8}] [{0,1,2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{3,5},{0,6},{1,6},{2,6},{0,7},{1,4,7},{2,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,5,6,8},{7,8}]=true
  decide +kernel

theorem recovered323 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 323) T=TwentyFiveEightLow.Case323.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case323.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 323)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case323.support T pos))
  · decide +kernel
theorem completion324 : pairCompletion (big 324)=full 324 := by
  have same : big 324=([{0,1,2,3},{0,4,5},{1,4,6},{3,5,6},{3,4,7},{2,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,5},{1,4,6},{3,5,6},{3,4,7},{2,5,7},{6,7,8}] [{0,1,2,3},{2,4},{1,5},{0,4,5},{0,6},{2,6},{1,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered324 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 324) T=TwentyFiveEightLow.Case324.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case324.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 324)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case324.support T pos))
  · decide +kernel
theorem completion325 : pairCompletion (big 325)=full 325 := by
  have same : big 325=([{0,1,2,3},{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,7,8}] [{0,1,2,3},{0,4},{0,5},{1,4,5},{0,6},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{1,8},{2,8},{3,8},{4,8},{5,8},{6,8},{0,7,8}]=true
  decide +kernel

theorem recovered325 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 325) T=TwentyFiveEightLow.Case325.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case325.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 325)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case325.support T pos))
  · decide +kernel
theorem completion326 : pairCompletion (big 326)=full 326 := by
  have same : big 326=([{1,2,3,4},{3,5,6},{0,1,7},{4,5,7},{2,6,7},{0,2,8},{1,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3,4},{3,5,6},{0,1,7},{4,5,7},{2,6,7},{0,2,8},{1,5,8},{4,6,8},{3,7,8}] [{0,3},{0,4},{1,2,3,4},{0,5},{2,5},{0,6},{1,6},{3,5,6},{0,1,7},{4,5,7},{2,6,7},{0,2,8},{1,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered326 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 326) T=TwentyFiveEightLow.Case326.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case326.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 326)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case326.support T pos))
  · decide +kernel
theorem completion327 : pairCompletion (big 327)=full 327 := by
  have same : big 327=([{1,2,3,4},{0,1,6},{3,5,6},{0,2,7},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3,4},{0,1,6},{3,5,6},{0,2,7},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}] [{0,3},{0,4},{1,2,3,4},{0,5},{2,5},{0,1,6},{3,5,6},{0,2,7},{1,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered327 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 327) T=TwentyFiveEightLow.Case327.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case327.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 327)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case327.support T pos))
  · decide +kernel
theorem completion328 : pairCompletion (big 328)=full 328 := by
  have same : big 328=([{3,4,5},{0,1,6},{2,4,6},{0,2,7},{1,5,7},{3,6,7},{1,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,1,6},{2,4,6},{0,2,7},{1,5,7},{3,6,7},{1,2,3,8},{5,6,8},{4,7,8}] [{0,3},{0,4},{1,4},{0,5},{2,5},{3,4,5},{0,1,6},{2,4,6},{0,2,7},{1,5,7},{3,6,7},{0,8},{1,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered328 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 328) T=TwentyFiveEightLow.Case328.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case328.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 328)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case328.support T pos))
  · decide +kernel
theorem completion329 : pairCompletion (big 329)=full 329 := by
  have same : big 329=([{0,1,6},{2,4,6},{3,5,6},{0,2,7},{3,4,7},{1,5,7},{1,2,3,8},{4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{2,4,6},{3,5,6},{0,2,7},{3,4,7},{1,5,7},{1,2,3,8},{4,5,8},{6,7,8}] [{0,3},{0,4},{1,4},{0,5},{2,5},{0,1,6},{2,4,6},{3,5,6},{0,2,7},{3,4,7},{1,5,7},{0,8},{1,2,3,8},{4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered329 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 329) T=TwentyFiveEightLow.Case329.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case329.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 329)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case329.support T pos))
  · decide +kernel
theorem completion330 : pairCompletion (big 330)=full 330 := by
  have same : big 330=([{2,4,5},{0,1,6},{3,4,6},{1,4,7},{3,5,7},{2,6,7},{1,2,3,8},{5,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{0,1,6},{3,4,6},{1,4,7},{3,5,7},{2,6,7},{1,2,3,8},{5,6,8},{0,7,8}] [{0,2},{0,3},{0,4},{0,5},{1,5},{2,4,5},{0,1,6},{3,4,6},{1,4,7},{3,5,7},{2,6,7},{1,2,3,8},{4,8},{5,6,8},{0,7,8}]=true
  decide +kernel

theorem recovered330 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 330) T=TwentyFiveEightLow.Case330.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case330.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 330)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case330.support T pos))
  · decide +kernel
theorem completion331 : pairCompletion (big 331)=full 331 := by
  have same : big 331=([{0,1,2,3},{0,4,5},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,5},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{3,6,8},{2,7,8}] [{0,1,2,3},{2,4},{3,5},{0,4,5},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{0,8},{1,8},{4,8},{5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered331 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 331) T=TwentyFiveEightLow.Case331.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case331.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 331)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case331.support T pos))
  · decide +kernel
theorem completion332 : pairCompletion (big 332)=full 332 := by
  have same : big 332=([{0,1,2,3},{1,4,5},{2,4,6},{3,5,6},{0,4,7},{2,5,7},{1,6,7},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{1,4,5},{2,4,6},{3,5,6},{0,4,7},{2,5,7},{1,6,7},{3,7,8}] [{0,1,2,3},{3,4},{0,5},{1,4,5},{0,6},{2,4,6},{3,5,6},{0,4,7},{2,5,7},{1,6,7},{0,8},{1,8},{2,8},{4,8},{5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered332 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 332) T=TwentyFiveEightLow.Case332.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case332.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 332)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case332.support T pos))
  · decide +kernel
theorem completion333 : pairCompletion (big 333)=full 333 := by
  have same : big 333=([{0,1,2,3},{0,4,6},{1,5,6},{4,5,7},{2,6,7},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,6},{1,5,6},{4,5,7},{2,6,7},{3,7,8}] [{0,1,2,3},{1,4},{2,4},{3,4},{0,5},{2,5},{3,5},{3,6},{0,4,6},{1,5,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,8},{1,8},{2,8},{4,8},{5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered333 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 333) T=TwentyFiveEightLow.Case333.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case333.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 333)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case333.support T pos))
  · decide +kernel
theorem completion334 : pairCompletion (big 334)=full 334 := by
  have same : big 334=([{0,1,2,3},{0,4,6},{2,5,6},{1,4,7},{3,6,7},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,6},{2,5,6},{1,4,7},{3,6,7},{5,7,8}] [{0,1,2,3},{2,4},{3,4},{0,5},{1,5},{3,5},{4,5},{1,6},{0,4,6},{2,5,6},{0,7},{2,7},{1,4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered334 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 334) T=TwentyFiveEightLow.Case334.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case334.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 334)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case334.support T pos))
  · decide +kernel
theorem completion335 : pairCompletion (big 335)=full 335 := by
  have same : big 335=([{0,1,2,3},{0,4,6},{1,5,6},{2,4,7},{3,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,6},{1,5,6},{2,4,7},{3,5,7},{6,7,8}] [{0,1,2,3},{1,4},{3,4},{0,5},{2,5},{4,5},{2,6},{3,6},{0,4,6},{1,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered335 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 335) T=TwentyFiveEightLow.Case335.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case335.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 335)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case335.support T pos))
  · decide +kernel
theorem completion336 : pairCompletion (big 336)=full 336 := by
  have same : big 336=([{0,1,2,3},{4,5,6},{0,4,7},{1,5,7},{2,6,7},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{4,5,6},{0,4,7},{1,5,7},{2,6,7},{3,7,8}] [{0,1,2,3},{1,4},{2,4},{3,4},{0,5},{2,5},{3,5},{0,6},{1,6},{3,6},{4,5,6},{0,4,7},{1,5,7},{2,6,7},{0,8},{1,8},{2,8},{4,8},{5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered336 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 336) T=TwentyFiveEightLow.Case336.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case336.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 336)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case336.support T pos))
  · decide +kernel
theorem completion337 : pairCompletion (big 337)=full 337 := by
  have same : big 337=([{0,1,2,3,4},{0,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,4},{0,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}] [{0,1,2,3,4},{2,5},{3,5},{1,6},{3,6},{0,5,6},{0,7},{2,7},{1,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered337 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 337) T=TwentyFiveEightLow.Case337.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case337.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 337)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case337.support T pos))
  · decide +kernel
theorem completion338 : pairCompletion (big 338)=full 338 := by
  have same : big 338=([{0,4,5},{1,4,6},{2,5,7},{3,6,7},{0,1,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{1,4,6},{2,5,7},{3,6,7},{0,1,2,3,8},{5,6,8},{4,7,8}] [{2,4},{3,4},{1,5},{3,5},{0,4,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,1,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered338 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 338) T=TwentyFiveEightLow.Case338.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case338.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 338)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case338.support T pos))
  · decide +kernel
theorem completion339 : pairCompletion (big 339)=full 339 := by
  have same : big 339=([{0,4,5},{1,4,6},{3,5,6},{3,4,7},{2,5,7},{0,1,2,3,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{1,4,6},{3,5,6},{3,4,7},{2,5,7},{0,1,2,3,8},{6,7,8}] [{2,4},{1,5},{0,4,5},{0,6},{2,6},{1,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{0,1,2,3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered339 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 339) T=TwentyFiveEightLow.Case339.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case339.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 339)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case339.support T pos))
  · decide +kernel
theorem completion340 : pairCompletion (big 340)=full 340 := by
  have same : big 340=([{0,1,2,3,4},{1,5,6},{2,5,7},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,4},{1,5,6},{2,5,7},{3,6,8},{4,7,8}] [{0,1,2,3,4},{0,5},{3,5},{4,5},{0,6},{2,6},{4,6},{1,5,6},{0,7},{1,7},{3,7},{2,5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered340 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 340) T=TwentyFiveEightLow.Case340.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case340.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 340)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case340.support T pos))
  · decide +kernel
theorem completion341 : pairCompletion (big 341)=full 341 := by
  have same : big 341=([{1,4,5},{2,4,6},{3,5,7},{0,1,2,3,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,5},{2,4,6},{3,5,7},{0,1,2,3,8},{6,7,8}] [{0,4},{3,4},{0,5},{2,5},{1,4,5},{0,6},{1,6},{3,6},{2,4,6},{5,6},{0,7},{1,7},{2,7},{4,7},{3,5,7},{0,1,2,3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered341 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 341) T=TwentyFiveEightLow.Case341.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case341.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 341)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case341.support T pos))
  · decide +kernel
theorem completion342 : pairCompletion (big 342)=full 342 := by
  have same : big 342=([{0,4,5},{1,4,6},{2,5,7},{3,6,7},{0,1,2,3,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{1,4,6},{2,5,7},{3,6,7},{0,1,2,3,8}] [{2,4},{3,4},{1,5},{3,5},{0,4,5},{0,6},{2,6},{1,4,6},{5,6},{0,7},{1,7},{4,7},{2,5,7},{3,6,7},{0,1,2,3,8},{4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered342 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 342) T=TwentyFiveEightLow.Case342.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case342.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 342)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case342.support T pos))
  · decide +kernel
theorem completion343 : pairCompletion (big 343)=full 343 := by
  have same : big 343=([{0,1,2,3,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,1,2,3,4},{0,5},{2,5},{0,6},{2,6},{1,5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered343 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 343) T=TwentyFiveEightLow.Case343.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case343.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 343)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case343.support T pos))
  · decide +kernel
theorem completion344 : pairCompletion (big 344)=full 344 := by
  have same : big 344=([{1,4,5},{3,4,6},{3,5,7},{2,6,7},{0,1,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,5},{3,4,6},{3,5,7},{2,6,7},{0,1,2,3,8},{5,6,8},{4,7,8}] [{0,4},{2,4},{0,5},{2,5},{1,4,5},{0,6},{1,6},{3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,1,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered344 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 344) T=TwentyFiveEightLow.Case344.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case344.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 344)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case344.support T pos))
  · decide +kernel
theorem completion345 : pairCompletion (big 345)=full 345 := by
  have same : big 345=([{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,1,2,3,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,1,2,3,8},{6,7,8}] [{0,4},{0,5},{1,4,5},{0,6},{1,6},{2,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{0,1,2,3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered345 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 345) T=TwentyFiveEightLow.Case345.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case345.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 345)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case345.support T pos))
  · decide +kernel
theorem completion346 : pairCompletion (big 346)=full 346 := by
  have same : big 346=([{0,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,1,2,3,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,1,2,3,8}] [{1,4},{1,5},{0,4,5},{0,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{1,6,7},{0,1,2,3,8},{4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered346 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 346) T=TwentyFiveEightLow.Case346.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case346.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 346)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case346.support T pos))
  · decide +kernel
theorem completion347 : pairCompletion (big 347)=full 347 := by
  have same : big 347=([{0,1,2,3,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,1,2,3,4},{0,5},{1,5},{0,6},{1,6},{2,5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered347 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 347) T=TwentyFiveEightLow.Case347.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case347.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 347)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case347.support T pos))
  · decide +kernel
theorem completion348 : pairCompletion (big 348)=full 348 := by
  have same : big 348=([{2,4,5},{3,4,6},{3,5,7},{2,6,7},{0,1,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{3,4,6},{3,5,7},{2,6,7},{0,1,2,3,8},{5,6,8},{4,7,8}] [{0,4},{1,4},{0,5},{1,5},{2,4,5},{0,6},{1,6},{3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,1,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered348 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 348) T=TwentyFiveEightLow.Case348.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case348.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 348)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case348.support T pos))
  · decide +kernel
theorem completion349 : pairCompletion (big 349)=full 349 := by
  have same : big 349=([{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,1,2,3,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,1,2,3,8}] [{0,4},{0,5},{1,4,5},{0,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{1,6,7},{0,1,2,3,8},{4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered349 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 349) T=TwentyFiveEightLow.Case349.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case349.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 349)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case349.support T pos))
  · decide +kernel
theorem completion350 : pairCompletion (big 350)=full 350 := by
  have same : big 350=([{0,1,2,3,4},{0,5,7},{1,6,7},{2,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,4},{0,5,7},{1,6,7},{2,5,8},{3,6,8},{4,7,8}] [{0,1,2,3,4},{1,5},{3,5},{4,5},{0,6},{2,6},{4,6},{5,6},{2,7},{3,7},{0,5,7},{1,6,7},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered350 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 350) T=TwentyFiveEightLow.Case350.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case350.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 350)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case350.support T pos))
  · decide +kernel
theorem completion351 : pairCompletion (big 351)=full 351 := by
  have same : big 351=([{0,1,2,3,4},{0,5,6},{1,5,7},{2,6,7},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,4},{0,5,6},{1,5,7},{2,6,7},{3,6,8},{4,7,8}] [{0,1,2,3,4},{2,5},{3,5},{4,5},{1,6},{4,6},{0,5,6},{0,7},{3,7},{1,5,7},{2,6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered351 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 351) T=TwentyFiveEightLow.Case351.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case351.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 351)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case351.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
