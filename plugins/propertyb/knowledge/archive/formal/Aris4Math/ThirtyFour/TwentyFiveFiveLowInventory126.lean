import Aris4Math.ThirtyFour.TwentyFiveFiveLowData126
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case3024
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{1,2,3},{1,4,5},{3,4,6},{0,1,7},{2,4,7},{0,2,8},{3,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3024
namespace Case3025
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2},{1,3,4},{2,4,5},{0,3,7},{1,6,7},{2,3,8},{4,6,8},{5,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3025
namespace Case3026
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,5},{2,4,5},{0,2,6},{3,4,6},{1,3,7},{1,2,8},{0,3,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3026
namespace Case3027
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2},{1,3,5},{2,4,5},{0,3,6},{3,4,7},{0,4,8},{1,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3027
namespace Case3028
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2},{0,3,5},{2,4,5},{1,3,6},{3,4,7},{0,4,8},{2,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3028
namespace Case3029
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2},{2,3,5},{0,4,5},{0,3,6},{1,4,7},{1,3,8},{4,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3029
namespace Case3030
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2},{0,3,5},{1,4,5},{0,4,6},{2,3,7},{1,3,8},{2,6,8},{4,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3030
namespace Case3031
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3},{0,1,4},{1,3,5},{1,2,6},{2,4,7},{0,5,8},{4,6,8},{3,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3031
namespace Case3032
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3},{1,4,6},{2,4,7},{3,6,7},{3,4,8},{0,5,8},{2,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3032
namespace Case3033
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3},{2,4,6},{3,4,7},{1,6,7},{1,4,8},{0,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3033
namespace Case3034
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3},{0,4,5},{1,4,6},{2,4,7},{3,6,7},{3,4,8},{2,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3034
namespace Case3035
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3},{1,4,6},{2,4,7},{3,6,7},{3,4,8},{1,5,8},{2,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3035
namespace Case3036
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{2,3,4},{0,2,6},{1,3,7},{4,6,7},{0,4,8},{1,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3036
namespace Case3037
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,4,5},{0,2,6},{3,4,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3037
namespace Case3038
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,6},{3,4,6},{1,3,7},{2,4,7},{2,3,8},{0,4,8},{1,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3038
namespace Case3039
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{2,3,4},{0,4,5},{0,2,6},{1,3,7},{4,6,7},{1,4,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3039
namespace Case3040
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,4},{1,4,5},{1,3,6},{2,3,7},{4,6,7},{3,4,8},{2,6,8},{0,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3040
namespace Case3041
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3},{2,4,6},{3,4,7},{1,6,7},{0,4,8},{1,5,8},{3,6,8},{2,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3041
namespace Case3042
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,3},{1,4,5},{0,4,6},{2,4,7},{3,6,7},{3,4,8},{2,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3042
namespace Case3043
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,2,4},{1,4,5},{0,3,6},{2,3,7},{4,6,7},{3,4,8},{2,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3043
namespace Case3044
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2},{3,4,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{0,5,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3044
namespace Case3045
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2},{1,3,4},{2,3,7},{4,6,7},{2,4,8},{0,5,8},{3,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3045
namespace Case3046
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2},{1,3,4},{0,4,5},{2,3,7},{4,6,7},{2,4,8},{3,6,8},{1,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3046
namespace Case3047
theorem completion : pairCompletion big=full.toFinset := by
  have same : big=([{0,1,2},{0,4,5},{3,4,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{6,7,8}] : List (Finset (Fin 9))).toFinset := by decide +kernel
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
end Case3047
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
