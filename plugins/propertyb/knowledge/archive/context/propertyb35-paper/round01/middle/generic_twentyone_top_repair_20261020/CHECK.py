#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,time
start=time.process_time();D=comb(15,8)
p4R=F(comb(8,4),comb(15,4));p4B=F(comb(7,4),comb(15,4))
p5=F(comb(8,5)+comb(7,5),comb(15,5));p3R=F(comb(8,3),comb(15,3));p3B=F(comb(7,3),comb(15,3))
assert (p4R,p4B,p5,p3R,p3B)==(F(2,39),F(1,39),F(1,39),F(8,65),F(1,13))
original=8*p4R+16*p4B+5*p5;assert original==F(37,39)<1
assert F(8*comb(8,4)+16*comb(7,4),comb(15,4))==F(1120,1365)
assert 5*p5==F(5,39)
# Purely scalar identity for29 non-top original edges: b_i single traces, others empty.
for m in range(30):
 for a in range(m//3+1):
  risk=a*p4R+(m-a)*p4B+(29-m)*p5
  assert risk==F(29+a,39)<=F(38,39)<1
rows=[]
for r in range(6):
 k=min(r,2);a=8-k;blue=17-2*r+k;empty=4+r
 risk=a*p4R+blue*p4B+empty*p5+(r-k)*p3B
 assert risk==F(37+2*r-4*k,39)
 row=dict(pair_star_size=r,center_blue_risk=str(risk))
 if r<5:assert risk<1
 else:
  alternative=3*p4R+12*p4B+9*p5+p3R
  assert alternative==F(53,65)<1
  row['center_red_risk']=str(alternative)
 rows.append(row)
out=dict(status='PASS',scope='exact probability identities and six derived scalar star cases only; no H or old five-top domain enumeration',sample_count=D,
weights={k:str(v) for k,v in dict(positiveQ_single=p4R,blueQ_single=p4B,emptyQ=p5,redQ_pair=p3R,blueQ_pair=p3B).items()},
root_full_top_bound=str(original),root_success_samples=int(D*(1-original)),degree_free_full_top_bound='38/39',degree_free_success_samples=int(D/39),delta8_full_top_cases=rows,cpu_seconds=time.process_time()-start)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
