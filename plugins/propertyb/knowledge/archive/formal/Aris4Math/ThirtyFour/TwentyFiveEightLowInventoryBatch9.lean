import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion288 : pairCompletion (big 288)=full 288 := by
  have same : big 288=([{0,2,3,4},{0,1,5},{3,5,6},{4,5,7},{2,6,7},{1,2,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{0,1,5},{3,5,6},{4,5,7},{2,6,7},{1,2,8},{4,6,8},{3,7,8}] [{1,3},{1,4},{0,2,3,4},{0,1,5},{2,5},{0,6},{1,6},{3,5,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,8},{1,2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered288 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 288) T=TwentyFiveEightLow.Case288.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case288.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 288)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case288.support T pos))
  · decide +kernel
theorem completion289 : pairCompletion (big 289)=full 289 := by
  have same : big 289=([{0,2,3,4},{1,2,5},{3,5,6},{4,5,7},{2,6,7},{0,1,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{1,2,5},{3,5,6},{4,5,7},{2,6,7},{0,1,8},{4,6,8},{3,7,8}] [{1,3},{1,4},{0,2,3,4},{0,5},{1,2,5},{0,6},{1,6},{3,5,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,1,8},{2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered289 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 289) T=TwentyFiveEightLow.Case289.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case289.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 289)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case289.support T pos))
  · decide +kernel
theorem completion290 : pairCompletion (big 290)=full 290 := by
  have same : big 290=([{0,1,4},{1,2,5},{3,4,6},{3,5,7},{2,6,7},{0,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{1,2,5},{3,4,6},{3,5,7},{2,6,7},{0,2,3,8},{5,6,8},{4,7,8}] [{1,3},{0,1,4},{2,4},{0,5},{1,2,5},{4,5},{0,6},{1,6},{3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{1,8},{0,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered290 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 290) T=TwentyFiveEightLow.Case290.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case290.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 290)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case290.support T pos))
  · decide +kernel
theorem completion291 : pairCompletion (big 291)=full 291 := by
  have same : big 291=([{0,1,4},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,2,3,8},{1,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,2,3,8},{1,5,8},{6,7,8}] [{1,2},{1,3},{0,1,4},{0,5},{4,5},{0,6},{1,6},{2,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{0,2,3,8},{4,8},{1,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered291 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 291) T=TwentyFiveEightLow.Case291.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case291.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 291)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case291.support T pos))
  · decide +kernel
theorem completion292 : pairCompletion (big 292)=full 292 := by
  have same : big 292=([{0,1,2,3},{1,4,5},{2,4,6},{3,5,6},{2,5,7},{1,6,7},{0,4,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{1,4,5},{2,4,6},{3,5,6},{2,5,7},{1,6,7},{0,4,8},{3,7,8}] [{0,1,2,3},{3,4},{0,5},{1,4,5},{0,6},{2,4,6},{3,5,6},{0,7},{4,7},{2,5,7},{1,6,7},{1,8},{2,8},{0,4,8},{5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered292 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 292) T=TwentyFiveEightLow.Case292.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case292.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 292)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case292.support T pos))
  · decide +kernel
theorem completion293 : pairCompletion (big 293)=full 293 := by
  have same : big 293=([{0,1,4},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{1,2,3,8},{0,5,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{1,2,3,8},{0,5,8}] [{0,2},{0,3},{0,1,4},{1,5},{4,5},{0,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{1,6,7},{1,2,3,8},{4,8},{0,5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered293 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 293) T=TwentyFiveEightLow.Case293.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case293.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 293)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case293.support T pos))
  · decide +kernel
theorem completion294 : pairCompletion (big 294)=full 294 := by
  have same : big 294=([{0,2,3,4},{1,2,5},{0,5,6},{1,3,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{1,2,5},{0,5,6},{1,3,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,1},{1,4},{0,2,3,4},{1,2,5},{3,5},{1,6},{2,6},{0,5,6},{0,7},{1,3,7},{5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered294 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 294) T=TwentyFiveEightLow.Case294.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case294.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 294)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case294.support T pos))
  · decide +kernel
theorem completion295 : pairCompletion (big 295)=full 295 := by
  have same : big 295=([{0,2,3,4},{1,2,5},{0,5,6},{4,5,7},{3,6,7},{1,3,8},{4,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{1,2,5},{0,5,6},{4,5,7},{3,6,7},{1,3,8},{4,6,8},{2,7,8}] [{0,1},{1,4},{0,2,3,4},{1,2,5},{3,5},{1,6},{2,6},{0,5,6},{0,7},{1,7},{4,5,7},{3,6,7},{0,8},{1,3,8},{5,8},{4,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered295 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 295) T=TwentyFiveEightLow.Case295.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case295.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 295)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case295.support T pos))
  · decide +kernel
theorem completion296 : pairCompletion (big 296)=full 296 := by
  have same : big 296=([{0,2,3,4},{1,2,5},{1,3,6},{4,5,7},{2,6,7},{0,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{1,2,5},{1,3,6},{4,5,7},{2,6,7},{0,5,8},{4,6,8},{3,7,8}] [{0,1},{1,4},{0,2,3,4},{1,2,5},{3,5},{0,6},{1,3,6},{5,6},{0,7},{1,7},{4,5,7},{2,6,7},{1,8},{2,8},{0,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered296 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 296) T=TwentyFiveEightLow.Case296.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case296.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 296)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case296.support T pos))
  · decide +kernel
theorem completion297 : pairCompletion (big 297)=full 297 := by
  have same : big 297=([{0,2,3,4},{1,2,6},{4,5,6},{2,5,7},{3,6,7},{1,3,8},{0,5,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{1,2,6},{4,5,6},{2,5,7},{3,6,7},{1,3,8},{0,5,8},{4,7,8}] [{0,1},{1,4},{0,2,3,4},{1,5},{3,5},{0,6},{1,2,6},{4,5,6},{0,7},{1,7},{2,5,7},{3,6,7},{2,8},{1,3,8},{0,5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered297 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 297) T=TwentyFiveEightLow.Case297.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case297.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 297)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case297.support T pos))
  · decide +kernel
theorem completion298 : pairCompletion (big 298)=full 298 := by
  have same : big 298=([{1,2,4},{0,4,5},{1,3,6},{3,5,7},{2,6,7},{0,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,4},{0,4,5},{1,3,6},{3,5,7},{2,6,7},{0,2,3,8},{5,6,8},{4,7,8}] [{0,1},{1,2,4},{3,4},{1,5},{2,5},{0,4,5},{0,6},{1,3,6},{4,6},{0,7},{1,7},{3,5,7},{2,6,7},{1,8},{0,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered298 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 298) T=TwentyFiveEightLow.Case298.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case298.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 298)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case298.support T pos))
  · decide +kernel
theorem completion299 : pairCompletion (big 299)=full 299 := by
  have same : big 299=([{1,2,4},{0,4,5},{3,5,6},{3,4,7},{2,6,7},{0,2,3,8},{1,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,4},{0,4,5},{3,5,6},{3,4,7},{2,6,7},{0,2,3,8},{1,6,8},{5,7,8}] [{0,1},{1,3},{1,2,4},{1,5},{2,5},{0,4,5},{0,6},{4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,6,7},{0,2,3,8},{4,8},{1,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered299 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 299) T=TwentyFiveEightLow.Case299.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case299.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 299)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case299.support T pos))
  · decide +kernel
theorem completion300 : pairCompletion (big 300)=full 300 := by
  have same : big 300=([{0,4,5},{1,2,6},{3,5,6},{3,4,7},{2,5,7},{0,2,3,8},{1,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{1,2,6},{3,5,6},{3,4,7},{2,5,7},{0,2,3,8},{1,4,8},{6,7,8}] [{0,1},{1,3},{2,4},{1,5},{0,4,5},{0,6},{1,2,6},{4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{0,2,3,8},{1,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered300 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 300) T=TwentyFiveEightLow.Case300.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case300.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 300)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case300.support T pos))
  · decide +kernel
theorem completion301 : pairCompletion (big 301)=full 301 := by
  have same : big 301=([{0,1,2,3},{0,4,5},{2,4,6},{1,5,6},{1,4,7},{3,6,7},{3,5,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,5},{2,4,6},{1,5,6},{1,4,7},{3,6,7},{3,5,8},{2,7,8}] [{0,1,2,3},{3,4},{2,5},{0,4,5},{0,6},{2,4,6},{1,5,6},{0,7},{1,4,7},{5,7},{3,6,7},{0,8},{1,8},{4,8},{3,5,8},{6,8},{2,7,8}]=true
  decide +kernel

theorem recovered301 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 301) T=TwentyFiveEightLow.Case301.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case301.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 301)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case301.support T pos))
  · decide +kernel
theorem completion302 : pairCompletion (big 302)=full 302 := by
  have same : big 302=([{0,1,4},{0,2,5},{2,4,6},{3,5,6},{3,4,7},{1,6,7},{1,2,3,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{0,2,5},{2,4,6},{3,5,6},{3,4,7},{1,6,7},{1,2,3,8},{5,7,8}] [{0,3},{0,1,4},{1,5},{0,2,5},{4,5},{0,6},{2,4,6},{3,5,6},{0,7},{2,7},{3,4,7},{1,6,7},{0,8},{1,2,3,8},{4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered302 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 302) T=TwentyFiveEightLow.Case302.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case302.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 302)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case302.support T pos))
  · decide +kernel
theorem completion303 : pairCompletion (big 303)=full 303 := by
  have same : big 303=([{0,1,2,3},{1,4,5},{2,4,6},{5,6,7},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{1,4,5},{2,4,6},{5,6,7},{3,7,8}] [{0,1,2,3},{0,4},{3,4},{0,5},{2,5},{3,5},{1,4,5},{0,6},{1,6},{3,6},{2,4,6},{0,7},{1,7},{2,7},{4,7},{5,6,7},{0,8},{1,8},{2,8},{4,8},{5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered303 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 303) T=TwentyFiveEightLow.Case303.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case303.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 303)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case303.support T pos))
  · decide +kernel
theorem completion304 : pairCompletion (big 304)=full 304 := by
  have same : big 304=([{0,2,3,4},{0,5,6},{1,2,7},{4,5,7},{3,6,7},{1,3,8},{2,5,8},{4,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{0,5,6},{1,2,7},{4,5,7},{3,6,7},{1,3,8},{2,5,8},{4,6,8}] [{0,1},{1,4},{0,2,3,4},{1,5},{3,5},{1,6},{2,6},{0,5,6},{0,7},{1,2,7},{4,5,7},{3,6,7},{0,8},{1,3,8},{2,5,8},{4,6,8},{7,8}]=true
  decide +kernel

theorem recovered304 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 304) T=TwentyFiveEightLow.Case304.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case304.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 304)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case304.support T pos))
  · decide +kernel
theorem completion305 : pairCompletion (big 305)=full 305 := by
  have same : big 305=([{0,2,3,4},{1,2,6},{4,5,6},{1,3,7},{2,5,7},{0,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{1,2,6},{4,5,6},{1,3,7},{2,5,7},{0,5,8},{3,6,8},{4,7,8}] [{0,1},{1,4},{0,2,3,4},{1,5},{3,5},{0,6},{1,2,6},{4,5,6},{0,7},{1,3,7},{2,5,7},{6,7},{1,8},{2,8},{0,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered305 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 305) T=TwentyFiveEightLow.Case305.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case305.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 305)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case305.support T pos))
  · decide +kernel
theorem completion306 : pairCompletion (big 306)=full 306 := by
  have same : big 306=([{0,4,5},{1,2,6},{3,4,6},{1,3,7},{2,5,7},{0,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{1,2,6},{3,4,6},{1,3,7},{2,5,7},{0,2,3,8},{5,6,8},{4,7,8}] [{0,1},{1,4},{2,4},{1,5},{3,5},{0,4,5},{0,6},{1,2,6},{3,4,6},{0,7},{1,3,7},{2,5,7},{6,7},{1,8},{0,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered306 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 306) T=TwentyFiveEightLow.Case306.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case306.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 306)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case306.support T pos))
  · decide +kernel
theorem completion307 : pairCompletion (big 307)=full 307 := by
  have same : big 307=([{0,4,5},{1,2,6},{3,4,6},{2,4,7},{3,5,7},{0,2,3,8},{5,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{1,2,6},{3,4,6},{2,4,7},{3,5,7},{0,2,3,8},{5,6,8},{1,7,8}] [{0,1},{1,3},{1,4},{1,5},{2,5},{0,4,5},{0,6},{1,2,6},{3,4,6},{0,7},{2,4,7},{3,5,7},{6,7},{0,2,3,8},{4,8},{5,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered307 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 307) T=TwentyFiveEightLow.Case307.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case307.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 307)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case307.support T pos))
  · decide +kernel
theorem completion308 : pairCompletion (big 308)=full 308 := by
  have same : big 308=([{0,1,2,3},{0,4,5},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,5},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{3,6,8},{2,7,8}] [{0,1,2,3},{2,4},{3,5},{0,4,5},{0,6},{1,4,6},{2,5,6},{0,7},{3,4,7},{1,5,7},{6,7},{0,8},{1,8},{4,8},{5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered308 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 308) T=TwentyFiveEightLow.Case308.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case308.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 308)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case308.support T pos))
  · decide +kernel
theorem completion309 : pairCompletion (big 309)=full 309 := by
  have same : big 309=([{0,1,4},{0,2,5},{2,4,6},{3,5,6},{3,4,7},{1,5,7},{1,2,3,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{0,2,5},{2,4,6},{3,5,6},{3,4,7},{1,5,7},{1,2,3,8},{6,7,8}] [{0,3},{0,1,4},{0,2,5},{4,5},{0,6},{1,6},{2,4,6},{3,5,6},{0,7},{2,7},{3,4,7},{1,5,7},{0,8},{1,2,3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered309 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 309) T=TwentyFiveEightLow.Case309.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case309.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 309)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case309.support T pos))
  · decide +kernel
theorem completion310 : pairCompletion (big 310)=full 310 := by
  have same : big 310=([{0,1,2,3},{1,4,5},{2,4,6},{3,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{1,4,5},{2,4,6},{3,5,7},{6,7,8}] [{0,1,2,3},{0,4},{3,4},{0,5},{2,5},{1,4,5},{0,6},{1,6},{3,6},{2,4,6},{5,6},{0,7},{1,7},{2,7},{4,7},{3,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered310 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 310) T=TwentyFiveEightLow.Case310.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case310.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 310)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case310.support T pos))
  · decide +kernel
theorem completion311 : pairCompletion (big 311)=full 311 := by
  have same : big 311=([{0,1,2,3},{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{6,7,8}] [{0,1,2,3},{0,4},{0,5},{1,4,5},{0,6},{1,6},{2,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered311 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 311) T=TwentyFiveEightLow.Case311.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case311.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 311)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case311.support T pos))
  · decide +kernel
theorem completion312 : pairCompletion (big 312)=full 312 := by
  have same : big 312=([{0,2,3,4},{1,2,5,6},{3,5,7},{4,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{1,2,5,6},{3,5,7},{4,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}] [{1,3},{1,4},{0,2,3,4},{0,5},{0,6},{1,2,5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered312 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 312) T=TwentyFiveEightLow.Case312.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case312.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 312)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case312.support T pos))
  · decide +kernel
theorem completion313 : pairCompletion (big 313)=full 313 := by
  have same : big 313=([{0,2,3,4},{1,2,5,6},{0,1,7},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{1,2,5,6},{0,1,7},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] [{1,3},{1,4},{0,2,3,4},{0,5},{0,6},{1,2,5,6},{0,1,7},{3,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered313 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 313) T=TwentyFiveEightLow.Case313.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case313.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 313)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case313.support T pos))
  · decide +kernel
theorem completion314 : pairCompletion (big 314)=full 314 := by
  have same : big 314=([{0,2,4,5},{3,4,6},{0,1,7},{3,5,7},{2,6,7},{1,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4,5},{3,4,6},{0,1,7},{3,5,7},{2,6,7},{1,2,3,8},{5,6,8},{4,7,8}] [{0,3},{1,4},{1,5},{0,2,4,5},{0,6},{1,6},{3,4,6},{0,1,7},{3,5,7},{2,6,7},{0,8},{1,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered314 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 314) T=TwentyFiveEightLow.Case314.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case314.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 314)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case314.support T pos))
  · decide +kernel
theorem completion315 : pairCompletion (big 315)=full 315 := by
  have same : big 315=([{2,3,6},{4,5,6},{0,1,7},{2,4,7},{3,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,6},{4,5,6},{0,1,7},{2,4,7},{3,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}] [{0,2},{1,3},{1,4},{0,5},{0,6},{1,6},{2,3,6},{4,5,6},{0,1,7},{2,4,7},{3,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered315 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 315) T=TwentyFiveEightLow.Case315.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case315.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 315)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case315.support T pos))
  · decide +kernel
theorem completion316 : pairCompletion (big 316)=full 316 := by
  have same : big 316=([{0,1,2,3},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{1,4,5,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{1,4,5,8},{0,7,8}] [{0,1,2,3},{0,4},{0,5},{0,6},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{2,8},{3,8},{1,4,5,8},{6,8},{0,7,8}]=true
  decide +kernel

theorem recovered316 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 316) T=TwentyFiveEightLow.Case316.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case316.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 316)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case316.support T pos))
  · decide +kernel
theorem completion317 : pairCompletion (big 317)=full 317 := by
  have same : big 317=([{0,2,3,4},{1,2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{1,2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,1},{1,3},{1,4},{0,2,3,4},{0,5},{0,6},{1,2,5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered317 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 317) T=TwentyFiveEightLow.Case317.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case317.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 317)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case317.support T pos))
  · decide +kernel
theorem completion318 : pairCompletion (big 318)=full 318 := by
  have same : big 318=([{0,2,4,5},{3,4,6},{3,5,7},{2,6,7},{1,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4,5},{3,4,6},{3,5,7},{2,6,7},{1,2,3,8},{5,6,8},{4,7,8}] [{0,1},{0,3},{1,4},{1,5},{0,2,4,5},{0,6},{1,6},{3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,8},{1,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered318 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 318) T=TwentyFiveEightLow.Case318.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case318.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 318)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case318.support T pos))
  · decide +kernel
theorem completion319 : pairCompletion (big 319)=full 319 := by
  have same : big 319=([{2,3,6},{4,5,6},{2,4,7},{3,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,6},{4,5,6},{2,4,7},{3,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}] [{0,1},{0,2},{1,3},{1,4},{0,5},{0,6},{1,6},{2,3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered319 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 319) T=TwentyFiveEightLow.Case319.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case319.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 319)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case319.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
