import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion128 : pairCompletion (big 128)=full 128 := by
  have same : big 128=([{0,1,2,3},{0,4,5},{5,6,7},{1,4,8},{2,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,5},{5,6,7},{1,4,8},{2,6,8},{3,7,8}] [{0,1,2,3},{2,4},{3,4},{1,5},{2,5},{3,5},{0,4,5},{0,6},{1,6},{3,6},{4,6},{0,7},{1,7},{2,7},{4,7},{5,6,7},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered128 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 128) T=TwentyFiveEightLow.Case128.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case128.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 128)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case128.support T pos))
  · decide +kernel
theorem completion129 : pairCompletion (big 129)=full 129 := by
  have same : big 129=([{0,1,2,3},{0,4,5},{1,4,7},{2,6,7},{5,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,5},{1,4,7},{2,6,7},{5,6,8},{3,7,8}] [{0,1,2,3},{2,4},{3,4},{1,5},{2,5},{3,5},{0,4,5},{0,6},{1,6},{3,6},{4,6},{0,7},{1,4,7},{5,7},{2,6,7},{0,8},{1,8},{2,8},{4,8},{5,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered129 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 129) T=TwentyFiveEightLow.Case129.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case129.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 129)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case129.support T pos))
  · decide +kernel
theorem completion130 : pairCompletion (big 130)=full 130 := by
  have same : big 130=([{0,1,2,3},{0,4,7},{1,5,7},{2,6,7},{3,4,8},{5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,7},{1,5,7},{2,6,7},{3,4,8},{5,6,8}] [{0,1,2,3},{1,4},{2,4},{0,5},{2,5},{3,5},{4,5},{0,6},{1,6},{3,6},{4,6},{3,7},{0,4,7},{1,5,7},{2,6,7},{0,8},{1,8},{2,8},{3,4,8},{5,6,8},{7,8}]=true
  decide +kernel

theorem recovered130 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 130) T=TwentyFiveEightLow.Case130.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case130.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 130)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case130.support T pos))
  · decide +kernel
theorem completion131 : pairCompletion (big 131)=full 131 := by
  have same : big 131=([{0,1,2,3},{4,5,6},{0,4,7},{1,5,7},{2,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{4,5,6},{0,4,7},{1,5,7},{2,6,8},{3,7,8}] [{0,1,2,3},{1,4},{2,4},{3,4},{0,5},{2,5},{3,5},{0,6},{1,6},{3,6},{4,5,6},{2,7},{0,4,7},{1,5,7},{6,7},{0,8},{1,8},{4,8},{5,8},{2,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered131 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 131) T=TwentyFiveEightLow.Case131.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case131.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 131)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case131.support T pos))
  · decide +kernel
theorem completion132 : pairCompletion (big 132)=full 132 := by
  have same : big 132=([{0,3,4},{4,5,6},{1,3,7},{2,5,7},{0,1,2,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{4,5,6},{1,3,7},{2,5,7},{0,1,2,8},{6,7,8}] [{2,3},{1,4},{2,4},{0,3,4},{0,5},{1,5},{3,5},{0,6},{1,6},{2,6},{3,6},{4,5,6},{0,7},{1,3,7},{4,7},{2,5,7},{0,1,2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered132 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 132) T=TwentyFiveEightLow.Case132.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case132.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 132)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case132.support T pos))
  · decide +kernel
theorem completion133 : pairCompletion (big 133)=full 133 := by
  have same : big 133=([{0,3,4},{3,5,6},{1,5,7},{2,6,7},{0,1,2,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{3,5,6},{1,5,7},{2,6,7},{0,1,2,8},{4,7,8}] [{1,3},{2,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{4,5},{0,6},{1,6},{4,6},{3,5,6},{0,7},{3,7},{1,5,7},{2,6,7},{0,1,2,8},{3,8},{5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered133 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 133) T=TwentyFiveEightLow.Case133.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case133.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 133)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case133.support T pos))
  · decide +kernel
theorem completion134 : pairCompletion (big 134)=full 134 := by
  have same : big 134=([{3,4,6},{0,3,7},{1,4,7},{2,5,7},{0,1,2,8},{5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,6},{0,3,7},{1,4,7},{2,5,7},{0,1,2,8},{5,6,8}] [{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{0,3,7},{1,4,7},{2,5,7},{6,7},{0,1,2,8},{3,8},{4,8},{5,6,8},{7,8}]=true
  decide +kernel

theorem recovered134 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 134) T=TwentyFiveEightLow.Case134.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case134.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 134)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case134.support T pos))
  · decide +kernel
theorem completion135 : pairCompletion (big 135)=full 135 := by
  have same : big 135=([{0,1,2,3},{2,4,5},{3,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{2,4,5},{3,6,7},{4,6,8},{5,7,8}] [{0,1,2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{3,5},{2,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered135 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 135) T=TwentyFiveEightLow.Case135.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case135.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 135)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case135.support T pos))
  · decide +kernel
theorem completion136 : pairCompletion (big 136)=full 136 := by
  have same : big 136=([{0,1,2,3},{2,4,5},{4,6,7},{3,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{2,4,5},{4,6,7},{3,6,8},{5,7,8}] [{0,1,2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{3,5},{2,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{3,7},{4,6,7},{0,8},{1,8},{2,8},{4,8},{3,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered136 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 136) T=TwentyFiveEightLow.Case136.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case136.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 136)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case136.support T pos))
  · decide +kernel
theorem completion137 : pairCompletion (big 137)=full 137 := by
  have same : big 137=([{2,3,4},{3,5,6},{4,5,7},{0,1,2,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{3,5,6},{4,5,7},{0,1,2,8},{6,7,8}] [{0,3},{1,3},{0,4},{1,4},{2,3,4},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{4,6},{3,5,6},{0,7},{1,7},{2,7},{3,7},{4,5,7},{0,1,2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered137 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 137) T=TwentyFiveEightLow.Case137.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case137.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 137)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case137.support T pos))
  · decide +kernel
theorem completion138 : pairCompletion (big 138)=full 138 := by
  have same : big 138=([{1,3,4},{2,5,6},{3,5,7},{4,6,7},{0,1,2,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4},{2,5,6},{3,5,7},{4,6,7},{0,1,2,8}] [{0,3},{2,3},{0,4},{2,4},{1,3,4},{0,5},{1,5},{4,5},{0,6},{1,6},{3,6},{2,5,6},{0,7},{1,7},{2,7},{3,5,7},{4,6,7},{0,1,2,8},{3,8},{4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered138 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 138) T=TwentyFiveEightLow.Case138.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case138.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 138)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case138.support T pos))
  · decide +kernel
theorem completion139 : pairCompletion (big 139)=full 139 := by
  have same : big 139=([{0,1,2,3},{0,4,6},{2,5,6},{3,4,7},{1,5,7},{2,4,8},{3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,6},{2,5,6},{3,4,7},{1,5,7},{2,4,8},{3,5,8},{6,7,8}] [{0,1,2,3},{1,4},{0,5},{4,5},{1,6},{3,6},{0,4,6},{2,5,6},{0,7},{2,7},{3,4,7},{1,5,7},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered139 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 139) T=TwentyFiveEightLow.Case139.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case139.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 139)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case139.support T pos))
  · decide +kernel
theorem completion140 : pairCompletion (big 140)=full 140 := by
  have same : big 140=([{0,1,2,3},{0,4,5},{2,5,6},{2,4,7},{3,6,7},{3,4,8},{1,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,5},{2,5,6},{2,4,7},{3,6,7},{3,4,8},{1,6,8},{5,7,8}] [{0,1,2,3},{1,4},{1,5},{3,5},{0,4,5},{0,6},{4,6},{2,5,6},{0,7},{1,7},{2,4,7},{3,6,7},{0,8},{2,8},{3,4,8},{1,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered140 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 140) T=TwentyFiveEightLow.Case140.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case140.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 140)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case140.support T pos))
  · decide +kernel
theorem completion141 : pairCompletion (big 141)=full 141 := by
  have same : big 141=([{0,1,2,3},{0,4,5},{2,4,6},{3,4,7},{5,6,7},{3,5,8},{1,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,5},{2,4,6},{3,4,7},{5,6,7},{3,5,8},{1,6,8},{2,7,8}] [{0,1,2,3},{1,4},{1,5},{2,5},{0,4,5},{0,6},{3,6},{2,4,6},{0,7},{1,7},{3,4,7},{5,6,7},{0,8},{4,8},{3,5,8},{1,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered141 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 141) T=TwentyFiveEightLow.Case141.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case141.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 141)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case141.support T pos))
  · decide +kernel
theorem completion142 : pairCompletion (big 142)=full 142 := by
  have same : big 142=([{0,3,4},{2,3,5},{1,5,6},{2,4,7},{3,6,7},{0,1,2,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{2,3,5},{1,5,6},{2,4,7},{3,6,7},{0,1,2,8},{4,6,8},{5,7,8}] [{1,3},{1,4},{0,3,4},{0,5},{2,3,5},{4,5},{0,6},{2,6},{1,5,6},{0,7},{1,7},{2,4,7},{3,6,7},{0,1,2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered142 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 142) T=TwentyFiveEightLow.Case142.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case142.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 142)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case142.support T pos))
  · decide +kernel
theorem completion143 : pairCompletion (big 143)=full 143 := by
  have same : big 143=([{0,3,4},{1,3,5},{1,4,6},{2,5,6},{2,3,7},{4,5,7},{0,1,2,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{1,4,6},{2,5,6},{2,3,7},{4,5,7},{0,1,2,8},{6,7,8}] [{2,4},{0,3,4},{0,5},{1,3,5},{0,6},{3,6},{1,4,6},{2,5,6},{0,7},{1,7},{2,3,7},{4,5,7},{0,1,2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered143 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 143) T=TwentyFiveEightLow.Case143.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case143.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 143)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case143.support T pos))
  · decide +kernel
theorem completion144 : pairCompletion (big 144)=full 144 := by
  have same : big 144=([{0,1,2,3},{0,4,6},{1,5,7},{2,4,8},{3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,6},{1,5,7},{2,4,8},{3,5,8},{6,7,8}] [{0,1,2,3},{1,4},{3,4},{0,5},{2,5},{4,5},{1,6},{2,6},{3,6},{0,4,6},{5,6},{0,7},{2,7},{3,7},{4,7},{1,5,7},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered144 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 144) T=TwentyFiveEightLow.Case144.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case144.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 144)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case144.support T pos))
  · decide +kernel
theorem completion145 : pairCompletion (big 145)=full 145 := by
  have same : big 145=([{0,1,2,3},{0,4,5},{1,4,7},{2,6,7},{3,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,5},{1,4,7},{2,6,7},{3,6,8},{5,7,8}] [{0,1,2,3},{2,4},{3,4},{1,5},{2,5},{3,5},{0,4,5},{0,6},{1,6},{4,6},{5,6},{0,7},{3,7},{1,4,7},{2,6,7},{0,8},{1,8},{2,8},{4,8},{3,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered145 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 145) T=TwentyFiveEightLow.Case145.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case145.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 145)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case145.support T pos))
  · decide +kernel
theorem completion146 : pairCompletion (big 146)=full 146 := by
  have same : big 146=([{0,1,2,3},{0,4,5},{1,4,7},{5,6,7},{2,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,5},{1,4,7},{5,6,7},{2,6,8},{3,7,8}] [{0,1,2,3},{2,4},{3,4},{1,5},{2,5},{3,5},{0,4,5},{0,6},{1,6},{3,6},{4,6},{0,7},{2,7},{1,4,7},{5,6,7},{0,8},{1,8},{4,8},{5,8},{2,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered146 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 146) T=TwentyFiveEightLow.Case146.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case146.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 146)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case146.support T pos))
  · decide +kernel
theorem completion147 : pairCompletion (big 147)=full 147 := by
  have same : big 147=([{0,3,4},{1,5,6},{2,3,7},{4,5,7},{0,1,2,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,5,6},{2,3,7},{4,5,7},{0,1,2,8},{6,7,8}] [{1,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{3,5},{0,6},{2,6},{3,6},{4,6},{1,5,6},{0,7},{1,7},{2,3,7},{4,5,7},{0,1,2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered147 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 147) T=TwentyFiveEightLow.Case147.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case147.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 147)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case147.support T pos))
  · decide +kernel
theorem completion148 : pairCompletion (big 148)=full 148 := by
  have same : big 148=([{0,3,4},{1,3,7},{2,5,7},{4,6,7},{0,1,2,8},{5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,7},{2,5,7},{4,6,7},{0,1,2,8},{5,6,8}] [{2,3},{1,4},{2,4},{0,3,4},{0,5},{1,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{0,7},{1,3,7},{2,5,7},{4,6,7},{0,1,2,8},{3,8},{4,8},{5,6,8},{7,8}]=true
  decide +kernel

theorem recovered148 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 148) T=TwentyFiveEightLow.Case148.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case148.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 148)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case148.support T pos))
  · decide +kernel
theorem completion149 : pairCompletion (big 149)=full 149 := by
  have same : big 149=([{0,1,2,3},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{2,4,8},{3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{2,4,8},{3,5,8},{6,7,8}] [{0,1,2,3},{0,4},{0,5},{4,5},{0,6},{3,6},{1,4,6},{2,5,6},{0,7},{2,7},{3,4,7},{1,5,7},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered149 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 149) T=TwentyFiveEightLow.Case149.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case149.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 149)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case149.support T pos))
  · decide +kernel
theorem completion150 : pairCompletion (big 150)=full 150 := by
  have same : big 150=([{0,1,2,3},{1,4,5},{2,4,6},{3,4,7},{5,6,7},{2,5,8},{3,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{1,4,5},{2,4,6},{3,4,7},{5,6,7},{2,5,8},{3,6,8},{1,7,8}] [{0,1,2,3},{0,4},{0,5},{3,5},{1,4,5},{0,6},{1,6},{2,4,6},{0,7},{2,7},{3,4,7},{5,6,7},{0,8},{4,8},{2,5,8},{3,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered150 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 150) T=TwentyFiveEightLow.Case150.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case150.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 150)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case150.support T pos))
  · decide +kernel
theorem completion151 : pairCompletion (big 151)=full 151 := by
  have same : big 151=([{1,3,4},{2,3,5},{2,4,6},{1,5,7},{3,6,7},{0,1,2,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4},{2,3,5},{2,4,6},{1,5,7},{3,6,7},{0,1,2,8},{5,6,8},{4,7,8}] [{0,3},{0,4},{1,3,4},{0,5},{2,3,5},{4,5},{0,6},{1,6},{2,4,6},{0,7},{2,7},{1,5,7},{3,6,7},{0,1,2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered151 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 151) T=TwentyFiveEightLow.Case151.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case151.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 151)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case151.support T pos))
  · decide +kernel
theorem completion152 : pairCompletion (big 152)=full 152 := by
  have same : big 152=([{0,3,5},{1,4,5},{1,3,6},{2,4,6},{2,3,7},{0,4,7},{5,6,7},{0,1,2,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,5},{1,4,5},{1,3,6},{2,4,6},{2,3,7},{0,4,7},{5,6,7},{0,1,2,8}] [{3,4},{2,5},{0,3,5},{1,4,5},{0,6},{1,3,6},{2,4,6},{1,7},{2,3,7},{0,4,7},{5,6,7},{0,1,2,8},{3,8},{4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered152 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 152) T=TwentyFiveEightLow.Case152.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case152.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 152)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case152.support T pos))
  · decide +kernel
theorem completion153 : pairCompletion (big 153)=full 153 := by
  have same : big 153=([{0,1,2,3},{0,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}] [{0,1,2,3},{0,4},{1,4},{2,4},{3,4},{2,5},{3,5},{1,6},{3,6},{0,5,6},{0,7},{2,7},{1,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered153 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 153) T=TwentyFiveEightLow.Case153.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case153.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 153)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case153.support T pos))
  · decide +kernel
theorem completion154 : pairCompletion (big 154)=full 154 := by
  have same : big 154=([{0,1,2,3},{0,4,5},{1,4,6},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,5},{1,4,6},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] [{0,1,2,3},{2,4},{3,4},{1,5},{3,5},{0,4,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered154 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 154) T=TwentyFiveEightLow.Case154.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case154.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 154)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case154.support T pos))
  · decide +kernel
theorem completion155 : pairCompletion (big 155)=full 155 := by
  have same : big 155=([{0,4,5},{1,4,6},{3,5,6},{3,4,7},{2,5,7},{0,1,2,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{1,4,6},{3,5,6},{3,4,7},{2,5,7},{0,1,2,8},{6,7,8}] [{0,3},{1,3},{2,3},{2,4},{1,5},{0,4,5},{0,6},{2,6},{1,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{0,1,2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered155 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 155) T=TwentyFiveEightLow.Case155.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case155.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 155)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case155.support T pos))
  · decide +kernel
theorem completion156 : pairCompletion (big 156)=full 156 := by
  have same : big 156=([{0,1,2,3},{4,5,6},{1,4,7},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{1,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{4,5,6},{1,4,7},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{1,6,8},{0,7,8}] [{0,1,2,3},{0,4},{3,4},{0,5},{1,5},{0,6},{2,6},{4,5,6},{1,4,7},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{1,6,8},{0,7,8}]=true
  decide +kernel

theorem recovered156 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 156) T=TwentyFiveEightLow.Case156.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case156.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 156)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case156.support T pos))
  · decide +kernel
theorem completion157 : pairCompletion (big 157)=full 157 := by
  have same : big 157=([{0,1,2,3},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,1,2,3},{0,4},{2,4},{0,5},{3,5},{1,4,6},{2,5,6},{3,4,7},{1,5,7},{0,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered157 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 157) T=TwentyFiveEightLow.Case157.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case157.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 157)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case157.support T pos))
  · decide +kernel
theorem completion158 : pairCompletion (big 158)=full 158 := by
  have same : big 158=([{3,4,5},{1,3,6},{2,4,6},{2,3,7},{1,5,7},{0,6,7},{0,1,2,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{1,3,6},{2,4,6},{2,3,7},{1,5,7},{0,6,7},{0,1,2,8},{5,6,8},{4,7,8}] [{0,3},{0,4},{1,4},{0,5},{2,5},{3,4,5},{1,3,6},{2,4,6},{2,3,7},{1,5,7},{0,6,7},{0,1,2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered158 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 158) T=TwentyFiveEightLow.Case158.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case158.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 158)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case158.support T pos))
  · decide +kernel
theorem completion159 : pairCompletion (big 159)=full 159 := by
  have same : big 159=([{3,4,5},{0,3,6},{1,4,6},{2,5,6},{1,3,7},{2,4,7},{0,5,7},{0,1,2,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,3,6},{1,4,6},{2,5,6},{1,3,7},{2,4,7},{0,5,7},{0,1,2,8},{6,7,8}] [{2,3},{0,4},{1,5},{3,4,5},{0,3,6},{1,4,6},{2,5,6},{1,3,7},{2,4,7},{0,5,7},{0,1,2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered159 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 159) T=TwentyFiveEightLow.Case159.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case159.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 159)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case159.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
