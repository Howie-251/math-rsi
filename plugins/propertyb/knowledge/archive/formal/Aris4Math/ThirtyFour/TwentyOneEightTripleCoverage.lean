import Aris4Math.ThirtyFour.TwentyOneEightTriple888
import Aris4Math.ThirtyFour.TwentyOneEightJointTriple0
namespace Aris4Math.ThirtyFour.TwentyOneEightTripleCoverage
open scoped BigOperators
open Aris4Math.ThirtyThree.TripleProfiles
set_option maxRecDepth 100000
set_option maxHeartbeats 0
abbrev Case:=Fin 15
abbrev Perm:=Fin 6
def permFn : Perm→Fin 3→Fin 3:=![![0,1,2],![0,2,1],![1,0,2],![1,2,0],![2,0,1],![2,1,0]]
theorem permFn_injective : ∀p,Function.Injective (permFn p) := by decide +kernel
noncomputable def perm (p : Perm) : Equiv.Perm (Fin 3):=
  Equiv.ofBijective (permFn p) ⟨permFn_injective p,Finite.surjective_of_injective (permFn_injective p)⟩
def μ (c : Case) (T : Finset (Fin 3)) : ℕ:=
  if h:c.val<14 then TwentyOneEightTriple888Data.μ ⟨c.val,h⟩ T else TwentyOneEightJointTriple0Data.μ T

def choose : ℕ→Case×Perm
  | 0 => (0,0)
  | 5 => (3,5)
  | 7 => (3,3)
  | 8 => (5,3)
  | 11 => (3,4)
  | 15 => (3,2)
  | 17 => (8,3)
  | 19 => (3,1)
  | 20 => (5,1)
  | 21 => (3,0)
  | 23 => (8,1)
  | 24 => (5,0)
  | 25 => (8,0)
  | 27 => (1,0)
  | 29 => (2,4)
  | 32 => (4,5)
  | 33 => (2,2)
  | 34 => (4,3)
  | 35 => (6,3)
  | 38 => (4,4)
  | 41 => (14,4)
  | 42 => (4,2)
  | 43 => (14,2)
  | 44 => (9,3)
  | 45 => (2,0)
  | 46 => (4,1)
  | 47 => (6,1)
  | 48 => (4,0)
  | 49 => (14,0)
  | 50 => (9,1)
  | 51 => (6,0)
  | 52 => (9,0)
  | 53 => (11,0)
  | 68 => (7,4)
  | 70 => (7,2)
  | 71 => (10,3)
  | 76 => (7,0)
  | 77 => (10,1)
  | 79 => (10,0)
  | 80 => (12,0)
  | 107 => (13,0)
  | _ => (0,0)
def code (a b c : Fin 3) (t : Fin 4) : ℕ:=a.val+3*b.val+9*c.val+27*t.val
def Residue (a b c t : ℕ) : Prop:=
  ((a=3 ∨ b=3 ∨ c=3)→t=0) ∧ ¬(a=1 ∧ b=1 ∧ c=1)
instance (a b c t : ℕ) : Decidable (Residue a b c t) := by unfold Residue;infer_instance

theorem coverage : ∀a b c : Fin 3,∀t : Fin 4,
    t.val≤a.val+1→t.val≤b.val+1→t.val≤c.val+1→
    Residue (a.val+1) (b.val+1) (c.val+1) t.val ∨
    (∀T,recovered 34 8 8 8 (a.val+1) (b.val+1) (c.val+1) t.val
      (T.map (perm (choose (code a b c t)).2).toEmbedding)=μ (choose (code a b c t)).1 T) := by decide +kernel

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 21)) (f : Fin 3↪Fin 21)
    (c : Case) (counts : ∀T,Aris4Math.ThirtyThree.MultiLockRecovery.count H f T=μ c T) : PropertyB H := by
  by_cases small:c.val<14
  · apply TwentyOneEightTriple888.propertyB_of_counts H f ⟨c.val,small⟩
    simpa only [μ,dif_pos small] using counts
  · apply TwentyOneEightJointTriple0.propertyB_of_counts H f
    simpa only [μ,dif_neg small] using counts
end Aris4Math.ThirtyFour.TwentyOneEightTripleCoverage
