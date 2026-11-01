import Aris4Math.ThirtyFour.TwentyOneSevenTriple788
namespace Aris4Math.ThirtyFour.TwentyOneSevenTriple788Coverage
open Aris4Math.ThirtyThree.TripleProfiles
set_option maxRecDepth 100000
set_option maxHeartbeats 0
abbrev Case:=Fin 11
abbrev Perm:=Fin 2
def permFn : Perm→Fin 3→Fin 3:=![![0,1,2],![0,2,1]]
theorem permFn_injective : ∀p,Function.Injective (permFn p) := by decide +kernel
noncomputable def perm (p : Perm) : Equiv.Perm (Fin 3):=
  Equiv.ofBijective (permFn p) ⟨permFn_injective p,Finite.surjective_of_injective (permFn_injective p)⟩
def choose : ℕ→Case×Perm
  | 3 => (0,0)
  | 4 => (2,0)
  | 5 => (4,0)
  | 6 => (6,0)
  | 7 => (8,0)
  | 12 => (1,0)
  | 13 => (3,0)
  | 14 => (5,0)
  | 15 => (7,0)
  | 16 => (9,0)
  | 17 => (10,0)
  | _ => (0,0)
def code (c : Fin 9) (t : Fin 2) : ℕ:=c.val+9*t.val

theorem coverage : ∀c : Fin 9,∀t : Fin 2,t.val≤c.val→1+c.val≤8+t.val→
    c.val≤2 ∨
    (∀T,recovered 34 7 8 8 1 1 c.val t.val
      (T.map (perm (choose (code c t)).2).toEmbedding)=TwentyOneSevenTriple788Data.μ (choose (code c t)).1 T) := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSevenTriple788Coverage
