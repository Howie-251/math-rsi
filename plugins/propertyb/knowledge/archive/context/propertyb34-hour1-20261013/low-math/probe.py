from pathlib import Path
import sys,time,json
from itertools import combinations,permutations,product
from fractions import Fraction
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'computations'))
sys.path.insert(0,str(ROOT/'computations/propertyb33/round01'))
from multilock import Profile,rows,total_bound,json_value
from pure_quota import certificate
from independent_structure_bounds import independent_rows

def calc(v,ds,ls,ts,pos):
 if len(ds)==2:
  a=ls[0];dx,dy=ds;counts={0:34-dx-dy+a,1:dx-a,2:dy-a,3:a}
 elif len(ds)==3:
  a,b,c=ls;t=ts;dx,dy,dz=ds
  counts={0:34-dx-dy-dz+a+b+c-t,1:dx-a-b+t,2:dy-a-c+t,4:dz-b-c+t,3:a-t,5:b-t,6:c-t,7:t}
 if min(counts.values())<0:return None
 p=Profile(v,5,pos,counts)
 cs=[certificate(p,i) for i in range(len(ds))]
 rs=rows(p,deductions={pos[i]:cs[i]['loss'] for i in range(len(ds))})
 return dict(v=v,ds=ds,ls=ls,t=ts,pos=pos,counts=counts,cs=cs,rows=rs,bound=total_bound(rs))
def best(v,ds,ls,ts=0,exhaust=False):
 s=len(ds)
 if exhaust:poslist=combinations(range(1,v+1),s)
 else:poslist=[tuple(range(k,k+s)) for k in range(v//2-4,v//2+4)]+[(1, v//2+1)]*(s==2)
 out=[]
 for pos in poslist:
  for pp in set(permutations(pos)):
   r=calc(v,ds,ls,ts,pp)
   if r:out.append(r)
 return min(out,key=lambda r:r['bound']) if out else None
if __name__=='__main__':
 start=time.time();out=[]
 for v in [20,21]:
  for ds in [(6,6),(6,7),(6,8),(6,9),(7,7),(7,8),(7,9),(7,10),(8,8),(8,9)]:
   for a in range(1,min(ds)+1):
    r=best(v,ds,(a,));out.append(r)
    print(v,ds,a,r['pos'],r['bound'],float(r['bound']),flush=True)
 Path(__file__).with_name('DOUBLE_SCAN.json').write_text(json.dumps(json_value(out),indent=2))
 print('seconds',time.time()-start)
