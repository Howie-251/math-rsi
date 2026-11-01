import Aris4Math.ThirtyFour.TwentyFiveFiveLowInventory163
import Aris4Math.ThirtyFour.CachedChosenRows
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case3912
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(2781/2860 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3912
namespace Case3913
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(138/143 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3913
namespace Case3914
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(505/572 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3914
namespace Case3915
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(123/130 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3915
namespace Case3916
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(7745/8008 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3916
namespace Case3917
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,1,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(3779/4004 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3917
namespace Case3918
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,1,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(3797/4004 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3918
namespace Case3919
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(5331/5720 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3919
namespace Case3920
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(5631/5720 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3920
namespace Case3921
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(7339/8008 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3921
namespace Case3922
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(257/260 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3922
namespace Case3923
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(714/715 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3923
namespace Case3924
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,1,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(2545/2574 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3924
namespace Case3925
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(3951/4004 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3925
namespace Case3926
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(567/572 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3926
namespace Case3927
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(1125/1144 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3927
namespace Case3928
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(5523/5720 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3928
namespace Case3929
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(2711/2860 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3929
namespace Case3930
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(10611/11440 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3930
namespace Case3931
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(591/616 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3931
namespace Case3932
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(607/616 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3932
namespace Case3933
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(1117/1144 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3933
namespace Case3934
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(0/1 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3934
namespace Case3935
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(2279/2288 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case3935
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
