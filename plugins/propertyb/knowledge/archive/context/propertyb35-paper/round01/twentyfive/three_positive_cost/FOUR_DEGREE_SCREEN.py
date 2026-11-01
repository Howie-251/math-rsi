"""Complete bounded m=4 screen under repeat<=5; integer necessary blocker counts plus the actual blue-degree filter.
Stops at first nonstrict case or at110 seconds. Not an actual-H enumeration.
"""
from pathlib import Path
from itertools import product,combinations
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();non=[m for m in range(1,16) if m.bit_count()>=2];families=[]
def rec(j,left,occ,cell):
 if j==len(non):
  d=dict(zip(non,cell));d.update({1<<k:4-occ[k] for k in range(4)});cc=tuple(d.get(m,0) for m in range(1,16));A=[tuple(m for m in range(1,16) if m>>k&1 and cc[m-1]) for k in range(4)]
  if len(set(A))==4:families.append(cc)
  return
 m=non[j];w=m.bit_count()-1
 for z in range(min(left//w,*(4-occ[k] for k in range(4) if m>>k&1))+1):rec(j+1,left-w*z,[x+z*int(m>>k&1) for k,x in enumerate(occ)],cell+[z])
rec(0,5,[0]*4,[])
def check(A,F):
 raw={0}
 for aa in A:raw={z|v for z in raw for v in aa if not v&F}
 mins=[];T={k:[] for k in range(1,5)}
 for k in range(1,5):
  candidates=[z for z in raw if z.bit_count()==k and not any(w&z==w for w in mins)]
  T[k]=candidates;mins.extend(candidates)
 sizes=[len(T[k]) for k in range(1,5)];q=F.bit_count()
 free_union=0
 for aa in A:
  for v in aa:
   if not v&F:free_union|=v
 positive_occ=sum(sum(not bool(v&F) for v in aa) for aa in A)
 degree_capacity=7*free_union.bit_count()+7-positive_occ
 if T[1]:return dict(strict=True,candidates=sizes,reason='singleton')
 C23=Counter();C24=Counter();C34=Counter()
 for k in [3,4]:
  for z in T[k]:
   vv=[1<<v for v in range(z.bit_length()) if z>>v&1]
   for a,b in combinations(vv,2):(C23 if k==3 else C24)[a|b]+=1
   if k==4:
    for a,b,c in combinations(vv,3):C34[a|b|c]+=1
 K23=max(C23.values(),default=0);K24=max(C24.values(),default=0);K34=max(C34.values(),default=0);p0=len(T[2]);gaps=[];remaining=[]
 for p in range(p0,min((24-9*q)//4,(8-3*q)//2)+1):
  lower3=max(0,len(T[3])-(p-p0)*K23)
  for t in range(lower3,min(24-9*q-4*p,8-3*q-2*p)+1):
   required4=max(0,len(T[4])-(p-p0)*K24-(t-lower3)*K34)
   available4=28-q-p-t;gap=required4-available4;gaps.append(gap)
   negative_incidence=2*p+3*t+4*required4
   if gap<=0 and negative_incidence<=degree_capacity:remaining.append([p,t,required4,negative_incidence])
 return dict(strict=not remaining,candidates=sizes,K=[K23,K24,K34],minimum_gap=min(gaps,default=None),degree_capacity=degree_capacity,free_points=free_union.bit_count(),positive_free_occ=positive_occ,remaining=remaining)
records=[];survivor=None;complete=True;checkpoint=None
for family_id,cc in enumerate(families):
 cells=[];v=0;A=[[] for _ in range(4)]
 for m,sz in enumerate(cc,1):
  vv=[1<<i for i in range(v,v+sz)];v+=sz;cells.append(vv)
  for k in range(4):
   if m>>k&1:A[k].extend(vv)
 nonzero=[j for j,z in enumerate(cells) if z]
 Fs=[(0,[])]+[(cells[j][0],[j+1]) for j in nonzero]+[(cells[j][0]|cells[k][0],[j+1,k+1]) for j,k in combinations(nonzero,2)]+[(cells[j][0]|cells[j][1],[j+1,j+1]) for j in nonzero if len(cells[j])>=2]
 for F,Fcells in Fs:
  r=check(A,F);r.update(family_id=family_id,Fcells=Fcells);records.append(r)
  if not r['strict']:
   survivor=dict(cells=cc,A=[[x.bit_length()-1 for x in aa] for aa in A],F=[i for i in range(v) if F>>i&1],**r);break
  if checkpoint is None and time.perf_counter()-st>=10:checkpoint=dict(states=len(records),families=family_id+1,elapsed_seconds=time.perf_counter()-st);print('10sec_profile',json.dumps(checkpoint),flush=True)
  if time.perf_counter()-st>110:complete=False;break
 if survivor or not complete:break
summary=dict(scope=__doc__,families=len(families),states=len(records),strict=sum(r['strict'] for r in records),complete=complete and survivor is None,first_nonstrict=survivor,ten_second_checkpoint=checkpoint,elapsed_seconds=time.perf_counter()-st,by_q=dict(Counter(len(r['Fcells']) for r in records)))
(P/'FOUR_DEGREE_SCREEN.json').write_text(json.dumps(dict(summary=summary,families=families,records=records),separators=(',',':'))+'\n');print(json.dumps(summary,indent=2))
