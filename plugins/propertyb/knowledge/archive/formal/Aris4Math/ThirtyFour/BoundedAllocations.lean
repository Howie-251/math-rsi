import Aris4Math.ThirtyThree.BoundedTraceFamilies

/-! A complete, capacity-pruned catalogue of bounded integer allocations.
The entries are local edge types, not edges of the original hypergraph.
The caller supplies the actual type multiplicities and incidence budgets. -/

namespace Aris4Math.ThirtyFour.BoundedAllocations

variable {α β : Type*} [Fintype β]

/-- For each `(a,b)` choose an integer between zero and b, while respecting
every remaining capacity. Returned values follow the input list order. -/
def enumerate (cost : α → β → ℕ) : List (α × ℕ) → (β → ℕ) → List (List ℕ)
  | [], _ => [[]]
  | (a,b) :: rest, cap =>
    (List.range (b+1)).flatMap fun k =>
      if ∀ j, k * cost a j ≤ cap j then
        (enumerate cost rest (fun j => cap j-k*cost a j)).map (List.cons k)
      else []

/-- No allocation with these actual bounds and budgets is omitted by the
recursive capacity pruning. No search-success assumption is required. -/
theorem mem_enumerate (cost : α → β → ℕ) (entries : List (α × ℕ))
    (cap : β → ℕ) (value : α → ℕ)
    (bounds : ∀ e ∈ entries, value e.1 ≤ e.2)
    (budget : ∀ j, (entries.map (fun e => value e.1 * cost e.1 j)).sum ≤ cap j) :
    entries.map (fun e => value e.1) ∈ enumerate cost entries cap := by
  induction entries generalizing cap with
  | nil => simp [enumerate]
  | cons e rest ih =>
    rcases e with ⟨a,b⟩
    have bound : value a ≤ b := bounds (a,b) List.mem_cons_self
    have used (j : β) : value a * cost a j ≤ cap j := by
      have h := budget j
      simp only [List.map_cons,List.sum_cons] at h
      omega
    have bounds' : ∀ e ∈ rest, value e.1 ≤ e.2 := by
      intro e he
      exact bounds e (List.mem_cons_of_mem _ he)
    have budget' (j : β) :
        (rest.map (fun e => value e.1 * cost e.1 j)).sum ≤ cap j-value a*cost a j := by
      have h := budget j
      simp only [List.map_cons,List.sum_cons] at h
      omega
    have tail := ih (fun j => cap j-value a*cost a j) bounds' budget'
    change value a :: rest.map (fun e => value e.1) ∈ _
    apply List.mem_flatMap.mpr
    refine ⟨value a,List.mem_range.mpr (by omega),?_⟩
    rw [if_pos used]
    exact List.mem_map.mpr ⟨rest.map (fun e => value e.1),tail,rfl⟩

section Decode
variable [DecidableEq α]

/-- Read a catalogue allocation back as a function on local types. -/
def decode : List (α × ℕ) → List ℕ → α → ℕ
  | (a,_) :: rest, k :: values, x =>
      if x=a then k else decode rest values x
  | _, _, _ => 0

theorem decode_map (entries : List (α × ℕ)) (value : α → ℕ) (a : α) :
    decode entries (entries.map (fun e => value e.1)) a =
      if a ∈ entries.map Prod.fst then value a else 0 := by
  induction entries with
  | nil => simp [decode]
  | cons e rest ih =>
    rcases e with ⟨x,b⟩
    by_cases h : a=x
    · simp [decode,h]
    · change (if a=x then value x else decode rest (rest.map (fun e => value e.1)) a) =
        if a ∈ x :: rest.map Prod.fst then value a else 0
      rw [if_neg h, ih]
      by_cases mem : a ∈ rest.map Prod.fst
      · rw [if_pos mem, if_pos (List.mem_cons_of_mem x mem)]
      · have absent : a ∉ x :: rest.map Prod.fst := by
          simp only [List.mem_cons, h, false_or, mem, not_false_eq_true]
        rw [if_neg mem, if_neg absent]

/-- Recover the actual function, including every zero type outside the
support. Repeated entries need no extra premise: they store the same value. -/
theorem decode_actual (entries : List (α × ℕ)) (value : α → ℕ)
    (support : ∀ a, a ∉ entries.map Prod.fst → value a=0) (a : α) :
    decode entries (entries.map (fun e => value e.1)) a=value a := by
  rw [decode_map]
  by_cases h : a ∈ entries.map Prod.fst
  · simp [h]
  · simp [h,support a h]

end Decode

end Aris4Math.ThirtyFour.BoundedAllocations

#print axioms Aris4Math.ThirtyFour.BoundedAllocations.mem_enumerate
