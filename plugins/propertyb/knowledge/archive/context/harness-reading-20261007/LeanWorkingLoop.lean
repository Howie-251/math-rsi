import Mathlib.Data.Finset.Card

-- Library-search result, checked in this project's pinned Mathlib.
#check @Finset.card_union_le
#check @Finset.card_union_of_disjoint

namespace HarnessReadingProbe

-- A real caller supplies the lemma's sets, typeclass and numeric bounds.
theorem union_bound {α : Type*} [DecidableEq α]
    (s t : Finset α) (hs : s.card ≤ 12) (ht : t.card ≤ 20) :
    (s ∪ t).card ≤ 32 := by
  exact (Finset.card_union_le s t).trans (Nat.add_le_add hs ht)

-- A proposed equality needs more than the upper-bound theorem's premises.
-- This witness refutes that overstrong route, not a separate original goal.
theorem overlapping_union_not_additive :
    (({0} : Finset Nat) ∪ {0}).card ≠
      ({0} : Finset Nat).card + ({0} : Finset Nat).card := by
  decide

#print union_bound
#print axioms union_bound
#print axioms overlapping_union_not_additive

end HarnessReadingProbe
