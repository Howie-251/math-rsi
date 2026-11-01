"""Rebind the existing 36 mixed-degree certificates to exact high-promotion inputs.
No layout search: singleton promotions are mathematically recovered from codegrees.
"""
from pathlib import Path
from itertools import permutations
import json
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent;OUT=ROOT/'formal/Aris4Math/ThirtyFour';SRC=ROOT/'context/propertyb34/round01/middle-math'
def fs(t,n):return '{'+','.join(str(i)for i in range(n)if t>>i&1)+'}'if t else'∅'
def vec(xs):return '!['+','.join(map(str,xs))+']'
def mu(ns,n):return '(fun T => '+''.join(f'if T={fs(t,n)} then {v} else 'for t,v in sorted(ns.items())if v)+'0)'
def key(ns):return tuple(sorted((t,v)for t,v in ns.items()if v))
def image(t,p):return sum(1<<p[i]for i in range(len(p))if t>>i&1)
def write(p,s):
 if not p.exists()or p.read_text()!=s:p.write_text(s)
old={int(t):v for t,v in json.loads((SRC/'EXTEND_LOW_23_6.json').read_text())['results'][2]['counts'].items()if v}
raw=json.loads((SRC/'MIXED_LOW_23.json').read_text())['results'];targets=[]
for d in [7,8]:
 rs=[r for r in raw if r['degrees'][-1]==d];assert len(rs)==18
 targets.append([{int(t):v for t,v in r['counts'].items()if v}for r in rs])
perms=list(permutations(range(6)));lookup=[]
for ds in targets:
 l={}
 for q,row in enumerate(ds):
  for pi,p in enumerate(perms):l.setdefault(key({image(t,p+(6,)):v for t,v in row.items()}),(q,pi))
 lookup.append(l)
entries=[(t,v)for t,v in sorted(old.items())if t.bit_count()>=2];assert len(entries)==11
cats=[];records=[]
for b in range(7):
 lam=[2 if b==i else 1 for i in range(6)];cat=[]
 def rec(j,used,vals):
  if j==len(entries):cat.append(vals);return
  t,lim=entries[j];cap=min(lim,*[lam[i]-used[i]for i in range(6)if t>>i&1])
  for v in range(cap+1):rec(j+1,[c+v if t>>i&1 else c for i,c in enumerate(used)],vals+[v])
 rec(0,[0]*6,[]);cats.append(cat);recs=[]
 for values in cat:
  ps={t:v for(t,_),v in zip(entries,values)}
  for i in range(6):ps[1<<i]=lam[i]-sum(v for t,v in ps.items()if t.bit_count()>=2 and t>>i&1)
  witness=[]
  for di,d in enumerate([7,8]):
   ps[0]=d-sum(v for t,v in ps.items()if t);assert 0<=ps[0]<=old[0]
   out={}
   for t,v in old.items():out[t]=v-ps.get(t,0);out[t|64]=ps.get(t,0)
   assert min(out.values())>=0
   q,p=lookup[di][key(out)]
   # lookup image maps target coordinates to actual coordinates.
   assert all(out.get(image(t,perms[p]+(6,)),0)==targets[di][q].get(t,0)for t in range(128))
   witness.append((q,p))
  recs.append((values,witness))
 records.append(recs)
used=sorted({p for rs in records for _,ws in rs for _,p in ws});dense={p:i for i,p in enumerate(used)}
def factoradic(code):
 p=list(range(6))
 for a,b in [(0,code%6),(1,1+(code//6)%5),(2,2+(code//30)%4),(3,3+(code//120)%3),(4,4+(code//360)%2)]:
  p=[b if x==a else a if x==b else x for x in p]
 return tuple(p)
fcodes={factoradic(c):c for c in range(720)};assert len(fcodes)==720
name='TwentyThreeSixLowExtraCatalogue'
s=f'''import Aris4Math.ThirtyFour.TwentyThreeSixLowClassified
import Aris4Math.ThirtyFour.TwentyThreeSparsePromotion
import Aris4Math.ThirtyFour.TwentyFourPermutation
namespace Aris4Math.ThirtyFour.{name}
open scoped BigOperators
open LockExtension PromotionReconstruction TwentyThreeHighPromotion TwentyThreeSparsePromotion
abbrev Degree := Fin 2
abbrev NewCase := Fin 18
abbrev Pattern := Option (Fin 6)
abbrev PermIndex := Fin {len(used)}
def degree (d : Degree) : ℕ := 7+d.val
def oldCounts := TwentyThreeSixLowClassified.residualCounts 0
def μ : Degree → NewCase → Finset (Fin 7) → ℕ := {vec(vec(mu(row,7)for row in ds)for ds in targets)}
def entries : List (Finset (Fin 6) × ℕ) := [{','.join(f'({fs(t,6)},{v})'for t,v in entries)}]
def permCode : PermIndex → Fin 720 := {vec(fcodes[perms[p]]for p in used)}
def oldPerm (p : PermIndex) : Equiv.Perm (Fin 6) := TwentyFourPermutation.perm (permCode p)
noncomputable def newPerm (p : PermIndex) : Equiv.Perm (Fin 7) := LockLiftRelabel.lift (oldPerm p)
def cost (T : Finset (Fin 6)) (i : Fin 6) : ℕ := if i∈T then 1 else 0
def catalogue (b : Pattern) := BoundedAllocations.enumerate cost entries (oneDouble b)
def vector (values : List ℕ) := BoundedAllocations.decode entries values
def highSupport : Finset (Finset (Fin 6)) := (entries.map Prod.fst).toFinset
theorem highSupport_large : ∀ T∈highSupport, 2≤T.card := by decide +kernel
theorem vector_support (values : List ℕ) (T : Finset (Fin 6)) (absent : T∉highSupport) : vector values T=0 := by
  apply decode_zero_of_not_mem
  simpa only [highSupport,List.mem_toFinset] using absent
def newCounts (d : Degree) (b : Pattern) (values : List ℕ) :=
  extendSparse highSupport oldCounts (vector values) (oneDouble b) (degree d)
theorem newCounts_eq (d : Degree) (b : Pattern) (values : List ℕ) :
    newCounts d b values=extend oldCounts (complete (vector values) (oneDouble b)) (degree d) :=
  extendSparse_eq highSupport oldCounts (vector values) (oneDouble b) (degree d)
    highSupport_large (vector_support values)
abbrev Witness := NewCase × PermIndex
def Matched (d : Degree) (b : Pattern) (values : List ℕ) (w : Witness) : Prop :=
  ∀ T, newCounts d b values (T.map (newPerm w.2).toEmbedding)=μ d w.1 T
noncomputable instance (d b values w) : Decidable (Matched d b values w) := by
  unfold Matched
  infer_instance
end Aris4Math.ThirtyFour.{name}
'''
write(OUT/(name+'Data.lean'),s)
for b,recs in enumerate(records):
 bp='none'if b==6 else f'(some {b})'
 row='[\n'+',\n'.join('(['+','.join(map(str,vals))+'],'+vec(f'({q},{dense[p]})'for q,p in ws)+')'for vals,ws in recs)+'\n]'
 s=f'''import Aris4Math.ThirtyFour.{name}Data
namespace Aris4Math.ThirtyFour.{name}
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows{b} : List (List ℕ × (Degree → Witness)) := {row}
theorem catalogue_eq{b} : catalogue {bp}=rows{b}.map Prod.fst := by decide +kernel
theorem rows_checked{b} : rows{b}.all (fun r => decide (∀ d : Degree, Matched d {bp} r.1 (r.2 d)))=true := by decide +kernel
theorem coverage{b} (values : List ℕ) (mem : values∈catalogue {bp}) (d : Degree) :
    ∃ w : Witness, Matched d {bp} values w := by
  rw [catalogue_eq{b}] at mem
  obtain ⟨r,member,same⟩ := List.mem_map.mp mem
  subst values
  exact ⟨r.2 d,(of_decide_eq_true (List.all_eq_true.mp rows_checked{b} r member)) d⟩
end Aris4Math.ThirtyFour.{name}
'''
 write(OUT/(name+f'Coverage{b}.lean'),s)
s='import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage0\nimport Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage6\nnamespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue\ntheorem coverage (b : Pattern) (values : List ℕ) (mem : values∈catalogue b) (d : Degree)\n    (normalized : b=none ∨ b=some 0) : ∃ w : Witness, Matched d b values w := by\n  rcases normalized with rfl | rfl\n  · exact coverage6 values mem d\n  · exact coverage0 values mem d\nend Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue\n'
write(OUT/(name+'Numeric.lean'),s)
summary=dict(high_entries=len(entries),capacity_rows=[len(c)for c in cats],total_per_degree=sum(map(len,cats)),stored_permutations=len(used),status='source generated; coverage not Lean checked; no new layout search')
(HERE/'SIX_EXTRA_HIGH_CATALOGUE_EXPORT.json').write_text(json.dumps(summary,indent=2)+'\n');print(summary)

import runpy
runpy.run_path(str(HERE/'split_six_extra_coverage.py'),run_name='__main__')
