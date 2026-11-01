"""Unique5 center, all outside>=7: actual four unit-neighbour shared-partition domains after all prior three views."""
from pathlib import Path
import sys,itertools,time,json
from star_low import parts,recover,SubsetEngine,json_value
from six_eights_four import canon,restrict
HERE=Path(__file__).parent
DEGREES=[(7,7,7,7),(7,7,7,8),(7,7,8,8),(7,8,8,8),(8,8,8,8)]
def domain():
 lookup={}
 for r in json.loads((HERE/'STAR_THREE_DP.json').read_text())['cases']:
  if not r['strict']:lookup.setdefault((tuple(r['neighbor_degrees']),tuple(r['neighbor_codegrees']),canon(r['center_partition'])),set()).add(r['neighbor_triple'])
 out=[];pairs=list(itertools.combinations(range(4),2));subs=list(itertools.combinations(range(4),3));bits=[sum(1<<i for i in S) for S in subs]
 for ds in DEGREES:
  for ps in itertools.product(range(1,4),repeat=6):
   pmap=dict(zip(pairs,ps))
   for pp in parts(4):
    opts=[lookup.get((tuple(ds[i] for i in S),tuple(pmap[ij] for ij in itertools.combinations(S,2)),restrict(pp,S)),()) for S in subs]
    if any(not z for z in opts):continue
    for ts in itertools.product(*opts):
     for q in range(min(ts)+1):
      ns=recover(5,ds,ps,pp,dict(zip(bits,ts))|{15:q})
      if ns is not None:out.append(dict(neighbor_degrees=ds,neighbor_codegrees=ps,center_partition=pp,triples=ts,four=q,counts=ns))
 return out

def main():
 st=time.time();dom=domain();(HERE/'GENERIC_FOUR_DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,cases=dom,elapsed_seconds=time.time()-st)),indent=2)+'\n')
 print('domain',len(dom),'bydegrees',{str(ds):sum(tuple(z['neighbor_degrees'])==ds for z in dom) for ds in DEGREES},'seconds',time.time()-st,flush=True)
 out=[]
 for ds in DEGREES:
  group=[(i,r) for i,r in enumerate(dom) if r['neighbor_degrees']==ds];indices=sorted(set(round(i*(len(group)-1)/9) for i in range(10)))
  for j in indices:
   idx,r=group[j];eng=SubsetEngine(21,5,r['counts']);z=eng.verify(eng.solve());z.update(r);z.update(source_id=idx,strict=z['bound']<1);out.append(z)
  rr=[z for z in out if z['neighbor_degrees']==ds];print(ds,'pilot',len(rr),'strict',sum(z['strict'] for z in rr),'max',max(z['bound'] for z in rr),flush=True)
 (HERE/'GENERIC_FOUR_PILOT.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=False,domain_size=len(dom),cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st)
if __name__=='__main__':main()
