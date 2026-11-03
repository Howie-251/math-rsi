import Mathlib.Data.Matrix.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Logic.Equiv.Basic
import Lean.Elab.Tactic.Omega
import Lean.Elab.Tactic.RCases

/-!
The four-label integer block in the triple-repeat reduction.

This module classifies the supplied matrix itself, under a permutation of its
four labels fixing 0. It does not construct that matrix from an original graph.
-/

namespace DegreeDiameter

open scoped BigOperators

/-- The six upper-triangular entries, with equal opposite entries. -/
def tripleFourPattern (N : Matrix (Fin 4) (Fin 4) ℤ) (a b c : ℤ) : Prop :=
  N 0 1 = a ∧ N 0 2 = b ∧ N 0 3 = c ∧
  N 1 2 = c ∧ N 1 3 = b ∧ N 2 3 = a

/-- Symmetry, zero diagonal, and the four row equations force opposite entries. -/
theorem n62_four_block_opposite_entries (N : Matrix (Fin 4) (Fin 4) ℤ)
    (hsym : ∀ i j, N i j = N j i)
    (hdiag : ∀ i, N i i = 0)
    (hrow : ∀ i, ∑ j : Fin 4, N i j = 3) :
    N 0 1 = N 2 3 ∧ N 0 2 = N 1 3 ∧ N 0 3 = N 1 2 ∧
      N 0 1 + N 0 2 + N 0 3 = 3 := by
  have h0 : N 0 0 + N 0 1 + N 0 2 + N 0 3 = 3 := by
    simpa [Fin.sum_univ_succ, add_assoc] using hrow 0
  have h1 : N 1 0 + N 1 1 + N 1 2 + N 1 3 = 3 := by
    simpa [Fin.sum_univ_succ, add_assoc] using hrow 1
  have h2 : N 2 0 + N 2 1 + N 2 2 + N 2 3 = 3 := by
    simpa [Fin.sum_univ_succ, add_assoc] using hrow 2
  have h3 : N 3 0 + N 3 1 + N 3 2 + N 3 3 = 3 := by
    simpa [Fin.sum_univ_succ, add_assoc] using hrow 3
  have hd0 := hdiag 0
  have hd1 := hdiag 1
  have hd2 := hdiag 2
  have hd3 := hdiag 3
  have h10 := hsym 1 0
  have h20 := hsym 2 0
  have h30 := hsym 3 0
  have h21 := hsym 2 1
  have h31 := hsym 3 1
  have h32 := hsym 3 2
  omega

/-- An explicit ten-case statement about the entries of the supplied matrix. -/
theorem n62_four_block_weight_cases (N : Matrix (Fin 4) (Fin 4) ℤ)
    (hsym : ∀ i j, N i j = N j i)
    (hdiag : ∀ i, N i i = 0)
    (hnonneg : ∀ i j, 0 ≤ N i j)
    (hrow : ∀ i, ∑ j : Fin 4, N i j = 3) :
    (N 0 1 = 3 ∧ N 0 2 = 0 ∧ N 0 3 = 0) ∨
    (N 0 1 = 0 ∧ N 0 2 = 3 ∧ N 0 3 = 0) ∨
    (N 0 1 = 0 ∧ N 0 2 = 0 ∧ N 0 3 = 3) ∨
    (N 0 1 = 2 ∧ N 0 2 = 1 ∧ N 0 3 = 0) ∨
    (N 0 1 = 2 ∧ N 0 2 = 0 ∧ N 0 3 = 1) ∨
    (N 0 1 = 1 ∧ N 0 2 = 2 ∧ N 0 3 = 0) ∨
    (N 0 1 = 0 ∧ N 0 2 = 2 ∧ N 0 3 = 1) ∨
    (N 0 1 = 1 ∧ N 0 2 = 0 ∧ N 0 3 = 2) ∨
    (N 0 1 = 0 ∧ N 0 2 = 1 ∧ N 0 3 = 2) ∨
    (N 0 1 = 1 ∧ N 0 2 = 1 ∧ N 0 3 = 1) := by
  have hsum := (n62_four_block_opposite_entries N hsym hdiag hrow).2.2.2
  have ha := hnonneg 0 1
  have hb := hnonneg 0 2
  have hc := hnonneg 0 3
  have hcasesa : N 0 1 = 0 ∨ N 0 1 = 1 ∨ N 0 1 = 2 ∨ N 0 1 = 3 := by omega
  have hcasesb : N 0 2 = 0 ∨ N 0 2 = 1 ∨ N 0 2 = 2 ∨ N 0 2 = 3 := by omega
  rcases hcasesa with ha | ha | ha | ha <;>
    rcases hcasesb with hb | hb | hb | hb <;> simp [ha, hb] <;> omega

/-- A permutation of the four matrix labels, fixing 0, gives exactly one of
the three possible opposite-entry patterns 300, 210, and 111. -/
theorem n62_four_block_classification (N : Matrix (Fin 4) (Fin 4) ℤ)
    (hsym : ∀ i j, N i j = N j i)
    (hdiag : ∀ i, N i i = 0)
    (hnonneg : ∀ i j, 0 ≤ N i j)
    (hrow : ∀ i, ∑ j : Fin 4, N i j = 3) :
    ∃ σ : Equiv.Perm (Fin 4), σ 0 = 0 ∧
      (tripleFourPattern (fun i j => N (σ i) (σ j)) 3 0 0 ∨
       tripleFourPattern (fun i j => N (σ i) (σ j)) 2 1 0 ∨
       tripleFourPattern (fun i j => N (σ i) (σ j)) 1 1 1) := by
  obtain ⟨hop1, hop2, hop3, _⟩ := n62_four_block_opposite_entries N hsym hdiag hrow
  have h12 := hop3.symm
  have h13 := hop2.symm
  have h23 := hop1.symm
  have h21 := hsym 2 1
  have h31 := hsym 3 1
  have h32 := hsym 3 2
  rcases n62_four_block_weight_cases N hsym hdiag hnonneg hrow with
    h | h | h | h | h | h | h | h | h | h
  · refine ⟨Equiv.refl _, rfl, Or.inl ?_⟩
    rcases h with ⟨ha, hb, hc⟩
    simp [tripleFourPattern, ha, hb, hc, h12, h13, h23]
  · refine ⟨Equiv.swap 1 2, ?_, Or.inl ?_⟩
    · decide
    · rcases h with ⟨ha, hb, hc⟩
      simp [tripleFourPattern, Equiv.swap_apply_def, ha, hb, hc, h12, h13, h23,
        h21]
  · refine ⟨Equiv.swap 1 3, ?_, Or.inl ?_⟩
    · decide
    · rcases h with ⟨ha, hb, hc⟩
      simp [tripleFourPattern, Equiv.swap_apply_def, ha, hb, hc, h12, h13, h23,
        h21, h31, h32]
  · refine ⟨Equiv.refl _, rfl, Or.inr (Or.inl ?_)⟩
    rcases h with ⟨ha, hb, hc⟩
    simp [tripleFourPattern, ha, hb, hc, h12, h13, h23]
  · refine ⟨Equiv.swap 2 3, ?_, Or.inr (Or.inl ?_)⟩
    · decide
    · rcases h with ⟨ha, hb, hc⟩
      simp [tripleFourPattern, Equiv.swap_apply_def, ha, hb, hc, h12, h13, h23,
        h32]
  · refine ⟨Equiv.swap 1 2, ?_, Or.inr (Or.inl ?_)⟩
    · decide
    · rcases h with ⟨ha, hb, hc⟩
      simp [tripleFourPattern, Equiv.swap_apply_def, ha, hb, hc, h12, h13, h23,
        h21]
  · refine ⟨(Equiv.swap 1 2).trans (Equiv.swap 1 3), ?_, Or.inr (Or.inl ?_)⟩
    · decide
    · rcases h with ⟨ha, hb, hc⟩
      simp [tripleFourPattern, Equiv.swap_apply_def, Equiv.trans_apply,
        ha, hb, hc, h12, h13, h23, h21, h31]
  · refine ⟨(Equiv.swap 1 3).trans (Equiv.swap 1 2), ?_, Or.inr (Or.inl ?_)⟩
    · decide
    · rcases h with ⟨ha, hb, hc⟩
      simp [tripleFourPattern, Equiv.swap_apply_def, Equiv.trans_apply,
        ha, hb, hc, h12, h13, h23, h31, h32]
  · refine ⟨Equiv.swap 1 3, ?_, Or.inr (Or.inl ?_)⟩
    · decide
    · rcases h with ⟨ha, hb, hc⟩
      simp [tripleFourPattern, Equiv.swap_apply_def, ha, hb, hc, h12, h13, h23,
        h21, h31, h32]
  · refine ⟨Equiv.refl _, rfl, Or.inr (Or.inr ?_)⟩
    rcases h with ⟨ha, hb, hc⟩
    simp [tripleFourPattern, ha, hb, hc, h12, h13, h23]

end DegreeDiameter
