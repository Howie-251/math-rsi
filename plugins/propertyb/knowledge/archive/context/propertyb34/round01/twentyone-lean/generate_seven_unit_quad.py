from pathlib import Path
from itertools import permutations,combinations
import json
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
vec=lambda xs:'!['+','.join(map(str,xs))+']'
ordinary='TwentyOneSevenQuad7888';name='TwentyOneSevenUnitQuadCoverage';rows=json.load(open(HERE/(ordinary+'_REPLAY.json')))
ps=[(0,)+p for p in permutations((1,2,3))];lookup={}
for c,row in enumerate(rows):
 for pi,p in enumerate(ps):
  mu={sum(1<<p[j] for j in range(4) if t>>j&1):v for ts,v in row['counts'].items() if (t:=int(ts))>=0}
  co=[sum(v for t,v in mu.items() if t>>i&1 and t>>j&1) for i,j in [(1,2),(1,3),(2,3)]]
  key=sum((v-1)*2**j for j,v in enumerate(co))+8*sum(mu.get(t,0)*3**j for j,t in enumerate([7,11,13,14,15]))
  lookup.setdefault(key,(c,pi))
s=f'''import Aris4Math.ThirtyFour.{ordinary}
import Aris4Math.ThirtyThree.TwentyTwoQuadAssembly
namespace Aris4Math.ThirtyFour.{name}
open scoped BigOperators
open Aris4Math.ThirtyThree.QuadProfiles
set_option maxRecDepth 100000
set_option maxHeartbeats 0
abbrev Case:=Fin {len(rows)}
abbrev Perm:=Fin {len(ps)}
def permFn : Perm→Fin 4→Fin 4:={vec(vec(p) for p in ps)}
theorem permFn_injective : ∀p,Function.Injective (permFn p) := by decide +kernel
noncomputable def perm (p : Perm) : Equiv.Perm (Fin 4):=
  Equiv.ofBijective (permFn p) ⟨permFn_injective p,Finite.surjective_of_injective (permFn_injective p)⟩
def choose : ℕ→Case×Perm
'''
for k,(c,p) in sorted(lookup.items()):s+=f'  | {k} => ({c},{p})\n'
s+='  | _ => (0,0)\n'
s+=f'''def co (a b c : ℕ) : Fin 6→ℕ:=![1,1,1,a,b,c]
def code (a b c : Fin 2) (h : Fin 5→Fin 3) : ℕ:=a.val+2*b.val+4*c.val+8*(∑j,(h j).val*3^j.val)

theorem coverage : ∀a b c : Fin 2,∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤co (a.val+1) (b.val+1) (c.val+1) j)→
    (a.val+1=2 ∧ b.val+1=2 ∧ c.val+1=2 ∧ (h 4).val=0) ∨
    (∀T,recovered 34 ![7,8,8,8] (co (a.val+1) (b.val+1) (c.val+1)) (fun j=>(h j).val)
      (T.map (perm (choose (code a b c h)).2).toEmbedding)={ordinary}Data.μ (choose (code a b c h)).1 T) := by decide +kernel
end Aris4Math.ThirtyFour.{name}
'''
(ROOT/f'formal/Aris4Math/ThirtyFour/{name}.lean').write_text(s)
print(name,len(lookup))
