import Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3Data
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric
open scoped BigOperators
open TwentyThreeFiveLowStrictJoint3Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option synthInstance.maxSize 2000
theorem data_valid :
    (∀ T, 0<μ T → T ∈ support) ∧
    (∀ l, Numeric.validProfile (p l) 34) ∧
    (∀ l, (p l).emptyPairCap=none) ∧
    (∀ l j, (positions l j).val+1 ∈ (p l).correctionCenters) ∧
    (∀ l, 0 ≤ gamma l) ∧ (∑ l, gamma l)=1 ∧
    (∀ l j, 0 ≤ beta l j) ∧ (∀ l j, beta l j ≤ gamma l) ∧
    (∀ j q, 0 ≤ delta j q) ∧ (∀ j q, j ∉ R j q) ∧
    (∀ j q, quota j q ≤ (4*available support μ j (R j q)+2-(23-1-(R j q).card))/3) := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel

def cachedFree (l : Layout) : ℚ :=
  ∑ k ∈ Finset.univ.filter (fun k : Fin 23 => ¬ ∃ j, positions l j = k),
    min (CachedRows.cachedA (p l) (k.val+1) true)
      (min (CachedRows.cachedA (p l) (k.val+1) false) (CachedRows.cachedC (p l) (k.val+1)))
def cachedCenterA (l : Layout) (j : Fin 5) : ℚ :=
  min (CachedRows.cachedA (p l) ((positions l j).val+1) true)
    (CachedRows.cachedA (p l) ((positions l j).val+1) false)
def cachedCenterC (l : Layout) (j : Fin 5) : ℚ :=
  CachedRows.cachedC (p l) ((positions l j).val+1)

theorem free_eq (l : Layout) : free (positions l) (p l) = cachedFree l := by
  unfold free cachedFree
  apply Finset.sum_congr rfl
  intro k hk
  obtain ⟨ha,hb,hc⟩ := CachedRows.rows_eq (p l) 34 (k.val+1)
    (data_valid.2.1 l) (data_valid.2.2.1 l)
  rw [ha,hb,hc]
theorem a_eq (l : Layout) (j : Fin 5) : a positions p l j = cachedCenterA l j := by
  unfold a cachedCenterA
  obtain ⟨ha,hb,hc⟩ := CachedRows.rows_eq (p l) 34 ((positions l j).val+1)
    (data_valid.2.1 l) (data_valid.2.2.1 l)
  rw [ha,hb]
theorem c_eq (l : Layout) (j : Fin 5) : c positions p l j = cachedCenterC l j := by
  exact (CachedRows.rows_eq (p l) 34 ((positions l j).val+1)
    (data_valid.2.1 l) (data_valid.2.2.1 l)).2.2

/-- Exact proposed values; each entry is checked against its original profile below. -/
def freeValue : Layout → ℚ := ![(42/85:ℚ),(42/85:ℚ),(42/85:ℚ),(42/85:ℚ),(42/85:ℚ),(42/85:ℚ),(42/85:ℚ),(42/85:ℚ),(42/85:ℚ),(42/85:ℚ),(42/85:ℚ),(42/85:ℚ),(42/85:ℚ),(7/17:ℚ),(7/17:ℚ),(7/17:ℚ),(7/17:ℚ),(7/17:ℚ),(7/17:ℚ),(7/17:ℚ)]
def aValue : Layout → Fin 5 → ℚ := ![![(7/85:ℚ),(63/340:ℚ),(49/170:ℚ),(63/340:ℚ),(0/1:ℚ)],![(7/85:ℚ),(49/170:ℚ),(0/1:ℚ),(63/340:ℚ),(63/340:ℚ)],![(7/85:ℚ),(0/1:ℚ),(49/170:ℚ),(63/340:ℚ),(63/340:ℚ)],![(7/85:ℚ),(0/1:ℚ),(63/340:ℚ),(63/340:ℚ),(49/170:ℚ)],![(63/340:ℚ),(7/85:ℚ),(49/170:ℚ),(0/1:ℚ),(63/340:ℚ)],![(63/340:ℚ),(7/85:ℚ),(0/1:ℚ),(63/340:ℚ),(49/170:ℚ)],![(63/340:ℚ),(49/170:ℚ),(63/340:ℚ),(7/85:ℚ),(0/1:ℚ)],![(63/340:ℚ),(49/170:ℚ),(63/340:ℚ),(0/1:ℚ),(7/85:ℚ)],![(49/170:ℚ),(7/85:ℚ),(63/340:ℚ),(63/340:ℚ),(0/1:ℚ)],![(49/170:ℚ),(63/340:ℚ),(0/1:ℚ),(63/340:ℚ),(7/85:ℚ)],![(49/170:ℚ),(0/1:ℚ),(7/85:ℚ),(63/340:ℚ),(63/340:ℚ)],![(63/340:ℚ),(7/85:ℚ),(0/1:ℚ),(63/340:ℚ),(49/170:ℚ)],![(0/1:ℚ),(49/170:ℚ),(7/85:ℚ),(63/340:ℚ),(63/340:ℚ)],![(7/85:ℚ),(63/340:ℚ),(7/85:ℚ),(63/340:ℚ),(49/170:ℚ)],![(7/85:ℚ),(49/170:ℚ),(63/340:ℚ),(63/340:ℚ),(7/85:ℚ)],![(7/85:ℚ),(7/85:ℚ),(49/170:ℚ),(63/340:ℚ),(63/340:ℚ)],![(63/340:ℚ),(49/170:ℚ),(7/85:ℚ),(63/340:ℚ),(7/85:ℚ)],![(49/170:ℚ),(7/85:ℚ),(7/85:ℚ),(63/340:ℚ),(63/340:ℚ)],![(49/170:ℚ),(63/340:ℚ),(7/85:ℚ),(7/85:ℚ),(63/340:ℚ)],![(49/170:ℚ),(63/340:ℚ),(7/85:ℚ),(7/85:ℚ),(63/340:ℚ)]]
def cValue : Layout → Fin 5 → ℚ := ![![(210/2431:ℚ),(1743/12155:ℚ),(1974/12155:ℚ),(1743/12155:ℚ),(0/1:ℚ)],![(210/2431:ℚ),(1974/12155:ℚ),(0/1:ℚ),(1743/12155:ℚ),(1743/12155:ℚ)],![(210/2431:ℚ),(0/1:ℚ),(1974/12155:ℚ),(1743/12155:ℚ),(1743/12155:ℚ)],![(210/2431:ℚ),(0/1:ℚ),(1743/12155:ℚ),(1743/12155:ℚ),(1974/12155:ℚ)],![(1743/12155:ℚ),(210/2431:ℚ),(1974/12155:ℚ),(0/1:ℚ),(1743/12155:ℚ)],![(1743/12155:ℚ),(210/2431:ℚ),(0/1:ℚ),(1743/12155:ℚ),(1974/12155:ℚ)],![(1743/12155:ℚ),(1974/12155:ℚ),(1743/12155:ℚ),(210/2431:ℚ),(0/1:ℚ)],![(1743/12155:ℚ),(1974/12155:ℚ),(1743/12155:ℚ),(0/1:ℚ),(210/2431:ℚ)],![(1974/12155:ℚ),(210/2431:ℚ),(1743/12155:ℚ),(1743/12155:ℚ),(0/1:ℚ)],![(1974/12155:ℚ),(1743/12155:ℚ),(0/1:ℚ),(1743/12155:ℚ),(210/2431:ℚ)],![(1974/12155:ℚ),(0/1:ℚ),(210/2431:ℚ),(1743/12155:ℚ),(1743/12155:ℚ)],![(1743/12155:ℚ),(210/2431:ℚ),(0/1:ℚ),(1743/12155:ℚ),(1974/12155:ℚ)],![(0/1:ℚ),(1974/12155:ℚ),(210/2431:ℚ),(1743/12155:ℚ),(1743/12155:ℚ)],![(210/2431:ℚ),(1743/12155:ℚ),(210/2431:ℚ),(1743/12155:ℚ),(1974/12155:ℚ)],![(210/2431:ℚ),(1974/12155:ℚ),(1743/12155:ℚ),(1743/12155:ℚ),(210/2431:ℚ)],![(210/2431:ℚ),(210/2431:ℚ),(1974/12155:ℚ),(1743/12155:ℚ),(1743/12155:ℚ)],![(1743/12155:ℚ),(1974/12155:ℚ),(210/2431:ℚ),(1743/12155:ℚ),(210/2431:ℚ)],![(1974/12155:ℚ),(210/2431:ℚ),(210/2431:ℚ),(1743/12155:ℚ),(1743/12155:ℚ)],![(1974/12155:ℚ),(1743/12155:ℚ),(210/2431:ℚ),(210/2431:ℚ),(1743/12155:ℚ)],![(1974/12155:ℚ),(1743/12155:ℚ),(210/2431:ℚ),(210/2431:ℚ),(1743/12155:ℚ)]]
end Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric
namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric
open scoped BigOperators
open TwentyThreeFiveLowStrictJoint3Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem rows_0 : cachedFree 0 = freeValue 0 ∧
    (∀ j : Fin 5, cachedCenterA 0 j = aValue 0 j ∧ cachedCenterC 0 j = cValue 0 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel

theorem rows_1 : cachedFree 1 = freeValue 1 ∧
    (∀ j : Fin 5, cachedCenterA 1 j = aValue 1 j ∧ cachedCenterC 1 j = cValue 1 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel

theorem rows_2 : cachedFree 2 = freeValue 2 ∧
    (∀ j : Fin 5, cachedCenterA 2 j = aValue 2 j ∧ cachedCenterC 2 j = cValue 2 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel

theorem rows_3 : cachedFree 3 = freeValue 3 ∧
    (∀ j : Fin 5, cachedCenterA 3 j = aValue 3 j ∧ cachedCenterC 3 j = cValue 3 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel

theorem rows_4 : cachedFree 4 = freeValue 4 ∧
    (∀ j : Fin 5, cachedCenterA 4 j = aValue 4 j ∧ cachedCenterC 4 j = cValue 4 j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric
#print axioms Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric.rows_4
