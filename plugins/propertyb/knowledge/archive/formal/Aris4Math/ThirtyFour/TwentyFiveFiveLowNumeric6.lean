import Aris4Math.ThirtyFour.TwentyFiveFiveLowInventory6
import Aris4Math.ThirtyFour.CachedChosenRows
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case144
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(5509/5720 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case144
namespace Case145
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,1,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(7503/8008 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case145
namespace Case146
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(11117/11440 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case146
namespace Case147
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(11117/11440 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case147
namespace Case148
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,1,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(1889/2002 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case148
namespace Case149
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,1,1,1,0,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(34/35 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case149
namespace Case150
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(145/154 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case150
namespace Case151
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,1,1,1,0,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(34/35 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case151
namespace Case152
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(145/154 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case152
namespace Case153
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(942/1001 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case153
namespace Case154
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(565/572 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case154
namespace Case155
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(565/572 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case155
namespace Case156
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(565/572 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case156
namespace Case157
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(3973/4004 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case157
namespace Case158
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(1895/2002 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case158
namespace Case159
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(10877/11440 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case159
namespace Case160
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(553/572 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case160
namespace Case161
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(1895/2002 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case161
namespace Case162
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(331/364 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case162
namespace Case163
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(5509/5720 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case163
namespace Case164
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(7593/8008 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case164
namespace Case165
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(7593/8008 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case165
namespace Case166
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(10961/11440 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case166
namespace Case167
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1]
theorem value : CachedChosenRows.bound computed choices=(79/80 : ℚ) := by decide +kernel
 theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9↪Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile];exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [value];norm_num
 theorem safe : Safe (standard 5) big := of_counts (standard 5) big μ recovered propertyB_of_counts
end Case167
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
