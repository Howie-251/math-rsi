"""All actual three-unit-neighbor inventories needed for9^5 or8^2 9^3 selection;
small fixed-DP pilot before any full processing. All projections share one partition.
"""
from common import *
from itertools import product
start=time.time();two=json.loads((HERE/'UNIT_TWO.json').read_text())['cases'];res={(tuple(r['neighbor_degrees']),r['neighbor_codegree'],tuple(tuple(B) for B in r['partition'])) for r in two if not r['strict']};out=[];sizes={}
for ds in ((8,8,9),(8,9,9),(9,9,9)):
 before=len(out)
 for part in parts(3):
  options=[]
  for i,j in combinations(range(3),2):
   same=any(i in B and j in B for B in part);p=((0,1),) if same else ((0,),(1,));options.append([c for dd,c,q in res if dd==(ds[i],ds[j]) and q==p])
  for ps in product(*options):
   for t in range(min(ps)+1):
    ns=recover(8,ds,ps,part,{7:t})
    if ns is not None:out.append(dict(id=len(out),neighbor_degrees=ds,neighbor_codegrees=ps,partition=part,neighbor_triple=t,counts=ns))
 sizes[str(ds)]=len(out)-before
(HERE/'THREE_DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,sizes=sizes,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('domain',sizes,'total',len(out),'seconds',time.time()-start,flush=True)
ids={round(i*(len(out)-1)/17) for i in range(18)};rr=[]
for i in sorted(ids):
 r=out[i];en=SubsetEngine(20,4,r['counts']);z=en.verify(en.solve());z.update(r);z['strict']=z['bound']<1;rr.append(z);print(i,r['neighbor_degrees'],r['neighbor_codegrees'],r['partition'],r['neighbor_triple'],z['bound'],z['strict'],flush=True)
(HERE/'THREE_PILOT.json').write_text(json.dumps(json_value(dict(scope=__doc__,domain_count=len(out),cases=rr,sample_count=len(rr),fixed_strict=sum(r['strict'] for r in rr),elapsed_seconds=time.time()-start)),indent=2)+'\n');print('pilot',len(rr),'strict',sum(r['strict'] for r in rr),'seconds',time.time()-start)
