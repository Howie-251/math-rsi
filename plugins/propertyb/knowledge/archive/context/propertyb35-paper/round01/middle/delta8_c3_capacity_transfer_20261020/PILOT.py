"""Only quad-degree multisets from the actual15 delta8 degree spectra; migrate missing c>=14 gate using fixed old3-layout menu. No new layout solve."""
from pathlib import Path
from itertools import combinations,permutations,product
from collections import Counter,defaultdict
from fractions import Fraction
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
st=time.process_time();spectra=json.loads((P.parent/'min_degree_eight_singleton_star_20261020/CONDITIONAL_SCALAR_RESULT.json').read_text())['jobs']
support=defaultdict(list)
for j in spectra:
 for q in sorted({tuple(sorted(j['degrees'][i] for i in ids)) for ids in combinations(range(21),4)}):
  support[q].append(j['spectrum_id'])
new={q for q in support if max(q)>13 or sum(max(x-9,0) for x in q)>4}
assert new=={(8,8,10,13),(8,8,11,12),(8,8,8,14),(8,8,9,14),(8,8,8,15)}
ordered=sorted({p for q in new for p in permutations(q)})
group=[p for p in permutations(range(4)) if {frozenset(p[:2]),frozenset(p[2:])}=={frozenset((0,1)),frozenset((2,3))}]
maps=[tuple(sum(1<<p[i] for i in range(4) if m>>i&1) for m in range(16)) for p in group]
def image(ns,p):
 out=[0]*16
 for m,n in enumerate(ns):out[p[m]]=n
 return tuple(out)
def degree(ns):return tuple(sum(n for m,n in enumerate(ns) if m>>i&1) for i in range(4))
keys=set();by_t=Counter();shapes=Counter();cross=(5,6,9,10);tris=(7,11,13,14)
for t in (14,15,16):
 for aa in product(range(5),repeat=4):
  if sum(aa)!=t:continue
  for tri in (0,*tris):
   if t+2*int(bool(tri))>16:continue
   if any(a+int(bool(tri) and tri&m==m)>4 for a,m in zip(aa,cross)):continue
   for A,B in product(range(1,5),repeat=2):
    if A+int(bool(tri) and tri&3==3)>4 or B+int(bool(tri) and tri&12==12)>4:continue
    base=[0]*16;base[3]=A;base[12]=B
    for m,n in zip(cross,aa):base[m]=n
    if tri:base[tri]=1
    dd=degree(base);shapes[t]+=1
    for ds in ordered:
     ss=[d-x for d,x in zip(ds,dd)]
     if min(ss)<0:continue
     ns=base.copy()
     for i,n in enumerate(ss):ns[1<<i]=n
     ns[0]=35-sum(ns)
     if ns[0]<0:continue
     assert degree(ns)==ds and all(sum(n for m,n in enumerate(ns) if m&pair==pair)<=4 for pair in (3,5,6,9,10,12))
     keys.add(tuple(ns))
reps=sorted({min(image(ns,p) for p in maps) for ns in keys})
menu=sorted({tuple(c['positions']) for c in json.loads((P.parent/'generic_c3_fourteen_gate_20261020/RESULT.json').read_text())['cases']});assert len(menu)==3
profile={'all_selected_multisets':len(support),'imported_multisets':len(support)-len(new),'new_multisets':len(new),'new_ordered_degrees':len(ordered),'labels':len(keys),'orbits':len(reps),'labels_by_t':dict(Counter(sum(ns[m] for m in cross) for ns in keys)),'generation_cpu':time.process_time()-st}
(P/'DOMAIN.json').write_text(json.dumps({'profile':profile,'new_degree_support':[{'quad_degrees':q,'spectrum_ids':support[q]} for q in sorted(new)],'imported_degree_support':[{'quad_degrees':q,'spectrum_ids':support[q]} for q in sorted(set(support)-new)],'menu':menu,'labeled_keys':sorted(keys),'representative_keys':reps},indent=2)+'\n');print('DOMAIN',profile,flush=True)
results=[]
for ns in reps:
 e=SubsetEngine(21,4,{m:n for m,n in enumerate(ns) if n});e.inv={p:(0,0,[]) for p in e.inv};vals=[]
 for pos in menu:
  bypos={k:1<<v for v,k in enumerate(pos)};left=0;value=0
  for k in range(1,22):
   p=bypos.get(k,0);term=e.value(k,left,p);assert term is not None;value+=term;left|=p
  vals.append({'positions':pos,'bound':str(Fraction(value,e.D)),'strict':value<e.D})
 best=min(vals,key=lambda z:Fraction(z['bound']));results.append({'counts':ns,'degrees':degree(ns),'t':sum(ns[m] for m in cross),'zero_quota':True,'menu':vals,'best':best})
 if time.process_time()-st>18:break
out={'status':'COMPLETE_FIXED_MENU' if len(results)==len(reps) else 'CPU_PROFILE_PARTIAL','scope':__doc__,'profile':profile,'cases':results,'strict_count':sum(z['best']['strict'] for z in results),'nonstrict':[z for z in results if not z['best']['strict']],'maximum_best_bound':str(max(Fraction(z['best']['bound']) for z in results)),'cpu_seconds':time.process_time()-st}
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],'CASES',len(results),'STRICT',out['strict_count'],'MAX',out['maximum_best_bound'],'CPU',out['cpu_seconds'],flush=True)
