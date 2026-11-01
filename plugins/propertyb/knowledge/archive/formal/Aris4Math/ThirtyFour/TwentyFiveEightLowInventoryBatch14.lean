import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion448 : pairCompletion (big 448)=full 448 := by
  have same : big 448=([{0,4,5},{1,4,6},{2,4,7},{3,5,7},{0,6,7},{2,5,8},{3,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{1,4,6},{2,4,7},{3,5,7},{0,6,7},{2,5,8},{3,6,8},{1,7,8}] [{0,1},{0,2},{1,2},{0,3},{1,3},{2,3},{3,4},{1,5},{0,4,5},{2,6},{1,4,6},{5,6},{2,4,7},{3,5,7},{0,6,7},{0,8},{4,8},{2,5,8},{3,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered448 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 448) T=TwentyFiveEightLow.Case448.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case448.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 448)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case448.support T pos))
  · decide +kernel
theorem completion449 : pairCompletion (big 449)=full 449 := by
  have same : big 449=([{0,3,4},{1,3,5},{2,4,6},{2,3,7},{0,5,7},{1,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{2,4,6},{2,3,7},{0,5,7},{1,6,7},{5,6,8},{4,7,8}] [{0,1},{0,2},{1,2},{1,4},{0,3,4},{2,5},{1,3,5},{4,5},{0,6},{3,6},{2,4,6},{2,3,7},{0,5,7},{1,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered449 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 449) T=TwentyFiveEightLow.Case449.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case449.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 449)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case449.support T pos))
  · decide +kernel
theorem completion450 : pairCompletion (big 450)=full 450 := by
  have same : big 450=([{0,2,3},{1,4,5},{2,4,6},{3,5,6},{0,1,7},{3,4,7},{2,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{1,4,5},{2,4,6},{3,5,6},{0,1,7},{3,4,7},{2,5,7},{6,7,8}] [{1,2},{1,3},{0,2,3},{0,4},{0,5},{1,4,5},{0,6},{1,6},{2,4,6},{3,5,6},{0,1,7},{3,4,7},{2,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered450 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 450) T=TwentyFiveEightLow.Case450.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case450.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 450)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case450.support T pos))
  · decide +kernel
theorem completion451 : pairCompletion (big 451)=full 451 := by
  have same : big 451=([{0,3,4},{0,1,2,6},{4,5,6},{1,3,7},{2,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{0,1,2,6},{4,5,6},{1,3,7},{2,5,7},{6,7,8}] [{2,3},{1,4},{2,4},{0,3,4},{0,5},{1,5},{3,5},{0,1,2,6},{3,6},{4,5,6},{0,7},{1,3,7},{4,7},{2,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered451 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 451) T=TwentyFiveEightLow.Case451.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case451.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 451)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case451.support T pos))
  · decide +kernel
theorem completion452 : pairCompletion (big 452)=full 452 := by
  have same : big 452=([{0,1,4,5},{1,2,6},{3,4,7},{5,6,7},{3,5,8},{4,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{1,2,6},{3,4,7},{5,6,7},{3,5,8},{4,6,8},{2,7,8}] [{0,2},{0,3},{1,3},{2,3},{2,4},{2,5},{0,1,4,5},{0,6},{1,2,6},{3,6},{0,7},{1,7},{3,4,7},{5,6,7},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered452 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 452) T=TwentyFiveEightLow.Case452.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case452.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 452)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case452.support T pos))
  · decide +kernel
theorem completion453 : pairCompletion (big 453)=full 453 := by
  have same : big 453=([{0,1,4,5},{3,4,6},{3,5,7},{2,6,7},{1,2,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{3,4,6},{3,5,7},{2,6,7},{1,2,8},{5,6,8},{4,7,8}] [{0,2},{0,3},{1,3},{2,3},{2,4},{2,5},{0,1,4,5},{0,6},{1,6},{3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,8},{1,2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered453 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 453) T=TwentyFiveEightLow.Case453.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case453.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 453)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case453.support T pos))
  · decide +kernel
theorem completion454 : pairCompletion (big 454)=full 454 := by
  have same : big 454=([{1,2,5},{3,4,6},{4,5,7},{2,6,7},{0,1,4,8},{5,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,5},{3,4,6},{4,5,7},{2,6,7},{0,1,4,8},{5,6,8},{3,7,8}] [{0,2},{0,3},{1,3},{2,3},{2,4},{0,5},{1,2,5},{3,5},{0,6},{1,6},{3,4,6},{0,7},{1,7},{4,5,7},{2,6,7},{2,8},{0,1,4,8},{5,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered454 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 454) T=TwentyFiveEightLow.Case454.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case454.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 454)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case454.support T pos))
  · decide +kernel
theorem completion455 : pairCompletion (big 455)=full 455 := by
  have same : big 455=([{0,1,3,4},{1,2,5},{3,5,6},{4,5,7},{2,6,7},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{1,2,5},{3,5,6},{4,5,7},{2,6,7},{4,6,8},{3,7,8}] [{0,2},{2,3},{2,4},{0,1,3,4},{0,5},{1,2,5},{0,6},{1,6},{3,5,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered455 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 455) T=TwentyFiveEightLow.Case455.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case455.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 455)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case455.support T pos))
  · decide +kernel
theorem completion456 : pairCompletion (big 456)=full 456 := by
  have same : big 456=([{0,1,3,4},{2,3,6},{4,5,6},{2,4,7},{3,5,7},{1,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{2,3,6},{4,5,6},{2,4,7},{3,5,7},{1,5,8},{6,7,8}] [{0,2},{1,2},{0,1,3,4},{0,5},{2,5},{0,6},{1,6},{2,3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,8},{2,8},{3,8},{4,8},{1,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered456 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 456) T=TwentyFiveEightLow.Case456.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case456.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 456)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case456.support T pos))
  · decide +kernel
theorem completion457 : pairCompletion (big 457)=full 457 := by
  have same : big 457=([{1,3,5},{1,4,6},{2,5,6},{4,5,7},{3,6,7},{0,3,4,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,5},{1,4,6},{2,5,6},{4,5,7},{3,6,7},{0,3,4,8},{2,7,8}] [{0,1},{0,2},{1,2},{2,3},{2,4},{0,5},{1,3,5},{0,6},{1,4,6},{2,5,6},{0,7},{1,7},{4,5,7},{3,6,7},{1,8},{0,3,4,8},{5,8},{6,8},{2,7,8}]=true
  decide +kernel

theorem recovered457 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 457) T=TwentyFiveEightLow.Case457.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case457.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 457)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case457.support T pos))
  · decide +kernel
theorem completion458 : pairCompletion (big 458)=full 458 := by
  have same : big 458=([{0,1,5},{2,3,6},{4,5,6},{2,4,7},{3,5,7},{1,6,7},{0,3,4,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{2,3,6},{4,5,6},{2,4,7},{3,5,7},{1,6,7},{0,3,4,8}] [{0,2},{1,2},{1,3},{1,4},{0,1,5},{2,5},{0,6},{2,3,6},{4,5,6},{0,7},{2,4,7},{3,5,7},{1,6,7},{1,8},{2,8},{0,3,4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered458 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 458) T=TwentyFiveEightLow.Case458.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case458.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 458)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case458.support T pos))
  · decide +kernel
theorem completion459 : pairCompletion (big 459)=full 459 := by
  have same : big 459=([{0,1,4,5},{2,4,6},{3,5,7},{1,6,7},{2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{2,4,6},{3,5,7},{1,6,7},{2,3,8},{5,6,8},{4,7,8}] [{0,2},{1,2},{0,3},{1,3},{3,4},{2,5},{0,1,4,5},{0,6},{3,6},{2,4,6},{0,7},{2,7},{3,5,7},{1,6,7},{0,8},{1,8},{2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered459 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 459) T=TwentyFiveEightLow.Case459.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case459.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 459)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case459.support T pos))
  · decide +kernel
theorem completion460 : pairCompletion (big 460)=full 460 := by
  have same : big 460=([{0,1,4,5},{2,4,6},{2,3,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{2,4,6},{2,3,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}] [{0,2},{1,2},{0,3},{1,3},{3,4},{2,5},{0,1,4,5},{0,6},{3,6},{2,4,6},{0,7},{1,7},{2,3,7},{5,6,7},{0,8},{2,8},{3,5,8},{1,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered460 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 460) T=TwentyFiveEightLow.Case460.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case460.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 460)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case460.support T pos))
  · decide +kernel
theorem completion461 : pairCompletion (big 461)=full 461 := by
  have same : big 461=([{2,4,5},{1,5,6},{2,3,7},{4,6,7},{0,1,4,8},{3,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{1,5,6},{2,3,7},{4,6,7},{0,1,4,8},{3,6,8},{5,7,8}] [{0,2},{1,2},{0,3},{1,3},{3,4},{0,5},{3,5},{2,4,5},{0,6},{2,6},{1,5,6},{0,7},{1,7},{2,3,7},{4,6,7},{2,8},{0,1,4,8},{3,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered461 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 461) T=TwentyFiveEightLow.Case461.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case461.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 461)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case461.support T pos))
  · decide +kernel
theorem completion462 : pairCompletion (big 462)=full 462 := by
  have same : big 462=([{0,1,3,4},{2,3,5},{1,5,6},{4,5,7},{3,6,7},{4,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{2,3,5},{1,5,6},{4,5,7},{3,6,7},{4,6,8},{2,7,8}] [{0,2},{1,2},{2,4},{0,1,3,4},{0,5},{2,3,5},{0,6},{2,6},{1,5,6},{0,7},{1,7},{4,5,7},{3,6,7},{0,8},{1,8},{3,8},{5,8},{4,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered462 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 462) T=TwentyFiveEightLow.Case462.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case462.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 462)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case462.support T pos))
  · decide +kernel
theorem completion463 : pairCompletion (big 463)=full 463 := by
  have same : big 463=([{1,2,5},{1,3,6},{4,5,6},{2,4,7},{3,5,7},{0,3,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,5},{1,3,6},{4,5,6},{2,4,7},{3,5,7},{0,3,4,8},{6,7,8}] [{0,1},{0,2},{2,3},{1,4},{0,5},{1,2,5},{0,6},{2,6},{1,3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{1,8},{2,8},{0,3,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered463 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 463) T=TwentyFiveEightLow.Case463.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case463.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 463)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case463.support T pos))
  · decide +kernel
theorem completion464 : pairCompletion (big 464)=full 464 := by
  have same : big 464=([{1,3,5},{2,4,6},{0,5,6},{1,2,7},{4,5,7},{3,6,7},{0,3,4,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,5},{2,4,6},{0,5,6},{1,2,7},{4,5,7},{3,6,7},{0,3,4,8}] [{0,1},{0,2},{2,3},{1,4},{2,5},{1,3,5},{1,6},{2,4,6},{0,5,6},{0,7},{1,2,7},{4,5,7},{3,6,7},{1,8},{2,8},{0,3,4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered464 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 464) T=TwentyFiveEightLow.Case464.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case464.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 464)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case464.support T pos))
  · decide +kernel
theorem completion465 : pairCompletion (big 465)=full 465 := by
  have same : big 465=([{0,1,4,5},{3,4,6},{3,5,7},{0,2,6,7},{1,2,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{3,4,6},{3,5,7},{0,2,6,7},{1,2,8},{5,6,8},{4,7,8}] [{0,3},{1,3},{2,3},{2,4},{2,5},{0,1,4,5},{1,6},{3,4,6},{1,7},{3,5,7},{0,2,6,7},{0,8},{1,2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered465 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 465) T=TwentyFiveEightLow.Case465.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case465.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 465)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case465.support T pos))
  · decide +kernel
theorem completion466 : pairCompletion (big 466)=full 466 := by
  have same : big 466=([{3,4,5},{0,1,5,6},{1,2,7},{4,6,7},{0,2,4,8},{3,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,1,5,6},{1,2,7},{4,6,7},{0,2,4,8},{3,6,8},{5,7,8}] [{0,3},{1,3},{2,3},{1,4},{2,5},{3,4,5},{2,6},{0,1,5,6},{0,7},{1,2,7},{3,7},{4,6,7},{1,8},{0,2,4,8},{3,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered466 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 466) T=TwentyFiveEightLow.Case466.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case466.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 466)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case466.support T pos))
  · decide +kernel
theorem completion467 : pairCompletion (big 467)=full 467 := by
  have same : big 467=([{0,1,3,4},{0,2,5,6},{1,2,7},{3,5,7},{4,6,7},{4,5,8},{3,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{0,2,5,6},{1,2,7},{3,5,7},{4,6,7},{4,5,8},{3,6,8}] [{2,3},{2,4},{0,1,3,4},{1,5},{1,6},{0,2,5,6},{0,7},{1,2,7},{3,5,7},{4,6,7},{0,8},{1,8},{2,8},{4,5,8},{3,6,8},{7,8}]=true
  decide +kernel

theorem recovered467 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 467) T=TwentyFiveEightLow.Case467.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case467.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 467)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case467.support T pos))
  · decide +kernel
theorem completion468 : pairCompletion (big 468)=full 468 := by
  have same : big 468=([{0,1,3,4},{2,3,5},{2,4,6},{4,5,7},{3,6,7},{0,5,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{2,3,5},{2,4,6},{4,5,7},{3,6,7},{0,5,6,8},{1,7,8}] [{0,2},{1,2},{0,1,3,4},{1,5},{2,3,5},{1,6},{2,4,6},{0,7},{2,7},{4,5,7},{3,6,7},{2,8},{3,8},{4,8},{0,5,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered468 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 468) T=TwentyFiveEightLow.Case468.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case468.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 468)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case468.support T pos))
  · decide +kernel
theorem completion469 : pairCompletion (big 469)=full 469 := by
  have same : big 469=([{2,3,4},{2,5,6},{0,1,7},{3,5,7},{4,6,7},{0,4,5,8},{1,3,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{2,5,6},{0,1,7},{3,5,7},{4,6,7},{0,4,5,8},{1,3,6,8}] [{0,2},{1,2},{0,3},{1,4},{2,3,4},{1,5},{0,6},{2,5,6},{0,1,7},{2,7},{3,5,7},{4,6,7},{2,8},{0,4,5,8},{1,3,6,8},{7,8}]=true
  decide +kernel

theorem recovered469 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 469) T=TwentyFiveEightLow.Case469.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case469.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 469)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case469.support T pos))
  · decide +kernel
theorem completion470 : pairCompletion (big 470)=full 470 := by
  have same : big 470=([{0,2,4,5},{1,3,4,6},{1,5,7},{0,6,7},{3,5,8},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4,5},{1,3,4,6},{1,5,7},{0,6,7},{3,5,8},{2,6,8},{4,7,8}] [{0,1},{1,2},{0,3},{2,3},{0,2,4,5},{1,3,4,6},{5,6},{2,7},{3,7},{1,5,7},{0,6,7},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered470 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 470) T=TwentyFiveEightLow.Case470.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case470.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 470)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case470.support T pos))
  · decide +kernel
theorem completion471 : pairCompletion (big 471)=full 471 := by
  have same : big 471=([{2,3,4,5},{0,5,6},{1,5,7},{4,6,7},{0,1,4,8},{2,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4,5},{0,5,6},{1,5,7},{4,6,7},{0,1,4,8},{2,6,8},{3,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3,4,5},{1,6},{3,6},{0,5,6},{0,7},{2,7},{1,5,7},{4,6,7},{0,1,4,8},{5,8},{2,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered471 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 471) T=TwentyFiveEightLow.Case471.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case471.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 471)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case471.support T pos))
  · decide +kernel
theorem completion472 : pairCompletion (big 472)=full 472 := by
  have same : big 472=([{0,4,6},{1,5,6},{2,4,7},{3,5,7},{1,3,4,8},{0,2,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,6},{1,5,6},{2,4,7},{3,5,7},{1,3,4,8},{0,2,5,8},{6,7,8}] [{0,1},{1,2},{0,3},{2,3},{4,5},{2,6},{3,6},{0,4,6},{1,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{1,3,4,8},{0,2,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered472 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 472) T=TwentyFiveEightLow.Case472.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case472.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 472)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case472.support T pos))
  · decide +kernel
theorem completion473 : pairCompletion (big 473)=full 473 := by
  have same : big 473=([{0,1,3,5},{0,4,6},{2,5,6},{1,4,7},{3,6,7},{2,3,4,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,5},{0,4,6},{2,5,6},{1,4,7},{3,6,7},{2,3,4,8},{5,7,8}] [{0,2},{1,2},{0,1,3,5},{4,5},{1,6},{0,4,6},{2,5,6},{0,7},{2,7},{1,4,7},{3,6,7},{0,8},{1,8},{2,3,4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered473 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 473) T=TwentyFiveEightLow.Case473.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case473.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 473)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case473.support T pos))
  · decide +kernel
theorem completion474 : pairCompletion (big 474)=full 474 := by
  have same : big 474=([{0,1,4,5},{2,5,6},{3,4,7},{1,6,7},{2,4,8},{3,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{2,5,6},{3,4,7},{1,6,7},{2,4,8},{3,6,8},{5,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{3,5},{0,1,4,5},{0,6},{4,6},{2,5,6},{0,7},{2,7},{3,4,7},{1,6,7},{0,8},{1,8},{2,4,8},{3,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered474 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 474) T=TwentyFiveEightLow.Case474.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case474.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 474)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case474.support T pos))
  · decide +kernel
theorem completion475 : pairCompletion (big 475)=full 475 := by
  have same : big 475=([{0,1,4,5},{2,5,6},{2,4,7},{3,6,7},{3,4,8},{1,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{2,5,6},{2,4,7},{3,6,7},{3,4,8},{1,6,8},{5,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{3,5},{0,1,4,5},{0,6},{4,6},{2,5,6},{0,7},{1,7},{2,4,7},{3,6,7},{0,8},{2,8},{3,4,8},{1,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered475 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 475) T=TwentyFiveEightLow.Case475.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case475.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 475)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case475.support T pos))
  · decide +kernel
theorem completion476 : pairCompletion (big 476)=full 476 := by
  have same : big 476=([{0,1,4,5},{3,4,6},{2,4,7},{5,6,7},{2,5,8},{1,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{3,4,6},{2,4,7},{5,6,7},{2,5,8},{1,6,8},{3,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{3,5},{0,1,4,5},{0,6},{2,6},{3,4,6},{0,7},{1,7},{2,4,7},{5,6,7},{0,8},{4,8},{2,5,8},{1,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered476 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 476) T=TwentyFiveEightLow.Case476.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case476.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 476)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case476.support T pos))
  · decide +kernel
theorem completion477 : pairCompletion (big 477)=full 477 := by
  have same : big 477=([{2,4,5},{1,5,6},{3,4,7},{2,6,7},{0,1,4,8},{3,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{1,5,6},{3,4,7},{2,6,7},{0,1,4,8},{3,6,8},{5,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{0,5},{3,5},{2,4,5},{0,6},{4,6},{1,5,6},{0,7},{1,7},{3,4,7},{2,6,7},{2,8},{0,1,4,8},{3,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered477 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 477) T=TwentyFiveEightLow.Case477.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case477.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 477)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case477.support T pos))
  · decide +kernel
theorem completion478 : pairCompletion (big 478)=full 478 := by
  have same : big 478=([{2,4,5},{1,5,6},{3,5,7},{4,6,7},{0,1,4,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{1,5,6},{3,5,7},{4,6,7},{0,1,4,8},{3,6,8},{2,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{3,4},{0,5},{2,4,5},{0,6},{2,6},{1,5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,1,4,8},{5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered478 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 478) T=TwentyFiveEightLow.Case478.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case478.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 478)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case478.support T pos))
  · decide +kernel
theorem completion479 : pairCompletion (big 479)=full 479 := by
  have same : big 479=([{0,1,3,4},{2,3,5},{1,5,6},{2,4,7},{3,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{2,3,5},{1,5,6},{2,4,7},{3,6,7},{4,6,8},{5,7,8}] [{0,2},{1,2},{0,1,3,4},{0,5},{2,3,5},{4,5},{0,6},{2,6},{1,5,6},{0,7},{1,7},{2,4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered479 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 479) T=TwentyFiveEightLow.Case479.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case479.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 479)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case479.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
