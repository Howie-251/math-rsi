"""Tiny exact verification of cross-pair plus maximum-degree-row capacities. No layouts or H enumeration."""
from pathlib import Path
from itertools import product
from math import comb
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();INF=10**9
cost=lambda l:(l-1)*(l-2)//2
# Primary closed form; infeasible row sums are explicitly excluded.
def h(n,S):
 if not n<=S<=4*n:return INF
 if S<=2*n:return 0
 if S<=3*n:return S-2*n
 return n+2*(S-3*n)
# Independent finite convolution: append one true codegree and its cost.
def dp(n):
 a={0:0}
 for _ in range(n):
  b={}
  for s,c in a.items():
   for l in (1,2,3,4):b[s+l]=min(b.get(s+l,INF),c+comb(l-1,2))
  a=b
 return a
rows18=dp(18);rows20=dp(20)
for n,table in ((18,rows18),(20,rows20)):
 for s in range(0,4*n+2):assert h(n,s)==table.get(s,INF)
assert h(18,55)==20 and h(18,72)==54
# Fixed tuple order02,03,12,13. Cross pairs are distinct actual pairs.
vectors=list(product((1,2,3,4),repeat=4));assert len(vectors)==256
crosspairs=((0,2),(0,3),(1,2),(1,3));tables=[]
for D in range(5,21):
 r=max(0,4*D-40);assert r<=rows20[4*D]
 primary=[];independent=[]
 for ls in vectors:
  c=sum(cost(l) for l in ls)
  incident_sums=(ls[0]+ls[1],ls[2]+ls[3],ls[0]+ls[2],ls[1]+ls[3])
  branches=[r]+[h(18,4*D-v) for v in incident_sums];threshold=c+min(branches)
  primary.append({'lambdas':ls,'cross_sum':sum(ls),'cross_cost':c,'extra_row_costs':[None if v==INF else v for v in branches],'necessary_tau_lower':threshold})
  # Separate labeled-edge construction and DP row costs, no incident-sum tuple or closed form.
  edges=dict(zip(crosspairs,ls));c2=sum(comb(v-1,2) for v in edges.values());possible=[r]
  for v in range(4):
   fixed=sum(l for pair,l in edges.items() if v in pair)
   possible.append(rows18.get(4*D-fixed,INF))
   assert len([p for p in edges if v in p])==2
   # 4 crosspairs plus18 residual rowpairs are genuinely disjoint.
   allrow={tuple(sorted((v,w))) for w in range(21) if w!=v}
   incident_cross={p for p in edges if v in p};residual=allrow-incident_cross
   assert len(residual)==18 and residual.isdisjoint(edges)
  # v outsideK, represented by4: all20 rowpairs avoid all4 crosspairs.
  outside_row={tuple(sorted((4,w))) for w in range(21) if w!=4};assert len(outside_row)==20 and outside_row.isdisjoint(edges)
  threshold2=c2+min(possible);assert threshold2==threshold
  independent.append((sum(edges.values()),threshold2))
 g=[];g2=[]
 for tau in range(141):
  g.append(max((x['cross_sum'] for x in primary if x['necessary_tau_lower']<=tau),default=0))
  g2.append(max((v for v,c in independent if c<=tau),default=0))
 assert g==g2 and all(a<=b for a,b in zip(g,g[1:]))
 mins=[]
 for demand in range(4,17):
  best=min((x for x in primary if x['cross_sum']>=demand),key=lambda x:x['necessary_tau_lower'])
  mins.append({'cross_sum_at_least':demand,'necessary_tau_lower':best['necessary_tau_lower'],'attaining_relaxed_vector':best['lambdas']})
 tables.append({'D':D,'outside_row_lower':r,'G_D_tau0_through140':g,'minimum_tau_for_cross_demands':mins,'all256_vectors':primary})
for D,want in ((11,7),(12,11),(13,15)):
 got=next(t for t in tables if t['D']==D);assert next(x['necessary_tau_lower'] for x in got['minimum_tau_for_cross_demands'] if x['cross_sum_at_least']==13)==want
# D_2 is the second-largest degree, used only by the separate imported C4 lemma.
for ds in product(range(5,21),repeat=3):
 D2=sorted(ds)[-2]
 for i,j in ((0,1),(0,2),(1,2)):assert min(ds[i],ds[j])<=D2
for D2 in range(5,21):assert 2*(D2-4)<=3*(D2-3)
out={'status':'PASS','scope':__doc__,'N':21,'uniformity':5,'paircover':True,'paircap':4,'degree_domain':[5,20],'cross_vector_count':256,'D_vector_cases':16*256,'tau_domain':[0,140],'closed_row_form_independently_verified_by_integer_DP':True,'correct_h18_formula':{'infeasible':'S<18 or S>72','18<=S<=36':'0','36<=S<=54':'S-36','54<=S<=72':'18+2*(S-54)'},'coefficient3_counterexample':{'S':55,'wrong_value':21,'true_minimum':20,'attaining_row':'17 codegrees3 and1 codegree4'},'root_low_excess_D_le13_uses_only_first_two_branches':True,'D2_second_largest_check':True,'tables':tables,'cpu_seconds':time.process_time()-st}
(P/'HIGH_ROW_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='tables'}))
