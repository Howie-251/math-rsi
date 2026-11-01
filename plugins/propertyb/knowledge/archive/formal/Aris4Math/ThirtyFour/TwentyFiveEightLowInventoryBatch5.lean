import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion160 : pairCompletion (big 160)=full 160 := by
  have same : big 160=([{0,1,2,3},{0,4,5,6},{1,4,7},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{1,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,5,6},{1,4,7},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{1,6,8}] [{0,1,2,3},{3,4},{1,5},{2,6},{0,4,5,6},{0,7},{1,4,7},{2,5,7},{3,6,7},{0,8},{2,4,8},{3,5,8},{1,6,8},{7,8}]=true
  decide +kernel

theorem recovered160 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 160) T=TwentyFiveEightLow.Case160.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case160.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 160)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case160.support T pos))
  · decide +kernel
theorem completion161 : pairCompletion (big 161)=full 161 := by
  have same : big 161=([{0,1,4,5},{1,2,6},{3,4,6},{1,3,7},{2,5,7},{0,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{1,2,6},{3,4,6},{1,3,7},{2,5,7},{0,2,3,8},{5,6,8},{4,7,8}] [{2,4},{3,5},{0,1,4,5},{0,6},{1,2,6},{3,4,6},{0,7},{1,3,7},{2,5,7},{6,7},{1,8},{0,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered161 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 161) T=TwentyFiveEightLow.Case161.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case161.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 161)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case161.support T pos))
  · decide +kernel
theorem completion162 : pairCompletion (big 162)=full 162 := by
  have same : big 162=([{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{0,3,4,8},{1,2,5,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{0,3,4,8},{1,2,5,8}] [{1,3},{2,4},{0,5},{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{6,7},{0,3,4,8},{1,2,5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered162 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 162) T=TwentyFiveEightLow.Case162.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case162.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 162)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case162.support T pos))
  · decide +kernel
theorem completion163 : pairCompletion (big 163)=full 163 := by
  have same : big 163=([{0,1,2,3},{0,4,5,6},{1,4,7},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{1,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{0,4,5,6},{1,4,7},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{1,6,8},{0,7,8}] [{0,1,2,3},{3,4},{1,5},{2,6},{0,4,5,6},{1,4,7},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{1,6,8},{0,7,8}]=true
  decide +kernel

theorem recovered163 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 163) T=TwentyFiveEightLow.Case163.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case163.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 163)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case163.support T pos))
  · decide +kernel
theorem completion164 : pairCompletion (big 164)=full 164 := by
  have same : big 164=([{0,1,4,5},{1,2,6},{3,4,6},{1,3,7},{2,5,7},{0,6,7},{0,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{1,2,6},{3,4,6},{1,3,7},{2,5,7},{0,6,7},{0,2,3,8},{5,6,8},{4,7,8}] [{2,4},{3,5},{0,1,4,5},{1,2,6},{3,4,6},{1,3,7},{2,5,7},{0,6,7},{1,8},{0,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered164 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 164) T=TwentyFiveEightLow.Case164.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case164.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 164)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case164.support T pos))
  · decide +kernel
theorem completion165 : pairCompletion (big 165)=full 165 := by
  have same : big 165=([{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}] [{1,3},{2,4},{0,5},{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered165 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 165) T=TwentyFiveEightLow.Case165.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case165.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 165)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case165.support T pos))
  · decide +kernel
theorem completion166 : pairCompletion (big 166)=full 166 := by
  have same : big 166=([{0,1,2,4},{1,3,5,6},{2,3,7},{4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,4},{1,3,5,6},{2,3,7},{4,5,8},{6,7,8}] [{0,3},{0,1,2,4},{3,4},{0,5},{2,5},{0,6},{2,6},{4,6},{1,3,5,6},{0,7},{1,7},{2,3,7},{4,7},{5,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered166 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 166) T=TwentyFiveEightLow.Case166.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case166.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 166)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case166.support T pos))
  · decide +kernel
theorem completion167 : pairCompletion (big 167)=full 167 := by
  have same : big 167=([{0,1,2,3},{2,4,6},{3,5,7},{1,4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{2,4,6},{3,5,7},{1,4,5,8},{6,7,8}] [{0,1,2,3},{0,4},{3,4},{0,5},{2,5},{0,6},{1,6},{3,6},{2,4,6},{5,6},{0,7},{1,7},{2,7},{4,7},{3,5,7},{0,8},{2,8},{3,8},{1,4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered167 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 167) T=TwentyFiveEightLow.Case167.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case167.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 167)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case167.support T pos))
  · decide +kernel
theorem completion168 : pairCompletion (big 168)=full 168 := by
  have same : big 168=([{0,1,2,5},{2,3,6},{4,6,7},{1,3,4,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{2,3,6},{4,6,7},{1,3,4,8},{5,7,8}] [{0,3},{0,4},{2,4},{0,1,2,5},{3,5},{4,5},{0,6},{1,6},{2,3,6},{5,6},{0,7},{1,7},{2,7},{3,7},{4,6,7},{0,8},{2,8},{1,3,4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered168 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 168) T=TwentyFiveEightLow.Case168.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case168.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 168)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case168.support T pos))
  · decide +kernel
theorem completion169 : pairCompletion (big 169)=full 169 := by
  have same : big 169=([{1,3,4,5},{2,3,6},{4,6,7},{0,1,2,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4,5},{2,3,6},{4,6,7},{0,1,2,8},{5,7,8}] [{0,3},{0,4},{2,4},{0,5},{2,5},{1,3,4,5},{0,6},{1,6},{2,3,6},{5,6},{0,7},{1,7},{2,7},{3,7},{4,6,7},{0,1,2,8},{3,8},{4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered169 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 169) T=TwentyFiveEightLow.Case169.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case169.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 169)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case169.support T pos))
  · decide +kernel
theorem completion170 : pairCompletion (big 170)=full 170 := by
  have same : big 170=([{1,3,6},{2,4,7},{5,6,7},{0,1,2,8},{3,4,5,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,6},{2,4,7},{5,6,7},{0,1,2,8},{3,4,5,8}] [{0,3},{2,3},{0,4},{1,4},{0,5},{1,5},{2,5},{0,6},{2,6},{1,3,6},{4,6},{0,7},{1,7},{3,7},{2,4,7},{5,6,7},{0,1,2,8},{3,4,5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered170 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 170) T=TwentyFiveEightLow.Case170.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case170.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 170)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case170.support T pos))
  · decide +kernel
theorem completion171 : pairCompletion (big 171)=full 171 := by
  have same : big 171=([{0,1,2,5},{1,3,6},{2,4,7},{5,6,7},{0,3,4,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{1,3,6},{2,4,7},{5,6,7},{0,3,4,8}] [{2,3},{1,4},{0,1,2,5},{3,5},{4,5},{0,6},{2,6},{1,3,6},{4,6},{0,7},{1,7},{3,7},{2,4,7},{5,6,7},{1,8},{2,8},{0,3,4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered171 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 171) T=TwentyFiveEightLow.Case171.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case171.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 171)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case171.support T pos))
  · decide +kernel
theorem completion172 : pairCompletion (big 172)=full 172 := by
  have same : big 172=([{0,1,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] [{0,1,2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{0,7},{2,7},{1,4,7},{5,6,7},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered172 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 172) T=TwentyFiveEightLow.Case172.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case172.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 172)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case172.support T pos))
  · decide +kernel
theorem completion173 : pairCompletion (big 173)=full 173 := by
  have same : big 173=([{0,1,2,3},{1,4,6},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{1,4,6},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] [{0,1,2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{3,5},{4,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered173 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 173) T=TwentyFiveEightLow.Case173.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case173.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 173)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case173.support T pos))
  · decide +kernel
theorem completion174 : pairCompletion (big 174)=full 174 := by
  have same : big 174=([{0,1,2,3},{1,4,6},{4,5,7},{2,6,7},{5,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{1,4,6},{4,5,7},{2,6,7},{5,6,8},{3,7,8}] [{0,1,2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{2,5},{3,5},{0,6},{3,6},{1,4,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,8},{1,8},{2,8},{4,8},{5,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered174 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 174) T=TwentyFiveEightLow.Case174.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case174.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 174)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case174.support T pos))
  · decide +kernel
theorem completion175 : pairCompletion (big 175)=full 175 := by
  have same : big 175=([{1,3,6},{4,5,6},{2,4,7},{3,5,7},{0,1,2,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,6},{4,5,6},{2,4,7},{3,5,7},{0,1,2,8},{6,7,8}] [{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{0,6},{2,6},{1,3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,1,2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered175 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 175) T=TwentyFiveEightLow.Case175.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case175.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 175)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case175.support T pos))
  · decide +kernel
theorem completion176 : pairCompletion (big 176)=full 176 := by
  have same : big 176=([{1,3,6},{4,5,6},{3,4,7},{2,6,7},{0,1,2,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,6},{4,5,6},{3,4,7},{2,6,7},{0,1,2,8},{5,7,8}] [{0,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,5},{0,6},{1,3,6},{4,5,6},{0,7},{1,7},{3,4,7},{2,6,7},{0,1,2,8},{3,8},{4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered176 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 176) T=TwentyFiveEightLow.Case176.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case176.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 176)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case176.support T pos))
  · decide +kernel
theorem completion177 : pairCompletion (big 177)=full 177 := by
  have same : big 177=([{0,3,6},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{0,1,2,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,6},{4,5,6},{1,4,7},{3,5,7},{2,6,7},{0,1,2,8}] [{1,3},{2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{2,5},{1,6},{0,3,6},{4,5,6},{0,7},{1,4,7},{3,5,7},{2,6,7},{0,1,2,8},{3,8},{4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered177 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 177) T=TwentyFiveEightLow.Case177.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case177.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 177)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case177.support T pos))
  · decide +kernel
theorem completion178 : pairCompletion (big 178)=full 178 := by
  have same : big 178=([{0,1,2,3},{4,5,6,7},{0,4,8},{1,5,8},{2,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{4,5,6,7},{0,4,8},{1,5,8},{2,6,8},{3,7,8}] [{0,1,2,3},{1,4},{2,4},{3,4},{0,5},{2,5},{3,5},{0,6},{1,6},{3,6},{0,7},{1,7},{2,7},{4,5,6,7},{0,4,8},{1,5,8},{2,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered178 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 178) T=TwentyFiveEightLow.Case178.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case178.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 178)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case178.support T pos))
  · decide +kernel
theorem completion179 : pairCompletion (big 179)=full 179 := by
  have same : big 179=([{0,1,2,6},{0,3,7},{1,4,7},{2,5,7},{3,4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,6},{0,3,7},{1,4,7},{2,5,7},{3,4,5,8},{6,7,8}] [{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{0,1,2,6},{3,6},{4,6},{5,6},{0,3,7},{1,4,7},{2,5,7},{0,8},{1,8},{2,8},{3,4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered179 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 179) T=TwentyFiveEightLow.Case179.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case179.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 179)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case179.support T pos))
  · decide +kernel
theorem completion180 : pairCompletion (big 180)=full 180 := by
  have same : big 180=([{0,1,4},{2,5,6},{3,5,7},{4,6,7},{2,3,8},{4,5,8},{0,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{2,5,6},{3,5,7},{4,6,7},{2,3,8},{4,5,8},{0,6,8},{1,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,1,4},{2,4},{3,4},{0,5},{1,5},{1,6},{3,6},{2,5,6},{0,7},{2,7},{3,5,7},{4,6,7},{2,3,8},{4,5,8},{0,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered180 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 180) T=TwentyFiveEightLow.Case180.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case180.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 180)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case180.support T pos))
  · decide +kernel
theorem completion181 : pairCompletion (big 181)=full 181 := by
  have same : big 181=([{0,1,4},{2,5,6},{2,3,7},{0,5,7},{4,6,7},{4,5,8},{3,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{2,5,6},{2,3,7},{0,5,7},{4,6,7},{4,5,8},{3,6,8},{1,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,1,4},{2,4},{3,4},{1,5},{3,5},{0,6},{1,6},{2,5,6},{2,3,7},{0,5,7},{4,6,7},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered181 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 181) T=TwentyFiveEightLow.Case181.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case181.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 181)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case181.support T pos))
  · decide +kernel
theorem completion182 : pairCompletion (big 182)=full 182 := by
  have same : big 182=([{0,1,4},{4,5,6},{2,3,7},{0,5,7},{1,6,7},{2,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{4,5,6},{2,3,7},{0,5,7},{1,6,7},{2,5,8},{3,6,8},{4,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,1,4},{2,4},{3,4},{1,5},{3,5},{0,6},{2,6},{4,5,6},{2,3,7},{0,5,7},{1,6,7},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered182 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 182) T=TwentyFiveEightLow.Case182.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case182.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 182)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case182.support T pos))
  · decide +kernel
theorem completion183 : pairCompletion (big 183)=full 183 := by
  have same : big 183=([{0,4,5},{1,4,6},{0,1,7},{2,5,7},{3,6,7},{2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{1,4,6},{0,1,7},{2,5,7},{3,6,7},{2,3,8},{5,6,8},{4,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,4},{3,4},{1,5},{3,5},{0,4,5},{0,6},{2,6},{1,4,6},{0,1,7},{2,5,7},{3,6,7},{0,8},{1,8},{2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered183 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 183) T=TwentyFiveEightLow.Case183.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case183.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 183)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case183.support T pos))
  · decide +kernel
theorem completion184 : pairCompletion (big 184)=full 184 := by
  have same : big 184=([{0,1,3},{2,4,5},{3,4,6},{0,4,7},{3,5,7},{1,6,7},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{2,4,5},{3,4,6},{0,4,7},{3,5,7},{1,6,7},{5,6,8},{2,7,8}] [{0,2},{1,2},{0,1,3},{2,3},{1,4},{0,5},{1,5},{2,4,5},{0,6},{2,6},{3,4,6},{0,4,7},{3,5,7},{1,6,7},{0,8},{1,8},{3,8},{4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered184 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 184) T=TwentyFiveEightLow.Case184.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case184.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 184)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case184.support T pos))
  · decide +kernel
theorem completion185 : pairCompletion (big 185)=full 185 := by
  have same : big 185=([{0,3,4},{1,3,5},{4,5,6},{0,1,7},{2,4,7},{3,6,7},{2,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{4,5,6},{0,1,7},{2,4,7},{3,6,7},{2,6,8},{5,7,8}] [{0,2},{1,2},{2,3},{1,4},{0,3,4},{0,5},{2,5},{1,3,5},{0,6},{1,6},{4,5,6},{0,1,7},{2,4,7},{3,6,7},{0,8},{1,8},{3,8},{4,8},{2,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered185 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 185) T=TwentyFiveEightLow.Case185.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case185.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 185)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case185.support T pos))
  · decide +kernel
theorem completion186 : pairCompletion (big 186)=full 186 := by
  have same : big 186=([{0,1,4},{3,5,6},{2,5,7},{4,6,7},{0,2,8},{4,5,8},{1,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{3,5,6},{2,5,7},{4,6,7},{0,2,8},{4,5,8},{1,6,8},{3,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,1,4},{2,4},{3,4},{0,5},{1,5},{0,6},{2,6},{3,5,6},{0,7},{1,7},{2,5,7},{4,6,7},{0,2,8},{4,5,8},{1,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered186 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 186) T=TwentyFiveEightLow.Case186.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case186.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 186)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case186.support T pos))
  · decide +kernel
theorem completion187 : pairCompletion (big 187)=full 187 := by
  have same : big 187=([{0,1,4},{3,5,6},{0,2,7},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{3,5,6},{0,2,7},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,1,4},{2,4},{3,4},{0,5},{2,5},{0,6},{1,6},{3,5,6},{0,2,7},{1,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered187 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 187) T=TwentyFiveEightLow.Case187.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case187.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 187)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case187.support T pos))
  · decide +kernel
theorem completion188 : pairCompletion (big 188)=full 188 := by
  have same : big 188=([{0,1,4},{2,5,6},{0,2,7},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{2,5,6},{0,2,7},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{1,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,1,4},{2,4},{3,4},{0,5},{1,5},{0,6},{1,6},{2,5,6},{0,2,7},{3,5,7},{4,6,7},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered188 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 188) T=TwentyFiveEightLow.Case188.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case188.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 188)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case188.support T pos))
  · decide +kernel
theorem completion189 : pairCompletion (big 189)=full 189 := by
  have same : big 189=([{0,1,4},{4,5,6},{0,2,7},{1,5,7},{3,6,7},{3,5,8},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{4,5,6},{0,2,7},{1,5,7},{3,6,7},{3,5,8},{2,6,8},{4,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,1,4},{2,4},{3,4},{0,5},{2,5},{0,6},{1,6},{4,5,6},{0,2,7},{1,5,7},{3,6,7},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered189 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 189) T=TwentyFiveEightLow.Case189.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case189.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 189)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case189.support T pos))
  · decide +kernel
theorem completion190 : pairCompletion (big 190)=full 190 := by
  have same : big 190=([{1,4,5},{3,4,6},{0,1,7},{3,5,7},{2,6,7},{0,2,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,5},{3,4,6},{0,1,7},{3,5,7},{2,6,7},{0,2,8},{5,6,8},{4,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,4},{2,4},{0,5},{2,5},{1,4,5},{0,6},{1,6},{3,4,6},{0,1,7},{3,5,7},{2,6,7},{1,8},{0,2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered190 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 190) T=TwentyFiveEightLow.Case190.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case190.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 190)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case190.support T pos))
  · decide +kernel
theorem completion191 : pairCompletion (big 191)=full 191 := by
  have same : big 191=([{0,1,3},{2,4,5},{3,4,6},{0,2,7},{3,5,7},{1,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{2,4,5},{3,4,6},{0,2,7},{3,5,7},{1,6,7},{5,6,8},{4,7,8}] [{1,2},{0,1,3},{2,3},{0,4},{1,4},{0,5},{1,5},{2,4,5},{0,6},{2,6},{3,4,6},{0,2,7},{3,5,7},{1,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered191 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 191) T=TwentyFiveEightLow.Case191.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case191.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 191)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case191.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
