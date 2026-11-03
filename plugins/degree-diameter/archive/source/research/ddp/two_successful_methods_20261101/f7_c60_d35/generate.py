#!/usr/bin/env python3
"""Deterministic one-graph generator from saved parameters; no BFS or search."""
import json
import os
import resource
import time
from pathlib import Path

HERE=Path(__file__).resolve().parent
def save(name,value):
    (HERE/name).write_text(json.dumps(value,indent=2)+'\n')

def main():
    start=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(20,20))
    save('GENERATION_HANDLE.json',{'status':'RUNNING','pid':os.getpid(),'CPU_limit':20})
    gate=json.loads((HERE/'GATE_RESULT.json').read_text())
    assert gate['status']=='PASS_SIX_CHARTS_AND_ALL_C60_PAIRS'
    P=json.loads((HERE/'PARAMETERS.json').read_text())
    C,T,L,inv,assignment=(P[k] for k in ['controller','matrices','directions','inverse_ports','dart_chart_index'])
    n=P['order'];G=[set() for _ in range(n)]
    tables=[]
    for ci,M in enumerate(T):
        p=P['chart_ports'][ci];d=L[inv[p]];table=[]
        for code in range(343):
            x=[code%7,code//7%7,code//49]
            y=[sum(a*b for a,b in zip(row,x))%7 for row in M]
            table.append([sum(((y[j]+t*d[j])%7)*7**j for j in range(3)) for t in range(7)])
        tables.append(table)
    for u,row in enumerate(C):
        for p,v in enumerate(row):
            table=tables[assignment[u][p]]
            for x,targets in enumerate(table):
                G[343*u+x].update(343*v+y for y in targets)
    assert all(len(row)==35 and u not in row for u,row in enumerate(G))
    assert all(u in G[v] for u,row in enumerate(G) for v in row)
    m=sum(map(len,G))//2
    assert n==20580 and m==360150
    out=HERE/'graph_d35_D3_n20580.edges'
    with out.open('w') as f:
        f.write(f'{n} {m}\n')
        for u,row in enumerate(G):
            for v in sorted(row):
                if u<v:f.write(f'{u} {v}\n')
    result={'status':'COMPLETE_LITERAL_GRAPH_GENERATED_WITH_ALL_PAIR_ROUTE_CERTIFICATE',
        'pid':os.getpid(),'CPU_seconds':time.process_time()-start,'budget_seconds':20,
        'n':n,'m':m,'min_degree':35,'max_degree':35,'simple':True,'undirected':True,
        'edge_file':str(out.relative_to(HERE)),
        'D_upper_bound':3,'D_upper_bound_evidence':'All3600 controller pairs + six local inverse/direction/full-rank/eight-plane certificates; proof in PROOF.md.',
        'diameter_exact_by_Moore_lower_bound':3,'Moore_degree35_D2':1226,
        'graph_BFS_performed':False,'independent_validation':'PENDING_ROOT_ARRANGED',
        'global_record_claim':False,'latest_global_record_status':'UNRESOLVED',
        'old1620_or3750_reverified':False}
    save('GENERATION_RESULT.json',result)
    save('GENERATION_HANDLE.json',{'status':'TERMINAL','pid':os.getpid(),'return_code':0,'CPU_seconds':result['CPU_seconds']})
    print(json.dumps(result),flush=True)

if __name__=='__main__':main()
