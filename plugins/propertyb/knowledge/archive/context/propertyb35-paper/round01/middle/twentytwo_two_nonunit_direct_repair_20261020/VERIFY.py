#!/usr/bin/env python3
from itertools import combinations_with_replacement
from math import comb
from fractions import Fraction as F
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;start=time.process_time();saved=json.loads(P.joinpath('PROFILE.json').read_text())
def C(n,k):return comb(n,k) if 0<=k<=n else 0
kinds=['P','D','B2','B3','B4'];master={}
def risk(k,r):
 if k=='P':return F(0)
 if k=='D':return F(C(r,5)+C(17-r,5),C(17,5))
 j=int(k[1:]);return F(C(17-r,5-j),C(17,5-j))
for pair in combinations_with_replacement(kinds,2):
 caps=[]
 for r in range(9,18):
  alpha=F(C(r,4),C(17,4));beta=F(C(17-r,4),C(17,4));delta=F(C(r,8),C(17,8))
  good=[c for c in range(33) if c*alpha+(32-c)*beta-max(c-1,0)*delta+sum((risk(k,r) for k in pair),F())<1]
  assert good==list(range(len(good)));caps.append(max(good,default=-1))
 best=max(caps);assert max(caps[1:4])==best # r10,11,12 suffice for same thresholds.
 master[pair]=dict(k=best+1,r_caps=caps)
def category(T,v):return 'D' if not T else ('P' if T>>v&1 else 'B'+str(T.bit_count()))
classes={}
for row in saved['cases']:
 T,U=row['traces'];key=(min(T.bit_count(),U.bit_count()),max(T.bit_count(),U.bit_count()),(T&U).bit_count());assert key not in classes;classes[key]=row
 for v in range(5):
  pair=tuple(sorted((category(T,v),category(U,v)),key=kinds.index));m=master[pair]
  assert m['k']==row['k'][v]
  assert m['r_caps']==[r['max_safe_c'] for r in row['per_point_r_caps'][v]]
counts={key:0 for key in classes};masks=[m for m in range(32) if m.bit_count() in(0,2,3,4)]
for T,U in combinations_with_replacement(masks,2):
 key=(min(T.bit_count(),U.bit_count()),max(T.bit_count(),U.bit_count()),(T&U).bit_count());assert key in classes;counts[key]+=1
assert len(classes)==19 and sum(counts.values())==351
for key,num in counts.items():assert num==classes[key]['orbit_size']
# Independently enumerate local non-strict degree compositions for the five residual types only.
# Total residual surplus over k is at most one, so no large attachment scan is needed.
res=[]
for row in saved['cases']:
 if sum(row['k'])>32:continue
 gap=32-sum(row['k']);assert gap in(0,1)
 vectors=[row['k'][:]] if not gap else [[a+(i==v) for i,a in enumerate(row['k'])] for v in range(5)]
 degrees=[[1+a+m for a,m in zip(v,row['multiplicities'])] for v in vectors]
 res.append(dict(traces=row['traces'],sizes=row['sizes'],intersection=row['intersection'],k=row['k'],degree_vectors=degrees))
out=dict(status='PASS',scope='independent hypergeometric probability expressions and complete size/intersection classification; no original H enumeration',trace_pairs=351,orbits=19,master_risk_table=[dict(kinds=list(p),**v) for p,v in master.items()],residual_degree_vectors=res,cpu_seconds=time.process_time()-start)
P.joinpath('VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in('master_risk_table','residual_degree_vectors')}))
