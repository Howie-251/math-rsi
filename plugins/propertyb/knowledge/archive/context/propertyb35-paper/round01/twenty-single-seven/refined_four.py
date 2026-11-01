from pilot import *
from fractions import Fraction as Q
start=time.time();old=json.loads((HERE/'UNIT_THREE.json').read_text())['cases']
def canon(p):return tuple(sorted(tuple(sorted(B)) for B in p))
def project(part,S):
 m={i:j for j,i in enumerate(S)};return canon([[m[i] for i in B if i in m] for B in part if any(i in m for i in B)])
joint=json.loads((HERE/'JOINT_THREE_ALL.json').read_text())['results']
strictjoint={z['source_id'] for z in joint if Q(z.get('bound','2'))<1}
lookup={}
for idx,r in enumerate(old):
 if r['strict'] or idx in strictjoint:continue
 key=(tuple(r['neighbor_degrees']),tuple(r['neighbor_codegrees']),canon(r['partition']))
 lookup.setdefault(key,set()).add(r['neighbor_triple'])
domain=[]
patterns=[(8,8,8,8),(8,8,8,9),(8,8,9,9),(8,9,9,9),(9,9,9,9)]
for ds in patterns:
 before=len(domain);pairs=list(combinations(range(4),2));subs=list(combinations(range(4),3));bits=[sum(1<<i for i in S) for S in subs]
 for ps in product(range(1,4),repeat=6):
  pm=dict(zip(pairs,ps))
  for part in parts(4):
   opts=[lookup.get((tuple(ds[i] for i in S),tuple(pm[ij] for ij in combinations(S,2)),project(part,S)),()) for S in subs]
   if any(not o for o in opts):continue
   for ts in product(*opts):
    for q in range(min(ts)+1):
     ns=recover(7,ds,ps,part,{**dict(zip(bits,ts)),15:q})
     if ns is not None:domain.append(dict(neighbor_degrees=ds,neighbor_codegrees=ps,partition=part,triples=ts,four=q,counts=ns))
 print('domain',ds,len(domain)-before,flush=True)
(HERE/'REFINED_FOUR_DOMAIN.json').write_text(json.dumps(json_value(dict(cases=domain,elapsed_seconds=time.time()-start)),indent=2)+'\n')
out=[]
for ds in patterns:
 group=[(i,r) for i,r in enumerate(domain) if r['neighbor_degrees']==ds]
 for n,(idx,r) in enumerate(group):
  eng=SubsetEngine(20,5,r['counts']);z=eng.verify(eng.solve());z.update(r);z.update(source_id=idx,strict=z['bound']<1);out.append(z)
  if n in (9,99) or n+1==len(group):print('DP',ds,n+1,'strict',sum(r['strict'] for r in out if r['neighbor_degrees']==ds),'sec',time.time()-start,flush=True)
  if time.time()-start>100:break
 (HERE/'REFINED_FOUR_DP.json').write_text(json.dumps(json_value(dict(cases=out,domain_size=len(domain),processed=len(out),complete=len(out)==len(domain),elapsed_seconds=time.time()-start)),indent=2)+'\n')
 if time.time()-start>100:break
