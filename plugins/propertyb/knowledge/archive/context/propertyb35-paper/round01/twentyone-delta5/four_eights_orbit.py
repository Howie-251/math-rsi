"""Complete8888 actual four-star domain, solving each actual neighbour relabelling orbit once."""
from pathlib import Path
import itertools,json,time
from star_low import SubsetEngine,json_value
HERE=Path(__file__).parent
st=time.time();src=json.loads((HERE/'GENERIC_FOUR_DOMAIN.json').read_text())['cases'];dom=[(i,r) for i,r in enumerate(src) if r['neighbor_degrees']==[8]*4];cache={};out=[]
perms=list(itertools.permutations(range(4)));maps=[[(m&1)|sum(1<<(p[i]+1) for i in range(4) if m>>(i+1)&1) for m in range(32)] for p in perms]
for idx,r in dom:
 ns={int(t):n for t,n in r['counts'].items()};arr=[ns.get(m,0) for m in range(32)];candidates=[]
 for perm,move in zip(perms,maps):
  moved=[0]*32
  for m,n in enumerate(arr):moved[move[m]]=n
  candidates.append((tuple(moved),perm))
 key,perm=min(candidates)
 if key not in cache:
  eng=SubsetEngine(21,5,dict(enumerate(key)));cache[key]=eng.solve()
 best=cache[key];pos=[best['positions'][0]]+[best['positions'][perm[i]+1] for i in range(4)]
 eng=SubsetEngine(21,5,ns);z=eng.verify(dict(bound=best['bound'],positions=pos,counts=ns));z.update(r);z.update(source_id=idx,strict=z['bound']<1);out.append(z)
 if len(out)%400==0:print(len(out),'strict',sum(z['strict'] for z in out),'orbits',len(cache),'seconds',time.time()-st,flush=True)
 assert time.time()-st<55
(HERE/'GENERIC_8888_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(dom),domain_size=len(dom),orbit_count=len(cache),cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('done',len(out),'strict',sum(z['strict'] for z in out),'orbits',len(cache),'max',max(z['bound'] for z in out),'seconds',time.time()-st)
