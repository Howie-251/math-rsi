#!/usr/bin/env python3
"""Portable deterministic reconstruction, standard-library Python only.

Inputs define source geometry/graph plus fixed choices; graphs/ is never read by
construct_h9 or construct_d12. This packaging adapter changes paths only, not
accepted mathematical choices. Outputs are compared using exact edge sets.
"""
from array import array
from collections import Counter
from pathlib import Path
import argparse,json,time
HERE=Path(__file__).resolve().parent

def read_edges(path):
    with Path(path).open() as f:
        n,m=map(int,next(f).split()); edges=set()
        for row in f:
            if not row.strip():continue
            u,v=map(int,row.split());assert 0<=u<v<n and (u,v) not in edges
            edges.add((u,v))
    assert len(edges)==m
    return n,edges

def write_edges(path,n,edges):
    with Path(path).open('w') as f:
        f.write(f'{n} {len(edges)}\n')
        for u,v in sorted(edges):f.write(f'{u} {v}\n')

def degrees(n,edges):
    d=[0]*n
    for u,v in edges:d[u]+=1;d[v]+=1
    return d

def binary(name,kind,length):
    x=array(kind);x.frombytes((HERE/'inputs'/name).read_bytes())
    # The bundled cache encoding is little-endian, independent of host byte order.
    import sys
    if sys.byteorder!='little' and x.itemsize>1:x.byteswap()
    assert len(x)==length
    return x

def construct_h9(output):
    tau=binary('h9_tau.i32.bin','i',132860);pi=binary('h9_pi.u16.bin','H',66430)
    lines=binary('h9_line_points.i32.bin','i',664300)
    choice=json.loads((HERE/'inputs/h9_parameters.json').read_text())
    classes=json.loads((HERE/'inputs/fold11_classes.json').read_text())
    inverse=[0]*len(tau)
    assert sorted(tau)==list(range(len(tau)))
    for u,v in enumerate(tau):inverse[v]=u
    eps=bytearray(66430)
    for fold in classes['split_fold_ids']:
        p=classes['point_representatives'][fold]
        eps[p]=eps[tau[tau[p]]]=choice['colors'][str(fold)]
    sigma=[tau[p] if eps[p] else inverse[p] for p in range(66430)]
    assert sorted(sigma)==list(range(66430,132860))
    edges=set()
    for p,line in enumerate(sigma):
        for q in lines[10*(line-66430):10*(line-66430+1)]:
            if p==q:continue
            u,v=sorted((pi[p],pi[q]));assert u!=v;edges.add((u,v))
    assert max(pi)==37470 and len(edges)==203747
    n,old=read_edges(HERE/'inputs/h9_source37631.edges');assert (n,len(old))==(37631,205329)
    outside={e for e in old if e[1]>=37471};assert len(outside)==1608
    edges.update(outside)
    # Final PARAMETERS already includes anchor31; the earlier CANDIDATE had10.
    pins=sorted(choice['pins']);assert len(set(pins))==len(pins)==11 and choice['anchor'] in pins
    edges.update((p,37631) for p in pins)
    d=degrees(37632,edges);assert len(edges)==205366 and max(d)==11
    write_edges(output,37632,edges)
    return dict(n=37632,m=len(edges),maximum_degree=max(d),core_edges=203747,retained_exterior_edges=1608,pins=pins,degree_histogram=dict(sorted(Counter(d).items())),distance_scope='Use verify.py: true-H9/sigma/pi core theorem plus all161 remaining roots, not pure old-core retention.')

def construct_d12(output):
    n,edges=read_edges(HERE/'inputs/d12_source42402.edges');assert (n,len(edges))==(42402,245937)
    d=degrees(n,edges);assert max(d)<=12
    additions=json.loads((HERE/'inputs/d12_additions.json').read_text());assert len(additions)==31
    for row in additions:
        assert row['source_n']==row['new_vertex']==n
        pins=row['pins'];assert len(pins)==len(set(pins))<=12
        assert all(0<=p<n and d[p]<12 for p in pins)
        for p in pins:edges.add((p,n));d[p]+=1
        d.append(len(pins));n+=1
    assert n==42433 and len(edges)==246309 and max(d)==12
    write_edges(output,n,edges)
    return dict(n=n,m=len(edges),maximum_degree=max(d),added_vertices=31,all_source_edges_retained=True,degree_histogram=dict(sorted(Counter(d).items())),distance_scope='Use verify.py: inherited actual42402 source D5 plus all31 added roots. Concrete source Lean remains open.')

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--family',choices=['both','11,5','12,5'],default='both');p.add_argument('--output-dir',type=Path,default=HERE/'generated');p.add_argument('--compare',action='store_true');a=p.parse_args();a.output_dir.mkdir(parents=True,exist_ok=True);results=[]
    for family,name,fn in [('11,5','graph_d11_D5_n37632.edges',construct_h9),('12,5','graph_d12_D5_n42433.edges',construct_d12)]:
        if a.family not in ['both',family]:continue
        start=time.process_time();dst=a.output_dir/name;x=fn(dst);x.update(family=family,output=str(dst),CPU_seconds=time.process_time()-start)
        if a.compare:
            n,e=read_edges(dst);rn,re=read_edges(HERE/'graphs'/name)
            x['exact_edge_set_match']=n==rn and e==re;assert x['exact_edge_set_match']
        results.append(x)
    print(json.dumps(results,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
