"""Four exact rare-low-unit conflict cores; local trace inventories, not H enumeration."""
from pathlib import Path
import sys, itertools, json, time
ROOT=Path(__file__).resolve().parents[5]
sys.path.insert(0,str(ROOT/'context/propertyb35-paper/round01/middle'))
from pilot import evaluate,json_value
sys.path.insert(0,str(ROOT/'context/propertyb35-paper/round01/twentyfour'))
from fourlock_pilot import inventory
HERE=Path(__file__).parent
CORES={
 'four_cycle':([6]*4,[(0,1),(1,2),(2,3),(0,3)]),
 'five_cycle_seven':([6,6,6,6,7],[(0,1),(1,2),(2,3),(3,4),(0,4)]),
 'bowtie_seven':([6,6,6,6,7],[(0,1),(2,3),(0,4),(1,4),(2,4),(3,4)]),
 'five_cycle_six':([6]*5,[(0,1),(1,2),(2,3),(3,4),(0,4)])}
def domain(name):
 ds,edges=CORES[name];s=len(ds);edges={tuple(sorted(e)) for e in edges}
 pairs={(i,j):1+int((i,j) in edges) for i,j in itertools.combinations(range(s),2)}
 for ns in inventory(s,ds,pairs):
  # On five selected vertices an exact full trace is a unique actual edge.
  if s==5 and ns[(1<<s)-1]>1:continue
  yield ns
def main():
 st=time.time();out=[]
 for name,(ds,_) in CORES.items():
  dom=list(domain(name));s=len(ds)
  print('domain',name,len(dom),flush=True)
  positions=[tuple(range(k,k+s)) for k in range(1,24-s+1)]
  positions += [(1,6,12,18)] if s==4 else [(1,6,12,18,23),(1,2,11,12,13)]
  for ns in dom:
   z=min((evaluate(23,ns,p) for p in positions),key=lambda z:z['bound'])
   out.append(dict(core=name,counts=ns,positions=z['positions'],bound=z['bound'],strict=z['strict']))
  rr=[z for z in out if z['core']==name]
  print('result',name,sum(z['strict'] for z in rr),'/',len(rr),'max',max(z['bound'] for z in rr),'time',time.time()-st,flush=True)
 (HERE/'CORE_PILOT.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed_seconds=time.time()-st,cores=CORES,profiles=out)),indent=2)+'\n')
if __name__=='__main__':main()
