from pathlib import Path
from itertools import permutations,combinations
import json
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
vec=lambda xs:'!['+','.join(map(str,xs))+']'
ordinary='TwentyOneSevenQuad7777';name='TwentyOneSevenQuadCoverage'
rows=json.load(open(HERE/(ordinary+'_REPLAY.json')))
ids=[0,1,3,4,18,19,20,21,32]
raw=json.load(open(ROOT/'context/propertyb34/round01/twentyone-math/MANY_SEVENS_JOINT.json'))['results']
res=json.load(open(ROOT/'context/propertyb34/round01/twentyone-math/FOUR_SEVENS_RESIDUES.json'))['representatives']
allrows=rows+[raw[i] for i in ids]+res
ps=list(permutations(range(4)));lookup={}
for c,row in enumerate(allrows):
 for pi,p in enumerate(ps):
  mu={sum(1<<p[j] for j in range(4) if t>>j&1):v for ts,v in row['counts'].items() if (t:=int(ts))>=0}
  co=[sum(v for t,v in mu.items() if t>>i&1 and t>>j&1) for i,j in combinations(range(4),2)]
  key=sum((v-1)*2**j for j,v in enumerate(co))+64*sum(mu.get(t,0)*3**j for j,t in enumerate([7,11,13,14,15]))
  lookup.setdefault(key,(c,pi))
assert len(lookup)==674,len(lookup)
fs=lambda t:'{'+','.join(str(i) for i in range(4) if t>>i&1)+'}' if t else '∅'
strict=len(rows)+len(ids)
s=f'import Aris4Math.ThirtyFour.{ordinary}\n'
for i in ids:s+=f'import Aris4Math.ThirtyFour.TwentyOneSevenJointQuad{i}\n'
s+=f'''import Aris4Math.ThirtyThree.TwentyTwoQuadAssembly
namespace Aris4Math.ThirtyFour.{name}
open scoped BigOperators
open Aris4Math.ThirtyThree.QuadProfiles
set_option maxRecDepth 100000
set_option maxHeartbeats 0
abbrev Case:=Fin {len(allrows)}
abbrev Residue:=Fin {len(res)}
abbrev Perm:=Fin {len(ps)}
def permFn : Perm→Fin 4→Fin 4:={vec(vec(p) for p in ps)}
theorem permFn_injective : ∀p,Function.Injective (permFn p) := by decide +kernel
noncomputable def perm (p : Perm) : Equiv.Perm (Fin 4):=
  Equiv.ofBijective (permFn p) ⟨permFn_injective p,Finite.surjective_of_injective (permFn_injective p)⟩
def residueμ : Residue → Finset (Fin 4) → ℕ := '''+vec('fun T => '+''.join(f'if T={fs(int(t))} then {k} else ' for t,k in sorted(row['counts'].items(),key=lambda a:int(a[0])) if k)+'0' for row in res)+'\n'
s+=f'def μ (c : Case) (T : Finset (Fin 4)) : ℕ:=\n  if h:c.val<{len(rows)} then {ordinary}Data.μ ⟨c.val,h⟩ T\n'
for k,i in enumerate(ids):s+=f'  else if c.val={len(rows)+k} then TwentyOneSevenJointQuad{i}Data.μ T\n'
s+=f'  else residueμ ⟨c.val-{strict},by omega⟩ T\n'
s+='def choices : List (ℕ×(Case×Perm)):= ['+','.join(f'({k},({c},{p}))' for k,(c,p) in sorted(lookup.items()) if (c,p)!=(0,0))+']\n'
s+='def choose (k : ℕ) : Case×Perm:=(choices.lookup k).getD (0,0)\n'
s+=f'''def code (co : Fin 6→Fin 2) (h : Fin 5→Fin 3) : ℕ:=
  (∑j,(co j).val*2^j.val)+64*(∑j,(h j).val*3^j.val)

theorem coverage : ∀co : Fin 6→Fin 2,∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(co j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(co j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code co h)).2).toEmbedding)=μ (choose (code co h)).1 T) := by decide +kernel

theorem residue_readback (c : Case) (h : {strict}≤c.val) (T : Finset (Fin 4)) :
    μ c T=residueμ ⟨c.val-{strict},by omega⟩ T := by
  have low : ¬ c.val<{len(rows)} := by omega
  simp only [μ,dif_neg low]
  split_ifs <;> omega

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 21)) (f : Fin 4↪Fin 21)
    (c : Case) (strict : c.val<{strict})
    (counts : ∀T,Aris4Math.ThirtyThree.MultiLockRecovery.count H f T=μ c T) : PropertyB H := by
  by_cases small:c.val<{len(rows)}
  · apply {ordinary}.propertyB_of_counts H f ⟨c.val,small⟩
    simpa only [μ,dif_pos small] using counts
  · have lower : {len(rows)}≤c.val := by omega
    have bound : c.val<{len(allrows)}:=c.isLt
    interval_cases v:c.val
'''
for i in ids:
 s+=f'    · apply TwentyOneSevenJointQuad{i}.propertyB_of_counts H f\n      simpa [μ,v] using counts\n'
s+=f'end Aris4Math.ThirtyFour.{name}\n'
(ROOT/f'formal/Aris4Math/ThirtyFour/{name}.lean').write_text(s)
print(name,len(lookup),'profiles',len(allrows),'representatives',strict,'strict')
