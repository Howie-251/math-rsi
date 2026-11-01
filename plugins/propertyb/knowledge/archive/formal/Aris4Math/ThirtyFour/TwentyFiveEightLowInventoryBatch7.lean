import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion224 : pairCompletion (big 224)=full 224 := by
  have same : big 224=([{0,3,4},{1,2,5},{0,2,6},{4,5,6},{1,3,7},{2,4,7},{3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,2,5},{0,2,6},{4,5,6},{1,3,7},{2,4,7},{3,5,8},{6,7,8}] [{0,1},{2,3},{1,4},{0,3,4},{0,5},{1,2,5},{1,6},{0,2,6},{3,6},{4,5,6},{0,7},{1,3,7},{2,4,7},{5,7},{0,8},{1,8},{2,8},{4,8},{3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered224 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 224) T=TwentyFiveEightLow.Case224.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case224.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 224)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case224.support T pos))
  · decide +kernel
theorem completion225 : pairCompletion (big 225)=full 225 := by
  have same : big 225=([{0,3,4},{1,3,5},{0,5,6},{2,4,7},{3,6,7},{4,5,8},{2,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{0,5,6},{2,4,7},{3,6,7},{4,5,8},{2,6,8},{1,7,8}] [{0,1},{0,2},{1,2},{2,3},{1,4},{0,3,4},{2,5},{1,3,5},{1,6},{4,6},{0,5,6},{0,7},{2,4,7},{5,7},{3,6,7},{0,8},{3,8},{4,5,8},{2,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered225 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 225) T=TwentyFiveEightLow.Case225.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case225.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 225)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case225.support T pos))
  · decide +kernel
theorem completion226 : pairCompletion (big 226)=full 226 := by
  have same : big 226=([{1,3,4},{2,3,5},{0,4,6},{0,5,7},{3,6,7},{4,5,8},{1,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4},{2,3,5},{0,4,6},{0,5,7},{3,6,7},{4,5,8},{1,6,8},{2,7,8}] [{0,1},{0,2},{1,2},{0,3},{2,4},{1,3,4},{1,5},{2,3,5},{2,6},{0,4,6},{5,6},{1,7},{4,7},{0,5,7},{3,6,7},{0,8},{3,8},{4,5,8},{1,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered226 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 226) T=TwentyFiveEightLow.Case226.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case226.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 226)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case226.support T pos))
  · decide +kernel
theorem completion227 : pairCompletion (big 227)=full 227 := by
  have same : big 227=([{0,2,3},{1,2,4},{1,3,5},{3,4,6},{2,5,7},{0,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{1,2,4},{1,3,5},{3,4,6},{2,5,7},{0,6,7},{5,6,8},{4,7,8}] [{0,1},{0,2,3},{0,4},{1,2,4},{0,5},{1,3,5},{4,5},{1,6},{2,6},{3,4,6},{1,7},{3,7},{2,5,7},{0,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered227 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 227) T=TwentyFiveEightLow.Case227.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case227.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 227)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case227.support T pos))
  · decide +kernel
theorem completion228 : pairCompletion (big 228)=full 228 := by
  have same : big 228=([{0,2,4},{1,2,5},{3,4,5},{0,3,6},{1,3,7},{2,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4},{1,2,5},{3,4,5},{0,3,6},{1,3,7},{2,6,7},{4,6,8},{5,7,8}] [{0,1},{2,3},{1,4},{0,2,4},{0,5},{1,2,5},{3,4,5},{1,6},{0,3,6},{5,6},{0,7},{1,3,7},{4,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered228 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 228) T=TwentyFiveEightLow.Case228.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case228.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 228)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case228.support T pos))
  · decide +kernel
theorem completion229 : pairCompletion (big 229)=full 229 := by
  have same : big 229=([{1,3,4},{2,3,5},{0,4,6},{0,5,7},{3,6,7},{4,5,8},{2,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4},{2,3,5},{0,4,6},{0,5,7},{3,6,7},{4,5,8},{2,6,8},{1,7,8}] [{0,1},{0,2},{1,2},{0,3},{2,4},{1,3,4},{1,5},{2,3,5},{1,6},{0,4,6},{5,6},{2,7},{4,7},{0,5,7},{3,6,7},{0,8},{3,8},{4,5,8},{2,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered229 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 229) T=TwentyFiveEightLow.Case229.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case229.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 229)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case229.support T pos))
  · decide +kernel
theorem completion230 : pairCompletion (big 230)=full 230 := by
  have same : big 230=([{0,2,4},{1,2,5},{3,4,5},{0,3,6},{1,3,7},{2,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4},{1,2,5},{3,4,5},{0,3,6},{1,3,7},{2,6,7},{5,6,8},{4,7,8}] [{0,1},{2,3},{1,4},{0,2,4},{0,5},{1,2,5},{3,4,5},{1,6},{0,3,6},{4,6},{0,7},{1,3,7},{5,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered230 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 230) T=TwentyFiveEightLow.Case230.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case230.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 230)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case230.support T pos))
  · decide +kernel
theorem completion231 : pairCompletion (big 231)=full 231 := by
  have same : big 231=([{0,3,4},{1,3,5},{2,6,7},{0,1,2,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{2,6,7},{0,1,2,8},{4,6,8},{5,7,8}] [{2,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{1,3,5},{4,5},{0,6},{1,6},{3,6},{5,6},{0,7},{1,7},{3,7},{4,7},{2,6,7},{0,1,2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered231 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 231) T=TwentyFiveEightLow.Case231.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case231.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 231)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case231.support T pos))
  · decide +kernel
theorem completion232 : pairCompletion (big 232)=full 232 := by
  have same : big 232=([{0,3,4},{1,3,5},{0,1,2,7},{4,6,7},{2,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{0,1,2,7},{4,6,7},{2,6,8},{5,7,8}] [{2,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{1,3,5},{4,5},{0,6},{1,6},{3,6},{5,6},{0,1,2,7},{3,7},{4,6,7},{0,8},{1,8},{3,8},{4,8},{2,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered232 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 232) T=TwentyFiveEightLow.Case232.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case232.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 232)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case232.support T pos))
  · decide +kernel
theorem completion233 : pairCompletion (big 233)=full 233 := by
  have same : big 233=([{0,3,4},{1,5,6},{0,1,2,7},{4,5,7},{2,3,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,5,6},{0,1,2,7},{4,5,7},{2,3,8},{6,7,8}] [{1,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{3,5},{0,6},{2,6},{3,6},{4,6},{1,5,6},{0,1,2,7},{3,7},{4,5,7},{0,8},{1,8},{2,3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered233 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 233) T=TwentyFiveEightLow.Case233.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case233.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 233)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case233.support T pos))
  · decide +kernel
theorem completion234 : pairCompletion (big 234)=full 234 := by
  have same : big 234=([{0,3,4},{0,1,2,7},{3,5,7},{4,6,7},{1,5,8},{2,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{0,1,2,7},{3,5,7},{4,6,7},{1,5,8},{2,6,8}] [{1,3},{2,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{4,5},{0,6},{1,6},{3,6},{5,6},{0,1,2,7},{3,5,7},{4,6,7},{0,8},{3,8},{4,8},{1,5,8},{2,6,8},{7,8}]=true
  decide +kernel

theorem recovered234 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 234) T=TwentyFiveEightLow.Case234.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case234.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 234)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case234.support T pos))
  · decide +kernel
theorem completion235 : pairCompletion (big 235)=full 235 := by
  have same : big 235=([{0,2,3},{1,2,4},{3,5,7},{4,6,7},{5,6,8},{0,1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{1,2,4},{3,5,7},{4,6,7},{5,6,8},{0,1,7,8}] [{1,3},{0,2,3},{0,4},{1,2,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{2,7},{3,5,7},{4,6,7},{2,8},{3,8},{4,8},{5,6,8},{0,1,7,8}]=true
  decide +kernel

theorem recovered235 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 235) T=TwentyFiveEightLow.Case235.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case235.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 235)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case235.support T pos))
  · decide +kernel
theorem completion236 : pairCompletion (big 236)=full 236 := by
  have same : big 236=([{0,2,3},{1,4,5},{2,4,7},{3,6,7},{5,6,8},{0,1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{1,4,5},{2,4,7},{3,6,7},{5,6,8},{0,1,7,8}] [{1,2},{1,3},{0,2,3},{0,4},{3,4},{0,5},{2,5},{3,5},{1,4,5},{0,6},{1,6},{2,6},{4,6},{2,4,7},{5,7},{3,6,7},{2,8},{3,8},{4,8},{5,6,8},{0,1,7,8}]=true
  decide +kernel

theorem recovered236 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 236) T=TwentyFiveEightLow.Case236.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case236.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 236)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case236.support T pos))
  · decide +kernel
theorem completion237 : pairCompletion (big 237)=full 237 := by
  have same : big 237=([{0,3,4},{1,3,5},{1,4,6},{2,5,7},{0,6,7},{2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{1,4,6},{2,5,7},{0,6,7},{2,3,8},{5,6,8},{4,7,8}] [{0,1},{0,2},{1,2},{2,4},{0,3,4},{0,5},{1,3,5},{4,5},{2,6},{3,6},{1,4,6},{1,7},{3,7},{2,5,7},{0,6,7},{0,8},{1,8},{2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered237 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 237) T=TwentyFiveEightLow.Case237.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case237.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 237)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case237.support T pos))
  · decide +kernel
theorem completion238 : pairCompletion (big 238)=full 238 := by
  have same : big 238=([{1,3,4},{0,3,5},{0,4,6},{2,3,7},{5,6,7},{2,5,8},{1,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4},{0,3,5},{0,4,6},{2,3,7},{5,6,7},{2,5,8},{1,6,8},{4,7,8}] [{0,1},{0,2},{1,2},{2,4},{1,3,4},{1,5},{0,3,5},{4,5},{2,6},{3,6},{0,4,6},{0,7},{1,7},{2,3,7},{5,6,7},{0,8},{3,8},{2,5,8},{1,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered238 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 238) T=TwentyFiveEightLow.Case238.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case238.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 238)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case238.support T pos))
  · decide +kernel
theorem completion239 : pairCompletion (big 239)=full 239 := by
  have same : big 239=([{1,3,4},{0,4,5},{2,3,6},{0,3,7},{5,6,7},{2,5,8},{1,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4},{0,4,5},{2,3,6},{0,3,7},{5,6,7},{2,5,8},{1,6,8},{4,7,8}] [{0,1},{0,2},{1,2},{2,4},{1,3,4},{1,5},{3,5},{0,4,5},{0,6},{2,3,6},{4,6},{1,7},{2,7},{0,3,7},{5,6,7},{0,8},{3,8},{2,5,8},{1,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered239 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 239) T=TwentyFiveEightLow.Case239.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case239.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 239)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case239.support T pos))
  · decide +kernel
theorem completion240 : pairCompletion (big 240)=full 240 := by
  have same : big 240=([{0,3,4},{2,4,5},{0,5,6},{1,3,7},{4,6,7},{2,3,8},{1,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{2,4,5},{0,5,6},{1,3,7},{4,6,7},{2,3,8},{1,6,8},{5,7,8}] [{0,1},{0,2},{1,2},{1,4},{0,3,4},{1,5},{3,5},{2,4,5},{2,6},{3,6},{0,5,6},{0,7},{2,7},{1,3,7},{4,6,7},{0,8},{2,3,8},{4,8},{1,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered240 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 240) T=TwentyFiveEightLow.Case240.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case240.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 240)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case240.support T pos))
  · decide +kernel
theorem completion241 : pairCompletion (big 241)=full 241 := by
  have same : big 241=([{1,3,4},{0,4,5},{2,5,6},{0,3,7},{4,6,7},{2,3,8},{1,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4},{0,4,5},{2,5,6},{0,3,7},{4,6,7},{2,3,8},{1,6,8},{5,7,8}] [{0,1},{0,2},{1,2},{2,4},{1,3,4},{1,5},{3,5},{0,4,5},{0,6},{3,6},{2,5,6},{1,7},{2,7},{0,3,7},{4,6,7},{0,8},{2,3,8},{4,8},{1,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered241 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 241) T=TwentyFiveEightLow.Case241.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case241.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 241)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case241.support T pos))
  · decide +kernel
theorem completion242 : pairCompletion (big 242)=full 242 := by
  have same : big 242=([{0,3,4},{1,3,5},{2,4,6},{4,5,7},{3,6,7},{0,5,8},{1,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{2,4,6},{4,5,7},{3,6,7},{0,5,8},{1,6,8},{2,7,8}] [{0,1},{0,2},{1,2},{2,3},{1,4},{0,3,4},{2,5},{1,3,5},{0,6},{2,4,6},{5,6},{0,7},{1,7},{4,5,7},{3,6,7},{3,8},{4,8},{0,5,8},{1,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered242 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 242) T=TwentyFiveEightLow.Case242.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case242.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 242)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case242.support T pos))
  · decide +kernel
theorem completion243 : pairCompletion (big 243)=full 243 := by
  have same : big 243=([{0,2,3},{1,2,4},{1,3,5},{0,4,6},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{1,2,4},{1,3,5},{0,4,6},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] [{0,1},{0,2,3},{1,2,4},{3,4},{0,5},{1,3,5},{4,5},{1,6},{2,6},{0,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered243 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 243) T=TwentyFiveEightLow.Case243.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case243.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 243)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case243.support T pos))
  · decide +kernel
theorem completion244 : pairCompletion (big 244)=full 244 := by
  have same : big 244=([{0,2,3},{1,3,4},{1,2,5},{2,4,6},{4,5,7},{0,6,7},{5,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{1,3,4},{1,2,5},{2,4,6},{4,5,7},{0,6,7},{5,6,8},{3,7,8}] [{0,1},{0,2,3},{0,4},{1,3,4},{0,5},{1,2,5},{3,5},{1,6},{3,6},{2,4,6},{1,7},{2,7},{4,5,7},{0,6,7},{0,8},{1,8},{2,8},{4,8},{5,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered244 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 244) T=TwentyFiveEightLow.Case244.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case244.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 244)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case244.support T pos))
  · decide +kernel
theorem completion245 : pairCompletion (big 245)=full 245 := by
  have same : big 245=([{0,3,4},{0,2,5},{1,2,6},{4,5,6},{1,3,7},{2,4,7},{3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{0,2,5},{1,2,6},{4,5,6},{1,3,7},{2,4,7},{3,5,8},{6,7,8}] [{0,1},{2,3},{1,4},{0,3,4},{1,5},{0,2,5},{0,6},{1,2,6},{3,6},{4,5,6},{0,7},{1,3,7},{2,4,7},{5,7},{0,8},{1,8},{2,8},{4,8},{3,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered245 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 245) T=TwentyFiveEightLow.Case245.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case245.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 245)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case245.support T pos))
  · decide +kernel
theorem completion246 : pairCompletion (big 246)=full 246 := by
  have same : big 246=([{0,2,3},{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,6,7},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{1,4,5},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,6,7},{1,7,8}] [{0,1},{1,2},{1,3},{0,2,3},{0,4},{0,5},{1,4,5},{1,6},{2,4,6},{3,5,6},{3,4,7},{2,5,7},{0,6,7},{0,8},{2,8},{3,8},{4,8},{5,8},{6,8},{1,7,8}]=true
  decide +kernel

theorem recovered246 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 246) T=TwentyFiveEightLow.Case246.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case246.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 246)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case246.support T pos))
  · decide +kernel
theorem completion247 : pairCompletion (big 247)=full 247 := by
  have same : big 247=([{1,3,4},{0,1,2,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4},{0,1,2,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}] [{0,3},{2,3},{0,4},{2,4},{1,3,4},{0,5},{1,5},{3,5},{4,5},{0,6},{1,6},{2,6},{4,6},{0,1,2,7},{3,7},{5,6,7},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered247 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 247) T=TwentyFiveEightLow.Case247.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case247.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 247)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case247.support T pos))
  · decide +kernel
theorem completion248 : pairCompletion (big 248)=full 248 := by
  have same : big 248=([{1,3,4},{2,5,7},{3,6,7},{0,1,2,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4},{2,5,7},{3,6,7},{0,1,2,8},{5,6,8},{4,7,8}] [{0,3},{2,3},{0,4},{2,4},{1,3,4},{0,5},{1,5},{3,5},{4,5},{0,6},{1,6},{2,6},{4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,1,2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered248 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 248) T=TwentyFiveEightLow.Case248.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case248.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 248)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case248.support T pos))
  · decide +kernel
theorem completion249 : pairCompletion (big 249)=full 249 := by
  have same : big 249=([{1,3,4},{0,1,2,6},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4},{0,1,2,6},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] [{0,3},{2,3},{0,4},{2,4},{1,3,4},{0,5},{1,5},{3,5},{4,5},{0,1,2,6},{4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered249 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 249) T=TwentyFiveEightLow.Case249.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case249.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 249)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case249.support T pos))
  · decide +kernel
theorem completion250 : pairCompletion (big 250)=full 250 := by
  have same : big 250=([{1,3,4},{0,1,2,6},{3,5,7},{4,6,7},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,4},{0,1,2,6},{3,5,7},{4,6,7},{5,6,8},{2,7,8}] [{0,3},{2,3},{0,4},{2,4},{1,3,4},{0,5},{1,5},{2,5},{4,5},{0,1,2,6},{3,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{1,8},{3,8},{4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered250 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 250) T=TwentyFiveEightLow.Case250.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case250.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 250)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case250.support T pos))
  · decide +kernel
theorem completion251 : pairCompletion (big 251)=full 251 := by
  have same : big 251=([{0,1,2,6},{3,5,6},{1,3,7},{4,5,7},{2,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,6},{3,5,6},{1,3,7},{4,5,7},{2,4,8},{6,7,8}] [{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{0,1,2,6},{4,6},{3,5,6},{0,7},{2,7},{1,3,7},{4,5,7},{0,8},{1,8},{3,8},{2,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered251 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 251) T=TwentyFiveEightLow.Case251.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case251.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 251)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case251.support T pos))
  · decide +kernel
theorem completion252 : pairCompletion (big 252)=full 252 := by
  have same : big 252=([{0,1,2,6},{3,5,6},{1,3,7},{4,6,7},{2,4,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,6},{3,5,6},{1,3,7},{4,6,7},{2,4,8},{5,7,8}] [{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,1,2,6},{3,5,6},{0,7},{2,7},{1,3,7},{4,6,7},{0,8},{1,8},{3,8},{2,4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered252 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 252) T=TwentyFiveEightLow.Case252.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case252.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 252)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case252.support T pos))
  · decide +kernel
theorem completion253 : pairCompletion (big 253)=full 253 := by
  have same : big 253=([{1,2,3},{4,5,6},{2,4,7},{3,6,7},{0,1,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3},{4,5,6},{2,4,7},{3,6,7},{0,1,6,8},{5,7,8}] [{0,2},{0,3},{1,2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{3,5},{2,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,6,7},{2,8},{3,8},{4,8},{0,1,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered253 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 253) T=TwentyFiveEightLow.Case253.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case253.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 253)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case253.support T pos))
  · decide +kernel
theorem completion254 : pairCompletion (big 254)=full 254 := by
  have same : big 254=([{2,3,6},{1,2,7},{3,4,7},{5,6,7},{4,5,8},{0,1,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,6},{1,2,7},{3,4,7},{5,6,7},{4,5,8},{0,1,6,8}] [{0,2},{0,3},{1,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,5},{2,3,6},{4,6},{0,7},{1,2,7},{3,4,7},{5,6,7},{2,8},{3,8},{4,5,8},{0,1,6,8},{7,8}]=true
  decide +kernel

theorem recovered254 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 254) T=TwentyFiveEightLow.Case254.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case254.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 254)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case254.support T pos))
  · decide +kernel
theorem completion255 : pairCompletion (big 255)=full 255 := by
  have same : big 255=([{0,2,3},{4,5,6},{1,4,7},{2,5,7},{3,6,7},{0,1,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3},{4,5,6},{1,4,7},{2,5,7},{3,6,7},{0,1,6,8}] [{1,2},{1,3},{0,2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{3,5},{2,6},{4,5,6},{0,7},{1,4,7},{2,5,7},{3,6,7},{2,8},{3,8},{4,8},{5,8},{0,1,6,8},{7,8}]=true
  decide +kernel

theorem recovered255 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 255) T=TwentyFiveEightLow.Case255.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case255.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 255)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case255.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
