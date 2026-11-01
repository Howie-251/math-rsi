from pathlib import Path
from itertools import permutations,combinations
import json
ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).parent
vec=lambda xs:'!['+','.join(map(str,xs))+']'
for n,kind,ordinary,joint in [(3,'Triple','TwentyOneEightTriple888','TwentyOneEightJointTriple0'),(4,'Quad','TwentyOneEightQuad8888','TwentyOneEightJointQuad0')]:
 reps=json.load(open(HERE/(ordinary+'_REPLAY.json')))
 mus=[{int(k):v for k,v in r['counts'].items()} for r in reps]
 jfile='EIGHT_TRIPLES_STRICT_JOINT' if n==3 else 'FOUR_EIGHTS_STRICT_JOINT'
 jointrows=json.load(open(ROOT/f'context/propertyb34/round01/twentyone-math/{jfile}.json'))['results']
 mus.append({int(k):v for k,v in jointrows[0]['counts'].items()})
 ps=list(permutations(range(n)));pairs=list(combinations(range(n),2));high=[7] if n==3 else [7,11,13,14,15]
 def trans(ns,p):
  return {sum(1<<p[i] for i in range(n) if t>>i&1):m for t,m in ns.items() if m}
 def key(ns):
  co=[sum(m for t,m in ns.items() if all(t>>i&1 for i in pair))-1 for pair in pairs]
  hs=[ns.get(t,0) for t in high]
  base=3 if n==3 else 2
  return sum(a*base**j for j,a in enumerate(co))+base**len(co)*sum(a*(4 if n==3 else 3)**j for j,a in enumerate(hs))
 lookup={}
 for c,mu in enumerate(mus):
  for p,perm in enumerate(ps):
   actual=trans(mu,perm)
   k=key(actual)
   lookup.setdefault(k,(c,p))
 fs=lambda t:'{'+','.join(str(i) for i in range(n) if t>>i&1)+'}' if t else '∅'
 name='TwentyOneEight'+kind+'Coverage'
 s=f'''import Aris4Math.ThirtyFour.{ordinary}
import Aris4Math.ThirtyFour.{joint}
namespace Aris4Math.ThirtyFour.{name}
open scoped BigOperators
open Aris4Math.ThirtyThree.{'TripleProfiles' if n==3 else 'QuadProfiles'}
set_option maxRecDepth 100000
set_option maxHeartbeats 0
abbrev Case:=Fin {len(mus)}
abbrev Perm:=Fin {len(ps)}
def permFn : Perm→Fin {n}→Fin {n}:={vec(vec(p) for p in ps)}
theorem permFn_injective : ∀p,Function.Injective (permFn p) := by decide +kernel
noncomputable def perm (p : Perm) : Equiv.Perm (Fin {n}):=
  Equiv.ofBijective (permFn p) ⟨permFn_injective p,Finite.surjective_of_injective (permFn_injective p)⟩
def μ (c : Case) (T : Finset (Fin {n})) : ℕ:=
  if h:c.val<{len(reps)} then {ordinary}Data.μ ⟨c.val,h⟩ T else {joint}Data.μ T

def choose : ℕ→Case×Perm
'''
 for k,(c,p) in sorted(lookup.items()):s+=f'  | {k} => ({c},{p})\n'
 s+='  | _ => (0,0)\n'
 if n==3:
  s+='''def code (a b c : Fin 3) (t : Fin 4) : ℕ:=a.val+3*b.val+9*c.val+27*t.val
def Residue (a b c t : ℕ) : Prop:=
  ((a=3 ∨ b=3 ∨ c=3)→t=0) ∧ ¬(a=1 ∧ b=1 ∧ c=1)
instance (a b c t : ℕ) : Decidable (Residue a b c t) := by unfold Residue;infer_instance

theorem coverage : ∀a b c : Fin 3,∀t : Fin 4,
    t.val≤a.val+1→t.val≤b.val+1→t.val≤c.val+1→
    Residue (a.val+1) (b.val+1) (c.val+1) t.val ∨
    (∀T,recovered 34 8 8 8 (a.val+1) (b.val+1) (c.val+1) t.val
      (T.map (perm (choose (code a b c t)).2).toEmbedding)=μ (choose (code a b c t)).1 T) := by decide +kernel
'''
 else:
  s+='''def code (co : Fin 6→Fin 2) (h : Fin 5→Fin 3) : ℕ:=
  (∑j,(co j).val*2^j.val)+64*(∑j,(h j).val*3^j.val)
def pair (co : Fin 6→ℕ) (i j : Fin 4) : ℕ:=
  if i=j then 0 else if {i,j}=({0,1}:Finset (Fin 4)) then co 0 else
  if {i,j}=({0,2}:Finset (Fin 4)) then co 1 else
  if {i,j}=({0,3}:Finset (Fin 4)) then co 2 else
  if {i,j}=({1,2}:Finset (Fin 4)) then co 3 else
  if {i,j}=({1,3}:Finset (Fin 4)) then co 4 else co 5
def TriangleFree (co : Fin 6→ℕ) : Prop:=
  ∀i j k : Fin 4,i≠j→i≠k→j≠k→¬(pair co i j=1 ∧ pair co i k=1 ∧ pair co j k=1)
instance (co : Fin 6→ℕ) : Decidable (TriangleFree co) := by unfold TriangleFree;infer_instance

def Residue (co : Fin 6→ℕ) (h : Fin 5→ℕ) : Prop:=
  co≠![1,1,2,2,2,2] ∧ (co=![2,1,1,1,1,2]→h 4=1) ∧
  (co=![1,1,1,2,2,2]→h 4=0 ∨ (h 4=1 ∧ h 3=1))
instance (co : Fin 6→ℕ) (h : Fin 5→ℕ) : Decidable (Residue co h) := by unfold Residue;infer_instance

theorem coverage : ∀co : Fin 6→Fin 2,∀h : Fin 5→Fin 3,
    TriangleFree (fun j=>(co j).val+1)→
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(co j).val+1)→
    Residue (fun j=>(co j).val+1) (fun j=>(h j).val) ∨
    (∀T,recovered 34 (fun _=>8) (fun j=>(co j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code co h)).2).toEmbedding)=μ (choose (code co h)).1 T) := by decide +kernel
'''
  s=s.replace(f'import Aris4Math.ThirtyFour.{ordinary}',f'import Aris4Math.ThirtyThree.TwentyTwoQuadAssembly\nimport Aris4Math.ThirtyFour.{ordinary}',1)
 s+=f'''
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 21)) (f : Fin {n}↪Fin 21)
    (c : Case) (counts : ∀T,Aris4Math.ThirtyThree.MultiLockRecovery.count H f T=μ c T) : PropertyB H := by
  by_cases small:c.val<{len(reps)}
  · apply {ordinary}.propertyB_of_counts H f ⟨c.val,small⟩
    simpa only [μ,dif_pos small] using counts
  · apply {joint}.propertyB_of_counts H f
    simpa only [μ,dif_neg small] using counts
end Aris4Math.ThirtyFour.{name}
'''
 (ROOT/f'formal/Aris4Math/ThirtyFour/{name}.lean').write_text(s)
 print(name,len(lookup),'strict input labels',len(mus),'numeric representatives')
