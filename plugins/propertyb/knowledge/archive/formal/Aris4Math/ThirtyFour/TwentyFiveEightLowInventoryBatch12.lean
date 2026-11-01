import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion384 : pairCompletion (big 384)=full 384 := by
  have same : big 384=([{0,3,5},{1,5,6},{3,4,7},{2,6,7},{0,1,2,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,5},{1,5,6},{3,4,7},{2,6,7},{0,1,2,8},{4,6,8},{5,7,8}] [{1,3},{2,3},{0,4},{1,4},{2,4},{2,5},{0,3,5},{4,5},{0,6},{3,6},{1,5,6},{0,7},{1,7},{3,4,7},{2,6,7},{0,1,2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered384 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 384) T=TwentyFiveEightLow.Case384.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case384.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 384)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case384.support T pos))
  · decide +kernel
theorem completion385 : pairCompletion (big 385)=full 385 := by
  have same : big 385=([{0,1,2,4},{0,3,5},{1,5,6},{4,5,7},{2,6,7},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,4},{0,3,5},{1,5,6},{4,5,7},{2,6,7},{4,6,8},{3,7,8}] [{1,3},{2,3},{0,1,2,4},{3,4},{2,5},{0,3,5},{0,6},{3,6},{1,5,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered385 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 385) T=TwentyFiveEightLow.Case385.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case385.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 385)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case385.support T pos))
  · decide +kernel
theorem completion386 : pairCompletion (big 386)=full 386 := by
  have same : big 386=([{0,1,2,4},{3,4,5},{0,5,6},{1,5,7},{4,6,7},{2,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,4},{3,4,5},{0,5,6},{1,5,7},{4,6,7},{2,6,8},{3,7,8}] [{0,3},{1,3},{2,3},{0,1,2,4},{2,5},{3,4,5},{1,6},{3,6},{0,5,6},{0,7},{2,7},{1,5,7},{4,6,7},{0,8},{1,8},{4,8},{5,8},{2,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered386 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 386) T=TwentyFiveEightLow.Case386.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case386.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 386)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case386.support T pos))
  · decide +kernel
theorem completion387 : pairCompletion (big 387)=full 387 := by
  have same : big 387=([{0,2,5},{3,4,6},{1,5,6},{2,3,7},{4,5,7},{0,1,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,5},{3,4,6},{1,5,6},{2,3,7},{4,5,7},{0,1,4,8},{6,7,8}] [{1,2},{0,3},{1,3},{2,4},{0,2,5},{3,5},{0,6},{2,6},{3,4,6},{1,5,6},{0,7},{1,7},{2,3,7},{4,5,7},{2,8},{3,8},{0,1,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered387 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 387) T=TwentyFiveEightLow.Case387.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case387.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 387)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case387.support T pos))
  · decide +kernel
theorem completion388 : pairCompletion (big 388)=full 388 := by
  have same : big 388=([{0,2,5},{2,3,6},{4,5,6},{3,4,7},{1,6,7},{0,1,4,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,5},{2,3,6},{4,5,6},{3,4,7},{1,6,7},{0,1,4,8},{5,7,8}] [{1,2},{0,3},{1,3},{2,4},{1,5},{0,2,5},{3,5},{0,6},{2,3,6},{4,5,6},{0,7},{2,7},{3,4,7},{1,6,7},{2,8},{3,8},{0,1,4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered388 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 388) T=TwentyFiveEightLow.Case388.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case388.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 388)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case388.support T pos))
  · decide +kernel
theorem completion389 : pairCompletion (big 389)=full 389 := by
  have same : big 389=([{2,4,5},{2,3,6},{0,5,6},{1,5,7},{4,6,7},{0,1,4,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{2,3,6},{0,5,6},{1,5,7},{4,6,7},{0,1,4,8},{3,7,8}] [{0,2},{1,2},{0,3},{1,3},{3,4},{3,5},{2,4,5},{1,6},{2,3,6},{0,5,6},{0,7},{2,7},{1,5,7},{4,6,7},{2,8},{0,1,4,8},{5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered389 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 389) T=TwentyFiveEightLow.Case389.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case389.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 389)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case389.support T pos))
  · decide +kernel
theorem completion390 : pairCompletion (big 390)=full 390 := by
  have same : big 390=([{0,1,2,5},{0,3,6},{4,5,7},{1,6,7},{3,5,8},{4,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{0,3,6},{4,5,7},{1,6,7},{3,5,8},{4,6,8},{2,7,8}] [{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,1,2,5},{2,6},{0,3,6},{5,6},{0,7},{3,7},{4,5,7},{1,6,7},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered390 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 390) T=TwentyFiveEightLow.Case390.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case390.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 390)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case390.support T pos))
  · decide +kernel
theorem completion391 : pairCompletion (big 391)=full 391 := by
  have same : big 391=([{0,1,2,5},{0,3,6},{3,5,7},{4,6,7},{4,5,8},{1,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{0,3,6},{3,5,7},{4,6,7},{4,5,8},{1,6,8},{2,7,8}] [{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,1,2,5},{2,6},{0,3,6},{5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{3,8},{4,5,8},{1,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered391 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 391) T=TwentyFiveEightLow.Case391.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case391.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 391)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case391.support T pos))
  · decide +kernel
theorem completion392 : pairCompletion (big 392)=full 392 := by
  have same : big 392=([{0,1,2,5},{4,5,6},{3,5,7},{1,6,7},{0,3,8},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{4,5,6},{3,5,7},{1,6,7},{0,3,8},{2,6,8},{4,7,8}] [{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,1,2,5},{0,6},{3,6},{4,5,6},{0,7},{2,7},{3,5,7},{1,6,7},{1,8},{0,3,8},{5,8},{2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered392 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 392) T=TwentyFiveEightLow.Case392.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case392.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 392)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case392.support T pos))
  · decide +kernel
theorem completion393 : pairCompletion (big 393)=full 393 := by
  have same : big 393=([{0,3,5},{1,5,6},{4,5,7},{2,6,7},{0,1,2,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,5},{1,5,6},{4,5,7},{2,6,7},{0,1,2,8},{4,6,8},{3,7,8}] [{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{2,5},{0,3,5},{0,6},{3,6},{1,5,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,1,2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered393 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 393) T=TwentyFiveEightLow.Case393.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case393.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 393)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case393.support T pos))
  · decide +kernel
theorem completion394 : pairCompletion (big 394)=full 394 := by
  have same : big 394=([{0,1,2,4},{0,3,5},{1,5,6},{3,4,7},{2,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,4},{0,3,5},{1,5,6},{3,4,7},{2,6,7},{4,6,8},{5,7,8}] [{1,3},{2,3},{0,1,2,4},{2,5},{0,3,5},{4,5},{0,6},{3,6},{1,5,6},{0,7},{1,7},{3,4,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered394 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 394) T=TwentyFiveEightLow.Case394.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case394.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 394)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case394.support T pos))
  · decide +kernel
theorem completion395 : pairCompletion (big 395)=full 395 := by
  have same : big 395=([{0,1,2,4},{3,4,5},{0,5,6},{1,5,7},{3,6,7},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,4},{3,4,5},{0,5,6},{1,5,7},{3,6,7},{2,6,8},{4,7,8}] [{0,3},{1,3},{2,3},{0,1,2,4},{2,5},{3,4,5},{1,6},{4,6},{0,5,6},{0,7},{2,7},{1,5,7},{3,6,7},{0,8},{1,8},{3,8},{5,8},{2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered395 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 395) T=TwentyFiveEightLow.Case395.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case395.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 395)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case395.support T pos))
  · decide +kernel
theorem completion396 : pairCompletion (big 396)=full 396 := by
  have same : big 396=([{0,2,5},{3,4,6},{1,5,6},{2,4,7},{3,5,7},{0,1,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,5},{3,4,6},{1,5,6},{2,4,7},{3,5,7},{0,1,4,8},{6,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,2,5},{4,5},{0,6},{2,6},{3,4,6},{1,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{2,8},{3,8},{0,1,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered396 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 396) T=TwentyFiveEightLow.Case396.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case396.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 396)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case396.support T pos))
  · decide +kernel
theorem completion397 : pairCompletion (big 397)=full 397 := by
  have same : big 397=([{0,2,5},{2,4,6},{3,5,6},{3,4,7},{1,6,7},{0,1,4,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,5},{2,4,6},{3,5,6},{3,4,7},{1,6,7},{0,1,4,8},{5,7,8}] [{1,2},{0,3},{1,3},{2,3},{1,5},{0,2,5},{4,5},{0,6},{2,4,6},{3,5,6},{0,7},{2,7},{3,4,7},{1,6,7},{2,8},{3,8},{0,1,4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered397 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 397) T=TwentyFiveEightLow.Case397.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case397.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 397)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case397.support T pos))
  · decide +kernel
theorem completion398 : pairCompletion (big 398)=full 398 := by
  have same : big 398=([{2,4,5},{3,4,6},{0,5,6},{1,5,7},{2,6,7},{0,1,4,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{3,4,6},{0,5,6},{1,5,7},{2,6,7},{0,1,4,8},{3,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{3,5},{2,4,5},{1,6},{3,4,6},{0,5,6},{0,7},{4,7},{1,5,7},{2,6,7},{2,8},{0,1,4,8},{5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered398 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 398) T=TwentyFiveEightLow.Case398.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case398.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 398)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case398.support T pos))
  · decide +kernel
theorem completion399 : pairCompletion (big 399)=full 399 := by
  have same : big 399=([{0,1,2,5},{1,4,6},{0,3,7},{5,6,7},{3,5,8},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{1,4,6},{0,3,7},{5,6,7},{3,5,8},{2,6,8},{4,7,8}] [{1,3},{2,3},{0,4},{2,4},{3,4},{0,1,2,5},{4,5},{0,6},{3,6},{1,4,6},{1,7},{2,7},{0,3,7},{5,6,7},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered399 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 399) T=TwentyFiveEightLow.Case399.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case399.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 399)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case399.support T pos))
  · decide +kernel
theorem completion400 : pairCompletion (big 400)=full 400 := by
  have same : big 400=([{0,1,2,5},{0,3,6},{4,5,7},{2,6,7},{1,4,8},{5,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{0,3,6},{4,5,7},{2,6,7},{1,4,8},{5,6,8},{3,7,8}] [{1,3},{2,3},{0,4},{2,4},{3,4},{0,1,2,5},{3,5},{1,6},{0,3,6},{4,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,8},{2,8},{1,4,8},{5,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered400 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 400) T=TwentyFiveEightLow.Case400.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case400.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 400)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case400.support T pos))
  · decide +kernel
theorem completion401 : pairCompletion (big 401)=full 401 := by
  have same : big 401=([{0,1,2,5},{0,3,6},{3,5,7},{4,6,7},{1,4,8},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{0,3,6},{3,5,7},{4,6,7},{1,4,8},{5,6,8},{2,7,8}] [{1,3},{2,3},{0,4},{2,4},{3,4},{0,1,2,5},{4,5},{1,6},{2,6},{0,3,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{3,8},{1,4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered401 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 401) T=TwentyFiveEightLow.Case401.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case401.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 401)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case401.support T pos))
  · decide +kernel
theorem completion402 : pairCompletion (big 402)=full 402 := by
  have same : big 402=([{0,3,5},{1,4,6},{2,5,7},{3,6,7},{0,1,2,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,5},{1,4,6},{2,5,7},{3,6,7},{0,1,2,8},{5,6,8},{4,7,8}] [{1,3},{2,3},{0,4},{2,4},{3,4},{1,5},{0,3,5},{4,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,1,2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered402 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 402) T=TwentyFiveEightLow.Case402.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case402.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 402)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case402.support T pos))
  · decide +kernel
theorem completion403 : pairCompletion (big 403)=full 403 := by
  have same : big 403=([{0,1,2,4},{0,3,5},{4,5,6},{3,4,7},{1,6,7},{2,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,4},{0,3,5},{4,5,6},{3,4,7},{1,6,7},{2,6,8},{5,7,8}] [{1,3},{2,3},{0,1,2,4},{1,5},{2,5},{0,3,5},{0,6},{3,6},{4,5,6},{0,7},{2,7},{3,4,7},{1,6,7},{0,8},{1,8},{3,8},{4,8},{2,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered403 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 403) T=TwentyFiveEightLow.Case403.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case403.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 403)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case403.support T pos))
  · decide +kernel
theorem completion404 : pairCompletion (big 404)=full 404 := by
  have same : big 404=([{0,1,2,4},{0,3,5},{1,5,6},{4,5,7},{3,6,7},{4,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,4},{0,3,5},{1,5,6},{4,5,7},{3,6,7},{4,6,8},{2,7,8}] [{1,3},{2,3},{0,1,2,4},{3,4},{2,5},{0,3,5},{0,6},{2,6},{1,5,6},{0,7},{1,7},{4,5,7},{3,6,7},{0,8},{1,8},{3,8},{5,8},{4,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered404 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 404) T=TwentyFiveEightLow.Case404.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case404.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 404)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case404.support T pos))
  · decide +kernel
theorem completion405 : pairCompletion (big 405)=full 405 := by
  have same : big 405=([{0,2,5},{1,3,6},{4,5,6},{2,4,7},{3,5,7},{0,1,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,5},{1,3,6},{4,5,6},{2,4,7},{3,5,7},{0,1,4,8},{6,7,8}] [{1,2},{0,3},{2,3},{3,4},{1,5},{0,2,5},{0,6},{2,6},{1,3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{2,8},{3,8},{0,1,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered405 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 405) T=TwentyFiveEightLow.Case405.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case405.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 405)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case405.support T pos))
  · decide +kernel
theorem completion406 : pairCompletion (big 406)=full 406 := by
  have same : big 406=([{0,2,5},{2,4,6},{3,5,6},{4,5,7},{1,6,7},{0,1,4,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,5},{2,4,6},{3,5,6},{4,5,7},{1,6,7},{0,1,4,8},{3,7,8}] [{1,2},{0,3},{1,3},{2,3},{3,4},{1,5},{0,2,5},{0,6},{2,4,6},{3,5,6},{0,7},{2,7},{4,5,7},{1,6,7},{2,8},{0,1,4,8},{5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered406 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 406) T=TwentyFiveEightLow.Case406.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case406.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 406)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case406.support T pos))
  · decide +kernel
theorem completion407 : pairCompletion (big 407)=full 407 := by
  have same : big 407=([{0,2,5},{3,4,6},{1,5,6},{4,5,7},{2,6,7},{0,1,4,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,5},{3,4,6},{1,5,6},{4,5,7},{2,6,7},{0,1,4,8},{3,7,8}] [{1,2},{0,3},{1,3},{2,3},{2,4},{0,2,5},{3,5},{0,6},{3,4,6},{1,5,6},{0,7},{1,7},{4,5,7},{2,6,7},{2,8},{0,1,4,8},{5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered407 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 407) T=TwentyFiveEightLow.Case407.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case407.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 407)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case407.support T pos))
  · decide +kernel
theorem completion408 : pairCompletion (big 408)=full 408 := by
  have same : big 408=([{0,1,2,5},{3,4,6},{3,5,7},{0,6,7},{4,5,8},{1,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{3,4,6},{3,5,7},{0,6,7},{4,5,8},{1,6,8},{2,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,1,2,5},{2,6},{3,4,6},{5,6},{1,7},{4,7},{3,5,7},{0,6,7},{0,8},{3,8},{4,5,8},{1,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered408 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 408) T=TwentyFiveEightLow.Case408.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case408.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 408)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case408.support T pos))
  · decide +kernel
theorem completion409 : pairCompletion (big 409)=full 409 := by
  have same : big 409=([{0,1,2,5},{3,5,6},{4,5,7},{0,6,7},{3,4,8},{1,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{3,5,6},{4,5,7},{0,6,7},{3,4,8},{1,6,8},{2,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,1,2,5},{2,6},{4,6},{3,5,6},{1,7},{3,7},{4,5,7},{0,6,7},{0,8},{3,4,8},{5,8},{1,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered409 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 409) T=TwentyFiveEightLow.Case409.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case409.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 409)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case409.support T pos))
  · decide +kernel
theorem completion410 : pairCompletion (big 410)=full 410 := by
  have same : big 410=([{3,4,5},{0,5,6},{1,5,7},{2,6,7},{0,1,2,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,5,6},{1,5,7},{2,6,7},{0,1,2,8},{3,6,8},{4,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{2,5},{3,4,5},{1,6},{4,6},{0,5,6},{0,7},{3,7},{1,5,7},{2,6,7},{0,1,2,8},{5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered410 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 410) T=TwentyFiveEightLow.Case410.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case410.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 410)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case410.support T pos))
  · decide +kernel
theorem completion411 : pairCompletion (big 411)=full 411 := by
  have same : big 411=([{0,1,2,4},{3,4,5},{0,5,6},{1,5,7},{2,6,7},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,4},{3,4,5},{0,5,6},{1,5,7},{2,6,7},{3,6,8},{4,7,8}] [{0,3},{1,3},{2,3},{0,1,2,4},{2,5},{3,4,5},{1,6},{4,6},{0,5,6},{0,7},{3,7},{1,5,7},{2,6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered411 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 411) T=TwentyFiveEightLow.Case411.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case411.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 411)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case411.support T pos))
  · decide +kernel
theorem completion412 : pairCompletion (big 412)=full 412 := by
  have same : big 412=([{2,3,5},{2,4,6},{0,5,6},{3,4,7},{1,5,7},{0,1,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{2,4,6},{0,5,6},{3,4,7},{1,5,7},{0,1,4,8},{6,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3,5},{4,5},{1,6},{3,6},{2,4,6},{0,5,6},{0,7},{2,7},{3,4,7},{1,5,7},{2,8},{3,8},{0,1,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered412 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 412) T=TwentyFiveEightLow.Case412.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case412.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 412)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case412.support T pos))
  · decide +kernel
theorem completion413 : pairCompletion (big 413)=full 413 := by
  have same : big 413=([{2,4,5},{2,3,6},{0,5,6},{3,4,7},{1,5,7},{0,1,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{2,3,6},{0,5,6},{3,4,7},{1,5,7},{0,1,4,8},{6,7,8}] [{0,2},{1,2},{0,3},{1,3},{3,5},{2,4,5},{1,6},{2,3,6},{4,6},{0,5,6},{0,7},{2,7},{3,4,7},{1,5,7},{2,8},{3,8},{0,1,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered413 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 413) T=TwentyFiveEightLow.Case413.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case413.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 413)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case413.support T pos))
  · decide +kernel
theorem completion414 : pairCompletion (big 414)=full 414 := by
  have same : big 414=([{0,2,3},{1,4,5},{2,4,6},{3,5,6},{1,2,7},{3,4,7},{0,6,7},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{1,4,5},{2,4,6},{3,5,6},{1,2,7},{3,4,7},{0,6,7},{5,7,8}] [{0,1},{1,3},{0,2,3},{0,4},{0,5},{2,5},{1,4,5},{1,6},{2,4,6},{3,5,6},{1,2,7},{3,4,7},{0,6,7},{0,8},{1,8},{2,8},{3,8},{4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered414 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 414) T=TwentyFiveEightLow.Case414.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case414.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 414)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case414.support T pos))
  · decide +kernel
theorem completion415 : pairCompletion (big 415)=full 415 := by
  have same : big 415=([{0,1,4},{0,2,5},{1,3,6},{4,5,6},{2,4,7},{3,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{0,2,5},{1,3,6},{4,5,6},{2,4,7},{3,5,7},{6,7,8}] [{1,2},{0,3},{2,3},{0,1,4},{3,4},{1,5},{0,2,5},{0,6},{2,6},{1,3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered415 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 415) T=TwentyFiveEightLow.Case415.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case415.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 415)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case415.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
