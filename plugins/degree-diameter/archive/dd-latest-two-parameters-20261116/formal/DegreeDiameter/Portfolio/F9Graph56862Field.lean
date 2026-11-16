import DegreeDiameter.Portfolio.SingleExtension
import Mathlib.Data.Fin.VecNotation
import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Ring
import Mathlib.Tactic.DeriveFintype
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
/-- code a+3b denotes a+bw, with w²=-1 over F3. -/
inductive F where
  | c0 | c1 | c2 | c3 | c4 | c5 | c6 | c7 | c8
  deriving DecidableEq, Fintype
namespace F
instance : Zero F := ⟨c0⟩
instance : One F := ⟨c1⟩
def add : F → F → F
  | c0,c0 => c0
  | c0,c1 => c1
  | c0,c2 => c2
  | c0,c3 => c3
  | c0,c4 => c4
  | c0,c5 => c5
  | c0,c6 => c6
  | c0,c7 => c7
  | c0,c8 => c8
  | c1,c0 => c1
  | c1,c1 => c2
  | c1,c2 => c0
  | c1,c3 => c4
  | c1,c4 => c5
  | c1,c5 => c3
  | c1,c6 => c7
  | c1,c7 => c8
  | c1,c8 => c6
  | c2,c0 => c2
  | c2,c1 => c0
  | c2,c2 => c1
  | c2,c3 => c5
  | c2,c4 => c3
  | c2,c5 => c4
  | c2,c6 => c8
  | c2,c7 => c6
  | c2,c8 => c7
  | c3,c0 => c3
  | c3,c1 => c4
  | c3,c2 => c5
  | c3,c3 => c6
  | c3,c4 => c7
  | c3,c5 => c8
  | c3,c6 => c0
  | c3,c7 => c1
  | c3,c8 => c2
  | c4,c0 => c4
  | c4,c1 => c5
  | c4,c2 => c3
  | c4,c3 => c7
  | c4,c4 => c8
  | c4,c5 => c6
  | c4,c6 => c1
  | c4,c7 => c2
  | c4,c8 => c0
  | c5,c0 => c5
  | c5,c1 => c3
  | c5,c2 => c4
  | c5,c3 => c8
  | c5,c4 => c6
  | c5,c5 => c7
  | c5,c6 => c2
  | c5,c7 => c0
  | c5,c8 => c1
  | c6,c0 => c6
  | c6,c1 => c7
  | c6,c2 => c8
  | c6,c3 => c0
  | c6,c4 => c1
  | c6,c5 => c2
  | c6,c6 => c3
  | c6,c7 => c4
  | c6,c8 => c5
  | c7,c0 => c7
  | c7,c1 => c8
  | c7,c2 => c6
  | c7,c3 => c1
  | c7,c4 => c2
  | c7,c5 => c0
  | c7,c6 => c4
  | c7,c7 => c5
  | c7,c8 => c3
  | c8,c0 => c8
  | c8,c1 => c6
  | c8,c2 => c7
  | c8,c3 => c2
  | c8,c4 => c0
  | c8,c5 => c1
  | c8,c6 => c5
  | c8,c7 => c3
  | c8,c8 => c4
def mul : F → F → F
  | c0,c0 => c0
  | c0,c1 => c0
  | c0,c2 => c0
  | c0,c3 => c0
  | c0,c4 => c0
  | c0,c5 => c0
  | c0,c6 => c0
  | c0,c7 => c0
  | c0,c8 => c0
  | c1,c0 => c0
  | c1,c1 => c1
  | c1,c2 => c2
  | c1,c3 => c3
  | c1,c4 => c4
  | c1,c5 => c5
  | c1,c6 => c6
  | c1,c7 => c7
  | c1,c8 => c8
  | c2,c0 => c0
  | c2,c1 => c2
  | c2,c2 => c1
  | c2,c3 => c6
  | c2,c4 => c8
  | c2,c5 => c7
  | c2,c6 => c3
  | c2,c7 => c5
  | c2,c8 => c4
  | c3,c0 => c0
  | c3,c1 => c3
  | c3,c2 => c6
  | c3,c3 => c2
  | c3,c4 => c5
  | c3,c5 => c8
  | c3,c6 => c1
  | c3,c7 => c4
  | c3,c8 => c7
  | c4,c0 => c0
  | c4,c1 => c4
  | c4,c2 => c8
  | c4,c3 => c5
  | c4,c4 => c6
  | c4,c5 => c1
  | c4,c6 => c7
  | c4,c7 => c2
  | c4,c8 => c3
  | c5,c0 => c0
  | c5,c1 => c5
  | c5,c2 => c7
  | c5,c3 => c8
  | c5,c4 => c1
  | c5,c5 => c3
  | c5,c6 => c4
  | c5,c7 => c6
  | c5,c8 => c2
  | c6,c0 => c0
  | c6,c1 => c6
  | c6,c2 => c3
  | c6,c3 => c1
  | c6,c4 => c7
  | c6,c5 => c4
  | c6,c6 => c2
  | c6,c7 => c8
  | c6,c8 => c5
  | c7,c0 => c0
  | c7,c1 => c7
  | c7,c2 => c5
  | c7,c3 => c4
  | c7,c4 => c2
  | c7,c5 => c6
  | c7,c6 => c8
  | c7,c7 => c3
  | c7,c8 => c1
  | c8,c0 => c0
  | c8,c1 => c8
  | c8,c2 => c4
  | c8,c3 => c7
  | c8,c4 => c3
  | c8,c5 => c2
  | c8,c6 => c5
  | c8,c7 => c1
  | c8,c8 => c6
def neg : F → F
  | c0 => c0
  | c1 => c2
  | c2 => c1
  | c3 => c6
  | c4 => c8
  | c5 => c7
  | c6 => c3
  | c7 => c5
  | c8 => c4
instance : Add F := ⟨add⟩
instance : Mul F := ⟨mul⟩
instance : Neg F := ⟨neg⟩
instance : CommRing F where
  add_assoc := by decide +kernel
  zero_add := by decide +kernel
  add_zero := by decide +kernel
  add_comm := by decide +kernel
  neg_add_cancel := by decide +kernel
  nsmul := nsmulRec
  zsmul := zsmulRec
  mul_assoc := by decide +kernel
  one_mul := by decide +kernel
  mul_one := by decide +kernel
  mul_comm := by decide +kernel
  left_distrib := by decide +kernel
  right_distrib := by decide +kernel
  zero_mul := by decide +kernel
  mul_zero := by decide +kernel
def ofCode (n : Nat) : F := match n % 9 with
  | 0 => c0
  | 1 => c1
  | 2 => c2
  | 3 => c3
  | 4 => c4
  | 5 => c5
  | 6 => c6
  | 7 => c7
  | _ => c8
def code : F → Nat
  | c0 => 0
  | c1 => 1
  | c2 => 2
  | c3 => 3
  | c4 => 4
  | c5 => 5
  | c6 => 6
  | c7 => 7
  | c8 => 8
theorem code_lt (a : F) : code a < 9 := by cases a <;> decide
theorem ofCode_code (a : F) : ofCode (code a) = a := by cases a <;> rfl
theorem code_ofCode (a : Fin 9) : code (ofCode a.val) = a.val := by revert a; decide +kernel
end F
abbrev Vec := Fin 3 → F
abbrev Mat := Fin 3 → Fin 3 → F
def act (A : Mat) (x : Vec) : Vec := fun i => A i 0 * x 0 + A i 1 * x 1 + A i 2 * x 2

theorem act_add (A : Mat) (x y : Vec) : act A (x + y) = act A x + act A y := by
  funext i
  simp only [act, Pi.add_apply, mul_add]
  abel

theorem act_smul (A : Mat) (t : F) (x : Vec) : act A (t • x) = t • act A x := by
  funext i
  simp only [act, Pi.smul_apply, smul_eq_mul]
  ring

def basisVec (j : Fin 3) : Vec := fun i => if i = j then 1 else 0

theorem vec_basis (x : Vec) :
    x = x 0 • basisVec 0 + x 1 • basisVec 1 + x 2 • basisVec 2 := by
  funext i
  fin_cases i <;> simp [basisVec]

theorem additive_ext (f g : Vec → Vec)
    (fa : ∀ x y, f (x+y) = f x + f y) (ga : ∀ x y, g (x+y) = g x + g y)
    (fs : ∀ (t : F) (x : Vec), f (t • x) = t • f x) (gs : ∀ (t : F) (x : Vec), g (t • x) = t • g x)
    (h : ∀ j, f (basisVec j) = g (basisVec j)) : f = g := by
  funext x
  conv_lhs => rw [vec_basis x]
  conv_rhs => rw [vec_basis x]
  simp only [fa, ga, fs, gs, h]
end DegreeDiameter.Portfolio.F9Graph56862
