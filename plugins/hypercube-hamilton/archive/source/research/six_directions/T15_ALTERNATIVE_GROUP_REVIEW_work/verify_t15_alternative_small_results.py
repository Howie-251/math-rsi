import json,itertools,hashlib
from pathlib import Path
R=Path('.')
B=json.loads((R/'t15_alternative_B_independent.json').read_text())
geo=json.loads((R/'t15_analytic_geometry.json').read_text())['T15']['residual_orbits'];out=[]
for k,cut,x,r,s,y in [(18,2,3,6,12,1),(21,2,3,10,12,1),(25,1,9,3,6,8)]:
 for c in (1,3):
  a=json.loads((R/f't15_alternative_core{k}_c{c}.json').read_text());b=next(t for t in B if t['core']==k and t['c']==c)
  assert a['B_types']==b['B_types'] and b['total']==(135135 if c==1 else 1621620)
  if c==3:assert all((int(m)&7).bit_count()>=2 or (int(m)>>3).bit_count()>=2 for m in b['B_types'])
  else:
   lines=[]
   for line in (R/f't15_alternative_core{k}_c1_B_exceptions.txt').read_text().splitlines():
    t=line.split();j=t.index('F');lines.append(tuple(map(int,t[1:j]+t[j+1:])))
   req=[tuple(map(int,z.split())) for z in (R/f't15_alternative_core{k}_c1_B_inputs.txt').read_text().splitlines()]
   assert set(lines)==set(req) and len(lines)==len(req)==b['B_types']['0']
 g=geo[k];holes={0,*g['avoided'],*g['included']}
 drop=lambda v:(v&((1<<cut)-1))|((v>>(cut+1))<<cut)
 found=[]
 for p in itertools.permutations(range(4)):
  tr=lambda v:sum(((v>>j)&1)<<p[j] for j in range(4))
  A={tr(drop(v)) for v in holes if v>>cut&1};BB={tr(drop(v)) for v in holes if not(v>>cut&1)}
  if A=={x,r,s} and BB=={0,7,y} and {tr(drop(v)) for v in g['avoided'] if v>>cut&1}=={x} and {tr(drop(v)) for v in g['avoided'] if not(v>>cut&1)}=={y}:found.append(p)
 assert found
 out.append({'core':k,'global_geometry':g,'cut':cut,'local_bit_permutation':found[0],'A_holes':[x,r,s],'B_holes':[0,7,y],'c3_B_complete':True,'c1_B_exceptions':len(req)})
(R/'t15_alternative_small_verification.json').write_text(json.dumps({'status':'PASS','rows':out},indent=2))
print(json.dumps(out))
