import Aris4Math.ThirtyFour.TwentyFiveFiveLowData331
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case7944
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{3,4,6},{0,2,5,6,7},{1,2,3,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7944
namespace Case7945
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3,5,6},{1,4,6,7},{2,4,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7945
namespace Case7946
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3,5,6},{2,4,7},{3,4,8},{1,6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7946
namespace Case7947
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,3,4,6},{0,2,5,6,7},{2,3,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7947
namespace Case7948
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{2,3,4},{0,2,5,6,7},{1,3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7948
namespace Case7949
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{3,4,7},{0,2,5,6,7},{2,4,8},{1,3,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7949
namespace Case7950
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,2,3,6},{2,4,7},{3,4,8},{0,5,6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7950
namespace Case7951
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2,3,5},{1,4,6,7},{2,4,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7951
namespace Case7952
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2,3,5},{2,4,7},{3,4,8},{1,6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7952
namespace Case7953
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,3,4,6},{0,1,2,5,7},{2,3,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7953
namespace Case7954
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{2,3,4},{0,1,2,5,7},{1,3,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7954
namespace Case7955
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{3,4,7},{0,1,2,5,7},{2,4,8},{1,3,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7955
namespace Case7956
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,2,3,6},{2,4,7},{3,4,8},{0,1,5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7956
namespace Case7957
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2,5,7},{3,4,6,7},{1,3,8},{2,4,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7957
namespace Case7958
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,3,4},{0,1,2,5,7},{2,4,8},{3,6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7958
namespace Case7959
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,2,4},{2,3,6,7},{3,4,8},{0,1,5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7959
namespace Case7960
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,2,3,5,6},{0,1,4,7},{2,4,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7960
namespace Case7961
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,2,3,5,6},{2,4,7},{3,4,8},{0,1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7961
namespace Case7962
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,3,4},{1,2,5,6,7},{2,3,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7962
namespace Case7963
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{2,3,4},{1,2,5,6,7},{0,1,3,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7963
namespace Case7964
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{3,4,7},{1,2,5,6,7},{0,1,3,8},{2,4,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7964
namespace Case7965
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2,3},{2,4,7},{3,4,8},{1,5,6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7965
namespace Case7966
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,3,4,7},{1,2,5,6,7},{1,3,8},{2,4,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7966
namespace Case7967
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,3,4},{1,2,5,6,7},{2,4,8},{0,3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case7967
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
