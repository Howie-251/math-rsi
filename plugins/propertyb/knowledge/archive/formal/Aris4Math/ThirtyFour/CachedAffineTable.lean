import Aris4Math.ThirtyFour.CachedAffineBinding

/-! A shared list of trace shapes is bound once to every actual count vector.
Zero-count shapes are allowed in the arithmetic representation. -/
namespace Aris4Math.ThirtyFour.CachedAffineTable
open scoped BigOperators
open CachedAffine CachedRows CachedAffineBinding

def zero : Affine n := ⟨0,fun _ => 0⟩
def scale (c : ℚ) (a : Affine n) : Affine n := ⟨c*a.constant,fun i => c*a.linear i⟩
def sum {α : Type*} (S : Finset α) (a : α → Affine n) : Affine n :=
  ⟨∑ t∈S,(a t).constant,fun i => ∑ t∈S,(a t).linear i⟩

theorem zero_eval (x : Fin n → ℚ) : (zero : Affine n).eval x=0 := by
  simp [zero,Affine.eval]
theorem scale_eval (c : ℚ) (a : Affine n) (x : Fin n → ℚ) :
    (scale c a).eval x=c*a.eval x := by
  simp only [scale,Affine.eval,mul_assoc,← Finset.mul_sum,mul_add]
theorem sum_eval {α : Type*} (S : Finset α) (a : α → Affine n) (x : Fin n → ℚ) :
    (sum S a).eval x=∑ t∈S,(a t).eval x := by
  simp only [sum,Affine.eval,Finset.sum_mul,Finset.sum_add_distrib]
  rw [Finset.sum_comm]

def profile (geometry : Numeric.Profile) (shapes : List (List ℕ))
    (count : List ℕ → ℕ) : Numeric.Profile :=
  {geometry with types := shapes.map fun t => ⟨t,count t⟩}

def mass (geometry : Numeric.Profile) (shapes : List (List ℕ))
    (weights : List ℕ → Affine n) (k : ℕ) (last : Bool) (r : Fin 6) : Affine n :=
  sum shapes.toFinset fun t =>
    if residual ⟨t,0⟩=r ∧ compatible geometry ⟨t,0⟩ k last then weights t else zero

def diagonal (geometry : Numeric.Profile) (shapes : List (List ℕ))
    (weights : List ℕ → Affine n) (k : ℕ) : Affine n :=
  sum shapes.toFinset fun t =>
    if compatible geometry ⟨t,0⟩ k true ∧ compatible geometry ⟨t,0⟩ k false
    then scale (cCoeff geometry k (residual ⟨t,0⟩) (residual ⟨t,0⟩)) (weights t) else zero

theorem mass_binding (geometry : Numeric.Profile) (shapes : List (List ℕ))
    (count : List ℕ → ℕ) (weights : List ℕ → Affine n) (x : Fin n → ℚ)
    (counts : ∀ t∈shapes,(count t : ℚ)=(weights t).eval x)
    (k : ℕ) (last : Bool) (r : Fin 6) :
    CachedRows.mass (profile geometry shapes count) k last r=
      (mass geometry shapes weights k last r).eval x := by
  unfold CachedRows.mass
  simp only [profile]
  have image : (shapes.map fun t => (⟨t,count t⟩ : Numeric.EdgeType)).toFinset=
      shapes.toFinset.image (fun t => (⟨t,count t⟩ : Numeric.EdgeType)) := by
    ext t; simp
  rw [image]
  rw [Finset.sum_image]
  · rw [mass,sum_eval]
    apply Finset.sum_congr rfl
    intro t ht
    have compat : compatible {geometry with types := shapes.map fun t => ⟨t,count t⟩}
        ⟨t,count t⟩ k last=compatible geometry ⟨t,0⟩ k last := rfl
    change (if residual ⟨t,0⟩=r ∧ compatible geometry ⟨t,0⟩ k last then (count t : ℚ) else 0)=_
    split_ifs
    · exact counts t (List.mem_toFinset.mp ht)
    · exact (zero_eval x).symm
  · intro a _ b _ h
    exact congrArg Numeric.EdgeType.locks h

theorem diagonal_binding (geometry : Numeric.Profile) (shapes : List (List ℕ))
    (count : List ℕ → ℕ) (weights : List ℕ → Affine n) (x : Fin n → ℚ)
    (counts : ∀ t∈shapes,(count t : ℚ)=(weights t).eval x) (k : ℕ) :
    cachedDiagonal (profile geometry shapes count) k=
      (diagonal geometry shapes weights k).eval x := by
  unfold cachedDiagonal
  simp only [profile]
  have image : (shapes.map fun t => (⟨t,count t⟩ : Numeric.EdgeType)).toFinset=
      shapes.toFinset.image (fun t => (⟨t,count t⟩ : Numeric.EdgeType)) := by
    ext t; simp
  rw [image]
  rw [Finset.sum_image]
  · rw [diagonal,sum_eval]
    apply Finset.sum_congr rfl
    intro t ht
    have compat (last : Bool) : compatible {geometry with types := shapes.map fun t => ⟨t,count t⟩}
        ⟨t,count t⟩ k last=compatible geometry ⟨t,0⟩ k last := rfl
    change (if compatible geometry ⟨t,0⟩ k true ∧ compatible geometry ⟨t,0⟩ k false then
      (count t : ℚ)*cCoeff geometry k (residual ⟨t,0⟩) (residual ⟨t,0⟩) else 0)=_
    split_ifs
    · rw [scale_eval,counts t (List.mem_toFinset.mp ht),mul_comm]
    · exact (zero_eval x).symm
  · intro a _ b _ h
    exact congrArg Numeric.EdgeType.locks h

def rows (geometry : Numeric.Profile) (shapes : List (List ℕ))
    (weights : List ℕ → Affine n) (choices : Fin v → Fin 3) : Rows n v where
  mass := fun k side r => mass geometry shapes weights (k.val+1) side r
  edge := fun k side r => aCoeff geometry (k.val+1) side r
  pair := fun k r s => cCoeff geometry (k.val+1) r s
  diagonal := fun k => diagonal geometry shapes weights (k.val+1)
  choices := choices

theorem bound_eq (geometry : Numeric.Profile) (shapes : List (List ℕ))
    (count : List ℕ → ℕ) (weights : List ℕ → Affine n) (x : Fin n → ℚ)
    (counts : ∀ t∈shapes,(count t : ℚ)=(weights t).eval x) (choices : Fin v → Fin 3) :
    (rows geometry shapes weights choices).polynomial.eval x=
      CachedChosenRows.bound (profile geometry shapes count) choices := by
  apply polynomial_eq_bound
  · exact fun k side r => mass_binding geometry shapes count weights x counts _ side r
  · intros; rfl
  · intros; rfl
  · exact fun k => diagonal_binding geometry shapes count weights x counts _

end Aris4Math.ThirtyFour.CachedAffineTable
