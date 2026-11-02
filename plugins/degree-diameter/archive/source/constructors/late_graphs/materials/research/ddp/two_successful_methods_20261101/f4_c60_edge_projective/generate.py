#!/usr/bin/env python3
"""Reproduce the unique saved3840 graph; does not solve or test distances."""
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
def mul(a,b):
    c=0
    while b:
        if b&1:c^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return c
def dot(a,b):
    z=0
    for x,y in zip(a,b):z^=mul(x,y)
    return z
def main():
    P=json.loads((HERE/'PARAMETERS.json').read_text())
    C,T,L,inv=(P[k] for k in ['controller','dart_matrices','directions','inverse_ports'])
    G=[set() for _ in range(3840)]
    for u in range(60):
        for p,v in enumerate(C[u]):
            for code in range(64):
                x=[code%4,code//4%4,code//16]
                y=[dot(row,x) for row in T[u][p]]
                for t in range(4):
                    out=sum((y[j]^mul(t,L[inv[p]][j]))*4**j for j in range(3))
                    G[64*u+code].add(64*v+out)
    assert all(len(row)==20 and u not in row for u,row in enumerate(G))
    assert all(u in G[v] for u,row in enumerate(G) for v in row)
    with (HERE/'graph_d20_D3_n3840.edges').open('w') as f:
        f.write('3840 38400\n')
        for u,row in enumerate(G):
            for v in sorted(row):
                if u<v:f.write(f'{u} {v}\n')
if __name__=='__main__':main()
