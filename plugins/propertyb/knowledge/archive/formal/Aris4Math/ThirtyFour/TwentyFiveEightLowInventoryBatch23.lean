import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion736 : pairCompletion (big 736)=full 736 := by
  have same : big 736=([{2,4,5},{0,1,5,6},{1,2,3,7},{4,6,7},{3,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{0,1,5,6},{1,2,3,7},{4,6,7},{3,6,8},{5,7,8}] [{0,2},{0,3},{0,4},{1,4},{3,4},{3,5},{2,4,5},{2,6},{0,1,5,6},{0,7},{1,2,3,7},{4,6,7},{0,8},{1,8},{2,8},{4,8},{3,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered736 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 736) T=TwentyFiveEightLow.Case736.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case736.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 736)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case736.support T pos))
  · decide +kernel
theorem completion737 : pairCompletion (big 737)=full 737 := by
  have same : big 737=([{2,3,5},{4,5,6},{0,1,5,7},{3,6,7},{1,2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{4,5,6},{0,1,5,7},{3,6,7},{1,2,6,8},{4,7,8}] [{0,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{2,3,5},{0,6},{4,5,6},{2,7},{0,1,5,7},{3,6,7},{0,8},{3,8},{5,8},{1,2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered737 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 737) T=TwentyFiveEightLow.Case737.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case737.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 737)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case737.support T pos))
  · decide +kernel
theorem completion738 : pairCompletion (big 738)=full 738 := by
  have same : big 738=([{1,3,5},{2,4,6},{4,5,7},{3,6,7},{0,5,6,8},{1,2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,5},{2,4,6},{4,5,7},{3,6,7},{0,5,6,8},{1,2,7,8}] [{0,1},{0,2},{0,3},{2,3},{0,4},{1,4},{3,4},{2,5},{1,3,5},{1,6},{2,4,6},{0,7},{4,5,7},{3,6,7},{3,8},{4,8},{0,5,6,8},{1,2,7,8}]=true
  decide +kernel

theorem recovered738 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 738) T=TwentyFiveEightLow.Case738.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case738.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 738)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case738.support T pos))
  · decide +kernel
theorem completion739 : pairCompletion (big 739)=full 739 := by
  have same : big 739=([{1,3,5},{2,4,6},{0,1,2,7},{4,5,7},{3,6,7},{0,5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,5},{2,4,6},{0,1,2,7},{4,5,7},{3,6,7},{0,5,6,8}] [{0,3},{2,3},{0,4},{1,4},{3,4},{2,5},{1,3,5},{1,6},{2,4,6},{0,1,2,7},{4,5,7},{3,6,7},{1,8},{2,8},{3,8},{4,8},{0,5,6,8},{7,8}]=true
  decide +kernel

theorem recovered739 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 739) T=TwentyFiveEightLow.Case739.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case739.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 739)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case739.support T pos))
  · decide +kernel
theorem completion740 : pairCompletion (big 740)=full 740 := by
  have same : big 740=([{0,2,4,6},{1,3,4,7},{5,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4,6},{1,3,4,7},{5,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}] [{1,2},{0,3},{2,3},{0,5},{1,5},{2,5},{3,5},{1,6},{0,2,4,6},{0,7},{1,3,4,7},{5,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered740 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 740) T=TwentyFiveEightLow.Case740.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case740.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 740)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case740.support T pos))
  · decide +kernel
theorem completion741 : pairCompletion (big 741)=full 741 := by
  have same : big 741=([{0,3,4,6},{0,1,7},{4,5,7},{2,6,7},{1,2,4,8},{5,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,6},{0,1,7},{4,5,7},{2,6,7},{1,2,4,8},{5,6,8},{3,7,8}] [{0,2},{1,3},{2,3},{0,5},{1,5},{2,5},{3,5},{1,6},{0,3,4,6},{0,1,7},{4,5,7},{2,6,7},{0,8},{1,2,4,8},{5,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered741 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 741) T=TwentyFiveEightLow.Case741.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case741.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 741)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case741.support T pos))
  · decide +kernel
theorem completion742 : pairCompletion (big 742)=full 742 := by
  have same : big 742=([{0,2,4,5},{1,3,4,6},{0,1,7},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4,5},{1,3,4,6},{0,1,7},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] [{1,2},{0,3},{2,3},{1,5},{0,2,4,5},{0,6},{1,3,4,6},{0,1,7},{3,5,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered742 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 742) T=TwentyFiveEightLow.Case742.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case742.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 742)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case742.support T pos))
  · decide +kernel
theorem completion743 : pairCompletion (big 743)=full 743 := by
  have same : big 743=([{4,5,6},{0,1,7},{2,5,7},{3,6,7},{0,3,5,8},{1,2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{4,5,6},{0,1,7},{2,5,7},{3,6,7},{0,3,5,8},{1,2,6,8},{4,7,8}] [{0,2},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{1,5},{0,6},{4,5,6},{0,1,7},{2,5,7},{3,6,7},{0,3,5,8},{1,2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered743 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 743) T=TwentyFiveEightLow.Case743.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case743.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 743)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case743.support T pos))
  · decide +kernel
theorem completion744 : pairCompletion (big 744)=full 744 := by
  have same : big 744=([{0,2,3,6},{4,5,6},{0,1,7},{3,4,7},{2,5,7},{1,3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,6},{4,5,6},{0,1,7},{3,4,7},{2,5,7},{1,3,5,8},{6,7,8}] [{1,2},{0,4},{1,4},{2,4},{0,5},{1,6},{0,2,3,6},{4,5,6},{0,1,7},{3,4,7},{2,5,7},{0,8},{2,8},{4,8},{1,3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered744 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 744) T=TwentyFiveEightLow.Case744.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case744.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 744)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case744.support T pos))
  · decide +kernel
theorem completion745 : pairCompletion (big 745)=full 745 := by
  have same : big 745=([{0,2,3,5},{4,5,6},{3,4,7},{1,5,7},{0,6,7},{1,3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,5},{4,5,6},{3,4,7},{1,5,7},{0,6,7},{1,3,6,8},{2,7,8}] [{0,1},{1,2},{0,4},{1,4},{2,4},{0,2,3,5},{2,6},{4,5,6},{3,4,7},{1,5,7},{0,6,7},{0,8},{4,8},{5,8},{1,3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered745 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 745) T=TwentyFiveEightLow.Case745.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case745.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 745)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case745.support T pos))
  · decide +kernel
theorem completion746 : pairCompletion (big 746)=full 746 := by
  have same : big 746=([{0,2,4,6},{1,3,4,7},{5,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4,6},{1,3,4,7},{5,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,1},{1,2},{0,3},{2,3},{0,5},{1,5},{2,5},{3,5},{1,6},{0,2,4,6},{0,7},{1,3,4,7},{5,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered746 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 746) T=TwentyFiveEightLow.Case746.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case746.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 746)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case746.support T pos))
  · decide +kernel
theorem completion747 : pairCompletion (big 747)=full 747 := by
  have same : big 747=([{0,3,4,6},{4,5,7},{2,6,7},{1,2,4,8},{5,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,6},{4,5,7},{2,6,7},{1,2,4,8},{5,6,8},{3,7,8}] [{0,1},{0,2},{1,3},{2,3},{0,5},{1,5},{2,5},{3,5},{1,6},{0,3,4,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,8},{1,2,4,8},{5,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered747 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 747) T=TwentyFiveEightLow.Case747.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case747.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 747)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case747.support T pos))
  · decide +kernel
theorem completion748 : pairCompletion (big 748)=full 748 := by
  have same : big 748=([{0,2,4,5},{1,3,4,6},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4,5},{1,3,4,6},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] [{0,1},{1,2},{0,3},{2,3},{1,5},{0,2,4,5},{0,6},{1,3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered748 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 748) T=TwentyFiveEightLow.Case748.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case748.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 748)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case748.support T pos))
  · decide +kernel
theorem completion749 : pairCompletion (big 749)=full 749 := by
  have same : big 749=([{4,5,6},{2,5,7},{3,6,7},{0,3,5,8},{1,2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{4,5,6},{2,5,7},{3,6,7},{0,3,5,8},{1,2,6,8},{4,7,8}] [{0,1},{0,2},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{1,5},{0,6},{4,5,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,3,5,8},{1,2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered749 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 749) T=TwentyFiveEightLow.Case749.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case749.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 749)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case749.support T pos))
  · decide +kernel
theorem completion750 : pairCompletion (big 750)=full 750 := by
  have same : big 750=([{0,2,3,6},{4,5,6},{3,4,7},{2,5,7},{1,3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,6},{4,5,6},{3,4,7},{2,5,7},{1,3,5,8},{6,7,8}] [{0,1},{1,2},{0,4},{1,4},{2,4},{0,5},{1,6},{0,2,3,6},{4,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{0,8},{2,8},{4,8},{1,3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered750 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 750) T=TwentyFiveEightLow.Case750.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case750.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 750)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case750.support T pos))
  · decide +kernel
theorem completion751 : pairCompletion (big 751)=full 751 := by
  have same : big 751=([{0,1,3,5},{4,5,6},{3,4,7},{2,5,7},{1,6,7},{2,3,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,5},{4,5,6},{3,4,7},{2,5,7},{1,6,7},{2,3,6,8}] [{0,2},{1,2},{0,4},{1,4},{2,4},{0,1,3,5},{0,6},{4,5,6},{0,7},{3,4,7},{2,5,7},{1,6,7},{0,8},{1,8},{4,8},{5,8},{2,3,6,8},{7,8}]=true
  decide +kernel

theorem recovered751 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 751) T=TwentyFiveEightLow.Case751.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case751.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 751)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case751.support T pos))
  · decide +kernel
theorem completion752 : pairCompletion (big 752)=full 752 := by
  have same : big 752=([{0,1,3,5},{0,2,4,6},{1,2,7},{4,5,7},{3,6,7},{5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,5},{0,2,4,6},{1,2,7},{4,5,7},{3,6,7},{5,6,8}] [{2,3},{1,4},{3,4},{2,5},{0,1,3,5},{1,6},{0,2,4,6},{0,7},{1,2,7},{4,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,6,8},{7,8}]=true
  decide +kernel

theorem recovered752 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 752) T=TwentyFiveEightLow.Case752.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case752.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 752)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case752.support T pos))
  · decide +kernel
theorem completion753 : pairCompletion (big 753)=full 753 := by
  have same : big 753=([{0,1,5},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{6,7,8}] [{1,2},{0,3},{1,3},{0,4},{2,4},{3,4},{0,1,5},{2,5},{0,6},{1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered753 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 753) T=TwentyFiveEightLow.Case753.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case753.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 753)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case753.support T pos))
  · decide +kernel
theorem completion754 : pairCompletion (big 754)=full 754 := by
  have same : big 754=([{2,3,5},{2,4,6},{0,1,5,6},{4,5,7},{3,6,7},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{2,4,6},{0,1,5,6},{4,5,7},{3,6,7},{1,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{3,4},{2,3,5},{2,4,6},{0,1,5,6},{0,7},{2,7},{4,5,7},{3,6,7},{0,8},{2,8},{3,8},{4,8},{5,8},{6,8},{1,7,8}]=true
  decide +kernel

theorem recovered754 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 754) T=TwentyFiveEightLow.Case754.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case754.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 754)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case754.support T pos))
  · decide +kernel
theorem completion755 : pairCompletion (big 755)=full 755 := by
  have same : big 755=([{0,3,4,6},{1,3,5,7},{2,4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,6},{1,3,5,7},{2,4,5,8},{6,7,8}] [{0,1},{0,2},{1,2},{2,3},{1,4},{0,5},{1,6},{2,6},{0,3,4,6},{5,6},{0,7},{2,7},{4,7},{1,3,5,7},{0,8},{1,8},{3,8},{2,4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered755 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 755) T=TwentyFiveEightLow.Case755.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case755.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 755)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case755.support T pos))
  · decide +kernel
theorem completion756 : pairCompletion (big 756)=full 756 := by
  have same : big 756=([{0,3,4,5},{5,6,7},{1,3,6,8},{2,4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,5},{5,6,7},{1,3,6,8},{2,4,7,8}] [{0,1},{0,2},{1,2},{2,3},{1,4},{1,5},{2,5},{0,3,4,5},{0,6},{2,6},{4,6},{0,7},{1,7},{3,7},{5,6,7},{0,8},{5,8},{1,3,6,8},{2,4,7,8}]=true
  decide +kernel

theorem recovered756 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 756) T=TwentyFiveEightLow.Case756.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case756.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 756)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case756.support T pos))
  · decide +kernel
theorem completion757 : pairCompletion (big 757)=full 757 := by
  have same : big 757=([{0,2,3,5},{1,2,4,6},{5,6,7},{3,4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,5},{1,2,4,6},{5,6,7},{3,4,7,8}] [{0,1},{1,3},{0,4},{1,5},{0,2,3,5},{4,5},{0,6},{3,6},{1,2,4,6},{0,7},{1,7},{2,7},{5,6,7},{0,8},{1,8},{2,8},{5,8},{6,8},{3,4,7,8}]=true
  decide +kernel

theorem recovered757 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 757) T=TwentyFiveEightLow.Case757.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case757.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 757)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case757.support T pos))
  · decide +kernel
theorem completion758 : pairCompletion (big 758)=full 758 := by
  have same : big 758=([{0,1,4},{0,2,5},{2,4,6},{3,5,6},{3,4,7},{1,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{0,2,5},{2,4,6},{3,5,6},{3,4,7},{1,5,7},{6,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,1,4},{0,2,5},{4,5},{0,6},{1,6},{2,4,6},{3,5,6},{0,7},{2,7},{3,4,7},{1,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered758 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 758) T=TwentyFiveEightLow.Case758.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case758.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 758)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case758.support T pos))
  · decide +kernel
theorem completion759 : pairCompletion (big 759)=full 759 := by
  have same : big 759=([{0,1,4},{2,3,5},{2,4,6},{0,5,6},{3,4,7},{1,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{2,3,5},{2,4,6},{0,5,6},{3,4,7},{1,5,7},{6,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,1,4},{2,3,5},{4,5},{1,6},{3,6},{2,4,6},{0,5,6},{0,7},{2,7},{3,4,7},{1,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered759 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 759) T=TwentyFiveEightLow.Case759.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case759.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 759)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case759.support T pos))
  · decide +kernel
theorem completion760 : pairCompletion (big 760)=full 760 := by
  have same : big 760=([{0,3,4},{0,1,2,6},{1,3,7},{2,5,7},{4,6,7},{5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{0,1,2,6},{1,3,7},{2,5,7},{4,6,7},{5,6,8}] [{2,3},{1,4},{2,4},{0,3,4},{0,5},{1,5},{3,5},{4,5},{0,1,2,6},{3,6},{0,7},{1,3,7},{2,5,7},{4,6,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,6,8},{7,8}]=true
  decide +kernel

theorem recovered760 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 760) T=TwentyFiveEightLow.Case760.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case760.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 760)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case760.support T pos))
  · decide +kernel
theorem completion761 : pairCompletion (big 761)=full 761 := by
  have same : big 761=([{0,1,5,6},{0,2,7},{3,5,7},{4,6,7},{1,2,8},{4,5,8},{3,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5,6},{0,2,7},{3,5,7},{4,6,7},{1,2,8},{4,5,8},{3,6,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{2,5},{2,6},{0,1,5,6},{1,7},{0,2,7},{3,5,7},{4,6,7},{0,8},{1,2,8},{4,5,8},{3,6,8},{7,8}]=true
  decide +kernel

theorem recovered761 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 761) T=TwentyFiveEightLow.Case761.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case761.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 761)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case761.support T pos))
  · decide +kernel
theorem completion762 : pairCompletion (big 762)=full 762 := by
  have same : big 762=([{0,2,6},{3,5,6},{1,2,7},{4,5,7},{0,1,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,6},{3,5,6},{1,2,7},{4,5,7},{0,1,5,8},{4,6,8},{3,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{2,5},{1,6},{0,2,6},{3,5,6},{0,7},{1,2,7},{4,5,7},{6,7},{2,8},{0,1,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered762 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 762) T=TwentyFiveEightLow.Case762.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case762.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 762)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case762.support T pos))
  · decide +kernel
theorem completion763 : pairCompletion (big 763)=full 763 := by
  have same : big 763=([{0,1,4,5},{0,2,6},{3,4,6},{1,2,7},{3,5,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{0,2,6},{3,4,6},{1,2,7},{3,5,7},{5,6,8},{4,7,8}] [{0,3},{1,3},{2,3},{2,4},{2,5},{0,1,4,5},{1,6},{0,2,6},{3,4,6},{0,7},{1,2,7},{3,5,7},{6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered763 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 763) T=TwentyFiveEightLow.Case763.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case763.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 763)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case763.support T pos))
  · decide +kernel
theorem completion764 : pairCompletion (big 764)=full 764 := by
  have same : big 764=([{0,1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,6,8},{1,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{0,1,4,5},{1,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{6,7},{2,8},{3,8},{4,8},{5,8},{0,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered764 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 764) T=TwentyFiveEightLow.Case764.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case764.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 764)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case764.support T pos))
  · decide +kernel
theorem completion765 : pairCompletion (big 765)=full 765 := by
  have same : big 765=([{0,1,6},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,4,5,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,4,5,8},{1,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{1,4},{1,5},{0,1,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{6,7},{2,8},{3,8},{0,4,5,8},{6,8},{1,7,8}]=true
  decide +kernel

theorem recovered765 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 765) T=TwentyFiveEightLow.Case765.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case765.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 765)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case765.support T pos))
  · decide +kernel
theorem completion766 : pairCompletion (big 766)=full 766 := by
  have same : big 766=([{0,1,5,6},{0,2,7},{4,5,7},{3,6,7},{1,3,8},{2,5,8},{4,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5,6},{0,2,7},{4,5,7},{3,6,7},{1,3,8},{2,5,8},{4,6,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{2,4},{3,4},{3,5},{2,6},{0,1,5,6},{1,7},{0,2,7},{4,5,7},{3,6,7},{0,8},{1,3,8},{2,5,8},{4,6,8},{7,8}]=true
  decide +kernel

theorem recovered766 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 766) T=TwentyFiveEightLow.Case766.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case766.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 766)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case766.support T pos))
  · decide +kernel
theorem completion767 : pairCompletion (big 767)=full 767 := by
  have same : big 767=([{0,2,6},{4,5,6},{1,3,7},{2,5,7},{0,1,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,6},{4,5,6},{1,3,7},{2,5,7},{0,1,5,8},{3,6,8},{4,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{2,4},{3,4},{3,5},{1,6},{0,2,6},{4,5,6},{0,7},{1,3,7},{2,5,7},{6,7},{2,8},{0,1,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered767 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 767) T=TwentyFiveEightLow.Case767.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case767.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 767)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case767.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
