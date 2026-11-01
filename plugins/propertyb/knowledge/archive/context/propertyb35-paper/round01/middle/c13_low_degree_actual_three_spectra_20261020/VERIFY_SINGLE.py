"""Independent inclusive-six-pair Mobius domain; every125 best fixed bound replayed on35 indexed edges. Single9,10,10,10 only."""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
st=time.process_time();d=json.loads((P/'SINGLE_QUAD_RESULT.json').read_text());assert d['status']=='COMPLETE_FIXED_MENU';pp=(3,5,6,9,10,12);cross=(5,6,9,10);tris=(7,11,13,14);keys=set()
for nine in range(4):
 ds=tuple(9 if i==nine else 10 for i in range(4))
 for vv in product(range(1,5),repeat=6):
  inc=dict(zip(pp,vv));c=sum(inc[m] for m in cross)
  if c<13:continue
  assert (c-13)//2<=1
  choices=[0,*tris] if c>=15 else [0]
  for tri in choices:
   ns=[0]*16
   if tri:ns[tri]=1
   for pair,n in inc.items():ns[pair]=n-int(bool(tri) and tri&pair==pair)
   if ns[3]<1 or ns[12]<1 or min(ns)<0 or sum(ns[m] for m in cross)<13:continue
   for i,x in enumerate(ds):ns[1<<i]=x-sum(n for m,n in inc.items() if m>>i&1)+int(bool(tri) and tri>>i&1)
   ns[0]=35-sum(ds)+sum(inc.values())-int(bool(tri))
   if min(ns)<0:continue
   assert sum(ns)==35
   keys.add(tuple(ns))
assert keys==set(map(tuple,d['labeled_keys'])) and len(keys)==932
perms=set()
for a,b,c in product((0,1),repeat=3):
 L=(1,0) if a else (0,1);R=(3,2) if b else (2,3);perms.add(R+L if c else L+R)
reps=set();sizes=Counter()
for ns in keys:
 images=[]
 for p in perms:
  out=[0]*16
  for m,n in enumerate(ns):out[sum(1<<p[i] for i in range(4) if m>>i&1)]=n
  images.append(tuple(out))
 rep=min(images);reps.add(rep);sizes[rep]+=1
assert reps==set(map(tuple,d['representative_keys'])) and len(reps)==125
outcases=[];strict=0
for z in d['cases']:
 ns=z['counts'];masks=[m for m,n in enumerate(ns) for _ in range(n)];assert len(masks)==35
 stubs=[frozenset(v+1 for v in range(4) if m>>v&1) for m in masks]
 rows=independent_rows(21,tuple(z['best']['positions']),stubs);U=sum((min(r['A'],r['B'],r['C']) for r in rows),Fraction())
 assert U==Fraction(z['best']['bound']);strict+=U<1
 outcases.append({'counts':ns,'degrees':z['degrees'],'orbit_labels':sizes[tuple(ns)],'source_support':z['source_support'],'positions':z['best']['positions'],'bound':str(U),'strict':U<1,'expanded35_masks':masks,'rows':[{k:str(v) if isinstance(v,Fraction) else v for k,v in r.items()} for r in rows]})
res={'status':'PASS_COMPLETE_DOMAIN_AND_FIXED_REPLAY_WITH_ONE_NONSTRICT','scope':__doc__,'selected_quad':[9,10,10,10],'source_support':['S1','S2','S3'],'labels':len(keys),'marked_group_order':8,'orbits':len(reps),'strict':strict,'nonstrict':[c for c in outcases if not c['strict']],'all_fixed_best_values_equal':True,'original_edge_indices':35,'ordered_distinct_pairs':1190,'rows_replayed':21*len(reps),'N':21,'locks':4,'free_vertices':17,'cpu_seconds':time.process_time()-st}
(P/'SINGLE_QUAD_VERIFY.json').write_text(json.dumps(res,indent=2)+'\n');(P/'SINGLE_QUAD_ROWS.json').write_text(json.dumps({'cases':outcases},indent=2)+'\n');print(json.dumps({k:v for k,v in res.items() if k!='nonstrict'}));print('residual orbit labels',res['nonstrict'][0]['orbit_labels'])
