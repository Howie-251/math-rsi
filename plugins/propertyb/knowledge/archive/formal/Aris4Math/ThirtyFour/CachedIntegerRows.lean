import Aris4Math.ThirtyFour.CachedRows

/-! Integer-scaled grouped rows. The C subtraction lives in ℤ, never truncated ℕ. -/
namespace Aris4Math.ThirtyFour.CachedIntegerRows
open scoped BigOperators
open CachedRows Numeric

def massNat (p : Profile) (k : ℕ) (last : Bool) (r : Fin 6) : ℕ :=
  ∑ t ∈ p.types.toFinset, if residual t=r ∧ compatible p t k last then t.count else 0

def pivotMass (p : Profile) (k : ℕ) : ℕ :=
  ∑ t ∈ p.types.toFinset, if t.locks=pivotTrace p k then t.count else 0

theorem massNat_cast (p : Profile) (k : ℕ) (last : Bool) (r : Fin 6) :
    (massNat p k last r : ℚ) = mass p k last r := by simp [massNat,mass]

def rowA (p : Profile) (k : ℕ) (last : Bool) (A : Fin 6 → ℤ) : ℤ :=
  ∑ r, (massNat p k last r : ℤ) * A r

def rowC (p : Profile) (k : ℕ) (C : Fin 6 → Fin 6 → ℤ) : ℤ :=
  (∑ r, ∑ q, (massNat p k true r : ℤ)*(massNat p k false q : ℤ)*C r q) -
    (pivotMass p k : ℤ)*C (residual ⟨pivotTrace p k,0⟩) (residual ⟨pivotTrace p k,0⟩)

theorem cachedA_scaled (p : Profile) (k : ℕ) (last : Bool) (A : Fin 6 → ℤ) (D : ℚ)
    (eq : ∀ r,aCoeff p k last r=(A r : ℚ)/D) :
    cachedA p k last = (rowA p k last A : ℚ)/D := by
  simp only [cachedA,eq,mul_div,rowA,Int.cast_sum,Int.cast_mul,Int.cast_natCast,
    massNat_cast,Finset.sum_div]

theorem cachedC_scaled (p : Profile) (k : ℕ) (C : Fin 6 → Fin 6 → ℤ) (D : ℚ)
    (nodup : ∀ t ∈ p.types,t.locks.Nodup)
    (eq : ∀ r q,cCoeff p k r q=(C r q : ℚ)/D) :
    cachedC p k = (rowC p k C : ℚ)/D := by
  rw [cachedC,cachedDiagonal_eq p k nodup]
  simp only [eq,mul_div,rowC,Int.cast_sub,Int.cast_sum,Int.cast_mul,Int.cast_natCast,
    massNat_cast,Finset.sum_div,sub_div,pivotMass,Nat.cast_sum]
  simp

theorem strict_of_integer {v : ℕ} (A B C : Fin v → ℤ) (D : ℕ) (pos : 0<D)
    (strict : (∑ k,min (A k) (min (B k) (C k))) < (D : ℤ)) :
    (∑ k,min ((A k : ℚ)/D) (min ((B k : ℚ)/D) ((C k : ℚ)/D))) < 1 := by
  have hD : (0 : ℚ) < D := by exact_mod_cast pos
  have min_div (a b : ℚ) : min (a/D) (b/D) = min a b / D := by
    by_cases h : a ≤ b
    · rw [min_eq_left h,min_eq_left ((div_le_div_iff_of_pos_right hD).mpr h)]
    · have h' : b ≤ a := le_of_not_ge h
      rw [min_eq_right h',min_eq_right ((div_le_div_iff_of_pos_right hD).mpr h')]
  simp_rw [min_div]
  rw [← Finset.sum_div,div_lt_iff₀ hD,one_mul]
  have cast : (∑ k,min ((A k : ℚ)) (min ((B k : ℚ)) ((C k : ℚ)))) =
      ((∑ k,min (A k) (min (B k) (C k)) : ℤ) : ℚ) := by
    simp only [Int.cast_sum,Int.cast_min]
  rw [cast]
  exact_mod_cast strict
end Aris4Math.ThirtyFour.CachedIntegerRows
#print axioms Aris4Math.ThirtyFour.CachedIntegerRows.cachedC_scaled
#print axioms Aris4Math.ThirtyFour.CachedIntegerRows.strict_of_integer
