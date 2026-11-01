import Aris4Math.ThirtyFour.TwentyFiveFiveLowData189
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case4536
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3},{1,2,5},{3,4,6},{2,4,7},{0,4,8},{1,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4536
namespace Case4537
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3},{1,2,6},{3,4,6},{2,4,7},{0,4,8},{1,5,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4537
namespace Case4538
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,5},{0,2,6},{3,4,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4538
namespace Case4539
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,3,6},{4,5,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4539
namespace Case4540
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,3,4},{4,5,6},{2,3,7},{1,4,7},{1,3,8},{2,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4540
namespace Case4541
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,3,4},{1,3,6},{2,3,7},{1,4,7},{2,4,8},{5,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4541
namespace Case4542
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,3,4},{1,3,7},{2,4,7},{0,6,7},{2,3,8},{1,4,8},{5,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4542
namespace Case4543
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3},{1,4,6},{3,5,6},{2,4,7},{1,2,8},{0,4,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4543
namespace Case4544
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3},{1,2,6},{4,5,6},{3,4,7},{1,3,8},{0,4,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4544
namespace Case4545
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,2,3},{0,2,4},{4,5,6},{3,4,7},{0,3,8},{1,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4545
namespace Case4546
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,2,3},{0,2,4},{0,3,6},{3,4,7},{1,4,8},{5,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4546
namespace Case4547
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2},{0,3,6},{4,5,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4547
namespace Case4548
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3},{1,2,4},{3,5,6},{4,6,7},{1,3,8},{0,4,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4548
namespace Case4549
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3},{1,2,4},{3,4,6},{2,5,7},{1,3,8},{0,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4549
namespace Case4550
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3},{1,2,4},{3,4,6},{2,6,7},{1,3,8},{0,4,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4550
namespace Case4551
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,3},{0,2,4},{2,3,6},{1,4,6},{1,2,7},{3,5,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4551
namespace Case4552
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{2,4,5},{0,1,6},{0,4,7},{3,6,7},{3,4,8},{2,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4552
namespace Case4553
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,4},{3,4,6},{2,4,7},{0,6,7},{2,5,8},{1,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4553
namespace Case4554
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,6},{2,4,6},{3,4,7},{2,5,7},{0,4,8},{3,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4554
namespace Case4555
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,6},{2,4,6},{0,4,7},{3,5,7},{1,4,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4555
namespace Case4556
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,3},{2,4,5},{0,4,7},{3,6,7},{2,3,8},{4,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4556
namespace Case4557
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{2,3,5},{3,4,6},{0,1,7},{2,4,7},{0,3,8},{1,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4557
namespace Case4558
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,3,4},{2,3,5},{0,1,7},{4,6,7},{1,4,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4558
namespace Case4559
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,3},{2,3,4},{0,4,7},{3,6,7},{2,5,8},{4,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  decide +kernel
theorem recovered (T : Finset (Fin 9)) : inventory 34 (standard 5) (pairCompletion big) T=μ T := by
  rw [completion]
  apply TwentyFiveInventorySupport.eq_of_support 34 (standard 5) full μ
  · intro U nonzero
    have member := support U nonzero
    have checked : labels.all (fun t => (TwentyFiveInventorySupport.labels full).contains t)=true := by decide +kernel
    exact List.contains_iff.mp (List.all_eq_true.mp checked U member)
  · decide +kernel
end Case4559
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
