from pathlib import Path
from itertools import combinations,permutations
import json
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/'formal/Aris4Math/ThirtyFour'
rows=[]
for b,bad in enumerate(['3','3_12','3_12_48']):
 new=json.loads((ROOT/f'context/propertyb34-hour1-20261013/high-math/MIXED_SIX_v24_low6_bad{bad}.json').read_text())['results']
 for r in new:r['extra']=b
 rows.extend(new)
vec=lambda a:'!['+','.join(map(str,a))+']'
fs=lambda t:'{'+','.join(str(j) for j in range(6) if t>>j&1)+'}' if t else '∅'
hi=[t for t in range(64) if 3<=t.bit_count()<=5]
pairs=[sum(1<<i for i in p) for p in combinations(range(6),2)]
transform=lambda t,p:sum(1<<p[j] for j in range(6) if t>>j&1)
def factoradic_perm(code):
 p=list(range(6))
 for a,b in [(0,code%6),(1,1+(code//6)%5),(2,2+(code//30)%4),(3,3+(code//120)%3),(4,4+(code//360)%2)]:
  p=[b if x==a else a if x==b else x for x in p]
 return tuple(p)
ps=[factoradic_perm(code) for code in range(720)]
assert len(set(ps))==720
lookup=[{},{},{}]
for i,r in enumerate(rows):
 ns={int(t):n for t,n in r['counts'].items() if n}; b=r['extra']
 for pi,p in enumerate(ps):
  bads=[3,12,48][:b+1]
  if {transform(t,p) for t in bads}!=set(bads):continue
  image={transform(t,p):v for t,v in ns.items()}
  code=sum(image.get(t,0)*(2**k) for k,t in enumerate(hi))
  lookup[b].setdefault(code,(i,pi))
assert list(map(len,lookup))==[467,611,787],list(map(len,lookup))
s='''import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.ActualAllocations
import Aris4Math.ThirtyFour.LockRelabel
import Aris4Math.ThirtyFour.TwentyFourPermutation
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open TwentyFourSixLowBadData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
'''
s+='def entries : List (Finset (Fin 6)×ℕ) := ['+','.join(f'({fs(t)},1)' for t in hi)+']\n'
s+='def pair : Fin 15→Finset (Fin 6) := '+vec(fs(t) for t in pairs)+'\n'
s+='''abbrev Pattern := Fin 3
def cap (b : Pattern) (j : Fin 15) : ℕ := if pair j={0,1} ∨ (1≤b.val ∧ pair j={2,3}) ∨ (2≤b.val ∧ pair j={4,5}) then 2 else 1
def catalogue (b : Pattern) := BoundedAllocations.enumerate (fun T j=>ActualAllocations.cost (pair j) T) entries (cap b)
def vector (values : List ℕ) := BoundedAllocations.decode entries values
def low (b : Pattern) (T : Finset (Fin 6)) : ℕ :=
  if T=∅ then 34 else if T.card=1 then 6 else if T={0,1} ∨ (1≤b.val ∧ T={2,3}) ∨ (2≤b.val ∧ T={4,5}) then 2 else 1
abbrev Perm := Fin 720
'''
s+='''abbrev perm := TwentyFourPermutation.perm
def choices : Pattern→List (ℕ×(Case×Perm))
'''
for b,name in [(0,'0'),(1,'1'),(2,'2')]:
 s+='  | '+name+' => ['+','.join(f'({key},({i},{p}))' for key,(i,p) in sorted(lookup[b].items()))+']\n'
s+='''def code (values : List ℕ) := (values.zipIdx.map (fun p=>p.1*2^p.2)).sum
def choose (b : Pattern) (values : List ℕ) : Case×Perm :=
  ((choices b).lookup (code values)).getD (0,0)
def Matched (b : Pattern) (values : List ℕ) : Prop :=
  (∀ T,T.card≤2→low b (T.map (perm (choose b values).2).toEmbedding)=upper (choose b values).1 T) ∧
  (∀ T,3≤T.card→vector values (T.map (perm (choose b values).2).toEmbedding)=μ (choose b values).1 T)
instance (b : Pattern) (values : List ℕ) : Decidable (Matched b values) := by unfold Matched;infer_instance
end Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage
'''
(OUT/'TwentyFourSixLowBadCoverageData.lean').write_text(s)
(OUT/'TwentyFourSixLowBadCoverageKernel.lean').write_text('''import Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverageData
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem coverage_zero : ∀values∈catalogue 0,Matched 0 values := by decide +kernel
theorem coverage_one : ∀values∈catalogue 1,Matched 1 values := by decide +kernel
theorem coverage_two : ∀values∈catalogue 2,Matched 2 values := by decide +kernel
theorem coverage (b : Pattern) (values : List ℕ) (member : values∈catalogue b) : Matched b values := by
  fin_cases b
  · exact coverage_zero values member
  · exact coverage_one values member
  · exact coverage_two values member
end Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage
''')
print('Complete lookup domains',list(map(len,lookup)))
