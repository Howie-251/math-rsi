"""Actual all-six unit incidence requires a common resolution into outside-point partitions."""
from core_pilot import *
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint, linprog
def partitions(xs):
 if not xs:yield ();return
 x,*ys=xs
 for pp in partitions(ys):
  yield (1<<x,)+pp
  for j,b in enumerate(pp):yield pp[:j]+(b|(1<<x),)+pp[j+1:]
def demands(name,ns):
 ds,_=CORES[name];s=sum(d==6 for d in ds);full=(1<<s)-1
 b=[0]*(1<<s)
 for mask,n in ns.items():
  low=mask&full
  if low:b[low]+=(5-mask.bit_count())*n
 return s,23-len(ds),b
def main():
 st=time.time();out=[]
 for name in CORES:
  ds=CORES[name][0];s=sum(d==6 for d in ds)
  pp=list(partitions(list(range(s))))
  # In C4 the only selected vertices are the sixes, so outside size is19.
  A=np.array([[1]*len(pp)]+[[int(m in p) for p in pp] for m in range(1,1<<s)])
  for index,ns in enumerate(domain(name)):
   _,N,b=demands(name,ns);rhs=np.array([N]+b[1:])
   lp=linprog(np.zeros(len(pp)),A_eq=A,b_eq=rhs,bounds=(0,None),method='highs')
   item=dict(core=name,index=index,demands=b,outside=N,lp_status=int(lp.status))
   if lp.success:
    z=milp(np.zeros(len(pp)),integrality=np.ones(len(pp)),bounds=Bounds(0,np.inf),constraints=LinearConstraint(A,rhs,rhs),options={'time_limit':1.0})
    item['integer_status']=int(z.status)
    if z.success:
     witness=[int(round(v)) for v in z.x]
     assert np.array_equal(A@np.array(witness),rhs)
     item['partition_witness']=[dict(blocks=p,count=n) for p,n in zip(pp,witness) if n]
   out.append(item)
  rr=[z for z in out if z['core']==name]
  print(name,'LP infeasible',sum(z['lp_status']==2 for z in rr),'integer infeasible',sum(z.get('integer_status')==2 for z in rr),'all',len(rr),'elapsed',time.time()-st,flush=True)
 (HERE/'PARTITION_PROBE.json').write_text(json.dumps(dict(scope=__doc__,elapsed_seconds=time.time()-st,profiles=out),indent=2)+'\n')
if __name__=='__main__':main()
