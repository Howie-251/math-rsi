import Aris4Math.ThirtyFour.LocalProfiles
import Mathlib.Tactic.Ring.Basic

/-! Small interface probe. No new catalogue or numeric table is generated. -/
namespace Aris4Math.ThirtyFour.TwentyFiveCoefficientProbe

open scoped BigOperators
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery

def geometry (v : ℕ) (positions : List ℕ) : Numeric.Profile :=
  { v := v, positions := positions, types := [] }

theorem edgeWeight_geometry (p : Numeric.Profile) (t : Numeric.EdgeType)
    (k : ℕ) (last : Bool) :
    Numeric.edgeWeight p t k last =
      Numeric.edgeWeight (geometry p.v p.positions) ⟨t.locks,0⟩ k last := rfl

theorem pairWeight_geometry (p : Numeric.Profile) (t u : Numeric.EdgeType) (k : ℕ) :
    Numeric.pairWeight p t u k =
      Numeric.pairWeight (geometry p.v p.positions) ⟨t.locks,0⟩ ⟨u.locks,0⟩ k := rfl

theorem boundA_geometry (p : Numeric.Profile) (k : ℕ) :
    Numeric.boundA p k = Numeric.qsum (p.types.map fun t => (t.count : ℚ) *
      Numeric.edgeWeight (geometry p.v p.positions) ⟨t.locks,0⟩ k true) := rfl

theorem boundB_geometry (p : Numeric.Profile) (k : ℕ) :
    Numeric.boundB p k = Numeric.qsum (p.types.map fun t => (t.count : ℚ) *
      Numeric.edgeWeight (geometry p.v p.positions) ⟨t.locks,0⟩ k false) := rfl

theorem boundC_geometry (p : Numeric.Profile) (noCap : p.emptyPairCap=none) (k : ℕ) :
    Numeric.boundC p k = Numeric.qsum (p.types.flatMap fun t => p.types.map fun u =>
      ((t.count * (u.count - if t.locks=u.locks then 1 else 0) : ℕ) : ℚ) *
      Numeric.pairWeight (geometry p.v p.positions) ⟨t.locks,0⟩ ⟨u.locks,0⟩ k) := by
  unfold Numeric.boundC
  congr 1
  apply List.flatMap_congr
  intro t ht
  apply List.map_congr_left
  intro u hu
  simp only [Numeric.pairCount,noCap,Option.getD_none,ite_self]
  rfl

/-- The kernel is literally independent of every actual trace multiplicity. -/
theorem profile_geometry {n v : ℕ} (labels : List (Finset (Fin n)))
    (positions : Fin n ↪ Fin v) (μ : Finset (Fin n) → ℕ) (centers : List ℕ) :
    geometry (profile labels positions μ centers).v
      (profile labels positions μ centers).positions =
      geometry v (canonicalType positions Finset.univ) := rfl

/-- This is the diagonal correction used by the aggregate bare C row. -/
theorem diagonal_count (a : ℕ) :
    ((a * (a-1) : ℕ) : ℚ) = (a : ℚ)*(a : ℚ)-(a : ℚ) := by
  cases a with
  | zero => norm_num
  | succ a =>
    simp only [Nat.succ_sub_one,Nat.cast_mul,Nat.cast_succ]
    ring1

/-- Actual H caller after cached rows have been connected to Numeric A/B/C.
The hypotheses `valid`, row identities and `strict` are explicit obligations;
this interface alone does not prove the 25-point branch. -/
theorem propertyB_of_cached_rows (H : Simple5Hypergraph (Fin 25))
    (vertices positions : Fin 9 ↪ Fin 25)
    (labels : List (Finset (Fin 9))) (nodup : labels.Nodup) (all : ∀ T,T∈labels)
    (μ : Finset (Fin 9) → ℕ) (counts : ∀ T,count H vertices T=μ T)
    (valid : Numeric.validProfile (profile labels positions μ []) 34)
    (A B C : Fin 25 → ℚ)
    (a_eq : ∀ k,Numeric.boundA (profile labels positions μ []) (k.val+1)=A k)
    (b_eq : ∀ k,Numeric.boundB (profile labels positions μ []) (k.val+1)=B k)
    (c_eq : ∀ k,Numeric.boundC (profile labels positions μ []) (k.val+1)=C k)
    (strict : (∑ k,min (A k) (min (B k) (C k)))<1) : PropertyB H := by
  have real := LocalProfiles.realizes H vertices positions labels nodup all μ counts [] valid
  apply ConditionalUnion.propertyB_of_position_bounds H vertices positions A B C
  · intro k
    rw [← a_eq k]
    exact le_of_eq (ProfileApplication.endpoint_sum_eq H vertices positions _ real k true)
  · intro k
    rw [← b_eq k]
    exact le_of_eq (ProfileApplication.endpoint_sum_eq H vertices positions _ real k false)
  · intro k
    rw [← c_eq k]
    exact ProfileApplication.critical_sum_le H vertices positions _ real rfl k
  · exact strict

end Aris4Math.ThirtyFour.TwentyFiveCoefficientProbe

#print axioms Aris4Math.ThirtyFour.TwentyFiveCoefficientProbe.boundC_geometry
#print axioms Aris4Math.ThirtyFour.TwentyFiveCoefficientProbe.diagonal_count
#print axioms Aris4Math.ThirtyFour.TwentyFiveCoefficientProbe.propertyB_of_cached_rows
