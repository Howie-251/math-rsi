import Mathlib

/-
N59_MANUAL12_ACTIVE, same-round continuation, 2026-09-28.
DRAFT / NOT_KERNEL_CHECKED.  This file is not a compiled project.
It proves a graph-semantic parent-column bridge conditional on the stated
commutation identity and nonnegative repeat entries.  Deriving commutation
from 8-regularity and the matrix polynomial is not formalized here.
No target N59 exclusion, RAW output, or requested inequality is an axiom.
-/
namespace N59Continuation

variable {V : Type*} [Fintype V] [DecidableEq V]

noncomputable def adjWeight (G : SimpleGraph V) (x y : V) : ℤ := by
  classical
  exact if G.Adj x y then 1 else 0

noncomputable def commonWeight (G : SimpleGraph V) (x y : V) : ℤ :=
  ∑ z : V, adjWeight G x z * adjWeight G y z

noncomputable def repeatWeight (G : SimpleGraph V) (x y : V) : ℤ :=
  if x = y then 0 else adjWeight G x y + commonWeight G x y - 1

theorem adjWeight_nonneg (G : SimpleGraph V) (x y : V) :
    0 ≤ adjWeight G x y := by
  classical
  unfold adjWeight
  split_ifs <;> norm_num

/-- The parent is an actual neighbour of the root; the bound comes from
one term of the actual AB product, not an independent aggregate variable. -/
theorem parent_repeat_le_column_budget (G : SimpleGraph V) (r p e : V)
    (hrp : G.Adj r p)
    (hnonneg : ∀ x, 0 ≤ repeatWeight G x e)
    (hcomm : (∑ x : V, adjWeight G r x * repeatWeight G x e) =
      ∑ x : V, repeatWeight G r x * adjWeight G x e) :
    repeatWeight G p e ≤ ∑ x : V, repeatWeight G r x * adjWeight G x e := by
  classical
  calc
    repeatWeight G p e = adjWeight G r p * repeatWeight G p e := by
      simp [adjWeight, hrp]
    _ ≤ ∑ x : V, adjWeight G r x * repeatWeight G x e := by
      apply Finset.single_le_sum
      · intro x hx
        exact mul_nonneg (adjWeight_nonneg G r x) (hnonneg x)
      · exact Finset.mem_univ p
    _ = ∑ x : V, repeatWeight G r x * adjWeight G x e := hcomm

/-- For an isolated exceptional point e, none of its real neighbours is in
the root's positive-repeat support.  Nonnegativity then forces EVERY parent
entry to vanish.  Identifying the support with the exceptional vertices
is a separate, explicitly unformalized BFS bridge. -/
theorem isolated_exception_parent_repeat_zero (G : SimpleGraph V) (r p e : V)
    (hrp : G.Adj r p)
    (hnonneg : ∀ x, 0 ≤ repeatWeight G x e)
    (hcomm : (∑ x : V, adjWeight G r x * repeatWeight G x e) =
      ∑ x : V, repeatWeight G r x * adjWeight G x e)
    (hnoSupportNeighbour : ∀ x, G.Adj x e → repeatWeight G r x = 0) :
    repeatWeight G p e = 0 := by
  classical
  have hzero : (∑ x : V, repeatWeight G r x * adjWeight G x e) = 0 := by
    apply Finset.sum_eq_zero
    intro x hx
    by_cases hxe : G.Adj x e
    · simp [adjWeight, hxe, hnoSupportNeighbour x hxe]
    · simp [adjWeight, hxe]
  have hbound := parent_repeat_le_column_budget G r p e hrp hnonneg hcomm
  rw [hzero] at hbound
  exact le_antisymm hbound (hnonneg p)

/-- An actual common neighbour gives an actual repeat charge on a triangle. -/
theorem commonWeight_ge_one (G : SimpleGraph V) (p x y : V)
    (hpy : G.Adj p y) (hxy : G.Adj x y) :
    1 ≤ commonWeight G p x := by
  classical
  have hy : adjWeight G p y * adjWeight G x y = 1 := by
    simp [adjWeight, hpy, hxy]
  unfold commonWeight
  calc
    (1 : ℤ) = adjWeight G p y * adjWeight G x y := hy.symm
    _ ≤ ∑ z : V, adjWeight G p z * adjWeight G x z := by
      apply Finset.single_le_sum
      · intro z hz
        exact mul_nonneg (adjWeight_nonneg G p z) (adjWeight_nonneg G x z)
      · exact Finset.mem_univ y

theorem triangle_repeat_ge_one (G : SimpleGraph V) (p x y : V)
    (hpxne : p ≠ x) (hpx : G.Adj p x)
    (hpy : G.Adj p y) (hxy : G.Adj x y) :
    1 ≤ repeatWeight G p x := by
  classical
  have hc := commonWeight_ge_one G p x y hpy hxy
  simpa [repeatWeight, hpxne, adjWeight, hpx] using hc

#print axioms parent_repeat_le_column_budget
#print axioms isolated_exception_parent_repeat_zero
#print axioms triangle_repeat_ge_one

end N59Continuation
