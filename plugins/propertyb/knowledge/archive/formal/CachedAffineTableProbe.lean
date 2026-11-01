import Aris4Math.ThirtyFour.CachedChosenRows
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

