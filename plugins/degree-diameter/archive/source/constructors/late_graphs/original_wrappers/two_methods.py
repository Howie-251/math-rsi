#!/usr/bin/env python3
"""Replay one of eight frozen constructions. No solver, BFS, Lean or hashes.
This delivery helper was statically prepared, not executed by the document task.
"""
import argparse,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
STAGE=HERE/'research/ddp/two_successful_methods_20261101'
EXPECTED={3900:(40500,21),4125:(45000,22),20580:(360150,35),3840:(38400,20),3984:(41280,21),4192:(45440,22),4336:(48320,23),6160:(73920,24)}
def read_json(path):return json.loads(path.read_text())
def gf4_mul(a,b):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return z

def field_lift(order):
    q=4 if order==3840 else 7
    P=read_json(STAGE/('f4_c60_edge_projective' if q==4 else 'f7_c60_d35')/'PARAMETERS.json')
    C,L,inv=[P[k]for k in ['controller','directions','inverse_ports']]
    edges=set();width=q**3
    for u,row in enumerate(C):
        for p,v in enumerate(row):
            T=P['dart_matrices'][u][p] if q==4 else P['matrices'][P['dart_chart_index'][u][p]]
            for code in range(width):
                x=[code%q,code//q%q,code//(q*q)]
                if q==4:
                    y=[gf4_mul(a,x[0])^gf4_mul(b,x[1])^gf4_mul(c,x[2])for a,b,c in T]
                else:y=[sum(a*b for a,b in zip(r,x))%q for r in T]
                for t in range(q):
                    z=[y[j]^gf4_mul(t,L[inv[p]][j]) if q==4 else (y[j]+t*L[inv[p]][j])%q for j in range(3)]
                    a=width*u+code;b=width*v+z[0]+q*z[1]+q*q*z[2]
                    if a!=b:edges.add((min(a,b),max(a,b)))
    return edges

def clone_lift(order):
    transfer=STAGE/'retained_edge_transfer'
    if order in [3900,4125]:
        source=HERE/'research/ddp/refresh_20261029/f5_full_d20_D3/graph_d20_D3_n3750.edges'
        recipe=transfer/('RECIPE_d21.json' if order==3900 else 'RECIPE_d22.json')
    else:
        source=STAGE/'f4_c60_edge_projective/graph_d20_D3_n3840.edges'
        if order==4336:recipe=transfer/'f4_c60_load_sums_23_24/RECIPE_d23.json'
        else:recipe=transfer/'f4_c60_plane_blocks'/('RECIPE_d21.json' if order==3984 else 'RECIPE_d22.json')
    with source.open()as f:
        n,m=map(int,f.readline().split());edges={tuple(map(int,line.split()))for line in f if line.strip()}
    adjacency=[[]for _ in range(n)]
    for a,b in edges:adjacency[a].append(b);adjacency[b].append(a)
    for item in read_json(recipe)['steps']:
        new=item['new_vertex'];owner=item['owner']
        for pin in adjacency[owner]:edges.add((pin,new))
    return edges

def gq_lift():
    P=read_json(STAGE/'retained_edge_transfer/opposite_gq35_spread24/PARAMETERS.json')
    lines=[r['points']for r in P['lines']];inc=P['point_incident_lines'];edges=set()
    for p in range(64):
        for l,L in enumerate(lines):
            u=96*p+l
            for q in L:
                for m in inc[p]:
                    v=96*q+m
                    if u<v:edges.add((u,v))
    for j,l in enumerate(P['spread_line_labels']):
        new=6144+j
        for p in lines[l]:
            for m in inc[p]:edges.add((96*p+m,new))
    return edges

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--order',type=int,choices=sorted(EXPECTED),required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():raise SystemExit('Choose a new output path; saved evidence is not overwritten.')
    n=args.order
    if n in [3840,20580]:edges=field_lift(n)
    elif n==6160:edges=gq_lift()
    else:edges=clone_lift(n)
    if len(edges)!=EXPECTED[n][0]:raise ValueError('Saved parameters/recipe do not produce the frozen expected edge count.')
    with args.output.open('w')as f:
        f.write(f'{n} {len(edges)}\n')
        for a,b in sorted(edges):f.write(f'{a} {b}\n')
    print(json.dumps({'order':n,'edges':len(edges),'output':str(args.output),'distance_check_executed':False}))
if __name__=='__main__':main()
