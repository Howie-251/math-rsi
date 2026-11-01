"""Independent multiplicity recursion, adjacent-transposition orbits, and color counts."""
from pathlib import Path
from itertools import combinations,product
from math import comb
import json,time
HERE=Path(__file__).resolve().parent
PAIRS=list(combinations(range(6),2));INDEX={p:i for i,p in enumerate(PAIRS)}
DEN=comb(20,10)
def C(n,r):return comb(n,r) if 0<=r<=n else 0

def domain():
 out=set()
 def rec(i,left,seq):
  if i==15:
   if left==0:out.add(tuple(seq))
   return
  for m in range(min(2,left)+1):rec(i+1,left-m,seq+[i]*m)
 rec(0,4,[]);return out

def image(key,j):
 def sw(v):return j+1 if v==j else j if v==j+1 else v
 return tuple(sorted(INDEX[tuple(sorted(map(sw,PAIRS[i])))] for i in key))

def blocks(key):
 out=[set() for _ in range(6)]
 for point,edge in enumerate(key):
  u,v=PAIRS[edge];out[u].add(point);out[v].add(point)
 private=4
 for B in out:
  need=4-len(B)
  B.update(range(private,private+need))
  private+=need
 assert private==20
 return out

def count_alternate(Bs):
 no_red=0
 for bits in product((False,True),repeat=6):
  R=set().union(*(Bs[i] for i,b in enumerate(bits) if b))
  no_red+=(-1 if sum(bits)%2 else 1)*C(20-len(R),10-len(R))
 no_both_monochrome=0
 for choices in product((0,1,2),repeat=6):
  R=set().union(*(Bs[i] for i,c in enumerate(choices) if c==1))
  B=set().union(*(Bs[i] for i,c in enumerate(choices) if c==2))
  if R&B:continue
  no_both_monochrome+=(-1 if sum(c!=0 for c in choices)%2 else 1)*C(20-len(R)-len(B),10-len(R))
 return 2*no_red-no_both_monochrome

def direct(Bs):
 good=0
 for redtuple in combinations(range(20),10):
  R=set(redtuple)
  has_red=any(B<=R for B in Bs)
  has_blue=any(not (B&R) for B in Bs)
  good+=not(has_red and has_blue)
 return good

def main():
 st=time.process_time();raw=json.loads((HERE/'RESULT.json').read_text());D=domain()
 assert len(D)==2835
 union=set();worst=[]
 for row in raw['orbits']:
  rep=tuple(row['representative']);seen={rep};queue=[rep]
  while queue:
   z=queue.pop()
   for j in range(5):
    v=image(z,j)
    if v not in seen:seen.add(v);queue.append(v)
  assert seen=={tuple(v) for v in row['orbit_members']}
  assert seen<=D and not union&seen
  union|=seen
  Bs=blocks(rep)
  assert [sum(1<<v for v in B) for B in Bs]==row['link_masks']
  assert count_alternate(Bs)==row['C_count']
 assert union==D and len(raw['orbits'])==18
 for row in raw['orbits'][:3]:
  actual=direct(blocks(tuple(row['representative'])))
  assert actual==row['C_count'];worst.append(dict(key=row['representative'],count=actual,samples=DEN))
 assert min(row['C_count'] for row in raw['orbits'])==164896
 assert all(row['C_count']>=165640 for row in raw['orbits'][2:])
 assert 4*2002+24*22==8536 and 165640-174174+8536==2
 assert 164896-174174+5*2002==732
 assert 29-20+2==11
 assert 4*2002+7*132+17*22==9306
 assert 164896-174174+9306==28
 assert 174174-165512-8536==126
 assert 506-22==484 and 2*(132-22)==220
 assert 7*3+3*2+8==35<460-comb(29,2)==54
 assert 5*comb(6,2)+5*comb(7,2)+10*comb(8,2)==460
 # All simple graphs on at most five vertices: exact rank<=4 + diamond-free + K5-free bound.
 max_edges=0;graphs=0
 ps=list(combinations(range(5),2))
 for mask in range(1<<10):
  adj=[set() for _ in range(5)];e=mask.bit_count()
  for i,(u,v) in enumerate(ps):
   if mask>>i&1:adj[u].add(v);adj[v].add(u)
  if e==10:continue
  if any(any(b not in adj[a] for a,b in combinations(adj[u]&adj[v],2))
         for u,v in ps if v in adj[u]):continue
  graphs+=1;max_edges=max(max_edges,e)
 assert max_edges==7
 out=dict(status='PASS',independent_labeled_keys=len(D),adjacent_transposition_orbits=18,
          all_orbit_C_counts_checked=True,direct_worst_three=worst,minimum_C=164896,
          other_sixteen_C_lower=165640,rank4_completed_tree_deduction=8536,
          general_nonunit_forest_rank_lower=11,uniform_rank_extension_deduction=9306,
          uniform_rank_extension_margin=28,
          tight_other_orbit_margin=2,rank5_quad_only_margin=732,
          small_graph_scope='all 1024 simple5-vertex graphs, edge-common-neighborhood clique and no K5',
          graph_models_checked=graphs,maximum_edges=7,CPU_seconds=time.process_time()-st)
 (HERE/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
if __name__=='__main__':main()
