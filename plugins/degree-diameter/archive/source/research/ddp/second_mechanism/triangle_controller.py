"""Bounded heuristic controller test; failure is not an impossibility proof."""
from pathlib import Path
import json,time,argparse
import numpy as np
from control_capacity import matrix_capacity

HERE=Path(__file__).resolve().parent


def search(n,budget,seed):
    rng=np.random.default_rng(seed)
    k4={31:1,32:2,33:0,34:1}[n]
    blocks=[3]*((n-4*k4)//3)+[4]*k4
    A0=np.zeros((n,n),dtype=np.int64);at=0
    for size in blocks:
        A0[at:at+size,at:at+size]=1
        at+=size
    np.fill_diagonal(A0,0)
    stubs=np.repeat(np.arange(n),4-A0.sum(axis=1))
    def initial():
        while True:
            ss=stubs.copy();rng.shuffle(ss);A=A0.copy();E=[];valid=True
            for x,y in zip(ss[::2],ss[1::2]):
                if x==y or A[x,y]:valid=False;break
                A[x,y]=A[y,x]=1;E.append((int(x),int(y)))
            if valid:return A,E
    start=time.monotonic();best=10**9;iterations=0;restarts=0;bestA=None
    while time.monotonic()-start<budget:
        A,E=initial();C=matrix_capacity(A);score=int(np.maximum(0,27-C).sum())
        local=time.monotonic();restarts+=1
        while time.monotonic()-start<budget and time.monotonic()-local<3:
            k,l=map(int,rng.choice(len(E),2,replace=False));a,b=E[k];c,d=E[l]
            if rng.random()<.5:c,d=d,c
            if len({a,b,c,d})<4 or A[a,c] or A[b,d]:continue
            A[a,b]=A[b,a]=A[c,d]=A[d,c]=0
            A[a,c]=A[c,a]=A[b,d]=A[d,b]=1
            Cnew=matrix_capacity(A);new=int(np.maximum(0,27-Cnew).sum());iterations+=1
            temp=25
            if new<=score or rng.random()<np.exp(min(0,(score-new)/temp)):
                E[k]=(a,c);E[l]=(b,d);C=Cnew;score=new
            else:
                A[a,c]=A[c,a]=A[b,d]=A[d,b]=0
                A[a,b]=A[b,a]=A[c,d]=A[d,c]=1
            if score<best:
                best=score;bestA=A.copy()
                print(json.dumps(dict(n=n,best=best,iterations=iterations,seconds=time.monotonic()-start)),flush=True)
            if best==0:break
        if best==0:break
    result=dict(status='necessary_control_condition_only',control_order=n,proposed_lift_order=27*n,
                degree=12,diameter_target=3,budget_seconds=budget,seed=seed,
                seconds=time.monotonic()-start,iterations=iterations,restarts=restarts,
                blocks=blocks,min_optimistic_missing=best,
                edges=[[i,j] for i in range(n) for j in range(i+1,n) if bestA[i,j]],
                bad_ordered_pairs=np.argwhere(matrix_capacity(bestA)<27).tolist())
    (HERE/f'triangle_controller_n{n}_seed{seed}.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('edges','bad_ordered_pairs')}),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--seconds',type=float,default=30)
    p.add_argument('--orders',type=int,nargs='+',default=[31,32,33,34])
    p.add_argument('--seed',type=int,default=20261026);a=p.parse_args()
    for n in a.orders:search(n,a.seconds,a.seed+n)
