import json,re,itertools
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]; HERE=Path(__file__).resolve().parent
src=ROOT/'formal/Aris4Math/ThirtyFour/TwentyThreeFiveLowPromotionData.lean'
s=src.read_text(); look={int(a):(int(b),int(c),int(d))for a,b,c,d in re.findall(r'\((\d+),\((\d+),(\d+),(\d+)\)\)',s)}
oldall=json.loads((ROOT/'context/propertyb34/round01/middle-math/FOUR_LOW_23.json').read_text())['results']
from fractions import Fraction as F
old=[{int(t):v for t,v in row['counts'].items()if v}for row in oldall if min(F(row['bound']),F(row.get('joint',row)['bound']))>=1]
def moments(ns):return tuple(sum(v**p for t,v in ns.items()if t.bit_count()==k)for k in range(5)for p in [1,2])
expected={moments(ns)for ns in old}
ns=old[7];es=[(t,v)for t,v in sorted(ns.items())if t]
cat=[]
def rec(i,used,lams,total,vs):
 if i==len(es):cat.append(vs);return
 t,k=es[i];cap=min(k,6-used,*[3-lams[j]for j in range(4)if t>>j&1],(6-total)//t.bit_count())
 for v in range(cap+1):rec(i+1,used+v,[a+v if t>>j&1 else a for j,a in enumerate(lams)],total+v*t.bit_count(),vs+[v])
rec(0,0,[0]*4,0,[])
selected={}
for vs in cat:
 out=dict(ns)
 for(t,k),v in zip(es,vs):out[t]-=v;out[t|16]=v
 p0=6-sum(vs);out[0]-=p0;out[16]=p0
 co=lambda i,j:sum(v for t,v in out.items()if t>>i&1 and t>>j&1)
 feasible=all(co(i,j)>=1 for i in range(5)for j in range(5)if i!=j)and all(sum(co(i,j)-1 for j in range(5)if i!=j)<=2 for i in range(5))
 key=7+8*sum(v*7**i for i,v in enumerate(reversed(vs)))
 if not feasible:kind='infeasible';choice=(0,0,0)
 else:
  choice=look[key];x=choice[0];proj={}
  for t,v in out.items():
   q=sum(1<<i for i,j in enumerate(j for j in range(5)if j!=x)if t>>j&1);proj[q]=proj.get(q,0)+v
  kind='residual'if moments(proj)not in expected else'survivor'
 selected[kind]=(vs,out,choice)
for kind,(vs,out,(x,c,p))in selected.items():
 val='['+','.join(map(str,vs))+']'
 body={'infeasible':f'¬ TwentyThreeLowPromotionBase.Feasible (newCounts 7 {val})','residual':f'¬ OldResidual (projected {x} (newCounts 7 {val}))','survivor':f'∀ T, newCounts 7 {val} (T.map (newPerm {p}).toEmbedding)=μ {c} T'}[kind]
 (HERE/f'RowPilot_{kind}.lean').write_text('import Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotionData\nnamespace Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion\nset_option maxHeartbeats 0\nset_option maxRecDepth 100000\nexample : '+body+' := by decide +kernel\nend Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion\n')
 print(kind,vs,(x,c,p))
(HERE/'ROW_PILOTS.json').write_text(json.dumps(selected,indent=2)+'\n')
vsrows=[]
for vs in reversed(cat):
 key=7+8*sum(v*7**i for i,v in enumerate(reversed(vs)))
 if key in look:
  vsrows.append((vs,look[key]))
  if len(vsrows)==5:break
rows='['+','.join('(['+','.join(map(str,vs))+f'],({x},{c},{p}))'for vs,(x,c,p)in vsrows)+']'
(HERE/'RowPilot_five.lean').write_text('''import Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotionData
namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def testRows : List (List ℕ × (Fin 5 × NewCase × NewPerm)) := '''+rows+'''
def testCovered (row : List ℕ × (Fin 5 × NewCase × NewPerm)) : Prop :=
  TwentyThreeLowPromotionBase.Feasible (newCounts 7 row.1) →
  OldResidual (projected row.2.1 (newCounts 7 row.1)) →
  ∀ T, newCounts 7 row.1 (T.map (newPerm row.2.2.2).toEmbedding)=μ row.2.2.1 T
noncomputable instance (r) : Decidable (testCovered r) := by unfold testCovered;infer_instance
example : testRows.all (fun row => decide (testCovered row))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion
''')
