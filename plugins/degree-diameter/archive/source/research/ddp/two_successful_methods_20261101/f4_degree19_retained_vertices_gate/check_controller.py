#!/usr/bin/env python3
"""One controller/rank gate; no graph generation, BFS, solver or source edits."""
import json
import time
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'f4_c60_edge_projective'

def mul(a,b):
    c=0
    while b:
        if b&1: c ^= a
        b >>= 1
        a <<= 1
        if a&4: a ^= 7
    return c

def add(*vectors):
    out=[0,0,0]
    for vec in vectors:
        for i in range(3): out[i] ^= vec[i]
    return out

def mv(A,x):
    return [mul(row[0],x[0]) ^ mul(row[1],x[1]) ^ mul(row[2],x[2]) for row in A]

def determinant(cols):
    a,b,c=cols
    return mul(a[0],mul(b[1],c[2]) ^ mul(b[2],c[1])) ^ mul(a[1],mul(b[0],c[2]) ^ mul(b[2],c[0])) ^ mul(a[2],mul(b[0],c[1]) ^ mul(b[1],c[0]))

def main():
    start=time.process_time()
    assert (HERE/'PRED.json').exists()
    P=json.loads((SOURCE/'PARAMETERS.json').read_text())
    C,T,L,inv=(P[k] for k in ['controller','dart_matrices','directions','inverse_ports'])
    paths=defaultdict(list)
    within2=[]
    for a in range(60):
        close={a,*C[a]}
        close.update(C[b][q] for b in C[a] for q in range(5))
        within2.append(close)
        for p,b in enumerate(C[a]):
            for q,c in enumerate(C[b]):
                for r,d in enumerate(C[c]):
                    paths[a,d].append(([a,b,c,d],[p,q,r]))
    unique=[]
    starts=defaultdict(list)
    rank_hist=Counter()
    for (a,d), routes in sorted(paths.items()):
        if d in within2[a] or len(routes)!=1: continue
        vertices,ports=routes[0]
        _,b,c,_=vertices;p,q,r=ports
        columns=[mv(T[c][r],mv(T[b][q],L[inv[p]])),mv(T[c][r],L[inv[q]]),L[inv[r]]]
        det=determinant(columns)
        rank_hist[str(det)]+=1
        row={'source':a,'target':d,'vertices':vertices,'ports':ports,'noise_columns':columns,'determinant':det,'controller_distance':3,'number_controller_length3_walks':1}
        unique.append(row)
        if det: starts[a,p].append(row)
    missing=[[a,p] for a in range(60) for p in range(5) if (a,p) not in starts]
    witnesses=[{'dart':[a,p],**starts[a,p][0]} for a in range(60) for p in range(5) if (a,p) in starts]
    certificate={'unique_distance3_pairs':unique,'first_dart_witnesses':witnesses,'missing_first_darts':missing}
    (HERE/'CONTROLLER_CERTIFICATE.json').write_text(json.dumps(certificate,indent=2)+'\n')
    literal=None
    if witnesses:
        w=witnesses[0]
        # One endpoint pair, from the literal source table, rather than a root BFS.
        root=64*w['source'];target=64*w['target']
        adjacency=[[] for _ in range(3840)]
        with (SOURCE/'graph_d20_D3_n3840.edges').open() as f:
            header=[int(v) for v in next(f).split()]
            assert header==[3840,38400]
            for line in f:
                a,b=map(int,line.split());adjacency[a].append(b);adjacency[b].append(a)
        paths03=[]
        if root==target: paths03.append([root])
        for b in adjacency[root]:
            if b==target: paths03.append([root,b])
            for c in adjacency[b]:
                if c==target: paths03.append([root,b,c])
                for d in adjacency[c]:
                    if d==target: paths03.append([root,b,c,d])
        expected=[64*v for v in w['vertices']]
        assert paths03==[expected],(paths03,expected)
        literal={'source':root,'target':target,'unique_path':expected,'length_le3_path_count':len(paths03),'edge_essential_example':expected[:2],'literal_source_read_once':True,'BFS_roots':0}
        (HERE/'LITERAL_SINGLE_PAIR_CHECK.json').write_text(json.dumps(literal,indent=2)+'\n')
    result={'status':'ALL_DARTS_UNIQUE_RANK3_WITNESS' if not missing else 'FIRST_DART_PREDICTION_REFUTED','controller_vertices':60,'controller_darts':300,'controller_length3_walks_enumerated':sum(map(len,paths.values())),'unique_distance3_pairs':len(unique),'rank3_unique_pairs':sum(v for k,v in rank_hist.items() if k!='0'),'determinant_histogram':dict(sorted(rank_hist.items())),'covered_first_darts':len(witnesses),'first_dart_witness_count_histogram':dict(sorted(Counter(len(starts[a,p]) for a in range(60) for p in range(5)).items())),'missing_first_darts':missing,'all_lifted_undirected_edges_certified_essential':38400 if not missing else None,'targeted_literal_endpoint_pairs':1 if literal else 0,'source_BFS_roots':0,'graphs_generated':0,'solver_calls':0,'Lean_rebuilds':0,'CPU_seconds':time.process_time()-start,'CPU_budget_seconds':60,'scope':'Fixed original3840 vertex graph, pure edge deletion only; not general19D3, rewiring or vertex deletion.'}
    (HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    (HERE/'TERMINAL.json').write_text(json.dumps({'status':result['status'],'running':False,'graphs_added':0,'source_modified':False,'next':'Stop pure edge thinning if all darts covered; no matching/seed/solver continuation.'},indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__': main()
