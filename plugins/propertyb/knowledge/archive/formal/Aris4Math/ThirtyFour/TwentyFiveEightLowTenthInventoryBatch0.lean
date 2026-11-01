import Aris4Math.ThirtyFour.TwentyFiveEightLowTenthInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowTenthInventory
open TwentyFiveEightLowTenthInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion0 : pairCompletion (big 0)=full 0 := by
  have same : big 0=([{5,6,7},{0,4,7},{1,4,5},{2,4,6},{0,3,5},{1,3,6},{2,3,7},{0,6,8},{1,7,8},{2,5,8},{3,4,8},{0,1,2,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{5,6,7},{0,4,7},{1,4,5},{2,4,6},{0,3,5},{1,3,6},{2,3,7},{0,6,8},{1,7,8},{2,5,8},{3,4,8},{0,1,2,9}] [{0,3,5},{1,4,5},{1,3,6},{2,4,6},{2,3,7},{0,4,7},{5,6,7},{3,4,8},{2,5,8},{0,6,8},{1,7,8},{0,1,2,9},{3,9},{4,9},{5,9},{6,9},{7,9},{8,9}]=true
  decide +kernel

theorem recovered0 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 0) T=TwentyFiveEightLowTenth.Case0.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case0.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 0)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case0.support T pos))
  · decide +kernel
theorem completion1 : pairCompletion (big 1)=full 1 := by
  have same : big 1=([{2,5,6},{0,2,3},{0,5,7},{0,4,6},{3,4,7},{1,3,5},{1,6,7},{1,2,4},{3,6,8},{2,7,8},{4,5,8},{0,1,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,5,6},{0,2,3},{0,5,7},{0,4,6},{3,4,7},{1,3,5},{1,6,7},{1,2,4},{3,6,8},{2,7,8},{4,5,8},{0,1,8,9}] [{0,2,3},{1,2,4},{1,3,5},{0,4,6},{2,5,6},{3,4,7},{0,5,7},{1,6,7},{4,5,8},{3,6,8},{2,7,8},{2,9},{3,9},{4,9},{5,9},{6,9},{7,9},{0,1,8,9}]=true
  decide +kernel

theorem recovered1 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 1) T=TwentyFiveEightLowTenth.Case1.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case1.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 1)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case1.support T pos))
  · decide +kernel
theorem completion2 : pairCompletion (big 2)=full 2 := by
  have same : big 2=([{5,6,7},{0,2,5},{0,4,6},{0,3,7},{1,2,6},{1,4,7},{1,3,5},{2,7,8},{4,5,8},{3,6,8},{0,1,8,9},{2,3,4,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{5,6,7},{0,2,5},{0,4,6},{0,3,7},{1,2,6},{1,4,7},{1,3,5},{2,7,8},{4,5,8},{3,6,8},{0,1,8,9},{2,3,4,9}] [{0,2,5},{1,3,5},{1,2,6},{0,4,6},{0,3,7},{1,4,7},{5,6,7},{4,5,8},{3,6,8},{2,7,8},{2,3,4,9},{5,9},{6,9},{7,9},{0,1,8,9}]=true
  decide +kernel

theorem recovered2 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 2) T=TwentyFiveEightLowTenth.Case2.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case2.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 2)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case2.support T pos))
  · decide +kernel
theorem completion3 : pairCompletion (big 3)=full 3 := by
  have same : big 3=([{0,1,6},{2,3,6},{0,2,7},{3,5,7},{1,4,7},{4,5,6},{1,3,8},{6,7,8},{0,5,8},{2,4,8},{0,3,4,9},{1,2,5,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{2,3,6},{0,2,7},{3,5,7},{1,4,7},{4,5,6},{1,3,8},{6,7,8},{0,5,8},{2,4,8},{0,3,4,9},{1,2,5,9}] [{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{1,3,8},{2,4,8},{0,5,8},{6,7,8},{0,3,4,9},{1,2,5,9},{6,9},{7,9},{8,9}]=true
  decide +kernel

theorem recovered3 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 3) T=TwentyFiveEightLowTenth.Case3.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case3.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 3)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case3.support T pos))
  · decide +kernel
theorem completion4 : pairCompletion (big 4)=full 4 := by
  have same : big 4=([{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,3,8},{0,1,2,9},{7,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,3,8},{0,1,2,9},{7,8,9}] [{1,3},{2,3},{0,4},{0,5},{1,4,5},{0,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{1,6,7},{1,8},{2,8},{0,3,8},{4,8},{5,8},{6,8},{0,1,2,9},{3,9},{4,9},{5,9},{6,9},{7,8,9}]=true
  decide +kernel

theorem recovered4 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 4) T=TwentyFiveEightLowTenth.Case4.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case4.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 4)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case4.support T pos))
  · decide +kernel
theorem completion5 : pairCompletion (big 5)=full 5 := by
  have same : big 5=([{2,4,6},{3,5,6},{1,6,7},{3,4,7},{2,5,7},{0,1,8},{0,2,3,9},{1,4,5,9},{7,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,6},{3,5,6},{1,6,7},{3,4,7},{2,5,7},{0,1,8},{0,2,3,9},{1,4,5,9},{7,8,9}] [{1,2},{1,3},{0,4},{0,5},{0,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{1,6,7},{0,1,8},{2,8},{3,8},{4,8},{5,8},{6,8},{0,2,3,9},{1,4,5,9},{6,9},{7,8,9}]=true
  decide +kernel

theorem recovered5 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 5) T=TwentyFiveEightLowTenth.Case5.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case5.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 5)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case5.support T pos))
  · decide +kernel
theorem completion6 : pairCompletion (big 6)=full 6 := by
  have same : big 6=([{2,3,5},{0,2,6},{1,3,6},{0,1,4},{4,6,7},{0,3,7},{1,2,7},{4,5,8},{5,6,9},{7,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{0,2,6},{1,3,6},{0,1,4},{4,6,7},{0,3,7},{1,2,7},{4,5,8},{5,6,9},{7,8,9}] [{0,1,4},{2,4},{3,4},{0,5},{1,5},{2,3,5},{0,2,6},{1,3,6},{1,2,7},{0,3,7},{5,7},{4,6,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,8},{0,9},{1,9},{2,9},{3,9},{4,9},{5,6,9},{7,8,9}]=true
  decide +kernel

theorem recovered6 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 6) T=TwentyFiveEightLowTenth.Case6.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case6.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 6)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case6.support T pos))
  · decide +kernel
theorem completion7 : pairCompletion (big 7)=full 7 := by
  have same : big 7=([{0,3,4},{1,3,6},{0,6,7},{1,5,7},{2,5,6},{0,1,2},{2,3,7},{4,5,8},{4,6,9},{7,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,6},{0,6,7},{1,5,7},{2,5,6},{0,1,2},{2,3,7},{4,5,8},{4,6,9},{7,8,9}] [{0,1,2},{1,4},{2,4},{0,3,4},{0,5},{3,5},{1,3,6},{2,5,6},{2,3,7},{4,7},{1,5,7},{0,6,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,8},{0,9},{1,9},{2,9},{3,9},{5,9},{4,6,9},{7,8,9}]=true
  decide +kernel

theorem recovered7 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 7) T=TwentyFiveEightLowTenth.Case7.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case7.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 7)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case7.support T pos))
  · decide +kernel
theorem completion8 : pairCompletion (big 8)=full 8 := by
  have same : big 8=([{3,4,5},{0,3,6},{1,4,6},{2,6,7},{0,4,7},{1,3,7},{2,5,8},{5,6,9},{0,1,2,9},{7,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,3,6},{1,4,6},{2,6,7},{0,4,7},{1,3,7},{2,5,8},{5,6,9},{0,1,2,9},{7,8,9}] [{2,3},{2,4},{0,5},{1,5},{3,4,5},{0,3,6},{1,4,6},{1,3,7},{0,4,7},{5,7},{2,6,7},{0,8},{1,8},{3,8},{4,8},{2,5,8},{6,8},{0,1,2,9},{3,9},{4,9},{5,6,9},{7,8,9}]=true
  decide +kernel

theorem recovered8 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 8) T=TwentyFiveEightLowTenth.Case8.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case8.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 8)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case8.support T pos))
  · decide +kernel
theorem completion9 : pairCompletion (big 9)=full 9 := by
  have same : big 9=([{0,3,4},{0,1,5},{2,4,5},{1,2,7},{5,6,7},{1,4,6},{0,2,6},{3,7,8},{3,5,9},{4,7,9},{6,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{0,1,5},{2,4,5},{1,2,7},{5,6,7},{1,4,6},{0,2,6},{3,7,8},{3,5,9},{4,7,9},{6,8,9}] [{1,3},{2,3},{0,3,4},{0,1,5},{2,4,5},{0,2,6},{3,6},{1,4,6},{0,7},{1,2,7},{5,6,7},{0,8},{1,8},{2,8},{4,8},{5,8},{3,7,8},{0,9},{1,9},{2,9},{3,5,9},{4,7,9},{6,8,9}]=true
  decide +kernel

theorem recovered9 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 9) T=TwentyFiveEightLowTenth.Case9.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case9.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 9)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case9.support T pos))
  · decide +kernel
theorem completion10 : pairCompletion (big 10)=full 10 := by
  have same : big 10=([{0,3,4},{0,1,5},{4,5,6},{1,6,7},{2,5,7},{1,2,4},{0,2,6},{3,7,8},{3,5,9},{4,7,9},{6,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{0,1,5},{4,5,6},{1,6,7},{2,5,7},{1,2,4},{0,2,6},{3,7,8},{3,5,9},{4,7,9},{6,8,9}] [{1,3},{2,3},{1,2,4},{0,3,4},{0,1,5},{0,2,6},{3,6},{4,5,6},{0,7},{2,5,7},{1,6,7},{0,8},{1,8},{2,8},{4,8},{5,8},{3,7,8},{0,9},{1,9},{2,9},{3,5,9},{4,7,9},{6,8,9}]=true
  decide +kernel

theorem recovered10 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 10) T=TwentyFiveEightLowTenth.Case10.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case10.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 10)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case10.support T pos))
  · decide +kernel
theorem completion11 : pairCompletion (big 11)=full 11 := by
  have same : big 11=([{0,3,4},{0,5,6},{1,4,5},{1,6,7},{2,5,7},{2,4,6},{0,1,2},{3,7,8},{3,5,9},{4,7,9},{6,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{0,5,6},{1,4,5},{1,6,7},{2,5,7},{2,4,6},{0,1,2},{3,7,8},{3,5,9},{4,7,9},{6,8,9}] [{0,1,2},{1,3},{2,3},{0,3,4},{1,4,5},{3,6},{2,4,6},{0,5,6},{0,7},{2,5,7},{1,6,7},{0,8},{1,8},{2,8},{4,8},{5,8},{3,7,8},{0,9},{1,9},{2,9},{3,5,9},{4,7,9},{6,8,9}]=true
  decide +kernel

theorem recovered11 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 11) T=TwentyFiveEightLowTenth.Case11.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case11.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 11)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case11.support T pos))
  · decide +kernel
theorem completion12 : pairCompletion (big 12)=full 12 := by
  have same : big 12=([{0,3,4},{1,3,6},{0,6,7},{1,5,7},{2,5,6},{2,3,7},{4,5,8},{4,6,9},{0,1,2,9},{7,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,6},{0,6,7},{1,5,7},{2,5,6},{2,3,7},{4,5,8},{4,6,9},{0,1,2,9},{7,8,9}] [{1,4},{2,4},{0,3,4},{0,5},{3,5},{1,3,6},{2,5,6},{2,3,7},{4,7},{1,5,7},{0,6,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,8},{0,1,2,9},{3,9},{5,9},{4,6,9},{7,8,9}]=true
  decide +kernel

theorem recovered12 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 12) T=TwentyFiveEightLowTenth.Case12.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case12.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 12)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case12.support T pos))
  · decide +kernel
theorem completion13 : pairCompletion (big 13)=full 13 := by
  have same : big 13=([{1,5,7},{1,3,6},{0,6,7},{0,3,4},{2,4,6},{2,3,7},{0,1,2},{4,5,8},{5,6,9},{7,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,5,7},{1,3,6},{0,6,7},{0,3,4},{2,4,6},{2,3,7},{0,1,2},{4,5,8},{5,6,9},{7,8,9}] [{0,1,2},{1,4},{0,3,4},{0,5},{2,5},{3,5},{1,3,6},{2,4,6},{2,3,7},{4,7},{1,5,7},{0,6,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,8},{0,9},{1,9},{2,9},{3,9},{4,9},{5,6,9},{7,8,9}]=true
  decide +kernel

theorem recovered13 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 13) T=TwentyFiveEightLowTenth.Case13.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case13.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 13)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case13.support T pos))
  · decide +kernel
theorem completion14 : pairCompletion (big 14)=full 14 := by
  have same : big 14=([{4,5,7},{1,4,6},{0,6,7},{2,3,6},{1,3,7},{0,3,4},{2,5,8},{5,6,9},{7,8,9},{0,1,2,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{4,5,7},{1,4,6},{0,6,7},{2,3,6},{1,3,7},{0,3,4},{2,5,8},{5,6,9},{7,8,9},{0,1,2,9}] [{2,4},{0,3,4},{0,5},{1,5},{3,5},{2,3,6},{1,4,6},{2,7},{1,3,7},{4,5,7},{0,6,7},{0,8},{1,8},{3,8},{4,8},{2,5,8},{6,8},{0,1,2,9},{3,9},{4,9},{5,6,9},{7,8,9}]=true
  decide +kernel

theorem recovered14 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 14) T=TwentyFiveEightLowTenth.Case14.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case14.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 14)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case14.support T pos))
  · decide +kernel
theorem completion15 : pairCompletion (big 15)=full 15 := by
  have same : big 15=([{0,3,4},{1,4,5},{0,5,6},{1,6,7},{2,5,7},{2,4,6},{3,7,8},{3,5,9},{4,7,9},{0,1,2,9},{6,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,4,5},{0,5,6},{1,6,7},{2,5,7},{2,4,6},{3,7,8},{3,5,9},{4,7,9},{0,1,2,9},{6,8,9}] [{1,3},{2,3},{0,3,4},{1,4,5},{3,6},{2,4,6},{0,5,6},{0,7},{2,5,7},{1,6,7},{0,8},{1,8},{2,8},{4,8},{5,8},{3,7,8},{0,1,2,9},{3,5,9},{4,7,9},{6,8,9}]=true
  decide +kernel

theorem recovered15 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 15) T=TwentyFiveEightLowTenth.Case15.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case15.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 15)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case15.support T pos))
  · decide +kernel
theorem completion16 : pairCompletion (big 16)=full 16 := by
  have same : big 16=([{3,4,5},{2,4,7},{1,5,7},{1,2,6},{0,6,7},{0,2,5},{0,1,4},{3,6,8},{3,7,9},{4,6,9},{5,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{2,4,7},{1,5,7},{1,2,6},{0,6,7},{0,2,5},{0,1,4},{3,6,8},{3,7,9},{4,6,9},{5,8,9}] [{0,3},{1,3},{2,3},{0,1,4},{0,2,5},{3,4,5},{1,2,6},{5,6},{2,4,7},{1,5,7},{0,6,7},{0,8},{1,8},{2,8},{4,8},{3,6,8},{7,8},{0,9},{1,9},{2,9},{4,6,9},{3,7,9},{5,8,9}]=true
  decide +kernel

theorem recovered16 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 16) T=TwentyFiveEightLowTenth.Case16.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case16.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 16)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case16.support T pos))
  · decide +kernel
theorem completion17 : pairCompletion (big 17)=full 17 := by
  have same : big 17=([{1,5,7},{1,3,6},{0,6,7},{0,3,4},{2,4,6},{2,3,7},{4,5,8},{5,6,9},{0,1,2,9},{7,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,5,7},{1,3,6},{0,6,7},{0,3,4},{2,4,6},{2,3,7},{4,5,8},{5,6,9},{0,1,2,9},{7,8,9}] [{1,4},{0,3,4},{0,5},{2,5},{3,5},{1,3,6},{2,4,6},{2,3,7},{4,7},{1,5,7},{0,6,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,8},{0,1,2,9},{3,9},{4,9},{5,6,9},{7,8,9}]=true
  decide +kernel

theorem recovered17 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 17) T=TwentyFiveEightLowTenth.Case17.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case17.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 17)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case17.support T pos))
  · decide +kernel
theorem completion18 : pairCompletion (big 18)=full 18 := by
  have same : big 18=([{0,2,3},{2,4,6},{3,4,7},{1,6,7},{1,4,5},{3,5,6},{2,5,7},{0,1,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{2,4,6},{3,4,7},{1,6,7},{1,4,5},{3,5,6},{2,5,7},{0,1,8,9}] [{1,2},{1,3},{0,2,3},{0,4},{0,5},{1,4,5},{0,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{1,6,7},{2,8},{3,8},{4,8},{5,8},{6,8},{7,8},{2,9},{3,9},{4,9},{5,9},{6,9},{7,9},{0,1,8,9}]=true
  decide +kernel

theorem recovered18 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 18) T=TwentyFiveEightLowTenth.Case18.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case18.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 18)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case18.support T pos))
  · decide +kernel
theorem completion19 : pairCompletion (big 19)=full 19 := by
  have same : big 19=([{0,1,5},{3,5,7},{2,4,7},{2,3,6},{1,6,7},{4,5,6},{0,2,8,9},{1,3,4,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{3,5,7},{2,4,7},{2,3,6},{1,6,7},{4,5,6},{0,2,8,9},{1,3,4,9}] [{1,2},{0,3},{0,4},{0,1,5},{2,5},{0,6},{2,3,6},{4,5,6},{0,7},{2,4,7},{3,5,7},{1,6,7},{1,8},{3,8},{4,8},{5,8},{6,8},{7,8},{1,3,4,9},{5,9},{6,9},{7,9},{0,2,8,9}]=true
  decide +kernel

theorem recovered19 : ∀ T : Finset (Fin 10),
    inventory 34 (standard 8) (full 19) T=TwentyFiveEightLowTenth.Case19.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLowTenth.Case19.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 19)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLowTenth.Case19.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowTenthInventory
