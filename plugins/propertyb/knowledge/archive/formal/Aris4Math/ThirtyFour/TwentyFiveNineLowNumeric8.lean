import Aris4Math.ThirtyFour.TwentyFiveNineLowData
namespace Aris4Math.ThirtyFour.TwentyFiveNineLow
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles CachedRows
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case99
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (3911/4290 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case99

namespace Case100
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (4021/4290 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case100

namespace Case101
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (5743/6435 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case101

namespace Case102
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (9771/11440 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case102

namespace Case103
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (394/429 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case103

namespace Case104
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (791/858 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case104

namespace Case105
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (791/858 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case105

namespace Case106
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (12737/12870 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case106

namespace Case107
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (12761/12870 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case107

namespace Case108
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (4243/4290 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case108

namespace Case109
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (4243/4290 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case109

namespace Case110
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (4271/4290 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case110
end Aris4Math.ThirtyFour.TwentyFiveNineLow
