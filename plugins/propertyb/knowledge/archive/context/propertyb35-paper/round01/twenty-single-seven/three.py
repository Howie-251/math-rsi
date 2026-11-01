from pilot import *
from itertools import combinations_with_replacement
start=time.time();two=json.loads((HERE/'UNIT_TWO.json').read_text())['cases']
res={(tuple(r['degrees'][1:]),r['neighbor_codegree'],tuple(tuple(B) for B in r['partition'])) for r in two if not r['strict']}
out=[];domains={}
for ds in combinations_with_replacement((8,9,10),3):
 domain=[]
 for part in parts(3):
  options=[]
  for i,j in combinations(range(3),2):
   same=any(i in B and j in B for B in part);p=((0,1),) if same else ((0,),(1,))
   options.append([c for d,c,q in res if d==(ds[i],ds[j]) and q==p])
  for ps in product(*options):
   for t in range(min(ps)+1):
    ns=recover(7,ds,ps,part,{7:t})
    if ns is not None:domain.append(dict(neighbor_degrees=ds,neighbor_codegrees=ps,partition=part,neighbor_triple=t,counts=ns))
 print('domain',ds,len(domain),flush=True);domains[str(ds)]=len(domain)
 for r in domain:
  eng=SubsetEngine(20,4,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
 print('done',ds,'res',sum(not r['strict'] for r in out if tuple(r['neighbor_degrees'])==ds),'seconds',time.time()-start,flush=True)
 (HERE/'UNIT_THREE.json').write_text(json.dumps(json_value(dict(complete=True,cases=out,domains=domains,elapsed_seconds=time.time()-start)),indent=2)+'\n')
 if time.time()-start>120:break
