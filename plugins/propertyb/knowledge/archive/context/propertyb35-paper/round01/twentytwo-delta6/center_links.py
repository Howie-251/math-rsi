"""Complete six-edge centre-link intersection classification with incidence excess three.
This enumerates only six labelled 4-set overlaps, not whole hypergraphs.
"""
from pathlib import Path
from itertools import combinations,combinations_with_replacement,permutations
from collections import Counter
import json,time
HERE=Path(__file__).resolve().parent
PERMS=list(permutations(range(6)))
SUBS={r:[sum(1<<i for i in S)for S in combinations(range(6),r)]for r in (2,3,4)}
def canon(xs):
 return min(tuple(sorted(sum(1<<p[i]for i in range(6)if x>>i&1)for x in xs))for p in PERMS)
def main():
 start=time.process_time();counts=Counter()
 for xs in [(x,)for x in SUBS[4]]:counts[canon(xs)]+=1
 for x in SUBS[3]:
  for y in SUBS[2]:counts[canon((x,y))]+=1
 for xs in combinations_with_replacement(SUBS[2],3):counts[canon(xs)]+=1
 out=[]
 for xs,c in sorted(counts.items(),key=lambda z:(len(z[0]),z[0])):
  unit=[4-sum(x>>i&1 for x in xs)for i in range(6)];assert min(unit)>=1
  bad=[(i,j)for i,j in combinations(range(6),2)if any(x>>i&1 and x>>j&1 for x in xs)]
  p=len(xs);h=sum(unit);assert h==21-p and sum(x.bit_count()-1for x in xs)==3
  out.append(dict(nonunit_incidence_masks=xs,nonunit_degrees_at_x=[x.bit_count()for x in xs],unit_group_sizes=unit,unit_count=h,bad_link_pairs=bad,labelled_patterns=c,low_pool_budget=3*h-43))
 assert len(out)==12 and sum(counts.values())==995
 (HERE/'CENTER_LINKS.json').write_text(json.dumps(dict(scope=__doc__,classes=out,labelled_patterns=995,class_count=12,cpu_seconds=time.process_time()-start),indent=2)+'\n');print('classes',len(out),'patterns',sum(counts.values()),'cpu',time.process_time()-start)
if __name__=='__main__':main()
