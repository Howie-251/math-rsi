import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion640 : pairCompletion (big 640)=full 640 := by
  have same : big 640=([{3,4,5},{0,1,6},{2,5,6},{0,2,7},{1,5,7},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,1,6},{2,5,6},{0,2,7},{1,5,7},{3,6,8},{4,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{3,4,5},{0,1,6},{4,6},{2,5,6},{0,2,7},{3,7},{1,5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered640 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 640) T=TwentyFiveEightLow.Case640.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case640.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 640)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case640.support T pos))
  · decide +kernel
theorem completion641 : pairCompletion (big 641)=full 641 := by
  have same : big 641=([{0,2,6},{1,4,6},{1,3,7},{0,5,7},{2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,6},{1,4,6},{1,3,7},{0,5,7},{2,3,8},{5,6,8},{4,7,8}] [{0,1},{1,2},{0,3},{0,4},{2,4},{3,4},{1,5},{2,5},{3,5},{4,5},{0,2,6},{3,6},{1,4,6},{2,7},{1,3,7},{0,5,7},{6,7},{0,8},{1,8},{2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered641 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 641) T=TwentyFiveEightLow.Case641.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case641.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 641)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case641.support T pos))
  · decide +kernel
theorem completion642 : pairCompletion (big 642)=full 642 := by
  have same : big 642=([{0,1,6},{3,4,6},{0,2,7},{5,6,7},{2,3,8},{1,5,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{3,4,6},{0,2,7},{5,6,7},{2,3,8},{1,5,8},{4,7,8}] [{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{0,5},{2,5},{3,5},{4,5},{0,1,6},{2,6},{3,4,6},{1,7},{0,2,7},{3,7},{5,6,7},{0,8},{2,3,8},{1,5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered642 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 642) T=TwentyFiveEightLow.Case642.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case642.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 642)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case642.support T pos))
  · decide +kernel
theorem completion643 : pairCompletion (big 643)=full 643 := by
  have same : big 643=([{1,3,5},{2,4,5},{0,1,6},{0,2,7},{3,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,5},{2,4,5},{0,1,6},{0,2,7},{3,6,7},{4,6,8},{5,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,3,5},{2,4,5},{0,1,6},{2,6},{5,6},{1,7},{0,2,7},{4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered643 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 643) T=TwentyFiveEightLow.Case643.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case643.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 643)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case643.support T pos))
  · decide +kernel
theorem completion644 : pairCompletion (big 644)=full 644 := by
  have same : big 644=([{1,3,5},{0,1,6},{2,5,6},{0,2,7},{4,5,7},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,5},{0,1,6},{2,5,6},{0,2,7},{4,5,7},{4,6,8},{3,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,5},{1,3,5},{0,1,6},{3,6},{2,5,6},{1,7},{0,2,7},{4,5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered644 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 644) T=TwentyFiveEightLow.Case644.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case644.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 644)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case644.support T pos))
  · decide +kernel
theorem completion645 : pairCompletion (big 645)=full 645 := by
  have same : big 645=([{0,3,5},{2,4,5},{0,1,6},{1,5,7},{2,6,7},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,5},{2,4,5},{0,1,6},{1,5,7},{2,6,7},{4,6,8},{3,7,8}] [{0,2},{1,2},{1,3},{2,3},{0,4},{1,4},{3,4},{0,3,5},{2,4,5},{0,1,6},{3,6},{5,6},{0,7},{4,7},{1,5,7},{2,6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered645 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 645) T=TwentyFiveEightLow.Case645.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case645.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 645)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case645.support T pos))
  · decide +kernel
theorem completion646 : pairCompletion (big 646)=full 646 := by
  have same : big 646=([{0,1,2,6},{3,4,7},{5,6,7},{3,5,8},{4,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,6},{3,4,7},{5,6,7},{3,5,8},{4,6,8},{2,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{4,5},{0,1,2,6},{3,6},{0,7},{1,7},{3,4,7},{5,6,7},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered646 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 646) T=TwentyFiveEightLow.Case646.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case646.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 646)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case646.support T pos))
  · decide +kernel
theorem completion647 : pairCompletion (big 647)=full 647 := by
  have same : big 647=([{3,4,6},{3,5,7},{2,6,7},{0,1,2,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,6},{3,5,7},{2,6,7},{0,1,2,8},{5,6,8},{4,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,1,2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered647 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 647) T=TwentyFiveEightLow.Case647.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case647.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 647)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case647.support T pos))
  · decide +kernel
theorem completion648 : pairCompletion (big 648)=full 648 := by
  have same : big 648=([{0,1,2,5},{3,4,6},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{3,4,6},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,1,2,5},{4,5},{0,6},{1,6},{3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered648 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 648) T=TwentyFiveEightLow.Case648.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case648.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 648)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case648.support T pos))
  · decide +kernel
theorem completion649 : pairCompletion (big 649)=full 649 := by
  have same : big 649=([{0,1,2,5},{3,5,6},{4,5,7},{2,6,7},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{3,5,6},{4,5,7},{2,6,7},{4,6,8},{3,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,1,2,5},{0,6},{1,6},{3,5,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered649 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 649) T=TwentyFiveEightLow.Case649.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case649.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 649)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case649.support T pos))
  · decide +kernel
theorem completion650 : pairCompletion (big 650)=full 650 := by
  have same : big 650=([{2,3,6},{4,5,6},{2,4,7},{3,5,7},{0,1,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,6},{4,5,6},{2,4,7},{3,5,7},{0,1,5,8},{6,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{3,4},{2,5},{0,6},{1,6},{2,3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{2,8},{3,8},{4,8},{0,1,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered650 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 650) T=TwentyFiveEightLow.Case650.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case650.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 650)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case650.support T pos))
  · decide +kernel
theorem completion651 : pairCompletion (big 651)=full 651 := by
  have same : big 651=([{2,3,6},{4,5,6},{2,4,7},{3,5,7},{1,6,7},{0,1,5,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,6},{4,5,6},{2,4,7},{3,5,7},{1,6,7},{0,1,5,8}] [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{3,4},{2,5},{0,6},{2,3,6},{4,5,6},{0,7},{2,4,7},{3,5,7},{1,6,7},{2,8},{3,8},{4,8},{0,1,5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered651 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 651) T=TwentyFiveEightLow.Case651.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case651.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 651)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case651.support T pos))
  · decide +kernel
theorem completion652 : pairCompletion (big 652)=full 652 := by
  have same : big 652=([{0,1,2,6},{3,5,7},{4,6,7},{0,3,8},{1,4,8},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,6},{3,5,7},{4,6,7},{0,3,8},{1,4,8},{5,6,8},{2,7,8}] [{1,3},{2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,1,2,6},{3,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,3,8},{1,4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered652 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 652) T=TwentyFiveEightLow.Case652.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case652.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 652)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case652.support T pos))
  · decide +kernel
theorem completion653 : pairCompletion (big 653)=full 653 := by
  have same : big 653=([{0,1,2,6},{0,3,7},{1,4,7},{5,6,7},{3,5,8},{4,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,6},{0,3,7},{1,4,7},{5,6,7},{3,5,8},{4,6,8},{2,7,8}] [{1,3},{2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,1,2,6},{3,6},{0,3,7},{1,4,7},{5,6,7},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered653 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 653) T=TwentyFiveEightLow.Case653.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case653.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 653)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case653.support T pos))
  · decide +kernel
theorem completion654 : pairCompletion (big 654)=full 654 := by
  have same : big 654=([{3,5,6},{0,3,7},{1,4,7},{2,6,7},{0,1,2,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,5,6},{0,3,7},{1,4,7},{2,6,7},{0,1,2,8},{4,6,8},{5,7,8}] [{1,3},{2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{3,5,6},{0,3,7},{1,4,7},{2,6,7},{0,1,2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered654 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 654) T=TwentyFiveEightLow.Case654.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case654.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 654)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case654.support T pos))
  · decide +kernel
theorem completion655 : pairCompletion (big 655)=full 655 := by
  have same : big 655=([{0,1,2,5},{3,5,6},{0,3,7},{1,4,7},{2,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{3,5,6},{0,3,7},{1,4,7},{2,6,7},{4,6,8},{5,7,8}] [{1,3},{2,3},{0,4},{2,4},{3,4},{0,1,2,5},{4,5},{0,6},{1,6},{3,5,6},{0,3,7},{1,4,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered655 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 655) T=TwentyFiveEightLow.Case655.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case655.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 655)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case655.support T pos))
  · decide +kernel
theorem completion656 : pairCompletion (big 656)=full 656 := by
  have same : big 656=([{0,1,2,5},{3,4,6},{0,3,7},{4,5,7},{1,6,7},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{3,4,6},{0,3,7},{4,5,7},{1,6,7},{5,6,8},{2,7,8}] [{1,3},{2,3},{0,4},{1,4},{2,4},{0,1,2,5},{3,5},{0,6},{2,6},{3,4,6},{0,3,7},{4,5,7},{1,6,7},{0,8},{1,8},{3,8},{4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered656 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 656) T=TwentyFiveEightLow.Case656.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case656.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 656)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case656.support T pos))
  · decide +kernel
theorem completion657 : pairCompletion (big 657)=full 657 := by
  have same : big 657=([{0,1,2,5},{3,5,6},{0,3,7},{4,5,7},{1,6,7},{4,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{3,5,6},{0,3,7},{4,5,7},{1,6,7},{4,6,8},{2,7,8}] [{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,1,2,5},{0,6},{2,6},{3,5,6},{0,3,7},{4,5,7},{1,6,7},{0,8},{1,8},{3,8},{5,8},{4,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered657 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 657) T=TwentyFiveEightLow.Case657.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case657.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 657)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case657.support T pos))
  · decide +kernel
theorem completion658 : pairCompletion (big 658)=full 658 := by
  have same : big 658=([{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{0,1,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{0,1,5,8},{6,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{2,5},{0,6},{1,6},{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{2,8},{3,8},{4,8},{0,1,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered658 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 658) T=TwentyFiveEightLow.Case658.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case658.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 658)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case658.support T pos))
  · decide +kernel
theorem completion659 : pairCompletion (big 659)=full 659 := by
  have same : big 659=([{2,3,6},{4,5,6},{0,2,7},{3,5,7},{1,6,7},{0,1,5,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,6},{4,5,6},{0,2,7},{3,5,7},{1,6,7},{0,1,5,8},{4,7,8}] [{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{2,5},{0,6},{2,3,6},{4,5,6},{0,2,7},{3,5,7},{1,6,7},{2,8},{3,8},{0,1,5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered659 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 659) T=TwentyFiveEightLow.Case659.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case659.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 659)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case659.support T pos))
  · decide +kernel
theorem completion660 : pairCompletion (big 660)=full 660 := by
  have same : big 660=([{3,4,6},{2,5,6},{0,2,7},{3,5,7},{1,6,7},{0,1,5,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,6},{2,5,6},{0,2,7},{3,5,7},{1,6,7},{0,1,5,8},{4,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{4,5},{0,6},{3,4,6},{2,5,6},{0,2,7},{3,5,7},{1,6,7},{2,8},{3,8},{0,1,5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered660 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 660) T=TwentyFiveEightLow.Case660.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case660.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 660)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case660.support T pos))
  · decide +kernel
theorem completion661 : pairCompletion (big 661)=full 661 := by
  have same : big 661=([{0,3,6},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{3,4,8},{2,5,8},{1,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,6},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{3,4,8},{2,5,8},{1,6,8},{0,7,8}] [{0,1},{0,2},{1,2},{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{0,3,6},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{3,4,8},{2,5,8},{1,6,8},{0,7,8}]=true
  decide +kernel

theorem recovered661 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 661) T=TwentyFiveEightLow.Case661.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case661.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 661)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case661.support T pos))
  · decide +kernel
theorem completion662 : pairCompletion (big 662)=full 662 := by
  have same : big 662=([{0,3,5},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,5},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,1},{0,2},{1,2},{1,3},{2,3},{0,4},{2,4},{0,3,5},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered662 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 662) T=TwentyFiveEightLow.Case662.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case662.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 662)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case662.support T pos))
  · decide +kernel
theorem completion663 : pairCompletion (big 663)=full 663 := by
  have same : big 663=([{0,2,5},{3,4,5},{1,3,6},{2,4,6},{2,3,7},{1,5,7},{0,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,5},{3,4,5},{1,3,6},{2,4,6},{2,3,7},{1,5,7},{0,6,7},{5,6,8},{4,7,8}] [{0,1},{1,2},{0,3},{0,4},{1,4},{0,2,5},{3,4,5},{1,3,6},{2,4,6},{2,3,7},{1,5,7},{0,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered663 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 663) T=TwentyFiveEightLow.Case663.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case663.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 663)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case663.support T pos))
  · decide +kernel
theorem completion664 : pairCompletion (big 664)=full 664 := by
  have same : big 664=([{0,1,5},{2,3,6},{4,5,6},{0,4,7},{2,5,7},{1,6,7},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{2,3,6},{4,5,6},{0,4,7},{2,5,7},{1,6,7},{3,7,8}] [{0,2},{1,2},{0,3},{1,3},{1,4},{2,4},{3,4},{0,1,5},{3,5},{0,6},{2,3,6},{4,5,6},{0,4,7},{2,5,7},{1,6,7},{0,8},{1,8},{2,8},{4,8},{5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered664 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 664) T=TwentyFiveEightLow.Case664.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case664.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 664)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case664.support T pos))
  · decide +kernel
theorem completion665 : pairCompletion (big 665)=full 665 := by
  have same : big 665=([{2,3,5},{0,1,5,6},{1,2,7},{4,5,7},{3,6,7},{4,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{0,1,5,6},{1,2,7},{4,5,7},{3,6,7},{4,6,8}] [{0,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{2,3,5},{2,6},{0,1,5,6},{0,7},{1,2,7},{4,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{5,8},{4,6,8},{7,8}]=true
  decide +kernel

theorem recovered665 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 665) T=TwentyFiveEightLow.Case665.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case665.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 665)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case665.support T pos))
  · decide +kernel
theorem completion666 : pairCompletion (big 666)=full 666 := by
  have same : big 666=([{0,1,4,6},{0,2,5,7},{3,6,7},{1,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,6},{0,2,5,7},{3,6,7},{1,2,3,8},{5,6,8},{4,7,8}] [{0,3},{2,4},{3,4},{1,5},{3,5},{4,5},{2,6},{0,1,4,6},{1,7},{0,2,5,7},{3,6,7},{0,8},{1,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered666 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 666) T=TwentyFiveEightLow.Case666.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case666.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 666)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case666.support T pos))
  · decide +kernel
theorem completion667 : pairCompletion (big 667)=full 667 := by
  have same : big 667=([{0,1,3,6},{4,5,6},{0,2,4,7},{3,5,7},{1,2,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,6},{4,5,6},{0,2,4,7},{3,5,7},{1,2,5,8},{6,7,8}] [{2,3},{1,4},{3,4},{0,5},{2,6},{0,1,3,6},{4,5,6},{1,7},{0,2,4,7},{3,5,7},{0,8},{3,8},{4,8},{1,2,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered667 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 667) T=TwentyFiveEightLow.Case667.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case667.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 667)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case667.support T pos))
  · decide +kernel
theorem completion668 : pairCompletion (big 668)=full 668 := by
  have same : big 668=([{0,1,2,5},{3,5,6},{4,5,7},{2,6,7},{0,4,6,8},{1,3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{3,5,6},{4,5,7},{2,6,7},{0,4,6,8},{1,3,7,8}] [{0,3},{2,3},{1,4},{2,4},{3,4},{0,1,2,5},{1,6},{3,5,6},{0,7},{4,5,7},{2,6,7},{2,8},{5,8},{0,4,6,8},{1,3,7,8}]=true
  decide +kernel

theorem recovered668 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 668) T=TwentyFiveEightLow.Case668.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case668.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 668)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case668.support T pos))
  · decide +kernel
theorem completion669 : pairCompletion (big 669)=full 669 := by
  have same : big 669=([{0,1,3,6},{1,2,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,6},{1,2,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] [{0,2},{2,3},{0,4},{3,4},{0,5},{1,5},{3,5},{4,5},{2,6},{0,1,3,6},{0,7},{1,2,4,7},{5,6,7},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered669 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 669) T=TwentyFiveEightLow.Case669.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case669.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 669)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case669.support T pos))
  · decide +kernel
theorem completion670 : pairCompletion (big 670)=full 670 := by
  have same : big 670=([{0,1,4,6},{2,5,7},{3,6,7},{1,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,6},{2,5,7},{3,6,7},{1,2,3,8},{5,6,8},{4,7,8}] [{0,2},{0,3},{2,4},{3,4},{0,5},{1,5},{3,5},{4,5},{2,6},{0,1,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,8},{1,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered670 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 670) T=TwentyFiveEightLow.Case670.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case670.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 670)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case670.support T pos))
  · decide +kernel
theorem completion671 : pairCompletion (big 671)=full 671 := by
  have same : big 671=([{1,2,4,6},{2,5,7},{3,6,7},{0,1,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,4,6},{2,5,7},{3,6,7},{0,1,3,8},{5,6,8},{4,7,8}] [{0,2},{2,3},{0,4},{3,4},{0,5},{1,5},{3,5},{4,5},{0,6},{1,2,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{2,8},{0,1,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered671 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 671) T=TwentyFiveEightLow.Case671.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case671.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 671)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case671.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
