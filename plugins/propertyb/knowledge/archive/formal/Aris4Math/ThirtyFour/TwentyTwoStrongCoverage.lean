import Aris4Math.ThirtyFour.TwentyTwoStrongTriple777
import Aris4Math.ThirtyFour.LockRelabel
import Aris4Math.ThirtyFour.TwentyOneSixIncidence
namespace Aris4Math.ThirtyFour.TwentyTwoStrongCoverage
open Aris4Math.ThirtyThree.TripleProfiles
open TwentyTwoStrongTriple777Data (Case μ)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
abbrev Perm := Fin 6
def permFn : Perm → Fin 3 → Fin 3 := ![![0,1,2],![0,2,1],![1,0,2],![1,2,0],![2,0,1],![2,1,0]]
theorem permFn_injective : ∀ p, Function.Injective (permFn p) := by decide +kernel
noncomputable def perm (p : Perm) : Equiv.Perm (Fin 3) :=
  Equiv.ofBijective (permFn p) ⟨permFn_injective p,Finite.surjective_of_injective (permFn_injective p)⟩
def choose : ℕ → Case × Perm
  | 23 => (0,4)
  | 27 => (2,5)
  | 29 => (0,2)
  | 30 => (2,3)
  | 31 => (4,3)
  | 39 => (2,4)
  | 43 => (6,4)
  | 45 => (2,2)
  | 46 => (6,2)
  | 47 => (9,3)
  | 53 => (0,0)
  | 54 => (2,1)
  | 55 => (4,1)
  | 57 => (2,0)
  | 58 => (6,0)
  | 59 => (9,1)
  | 61 => (4,0)
  | 62 => (9,0)
  | 63 => (12,0)
  | 87 => (1,4)
  | 91 => (3,5)
  | 93 => (1,2)
  | 94 => (3,3)
  | 95 => (5,3)
  | 103 => (3,4)
  | 107 => (7,4)
  | 109 => (3,2)
  | 110 => (7,2)
  | 111 => (10,3)
  | 117 => (1,0)
  | 118 => (3,1)
  | 119 => (5,1)
  | 121 => (3,0)
  | 122 => (7,0)
  | 123 => (10,1)
  | 125 => (5,0)
  | 126 => (10,0)
  | 127 => (13,0)
  | 171 => (8,4)
  | 174 => (8,2)
  | 175 => (11,3)
  | 186 => (8,0)
  | 187 => (11,1)
  | 190 => (11,0)
  | 191 => (14,0)
  | 255 => (15,0)
  | _ => (0,0)
def code (a b c t : Fin 4) : ℕ := a.val+4*b.val+16*c.val+64*t.val

set_option synthInstance.maxSize 1000 in
theorem coverage : ∀ a b c t : Fin 4,
    1≤a.val → 1≤b.val → 1≤c.val →
    (a.val=3 ∨ b.val=3 ∨ c.val=3) →
    t.val≤a.val → t.val≤b.val → t.val≤c.val →
    a.val+b.val≤7+t.val → a.val+c.val≤7+t.val → b.val+c.val≤7+t.val →
    ∀ T, recovered 34 7 7 7 a.val b.val c.val t.val
      (T.map (perm (choose (code a b c t)).2).toEmbedding)=μ (choose (code a b c t)).1 T := by decide +kernel

theorem propertyB_of_triple (H : Simple5Hypergraph (Fin 22)) (cover : H.PairCovering)
    (size : H.edges.card=34) (f : Fin 3 ↪ Fin 22)
    (degrees : ∀ j, H.degree (f j)=7)
    (pairs : ∀ i j, i≠j → H.codegree (f i) (f j)≤3)
    (high : H.codegree (f 0) (f 1)=3) : PropertyB H := by
  have xy := f.injective.ne (by decide : (0:Fin 3)≠1)
  have xz := f.injective.ne (by decide : (0:Fin 3)≠2)
  have yz := f.injective.ne (by decide : (1:Fin 3)≠2)
  have la := H.one_le_codegree cover xy
  have lb := H.one_le_codegree cover xz
  have lc := H.one_le_codegree cover yz
  have ua := pairs 0 1 (by decide)
  have ub := pairs 0 2 (by decide)
  have uc := pairs 1 2 (by decide)
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H (f 0) (f 1) (f 2)
  obtain ⟨ia,ib,ic⟩ := TwentyOneSixIncidence.inventories H (f 0) (f 1) (f 2) xy xz yz
  rw [degrees 0] at ia
  rw [degrees 1] at ib
  rw [degrees 2] at ic
  let a : Fin 4 := ⟨H.codegree (f 0) (f 1),by omega⟩
  let b : Fin 4 := ⟨H.codegree (f 0) (f 2),by omega⟩
  let c : Fin 4 := ⟨H.codegree (f 1) (f 2),by omega⟩
  let t : Fin 4 := ⟨tripleCodegree H (f 0) (f 1) (f 2),by omega⟩
  have matched := coverage a b c t la lb lc (Or.inl high) ta tb tc ia ib ic
  let chosen := choose (code a b c t)
  let σ := perm chosen.2
  apply TwentyTwoStrongTriple777.propertyB_of_counts H (σ.toEmbedding.trans f) chosen.1
  intro T
  rw [LockRelabel.count_comp_perm]
  change count H f (T.map σ.toEmbedding)=_
  rw [actual_recovered,triple_count_eq,size,degrees 0,degrees 1,degrees 2]
  exact matched T
end Aris4Math.ThirtyFour.TwentyTwoStrongCoverage
#print axioms Aris4Math.ThirtyFour.TwentyTwoStrongCoverage.propertyB_of_triple
