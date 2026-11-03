#!/usr/bin/env python3
"""Only C60 short words and a four-by-four matching necessary condition."""
import itertools
import json
import os
import resource
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'f7_c60_d35/PARAMETERS.json'

def save(name, obj):
    (HERE / name).write_text(json.dumps(obj, indent=2) + '\n')

def matching(rows, cols, forced):
    allowed = [(i,j) for i in rows for j in cols if (i,j) not in forced]
    for k in range(4,-1,-1):
        for pairs in itertools.combinations(allowed,k):
            if len({a for a,b in pairs}) == k and len({b for a,b in pairs}) == k:
                return k, [list(z) for z in pairs]

def main():
    start = time.process_time()
    resource.setrlimit(resource.RLIMIT_CPU,(5,5))
    save('HANDLE.json',{'status':'RUNNING','pid':os.getpid(),'CPU_limit':5})
    obj=json.loads(SOURCE.read_text()); C=obj['controller']; inv=obj['inverse_ports']
    assert len(C)==60 and inv==[1,0,3,2,4]
    paths=[[[] for _ in range(60)] for _ in range(60)]
    short2=[{u}|set(C[u])|{z for v in C[u] for z in C[v]} for u in range(60)]
    for u in range(60):
        for p,q,r in itertools.product(range(5),repeat=3):
            if q==inv[p] or r==inv[q]: continue
            a=C[u][p];b=C[a][q];v=C[b][r]
            paths[u][v].append(([u,a,b,v],[p,q,r]))
    forced={(a,p):{} for a in range(60) for p in range(5)}
    witnesses=[]
    for u in range(60):
        for v in range(60):
            if v in short2[u] or len(paths[u][v])!=1: continue
            vertices,ports=paths[u][v][0]
            a,b=vertices[1:3];p,q,r=ports
            i,j=inv[p],r
            rec={'endpoints':[u,v],'vertices':vertices,'ports':ports,
                 'central_dart':[a,b,q],'turn':[i,j]}
            witnesses.append(rec)
            forced[a,q].setdefault((i,j),[]).append([u,v])
    edges=[]
    for (a,p),cells in forced.items():
        b=C[a][p];r=inv[p]
        rows=[i for i in range(5) if i!=p]
        cols=[j for j in range(5) if j!=r]
        m,cert=matching(rows,cols,cells)
        edges.append({'source':a,'target':b,'port':p,'reverse_port':r,
            'forced_turn_count':len(cells),
            'forced_turns':[{'turn':list(k),'endpoint_witnesses':v} for k,v in sorted(cells.items())],
            'unforced_maximum_matching_size':m,'matching':cert,
            'local_F4_necessary_gate':m>=3})
    groups=[]
    for p in range(5):
        cells=set().union(*(set(forced[a,p]) for a in range(60)))
        m,cert=matching([i for i in range(5) if i!=p],
                        [j for j in range(5) if j!=inv[p]],cells)
        groups.append({'port':p,'forced_turns':[list(x) for x in sorted(cells)],
                       'forced_turn_count':len(cells),'unforced_maximum_matching_size':m,
                       'matching':cert,'necessary_gate':m>=3})
    save('FORCED_TURNS.json',{'directed_edges':edges,'global_port_groups':groups})
    save('UNIQUE_DISTANCE3_PATHS.json',witnesses)
    fail=[e for e in edges if not e['local_F4_necessary_gate']]
    result={'status':'EXCLUDED_LOCAL_ARC_FRAME_DOMAIN' if fail else 'LOCAL_MATCHING_GATE_SUPPORTED',
        'literal_controller_source':'../f7_c60_d35/PARAMETERS.json',
        'all_NB3_words':sum(len(x) for row in paths for x in row),
        'ordered_pairs':3600,'unique_distance3_pairs':len(witnesses),
        'directed_edges_checked':len(edges),'failed_directed_edges':len(fail),
        'forced_turn_count_histogram':dict(Counter(e['forced_turn_count'] for e in edges)),
        'unforced_matching_histogram':dict(Counter(e['unforced_maximum_matching_size'] for e in edges)),
        'global_port_groups':groups,'first_failure':fail[0] if fail else None,
        'CPU_seconds':time.process_time()-start,'pid':os.getpid(),
        'graph_generated':False,'graph_BFS':False,'matrices_enumerated':0,
        'scope':'C60 fixed; F4^3 fibers; each vertex has a shared five-direction arc frame; arbitrary invertible edge charts, true inverse/noise-line consistency.'}
    save('RESULT.json',result)
    save('HANDLE.json',{'status':'TERMINAL','pid':os.getpid(),'return_code':0,'CPU_seconds':result['CPU_seconds']})
    print(json.dumps(result),flush=True)

if __name__=='__main__':main()
