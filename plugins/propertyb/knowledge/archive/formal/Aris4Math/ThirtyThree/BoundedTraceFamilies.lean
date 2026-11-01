import Aris4Math.ThirtyThree.MultiLockRecovery

/-! A finite local trace catalogue with a proved capacity-pruning rule.
The recursion branches on a trace, never on the edges of a whole hypergraph.
-/
namespace Aris4Math.ThirtyThree.BoundedTraceFamilies
open scoped BigOperators

variable {α β : Type*} [DecidableEq α] [Fintype β]

def enumerate (cost : α → β → ℕ) : List α → (β → ℕ) → List (Finset α)
  | [], _ => [∅]
  | a :: rest, cap =>
    enumerate cost rest cap ++
      if (∀ p, cost a p ≤ cap p) then
        (enumerate cost rest (fun p => cap p - cost a p)).map (insert a)
      else []

/-- Every family with the stated support and capacities occurs in the list.
Pruning is justified by the same actual capacities, not by a search heuristic. -/
theorem mem_enumerate (cost : α → β → ℕ) (candidates : List α)
    (cap : β → ℕ) (F : Finset α)
    (supported : ∀ a ∈ F, a ∈ candidates)
    (budget : ∀ p, ∑ a ∈ F, cost a p ≤ cap p) :
    F ∈ enumerate cost candidates cap := by
  induction candidates generalizing cap F with
  | nil =>
    have empty : F = ∅ := by
      apply Finset.eq_empty_iff_forall_notMem.mpr
      intro a ha
      simpa using supported a ha
    simp [enumerate,empty]
  | cons a rest ih =>
    by_cases ha : a ∈ F
    · have used (p : β) : cost a p ≤ cap p :=
        (Finset.single_le_sum (fun b _ => Nat.zero_le (cost b p)) ha).trans (budget p)
      have support' : ∀ b ∈ F.erase a, b ∈ rest := by
        intro b hb
        have h := supported b (Finset.mem_of_mem_erase hb)
        exact (List.mem_cons.mp h).resolve_left (Finset.mem_erase.mp hb).1
      have budget' : ∀ p, ∑ b ∈ F.erase a, cost b p ≤ cap p - cost a p := by
        intro p
        have hsum : (∑ b ∈ F.erase a, cost b p) + cost a p = ∑ b ∈ F, cost b p :=
          Finset.sum_erase_add F (fun b => cost b p) ha
        have hb := budget p
        omega
      have tail := ih (fun p => cap p - cost a p) (F.erase a) support' budget'
      apply List.mem_append.mpr
      right
      rw [if_pos used]
      exact List.mem_map.mpr ⟨F.erase a,tail,Finset.insert_erase ha⟩
    · have support' : ∀ b ∈ F, b ∈ rest := by
        intro b hb
        have h := supported b hb
        exact (List.mem_cons.mp h).resolve_left (by intro eq; subst b; exact ha hb)
      exact List.mem_append.mpr (Or.inl (ih cap F support' budget))

end Aris4Math.ThirtyThree.BoundedTraceFamilies

#print axioms Aris4Math.ThirtyThree.BoundedTraceFamilies.mem_enumerate
