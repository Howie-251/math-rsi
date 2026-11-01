import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion352 : pairCompletion (big 352)=full 352 := by
  have same : big 352=([{0,4,6},{1,5,6},{2,4,7},{3,5,7},{0,1,2,3,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,6},{1,5,6},{2,4,7},{3,5,7},{0,1,2,3,8},{6,7,8}] [{1,4},{3,4},{0,5},{2,5},{4,5},{2,6},{3,6},{0,4,6},{1,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,1,2,3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered352 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 352) T=TwentyFiveEightLow.Case352.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case352.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 352)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case352.support T pos))
  · decide +kernel
theorem completion353 : pairCompletion (big 353)=full 353 := by
  have same : big 353=([{0,4,6},{2,5,6},{1,4,7},{3,6,7},{0,1,2,3,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,6},{2,5,6},{1,4,7},{3,6,7},{0,1,2,3,8},{5,7,8}] [{2,4},{3,4},{0,5},{1,5},{3,5},{4,5},{1,6},{0,4,6},{2,5,6},{0,7},{2,7},{1,4,7},{3,6,7},{0,1,2,3,8},{4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered353 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 353) T=TwentyFiveEightLow.Case353.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case353.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 353)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case353.support T pos))
  · decide +kernel
theorem completion354 : pairCompletion (big 354)=full 354 := by
  have same : big 354=([{0,1,2,3,4},{5,6,7},{2,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,4},{5,6,7},{2,5,8},{3,6,8},{4,7,8}] [{0,1,2,3,4},{0,5},{1,5},{3,5},{4,5},{0,6},{1,6},{2,6},{4,6},{0,7},{1,7},{2,7},{3,7},{5,6,7},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered354 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 354) T=TwentyFiveEightLow.Case354.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case354.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 354)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case354.support T pos))
  · decide +kernel
theorem completion355 : pairCompletion (big 355)=full 355 := by
  have same : big 355=([{0,1,2,3,4},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,4},{2,5,7},{3,6,7},{5,6,8},{4,7,8}] [{0,1,2,3,4},{0,5},{1,5},{3,5},{4,5},{0,6},{1,6},{2,6},{4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered355 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 355) T=TwentyFiveEightLow.Case355.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case355.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 355)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case355.support T pos))
  · decide +kernel
theorem completion356 : pairCompletion (big 356)=full 356 := by
  have same : big 356=([{4,5,6},{2,4,7},{3,5,7},{0,1,2,3,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{4,5,6},{2,4,7},{3,5,7},{0,1,2,3,8},{6,7,8}] [{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{3,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,1,2,3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered356 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 356) T=TwentyFiveEightLow.Case356.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case356.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 356)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case356.support T pos))
  · decide +kernel
theorem completion357 : pairCompletion (big 357)=full 357 := by
  have same : big 357=([{4,5,6},{1,4,7},{2,5,7},{3,6,7},{0,1,2,3,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{4,5,6},{1,4,7},{2,5,7},{3,6,7},{0,1,2,3,8}] [{0,4},{2,4},{3,4},{0,5},{1,5},{3,5},{0,6},{1,6},{2,6},{4,5,6},{0,7},{1,4,7},{2,5,7},{3,6,7},{0,1,2,3,8},{4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered357 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 357) T=TwentyFiveEightLow.Case357.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case357.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 357)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case357.support T pos))
  · decide +kernel
theorem completion358 : pairCompletion (big 358)=full 358 := by
  have same : big 358=([{0,1,2,3,4},{1,5,6,7},{2,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,4},{1,5,6,7},{2,5,8},{3,6,8},{4,7,8}] [{0,1,2,3,4},{0,5},{3,5},{4,5},{0,6},{2,6},{4,6},{0,7},{2,7},{3,7},{1,5,6,7},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered358 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 358) T=TwentyFiveEightLow.Case358.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case358.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 358)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case358.support T pos))
  · decide +kernel
theorem completion359 : pairCompletion (big 359)=full 359 := by
  have same : big 359=([{0,1,2,3,4},{2,5,7},{3,6,7},{1,5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,4},{2,5,7},{3,6,7},{1,5,6,8},{4,7,8}] [{0,1,2,3,4},{0,5},{3,5},{4,5},{0,6},{2,6},{4,6},{0,7},{1,7},{2,5,7},{3,6,7},{0,8},{2,8},{3,8},{1,5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered359 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 359) T=TwentyFiveEightLow.Case359.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case359.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 359)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case359.support T pos))
  · decide +kernel
theorem completion360 : pairCompletion (big 360)=full 360 := by
  have same : big 360=([{1,4,5,6},{2,4,7},{3,5,7},{0,1,2,3,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,5,6},{2,4,7},{3,5,7},{0,1,2,3,8},{6,7,8}] [{0,4},{3,4},{0,5},{2,5},{0,6},{2,6},{3,6},{1,4,5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,1,2,3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered360 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 360) T=TwentyFiveEightLow.Case360.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case360.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 360)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case360.support T pos))
  · decide +kernel
theorem completion361 : pairCompletion (big 361)=full 361 := by
  have same : big 361=([{1,4,7},{2,5,7},{3,6,7},{0,1,2,3,8},{4,5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,4,7},{2,5,7},{3,6,7},{0,1,2,3,8},{4,5,6,8}] [{0,4},{2,4},{3,4},{0,5},{1,5},{3,5},{0,6},{1,6},{2,6},{0,7},{1,4,7},{2,5,7},{3,6,7},{0,1,2,3,8},{4,5,6,8},{7,8}]=true
  decide +kernel

theorem recovered361 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 361) T=TwentyFiveEightLow.Case361.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case361.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 361)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case361.support T pos))
  · decide +kernel
theorem completion362 : pairCompletion (big 362)=full 362 := by
  have same : big 362=([{0,4,5,6},{1,4,7},{2,5,7},{3,6,7},{0,1,2,3,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,4,5,6},{1,4,7},{2,5,7},{3,6,7},{0,1,2,3,8}] [{2,4},{3,4},{1,5},{3,5},{1,6},{2,6},{0,4,5,6},{0,7},{1,4,7},{2,5,7},{3,6,7},{0,1,2,3,8},{4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered362 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 362) T=TwentyFiveEightLow.Case362.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case362.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 362)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case362.support T pos))
  · decide +kernel
theorem completion363 : pairCompletion (big 363)=full 363 := by
  have same : big 363=([{0,1,2,3,4},{5,6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,4},{5,6,7,8}] [{0,1,2,3,4},{0,5},{1,5},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{4,6},{0,7},{1,7},{2,7},{3,7},{4,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,6,7,8}]=true
  decide +kernel

theorem recovered363 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 363) T=TwentyFiveEightLow.Case363.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case363.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 363)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case363.support T pos))
  · decide +kernel
theorem completion364 : pairCompletion (big 364)=full 364 := by
  have same : big 364=([{4,5,6,7},{0,1,2,3,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{4,5,6,7},{0,1,2,3,8}] [{0,4},{1,4},{2,4},{3,4},{0,5},{1,5},{2,5},{3,5},{0,6},{1,6},{2,6},{3,6},{0,7},{1,7},{2,7},{3,7},{4,5,6,7},{0,1,2,3,8},{4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered364 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 364) T=TwentyFiveEightLow.Case364.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case364.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 364)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case364.support T pos))
  · decide +kernel
theorem completion365 : pairCompletion (big 365)=full 365 := by
  have same : big 365=([{0,1,4},{2,3,5},{2,4,6},{0,5,6},{4,5,7},{1,6,7},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{2,3,5},{2,4,6},{0,5,6},{4,5,7},{1,6,7},{3,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,1,4},{3,4},{1,5},{2,3,5},{3,6},{2,4,6},{0,5,6},{0,7},{2,7},{4,5,7},{1,6,7},{0,8},{1,8},{2,8},{4,8},{5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered365 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 365) T=TwentyFiveEightLow.Case365.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case365.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 365)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case365.support T pos))
  · decide +kernel
theorem completion366 : pairCompletion (big 366)=full 366 := by
  have same : big 366=([{0,1,4},{2,4,5},{3,4,6},{0,5,6},{3,5,7},{2,6,7},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{2,4,5},{3,4,6},{0,5,6},{3,5,7},{2,6,7},{1,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{0,1,4},{1,5},{2,4,5},{1,6},{3,4,6},{0,5,6},{0,7},{4,7},{3,5,7},{2,6,7},{0,8},{2,8},{3,8},{4,8},{5,8},{6,8},{1,7,8}]=true
  decide +kernel

theorem recovered366 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 366) T=TwentyFiveEightLow.Case366.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case366.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 366)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case366.support T pos))
  · decide +kernel
theorem completion367 : pairCompletion (big 367)=full 367 := by
  have same : big 367=([{0,1,4},{2,4,5},{3,4,6},{0,5,6},{1,5,7},{2,6,7},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{2,4,5},{3,4,6},{0,5,6},{1,5,7},{2,6,7},{3,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3},{0,1,4},{3,5},{2,4,5},{1,6},{3,4,6},{0,5,6},{0,7},{4,7},{1,5,7},{2,6,7},{0,8},{1,8},{2,8},{4,8},{5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered367 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 367) T=TwentyFiveEightLow.Case367.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case367.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 367)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case367.support T pos))
  · decide +kernel
theorem completion368 : pairCompletion (big 368)=full 368 := by
  have same : big 368=([{0,2,4},{0,1,5},{1,4,6},{3,5,6},{4,5,7},{2,6,7},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4},{0,1,5},{1,4,6},{3,5,6},{4,5,7},{2,6,7},{3,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,2,4},{3,4},{0,1,5},{2,5},{0,6},{1,4,6},{3,5,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,8},{1,8},{2,8},{4,8},{5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered368 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 368) T=TwentyFiveEightLow.Case368.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case368.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 368)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case368.support T pos))
  · decide +kernel
theorem completion369 : pairCompletion (big 369)=full 369 := by
  have same : big 369=([{1,3,5},{2,4,6},{0,5,6},{1,2,7},{4,5,7},{3,6,7},{3,4,8},{2,5,8},{1,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,3,5},{2,4,6},{0,5,6},{1,2,7},{4,5,7},{3,6,7},{3,4,8},{2,5,8},{1,6,8},{0,7,8}] [{0,1},{0,2},{0,3},{2,3},{0,4},{1,4},{1,3,5},{2,4,6},{0,5,6},{1,2,7},{4,5,7},{3,6,7},{3,4,8},{2,5,8},{1,6,8},{0,7,8}]=true
  decide +kernel

theorem recovered369 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 369) T=TwentyFiveEightLow.Case369.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case369.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 369)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case369.support T pos))
  · decide +kernel
theorem completion370 : pairCompletion (big 370)=full 370 := by
  have same : big 370=([{1,2,4},{1,3,5},{0,4,6},{2,5,6},{3,4,7},{0,5,7},{1,6,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,4},{1,3,5},{0,4,6},{2,5,6},{3,4,7},{0,5,7},{1,6,7},{4,5,8},{3,6,8},{2,7,8}] [{0,1},{0,2},{0,3},{2,3},{1,2,4},{1,3,5},{0,4,6},{2,5,6},{3,4,7},{0,5,7},{1,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered370 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 370) T=TwentyFiveEightLow.Case370.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case370.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 370)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case370.support T pos))
  · decide +kernel
theorem completion371 : pairCompletion (big 371)=full 371 := by
  have same : big 371=([{0,1,4},{0,2,5},{3,4,5},{1,3,6},{2,4,6},{2,3,7},{1,5,7},{0,6,7},{5,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{0,2,5},{3,4,5},{1,3,6},{2,4,6},{2,3,7},{1,5,7},{0,6,7},{5,6,8},{4,7,8}] [{1,2},{0,3},{0,1,4},{0,2,5},{3,4,5},{1,3,6},{2,4,6},{2,3,7},{1,5,7},{0,6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered371 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 371) T=TwentyFiveEightLow.Case371.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case371.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 371)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case371.support T pos))
  · decide +kernel
theorem completion372 : pairCompletion (big 372)=full 372 := by
  have same : big 372=([{0,2,4},{1,3,5},{0,1,6},{4,5,6},{3,4,7},{2,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4},{1,3,5},{0,1,6},{4,5,6},{3,4,7},{2,5,7},{6,7,8}] [{1,2},{0,3},{2,3},{1,4},{0,2,4},{0,5},{1,3,5},{0,1,6},{2,6},{3,6},{4,5,6},{0,7},{1,7},{3,4,7},{2,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered372 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 372) T=TwentyFiveEightLow.Case372.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case372.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 372)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case372.support T pos))
  · decide +kernel
theorem completion373 : pairCompletion (big 373)=full 373 := by
  have same : big 373=([{0,1,4},{0,2,5},{2,4,6},{3,5,6},{3,4,7},{1,6,7},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{0,2,5},{2,4,6},{3,5,6},{3,4,7},{1,6,7},{5,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,1,4},{1,5},{0,2,5},{4,5},{0,6},{2,4,6},{3,5,6},{0,7},{2,7},{3,4,7},{1,6,7},{0,8},{1,8},{2,8},{3,8},{4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered373 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 373) T=TwentyFiveEightLow.Case373.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case373.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 373)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case373.support T pos))
  · decide +kernel
theorem completion374 : pairCompletion (big 374)=full 374 := by
  have same : big 374=([{0,1,4},{2,3,5},{2,4,6},{0,5,6},{3,4,7},{1,6,7},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{2,3,5},{2,4,6},{0,5,6},{3,4,7},{1,6,7},{5,7,8}] [{0,2},{1,2},{0,3},{1,3},{0,1,4},{1,5},{2,3,5},{4,5},{3,6},{2,4,6},{0,5,6},{0,7},{2,7},{3,4,7},{1,6,7},{0,8},{1,8},{2,8},{3,8},{4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered374 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 374) T=TwentyFiveEightLow.Case374.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case374.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 374)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case374.support T pos))
  · decide +kernel
theorem completion375 : pairCompletion (big 375)=full 375 := by
  have same : big 375=([{1,2,5},{0,1,4,7},{3,6,7},{0,2,3,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,5},{0,1,4,7},{3,6,7},{0,2,3,8},{4,6,8},{5,7,8}] [{1,3},{2,4},{3,4},{0,5},{1,2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{5,6},{2,7},{0,1,4,7},{3,6,7},{1,8},{0,2,3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered375 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 375) T=TwentyFiveEightLow.Case375.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case375.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 375)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case375.support T pos))
  · decide +kernel
theorem completion376 : pairCompletion (big 376)=full 376 := by
  have same : big 376=([{1,2,5},{0,1,3,6},{0,2,4,7},{5,6,7},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,5},{0,1,3,6},{0,2,4,7},{5,6,7},{4,6,8},{3,7,8}] [{2,3},{1,4},{3,4},{0,5},{1,2,5},{3,5},{4,5},{2,6},{0,1,3,6},{1,7},{0,2,4,7},{5,6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered376 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 376) T=TwentyFiveEightLow.Case376.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case376.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 376)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case376.support T pos))
  · decide +kernel
theorem completion377 : pairCompletion (big 377)=full 377 := by
  have same : big 377=([{0,1,3,6},{4,5,6},{0,2,4,7},{3,5,7},{1,2,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,6},{4,5,6},{0,2,4,7},{3,5,7},{1,2,8},{6,7,8}] [{2,3},{1,4},{3,4},{0,5},{1,5},{2,5},{2,6},{0,1,3,6},{4,5,6},{1,7},{0,2,4,7},{3,5,7},{0,8},{1,2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered377 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 377) T=TwentyFiveEightLow.Case377.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case377.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 377)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case377.support T pos))
  · decide +kernel
theorem completion378 : pairCompletion (big 378)=full 378 := by
  have same : big 378=([{1,2,4},{3,5,6},{0,1,3,7},{4,6,7},{0,2,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,4},{3,5,6},{0,1,3,7},{4,6,7},{0,2,6,8},{5,7,8}] [{2,3},{0,4},{1,2,4},{3,4},{0,5},{1,5},{2,5},{4,5},{1,6},{3,5,6},{2,7},{0,1,3,7},{4,6,7},{1,8},{3,8},{4,8},{0,2,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered378 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 378) T=TwentyFiveEightLow.Case378.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case378.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 378)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case378.support T pos))
  · decide +kernel
theorem completion379 : pairCompletion (big 379)=full 379 := by
  have same : big 379=([{0,1,3,6},{2,4,6},{1,4,7},{5,6,7},{3,5,8},{0,2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,6},{2,4,6},{1,4,7},{5,6,7},{3,5,8},{0,2,7,8}] [{1,2},{2,3},{0,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,1,3,6},{2,4,6},{3,7},{1,4,7},{5,6,7},{1,8},{4,8},{3,5,8},{6,8},{0,2,7,8}]=true
  decide +kernel

theorem recovered379 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 379) T=TwentyFiveEightLow.Case379.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case379.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 379)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case379.support T pos))
  · decide +kernel
theorem completion380 : pairCompletion (big 380)=full 380 := by
  have same : big 380=([{0,1,4},{2,5,6},{3,5,7},{4,6,7},{0,3,6,8},{1,2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4},{2,5,6},{3,5,7},{4,6,7},{0,3,6,8},{1,2,7,8}] [{0,2},{1,3},{2,3},{0,1,4},{2,4},{3,4},{0,5},{1,5},{4,5},{1,6},{2,5,6},{0,7},{3,5,7},{4,6,7},{4,8},{5,8},{0,3,6,8},{1,2,7,8}]=true
  decide +kernel

theorem recovered380 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 380) T=TwentyFiveEightLow.Case380.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case380.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 380)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case380.support T pos))
  · decide +kernel
theorem completion381 : pairCompletion (big 381)=full 381 := by
  have same : big 381=([{0,1,2,5},{0,3,6},{4,5,7},{1,6,7},{3,4,8},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{0,3,6},{4,5,7},{1,6,7},{3,4,8},{5,6,8},{2,7,8}] [{1,3},{2,3},{0,4},{1,4},{2,4},{0,1,2,5},{3,5},{2,6},{0,3,6},{4,6},{0,7},{3,7},{4,5,7},{1,6,7},{0,8},{1,8},{3,4,8},{5,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered381 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 381) T=TwentyFiveEightLow.Case381.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case381.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 381)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case381.support T pos))
  · decide +kernel
theorem completion382 : pairCompletion (big 382)=full 382 := by
  have same : big 382=([{0,1,2,5},{0,3,6},{3,4,7},{5,6,7},{4,5,8},{1,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{0,3,6},{3,4,7},{5,6,7},{4,5,8},{1,6,8},{2,7,8}] [{1,3},{2,3},{0,4},{1,4},{2,4},{0,1,2,5},{3,5},{2,6},{0,3,6},{4,6},{0,7},{1,7},{3,4,7},{5,6,7},{0,8},{3,8},{4,5,8},{1,6,8},{2,7,8}]=true
  decide +kernel

theorem recovered382 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 382) T=TwentyFiveEightLow.Case382.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case382.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 382)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case382.support T pos))
  · decide +kernel
theorem completion383 : pairCompletion (big 383)=full 383 := by
  have same : big 383=([{0,1,2,5},{4,5,6},{3,4,7},{1,6,7},{0,3,8},{2,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,5},{4,5,6},{3,4,7},{1,6,7},{0,3,8},{2,6,8},{5,7,8}] [{1,3},{2,3},{0,4},{1,4},{2,4},{0,1,2,5},{3,5},{0,6},{3,6},{4,5,6},{0,7},{2,7},{3,4,7},{1,6,7},{1,8},{0,3,8},{4,8},{2,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered383 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 383) T=TwentyFiveEightLow.Case383.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case383.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 383)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case383.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
