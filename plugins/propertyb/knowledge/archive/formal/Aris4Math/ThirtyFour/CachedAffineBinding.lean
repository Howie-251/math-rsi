import Aris4Math.ThirtyFour.CachedAffine

namespace Aris4Math.ThirtyFour.CachedAffineBinding
open scoped BigOperators
open CachedAffine CachedRows

structure Rows (n v : ℕ) where
  mass : Fin v → Bool → Fin 6 → Affine n
  edge : Fin v → Bool → Fin 6 → ℚ
  pair : Fin v → Fin 6 → Fin 6 → ℚ
  diagonal : Fin v → Affine n
  choices : Fin v → Fin 3

def Rows.polynomial (data : Rows n v) : Quadratic n :=
  Quadratic.sum fun k =>
    if data.choices k=0 then rowA (data.mass k true) (data.edge k true)
    else if data.choices k=1 then rowA (data.mass k false) (data.edge k false)
    else rowC (data.mass k true) (data.mass k false) (data.pair k) (data.diagonal k)

/-- Binding to actual numerical rows includes the diagonal correction. -/
theorem polynomial_eq_bound (data : Rows n v) (p : Numeric.Profile) (x : Fin n → ℚ)
    (masses : ∀ k side r,mass p (k.val+1) side r=(data.mass k side r).eval x)
    (edges : ∀ k side r,aCoeff p (k.val+1) side r=data.edge k side r)
    (pairs : ∀ k r s,cCoeff p (k.val+1) r s=data.pair k r s)
    (diagonal : ∀ k,cachedDiagonal p (k.val+1)=(data.diagonal k).eval x) :
    data.polynomial.eval x=CachedChosenRows.bound p data.choices := by
  rw [Rows.polynomial,sum_eval]
  apply Finset.sum_congr rfl
  intro k _
  unfold CachedChosenRows.profileRow
  split_ifs
  · rw [rowA_eval]
    simp only [cachedA,masses,edges]
  · rw [rowA_eval]
    simp only [cachedA,masses,edges]
  · rw [rowC_eval]
    simp only [cachedC,masses,pairs,diagonal]

theorem strict (data : Rows n v) (p : Numeric.Profile) (x : Fin n → ℚ)
    (masses : ∀ k side r,mass p (k.val+1) side r=(data.mass k side r).eval x)
    (edges : ∀ k side r,aCoeff p (k.val+1) side r=data.edge k side r)
    (pairs : ∀ k r s,cCoeff p (k.val+1) r s=data.pair k r s)
    (diagonal : ∀ k,cachedDiagonal p (k.val+1)=(data.diagonal k).eval x)
    (boolean : ∀ i,x i*x i=x i)
    (offDiagonal : ∀ i j,i≠j → data.polynomial.square i j=0)
    (less : data.polynomial.linearize.eval x<1) :
    (∑ k : Fin v,min (cachedA p (k.val+1) true)
      (min (cachedA p (k.val+1) false) (cachedC p (k.val+1))))<1 := by
  apply CachedChosenRows.strict p data.choices
  rw [← polynomial_eq_bound data p x masses edges pairs diagonal,
    linearize_eval data.polynomial x boolean offDiagonal]
  exact less

end Aris4Math.ThirtyFour.CachedAffineBinding
