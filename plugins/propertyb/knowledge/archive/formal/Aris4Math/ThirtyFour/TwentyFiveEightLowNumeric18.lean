import Aris4Math.ThirtyFour.TwentyFiveEightLowData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLow
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles CachedRows
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case218
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (428/429 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case218

namespace Case219
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (54/55 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case219

namespace Case220
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (11179/11440 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case220

namespace Case221
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (2803/2860 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case221

namespace Case222
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (11179/11440 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case222

namespace Case223
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (2803/2860 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case223

namespace Case224
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (54/55 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case224

namespace Case225
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (79/80 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case225

namespace Case226
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (2803/2860 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case226

namespace Case227
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (79/80 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case227

namespace Case228
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (2803/2860 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case228

namespace Case229
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (2803/2860 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case229
end Aris4Math.ThirtyFour.TwentyFiveEightLow
