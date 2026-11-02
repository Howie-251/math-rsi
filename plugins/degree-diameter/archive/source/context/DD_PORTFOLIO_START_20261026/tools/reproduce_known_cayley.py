#!/usr/bin/env python3
"""Regenerate four PUBLISHED/RECORDED baselines, never new discoveries.

The construction uses (x,y)*(u,v)=(x+u mod m,y*a**u+v mod n).
Specifications are attributed in baselines/generator_specs.json.
Default writes into a new directory rather than modifying research output.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path

def generate(spec:dict)->tuple[int,list[tuple[int,int]]]:
    m,n,a=(int(spec[k]) for k in ('m','n','a'))
    if math.gcd(a,n)!=1 or pow(a,m,n)!=1:raise ValueError('invalid semidirect-product parameters')
    generators=set()
    for u,v in spec['generators']:
        if not (0<=u<m and 0<=v<n):raise ValueError('generator outside group')
        generators.add((u,v))
        generators.add(((-u)%m,(-v*pow(a,(-u)%m,n))%n))
    if (0,0) in generators or len(generators)!=spec['degree']:raise ValueError('bad inverse closure')
    edges=set()
    for x in range(m):
        for y in range(n):
            p=x*n+y
            for u,v in generators:
                q=((x+u)%m)*n+(y*pow(a,u,n)+v)%n
                if p==q:raise ValueError('unexpected loop')
                edges.add((min(p,q),max(p,q)))
    return m*n,sorted(edges)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--specs',type=Path,default=Path(__file__).resolve().parents[1]/'baselines/generator_specs.json')
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    for spec in json.loads(a.specs.read_text()):
        n,edges=generate(spec);dest=a.out/f"{spec['id']}_known.edges"
        if dest.exists():raise FileExistsError(f'{dest} already exists; select a fresh output directory')
        dest.write_text(f'{n} {len(edges)}\n'+''.join(f'{u} {v}\n' for u,v in edges),encoding='utf-8')
        print(f"KNOWN_BASELINE_ONLY {spec['id']} n={n} m={len(edges)} -> {dest}")
