#!/usr/bin/env python3
"""Export the saved deterministic graph recipe into a NEW file; no validators.

This utility is supplied as source and is not executed by the delivery builder.
The original independent acceptance and original generators are also included.
"""
from pathlib import Path
import argparse,json
HERE=Path(__file__).resolve().parent
STAGE=HERE/'research/ddp/two_successful_methods_20261101'
G64=STAGE/'retained_edge_transfer/opposite_gq77_spread64'
G54=STAGE/'affine_field_conditions/r6_schreier78_controller/f9_degree54'
def data(path):return json.loads(path.read_text())
def add(a,b):return (a%3+b%3)%3+3*((a//3+b//3)%3)
def gq_neighbors(d,u):
    w=len(d['lines']);old=w*w
    if u>=old:
        return {w*p+l for p in d['spread'][u-old]['points'] for l in d['point_incident_lines'][p]}
    p,l=divmod(u,w)
    ns={w*r+m for r in d['lines'][l]['points'] for m in d['point_incident_lines'][p]}
    ns.discard(u)
    if l in d['point_incident_lines'][p]:ns.add(old+d['point_spread_owner'][p])
    return ns
def f9_neighbors(d,u):
    c,z=divmod(u,729);x=[z%9,(z//9)%9,z//81];mul=d['field']['multiplication'];ns=set()
    for p,v in enumerate(d['controller'][c]):
        mat=d['matrices'][d['dart_chart_index'][c][p]];q=d['inverse_ports'][p];ell=d['directions'][q]
        y=[add(add(mul[mat[i][0]][x[0]],mul[mat[i][1]][x[1]]),mul[mat[i][2]][x[2]]) for i in range(3)]
        for t in range(9):
            a=[add(y[i],mul[t][ell[i]]) for i in range(3)];ns.add(729*v+a[0]+9*a[1]+81*a[2])
    return ns
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--order',type=int,choices=[160050,161150,166650,56862,56943],required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    g=data(G64/'PARAMETERS.json') if a.order in [160050,161150,166650] else data(G54/'PARAMETERS.json')
    source_n=160050 if a.order in [160050,161150,166650] else 56862
    source_ns=(lambda u:gq_neighbors(g,u)) if source_n==160050 else (lambda u:f9_neighbors(g,u))
    centers=[]
    if a.order==161150:centers=data(G64/'partial_ovoid65_gate/cubic_coset22/PARAMETERS.json')['source_center_labels_original_order']
    if a.order==166650:centers=data(G64/'cubic22_multiplicity70/PARAMETERS.json')['source_base_center_labels_original_order']*6
    if a.order==56943:centers=data(G54/'single_fiber_plane55_graph/PARAMETERS.json')['center_old_labels']
    extra={};pins=[]
    for j,c in enumerate(centers):
        ns=source_ns(c);pins.append(ns)
        for v in ns:extra.setdefault(v,[]).append(source_n+j)
    expected={160050:5121600,161150:5192000,166650:5544000,56862:1535274,56943:1539648}[a.order]
    count=0
    with a.output.open('x') as out:
        if a.order in [160050,161150,166650]:out.write(f'{a.order} {expected}\n')
        for u in range(a.order):
            ns=source_ns(u)|set(extra.get(u,[])) if u<source_n else pins[u-source_n]
            for v in sorted(v for v in ns if v>u):out.write(f'{u} {v}\n');count+=1
    if count!=expected:raise ValueError((count,expected))
    print(json.dumps({'order':a.order,'edges_written':count,'output':str(a.output)}))
if __name__=='__main__':main()
