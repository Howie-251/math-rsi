from pathlib import Path
from collections import Counter
from fractions import Fraction
from itertools import product
import sys,time,json,argparse
P=Path(__file__).resolve().parent; ROOT=P.parents[4];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from independent_structure_bounds import independent_rows
st=time.process_time();ap=argparse.ArgumentParser();ap.add_argument('--profile',action='store_true');args=ap.parse_args()
oldp=P.parent/'three_nonunit_direct_repair_20261020'
fives=json.loads((oldp/'FIVE_LOCK_FULL83.json').read_text())
min8=[j for j in fives['cases'] if min(j['selected_degrees'])>=8]
tails=[j for j in min8 if not j['best']['strict']]
assert len(min8)==25 and len(tails)==2
assert [(tuple(j['traces']),tuple(j['attachments'])) for j in tails]==[((7,25,30),(5,7,7,6,6)),((7,27,29),(9,5,5,6,6))]
def comps(n,k):
 if k==1:yield (n,);return
 for a in range(1,n-k+2):
  for t in comps(n-a,k-1):yield (a,)+t
results=[]
for sid,source in zip(('C','D'),tails):
 traces=source['traces'];a=source['attachments'];Tcost=sum((t.bit_count()-1)*(5-t.bit_count()) for t in traces)
 assert Tcost==({'C':11,'D':10}[sid])
 dF=source['selected_degrees'];eF=sum(max(d-9,0) for d in dF)
 assert 14+eF-dF.count(8)=={'C':15,'D':16}[sid]
 choices=list(comps(8,5));second={s for s in product(range(1,5),repeat=5) if sum(s)==8}
 assert len(choices)==35 and set(choices)==second
 old=Counter({31:1});old.update(traces)
 for v,n in enumerate(a):old[1<<v]+=n
 assert sum(old.values())==35 and 0 not in old
 for s in choices:
  assert all(s[v]<=a[v] for v in range(5))
  counts=Counter()
  for t,n in old.items():
   chosen=s[t.bit_length()-1] if t.bit_count()==1 else 0
   if n-chosen:counts[2*t]+=n-chosen
   if chosen:counts[2*t+1]+=chosen
  assert sum(counts.values())==35
  degrees=[sum(n for t,n in counts.items() if t>>v&1) for v in range(6)]
  assert degrees==[8]+dF
  e=SubsetEngine(21,6,counts);e.inv={p:(0,0,[]) for p in e.inv}
  menu=[(z,*source['best']['positions']) for z in (1,9,10,11,20,21) if z not in source['best']['positions']]
  vals=[]
  for pos in menu:
   bypos={k:1<<v for v,k in enumerate(pos)};left=0;total=0
   for k in range(1,22):
    pivot=bypos.get(k,0);value=e.value(k,left,pivot);assert value is not None;total+=value;left|=pivot
   vals.append({'positions':pos,'bound':str(Fraction(total,e.D)),'strict':total<e.D})
  best=min(vals,key=lambda r:Fraction(r['bound']))
  row={'source':sid,'traces':traces,'attachments':a,'singleton_star':s,'counts':dict(counts),'degrees':degrees,'menu':vals,'best':best}
  if args.profile:
   (P/'PROFILE.json').write_text(json.dumps({'cpu_seconds':time.process_time()-st,'sample':row,'remaining_not_executed':69},indent=2)+'\n');print('PROFILE',time.process_time()-st,best);raise SystemExit
  results.append(row)
  assert time.process_time()-st<10,'Bounded first CPU pass exceeded10seconds'
res={'scope':'21points,35 indexed5edges; two qGamma3 trace tails C,D from full119 generic keys filtered only by minFdegree8; no global e<=4 bound (seeSCOPE_CHECK). Complete35 positive singleton vectors per outside8star; fixed old five-lock witness plus six declared central/end insertion slots. Zero quotas, no layout search. No original-H enumeration. Structural proof separate.','N':21,'locked':6,'free':15,'sample_denominator':e.D,'source_min8_count':25,'source_five_lock_strict':23,'cases':results,'strict_count':sum(r['best']['strict'] for r in results),'maximum_best_bound':str(max(Fraction(r['best']['bound']) for r in results)),'nonstrict':[r for r in results if not r['best']['strict']],'cpu_seconds':time.process_time()-st}
(P/'RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print('TOTAL',len(results),'STRICT',res['strict_count'],'MAX',res['maximum_best_bound'],'CPU',res['cpu_seconds'])
