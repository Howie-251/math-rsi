import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion576 : pairCompletion (big 576)=full 576 := by
  have same : big 576=([{1,3,6},{4,5,6},{2,3,7},{1,4,7},{0,5,7},{0,3,4,8},{2,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,6},{4,5,6},{2,3,7},{1,4,7},{0,5,7},{0,3,4,8},{2,5,8},{6,7,8}] [{0,1},{0,2},{1,2},{2,4},{1,5},{3,5},{0,6},{2,6},{1,3,6},{4,5,6},{2,3,7},{1,4,7},{0,5,7},{1,8},{0,3,4,8},{2,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered576 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 576) T=TwentyFiveEightLow.Case576.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case576.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 576)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case576.support T pos))
  · decide +kernel
theorem completion577 : pairCompletion (big 577)=full 577 := by
  have same : big 577=([{1,3,5},{4,5,6},{2,4,7},{0,5,7},{3,6,7},{0,3,4,8},{2,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,5},{4,5,6},{2,4,7},{0,5,7},{3,6,7},{0,3,4,8},{2,6,8},{1,7,8}] [{0,1},{0,2},{1,2},{2,3},{1,4},{2,5},{1,3,5},{0,6},{1,6},{4,5,6},{2,4,7},{0,5,7},{3,6,7},{0,3,4,8},{5,8},{2,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered577 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 577) T=TwentyFiveEightLow.Case577.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case577.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 577)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case577.support T pos))
  · decide +kernel
theorem completion578 : pairCompletion (big 578)=full 578 := by
  have same : big 578=([{0,2,3,4},{1,2,6},{3,5,6},{1,3,7},{0,5,7},{4,6,7},{4,5,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{1,2,6},{3,5,6},{1,3,7},{0,5,7},{4,6,7},{4,5,8},{2,7,8}] [{0,1},{1,4},{0,2,3,4},{1,5},{2,5},{0,6},{1,2,6},{3,5,6},{1,3,7},{0,5,7},{4,6,7},{0,8},{1,8},{3,8},{4,5,8},{6,8},{2,7,8}]=true
  decide +kernel

theorem recovered578 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 578) T=TwentyFiveEightLow.Case578.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case578.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 578)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case578.support T pos))
  · decide +kernel
theorem completion579 : pairCompletion (big 579)=full 579 := by
  have same : big 579=([{0,2,3,4},{1,2,5},{4,5,6},{1,3,7},{0,5,7},{2,6,7},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{1,2,5},{4,5,6},{1,3,7},{0,5,7},{2,6,7},{3,6,8},{4,7,8}] [{0,1},{1,4},{0,2,3,4},{1,2,5},{3,5},{0,6},{1,6},{4,5,6},{1,3,7},{0,5,7},{2,6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered579 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 579) T=TwentyFiveEightLow.Case579.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case579.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 579)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case579.support T pos))
  · decide +kernel
theorem completion580 : pairCompletion (big 580)=full 580 := by
  have same : big 580=([{0,2,5},{1,3,6},{4,5,6},{1,2,7},{0,4,7},{3,5,7},{2,3,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,5},{1,3,6},{4,5,6},{1,2,7},{0,4,7},{3,5,7},{2,3,4,8},{6,7,8}] [{0,1},{0,3},{1,4},{1,5},{0,2,5},{0,6},{2,6},{1,3,6},{4,5,6},{1,2,7},{0,4,7},{3,5,7},{0,8},{1,8},{2,3,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered580 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 580) T=TwentyFiveEightLow.Case580.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case580.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 580)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case580.support T pos))
  · decide +kernel
theorem completion581 : pairCompletion (big 581)=full 581 := by
  have same : big 581=([{1,3,4,5},{2,3,6,7},{0,1,2,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4,5},{2,3,6,7},{0,1,2,8},{4,6,8},{5,7,8}] [{0,3},{0,4},{2,4},{0,5},{2,5},{1,3,4,5},{0,6},{1,6},{5,6},{0,7},{1,7},{4,7},{2,3,6,7},{0,1,2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered581 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 581) T=TwentyFiveEightLow.Case581.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case581.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 581)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case581.support T pos))
  · decide +kernel
theorem completion582 : pairCompletion (big 582)=full 582 := by
  have same : big 582=([{1,3,4,6},{0,1,2,7},{4,5,7},{2,3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4,6},{0,1,2,7},{4,5,7},{2,3,5,8},{6,7,8}] [{0,3},{0,4},{2,4},{0,5},{1,5},{0,6},{2,6},{1,3,4,6},{5,6},{0,1,2,7},{3,7},{4,5,7},{0,8},{1,8},{4,8},{2,3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered582 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 582) T=TwentyFiveEightLow.Case582.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case582.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 582)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case582.support T pos))
  · decide +kernel
theorem completion583 : pairCompletion (big 583)=full 583 := by
  have same : big 583=([{0,1,2,7},{3,4,7},{5,6,7},{1,3,5,8},{2,4,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,7},{3,4,7},{5,6,7},{1,3,5,8},{2,4,6,8}] [{0,3},{2,3},{0,4},{1,4},{0,5},{2,5},{4,5},{0,6},{1,6},{3,6},{0,1,2,7},{3,4,7},{5,6,7},{0,8},{1,3,5,8},{2,4,6,8},{7,8}]=true
  decide +kernel

theorem recovered583 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 583) T=TwentyFiveEightLow.Case583.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case583.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 583)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case583.support T pos))
  · decide +kernel
theorem completion584 : pairCompletion (big 584)=full 584 := by
  have same : big 584=([{1,2,3,4},{3,5,7},{4,6,7},{2,5,6,8},{0,1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3,4},{3,5,7},{4,6,7},{2,5,6,8},{0,1,7,8}] [{0,2},{0,3},{0,4},{1,2,3,4},{0,5},{1,5},{4,5},{0,6},{1,6},{3,6},{2,7},{3,5,7},{4,6,7},{3,8},{4,8},{2,5,6,8},{0,1,7,8}]=true
  decide +kernel

theorem recovered584 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 584) T=TwentyFiveEightLow.Case584.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case584.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 584)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case584.support T pos))
  · decide +kernel
theorem completion585 : pairCompletion (big 585)=full 585 := by
  have same : big 585=([{0,1,3,4},{0,2,5,6},{3,5,7},{4,6,7},{1,2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{0,2,5,6},{3,5,7},{4,6,7},{1,2,7,8}] [{2,3},{2,4},{0,1,3,4},{1,5},{4,5},{1,6},{3,6},{0,2,5,6},{0,7},{3,5,7},{4,6,7},{0,8},{3,8},{4,8},{5,8},{6,8},{1,2,7,8}]=true
  decide +kernel

theorem recovered585 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 585) T=TwentyFiveEightLow.Case585.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case585.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 585)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case585.support T pos))
  · decide +kernel
theorem completion586 : pairCompletion (big 586)=full 586 := by
  have same : big 586=([{0,1,3,4,5},{2,3,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4,5},{2,3,6,7},{4,6,8},{5,7,8}] [{0,2},{1,2},{2,4},{2,5},{0,1,3,4,5},{0,6},{1,6},{5,6},{0,7},{1,7},{4,7},{2,3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered586 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 586) T=TwentyFiveEightLow.Case586.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case586.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 586)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case586.support T pos))
  · decide +kernel
theorem completion587 : pairCompletion (big 587)=full 587 := by
  have same : big 587=([{0,1,3,4,5},{4,6,7},{2,3,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4,5},{4,6,7},{2,3,6,8},{5,7,8}] [{0,2},{1,2},{2,4},{2,5},{0,1,3,4,5},{0,6},{1,6},{5,6},{0,7},{1,7},{2,7},{3,7},{4,6,7},{0,8},{1,8},{4,8},{2,3,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered587 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 587) T=TwentyFiveEightLow.Case587.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case587.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 587)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case587.support T pos))
  · decide +kernel
theorem completion588 : pairCompletion (big 588)=full 588 := by
  have same : big 588=([{2,3,5,6},{4,5,7},{0,1,3,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5,6},{4,5,7},{0,1,3,4,8},{6,7,8}] [{0,2},{1,2},{2,4},{0,5},{1,5},{0,6},{1,6},{4,6},{2,3,5,6},{0,7},{1,7},{2,7},{3,7},{4,5,7},{2,8},{0,1,3,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered588 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 588) T=TwentyFiveEightLow.Case588.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case588.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 588)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case588.support T pos))
  · decide +kernel
theorem completion589 : pairCompletion (big 589)=full 589 := by
  have same : big 589=([{3,5,7},{4,6,7},{0,1,3,4,8},{2,5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,5,7},{4,6,7},{0,1,3,4,8},{2,5,6,8}] [{0,2},{1,2},{2,3},{2,4},{0,5},{1,5},{4,5},{0,6},{1,6},{3,6},{0,7},{1,7},{2,7},{3,5,7},{4,6,7},{0,1,3,4,8},{2,5,6,8},{7,8}]=true
  decide +kernel

theorem recovered589 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 589) T=TwentyFiveEightLow.Case589.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case589.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 589)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case589.support T pos))
  · decide +kernel
theorem completion590 : pairCompletion (big 590)=full 590 := by
  have same : big 590=([{0,1,2,3,4},{3,5,7},{4,6,7},{2,5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,4},{3,5,7},{4,6,7},{2,5,6,8}] [{0,1,2,3,4},{0,5},{1,5},{4,5},{0,6},{1,6},{3,6},{0,7},{1,7},{2,7},{3,5,7},{4,6,7},{0,8},{1,8},{3,8},{4,8},{2,5,6,8},{7,8}]=true
  decide +kernel

theorem recovered590 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 590) T=TwentyFiveEightLow.Case590.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case590.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 590)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case590.support T pos))
  · decide +kernel
theorem completion591 : pairCompletion (big 591)=full 591 := by
  have same : big 591=([{1,2,5,6},{3,5,7},{4,6,7},{0,2,3,4,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,5,6},{3,5,7},{4,6,7},{0,2,3,4,8}] [{0,1},{1,3},{1,4},{0,5},{4,5},{0,6},{3,6},{1,2,5,6},{0,7},{1,7},{2,7},{3,5,7},{4,6,7},{1,8},{0,2,3,4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered591 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 591) T=TwentyFiveEightLow.Case591.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case591.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 591)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case591.support T pos))
  · decide +kernel
theorem completion592 : pairCompletion (big 592)=full 592 := by
  have same : big 592=([{2,3,4,5},{0,1,5,7},{3,6,7},{1,2,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4,5},{0,1,5,7},{3,6,7},{1,2,8},{5,6,8},{4,7,8}] [{0,2},{0,3},{1,3},{0,4},{1,4},{2,3,4,5},{0,6},{1,6},{2,6},{4,6},{2,7},{0,1,5,7},{3,6,7},{0,8},{1,2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered592 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 592) T=TwentyFiveEightLow.Case592.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case592.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 592)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case592.support T pos))
  · decide +kernel
theorem completion593 : pairCompletion (big 593)=full 593 := by
  have same : big 593=([{2,3,4,5},{1,2,7},{5,6,7},{0,1,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4,5},{1,2,7},{5,6,7},{0,1,5,8},{3,6,8},{4,7,8}] [{0,2},{0,3},{1,3},{0,4},{1,4},{2,3,4,5},{0,6},{1,6},{2,6},{4,6},{0,7},{1,2,7},{3,7},{5,6,7},{2,8},{0,1,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered593 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 593) T=TwentyFiveEightLow.Case593.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case593.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 593)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case593.support T pos))
  · decide +kernel
theorem completion594 : pairCompletion (big 594)=full 594 := by
  have same : big 594=([{2,3,4,5},{0,1,5,6},{1,2,7},{3,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4,5},{0,1,5,6},{1,2,7},{3,6,7},{4,6,8},{5,7,8}] [{0,2},{0,3},{1,3},{0,4},{1,4},{2,3,4,5},{2,6},{0,1,5,6},{0,7},{1,2,7},{4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered594 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 594) T=TwentyFiveEightLow.Case594.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case594.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 594)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case594.support T pos))
  · decide +kernel
theorem completion595 : pairCompletion (big 595)=full 595 := by
  have same : big 595=([{3,5,6},{1,2,7},{4,6,7},{2,3,4,8},{0,1,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,5,6},{1,2,7},{4,6,7},{2,3,4,8},{0,1,6,8},{5,7,8}] [{0,2},{0,3},{1,3},{0,4},{1,4},{0,5},{1,5},{2,5},{4,5},{2,6},{3,5,6},{0,7},{1,2,7},{3,7},{4,6,7},{2,3,4,8},{0,1,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered595 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 595) T=TwentyFiveEightLow.Case595.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case595.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 595)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case595.support T pos))
  · decide +kernel
theorem completion596 : pairCompletion (big 596)=full 596 := by
  have same : big 596=([{0,1,4,6},{3,5,6},{1,2,7},{4,5,7},{2,3,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,6},{3,5,6},{1,2,7},{4,5,7},{2,3,4,8},{6,7,8}] [{0,2},{0,3},{1,3},{0,5},{1,5},{2,5},{2,6},{0,1,4,6},{3,5,6},{0,7},{1,2,7},{3,7},{4,5,7},{0,8},{1,8},{2,3,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered596 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 596) T=TwentyFiveEightLow.Case596.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case596.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 596)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case596.support T pos))
  · decide +kernel
theorem completion597 : pairCompletion (big 597)=full 597 := by
  have same : big 597=([{0,1,4,6},{1,2,7},{4,5,7},{3,6,7},{2,3,4,8},{5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,6},{1,2,7},{4,5,7},{3,6,7},{2,3,4,8},{5,6,8}] [{0,2},{0,3},{1,3},{0,5},{1,5},{2,5},{3,5},{2,6},{0,1,4,6},{0,7},{1,2,7},{4,5,7},{3,6,7},{0,8},{1,8},{2,3,4,8},{5,6,8},{7,8}]=true
  decide +kernel

theorem recovered597 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 597) T=TwentyFiveEightLow.Case597.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case597.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 597)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case597.support T pos))
  · decide +kernel
theorem completion598 : pairCompletion (big 598)=full 598 := by
  have same : big 598=([{0,3,4,6},{1,5,6},{4,5,7},{2,6,7},{1,2,4,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,6},{1,5,6},{4,5,7},{2,6,7},{1,2,4,8},{3,7,8}] [{0,1},{0,2},{1,3},{2,3},{0,5},{2,5},{3,5},{0,3,4,6},{1,5,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,8},{1,2,4,8},{5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered598 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 598) T=TwentyFiveEightLow.Case598.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case598.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 598)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case598.support T pos))
  · decide +kernel
theorem completion599 : pairCompletion (big 599)=full 599 := by
  have same : big 599=([{1,2,3,4},{1,5,6},{4,5,7},{2,6,7},{0,4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3,4},{1,5,6},{4,5,7},{2,6,7},{0,4,6,8},{3,7,8}] [{0,1},{0,2},{0,3},{1,2,3,4},{0,5},{2,5},{3,5},{3,6},{1,5,6},{0,7},{1,7},{4,5,7},{2,6,7},{1,8},{2,8},{5,8},{0,4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered599 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 599) T=TwentyFiveEightLow.Case599.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case599.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 599)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case599.support T pos))
  · decide +kernel
theorem completion600 : pairCompletion (big 600)=full 600 := by
  have same : big 600=([{0,2,3,4},{2,5,6},{0,1,7},{4,5,7},{3,6,7},{1,4,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{2,5,6},{0,1,7},{4,5,7},{3,6,7},{1,4,6,8}] [{1,2},{1,3},{0,2,3,4},{0,5},{1,5},{3,5},{0,6},{2,5,6},{0,1,7},{2,7},{4,5,7},{3,6,7},{0,8},{2,8},{3,8},{5,8},{1,4,6,8},{7,8}]=true
  decide +kernel

theorem recovered600 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 600) T=TwentyFiveEightLow.Case600.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case600.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 600)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case600.support T pos))
  · decide +kernel
theorem completion601 : pairCompletion (big 601)=full 601 := by
  have same : big 601=([{2,3,4,5},{3,6,7},{0,1,2,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4,5},{3,6,7},{0,1,2,8},{4,6,8},{5,7,8}] [{0,3},{1,3},{0,4},{1,4},{0,5},{1,5},{2,3,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{4,7},{3,6,7},{0,1,2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered601 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 601) T=TwentyFiveEightLow.Case601.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case601.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 601)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case601.support T pos))
  · decide +kernel
theorem completion602 : pairCompletion (big 602)=full 602 := by
  have same : big 602=([{2,3,4,5},{0,1,2,7},{3,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4,5},{0,1,2,7},{3,6,7},{4,6,8},{5,7,8}] [{0,3},{1,3},{0,4},{1,4},{0,5},{1,5},{2,3,4,5},{0,6},{1,6},{2,6},{5,6},{0,1,2,7},{4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered602 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 602) T=TwentyFiveEightLow.Case602.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case602.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 602)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case602.support T pos))
  · decide +kernel
theorem completion603 : pairCompletion (big 603)=full 603 := by
  have same : big 603=([{3,5,6},{0,1,2,7},{4,5,7},{2,3,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,5,6},{0,1,2,7},{4,5,7},{2,3,4,8},{6,7,8}] [{0,3},{1,3},{0,4},{1,4},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{4,6},{3,5,6},{0,1,2,7},{3,7},{4,5,7},{0,8},{1,8},{2,3,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered603 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 603) T=TwentyFiveEightLow.Case603.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case603.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 603)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case603.support T pos))
  · decide +kernel
theorem completion604 : pairCompletion (big 604)=full 604 := by
  have same : big 604=([{0,1,2,7},{3,5,7},{4,6,7},{2,3,4,8},{5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,7},{3,5,7},{4,6,7},{2,3,4,8},{5,6,8}] [{0,3},{1,3},{0,4},{1,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{0,1,2,7},{3,5,7},{4,6,7},{0,8},{1,8},{2,3,4,8},{5,6,8},{7,8}]=true
  decide +kernel

theorem recovered604 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 604) T=TwentyFiveEightLow.Case604.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case604.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 604)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case604.support T pos))
  · decide +kernel
theorem completion605 : pairCompletion (big 605)=full 605 := by
  have same : big 605=([{2,5,6},{3,5,7},{4,6,7},{2,3,4,8},{0,1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,5,6},{3,5,7},{4,6,7},{2,3,4,8},{0,1,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{0,5},{1,5},{4,5},{0,6},{1,6},{3,6},{2,5,6},{2,7},{3,5,7},{4,6,7},{2,3,4,8},{5,8},{6,8},{0,1,7,8}]=true
  decide +kernel

theorem recovered605 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 605) T=TwentyFiveEightLow.Case605.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case605.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 605)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case605.support T pos))
  · decide +kernel
theorem completion606 : pairCompletion (big 606)=full 606 := by
  have same : big 606=([{1,2,3,4},{2,5,6},{3,5,7},{4,6,7},{0,1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3,4},{2,5,6},{3,5,7},{4,6,7},{0,1,7,8}] [{0,2},{0,3},{0,4},{1,2,3,4},{0,5},{1,5},{4,5},{0,6},{1,6},{3,6},{2,5,6},{2,7},{3,5,7},{4,6,7},{2,8},{3,8},{4,8},{5,8},{6,8},{0,1,7,8}]=true
  decide +kernel

theorem recovered606 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 606) T=TwentyFiveEightLow.Case606.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case606.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 606)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case606.support T pos))
  · decide +kernel
theorem completion607 : pairCompletion (big 607)=full 607 := by
  have same : big 607=([{2,3,4,5},{5,6,7},{0,1,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4,5},{5,6,7},{0,1,5,8},{3,6,8},{4,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{2,3,4,5},{0,6},{1,6},{2,6},{4,6},{0,7},{1,7},{2,7},{3,7},{5,6,7},{2,8},{0,1,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered607 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 607) T=TwentyFiveEightLow.Case607.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case607.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 607)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case607.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
