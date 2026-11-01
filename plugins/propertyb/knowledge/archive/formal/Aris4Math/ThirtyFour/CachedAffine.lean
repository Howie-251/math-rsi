import Aris4Math.ThirtyFour.CachedChosenRows

/-! Small exact polynomial certificates for a family of count vectors.
Only Boolean coordinates are linearized. No minimum of rows is asserted affine. -/
namespace Aris4Math.ThirtyFour.CachedAffine
open scoped BigOperators

structure Affine (n : ℕ) where
  constant : ℚ
  linear : Fin n → ℚ

structure Quadratic (n : ℕ) where
  constant : ℚ
  linear : Fin n → ℚ
  square : Fin n → Fin n → ℚ

def Affine.eval (a : Affine n) (x : Fin n → ℚ) : ℚ :=
  a.constant + ∑ i, a.linear i*x i

def Quadratic.eval (a : Quadratic n) (x : Fin n → ℚ) : ℚ :=
  a.constant + (∑ i, a.linear i*x i) + ∑ i, ∑ j, a.square i j*x i*x j

def Affine.toQuadratic (a : Affine n) : Quadratic n :=
  ⟨a.constant,a.linear,fun _ _ => 0⟩

def Affine.product (a b : Affine n) : Quadratic n :=
  ⟨a.constant*b.constant,
    fun i => a.constant*b.linear i+b.constant*a.linear i,
    fun i j => a.linear i*b.linear j⟩

def Quadratic.scale (r : ℚ) (a : Quadratic n) : Quadratic n :=
  ⟨r*a.constant,fun i => r*a.linear i,fun i j => r*a.square i j⟩

def Quadratic.add (a b : Quadratic n) : Quadratic n :=
  ⟨a.constant+b.constant,fun i => a.linear i+b.linear i,
    fun i j => a.square i j+b.square i j⟩

def Quadratic.sum {α : Type*} [Fintype α] (a : α → Quadratic n) : Quadratic n :=
  ⟨∑ k,(a k).constant, fun i => ∑ k,(a k).linear i,
    fun i j => ∑ k,(a k).square i j⟩

theorem toQuadratic_eval (a : Affine n) (x : Fin n → ℚ) :
    a.toQuadratic.eval x=a.eval x := by simp [Quadratic.eval,Affine.eval,Affine.toQuadratic]

theorem product_eval (a b : Affine n) (x : Fin n → ℚ) :
    (a.product b).eval x=a.eval x*b.eval x := by
  unfold Quadratic.eval Affine.product Affine.eval
  simp only [add_mul,Finset.sum_add_distrib]
  have cross : (∑ i, ∑ j, a.linear i*b.linear j*x i*x j)=
      (∑ i,a.linear i*x i)*(∑ j,b.linear j*x j) := by
    rw [Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro i _
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro j _
    ring1
  rw [cross]
  simp_rw [mul_assoc,← Finset.mul_sum]
  ring1

theorem scale_eval (r : ℚ) (a : Quadratic n) (x : Fin n → ℚ) :
    (a.scale r).eval x=r*a.eval x := by
  unfold Quadratic.scale Quadratic.eval
  simp_rw [mul_assoc,← Finset.mul_sum]
  ring1

theorem add_eval (a b : Quadratic n) (x : Fin n → ℚ) :
    (a.add b).eval x=a.eval x+b.eval x := by
  unfold Quadratic.add Quadratic.eval
  simp_rw [add_mul,Finset.sum_add_distrib]
  ring1

theorem sum_eval {α : Type*} [Fintype α] (a : α → Quadratic n) (x : Fin n → ℚ) :
    (Quadratic.sum a).eval x=∑ k,(a k).eval x := by
  unfold Quadratic.sum Quadratic.eval
  simp_rw [Finset.sum_mul,Finset.sum_add_distrib]
  have linear : (∑ i,∑ k,(a k).linear i*x i)=∑ k,∑ i,(a k).linear i*x i := Finset.sum_comm
  have square : (∑ i,∑ j,∑ k,(a k).square i j*x i*x j)=∑ k,∑ i,∑ j,(a k).square i j*x i*x j := by
    calc
      _ = ∑ i,∑ k,∑ j,(a k).square i j*x i*x j := by
        apply Finset.sum_congr rfl;intro i _;exact Finset.sum_comm
      _ = _ := Finset.sum_comm
  rw [linear,square]

def Quadratic.linearize (a : Quadratic n) : Affine n :=
  ⟨a.constant,fun i => a.linear i+a.square i i⟩

theorem linearize_eval (a : Quadratic n) (x : Fin n → ℚ)
    (boolean : ∀ i,x i*x i=x i)
    (offDiagonal : ∀ i j,i≠j → a.square i j=0) :
    a.eval x=a.linearize.eval x := by
  have diagonal : (∑ i,∑ j,a.square i j*x i*x j)=∑ i,a.square i i*x i := by
    apply Finset.sum_congr rfl
    intro i _
    rw [Finset.sum_eq_single i]
    · rw [mul_assoc,boolean]
    · intro j _ ne
      rw [offDiagonal i j (Ne.symm ne)];ring1
    · simp
  unfold Quadratic.eval Affine.eval Quadratic.linearize
  rw [diagonal]
  simp_rw [add_mul,Finset.sum_add_distrib]
  ring1

def rowA (m : Fin 6 → Affine n) (c : Fin 6 → ℚ) : Quadratic n :=
  Quadratic.sum fun r => (m r).toQuadratic.scale (c r)

def rowC (l r : Fin 6 → Affine n) (c : Fin 6 → Fin 6 → ℚ)
    (diagonal : Affine n) : Quadratic n :=
  (Quadratic.sum fun i => Quadratic.sum fun j =>
    ((l i).product (r j)).scale (c i j)).add (diagonal.toQuadratic.scale (-1))

theorem rowA_eval (m : Fin 6 → Affine n) (c : Fin 6 → ℚ) (x : Fin n → ℚ) :
    (rowA m c).eval x=∑ r,(m r).eval x*c r := by
  simp only [rowA,sum_eval,scale_eval,toQuadratic_eval,mul_comm]

theorem rowC_eval (l r : Fin 6 → Affine n) (c : Fin 6 → Fin 6 → ℚ)
    (diagonal : Affine n) (x : Fin n → ℚ) :
    (rowC l r c diagonal).eval x=
      (∑ i,∑ j,(l i).eval x*(r j).eval x*c i j)-diagonal.eval x := by
  simp only [rowC,add_eval,sum_eval,scale_eval,product_eval,toQuadratic_eval]
  simp only [mul_comm (c _ _), neg_one_mul, sub_eq_add_neg]

end Aris4Math.ThirtyFour.CachedAffine
