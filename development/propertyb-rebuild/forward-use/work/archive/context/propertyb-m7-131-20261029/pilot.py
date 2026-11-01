import importlib.util,json,time,itertools
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent;ROOT=P.parents[1]
spec=importlib.util.spec_from_file_location('c',ROOT/'propertyB_small_k/propertyB_m7_certificate.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c);c.M=130
START=time.process_time()
def deletion(v,pos,ell,j):
 bit=1<<j;other=((1<<len(pos))-1)^bit
 typ=[T for T,n in ell.items() if n and T&bit];cells=[]
 for a,T in enumerate(typ):
  for U in typ[a:]:
   cap=c.C(ell[T],2) if T==U else ell[T]*ell[U]
   if cap:cells.append((T,U,cap,c.weight(v,pos,pos[j],T,U)+c.weight(v,pos,pos[j],U,T)))
 core=next(x for x in cells if x[0]==bit and x[1]==bit);rest=[x for x in cells if x!=core]
 quotas=[]
 for R in range(1<<len(pos)):
  if R&~other:continue
  f=sum(n for T,n in ell.items() if T&bit and not T&R)
  quotas.append((R,max(0,c.ceil(6*f-(v-1-R.bit_count()),5))))
 best=None
 for z in itertools.product(*(range(x[2]+1) for x in rest)):
  z0=max([0]+[q-sum(k for k,cell in zip(z,rest) if not (cell[0]|cell[1])&R) for R,q in quotas])
  if z0>core[2]:continue
  val=z0*core[3]+sum(k*cell[3] for k,cell in zip(z,rest))
  if best is None or val<best:best=val
 assert best is not None
 assert best>=c.deletion(v,pos,ell,j)
 return best

def bound(v,pos,ell,avoid=False):
 pos=tuple(pos)
 if not avoid:return c.profile_bound(v,pos,ell)
 ds={pos[j]:deletion(v,pos,ell,j) for j in range(len(pos))};u=F(0)
 for h in range(1,v+1):
  A=sum(n*c.endpoint(v,pos,h,T,True) for T,n in ell.items());B=sum(n*c.endpoint(v,pos,h,T,False) for T,n in ell.items())
  Q=sum(n*(m-(T==U))*c.weight(v,pos,h,T,U) for T,n in ell.items() for U,m in ell.items());cc=Q-ds.get(h,F(0));assert cc>=0
  u+=min(A,B,cc)
 return u

def main():
 rows=[];ranges={};balanced=[]
 for v in range(13,74):
  z=F(130*(c.C(v//2,7)+c.C(v-v//2,7)),c.C(v,7))
  if z<1:balanced.append(v)
 for v in range(37,57):rows.append(dict(v=v,kind='zero',U=str(c.unlocked(v))))
 for v in range(57,62):
  for d in range(c.ceil(v-1,6),910//v+1):rows.append(dict(v=v,kind='one',degrees=[d],positions=[v//2],ell={0:130-d,1:d},U=str(c.one(v,d))))
 for v in range(62,71):
  rr=[]
  for d in range(c.ceil(v-1,6),910//v+1):
   s=2*(v-1)-6*d;assert s>0
   B=next(b for b in range(d,911) if v*d+s*(b+1-d)>910);rr.append([d,B])
   for dy in range(d,B+1):rows.append(dict(v=v,kind='two',degrees=[d,dy],B=B,positions=[v//2,v//2+1],ell={0:131-d-dy,1:d-1,2:dy-1,3:1},U=str(c.two(v,d,dy))))
  ranges[v]=rr
 for v in range(71,74):
  r=13*v-910;e=73-v;assert r>=3*(e+1)
  for tri in (0,1):
   ell={0:96,1:11,2:11,4:11,7:1} if tri else {0:97,1:10,2:10,4:10,3:1,5:1,6:1}
   rows.append(dict(v=v,kind='three',degrees=[12]*3,tri=tri,positions=[v//2-1,v//2,v//2+1],ell=ell,U=str(c.three(v,(12,12,12),tri))))
 failures=[r for r in rows if F(r['U'])>=1]
 out=dict(M=130,degree_budget=910,vertex_max=73,balanced_last=max(balanced),ranges=ranges,profiles=len(rows),failures=failures,rows=rows,cpu=time.process_time()-START)
 (P/'BASELINE.json').write_text(json.dumps(out,indent=2))
 print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
 print('avoid rescue')
 for r in failures:
  if r['kind']!='two':continue
  ell=r['ell'];v=r['v'];mid=v//2;trials=[]
  for shift in range(-2,3):
   for orientation in (0,1):
    pos=[mid+shift,mid+shift+1]
    if orientation:pos=pos[::-1]
    u=bound(v,pos,ell,True);trials.append(dict(positions=pos,U=str(u),strict=u<1))
  r['avoid_trials']=trials;r['best']=min(trials,key=lambda x:F(x['U']))
  print(v,r['degrees'],'old',r['U'],'best',r['best'],flush=True)
 out['cpu']=time.process_time()-START;(P/'RESULTS.json').write_text(json.dumps(out,indent=2))
 print('CPU',out['cpu'])
if __name__=='__main__':main()
