"""Second orbit exact2820 domain, integer charging and1967 strict replays."""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
from collections import Counter
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[5];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows,injection_probability
d=json.loads((P/'TABLES.json').read_text());lp=json.loads((P/'LP_RESULT.json').read_text())
mu=d['source_counts'];T=tuple(m for m,n in enumerate(mu) if n);assert T==tuple(d['T'])
def weak(n,k):
 if k==1:yield(n,);return
 for a in range(n+1):
  for rest in weak(n-a,k-1):yield(a,)+rest
independent={}
for r in (7,9):
 for c in weak(r,len(T)):
  if any(n>mu[m] for m,n in zip(T,c)):continue
  row=tuple(sum(n for m,n in zip(T,c) if m>>i&1) for i in range(4))
  if any(not 1<=n<=4 for n in row):continue
  independent[(r,c)]=row
saved={(z['r'],tuple(z['c'])):tuple(z['row']) for z in d['views']}
assert saved==independent and len(saved)==2820
y=lp['dual_integer'];assert len(y)==11
assert sum(a*b for a,b in zip(d['target_columns']+[9,8],y))==-24
negative=[]
for z in d['views']:
 c=z['c'];phi=sum(a*b for a,b in zip(c,y[:9]))+y[9 if z['r']==7 else 10]
 score=2*c[0]+c[1]+c[2]+3*c[3]+3*c[8]
 assert phi==2*score-24
 if not z['strict']:assert phi>=0
 if score<12:assert z['strict'];negative.append(z)
assert len(negative)==1967
assert sum(w*a for w,a in zip((2,1,1,3,0,0,0,0,3),d['target_columns']))==192<204
cert=[];maximum=Fraction()
for i,z in enumerate(negative):
 ns={}
 for m,c in zip(T,z['c']):ns[2*m]=mu[m]-c;ns[2*m+1]=c
 assert ns=={int(m):n for m,n in z['counts'].items()}
 masks=[m for m,n in ns.items() for _ in range(n)];assert len(masks)==35
 types=[frozenset(j+1 for j in range(5) if m>>j&1) for m in masks]
 pos=tuple(z['positions']);ir=independent_rows(21,pos,types);pure=ns.get(1,0);quota=max(0,(4*pure-16+2)//3)
 assert quota==z['pure_quota']
 total=Fraction();rows=[]
 for rr in ir:
  W=injection_probability(16,rr['a'],rr['b'],4,4,False) if rr['k']==pos[0] else Fraction()
  loss=2*quota*W;C=rr['C']-loss;assert C>=0
  minimum=min(rr['A'],rr['B'],C);total+=minimum
  rows.append(dict(k=rr['k'],A=str(rr['A']),B=str(rr['B']),Czero=str(rr['C']),loss=str(loss),Cnew=str(C),minimum=str(minimum)))
 assert total==Fraction(z['bound'])<1;maximum=max(maximum,total)
 cert.append(dict(view_index=z['index'],r=z['r'],c=z['c'],score=2*z['c'][0]+z['c'][1]+z['c'][2]+3*z['c'][3]+3*z['c'][8],positions=pos,bound=str(total),pure_unordered_quota=quota,expanded35_masks=masks,rows=rows))
 if i==99:print('100_REPLAY_CPU',time.process_time()-st,flush=True)
 assert time.process_time()-st<16,'16CPU independent replay cutoff'
out=dict(status='PASS_COMPLETE_ACTUAL_DOMAIN_AND_EXACT_CHARGING_CLOSURE',scope=__doc__,complete_views=2820,degree_counts=dict(Counter(r for r,c in independent)),complete_clean7=448,integer_dual=y,dual_actual_rhs=-24,failed_columns_nonnegative=113,charging_coefficients=[2,1,1,3,0,0,0,0,3],charging_actual_sum=192,charging_if_all_failed_minimum=204,low_charge_strict_views=1967,low_charge_by_degree=dict(Counter(z['r'] for z in negative)),strict_maximum=str(maximum),replayed_rows=1967*21,original_indices_per_case=35,ordered_distinct_pairs_per_case=1190,cases=cert,cpu_seconds=time.process_time()-st)
(P/'VERIFY_DUAL.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='cases'})
