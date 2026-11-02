#!/usr/bin/env python3
"""Independent exact all-vertices reachability checker for n-m edge files.

Uses integer bitsets and the recurrence R_(k+1)(v)=R_k(v) union
union_{w adjacent v} R_k(w), not the C++ breadth-first implementation.
Only a finite verifier; no searches, no external requests or packages.
"""
from __future__ import annotations
import argparse,json,time
from pathlib import Path

def verify(path:Path, max_degree:int, max_diameter:int)->dict:
    begin=time.perf_counter()
    with path.open(encoding='utf-8') as f:
        header=f.readline().split()
        if len(header)!=2: raise ValueError('header must be n m')
        n,m=map(int,header)
        if n<1 or m<0: raise ValueError('invalid order or size')
        adj=[set() for _ in range(n)]
        edges=set()
        for line in f:
            if not line.strip(): continue
            values=line.split()
            if len(values)!=2: raise ValueError('edge requires two integers')
            u,v=map(int,values)
            if not (0<=u<n and 0<=v<n) or u==v: raise ValueError('bad vertex/self-loop')
            e=tuple(sorted((u,v)))
            if e in edges: raise ValueError('duplicate edge')
            edges.add(e);adj[u].add(v);adj[v].add(u)
        if len(edges)!=m: raise ValueError('edge count mismatch')
    masks=[1<<v for v in range(n)]
    full=(1<<n)-1
    totals=[n]
    for depth in range(1,max_diameter+1):
        nxt=[]
        for v,neighbors in enumerate(adj):
            r=masks[v]
            for w in neighbors:r|=masks[w]
            nxt.append(r)
        masks=nxt
        totals.append(sum(r.bit_count() for r in masks))
    diameter=next((d for d,t in enumerate(totals) if t==n*n),None)
    ok=max(map(len,adj))<=max_degree and all(r==full for r in masks)
    return {'n':n,'m':m,'min_degree':min(map(len,adj)),'max_degree':max(map(len,adj)),
            'diameter_within_checked_radius':diameter,'all_pairs_reached':all(r==full for r in masks),
            'ordered_reachability_totals':totals,'valid':ok,'seconds':time.perf_counter()-begin}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file',type=Path)
    parser.add_argument('max_degree',type=int)
    parser.add_argument('max_diameter',type=int)
    args=parser.parse_args()
    result=verify(args.file,args.max_degree,args.max_diameter)
    print(json.dumps(result,ensure_ascii=False))
    raise SystemExit(0 if result['valid'] else 1)
