from pathlib import Path
from fractions import Fraction as Q
from math import comb
import importlib.util,json,time,signal
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
spec=importlib.util.spec_from_file_location('old',ROOT/'propertyB_small_k/propertyB_m8_certificate_v2.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
START=time.process_time()
def timeout(s,f):raise TimeoutError('40 CPU-second trial budget')
signal.signal(signal.SIGPROF,timeout);signal.setitimer(signal.ITIMER_PROF,40);signal.alarm(80)
FMAX,QMAX,INF=30,80,100000
exact=[[INF]*(QMAX+1)for _ in range(FMAX+1)];exact[0][0]=0
for f in range(1,FMAX+1):
 for t in range(1,f+1):
  for e in range(t-1,min(comb(t,2),QMAX)+1):
   support=7 if t==1 else max(8,7*m.CEIL(t*t,t+2*e),7*m.CEIL(2*t-e-1,2),15 if e<comb(t,2)-t//2 else 0)
   for q in range(e,QMAX+1):exact[f][q]=min(exact[f][q],support+exact[f-t][q-e])
atmost=[]
for row in exact:
 x=INF;out=[]
 for z in row:x=min(x,z);out.append(x)
 atmost.append(out)
def quota(f,N):
 assert f<=FMAX
 return next(q for q in range(QMAX+1)if atmost[f][q]<=N)
class Strong(m.Calculator):
 def deletion(self,v,pos,ell,j):
  bit=1<<j;typ=[t for t,n in ell.items()if n and t&bit];cells=[]
  for i,t in enumerate(typ):
   for u in typ[i:]:
    cap=comb(ell[t],2)if t==u else ell[t]*ell[u]
    if cap:cells.append((self.weight(v,pos,pos[j],t,u)+self.weight(v,pos,pos[j],u,t),cap,t|u))
  costs=[]
  for R in range(1<<len(pos)):
   if R&bit:continue
   f=sum(n for t,n in ell.items()if t&bit and not t&R);need=quota(f,v-1-R.bit_count());cost=Q(0)
   for w,cap,union in sorted(cells):
    if not union&R:
     take=min(cap,need);cost+=take*w;need-=take
   assert need==0
   costs.append(cost)
  return max(costs)
cal=Strong(8,266)
def main():
 rows=[];ranges=[]
 for v in range(83,90):
  for d in range(m.CEIL(v-1,7),2128//v+1):
   u=cal.one(v,d);rows.append(dict(v=v,kind='one',degrees=[d],positions=[v//2],ell={0:266-d,1:d},U=str(u),strict=u<1))
 for v in range(90,108):
  for d in range(m.CEIL(v-1,7),2128//v+1):
   n=2*(v-1)-7*d;assert n>0
   upper=d+(2128-v*d)//n;ranges.append(dict(v=v,d=d,n=n,upper=upper))
   for e in range(d,upper+1):
    ell={0:267-d-e,1:d-1,2:e-1,3:1};best=None
    for pos in ((v//2,v//2+1),(v//2+1,v//2),(v//2-1,v//2)):
     u=cal.bound(v,pos,ell)
     if best is None or u<best[0]:best=u,pos
     if u<1:break
    rows.append(dict(v=v,kind='two',degrees=[d,e],positions=best[1],ell=ell,U=str(best[0]),strict=best[0]<1))
 ell={0:269-51,1:15,2:15,4:15,3:1,5:1,6:1};pos=(59,60,61);u=cal.bound(120,pos,ell)
 rows.append(dict(v=120,kind='three_repair',degrees=[17]*3,tri=0,ell=ell,positions=pos,U=str(u),strict=u<1))
 out=dict(scope='Strong component max_R; one83..89, complete two90..107, and120 lowest separate triple',k=8,M=266,rows=rows,ranges=ranges,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-START)
 (HERE/'COMPONENT_TRIAL.json').write_text(json.dumps(out,indent=2)+'\n');print('rows',len(rows),'fails',len(out['failures']),'CPU',out['cpu_seconds']);print(json.dumps(out['failures'][:30],indent=2));print('tail',rows[-1],flush=True)
if __name__=='__main__':main()
