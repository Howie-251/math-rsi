import Aris4Math.ThirtyFour.TwentyFiveEightLowData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLow
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles CachedRows
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case38
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (11251/11440 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case38

namespace Case39
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (867/880 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case39

namespace Case40
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (11251/11440 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case40

namespace Case41
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (867/880 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case41

namespace Case42
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (11251/11440 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case42

namespace Case43
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (867/880 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case43

namespace Case44
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (563/572 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case44

namespace Case45
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (2841/2860 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case45

namespace Case46
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (2799/2860 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case46

namespace Case47
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (11131/11440 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case47

namespace Case48
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (2799/2860 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case48

namespace Case49
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (2799/2860 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case49
end Aris4Math.ThirtyFour.TwentyFiveEightLow
