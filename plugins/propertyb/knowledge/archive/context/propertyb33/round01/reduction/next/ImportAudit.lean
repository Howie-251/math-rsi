import Aris4Math.ThirtyThree.Assembly
import Aris4Math.ThirtyThree.TwentyTwoStructure

#print Aris4Math.ThirtyThree.RemainingGoal
#check Aris4Math.ThirtyThree.target_iff_remaining_goal
#check Aris4Math.ThirtyThree.exists_two_locks_of_twenty_two
#print axioms Aris4Math.ThirtyThree.target_iff_remaining_goal
#print axioms Aris4Math.ThirtyThree.exists_two_locks_of_twenty_two

universe u

example (remaining : Aris4Math.ThirtyThree.RemainingGoal)
    (V : Type u) [Fintype V] (H : Aris4Math.Simple5Hypergraph V)
    (edges : H.edges.card ≤ 33) :
    ∃ color : V → Bool, ∀ edge ∈ H.edges,
      1 ≤ (edge.filter (fun x => color x = true)).card ∧
      (edge.filter (fun x => color x = true)).card ≤ 4 :=
  Aris4Math.ThirtyThree.target_of_remaining_goal remaining V H edges

example (H : Aris4Math.Simple5Hypergraph (Fin 22))
    (edges : H.edges.card = 33) (cover : H.PairCovering) :
    ∃ x y, x ≠ y ∧ H.codegree x y = 1 ∧
      6 ≤ H.degree x ∧ H.degree x ≤ H.degree y ∧ H.degree y ≤ 7 := by
  obtain ⟨x, y, hne, hone, degrees⟩ :=
    Aris4Math.ThirtyThree.exists_two_locks_of_twenty_two H cover edges (by simp)
  refine ⟨x, y, hne, hone, ?_⟩
  rcases degrees with h | h | h <;> omega
