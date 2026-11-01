"""Fresh M542 k9 exact domain and original-framework short profile."""
from pathlib import Path
import importlib.util,itertools,json,time,signal
from fractions import Fraction as F
from math import comb
P=Path(__file__).resolve().parent;ROOT=P.parents[1]
s=importlib.util.spec_from_file_location('original_k9',ROOT/'propertyB_small_k/propertyB_m9_certificate_v2.py');src=importlib.util.module_from_spec(s);s.loader.exec_module(src)
K,M=9,542;BUDGET=K*M;c=src.Calculator(K,M)

def asrow(v,kind,ell,pos,U,**kwargs):return dict(v=v,kind=kind,ell=ell,positions=pos,U=str(U),strict=U<1,**kwargs)

def main():
 start=time.process_time();balanced=[];rows=[];selection=[]
 domain=[v for v in range(1,BUDGET+1)if v*src.CEIL(v-1,K-1)<=BUDGET]
 vmax=max(domain)
 for v in range(2*K-1,vmax+1):
  p=F(M*(src.C(v//2,K)+src.C(v-v//2,K)),src.C(v,K))
  if p<1:balanced.append(dict(v=v,U=str(p)))
 vmin=max(r['v']for r in balanced)+1
 assert vmin==57 and vmax==195 and BUDGET==4878
 for v in range(vmin,vmax+1):
  lo=src.CEIL(v-1,K-1);hi=BUDGET//v
  if v<=139:
   U=c.unlocked(v);rows.append(asrow(v,'zero',{},[],U))
  elif v<=154:
   for d in range(lo,hi+1):
    ell={0:M-d,1:d};pos=(v//2,);rows.append(asrow(v,'one',ell,pos,c.bound(v,pos,ell),degrees=[d]))
  elif v<=182:
   for d in range(lo,hi+1):
    n=2*(v-1)-(K-1)*d;assert n>0
    upper=d+(BUDGET-v*d)//n
    selection.append(dict(v=v,d=d,unit_pool_lower=n,partner_upper=upper))
    for e in range(d,upper+1):
     ell={0:M-d-e+1,1:d-1,2:e-1,3:1};pos=(v//2,v//2+1)
     rows.append(asrow(v,'two',ell,pos,c.bound(v,pos,ell),degrees=[d,e]))
  else:
   D=28;Z=(D+1)*v-BUDGET;T=(K-1)*(D+1)-v+2
   assert Z>0 and 2*(K-1)*Z>T*T
   selection.append(dict(v=v,D=D,Z=Z,T=T,CW_gap=2*(K-1)*Z-T*T))
   for ds in itertools.combinations_with_replacement(range(lo,D+1),3):
    for t in(0,1):
     if t:ell={0:M-sum(ds)+2,1:ds[0]-1,2:ds[1]-1,4:ds[2]-1,7:1}
     else:ell={0:M-sum(ds)+3,1:ds[0]-2,2:ds[1]-2,4:ds[2]-2,3:1,5:1,6:1}
     pos=(v//2-1,v//2,v//2+1);rows.append(asrow(v,'three',ell,pos,c.bound(v,pos,ell),degrees=ds,triple=t))
  for func in(c.context,c.endpoint,c.weight):func.cache_clear()
 summary=[]
 for kind in('zero','one','two','three'):
  rr=[r for r in rows if r['kind']==kind];summary.append(dict(kind=kind,profiles=len(rr),failures=sum(not r['strict']for r in rr),maximum=str(max(F(r['U'])for r in rr))))
 out=dict(status='complete originalrecipe profile',k=K,M=M,total_degree=BUDGET,link_uniformity=8,link_max_intersection=7,vertex_min=vmin,vertex_max=vmax,balanced=balanced,selection=selection,summary=summary,rows=rows,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-start)
 (P/'PROFILE.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items()if k not in('rows','selection','balanced','failures')},indent=2));print('FAILURES',len(out['failures']))
 for r in out['failures'][:20]:print(r)
if __name__=='__main__':main()
