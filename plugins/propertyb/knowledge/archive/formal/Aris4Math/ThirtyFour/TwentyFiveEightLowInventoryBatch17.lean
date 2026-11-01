import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion544 : pairCompletion (big 544)=full 544 := by
  have same : big 544=([{2,3,4},{0,2,6},{3,5,6},{1,3,7},{2,5,7},{4,6,7},{4,5,8},{1,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{0,2,6},{3,5,6},{1,3,7},{2,5,7},{4,6,7},{4,5,8},{1,6,8},{0,7,8}] [{0,1},{1,2},{0,3},{0,4},{1,4},{2,3,4},{0,5},{1,5},{0,2,6},{3,5,6},{1,3,7},{2,5,7},{4,6,7},{2,8},{3,8},{4,5,8},{1,6,8},{0,7,8}]=true
  decide +kernel

theorem recovered544 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 544) T=TwentyFiveEightLow.Case544.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case544.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 544)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case544.support T pos))
  · decide +kernel
theorem completion545 : pairCompletion (big 545)=full 545 := by
  have same : big 545=([{2,3,4},{1,3,5},{0,1,6},{4,5,6},{0,2,7},{1,4,7},{3,6,7},{2,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{1,3,5},{0,1,6},{4,5,6},{0,2,7},{1,4,7},{3,6,7},{2,6,8},{5,7,8}] [{1,2},{0,3},{0,4},{2,3,4},{0,5},{2,5},{1,3,5},{0,1,6},{4,5,6},{0,2,7},{1,4,7},{3,6,7},{0,8},{1,8},{3,8},{4,8},{2,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered545 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 545) T=TwentyFiveEightLow.Case545.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case545.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 545)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case545.support T pos))
  · decide +kernel
theorem completion546 : pairCompletion (big 546)=full 546 := by
  have same : big 546=([{3,4,5},{3,6,7},{0,1,2,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{3,6,7},{0,1,2,8},{4,6,8},{5,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{4,7},{3,6,7},{0,1,2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered546 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 546) T=TwentyFiveEightLow.Case546.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case546.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 546)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case546.support T pos))
  · decide +kernel
theorem completion547 : pairCompletion (big 547)=full 547 := by
  have same : big 547=([{3,4,5},{0,1,2,7},{3,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,1,2,7},{3,6,7},{4,6,8},{5,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,4,5},{0,6},{1,6},{2,6},{5,6},{0,1,2,7},{4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered547 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 547) T=TwentyFiveEightLow.Case547.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case547.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 547)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case547.support T pos))
  · decide +kernel
theorem completion548 : pairCompletion (big 548)=full 548 := by
  have same : big 548=([{0,1,2,7},{3,4,7},{5,6,7},{3,5,8},{4,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,7},{3,4,7},{5,6,7},{3,5,8},{4,6,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{0,1,2,7},{3,4,7},{5,6,7},{0,8},{1,8},{2,8},{3,5,8},{4,6,8},{7,8}]=true
  decide +kernel

theorem recovered548 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 548) T=TwentyFiveEightLow.Case548.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case548.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 548)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case548.support T pos))
  · decide +kernel
theorem completion549 : pairCompletion (big 549)=full 549 := by
  have same : big 549=([{2,3,4},{2,5,6},{3,5,7},{4,6,7},{0,1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{2,5,6},{3,5,7},{4,6,7},{0,1,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{2,3,4},{0,5},{1,5},{4,5},{0,6},{1,6},{3,6},{2,5,6},{2,7},{3,5,7},{4,6,7},{2,8},{3,8},{4,8},{5,8},{6,8},{0,1,7,8}]=true
  decide +kernel

theorem recovered549 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 549) T=TwentyFiveEightLow.Case549.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case549.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 549)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case549.support T pos))
  · decide +kernel
theorem completion550 : pairCompletion (big 550)=full 550 := by
  have same : big 550=([{0,3,4,5},{0,1,2,6},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,5},{0,1,2,6},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] [{1,3},{2,3},{2,4},{1,5},{0,3,4,5},{0,1,2,6},{3,6},{0,7},{2,7},{1,4,7},{5,6,7},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered550 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 550) T=TwentyFiveEightLow.Case550.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case550.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 550)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case550.support T pos))
  · decide +kernel
theorem completion551 : pairCompletion (big 551)=full 551 := by
  have same : big 551=([{0,3,4,5},{1,4,6},{2,5,7},{3,6,7},{0,1,2,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,5},{1,4,6},{2,5,7},{3,6,7},{0,1,2,8},{5,6,8},{4,7,8}] [{1,3},{2,3},{2,4},{1,5},{0,3,4,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,1,2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered551 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 551) T=TwentyFiveEightLow.Case551.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case551.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 551)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case551.support T pos))
  · decide +kernel
theorem completion552 : pairCompletion (big 552)=full 552 := by
  have same : big 552=([{0,1,3,5},{1,4,6},{4,5,7},{2,6,7},{0,2,4,8},{5,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,5},{1,4,6},{4,5,7},{2,6,7},{0,2,4,8},{5,6,8},{3,7,8}] [{1,2},{2,3},{3,4},{2,5},{0,1,3,5},{0,6},{3,6},{1,4,6},{0,7},{1,7},{4,5,7},{2,6,7},{1,8},{0,2,4,8},{5,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered552 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 552) T=TwentyFiveEightLow.Case552.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case552.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 552)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case552.support T pos))
  · decide +kernel
theorem completion553 : pairCompletion (big 553)=full 553 := by
  have same : big 553=([{0,1,2,5},{1,3,6},{4,5,6},{2,4,7},{3,5,7},{0,3,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{1,3,6},{4,5,6},{2,4,7},{3,5,7},{0,3,4,8},{6,7,8}] [{2,3},{1,4},{0,1,2,5},{0,6},{2,6},{1,3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{1,8},{2,8},{0,3,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered553 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 553) T=TwentyFiveEightLow.Case553.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case553.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 553)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case553.support T pos))
  · decide +kernel
theorem completion554 : pairCompletion (big 554)=full 554 := by
  have same : big 554=([{0,2,3,5},{1,3,6},{4,5,6},{3,4,7},{2,6,7},{0,1,4,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,5},{1,3,6},{4,5,6},{3,4,7},{2,6,7},{0,1,4,8},{5,7,8}] [{1,2},{2,4},{1,5},{0,2,3,5},{0,6},{1,3,6},{4,5,6},{0,7},{1,7},{3,4,7},{2,6,7},{2,8},{3,8},{0,1,4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered554 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 554) T=TwentyFiveEightLow.Case554.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case554.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 554)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case554.support T pos))
  · decide +kernel
theorem completion555 : pairCompletion (big 555)=full 555 := by
  have same : big 555=([{0,3,6},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{2,3,4,8},{0,1,5,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,6},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{2,3,4,8},{0,1,5,8}] [{0,2},{1,2},{1,3},{0,4},{2,5},{1,6},{0,3,6},{4,5,6},{0,7},{1,4,7},{3,5,7},{2,6,7},{2,3,4,8},{0,1,5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered555 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 555) T=TwentyFiveEightLow.Case555.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case555.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 555)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case555.support T pos))
  · decide +kernel
theorem completion556 : pairCompletion (big 556)=full 556 := by
  have same : big 556=([{0,3,4,5},{1,3,6},{2,4,7},{5,6,7},{0,1,8},{2,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,5},{1,3,6},{2,4,7},{5,6,7},{0,1,8},{2,5,8},{4,6,8},{3,7,8}] [{0,2},{1,2},{2,3},{1,4},{1,5},{0,3,4,5},{0,6},{2,6},{1,3,6},{0,7},{1,7},{2,4,7},{5,6,7},{0,1,8},{2,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered556 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 556) T=TwentyFiveEightLow.Case556.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case556.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 556)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case556.support T pos))
  · decide +kernel
theorem completion557 : pairCompletion (big 557)=full 557 := by
  have same : big 557=([{0,3,4,5},{1,3,6},{0,1,7},{2,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,5},{1,3,6},{0,1,7},{2,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] [{0,2},{1,2},{2,3},{1,4},{1,5},{0,3,4,5},{0,6},{2,6},{1,3,6},{0,1,7},{2,4,7},{5,6,7},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered557 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 557) T=TwentyFiveEightLow.Case557.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case557.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 557)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case557.support T pos))
  · decide +kernel
theorem completion558 : pairCompletion (big 558)=full 558 := by
  have same : big 558=([{0,3,4,5},{2,3,6},{0,1,7},{2,4,7},{5,6,7},{1,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,5},{2,3,6},{0,1,7},{2,4,7},{5,6,7},{1,5,8},{4,6,8},{3,7,8}] [{0,2},{1,2},{1,3},{1,4},{2,5},{0,3,4,5},{0,6},{1,6},{2,3,6},{0,1,7},{2,4,7},{5,6,7},{0,8},{2,8},{1,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered558 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 558) T=TwentyFiveEightLow.Case558.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case558.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 558)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case558.support T pos))
  · decide +kernel
theorem completion559 : pairCompletion (big 559)=full 559 := by
  have same : big 559=([{1,3,5},{2,4,6},{0,1,7},{4,5,7},{3,6,7},{0,3,4,8},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,5},{2,4,6},{0,1,7},{4,5,7},{3,6,7},{0,3,4,8},{5,6,8},{2,7,8}] [{0,2},{1,2},{2,3},{1,4},{0,5},{2,5},{1,3,5},{0,6},{1,6},{2,4,6},{0,1,7},{4,5,7},{3,6,7},{1,8},{0,3,4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered559 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 559) T=TwentyFiveEightLow.Case559.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case559.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 559)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case559.support T pos))
  · decide +kernel
theorem completion560 : pairCompletion (big 560)=full 560 := by
  have same : big 560=([{1,3,5},{4,5,6},{0,1,7},{2,4,7},{3,6,7},{0,3,4,8},{2,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,5},{4,5,6},{0,1,7},{2,4,7},{3,6,7},{0,3,4,8},{2,6,8},{5,7,8}] [{0,2},{1,2},{2,3},{1,4},{0,5},{2,5},{1,3,5},{0,6},{1,6},{4,5,6},{0,1,7},{2,4,7},{3,6,7},{1,8},{0,3,4,8},{2,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered560 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 560) T=TwentyFiveEightLow.Case560.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case560.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 560)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case560.support T pos))
  · decide +kernel
theorem completion561 : pairCompletion (big 561)=full 561 := by
  have same : big 561=([{2,3,5},{4,5,6},{0,1,7},{2,4,7},{3,6,7},{0,3,4,8},{1,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{4,5,6},{0,1,7},{2,4,7},{3,6,7},{0,3,4,8},{1,6,8},{5,7,8}] [{0,2},{1,2},{1,3},{1,4},{0,5},{1,5},{2,3,5},{0,6},{2,6},{4,5,6},{0,1,7},{2,4,7},{3,6,7},{2,8},{0,3,4,8},{1,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered561 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 561) T=TwentyFiveEightLow.Case561.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case561.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 561)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case561.support T pos))
  · decide +kernel
theorem completion562 : pairCompletion (big 562)=full 562 := by
  have same : big 562=([{0,2,3,4},{1,2,5},{3,5,6},{0,1,7},{4,5,7},{2,6,7},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{1,2,5},{3,5,6},{0,1,7},{4,5,7},{2,6,7},{4,6,8},{3,7,8}] [{1,3},{1,4},{0,2,3,4},{0,5},{1,2,5},{0,6},{1,6},{3,5,6},{0,1,7},{4,5,7},{2,6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered562 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 562) T=TwentyFiveEightLow.Case562.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case562.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 562)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case562.support T pos))
  · decide +kernel
theorem completion563 : pairCompletion (big 563)=full 563 := by
  have same : big 563=([{0,2,3,4},{1,2,5},{3,5,6},{1,3,7},{4,5,7},{2,6,7},{4,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{1,2,5},{3,5,6},{1,3,7},{4,5,7},{2,6,7},{4,6,8},{0,7,8}] [{0,1},{1,4},{0,2,3,4},{0,5},{1,2,5},{0,6},{1,6},{3,5,6},{1,3,7},{4,5,7},{2,6,7},{1,8},{2,8},{3,8},{5,8},{4,6,8},{0,7,8}]=true
  decide +kernel

theorem recovered563 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 563) T=TwentyFiveEightLow.Case563.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case563.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 563)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case563.support T pos))
  · decide +kernel
theorem completion564 : pairCompletion (big 564)=full 564 := by
  have same : big 564=([{0,2,5},{1,3,6},{4,5,6},{0,4,7},{3,5,7},{2,6,7},{2,3,4,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,5},{1,3,6},{4,5,6},{0,4,7},{3,5,7},{2,6,7},{2,3,4,8},{1,7,8}] [{0,1},{1,2},{0,3},{1,4},{1,5},{0,2,5},{0,6},{1,3,6},{4,5,6},{0,4,7},{3,5,7},{2,6,7},{0,8},{2,3,4,8},{5,8},{6,8},{1,7,8}]=true
  decide +kernel

theorem recovered564 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 564) T=TwentyFiveEightLow.Case564.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case564.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 564)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case564.support T pos))
  · decide +kernel
theorem completion565 : pairCompletion (big 565)=full 565 := by
  have same : big 565=([{0,2,3,4},{1,2,5},{1,3,6},{4,5,6},{3,5,7},{2,6,7},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{1,2,5},{1,3,6},{4,5,6},{3,5,7},{2,6,7},{4,7,8}] [{0,1},{1,4},{0,2,3,4},{0,5},{1,2,5},{0,6},{1,3,6},{4,5,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered565 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 565) T=TwentyFiveEightLow.Case565.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case565.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 565)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case565.support T pos))
  · decide +kernel
theorem completion566 : pairCompletion (big 566)=full 566 := by
  have same : big 566=([{0,3,4,5},{1,2,3,6},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,5},{1,2,3,6},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] [{0,1},{0,2},{2,4},{1,5},{0,3,4,5},{0,6},{1,2,3,6},{0,7},{2,7},{1,4,7},{5,6,7},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered566 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 566) T=TwentyFiveEightLow.Case566.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case566.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 566)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case566.support T pos))
  · decide +kernel
theorem completion567 : pairCompletion (big 567)=full 567 := by
  have same : big 567=([{0,3,4,5},{1,4,6},{2,5,7},{3,6,7},{1,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,5},{1,4,6},{2,5,7},{3,6,7},{1,2,3,8},{5,6,8},{4,7,8}] [{0,1},{0,2},{2,4},{1,5},{0,3,4,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,8},{1,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered567 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 567) T=TwentyFiveEightLow.Case567.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case567.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 567)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case567.support T pos))
  · decide +kernel
theorem completion568 : pairCompletion (big 568)=full 568 := by
  have same : big 568=([{1,2,3,5},{1,4,6},{4,5,7},{3,6,7},{0,3,4,8},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3,5},{1,4,6},{4,5,7},{3,6,7},{0,3,4,8},{5,6,8},{2,7,8}] [{0,1},{0,2},{2,4},{0,5},{1,2,3,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{4,5,7},{3,6,7},{1,8},{0,3,4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered568 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 568) T=TwentyFiveEightLow.Case568.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case568.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 568)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case568.support T pos))
  · decide +kernel
theorem completion569 : pairCompletion (big 569)=full 569 := by
  have same : big 569=([{1,3,6},{4,5,6},{2,4,7},{3,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,6},{4,5,6},{2,4,7},{3,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}] [{0,1},{0,2},{2,3},{1,4},{0,5},{0,6},{2,6},{1,3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered569 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 569) T=TwentyFiveEightLow.Case569.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case569.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 569)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case569.support T pos))
  · decide +kernel
theorem completion570 : pairCompletion (big 570)=full 570 := by
  have same : big 570=([{0,2,3,5},{1,3,6},{4,5,6},{3,4,7},{2,6,7},{1,2,4,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,5},{1,3,6},{4,5,6},{3,4,7},{2,6,7},{1,2,4,8},{5,7,8}] [{0,1},{0,4},{1,5},{0,2,3,5},{0,6},{1,3,6},{4,5,6},{0,7},{1,7},{3,4,7},{2,6,7},{0,8},{3,8},{1,2,4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered570 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 570) T=TwentyFiveEightLow.Case570.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case570.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 570)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case570.support T pos))
  · decide +kernel
theorem completion571 : pairCompletion (big 571)=full 571 := by
  have same : big 571=([{0,1,2,5},{0,3,6},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{2,3,4,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{0,3,6},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{2,3,4,8}] [{1,3},{0,4},{0,1,2,5},{1,6},{0,3,6},{4,5,6},{0,7},{1,4,7},{3,5,7},{2,6,7},{0,8},{1,8},{2,3,4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered571 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 571) T=TwentyFiveEightLow.Case571.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case571.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 571)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case571.support T pos))
  · decide +kernel
theorem completion572 : pairCompletion (big 572)=full 572 := by
  have same : big 572=([{0,3,4,5},{2,4,6},{1,3,7},{5,6,7},{2,3,8},{1,5,8},{0,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,5},{2,4,6},{1,3,7},{5,6,7},{2,3,8},{1,5,8},{0,6,8},{4,7,8}] [{0,1},{0,2},{1,2},{1,4},{2,5},{0,3,4,5},{1,6},{3,6},{2,4,6},{0,7},{2,7},{1,3,7},{5,6,7},{2,3,8},{1,5,8},{0,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered572 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 572) T=TwentyFiveEightLow.Case572.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case572.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 572)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case572.support T pos))
  · decide +kernel
theorem completion573 : pairCompletion (big 573)=full 573 := by
  have same : big 573=([{0,3,4,5},{1,3,6},{1,4,7},{2,5,7},{0,6,7},{2,4,8},{5,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,5},{1,3,6},{1,4,7},{2,5,7},{0,6,7},{2,4,8},{5,6,8},{3,7,8}] [{0,1},{0,2},{1,2},{2,3},{1,5},{0,3,4,5},{2,6},{1,3,6},{4,6},{1,4,7},{2,5,7},{0,6,7},{0,8},{1,8},{2,4,8},{5,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered573 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 573) T=TwentyFiveEightLow.Case573.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case573.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 573)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case573.support T pos))
  · decide +kernel
theorem completion574 : pairCompletion (big 574)=full 574 := by
  have same : big 574=([{0,3,4,5},{1,3,6},{2,3,7},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,5},{1,3,6},{2,3,7},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{0,7,8}] [{0,1},{0,2},{1,2},{2,4},{1,5},{0,3,4,5},{0,6},{2,6},{1,3,6},{2,3,7},{1,4,7},{5,6,7},{1,8},{3,8},{2,5,8},{4,6,8},{0,7,8}]=true
  decide +kernel

theorem recovered574 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 574) T=TwentyFiveEightLow.Case574.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case574.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 574)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case574.support T pos))
  · decide +kernel
theorem completion575 : pairCompletion (big 575)=full 575 := by
  have same : big 575=([{1,4,5},{2,3,6},{1,3,7},{0,5,7},{4,6,7},{0,3,4,8},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,5},{2,3,6},{1,3,7},{0,5,7},{4,6,7},{0,3,4,8},{5,6,8},{2,7,8}] [{0,1},{0,2},{1,2},{2,4},{2,5},{3,5},{1,4,5},{0,6},{1,6},{2,3,6},{1,3,7},{0,5,7},{4,6,7},{1,8},{0,3,4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered575 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 575) T=TwentyFiveEightLow.Case575.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case575.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 575)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case575.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
