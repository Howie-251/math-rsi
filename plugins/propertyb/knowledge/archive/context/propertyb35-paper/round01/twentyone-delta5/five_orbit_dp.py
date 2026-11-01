"""Degree-preserving actual-neighbour relabelling orbits; fixed original witnesses are independently replayed separately."""
from pathlib import Path
import argparse,itertools,json,time
from star_low import SubsetEngine,json_value
HERE=Path(__file__).parent
p=argparse.ArgumentParser();p.add_argument('degrees',choices=['78888','88888']);a=p.parse_args();ds=[int(c) for c in a.degrees];st=time.time();source=json.loads((HERE/f'GENERIC_{a.degrees}_DOMAIN.json').read_text());assert source['complete'];dom=source['cases'];cache={};out=[]
perms=[p for p in itertools.permutations(range(5)) if all(ds[i]==ds[p[i]] for i in range(5))];maps=[[(m&1)|sum(1<<(p[i]+1) for i in range(5) if m>>(i+1)&1) for m in range(64)] for p in perms]
for idx,r in enumerate(dom):
 ns={int(t):n for t,n in r['counts'].items()};arr=[ns.get(m,0) for m in range(64)];candidates=[]
 for perm,move in zip(perms,maps):
  moved=[0]*64
  for m,n in enumerate(arr):moved[move[m]]=n
  candidates.append((tuple(moved),perm))
 key,perm=min(candidates)
 if key not in cache:
  eng=SubsetEngine(21,6,dict(enumerate(key)));cache[key]=eng.verify(eng.solve());cache[key]['orbit_id']=len(cache)-1
 best=cache[key];pos=[best['positions'][0]]+[best['positions'][perm[i]+1] for i in range(5)]
 z=dict(r,bound=best['bound'],positions=pos,strict=best['bound']<1,source_id=idx,orbit_id=best['orbit_id'],neighbor_permutation=perm);out.append(z)
 if len(out)%500==0:print(len(out),'strict',sum(z['strict'] for z in out),'orbits',len(cache),'seconds',time.time()-st,flush=True)
 if time.time()-st>55:break
(HERE/f'GENERIC_{a.degrees}_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(dom),domain_size=len(dom),orbit_count=len(cache),orbits=sorted(cache.values(),key=lambda z:z['orbit_id']),cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('done',len(out),'strict',sum(z['strict'] for z in out),'orbits',len(cache),'max',max(z['bound'] for z in out),'seconds',time.time()-st)
