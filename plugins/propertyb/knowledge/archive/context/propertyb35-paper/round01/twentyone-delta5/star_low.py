"""Complete necessary three-neighbour unit star of degree5 center v21/M35; degree7/8 neighbours."""
from pathlib import Path
import sys,itertools,time,json
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
sys.path[:0]=[str(ROOT/'context/propertyb35-paper/round01/middle'),str(ROOT/'context/propertyb35-paper/round01/middle/twentytwo'),str(ROOT/'context/propertyb34/round01/high-math')]
from pilot import json_value
def parts(n):
 def rec(i,blocks):
  if i==n:yield tuple(tuple(b) for b in blocks);return
  for j in range(len(blocks)):
   blocks[j].append(i);yield from rec(i+1,blocks);blocks[j].pop()
  yield from rec(i+1,blocks+[[i]])
 yield from rec(0,[])
def recover(center,ds,ps,partition,high):
 s=len(ds);ns={1:center-len(partition)}
 for b in partition:ns[1|sum(1<<(i+1) for i in b)]=1
 inc={1<<i:d for i,d in enumerate(ds)}
 inc.update({sum(1<<i for i in ij):c for ij,c in zip(itertools.combinations(range(s),2),ps)});inc.update(high)
 exact={}
 for t in sorted(range(1,1<<s),key=int.bit_count,reverse=True):
  center_contribution=int(any(all(i in b for i in range(s) if t>>i&1) for b in partition))
  exact[t]=inc[t]-center_contribution-sum(n for u,n in exact.items() if u&t==t)
  if exact[t]<0:return None
 for t,n in exact.items():ns[t<<1]=n
 ns[0]=35-sum(ns.values())
 return ns if min(ns.values())>=0 else None
from subset_position_dp import SubsetEngine
HERE=Path(__file__).parent

def main():
 st=time.time();src=json.loads((HERE/'PILOT.json').read_text())['triples'];lookup={(tuple(r['degrees'][1:]),r['codegrees'][2],r['triple']):r['strict'] for r in src};dom=[]
 for ds in [(5,8,8),(6,7,7),(6,7,8),(6,8,8)]:
  for ps in itertools.product(range(1,4),repeat=3):
   for pp in parts(3):
    if any(sum(c-1 for ij,c in zip(itertools.combinations(range(3),2),ps) if i in ij)>4*d-20 for i,d in enumerate(ds)):continue
    if any(lookup[(tuple(ds[i] for i in ij),c,int(any(all(i in b for i in ij) for b in pp)))] for ij,c in zip(itertools.combinations(range(3),2),ps)):continue
    for t in range(min(ps)+1):
     ns=recover(5,ds,ps,pp,{7:t})
     if ns is None:continue
     dom.append(dict(neighbor_degrees=ds,neighbor_codegrees=ps,center_partition=pp,neighbor_triple=t,counts=ns))
 (HERE/'STAR_LOW_DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,cases=dom)),indent=2)+'\n')
 out=[]
 for r in dom:
  eng=SubsetEngine(21,4,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
 for ds in [(5,8,8),(6,7,7),(6,7,8),(6,8,8)]:
  rr=[z for z in out if z['neighbor_degrees']==ds];print(ds,'domain',len(rr),'strict',sum(z['strict'] for z in rr),'max',max(z['bound'] for z in rr),flush=True)
 (HERE/'STAR_LOW_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(dom),cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st)
if __name__=='__main__':main()
