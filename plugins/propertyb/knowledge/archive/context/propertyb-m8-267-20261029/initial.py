from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from math import comb
import importlib.util,json,time,signal
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
spec=importlib.util.spec_from_file_location('existing_k8',ROOT/'propertyB_small_k/propertyB_m8_certificate_v2.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
START=time.process_time()
def timeout(s,f):raise TimeoutError('60 CPU-second budget')
signal.signal(signal.SIGPROF,timeout);signal.setitimer(signal.ITIMER_PROF,60);signal.alarm(90)
cal=m.Calculator(8,266)

def main():
 balanced=[]
 for v in range(15,121):
  u=Q(266*(m.C(v//2,8)+m.C(v-v//2,8)),m.C(v,8));balanced.append(dict(v=v,U=str(u),strict=u<1))
 domain=[v for v in range(15,123) if v*m.CEIL(v-1,7)<=2128 and Q(266*(m.C(v//2,8)+m.C(v-v//2,8)),m.C(v,8))>=1]
 print('DOMAIN',min(domain),max(domain),flush=True)
 rows=[];sels=[];partner=[]
 for v in domain:
  if v<=84:rows.append(dict(v=v,kind='zero',U=str(cal.unlocked(v))))
  elif v<=94:
   for d in range(m.CEIL(v-1,7),2128//v+1):rows.append(dict(v=v,kind='one',degrees=[d],positions=[v//2],ell={0:266-d,1:d},U=str(cal.one(v,d))))
  elif v<=107:
   for d in range(m.CEIL(v-1,7),2128//v+1):
    n=2*(v-1)-7*d;assert n>0
    upper=d+(2128-v*d)//n
    partner.append(dict(v=v,d=d,n=n,upper=upper))
    for e in range(d,upper+1):rows.append(dict(v=v,kind='two',degrees=[d,e],positions=[v//2,v//2+1],ell={0:267-d-e,1:d-1,2:e-1,3:1},U=str(cal.two(v,d,e))))
  else:
   D=20;Z=21*v-2128;T=149-v;assert Z>0 and 28*Z>2*T*T
   sels.append(dict(v=v,D=D,Z=Z,T=T,gap=28*Z-2*T*T))
   for ds in combinations_with_replacement(range(m.CEIL(v-1,7),21),3):
    for tri in (0,1):
     ell={0:268-sum(ds),1:ds[0]-1,2:ds[1]-1,4:ds[2]-1,7:1} if tri else {0:269-sum(ds),1:ds[0]-2,2:ds[1]-2,4:ds[2]-2,3:1,5:1,6:1}
     rows.append(dict(v=v,kind='three',degrees=ds,tri=tri,positions=[v//2-1,v//2,v//2+1],ell=ell,U=str(cal.three(v,ds,tri))))
 for r in rows:r['strict']=Q(r['U'])<1
 failures=[r for r in rows if not r['strict']]
 out=dict(k=8,M=266,degree_budget=2128,domain=domain,balanced=balanced,selection=sels,partner=partner,rows=rows,failures=failures,cpu_seconds=time.process_time()-START)
 (HERE/'INITIAL.json').write_text(json.dumps(out,indent=2)+'\n')
 print('ROWS',len(rows),'FAIL',len(failures),'CPU',out['cpu_seconds'])
 print(json.dumps(failures[:40],indent=2))
if __name__=='__main__':main()
