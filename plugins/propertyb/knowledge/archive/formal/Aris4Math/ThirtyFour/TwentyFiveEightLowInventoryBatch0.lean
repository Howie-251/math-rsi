import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion0 : pairCompletion (big 0)=full 0 := by
  have same : big 0=([{0,1,2},{0,3,4},{1,3,5},{2,3,6},{4,5,6},{1,4,7},{2,5,7},{0,6,7},{2,4,8},{0,5,8},{1,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,4},{1,3,5},{2,3,6},{4,5,6},{1,4,7},{2,5,7},{0,6,7},{2,4,8},{0,5,8},{1,6,8},{3,7,8}] [{0,1,2},{0,3,4},{1,3,5},{2,3,6},{4,5,6},{1,4,7},{2,5,7},{0,6,7},{2,4,8},{0,5,8},{1,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered0 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 0) T=TwentyFiveEightLow.Case0.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case0.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 0)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case0.support T pos))
  · decide +kernel
theorem completion1 : pairCompletion (big 1)=full 1 := by
  have same : big 1=([{0,1,2},{0,3,4},{1,3,5},{1,4,6},{0,5,7},{2,6,7},{2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,4},{1,3,5},{1,4,6},{0,5,7},{2,6,7},{2,3,8},{5,6,8},{4,7,8}] [{0,1,2},{2,4},{0,3,4},{2,5},{1,3,5},{4,5},{0,6},{3,6},{1,4,6},{1,7},{3,7},{0,5,7},{2,6,7},{0,8},{1,8},{2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered1 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 1) T=TwentyFiveEightLow.Case1.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case1.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 1)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case1.support T pos))
  · decide +kernel
theorem completion2 : pairCompletion (big 2)=full 2 := by
  have same : big 2=([{0,2,3},{1,2,4},{1,3,5},{0,4,6},{0,5,7},{1,6,7},{3,4,8},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{1,2,4},{1,3,5},{0,4,6},{0,5,7},{1,6,7},{3,4,8},{5,6,8},{2,7,8}] [{0,1},{0,2,3},{1,2,4},{2,5},{1,3,5},{4,5},{2,6},{3,6},{0,4,6},{3,7},{4,7},{0,5,7},{1,6,7},{0,8},{1,8},{3,4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered2 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 2) T=TwentyFiveEightLow.Case2.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case2.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 2)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case2.support T pos))
  · decide +kernel
theorem completion3 : pairCompletion (big 3)=full 3 := by
  have same : big 3=([{0,1,2},{0,3,4},{1,3,5},{1,4,6},{0,5,7},{2,6,7},{2,4,8},{5,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,4},{1,3,5},{1,4,6},{0,5,7},{2,6,7},{2,4,8},{5,6,8},{3,7,8}] [{0,1,2},{2,3},{0,3,4},{2,5},{1,3,5},{4,5},{0,6},{3,6},{1,4,6},{1,7},{4,7},{0,5,7},{2,6,7},{0,8},{1,8},{2,4,8},{5,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered3 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 3) T=TwentyFiveEightLow.Case3.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case3.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 3)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case3.support T pos))
  · decide +kernel
theorem completion4 : pairCompletion (big 4)=full 4 := by
  have same : big 4=([{0,2,3},{1,2,4},{1,3,5},{0,4,6},{0,5,7},{1,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{1,2,4},{1,3,5},{0,4,6},{0,5,7},{1,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,1},{0,2,3},{1,2,4},{3,4},{2,5},{1,3,5},{2,6},{0,4,6},{5,6},{3,7},{4,7},{0,5,7},{1,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered4 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 4) T=TwentyFiveEightLow.Case4.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case4.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 4)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case4.support T pos))
  · decide +kernel
theorem completion5 : pairCompletion (big 5)=full 5 := by
  have same : big 5=([{0,1,2},{0,3,4},{1,3,5},{2,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,4},{1,3,5},{2,6,7},{4,6,8},{5,7,8}] [{0,1,2},{2,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{1,3,5},{4,5},{0,6},{1,6},{3,6},{5,6},{0,7},{1,7},{3,7},{4,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered5 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 5) T=TwentyFiveEightLow.Case5.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case5.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 5)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case5.support T pos))
  · decide +kernel
theorem completion6 : pairCompletion (big 6)=full 6 := by
  have same : big 6=([{0,1,4},{0,2,5},{1,3,6},{2,3,7},{4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{0,2,5},{1,3,6},{2,3,7},{4,5,8},{6,7,8}] [{1,2},{0,3},{0,1,4},{2,4},{3,4},{1,5},{0,2,5},{3,5},{0,6},{2,6},{1,3,6},{4,6},{5,6},{0,7},{1,7},{2,3,7},{4,7},{5,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered6 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 6) T=TwentyFiveEightLow.Case6.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case6.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 6)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case6.support T pos))
  · decide +kernel
theorem completion7 : pairCompletion (big 7)=full 7 := by
  have same : big 7=([{0,1,2},{0,3,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,1,2},{1,3},{2,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{0,6},{2,6},{1,5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered7 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 7) T=TwentyFiveEightLow.Case7.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case7.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 7)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case7.support T pos))
  · decide +kernel
theorem completion8 : pairCompletion (big 8)=full 8 := by
  have same : big 8=([{0,2,3},{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,1,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,1,8},{6,7,8}] [{1,2},{1,3},{0,2,3},{0,4},{0,5},{1,4,5},{0,6},{1,6},{2,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{0,1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered8 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 8) T=TwentyFiveEightLow.Case8.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case8.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 8)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case8.support T pos))
  · decide +kernel
theorem completion9 : pairCompletion (big 9)=full 9 := by
  have same : big 9=([{0,1,4},{0,2,5},{1,3,6},{2,3,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{0,2,5},{1,3,6},{2,3,7},{5,6,8},{4,7,8}] [{1,2},{0,3},{0,1,4},{2,4},{3,4},{1,5},{0,2,5},{3,5},{4,5},{0,6},{2,6},{1,3,6},{4,6},{0,7},{1,7},{2,3,7},{5,7},{6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered9 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 9) T=TwentyFiveEightLow.Case9.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case9.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 9)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case9.support T pos))
  · decide +kernel
theorem completion10 : pairCompletion (big 10)=full 10 := by
  have same : big 10=([{0,1,2},{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,3,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,3,8}] [{0,1,2},{1,3},{2,3},{0,4},{0,5},{1,4,5},{0,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{1,6,7},{1,8},{2,8},{0,3,8},{4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered10 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 10) T=TwentyFiveEightLow.Case10.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case10.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 10)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case10.support T pos))
  · decide +kernel
theorem completion11 : pairCompletion (big 11)=full 11 := by
  have same : big 11=([{0,1,2},{1,3,4},{2,5,6},{4,5,7},{3,6,7},{0,3,8},{1,5,8},{4,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{1,3,4},{2,5,6},{4,5,7},{3,6,7},{0,3,8},{1,5,8},{4,6,8},{2,7,8}] [{0,1,2},{2,3},{0,4},{2,4},{1,3,4},{0,5},{3,5},{0,6},{1,6},{2,5,6},{0,7},{1,7},{4,5,7},{3,6,7},{0,3,8},{1,5,8},{4,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered11 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 11) T=TwentyFiveEightLow.Case11.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case11.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 11)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case11.support T pos))
  · decide +kernel
theorem completion12 : pairCompletion (big 12)=full 12 := by
  have same : big 12=([{0,1,2},{1,3,4},{2,5,6},{0,3,7},{1,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{1,3,4},{2,5,6},{0,3,7},{1,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,1,2},{2,3},{0,4},{2,4},{1,3,4},{0,5},{3,5},{0,6},{1,6},{2,5,6},{0,3,7},{1,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered12 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 12) T=TwentyFiveEightLow.Case12.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case12.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 12)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case12.support T pos))
  · decide +kernel
theorem completion13 : pairCompletion (big 13)=full 13 := by
  have same : big 13=([{0,1,2},{1,3,4},{4,5,6},{0,3,7},{1,5,7},{2,6,7},{2,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{1,3,4},{4,5,6},{0,3,7},{1,5,7},{2,6,7},{2,5,8},{3,6,8},{4,7,8}] [{0,1,2},{2,3},{0,4},{2,4},{1,3,4},{0,5},{3,5},{0,6},{1,6},{4,5,6},{0,3,7},{1,5,7},{2,6,7},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered13 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 13) T=TwentyFiveEightLow.Case13.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case13.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 13)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case13.support T pos))
  · decide +kernel
theorem completion14 : pairCompletion (big 14)=full 14 := by
  have same : big 14=([{0,1,2},{1,3,4},{3,5,6},{0,3,7},{2,5,7},{4,6,7},{4,5,8},{2,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{1,3,4},{3,5,6},{0,3,7},{2,5,7},{4,6,7},{4,5,8},{2,6,8},{1,7,8}] [{0,1,2},{2,3},{0,4},{2,4},{1,3,4},{0,5},{1,5},{0,6},{1,6},{3,5,6},{0,3,7},{2,5,7},{4,6,7},{0,8},{3,8},{4,5,8},{2,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered14 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 14) T=TwentyFiveEightLow.Case14.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case14.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 14)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case14.support T pos))
  · decide +kernel
theorem completion15 : pairCompletion (big 15)=full 15 := by
  have same : big 15=([{0,1,2},{1,4,5},{3,4,6},{0,3,7},{2,5,7},{1,6,7},{2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{1,4,5},{3,4,6},{0,3,7},{2,5,7},{1,6,7},{2,3,8},{5,6,8},{4,7,8}] [{0,1,2},{1,3},{0,4},{2,4},{0,5},{3,5},{1,4,5},{0,6},{2,6},{3,4,6},{0,3,7},{2,5,7},{1,6,7},{0,8},{1,8},{2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered15 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 15) T=TwentyFiveEightLow.Case15.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case15.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 15)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case15.support T pos))
  · decide +kernel
theorem completion16 : pairCompletion (big 16)=full 16 := by
  have same : big 16=([{0,1,2},{1,3,4},{3,5,6},{2,3,7},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{1,3,4},{3,5,6},{2,3,7},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{0,7,8}] [{0,1,2},{0,3},{0,4},{2,4},{1,3,4},{0,5},{2,5},{0,6},{1,6},{3,5,6},{2,3,7},{1,5,7},{4,6,7},{1,8},{3,8},{4,5,8},{2,6,8},{0,7,8}]=true
  decide +kernel

theorem recovered16 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 16) T=TwentyFiveEightLow.Case16.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case16.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 16)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case16.support T pos))
  · decide +kernel
theorem completion17 : pairCompletion (big 17)=full 17 := by
  have same : big 17=([{1,2,3},{1,4,5},{3,4,6},{0,1,7},{3,5,7},{2,6,7},{0,2,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3},{1,4,5},{3,4,6},{0,1,7},{3,5,7},{2,6,7},{0,2,8},{5,6,8},{4,7,8}] [{0,3},{1,2,3},{0,4},{2,4},{0,5},{2,5},{1,4,5},{0,6},{1,6},{3,4,6},{0,1,7},{3,5,7},{2,6,7},{1,8},{0,2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered17 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 17) T=TwentyFiveEightLow.Case17.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case17.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 17)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case17.support T pos))
  · decide +kernel
theorem completion18 : pairCompletion (big 18)=full 18 := by
  have same : big 18=([{1,3,4},{2,3,5},{4,5,6},{0,1,7},{2,4,7},{3,6,7},{0,2,8},{1,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4},{2,3,5},{4,5,6},{0,1,7},{2,4,7},{3,6,7},{0,2,8},{1,6,8},{5,7,8}] [{1,2},{0,3},{0,4},{1,3,4},{0,5},{1,5},{2,3,5},{0,6},{2,6},{4,5,6},{0,1,7},{2,4,7},{3,6,7},{0,2,8},{3,8},{4,8},{1,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered18 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 18) T=TwentyFiveEightLow.Case18.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case18.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 18)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case18.support T pos))
  · decide +kernel
theorem completion19 : pairCompletion (big 19)=full 19 := by
  have same : big 19=([{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,3,7},{0,5,7},{1,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,3,7},{0,5,7},{1,6,7},{5,6,8},{4,7,8}] [{0,1,2},{1,4},{0,3,4},{2,5},{1,3,5},{4,5},{0,6},{3,6},{2,4,6},{2,3,7},{0,5,7},{1,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered19 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 19) T=TwentyFiveEightLow.Case19.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case19.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 19)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case19.support T pos))
  · decide +kernel
theorem completion20 : pairCompletion (big 20)=full 20 := by
  have same : big 20=([{0,1,2},{3,4,5},{0,3,7},{1,4,7},{2,6,7},{5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{3,4,5},{0,3,7},{1,4,7},{2,6,7},{5,6,8}] [{0,1,2},{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{2,5},{3,4,5},{0,6},{1,6},{3,6},{4,6},{0,3,7},{1,4,7},{5,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,6,8},{7,8}]=true
  decide +kernel

theorem recovered20 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 20) T=TwentyFiveEightLow.Case20.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case20.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 20)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case20.support T pos))
  · decide +kernel
theorem completion21 : pairCompletion (big 21)=full 21 := by
  have same : big 21=([{0,1,2},{0,3,6},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{3,4,8},{2,5,8},{1,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,6},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{3,4,8},{2,5,8},{1,6,8},{0,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{0,3,6},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{3,4,8},{2,5,8},{1,6,8},{0,7,8}]=true
  decide +kernel

theorem recovered21 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 21) T=TwentyFiveEightLow.Case21.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case21.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 21)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case21.support T pos))
  · decide +kernel
theorem completion22 : pairCompletion (big 22)=full 22 := by
  have same : big 22=([{0,1,2},{0,3,5},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,5},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{2,4},{0,3,5},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered22 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 22) T=TwentyFiveEightLow.Case22.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case22.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 22)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case22.support T pos))
  · decide +kernel
theorem completion23 : pairCompletion (big 23)=full 23 := by
  have same : big 23=([{0,2,5},{1,3,5},{1,2,6},{0,4,6},{0,1,7},{4,5,7},{3,6,7},{3,4,8},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,5},{1,3,5},{1,2,6},{0,4,6},{0,1,7},{4,5,7},{3,6,7},{3,4,8},{5,6,8},{2,7,8}] [{0,3},{2,3},{1,4},{2,4},{0,2,5},{1,3,5},{1,2,6},{0,4,6},{0,1,7},{4,5,7},{3,6,7},{0,8},{1,8},{3,4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered23 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 23) T=TwentyFiveEightLow.Case23.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case23.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 23)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case23.support T pos))
  · decide +kernel
theorem completion24 : pairCompletion (big 24)=full 24 := by
  have same : big 24=([{0,1,2},{0,3,6},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,6},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{3,5},{4,5},{1,6},{2,6},{0,3,6},{0,7},{2,7},{1,4,7},{5,6,7},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered24 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 24) T=TwentyFiveEightLow.Case24.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case24.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 24)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case24.support T pos))
  · decide +kernel
theorem completion25 : pairCompletion (big 25)=full 25 := by
  have same : big 25=([{0,1,2},{0,3,5},{1,4,6},{4,5,7},{3,6,7},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,5},{1,4,6},{4,5,7},{3,6,7},{5,6,8},{2,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{2,4},{3,4},{1,5},{2,5},{0,3,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{4,5,7},{3,6,7},{0,8},{1,8},{3,8},{4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered25 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 25) T=TwentyFiveEightLow.Case25.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case25.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 25)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case25.support T pos))
  · decide +kernel
theorem completion26 : pairCompletion (big 26)=full 26 := by
  have same : big 26=([{0,2,5},{1,3,6},{4,5,6},{3,5,7},{2,6,7},{0,1,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,5},{1,3,6},{4,5,6},{3,5,7},{2,6,7},{0,1,8},{4,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{2,4},{3,4},{1,5},{0,2,5},{0,6},{1,3,6},{4,5,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,1,8},{2,8},{3,8},{5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered26 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 26) T=TwentyFiveEightLow.Case26.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case26.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 26)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case26.support T pos))
  · decide +kernel
theorem completion27 : pairCompletion (big 27)=full 27 := by
  have same : big 27=([{0,1,2},{0,3,6},{1,4,7},{5,6,7},{3,5,8},{4,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,6},{1,4,7},{5,6,7},{3,5,8},{4,6,8},{2,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{2,5},{4,5},{1,6},{2,6},{0,3,6},{0,7},{3,7},{1,4,7},{5,6,7},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered27 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 27) T=TwentyFiveEightLow.Case27.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case27.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 27)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case27.support T pos))
  · decide +kernel
theorem completion28 : pairCompletion (big 28)=full 28 := by
  have same : big 28=([{0,1,2},{0,3,6},{3,4,7},{5,6,7},{1,5,8},{4,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,6},{3,4,7},{5,6,7},{1,5,8},{4,6,8},{2,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{2,5},{3,5},{4,5},{1,6},{2,6},{0,3,6},{0,7},{1,7},{3,4,7},{5,6,7},{0,8},{3,8},{1,5,8},{4,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered28 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 28) T=TwentyFiveEightLow.Case28.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case28.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 28)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case28.support T pos))
  · decide +kernel
theorem completion29 : pairCompletion (big 29)=full 29 := by
  have same : big 29=([{0,1,2},{0,4,6},{3,5,7},{2,6,7},{1,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,4,6},{3,5,7},{2,6,7},{1,3,8},{5,6,8},{4,7,8}] [{0,1,2},{0,3},{2,3},{1,4},{2,4},{3,4},{0,5},{1,5},{2,5},{4,5},{1,6},{3,6},{0,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,8},{2,8},{1,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered29 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 29) T=TwentyFiveEightLow.Case29.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case29.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 29)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case29.support T pos))
  · decide +kernel
theorem completion30 : pairCompletion (big 30)=full 30 := by
  have same : big 30=([{0,1,2},{0,3,5},{1,4,6},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,5},{1,4,6},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{2,4},{3,4},{1,5},{0,3,5},{4,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered30 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 30) T=TwentyFiveEightLow.Case30.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case30.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 30)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case30.support T pos))
  · decide +kernel
theorem completion31 : pairCompletion (big 31)=full 31 := by
  have same : big 31=([{0,1,2},{0,3,5},{3,4,6},{4,5,7},{1,6,7},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,5},{3,4,6},{4,5,7},{1,6,7},{5,6,8},{2,7,8}] [{0,1,2},{1,3},{2,3},{0,4},{1,4},{2,4},{1,5},{2,5},{0,3,5},{0,6},{2,6},{3,4,6},{0,7},{3,7},{4,5,7},{1,6,7},{0,8},{1,8},{3,8},{4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered31 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 31) T=TwentyFiveEightLow.Case31.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case31.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 31)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case31.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
