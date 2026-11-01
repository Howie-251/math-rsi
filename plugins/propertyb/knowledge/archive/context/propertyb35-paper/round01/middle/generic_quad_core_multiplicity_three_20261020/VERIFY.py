"""Independent inclusive-Mobius domain, degree-stabilizer transport and35-index fixed replay."""
from pathlib import Path
from itertools import combinations_with_replacement,permutations,product
from fractions import Fraction
from collections import Counter
import json,sys,importlib.util,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time()
sys.path.insert(0,str(ROOT/'computations'));from independent_structure_bounds import independent_rows
sp=importlib.util.spec_from_file_location('independent_nested',P.parents[1]/'twentyone-delta5/replay.py');nested=importlib.util.module_from_spec(sp);sp.loader.exec_module(nested)
data=json.loads((P/'DOMAIN.json').read_text());result=json.loads((P/'RESULT.json').read_text())
PM=(3,5,6,9,10,12);TM=(7,11,13,14);expected={d for d in combinations_with_replacement(range(7,14),4) if sum(max(x-9,0) for x in d)<=4}
assert expected=={tuple(j['degrees']) for j in data['jobs']}
allreps=set();summ=[]
for job in data['jobs']:
 d=tuple(job['degrees']);keys=set()
 for q in (3,4):
  for c in product(range(q,5),repeat=6):
   cc=dict(zip(PM,c))
   for it in product(*(range(q,min(cc[p] for p in PM if p&t==p)+1) for t in TM)):
    ii=dict(zip(TM,it));ns=[0]*16;ns[15]=q
    for t,v in ii.items():ns[t]=v-q
    for p,v in cc.items():ns[p]=v-sum(z for t,z in ii.items() if t&p==p)+q
    for i in range(4):ns[1<<i]=d[i]-sum(v for p,v in cc.items() if p>>i&1)+sum(v for t,v in ii.items() if t>>i&1)-q
    ns[0]=35-sum(d)+sum(c)-sum(it)+q
    if min(ns)<0:continue
    # Actual selected-to-free pair covering: use sum of all outside slots, sharpen
    # q full edges by their q distinct fifth vertices (simple original H).
    if any(q+sum(v*(5-m.bit_count()) for m,v in enumerate(ns) if m!=15 and m>>i&1)<17 for i in range(4)):continue
    keys.add(tuple(ns))
 assert keys==set(map(tuple,job['label_keys'])),d
 perms=[p for p in permutations(range(4)) if tuple(d[p[i]] for i in range(4))==d]
 reps=set()
 for ns in keys:
  images=[]
  for p in perms:
   out=[0]*16
   for m,v in enumerate(ns):out[sum(1<<p[i] for i in range(4) if m>>i&1)]=v
   images.append(tuple(out))
  reps.add(min(images))
 assert reps==set(map(tuple,job['representative_keys']))
 allreps.update((d,ns) for ns in reps)
 summ.append(dict(degrees=d,labels=len(keys),orbits=len(reps)))
saved={(tuple(c['degrees']),tuple(c['counts'])) for c in result['cases']};assert saved<=allreps
assert {(d,ns) for d,ns in allreps if ns[15]==4 or max(d)<=9}<=saved
vals=[];modes=Counter();strict=[]
for c in result['cases']:
 ns={m:v for m,v in enumerate(c['counts']) if v};pos=tuple(c['positions']);d=tuple(sum(v for m,v in ns.items() if m>>i&1) for i in range(4));assert d==tuple(c['degrees']) and sum(ns.values())==35
 stubs=[frozenset(i+1 for i in range(4) if m>>i&1) for m,v in ns.items() for _ in range(v)]
 rows=independent_rows(21,pos,stubs)
 losses={pos[i]:nested.deduction(ns,pos,i) for i in range(4)} if c['mode']=='nested_total_pure' else {}
 value=sum((min(r['A'],r['B'],r['C']-losses.get(r['k'],Fraction())) for r in rows),Fraction())
 assert value==Fraction(c['bound']) and (value<1)==c['strict'];vals.append(value);modes[c['mode']]+=1
 if value<1:strict.append(c)
closed={}
for name,pred in [('q4',lambda d,ns:ns[15]==4),('q3_maxdegree9',lambda d,ns:ns[15]==3 and max(d)<=9)]:
 family={(d,ns) for d,ns in allreps if pred(d,ns)};rows=[c for c in result['cases'] if (tuple(c['degrees']),tuple(c['counts'])) in family];assert len(rows)==len(family) and all(c['strict'] for c in rows)
 closed[name]=dict(representatives=len(rows),labels=sum(1 for j in data['jobs'] for ns in j['label_keys'] if pred(tuple(j['degrees']),ns)),maximum_bound=str(max(Fraction(c['bound']) for c in rows)),quota_cases=sum(c['mode']!='zero' for c in rows))
out=dict(status='PASS',scope=__doc__,complete_domain_labels=sum(x['labels'] for x in summ),complete_domain_orbits=len(allreps),replayed_cases=len(vals),strict_cases=sum(v<1 for v in vals),nonstrict_cases=sum(v>=1 for v in vals),mode_counts=dict(modes),closed_subdomains=closed,all_probability_complete=False,first_nonstrict=result['cases'][-1],cpu_seconds=time.process_time()-st)
(P/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
