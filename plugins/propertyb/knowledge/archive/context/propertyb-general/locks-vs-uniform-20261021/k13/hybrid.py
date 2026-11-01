"""One/two-lock selection conditional on the actual global minimum degree.
Uses the SAME certificate formulas and selection facts; no degree monotonicity.
Reuses the fully verified v105..856 prefix from M9544.json, then completes.
"""
import json,time,resource
from itertools import combinations_with_replacement
from scan import *
m=9544;t=time.monotonic();x=json.loads((OUT/f'M{m}.json').read_text());rows=x['rows'][:];fails=[];done=False
for v in x['candidate_v'][len(rows):]:
 if time.monotonic()-t>150:break
 c1=FastExact(K,m);c2=FastExact(K,m);d0=CEIL(v-1,KM1);hi=K*m//v;count=0;worst=(-1,None);branches=[];bad=None
 for d in range(d0,hi+1):
  z=c1.one(v,d)
  if z<S:
   branches.append({'mode':'one','d':d,'profiles':1,'worst_z':z});count+=1
   if z>worst[0]:worst=(z,{'mode':'one','d':d})
   continue
  sd=2*(v-1)-KM1*d
  if sd<=0:bad={'mode':'hybrid','v':v,'d':d,'one_z':z,'s_d':sd};break
  B=max(d,(K*m-v*d)//sd+d);worste=(-1,None)
  for e in range(d,B+1):
   z2=c2.two(v,d,e);count+=1
   if z2>worste[0]:worste=(z2,e)
   if z2>=S:bad={'mode':'hybrid','v':v,'d':d,'e':e,'two_z':z2};break
  if bad:break
  branches.append({'mode':'two','d':d,'s_d':sd,'e_min':d,'e_max':B,'profiles':B-d+1,'worst_z':worste[0],'worst_e':worste[1]})
  if worste[0]>worst[0]:worst=(worste[0],{'mode':'two','d':d,'e':worste[1]})
 if not bad:
  rows.append({'v':v,'mode':'hybrid','profiles':count,'worst_z':worst[0],'worst_profile':worst[1],'gap':S-worst[0],'d0':d0,'minimum_degree_upper':hi,'branches':branches})
 else:
  fails.append(bad);D=getD(m,v)
  if D is None:print('UNCOVERED',v,'no D',flush=True);break
  c3=FastExact(K,m);p3=list(combinations_with_replacement(range(d0,D+1),3));worst=(-1,None);count=0;bad3=None
  for ds in p3:
   for flag in (False,True):
    z=c3.three(v,ds,flag);count+=1
    if z>worst[0]:worst=(z,[ds,flag])
    if z>=S:bad3={'v':v,'mode':'three','ds':ds,'flag':flag,'z':z};break
   if bad3:break
  if bad3:fails.append(bad3);print('UNCOVERED',v,bad3,flush=True);break
  rows.append({'v':v,'mode':'three','profiles':count,'D':D,'d0':d0,'worst_z':worst[0],'worst_profile':worst[1],'gap':S-worst[0]})
 if v%10==0 or v==x['candidate_v'][-1]:print('PASS',v,rows[-1]['mode'],'profiles',sum(r['profiles'] for r in rows),'sec',round(time.monotonic()-t,3),flush=True)
x['rows']=rows;x['failures']=fails;x['complete']=len(rows)==len(x['candidate_v']);x['hybrid_seconds']=time.monotonic()-t;x['prefix_reused']='M9544.json fully verified rows';x['peakrss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
(OUT/'M9544-hybrid.json').write_text(json.dumps(x,indent=2));print('DONE',x['complete'],'rows',len(rows),'sec',x['hybrid_seconds'],flush=True)
