import DegreeDiameter.Portfolio.SingleExtension
import Mathlib.Data.Fin.VecNotation
import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Ring
import Mathlib.Tactic.DeriveFintype

namespace DegreeDiameter.Portfolio.F4Graph3840
/-- Polynomial encoding 0,1,w,w+1, with w²=w+1. Numerals in this ring
are characteristic-two numerals; literal parameters use `ofCode`. -/
inductive F where
  | z | o | w | v
  deriving DecidableEq, Fintype
namespace F
instance : Zero F := ⟨z⟩
instance : One F := ⟨o⟩
def add : F → F → F
  | z,b => b
  | a,z => a
  | o,o => z
  | o,w => v
  | o,v => w
  | w,o => v
  | w,w => z
  | w,v => o
  | v,o => w
  | v,w => o
  | v,v => z
def mul : F → F → F
  | z,_ => z
  | _,z => z
  | o,b => b
  | a,o => a
  | w,w => v
  | w,v => o
  | v,w => o
  | v,v => w
instance : Add F := ⟨add⟩
instance : Mul F := ⟨mul⟩
instance : Neg F := ⟨id⟩
instance : CommRing F where
  add_assoc := by decide
  zero_add := by decide
  add_zero := by decide
  add_comm := by decide
  neg_add_cancel := by decide
  nsmul := nsmulRec
  zsmul := zsmulRec
  mul_assoc := by decide
  one_mul := by decide
  mul_one := by decide
  mul_comm := by decide
  left_distrib := by decide
  right_distrib := by decide
  zero_mul := by decide
  mul_zero := by decide

def ofCode (n : Nat) : F := match n % 4 with | 0 => z | 1 => o | 2 => w | _ => v
def code : F → Nat | z => 0 | o => 1 | w => 2 | v => 3
theorem code_lt (a : F) : code a < 4 := by cases a <;> decide
theorem ofCode_code (a : F) : ofCode (code a) = a := by cases a <;> rfl
theorem code_ofCode (a : Fin 4) : code (ofCode a.val) = a.val := by revert a; decide
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
end DegreeDiameter.Portfolio.F4Graph3840
