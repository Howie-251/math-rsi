#!/usr/bin/env python3
"""Expand saved A,B,C; no searcher's masks/distance state are reused."""
import argparse
import json
from pathlib import Path

P=[sorted({(i+1)%5,(i-1)%5,i+5}) for i in range(5)]+[sorted({5+(i+2)%5,5+(i-2)%5,i}) for i in range(5)]
R=[(i+1)%5 for i in range(5)]+[5+(i+1)%5 for i in range(5)]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('params',type=Path);args=ap.parse_args()
    data=json.loads(args.params.read_text());A,B,C=[data[k] for k in ('A','B','C')]
    for perm in (A,B,C,R):assert sorted(perm)==list(range(10))
    for u in range(10):
        v=u
        for _ in range(5):v=R[v]
        assert v==u and R[u]!=u
        assert set(map(R.__getitem__,P[u]))==set(P[R[u]])
    edges=set()
    for f in range(6):
        for u in range(10):
            for v in P[u]:edges.add(tuple(sorted((10*f+u,10*f+v))))
    # Fibers 0,...,4 are external; fiber 5 is infinity.
    for i in range(5):
        for u in range(10):
            v=u
            for _ in range((-i)%5):v=R[v]
            edges.add(tuple(sorted((50+u,10*i+A[v]))))
            edges.add(tuple(sorted((10*i+u,10*((i+1)%5)+B[u]))))
            edges.add(tuple(sorted((10*i+u,10*((i+2)%5)+C[u]))))
    target=args.params.with_suffix('').with_suffix('.edges')
    target.write_text(f'60 {len(edges)}\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
    print(target)
if __name__=='__main__':main()
