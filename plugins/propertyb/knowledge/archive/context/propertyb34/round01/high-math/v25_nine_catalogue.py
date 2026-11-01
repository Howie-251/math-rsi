"""Attach all feasible 6/7 degree colors to the complete nine-unit local catalogue."""
from pathlib import Path
from itertools import combinations
import json,sys,time
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE))
from unit_catalogue import fullblocks,canonical

def profile(big,q):
 bs=fullblocks(big,9);ns={t:1 for t in bs}
 for i in range(9):ns[1<<i]=(6 if i<q else 7)-sum(bool(t&(1<<i)) for t in bs)
 ns[0]=34-sum(ns.values())
 assert min(ns.values())>=0
 return {t:n for t,n in ns.items() if n}

if __name__=='__main__':
 source=json.loads((HERE/'UNIT_CATALOGUE_9.json').read_text());assert source['complete'];start=time.perf_counter();out=[]
 for q in (9,8,7,6,5):
  seen={};raw=0
  for base,big in enumerate(source['orbits']):
   bs=fullblocks(big,9);deg=[sum(bool(t&(1<<i)) for t in bs) for i in range(9)]
   for low in combinations(range(9),q):
    singles=[(6 if i in low else 7)-deg[i] for i in range(9)]
    if min(singles)<0 or 34-len(bs)-sum(singles)<0:continue
    raw+=1
    key,p=canonical(big,9,[0 if i in low else 1 for i in range(9)],True)
    assert sum(1<<p[i] for i in low)==(1<<q)-1
    if key not in seen:seen[key]=dict(base=base,large_blocks=key,counts=profile(key,q))
  records=[dict(id=i,**x) for i,x in enumerate(seen.values())]
  result=dict(q=q,complete=True,feasible_colorings=raw,colored_orbits=len(records),elapsed=time.perf_counter()-start,results=records)
  (HERE/f'V25_NINE_Q{q}_CATALOGUE.json').write_text(json.dumps(result,indent=2)+'\n');out.append(dict(q=q,raw=raw,orbits=len(records)));print(out[-1],'seconds',time.perf_counter()-start,flush=True)
 (HERE/'V25_NINE_COLORED_SUMMARY.json').write_text(json.dumps(dict(scope=__doc__,complete=True,elapsed=time.perf_counter()-start,results=out),indent=2)+'\n')
