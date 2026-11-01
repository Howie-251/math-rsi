"""Complete S6 quotient of four repeated link-points; exact balanced-star counts."""
from pathlib import Path
from itertools import combinations,combinations_with_replacement,permutations
from collections import Counter
from math import comb
import json,time
HERE=Path(__file__).resolve().parent
PAIRS=list(combinations(range(6),2));PINDEX={p:i for i,p in enumerate(PAIRS)}
DEN=comb(20,10)
def C(n,r):return comb(n,r) if 0<=r<=n else 0

def links(key):
 blocks=[set() for _ in range(6)]
 for b,pi in enumerate(key):
  for v in PAIRS[pi]:blocks[v].add(b)
 nxt=4
 for block in blocks:
  while len(block)<4:block.add(nxt);nxt+=1
 assert nxt==20 and len({frozenset(v) for v in blocks})==6
 return [sum(1<<v for v in b) for b in blocks]

def IE(lm):
 union=[0]*64
 for m in range(1,64):
  bit=m&-m;union[m]=union[m^bit]|lm[bit.bit_length()-1]
 both=0
 for red in range(1,64):
  blue=(63^red)
  while blue:
   R=union[red];B=union[blue]
   if not R&B:
    nr=R.bit_count();nb=B.bit_count()
    both+=(-1 if (red.bit_count()+blue.bit_count())%2 else 1)*C(20-nr-nb,10-nr)
   blue=(blue-1)&(63^red)
 return DEN-both

def direct(lm):
 red=(1<<10)-1;limit=1<<20;count=0;samples=0
 while red<limit:
  hasR=False;hasB=False
  for L in lm:
   v=red&L
   if v==L:hasR=True
   if v==0:hasB=True
  count+=not(hasR and hasB);samples+=1
  low=red&-red;tmp=red+low;red=tmp|(((tmp^red)>>2)//low)
 assert samples==DEN
 return count

def main():
 st=time.process_time()
 raw=list(combinations_with_replacement(range(15),4))
 assert len(raw)==3060
 domain={k for k in raw if max(Counter(k).values())<=2}
 assert len(domain)==2835
 actions=[]
 for p in permutations(range(6)):
  actions.append(tuple(PINDEX[tuple(sorted((p[u],p[v])))] for u,v in PAIRS))
 unseen=set(domain);rows=[]
 while unseen:
  rep=min(unseen);orbit={tuple(sorted(act[i] for i in rep)) for act in actions}
  assert orbit<=unseen and orbit<=domain
  unseen-=orbit
  lm=links(rep);count=IE(lm)
  deg=[sum(v in PAIRS[i] for i in rep) for v in range(6)]
  assert max(deg)<=4
  rows.append(dict(representative=rep,edge_pairs=[PAIRS[i] for i in rep],block_degrees=deg,
                   orbit_members=sorted(orbit),orbit_size=len(orbit),link_masks=lm,C_count=count))
 rows.sort(key=lambda r:(r['C_count'],r['representative']))
 checks=[]
 for r in rows[:3]:
  actual=direct(r['link_masks']);assert actual==r['C_count']
  checks.append(dict(representative=r['representative'],samples=DEN,IE=r['C_count'],direct=actual))
 minimum=rows[0]['C_count'];gap=29*6006-minimum
 threshold=gap//2002+1
 mono_pairs=[]
 for j in range(5):
  same=2*C(10+j,j)
  opposite=2*C(10,5) if j==0 else 0
  mono_pairs.append(same+opposite)
 assert mono_pairs==[506,22,132,572,2002]
 out=dict(complete=True,raw_multichoose=3060,complete_labeled_domain=len(domain),
          orbit_count=len(rows),orbits=rows,minimum_C_count=minimum,
          minimum_representatives=[r['representative'] for r in rows if r['C_count']==minimum],
          balanced_sample_count=DEN,direct_checks=checks,Hbar_union_single_sum=174174,
          deficit=gap,four_intersection_forest_rank_sufficient=threshold,
          pair_monochromatic_counts=mono_pairs,CPU_seconds=time.process_time()-st)
 (HERE/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
 print({k:v for k,v in out.items() if k not in ['orbits','direct_checks']})
if __name__=='__main__':main()
