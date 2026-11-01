"""Independent inclusive-pair/Mobius full remaining-quad domain and all1073 original35-index zero-quota fixed certificate replays."""
from pathlib import Path
from itertools import product
from collections import Counter,defaultdict
from fractions import Fraction
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'));from independent_structure_bounds import independent_rows
st=time.process_time();d=json.loads((P/'ALL_RESULT.json').read_text());assert d['status']=='COMPLETE_FIXED_MENU';pp=(3,5,6,9,10,12);cross=(5,6,9,10);tris=(7,11,13,14)
# Independent actual degree-multiplicity inclusion, no21choose4 procedure reused.
source={'S1':{7:8,8:1,9:9,10:3},'S2':{7:9,9:8,10:4},'S3':{7:7,8:3,9:8,10:3}}
support=defaultdict(list);ordered=[]
for ds in product(range(7,11),repeat=4):
 q=tuple(sorted(ds));need=Counter(ds);ids=[sid for sid,counts in source.items() if all(n<=counts.get(v,0) for v,n in need.items())]
 if not ids or q in ((9,10,10,10),(10,10,10,10)):continue
 ordered.append(ds)
 if q not in support:support[q]=ids
assert set(support)=={tuple(z['quad']) for z in d['quad_support']}
assert all(support[tuple(z['quad'])]==z['sources'] for z in d['quad_support'])
keys=set()
for cv in product(range(1,5),repeat=4):
 crosssum=sum(cv)
 if crosssum<13:continue
 choices=[0,*tris] if crosssum>=15 else [0]
 for A,B in product(range(1,5),repeat=2):
  inc={3:A,12:B,**dict(zip(cross,cv))}
  for tri in choices:
   base=[0]*16
   if tri:base[tri]=1
   for pair,n in inc.items():base[pair]=n-int(bool(tri) and tri&pair==pair)
   if min(base)<0 or base[3]<1 or base[12]<1 or sum(base[m] for m in cross)<13:continue
   for ds in ordered:
    ns=base.copy()
    for i,v in enumerate(ds):ns[1<<i]=v-sum(n for m,n in inc.items() if m>>i&1)+int(bool(tri) and tri>>i&1)
    ns[0]=35-sum(ds)+sum(inc.values())-int(bool(tri))
    if min(ns)<0:continue
    assert sum(ns)==35;keys.add(tuple(ns))
assert keys==set(map(tuple,d['labeled_keys'])) and len(keys)==7977
perms=set()
for a,b,c in product((0,1),repeat=3):
 L=(1,0) if a else (0,1);R=(3,2) if b else (2,3);perms.add(R+L if c else L+R)
reps=set()
for ns in keys:
 images=[]
 for p in perms:
  out=[0]*16
  for m,n in enumerate(ns):out[sum(1<<p[i] for i in range(4) if m>>i&1)]=n
  images.append(tuple(out))
 reps.add(min(images))
assert reps==set(map(tuple,d['representative_keys']))=={tuple(z['counts']) for z in d['cases']} and len(reps)==1073
rowsout=[];values=[];byquad=defaultdict(list)
for z in d['cases']:
 ns=z['counts'];masks=[m for m,n in enumerate(ns) for _ in range(n)];assert len(masks)==35
 stubs=[frozenset(v+1 for v in range(4) if m>>v&1) for m in masks];rr=independent_rows(21,tuple(z['best']['positions']),stubs);value=sum((min(r['A'],r['B'],r['C']) for r in rr),Fraction());assert value==Fraction(z['best']['bound'])<1
 values.append(value);byquad[tuple(z['quad'])].append(value)
 rowsout.append({'quad':z['quad'],'degrees':z['degrees'],'source_support':z['source_support'],'counts':ns,'expanded35_masks':masks,'positions':z['best']['positions'],'bound':str(value),'quota':0,'rows':[{k:str(v) if isinstance(v,Fraction) else v for k,v in r.items()} for r in rr]})
 assert time.process_time()-st<18
(P/'VERIFY_ROWS.json').write_text(json.dumps({'cases':rowsout},indent=2)+'\n')
out={'status':'PASS_COMPLETE_REMAINING_ACTUAL_QUAD_DOMAIN_AND_ALL1073_STRICT_CERTIFICATES','scope':__doc__,'actual_selected_quads_total':d['all_actual_quad_count'],'quads_checked':len(support),'ordered_degrees_checked':len(ordered),'excluded_9_10pow3_and10pow4_not_recomputed':True,'labels':len(keys),'true_marked_group_order':8,'orbits':len(reps),'strict':len(values),'maximum_bound':str(max(values)),'nonstrict':[],'per_quad':[{'quad':q,'source_support':support[q],'labels':sum(tuple(sorted(sum(n for m,n in enumerate(ns) if m>>i&1) for i in range(4)))==q for ns in keys),'orbits':len(vs),'maximum_bound':str(max(vs))} for q,vs in sorted(byquad.items())],'N':21,'locks':4,'free_vertices':17,'original_edge_indices':35,'ordered_distinct_pairs':1190,'rows':21*len(values),'cpu_seconds':time.process_time()-st}
(P/'VERIFY_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='per_quad'}))
