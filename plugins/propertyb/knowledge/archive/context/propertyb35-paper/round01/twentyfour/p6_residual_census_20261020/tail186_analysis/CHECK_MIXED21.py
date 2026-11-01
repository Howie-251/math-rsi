"""Replay unchanged seven/86/59/94 local inventories at negative-four budget21."""
from pathlib import Path
from itertools import combinations
from collections import Counter
from fractions import Fraction as F
import json,time
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]/'positive_occ_three'
start=time.process_time();checks=[]

def evaluate(name,sets,claimed):
 A=list(map(set,sets));U=sorted(set().union(*A))
 reds=[c for c in combinations(U,4) if all(set(c)&a for a in A)]
 assert len(reds)==claimed
 # Conditional fourth-point intersection, independent of a counter over reds.
 h=0
 for tri in combinations(U,3):
  Q=set(tri);miss=[a for a in A if not a&Q]
  good=set.intersection(*miss) if miss else set(U)
  ext=len(good-Q)
  assert ext==sum(Q<=set(c) for c in reds)
  h=max(h,ext)
 bound=21+4*max(h-1,0)
 assert len(reds)>bound
 return {'case':name,'sizes':list(map(len,sets)),'U':len(U),'C4':len(reds),'h3':h,'N4_budget':21,'block_bound':bound,'margin':len(reds)-bound}

def reconstruct(vector,caps):
 A=[[] for _ in caps];d=[0]*5;n=0
 for (a,b),v in zip(combinations(range(5),2),vector):
  d[a]+=v;d[b]+=v
  for _ in range(v):A[a].append(n);A[b].append(n);n+=1
 for a in range(5):
  for _ in range(caps[a]-d[a]):A[a].append(n);n+=1
 return A
j=json.loads((BASE/'eighteen_one_triple/THREE_EDGE_CHECK.json').read_text())
for i,r in enumerate(j['results']):checks.append(evaluate('all4_E3_'+str(i),reconstruct(r['vector'],[4]*5),r['C4_direct']))
j=json.loads((BASE/'five_graph_catalogue.json').read_text())
for i,r in enumerate(j['graphs']):checks.append(evaluate('all4_old86_'+str(i),reconstruct(r['edge_vector'],[4]*5),r['C4']))
j=json.loads((BASE/'eight_mixed_eighteen/SMALL_GRAPH_CHECK.json').read_text())
for i,r in enumerate(j['rows']):checks.append(evaluate('one3_old59_'+str(i),r['sets'],r['C4']))
j=json.loads((BASE/'eight_mixed_two_small_20261020/CHECK.json').read_text())
for i,r in enumerate(j['rows']):checks.append(evaluate('two3_old94_'+str(i),r['sets'],r['C4']))
analytic=[('high_occ_disjoint_four',144,4*21),('all4_zeroM2_star',175,21+13*4),('all4_zeroM2_triangle',80,21+13*4),
 ('one3_zeroM2_star',84,21+13*4),('one3_zeroM2_triangle',36,21+3*4),('two3_zeroM2_fixed_edge',36,21+3*4),
 ('all4_M2_ge7_C3',14,4),('mixed_M2_ge3_C3',5,4)]
assert all(a>b for _,a,b in analytic)
out={'status':'PASS','old_domain_sizes_unchanged':[7,86,59,94],'rows_checked':len(checks),'rows':checks,
 'analytic_scalar_checks':[{'case':n,'candidates':a,'block_bound':b,'margin':a-b} for n,a,b in analytic],
 'low_occurrence_bound':str((6*F(3125,13122)+24*F(12005,131072))/4),'cpu_seconds':time.process_time()-start}
assert F(out['low_occurrence_bound'])<1
(HERE/'CHECK_MIXED21.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k!='rows'})
