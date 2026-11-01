"""Bounded global23-point pilot on3 complete degree spectra; no new layouts, no unproved paircap or Gamma4."""
from pathlib import Path
from math import comb
from fractions import Fraction
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();N=23;M=35;den=comb(23,11);pnum=comb(18,6)+comb(18,11);qnum=comb(14,6)+comb(14,7);weights=[comb(10+j,2+j)+comb(10+j,7) for j in range(5)];threshold=40*den-20*35*pnum;lower=-(-(5*(2*den-35*pnum))//(2*qnum));assert weights==[165,495,1287,3003,6435] and threshold==18811520 and lower==366
specs={'min7_max8':[7]*9+[8]*14,'rare_six_4_7_18eight':[6]*4+[7]+[8]*18,'rare_six_5_17eight_9':[6]*5+[8]*17+[9]}
def square(d,t):
 q,r=divmod(2*t,d);return (d-r)*q*q+r*(q+1)**2
def fivebox(s):
 q,r=divmod(s,5);return (s*s-(5-r)*q*q-r*(q+1)**2)//2
out=[]
for sid,ds in specs.items():
 assert len(ds)==23 and sum(ds)==175;W=sum(comb(d,2) for d in ds);D,D2=sorted(ds)[-1],sorted(ds)[-2];pv=[comb(d,2)-max(0,(4*d-22+2)//3) for d in ds];maxn=min(560,sum(pv));costs=sorted(d for d,p in zip(ds,pv) for _ in range(p));costpref=[0]
 for x in costs:costpref.append(costpref[-1]+x)
 margins=sorted(square(d,t)-square(d,t-1) for d,p in zip(ds,pv) for t in range(1,p+1));bpref=[0]
 for x in margins:bpref.append(bpref[-1]+x)
 # Everypair codegree<=D2; fixed total excess97. Pointwise convex row max gives a stronger global tau upper.
 maxrow=[]
 for d in ds:
  excess=4*d-22;cap=min(d,D2)-1;q,r=divmod(excess,cap);assert q+bool(r)<=22;maxrow.append(q*comb(cap,2)+comb(r,2))
 tauhi=sum(maxrow)//2
 # Four actual crosspairs share global tau; no cap4 assumption. Four-item exact dynamic programming.
 g={0:0}
 for _ in range(4):
  ng={}
  for c,v in g.items():
   for l in range(1,D2+1):cost=c+comb(l-1,2);ng[cost]=max(ng.get(cost,-1),v+l)
  g=ng
 g4=[max(v for c,v in g.items() if c<=t) for t in range(tauhi+1)]
 c2=min(33,(sum(sorted(ds)[-6:])-6)//2);c3generic=min(33,(sum(sorted(ds)[-4:])-4)//2)
 best=-1;witness=None;domain=0;failed=0;first=[];max_by_n1={};flagactive=0
 for n1 in range(lower,maxn+1):
  q,r=divmod(2*n1,32);oldP=q*fivebox(32)+fivebox(r);vertexP=(1024*q+r*r-bpref[n1])//2;shared=min(oldP,vertexP);flagactive+=int(vertexP<oldP)
  for t in range((W-n1)//4+1):
   lo=max(0,-((W-194+8*t-n1)//3),W+n1-1190-2*t);hi=min((2*tauhi-W+194-8*t+n1)//3,(W-n1-4*t)//3)
   if (lo-W+n1)%2:lo+=1
   for m in range(lo,hi+1,2):
    tau=(W-194+3*m+8*t-n1)//2;n2=(W-n1-3*m-4*t)//2;n0=595-(W+n1-m-2*t)//2;assert min(n0,n1,n2,m,t,tau)>=0 and tau<=tauhi
    domain+=1;lammax=max(l for l in range(1,D2+1) if comb(l-1,2)<=tau);cap4=min(D2*t,2*t+(D2-3)*tau,lammax*t);caps=[33*n0,35*n1-costpref[n1],c2*n2,min(c3generic,g4[tau])*m,cap4]
    tail=[sum(caps[i:]) for i in range(5)];deltas=[weights[0]]+[weights[i]-weights[i-1] for i in range(1,5)];v=4*qnum*n1+sum(dw*min(shared,a) for dw,a in zip(deltas,tail))
    if v>best:best=v;witness={'n':[n0,n1,n2,m,t],'tau':tau,'caps':caps,'oldP':oldP,'vertexP':vertexP,'P':shared,'value':v}
    if v>=threshold:
     failed+=1
     if len(first)<5:first.append({'n':[n0,n1,n2,m,t],'tau':tau,'value':v,'P':shared})
  assert time.process_time()-st<8
 out.append({'spectrum':sid,'degrees':ds,'W':W,'point_singleton_pair_capacities':pv,'n1_range':[lower,maxn],'tau_upper':tauhi,'C2_coefficient':c2,'generic_C3_coefficient':c3generic,'complete_moment_keys':domain,'strict':failed==0,'nonstrict_keys':failed,'maximum_value':best,'maximum_witness':witness,'first5_nonstrict':first,'n1_values_where_new_vertexP_improves_old':flagactive});print(sid,'KEYS',domain,'FAIL',failed,'MAX',best,'CPU',time.process_time()-st,flush=True)
r={'status':'COMPLETE_THREE_SPECTRA_GLOBAL_SCALAR_PILOT','scope':__doc__,'assumptions':['23points35simple5edges/paircover','Gamma minimumdegree2 from existing actualrepair theorem','actual degree spectrum exactlyspecified','no paircap beyond lambda<=secondhighestactualdegree','generic degree middlecaps, actual C1 capacity, global C4 matchingtau bound'],'parameters':{'denominator':den,'pnum':pnum,'qnum':qnum,'weights':weights,'threshold':threshold,'firstflip_n1_lower':lower,'Gamma2_singleton_box':32},'jobs':out,'cpu_seconds':time.process_time()-st};(P/'SCALAR_PILOT.json').write_text(json.dumps(r,indent=2)+'\n');print('TOTAL CPU',r['cpu_seconds'])
