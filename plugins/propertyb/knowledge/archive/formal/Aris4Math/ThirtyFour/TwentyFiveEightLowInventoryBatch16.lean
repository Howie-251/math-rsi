import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
open TwentyFiveEightLowInventoryData TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem completion512 : pairCompletion (big 512)=full 512 := by
  have same : big 512=([{0,2,3,5},{0,1,6},{4,5,6},{2,4,7},{3,6,7},{1,3,4,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,5},{0,1,6},{4,5,6},{2,4,7},{3,6,7},{1,3,4,8},{5,7,8}] [{1,2},{0,4},{1,5},{0,2,3,5},{0,1,6},{2,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,6,7},{0,8},{2,8},{1,3,4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered512 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 512) T=TwentyFiveEightLow.Case512.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case512.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 512)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case512.support T pos))
  · decide +kernel
theorem completion513 : pairCompletion (big 513)=full 513 := by
  have same : big 513=([{0,2,3,4},{1,4,6},{0,5,6},{4,5,7},{3,6,7},{1,3,5,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{1,4,6},{0,5,6},{4,5,7},{3,6,7},{1,3,5,8},{2,7,8}] [{0,1},{1,2},{0,2,3,4},{2,5},{2,6},{1,4,6},{0,5,6},{0,7},{1,7},{4,5,7},{3,6,7},{0,8},{4,8},{1,3,5,8},{6,8},{2,7,8}]=true
  decide +kernel

theorem recovered513 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 513) T=TwentyFiveEightLow.Case513.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case513.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 513)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case513.support T pos))
  · decide +kernel
theorem completion514 : pairCompletion (big 514)=full 514 := by
  have same : big 514=([{0,2,4,5},{3,6,7},{1,2,3,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,4,5},{3,6,7},{1,2,3,8},{4,6,8},{5,7,8}] [{0,1},{0,3},{1,4},{3,4},{1,5},{3,5},{0,2,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{4,7},{3,6,7},{0,8},{1,2,3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered514 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 514) T=TwentyFiveEightLow.Case514.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case514.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 514)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case514.support T pos))
  · decide +kernel
theorem completion515 : pairCompletion (big 515)=full 515 := by
  have same : big 515=([{0,2,3,5},{1,2,4,7},{3,6,7},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,5},{1,2,4,7},{3,6,7},{4,6,8},{5,7,8}] [{0,1},{1,3},{0,4},{3,4},{1,5},{0,2,3,5},{4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,2,4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered515 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 515) T=TwentyFiveEightLow.Case515.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case515.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 515)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case515.support T pos))
  · decide +kernel
theorem completion516 : pairCompletion (big 516)=full 516 := by
  have same : big 516=([{3,5,6},{0,2,3,7},{4,5,7},{1,2,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,5,6},{0,2,3,7},{4,5,7},{1,2,4,8},{6,7,8}] [{0,1},{1,3},{0,4},{3,4},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{4,6},{3,5,6},{1,7},{0,2,3,7},{4,5,7},{0,8},{3,8},{1,2,4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered516 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 516) T=TwentyFiveEightLow.Case516.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case516.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 516)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case516.support T pos))
  · decide +kernel
theorem completion517 : pairCompletion (big 517)=full 517 := by
  have same : big 517=([{0,2,3,4},{3,5,7},{4,6,7},{5,6,8},{1,2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,3,4},{3,5,7},{4,6,7},{5,6,8},{1,2,7,8}] [{0,1},{1,3},{1,4},{0,2,3,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{0,7},{3,5,7},{4,6,7},{0,8},{3,8},{4,8},{5,6,8},{1,2,7,8}]=true
  decide +kernel

theorem recovered517 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 517) T=TwentyFiveEightLow.Case517.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case517.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 517)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case517.support T pos))
  · decide +kernel
theorem completion518 : pairCompletion (big 518)=full 518 := by
  have same : big 518=([{2,5,6},{3,5,7},{4,6,7},{0,3,4,8},{1,2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,5,6},{3,5,7},{4,6,7},{0,3,4,8},{1,2,7,8}] [{0,1},{0,2},{1,3},{2,3},{1,4},{2,4},{0,5},{1,5},{4,5},{0,6},{1,6},{3,6},{2,5,6},{0,7},{3,5,7},{4,6,7},{0,3,4,8},{5,8},{6,8},{1,2,7,8}]=true
  decide +kernel

theorem recovered518 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 518) T=TwentyFiveEightLow.Case518.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case518.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 518)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case518.support T pos))
  · decide +kernel
theorem completion519 : pairCompletion (big 519)=full 519 := by
  have same : big 519=([{0,1,3,4},{2,5,6},{3,5,7},{4,6,7},{1,2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{2,5,6},{3,5,7},{4,6,7},{1,2,7,8}] [{0,2},{2,3},{2,4},{0,1,3,4},{0,5},{1,5},{4,5},{0,6},{1,6},{3,6},{2,5,6},{0,7},{3,5,7},{4,6,7},{0,8},{3,8},{4,8},{5,8},{6,8},{1,2,7,8}]=true
  decide +kernel

theorem recovered519 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 519) T=TwentyFiveEightLow.Case519.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case519.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 519)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case519.support T pos))
  · decide +kernel
theorem completion520 : pairCompletion (big 520)=full 520 := by
  have same : big 520=([{2,5,6},{0,1,2,7},{3,5,7},{4,6,7},{1,3,4,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,5,6},{0,1,2,7},{3,5,7},{4,6,7},{1,3,4,8}] [{0,3},{2,3},{0,4},{2,4},{0,5},{1,5},{4,5},{0,6},{1,6},{3,6},{2,5,6},{0,1,2,7},{3,5,7},{4,6,7},{0,8},{2,8},{1,3,4,8},{5,8},{6,8},{7,8}]=true
  decide +kernel

theorem recovered520 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 520) T=TwentyFiveEightLow.Case520.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case520.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 520)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case520.support T pos))
  · decide +kernel
theorem completion521 : pairCompletion (big 521)=full 521 := by
  have same : big 521=([{0,1,3,4},{2,3,5},{2,4,6},{0,5,6},{4,5,7},{3,6,7},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{2,3,5},{2,4,6},{0,5,6},{4,5,7},{3,6,7},{1,7,8}] [{0,2},{1,2},{0,1,3,4},{1,5},{2,3,5},{1,6},{2,4,6},{0,5,6},{0,7},{2,7},{4,5,7},{3,6,7},{0,8},{2,8},{3,8},{4,8},{5,8},{6,8},{1,7,8}]=true
  decide +kernel

theorem recovered521 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 521) T=TwentyFiveEightLow.Case521.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case521.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 521)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case521.support T pos))
  · decide +kernel
theorem completion522 : pairCompletion (big 522)=full 522 := by
  have same : big 522=([{0,1,3,4},{0,2,5},{2,3,6},{4,5,6},{3,5,7},{1,6,7},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{0,2,5},{2,3,6},{4,5,6},{3,5,7},{1,6,7},{4,7,8}] [{1,2},{2,4},{0,1,3,4},{1,5},{0,2,5},{0,6},{2,3,6},{4,5,6},{0,7},{2,7},{3,5,7},{1,6,7},{0,8},{1,8},{2,8},{3,8},{5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered522 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 522) T=TwentyFiveEightLow.Case522.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case522.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 522)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case522.support T pos))
  · decide +kernel
theorem completion523 : pairCompletion (big 523)=full 523 := by
  have same : big 523=([{0,1,3,4},{2,3,5},{2,4,6},{0,5,6},{1,5,7},{3,6,7},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3,4},{2,3,5},{2,4,6},{0,5,6},{1,5,7},{3,6,7},{4,7,8}] [{0,2},{1,2},{0,1,3,4},{2,3,5},{4,5},{1,6},{2,4,6},{0,5,6},{0,7},{2,7},{1,5,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered523 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 523) T=TwentyFiveEightLow.Case523.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case523.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 523)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case523.support T pos))
  · decide +kernel
theorem completion524 : pairCompletion (big 524)=full 524 := by
  have same : big 524=([{0,1,2,3,4},{3,5,6},{4,5,7},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2,3,4},{3,5,6},{4,5,7},{6,7,8}] [{0,1,2,3,4},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{4,6},{3,5,6},{0,7},{1,7},{2,7},{3,7},{4,5,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,8},{6,7,8}]=true
  decide +kernel

theorem recovered524 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 524) T=TwentyFiveEightLow.Case524.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case524.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 524)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case524.support T pos))
  · decide +kernel
theorem completion525 : pairCompletion (big 525)=full 525 := by
  have same : big 525=([{3,4,5},{0,1,5,6},{0,2,7},{3,6,7},{1,2,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,1,5,6},{0,2,7},{3,6,7},{1,2,8},{4,6,8},{5,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{2,5},{3,4,5},{2,6},{0,1,5,6},{1,7},{0,2,7},{4,7},{3,6,7},{0,8},{1,2,8},{3,8},{4,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered525 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 525) T=TwentyFiveEightLow.Case525.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case525.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 525)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case525.support T pos))
  · decide +kernel
theorem completion526 : pairCompletion (big 526)=full 526 := by
  have same : big 526=([{3,4,5},{0,2,6},{1,2,7},{5,6,7},{0,1,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,2,6},{1,2,7},{5,6,7},{0,1,5,8},{3,6,8},{4,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{2,5},{3,4,5},{1,6},{0,2,6},{4,6},{0,7},{1,2,7},{3,7},{5,6,7},{2,8},{0,1,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered526 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 526) T=TwentyFiveEightLow.Case526.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case526.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 526)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case526.support T pos))
  · decide +kernel
theorem completion527 : pairCompletion (big 527)=full 527 := by
  have same : big 527=([{0,2,6},{3,5,6},{1,2,7},{4,5,7},{3,4,8},{0,1,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,6},{3,5,6},{1,2,7},{4,5,7},{3,4,8},{0,1,5,8},{6,7,8}] [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{2,5},{1,6},{0,2,6},{4,6},{3,5,6},{0,7},{1,2,7},{3,7},{4,5,7},{2,8},{3,4,8},{0,1,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered527 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 527) T=TwentyFiveEightLow.Case527.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case527.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 527)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case527.support T pos))
  · decide +kernel
theorem completion528 : pairCompletion (big 528)=full 528 := by
  have same : big 528=([{0,1,4,5},{0,2,6},{3,4,6},{1,2,7},{5,6,7},{3,5,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{0,2,6},{3,4,6},{1,2,7},{5,6,7},{3,5,8},{4,7,8}] [{0,3},{1,3},{2,3},{2,4},{2,5},{0,1,4,5},{1,6},{0,2,6},{3,4,6},{0,7},{1,2,7},{3,7},{5,6,7},{0,8},{1,8},{2,8},{3,5,8},{6,8},{4,7,8}]=true
  decide +kernel

theorem recovered528 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 528) T=TwentyFiveEightLow.Case528.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case528.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 528)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case528.support T pos))
  · decide +kernel
theorem completion529 : pairCompletion (big 529)=full 529 := by
  have same : big 529=([{2,3,4},{0,1,4,5},{2,5,6},{3,5,7},{4,6,7},{0,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{0,1,4,5},{2,5,6},{3,5,7},{4,6,7},{0,6,8},{1,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3,4},{0,1,4,5},{1,6},{3,6},{2,5,6},{0,7},{2,7},{3,5,7},{4,6,7},{2,8},{3,8},{4,8},{5,8},{0,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered529 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 529) T=TwentyFiveEightLow.Case529.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case529.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 529)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case529.support T pos))
  · decide +kernel
theorem completion530 : pairCompletion (big 530)=full 530 := by
  have same : big 530=([{2,3,4},{0,1,6},{2,5,6},{3,5,7},{4,6,7},{0,4,5,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{0,1,6},{2,5,6},{3,5,7},{4,6,7},{0,4,5,8},{1,7,8}] [{0,2},{1,2},{0,3},{1,3},{1,4},{2,3,4},{1,5},{0,1,6},{3,6},{2,5,6},{0,7},{2,7},{3,5,7},{4,6,7},{2,8},{3,8},{0,4,5,8},{6,8},{1,7,8}]=true
  decide +kernel

theorem recovered530 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 530) T=TwentyFiveEightLow.Case530.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case530.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 530)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case530.support T pos))
  · decide +kernel
theorem completion531 : pairCompletion (big 531)=full 531 := by
  have same : big 531=([{3,4,5},{0,1,5,6},{0,2,7},{3,6,7},{2,5,8},{4,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,1,5,6},{0,2,7},{3,6,7},{2,5,8},{4,6,8},{1,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4,5},{2,6},{0,1,5,6},{0,2,7},{4,7},{5,7},{3,6,7},{0,8},{3,8},{2,5,8},{4,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered531 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 531) T=TwentyFiveEightLow.Case531.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case531.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 531)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case531.support T pos))
  · decide +kernel
theorem completion532 : pairCompletion (big 532)=full 532 := by
  have same : big 532=([{3,4,5},{0,1,5,6},{2,5,7},{3,6,7},{0,2,8},{4,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,1,5,6},{2,5,7},{3,6,7},{0,2,8},{4,6,8},{1,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4,5},{2,6},{0,1,5,6},{0,7},{4,7},{2,5,7},{3,6,7},{0,2,8},{3,8},{5,8},{4,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered532 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 532) T=TwentyFiveEightLow.Case532.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case532.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 532)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case532.support T pos))
  · decide +kernel
theorem completion533 : pairCompletion (big 533)=full 533 := by
  have same : big 533=([{3,4,5},{0,2,6},{2,5,7},{1,6,7},{0,1,5,8},{3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,2,6},{2,5,7},{1,6,7},{0,1,5,8},{3,6,8},{4,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4,5},{0,2,6},{4,6},{5,6},{0,7},{3,7},{2,5,7},{1,6,7},{2,8},{0,1,5,8},{3,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered533 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 533) T=TwentyFiveEightLow.Case533.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case533.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 533)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case533.support T pos))
  · decide +kernel
theorem completion534 : pairCompletion (big 534)=full 534 := by
  have same : big 534=([{0,2,6},{3,5,6},{4,5,7},{1,6,7},{3,4,8},{0,1,5,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,6},{3,5,6},{4,5,7},{1,6,7},{3,4,8},{0,1,5,8},{2,7,8}] [{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{2,5},{0,2,6},{4,6},{3,5,6},{0,7},{3,7},{4,5,7},{1,6,7},{3,4,8},{0,1,5,8},{6,8},{2,7,8}]=true
  decide +kernel

theorem recovered534 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 534) T=TwentyFiveEightLow.Case534.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case534.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 534)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case534.support T pos))
  · decide +kernel
theorem completion535 : pairCompletion (big 535)=full 535 := by
  have same : big 535=([{0,1,4,5},{0,2,6},{3,5,6},{2,4,7},{1,6,7},{3,4,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{0,2,6},{3,5,6},{2,4,7},{1,6,7},{3,4,8},{5,7,8}] [{1,2},{0,3},{1,3},{2,3},{2,5},{0,1,4,5},{0,2,6},{4,6},{3,5,6},{0,7},{3,7},{2,4,7},{1,6,7},{0,8},{1,8},{2,8},{3,4,8},{6,8},{5,7,8}]=true
  decide +kernel

theorem recovered535 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 535) T=TwentyFiveEightLow.Case535.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case535.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 535)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case535.support T pos))
  · decide +kernel
theorem completion536 : pairCompletion (big 536)=full 536 := by
  have same : big 536=([{0,1,4,5},{0,2,6},{2,4,7},{3,5,7},{1,6,7},{3,4,8},{5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,4,5},{0,2,6},{2,4,7},{3,5,7},{1,6,7},{3,4,8},{5,6,8}] [{1,2},{0,3},{1,3},{2,3},{2,5},{0,1,4,5},{0,2,6},{3,6},{4,6},{0,7},{2,4,7},{3,5,7},{1,6,7},{0,8},{1,8},{2,8},{3,4,8},{5,6,8},{7,8}]=true
  decide +kernel

theorem recovered536 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 536) T=TwentyFiveEightLow.Case536.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case536.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 536)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case536.support T pos))
  · decide +kernel
theorem completion537 : pairCompletion (big 537)=full 537 := by
  have same : big 537=([{2,3,4},{0,1,4,5},{2,5,6},{3,5,7},{0,6,7},{1,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{0,1,4,5},{2,5,6},{3,5,7},{0,6,7},{1,6,8},{4,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3,4},{0,1,4,5},{3,6},{4,6},{2,5,6},{1,7},{2,7},{3,5,7},{0,6,7},{0,8},{2,8},{3,8},{5,8},{1,6,8},{4,7,8}]=true
  decide +kernel

theorem recovered537 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 537) T=TwentyFiveEightLow.Case537.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case537.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 537)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case537.support T pos))
  · decide +kernel
theorem completion538 : pairCompletion (big 538)=full 538 := by
  have same : big 538=([{2,3,4},{0,1,6},{2,5,6},{1,4,7},{3,5,7},{0,4,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,3,4},{0,1,6},{2,5,6},{1,4,7},{3,5,7},{0,4,5,8},{6,7,8}] [{0,2},{1,2},{0,3},{1,3},{2,3,4},{1,5},{0,1,6},{3,6},{4,6},{2,5,6},{0,7},{2,7},{1,4,7},{3,5,7},{1,8},{2,8},{3,8},{0,4,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered538 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 538) T=TwentyFiveEightLow.Case538.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case538.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 538)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case538.support T pos))
  · decide +kernel
theorem completion539 : pairCompletion (big 539)=full 539 := by
  have same : big 539=([{1,2,4},{3,4,6},{1,5,6},{2,5,7},{0,6,7},{0,4,5,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{1,2,4},{3,4,6},{1,5,6},{2,5,7},{0,6,7},{0,4,5,8},{3,7,8}] [{0,1},{0,2},{0,3},{1,3},{2,3},{1,2,4},{3,5},{2,6},{3,4,6},{1,5,6},{1,7},{4,7},{2,5,7},{0,6,7},{1,8},{2,8},{0,4,5,8},{6,8},{3,7,8}]=true
  decide +kernel

theorem recovered539 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 539) T=TwentyFiveEightLow.Case539.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case539.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 539)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case539.support T pos))
  · decide +kernel
theorem completion540 : pairCompletion (big 540)=full 540 := by
  have same : big 540=([{3,4,5},{2,5,6},{0,2,7},{1,3,7},{4,6,7},{1,2,8},{0,4,8},{3,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{2,5,6},{0,2,7},{1,3,7},{4,6,7},{1,2,8},{0,4,8},{3,6,8},{5,7,8}] [{0,1},{0,3},{2,3},{1,4},{2,4},{0,5},{1,5},{3,4,5},{0,6},{1,6},{2,5,6},{0,2,7},{1,3,7},{4,6,7},{1,2,8},{0,4,8},{3,6,8},{5,7,8}]=true
  decide +kernel

theorem recovered540 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 540) T=TwentyFiveEightLow.Case540.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case540.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 540)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case540.support T pos))
  · decide +kernel
theorem completion541 : pairCompletion (big 541)=full 541 := by
  have same : big 541=([{3,4,5},{0,2,6},{1,3,6},{1,2,7},{0,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,4,5},{0,2,6},{1,3,6},{1,2,7},{0,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}] [{0,1},{0,3},{2,3},{1,4},{2,4},{0,5},{1,5},{3,4,5},{0,2,6},{1,3,6},{1,2,7},{0,4,7},{5,6,7},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]=true
  decide +kernel

theorem recovered541 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 541) T=TwentyFiveEightLow.Case541.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case541.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 541)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case541.support T pos))
  · decide +kernel
theorem completion542 : pairCompletion (big 542)=full 542 := by
  have same : big 542=([{0,2,6},{1,3,6},{4,5,6},{1,2,7},{0,4,7},{3,5,7},{3,4,8},{2,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,2,6},{1,3,6},{4,5,6},{1,2,7},{0,4,7},{3,5,7},{3,4,8},{2,5,8},{6,7,8}] [{0,1},{0,3},{2,3},{1,4},{2,4},{0,5},{1,5},{0,2,6},{1,3,6},{4,5,6},{1,2,7},{0,4,7},{3,5,7},{0,8},{1,8},{3,4,8},{2,5,8},{6,7,8}]=true
  decide +kernel

theorem recovered542 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 542) T=TwentyFiveEightLow.Case542.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case542.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 542)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case542.support T pos))
  · decide +kernel
theorem completion543 : pairCompletion (big 543)=full 543 := by
  have same : big 543=([{2,4,5},{1,2,6},{0,3,6},{0,2,7},{3,4,7},{5,6,7},{3,5,8},{4,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{2,4,5},{1,2,6},{0,3,6},{0,2,7},{3,4,7},{5,6,7},{3,5,8},{4,6,8},{1,7,8}] [{0,1},{1,3},{2,3},{0,4},{1,4},{0,5},{1,5},{2,4,5},{1,2,6},{0,3,6},{0,2,7},{3,4,7},{5,6,7},{0,8},{2,8},{3,5,8},{4,6,8},{1,7,8}]=true
  decide +kernel

theorem recovered543 : ∀ T : Finset (Fin 9),
    inventory 34 (standard 8) (full 543) T=TwentyFiveEightLow.Case543.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : TwentyFiveEightLow.Case543.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 543)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveEightLow.Case543.support T pos))
  · decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
