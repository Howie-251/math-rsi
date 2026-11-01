import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion480 : pairCompletion (big 480)=full 480 := by
  have same : big 480=([{0,1,3,4},{2,3,5},{1,5,6},{4,5,7},{2,6,7},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{2,3,5},{1,5,6},{4,5,7},{2,6,7},{4,6,8},{3,7,8}] [{0,2},{1,2},{2,4},{0,1,3,4},{0,5},{2,3,5},{0,6},{3,6},{1,5,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered480 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 480) T=TwentyFiveEightLow.Case480.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case480.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 480)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case480.support T pos))
  · decide +kernel
theorem completion481 : pairCompletion (big 481)=full 481 := by
  have same : big 481=([{1,3,5},{1,4,6},{2,5,6},{2,3,7},{4,5,7},{0,3,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,5},{1,4,6},{2,5,6},{2,3,7},{4,5,7},{0,3,4,8},{6,7,8}] [{0,1},{0,2},{1,2},{2,4},{0,5},{1,3,5},{0,6},{3,6},{1,4,6},{2,5,6},{0,7},{1,7},{2,3,7},{4,5,7},{1,8},{2,8},{0,3,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered481 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 481) T=TwentyFiveEightLow.Case481.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case481.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 481)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case481.support T pos))
  · decide +kernel
theorem completion482 : pairCompletion (big 482)=full 482 := by
  have same : big 482=([{1,4,5},{2,3,6},{0,5,6},{1,3,7},{2,5,7},{4,6,7},{0,3,4,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,5},{2,3,6},{0,5,6},{1,3,7},{2,5,7},{4,6,7},{0,3,4,8}] [{0,1},{0,2},{1,2},{2,4},{3,5},{1,4,5},{1,6},{2,3,6},{0,5,6},{0,7},{1,3,7},{2,5,7},{4,6,7},{1,8},{2,8},{0,3,4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered482 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 482) T=TwentyFiveEightLow.Case482.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case482.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 482)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case482.support T pos))
  · decide +kernel
theorem completion483 : pairCompletion (big 483)=full 483 := by
  have same : big 483=([{0,1,2,3},{1,4,5,6},{2,4,7},{3,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{1,4,5,6},{2,4,7},{3,5,7},{6,7,8}] [{0,1,2,3},{0,4},{3,4},{0,5},{2,5},{0,6},{2,6},{3,6},{1,4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered483 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 483) T=TwentyFiveEightLow.Case483.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case483.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 483)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case483.support T pos))
  · decide +kernel
theorem completion484 : pairCompletion (big 484)=full 484 := by
  have same : big 484=([{0,1,4,5},{2,3,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{2,3,6,7},{4,6,8},{5,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,4},{3,4},{2,5},{3,5},{0,1,4,5},{0,6},{1,6},{5,6},{0,7},{1,7},{4,7},{2,3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered484 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 484) T=TwentyFiveEightLow.Case484.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case484.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 484)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case484.support T pos))
  · decide +kernel
theorem completion485 : pairCompletion (big 485)=full 485 := by
  have same : big 485=([{0,1,4,6},{4,5,7},{2,3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,6},{4,5,7},{2,3,5,8},{6,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,4},{3,4},{0,5},{1,5},{2,6},{3,6},{0,1,4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{4,5,7},{0,8},{1,8},{4,8},{2,3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered485 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 485) T=TwentyFiveEightLow.Case485.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case485.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 485)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case485.support T pos))
  · decide +kernel
theorem completion486 : pairCompletion (big 486)=full 486 := by
  have same : big 486=([{0,1,3,4},{3,5,7},{4,6,7},{2,5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{3,5,7},{4,6,7},{2,5,6,8}] [{0,2},{1,2},{2,3},{2,4},{0,1,3,4},{0,5},{1,5},{4,5},{0,6},{1,6},{3,6},{0,7},{1,7},{2,7},{3,5,7},{4,6,7},{0,8},{1,8},{3,8},{4,8},{2,5,6,8},{7,8}]=true
  decide +kernel

theorem recovered486 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 486) T=TwentyFiveEightLow.Case486.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case486.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 486)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case486.support T pos))
  · decide +kernel
theorem completion487 : pairCompletion (big 487)=full 487 := by
  have same : big 487=([{2,4,5},{3,4,6},{0,1,7},{3,5,7},{2,6,7},{0,2,8},{1,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{3,4,6},{0,1,7},{3,5,7},{2,6,7},{0,2,8},{1,3,8},{5,6,8},{4,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{0,5},{1,5},{2,4,5},{0,6},{1,6},{3,4,6},{0,1,7},{3,5,7},{2,6,7},{0,2,8},{1,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered487 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 487) T=TwentyFiveEightLow.Case487.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case487.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 487)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case487.support T pos))
  · decide +kernel
theorem completion488 : pairCompletion (big 488)=full 488 := by
  have same : big 488=([{2,4,5},{3,4,6},{0,2,7},{1,3,7},{5,6,7},{0,1,8},{3,5,8},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{3,4,6},{0,2,7},{1,3,7},{5,6,7},{0,1,8},{3,5,8},{2,6,8},{4,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{0,5},{1,5},{2,4,5},{0,6},{1,6},{3,4,6},{0,2,7},{1,3,7},{5,6,7},{0,1,8},{3,5,8},{2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered488 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 488) T=TwentyFiveEightLow.Case488.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case488.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 488)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case488.support T pos))
  · decide +kernel
theorem completion489 : pairCompletion (big 489)=full 489 := by
  have same : big 489=([{2,4,5},{0,1,6},{3,4,6},{0,2,7},{1,3,7},{5,6,7},{3,5,8},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{0,1,6},{3,4,6},{0,2,7},{1,3,7},{5,6,7},{3,5,8},{2,6,8},{4,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{0,5},{1,5},{2,4,5},{0,1,6},{3,4,6},{0,2,7},{1,3,7},{5,6,7},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered489 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 489) T=TwentyFiveEightLow.Case489.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case489.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 489)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case489.support T pos))
  · decide +kernel
theorem completion490 : pairCompletion (big 490)=full 490 := by
  have same : big 490=([{0,1,6},{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{3,4,8},{2,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{3,4,8},{2,5,8},{6,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{0,5},{1,5},{0,1,6},{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{0,8},{1,8},{3,4,8},{2,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered490 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 490) T=TwentyFiveEightLow.Case490.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case490.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 490)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case490.support T pos))
  · decide +kernel
theorem completion491 : pairCompletion (big 491)=full 491 := by
  have same : big 491=([{2,3,4},{0,1,6},{2,5,6},{0,2,7},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{0,1,6},{2,5,6},{0,2,7},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{1,7,8}] [{1,2},{0,3},{1,3},{0,4},{1,4},{2,3,4},{0,5},{1,5},{0,1,6},{2,5,6},{0,2,7},{3,5,7},{4,6,7},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered491 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 491) T=TwentyFiveEightLow.Case491.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case491.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 491)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case491.support T pos))
  · decide +kernel
theorem completion492 : pairCompletion (big 492)=full 492 := by
  have same : big 492=([{1,2,3},{2,4,5},{0,1,6},{3,4,6},{1,4,7},{3,5,7},{2,6,7},{5,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3},{2,4,5},{0,1,6},{3,4,6},{1,4,7},{3,5,7},{2,6,7},{5,6,8},{0,7,8}] [{0,2},{0,3},{1,2,3},{0,4},{0,5},{1,5},{2,4,5},{0,1,6},{3,4,6},{1,4,7},{3,5,7},{2,6,7},{1,8},{2,8},{3,8},{4,8},{5,6,8},{0,7,8}]=true
  decide +kernel

theorem recovered492 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 492) T=TwentyFiveEightLow.Case492.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case492.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 492)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case492.support T pos))
  · decide +kernel
theorem completion493 : pairCompletion (big 493)=full 493 := by
  have same : big 493=([{2,4,5},{0,1,5,6},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{0,1,5,6},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{3,5},{2,4,5},{2,6},{0,1,5,6},{1,7},{0,2,7},{4,7},{3,6,7},{0,8},{2,8},{1,3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered493 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 493) T=TwentyFiveEightLow.Case493.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case493.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 493)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case493.support T pos))
  · decide +kernel
theorem completion494 : pairCompletion (big 494)=full 494 := by
  have same : big 494=([{3,4,5},{0,1,5,6},{0,2,7},{4,6,7},{1,3,8},{2,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,1,5,6},{0,2,7},{4,6,7},{1,3,8},{2,6,8},{5,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{2,4},{2,5},{3,4,5},{3,6},{0,1,5,6},{1,7},{0,2,7},{3,7},{4,6,7},{0,8},{1,3,8},{4,8},{2,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered494 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 494) T=TwentyFiveEightLow.Case494.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case494.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 494)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case494.support T pos))
  · decide +kernel
theorem completion495 : pairCompletion (big 495)=full 495 := by
  have same : big 495=([{2,4,5},{0,2,6},{1,3,7},{5,6,7},{0,1,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{0,2,6},{1,3,7},{5,6,7},{0,1,5,8},{3,6,8},{4,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{3,5},{2,4,5},{1,6},{0,2,6},{4,6},{0,7},{2,7},{1,3,7},{5,6,7},{2,8},{0,1,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered495 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 495) T=TwentyFiveEightLow.Case495.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case495.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 495)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case495.support T pos))
  · decide +kernel
theorem completion496 : pairCompletion (big 496)=full 496 := by
  have same : big 496=([{0,2,6},{3,5,6},{1,3,7},{4,5,7},{2,4,8},{0,1,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,6},{3,5,6},{1,3,7},{4,5,7},{2,4,8},{0,1,5,8},{6,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{2,5},{1,6},{0,2,6},{4,6},{3,5,6},{0,7},{2,7},{1,3,7},{4,5,7},{3,8},{2,4,8},{0,1,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered496 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 496) T=TwentyFiveEightLow.Case496.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case496.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 496)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case496.support T pos))
  · decide +kernel
theorem completion497 : pairCompletion (big 497)=full 497 := by
  have same : big 497=([{0,1,4,5},{1,3,6},{2,4,6},{0,2,7},{5,6,7},{3,5,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{1,3,6},{2,4,6},{0,2,7},{5,6,7},{3,5,8},{4,7,8}] [{1,2},{0,3},{2,3},{3,4},{2,5},{0,1,4,5},{0,6},{1,3,6},{2,4,6},{1,7},{0,2,7},{3,7},{5,6,7},{0,8},{1,8},{2,8},{3,5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered497 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 497) T=TwentyFiveEightLow.Case497.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case497.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 497)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case497.support T pos))
  · decide +kernel
theorem completion498 : pairCompletion (big 498)=full 498 := by
  have same : big 498=([{2,3,4},{0,1,4,5},{0,2,6},{3,5,7},{4,6,7},{5,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{0,1,4,5},{0,2,6},{3,5,7},{4,6,7},{5,6,8},{1,7,8}] [{1,2},{0,3},{1,3},{2,3,4},{2,5},{0,1,4,5},{1,6},{0,2,6},{3,6},{0,7},{2,7},{3,5,7},{4,6,7},{0,8},{2,8},{3,8},{4,8},{5,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered498 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 498) T=TwentyFiveEightLow.Case498.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case498.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 498)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case498.support T pos))
  · decide +kernel
theorem completion499 : pairCompletion (big 499)=full 499 := by
  have same : big 499=([{0,1,4,5},{0,2,6},{3,4,6},{2,4,7},{5,6,7},{3,5,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{0,2,6},{3,4,6},{2,4,7},{5,6,7},{3,5,8},{1,7,8}] [{1,2},{0,3},{1,3},{2,3},{2,5},{0,1,4,5},{1,6},{0,2,6},{3,4,6},{0,7},{3,7},{2,4,7},{5,6,7},{0,8},{2,8},{4,8},{3,5,8},{6,8},{1,7,8}]=true
  decide +kernel

theorem recovered499 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 499) T=TwentyFiveEightLow.Case499.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case499.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 499)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case499.support T pos))
  · decide +kernel
theorem completion500 : pairCompletion (big 500)=full 500 := by
  have same : big 500=([{1,2,4},{0,1,6},{3,5,6},{2,5,7},{4,6,7},{0,4,5,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,4},{0,1,6},{3,5,6},{2,5,7},{4,6,7},{0,4,5,8},{3,7,8}] [{0,2},{0,3},{1,3},{2,3},{1,2,4},{3,4},{1,5},{0,1,6},{2,6},{3,5,6},{0,7},{1,7},{2,5,7},{4,6,7},{1,8},{2,8},{0,4,5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered500 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 500) T=TwentyFiveEightLow.Case500.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case500.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 500)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case500.support T pos))
  · decide +kernel
theorem completion501 : pairCompletion (big 501)=full 501 := by
  have same : big 501=([{2,3,4},{0,1,6},{2,5,6},{1,5,7},{4,6,7},{0,4,5,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{0,1,6},{2,5,6},{1,5,7},{4,6,7},{0,4,5,8},{3,7,8}] [{0,2},{1,2},{0,3},{1,3},{1,4},{2,3,4},{3,5},{0,1,6},{3,6},{2,5,6},{0,7},{2,7},{1,5,7},{4,6,7},{1,8},{2,8},{0,4,5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered501 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 501) T=TwentyFiveEightLow.Case501.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case501.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 501)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case501.support T pos))
  · decide +kernel
theorem completion502 : pairCompletion (big 502)=full 502 := by
  have same : big 502=([{0,3,4},{0,1,2,6},{3,5,6},{1,5,7},{4,6,7},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{0,1,2,6},{3,5,6},{1,5,7},{4,6,7},{2,7,8}] [{1,3},{2,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{4,5},{0,1,2,6},{3,5,6},{0,7},{3,7},{1,5,7},{4,6,7},{0,8},{1,8},{3,8},{4,8},{5,8},{6,8},{2,7,8}]=true
  decide +kernel

theorem recovered502 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 502) T=TwentyFiveEightLow.Case502.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case502.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 502)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case502.support T pos))
  · decide +kernel
theorem completion503 : pairCompletion (big 503)=full 503 := by
  have same : big 503=([{2,3,4},{0,1,2,7},{3,5,7},{4,6,7},{5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{0,1,2,7},{3,5,7},{4,6,7},{5,6,8}] [{0,3},{1,3},{0,4},{1,4},{2,3,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{0,1,2,7},{3,5,7},{4,6,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,6,8},{7,8}]=true
  decide +kernel

theorem recovered503 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 503) T=TwentyFiveEightLow.Case503.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case503.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 503)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case503.support T pos))
  · decide +kernel
theorem completion504 : pairCompletion (big 504)=full 504 := by
  have same : big 504=([{2,4,5},{3,6,7},{0,1,2,3,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{3,6,7},{0,1,2,3,8},{4,6,8},{5,7,8}] [{0,4},{1,4},{3,4},{0,5},{1,5},{3,5},{2,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{4,7},{3,6,7},{0,1,2,3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered504 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 504) T=TwentyFiveEightLow.Case504.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case504.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 504)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case504.support T pos))
  · decide +kernel
theorem completion505 : pairCompletion (big 505)=full 505 := by
  have same : big 505=([{2,4,5},{0,1,2,3,7},{4,6,7},{3,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{0,1,2,3,7},{4,6,7},{3,6,8},{5,7,8}] [{0,4},{1,4},{3,4},{0,5},{1,5},{3,5},{2,4,5},{0,6},{1,6},{2,6},{5,6},{0,1,2,3,7},{4,6,7},{0,8},{1,8},{2,8},{4,8},{3,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered505 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 505) T=TwentyFiveEightLow.Case505.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case505.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 505)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case505.support T pos))
  · decide +kernel
theorem completion506 : pairCompletion (big 506)=full 506 := by
  have same : big 506=([{2,3,4},{3,5,7},{4,6,7},{5,6,8},{0,1,2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{3,5,7},{4,6,7},{5,6,8},{0,1,2,7,8}] [{0,3},{1,3},{0,4},{1,4},{2,3,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{3,5,7},{4,6,7},{3,8},{4,8},{5,6,8},{0,1,2,7,8}]=true
  decide +kernel

theorem recovered506 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 506) T=TwentyFiveEightLow.Case506.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case506.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 506)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case506.support T pos))
  · decide +kernel
theorem completion507 : pairCompletion (big 507)=full 507 := by
  have same : big 507=([{1,3,4},{2,5,6},{3,5,7},{4,6,7},{0,1,2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4},{2,5,6},{3,5,7},{4,6,7},{0,1,2,7,8}] [{0,3},{2,3},{0,4},{2,4},{1,3,4},{0,5},{1,5},{4,5},{0,6},{1,6},{3,6},{2,5,6},{3,5,7},{4,6,7},{3,8},{4,8},{5,8},{6,8},{0,1,2,7,8}]=true
  decide +kernel

theorem recovered507 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 507) T=TwentyFiveEightLow.Case507.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case507.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 507)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case507.support T pos))
  · decide +kernel
theorem completion508 : pairCompletion (big 508)=full 508 := by
  have same : big 508=([{0,2,4,5},{1,3,4,6},{0,1,7},{5,6,7},{3,5,8},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4,5},{1,3,4,6},{0,1,7},{5,6,7},{3,5,8},{2,6,8},{4,7,8}] [{1,2},{0,3},{2,3},{1,5},{0,2,4,5},{0,6},{1,3,4,6},{0,1,7},{2,7},{3,7},{5,6,7},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered508 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 508) T=TwentyFiveEightLow.Case508.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case508.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 508)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case508.support T pos))
  · decide +kernel
theorem completion509 : pairCompletion (big 509)=full 509 := by
  have same : big 509=([{0,2,4,5},{1,3,4,6},{3,5,7},{2,6,7},{0,1,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4,5},{1,3,4,6},{3,5,7},{2,6,7},{0,1,8},{5,6,8},{4,7,8}] [{1,2},{0,3},{2,3},{1,5},{0,2,4,5},{0,6},{1,3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered509 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 509) T=TwentyFiveEightLow.Case509.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case509.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 509)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case509.support T pos))
  · decide +kernel
theorem completion510 : pairCompletion (big 510)=full 510 := by
  have same : big 510=([{0,3,4,5},{0,1,6},{2,5,7},{4,6,7},{1,2,4,8},{5,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,5},{0,1,6},{2,5,7},{4,6,7},{1,2,4,8},{5,6,8},{3,7,8}] [{0,2},{1,3},{2,3},{1,5},{0,3,4,5},{0,1,6},{2,6},{3,6},{0,7},{1,7},{2,5,7},{4,6,7},{0,8},{1,2,4,8},{5,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered510 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 510) T=TwentyFiveEightLow.Case510.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case510.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 510)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case510.support T pos))
  · decide +kernel
theorem completion511 : pairCompletion (big 511)=full 511 := by
  have same : big 511=([{0,1,6},{4,5,6},{2,4,7},{3,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{4,5,6},{2,4,7},{3,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}] [{0,2},{1,3},{2,3},{1,4},{0,5},{0,1,6},{2,6},{3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered511 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 511) T=TwentyFiveEightLow.Case511.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case511.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 511)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case511.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
