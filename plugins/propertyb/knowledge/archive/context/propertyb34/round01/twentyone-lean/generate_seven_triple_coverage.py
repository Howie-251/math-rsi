from pathlib import Path
import json
from itertools import permutations,combinations
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
vec=lambda xs:'!['+','.join(map(str,xs))+']'
for deg in [(7,7,7),(7,7,8),(7,8,8)]:
 suffix=''.join(map(str,deg));ordinary='TwentyOneSevenTriple'+suffix;name=ordinary+'Coverage'
 rows=json.load(open(HERE/(ordinary+'_REPLAY.json')));ps=[p for p in permutations(range(3)) if all(deg[j]==deg[p[j]] for j in range(3))]
 lookup={}
 for c,row in enumerate(rows):
  for pi,p in enumerate(ps):
   mu={sum(1<<p[j] for j in range(3) if t>>j&1):v for ts,v in row['counts'].items() if (t:=int(ts))>=0}
   co=[sum(v for t,v in mu.items() if t>>i&1 and t>>j&1) for i,j in combinations(range(3),2)]
   key=sum((v-1)*4**j for j,v in enumerate(co))+64*mu.get(7,0) if deg!=(7,8,8) else co[2]+9*mu.get(7,0)
   lookup.setdefault(key,(c,pi))
 s=f'''import Aris4Math.ThirtyFour.{ordinary}
namespace Aris4Math.ThirtyFour.{name}
open Aris4Math.ThirtyThree.TripleProfiles
set_option maxRecDepth 100000
set_option maxHeartbeats 0
abbrev Case:=Fin {len(rows)}
abbrev Perm:=Fin {len(ps)}
def permFn : Perm→Fin 3→Fin 3:={vec(vec(p) for p in ps)}
theorem permFn_injective : ∀p,Function.Injective (permFn p) := by decide +kernel
noncomputable def perm (p : Perm) : Equiv.Perm (Fin 3):=
  Equiv.ofBijective (permFn p) ⟨permFn_injective p,Finite.surjective_of_injective (permFn_injective p)⟩
def choose : ℕ→Case×Perm
'''
 for k,(c,p) in sorted(lookup.items()):s+=f'  | {k} => ({c},{p})\n'
 s+='  | _ => (0,0)\n'
 if deg!=(7,8,8):
  s+=f'''def code (a b c : Fin 4) (t : Fin 5) : ℕ:=a.val+4*b.val+16*c.val+64*t.val

theorem coverage : ∀a b c : Fin 4,∀t : Fin 5,
    t.val≤a.val+1→t.val≤b.val+1→t.val≤c.val+1→
    a.val+1+(b.val+1)≤7+t.val→a.val+1+(c.val+1)≤7+t.val→
    b.val+1+(c.val+1)≤{deg[2]}+t.val→
    (a.val+1≤2 ∧ b.val+1≤2 ∧ c.val+1≤2) ∨
    (∀T,recovered 34 {deg[0]} {deg[1]} {deg[2]} (a.val+1) (b.val+1) (c.val+1) t.val
      (T.map (perm (choose (code a b c t)).2).toEmbedding)={ordinary}Data.μ (choose (code a b c t)).1 T) := by decide +kernel
'''
 else:
  s+=f'''def code (c : Fin 9) (t : Fin 2) : ℕ:=c.val+9*t.val

theorem coverage : ∀c : Fin 9,∀t : Fin 2,t.val≤c.val→1+c.val≤8+t.val→
    c.val≤2 ∨
    (∀T,recovered 34 7 8 8 1 1 c.val t.val
      (T.map (perm (choose (code c t)).2).toEmbedding)={ordinary}Data.μ (choose (code c t)).1 T) := by decide +kernel
'''
 s+=f'end Aris4Math.ThirtyFour.{name}\n'
 (ROOT/f'formal/Aris4Math/ThirtyFour/{name}.lean').write_text(s)
 print(name,len(lookup))
