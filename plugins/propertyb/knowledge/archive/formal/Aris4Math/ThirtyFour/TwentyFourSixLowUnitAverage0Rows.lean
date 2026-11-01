import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Data
import Aris4Math.ThirtyFour.TwentyFourCachedCongruence
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
def referenceA : Fin 24→ℚ := ![(0/1:ℚ),(0/1:ℚ),(0/1:ℚ),(0/1:ℚ),(13/8568:ℚ),(65/8568:ℚ),(65/2856:ℚ),(65/1224:ℚ),(65/612:ℚ),(7/170:ℚ),(49/340:ℚ),(21/85:ℚ),(21/85:ℚ),(49/340:ℚ),(7/170:ℚ),(65/612:ℚ),(65/1224:ℚ),(65/2856:ℚ),(65/8568:ℚ),(13/8568:ℚ),(0/1:ℚ),(0/1:ℚ),(0/1:ℚ),(0/1:ℚ)]
def referenceC : Fin 24→ℚ := ![(0/1:ℚ),(0/1:ℚ),(0/1:ℚ),(0/1:ℚ),(143/14280:ℚ),(37/952:ℚ),(509/5712:ℚ),(467/2992:ℚ),(39/170:ℚ),(21/442:ℚ),(21/170:ℚ),(21/130:ℚ),(21/130:ℚ),(21/170:ℚ),(21/442:ℚ),(39/170:ℚ),(467/2992:ℚ),(509/5712:ℚ),(37/952:ℚ),(143/14280:ℚ),(0/1:ℚ),(0/1:ℚ),(0/1:ℚ),(0/1:ℚ)]
theorem geometry : ∀l,(p l).v=(p 0).v ∧ (p l).positions=(p 0).positions ∧
    (p l).types.toFinset=(p 0).types.toFinset := by
  intro l;fin_cases l <;> decide +kernel

theorem free_positions : ∀l,
    Finset.univ.filter (fun k : Fin 24=>¬∃j,positions l j=k)=
      Finset.univ.filter (fun k : Fin 24=>¬∃j,positions 0 j=k) := by
  intro l;fin_cases l <;> decide +kernel

theorem reference_rows : ∀k : Fin 24,
    min (CachedRows.cachedA (p 0) (k.val+1) true)
      (CachedRows.cachedA (p 0) (k.val+1) false)=referenceA k ∧
    CachedRows.cachedC (p 0) (k.val+1)=referenceC k := by
  intro k;fin_cases k <;> decide +kernel

theorem reference_free : TwentyFourSlotAverageCache.cachedFree (positions 0) (p 0)=freeValue 0 := by
  unfold TwentyFourSlotAverageCache.cachedFree
  decide +kernel

theorem stored_rows : ∀l j,referenceA (positions l j)=aValue l j ∧
    referenceC (positions l j)=cValue l j := by
  intro l;fin_cases l <;> decide +kernel

theorem rows_exact (l : Layout) : TwentyFourSlotAverageCache.cachedFree (positions l) (p l)=freeValue l ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions l) (p l) j=aValue l j ∧
      TwentyFourSlotAverageCache.cachedC (positions l) (p l) j=cValue l j) := by
  have eq (k : ℕ) := TwentyFourCachedCongruence.rows (p l) (p 0)
    (geometry l).1 (geometry l).2.1 (geometry l).2.2 k
  constructor
  · have same : TwentyFourSlotAverageCache.cachedFree (positions l) (p l)=
        TwentyFourSlotAverageCache.cachedFree (positions 0) (p 0) := by
      unfold TwentyFourSlotAverageCache.cachedFree
      rw [free_positions l]
      apply Finset.sum_congr rfl
      intro k _
      rw [(eq _).1 true,(eq _).1 false,(eq _).2]
    rw [same,reference_free]
    rfl
  · intro j
    unfold TwentyFourSlotAverageCache.cachedA TwentyFourSlotAverageCache.cachedC
    rw [(eq _).1 true,(eq _).1 false,(eq _).2,
      (reference_rows _).1,(reference_rows _).2]
    exact stored_rows l j
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0
