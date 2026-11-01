"""Exact4096 six-pair capacities, finite kernel-family shape checks, and last2 scalar keys. No probability tables or layouts."""
from pathlib import Path
from itertools import product,combinations
from math import comb
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();edges=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3));partitions=((0,5),(1,4),(2,3));caps={8:(-1,None),10:(-1,None)};rows=[]
for ls in product(range(1,5),repeat=6):
 cost=sum(comb(l-1,2) for l in ls);L=sum(ls);eligible=[(i,j) for i,j in partitions if L-ls[i]-ls[j]>=13];matching=sum(min(ls[i],ls[j]) for i,j in eligible)
 assert cost>=2*L-30
 if cost<=8:assert L<=19 and len(eligible)<=2 and matching<=6
 if cost<=10:assert L<=20 and matching<=9
 for cap in (8,10):
  if cost<=cap and matching>caps[cap][0]:caps[cap]=(matching,{'lambdas':ls,'cost':cost,'sum':L,'eligible_side_pair_edge_indices':eligible})
 rows.append({'lambdas':ls,'cost':cost,'sum':L,'matching_bound':matching})
assert caps[8][0]==6 and caps[10][0]==9
triangle=sorted({sum(z) for z in product((0,1,3),repeat=3)});assert triangle==[0,1,2,3,4,5,6,7,9]
three=[c for c in triangle if c+3*max(1,8-c)<=10];four=[c for c in triangle if c+4*max(1,8-c)<=10];assert three==[7] and four==[]
# A zero-cost outside vertex contributes at most2 to each of its incident pairs.
for tri in product(range(1,5),repeat=3):
 for attach in product((1,2),repeat=3):
  ll=(tri[0],tri[1],attach[0],tri[2],attach[1],attach[2]);L=sum(ll)
  assert max(L-ll[i]-ll[j] for i,j in partitions)<=12
# Up to4 four-sets with pairwise intersection3 lie on at most7 points.
ks=[sum(1<<i for i in a) for a in combinations(range(7),4)];triple_cases=quad_cases=0
for A,B,C in combinations(ks,3):
 if min((A&B).bit_count(),(A&C).bit_count(),(B&C).bit_count())!=3:continue
 common=A&B&C;union=A|B|C;triple_cases+=1
 if common.bit_count()!=3:
  assert common.bit_count()==2 and union.bit_count()==5
  multiplicities=[]
  for e in combinations(range(7),2):
   mask=(1<<e[0])|(1<<e[1]);m=sum((K&mask)==mask for K in (A,B,C));multiplicities.append((mask,m))
  assert sum(m==3 for _,m in multiplicities)==1
  assert all(m<=2 or mask==common for mask,m in multiplicities)
for fam in combinations(ks,4):
 if not all((A&B).bit_count()==3 for A,B in combinations(fam,2)):continue
 if not all((A&B&C).bit_count()==3 for A,B,C in combinations(fam,3)):continue
 common=fam[0]&fam[1]&fam[2]&fam[3];assert common.bit_count()==3;quad_cases+=1
# Bind cost>=8 to every still-implicated actual failure inventory of the last2 keys.
ind=json.loads((P/'independent/RESULT.json').read_text());assert ind['status']=='PASS_COMPLETE_SCOPED_INDEPENDENT_VERIFICATION'
typed=json.loads((P/'IMPLICATED_THREE_KEYS.json').read_text());local=[]
for j in typed['jobs']:
 if (j['spectrum_id'],j['key']['tau']) not in ((90,10),(95,9)):continue
 costs=[z['K6_cost'] for z in j['implicated_tails']];assert costs and min(costs)>=8
 local.append({'spectrum_id':j['spectrum_id'],'tau':j['key']['tau'],'implicated_inventories':len(costs),'minimum_K6_cost':min(costs)})
assert len(local)==2
old=json.loads((P/'LOW_TAU_KEY_REFINEMENT.json').read_text());last=[]
for z in old['remaining_keys']:
 cc=z['caps'].copy();cc[3]=min(cc[3],12*z['n'][3]+18);shared=z['newP'];v=6864*z['n'][1]+sum(dw*min(shared,sum(cc[i:])) for i,dw in enumerate((36,84,210,462,924)));assert v<5445440
 last.append({'spectrum_id':z['spectrum_id'],'n':z['n'],'tau':z['tau'],'newP':shared,'new_caps':cc,'new_twice_L':v,'margin':5445440-v})
out={'status':'PASS_TINY_BAD_KERNEL_CAPACITY_AND_LAST2_VALUES','scope':__doc__,'six_pair_vectors':4096,'max_matching_capacity_at_cost_le8':caps[8],'max_matching_capacity_at_cost_le10':caps[10],'all4096_values':rows,'triangle_cost_values':triangle,'possible_triangle_cost_with3_kernels_tau_le10':three,'possible_triangle_cost_with4_kernels_tau_le10':four,'three_kernel_shape_cases_on7_vertices':triple_cases,'four_kernel_star_shape_cases_on7_vertices':quad_cases,'last2_local_inventory_binding':local,'bad_outer_pair_bound':18,'C3_bound':'12*n3+18 (also retain13*n3)','last2':last,'cpu_seconds':time.process_time()-st};(P/'BAD_KERNEL_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='all4096_values'}))
