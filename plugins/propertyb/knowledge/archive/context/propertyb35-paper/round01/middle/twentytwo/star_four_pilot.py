"""Complete minimum-weight four-neighbour core for M35 v22 unique seven-degree point.
Six weighted graphs, actual center-edge set partitions, inclusive high intersections.
"""
from star_pilot import *
HERE=Path(__file__).parent
GRAPHS=[('2K2_11',[(0,1,1),(2,3,1)]),('2K2_12',[(0,1,1),(2,3,2)]),('2K2_22',[(0,1,2),(2,3,2)]),('P4',[(0,1,1),(1,2,1),(2,3,1)]),('C4',[(0,1,1),(1,2,1),(2,3,1),(3,0,1)]),('K3+K1',[(0,1,1),(0,2,1),(1,2,1)])]

def domain():
 out=[];bits=[7,11,13,14]
 for name,edges in GRAPHS:
  ws={frozenset((a,b)):w for a,b,w in edges};pairs=list(combinations(range(4),2));ps=[1+ws.get(frozenset(ij),0) for ij in pairs]
  triplecaps=[min(ps[j] for j,ij in enumerate(pairs) if all(t>>i&1 for i in ij)) for t in bits]
  for part in parts(4):
   for ts in product(*(range(c+1) for c in triplecaps)):
    for q in range(min(ts)+1):
     ns=recover(7,[8]*4,ps,part,{**dict(zip(bits,ts)),15:q})
     if ns is None:continue
     out.append(dict(graph=name,weights=edges,neighbor_codegrees=ps,center_partition=part,triples=ts,four=q,counts=ns))
 return out

def main():
 start=time.time();groups=domain();print('domain',len(groups),flush=True)
 (HERE/'STAR_FOUR_DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,cases=groups)),indent=2)+'\n')
 out=[]
 # Center role may occupy each position; all neighbour role permutations.
 poses=[p for k in (9,8,10,7,11) for p in permutations(range(k,k+5))]
 for idx,r in enumerate(groups):
  ns=r['counts'];win=None
  for pos in poses:
   z=evaluate(22,ns,pos)
   if win is None or z['bound']<win['bound']:win=z
   if win['strict']:break
  win.update(r);out.append(win)
  print(idx,r['graph'],r['center_partition'],r['triples'],r['four'],win['bound'],flush=True)
  if time.time()-start>180:break
 (HERE/'STAR_FOUR.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(groups),domain_size=len(groups),cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
 print('done',len(out),'strict',sum(r['strict'] for r in out),'domain',len(groups),'seconds',time.time()-start)
if __name__=='__main__':main()
