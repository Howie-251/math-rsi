import Aris4Math.ThirtyFour.TwentyFiveFiveLowInventory99
import Aris4Math.ThirtyFour.CachedChosenRows
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case2376
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(11267/11440 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2376
namespace Case2377
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(11183/11440 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2377
namespace Case2378
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(11267/11440 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2378
namespace Case2379
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(5683/5720 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2379
namespace Case2380
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(2279/2288 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2380
namespace Case2381
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(7633/8008 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2381
namespace Case2382
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(549/572 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2382
namespace Case2383
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,0,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(1063/1144 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2383
namespace Case2384
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(7369/8008 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2384
namespace Case2385
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(3841/4004 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2385
namespace Case2386
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(5419/5720 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2386
namespace Case2387
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,0,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(3547/4004 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2387
namespace Case2388
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(11021/11440 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2388
namespace Case2389
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(11021/11440 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2389
namespace Case2390
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(7547/8008 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2390
namespace Case2391
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(3767/4004 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2391
namespace Case2392
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(7547/8008 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2392
namespace Case2393
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(7587/8008 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2393
namespace Case2394
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(3881/4004 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2394
namespace Case2395
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(3881/4004 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2395
namespace Case2396
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(3845/4004 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2396
namespace Case2397
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(3767/4004 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2397
namespace Case2398
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(1975/2002 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2398
namespace Case2399
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(7587/8008 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case2399
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
