"""Exact monochromatic probabilities for color families adapted to the unique-repeat six-link."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product,permutations
from math import comb
import json,time,numpy as np
from scipy.optimize import linprog
HERE=Path(__file__).parent

def choices(xs):return sorted(set(permutations(xs)))
def ratio(n,a,k):return Q(comb(a,k),comb(n,k)) if a>=k else Q(0)
def main():
 st=time.time();colors=[]
 for pc in (0,1):
  for a in range(4-pc):
   for b in range(a,4-pc):
    for cs in product(range(4),repeat=4):
     if list(cs)!=sorted(cs):continue
     colors.append((pc,a,b,*cs))
 edges=[]
 for ep in (0,1):
  for a in range(4):
   for b in range(a,4):
    for cs in product(range(5),repeat=4):
     if list(cs)!=sorted(cs) or a+b+sum(cs)+ep!=5:continue
     edges.append((ep,a,b,*cs))
 P=[]
 for co in colors:
  pc=co[0]; variants=[a+b for a in choices(co[1:3]) for b in choices(co[3:])];row=[]
  for ep,*ed in edges:
   val=Q()
   for rc in variants:
    red=Q(int(not ep or pc));blue=Q(int(not ep or not pc))
    for n,r,k in zip((3,3,4,4,4,4),rc,ed):red*=ratio(n,r,k);blue*=ratio(n,n-r,k)
    val+=red+blue
   row.append(val/len(variants))
  P.append(row)
 mat=np.array([[float(x) for x in r] for r in P])
 # q macrocolor distribution + worst per-edge mono prob t.
 sol=linprog([0]*len(colors)+[1],A_ub=np.column_stack((mat.T,-np.ones(len(edges)))),b_ub=np.zeros(len(edges)),A_eq=[[1]*len(colors)+[0]],b_eq=[1],bounds=[(0,None)]*len(colors)+[(0,None)],method='highs')
 active=[(colors[i],float(w)) for i,w in enumerate(sol.x[:-1]) if w>1e-9]
 print('colors',len(colors),'edges',len(edges),'minimax',sol.fun,'29x',29*sol.fun,'active',active,'seconds',time.time()-st,flush=True)
 # Type counts relaxed: sum n=29, external degrees each >=5 for unique points, p>=4.
 # A and B have 3 unique vertices external degree >=5 => aggregate incidence >=15;
 # each ordinary four-block >=20; p external deg>=4.
 es=np.array([e for e in edges],float)
 Aeq=np.ones((1,len(edges)));beq=[29]
 Aub=np.vstack((-es[:,0],-(es[:,1]+es[:,2]),-es[:,3:].sum(axis=1)))
 bub=[-4,-30,-80]
 # Every cross-group pair of unique vertices needs an external edge.
 extra=np.array([[e[1]*e[2],sum(e[1:3])*sum(e[3:]),sum(e[i]*e[j] for i in range(3,7) for j in range(i+1,7))] for e in edges],float).T
 Aub=np.vstack((Aub,-extra));bub += [-9,-96,-96]
 # maximize t subject every chosen color family monochromatic expected edges>=t.
 sol2=linprog([0]*len(edges)+[-1],A_ub=np.vstack((np.column_stack((-mat,np.ones(len(colors)))),np.column_stack((Aub,np.zeros(len(bub)))))),b_ub=np.r_[np.zeros(len(colors)),bub],A_eq=[[*Aeq[0],0]],b_eq=beq,bounds=[(0,None)]*len(edges)+[(None,None)],method='highs')
 print('type-count fractional maximin',sol2.fun,'active',[(edges[i],v) for i,v in enumerate(sol2.x[:-1]) if v>1e-8],flush=True)
 out=dict(scope=__doc__,colors=colors,edges=edges,probabilities=[[str(x) for x in r] for r in P],minimax=sol.fun,minimax_active=active,fractional_type_maximin=-sol2.fun,fractional_active=[(edges[i],float(v)) for i,v in enumerate(sol2.x[:-1]) if v>1e-8],elapsed_seconds=time.time()-st)
 (HERE/'LINK_BLOCK_PILOT.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
