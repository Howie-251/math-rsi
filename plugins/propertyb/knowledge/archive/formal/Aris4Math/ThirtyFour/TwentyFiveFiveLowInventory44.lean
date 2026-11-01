import Aris4Math.ThirtyFour.TwentyFiveFiveLowData44
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case1056
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{2,3,4},{1,2,6},{0,3,6},{0,2,7},{4,5,7},{1,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1056
namespace Case1057
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{3,4,5},{1,2,6},{0,3,6},{0,2,7},{4,6,7},{2,4,8},{1,5,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1057
namespace Case1058
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3},{1,2,6},{0,4,6},{3,4,7},{1,5,7},{4,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1058
namespace Case1059
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3},{1,2,6},{3,4,6},{2,4,7},{1,5,7},{4,5,8},{0,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1059
namespace Case1060
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{2,4,5},{0,2,6},{3,4,6},{0,3,7},{1,6,7},{2,3,8},{1,5,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1060
namespace Case1061
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2},{0,3,5},{1,4,6},{2,3,7},{4,5,7},{3,4,8},{2,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1061
namespace Case1062
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2},{1,3,4},{0,3,5},{2,4,7},{1,6,7},{4,5,8},{2,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1062
namespace Case1063
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2},{0,3,5},{1,4,6},{1,3,7},{2,4,7},{3,4,8},{2,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1063
namespace Case1064
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,5},{3,4,5},{2,3,6},{0,2,7},{1,4,7},{1,3,8},{2,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1064
namespace Case1065
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,3,4},{0,1,5},{2,3,6},{0,2,7},{4,6,7},{2,4,8},{3,5,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1065
namespace Case1066
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{2,3,4},{0,1,5},{0,2,7},{1,3,7},{4,6,7},{1,4,8},{3,5,8},{2,6,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1066
namespace Case1067
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,2,3},{0,1,5},{3,4,5},{0,2,7},{4,6,7},{1,4,8},{2,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1067
namespace Case1068
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,3,4},{0,1,5},{2,3,6},{0,2,7},{4,6,7},{1,2,8},{4,5,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1068
namespace Case1069
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,2,3},{0,1,5},{2,4,6},{0,2,7},{3,4,7},{1,4,8},{3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1069
namespace Case1070
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,2,3},{0,1,5},{2,4,5},{1,4,7},{3,6,7},{3,4,8},{2,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1070
namespace Case1071
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2},{3,4,5},{1,3,6},{2,4,7},{0,5,7},{1,4,8},{2,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1071
namespace Case1072
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2},{2,3,6},{1,4,6},{3,4,7},{0,5,7},{1,3,8},{4,5,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1072
namespace Case1073
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2},{1,3,4},{2,3,6},{2,4,7},{0,5,7},{4,5,8},{1,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1073
namespace Case1074
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,2,3},{2,4,5},{1,4,6},{0,1,7},{3,6,7},{3,4,8},{0,5,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1074
namespace Case1075
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{3,4,5},{1,2,6},{0,1,7},{2,3,7},{4,6,7},{1,3,8},{2,4,8},{0,5,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1075
namespace Case1076
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,5},{3,4,5},{1,4,6},{1,3,7},{2,6,7},{2,3,8},{0,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1076
namespace Case1077
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3},{1,4,5},{1,2,6},{2,4,7},{3,6,7},{3,5,8},{4,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1077
namespace Case1078
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,5},{0,3,6},{1,4,6},{2,3,7},{4,5,7},{3,4,8},{2,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1078
namespace Case1079
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,5},{2,3,6},{1,4,6},{1,3,7},{4,5,7},{3,4,8},{0,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case1079
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
