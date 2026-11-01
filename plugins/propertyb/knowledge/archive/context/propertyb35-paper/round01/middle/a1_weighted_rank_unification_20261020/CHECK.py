"""Tiny component-rank arithmetic plus one structured 4x4 construction, no random search."""
from pathlib import Path
from itertools import permutations,combinations
from collections import Counter
from fractions import Fraction as Rat
import json,time
HERE=Path(__file__).resolve().parent

def parts(n,lo=1):
 if n==0:yield ();return
 for x in range(lo,n+1):
  for rest in parts(n-x,x):yield (x,)+rest

def ceil_log2(s):return (s-1).bit_length()
def rank_graph(edges,selected):
 parent=list(range(29))
 def find(x):
  while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
  return x
 r=0
 for i,j,n in edges:
  if n not in selected:continue
  a,b=find(i),find(j)
  if a!=b:parent[a]=b;r+=1
 return r

def pairings(xs):
 if not xs:yield ();return
 a=xs[0]
 for b in xs[1:]:
  for rest in pairings([x for x in xs[1:] if x!=b]):yield ((a,b),)+rest

def main():
 st=time.process_time();possible=[]
 for r in range(15):
  for rs in parts(r):
   sizes=tuple(x+1 for x in rs);isolates=29-sum(sizes)
   if isolates<0 or sum(ceil_log2(s) for s in sizes)>r-9:continue
   deficit=7*isolates+8*sizes.count(2)
   possible.append(dict(rank=r,nontrivial_sizes=sizes,isolates=isolates,deficit_lower=deficit))
 assert [(r['nontrivial_sizes'],r['isolates']) for r in possible]==[((14,),15),((2,14),13),((15,),14)]
 assert all(r['deficit_lower']>95 for r in possible)
 allparts=list(parts(29));assert len(allparts)==4565
 low=[];improved=[]
 for ss in allparts:
  if ss.count(1)>3:continue
  base=sum(1+ceil_log2(s) for s in ss)
  if base>20:continue
  r=29-len(ss)
  if r<=20:low.append(dict(forest_rank=r,component_sizes=ss,rank_lower=base,slack=20-base))
  # Rank5 blocks of sizes13..16 are excluded by the paper affine-cube lemma.
  stronger=base+sum(13<=s<=16 for s in ss)
  if stronger<=20:improved.append((r,ss,stronger))
 assert len(low)==16 and min(z['forest_rank'] for z in low)==19
 assert min(r for r,ss,cost in improved)==20
 remainder=[dict(component_sizes=ss,new_rank_lower=cost) for r,ss,cost in improved if r==20]
 after8=[];after7=[]
 for row in remainder:
  ss=row['component_sizes'];cost=row['new_rank_lower']+ss.count(8)
  if cost<=20:
   after8.append(dict(component_sizes=ss,new_rank_lower=cost))
   cost7=cost+ss.count(7)
   if cost7<=20:after7.append(dict(component_sizes=ss,new_rank_lower=cost7))
 assert len(after8)==7 and len(after7)==6
 S=list(permutations(range(4)))
 V=[(0,1,2,3),(1,0,3,2),(2,3,0,1),(3,2,1,0)]
 unseen=set(S);cosets=[]
 while unseen:
  p=min(unseen);coset={tuple(p[v[i]] for i in range(4)) for v in V}
  cosets.append(coset);unseen-=coset
 removed={(0,1,2,3),(1,0,2,3),(0,1,3,2)}
 base=[set([16]+[4*i+j for j in range(4)]) for i in range(4)]
 base +=[set([16]+[4*i+j for i in range(4)]) for j in range(4)]
 records=[]
 for grouping in pairings(list(range(6))):
  groups=[(cosets[a]|cosets[b])-removed for a,b in grouping]
  if sorted(map(len,groups))!=[6,7,8]:continue
  groups.sort(key=len)
  H=base+[set([17+c]+[4*i+p[i] for i in range(4)]) for c,G in enumerate(groups) for p in sorted(G)]
  assert len(H)==29 and len({tuple(sorted(e)) for e in H})==29
  degrees=[sum(v in e for e in H) for v in range(20)]
  assert sorted(degrees)==[6]*5+[7]*5+[8]*10
  inter=[(i,j,len(H[i]&H[j])) for i,j in combinations(range(29),2)]
  ranks=[rank_graph(inter,z) for z in [{0,2,3,4},{0,3,4},{3,4},{4}]]
  F=616+110*ranks[0]+374*ranks[1]+66*ranks[2]+1430*ranks[3]
  records.append(dict(coset_pairs=grouping,ranks=ranks,F=F,edges=[sorted(e) for e in H],degrees=degrees,
                      intersection_histogram=dict(sorted(Counter(n for _,_,n in inter).items()))))
 best=min(records,key=lambda r:r['F'])
 trace=Rat(435,4);trace_square_constant=Rat(6473,16)
 assert trace*trace-19*trace_square_constant==Rat(66238,16)
 assert -(-66238//608)==109
 hunter=616+110*19+374*6+66*3+1430*3
 assert hunter==9438 and 164896-174174+hunter==160
 assert 17826*8+8838*13<259248<=17826*8+8838*14
 out=dict(status='PASS',low_rank_component_patterns=possible,degree_deficit_total=95,
          full_integer_partition_count=4565,isolates_upper=3,rank_le20_full_base_partitions=low,
          rank20_after_rank5_cube_exclusion=remainder,
          rank20_after_additional_size8_exclusion=after8,
          rank20_after_additional_size7_imbalance_exclusion=after7,
          proved_nonunit_rank_lower=20,structured_construction_count=len(records),
          best_structured_F=best['F'],best_structured=best,
          goal_F_le_9278_found=best['F']<=9278,CPU_seconds=time.process_time()-st)
 out['strong_forest_corollary']=dict(centered_trace=str(trace),centered_trace_square_constant=str(trace_square_constant),
     Q_inequality='608Q>=66238',Q_integer_lower=109,heavy_pair_lower='a0+a3+3a4>=28',
     q3_Hunter_lower=hunter,minimum_star_success_margin=160,original_n4_upper=8)
 (HERE/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='best_structured'})
if __name__=='__main__':main()
