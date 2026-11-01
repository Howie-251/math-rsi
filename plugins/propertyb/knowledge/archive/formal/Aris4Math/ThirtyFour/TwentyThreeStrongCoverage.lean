import Aris4Math.ThirtyFour.TwentyThreeStrongTriple777
import Aris4Math.ThirtyFour.LockRelabel
import Aris4Math.ThirtyFour.TwentyOneSixIncidence
namespace Aris4Math.ThirtyFour.TwentyThreeStrongCoverage
open Aris4Math.ThirtyThree.TripleProfiles
open TwentyThreeStrongTriple777Data (Case μ)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
abbrev Perm := Fin 6
def permFn : Perm → Fin 3 → Fin 3 := ![![0,1,2],![0,2,1],![1,0,2],![1,2,0],![2,0,1],![2,1,0]]
theorem permFn_injective : ∀ p, Function.Injective (permFn p) := by decide +kernel
noncomputable def perm (p : Perm) : Equiv.Perm (Fin 3) :=
  Equiv.ofBijective (permFn p) ⟨permFn_injective p,Finite.surjective_of_injective (permFn_injective p)⟩
def choose : ℕ → Case × Perm
  | 34 => (0,4)
  | 39 => (2,5)
  | 44 => (4,5)
  | 46 => (0,2)
  | 47 => (2,3)
  | 48 => (4,3)
  | 59 => (2,4)
  | 64 => (7,4)
  | 69 => (10,5)
  | 71 => (2,2)
  | 72 => (7,2)
  | 73 => (10,3)
  | 84 => (4,4)
  | 89 => (10,4)
  | 94 => (15,4)
  | 96 => (4,2)
  | 97 => (10,2)
  | 98 => (15,2)
  | 106 => (0,0)
  | 107 => (2,1)
  | 108 => (4,1)
  | 111 => (2,0)
  | 112 => (7,0)
  | 113 => (10,1)
  | 116 => (4,0)
  | 117 => (10,0)
  | 118 => (15,0)
  | 159 => (1,4)
  | 164 => (3,5)
  | 169 => (5,5)
  | 171 => (1,2)
  | 172 => (3,3)
  | 173 => (5,3)
  | 174 => (6,3)
  | 184 => (3,4)
  | 189 => (8,4)
  | 194 => (11,5)
  | 196 => (3,2)
  | 197 => (8,2)
  | 198 => (11,3)
  | 199 => (13,3)
  | 209 => (5,4)
  | 214 => (11,4)
  | 219 => (16,4)
  | 221 => (5,2)
  | 222 => (11,2)
  | 223 => (16,2)
  | 224 => (19,3)
  | 231 => (1,0)
  | 232 => (3,1)
  | 233 => (5,1)
  | 234 => (6,1)
  | 236 => (3,0)
  | 237 => (8,0)
  | 238 => (11,1)
  | 239 => (13,1)
  | 241 => (5,0)
  | 242 => (11,0)
  | 243 => (16,0)
  | 244 => (19,1)
  | 246 => (6,0)
  | 247 => (13,0)
  | 248 => (19,0)
  | 249 => (22,0)
  | 314 => (9,4)
  | 319 => (12,5)
  | 322 => (9,2)
  | 323 => (12,3)
  | 324 => (14,3)
  | 339 => (12,4)
  | 344 => (17,4)
  | 347 => (12,2)
  | 348 => (17,2)
  | 349 => (20,3)
  | 362 => (9,0)
  | 363 => (12,1)
  | 364 => (14,1)
  | 367 => (12,0)
  | 368 => (17,0)
  | 369 => (20,1)
  | 372 => (14,0)
  | 373 => (20,0)
  | 374 => (23,0)
  | 469 => (18,4)
  | 473 => (18,2)
  | 474 => (21,3)
  | 493 => (18,0)
  | 494 => (21,1)
  | 498 => (21,0)
  | 499 => (24,0)
  | 624 => (25,0)
  | _ => (0,0)
def code (a b c t : Fin 5) : ℕ := a.val+5*b.val+25*c.val+125*t.val

set_option synthInstance.maxSize 1000 in
theorem coverage : ∀ a b c t : Fin 5,
    1≤a.val → 1≤b.val → 1≤c.val →
    (a.val=4 ∨ b.val=4 ∨ c.val=4) →
    t.val≤a.val → t.val≤b.val → t.val≤c.val →
    a.val+b.val≤7+t.val → a.val+c.val≤7+t.val → b.val+c.val≤7+t.val →
    ∀ T, recovered 34 7 7 7 a.val b.val c.val t.val
      (T.map (perm (choose (code a b c t)).2).toEmbedding)=μ (choose (code a b c t)).1 T := by decide +kernel

theorem propertyB_of_triple (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (size : H.edges.card=34) (f : Fin 3 ↪ Fin 23)
    (degrees : ∀ j, H.degree (f j)=7)
    (pairs : ∀ i j, i≠j → H.codegree (f i) (f j)≤4)
    (high : H.codegree (f 0) (f 1)=4) : PropertyB H := by
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
  let a : Fin 5 := ⟨H.codegree (f 0) (f 1),by omega⟩
  let b : Fin 5 := ⟨H.codegree (f 0) (f 2),by omega⟩
  let c : Fin 5 := ⟨H.codegree (f 1) (f 2),by omega⟩
  let t : Fin 5 := ⟨tripleCodegree H (f 0) (f 1) (f 2),by omega⟩
  have matched := coverage a b c t la lb lc (Or.inl high) ta tb tc ia ib ic
  let chosen := choose (code a b c t)
  let σ := perm chosen.2
  apply TwentyThreeStrongTriple777.propertyB_of_counts H (σ.toEmbedding.trans f) chosen.1
  intro T
  rw [LockRelabel.count_comp_perm]
  change count H f (T.map σ.toEmbedding)=_
  rw [actual_recovered,triple_count_eq,size,degrees 0,degrees 1,degrees 2]
  exact matched T
end Aris4Math.ThirtyFour.TwentyThreeStrongCoverage
#print axioms Aris4Math.ThirtyFour.TwentyThreeStrongCoverage.propertyB_of_triple
