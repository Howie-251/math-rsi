"""Exact integer avoided-link quota minimum for the 195 M=65 pilot profiles."""
import importlib.util, itertools, json, time
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('cert',ROOT/'propertyB_small_k/propertyB_m6_certificate.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c);c.M=65
OUT=Path(__file__).resolve().parent
BASE=json.loads((OUT.parent/'pilot/baseline.json').read_text())

def ell_for(row,ds=None):
 ds=ds or row['degrees'];s=len(ds)
 if s==1:return {0:65-ds[0],1:ds[0]}
 if s==2:return {0:66-sum(ds),1:ds[0]-1,2:ds[1]-1,3:1}
 if row['tri']:return {0:67-sum(ds),1:ds[0]-1,2:ds[1]-1,4:ds[2]-1,7:1}
 return {0:68-sum(ds),1:ds[0]-2,2:ds[1]-2,4:ds[2]-2,3:1,5:1,6:1}

stats={'center_evaluations':0,'integer_fill_vectors':0}
def deletion(v,pos,ell,j,detail=False):
 bit=1<<j; other=((1<<len(pos))-1)^bit
 typ=[T for T,n in ell.items() if n and T&bit]
 cells=[]
 for a,T in enumerate(typ):
  for U in typ[a:]:
   cap=c.C(ell[T],2) if T==U else ell[T]*ell[U]
   if cap:
    w=c.weight(v,pos,pos[j],T,U)+c.weight(v,pos,pos[j],U,T)
    cells.append((T,U,cap,w))
 core=next(x for x in cells if x[0]==bit and x[1]==bit)
 rest=[x for x in cells if x!=core]
 quotas=[]
 for R in range(1<<len(pos)):
  if R&~other:continue
  f=sum(n for T,n in ell.items() if T&bit and not T&R)
  q=max(0,c.ceilings(5*f-(v-1-R.bit_count()),4))
  quotas.append((R,q))
 best=None;bestz=None
 for z in itertools.product(*(range(x[2]+1) for x in rest)):
  zcore=max([0]+[q-sum(k for k,cell in zip(z,rest) if not (cell[0]|cell[1])&R) for R,q in quotas])
  if zcore>core[2]:continue
  value=zcore*core[3]+sum(k*cell[3] for k,cell in zip(z,rest))
  if best is None or value<best:best=value;bestz=[zcore,*z]
  stats['integer_fill_vectors']+=1
 assert best is not None
 stats['center_evaluations']+=1
 assert best>=c.bad_pair_deletion(v,pos,ell,j)
 if detail:return {'D':str(best),'quotas':quotas,'cells':[[T,U,cap,str(w)] for T,U,cap,w in [core,*rest]],'minimizer':bestz}
 return best

def bound(row,pos=None,ds=None,details=False):
 if row['kind']=='zero':return F(row['U'])
 v=row['v'];pos=tuple(pos or row['positions']);ell=ell_for(row,ds)
 dels={pos[j]:deletion(v,pos,ell,j) for j in range(len(pos))}
 total=F(0)
 for h in range(1,v+1):
  A=sum(n*c.endpoint(v,pos,h,T,True) for T,n in ell.items())
  B=sum(n*c.endpoint(v,pos,h,T,False) for T,n in ell.items())
  Q=sum(n*(m-(T==U))*c.weight(v,pos,h,T,U) for T,n in ell.items() for U,m in ell.items())
  Cr=Q-dels.get(h,F(0));assert Cr>=0
  total+=min(A,B,Cr)
 return total

def main():
 start=time.process_time();rows=[];groups=defaultdict(lambda:{'profiles':0,'baseline_failures':0,'rescued':0,'remaining':0,'tightened':0})
 for r in BASE['rows']:
  u=bound(r);old=F(r['U']);assert u<=old
  out={k:r[k] for k in ('v','kind','degrees','tri','positions')}
  out.update(baseline_U=str(old),U=str(u),approx=float(u),strict=u<1,tightened=u<old,rescued=old>=1 and u<1)
  rows.append(out);g=groups[str(r['v'])+'_'+r['kind']];g['profiles']+=1;g['baseline_failures']+=old>=1;g['rescued']+=out['rescued'];g['remaining']+=u>=1;g['tightened']+=u<old
 result={'M':65,'profiles':len(rows),'baseline_failures':len(BASE['failures']),'rescued':sum(r['rescued'] for r in rows),'remaining':sum(not r['strict'] for r in rows),'tightened':sum(r['tightened'] for r in rows),'groups':dict(groups),'cpu_seconds':time.process_time()-start,'stats':stats,'rows':rows}
 (OUT/'RESULTS.json').write_text(json.dumps(result,indent=2))
 print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
if __name__=='__main__':main()
