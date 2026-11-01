import Aris4Math.ThirtyThree.TwentyStructure

#check Aris4Math.ThirtyThree.exists_two_locks_of_twenty
#print axioms Aris4Math.ThirtyThree.exists_two_locks_of_twenty

/-- Actual caller on the finite labels used by the main reduction. -/
example (H : Aris4Math.Simple5Hypergraph (Fin 20))
    (cover : H.PairCovering) (edges : H.edges.card = 33) :
    ∃ x y, x ≠ y ∧ H.codegree x y = 1 ∧
      ((H.degree x = 5 ∧ 5 ≤ H.degree y ∧ H.degree y ≤ 8) ∨
       (H.degree x = 6 ∧ 6 ≤ H.degree y ∧ H.degree y ≤ 9) ∨
       (H.degree x = 7 ∧ 7 ≤ H.degree y ∧ H.degree y ≤ 9) ∨
       (H.degree x = 8 ∧ H.degree y = 8)) :=
  Aris4Math.ThirtyThree.exists_two_locks_of_twenty H cover edges (by simp)

/-- The four integer ranges are precisely twelve ordered degree pairs. -/
example (a b : ℕ)
    (h : (a = 5 ∧ 5 ≤ b ∧ b ≤ 8) ∨
      (a = 6 ∧ 6 ≤ b ∧ b ≤ 9) ∨
      (a = 7 ∧ 7 ≤ b ∧ b ≤ 9) ∨ (a = 8 ∧ b = 8)) :
    (a = 5 ∧ b = 5) ∨ (a = 5 ∧ b = 6) ∨
    (a = 5 ∧ b = 7) ∨ (a = 5 ∧ b = 8) ∨
    (a = 6 ∧ b = 6) ∨ (a = 6 ∧ b = 7) ∨
    (a = 6 ∧ b = 8) ∨ (a = 6 ∧ b = 9) ∨
    (a = 7 ∧ b = 7) ∨ (a = 7 ∧ b = 8) ∨
    (a = 7 ∧ b = 9) ∨ (a = 8 ∧ b = 8) := by
  rcases h with ⟨rfl, hl, hu⟩ | ⟨rfl, hl, hu⟩ | ⟨rfl, hl, hu⟩ | ⟨rfl, rfl⟩
  · interval_cases b <;> simp
  · interval_cases b <;> simp
  · interval_cases b <;> simp
  · simp
