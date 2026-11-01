import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion768 : pairCompletion (big 768)=full 768 := by
  have same : big 768=([{0,1,4,5},{0,2,6},{3,4,6},{1,3,7},{2,5,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{0,2,6},{3,4,6},{1,3,7},{2,5,7},{5,6,8},{4,7,8}] [{1,2},{0,3},{2,3},{2,4},{3,5},{0,1,4,5},{1,6},{0,2,6},{3,4,6},{0,7},{1,3,7},{2,5,7},{6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered768 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 768) T=TwentyFiveEightLow.Case768.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case768.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 768)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case768.support T pos))
  · decide +kernel
theorem completion769 : pairCompletion (big 769)=full 769 := by
  have same : big 769=([{0,1,4,5},{0,2,6},{3,4,6},{2,4,7},{3,5,7},{5,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{0,2,6},{3,4,6},{2,4,7},{3,5,7},{5,6,8},{1,7,8}] [{1,2},{0,3},{1,3},{2,3},{2,5},{0,1,4,5},{1,6},{0,2,6},{3,4,6},{0,7},{2,4,7},{3,5,7},{6,7},{0,8},{2,8},{3,8},{4,8},{5,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered769 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 769) T=TwentyFiveEightLow.Case769.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case769.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 769)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case769.support T pos))
  · decide +kernel
theorem completion770 : pairCompletion (big 770)=full 770 := by
  have same : big 770=([{0,1,6},{2,4,6},{3,5,6},{1,4,7},{2,5,7},{0,4,5,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{2,4,6},{3,5,6},{1,4,7},{2,5,7},{0,4,5,8},{3,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{3,4},{1,5},{0,1,6},{2,4,6},{3,5,6},{0,7},{1,4,7},{2,5,7},{6,7},{1,8},{2,8},{0,4,5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered770 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 770) T=TwentyFiveEightLow.Case770.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case770.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 770)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case770.support T pos))
  · decide +kernel
theorem completion771 : pairCompletion (big 771)=full 771 := by
  have same : big 771=([{0,1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{6,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{0,1,4,5},{0,6},{1,6},{2,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered771 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 771) T=TwentyFiveEightLow.Case771.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case771.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 771)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case771.support T pos))
  · decide +kernel
theorem completion772 : pairCompletion (big 772)=full 772 := by
  have same : big 772=([{3,5,6},{4,5,7},{0,2,6,7},{1,2,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,5,6},{4,5,7},{0,2,6,7},{1,2,5,8},{4,6,8},{3,7,8}] [{0,1},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,5},{1,6},{3,5,6},{1,7},{4,5,7},{0,2,6,7},{0,8},{1,2,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered772 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 772) T=TwentyFiveEightLow.Case772.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case772.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 772)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case772.support T pos))
  · decide +kernel
theorem completion773 : pairCompletion (big 773)=full 773 := by
  have same : big 773=([{0,2,4,5},{3,4,6},{3,5,7},{1,2,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4,5},{3,4,6},{3,5,7},{1,2,6,7},{5,6,8},{4,7,8}] [{0,1},{0,3},{1,3},{2,3},{1,4},{1,5},{0,2,4,5},{0,6},{3,4,6},{0,7},{3,5,7},{1,2,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered773 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 773) T=TwentyFiveEightLow.Case773.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case773.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 773)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case773.support T pos))
  · decide +kernel
theorem completion774 : pairCompletion (big 774)=full 774 := by
  have same : big 774=([{2,4,5},{3,4,6},{3,5,7},{2,6,7},{0,5,6,8},{1,4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{3,4,6},{3,5,7},{2,6,7},{0,5,6,8},{1,4,7,8}] [{0,1},{0,2},{1,2},{0,3},{1,3},{2,3},{0,4},{1,5},{2,4,5},{1,6},{3,4,6},{0,7},{3,5,7},{2,6,7},{2,8},{3,8},{0,5,6,8},{1,4,7,8}]=true
  decide +kernel

theorem recovered774 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 774) T=TwentyFiveEightLow.Case774.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case774.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 774)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case774.support T pos))
  · decide +kernel
theorem completion775 : pairCompletion (big 775)=full 775 := by
  have same : big 775=([{0,1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{0,1,4,5},{0,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{0,8},{2,8},{3,8},{4,8},{5,8},{1,6,7,8}]=true
  decide +kernel

theorem recovered775 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 775) T=TwentyFiveEightLow.Case775.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case775.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 775)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case775.support T pos))
  · decide +kernel
theorem completion776 : pairCompletion (big 776)=full 776 := by
  have same : big 776=([{0,1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,6,7},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,6,7},{1,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{0,1,4,5},{1,6},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,6,7},{0,8},{2,8},{3,8},{4,8},{5,8},{6,8},{1,7,8}]=true
  decide +kernel

theorem recovered776 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 776) T=TwentyFiveEightLow.Case776.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case776.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 776)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case776.support T pos))
  · decide +kernel
theorem completion777 : pairCompletion (big 777)=full 777 := by
  have same : big 777=([{0,1,4,5},{2,4,6},{3,5,6},{0,2,7},{3,4,7},{1,6,7},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{2,4,6},{3,5,6},{0,2,7},{3,4,7},{1,6,7},{5,7,8}] [{1,2},{0,3},{1,3},{2,3},{2,5},{0,1,4,5},{0,6},{2,4,6},{3,5,6},{0,2,7},{3,4,7},{1,6,7},{0,8},{1,8},{2,8},{3,8},{4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered777 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 777) T=TwentyFiveEightLow.Case777.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case777.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 777)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case777.support T pos))
  · decide +kernel
theorem completion778 : pairCompletion (big 778)=full 778 := by
  have same : big 778=([{0,1,2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,1,2,5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered778 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 778) T=TwentyFiveEightLow.Case778.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case778.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 778)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case778.support T pos))
  · decide +kernel
theorem completion779 : pairCompletion (big 779)=full 779 := by
  have same : big 779=([{3,5,6},{4,5,7},{2,6,7},{0,1,2,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,5,6},{4,5,7},{2,6,7},{0,1,2,5,8},{4,6,8},{3,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,6},{1,6},{3,5,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,1,2,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered779 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 779) T=TwentyFiveEightLow.Case779.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case779.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 779)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case779.support T pos))
  · decide +kernel
theorem completion780 : pairCompletion (big 780)=full 780 := by
  have same : big 780=([{0,1,2,4,5},{3,4,6},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,4,5},{3,4,6},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] [{0,3},{1,3},{2,3},{0,1,2,4,5},{0,6},{1,6},{3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered780 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 780) T=TwentyFiveEightLow.Case780.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case780.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 780)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case780.support T pos))
  · decide +kernel
theorem completion781 : pairCompletion (big 781)=full 781 := by
  have same : big 781=([{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,1,4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,1,4,5,8},{6,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{0,6},{1,6},{2,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{2,8},{3,8},{0,1,4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered781 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 781) T=TwentyFiveEightLow.Case781.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case781.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 781)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case781.support T pos))
  · decide +kernel
theorem completion782 : pairCompletion (big 782)=full 782 := by
  have same : big 782=([{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,1,4,5,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,1,4,5,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{0,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{1,6,7},{2,8},{3,8},{0,1,4,5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered782 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 782) T=TwentyFiveEightLow.Case782.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case782.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 782)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case782.support T pos))
  · decide +kernel
theorem completion783 : pairCompletion (big 783)=full 783 := by
  have same : big 783=([{3,5,6},{0,1,7},{4,5,7},{2,6,7},{0,2,8},{1,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,5,6},{0,1,7},{4,5,7},{2,6,7},{0,2,8},{1,5,8},{4,6,8},{3,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,5},{2,5},{0,6},{1,6},{3,5,6},{0,1,7},{4,5,7},{2,6,7},{0,2,8},{1,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered783 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 783) T=TwentyFiveEightLow.Case783.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case783.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 783)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case783.support T pos))
  · decide +kernel
theorem completion784 : pairCompletion (big 784)=full 784 := by
  have same : big 784=([{0,1,6},{3,5,6},{0,2,7},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{3,5,6},{0,2,7},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,5},{2,5},{0,1,6},{3,5,6},{0,2,7},{1,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered784 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 784) T=TwentyFiveEightLow.Case784.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case784.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 784)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case784.support T pos))
  · decide +kernel
theorem completion785 : pairCompletion (big 785)=full 785 := by
  have same : big 785=([{3,4,5},{0,1,6},{2,4,6},{0,2,7},{1,5,7},{3,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,1,6},{2,4,6},{0,2,7},{1,5,7},{3,6,7},{5,6,8},{4,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{0,5},{2,5},{3,4,5},{0,1,6},{2,4,6},{0,2,7},{1,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered785 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 785) T=TwentyFiveEightLow.Case785.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case785.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 785)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case785.support T pos))
  · decide +kernel
theorem completion786 : pairCompletion (big 786)=full 786 := by
  have same : big 786=([{0,1,6},{2,4,6},{3,5,6},{0,2,7},{3,4,7},{1,5,7},{4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{2,4,6},{3,5,6},{0,2,7},{3,4,7},{1,5,7},{4,5,8},{6,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{0,5},{2,5},{0,1,6},{2,4,6},{3,5,6},{0,2,7},{3,4,7},{1,5,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered786 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 786) T=TwentyFiveEightLow.Case786.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case786.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 786)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case786.support T pos))
  · decide +kernel
theorem completion787 : pairCompletion (big 787)=full 787 := by
  have same : big 787=([{2,4,5},{0,1,6},{3,4,6},{0,4,7},{3,5,7},{2,6,7},{5,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{0,1,6},{3,4,6},{0,4,7},{3,5,7},{2,6,7},{5,6,8},{1,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{1,4},{0,5},{1,5},{2,4,5},{0,1,6},{3,4,6},{0,4,7},{3,5,7},{2,6,7},{0,8},{2,8},{3,8},{4,8},{5,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered787 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 787) T=TwentyFiveEightLow.Case787.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case787.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 787)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case787.support T pos))
  · decide +kernel
theorem completion788 : pairCompletion (big 788)=full 788 := by
  have same : big 788=([{0,4,5},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{3,6,8},{2,7,8}] [{0,1},{0,2},{1,2},{0,3},{1,3},{2,3},{2,4},{3,5},{0,4,5},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{0,8},{1,8},{4,8},{5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered788 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 788) T=TwentyFiveEightLow.Case788.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case788.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 788)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case788.support T pos))
  · decide +kernel
theorem completion789 : pairCompletion (big 789)=full 789 := by
  have same : big 789=([{3,5,6},{0,1,2,7},{4,5,7},{1,3,8},{2,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,5,6},{0,1,2,7},{4,5,7},{1,3,8},{2,4,8},{6,7,8}] [{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{4,6},{3,5,6},{0,1,2,7},{3,7},{4,5,7},{0,8},{1,3,8},{2,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered789 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 789) T=TwentyFiveEightLow.Case789.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case789.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 789)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case789.support T pos))
  · decide +kernel
theorem completion790 : pairCompletion (big 790)=full 790 := by
  have same : big 790=([{3,5,6},{1,3,7},{2,4,7},{0,1,2,8},{4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,5,6},{1,3,7},{2,4,7},{0,1,2,8},{4,5,8},{6,7,8}] [{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{4,6},{3,5,6},{0,7},{1,3,7},{2,4,7},{5,7},{0,1,2,8},{3,8},{4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered790 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 790) T=TwentyFiveEightLow.Case790.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case790.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 790)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case790.support T pos))
  · decide +kernel
theorem completion791 : pairCompletion (big 791)=full 791 := by
  have same : big 791=([{0,1,2,6},{3,5,6},{1,3,7},{2,4,7},{4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,6},{3,5,6},{1,3,7},{2,4,7},{4,5,8},{6,7,8}] [{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{0,1,2,6},{4,6},{3,5,6},{0,7},{1,3,7},{2,4,7},{5,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered791 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 791) T=TwentyFiveEightLow.Case791.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case791.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 791)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case791.support T pos))
  · decide +kernel
theorem completion792 : pairCompletion (big 792)=full 792 := by
  have same : big 792=([{0,1,2,6},{1,3,7},{2,4,7},{5,6,7},{3,5,8},{4,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,6},{1,3,7},{2,4,7},{5,6,7},{3,5,8},{4,6,8}] [{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,1,2,6},{3,6},{0,7},{1,3,7},{2,4,7},{5,6,7},{0,8},{1,8},{2,8},{3,5,8},{4,6,8},{7,8}]=true
  decide +kernel

theorem recovered792 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 792) T=TwentyFiveEightLow.Case792.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case792.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 792)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case792.support T pos))
  · decide +kernel
theorem completion793 : pairCompletion (big 793)=full 793 := by
  have same : big 793=([{3,4,5},{0,1,2,6},{1,3,7},{4,6,7},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,1,2,6},{1,3,7},{4,6,7},{5,6,8},{2,7,8}] [{0,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,4,5},{0,1,2,6},{3,6},{0,7},{1,3,7},{5,7},{4,6,7},{0,8},{1,8},{3,8},{4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered793 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 793) T=TwentyFiveEightLow.Case793.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case793.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 793)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case793.support T pos))
  · decide +kernel
theorem completion794 : pairCompletion (big 794)=full 794 := by
  have same : big 794=([{0,1,2,6},{3,4,6},{1,3,7},{5,6,7},{4,5,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,6},{3,4,6},{1,3,7},{5,6,7},{4,5,8},{2,7,8}] [{0,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,5},{0,1,2,6},{3,4,6},{0,7},{1,3,7},{4,7},{5,6,7},{0,8},{1,8},{3,8},{4,5,8},{6,8},{2,7,8}]=true
  decide +kernel

theorem recovered794 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 794) T=TwentyFiveEightLow.Case794.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case794.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 794)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case794.support T pos))
  · decide +kernel
theorem completion795 : pairCompletion (big 795)=full 795 := by
  have same : big 795=([{2,3,4},{3,5,6},{1,2,7},{4,6,7},{0,1,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{3,5,6},{1,2,7},{4,6,7},{0,1,6,8},{5,7,8}] [{0,2},{0,3},{1,3},{0,4},{1,4},{2,3,4},{0,5},{1,5},{2,5},{4,5},{2,6},{3,5,6},{0,7},{1,2,7},{3,7},{4,6,7},{2,8},{3,8},{4,8},{0,1,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered795 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 795) T=TwentyFiveEightLow.Case795.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case795.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 795)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case795.support T pos))
  · decide +kernel
theorem completion796 : pairCompletion (big 796)=full 796 := by
  have same : big 796=([{3,4,5},{2,3,6},{1,2,7},{4,6,7},{0,1,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{2,3,6},{1,2,7},{4,6,7},{0,1,6,8},{5,7,8}] [{0,2},{0,3},{1,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,4,5},{2,3,6},{5,6},{0,7},{1,2,7},{3,7},{4,6,7},{2,8},{3,8},{4,8},{0,1,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered796 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 796) T=TwentyFiveEightLow.Case796.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case796.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 796)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case796.support T pos))
  · decide +kernel
theorem completion797 : pairCompletion (big 797)=full 797 := by
  have same : big 797=([{2,4,5},{3,4,6},{0,2,7},{1,3,7},{5,6,7},{0,1,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{3,4,6},{0,2,7},{1,3,7},{5,6,7},{0,1,6,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{0,5},{1,5},{3,5},{2,4,5},{2,6},{3,4,6},{0,2,7},{1,3,7},{4,7},{5,6,7},{2,8},{3,8},{4,8},{5,8},{0,1,6,8},{7,8}]=true
  decide +kernel

theorem recovered797 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 797) T=TwentyFiveEightLow.Case797.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case797.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 797)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case797.support T pos))
  · decide +kernel
theorem completion798 : pairCompletion (big 798)=full 798 := by
  have same : big 798=([{2,3,4},{3,5,6},{0,1,2,7},{4,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{3,5,6},{0,1,2,7},{4,5,7},{6,7,8}] [{0,3},{1,3},{0,4},{1,4},{2,3,4},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{4,6},{3,5,6},{0,1,2,7},{3,7},{4,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered798 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 798) T=TwentyFiveEightLow.Case798.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case798.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 798)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case798.support T pos))
  · decide +kernel
theorem completion799 : pairCompletion (big 799)=full 799 := by
  have same : big 799=([{1,3,4,5},{2,3,6},{0,1,2,7},{4,6,7},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4,5},{2,3,6},{0,1,2,7},{4,6,7},{5,7,8}] [{0,3},{0,4},{2,4},{0,5},{2,5},{1,3,4,5},{0,6},{1,6},{2,3,6},{5,6},{0,1,2,7},{3,7},{4,6,7},{0,8},{1,8},{2,8},{3,8},{4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered799 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 799) T=TwentyFiveEightLow.Case799.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case799.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 799)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case799.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
