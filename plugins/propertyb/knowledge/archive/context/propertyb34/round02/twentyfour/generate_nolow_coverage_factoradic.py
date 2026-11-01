from pathlib import Path
from itertools import combinations,permutations
import json
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/'formal/Aris4Math/ThirtyFour'
rows=json.loads((ROOT/'context/propertyb34-hour1-20261013/high-math/V24_NO_SIX_CERTIFICATES.json').read_text())['results']
vec=lambda a:'!['+','.join(map(str,a))+']'
fs=lambda t:'{'+','.join(str(j) for j in range(6) if t>>j&1)+'}' if t else '∅'
hi=[t for t in range(64) if 3<=t.bit_count()<=5]
pairs=[sum(1<<i for i in p) for p in combinations(range(6),2)]
def factoradic_perm(code):
 p=list(range(6))
 for a,b in [(0,code%6),(1,1+(code//6)%5),(2,2+(code//30)%4),(3,3+(code//120)%3),(4,4+(code//360)%2)]:
  p=[b if x==a else a if x==b else x for x in p]
 return tuple(p)
ps=[factoradic_perm(code) for code in range(720)]
assert len(set(ps))==720
transform=lambda t,p:sum(1<<p[j] for j in range(6) if t>>j&1)
lookup=[{},{}]
for i,r in enumerate(rows):
 ns={int(t):n for t,n in r['counts'].items() if n}; b=r['extra']
 for pi,p in enumerate(ps):
  if b and transform(3,p)!=3:continue
  image={transform(t,p):v for t,v in ns.items()}
  code=sum(image.get(t,0)*(2**k) for k,t in enumerate(hi))
  lookup[b].setdefault(code,(i,pi))
assert list(map(len,lookup))==[352,467],list(map(len,lookup))
s='''import Aris4Math.ThirtyFour.TwentyFourNoLowSix
import Aris4Math.ThirtyFour.ActualAllocations
import Aris4Math.ThirtyFour.LockRelabel
import Aris4Math.ThirtyFour.TwentyFourPermutation
namespace Aris4Math.ThirtyFour.TwentyFourNoLowCoverage
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open TwentyFourNoLowSixData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
'''
s+='def entries : List (Finset (Fin 6)×ℕ) := ['+','.join(f'({fs(t)},1)' for t in hi)+']\n'
s+='def pair : Fin 15→Finset (Fin 6) := '+vec(fs(t) for t in pairs)+'\n'
s+='''def cap (b : Bool) (j : Fin 15) : ℕ := if b && j==0 then 2 else 1
def catalogue (b : Bool) := BoundedAllocations.enumerate (fun T j=>ActualAllocations.cost (pair j) T) entries (cap b)
def vector (values : List ℕ) := BoundedAllocations.decode entries values
def low (b : Bool) (T : Finset (Fin 6)) : ℕ :=
  if T=∅ then 34 else if T.card=1 then 7 else if b && T=={0,1} then 2 else 1
abbrev Perm := Fin 720
'''
s+='''abbrev perm := TwentyFourPermutation.perm
def choices : Bool→List (ℕ×(Case×Perm))
'''
for b,name in [(0,'false'),(1,'true')]:
 s+='  | '+name+' => ['+','.join(f'({key},({i},{p}))' for key,(i,p) in sorted(lookup[b].items()))+']\n'
s+='''def code (values : List ℕ) := (values.zipIdx.map (fun p=>p.1*2^p.2)).sum
def choose (b : Bool) (values : List ℕ) : Case×Perm :=
  ((choices b).lookup (code values)).getD (0,0)
def Matched (b : Bool) (values : List ℕ) : Prop :=
  (∀ T,T.card≤2→low b (T.map (perm (choose b values).2).toEmbedding)=upper (choose b values).1 T) ∧
  (∀ T,3≤T.card→vector values (T.map (perm (choose b values).2).toEmbedding)=μ (choose b values).1 T)
instance (b : Bool) (values : List ℕ) : Decidable (Matched b values) := by unfold Matched;infer_instance
end Aris4Math.ThirtyFour.TwentyFourNoLowCoverage
'''
(OUT/'TwentyFourNoLowCoverageData.lean').write_text(s)
(OUT/'TwentyFourNoLowCoverageKernel.lean').write_text('''import Aris4Math.ThirtyFour.TwentyFourNoLowCoverageData
namespace Aris4Math.ThirtyFour.TwentyFourNoLowCoverage
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem coverage_false : ∀values∈catalogue false,Matched false values := by decide +kernel
theorem coverage_true : ∀values∈catalogue true,Matched true values := by decide +kernel
theorem coverage (b : Bool) (values : List ℕ) (member : values∈catalogue b) : Matched b values := by
  cases b
  · exact coverage_false values member
  · exact coverage_true values member
end Aris4Math.ThirtyFour.TwentyFourNoLowCoverage
''')
print('Complete lookup domains',list(map(len,lookup)))
