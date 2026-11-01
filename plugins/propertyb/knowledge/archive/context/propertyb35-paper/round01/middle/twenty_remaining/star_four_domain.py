"""Actual four unit-neighbour shared-star domain after all 440 three-neighbour projections.
Used only when at least4 unit neighbours have degree8/9; the exactly3 exception
has actual degree spectrum x6, outside five7, unit three8 and eleven10.
"""
from pathlib import Path
import sys
HERE=Path(__file__).parent;sys.path[:0]=[str(HERE.parent),str(HERE.parent/'twentytwo')]
from star_pilot import parts,recover
from pilot import *
HERE=Path(__file__).parent

def canon(part):return tuple(sorted(tuple(sorted(B)) for B in part))
def projected_part(part,S):
 oldnew={old:new for new,old in enumerate(S)}
 return canon([[oldnew[i] for i in B if i in oldnew] for B in part if any(i in oldnew for i in B)])
def main():
 start=time.time();old=json.loads((HERE/'STAR_THREE_REFINED.json').read_text())['cases']
 joint=json.loads((HERE/'STAR_THREE_JOINT.json').read_text())['results']
 strict_joint={z['source_id'] for z in joint if Q(z.get('bound','2'))<1}
 lookup={}
 for idx,r in enumerate(old):
  if r['strict'] or idx in strict_joint:continue
  key=(tuple(r['neighbor_degrees']),tuple(r['neighbor_codegrees']),canon(r['center_partition']))
  lookup.setdefault(key,set()).add(r['neighbor_triple'])
 groups=[]
 for ds in ((8,8,8,8),(8,8,8,9),(8,8,9,9),(8,9,9,9),(9,9,9,9)):
  pairs=list(combinations(range(4),2));subs=list(combinations(range(4),3));bits=[sum(1<<i for i in S) for S in subs]
  for ps in product(range(1,4),repeat=6):
   pairmap=dict(zip(pairs,ps))
   for part in parts(4):
    opts=[]
    for S in subs:
     key=(tuple(ds[i] for i in S),tuple(pairmap[ij] for ij in combinations(S,2)),projected_part(part,S))
     opts.append(lookup.get(key,set()))
    if any(not o for o in opts):continue
    for ts in product(*opts):
     for q in range(min(ts)+1):
      ns=recover(6,ds,ps,part,{**dict(zip(bits,ts)),15:q})
      if ns is None:continue
      groups.append(dict(neighbor_degrees=ds,neighbor_codegrees=ps,center_partition=part,triples=ts,four=q,counts=ns))
 (HERE/'STAR_FOUR_DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,cases=groups,elapsed_seconds=time.time()-start)),indent=2)+'\n')
 print('domain',len(groups),'bydegrees',{str(ds):sum(tuple(z['neighbor_degrees'])==ds for z in groups) for ds in ((8,8,8,8),(8,8,8,9),(8,8,9,9),(8,9,9,9),(9,9,9,9))},'seconds',time.time()-start)
if __name__=='__main__':main()
