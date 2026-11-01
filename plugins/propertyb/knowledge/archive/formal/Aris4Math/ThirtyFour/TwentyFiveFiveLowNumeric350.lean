import Aris4Math.ThirtyFour.TwentyFiveFiveLowInventory350
import Aris4Math.ThirtyFour.CachedChosenRows
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case8400
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(10969/11440 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8400
namespace Case8401
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,0,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(1039/1144 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8401
namespace Case8402
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(1889/2002 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8402
namespace Case8403
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,0,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(7589/8008 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8403
namespace Case8404
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(5639/5720 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8404
namespace Case8405
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(11263/11440 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8405
namespace Case8406
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(7947/8008 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8406
namespace Case8407
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(181/182 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8407
namespace Case8408
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(7947/8008 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8408
namespace Case8409
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(7769/8008 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8409
namespace Case8410
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(1097/1144 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8410
namespace Case8411
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(3947/4004 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8411
namespace Case8412
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(5639/5720 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8412
namespace Case8413
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(1421/1430 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8413
namespace Case8414
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(1889/2002 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8414
namespace Case8415
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(2729/2860 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8415
namespace Case8416
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(3891/4004 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8416
namespace Case8417
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(3947/4004 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8417
namespace Case8418
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(3947/4004 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8418
namespace Case8419
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,1,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(7765/8008 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8419
namespace Case8420
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,1,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(7765/8008 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8420
namespace Case8421
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(1033/1040 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8421
namespace Case8422
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,0,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(3813/4004 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8422
namespace Case8423
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(928/1001 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case8423
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
