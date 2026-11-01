import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion672 : pairCompletion (big 672)=full 672 := by
  have same : big 672=([{0,1,2,5},{1,3,4,6},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{1,3,4,6},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] [{0,3},{2,3},{0,4},{2,4},{0,1,2,5},{4,5},{0,6},{1,3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered672 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 672) T=TwentyFiveEightLow.Case672.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case672.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 672)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case672.support T pos))
  · decide +kernel
theorem completion673 : pairCompletion (big 673)=full 673 := by
  have same : big 673=([{0,1,3,6},{4,5,6},{2,4,7},{3,5,7},{1,2,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,6},{4,5,6},{2,4,7},{3,5,7},{1,2,5,8},{6,7,8}] [{0,2},{2,3},{0,4},{1,4},{3,4},{0,5},{2,6},{0,1,3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,8},{3,8},{4,8},{1,2,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered673 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 673) T=TwentyFiveEightLow.Case673.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case673.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 673)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case673.support T pos))
  · decide +kernel
theorem completion674 : pairCompletion (big 674)=full 674 := by
  have same : big 674=([{1,2,3,6},{4,5,6},{2,4,7},{3,5,7},{0,1,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3,6},{4,5,6},{2,4,7},{3,5,7},{0,1,5,8},{6,7,8}] [{0,2},{0,3},{0,4},{1,4},{3,4},{2,5},{0,6},{1,2,3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{2,8},{3,8},{4,8},{0,1,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered674 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 674) T=TwentyFiveEightLow.Case674.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case674.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 674)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case674.support T pos))
  · decide +kernel
theorem completion675 : pairCompletion (big 675)=full 675 := by
  have same : big 675=([{0,1,2,5},{4,5,6},{3,5,7},{2,6,7},{1,3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{4,5,6},{3,5,7},{2,6,7},{1,3,6,8},{4,7,8}] [{0,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,1,2,5},{0,6},{4,5,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,8},{2,8},{5,8},{1,3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered675 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 675) T=TwentyFiveEightLow.Case675.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case675.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 675)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case675.support T pos))
  · decide +kernel
theorem completion676 : pairCompletion (big 676)=full 676 := by
  have same : big 676=([{4,5,6},{1,4,7},{3,5,7},{2,6,7},{0,2,5,8},{1,3,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{4,5,6},{1,4,7},{3,5,7},{2,6,7},{0,2,5,8},{1,3,6,8}] [{0,1},{1,2},{0,3},{2,3},{0,4},{2,4},{3,4},{1,5},{0,6},{4,5,6},{0,7},{1,4,7},{3,5,7},{2,6,7},{4,8},{0,2,5,8},{1,3,6,8},{7,8}]=true
  decide +kernel

theorem recovered676 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 676) T=TwentyFiveEightLow.Case676.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case676.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 676)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case676.support T pos))
  · decide +kernel
theorem completion677 : pairCompletion (big 677)=full 677 := by
  have same : big 677=([{0,1,2,5},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{0,3,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{0,3,6,8}] [{1,3},{2,3},{0,4},{2,4},{3,4},{0,1,2,5},{1,6},{4,5,6},{0,7},{1,4,7},{3,5,7},{2,6,7},{1,8},{2,8},{4,8},{5,8},{0,3,6,8},{7,8}]=true
  decide +kernel

theorem recovered677 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 677) T=TwentyFiveEightLow.Case677.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case677.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 677)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case677.support T pos))
  · decide +kernel
theorem completion678 : pairCompletion (big 678)=full 678 := by
  have same : big 678=([{0,1,3,4},{2,3,5,6},{4,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{2,3,5,6},{4,5,7},{6,7,8}] [{0,2},{1,2},{2,4},{0,1,3,4},{0,5},{1,5},{0,6},{1,6},{4,6},{2,3,5,6},{0,7},{1,7},{2,7},{3,7},{4,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered678 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 678) T=TwentyFiveEightLow.Case678.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case678.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 678)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case678.support T pos))
  · decide +kernel
theorem completion679 : pairCompletion (big 679)=full 679 := by
  have same : big 679=([{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{2,3,8},{0,4,8},{1,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{2,3,8},{0,4,8},{1,5,8},{6,7,8}] [{0,1},{1,2},{0,3},{1,4},{3,4},{0,5},{2,5},{0,6},{1,6},{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{2,3,8},{0,4,8},{1,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered679 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 679) T=TwentyFiveEightLow.Case679.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case679.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 679)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case679.support T pos))
  · decide +kernel
theorem completion680 : pairCompletion (big 680)=full 680 := by
  have same : big 680=([{0,2,6},{1,3,6},{4,5,6},{2,3,7},{0,4,7},{1,5,7},{2,4,8},{3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,6},{1,3,6},{4,5,6},{2,3,7},{0,4,7},{1,5,7},{2,4,8},{3,5,8},{6,7,8}] [{0,1},{1,2},{0,3},{1,4},{3,4},{0,5},{2,5},{0,2,6},{1,3,6},{4,5,6},{2,3,7},{0,4,7},{1,5,7},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered680 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 680) T=TwentyFiveEightLow.Case680.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case680.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 680)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case680.support T pos))
  · decide +kernel
theorem completion681 : pairCompletion (big 681)=full 681 := by
  have same : big 681=([{2,3,5},{0,2,6},{1,4,6},{0,3,7},{2,4,7},{5,6,7},{4,5,8},{3,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{0,2,6},{1,4,6},{0,3,7},{2,4,7},{5,6,7},{4,5,8},{3,6,8},{1,7,8}] [{0,1},{1,2},{1,3},{0,4},{3,4},{0,5},{1,5},{2,3,5},{0,2,6},{1,4,6},{0,3,7},{2,4,7},{5,6,7},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered681 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 681) T=TwentyFiveEightLow.Case681.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case681.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 681)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case681.support T pos))
  · decide +kernel
theorem completion682 : pairCompletion (big 682)=full 682 := by
  have same : big 682=([{1,2,3},{3,4,5},{0,1,6},{2,4,6},{0,2,7},{1,5,7},{3,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3},{3,4,5},{0,1,6},{2,4,6},{0,2,7},{1,5,7},{3,6,7},{5,6,8},{4,7,8}] [{0,3},{1,2,3},{0,4},{1,4},{0,5},{2,5},{3,4,5},{0,1,6},{2,4,6},{0,2,7},{1,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered682 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 682) T=TwentyFiveEightLow.Case682.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case682.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 682)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case682.support T pos))
  · decide +kernel
theorem completion683 : pairCompletion (big 683)=full 683 := by
  have same : big 683=([{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{2,3,8},{1,4,8},{0,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{2,3,8},{1,4,8},{0,5,8},{6,7,8}] [{0,1},{1,2},{0,3},{0,4},{3,4},{1,5},{2,5},{0,6},{1,6},{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{2,3,8},{1,4,8},{0,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered683 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 683) T=TwentyFiveEightLow.Case683.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case683.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 683)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case683.support T pos))
  · decide +kernel
theorem completion684 : pairCompletion (big 684)=full 684 := by
  have same : big 684=([{0,2,6},{1,3,6},{4,5,6},{2,3,7},{0,4,7},{1,5,7},{3,4,8},{2,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,6},{1,3,6},{4,5,6},{2,3,7},{0,4,7},{1,5,7},{3,4,8},{2,5,8},{6,7,8}] [{0,1},{1,2},{0,3},{1,4},{2,4},{0,5},{3,5},{0,2,6},{1,3,6},{4,5,6},{2,3,7},{0,4,7},{1,5,7},{0,8},{1,8},{3,4,8},{2,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered684 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 684) T=TwentyFiveEightLow.Case684.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case684.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 684)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case684.support T pos))
  · decide +kernel
theorem completion685 : pairCompletion (big 685)=full 685 := by
  have same : big 685=([{2,3,5},{1,2,6},{0,4,6},{0,3,7},{2,4,7},{5,6,7},{4,5,8},{3,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{1,2,6},{0,4,6},{0,3,7},{2,4,7},{5,6,7},{4,5,8},{3,6,8},{1,7,8}] [{0,1},{0,2},{1,3},{1,4},{3,4},{0,5},{1,5},{2,3,5},{1,2,6},{0,4,6},{0,3,7},{2,4,7},{5,6,7},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered685 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 685) T=TwentyFiveEightLow.Case685.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case685.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 685)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case685.support T pos))
  · decide +kernel
theorem completion686 : pairCompletion (big 686)=full 686 := by
  have same : big 686=([{1,3,4},{2,3,5},{0,1,6},{2,4,6},{0,2,7},{1,5,7},{3,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4},{2,3,5},{0,1,6},{2,4,6},{0,2,7},{1,5,7},{3,6,7},{5,6,8},{4,7,8}] [{1,2},{0,3},{0,4},{1,3,4},{0,5},{2,3,5},{4,5},{0,1,6},{2,4,6},{0,2,7},{1,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered686 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 686) T=TwentyFiveEightLow.Case686.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case686.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 686)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case686.support T pos))
  · decide +kernel
theorem completion687 : pairCompletion (big 687)=full 687 := by
  have same : big 687=([{0,2,3,6},{1,4,5,6},{0,1,7},{2,4,8},{3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,6},{1,4,5,6},{0,1,7},{2,4,8},{3,5,8},{6,7,8}] [{1,2},{1,3},{0,4},{3,4},{0,5},{2,5},{0,2,3,6},{1,4,5,6},{0,1,7},{2,7},{3,7},{4,7},{5,7},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered687 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 687) T=TwentyFiveEightLow.Case687.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case687.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 687)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case687.support T pos))
  · decide +kernel
theorem completion688 : pairCompletion (big 688)=full 688 := by
  have same : big 688=([{0,1,4,6},{2,3,5,6},{0,2,7},{1,3,7},{4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,6},{2,3,5,6},{0,2,7},{1,3,7},{4,5,8},{6,7,8}] [{1,2},{0,3},{2,4},{3,4},{0,5},{1,5},{0,1,4,6},{2,3,5,6},{0,2,7},{1,3,7},{4,7},{5,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered688 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 688) T=TwentyFiveEightLow.Case688.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case688.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 688)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case688.support T pos))
  · decide +kernel
theorem completion689 : pairCompletion (big 689)=full 689 := by
  have same : big 689=([{0,1,6},{2,3,7},{4,5,7},{0,2,4,8},{1,3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{2,3,7},{4,5,7},{0,2,4,8},{1,3,5,8},{6,7,8}] [{1,2},{0,3},{1,4},{3,4},{0,5},{2,5},{0,1,6},{2,6},{3,6},{4,6},{5,6},{0,7},{1,7},{2,3,7},{4,5,7},{0,2,4,8},{1,3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered689 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 689) T=TwentyFiveEightLow.Case689.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case689.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 689)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case689.support T pos))
  · decide +kernel
theorem completion690 : pairCompletion (big 690)=full 690 := by
  have same : big 690=([{0,2,4,5},{0,1,6},{2,3,7},{5,6,7},{1,3,5,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4,5},{0,1,6},{2,3,7},{5,6,7},{1,3,5,8},{4,7,8}] [{1,2},{0,3},{1,4},{3,4},{0,2,4,5},{0,1,6},{2,6},{3,6},{4,6},{0,7},{1,7},{2,3,7},{5,6,7},{0,8},{2,8},{1,3,5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered690 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 690) T=TwentyFiveEightLow.Case690.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case690.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 690)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case690.support T pos))
  · decide +kernel
theorem completion691 : pairCompletion (big 691)=full 691 := by
  have same : big 691=([{0,1,4,5},{0,2,7},{1,3,7},{5,6,7},{2,3,5,8},{4,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{0,2,7},{1,3,7},{5,6,7},{2,3,5,8},{4,6,8}] [{1,2},{0,3},{2,4},{3,4},{0,1,4,5},{0,6},{1,6},{2,6},{3,6},{0,2,7},{1,3,7},{4,7},{5,6,7},{0,8},{1,8},{2,3,5,8},{4,6,8},{7,8}]=true
  decide +kernel

theorem recovered691 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 691) T=TwentyFiveEightLow.Case691.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case691.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 691)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case691.support T pos))
  · decide +kernel
theorem completion692 : pairCompletion (big 692)=full 692 := by
  have same : big 692=([{0,2,4,6},{1,3,5,6},{2,3,7},{4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4,6},{1,3,5,6},{2,3,7},{4,5,8},{6,7,8}] [{0,1},{1,2},{0,3},{1,4},{3,4},{0,5},{2,5},{0,2,4,6},{1,3,5,6},{0,7},{1,7},{2,3,7},{4,7},{5,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered692 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 692) T=TwentyFiveEightLow.Case692.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case692.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 692)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case692.support T pos))
  · decide +kernel
theorem completion693 : pairCompletion (big 693)=full 693 := by
  have same : big 693=([{2,3,6},{4,5,7},{0,2,4,8},{1,3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,6},{4,5,7},{0,2,4,8},{1,3,5,8},{6,7,8}] [{0,1},{1,2},{0,3},{1,4},{3,4},{0,5},{2,5},{0,6},{1,6},{2,3,6},{4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{4,5,7},{0,2,4,8},{1,3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered693 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 693) T=TwentyFiveEightLow.Case693.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case693.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 693)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case693.support T pos))
  · decide +kernel
theorem completion694 : pairCompletion (big 694)=full 694 := by
  have same : big 694=([{0,2,4,5},{2,3,6},{5,6,7},{1,3,5,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4,5},{2,3,6},{5,6,7},{1,3,5,8},{4,7,8}] [{0,1},{1,2},{0,3},{1,4},{3,4},{0,2,4,5},{0,6},{1,6},{2,3,6},{4,6},{0,7},{1,7},{2,7},{3,7},{5,6,7},{0,8},{2,8},{1,3,5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered694 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 694) T=TwentyFiveEightLow.Case694.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case694.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 694)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case694.support T pos))
  · decide +kernel
theorem completion695 : pairCompletion (big 695)=full 695 := by
  have same : big 695=([{0,1,2,5},{1,3,6},{2,4,7},{5,6,7},{3,4,5,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{1,3,6},{2,4,7},{5,6,7},{3,4,5,8}] [{0,3},{2,3},{0,4},{1,4},{0,1,2,5},{0,6},{2,6},{1,3,6},{4,6},{0,7},{1,7},{3,7},{2,4,7},{5,6,7},{0,8},{1,8},{2,8},{3,4,5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered695 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 695) T=TwentyFiveEightLow.Case695.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case695.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 695)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case695.support T pos))
  · decide +kernel
theorem completion696 : pairCompletion (big 696)=full 696 := by
  have same : big 696=([{0,1,2,5},{1,3,6},{4,5,6},{3,5,7},{2,6,7},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{1,3,6},{4,5,6},{3,5,7},{2,6,7},{4,7,8}] [{0,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,1,2,5},{0,6},{1,3,6},{4,5,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered696 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 696) T=TwentyFiveEightLow.Case696.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case696.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 696)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case696.support T pos))
  · decide +kernel
theorem completion697 : pairCompletion (big 697)=full 697 := by
  have same : big 697=([{0,1,2,5},{1,3,6},{4,5,6},{2,4,7},{3,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{1,3,6},{4,5,6},{2,4,7},{3,5,7},{6,7,8}] [{0,3},{2,3},{0,4},{1,4},{3,4},{0,1,2,5},{0,6},{2,6},{1,3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered697 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 697) T=TwentyFiveEightLow.Case697.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case697.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 697)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case697.support T pos))
  · decide +kernel
theorem completion698 : pairCompletion (big 698)=full 698 := by
  have same : big 698=([{0,1,2,5},{1,3,6},{4,5,6},{3,4,7},{2,6,7},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{1,3,6},{4,5,6},{3,4,7},{2,6,7},{5,7,8}] [{0,3},{2,3},{0,4},{1,4},{2,4},{0,1,2,5},{3,5},{0,6},{1,3,6},{4,5,6},{0,7},{1,7},{3,4,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered698 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 698) T=TwentyFiveEightLow.Case698.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case698.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 698)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case698.support T pos))
  · decide +kernel
theorem completion699 : pairCompletion (big 699)=full 699 := by
  have same : big 699=([{0,1,2,3,6},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,6},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] [{0,4},{2,4},{3,4},{0,5},{1,5},{3,5},{4,5},{0,1,2,3,6},{0,7},{2,7},{1,4,7},{5,6,7},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered699 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 699) T=TwentyFiveEightLow.Case699.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case699.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 699)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case699.support T pos))
  · decide +kernel
theorem completion700 : pairCompletion (big 700)=full 700 := by
  have same : big 700=([{1,4,6},{2,5,7},{3,6,7},{0,1,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,6},{2,5,7},{3,6,7},{0,1,2,3,8},{5,6,8},{4,7,8}] [{0,4},{2,4},{3,4},{0,5},{1,5},{3,5},{4,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,1,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered700 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 700) T=TwentyFiveEightLow.Case700.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case700.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 700)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case700.support T pos))
  · decide +kernel
theorem completion701 : pairCompletion (big 701)=full 701 := by
  have same : big 701=([{0,1,2,3,5},{1,4,6},{4,5,7},{2,6,7},{5,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,5},{1,4,6},{4,5,7},{2,6,7},{5,6,8},{3,7,8}] [{0,4},{2,4},{3,4},{0,1,2,3,5},{0,6},{3,6},{1,4,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,8},{1,8},{2,8},{4,8},{5,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered701 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 701) T=TwentyFiveEightLow.Case701.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case701.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 701)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case701.support T pos))
  · decide +kernel
theorem completion702 : pairCompletion (big 702)=full 702 := by
  have same : big 702=([{1,3,6},{4,5,6},{2,4,7},{3,5,7},{0,1,2,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,6},{4,5,6},{2,4,7},{3,5,7},{0,1,2,5,8},{6,7,8}] [{0,3},{2,3},{0,4},{1,4},{3,4},{0,6},{2,6},{1,3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{3,8},{4,8},{0,1,2,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered702 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 702) T=TwentyFiveEightLow.Case702.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case702.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 702)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case702.support T pos))
  · decide +kernel
theorem completion703 : pairCompletion (big 703)=full 703 := by
  have same : big 703=([{1,3,6},{4,5,6},{3,5,7},{2,6,7},{0,1,2,5,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,6},{4,5,6},{3,5,7},{2,6,7},{0,1,2,5,8},{4,7,8}] [{0,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,6},{1,3,6},{4,5,6},{0,7},{1,7},{3,5,7},{2,6,7},{3,8},{0,1,2,5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered703 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 703) T=TwentyFiveEightLow.Case703.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case703.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 703)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case703.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
