"""Single additional selected degreequad8^4. Exactcross13..16, internal paircap4, oldthree fixed zero-quota layouts only."""
from pathlib import Path
from itertools import product,permutations,combinations
from collections import Counter,defaultdict
from fractions import Fraction
import sys,json,time,argparse
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
st=time.process_time();ap=argparse.ArgumentParser();ap.add_argument('--all',action='store_true');arg=ap.parse_args();limit=3
specs={'local8888':[8]*4}
support=defaultdict(list)
for sid,ds in specs.items():
 assert ds==[8]*4
 for q in sorted({tuple(sorted(ds[i] for i in ix)) for ix in combinations(range(len(ds)),4)}):support[q].append(sid)
selected=[(8,8,8,8)]
menu=((8,9,20,21),(9,10,20,21),(9,20,10,21));cross=(5,6,9,10);pairs=(3,5,6,9,10,12);tris=(7,11,13,14)
group=[p for p in permutations(range(4)) if {frozenset(p[:2]),frozenset(p[2:])}=={frozenset((0,1)),frozenset((2,3))}]
maps=[tuple(sum(1<<p[i] for i in range(4) if m>>i&1) for m in range(16)) for p in group]
def image(ns,p):
 out=[0]*16
 for m,n in enumerate(ns):out[p[m]]=n
 return tuple(out)
def degree(ns):return tuple(sum(n for m,n in enumerate(ns) if m>>i&1) for i in range(4))
keys=set();byquad=Counter()
for q in selected:
 for ds in set(permutations(q)):
  for tri in (0,*tris):
   cap={m:4-int(bool(tri) and tri&m==m) for m in pairs}
   for aa in product(*(range(cap[m]+1) for m in cross)):
    if sum(aa)<13:continue
    for A,B in product(range(1,cap[3]+1),range(1,cap[12]+1)):
     ns=[0]*16;ns[3]=A;ns[12]=B
     for m,n in zip(cross,aa):ns[m]=n
     if tri:ns[tri]=1
     for i,d in enumerate(ds):ns[1<<i]=d-sum(n for m,n in enumerate(ns) if m>>i&1)
     ns[0]=35-sum(ns)
     if min(ns)<0:continue
     assert degree(ns)==ds and sum(ns)==35
     keys.add(tuple(ns));byquad[q]+=1
reps=sorted({min(image(ns,p) for p in maps) for ns in keys})
print('DOMAIN','single' if not arg.all else 'all','labels',len(keys),'reps',len(reps),'CPU',time.process_time()-st,flush=True)
results=[];partial=False
for ns in reps:
 e=SubsetEngine(21,4,{m:n for m,n in enumerate(ns) if n});e.inv={p:(0,0,[]) for p in e.inv};vals=[]
 for pos in menu:
  bp={k:1<<v for v,k in enumerate(pos)};left=0;v=0
  for k in range(1,22):pivot=bp.get(k,0);v+=e.value(k,left,pivot);left|=pivot
  vals.append({'positions':pos,'bound':str(Fraction(v,e.D)),'strict':v<e.D})
 best=min(vals,key=lambda x:Fraction(x['bound']));results.append({'counts':ns,'degrees':degree(ns),'quad':sorted(degree(ns)),'source_support':support[tuple(sorted(degree(ns)))],'exactcross':sum(ns[m] for m in cross),'triple_mass':sum(ns[m] for m in tris),'menu':vals,'best':best})
 if time.process_time()-st>limit:partial=True;break
prefix='QUAD8888'
out={'status':'CPU_PROFILE_PARTIAL' if partial else 'COMPLETE_FIXED_MENU','scope':__doc__,'source_spectra':specs,'selected_quad_count':len(selected),'all_actual_quad_count':len(support),'excluded_domains':{},'quad_support':[{'quad':q,'sources':support[q],'labels':byquad[q]} for q in selected],'labels':len(keys),'representatives':len(reps),'labeled_keys':sorted(keys),'representative_keys':reps,'cases':results,'strict_count':sum(r['best']['strict'] for r in results),'nonstrict':[r for r in results if not r['best']['strict']],'maximum_best_bound':str(max(Fraction(r['best']['bound']) for r in results)),'cpu_seconds':time.process_time()-st}
(P/(prefix+'_RESULT.json')).write_text(json.dumps(out,indent=2)+'\n');print(out['status'],'STRICT',out['strict_count'],'NONSTRICT',len(out['nonstrict']),'MAX',out['maximum_best_bound'],'CPU',out['cpu_seconds'])
