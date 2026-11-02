"""Necessary route-cardinality bound for q=3,s=3 affine line lifts.

Only 4-regular simple control graphs are in scope. For their adjacency A,
C = 27 A^3 + 9 A^2 - 129 A - 23 I bounds the number of reachable fibre
points via walks of length <=3. Immediate base-edge reversals have rank 1
at length 2, and rank <=2 at length 3 (rank 1 for three uses of one edge).
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import argparse
import json
import time
import numpy as np

HERE=Path(__file__).resolve().parent


def darts(a,b,c,d):
    return [[(1,0,0),(1,a,1),(2,0,2),(2,b,3)],
            [(0,0,0),(0,-a,1),(2,c,4),(2,d,5)],
            [(0,0,2),(0,-b,3),(1,-c,4),(1,-d,5)]]


def word_capacity(m, ds):
    caps=[]
    for s in range(3):
        cap=Counter({(s,0):1}); paths=[(s,0,())]
        for depth in range(1,4):
            nxt=[]
            for i,z,hist in paths:
                for j,v,e in ds[i]:
                    h=hist+(e,);nxt.append((j,(z+v)%m,h))
                    rank=depth-sum(h[k]==h[k+1] for k in range(depth-1))
                    cap[j,(z+v)%m]+=3**rank
            paths=nxt
        caps.append([cap[i,z] for i in range(3) for z in range(m)])
    return np.array(caps,dtype=np.int64)


def cyclic_adj(m,ds):
    A=np.zeros((3*m,3*m),dtype=np.int64)
    for i in range(3):
        for j,a,_ in ds[i]:
            for z in range(m): A[i*m+z,j*m+(z+a)%m]=1
    return A


def matrix_capacity(A):
    assert np.array_equal(A,A.T) and not np.any(np.diag(A)) and np.all(A.sum(axis=1)==4)
    A2=A@A
    return 27*(A2@A)+9*A2-129*A-23*np.eye(len(A),dtype=np.int64)


def enumerate_cyclic():
    result=[]
    for m in range(10,18):
        start=time.monotonic(); total=0;passing=0;best=10**9;bp=None
        # For prime m, multiplication of all voltages by a^{-1} fixes a=1.
        avals=[1] if m in (11,13,17) else range(1,m)
        for a in avals:
            for b in range(1,m):
                for c,d in combinations(range(m),2):
                    ds=darts(a,b,c,d)
                    C=word_capacity(m,ds)
                    deficit=int(np.maximum(0,27-C).sum());total+=1
                    if deficit==0:passing+=1
                    if deficit<best:best=deficit;bp=[a,b,c,d]
        ds=darts(*bp)
        C=matrix_capacity(cyclic_adj(m,ds))[[0,m,2*m]]
        assert np.array_equal(C,word_capacity(m,ds))
        rec=dict(m=m,n=81*m,enumerated=total,passing=passing,
                 min_optimistic_missing=best,best_parameters=bp,
                 independent_matrix_check=True,seconds=time.monotonic()-start)
        result.append(rec);print(json.dumps(rec),flush=True)
        (HERE/'cyclic_capacity_results.json').write_text(json.dumps(result,indent=2)+'\n')
    # Original recovered control voltages gauge to (a,b,c,d)=(5,3,0,9).
    # Gauge sets first 01=0 and first 02=0 using original 02 voltage 8;
    # original 12 voltages 7,8 become 9,0.
    ds=darts(5,3,0,9)
    C=word_capacity(10,ds)
    assert np.array_equal(C,matrix_capacity(cyclic_adj(10,ds))[[0,10,20]])
    assert np.all(C>=27)


def controller_adj(perms):
    m=len(perms[0]);A=np.zeros((3*m,3*m),dtype=np.int64)
    for pair,p in zip([(0,1),(0,2),(1,2)],perms):
        i,j=pair
        for z in range(m):
            for w in (z,int(p[z])):
                A[i*m+z,j*m+w]=1;A[j*m+w,i*m+z]=1
    return A


def search_controller(m,budget,seed):
    rng=np.random.default_rng(seed)
    def random_derangement():
        while True:
            p=rng.permutation(m)
            if np.all(p!=np.arange(m)):return p
    start=time.monotonic();iterations=0;restarts=0;best=10**9;bestp=None;bestbad=None
    while time.monotonic()-start<budget:
        perms=[random_derangement() for _ in range(3)]
        A=controller_adj(perms);C=matrix_capacity(A)
        score=int(np.maximum(0,27-C).sum());local_start=time.monotonic();restarts+=1
        while time.monotonic()-start<budget and time.monotonic()-local_start<2:
            which=int(rng.integers(3));x,y=map(int,rng.choice(m,2,replace=False))
            p=perms[which]
            if p[y]==x or p[x]==y:continue
            p[x],p[y]=p[y],p[x]
            Anew=controller_adj(perms);Cnew=matrix_capacity(Anew)
            new=int(np.maximum(0,27-Cnew).sum());iterations+=1
            temperature=20.0
            if new<=score or rng.random()<np.exp(min(0,(score-new)/temperature)):
                score=new;A=Anew;C=Cnew
            else:p[x],p[y]=p[y],p[x]
            if score<best:
                best=score;bestp=[p.tolist() for p in perms]
                bestbad=np.argwhere(C<27).tolist()
                print(json.dumps(dict(best=best,iterations=iterations,seconds=time.monotonic()-start)),flush=True)
            if best==0:break
        if best==0:break
    result=dict(status='necessary_control_condition_only',m=m,control_order=3*m,
                proposed_lift_order=81*m,degree=12,diameter_target=3,budget_seconds=budget,
                seed=seed,seconds=time.monotonic()-start,iterations=iterations,restarts=restarts,
                min_optimistic_missing=best,permutations=bestp,bad_ordered_pairs=bestbad)
    (HERE/f'controller_m{m}_seed{seed}.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('permutations','bad_ordered_pairs')}))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['enumerate','search'])
    parser.add_argument('--m',type=int,default=11);parser.add_argument('--seconds',type=float,default=60)
    parser.add_argument('--seed',type=int,default=20261026);args=parser.parse_args()
    if args.mode=='enumerate':enumerate_cyclic()
    else:search_controller(args.m,args.seconds,args.seed)
