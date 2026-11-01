import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion192 : pairCompletion (big 192)=full 192 := by
  have same : big 192=([{0,1,3},{2,4,5},{3,4,6},{0,4,7},{3,5,7},{2,6,7},{5,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{2,4,5},{3,4,6},{0,4,7},{3,5,7},{2,6,7},{5,6,8},{1,7,8}] [{0,2},{1,2},{0,1,3},{2,3},{1,4},{0,5},{1,5},{2,4,5},{0,6},{1,6},{3,4,6},{0,4,7},{3,5,7},{2,6,7},{0,8},{2,8},{3,8},{4,8},{5,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered192 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 192) T=TwentyFiveEightLow.Case192.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case192.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 192)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case192.support T pos))
  · decide +kernel
theorem completion193 : pairCompletion (big 193)=full 193 := by
  have same : big 193=([{0,3,4},{2,3,5},{4,5,6},{0,1,7},{2,4,7},{3,6,7},{1,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{2,3,5},{4,5,6},{0,1,7},{2,4,7},{3,6,7},{1,6,8},{5,7,8}] [{0,2},{1,2},{1,3},{1,4},{0,3,4},{0,5},{1,5},{2,3,5},{0,6},{2,6},{4,5,6},{0,1,7},{2,4,7},{3,6,7},{0,8},{2,8},{3,8},{4,8},{1,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered193 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 193) T=TwentyFiveEightLow.Case193.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case193.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 193)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case193.support T pos))
  · decide +kernel
theorem completion194 : pairCompletion (big 194)=full 194 := by
  have same : big 194=([{0,3,4},{1,3,5},{4,5,6},{2,4,7},{0,5,7},{3,6,7},{2,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{4,5,6},{2,4,7},{0,5,7},{3,6,7},{2,6,8},{1,7,8}] [{0,1},{0,2},{1,2},{2,3},{1,4},{0,3,4},{2,5},{1,3,5},{0,6},{1,6},{4,5,6},{2,4,7},{0,5,7},{3,6,7},{0,8},{3,8},{4,8},{5,8},{2,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered194 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 194) T=TwentyFiveEightLow.Case194.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case194.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 194)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case194.support T pos))
  · decide +kernel
theorem completion195 : pairCompletion (big 195)=full 195 := by
  have same : big 195=([{0,1,4},{3,5,6},{2,5,7},{4,6,7},{2,4,8},{0,5,8},{1,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{3,5,6},{2,5,7},{4,6,7},{2,4,8},{0,5,8},{1,6,8},{3,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{0,1,4},{3,4},{1,5},{4,5},{0,6},{2,6},{3,5,6},{0,7},{1,7},{2,5,7},{4,6,7},{2,4,8},{0,5,8},{1,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered195 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 195) T=TwentyFiveEightLow.Case195.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case195.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 195)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case195.support T pos))
  · decide +kernel
theorem completion196 : pairCompletion (big 196)=full 196 := by
  have same : big 196=([{0,1,4},{2,5,6},{3,4,7},{0,5,7},{1,6,7},{3,5,8},{4,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{2,5,6},{3,4,7},{0,5,7},{1,6,7},{3,5,8},{4,6,8},{2,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{0,1,4},{2,4},{1,5},{4,5},{0,6},{3,6},{2,5,6},{3,4,7},{0,5,7},{1,6,7},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered196 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 196) T=TwentyFiveEightLow.Case196.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case196.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 196)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case196.support T pos))
  · decide +kernel
theorem completion197 : pairCompletion (big 197)=full 197 := by
  have same : big 197=([{0,1,4},{2,5,6},{2,4,7},{0,5,7},{3,6,7},{3,5,8},{4,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{2,5,6},{2,4,7},{0,5,7},{3,6,7},{3,5,8},{4,6,8},{1,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{0,1,4},{3,4},{1,5},{4,5},{0,6},{1,6},{2,5,6},{2,4,7},{0,5,7},{3,6,7},{0,8},{2,8},{3,5,8},{4,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered197 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 197) T=TwentyFiveEightLow.Case197.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case197.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 197)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case197.support T pos))
  · decide +kernel
theorem completion198 : pairCompletion (big 198)=full 198 := by
  have same : big 198=([{0,1,4},{4,5,6},{2,4,7},{0,5,7},{3,6,7},{3,5,8},{2,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{4,5,6},{2,4,7},{0,5,7},{3,6,7},{3,5,8},{2,6,8},{1,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{0,1,4},{3,4},{1,5},{2,5},{0,6},{1,6},{4,5,6},{2,4,7},{0,5,7},{3,6,7},{0,8},{4,8},{3,5,8},{2,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered198 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 198) T=TwentyFiveEightLow.Case198.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case198.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 198)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case198.support T pos))
  · decide +kernel
theorem completion199 : pairCompletion (big 199)=full 199 := by
  have same : big 199=([{2,4,5},{3,4,6},{0,4,7},{1,5,7},{2,6,7},{0,1,8},{5,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{3,4,6},{0,4,7},{1,5,7},{2,6,7},{0,1,8},{5,6,8},{3,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{1,4},{0,5},{3,5},{2,4,5},{0,6},{1,6},{3,4,6},{0,4,7},{1,5,7},{2,6,7},{0,1,8},{2,8},{4,8},{5,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered199 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 199) T=TwentyFiveEightLow.Case199.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case199.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 199)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case199.support T pos))
  · decide +kernel
theorem completion200 : pairCompletion (big 200)=full 200 := by
  have same : big 200=([{0,1,3},{2,4,5},{3,5,6},{2,3,7},{0,4,7},{1,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{2,4,5},{3,5,6},{2,3,7},{0,4,7},{1,6,7},{4,6,8},{5,7,8}] [{0,2},{1,2},{0,1,3},{1,4},{3,4},{0,5},{1,5},{2,4,5},{0,6},{2,6},{3,5,6},{2,3,7},{0,4,7},{1,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered200 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 200) T=TwentyFiveEightLow.Case200.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case200.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 200)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case200.support T pos))
  · decide +kernel
theorem completion201 : pairCompletion (big 201)=full 201 := by
  have same : big 201=([{0,1,3},{2,4,5},{3,4,6},{0,4,7},{1,5,7},{2,6,7},{5,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{2,4,5},{3,4,6},{0,4,7},{1,5,7},{2,6,7},{5,6,8},{3,7,8}] [{0,2},{1,2},{0,1,3},{2,3},{1,4},{0,5},{3,5},{2,4,5},{0,6},{1,6},{3,4,6},{0,4,7},{1,5,7},{2,6,7},{0,8},{1,8},{2,8},{4,8},{5,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered201 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 201) T=TwentyFiveEightLow.Case201.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case201.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 201)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case201.support T pos))
  · decide +kernel
theorem completion202 : pairCompletion (big 202)=full 202 := by
  have same : big 202=([{0,3,4},{1,3,5},{4,5,6},{2,3,7},{1,4,7},{0,6,7},{2,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{4,5,6},{2,3,7},{1,4,7},{0,6,7},{2,6,8},{5,7,8}] [{0,1},{0,2},{1,2},{2,4},{0,3,4},{0,5},{2,5},{1,3,5},{1,6},{3,6},{4,5,6},{2,3,7},{1,4,7},{0,6,7},{0,8},{1,8},{3,8},{4,8},{2,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered202 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 202) T=TwentyFiveEightLow.Case202.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case202.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 202)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case202.support T pos))
  · decide +kernel
theorem completion203 : pairCompletion (big 203)=full 203 := by
  have same : big 203=([{1,3,4},{0,3,5},{4,5,6},{0,4,7},{2,5,7},{1,6,7},{2,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4},{0,3,5},{4,5,6},{0,4,7},{2,5,7},{1,6,7},{2,6,8},{3,7,8}] [{0,1},{0,2},{1,2},{2,3},{2,4},{1,3,4},{1,5},{0,3,5},{0,6},{3,6},{4,5,6},{0,4,7},{2,5,7},{1,6,7},{0,8},{1,8},{4,8},{5,8},{2,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered203 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 203) T=TwentyFiveEightLow.Case203.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case203.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 203)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case203.support T pos))
  · decide +kernel
theorem completion204 : pairCompletion (big 204)=full 204 := by
  have same : big 204=([{0,1,2,6},{3,4,6},{0,3,7},{1,4,7},{5,6,7},{2,5,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,6},{3,4,6},{0,3,7},{1,4,7},{5,6,7},{2,5,8}] [{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{3,5},{4,5},{0,1,2,6},{3,4,6},{2,7},{0,3,7},{1,4,7},{5,6,7},{0,8},{1,8},{3,8},{4,8},{2,5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered204 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 204) T=TwentyFiveEightLow.Case204.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case204.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 204)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case204.support T pos))
  · decide +kernel
theorem completion205 : pairCompletion (big 205)=full 205 := by
  have same : big 205=([{0,1,2},{0,3,4},{1,5,6},{2,3,7},{4,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,4},{1,5,6},{2,3,7},{4,5,7},{6,7,8}] [{0,1,2},{1,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{3,5},{0,6},{2,6},{3,6},{4,6},{1,5,6},{0,7},{1,7},{2,3,7},{4,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered205 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 205) T=TwentyFiveEightLow.Case205.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case205.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 205)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case205.support T pos))
  · decide +kernel
theorem completion206 : pairCompletion (big 206)=full 206 := by
  have same : big 206=([{1,2,4},{0,4,5,6},{1,5,7},{3,6,7},{3,5,8},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,4},{0,4,5,6},{1,5,7},{3,6,7},{3,5,8},{2,6,8},{4,7,8}] [{0,1},{0,2},{0,3},{1,3},{2,3},{1,2,4},{3,4},{2,5},{1,6},{0,4,5,6},{0,7},{2,7},{1,5,7},{3,6,7},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered206 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 206) T=TwentyFiveEightLow.Case206.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case206.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 206)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case206.support T pos))
  · decide +kernel
theorem completion207 : pairCompletion (big 207)=full 207 := by
  have same : big 207=([{1,2,4},{1,5,6},{3,5,7},{4,6,7},{0,4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,4},{1,5,6},{3,5,7},{4,6,7},{0,4,5,8},{3,6,8},{2,7,8}] [{0,1},{0,2},{0,3},{1,3},{2,3},{1,2,4},{3,4},{2,5},{0,6},{2,6},{1,5,6},{0,7},{1,7},{3,5,7},{4,6,7},{1,8},{0,4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered207 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 207) T=TwentyFiveEightLow.Case207.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case207.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 207)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case207.support T pos))
  · decide +kernel
theorem completion208 : pairCompletion (big 208)=full 208 := by
  have same : big 208=([{1,4,6},{3,5,6},{3,4,7},{2,5,7},{1,2,8},{0,4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,6},{3,5,6},{3,4,7},{2,5,7},{1,2,8},{0,4,5,8},{6,7,8}] [{0,1},{0,2},{0,3},{1,3},{2,3},{2,4},{1,5},{0,6},{2,6},{1,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{1,2,8},{3,8},{0,4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered208 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 208) T=TwentyFiveEightLow.Case208.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case208.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 208)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case208.support T pos))
  · decide +kernel
theorem completion209 : pairCompletion (big 209)=full 209 := by
  have same : big 209=([{1,2,3},{0,3,4,5},{1,4,6},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3},{0,3,4,5},{1,4,6},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] [{0,1},{0,2},{1,2,3},{2,4},{1,5},{0,3,4,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered209 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 209) T=TwentyFiveEightLow.Case209.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case209.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 209)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case209.support T pos))
  · decide +kernel
theorem completion210 : pairCompletion (big 210)=full 210 := by
  have same : big 210=([{0,3,4,5},{2,3,6},{1,4,6},{1,3,7},{5,6,7},{2,5,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4,5},{2,3,6},{1,4,6},{1,3,7},{5,6,7},{2,5,8},{4,7,8}] [{0,1},{0,2},{1,2},{2,4},{1,5},{0,3,4,5},{0,6},{2,3,6},{1,4,6},{0,7},{2,7},{1,3,7},{5,6,7},{0,8},{1,8},{3,8},{2,5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered210 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 210) T=TwentyFiveEightLow.Case210.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case210.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 210)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case210.support T pos))
  · decide +kernel
theorem completion211 : pairCompletion (big 211)=full 211 := by
  have same : big 211=([{0,1,3},{0,4,6},{2,5,6},{2,4,7},{1,5,7},{3,6,7},{3,4,5,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{0,4,6},{2,5,6},{2,4,7},{1,5,7},{3,6,7},{3,4,5,8}] [{0,2},{1,2},{0,1,3},{2,3},{1,4},{0,5},{1,6},{0,4,6},{2,5,6},{0,7},{2,4,7},{1,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,4,5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered211 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 211) T=TwentyFiveEightLow.Case211.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case211.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 211)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case211.support T pos))
  · decide +kernel
theorem completion212 : pairCompletion (big 212)=full 212 := by
  have same : big 212=([{0,1,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,3},{1,3},{2,3},{0,1,2,4},{3,4},{0,5},{2,5},{0,6},{2,6},{1,5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered212 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 212) T=TwentyFiveEightLow.Case212.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case212.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 212)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case212.support T pos))
  · decide +kernel
theorem completion213 : pairCompletion (big 213)=full 213 := by
  have same : big 213=([{1,4,5},{3,4,6},{3,5,7},{2,6,7},{0,1,2,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,5},{3,4,6},{3,5,7},{2,6,7},{0,1,2,8},{5,6,8},{4,7,8}] [{0,3},{1,3},{2,3},{0,4},{2,4},{0,5},{2,5},{1,4,5},{0,6},{1,6},{3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,1,2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered213 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 213) T=TwentyFiveEightLow.Case213.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case213.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 213)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case213.support T pos))
  · decide +kernel
theorem completion214 : pairCompletion (big 214)=full 214 := by
  have same : big 214=([{0,1,2,3},{1,4,5},{3,4,6},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{1,4,5},{3,4,6},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] [{0,1,2,3},{0,4},{2,4},{0,5},{2,5},{1,4,5},{0,6},{1,6},{3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered214 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 214) T=TwentyFiveEightLow.Case214.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case214.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 214)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case214.support T pos))
  · decide +kernel
theorem completion215 : pairCompletion (big 215)=full 215 := by
  have same : big 215=([{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,1,3,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,1,3,8},{6,7,8}] [{0,2},{1,2},{2,3},{0,4},{0,5},{1,4,5},{0,6},{1,6},{2,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{2,8},{0,1,3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered215 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 215) T=TwentyFiveEightLow.Case215.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case215.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 215)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case215.support T pos))
  · decide +kernel
theorem completion216 : pairCompletion (big 216)=full 216 := by
  have same : big 216=([{0,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,1,3,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,1,3,8}] [{0,2},{1,2},{2,3},{1,4},{1,5},{0,4,5},{0,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{1,6,7},{2,8},{0,1,3,8},{4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered216 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 216) T=TwentyFiveEightLow.Case216.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case216.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 216)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case216.support T pos))
  · decide +kernel
theorem completion217 : pairCompletion (big 217)=full 217 := by
  have same : big 217=([{0,3,5},{1,4,5},{1,3,6},{2,4,6},{2,3,7},{0,4,7},{5,6,7},{3,4,8},{2,5,8},{0,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,5},{1,4,5},{1,3,6},{2,4,6},{2,3,7},{0,4,7},{5,6,7},{3,4,8},{2,5,8},{0,6,8},{1,7,8}] [{0,1},{0,2},{1,2},{0,3,5},{1,4,5},{1,3,6},{2,4,6},{2,3,7},{0,4,7},{5,6,7},{3,4,8},{2,5,8},{0,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered217 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 217) T=TwentyFiveEightLow.Case217.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case217.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 217)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case217.support T pos))
  · decide +kernel
theorem completion218 : pairCompletion (big 218)=full 218 := by
  have same : big 218=([{0,2,3},{1,2,4},{1,3,5},{0,4,6},{2,5,6},{3,4,7},{0,5,7},{1,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{1,2,4},{1,3,5},{0,4,6},{2,5,6},{3,4,7},{0,5,7},{1,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,1},{0,2,3},{1,2,4},{1,3,5},{0,4,6},{2,5,6},{3,4,7},{0,5,7},{1,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered218 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 218) T=TwentyFiveEightLow.Case218.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case218.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 218)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case218.support T pos))
  · decide +kernel
theorem completion219 : pairCompletion (big 219)=full 219 := by
  have same : big 219=([{0,3,4},{1,3,5},{1,4,6},{0,5,7},{2,6,7},{2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{1,4,6},{0,5,7},{2,6,7},{2,3,8},{5,6,8},{4,7,8}] [{0,1},{0,2},{1,2},{2,4},{0,3,4},{2,5},{1,3,5},{4,5},{0,6},{3,6},{1,4,6},{1,7},{3,7},{0,5,7},{2,6,7},{0,8},{1,8},{2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered219 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 219) T=TwentyFiveEightLow.Case219.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case219.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 219)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case219.support T pos))
  · decide +kernel
theorem completion220 : pairCompletion (big 220)=full 220 := by
  have same : big 220=([{1,3,4},{0,3,5},{0,4,6},{2,3,7},{5,6,7},{1,5,8},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4},{0,3,5},{0,4,6},{2,3,7},{5,6,7},{1,5,8},{2,6,8},{4,7,8}] [{0,1},{0,2},{1,2},{2,4},{1,3,4},{2,5},{0,3,5},{4,5},{1,6},{3,6},{0,4,6},{0,7},{1,7},{2,3,7},{5,6,7},{0,8},{3,8},{1,5,8},{2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered220 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 220) T=TwentyFiveEightLow.Case220.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case220.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 220)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case220.support T pos))
  · decide +kernel
theorem completion221 : pairCompletion (big 221)=full 221 := by
  have same : big 221=([{1,3,4},{2,4,5},{0,5,6},{0,3,7},{4,6,7},{2,3,8},{1,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4},{2,4,5},{0,5,6},{0,3,7},{4,6,7},{2,3,8},{1,6,8},{5,7,8}] [{0,1},{0,2},{1,2},{0,4},{1,3,4},{1,5},{3,5},{2,4,5},{2,6},{3,6},{0,5,6},{1,7},{2,7},{0,3,7},{4,6,7},{0,8},{2,3,8},{4,8},{1,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered221 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 221) T=TwentyFiveEightLow.Case221.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case221.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 221)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case221.support T pos))
  · decide +kernel
theorem completion222 : pairCompletion (big 222)=full 222 := by
  have same : big 222=([{0,3,4},{1,3,5},{2,4,6},{4,5,7},{3,6,7},{2,5,8},{1,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{2,4,6},{4,5,7},{3,6,7},{2,5,8},{1,6,8},{0,7,8}] [{0,1},{0,2},{1,2},{2,3},{1,4},{0,3,4},{0,5},{1,3,5},{0,6},{2,4,6},{5,6},{1,7},{2,7},{4,5,7},{3,6,7},{3,8},{4,8},{2,5,8},{1,6,8},{0,7,8}]=true
  decide +kernel

theorem recovered222 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 222) T=TwentyFiveEightLow.Case222.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case222.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 222)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case222.support T pos))
  · decide +kernel
theorem completion223 : pairCompletion (big 223)=full 223 := by
  have same : big 223=([{0,2,4},{1,3,4},{1,2,5},{0,3,6},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4},{1,3,4},{1,2,5},{0,3,6},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] [{0,1},{2,3},{0,2,4},{1,3,4},{0,5},{1,2,5},{4,5},{1,6},{0,3,6},{4,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered223 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 223) T=TwentyFiveEightLow.Case223.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case223.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 223)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case223.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
