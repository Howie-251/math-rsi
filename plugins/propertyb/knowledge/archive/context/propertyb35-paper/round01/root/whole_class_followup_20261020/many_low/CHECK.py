"""Count-only common low-star deficiency gate. No H/layout search."""
from collections import Counter
from itertools import product
from math import comb
from pathlib import Path
from time import process_time
import json
start=process_time()
probs={(1,1,1,1,1):180,(2,1,1,1):440,(2,2,1):832,
       (3,1,1):1136,(3,2):1792,(4,1):2048}
occ=[]
for t in product(range(5),repeat=6):
 if sum(t)==5:occ.append((t,probs[tuple(sorted((x for x in t if x),reverse=True))],sum(comb(x,2) for x in t)))
assert len(occ)==246

def local(r):
 out=[]
 for u1 in range(7):
  for u2 in range(7-u1):
   for u3 in range(7-u1-u2):
    u4=6-u1-u2-u3;u=(0,u1,u2,u3,u4)
    if 3*u1+2*u2+u3!=19-r:continue
    k=[4]*u1+[3]*u2+[2]*u3+[1]*u4
    costs=[-1]*5;phi=[-1]*5;possible32=False
    for t,c,w in occ:
     if any(x>=2 and x>cap for x,cap in zip(t,k)):continue
     lmax=sum(x==1 and cap<4 for x,cap in zip(t,k))
     for j in range(min(lmax,4)+1):costs[j]=max(costs[j],c);phi[j]=max(phi[j],w)
     if c==1792:possible32=True
    out.append({'u':u,'high_sizes':k,'costs':costs,'phi':phi,'T':sum(comb(x,2) for x in k),'possible32':possible32})
 return out

def bad_allocation(r,n,bad):
 # Exact integer counts of r stars, preserving all four incidence totals.
 # u1/u2 suffice; the sum and deficiency equations recover u3/u4 totals.
 A=n[1];B=2*n[2];width=B+1;states=[1];moves=[]
 for x in bad:
  u=x['u'];a=u[1];b=u[2]
  mask=sum(((1<<(B-b+1))-1)<<(v*width) for v in range(A-a+1))
  moves.append((a*width+b,mask,x))
 for _ in range(r):
  old=states[-1];new=0
  for shift,mask,_ in moves:new|=(old&mask)<<shift
  states.append(new)
 target=A*width+B
 if not (states[-1]>>target&1):return None
 x=A;y=B;chosen=Counter()
 for level in range(r,0,-1):
  for shift,mask,t in moves:
   a=t['u'][1];b=t['u'][2]
   if x>=a and y>=b and states[level-1]>>((x-a)*width+y-b)&1:
    chosen[tuple(t['u'])]+=1;x-=a;y-=b;break
  else:raise AssertionError('backtrack')
 assert x==y==0
 assert all(sum(c*u[j] for u,c in chosen.items())==j*n[j] for j in range(1,5))
 return [{'u':u,'count':c} for u,c in sorted(chosen.items())]

allcases=[];summary=[]
for r in range(3,17):
 types=local(r);total=closed=0;remaining=[]
 for n4 in range(36):
  for n3 in range(36-n4):
   n2=comb(r,2)-6*n4-3*n3;n1=6*r-4*n4-3*n3-2*n2;n0=35-n1-n2-n3-n4
   if min(n0,n1,n2)<0:continue
   n=(n0,n1,n2,n3,n4);total+=1;bad=[];evaluated=[]
   rem=r;amax=0
   for j in (1,2,3):take=min(n[j],rem//j);amax+=take;rem-=j*take
   for x in types:
    u=x['u']
    if any(u[j]>n[j] for j in range(1,5)):continue
    if any(n[j]>u[j] and x['costs'][j]<0 for j in range(5)):continue
    Cdirect=sum((n[j]-u[j])*x['costs'][j] for j in range(5))
    Wdirect=sum((n[j]-u[j])*x['phi'][j] for j in range(5))
    Wpacking=x['T']*(amax-1)+n0*x['phi'][0]
    Wcap=min(50,Wdirect,Wpacking)
    Cfine=5220+326*Wcap+308*n0*x['possible32']
    Ccap=min(Cdirect,Cfine)
    record={'u':u,'Wcap':Wcap,'Ccap':Ccap,'Cdirect':Cdirect,'Cfine':Cfine}
    evaluated.append(record)
    if Wcap>25 and Ccap>=15360:bad.append(record)
   witness=bad_allocation(r,n,bad)
   passed=witness is None
   closed+=passed
   case={'r':r,'n':n,'certified_by_common_gate':passed,'Amax':amax,'local_types':evaluated}
   if not passed:
    case['integer_bad_star_allocation']=witness;remaining.append(case)
   allcases.append(case)
 summary.append({'r':r,'necessary_count_vectors':total,'all_count_vectors_certified':closed==total,
                 'certified_count_vectors':closed,'remaining_count_vectors':total-closed,
                 'first_remaining':remaining[0] if remaining else None})
res={'status':'COMPLETE_COUNT_ONLY_DIAGNOSTIC','scope':'r3..16, no all-low edge, global n0..4 and integer local deficiency star counts; not H realizability',
     'occupancy_vectors_per_high_size_type':246,'cpu_seconds':process_time()-start,'summary':summary,'cases':allcases}
Path(__file__).with_name('RESULT.json').write_text(json.dumps(res,indent=2)+'\n')
for x in summary:print(x['r'],x['necessary_count_vectors'],x['certified_count_vectors'],x['remaining_count_vectors'], None if x['first_remaining'] is None else x['first_remaining']['n'])
print('CPU',res['cpu_seconds'])
