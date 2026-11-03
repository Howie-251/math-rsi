#!/usr/bin/env python3
"""Generate any literal H9-extension example listed in families.json, without searching."""
import argparse
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
PROJECT=HERE.parents[3]


def read_base(path, expected):
    adjacency=[]
    with path.open() as stream:
        for line in stream:
            if not line.strip() or line.startswith('#'):
                continue
            row=list(map(int,line.split()))
            if row[0]!=len(adjacency):
                raise ValueError('base rows must use consecutive labels starting at 0')
            adjacency.append(row[1:])
    n=expected['n']
    if len(adjacency)!=n:
        raise ValueError('base order differs from the family parameters')
    for u,neighbors in enumerate(adjacency):
        if len(neighbors)!=len(set(neighbors)) or any(v==u or v<0 or v>=n for v in neighbors):
            raise ValueError('base adjacency is not simple')
    neighbor_sets=list(map(set,adjacency))
    if any(u not in neighbor_sets[v] for u,neighbors in enumerate(adjacency) for v in neighbors):
        raise ValueError('base adjacency is not symmetric')
    edges={(u,v) for u,neighbors in enumerate(adjacency) for v in neighbors if u<v}
    if len(edges)!=expected['m']:
        raise ValueError('base edge count differs from the family parameters')
    return list(map(len,adjacency)),edges


def read_edge_set(path):
    with path.open() as stream:
        n,m=map(int,stream.readline().split())
        rows=[tuple(sorted(map(int,line.split()))) for line in stream if line.strip()]
    return n,m,rows,set(rows)


def construct(family,order,source):
    if order not in family['example_orders']:
        raise ValueError(f"order must be one of {family['example_orders']}")
    degree,edges=read_base(source,family['base'])
    cap=family['degree']
    base_edges=len(edges)
    applied=[]
    for step in family['steps']:
        if step['new_n']>order:
            break
        n=len(degree)
        assert step['source_n']==step['new_vertex']==n
        assert step['source_m']==len(edges)
        pins=step['pins']
        assert pins==sorted(set(pins)) and len(pins)==step['new_vertex_degree']<=cap
        assert all(0<=v<n and degree[v]<cap for v in pins)
        assert sorted(step['mandatory_pins']+step['anchors'])==pins
        actual_old_degrees=[degree[v] for v in pins]
        assert actual_old_degrees==step['old_pin_degrees']
        for v in pins:
            edges.add((v,n));degree[v]+=1
        degree.append(len(pins))
        assert len(degree)==step['new_n'] and len(edges)==step['new_m']
        assert max(degree)<=cap
        applied.append(n)
    assert len(degree)==order
    return edges,dict(degree_parameter=cap,n=order,m=len(edges),min_degree=min(degree),
                      max_degree=max(degree),source_n=family['base']['n'],source_m=base_edges,
                      steps_applied=len(applied),new_vertex_labels=applied,
                      all_old_edges_preserved=True,degree_label_cardinality_checks_passed=True,
                      D5_basis='Fixed per-step complete current-baseR4 certificates; see families.json',
                      BFS_performed=False)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--degree',type=int,choices=[11,12,13],required=True)
    parser.add_argument('--order',type=int,required=True)
    parser.add_argument('--output',type=Path,help='Write a rebuilt n/m edge list to this path')
    parser.add_argument('--source',type=Path,help='Override the project-saved original author raw adjacency')
    parser.add_argument('--families',type=Path,default=HERE/'families.json')
    parser.add_argument('--dry-run',action='store_true',help='Construct in memory only; never write a graph')
    parser.add_argument('--compare',type=Path,help='Compare to a saved edge list without BFS')
    args=parser.parse_args()
    if not args.dry_run and args.output is None:
        parser.error('--output is required unless --dry-run is used')
    parameters=json.loads(args.families.read_text())
    family=parameters['families'][str(args.degree)]
    source=args.source or PROJECT/family['base']['project_file']
    edges,report=construct(family,args.order,source)
    report.update(dry_run=args.dry_run,graph_written=False)
    if args.compare:
        n,m,rows,actual=read_edge_set(args.compare)
        report['comparison']=dict(file=str(args.compare),header_matches=n==args.order and m==len(edges),
                                  edge_set_matches=actual==edges,repeated_edges=len(rows)-len(actual),
                                  missing_edges=len(edges-actual),extra_edges=len(actual-edges))
        c=report['comparison']
        assert c['header_matches'] and c['edge_set_matches'] and c['repeated_edges']==0
    if not args.dry_run:
        with args.output.open('w') as stream:
            stream.write(f"{report['n']} {report['m']}\n")
            for u,v in sorted(edges):
                stream.write(f'{u} {v}\n')
        report.update(graph_written=True,output=str(args.output))
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
