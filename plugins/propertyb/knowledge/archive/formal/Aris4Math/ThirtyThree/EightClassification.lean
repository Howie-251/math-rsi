import Aris4Math.BlockClassification
import Mathlib.Data.List.Forall2
import Mathlib.Tactic.FinCases

/-!
Coverage machinery for the eight-point local triple classification.
This module does not assert the Property B theorem.
-/

namespace Aris4Math.ThirtyThree.EightClassification

open BlockClassification

variable {α : Type*} [DecidableEq α]

/-- Add compatible candidates, retaining both the exclude and include branch. -/
def extensions (candidates : List (Finset α)) (chosen : Finset (Finset α)) :
    List (Finset (Finset α)) :=
  match candidates with
  | [] => [chosen]
  | B :: rest =>
    extensions rest chosen ++
      if ∀ C ∈ chosen, B ≠ C → (B ∩ C).card ≤ 1 then
        extensions rest (insert B chosen)
      else []

/-- Every actual linear family within the candidates occurs in the recursion.
The proof follows its actual membership decisions and never assumes a table. -/
theorem extensions_complete (candidates : List (Finset α))
    (chosen target : Finset (Finset α)) (contained : chosen ⊆ target)
    (remaining : target ⊆ chosen ∪ candidates.toFinset) (linear : Linear target) :
    target ∈ extensions candidates chosen := by
  induction candidates generalizing chosen with
  | nil =>
    have eq : target = chosen := Finset.Subset.antisymm (by simpa using remaining) contained
    simp [extensions, eq]
  | cons B rest ih =>
    by_cases mem : B ∈ target
    · have compatible : ∀ C ∈ chosen, B ≠ C → (B ∩ C).card ≤ 1 := by
        intro C hC ne
        exact linear B mem C (contained hC) ne
      have contained' : insert B chosen ⊆ target := Finset.insert_subset mem contained
      have remaining' : target ⊆ insert B chosen ∪ rest.toFinset := by
        intro C hC
        have hc := remaining hC
        simp only [List.toFinset_cons, Finset.mem_union, Finset.mem_insert] at hc ⊢
        rcases hc with h | h | h
        · exact Or.inl (Or.inr h)
        · exact Or.inl (Or.inl h)
        · exact Or.inr h
      have occurs := ih (insert B chosen) contained' remaining'
      change target ∈ extensions rest chosen ++
        (if ∀ C ∈ chosen, B ≠ C → (B ∩ C).card ≤ 1 then
          extensions rest (insert B chosen) else [])
      rw [if_pos compatible, List.mem_append]
      exact Or.inr occurs
    · have remaining' : target ⊆ chosen ∪ rest.toFinset := by
        intro C hC
        have hc := remaining hC
        simp only [List.toFinset_cons, Finset.mem_union, Finset.mem_insert] at hc ⊢
        rcases hc with h | h | h
        · exact Or.inl h
        · exact False.elim (mem (h ▸ hC))
        · exact Or.inr h
      have occurs := ih chosen contained remaining'
      exact List.mem_append_left _ occurs

/-- Three-element blocks in an eight-point linear family have degree at most 3. -/
theorem triple_degree_le_three (W : Finset α) (triples : Finset (Finset α))
    (eight : W.card = 8) (inside : ∀ B ∈ triples, B ⊆ W)
    (three : ∀ B ∈ triples, B.card = 3) (linear : Linear triples)
    (x : α) : (triples.filter (fun B => x ∈ B)).card ≤ 3 := by
  let star := triples.filter (fun B => x ∈ B)
  by_cases hx : x ∈ W
  · have disj : (↑star : Set (Finset α)).PairwiseDisjoint (fun B => B.erase x) := by
      intro B hB C hC hne
      exact erased_blocks_disjoint triples linear
        (Finset.mem_filter.mp hB).1 (Finset.mem_filter.mp hC).1 hne
        (Finset.mem_filter.mp hB).2 (Finset.mem_filter.mp hC).2
    have small : star.biUnion (fun B => B.erase x) ⊆ W.erase x := by
      intro y hy
      obtain ⟨B, hB, hy⟩ := Finset.mem_biUnion.mp hy
      exact Finset.mem_erase.mpr ⟨(Finset.mem_erase.mp hy).1,
        inside B (Finset.mem_filter.mp hB).1 (Finset.mem_of_mem_erase hy)⟩
    have bound := Finset.card_le_card small
    rw [Finset.card_biUnion disj] at bound
    have sum : (∑ B ∈ star, (B.erase x).card) = star.card * 2 := by
      apply Finset.sum_const_nat
      intro B hB
      have hcard := Finset.card_erase_add_one (Finset.mem_filter.mp hB).2
      have hb := three B (Finset.mem_filter.mp hB).1
      omega
    rw [sum, Finset.card_erase_of_mem hx, eight] at bound
    dsimp [star] at bound
    omega
  · have empty : star = ∅ := by
      apply Finset.eq_empty_iff_forall_notMem.mpr
      intro B hB
      exact hx (inside B (Finset.mem_filter.mp hB).1 (Finset.mem_filter.mp hB).2)
    change star.card ≤ 3
    simp [empty]

end Aris4Math.ThirtyThree.EightClassification

#print axioms Aris4Math.ThirtyThree.EightClassification.extensions_complete
#print axioms Aris4Math.ThirtyThree.EightClassification.triple_degree_le_three

namespace Aris4Math.ThirtyThree.EightClassification
abbrev Family8 := Finset (Finset (Fin 8))
def seed8 : Family8 := {{0, 1, 2}, {0, 3, 6}, {3, 4, 5}}
def candidates8 : List (Finset (Fin 8)) := [{0, 4, 7}, {0, 5, 7}, {1, 3, 7}, {1, 4, 6}, {1, 4, 7}, {1, 5, 6}, {1, 5, 7}, {1, 6, 7}, {2, 3, 7}, {2, 4, 6}, {2, 4, 7}, {2, 5, 6}, {2, 5, 7}, {2, 6, 7}, {4, 6, 7}, {5, 6, 7}]
def representative8 (k : Fin 14) : Family8 :=
  match k.val with
  | 0 => {{0, 6, 7}, {1, 5, 6}, {2, 3, 5}, {3, 4, 6}, {4, 5, 7}}
  | 1 => {{0, 6, 7}, {1, 3, 4}, {1, 5, 7}, {2, 3, 6}, {2, 4, 7}}
  | 2 => {{0, 6, 7}, {1, 3, 5}, {2, 3, 6}, {2, 5, 7}, {3, 4, 7}, {4, 5, 6}}
  | 3 => {{0, 6, 7}, {1, 4, 5}, {2, 3, 4}, {2, 5, 6}, {3, 5, 7}}
  | 4 => {{0, 6, 7}, {1, 2, 5}, {1, 4, 6}, {2, 3, 7}, {3, 5, 6}, {4, 5, 7}}
  | 5 => {{0, 6, 7}, {1, 3, 4}, {1, 5, 6}, {2, 3, 5}, {2, 4, 6}}
  | 6 => {{0, 6, 7}, {1, 3, 4}, {1, 5, 6}, {2, 3, 6}, {2, 4, 5}, {3, 5, 7}}
  | 7 => {{0, 6, 7}, {1, 3, 4}, {1, 5, 6}, {2, 3, 5}, {2, 4, 7}}
  | 8 => {{0, 6, 7}, {1, 2, 4}, {1, 3, 6}, {1, 5, 7}, {2, 3, 7}, {2, 5, 6}, {3, 4, 5}}
  | 9 => {{0, 4, 5}, {0, 6, 7}, {1, 3, 4}, {1, 5, 6}, {2, 3, 5}, {2, 4, 7}}
  | 10 => {{0, 4, 5}, {0, 6, 7}, {1, 3, 4}, {1, 5, 6}, {2, 3, 6}, {2, 4, 7}}
  | 11 => {{0, 4, 5}, {0, 6, 7}, {1, 3, 4}, {1, 5, 6}, {2, 3, 6}, {2, 4, 7}, {3, 5, 7}}
  | 12 => {{0, 4, 5}, {0, 6, 7}, {1, 2, 4}, {1, 3, 5}, {2, 3, 6}, {2, 5, 7}, {3, 4, 7}}
  | _ => {{0, 2, 3}, {0, 4, 5}, {0, 6, 7}, {1, 2, 4}, {1, 3, 6}, {1, 5, 7}, {2, 5, 6}, {3, 4, 7}}

abbrev RelabelWitness := Option (Fin 14 × (Fin 8 → Fin 8))
def witnesses8 : List RelabelWitness := [
  none,
  none,
  none,
  none,
  none,
  some (7, ![6, 0, 7, 1, 3, 4, 5, 2]),
  none,
  some (3, ![6, 0, 7, 2, 4, 3, 5, 1]),
  none,
  some (7, ![6, 0, 7, 1, 4, 3, 5, 2]),
  some (1, ![6, 0, 7, 3, 1, 4, 2, 5]),
  none,
  some (3, ![6, 0, 7, 2, 3, 4, 5, 1]),
  some (1, ![6, 0, 7, 3, 4, 1, 2, 5]),
  none,
  some (3, ![6, 0, 7, 5, 1, 4, 2, 3]),
  some (3, ![6, 0, 7, 5, 4, 1, 2, 3]),
  some (0, ![7, 0, 6, 5, 2, 3, 4, 1]),
  some (6, ![7, 0, 6, 3, 4, 1, 5, 2]),
  some (0, ![7, 0, 6, 5, 3, 2, 4, 1]),
  some (6, ![7, 0, 6, 3, 1, 4, 5, 2]),
  none,
  some (7, ![1, 3, 4, 6, 0, 7, 5, 2]),
  some (3, ![2, 4, 3, 6, 0, 7, 5, 1]),
  some (7, ![1, 3, 4, 6, 7, 0, 5, 2]),
  some (9, ![1, 3, 4, 6, 7, 0, 5, 2]),
  some (3, ![2, 4, 3, 6, 7, 0, 5, 1]),
  some (9, ![1, 3, 4, 6, 0, 7, 5, 2]),
  some (5, ![1, 3, 4, 6, 0, 7, 5, 2]),
  some (6, ![1, 4, 3, 6, 0, 7, 5, 2]),
  some (6, ![1, 4, 3, 6, 7, 0, 5, 2]),
  none,
  some (7, ![6, 7, 0, 1, 3, 4, 5, 2]),
  some (7, ![1, 4, 3, 6, 0, 7, 5, 2]),
  some (1, ![3, 1, 4, 6, 0, 7, 2, 5]),
  some (9, ![6, 7, 0, 1, 3, 4, 5, 2]),
  some (7, ![6, 1, 5, 7, 2, 4, 0, 3]),
  some (9, ![6, 1, 5, 7, 2, 4, 0, 3]),
  some (7, ![1, 6, 5, 4, 2, 7, 3, 0]),
  some (1, ![1, 3, 4, 7, 0, 6, 5, 2]),
  some (9, ![7, 6, 0, 4, 3, 1, 2, 5]),
  some (4, ![1, 2, 5, 6, 0, 7, 4, 3]),
  some (12, ![0, 6, 7, 4, 1, 2, 5, 3]),
  some (9, ![1, 6, 5, 4, 2, 7, 3, 0]),
  none,
  some (3, ![6, 7, 0, 2, 4, 3, 5, 1]),
  some (3, ![2, 3, 4, 6, 0, 7, 5, 1]),
  some (1, ![3, 4, 1, 6, 0, 7, 2, 5]),
  some (9, ![6, 0, 7, 1, 3, 4, 5, 2]),
  some (7, ![1, 5, 6, 4, 7, 2, 3, 0]),
  none,
  some (4, ![1, 4, 6, 2, 3, 7, 5, 0]),
  some (1, ![4, 3, 1, 7, 0, 6, 2, 5]),
  some (9, ![0, 6, 7, 4, 3, 1, 5, 2]),
  some (4, ![4, 1, 6, 7, 3, 2, 5, 0]),
  none,
  some (7, ![6, 7, 0, 1, 4, 3, 5, 2]),
  some (7, ![1, 4, 3, 6, 7, 0, 5, 2]),
  some (7, ![6, 1, 5, 7, 4, 2, 0, 3]),
  some (7, ![1, 6, 5, 4, 7, 2, 3, 0]),
  some (1, ![3, 1, 4, 6, 7, 0, 2, 5]),
  some (9, ![6, 7, 0, 1, 4, 3, 5, 2]),
  some (9, ![6, 1, 5, 7, 4, 2, 0, 3]),
  some (1, ![1, 3, 4, 7, 6, 0, 5, 2]),
  some (9, ![7, 6, 0, 4, 1, 3, 2, 5]),
  some (9, ![1, 6, 5, 4, 7, 2, 3, 0]),
  some (4, ![1, 2, 5, 6, 7, 0, 4, 3]),
  some (12, ![0, 6, 7, 4, 2, 1, 5, 3]),
  some (1, ![6, 7, 0, 3, 1, 4, 2, 5]),
  some (9, ![1, 4, 3, 6, 7, 0, 5, 2]),
  some (9, ![6, 5, 1, 7, 2, 4, 0, 3]),
  some (4, ![1, 6, 4, 2, 7, 3, 5, 0]),
  some (12, ![0, 4, 5, 6, 2, 3, 7, 1]),
  some (10, ![0, 6, 7, 4, 3, 1, 5, 2]),
  some (11, ![0, 6, 7, 4, 3, 1, 5, 2]),
  none,
  some (3, ![6, 7, 0, 2, 3, 4, 5, 1]),
  some (3, ![2, 3, 4, 6, 7, 0, 5, 1]),
  some (7, ![1, 5, 6, 4, 2, 7, 3, 0]),
  none,
  some (1, ![3, 4, 1, 6, 7, 0, 2, 5]),
  some (9, ![6, 0, 7, 1, 4, 3, 5, 2]),
  some (4, ![1, 4, 6, 2, 7, 3, 5, 0]),
  some (1, ![4, 3, 1, 7, 6, 0, 2, 5]),
  some (9, ![0, 6, 7, 4, 1, 3, 5, 2]),
  some (4, ![4, 1, 6, 7, 2, 3, 5, 0]),
  some (1, ![6, 7, 0, 3, 4, 1, 2, 5]),
  some (9, ![1, 4, 3, 6, 0, 7, 5, 2]),
  some (4, ![1, 6, 4, 2, 3, 7, 5, 0]),
  some (9, ![6, 5, 1, 7, 4, 2, 0, 3]),
  some (12, ![0, 5, 4, 6, 2, 3, 7, 1]),
  some (10, ![0, 6, 7, 4, 1, 3, 5, 2]),
  some (11, ![0, 6, 7, 4, 1, 3, 5, 2]),
  none,
  some (3, ![6, 7, 0, 5, 1, 4, 2, 3]),
  some (3, ![6, 7, 0, 5, 4, 1, 2, 3]),
  some (5, ![1, 4, 3, 6, 0, 7, 5, 2]),
  some (1, ![1, 4, 3, 7, 0, 6, 5, 2]),
  some (9, ![7, 0, 6, 4, 3, 1, 2, 5]),
  some (1, ![4, 1, 3, 7, 0, 6, 2, 5]),
  some (9, ![0, 7, 6, 4, 3, 1, 5, 2]),
  some (1, ![1, 4, 3, 7, 6, 0, 5, 2]),
  some (9, ![7, 0, 6, 4, 1, 3, 2, 5]),
  some (10, ![0, 7, 6, 4, 3, 1, 5, 2]),
  some (1, ![4, 1, 3, 7, 6, 0, 2, 5]),
  some (9, ![0, 7, 6, 4, 1, 3, 5, 2]),
  some (10, ![0, 7, 6, 4, 1, 3, 5, 2]),
  some (0, ![7, 6, 0, 5, 2, 3, 4, 1]),
  some (6, ![7, 6, 0, 3, 4, 1, 5, 2]),
  some (6, ![1, 3, 4, 6, 0, 7, 5, 2]),
  some (4, ![1, 5, 2, 6, 0, 7, 4, 3]),
  some (12, ![0, 7, 6, 4, 1, 2, 5, 3]),
  some (9, ![1, 5, 6, 4, 7, 2, 3, 0]),
  some (4, ![4, 6, 1, 7, 2, 3, 5, 0]),
  some (11, ![0, 7, 6, 4, 1, 3, 5, 2]),
  some (0, ![7, 6, 0, 5, 3, 2, 4, 1]),
  some (6, ![7, 6, 0, 3, 1, 4, 5, 2]),
  some (6, ![1, 3, 4, 6, 7, 0, 5, 2]),
  some (9, ![1, 5, 6, 4, 2, 7, 3, 0]),
  some (4, ![4, 6, 1, 7, 3, 2, 5, 0]),
  some (4, ![1, 5, 2, 6, 7, 0, 4, 3]),
  some (12, ![0, 7, 6, 4, 2, 1, 5, 3]),
  some (11, ![0, 7, 6, 4, 3, 1, 5, 2]),
  none,
  some (5, ![6, 0, 7, 1, 3, 4, 5, 2]),
  some (3, ![5, 1, 4, 6, 0, 7, 2, 3]),
  some (0, ![6, 0, 7, 3, 2, 5, 4, 1]),
  some (6, ![6, 0, 7, 1, 4, 3, 5, 2]),
  some (1, ![7, 0, 6, 1, 3, 4, 5, 2]),
  some (4, ![6, 0, 7, 1, 2, 5, 4, 3]),
  some (1, ![7, 0, 6, 4, 3, 1, 2, 5]),
  some (0, ![6, 0, 7, 5, 2, 3, 1, 4]),
  some (6, ![6, 0, 7, 3, 4, 1, 2, 5]),
  some (2, ![6, 0, 7, 3, 1, 5, 2, 4]),
  some (8, ![6, 0, 7, 1, 4, 2, 3, 5]),
  some (4, ![7, 0, 6, 5, 1, 2, 4, 3]),
  some (3, ![5, 4, 1, 6, 0, 7, 2, 3]),
  some (6, ![3, 4, 1, 7, 0, 6, 5, 2]),
  some (9, ![4, 3, 1, 7, 6, 0, 2, 5]),
  some (12, ![4, 1, 2, 0, 6, 7, 5, 3]),
  some (9, ![4, 3, 1, 0, 6, 7, 5, 2]),
  some (6, ![3, 4, 1, 6, 0, 7, 2, 5]),
  some (8, ![1, 4, 2, 6, 0, 7, 3, 5]),
  some (12, ![2, 1, 4, 7, 0, 6, 5, 3]),
  some (0, ![6, 7, 0, 3, 2, 5, 4, 1]),
  some (6, ![6, 7, 0, 1, 4, 3, 5, 2]),
  some (6, ![3, 1, 4, 7, 0, 6, 5, 2]),
  some (9, ![5, 1, 6, 2, 7, 4, 3, 0]),
  some (4, ![6, 4, 1, 3, 2, 7, 5, 0]),
  some (4, ![5, 1, 2, 7, 0, 6, 4, 3]),
  some (12, ![7, 0, 6, 2, 1, 4, 5, 3]),
  some (11, ![7, 0, 6, 3, 1, 4, 5, 2]),
  some (1, ![7, 6, 0, 1, 3, 4, 5, 2]),
  some (9, ![4, 1, 3, 7, 6, 0, 2, 5]),
  some (9, ![5, 6, 1, 2, 7, 4, 3, 0]),
  some (10, ![6, 0, 7, 3, 4, 1, 2, 5]),
  some (4, ![6, 1, 4, 7, 2, 3, 0, 5]),
  some (12, ![4, 0, 5, 2, 6, 3, 1, 7]),
  some (11, ![6, 0, 7, 3, 4, 1, 2, 5]),
  some (4, ![6, 7, 0, 1, 2, 5, 4, 3]),
  some (12, ![4, 2, 1, 0, 6, 7, 5, 3]),
  some (11, ![6, 7, 0, 1, 4, 3, 5, 2]),
  some (11, ![7, 6, 0, 4, 1, 3, 2, 5]),
  some (13, ![0, 2, 3, 7, 1, 5, 6, 4]),
  some (1, ![7, 6, 0, 4, 3, 1, 2, 5]),
  some (9, ![4, 1, 3, 0, 6, 7, 5, 2]),
  some (4, ![6, 1, 4, 3, 2, 7, 5, 0]),
  some (10, ![6, 0, 7, 1, 4, 3, 5, 2]),
  some (11, ![6, 0, 7, 1, 4, 3, 5, 2]),
  some (9, ![5, 6, 1, 4, 7, 2, 0, 3]),
  some (12, ![5, 0, 4, 2, 6, 3, 7, 1]),
  some (0, ![6, 7, 0, 5, 2, 3, 1, 4]),
  some (6, ![6, 7, 0, 3, 4, 1, 2, 5]),
  some (6, ![3, 1, 4, 6, 0, 7, 2, 5]),
  some (4, ![5, 1, 2, 6, 0, 7, 3, 4]),
  some (12, ![7, 0, 6, 4, 1, 2, 3, 5]),
  some (4, ![6, 4, 1, 7, 2, 3, 0, 5]),
  some (11, ![7, 0, 6, 4, 1, 3, 2, 5]),
  some (9, ![5, 1, 6, 4, 7, 2, 0, 3]),
  some (2, ![6, 7, 0, 3, 1, 5, 2, 4]),
  some (8, ![6, 7, 0, 1, 4, 2, 3, 5]),
  some (8, ![1, 2, 4, 6, 0, 7, 3, 5]),
  some (12, ![4, 5, 0, 2, 6, 3, 1, 7]),
  some (12, ![5, 4, 0, 2, 6, 3, 7, 1]),
  some (4, ![7, 6, 0, 5, 1, 2, 4, 3]),
  some (12, ![2, 4, 1, 7, 0, 6, 5, 3]),
  some (11, ![7, 6, 0, 3, 1, 4, 5, 2]),
  some (11, ![6, 7, 0, 3, 4, 1, 2, 5]),
  some (13, ![0, 2, 3, 5, 1, 7, 4, 6]),
  none,
  some (5, ![6, 0, 7, 1, 4, 3, 5, 2]),
  some (3, ![5, 1, 4, 6, 7, 0, 2, 3]),
  some (1, ![7, 0, 6, 1, 4, 3, 5, 2]),
  some (1, ![7, 0, 6, 4, 1, 3, 2, 5]),
  some (0, ![6, 0, 7, 3, 5, 2, 4, 1]),
  some (6, ![6, 0, 7, 1, 3, 4, 5, 2]),
  some (4, ![6, 0, 7, 1, 5, 2, 4, 3]),
  some (0, ![6, 0, 7, 5, 3, 2, 1, 4]),
  some (6, ![6, 0, 7, 3, 1, 4, 2, 5]),
  some (4, ![6, 0, 7, 5, 1, 2, 3, 4]),
  some (2, ![6, 0, 7, 3, 5, 1, 2, 4]),
  some (8, ![6, 0, 7, 1, 2, 4, 3, 5]),
  some (3, ![5, 4, 1, 6, 7, 0, 2, 3]),
  some (9, ![4, 3, 1, 7, 0, 6, 2, 5]),
  some (9, ![4, 3, 1, 0, 7, 6, 5, 2]),
  some (6, ![3, 4, 1, 7, 6, 0, 5, 2]),
  some (12, ![4, 1, 2, 0, 7, 6, 5, 3]),
  some (6, ![3, 4, 1, 6, 7, 0, 2, 5]),
  some (12, ![4, 1, 2, 7, 0, 6, 3, 5]),
  some (8, ![1, 4, 2, 6, 7, 0, 3, 5]),
  some (1, ![7, 6, 0, 1, 4, 3, 5, 2]),
  some (9, ![4, 1, 3, 7, 0, 6, 2, 5]),
  some (10, ![6, 0, 7, 3, 1, 4, 2, 5]),
  some (9, ![5, 6, 1, 2, 4, 7, 3, 0]),
  some (4, ![6, 1, 4, 7, 3, 2, 0, 5]),
  some (11, ![6, 0, 7, 3, 1, 4, 2, 5]),
  some (12, ![4, 0, 5, 2, 3, 6, 1, 7]),
  some (1, ![7, 6, 0, 4, 1, 3, 2, 5]),
  some (9, ![4, 1, 3, 0, 7, 6, 5, 2]),
  some (10, ![6, 0, 7, 1, 3, 4, 5, 2]),
  some (4, ![6, 1, 4, 3, 7, 2, 5, 0]),
  some (11, ![6, 0, 7, 1, 3, 4, 5, 2]),
  some (9, ![5, 6, 1, 4, 2, 7, 0, 3]),
  some (12, ![5, 0, 4, 2, 3, 6, 7, 1]),
  some (0, ![6, 7, 0, 3, 5, 2, 4, 1]),
  some (6, ![6, 7, 0, 1, 3, 4, 5, 2]),
  some (6, ![3, 1, 4, 7, 6, 0, 5, 2]),
  some (9, ![5, 1, 6, 2, 4, 7, 3, 0]),
  some (4, ![6, 4, 1, 3, 7, 2, 5, 0]),
  some (4, ![5, 1, 2, 7, 6, 0, 4, 3]),
  some (12, ![7, 0, 6, 2, 4, 1, 5, 3]),
  some (11, ![7, 0, 6, 3, 4, 1, 5, 2]),
  some (4, ![6, 7, 0, 1, 5, 2, 4, 3]),
  some (12, ![4, 2, 1, 0, 7, 6, 5, 3]),
  some (11, ![6, 7, 0, 1, 3, 4, 5, 2]),
  some (11, ![7, 6, 0, 4, 3, 1, 2, 5]),
  some (13, ![0, 2, 3, 7, 5, 1, 6, 4]),
  some (0, ![6, 7, 0, 5, 3, 2, 1, 4]),
  some (6, ![6, 7, 0, 3, 1, 4, 2, 5]),
  some (6, ![3, 1, 4, 6, 7, 0, 2, 5]),
  some (4, ![6, 4, 1, 7, 3, 2, 0, 5]),
  some (9, ![5, 1, 6, 4, 2, 7, 0, 3]),
  some (4, ![5, 1, 2, 6, 7, 0, 3, 4]),
  some (12, ![7, 0, 6, 4, 2, 1, 3, 5]),
  some (11, ![7, 0, 6, 4, 3, 1, 2, 5]),
  some (4, ![6, 7, 0, 5, 1, 2, 3, 4]),
  some (12, ![4, 2, 1, 7, 0, 6, 3, 5]),
  some (11, ![6, 7, 0, 3, 1, 4, 2, 5]),
  some (11, ![7, 6, 0, 3, 4, 1, 5, 2]),
  some (13, ![0, 2, 3, 5, 7, 1, 4, 6]),
  some (2, ![6, 7, 0, 3, 5, 1, 2, 4]),
  some (8, ![6, 7, 0, 1, 2, 4, 3, 5]),
  some (8, ![1, 2, 4, 6, 7, 0, 3, 5]),
  some (12, ![4, 5, 0, 2, 3, 6, 1, 7]),
  some (12, ![5, 4, 0, 2, 3, 6, 7, 1])
]

end Aris4Math.ThirtyThree.EightClassification

namespace Aris4Math.ThirtyThree.EightClassification

def Admissible8 (T : Family8) : Prop :=
  5 ≤ T.card ∧ ∀ x : Fin 8, ∃ B ∈ T, x ∈ B

instance (T : Family8) : Decidable (Admissible8 T) := by
  unfold Admissible8
  infer_instance

def WitnessOK (T : Family8) (w : RelabelWitness) : Prop :=
  match w with
  | none => ¬ Admissible8 T
  | some (k, f) => Function.Bijective f ∧ T.image (fun B => B.image f) = representative8 k

instance (T : Family8) (w : RelabelWitness) : Decidable (WitnessOK T w) := by
  cases w with
  | none => exact inferInstanceAs (Decidable (¬ Admissible8 T))
  | some p =>
    exact inferInstanceAs (Decidable
      (Function.Bijective p.2 ∧ T.image (fun B => B.image p.2) = representative8 p.1))

def checkWitnesses : List Family8 → List RelabelWitness → Bool
  | [], [] => true
  | T :: ts, w :: ws => decide (WitnessOK T w) && checkWitnesses ts ws
  | _, _ => false

theorem checkWitnesses_sound {ts : List Family8} {ws : List RelabelWitness}
    (checked : checkWitnesses ts ws = true) :
    ∀ T ∈ ts, Admissible8 T → ∃ k : Fin 14, ∃ f : Fin 8 → Fin 8,
      Function.Bijective f ∧ T.image (fun B => B.image f) = representative8 k := by
  induction ts generalizing ws with
  | nil => simp
  | cons T ts ih =>
    cases ws with
    | nil => simp [checkWitnesses] at checked
    | cons w ws =>
      have hc : WitnessOK T w ∧ checkWitnesses ts ws = true := by
        simpa only [checkWitnesses, Bool.and_eq_true, decide_eq_true_eq] using checked
      intro S mem admissible
      rcases List.mem_cons.mp mem with rfl | mem
      · cases w with
        | none => exact False.elim (hc.1 admissible)
        | some p => exact ⟨p.1, p.2, hc.1⟩
      · exact ih hc.2 S mem admissible

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem normalized_certificate_checked :
    checkWitnesses (extensions candidates8 seed8) witnesses8 = true := by decide

theorem classify_normalized_eight (T : Family8)
    (linear : BlockClassification.Linear T) (seed : seed8 ⊆ T)
    (allowed : T ⊆ seed8 ∪ candidates8.toFinset) (admissible : Admissible8 T) :
    ∃ k : Fin 14, ∃ f : Fin 8 → Fin 8,
      Function.Bijective f ∧ T.image (fun B => B.image f) = representative8 k := by
  exact checkWitnesses_sound normalized_certificate_checked T
    (extensions_complete candidates8 seed8 T seed allowed linear) admissible

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem compatible_triple_is_candidate :
    ∀ B : Finset (Fin 8), B.card = 3 →
      (∀ C ∈ seed8, B ≠ C → (B ∩ C).card ≤ 1) →
      B ∈ seed8 ∪ candidates8.toFinset := by decide

/-- The caller supplies actual triples and the analytic seed, not an assumed
membership in the candidate table. -/
theorem classify_seed_eight (T : Family8)
    (three : ∀ B ∈ T, B.card = 3)
    (linear : BlockClassification.Linear T) (seed : seed8 ⊆ T)
    (admissible : Admissible8 T) :
    ∃ k : Fin 14, ∃ f : Fin 8 → Fin 8,
      Function.Bijective f ∧ T.image (fun B => B.image f) = representative8 k := by
  apply classify_normalized_eight T linear seed ?_ admissible
  intro B hB
  exact compatible_triple_is_candidate B (three B hB)
    (fun C hC hne => linear B hB C (seed hC) hne)

end Aris4Math.ThirtyThree.EightClassification

#print axioms Aris4Math.ThirtyThree.EightClassification.classify_normalized_eight
#print axioms Aris4Math.ThirtyThree.EightClassification.classify_seed_eight

namespace Aris4Math.ThirtyThree.EightClassification

open BlockClassification

theorem restricted_incidence (A : Finset (Fin 8)) (T : Family8) :
    (∑ x ∈ A, (T.filter (fun B => x ∈ B)).card) = ∑ B ∈ T, (A ∩ B).card := by
  simp only [Finset.card_eq_sum_ones, Finset.sum_filter]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro B hB
  rw [← Finset.sum_filter]
  simp [Finset.filter_mem_eq_inter]

/-- A covering linear triple family with five blocks on eight points cannot
be intersecting. This is an analytic statement about an arbitrary family. -/
theorem exists_disjoint_triples (T : Family8)
    (three : ∀ B ∈ T, B.card = 3) (linear : Linear T)
    (covers : ∀ x : Fin 8, ∃ B ∈ T, x ∈ B) (many : 5 ≤ T.card) :
    ∃ A ∈ T, ∃ B ∈ T, Disjoint A B := by
  by_contra no
  have inter_one : ∀ A ∈ T, ∀ B ∈ T, A ≠ B → (A ∩ B).card = 1 := by
    intro A hA B hB ne
    have upper := linear A hA B hB ne
    have nonzero : (A ∩ B).card ≠ 0 := by
      intro zero
      exact no ⟨A, hA, B, hB, Finset.disjoint_iff_inter_eq_empty.mpr
        (Finset.card_eq_zero.mp zero)⟩
    omega
  obtain ⟨A, hA⟩ := Finset.card_pos.mp (show 0 < T.card by omega)
  let others := T.erase A
  have many_others : 4 ≤ others.card := by
    have h := Finset.card_erase_add_one hA
    dsimp [others]
    omega
  have incidence := restricted_incidence A others
  have sum_right : (∑ B ∈ others, (A ∩ B).card) = others.card := by
    calc
      _ = ∑ _B ∈ others, 1 := Finset.sum_congr rfl (by
        intro B hB
        exact inter_one A hA B (Finset.mem_of_mem_erase hB)
          (Finset.mem_erase.mp hB).1.symm)
      _ = others.card := by simp
  have shared : ∃ x ∈ A, 2 ≤ (others.filter (fun B => x ∈ B)).card := by
    by_contra h
    have small : ∀ x ∈ A, (others.filter (fun B => x ∈ B)).card ≤ 1 := by
      intro x hx
      by_contra hn
      exact h ⟨x, hx, by omega⟩
    have bound : others.card ≤ 3 := by
      calc
        others.card = ∑ x ∈ A, (others.filter (fun B => x ∈ B)).card := by
          rw [incidence, sum_right]
        _ ≤ ∑ _x ∈ A, 1 := Finset.sum_le_sum small
        _ = 3 := by simp [three A hA]
    omega
  obtain ⟨x, hxA, shared⟩ := shared
  obtain ⟨B, hB, C, hC, neBC⟩ := Finset.one_lt_card.mp (by omega :
    1 < (others.filter (fun B => x ∈ B)).card)
  obtain ⟨hBo, hxB⟩ := Finset.mem_filter.mp hB
  obtain ⟨hCo, hxC⟩ := Finset.mem_filter.mp hC
  have hBT := Finset.mem_of_mem_erase hBo
  have hCT := Finset.mem_of_mem_erase hCo
  have neBA := (Finset.mem_erase.mp hBo).1
  have neCA := (Finset.mem_erase.mp hCo).1
  have eq_inter (P Q : Finset (Fin 8)) (hP : P ∈ T) (hQ : Q ∈ T)
      (ne : P ≠ Q) (hxP : x ∈ P) (hxQ : x ∈ Q) : P ∩ Q = {x} := by
    apply (Finset.eq_of_subset_of_card_le
      (Finset.singleton_subset_iff.mpr (Finset.mem_inter.mpr ⟨hxP, hxQ⟩)) ?_).symm
    simp [inter_one P hP Q hQ ne]
  have ab := eq_inter A B hA hBT neBA.symm hxA hxB
  have ac := eq_inter A C hA hCT neCA.symm hxA hxC
  have bc := eq_inter B C hBT hCT neBC hxB hxC
  have degree := triple_degree_le_three Finset.univ T (by decide)
    (fun _ _ => Finset.subset_univ _) three linear x
  have subset_star : ({A, B, C} : Family8) ⊆ T.filter (fun D => x ∈ D) := by
    intro D hD
    simp only [Finset.mem_insert, Finset.mem_singleton] at hD
    rcases hD with rfl | rfl | rfl <;> simp [hA, hBT, hCT, hxA, hxB, hxC]
  have abc_card : ({A, B, C} : Family8).card = 3 := by
    simp [neBA.symm, neCA.symm, neBC]
  have star_eq : T.filter (fun D => x ∈ D) = {A, B, C} :=
    (Finset.eq_of_subset_of_card_le subset_star (by omega)).symm
  have interC : (A ∪ B) ∩ C = {x} := by
    rw [Finset.union_inter_distrib_right, ac, bc]
    simp
  have union_card : ((A ∪ B) ∪ C).card = 7 := by
    have absize := Finset.card_union_add_card_inter A B
    have abcsize := Finset.card_union_add_card_inter (A ∪ B) C
    rw [ab] at absize
    rw [interC] at abcsize
    have a3 := three A hA
    have b3 := three B hBT
    have c3 := three C hCT
    simp only [Finset.card_singleton] at absize abcsize
    omega
  have all_inside : ∀ D ∈ T, D ⊆ (A ∪ B) ∪ C := by
    intro D hD
    by_cases dA : D = A
    · subst D
      exact Finset.Subset.trans Finset.subset_union_left Finset.subset_union_left
    by_cases dB : D = B
    · subst D
      exact Finset.Subset.trans Finset.subset_union_right Finset.subset_union_left
    by_cases dC : D = C
    · subst D
      exact Finset.subset_union_right
    have nx : x ∉ D := by
      intro hx
      have hm : D ∈ T.filter (fun E => x ∈ E) := Finset.mem_filter.mpr ⟨hD, hx⟩
      rw [star_eq] at hm
      simp [dA, dB, dC] at hm
    have disj_inter (P Q : Finset (Fin 8)) (eq : P ∩ Q = {x}) :
        Disjoint (D ∩ P) (D ∩ Q) := by
      apply Finset.disjoint_left.mpr
      intro y hyP hyQ
      have hy : y ∈ P ∩ Q := Finset.mem_inter.mpr
        ⟨(Finset.mem_inter.mp hyP).2, (Finset.mem_inter.mp hyQ).2⟩
      rw [eq, Finset.mem_singleton] at hy
      exact nx (hy ▸ (Finset.mem_inter.mp hyP).1)
    have pAB := disj_inter A B ab
    have pAC := disj_inter A C ac
    have pBC := disj_inter B C bc
    have inter_card : (D ∩ ((A ∪ B) ∪ C)).card = 3 := by
      rw [Finset.inter_union_distrib_left, Finset.inter_union_distrib_left,
        Finset.card_union_of_disjoint (Finset.disjoint_union_left.mpr ⟨pAC, pBC⟩),
        Finset.card_union_of_disjoint pAB,
        inter_one D hD A hA dA, inter_one D hD B hBT dB,
        inter_one D hD C hCT dC]
    have eq : D ∩ ((A ∪ B) ∪ C) = D := Finset.eq_of_subset_of_card_le
      Finset.inter_subset_left (by rw [inter_card, three D hD])
    exact Finset.inter_eq_left.mp eq
  have univ_subset : (Finset.univ : Finset (Fin 8)) ⊆ (A ∪ B) ∪ C := by
    intro y _
    obtain ⟨D, hD, hy⟩ := covers y
    exact all_inside D hD hy
  have bound := Finset.card_le_card univ_subset
  rw [union_card] at bound
  norm_num at bound

end Aris4Math.ThirtyThree.EightClassification

#print axioms Aris4Math.ThirtyThree.EightClassification.exists_disjoint_triples

namespace Aris4Math.ThirtyThree.EightClassification

open BlockClassification

theorem exists_seed_blocks (T : Family8)
    (three : ∀ B ∈ T, B.card = 3) (linear : Linear T)
    (covers : ∀ x : Fin 8, ∃ B ∈ T, x ∈ B) (many : 5 ≤ T.card) :
    ∃ A ∈ T, ∃ B ∈ T, ∃ C ∈ T,
      Disjoint A B ∧ (A ∩ C).card = 1 ∧ (B ∩ C).card = 1 := by
  obtain ⟨A, hA, B, hB, disj⟩ := exists_disjoint_triples T three linear covers many
  have abcard : (A ∪ B).card = 6 := by
    rw [Finset.card_union_of_disjoint disj, three A hA, three B hB]
  let Z := (Finset.univ : Finset (Fin 8)) \ (A ∪ B)
  have zcard : Z.card = 2 := by
    dsimp [Z]
    rw [Finset.card_sdiff_of_subset (Finset.subset_univ _), abcard]
    decide
  let others := T \ {A, B}
  have many_others : 3 ≤ others.card := by
    have split := Finset.card_sdiff_add_card_inter T {A, B}
    have bound : (T ∩ {A, B}).card ≤ 2 :=
      (Finset.card_le_card Finset.inter_subset_right).trans Finset.card_le_two
    dsimp [others]
    omega
  have neA (D : Finset (Fin 8)) (hD : D ∈ others) : D ≠ A := by
    have h := (Finset.mem_sdiff.mp hD).2
    exact fun eq => h (by simp [eq])
  have neB (D : Finset (Fin 8)) (hD : D ∈ others) : D ≠ B := by
    have h := (Finset.mem_sdiff.mp hD).2
    exact fun eq => h (by simp [eq])
  have connecting : ∃ C ∈ others, (A ∩ C).card = 1 ∧ (B ∩ C).card = 1 := by
    by_contra no
    have containsZ : ∀ D ∈ others, Z ⊆ D := by
      intro D hD
      have hDT := (Finset.mem_sdiff.mp hD).1
      have a_upper := linear A hA D hDT (neA D hD).symm
      have b_upper := linear B hB D hDT (neB D hD).symm
      have low : (D ∩ (A ∪ B)).card ≤ 1 := by
        rw [Finset.inter_union_distrib_left]
        by_cases a0 : (A ∩ D).card = 0
        · rw [Finset.inter_comm D A, Finset.card_eq_zero.mp a0, Finset.empty_union,
            Finset.inter_comm D B]
          exact b_upper
        · have b0 : (B ∩ D).card = 0 := by
            by_contra nz
            exact no ⟨D, hD, by omega, by omega⟩
          rw [Finset.inter_comm D B, Finset.card_eq_zero.mp b0, Finset.union_empty,
            Finset.inter_comm D A]
          exact a_upper
      have split := Finset.card_sdiff_add_card_inter D (A ∪ B)
      have d3 := three D hDT
      have sub : D \ (A ∪ B) ⊆ Z := Finset.sdiff_subset_sdiff
        (Finset.subset_univ _) (Finset.Subset.refl _)
      have eq : D \ (A ∪ B) = Z := Finset.eq_of_subset_of_card_le sub (by omega)
      rw [← eq]
      exact Finset.sdiff_subset
    obtain ⟨D, hD, E, hE, ne⟩ := Finset.one_lt_card.mp (by omega : 1 < others.card)
    have lower := Finset.card_le_card (Finset.subset_inter (containsZ D hD) (containsZ E hE))
    have upper := linear D (Finset.mem_sdiff.mp hD).1 E (Finset.mem_sdiff.mp hE).1 ne
    omega
  obtain ⟨C, hC, ac, bc⟩ := connecting
  exact ⟨A, hA, B, hB, C, (Finset.mem_sdiff.mp hC).1, disj, ac, bc⟩

/-- The actual three seed blocks admit the standard labels. -/
theorem label_seed_blocks (A B C : Finset (Fin 8))
    (a3 : A.card = 3) (b3 : B.card = 3) (c3 : C.card = 3)
    (disj : Disjoint A B) (ac : (A ∩ C).card = 1) (bc : (B ∩ C).card = 1) :
    ∃ e : Fin 8 ≃ Fin 8,
      A.map e.toEmbedding = {0, 1, 2} ∧ B.map e.toEmbedding = {3, 4, 5} ∧
      C.map e.toEmbedding = {0, 3, 6} := by
  let actual : Fin 3 → Finset (Fin 8) := ![A, B, C]
  let reference : Fin 3 → Finset (Fin 8) := ![{0, 1, 2}, {3, 4, 5}, {0, 3, 6}]
  have small (x : Fin 8) : (signature actual x).card ≤ 2 := by
    by_cases hx : x ∈ A
    · have nx : x ∉ B := Finset.disjoint_left.mp disj hx
      have sub : signature actual x ⊆ {0, 2} := by
        intro i hi
        fin_cases i <;> simp_all [actual, signature]
      exact (Finset.card_le_card sub).trans Finset.card_le_two
    · have sub : signature actual x ⊆ {1, 2} := by
        intro i hi
        fin_cases i <;> simp_all [actual, signature]
      exact (Finset.card_le_card sub).trans Finset.card_le_two
  have smallR : ∀ x : Fin 8, (signature reference x).card ≤ 2 := by decide
  have singles : ∀ i, (actual i).card = (reference i).card := by
    intro i
    fin_cases i <;> simp [actual, reference, a3, b3, c3]
  have pairs : ∀ i j, i ≠ j → (actual i ∩ actual j).card =
      (reference i ∩ reference j).card := by
    intro i j ne
    have ab := Finset.disjoint_iff_inter_eq_empty.mp disj
    have ba := Finset.disjoint_iff_inter_eq_empty.mp disj.symm
    have ca : (C ∩ A).card = 1 := by simpa [Finset.inter_comm] using ac
    have cb : (C ∩ B).card = 1 := by simpa [Finset.inter_comm] using bc
    fin_cases i <;> fin_cases j <;> simp_all [actual, reference]
  obtain ⟨e, he⟩ := exists_equiv_map_blocks actual reference small smallR rfl singles pairs
  exact ⟨e, he 0, he 1, he 2⟩

end Aris4Math.ThirtyThree.EightClassification

#print axioms Aris4Math.ThirtyThree.EightClassification.exists_seed_blocks
#print axioms Aris4Math.ThirtyThree.EightClassification.label_seed_blocks

namespace Aris4Math.ThirtyThree.EightClassification

open BlockClassification

/-- Classification of every actual eight-point covering linear triple family
with at least five blocks. There is no seed or table-membership hypothesis. -/
theorem classify_eight (T : Family8)
    (three : ∀ B ∈ T, B.card = 3) (linear : Linear T)
    (covers : ∀ x : Fin 8, ∃ B ∈ T, x ∈ B) (many : 5 ≤ T.card) :
    ∃ k : Fin 14, ∃ e : Fin 8 ≃ Fin 8,
      T.image (fun B => B.map e.toEmbedding) = representative8 k := by
  obtain ⟨A, hA, B, hB, C, hC, disj, ac, bc⟩ :=
    exists_seed_blocks T three linear covers many
  obtain ⟨e, heA, heB, heC⟩ := label_seed_blocks A B C
    (three A hA) (three B hB) (three C hC) disj ac bc
  let U := T.image (fun B => B.map e.toEmbedding)
  have threeU : ∀ P ∈ U, P.card = 3 := by
    intro P hP
    obtain ⟨D, hD, rfl⟩ := Finset.mem_image.mp hP
    simpa using three D hD
  have linearU : Linear U := by
    intro P hP Q hQ ne
    obtain ⟨D, hD, rfl⟩ := Finset.mem_image.mp hP
    obtain ⟨F, hF, rfl⟩ := Finset.mem_image.mp hQ
    have df : D ≠ F := by intro eq; exact ne (congrArg _ eq)
    rw [← Finset.map_inter, Finset.card_map]
    exact linear D hD F hF df
  have coversU : ∀ x : Fin 8, ∃ P ∈ U, x ∈ P := by
    intro x
    obtain ⟨D, hD, hx⟩ := covers (e.symm x)
    refine ⟨D.map e.toEmbedding, Finset.mem_image.mpr ⟨D, hD, rfl⟩, ?_⟩
    exact Finset.mem_map.mpr ⟨e.symm x, hx, e.apply_symm_apply x⟩
  have manyU : 5 ≤ U.card := by
    dsimp [U]
    rw [Finset.card_image_of_injective _ (Finset.map_injective e.toEmbedding)]
    exact many
  have seedU : seed8 ⊆ U := by
    simp only [seed8, Finset.insert_subset_iff, Finset.singleton_subset_iff]
    refine ⟨?_, ?_, ?_⟩
    · rw [← heA]
      exact Finset.mem_image.mpr ⟨A, hA, rfl⟩
    · rw [← heC]
      exact Finset.mem_image.mpr ⟨C, hC, rfl⟩
    · rw [← heB]
      exact Finset.mem_image.mpr ⟨B, hB, rfl⟩
  obtain ⟨k, f, bijective, mapped⟩ := classify_seed_eight U threeU linearU seedU
    ⟨manyU, coversU⟩
  let g := Equiv.ofBijective f bijective
  refine ⟨k, e.trans g, ?_⟩
  calc
    _ = U.image (fun B => B.image f) := by
      simp only [U, Finset.image_image, Finset.map_eq_image, Function.comp_def]
      rfl
    _ = representative8 k := mapped

end Aris4Math.ThirtyThree.EightClassification

#print axioms Aris4Math.ThirtyThree.EightClassification.classify_eight
