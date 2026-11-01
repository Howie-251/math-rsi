from pathlib import Path
from itertools import combinations
from collections import Counter
from fractions import Fraction
import json,time
P=Path(__file__).resolve().parent;R=P.parents[4];start=time.process_time()
old=R/'context/propertyb35-paper/round01/twentyone-high'
pairs=json.loads((old/'DOUBLES.json').read_text())['cases'];triples=json.loads((old/'TRIPLES.json').read_text())['cases']
lookup={(tuple(z['degrees']),z['codegree']):z for z in pairs}
def parts(n,lo=1):
 if not n:yield ();return
 for a in range(lo,n+1):
  for t in parts(n-a,a):yield (a,)+t
rows=[]
for increments in parts(28):
 if len(increments)>20:continue
 ds=[7]*(21-len(increments))+[7+x for x in increments]
 e=sum(max(x-9,0) for x in ds);a=ds.count(7);b=ds.count(8)
 assert 2*a+b==14+e and len(ds)==21 and sum(ds)==175
 # Real pair codegrees range max(1,u+v-35)..min(u,v).
 guaranteed=[]
 for u,v in sorted(set(combinations(ds,2))):
  cs=range(max(1,u+v-35),min(u,v)+1)
  if all((z:=lookup.get(((u,v),c))) and z['strict'] for c in cs):guaranteed.append([u,v])
 rows.append({'degrees':ds,'a7':a,'a8':b,'e':e,'Delta':max(ds),'whole_degree_pair_gate':guaranteed})
assert len({tuple(z['degrees']) for z in rows})==len(rows)
tr777=[z for z in triples if z['degrees']==[7,7,7]]
# Equal degree triple sorted pair labels is complete up to S3; includes every triple containing codegree3.
expected={(ps,t) for ps in [(1,1,3),(1,2,3),(1,3,3),(2,2,3),(2,3,3),(3,3,3)] for t in range(min(ps)+1)}
actual={(tuple(z['codegrees']),z['triple']) for z in tr777 if 3 in z['codegrees']}
assert expected==actual and all(z['strict'] for z in tr777 if 3 in z['codegrees'])
seven=[]
for D in range(7,36):
 cs=list(range(max(1,D+7-35),8));assert all(((7,D),c) in lookup for c in cs)
 seven.append({'other_degree':D,'strict_codegrees':[c for c in cs if lookup[((7,D),c)]['strict']], 'not_excluded_codegrees':[c for c in cs if not lookup[((7,D),c)]['strict']]})
hi=[r for r in rows if r['e']>4];remaining=[r for r in hi if not r['whole_degree_pair_gate']]
res={'status':'COMPLETE_INTEGER_DEGREE_SCOPE_ONLY','scope':'21 vertices min exactly7 sum175; all integer degree multisets, no H realization or moment sweep. Existing pair/triple certificate projection only.','total_spectra':len(rows),'e_le4':sum(r['e']<=4 for r in rows),'e_gt4':len(hi),'e_range':[min(r['e'] for r in rows),max(r['e'] for r in rows)],'Delta_range':[min(r['Delta'] for r in rows),max(r['Delta'] for r in rows)],'e_histogram':dict(Counter(r['e'] for r in rows)),'high_e_guaranteed_old_pair_gate':len(hi)-len(remaining),'high_e_after_unconditional_pair_gates':len(remaining),'remaining_e_range':[min(r['e'] for r in remaining),max(r['e'] for r in remaining)],'remaining_Delta_range':[min(r['Delta'] for r in remaining),max(r['Delta'] for r in remaining)],'seven_pair_gates':seven,'seven_triples_containing_codegree3_complete_strict':len(actual),'all_spectra':rows,'cpu_seconds':time.process_time()-start}
assert res['e_le4']==99 and all(r['Delta']<=18 for r in remaining)
assert res['cpu_seconds']<2
(P/'RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print({k:v for k,v in res.items() if k not in ['all_spectra','seven_pair_gates']})
print('highest e remaining',max(remaining,key=lambda r:r['e']))
print('smallest e>4 remaining',next(r for r in remaining if r['e']==5))
