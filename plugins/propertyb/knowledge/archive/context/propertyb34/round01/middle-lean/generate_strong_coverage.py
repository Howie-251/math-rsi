"""Full labelled coverage, orbit transport, and actual high-codegree callers."""
from pathlib import Path
from itertools import permutations, combinations
import json

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).parent
OUT = ROOT / "formal/Aris4Math/ThirtyFour"
vec = lambda xs: "![" + ",".join(map(str, xs)) + "]"
perms = list(permutations(range(3)))
for v, word, cutoff in [(22, "TwentyTwo", 3), (23, "TwentyThree", 4)]:
    triple = word + "StrongTriple777"
    name = word + "StrongCoverage"
    reps = json.loads((HERE / (triple + "_REPLAY.json")).read_text())
    base = cutoff + 1
    lookup = {}
    for case, row in enumerate(reps):
        for p, perm in enumerate(perms):
            counts = {sum(1 << perm[j] for j in range(3) if int(t) >> j & 1): m
                      for t, m in row["counts"].items()}
            co = [sum(m for t, m in counts.items() if t & mask == mask) for mask in (3, 5, 6)]
            code = sum(a * base**j for j, a in enumerate(co)) + base**3 * counts.get(7, 0)
            lookup.setdefault(code, (case, p))
    s = f'''import Aris4Math.ThirtyFour.{triple}
import Aris4Math.ThirtyFour.LockRelabel
import Aris4Math.ThirtyFour.TwentyOneSixIncidence
namespace Aris4Math.ThirtyFour.{name}
open Aris4Math.ThirtyThree.TripleProfiles
open {triple}Data (Case μ)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
abbrev Perm := Fin 6
def permFn : Perm → Fin 3 → Fin 3 := {vec(vec(p) for p in perms)}
theorem permFn_injective : ∀ p, Function.Injective (permFn p) := by decide +kernel
noncomputable def perm (p : Perm) : Equiv.Perm (Fin 3) :=
  Equiv.ofBijective (permFn p) ⟨permFn_injective p,Finite.surjective_of_injective (permFn_injective p)⟩
def choose : ℕ → Case × Perm
'''
    s += "".join(f"  | {k} => ({c},{p})\n" for k, (c, p) in sorted(lookup.items()))
    s += f'''  | _ => (0,0)
def code (a b c t : Fin {base}) : ℕ := a.val+{base}*b.val+{base**2}*c.val+{base**3}*t.val

set_option synthInstance.maxSize 1000 in
theorem coverage : ∀ a b c t : Fin {base},
    1≤a.val → 1≤b.val → 1≤c.val →
    (a.val={cutoff} ∨ b.val={cutoff} ∨ c.val={cutoff}) →
    t.val≤a.val → t.val≤b.val → t.val≤c.val →
    a.val+b.val≤7+t.val → a.val+c.val≤7+t.val → b.val+c.val≤7+t.val →
    ∀ T, recovered 34 7 7 7 a.val b.val c.val t.val
      (T.map (perm (choose (code a b c t)).2).toEmbedding)=μ (choose (code a b c t)).1 T := by decide +kernel

theorem propertyB_of_triple (H : Simple5Hypergraph (Fin {v})) (cover : H.PairCovering)
    (size : H.edges.card=34) (f : Fin 3 ↪ Fin {v})
    (degrees : ∀ j, H.degree (f j)=7)
    (pairs : ∀ i j, i≠j → H.codegree (f i) (f j)≤{cutoff})
    (high : H.codegree (f 0) (f 1)={cutoff}) : PropertyB H := by
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
  let a : Fin {base} := ⟨H.codegree (f 0) (f 1),by omega⟩
  let b : Fin {base} := ⟨H.codegree (f 0) (f 2),by omega⟩
  let c : Fin {base} := ⟨H.codegree (f 1) (f 2),by omega⟩
  let t : Fin {base} := ⟨tripleCodegree H (f 0) (f 1) (f 2),by omega⟩
  have matched := coverage a b c t la lb lc (Or.inl high) ta tb tc ia ib ic
  let chosen := choose (code a b c t)
  let σ := perm chosen.2
  apply {triple}.propertyB_of_counts H (σ.toEmbedding.trans f) chosen.1
  intro T
  rw [LockRelabel.count_comp_perm]
  change count H f (T.map σ.toEmbedding)=_
  rw [actual_recovered,triple_count_eq,size,degrees 0,degrees 1,degrees 2]
  exact matched T
end Aris4Math.ThirtyFour.{name}
#print axioms Aris4Math.ThirtyFour.{name}.propertyB_of_triple
'''
    (OUT / (name + ".lean")).write_text(s)

    name = word + "StrongCodegree"
    pos = 13 if v == 22 else 14
    s = f'''import Aris4Math.ThirtyFour.{word}StrongCoverage
import Aris4Math.ThirtyFour.NineteenPairs
import Aris4Math.ThirtyThree.TwentyThreeSelection
namespace Aris4Math.ThirtyFour.{name}
open Aris4Math.TypeCounting Aris4Math.DoubleLockProfiles
open Aris4Math.ThirtyThree.DoubleLockAt
open Aris4Math.ThirtyThree.TripleProfiles
open Aris4Math.ThirtyThree.TwentyThreeSelection (sevenVertices mem_sevenVertices)
open NineteenPairs
set_option maxHeartbeats 0
set_option maxRecDepth 100000

theorem pair_certificates : ∀ l : Fin 8, {cutoff+1}≤l.val →
    Numeric.validProfile (pairProfile {v} 1 {pos} 7 7 l.val []) 34 ∧
    Numeric.totalBound (pairProfile {v} 1 {pos} 7 7 l.val [])<1 := by
  unfold Numeric.validProfile
  decide +kernel

theorem propertyB_of_pair (H : Simple5Hypergraph (Fin {v})) (size : H.edges.card=34)
    (x y : Fin {v}) (xy : x≠y) (dx : H.degree x=7) (dy : H.degree y=7)
    (high : {cutoff+1}≤H.codegree x y) : PropertyB H := by
  have upper := ThirtyThree.TwentyOnePairAssembly.codegree_le_degree H x y
  rw [dx] at upper
  obtain ⟨valid,strict⟩ := pair_certificates ⟨H.codegree x y,by omega⟩ high
  have real := realizes_pair_profile H size (by decide : 1≤1) (by decide : 1<{pos})
    (by decide : {pos}≤{v}) x y xy [] (by simpa only [dx,dy] using valid)
  apply ProfileApplication.propertyB_of_uncorrected_profile H (twoVertices x y xy)
    (positionsAt {v} 1 {pos} (by decide) (by decide) (by decide))
    (pairProfile {v} 1 {pos} (H.degree x) (H.degree y) (H.codegree x y) []) real rfl rfl
  simpa only [dx,dy] using strict

/-- An actual degree-seven pair is small, after the proved strict branches. -/
theorem codegree_le (H : Simple5Hypergraph (Fin {v})) (cover : H.PairCovering)
    (size : H.edges.card=34) (many : 3≤(sevenVertices H).card) (noB : ¬PropertyB H)
    (x y : Fin {v}) (xy : x≠y) (dx : H.degree x=7) (dy : H.degree y=7) :
    H.codegree x y≤{cutoff-1} := by
  have upper (a b : Fin {v}) (ab : a≠b) (da : H.degree a=7) (db : H.degree b=7) :
      H.codegree a b≤{cutoff} := by
    by_contra h
    exact noB (propertyB_of_pair H size a b ab da db (by omega))
  have ux := upper x y xy dx dy
  by_contra fail
  have high : H.codegree x y={cutoff} := by omega
  have exists_third : ∃ z∈sevenVertices H, z≠x ∧ z≠y := by
    by_contra! h
    have sub : sevenVertices H⊆({{x,y}} : Finset (Fin {v})) := by
      intro z hz
      by_cases zx : z=x
      · simp [zx]
      · simp [h z hz zx]
    have bound := (Finset.card_le_card sub).trans Finset.card_le_two
    omega
  obtain ⟨z,hz,zx,zy⟩ := exists_third
  have dz := (mem_sevenVertices H z).mp hz
  let f := threeVertices x y z xy zx.symm zy.symm
  have degrees : ∀ j, H.degree (f j)=7 := by
    intro j
    fin_cases j
    · exact dx
    · exact dy
    · exact dz
  apply noB
  exact {word}StrongCoverage.propertyB_of_triple H cover size f degrees
    (fun i j ij => upper (f i) (f j) (f.injective.ne ij) (degrees i) (degrees j)) high
end Aris4Math.ThirtyFour.{name}
#print axioms Aris4Math.ThirtyFour.{name}.codegree_le
'''
    (OUT / (name + ".lean")).write_text(s)
    print(v, "orbit representatives", len(reps), "labelled profiles", len(lookup))
