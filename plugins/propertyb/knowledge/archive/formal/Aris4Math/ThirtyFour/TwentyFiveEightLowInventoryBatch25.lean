import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion800 : pairCompletion (big 800)=full 800 := by
  have same : big 800=([{4,5,6},{0,1,7},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{4,5,6},{0,1,7},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{1,5},{3,5},{0,6},{2,6},{4,5,6},{0,1,7},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered800 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 800) T=TwentyFiveEightLow.Case800.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case800.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 800)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case800.support T pos))
  · decide +kernel
theorem completion801 : pairCompletion (big 801)=full 801 := by
  have same : big 801=([{0,2,6},{1,5,6},{1,3,7},{0,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,6},{1,5,6},{1,3,7},{0,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,1},{1,2},{0,3},{2,3},{0,4},{1,4},{2,4},{3,4},{2,5},{3,5},{0,2,6},{1,5,6},{1,3,7},{0,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered801 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 801) T=TwentyFiveEightLow.Case801.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case801.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 801)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case801.support T pos))
  · decide +kernel
theorem completion802 : pairCompletion (big 802)=full 802 := by
  have same : big 802=([{0,1,6},{2,4,6},{3,5,6},{2,3,7},{0,4,7},{1,5,7},{4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{2,4,6},{3,5,6},{2,3,7},{0,4,7},{1,5,7},{4,5,8},{6,7,8}] [{0,2},{1,2},{0,3},{1,3},{1,4},{3,4},{0,5},{2,5},{0,1,6},{2,4,6},{3,5,6},{2,3,7},{0,4,7},{1,5,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered802 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 802) T=TwentyFiveEightLow.Case802.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case802.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 802)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case802.support T pos))
  · decide +kernel
theorem completion803 : pairCompletion (big 803)=full 803 := by
  have same : big 803=([{2,4,5},{0,1,6},{3,4,6},{0,4,7},{1,5,7},{2,6,7},{5,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{0,1,6},{3,4,6},{0,4,7},{1,5,7},{2,6,7},{5,6,8},{3,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{1,4},{0,5},{3,5},{2,4,5},{0,1,6},{3,4,6},{0,4,7},{1,5,7},{2,6,7},{0,8},{1,8},{2,8},{4,8},{5,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered803 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 803) T=TwentyFiveEightLow.Case803.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case803.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 803)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case803.support T pos))
  · decide +kernel
theorem completion804 : pairCompletion (big 804)=full 804 := by
  have same : big 804=([{3,4,5},{0,3,6},{1,4,6},{2,5,6},{1,3,7},{2,4,7},{0,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,3,6},{1,4,6},{2,5,6},{1,3,7},{2,4,7},{0,5,7},{6,7,8}] [{0,1},{0,2},{1,2},{2,3},{0,4},{1,5},{3,4,5},{0,3,6},{1,4,6},{2,5,6},{1,3,7},{2,4,7},{0,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered804 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 804) T=TwentyFiveEightLow.Case804.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case804.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 804)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case804.support T pos))
  · decide +kernel
theorem completion805 : pairCompletion (big 805)=full 805 := by
  have same : big 805=([{2,3,5},{3,4,6},{0,1,5,6},{1,2,7},{4,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{3,4,6},{0,1,5,6},{1,2,7},{4,5,7},{6,7,8}] [{0,2},{0,3},{1,3},{0,4},{1,4},{2,4},{2,3,5},{2,6},{3,4,6},{0,1,5,6},{0,7},{1,2,7},{3,7},{4,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered805 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 805) T=TwentyFiveEightLow.Case805.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case805.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 805)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case805.support T pos))
  · decide +kernel
theorem completion806 : pairCompletion (big 806)=full 806 := by
  have same : big 806=([{0,4,5,6},{1,4,7},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{1,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5,6},{1,4,7},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{1,6,8}] [{0,1},{0,2},{1,2},{0,3},{1,3},{2,3},{3,4},{1,5},{2,6},{0,4,5,6},{0,7},{1,4,7},{2,5,7},{3,6,7},{0,8},{2,4,8},{3,5,8},{1,6,8},{7,8}]=true
  decide +kernel

theorem recovered806 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 806) T=TwentyFiveEightLow.Case806.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case806.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 806)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case806.support T pos))
  · decide +kernel
theorem completion807 : pairCompletion (big 807)=full 807 := by
  have same : big 807=([{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,4,5,8},{3,6,8},{2,7,8}] [{0,1},{0,2},{1,2},{0,3},{1,3},{2,3},{2,4},{3,5},{0,6},{1,4,6},{2,5,6},{0,7},{3,4,7},{1,5,7},{6,7},{1,8},{0,4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered807 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 807) T=TwentyFiveEightLow.Case807.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case807.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 807)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case807.support T pos))
  · decide +kernel
theorem completion808 : pairCompletion (big 808)=full 808 := by
  have same : big 808=([{0,3,4,5},{1,3,6},{2,4,6},{2,3,7},{1,5,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,5},{1,3,6},{2,4,6},{2,3,7},{1,5,7},{5,6,8},{4,7,8}] [{0,1},{0,2},{1,2},{1,4},{2,5},{0,3,4,5},{0,6},{1,3,6},{2,4,6},{0,7},{2,3,7},{1,5,7},{6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered808 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 808) T=TwentyFiveEightLow.Case808.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case808.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 808)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case808.support T pos))
  · decide +kernel
theorem completion809 : pairCompletion (big 809)=full 809 := by
  have same : big 809=([{0,3,6},{1,4,6},{2,5,6},{1,3,7},{2,4,7},{0,5,7},{3,4,5,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,6},{1,4,6},{2,5,6},{1,3,7},{2,4,7},{0,5,7},{3,4,5,8}] [{0,1},{0,2},{1,2},{2,3},{0,4},{1,5},{0,3,6},{1,4,6},{2,5,6},{1,3,7},{2,4,7},{0,5,7},{6,7},{0,8},{1,8},{2,8},{3,4,5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered809 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 809) T=TwentyFiveEightLow.Case809.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case809.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 809)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case809.support T pos))
  · decide +kernel
theorem completion810 : pairCompletion (big 810)=full 810 := by
  have same : big 810=([{0,4,5,6},{1,4,7},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{1,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5,6},{1,4,7},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{1,6,8},{0,7,8}] [{0,1},{0,2},{1,2},{0,3},{1,3},{2,3},{3,4},{1,5},{2,6},{0,4,5,6},{1,4,7},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{1,6,8},{0,7,8}]=true
  decide +kernel

theorem recovered810 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 810) T=TwentyFiveEightLow.Case810.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case810.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 810)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case810.support T pos))
  · decide +kernel
theorem completion811 : pairCompletion (big 811)=full 811 := by
  have same : big 811=([{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{0,4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{0,4,5,8},{3,6,8},{2,7,8}] [{0,1},{0,2},{1,2},{0,3},{1,3},{2,3},{2,4},{3,5},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{1,8},{0,4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered811 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 811) T=TwentyFiveEightLow.Case811.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case811.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 811)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case811.support T pos))
  · decide +kernel
theorem completion812 : pairCompletion (big 812)=full 812 := by
  have same : big 812=([{0,3,4,5},{1,3,6},{2,4,6},{2,3,7},{1,5,7},{0,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,5},{1,3,6},{2,4,6},{2,3,7},{1,5,7},{0,6,7},{5,6,8},{4,7,8}] [{0,1},{0,2},{1,2},{1,4},{2,5},{0,3,4,5},{1,3,6},{2,4,6},{2,3,7},{1,5,7},{0,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered812 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 812) T=TwentyFiveEightLow.Case812.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case812.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 812)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case812.support T pos))
  · decide +kernel
theorem completion813 : pairCompletion (big 813)=full 813 := by
  have same : big 813=([{0,3,6},{1,4,6},{2,5,6},{1,3,7},{2,4,7},{0,5,7},{3,4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,6},{1,4,6},{2,5,6},{1,3,7},{2,4,7},{0,5,7},{3,4,5,8},{6,7,8}] [{0,1},{0,2},{1,2},{2,3},{0,4},{1,5},{0,3,6},{1,4,6},{2,5,6},{1,3,7},{2,4,7},{0,5,7},{0,8},{1,8},{2,8},{3,4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered813 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 813) T=TwentyFiveEightLow.Case813.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case813.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 813)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case813.support T pos))
  · decide +kernel
theorem completion814 : pairCompletion (big 814)=full 814 := by
  have same : big 814=([{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{6,7,8}] [{1,2},{0,3},{1,3},{0,4},{2,4},{3,4},{0,5},{1,5},{2,5},{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered814 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 814) T=TwentyFiveEightLow.Case814.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case814.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 814)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case814.support T pos))
  · decide +kernel
theorem completion815 : pairCompletion (big 815)=full 815 := by
  have same : big 815=([{0,1,2,7},{3,5,7},{4,6,7},{1,3,8},{2,4,8},{5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,7},{3,5,7},{4,6,7},{1,3,8},{2,4,8},{5,6,8}] [{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{0,1,2,7},{3,5,7},{4,6,7},{0,8},{1,3,8},{2,4,8},{5,6,8},{7,8}]=true
  decide +kernel

theorem recovered815 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 815) T=TwentyFiveEightLow.Case815.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case815.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 815)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case815.support T pos))
  · decide +kernel
theorem completion816 : pairCompletion (big 816)=full 816 := by
  have same : big 816=([{1,3,7},{2,4,7},{5,6,7},{0,1,2,8},{3,5,8},{4,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,7},{2,4,7},{5,6,7},{0,1,2,8},{3,5,8},{4,6,8}] [{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{0,7},{1,3,7},{2,4,7},{5,6,7},{0,1,2,8},{3,5,8},{4,6,8},{7,8}]=true
  decide +kernel

theorem recovered816 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 816) T=TwentyFiveEightLow.Case816.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case816.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 816)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case816.support T pos))
  · decide +kernel
theorem completion817 : pairCompletion (big 817)=full 817 := by
  have same : big 817=([{0,1,2,6},{3,5,6},{1,3,7},{2,4,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,6},{3,5,6},{1,3,7},{2,4,7},{4,6,8},{5,7,8}] [{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,1,2,6},{3,5,6},{0,7},{1,3,7},{2,4,7},{6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered817 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 817) T=TwentyFiveEightLow.Case817.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case817.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 817)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case817.support T pos))
  · decide +kernel
theorem completion818 : pairCompletion (big 818)=full 818 := by
  have same : big 818=([{0,1,2,6},{3,4,6},{1,3,7},{4,5,7},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,6},{3,4,6},{1,3,7},{4,5,7},{5,6,8},{2,7,8}] [{0,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,5},{0,1,2,6},{3,4,6},{0,7},{1,3,7},{4,5,7},{6,7},{0,8},{1,8},{3,8},{4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered818 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 818) T=TwentyFiveEightLow.Case818.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case818.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 818)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case818.support T pos))
  · decide +kernel
theorem completion819 : pairCompletion (big 819)=full 819 := by
  have same : big 819=([{2,3,6},{4,5,6},{1,2,7},{3,4,7},{0,1,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,6},{4,5,6},{1,2,7},{3,4,7},{0,1,6,8},{5,7,8}] [{0,2},{0,3},{1,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,5},{2,3,6},{4,5,6},{0,7},{1,2,7},{3,4,7},{6,7},{2,8},{3,8},{4,8},{0,1,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered819 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 819) T=TwentyFiveEightLow.Case819.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case819.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 819)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case819.support T pos))
  · decide +kernel
theorem completion820 : pairCompletion (big 820)=full 820 := by
  have same : big 820=([{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{0,1,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{0,1,6,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{6,7},{2,8},{3,8},{4,8},{5,8},{0,1,6,8},{7,8}]=true
  decide +kernel

theorem recovered820 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 820) T=TwentyFiveEightLow.Case820.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case820.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 820)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case820.support T pos))
  · decide +kernel
theorem completion821 : pairCompletion (big 821)=full 821 := by
  have same : big 821=([{0,3,4,7},{1,5,7},{2,6,7},{0,1,2,8},{3,5,8},{4,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,7},{1,5,7},{2,6,7},{0,1,2,8},{3,5,8},{4,6,8}] [{1,3},{2,3},{1,4},{2,4},{0,5},{2,5},{4,5},{0,6},{1,6},{3,6},{5,6},{0,3,4,7},{1,5,7},{2,6,7},{0,1,2,8},{3,5,8},{4,6,8},{7,8}]=true
  decide +kernel

theorem recovered821 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 821) T=TwentyFiveEightLow.Case821.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case821.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 821)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case821.support T pos))
  · decide +kernel
theorem completion822 : pairCompletion (big 822)=full 822 := by
  have same : big 822=([{0,1,3,6},{2,5,6},{0,2,4,7},{1,5,7},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,6},{2,5,6},{0,2,4,7},{1,5,7},{4,6,8},{3,7,8}] [{1,2},{2,3},{1,4},{3,4},{0,5},{3,5},{4,5},{0,1,3,6},{2,5,6},{0,2,4,7},{1,5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered822 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 822) T=TwentyFiveEightLow.Case822.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case822.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 822)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case822.support T pos))
  · decide +kernel
theorem completion823 : pairCompletion (big 823)=full 823 := by
  have same : big 823=([{1,4,6},{2,5,6},{0,1,2,7},{3,4,7},{0,3,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,6},{2,5,6},{0,1,2,7},{3,4,7},{0,3,6,8},{5,7,8}] [{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{3,5},{4,5},{1,4,6},{2,5,6},{0,1,2,7},{3,4,7},{6,7},{1,8},{2,8},{4,8},{0,3,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered823 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 823) T=TwentyFiveEightLow.Case823.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case823.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 823)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case823.support T pos))
  · decide +kernel
theorem completion824 : pairCompletion (big 824)=full 824 := by
  have same : big 824=([{0,4,6},{1,5,6},{2,4,7},{3,5,7},{2,3,6,8},{0,1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,6},{1,5,6},{2,4,7},{3,5,7},{2,3,6,8},{0,1,7,8}] [{0,2},{1,2},{0,3},{1,3},{1,4},{3,4},{0,5},{2,5},{4,5},{0,4,6},{1,5,6},{2,4,7},{3,5,7},{6,7},{4,8},{5,8},{2,3,6,8},{0,1,7,8}]=true
  decide +kernel

theorem recovered824 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 824) T=TwentyFiveEightLow.Case824.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case824.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 824)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case824.support T pos))
  · decide +kernel
theorem completion825 : pairCompletion (big 825)=full 825 := by
  have same : big 825=([{0,1,2,6},{3,4,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,6},{3,4,5,7},{6,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{0,1,2,6},{3,6},{4,6},{5,6},{0,7},{1,7},{2,7},{3,4,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered825 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 825) T=TwentyFiveEightLow.Case825.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case825.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 825)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case825.support T pos))
  · decide +kernel
theorem completion826 : pairCompletion (big 826)=full 826 := by
  have same : big 826=([{0,1,2,6},{3,4,6},{0,3,7},{1,4,7},{2,5,7},{5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,6},{3,4,6},{0,3,7},{1,4,7},{2,5,7},{5,6,8}] [{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{3,5},{4,5},{0,1,2,6},{3,4,6},{0,3,7},{1,4,7},{2,5,7},{6,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,6,8},{7,8}]=true
  decide +kernel

theorem recovered826 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 826) T=TwentyFiveEightLow.Case826.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case826.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 826)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case826.support T pos))
  · decide +kernel
theorem completion827 : pairCompletion (big 827)=full 827 := by
  have same : big 827=([{0,1,2,6},{3,4,5,6},{0,3,7},{1,4,7},{2,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,6},{3,4,5,6},{0,3,7},{1,4,7},{2,5,7},{6,7,8}] [{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{0,1,2,6},{3,4,5,6},{0,3,7},{1,4,7},{2,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered827 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 827) T=TwentyFiveEightLow.Case827.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case827.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 827)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case827.support T pos))
  · decide +kernel
theorem completion828 : pairCompletion (big 828)=full 828 := by
  have same : big 828=([{0,2,3,6},{4,5,6},{1,2,4,7},{3,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,6},{4,5,6},{1,2,4,7},{3,5,7},{6,7,8}] [{0,1},{1,3},{0,4},{3,4},{0,5},{1,5},{2,5},{1,6},{0,2,3,6},{4,5,6},{0,7},{1,2,4,7},{3,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered828 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 828) T=TwentyFiveEightLow.Case828.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case828.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 828)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case828.support T pos))
  · decide +kernel
theorem completion829 : pairCompletion (big 829)=full 829 := by
  have same : big 829=([{3,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,2,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{3,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,2,7,8}]=true
  decide +kernel

theorem recovered829 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 829) T=TwentyFiveEightLow.Case829.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case829.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 829)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case829.support T pos))
  · decide +kernel
theorem completion830 : pairCompletion (big 830)=full 830 := by
  have same : big 830=([{3,4,6},{3,5,7},{0,1,2,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,6},{3,5,7},{0,1,2,6,7},{5,6,8},{4,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{4,5},{3,4,6},{3,5,7},{0,1,2,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered830 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 830) T=TwentyFiveEightLow.Case830.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case830.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 830)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case830.support T pos))
  · decide +kernel
theorem completion831 : pairCompletion (big 831)=full 831 := by
  have same : big 831=([{2,3,6},{4,5,6},{2,4,7},{3,5,7},{0,1,6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,6},{4,5,6},{2,4,7},{3,5,7},{0,1,6,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{2,3,6},{4,5,6},{2,4,7},{3,5,7},{2,8},{3,8},{4,8},{5,8},{0,1,6,7,8}]=true
  decide +kernel

theorem recovered831 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 831) T=TwentyFiveEightLow.Case831.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case831.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 831)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case831.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
