import Aris4Math.ThirtyFour.TwentyFourSlotAverageTable
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSlotAverageCache
open scoped BigOperators
open MixedLayoutApplication TwentyFourSlotAverageTable
variable {n m : ℕ} {L : Type*} [Fintype L]

def cachedFree (positions : Fin n↪Fin 24) (p : Numeric.Profile) : ℚ :=
  ∑k∈Finset.univ.filter (fun k=>¬∃j,positions j=k),
    min (CachedRows.cachedA p (k.val+1) true)
      (min (CachedRows.cachedA p (k.val+1) false) (CachedRows.cachedC p (k.val+1)))
def cachedA (positions : Fin n↪Fin 24) (p : Numeric.Profile) (j : Fin n) : ℚ :=
  min (CachedRows.cachedA p ((positions j).val+1) true)
    (CachedRows.cachedA p ((positions j).val+1) false)
def cachedC (positions : Fin n↪Fin 24) (p : Numeric.Profile) (j : Fin n) : ℚ :=
  CachedRows.cachedC p ((positions j).val+1)

theorem free_eq (positions : Fin n↪Fin 24) (p : Numeric.Profile)
    (valid : Numeric.validProfile p m) (nocap : p.emptyPairCap=none) :
    free positions p=cachedFree positions p := by
  unfold free cachedFree
  apply Finset.sum_congr rfl
  intro k _
  obtain ⟨ha,hb,hc⟩ := CachedRows.rows_eq p m (k.val+1) valid nocap
  rw [ha,hb,hc]

theorem contribution_eq (positions : L→Fin n↪Fin 24) (p : L→Numeric.Profile)
    (l : L) (s : Slot n)
    (valid : Numeric.validProfile (p l) m) (nocap : (p l).emptyPairCap=none) :
    contribution positions p l s =
      min (cachedA (positions l) (p l) s.center)
        (cachedC (positions l) (p l) s.center-
          (LocalProfiles.executableWeights positions p l s.center s.left s.right+
           LocalProfiles.executableWeights positions p l s.center s.right s.left)) := by
  unfold contribution a c cachedA cachedC TwentyFourActualSlotAverage.slotWeight
  obtain ⟨ha,hb,hc⟩ := CachedRows.rows_eq (p l) m ((positions l s.center).val+1) valid nocap
  rw [ha,hb,hc,LocalProfiles.weights_eq]
end Aris4Math.ThirtyFour.TwentyFourSlotAverageCache
