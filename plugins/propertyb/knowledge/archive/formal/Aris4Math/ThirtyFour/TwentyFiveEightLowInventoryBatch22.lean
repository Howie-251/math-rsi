import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion704 : pairCompletion (big 704)=full 704 := by
  have same : big 704=([{0,3,6},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{0,1,2,5,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,6},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{0,1,2,5,8}] [{1,3},{2,3},{0,4},{2,4},{3,4},{1,6},{0,3,6},{4,5,6},{0,7},{1,4,7},{3,5,7},{2,6,7},{3,8},{4,8},{0,1,2,5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered704 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 704) T=TwentyFiveEightLow.Case704.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case704.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 704)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case704.support T pos))
  · decide +kernel
theorem completion705 : pairCompletion (big 705)=full 705 := by
  have same : big 705=([{0,4,6},{1,5,6},{2,4,7},{3,5,7},{0,1,8},{3,4,8},{2,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,6},{1,5,6},{2,4,7},{3,5,7},{0,1,8},{3,4,8},{2,5,8},{6,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{1,4},{0,5},{4,5},{2,6},{3,6},{0,4,6},{1,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,1,8},{3,4,8},{2,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered705 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 705) T=TwentyFiveEightLow.Case705.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case705.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 705)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case705.support T pos))
  · decide +kernel
theorem completion706 : pairCompletion (big 706)=full 706 := by
  have same : big 706=([{0,4,5},{1,4,6},{0,1,7},{2,5,7},{3,6,7},{3,5,8},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{1,4,6},{0,1,7},{2,5,7},{3,6,7},{3,5,8},{2,6,8},{4,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{2,4},{3,4},{1,5},{0,4,5},{0,6},{1,4,6},{5,6},{0,1,7},{2,5,7},{3,6,7},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered706 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 706) T=TwentyFiveEightLow.Case706.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case706.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 706)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case706.support T pos))
  · decide +kernel
theorem completion707 : pairCompletion (big 707)=full 707 := by
  have same : big 707=([{2,4,5},{3,4,6},{0,1,7},{3,5,7},{2,6,7},{0,5,8},{1,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{3,4,6},{0,1,7},{3,5,7},{2,6,7},{0,5,8},{1,6,8},{4,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{1,5},{2,4,5},{0,6},{3,4,6},{5,6},{0,1,7},{3,5,7},{2,6,7},{2,8},{3,8},{0,5,8},{1,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered707 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 707) T=TwentyFiveEightLow.Case707.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case707.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 707)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case707.support T pos))
  · decide +kernel
theorem completion708 : pairCompletion (big 708)=full 708 := by
  have same : big 708=([{0,4,5},{2,4,6},{0,1,7},{3,4,7},{5,6,7},{1,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{2,4,6},{0,1,7},{3,4,7},{5,6,7},{1,5,8},{3,6,8},{2,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{1,4},{2,5},{3,5},{0,4,5},{0,6},{1,6},{2,4,6},{0,1,7},{3,4,7},{5,6,7},{0,8},{4,8},{1,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered708 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 708) T=TwentyFiveEightLow.Case708.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case708.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 708)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case708.support T pos))
  · decide +kernel
theorem completion709 : pairCompletion (big 709)=full 709 := by
  have same : big 709=([{0,3,4},{1,3,5},{2,4,6},{0,1,7},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{2,4,6},{0,1,7},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] [{0,2},{1,2},{2,3},{1,4},{0,3,4},{0,5},{1,3,5},{4,5},{0,6},{1,6},{2,4,6},{0,1,7},{2,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered709 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 709) T=TwentyFiveEightLow.Case709.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case709.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 709)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case709.support T pos))
  · decide +kernel
theorem completion710 : pairCompletion (big 710)=full 710 := by
  have same : big 710=([{0,3,4},{1,4,5},{2,3,6},{1,3,7},{0,5,7},{4,6,7},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,4,5},{2,3,6},{1,3,7},{0,5,7},{4,6,7},{5,6,8},{2,7,8}] [{0,1},{0,2},{1,2},{2,4},{0,3,4},{2,5},{3,5},{1,4,5},{0,6},{1,6},{2,3,6},{1,3,7},{0,5,7},{4,6,7},{0,8},{1,8},{3,8},{4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered710 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 710) T=TwentyFiveEightLow.Case710.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case710.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 710)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case710.support T pos))
  · decide +kernel
theorem completion711 : pairCompletion (big 711)=full 711 := by
  have same : big 711=([{0,4,6},{2,5,6},{3,4,7},{1,5,7},{0,1,8},{2,4,8},{3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,6},{2,5,6},{3,4,7},{1,5,7},{0,1,8},{2,4,8},{3,5,8},{6,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{1,4},{0,5},{4,5},{1,6},{3,6},{0,4,6},{2,5,6},{0,7},{2,7},{3,4,7},{1,5,7},{0,1,8},{2,4,8},{3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered711 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 711) T=TwentyFiveEightLow.Case711.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case711.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 711)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case711.support T pos))
  · decide +kernel
theorem completion712 : pairCompletion (big 712)=full 712 := by
  have same : big 712=([{0,4,5},{2,4,6},{0,1,7},{2,5,7},{3,6,7},{3,5,8},{1,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{2,4,6},{0,1,7},{2,5,7},{3,6,7},{3,5,8},{1,6,8},{4,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{1,4},{3,4},{1,5},{0,4,5},{0,6},{2,4,6},{5,6},{0,1,7},{2,5,7},{3,6,7},{0,8},{2,8},{3,5,8},{1,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered712 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 712) T=TwentyFiveEightLow.Case712.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case712.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 712)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case712.support T pos))
  · decide +kernel
theorem completion713 : pairCompletion (big 713)=full 713 := by
  have same : big 713=([{0,4,5},{2,4,6},{0,1,7},{3,4,7},{5,6,7},{3,5,8},{1,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{2,4,6},{0,1,7},{3,4,7},{5,6,7},{3,5,8},{1,6,8},{2,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{1,4},{1,5},{2,5},{0,4,5},{0,6},{3,6},{2,4,6},{0,1,7},{3,4,7},{5,6,7},{0,8},{4,8},{3,5,8},{1,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered713 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 713) T=TwentyFiveEightLow.Case713.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case713.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 713)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case713.support T pos))
  · decide +kernel
theorem completion714 : pairCompletion (big 714)=full 714 := by
  have same : big 714=([{2,3,4},{0,3,5},{1,4,6},{0,1,7},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{0,3,5},{1,4,6},{0,1,7},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] [{0,2},{1,2},{1,3},{0,4},{2,3,4},{1,5},{0,3,5},{4,5},{0,6},{2,6},{1,4,6},{0,1,7},{2,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered714 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 714) T=TwentyFiveEightLow.Case714.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case714.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 714)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case714.support T pos))
  · decide +kernel
theorem completion715 : pairCompletion (big 715)=full 715 := by
  have same : big 715=([{2,3,4},{1,4,5},{0,3,6},{1,3,7},{0,5,7},{4,6,7},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{1,4,5},{0,3,6},{1,3,7},{0,5,7},{4,6,7},{5,6,8},{2,7,8}] [{0,1},{0,2},{1,2},{0,4},{2,3,4},{2,5},{3,5},{1,4,5},{1,6},{2,6},{0,3,6},{1,3,7},{0,5,7},{4,6,7},{0,8},{1,8},{3,8},{4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered715 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 715) T=TwentyFiveEightLow.Case715.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case715.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 715)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case715.support T pos))
  · decide +kernel
theorem completion716 : pairCompletion (big 716)=full 716 := by
  have same : big 716=([{0,2,4},{1,3,5},{3,4,6},{2,5,6},{1,2,7},{0,3,7},{4,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4},{1,3,5},{3,4,6},{2,5,6},{1,2,7},{0,3,7},{4,5,7},{6,7,8}] [{0,1},{2,3},{1,4},{0,2,4},{0,5},{1,3,5},{0,6},{1,6},{3,4,6},{2,5,6},{1,2,7},{0,3,7},{4,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered716 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 716) T=TwentyFiveEightLow.Case716.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case716.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 716)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case716.support T pos))
  · decide +kernel
theorem completion717 : pairCompletion (big 717)=full 717 := by
  have same : big 717=([{0,1,4,6},{3,5,6},{3,4,7},{0,2,5,7},{2,4,8},{1,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,6},{3,5,6},{3,4,7},{0,2,5,7},{2,4,8},{1,5,8},{6,7,8}] [{1,2},{0,3},{1,3},{2,3},{4,5},{2,6},{0,1,4,6},{3,5,6},{1,7},{3,4,7},{0,2,5,7},{0,8},{3,8},{2,4,8},{1,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered717 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 717) T=TwentyFiveEightLow.Case717.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case717.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 717)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case717.support T pos))
  · decide +kernel
theorem completion718 : pairCompletion (big 718)=full 718 := by
  have same : big 718=([{3,4,6},{0,1,5,6},{1,4,7},{2,5,7},{0,2,4,8},{3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,6},{0,1,5,6},{1,4,7},{2,5,7},{0,2,4,8},{3,5,8},{6,7,8}] [{1,2},{0,3},{1,3},{2,3},{4,5},{2,6},{3,4,6},{0,1,5,6},{0,7},{3,7},{1,4,7},{2,5,7},{1,8},{0,2,4,8},{3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered718 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 718) T=TwentyFiveEightLow.Case718.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case718.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 718)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case718.support T pos))
  · decide +kernel
theorem completion719 : pairCompletion (big 719)=full 719 := by
  have same : big 719=([{3,4,5},{0,2,4,6},{1,4,7},{5,6,7},{0,1,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,2,4,6},{1,4,7},{5,6,7},{0,1,5,8},{3,6,8},{2,7,8}] [{1,2},{0,3},{1,3},{2,3},{2,5},{3,4,5},{1,6},{0,2,4,6},{0,7},{3,7},{1,4,7},{5,6,7},{4,8},{0,1,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered719 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 719) T=TwentyFiveEightLow.Case719.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case719.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 719)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case719.support T pos))
  · decide +kernel
theorem completion720 : pairCompletion (big 720)=full 720 := by
  have same : big 720=([{0,1,3,5},{0,2,4,6},{2,3,7},{1,4,7},{5,6,7},{4,5,8},{3,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,5},{0,2,4,6},{2,3,7},{1,4,7},{5,6,7},{4,5,8},{3,6,8}] [{1,2},{3,4},{2,5},{0,1,3,5},{1,6},{0,2,4,6},{0,7},{2,3,7},{1,4,7},{5,6,7},{0,8},{1,8},{2,8},{4,5,8},{3,6,8},{7,8}]=true
  decide +kernel

theorem recovered720 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 720) T=TwentyFiveEightLow.Case720.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case720.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 720)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case720.support T pos))
  · decide +kernel
theorem completion721 : pairCompletion (big 721)=full 721 := by
  have same : big 721=([{2,3,4},{0,1,4,6},{2,5,6},{1,3,7},{4,5,7},{0,3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{0,1,4,6},{2,5,6},{1,3,7},{4,5,7},{0,3,5,8},{6,7,8}] [{0,2},{1,2},{2,3,4},{1,5},{3,6},{0,1,4,6},{2,5,6},{0,7},{2,7},{1,3,7},{4,5,7},{1,8},{2,8},{4,8},{0,3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered721 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 721) T=TwentyFiveEightLow.Case721.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case721.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 721)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case721.support T pos))
  · decide +kernel
theorem completion722 : pairCompletion (big 722)=full 722 := by
  have same : big 722=([{2,3,5},{2,4,6},{0,3,7},{1,4,7},{5,6,7},{0,4,5,8},{1,3,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{2,4,6},{0,3,7},{1,4,7},{5,6,7},{0,4,5,8},{1,3,6,8}] [{0,1},{0,2},{1,2},{3,4},{1,5},{2,3,5},{0,6},{2,4,6},{2,7},{0,3,7},{1,4,7},{5,6,7},{2,8},{0,4,5,8},{1,3,6,8},{7,8}]=true
  decide +kernel

theorem recovered722 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 722) T=TwentyFiveEightLow.Case722.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case722.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 722)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case722.support T pos))
  · decide +kernel
theorem completion723 : pairCompletion (big 723)=full 723 := by
  have same : big 723=([{0,2,5},{1,3,6},{4,5,6},{0,1,7},{3,5,7},{2,6,7},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,5},{1,3,6},{4,5,6},{0,1,7},{3,5,7},{2,6,7},{4,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{2,4},{3,4},{1,5},{0,2,5},{0,6},{1,3,6},{4,5,6},{0,1,7},{3,5,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered723 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 723) T=TwentyFiveEightLow.Case723.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case723.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 723)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case723.support T pos))
  · decide +kernel
theorem completion724 : pairCompletion (big 724)=full 724 := by
  have same : big 724=([{2,4,6},{3,5,7},{0,1,6,7},{0,2,8},{1,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,6},{3,5,7},{0,1,6,7},{0,2,8},{1,3,8},{5,6,8},{4,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{3,6},{2,4,6},{2,7},{3,5,7},{0,1,6,7},{0,2,8},{1,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered724 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 724) T=TwentyFiveEightLow.Case724.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case724.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 724)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case724.support T pos))
  · decide +kernel
theorem completion725 : pairCompletion (big 725)=full 725 := by
  have same : big 725=([{2,4,6},{0,2,7},{1,3,7},{5,6,7},{3,5,8},{0,1,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,6},{0,2,7},{1,3,7},{5,6,7},{3,5,8},{0,1,6,8},{4,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{3,6},{2,4,6},{0,2,7},{1,3,7},{5,6,7},{2,8},{3,5,8},{0,1,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered725 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 725) T=TwentyFiveEightLow.Case725.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case725.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 725)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case725.support T pos))
  · decide +kernel
theorem completion726 : pairCompletion (big 726)=full 726 := by
  have same : big 726=([{2,4,5},{0,1,5,6},{0,2,7},{1,3,7},{4,6,7},{3,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{0,1,5,6},{0,2,7},{1,3,7},{4,6,7},{3,6,8},{5,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{3,5},{2,4,5},{2,6},{0,1,5,6},{0,2,7},{1,3,7},{4,6,7},{0,8},{1,8},{2,8},{4,8},{3,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered726 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 726) T=TwentyFiveEightLow.Case726.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case726.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 726)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case726.support T pos))
  · decide +kernel
theorem completion727 : pairCompletion (big 727)=full 727 := by
  have same : big 727=([{2,3,5},{0,1,5,6},{0,2,7},{4,5,7},{3,6,7},{4,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{0,1,5,6},{0,2,7},{4,5,7},{3,6,7},{4,6,8},{1,7,8}] [{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{2,3,5},{2,6},{0,1,5,6},{0,2,7},{4,5,7},{3,6,7},{0,8},{2,8},{3,8},{5,8},{4,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered727 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 727) T=TwentyFiveEightLow.Case727.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case727.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 727)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case727.support T pos))
  · decide +kernel
theorem completion728 : pairCompletion (big 728)=full 728 := by
  have same : big 728=([{1,2,5},{3,4,6},{0,1,7},{3,5,7},{2,6,7},{0,5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,5},{3,4,6},{0,1,7},{3,5,7},{2,6,7},{0,5,6,8},{4,7,8}] [{0,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{1,2,5},{4,5},{1,6},{3,4,6},{0,1,7},{3,5,7},{2,6,7},{1,8},{2,8},{3,8},{0,5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered728 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 728) T=TwentyFiveEightLow.Case728.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case728.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 728)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case728.support T pos))
  · decide +kernel
theorem completion729 : pairCompletion (big 729)=full 729 := by
  have same : big 729=([{2,4,6},{3,5,7},{0,1,6,7},{2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,6},{3,5,7},{0,1,6,7},{2,3,8},{5,6,8},{4,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{3,6},{2,4,6},{2,7},{3,5,7},{0,1,6,7},{0,8},{1,8},{2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered729 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 729) T=TwentyFiveEightLow.Case729.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case729.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 729)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case729.support T pos))
  · decide +kernel
theorem completion730 : pairCompletion (big 730)=full 730 := by
  have same : big 730=([{2,3,6},{2,4,7},{5,6,7},{4,5,8},{0,1,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,6},{2,4,7},{5,6,7},{4,5,8},{0,1,6,8},{3,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{3,5},{2,3,6},{4,6},{0,7},{1,7},{2,4,7},{5,6,7},{2,8},{4,5,8},{0,1,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered730 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 730) T=TwentyFiveEightLow.Case730.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case730.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 730)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case730.support T pos))
  · decide +kernel
theorem completion731 : pairCompletion (big 731)=full 731 := by
  have same : big 731=([{2,3,5},{0,1,5,6},{2,4,7},{3,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{0,1,5,6},{2,4,7},{3,6,7},{4,6,8},{5,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{3,4},{2,3,5},{4,5},{2,6},{0,1,5,6},{0,7},{1,7},{2,4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered731 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 731) T=TwentyFiveEightLow.Case731.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case731.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 731)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case731.support T pos))
  · decide +kernel
theorem completion732 : pairCompletion (big 732)=full 732 := by
  have same : big 732=([{2,3,5},{0,1,5,6},{4,5,7},{2,6,7},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{0,1,5,6},{4,5,7},{2,6,7},{4,6,8},{3,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{2,3,5},{3,6},{0,1,5,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered732 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 732) T=TwentyFiveEightLow.Case732.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case732.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 732)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case732.support T pos))
  · decide +kernel
theorem completion733 : pairCompletion (big 733)=full 733 := by
  have same : big 733=([{1,3,5},{2,4,6},{1,2,7},{4,5,7},{3,6,7},{0,5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,5},{2,4,6},{1,2,7},{4,5,7},{3,6,7},{0,5,6,8}] [{0,1},{0,2},{0,3},{2,3},{0,4},{1,4},{3,4},{2,5},{1,3,5},{1,6},{2,4,6},{0,7},{1,2,7},{4,5,7},{3,6,7},{1,8},{2,8},{3,8},{4,8},{0,5,6,8},{7,8}]=true
  decide +kernel

theorem recovered733 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 733) T=TwentyFiveEightLow.Case733.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case733.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 733)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case733.support T pos))
  · decide +kernel
theorem completion734 : pairCompletion (big 734)=full 734 := by
  have same : big 734=([{2,4,6},{3,5,7},{0,1,6,7},{1,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,6},{3,5,7},{0,1,6,7},{1,2,3,8},{5,6,8},{4,7,8}] [{0,2},{0,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{3,6},{2,4,6},{2,7},{3,5,7},{0,1,6,7},{0,8},{1,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered734 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 734) T=TwentyFiveEightLow.Case734.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case734.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 734)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case734.support T pos))
  · decide +kernel
theorem completion735 : pairCompletion (big 735)=full 735 := by
  have same : big 735=([{2,4,6},{1,2,3,7},{5,6,7},{3,5,8},{0,1,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,6},{1,2,3,7},{5,6,7},{3,5,8},{0,1,6,8},{4,7,8}] [{0,2},{0,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{3,6},{2,4,6},{0,7},{1,2,3,7},{5,6,7},{2,8},{3,5,8},{0,1,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered735 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 735) T=TwentyFiveEightLow.Case735.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case735.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 735)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case735.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
