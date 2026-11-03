import DegreeDiameter.Portfolio.SingleExtension
import Mathlib.Data.Fintype.Sum
import Mathlib.Data.Fintype.Prod

/-!
A generic radius-two counting helper. This module contains no concrete graph
data and assumes the actual bounded-walk diameter property only as an explicit
hypothesis. It does not certify any particular graph's upper diameter bound.
-/

namespace DegreeDiameter.Portfolio.OppositeGQSpread

open SimpleGraph

/-- If every neighbor is among `k` supplied forward steps, a nonempty graph of
diameter at most two has at most one root, `k` one-step endpoints, and `k * k`
two-step endpoints. Repetitions and non-neighbors in `forward` are harmless. -/
theorem diameter_two_card_le {V : Type*} [Fintype V] [Nonempty V]
    (G : SimpleGraph V) (k : Nat) (forward : V → Fin k → V)
    (cover : ∀ u v, G.Adj u v → ∃ i, forward u i = v)
    (hD : DiameterAtMost G 2) : Fintype.card V ≤ 1 + k + k * k := by
  classical
  let root : V := Classical.choice inferInstance
  let endpoint : (Unit ⊕ Fin k) ⊕ (Fin k × Fin k) → V
    | Sum.inl (Sum.inl _) => root
    | Sum.inl (Sum.inr i) => forward root i
    | Sum.inr (i, j) => forward (forward root i) j
  have onto : Function.Surjective endpoint := by
    intro v
    obtain ⟨p, hp⟩ := hD root v
    cases p with
    | nil => exact ⟨Sum.inl (Sum.inl ()), rfl⟩
    | cons h p =>
      obtain ⟨i, hi⟩ := cover _ _ h
      cases p with
      | nil => exact ⟨Sum.inl (Sum.inr i), hi⟩
      | cons h' p =>
        obtain ⟨j, hj⟩ := cover _ _ h'
        cases p with
        | nil =>
          refine ⟨Sum.inr (i, j), ?_⟩
          change forward (forward root i) j = _
          rw [hi, hj]
        | cons h'' p =>
          have hlen : p.length + 3 ≤ 2 := by
            simpa only [Walk.length_cons, Nat.add_assoc] using hp
          have hthree : 3 ≤ p.length + 3 := Nat.le_add_left 3 p.length
          exact False.elim ((by decide : ¬ (3 ≤ 2)) (hthree.trans hlen))
  have bound := Fintype.card_le_of_surjective endpoint onto
  simpa only [Fintype.card_sum, Fintype.card_unit, Fintype.card_fin,
    Fintype.card_prod] using bound

#check @diameter_two_card_le
#print axioms diameter_two_card_le

end DegreeDiameter.Portfolio.OppositeGQSpread
