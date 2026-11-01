import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion96 : pairCompletion (big 96)=full 96 := by
  have same : big 96=([{0,1,2},{0,3,4},{1,3,5},{2,3,6},{4,5,6},{2,5,7},{1,6,7},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,4},{1,3,5},{2,3,6},{4,5,6},{2,5,7},{1,6,7},{4,7,8}] [{0,1,2},{1,4},{2,4},{0,3,4},{0,5},{1,3,5},{0,6},{2,3,6},{4,5,6},{0,7},{3,7},{2,5,7},{1,6,7},{0,8},{1,8},{2,8},{3,8},{5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered96 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 96) T=TwentyFiveEightLow.Case96.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case96.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 96)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case96.support T pos))
  · decide +kernel
theorem completion97 : pairCompletion (big 97)=full 97 := by
  have same : big 97=([{0,1,3},{0,2,4},{1,2,5},{2,3,6},{4,5,6},{1,4,7},{3,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{0,2,4},{1,2,5},{2,3,6},{4,5,6},{1,4,7},{3,5,7},{6,7,8}] [{0,1,3},{0,2,4},{3,4},{0,5},{1,2,5},{0,6},{1,6},{2,3,6},{4,5,6},{0,7},{2,7},{1,4,7},{3,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered97 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 97) T=TwentyFiveEightLow.Case97.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case97.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 97)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case97.support T pos))
  · decide +kernel
theorem completion98 : pairCompletion (big 98)=full 98 := by
  have same : big 98=([{0,2,3},{0,1,5,6},{2,5,7},{4,6,7},{4,5,8},{3,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{0,1,5,6},{2,5,7},{4,6,7},{4,5,8},{3,6,8},{1,7,8}] [{1,2},{1,3},{0,2,3},{0,4},{1,4},{2,4},{3,4},{3,5},{2,6},{0,1,5,6},{0,7},{3,7},{2,5,7},{4,6,7},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered98 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 98) T=TwentyFiveEightLow.Case98.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case98.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 98)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case98.support T pos))
  · decide +kernel
theorem completion99 : pairCompletion (big 99)=full 99 := by
  have same : big 99=([{0,2,3},{2,5,6},{4,5,7},{1,6,7},{0,1,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{2,5,6},{4,5,7},{1,6,7},{0,1,5,8},{4,6,8},{3,7,8}] [{1,2},{1,3},{0,2,3},{0,4},{1,4},{2,4},{3,4},{3,5},{0,6},{3,6},{2,5,6},{0,7},{2,7},{4,5,7},{1,6,7},{2,8},{0,1,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered99 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 99) T=TwentyFiveEightLow.Case99.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case99.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 99)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case99.support T pos))
  · decide +kernel
theorem completion100 : pairCompletion (big 100)=full 100 := by
  have same : big 100=([{0,2,3},{0,1,4,5},{2,4,6},{3,5,7},{1,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{0,1,4,5},{2,4,6},{3,5,7},{1,6,7},{5,6,8},{4,7,8}] [{1,2},{1,3},{0,2,3},{3,4},{2,5},{0,1,4,5},{0,6},{3,6},{2,4,6},{0,7},{2,7},{3,5,7},{1,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered100 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 100) T=TwentyFiveEightLow.Case100.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case100.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 100)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case100.support T pos))
  · decide +kernel
theorem completion101 : pairCompletion (big 101)=full 101 := by
  have same : big 101=([{0,1,4,5},{2,4,6},{3,5,6},{3,4,7},{1,6,7},{0,2,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{2,4,6},{3,5,6},{3,4,7},{1,6,7},{0,2,8},{5,7,8}] [{1,2},{0,3},{1,3},{2,3},{2,5},{0,1,4,5},{0,6},{2,4,6},{3,5,6},{0,7},{2,7},{3,4,7},{1,6,7},{1,8},{0,2,8},{3,8},{4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered101 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 101) T=TwentyFiveEightLow.Case101.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case101.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 101)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case101.support T pos))
  · decide +kernel
theorem completion102 : pairCompletion (big 102)=full 102 := by
  have same : big 102=([{0,1,2},{1,4,6},{3,5,6},{3,4,7},{2,5,7},{0,4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{1,4,6},{3,5,6},{3,4,7},{2,5,7},{0,4,5,8},{6,7,8}] [{0,1,2},{0,3},{1,3},{2,3},{2,4},{1,5},{0,6},{2,6},{1,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{1,8},{2,8},{3,8},{0,4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered102 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 102) T=TwentyFiveEightLow.Case102.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case102.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 102)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case102.support T pos))
  · decide +kernel
theorem completion103 : pairCompletion (big 103)=full 103 := by
  have same : big 103=([{1,4,6},{3,5,6},{3,4,7},{2,5,7},{0,6,7},{1,2,8},{0,4,5,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,6},{3,5,6},{3,4,7},{2,5,7},{0,6,7},{1,2,8},{0,4,5,8}] [{0,1},{0,2},{0,3},{1,3},{2,3},{2,4},{1,5},{2,6},{1,4,6},{3,5,6},{1,7},{3,4,7},{2,5,7},{0,6,7},{1,2,8},{3,8},{0,4,5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered103 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 103) T=TwentyFiveEightLow.Case103.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case103.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 103)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case103.support T pos))
  · decide +kernel
theorem completion104 : pairCompletion (big 104)=full 104 := by
  have same : big 104=([{0,2,3},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{2,4,8},{1,5,8},{3,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{2,4,8},{1,5,8},{3,6,8},{0,7,8}] [{0,1},{1,2},{1,3},{0,2,3},{0,4},{3,4},{0,5},{2,5},{0,6},{1,6},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{2,4,8},{1,5,8},{3,6,8},{0,7,8}]=true
  decide +kernel

theorem recovered104 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 104) T=TwentyFiveEightLow.Case104.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case104.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 104)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case104.support T pos))
  · decide +kernel
theorem completion105 : pairCompletion (big 105)=full 105 := by
  have same : big 105=([{0,2,3},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,1},{1,2},{1,3},{0,2,3},{0,4},{2,4},{0,5},{3,5},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered105 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 105) T=TwentyFiveEightLow.Case105.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case105.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 105)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case105.support T pos))
  · decide +kernel
theorem completion106 : pairCompletion (big 106)=full 106 := by
  have same : big 106=([{0,2,3},{1,4,6},{2,5,6},{2,4,7},{3,5,7},{0,6,7},{4,5,8},{3,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{1,4,6},{2,5,6},{2,4,7},{3,5,7},{0,6,7},{4,5,8},{3,6,8},{1,7,8}] [{0,1},{1,2},{1,3},{0,2,3},{0,4},{3,4},{0,5},{1,5},{1,4,6},{2,5,6},{2,4,7},{3,5,7},{0,6,7},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered106 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 106) T=TwentyFiveEightLow.Case106.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case106.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 106)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case106.support T pos))
  · decide +kernel
theorem completion107 : pairCompletion (big 107)=full 107 := by
  have same : big 107=([{2,3,5},{0,2,6},{4,5,6},{0,3,7},{2,4,7},{1,6,7},{1,4,8},{3,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{0,2,6},{4,5,6},{0,3,7},{2,4,7},{1,6,7},{1,4,8},{3,6,8},{5,7,8}] [{0,1},{1,2},{1,3},{0,4},{3,4},{0,5},{1,5},{2,3,5},{0,2,6},{4,5,6},{0,3,7},{2,4,7},{1,6,7},{0,8},{2,8},{1,4,8},{3,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered107 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 107) T=TwentyFiveEightLow.Case107.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case107.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 107)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case107.support T pos))
  · decide +kernel
theorem completion108 : pairCompletion (big 108)=full 108 := by
  have same : big 108=([{0,1,2},{3,4,5},{1,3,6},{2,4,6},{2,3,7},{1,5,7},{0,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{3,4,5},{1,3,6},{2,4,6},{2,3,7},{1,5,7},{0,6,7},{5,6,8},{4,7,8}] [{0,1,2},{0,3},{0,4},{1,4},{0,5},{2,5},{3,4,5},{1,3,6},{2,4,6},{2,3,7},{1,5,7},{0,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered108 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 108) T=TwentyFiveEightLow.Case108.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case108.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 108)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case108.support T pos))
  · decide +kernel
theorem completion109 : pairCompletion (big 109)=full 109 := by
  have same : big 109=([{1,2,3},{0,1,6},{2,4,6},{3,5,6},{0,2,7},{3,4,7},{1,5,7},{4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3},{0,1,6},{2,4,6},{3,5,6},{0,2,7},{3,4,7},{1,5,7},{4,5,8},{6,7,8}] [{0,3},{1,2,3},{0,4},{1,4},{0,5},{2,5},{0,1,6},{2,4,6},{3,5,6},{0,2,7},{3,4,7},{1,5,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered109 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 109) T=TwentyFiveEightLow.Case109.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case109.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 109)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case109.support T pos))
  · decide +kernel
theorem completion110 : pairCompletion (big 110)=full 110 := by
  have same : big 110=([{0,2,3},{1,4,5},{0,1,6},{2,4,7},{3,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{1,4,5},{0,1,6},{2,4,7},{3,5,7},{6,7,8}] [{1,2},{1,3},{0,2,3},{0,4},{3,4},{0,5},{2,5},{1,4,5},{0,1,6},{2,6},{3,6},{4,6},{5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered110 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 110) T=TwentyFiveEightLow.Case110.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case110.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 110)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case110.support T pos))
  · decide +kernel
theorem completion111 : pairCompletion (big 111)=full 111 := by
  have same : big 111=([{0,1,2,5},{0,3,4,6},{1,3,7},{2,4,7},{5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{0,3,4,6},{1,3,7},{2,4,7},{5,6,8}] [{2,3},{1,4},{0,1,2,5},{3,5},{4,5},{1,6},{2,6},{0,3,4,6},{0,7},{1,3,7},{2,4,7},{5,7},{6,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,6,8},{7,8}]=true
  decide +kernel

theorem recovered111 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 111) T=TwentyFiveEightLow.Case111.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case111.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 111)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case111.support T pos))
  · decide +kernel
theorem completion112 : pairCompletion (big 112)=full 112 := by
  have same : big 112=([{0,1,2},{0,4,5},{1,4,6},{3,5,6},{3,4,7},{2,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,4,5},{1,4,6},{3,5,6},{3,4,7},{2,5,7},{6,7,8}] [{0,1,2},{0,3},{1,3},{2,3},{2,4},{1,5},{0,4,5},{0,6},{2,6},{1,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered112 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 112) T=TwentyFiveEightLow.Case112.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case112.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 112)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case112.support T pos))
  · decide +kernel
theorem completion113 : pairCompletion (big 113)=full 113 := by
  have same : big 113=([{0,1,2},{3,4,5},{0,3,6},{1,4,6},{2,5,6},{1,3,7},{2,4,7},{0,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{3,4,5},{0,3,6},{1,4,6},{2,5,6},{1,3,7},{2,4,7},{0,5,7},{6,7,8}] [{0,1,2},{2,3},{0,4},{1,5},{3,4,5},{0,3,6},{1,4,6},{2,5,6},{1,3,7},{2,4,7},{0,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered113 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 113) T=TwentyFiveEightLow.Case113.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case113.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 113)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case113.support T pos))
  · decide +kernel
theorem completion114 : pairCompletion (big 114)=full 114 := by
  have same : big 114=([{1,2,3},{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3},{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}] [{0,2},{0,3},{1,2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{3,7},{2,4,7},{5,6,7},{2,8},{3,5,8},{4,6,8},{0,1,7,8}]=true
  decide +kernel

theorem recovered114 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 114) T=TwentyFiveEightLow.Case114.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case114.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 114)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case114.support T pos))
  · decide +kernel
theorem completion115 : pairCompletion (big 115)=full 115 := by
  have same : big 115=([{1,2,3},{2,4,6},{3,5,7},{0,1,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3},{2,4,6},{3,5,7},{0,1,6,7},{5,6,8},{4,7,8}] [{0,2},{0,3},{1,2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{3,6},{2,4,6},{2,7},{3,5,7},{0,1,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered115 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 115) T=TwentyFiveEightLow.Case115.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case115.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 115)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case115.support T pos))
  · decide +kernel
theorem completion116 : pairCompletion (big 116)=full 116 := by
  have same : big 116=([{1,2,3},{2,4,6},{4,5,7},{0,1,6,7},{5,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3},{2,4,6},{4,5,7},{0,1,6,7},{5,6,8},{3,7,8}] [{0,2},{0,3},{1,2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{3,5},{3,6},{2,4,6},{2,7},{4,5,7},{0,1,6,7},{0,8},{1,8},{2,8},{4,8},{5,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered116 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 116) T=TwentyFiveEightLow.Case116.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case116.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 116)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case116.support T pos))
  · decide +kernel
theorem completion117 : pairCompletion (big 117)=full 117 := by
  have same : big 117=([{2,3,6},{4,5,6},{3,4,7},{0,1,6,7},{1,2,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,6},{4,5,6},{3,4,7},{0,1,6,7},{1,2,8},{5,7,8}] [{0,2},{0,3},{1,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,5},{2,3,6},{4,5,6},{2,7},{3,4,7},{0,1,6,7},{0,8},{1,2,8},{3,8},{4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered117 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 117) T=TwentyFiveEightLow.Case117.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case117.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 117)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case117.support T pos))
  · decide +kernel
theorem completion118 : pairCompletion (big 118)=full 118 := by
  have same : big 118=([{1,2,6},{3,4,6},{1,3,7},{2,5,7},{4,5,8},{0,6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,6},{3,4,6},{1,3,7},{2,5,7},{4,5,8},{0,6,7,8}] [{0,1},{0,2},{0,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{3,5},{1,2,6},{3,4,6},{5,6},{1,3,7},{4,7},{2,5,7},{1,8},{2,8},{3,8},{4,5,8},{0,6,7,8}]=true
  decide +kernel

theorem recovered118 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 118) T=TwentyFiveEightLow.Case118.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case118.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 118)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case118.support T pos))
  · decide +kernel
theorem completion119 : pairCompletion (big 119)=full 119 := by
  have same : big 119=([{0,1,2},{1,3,6},{4,5,6},{2,4,7},{3,5,7},{0,6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{1,3,6},{4,5,6},{2,4,7},{3,5,7},{0,6,7,8}] [{0,1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{2,6},{1,3,6},{4,5,6},{1,7},{2,4,7},{3,5,7},{1,8},{2,8},{3,8},{4,8},{5,8},{0,6,7,8}]=true
  decide +kernel

theorem recovered119 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 119) T=TwentyFiveEightLow.Case119.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case119.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 119)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case119.support T pos))
  · decide +kernel
theorem completion120 : pairCompletion (big 120)=full 120 := by
  have same : big 120=([{0,1,2,3},{0,4,5},{1,4,6},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{0,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,5},{1,4,6},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{0,6,8},{1,7,8}] [{0,1,2,3},{3,4},{1,5},{0,4,5},{2,6},{1,4,6},{5,6},{0,7},{4,7},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{0,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered120 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 120) T=TwentyFiveEightLow.Case120.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case120.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 120)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case120.support T pos))
  · decide +kernel
theorem completion121 : pairCompletion (big 121)=full 121 := by
  have same : big 121=([{0,1,2,3},{0,4,5},{1,4,6},{2,4,7},{3,5,7},{0,6,7},{2,5,8},{3,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,5},{1,4,6},{2,4,7},{3,5,7},{0,6,7},{2,5,8},{3,6,8},{1,7,8}] [{0,1,2,3},{3,4},{1,5},{0,4,5},{2,6},{1,4,6},{5,6},{2,4,7},{3,5,7},{0,6,7},{0,8},{4,8},{2,5,8},{3,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered121 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 121) T=TwentyFiveEightLow.Case121.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case121.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 121)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case121.support T pos))
  · decide +kernel
theorem completion122 : pairCompletion (big 122)=full 122 := by
  have same : big 122=([{0,3,4},{1,3,5},{2,4,6},{2,3,7},{0,5,7},{1,6,7},{0,1,2,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{2,4,6},{2,3,7},{0,5,7},{1,6,7},{0,1,2,8},{5,6,8},{4,7,8}] [{1,4},{0,3,4},{2,5},{1,3,5},{4,5},{0,6},{3,6},{2,4,6},{2,3,7},{0,5,7},{1,6,7},{0,1,2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered122 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 122) T=TwentyFiveEightLow.Case122.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case122.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 122)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case122.support T pos))
  · decide +kernel
theorem completion123 : pairCompletion (big 123)=full 123 := by
  have same : big 123=([{0,1,2,3},{0,4,5},{1,4,6},{2,5,7},{3,6,7},{3,5,8},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,5},{1,4,6},{2,5,7},{3,6,7},{3,5,8},{2,6,8},{4,7,8}] [{0,1,2,3},{2,4},{3,4},{1,5},{0,4,5},{0,6},{1,4,6},{5,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered123 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 123) T=TwentyFiveEightLow.Case123.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case123.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 123)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case123.support T pos))
  · decide +kernel
theorem completion124 : pairCompletion (big 124)=full 124 := by
  have same : big 124=([{0,1,2,3},{0,4,5},{2,5,6},{3,5,7},{4,6,7},{1,4,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,5},{2,5,6},{3,5,7},{4,6,7},{1,4,8},{3,6,8},{2,7,8}] [{0,1,2,3},{2,4},{3,4},{1,5},{0,4,5},{0,6},{1,6},{2,5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered124 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 124) T=TwentyFiveEightLow.Case124.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case124.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 124)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case124.support T pos))
  · decide +kernel
theorem completion125 : pairCompletion (big 125)=full 125 := by
  have same : big 125=([{0,1,2,3},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,4,8},{1,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,4,8},{1,5,8},{6,7,8}] [{0,1,2,3},{1,4},{0,5},{4,5},{0,6},{1,6},{2,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{2,8},{3,8},{0,4,8},{1,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered125 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 125) T=TwentyFiveEightLow.Case125.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case125.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 125)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case125.support T pos))
  · decide +kernel
theorem completion126 : pairCompletion (big 126)=full 126 := by
  have same : big 126=([{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{0,1,2,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{0,1,2,8},{5,6,8},{4,7,8}] [{2,3},{1,4},{0,3,4},{0,5},{1,3,5},{4,5},{0,6},{1,6},{2,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,1,2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered126 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 126) T=TwentyFiveEightLow.Case126.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case126.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 126)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case126.support T pos))
  · decide +kernel
theorem completion127 : pairCompletion (big 127)=full 127 := by
  have same : big 127=([{0,3,4},{1,3,5},{2,3,6},{4,5,6},{2,5,7},{1,6,7},{0,1,2,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{2,3,6},{4,5,6},{2,5,7},{1,6,7},{0,1,2,8},{4,7,8}] [{1,4},{2,4},{0,3,4},{0,5},{1,3,5},{0,6},{2,3,6},{4,5,6},{0,7},{3,7},{2,5,7},{1,6,7},{0,1,2,8},{3,8},{5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered127 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 127) T=TwentyFiveEightLow.Case127.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case127.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 127)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case127.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
