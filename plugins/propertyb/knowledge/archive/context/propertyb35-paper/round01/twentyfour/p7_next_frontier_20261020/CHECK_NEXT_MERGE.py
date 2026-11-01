from itertools import combinations_with_replacement
from fractions import Fraction
from pathlib import Path
import json
D=Path(__file__).parent
old={1:{(17,0,0),(15,1,0),(14,0,1),(0,4,3),(1,2,4),(2,0,5),(0,1,5),(0,7,1)},
     2:{(13,0,0),(11,1,0),(10,0,1),(7,0,2),(4,0,3),(1,0,4),(0,5,1),(1,3,2),(2,1,3),(0,2,3),(8,1,1)}}
rows=[]
for I in [1,2]:
 inv={(a,b,c) for a in range(18) for b in range(9) for c in range(6) if a+2*b+3*c==21-4*I}
 assert old[I]<=inv
 new={(5,0,4)} if I==1 else set()
 remain=sorted(inv-old[I]-new,key=lambda x:(x[2],x[1]))
 rows.append({'I':I,'all_inventory_count':len(inv),'previous_complete':sorted(old[I]),'new_analytic_candidate':sorted(new),'remaining_whole_inventory_count':len(remain),'remaining_inventory':remain})
assert [(r['all_inventory_count'],r['remaining_whole_inventory_count']) for r in rows]==[(33,24),(21,10)]
scalars=[]
for g in combinations_with_replacement([2,3,4],4):
 if g==(2,2,2,2):continue
 N=g[0]*g[1]*g[2]*g[3]
 bad=4*max(g)-3+Fraction(3,2)*sum(g)
 assert bad<N
 scalars.append({'sizes':g,'candidate_count':N,'block_bound':str(bad),'margin':str(N-bad)})
assert len(scalars)==14
# The four C-frequency profiles are derived directly, not assumed.
profiles=sorted({tuple(sorted(x,reverse=True)) for x in __import__('itertools').product(range(3),repeat=5) if sum(x)>=8})
assert profiles==[(2,2,2,1,1),(2,2,2,2,0),(2,2,2,2,1),(2,2,2,2,2)]
# Exceptional degree-zero/high-count-zero C point: J on {w,d0,d1}.
exception=[]
for a in range(6):
 for b in range(6):
  for c in range(6):
   if a+b+c==5 and a>=1 and b>=1 and a+c<=3 and b+c<=3:
    assert (a,b,c) in [(2,3,0),(3,2,0),(2,2,1)]
    exception.append((a,b,c))
assert len(exception)==3
out={'status':'PASS','scope':'inventory arithmetic and local scalar inequalities only; no P-source or H enumeration','frontier':rows,
 'four_positive_disjoint_scalar_profiles':scalars,'minimum_scalar_margin':str(min(Fraction(x['margin']) for x in scalars)),
 'C_high_frequency_profiles':profiles,'exceptional_three_vertex_J':exception}
(D/'NEXT_MERGE_SCALARS.json').write_text(json.dumps(out,indent=2)+'\n')
print({'status':'PASS','remaining_whole_inventories':[24,10],'four_group_scalar_profiles':len(scalars),'minimum_margin':out['minimum_scalar_margin']})
