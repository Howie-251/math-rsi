import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion416 : pairCompletion (big 416)=full 416 := by
  have same : big 416=([{0,1,3,5},{0,2,4,7},{3,6,7},{1,2,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,5},{0,2,4,7},{3,6,7},{1,2,8},{4,6,8},{5,7,8}] [{2,3},{1,4},{3,4},{2,5},{0,1,3,5},{4,5},{0,6},{1,6},{2,6},{5,6},{1,7},{0,2,4,7},{3,6,7},{0,8},{1,2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered416 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 416) T=TwentyFiveEightLow.Case416.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case416.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 416)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case416.support T pos))
  · decide +kernel
theorem completion417 : pairCompletion (big 417)=full 417 := by
  have same : big 417=([{0,1,4,5},{1,2,7},{3,6,7},{0,2,3,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{1,2,7},{3,6,7},{0,2,3,8},{4,6,8},{5,7,8}] [{1,3},{2,4},{3,4},{2,5},{3,5},{0,1,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,2,7},{4,7},{3,6,7},{1,8},{0,2,3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered417 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 417) T=TwentyFiveEightLow.Case417.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case417.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 417)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case417.support T pos))
  · decide +kernel
theorem completion418 : pairCompletion (big 418)=full 418 := by
  have same : big 418=([{0,1,3,4},{0,2,5,6},{1,2,7},{3,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{0,2,5,6},{1,2,7},{3,6,7},{4,6,8},{5,7,8}] [{2,3},{2,4},{0,1,3,4},{1,5},{3,5},{4,5},{1,6},{0,2,5,6},{0,7},{1,2,7},{4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered418 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 418) T=TwentyFiveEightLow.Case418.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case418.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 418)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case418.support T pos))
  · decide +kernel
theorem completion419 : pairCompletion (big 419)=full 419 := by
  have same : big 419=([{0,1,4,6},{3,5,6},{1,2,7},{4,5,7},{0,2,3,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,6},{3,5,6},{1,2,7},{4,5,7},{0,2,3,8},{6,7,8}] [{1,3},{2,4},{3,4},{0,5},{1,5},{2,5},{2,6},{0,1,4,6},{3,5,6},{0,7},{1,2,7},{3,7},{4,5,7},{1,8},{0,2,3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered419 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 419) T=TwentyFiveEightLow.Case419.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case419.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 419)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case419.support T pos))
  · decide +kernel
theorem completion420 : pairCompletion (big 420)=full 420 := by
  have same : big 420=([{0,1,3,4},{3,5,6},{1,2,7},{4,6,7},{0,2,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{3,5,6},{1,2,7},{4,6,7},{0,2,6,8},{5,7,8}] [{2,3},{2,4},{0,1,3,4},{0,5},{1,5},{2,5},{4,5},{1,6},{3,5,6},{0,7},{1,2,7},{3,7},{4,6,7},{1,8},{3,8},{4,8},{0,2,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered420 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 420) T=TwentyFiveEightLow.Case420.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case420.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 420)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case420.support T pos))
  · decide +kernel
theorem completion421 : pairCompletion (big 421)=full 421 := by
  have same : big 421=([{0,1,3,6},{1,2,7},{3,5,7},{4,6,7},{0,2,4,8},{5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,6},{1,2,7},{3,5,7},{4,6,7},{0,2,4,8},{5,6,8}] [{2,3},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{2,6},{0,1,3,6},{0,7},{1,2,7},{3,5,7},{4,6,7},{1,8},{3,8},{0,2,4,8},{5,6,8},{7,8}]=true
  decide +kernel

theorem recovered421 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 421) T=TwentyFiveEightLow.Case421.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case421.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 421)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case421.support T pos))
  · decide +kernel
theorem completion422 : pairCompletion (big 422)=full 422 := by
  have same : big 422=([{0,1,3,4},{1,5,6},{2,5,7},{3,6,7},{0,2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{1,5,6},{2,5,7},{3,6,7},{0,2,6,8},{4,7,8}] [{1,2},{2,3},{2,4},{0,1,3,4},{0,5},{3,5},{4,5},{4,6},{1,5,6},{0,7},{1,7},{2,5,7},{3,6,7},{1,8},{3,8},{5,8},{0,2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered422 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 422) T=TwentyFiveEightLow.Case422.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case422.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 422)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case422.support T pos))
  · decide +kernel
theorem completion423 : pairCompletion (big 423)=full 423 := by
  have same : big 423=([{0,2,4,6},{1,5,6},{2,5,7},{3,6,7},{0,1,3,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4,6},{1,5,6},{2,5,7},{3,6,7},{0,1,3,8},{4,7,8}] [{1,2},{2,3},{1,4},{3,4},{0,5},{3,5},{4,5},{0,2,4,6},{1,5,6},{0,7},{1,7},{2,5,7},{3,6,7},{2,8},{0,1,3,8},{5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered423 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 423) T=TwentyFiveEightLow.Case423.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case423.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 423)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case423.support T pos))
  · decide +kernel
theorem completion424 : pairCompletion (big 424)=full 424 := by
  have same : big 424=([{2,5,6},{0,1,7},{3,5,7},{4,6,7},{0,2,4,8},{1,3,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,5,6},{0,1,7},{3,5,7},{4,6,7},{0,2,4,8},{1,3,6,8}] [{1,2},{0,3},{2,3},{1,4},{3,4},{0,5},{1,5},{4,5},{0,6},{2,5,6},{0,1,7},{2,7},{3,5,7},{4,6,7},{0,2,4,8},{5,8},{1,3,6,8},{7,8}]=true
  decide +kernel

theorem recovered424 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 424) T=TwentyFiveEightLow.Case424.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case424.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 424)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case424.support T pos))
  · decide +kernel
theorem completion425 : pairCompletion (big 425)=full 425 := by
  have same : big 425=([{2,3,5},{0,1,5,6},{0,2,7},{4,6,7},{4,5,8},{3,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{0,1,5,6},{0,2,7},{4,6,7},{4,5,8},{3,6,8},{1,7,8}] [{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{2,3,5},{2,6},{0,1,5,6},{0,2,7},{3,7},{5,7},{4,6,7},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered425 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 425) T=TwentyFiveEightLow.Case425.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case425.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 425)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case425.support T pos))
  · decide +kernel
theorem completion426 : pairCompletion (big 426)=full 426 := by
  have same : big 426=([{2,3,5},{0,1,5,6},{4,5,7},{3,6,7},{0,2,8},{4,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{0,1,5,6},{4,5,7},{3,6,7},{0,2,8},{4,6,8},{1,7,8}] [{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{2,3,5},{2,6},{0,1,5,6},{0,7},{2,7},{4,5,7},{3,6,7},{0,2,8},{3,8},{5,8},{4,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered426 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 426) T=TwentyFiveEightLow.Case426.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case426.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 426)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case426.support T pos))
  · decide +kernel
theorem completion427 : pairCompletion (big 427)=full 427 := by
  have same : big 427=([{2,3,5},{0,2,6},{4,5,7},{1,6,7},{0,1,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,5},{0,2,6},{4,5,7},{1,6,7},{0,1,5,8},{4,6,8},{3,7,8}] [{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{2,3,5},{0,2,6},{3,6},{5,6},{0,7},{2,7},{4,5,7},{1,6,7},{2,8},{0,1,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered427 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 427) T=TwentyFiveEightLow.Case427.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case427.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 427)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case427.support T pos))
  · decide +kernel
theorem completion428 : pairCompletion (big 428)=full 428 := by
  have same : big 428=([{0,2,6},{4,5,6},{3,5,7},{1,6,7},{2,3,8},{0,1,5,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,6},{4,5,6},{3,5,7},{1,6,7},{2,3,8},{0,1,5,8},{4,7,8}] [{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{2,5},{0,2,6},{3,6},{4,5,6},{0,7},{2,7},{3,5,7},{1,6,7},{2,3,8},{0,1,5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered428 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 428) T=TwentyFiveEightLow.Case428.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case428.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 428)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case428.support T pos))
  · decide +kernel
theorem completion429 : pairCompletion (big 429)=full 429 := by
  have same : big 429=([{2,3,4},{0,1,4,5},{0,2,6},{3,5,7},{1,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{0,1,4,5},{0,2,6},{3,5,7},{1,6,7},{5,6,8},{4,7,8}] [{1,2},{0,3},{1,3},{2,3,4},{2,5},{0,1,4,5},{0,2,6},{3,6},{4,6},{0,7},{2,7},{3,5,7},{1,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered429 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 429) T=TwentyFiveEightLow.Case429.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case429.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 429)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case429.support T pos))
  · decide +kernel
theorem completion430 : pairCompletion (big 430)=full 430 := by
  have same : big 430=([{0,1,4,5},{0,2,6},{3,5,6},{3,4,7},{1,6,7},{2,4,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{0,2,6},{3,5,6},{3,4,7},{1,6,7},{2,4,8},{5,7,8}] [{1,2},{0,3},{1,3},{2,3},{2,5},{0,1,4,5},{0,2,6},{4,6},{3,5,6},{0,7},{2,7},{3,4,7},{1,6,7},{0,8},{1,8},{3,8},{2,4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered430 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 430) T=TwentyFiveEightLow.Case430.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case430.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 430)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case430.support T pos))
  · decide +kernel
theorem completion431 : pairCompletion (big 431)=full 431 := by
  have same : big 431=([{0,1,4,5},{2,4,6},{3,4,7},{2,5,7},{0,6,7},{3,5,8},{1,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{2,4,6},{3,4,7},{2,5,7},{0,6,7},{3,5,8},{1,6,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{0,1,4,5},{3,6},{2,4,6},{5,6},{1,7},{3,4,7},{2,5,7},{0,6,7},{0,8},{2,8},{4,8},{3,5,8},{1,6,8},{7,8}]=true
  decide +kernel

theorem recovered431 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 431) T=TwentyFiveEightLow.Case431.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case431.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 431)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case431.support T pos))
  · decide +kernel
theorem completion432 : pairCompletion (big 432)=full 432 := by
  have same : big 432=([{1,2,4},{0,1,6},{3,5,6},{3,4,7},{2,5,7},{0,4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,4},{0,1,6},{3,5,6},{3,4,7},{2,5,7},{0,4,5,8},{6,7,8}] [{0,2},{0,3},{1,3},{2,3},{1,2,4},{1,5},{0,1,6},{2,6},{4,6},{3,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{1,8},{2,8},{3,8},{0,4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered432 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 432) T=TwentyFiveEightLow.Case432.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case432.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 432)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case432.support T pos))
  · decide +kernel
theorem completion433 : pairCompletion (big 433)=full 433 := by
  have same : big 433=([{1,2,4},{3,4,6},{1,5,6},{3,5,7},{0,6,7},{0,4,5,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,4},{3,4,6},{1,5,6},{3,5,7},{0,6,7},{0,4,5,8},{2,7,8}] [{0,1},{0,2},{0,3},{1,3},{2,3},{1,2,4},{2,5},{2,6},{3,4,6},{1,5,6},{1,7},{4,7},{3,5,7},{0,6,7},{1,8},{3,8},{0,4,5,8},{6,8},{2,7,8}]=true
  decide +kernel

theorem recovered433 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 433) T=TwentyFiveEightLow.Case433.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case433.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 433)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case433.support T pos))
  · decide +kernel
theorem completion434 : pairCompletion (big 434)=full 434 := by
  have same : big 434=([{0,2,3,5},{1,2,4,6},{4,5,7},{3,6,7},{1,3,8},{0,4,8},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,5},{1,2,4,6},{4,5,7},{3,6,7},{1,3,8},{0,4,8},{5,6,8},{2,7,8}] [{0,1},{3,4},{1,5},{0,2,3,5},{0,6},{1,2,4,6},{0,7},{1,7},{4,5,7},{3,6,7},{1,3,8},{0,4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered434 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 434) T=TwentyFiveEightLow.Case434.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case434.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 434)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case434.support T pos))
  · decide +kernel
theorem completion435 : pairCompletion (big 435)=full 435 := by
  have same : big 435=([{0,2,3,5},{1,2,4,6},{1,3,7},{0,4,7},{5,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,5},{1,2,4,6},{1,3,7},{0,4,7},{5,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,1},{3,4},{1,5},{0,2,3,5},{0,6},{1,2,4,6},{1,3,7},{0,4,7},{5,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered435 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 435) T=TwentyFiveEightLow.Case435.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case435.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 435)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case435.support T pos))
  · decide +kernel
theorem completion436 : pairCompletion (big 436)=full 436 := by
  have same : big 436=([{0,2,4,5},{3,5,6},{0,3,7},{1,4,7},{2,6,7},{1,2,3,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4,5},{3,5,6},{0,3,7},{1,4,7},{2,6,7},{1,2,3,8},{4,6,8},{5,7,8}] [{0,1},{3,4},{1,5},{0,2,4,5},{0,6},{1,6},{3,5,6},{0,3,7},{1,4,7},{2,6,7},{0,8},{1,2,3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered436 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 436) T=TwentyFiveEightLow.Case436.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case436.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 436)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case436.support T pos))
  · decide +kernel
theorem completion437 : pairCompletion (big 437)=full 437 := by
  have same : big 437=([{1,2,3,5},{3,4,6},{0,3,7},{4,5,7},{2,6,7},{0,2,4,8},{5,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,3,5},{3,4,6},{0,3,7},{4,5,7},{2,6,7},{0,2,4,8},{5,6,8},{1,7,8}] [{0,1},{1,4},{0,5},{1,2,3,5},{0,6},{1,6},{3,4,6},{0,3,7},{4,5,7},{2,6,7},{3,8},{0,2,4,8},{5,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered437 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 437) T=TwentyFiveEightLow.Case437.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case437.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 437)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case437.support T pos))
  · decide +kernel
theorem completion438 : pairCompletion (big 438)=full 438 := by
  have same : big 438=([{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}] [{0,1},{2,3},{1,4},{0,5},{0,6},{1,6},{2,4,6},{3,5,6},{0,2,7},{1,3,7},{4,5,7},{0,3,4,8},{1,2,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered438 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 438) T=TwentyFiveEightLow.Case438.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case438.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 438)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case438.support T pos))
  · decide +kernel
theorem completion439 : pairCompletion (big 439)=full 439 := by
  have same : big 439=([{0,1,3,5},{2,3,6},{4,5,6},{0,2,7},{3,4,7},{1,6,7},{1,2,4,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,5},{2,3,6},{4,5,6},{0,2,7},{3,4,7},{1,6,7},{1,2,4,8},{5,7,8}] [{0,4},{2,5},{0,1,3,5},{0,6},{2,3,6},{4,5,6},{0,2,7},{3,4,7},{1,6,7},{0,8},{3,8},{1,2,4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered439 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 439) T=TwentyFiveEightLow.Case439.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case439.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 439)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case439.support T pos))
  · decide +kernel
theorem completion440 : pairCompletion (big 440)=full 440 := by
  have same : big 440=([{0,4,5},{1,4,6},{2,5,7},{3,6,7},{0,1,8},{2,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{1,4,6},{2,5,7},{3,6,7},{0,1,8},{2,3,8},{5,6,8},{4,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,4},{3,4},{1,5},{3,5},{0,4,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,1,8},{2,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered440 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 440) T=TwentyFiveEightLow.Case440.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case440.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 440)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case440.support T pos))
  · decide +kernel
theorem completion441 : pairCompletion (big 441)=full 441 := by
  have same : big 441=([{0,4,5},{1,4,6},{0,1,7},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{1,4,6},{0,1,7},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,4},{3,4},{1,5},{3,5},{0,4,5},{0,6},{2,6},{1,4,6},{0,1,7},{2,3,7},{5,6,7},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered441 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 441) T=TwentyFiveEightLow.Case441.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case441.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 441)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case441.support T pos))
  · decide +kernel
theorem completion442 : pairCompletion (big 442)=full 442 := by
  have same : big 442=([{0,4,5},{1,4,6},{0,2,7},{1,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{1,4,6},{0,2,7},{1,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}] [{0,1},{1,2},{0,3},{2,3},{2,4},{3,4},{1,5},{3,5},{0,4,5},{0,6},{2,6},{1,4,6},{0,2,7},{1,3,7},{5,6,7},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered442 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 442) T=TwentyFiveEightLow.Case442.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case442.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 442)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case442.support T pos))
  · decide +kernel
theorem completion443 : pairCompletion (big 443)=full 443 := by
  have same : big 443=([{0,3,4},{1,3,5},{2,4,6},{0,1,7},{4,5,7},{3,6,7},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{2,4,6},{0,1,7},{4,5,7},{3,6,7},{5,6,8},{2,7,8}] [{0,2},{1,2},{2,3},{1,4},{0,3,4},{0,5},{2,5},{1,3,5},{0,6},{1,6},{2,4,6},{0,1,7},{4,5,7},{3,6,7},{0,8},{1,8},{3,8},{4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered443 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 443) T=TwentyFiveEightLow.Case443.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case443.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 443)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case443.support T pos))
  · decide +kernel
theorem completion444 : pairCompletion (big 444)=full 444 := by
  have same : big 444=([{0,4,5},{1,4,6},{2,5,7},{3,6,7},{1,2,8},{0,3,8},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{1,4,6},{2,5,7},{3,6,7},{1,2,8},{0,3,8},{5,6,8},{4,7,8}] [{0,1},{0,2},{1,3},{2,3},{2,4},{3,4},{1,5},{3,5},{0,4,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{2,5,7},{3,6,7},{1,2,8},{0,3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered444 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 444) T=TwentyFiveEightLow.Case444.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case444.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 444)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case444.support T pos))
  · decide +kernel
theorem completion445 : pairCompletion (big 445)=full 445 := by
  have same : big 445=([{0,4,5},{1,4,6},{0,2,7},{1,3,7},{5,6,7},{3,5,8},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{1,4,6},{0,2,7},{1,3,7},{5,6,7},{3,5,8},{2,6,8},{4,7,8}] [{0,1},{1,2},{0,3},{2,3},{2,4},{3,4},{1,5},{2,5},{0,4,5},{0,6},{3,6},{1,4,6},{0,2,7},{1,3,7},{5,6,7},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered445 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 445) T=TwentyFiveEightLow.Case445.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case445.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 445)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case445.support T pos))
  · decide +kernel
theorem completion446 : pairCompletion (big 446)=full 446 := by
  have same : big 446=([{2,3,4},{0,3,5},{1,4,6},{0,1,7},{4,5,7},{3,6,7},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{0,3,5},{1,4,6},{0,1,7},{4,5,7},{3,6,7},{5,6,8},{2,7,8}] [{0,2},{1,2},{1,3},{0,4},{2,3,4},{1,5},{2,5},{0,3,5},{0,6},{2,6},{1,4,6},{0,1,7},{4,5,7},{3,6,7},{0,8},{1,8},{3,8},{4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered446 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 446) T=TwentyFiveEightLow.Case446.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case446.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 446)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case446.support T pos))
  · decide +kernel
theorem completion447 : pairCompletion (big 447)=full 447 := by
  have same : big 447=([{0,4,5},{1,4,6},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{0,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5},{1,4,6},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{0,6,8},{1,7,8}] [{0,1},{0,2},{1,2},{0,3},{1,3},{2,3},{3,4},{1,5},{0,4,5},{2,6},{1,4,6},{5,6},{0,7},{4,7},{2,5,7},{3,6,7},{2,4,8},{3,5,8},{0,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered447 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 447) T=TwentyFiveEightLow.Case447.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case447.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 447)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case447.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
