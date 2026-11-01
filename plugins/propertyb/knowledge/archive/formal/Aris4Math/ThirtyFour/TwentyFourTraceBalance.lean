import Aris4Math.ThirtyThree.MultiLockRecovery

namespace Aris4Math.ThirtyFour.TwentyFourTraceBalance
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery

/-- Direct total/degree/pair balances imply the existing recovery formula.
The finite certificate evaluates each upper sum once, without nested recovery. -/
theorem recovered_eq_of_balance {n : ℕ} (low μ : Finset (Fin n) → ℕ)
    (balance : ∀ T, T.card ≤ 2 →
      μ T + (∑ U ∈ supers T (T.card+1), μ U) = low T) :
    ∀ T, recovered low μ T = μ T := by
  have pair_eq (T : Finset (Fin n)) (two : T.card=2) :
      recoveredPair low μ T = μ T := by
    have h := balance T (by omega)
    rw [two] at h
    change μ T + (∑ U ∈ supers T 3, μ U) = low T at h
    unfold recoveredPair
    omega
  have nonempty_eq (T : Finset (Fin n)) (nonempty : T.Nonempty) :
      recoveredNonempty low μ T = μ T := by
    by_cases large : 3 ≤ T.card
    · simp [recoveredNonempty,large]
    by_cases two : T.card=2
    · simpa only [recoveredNonempty,if_neg large,if_pos two] using pair_eq T two
    have one : T.card=1 := by have h := Finset.card_pos.mpr nonempty; omega
    have h := balance T (by omega)
    rw [one] at h
    change μ T + (∑ U ∈ supers T 2, μ U) = low T at h
    have eq : (∑ U ∈ supers T 2, if 3≤U.card then μ U else recoveredPair low μ U) =
        ∑ U ∈ supers T 2, μ U := by
      apply Finset.sum_congr rfl
      intro U hU
      have lower := (Finset.mem_filter.mp hU).2.2
      split_ifs with high
      · rfl
      · exact pair_eq U (by omega)
    simp only [recoveredNonempty,if_neg large,if_neg two,eq]
    omega
  intro T
  by_cases empty : T=∅
  · subst T
    have h := balance ∅ (by simp)
    rw [Finset.card_empty] at h
    change μ ∅ + (∑ U ∈ supers (∅ : Finset (Fin n)) 1, μ U) = low ∅ at h
    have eq : (∑ U ∈ supers (∅ : Finset (Fin n)) 1, recoveredNonempty low μ U) =
        ∑ U ∈ supers (∅ : Finset (Fin n)) 1, μ U := by
      apply Finset.sum_congr rfl
      intro U hU
      exact nonempty_eq U (Finset.card_pos.mp (Finset.mem_filter.mp hU).2.2)
    change low ∅ - (∑ U ∈ supers (∅ : Finset (Fin n)) 1, recoveredNonempty low μ U) = μ ∅
    rw [eq]
    omega
  · simp only [recovered,if_neg empty]
    exact nonempty_eq T (Finset.nonempty_iff_ne_empty.mpr empty)
end Aris4Math.ThirtyFour.TwentyFourTraceBalance
#print axioms Aris4Math.ThirtyFour.TwentyFourTraceBalance.recovered_eq_of_balance
