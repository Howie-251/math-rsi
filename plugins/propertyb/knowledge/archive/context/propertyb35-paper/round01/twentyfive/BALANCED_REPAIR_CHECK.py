"""Independent elementary swap counts for every five-set in a fixed balanced
25-point coloring; plus the older symmetric 22233 first-moment comparison.
No hypergraphs are generated or classified.
"""
from pathlib import Path
from itertools import combinations,permutations
from collections import Counter
from math import comb
from fractions import Fraction as Q
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();groups=[set(range(5*i,5*i+5)) for i in range(5)];r=[2,2,2,3,3]
red=set().union(*(set(sorted(g)[:rr]) for g,rr in zip(groups,r)));rm=sum(1<<v for v in red);full=(1<<25)-1
owner={v:i for i,g in enumerate(groups) for v in g}
swaps=[(u,v,(1<<u)|(1<<v)) for g in groups for u in g&red for v in g-red]
assert len(swaps)==30
hist=Counter(); max_create=0;mono_min_destroy=100; examples={}
for E in combinations(range(25),5):
 em=sum(1<<v for v in E);k=len(set(E)&red);old=k in (0,5);cre=des=0
 for u,v,sm in swaps:
  after=(em&(rm^sm)).bit_count();new=after in (0,5)
  cre+=new and not old;des+=old and not new
 if old:
  expected=sum((5-r[owner[v]]) if k==5 else r[owner[v]] for v in E)
  assert cre==0 and des==expected and des>=10;mono_min_destroy=min(mono_min_destroy,des)
 elif k in (1,4):
  minority=next(v for v in E if (v in red)==(k==1));i=owner[minority]
  majority_count=(5-r[i]) if k==1 else r[i]
  expected=majority_count-(sum(owner[v]==i for v in E)-1)
  assert des==0 and cre==expected and 0<=cre<=3
 else:assert cre==des==0
 max_create=max(max_create,cre);hist[(k,cre,des)]+=1
 if (k,cre,des) not in examples:examples[(k,cre,des)]=list(E)
# Symmetric random selection of which two groups receive red quota3,
# followed by uniform group-internal subsets. These exact edge probabilities
# depend only on the seven partitions of five.
parts=[[5],[4,1],[3,2],[3,1,1],[2,2,1],[2,1,1,1],[1,1,1,1,1]]
quotas=sorted(set(permutations([2,2,2,3,3])));assert len(quotas)==10
rows=[]
for a in parts:
 aa=a+[0]*(5-len(a));prob=Q(0)
 for rr in quotas:
  pr=pb=Q(1)
  for n,q in zip(aa,rr):
   pr*=Q(comb(q,n) if q>=n else 0,comb(5,n));pb*=Q(comb(5-q,n) if 5-q>=n else 0,comb(5,n))
  prob+=pr+pb
 prob/=10
 internal=sum(comb(n,2) for n in aa)
 rows.append(dict(partition=a,monochromatic_probability=str(prob),internal_pairs=internal))
p0=Q(rows[-1]['monochromatic_probability']);delta=min((p0-Q(v['monochromatic_probability']))/v['internal_pairs'] for v in rows if v['internal_pairs'])
assert delta>=0
bound=35*p0-100*delta
assert bound<2
out=dict(scope=__doc__,groups=[sorted(g) for g in groups],red=sorted(red),red_quotas=r,total_red=len(red),swaps=len(swaps),five_sets=comb(25,5),max_create=max_create,min_destroy_for_mono=mono_min_destroy,histogram=[dict(red_count=k,creates=c,destroys=d,sets=n,example=examples[(k,c,d)]) for (k,c,d),n in sorted(hist.items())],symmetric_firstmoment=dict(quota_orbit=[2,2,2,3,3],quota_placements=10,edge_partition_probabilities=rows,p_transversal=str(p0),penalty_per_internal_pair=str(delta),fixed_total_internal_pair_count=100,universal_expectation_bound=str(bound),already_implies_exists_at_most_one_mono=True,does_not_by_itself_keep_a_specified_quota_placement=True),elapsed_seconds=time.perf_counter()-st)
(P/'BALANCED_REPAIR_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['five_sets','max_create','min_destroy_for_mono','symmetric_firstmoment','elapsed_seconds']},indent=2))
