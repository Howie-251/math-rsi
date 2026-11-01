import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion608 : pairCompletion (big 608)=full 608 := by
  have same : big 608=([{2,3,4,5},{0,1,5,7},{3,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4,5},{0,1,5,7},{3,6,7},{5,6,8},{4,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{2,3,4,5},{0,6},{1,6},{2,6},{4,6},{2,7},{0,1,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered608 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 608) T=TwentyFiveEightLow.Case608.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case608.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 608)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case608.support T pos))
  · decide +kernel
theorem completion609 : pairCompletion (big 609)=full 609 := by
  have same : big 609=([{3,5,7},{4,6,7},{2,3,4,8},{5,6,8},{0,1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,5,7},{4,6,7},{2,3,4,8},{5,6,8},{0,1,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{2,7},{3,5,7},{4,6,7},{2,3,4,8},{5,6,8},{0,1,7,8}]=true
  decide +kernel

theorem recovered609 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 609) T=TwentyFiveEightLow.Case609.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case609.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 609)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case609.support T pos))
  · decide +kernel
theorem completion610 : pairCompletion (big 610)=full 610 := by
  have same : big 610=([{4,5,6},{0,1,4,7},{3,5,7},{2,3,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{4,5,6},{0,1,4,7},{3,5,7},{2,3,4,8},{6,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{3,6},{4,5,6},{2,7},{0,1,4,7},{3,5,7},{0,8},{1,8},{2,3,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered610 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 610) T=TwentyFiveEightLow.Case610.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case610.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 610)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case610.support T pos))
  · decide +kernel
theorem completion611 : pairCompletion (big 611)=full 611 := by
  have same : big 611=([{4,5,6},{0,1,4,7},{2,5,7},{3,6,7},{2,3,4,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{4,5,6},{0,1,4,7},{2,5,7},{3,6,7},{2,3,4,8}] [{0,2},{1,2},{0,3},{1,3},{0,5},{1,5},{3,5},{0,6},{1,6},{2,6},{4,5,6},{0,1,4,7},{2,5,7},{3,6,7},{0,8},{1,8},{2,3,4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered611 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 611) T=TwentyFiveEightLow.Case611.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case611.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 611)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case611.support T pos))
  · decide +kernel
theorem completion612 : pairCompletion (big 612)=full 612 := by
  have same : big 612=([{0,2,3,4},{4,5,6},{2,5,7},{3,6,7},{1,4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{4,5,6},{2,5,7},{3,6,7},{1,4,7,8}] [{0,1},{1,2},{1,3},{0,2,3,4},{0,5},{1,5},{3,5},{0,6},{1,6},{2,6},{4,5,6},{0,7},{2,5,7},{3,6,7},{0,8},{2,8},{3,8},{5,8},{6,8},{1,4,7,8}]=true
  decide +kernel

theorem recovered612 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 612) T=TwentyFiveEightLow.Case612.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case612.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 612)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case612.support T pos))
  · decide +kernel
theorem completion613 : pairCompletion (big 613)=full 613 := by
  have same : big 613=([{0,1,2,3,4},{1,5,6},{2,5,7},{3,6,7},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,4},{1,5,6},{2,5,7},{3,6,7},{4,7,8}] [{0,1,2,3,4},{0,5},{3,5},{4,5},{0,6},{2,6},{4,6},{1,5,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered613 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 613) T=TwentyFiveEightLow.Case613.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case613.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 613)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case613.support T pos))
  · decide +kernel
theorem completion614 : pairCompletion (big 614)=full 614 := by
  have same : big 614=([{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{1,2,8},{3,4,8},{0,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{1,2,8},{3,4,8},{0,5,8},{6,7,8}] [{0,3},{1,3},{0,4},{2,4},{1,5},{2,5},{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{1,2,8},{3,4,8},{0,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered614 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 614) T=TwentyFiveEightLow.Case614.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case614.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 614)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case614.support T pos))
  · decide +kernel
theorem completion615 : pairCompletion (big 615)=full 615 := by
  have same : big 615=([{0,1,5},{3,4,5},{0,2,6},{1,3,6},{1,2,7},{0,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{3,4,5},{0,2,6},{1,3,6},{1,2,7},{0,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] [{0,3},{2,3},{1,4},{2,4},{0,1,5},{3,4,5},{0,2,6},{1,3,6},{1,2,7},{0,4,7},{5,6,7},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered615 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 615) T=TwentyFiveEightLow.Case615.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case615.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 615)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case615.support T pos))
  · decide +kernel
theorem completion616 : pairCompletion (big 616)=full 616 := by
  have same : big 616=([{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{1,3,8},{2,4,8},{0,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{1,3,8},{2,4,8},{0,5,8},{6,7,8}] [{1,2},{0,3},{0,4},{3,4},{1,5},{2,5},{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{1,3,8},{2,4,8},{0,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered616 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 616) T=TwentyFiveEightLow.Case616.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case616.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 616)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case616.support T pos))
  · decide +kernel
theorem completion617 : pairCompletion (big 617)=full 617 := by
  have same : big 617=([{0,2,5},{1,3,5},{1,2,6},{0,4,6},{0,3,7},{1,4,7},{5,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,5},{1,3,5},{1,2,6},{0,4,6},{0,3,7},{1,4,7},{5,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,1},{2,3},{2,4},{3,4},{0,2,5},{1,3,5},{1,2,6},{0,4,6},{0,3,7},{1,4,7},{5,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered617 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 617) T=TwentyFiveEightLow.Case617.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case617.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 617)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case617.support T pos))
  · decide +kernel
theorem completion618 : pairCompletion (big 618)=full 618 := by
  have same : big 618=([{0,1,6},{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{0,1,6},{2,6},{3,6},{4,5,6},{0,2,7},{1,3,7},{4,7},{5,7},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered618 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 618) T=TwentyFiveEightLow.Case618.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case618.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 618)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case618.support T pos))
  · decide +kernel
theorem completion619 : pairCompletion (big 619)=full 619 := by
  have same : big 619=([{0,2,6},{1,3,6},{0,4,7},{1,5,7},{2,3,8},{4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,6},{1,3,6},{0,4,7},{1,5,7},{2,3,8},{4,5,8},{6,7,8}] [{0,1},{1,2},{0,3},{1,4},{2,4},{3,4},{0,5},{2,5},{3,5},{0,2,6},{1,3,6},{4,6},{5,6},{2,7},{3,7},{0,4,7},{1,5,7},{0,8},{1,8},{2,3,8},{4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered619 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 619) T=TwentyFiveEightLow.Case619.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case619.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 619)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case619.support T pos))
  · decide +kernel
theorem completion620 : pairCompletion (big 620)=full 620 := by
  have same : big 620=([{0,1,5},{2,3,5},{0,2,6},{1,4,7},{5,6,7},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{2,3,5},{0,2,6},{1,4,7},{5,6,7},{4,6,8},{3,7,8}] [{1,2},{0,3},{1,3},{0,4},{2,4},{3,4},{0,1,5},{2,3,5},{4,5},{1,6},{0,2,6},{3,6},{0,7},{2,7},{1,4,7},{5,6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered620 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 620) T=TwentyFiveEightLow.Case620.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case620.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 620)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case620.support T pos))
  · decide +kernel
theorem completion621 : pairCompletion (big 621)=full 621 := by
  have same : big 621=([{1,3,5},{2,4,5},{0,1,6},{0,2,7},{5,6,7},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,5},{2,4,5},{0,1,6},{0,2,7},{5,6,7},{3,6,8},{4,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,3,5},{2,4,5},{0,1,6},{2,6},{4,6},{1,7},{0,2,7},{3,7},{5,6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered621 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 621) T=TwentyFiveEightLow.Case621.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case621.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 621)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case621.support T pos))
  · decide +kernel
theorem completion622 : pairCompletion (big 622)=full 622 := by
  have same : big 622=([{0,2,6},{1,3,6},{0,4,7},{1,5,7},{2,4,8},{3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,6},{1,3,6},{0,4,7},{1,5,7},{2,4,8},{3,5,8},{6,7,8}] [{0,1},{1,2},{0,3},{2,3},{1,4},{3,4},{0,5},{2,5},{4,5},{0,2,6},{1,3,6},{4,6},{5,6},{2,7},{3,7},{0,4,7},{1,5,7},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered622 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 622) T=TwentyFiveEightLow.Case622.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case622.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 622)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case622.support T pos))
  · decide +kernel
theorem completion623 : pairCompletion (big 623)=full 623 := by
  have same : big 623=([{0,1,5},{3,4,5},{0,2,6},{1,2,7},{5,6,7},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{3,4,5},{0,2,6},{1,2,7},{5,6,7},{3,6,8},{4,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,1,5},{2,5},{3,4,5},{1,6},{0,2,6},{4,6},{0,7},{1,2,7},{3,7},{5,6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered623 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 623) T=TwentyFiveEightLow.Case623.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case623.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 623)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case623.support T pos))
  · decide +kernel
theorem completion624 : pairCompletion (big 624)=full 624 := by
  have same : big 624=([{0,2,6},{1,3,6},{0,4,7},{1,5,7},{3,4,8},{2,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,6},{1,3,6},{0,4,7},{1,5,7},{3,4,8},{2,5,8},{6,7,8}] [{0,1},{1,2},{0,3},{2,3},{1,4},{2,4},{0,5},{3,5},{4,5},{0,2,6},{1,3,6},{4,6},{5,6},{2,7},{3,7},{0,4,7},{1,5,7},{0,8},{1,8},{3,4,8},{2,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered624 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 624) T=TwentyFiveEightLow.Case624.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case624.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 624)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case624.support T pos))
  · decide +kernel
theorem completion625 : pairCompletion (big 625)=full 625 := by
  have same : big 625=([{1,3,5},{2,4,5},{0,1,6},{0,2,7},{5,6,7},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,5},{2,4,5},{0,1,6},{0,2,7},{5,6,7},{4,6,8},{3,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,3,5},{2,4,5},{0,1,6},{2,6},{3,6},{1,7},{0,2,7},{4,7},{5,6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered625 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 625) T=TwentyFiveEightLow.Case625.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case625.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 625)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case625.support T pos))
  · decide +kernel
theorem completion626 : pairCompletion (big 626)=full 626 := by
  have same : big 626=([{0,1,6},{3,5,6},{0,2,7},{1,4,7},{2,3,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{3,5,6},{0,2,7},{1,4,7},{2,3,8},{4,6,8},{5,7,8}] [{1,2},{0,3},{1,3},{0,4},{2,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,1,6},{2,6},{3,5,6},{0,2,7},{3,7},{1,4,7},{6,7},{0,8},{1,8},{2,3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered626 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 626) T=TwentyFiveEightLow.Case626.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case626.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 626)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case626.support T pos))
  · decide +kernel
theorem completion627 : pairCompletion (big 627)=full 627 := by
  have same : big 627=([{0,1,6},{3,4,6},{0,2,7},{5,6,7},{1,3,8},{2,5,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{3,4,6},{0,2,7},{5,6,7},{1,3,8},{2,5,8},{4,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{3,5},{4,5},{0,1,6},{2,6},{3,4,6},{1,7},{0,2,7},{3,7},{5,6,7},{0,8},{1,3,8},{2,5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered627 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 627) T=TwentyFiveEightLow.Case627.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case627.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 627)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case627.support T pos))
  · decide +kernel
theorem completion628 : pairCompletion (big 628)=full 628 := by
  have same : big 628=([{2,3,6},{0,4,6},{0,1,7},{5,6,7},{1,2,8},{3,5,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,6},{0,4,6},{0,1,7},{5,6,7},{1,2,8},{3,5,8},{4,7,8}] [{0,2},{0,3},{1,3},{1,4},{2,4},{3,4},{0,5},{1,5},{2,5},{4,5},{1,6},{2,3,6},{0,4,6},{0,1,7},{2,7},{3,7},{5,6,7},{0,8},{1,2,8},{3,5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered628 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 628) T=TwentyFiveEightLow.Case628.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case628.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 628)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case628.support T pos))
  · decide +kernel
theorem completion629 : pairCompletion (big 629)=full 629 := by
  have same : big 629=([{0,1,5},{2,3,5},{0,2,6},{1,4,7},{3,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{2,3,5},{0,2,6},{1,4,7},{3,6,7},{4,6,8},{5,7,8}] [{1,2},{0,3},{1,3},{0,4},{2,4},{3,4},{0,1,5},{2,3,5},{4,5},{1,6},{0,2,6},{5,6},{0,7},{2,7},{1,4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered629 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 629) T=TwentyFiveEightLow.Case629.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case629.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 629)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case629.support T pos))
  · decide +kernel
theorem completion630 : pairCompletion (big 630)=full 630 := by
  have same : big 630=([{2,3,5},{1,4,5},{0,1,6},{0,2,7},{3,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{1,4,5},{0,1,6},{0,2,7},{3,6,7},{4,6,8},{5,7,8}] [{1,2},{0,3},{1,3},{0,4},{2,4},{3,4},{0,5},{2,3,5},{1,4,5},{0,1,6},{2,6},{5,6},{1,7},{0,2,7},{4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered630 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 630) T=TwentyFiveEightLow.Case630.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case630.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 630)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case630.support T pos))
  · decide +kernel
theorem completion631 : pairCompletion (big 631)=full 631 := by
  have same : big 631=([{0,2,5},{1,3,5},{0,1,6},{4,5,7},{2,6,7},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,5},{1,3,5},{0,1,6},{4,5,7},{2,6,7},{4,6,8},{3,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,2,5},{1,3,5},{0,1,6},{3,6},{5,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered631 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 631) T=TwentyFiveEightLow.Case631.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case631.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 631)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case631.support T pos))
  · decide +kernel
theorem completion632 : pairCompletion (big 632)=full 632 := by
  have same : big 632=([{0,1,5},{0,2,6},{4,5,6},{1,3,7},{2,5,7},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{0,2,6},{4,5,6},{1,3,7},{2,5,7},{3,6,8},{4,7,8}] [{1,2},{0,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,1,5},{3,5},{1,6},{0,2,6},{4,5,6},{0,7},{1,3,7},{2,5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered632 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 632) T=TwentyFiveEightLow.Case632.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case632.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 632)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case632.support T pos))
  · decide +kernel
theorem completion633 : pairCompletion (big 633)=full 633 := by
  have same : big 633=([{0,3,5},{2,4,5},{0,1,6},{1,5,7},{2,6,7},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,5},{2,4,5},{0,1,6},{1,5,7},{2,6,7},{3,6,8},{4,7,8}] [{0,2},{1,2},{1,3},{2,3},{0,4},{1,4},{3,4},{0,3,5},{2,4,5},{0,1,6},{4,6},{5,6},{0,7},{3,7},{1,5,7},{2,6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered633 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 633) T=TwentyFiveEightLow.Case633.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case633.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 633)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case633.support T pos))
  · decide +kernel
theorem completion634 : pairCompletion (big 634)=full 634 := by
  have same : big 634=([{0,3,5},{0,1,6},{2,5,6},{2,4,7},{1,5,7},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,5},{0,1,6},{2,5,6},{2,4,7},{1,5,7},{4,6,8},{3,7,8}] [{0,2},{1,2},{1,3},{2,3},{0,4},{1,4},{3,4},{0,3,5},{4,5},{0,1,6},{3,6},{2,5,6},{0,7},{2,4,7},{1,5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered634 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 634) T=TwentyFiveEightLow.Case634.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case634.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 634)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case634.support T pos))
  · decide +kernel
theorem completion635 : pairCompletion (big 635)=full 635 := by
  have same : big 635=([{0,2,6},{1,4,6},{0,3,7},{1,5,7},{2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,6},{1,4,6},{0,3,7},{1,5,7},{2,3,8},{5,6,8},{4,7,8}] [{0,1},{1,2},{1,3},{0,4},{2,4},{3,4},{0,5},{2,5},{3,5},{4,5},{0,2,6},{3,6},{1,4,6},{2,7},{0,3,7},{1,5,7},{6,7},{0,8},{1,8},{2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered635 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 635) T=TwentyFiveEightLow.Case635.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case635.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 635)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case635.support T pos))
  · decide +kernel
theorem completion636 : pairCompletion (big 636)=full 636 := by
  have same : big 636=([{0,1,6},{3,4,6},{0,2,7},{5,6,7},{1,2,8},{3,5,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{3,4,6},{0,2,7},{5,6,7},{1,2,8},{3,5,8},{4,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{4,5},{0,1,6},{2,6},{3,4,6},{1,7},{0,2,7},{3,7},{5,6,7},{0,8},{1,2,8},{3,5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered636 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 636) T=TwentyFiveEightLow.Case636.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case636.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 636)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case636.support T pos))
  · decide +kernel
theorem completion637 : pairCompletion (big 637)=full 637 := by
  have same : big 637=([{0,1,5},{3,4,5},{0,2,6},{1,2,7},{3,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{3,4,5},{0,2,6},{1,2,7},{3,6,7},{4,6,8},{5,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,1,5},{2,5},{3,4,5},{1,6},{0,2,6},{5,6},{0,7},{1,2,7},{4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered637 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 637) T=TwentyFiveEightLow.Case637.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case637.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 637)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case637.support T pos))
  · decide +kernel
theorem completion638 : pairCompletion (big 638)=full 638 := by
  have same : big 638=([{0,1,5},{0,2,6},{3,5,6},{1,2,7},{4,5,7},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{0,2,6},{3,5,6},{1,2,7},{4,5,7},{4,6,8},{3,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,1,5},{2,5},{1,6},{0,2,6},{3,5,6},{0,7},{1,2,7},{4,5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered638 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 638) T=TwentyFiveEightLow.Case638.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case638.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 638)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case638.support T pos))
  · decide +kernel
theorem completion639 : pairCompletion (big 639)=full 639 := by
  have same : big 639=([{0,1,5},{3,4,5},{0,2,6},{2,5,7},{1,6,7},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,5},{3,4,5},{0,2,6},{2,5,7},{1,6,7},{3,6,8},{4,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,1,5},{3,4,5},{0,2,6},{4,6},{5,6},{0,7},{3,7},{2,5,7},{1,6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered639 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 639) T=TwentyFiveEightLow.Case639.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case639.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 639)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case639.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
