"""Bounded k14 diagnostic. Endpoint screens are NOT full certificates."""
import sys,time,json,resource,argparse
from pathlib import Path
SRC=Path('context/collaborator-small-k-20261019/m10-m11').resolve()
sys.path.insert(0,str(SRC))
from propertyB_k10_k11_verified import FastExact,CEIL,S,C
from propertyB_k10_k11_certified import FixedCertificate
OUT=Path(__file__).resolve().parent
K=14; A=13

def domain(m):
 return [v for v in range(27,K*m+1) if v*CEIL(v-1,A)<=K*m and m*(C(v//2,K)+C(v-v//2,K))>=C(v,K)]

def dinfo(m,v):
 # x=D+1. F(x)=26(v*x-14m)-(13x-v+2)^2 is concave,
 # vertex x=2(v-1)/13. Restrict to Z>0 and the COMPLETE D domain.
 lo=max(CEIL(v-1,A)+1,K*m//v+1);hi=m+1
 def f(x):return 2*A*(v*x-K*m)-(A*x-v+2)**2
 candidates=sorted({lo,hi,max(lo,min(hi,2*(v-1)//A)),max(lo,min(hi,CEIL(2*(v-1),A)))})
 xmax=max(candidates,key=f)
 r={'D_min':CEIL(v-1,A),'D_max':m,'positive_Z_D_min':lo-1,'max_F':f(xmax),'max_F_D':xmax-1,'max_F_Z':v*xmax-K*m}
 if f(xmax)<=0:r['first_D']=None;return r
 left=lo;right=xmax
 while left<right:
  mid=(left+right)//2
  if f(mid)>0:right=mid
  else:left=mid+1
 assert f(left)>0 and (left==lo or f(left-1)<=0)
 r['first_D']=left-1;return r

def main():
 ap=argparse.ArgumentParser();ap.add_argument('M',type=int);ap.add_argument('--seconds',type=float,default=75);args=ap.parse_args()
 m=args.M;t=time.monotonic();cpu=time.process_time();vs=domain(m)
 out={'k':K,'M':m,'S':S,'candidate_v':vs,'screen_only':True,'rows':[],'screen_all_v':False}
 print('DOMAIN',m,vs[0],vs[-1],len(vs),flush=True)
 for v in vs:
  if time.process_time()-cpu>args.seconds:out['timeout_v']=v;break
  c=FastExact(K,m);z0=c.unlocked(v)
  if z0<S:out['rows'].append({'v':v,'screen_mode':'none','z':z0});continue
  d0=CEIL(v-1,A);dh=K*m//v
  # Necessary tests for a minimum-degree-conditional one/two strategy.
  # No monotonicity is presumed: passing these endpoints is only a screen.
  ds=sorted({d0,dh,(d0+dh)//2,max(d0,min(dh,2*(v-1)//A))})
  c1=FastExact(K,m);c2=FastExact(K,m);fail=None;checks=[]
  for d in ds:
   z1=c1.one(v,d)
   if z1<S:checks.append({'d':d,'mode':'one','z':z1});continue
   sd=2*(v-1)-A*d
   if sd<=0:fail={'d':d,'one_z':z1,'s_d':sd};break
   B_raw=max(d,(K*m-v*d)//sd+d)
   assert v*d+sd*(B_raw+1-d)>K*m
   # Intersection exactly one also forces d+e-1<=M. Discard no actual type.
   B=min(B_raw,m-d+1)
   tests=[]
   for e in sorted({d,B}):
    z2=c2.two(v,d,e);tests.append({'e':e,'z':z2})
    if z2>=S:fail={'d':d,'e':e,'one_z':z1,'two_z':z2,'s_d':sd,'B':B,'B_raw':B_raw};break
   checks.append({'d':d,'mode':'two-screen','s_d':sd,'B':B,'B_raw':B_raw,'tests':tests})
   if fail:break
  if not fail:out['rows'].append({'v':v,'screen_mode':'hybrid','d0':d0,'dhi':dh,'checks':checks});continue
  di=dinfo(m,v);fail.update({'v':v,'d0':d0,'dhi':dh,'none_z':z0,'D_search':di})
  if di['first_D'] is not None:
   D=di['first_D'];c3=FastExact(K,m);tt=[]
   for deg in sorted({(d0,d0,d0),(D,D,D)}):
    for flag in (False,True):tt.append({'degrees':deg,'triple':flag,'z':c3.three(v,deg,flag)})
   fail['three_endpoint_tests']=tt
   if all(q['z']<S for q in tt):out['rows'].append({'v':v,'screen_mode':'three','D':D,'tests':tt});continue
  # Replay the concrete failed one/two types through arbitrary integers.
  scalar=FixedCertificate(K,m);rep={'none':scalar.unlocked(v),'one':scalar.one(v,fail['d'])}
  assert rep['none']==z0 and rep['one']==fail['one_z']
  if 'e' in fail:rep['two']=scalar.two(v,fail['d'],fail['e']);assert rep['two']==fail['two_z']
  if 'three_endpoint_tests' in fail:
   rep['three']=[]
   for q in fail['three_endpoint_tests']:
    zz=scalar.three(v,q['degrees'],q['triple']);assert zz==q['z'];rep['three'].append(zz)
  # Different brute-force calculation of COMPLETE D-domain maximum and first D.
  brute=[(2*A*((D+1)*v-K*m)-(A*(D+1)-v+2)**2,D,(D+1)*v-K*m) for D in range(d0,m+1) if (D+1)*v>K*m]
  best=max(brute);first=next((q[1] for q in brute if q[0]>0),None)
  assert best[0]==di['max_F'] and first==di['first_D']
  rep['brute_full_D_max']=best;rep['brute_first_D']=first;fail['scalar_replay']=rep
  out['failure']=fail;print('UNCOVERED',v,json.dumps(fail),flush=True);break
 else:out['screen_all_v']=True
 out['wall_seconds']=time.monotonic()-t;out['cpu_seconds']=time.process_time()-cpu;out['peakrss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 (OUT/f'M{m}-screen.json').write_text(json.dumps(out,indent=2));print('DONE',out['wall_seconds'],out['cpu_seconds'],flush=True)
if __name__=='__main__':main()
