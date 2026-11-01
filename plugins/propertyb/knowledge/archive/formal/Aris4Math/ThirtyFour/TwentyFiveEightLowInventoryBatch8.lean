import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion256 : pairCompletion (big 256)=full 256 := by
  have same : big 256=([{0,1,3,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,2},{1,2},{2,3},{2,4},{0,1,3,4},{0,5},{1,5},{0,6},{1,6},{2,5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered256 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 256) T=TwentyFiveEightLow.Case256.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case256.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 256)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case256.support T pos))
  · decide +kernel
theorem completion257 : pairCompletion (big 257)=full 257 := by
  have same : big 257=([{2,4,5},{3,4,6},{3,5,7},{2,6,7},{0,1,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{3,4,6},{3,5,7},{2,6,7},{0,1,3,8},{5,6,8},{4,7,8}] [{0,2},{1,2},{2,3},{0,4},{1,4},{0,5},{1,5},{2,4,5},{0,6},{1,6},{3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{2,8},{0,1,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered257 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 257) T=TwentyFiveEightLow.Case257.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case257.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 257)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case257.support T pos))
  · decide +kernel
theorem completion258 : pairCompletion (big 258)=full 258 := by
  have same : big 258=([{0,1,2,3},{2,4,5},{3,4,6},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{2,4,5},{3,4,6},{3,5,7},{2,6,7},{5,6,8},{4,7,8}] [{0,1,2,3},{0,4},{1,4},{0,5},{1,5},{2,4,5},{0,6},{1,6},{3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered258 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 258) T=TwentyFiveEightLow.Case258.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case258.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 258)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case258.support T pos))
  · decide +kernel
theorem completion259 : pairCompletion (big 259)=full 259 := by
  have same : big 259=([{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,2,3,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,2,3,8}] [{0,1},{1,2},{1,3},{0,4},{0,5},{1,4,5},{0,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{1,6,7},{1,8},{0,2,3,8},{4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered259 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 259) T=TwentyFiveEightLow.Case259.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case259.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 259)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case259.support T pos))
  · decide +kernel
theorem completion260 : pairCompletion (big 260)=full 260 := by
  have same : big 260=([{0,1,4,5},{3,4,6},{3,5,7},{0,2,6,7},{1,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{3,4,6},{3,5,7},{0,2,6,7},{1,2,3,8},{5,6,8},{4,7,8}] [{0,3},{2,4},{2,5},{0,1,4,5},{1,6},{3,4,6},{1,7},{3,5,7},{0,2,6,7},{0,8},{1,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered260 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 260) T=TwentyFiveEightLow.Case260.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case260.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 260)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case260.support T pos))
  · decide +kernel
theorem completion261 : pairCompletion (big 261)=full 261 := by
  have same : big 261=([{0,1,2,3},{2,4,5},{3,4,6},{3,5,7},{2,6,7},{0,5,6,8},{1,4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{2,4,5},{3,4,6},{3,5,7},{2,6,7},{0,5,6,8},{1,4,7,8}] [{0,1,2,3},{0,4},{1,5},{2,4,5},{1,6},{3,4,6},{0,7},{3,5,7},{2,6,7},{2,8},{3,8},{0,5,6,8},{1,4,7,8}]=true
  decide +kernel

theorem recovered261 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 261) T=TwentyFiveEightLow.Case261.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case261.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 261)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case261.support T pos))
  · decide +kernel
theorem completion262 : pairCompletion (big 262)=full 262 := by
  have same : big 262=([{3,4,5},{0,1,3,6},{0,2,4,7},{1,2,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,1,3,6},{0,2,4,7},{1,2,5,8},{6,7,8}] [{2,3},{1,4},{0,5},{3,4,5},{2,6},{0,1,3,6},{4,6},{5,6},{1,7},{3,7},{0,2,4,7},{5,7},{0,8},{3,8},{4,8},{1,2,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered262 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 262) T=TwentyFiveEightLow.Case262.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case262.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 262)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case262.support T pos))
  · decide +kernel
theorem completion263 : pairCompletion (big 263)=full 263 := by
  have same : big 263=([{0,1,2,3},{2,4,5},{3,6,7},{0,4,6,8},{1,5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{2,4,5},{3,6,7},{0,4,6,8},{1,5,7,8}] [{0,1,2,3},{1,4},{3,4},{0,5},{3,5},{2,4,5},{1,6},{2,6},{5,6},{0,7},{2,7},{4,7},{3,6,7},{2,8},{3,8},{0,4,6,8},{1,5,7,8}]=true
  decide +kernel

theorem recovered263 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 263) T=TwentyFiveEightLow.Case263.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case263.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 263)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case263.support T pos))
  · decide +kernel
theorem completion264 : pairCompletion (big 264)=full 264 := by
  have same : big 264=([{0,1,3,4},{1,2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{1,2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,2},{2,3},{2,4},{0,1,3,4},{0,5},{0,6},{1,2,5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered264 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 264) T=TwentyFiveEightLow.Case264.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case264.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 264)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case264.support T pos))
  · decide +kernel
theorem completion265 : pairCompletion (big 265)=full 265 := by
  have same : big 265=([{0,1,4,5},{3,4,6},{3,5,7},{2,6,7},{1,2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{3,4,6},{3,5,7},{2,6,7},{1,2,3,8},{5,6,8},{4,7,8}] [{0,2},{0,3},{2,4},{2,5},{0,1,4,5},{0,6},{1,6},{3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{0,8},{1,2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered265 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 265) T=TwentyFiveEightLow.Case265.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case265.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 265)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case265.support T pos))
  · decide +kernel
theorem completion266 : pairCompletion (big 266)=full 266 := by
  have same : big 266=([{1,2,4,5},{3,4,6},{3,5,7},{2,6,7},{0,1,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,4,5},{3,4,6},{3,5,7},{2,6,7},{0,1,3,8},{5,6,8},{4,7,8}] [{0,2},{2,3},{0,4},{0,5},{1,2,4,5},{0,6},{1,6},{3,4,6},{0,7},{1,7},{3,5,7},{2,6,7},{2,8},{0,1,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered266 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 266) T=TwentyFiveEightLow.Case266.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case266.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 266)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case266.support T pos))
  · decide +kernel
theorem completion267 : pairCompletion (big 267)=full 267 := by
  have same : big 267=([{0,1,2,3},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,4,5,8},{6,7,8}] [{0,1,2,3},{0,4},{0,5},{0,6},{1,6},{2,4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{0,8},{2,8},{3,8},{1,4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered267 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 267) T=TwentyFiveEightLow.Case267.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case267.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 267)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case267.support T pos))
  · decide +kernel
theorem completion268 : pairCompletion (big 268)=full 268 := by
  have same : big 268=([{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,2,3,8},{1,4,5,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,2,3,8},{1,4,5,8}] [{0,1},{1,2},{1,3},{0,4},{0,5},{0,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{1,6,7},{0,2,3,8},{1,4,5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered268 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 268) T=TwentyFiveEightLow.Case268.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case268.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 268)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case268.support T pos))
  · decide +kernel
theorem completion269 : pairCompletion (big 269)=full 269 := by
  have same : big 269=([{0,1,2,3},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,4,5,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{1,6,7},{0,4,5,8}] [{0,1,2,3},{1,4},{1,5},{0,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{1,6,7},{1,8},{2,8},{3,8},{0,4,5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered269 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 269) T=TwentyFiveEightLow.Case269.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case269.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 269)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case269.support T pos))
  · decide +kernel
theorem completion270 : pairCompletion (big 270)=full 270 := by
  have same : big 270=([{0,1,3,4},{3,5,6},{4,5,7},{2,6,7},{0,2,8},{1,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{3,5,6},{4,5,7},{2,6,7},{0,2,8},{1,5,8},{4,6,8},{3,7,8}] [{1,2},{2,3},{2,4},{0,1,3,4},{0,5},{2,5},{0,6},{1,6},{3,5,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,2,8},{1,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered270 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 270) T=TwentyFiveEightLow.Case270.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case270.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 270)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case270.support T pos))
  · decide +kernel
theorem completion271 : pairCompletion (big 271)=full 271 := by
  have same : big 271=([{0,1,3,4},{3,5,6},{0,2,7},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{3,5,6},{0,2,7},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}] [{1,2},{2,3},{2,4},{0,1,3,4},{0,5},{2,5},{0,6},{1,6},{3,5,6},{0,2,7},{1,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered271 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 271) T=TwentyFiveEightLow.Case271.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case271.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 271)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case271.support T pos))
  · decide +kernel
theorem completion272 : pairCompletion (big 272)=full 272 := by
  have same : big 272=([{0,1,3,4},{2,5,6},{0,2,7},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{2,5,6},{0,2,7},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{1,7,8}] [{1,2},{2,3},{2,4},{0,1,3,4},{0,5},{1,5},{0,6},{1,6},{2,5,6},{0,2,7},{3,5,7},{4,6,7},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered272 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 272) T=TwentyFiveEightLow.Case272.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case272.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 272)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case272.support T pos))
  · decide +kernel
theorem completion273 : pairCompletion (big 273)=full 273 := by
  have same : big 273=([{3,4,5},{2,5,6},{0,2,7},{1,4,7},{3,6,7},{0,1,3,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{2,5,6},{0,2,7},{1,4,7},{3,6,7},{0,1,3,8},{4,6,8},{5,7,8}] [{1,2},{2,3},{0,4},{2,4},{0,5},{1,5},{3,4,5},{0,6},{1,6},{2,5,6},{0,2,7},{1,4,7},{3,6,7},{2,8},{0,1,3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered273 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 273) T=TwentyFiveEightLow.Case273.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case273.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 273)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case273.support T pos))
  · decide +kernel
theorem completion274 : pairCompletion (big 274)=full 274 := by
  have same : big 274=([{0,1,2,3},{2,4,5},{3,4,6},{0,4,7},{3,5,7},{2,6,7},{5,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{2,4,5},{3,4,6},{0,4,7},{3,5,7},{2,6,7},{5,6,8},{1,7,8}] [{0,1,2,3},{1,4},{0,5},{1,5},{2,4,5},{0,6},{1,6},{3,4,6},{0,4,7},{3,5,7},{2,6,7},{0,8},{2,8},{3,8},{4,8},{5,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered274 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 274) T=TwentyFiveEightLow.Case274.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case274.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 274)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case274.support T pos))
  · decide +kernel
theorem completion275 : pairCompletion (big 275)=full 275 := by
  have same : big 275=([{1,4,5},{2,4,6},{3,5,6},{0,1,7},{3,4,7},{2,5,7},{0,2,3,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,5},{2,4,6},{3,5,6},{0,1,7},{3,4,7},{2,5,7},{0,2,3,8},{6,7,8}] [{1,2},{1,3},{0,4},{0,5},{1,4,5},{0,6},{1,6},{2,4,6},{3,5,6},{0,1,7},{3,4,7},{2,5,7},{1,8},{0,2,3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered275 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 275) T=TwentyFiveEightLow.Case275.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case275.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 275)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case275.support T pos))
  · decide +kernel
theorem completion276 : pairCompletion (big 276)=full 276 := by
  have same : big 276=([{2,4,5},{3,4,6},{1,5,6},{0,4,7},{3,5,7},{2,6,7},{0,2,3,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{3,4,6},{1,5,6},{0,4,7},{3,5,7},{2,6,7},{0,2,3,8},{1,7,8}] [{0,1},{1,2},{1,3},{1,4},{0,5},{2,4,5},{0,6},{3,4,6},{1,5,6},{0,4,7},{3,5,7},{2,6,7},{0,2,3,8},{4,8},{5,8},{6,8},{1,7,8}]=true
  decide +kernel

theorem recovered276 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 276) T=TwentyFiveEightLow.Case276.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case276.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 276)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case276.support T pos))
  · decide +kernel
theorem completion277 : pairCompletion (big 277)=full 277 := by
  have same : big 277=([{0,1,3,4},{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}] [{0,2},{1,2},{2,4},{0,1,3,4},{1,5},{3,5},{0,6},{2,6},{4,5,6},{0,7},{1,7},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered277 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 277) T=TwentyFiveEightLow.Case277.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case277.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 277)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case277.support T pos))
  · decide +kernel
theorem completion278 : pairCompletion (big 278)=full 278 := by
  have same : big 278=([{0,1,3,4},{4,5,6},{2,3,7},{0,5,7},{1,6,7},{2,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{4,5,6},{2,3,7},{0,5,7},{1,6,7},{2,5,8},{3,6,8},{4,7,8}] [{0,2},{1,2},{2,4},{0,1,3,4},{1,5},{3,5},{0,6},{2,6},{4,5,6},{2,3,7},{0,5,7},{1,6,7},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered278 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 278) T=TwentyFiveEightLow.Case278.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case278.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 278)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case278.support T pos))
  · decide +kernel
theorem completion279 : pairCompletion (big 279)=full 279 := by
  have same : big 279=([{0,1,3,4},{2,5,6},{2,3,7},{0,5,7},{4,6,7},{4,5,8},{3,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{2,5,6},{2,3,7},{0,5,7},{4,6,7},{4,5,8},{3,6,8},{1,7,8}] [{0,2},{1,2},{2,4},{0,1,3,4},{1,5},{3,5},{0,6},{1,6},{2,5,6},{2,3,7},{0,5,7},{4,6,7},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered279 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 279) T=TwentyFiveEightLow.Case279.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case279.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 279)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case279.support T pos))
  · decide +kernel
theorem completion280 : pairCompletion (big 280)=full 280 := by
  have same : big 280=([{0,1,3,4},{3,5,6},{2,3,7},{0,5,7},{4,6,7},{4,5,8},{2,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{3,5,6},{2,3,7},{0,5,7},{4,6,7},{4,5,8},{2,6,8},{1,7,8}] [{0,2},{1,2},{2,4},{0,1,3,4},{1,5},{2,5},{0,6},{1,6},{3,5,6},{2,3,7},{0,5,7},{4,6,7},{0,8},{3,8},{4,5,8},{2,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered280 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 280) T=TwentyFiveEightLow.Case280.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case280.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 280)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case280.support T pos))
  · decide +kernel
theorem completion281 : pairCompletion (big 281)=full 281 := by
  have same : big 281=([{2,4,6},{3,5,6},{2,3,7},{0,4,7},{1,5,7},{0,1,3,8},{4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,6},{3,5,6},{2,3,7},{0,4,7},{1,5,7},{0,1,3,8},{4,5,8},{6,7,8}] [{0,2},{1,2},{1,4},{3,4},{0,5},{2,5},{0,6},{1,6},{2,4,6},{3,5,6},{2,3,7},{0,4,7},{1,5,7},{2,8},{0,1,3,8},{4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered281 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 281) T=TwentyFiveEightLow.Case281.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case281.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 281)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case281.support T pos))
  · decide +kernel
theorem completion282 : pairCompletion (big 282)=full 282 := by
  have same : big 282=([{3,4,5},{2,4,6},{0,4,7},{1,5,7},{3,6,7},{0,1,3,8},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{2,4,6},{0,4,7},{1,5,7},{3,6,7},{0,1,3,8},{5,6,8},{2,7,8}] [{0,2},{1,2},{2,3},{1,4},{0,5},{2,5},{3,4,5},{0,6},{1,6},{2,4,6},{0,4,7},{1,5,7},{3,6,7},{0,1,3,8},{4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered282 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 282) T=TwentyFiveEightLow.Case282.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case282.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 282)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case282.support T pos))
  · decide +kernel
theorem completion283 : pairCompletion (big 283)=full 283 := by
  have same : big 283=([{0,1,2,3},{2,4,5},{3,4,6},{0,4,7},{1,5,7},{2,6,7},{5,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{2,4,5},{3,4,6},{0,4,7},{1,5,7},{2,6,7},{5,6,8},{3,7,8}] [{0,1,2,3},{1,4},{0,5},{3,5},{2,4,5},{0,6},{1,6},{3,4,6},{0,4,7},{1,5,7},{2,6,7},{0,8},{1,8},{2,8},{4,8},{5,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered283 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 283) T=TwentyFiveEightLow.Case283.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case283.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 283)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case283.support T pos))
  · decide +kernel
theorem completion284 : pairCompletion (big 284)=full 284 := by
  have same : big 284=([{1,4,5},{3,4,6},{2,5,6},{1,2,7},{0,4,7},{3,5,7},{0,2,3,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,5},{3,4,6},{2,5,6},{1,2,7},{0,4,7},{3,5,7},{0,2,3,8},{6,7,8}] [{0,1},{1,3},{2,4},{0,5},{1,4,5},{0,6},{1,6},{3,4,6},{2,5,6},{1,2,7},{0,4,7},{3,5,7},{1,8},{0,2,3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered284 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 284) T=TwentyFiveEightLow.Case284.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case284.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 284)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case284.support T pos))
  · decide +kernel
theorem completion285 : pairCompletion (big 285)=full 285 := by
  have same : big 285=([{2,4,5},{3,4,6},{1,5,6},{1,2,7},{0,4,7},{3,5,7},{0,2,3,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{3,4,6},{1,5,6},{1,2,7},{0,4,7},{3,5,7},{0,2,3,8},{6,7,8}] [{0,1},{1,3},{1,4},{0,5},{2,4,5},{0,6},{2,6},{3,4,6},{1,5,6},{1,2,7},{0,4,7},{3,5,7},{1,8},{0,2,3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered285 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 285) T=TwentyFiveEightLow.Case285.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case285.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 285)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case285.support T pos))
  · decide +kernel
theorem completion286 : pairCompletion (big 286)=full 286 := by
  have same : big 286=([{0,1,2,3},{4,5,6},{2,4,7},{3,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3},{4,5,6},{2,4,7},{3,5,7},{6,7,8}] [{0,1,2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered286 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 286) T=TwentyFiveEightLow.Case286.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case286.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 286)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case286.support T pos))
  · decide +kernel
theorem completion287 : pairCompletion (big 287)=full 287 := by
  have same : big 287=([{0,2,3,4},{0,1,5},{1,2,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{0,1,5},{1,2,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}] [{1,3},{1,4},{0,2,3,4},{0,1,5},{2,5},{0,6},{1,2,6},{5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered287 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 287) T=TwentyFiveEightLow.Case287.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case287.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 287)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case287.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
