import Aris4Math.ThirtyFour.TwentyOneSevenQuad7888
import Aris4Math.ThirtyThree.TwentyTwoQuadAssembly
namespace Aris4Math.ThirtyFour.TwentyOneSevenUnitQuadCoverage
open scoped BigOperators
open Aris4Math.ThirtyThree.QuadProfiles
set_option maxRecDepth 100000
set_option maxHeartbeats 0
abbrev Case:=Fin 18
abbrev Perm:=Fin 6
def permFn : Perm→Fin 4→Fin 4:=![![0,1,2,3],![0,1,3,2],![0,2,1,3],![0,2,3,1],![0,3,1,2],![0,3,2,1]]
theorem permFn_injective : ∀p,Function.Injective (permFn p) := by decide +kernel
noncomputable def perm (p : Perm) : Equiv.Perm (Fin 4):=
  Equiv.ofBijective (permFn p) ⟨permFn_injective p,Finite.surjective_of_injective (permFn_injective p)⟩
def choose : ℕ→Case×Perm
  | 0 => (0,0)
  | 1 => (4,4)
  | 2 => (4,2)
  | 3 => (10,3)
  | 4 => (4,0)
  | 5 => (10,1)
  | 6 => (10,0)
  | 8 => (2,4)
  | 9 => (6,4)
  | 10 => (8,3)
  | 11 => (12,5)
  | 12 => (8,1)
  | 13 => (12,4)
  | 14 => (14,0)
  | 24 => (2,2)
  | 25 => (8,5)
  | 26 => (6,2)
  | 27 => (12,3)
  | 28 => (8,0)
  | 29 => (14,1)
  | 30 => (12,2)
  | 72 => (2,0)
  | 73 => (8,4)
  | 74 => (8,2)
  | 75 => (14,3)
  | 76 => (6,0)
  | 77 => (12,1)
  | 78 => (12,0)
  | 216 => (1,0)
  | 217 => (5,4)
  | 218 => (5,2)
  | 219 => (11,3)
  | 220 => (5,0)
  | 221 => (11,1)
  | 222 => (11,0)
  | 225 => (7,4)
  | 227 => (13,5)
  | 229 => (13,4)
  | 242 => (7,2)
  | 243 => (13,3)
  | 246 => (13,2)
  | 292 => (7,0)
  | 293 => (13,1)
  | 294 => (13,0)
  | 648 => (3,0)
  | 649 => (9,4)
  | 650 => (9,2)
  | 651 => (15,3)
  | 652 => (9,0)
  | 653 => (15,1)
  | 654 => (15,0)
  | 655 => (16,0)
  | 871 => (17,0)
  | _ => (0,0)
def co (a b c : ℕ) : Fin 6→ℕ:=![1,1,1,a,b,c]
def code (a b c : Fin 2) (h : Fin 5→Fin 3) : ℕ:=a.val+2*b.val+4*c.val+8*(∑j,(h j).val*3^j.val)

theorem coverage : ∀a b c : Fin 2,∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤co (a.val+1) (b.val+1) (c.val+1) j)→
    (a.val+1=2 ∧ b.val+1=2 ∧ c.val+1=2 ∧ (h 4).val=0) ∨
    (∀T,recovered 34 ![7,8,8,8] (co (a.val+1) (b.val+1) (c.val+1)) (fun j=>(h j).val)
      (T.map (perm (choose (code a b c h)).2).toEmbedding)=TwentyOneSevenQuad7888Data.μ (choose (code a b c h)).1 T) := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSevenUnitQuadCoverage
