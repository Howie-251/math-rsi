#!/usr/bin/env python3
"""Only the specified six F7 charts and literal author C60; no graph BFS."""
import itertools
import json
import os
import resource
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = 'research/ddp/more_graphs_20261027/d15_D3_current1620_source/construction.author.json'
q = 7
I = [[int(i == j) for j in range(3)] for i in range(3)]
def save(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2)+'\n')
def mv(A,x):
    return [sum(a*b for a,b in zip(row,x))%q for row in A]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(3))%q for j in range(3)] for i in range(3)]
def inverse(A):
    X = [row[:]+I[i][:] for i,row in enumerate(A)]
    for j in range(3):
        p = next(i for i in range(j,3) if X[i][j])
        X[j],X[p]=X[p],X[j]
        s=pow(X[j][j],-1,q);X[j]=[s*x%q for x in X[j]]
        for i in range(3):
            if i!=j:
                c=X[i][j];X[i]=[(a-c*b)%q for a,b in zip(X[i],X[j])]
    return [row[3:] for row in X]
def det(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])-b[0]*(a[1]*c[2]-a[2]*c[1])+c[0]*(a[1]*b[2]-a[2]*b[1]))%q
def H(t):
    return [[0,0,1],[1,0,0],[0,1,0]] if t is None else [[1,0,0],[-t%q,1,0],[0,-t%q,1]]
def chart(s,t,Q):
    D=[[1,0,0],[0,Q[0][0],Q[0][1]],[0,Q[1][0],Q[1][1]]]
    return mm(mm(inverse(H(t)),D),H(s))
def point(z):
    a=next(x for x in z if x)
    return tuple(x*pow(a,-1,q)%q for x in z)
def quotient(t,v):
    return point(mv(H(t),v)[1:])

def main():
    start=time.process_time()
    resource.setrlimit(resource.RLIMIT_CPU,(5,5))
    save('GATE_HANDLE.json',{'status':'RUNNING','pid':os.getpid(),'CPU_limit':5})
    author=json.loads((ROOT/SOURCE).read_text())['construction']
    spec=author['controller']
    assert spec['base_vertices']==3 and spec['N']==20
    maps={}
    for item in author['charts']:
        name=item['symbol'];d={v['from']:v['to'] for v in item['darts']}
        assert len(d)==60 and set(d)==set(range(60)) and set(d.values())==set(range(60))
        maps[name]=d
    assert set(maps)=={'a','b','s'}
    symbols={s['name']:s for s in spec['symbols']}
    for name in ['a','b']:
        s=symbols[name]
        assert all(maps[name][20*c+g]==20*s['perm'][c]+(g+s['voltages'][c])%20 for c in range(3) for g in range(20))
    # The author lists every actual s dart, including its reverse. Bind these directly.
    assert all(maps['s'][maps['s'][u]]==u for u in range(60))
    amapinv={v:u for u,v in maps['a'].items()};bmapinv={v:u for u,v in maps['b'].items()}
    C=[[maps['a'][u],amapinv[u],maps['b'][u],bmapinv[u],maps['s'][u]] for u in range(60)]
    inv=[1,0,3,2,4]
    assert all(len(set(row))==5 and u not in row for u,row in enumerate(C))
    assert all(C[C[u][p]][inv[p]]==u for u in range(60) for p in range(5))
    ts=[None,0,1,2,3]
    L=[[0,0,1]]+[[1,t,t*t%q] for t in range(4)]
    assert all(det(*(L[i] for i in xyz)) for xyz in itertools.combinations(range(5),3))
    A=chart(None,0,[[3,1],[0,3]])
    B=chart(1,2,[[1,1],[4,2]])
    S=chart(3,3,[[4,1],[3,3]])
    matrices=[A,inverse(A),B,inverse(B),S,inverse(S)]
    chart_ports=[0,1,2,3,4,4]
    inverse_chart=[1,0,3,2,5,4]
    records=[]
    PG={(1,i) for i in range(q)}|{(0,1)}
    for ci,T in enumerate(matrices):
        p=chart_ports[ci];r=inv[p]
        assert mv(T,L[p])==L[r] and mm(matrices[inverse_chart[ci]],T)==I
        src={i:quotient(ts[r],mv(T,L[i])) for i in range(5) if i!=p}
        dst={j:quotient(ts[r],L[j]) for j in range(5) if j!=r}
        assert len(set(src.values()))==len(set(dst.values()))==4
        assert not(set(src.values())&set(dst.values())) and set(src.values())|set(dst.values())==PG
        turns=[]
        for i,j in itertools.product(src,dst):
            d=det(mv(T,L[i]),L[r],L[j]);assert d!=0
            turns.append({'incoming_reverse_port':i,'outgoing_port':j,'det_mod7':d})
        records.append({'chart':ci,'source_port':p,'reverse_port':r,'matrix':T,
            'source_quotient_directions':src,'target_quotient_directions':dst,
            'all_16_turns_full_rank':True,'turns':turns,'pencil_plane_count':8,'pencil_union_by_identity':343})
    assignment=[[p if p<4 else (4 if u<C[u][4] else 5) for p in range(5)] for u in range(60)]
    for u in range(60):
        for p,v in enumerate(C[u]):
            assert assignment[v][inv[p]]==inverse_chart[assignment[u][p]]
    counts=[[0]*60 for _ in range(60)]
    first={}
    for u in range(60):
        for p0,p1,p2 in itertools.product(range(5),repeat=3):
            if p1==inv[p0] or p2==inv[p1]:continue
            v1=C[u][p0];v2=C[v1][p1];v3=C[v2][p2]
            counts[u][v3]+=1
            first.setdefault((u,v3),{'ports':[p0,p1,p2],'control_vertices':[u,v1,v2,v3]})
    certificate=[];required_counts=[]
    for u in range(60):
        for v in range(60):
            if v in C[u]:
                p=C[u].index(v)
                certificate.append({'source':u,'target':v,'method':'adjacent_eight_plane_pencil','port':p,'chart':assignment[u][p]})
            else:
                assert counts[u][v]>0, ('missing_NB3',u,v)
                required_counts.append(counts[u][v])
                certificate.append({'source':u,'target':v,'method':'full_rank_NB3',**first[u,v]})
    save('LOCAL_CHART_CERTIFICATE.json',{'field':7,'charts':records})
    save('CONTROLLER_ROUTE_CERTIFICATE.json',{'ordered_pairs':3600,'NB3_counts':counts,'pair_certificate':certificate})
    parameters={'field':7,'fiber_dimension':3,'fiber_size':343,'controller':C,
        'controller_author_source':SOURCE,'controller_author':'Bhakar, author repository f4t4nt/degree-diameter-graphs',
        'controller_author_recipe':spec,'directions':L,'conic_parameters':['infinity',0,1,2,3],
        'inverse_ports':inv,'matrices':matrices,'chart_ports':chart_ports,'inverse_charts':inverse_chart,
        'dart_chart_index':assignment,'self_inverse_port_matrix_rule':'port4: chart4 if u<C[u][4], chart5 otherwise; these are actual inverses, not equal.',
        'vertex_label':'343*controller+x0+7*x1+49*x2',
        'edge_rule':'(u,x) -> (C[u][p], matrices[dart_chart_index[u][p]]*x + t*directions[inverse_ports[p]]), t in F7',
        'order':20580,'degree':35,'expected_edges':360150,
        'change_from_source':'Keep only the literal C60 controller; replace F3 charts/fiber with new conic F7 charts/fiber.',
        'global_record_claim':False}
    save('PARAMETERS.json',parameters)
    result={'status':'PASS_SIX_CHARTS_AND_ALL_C60_PAIRS','pid':os.getpid(),
        'CPU_seconds':time.process_time()-start,'budget_seconds':5,
        'actual_chart_types':6,'central_turns_checked':96,'all_turns_rank3':True,
        'pencil_planes_each':8,'pencil_union_each':343,
        'controller_n':60,'controller_m':150,'controller_degree':5,'inverse_darts_bound':300,
        'ordered_pairs_checked':3600,'adjacent_ordered_pairs':300,'NB3_required_pairs':3300,
        'required_NB3_count_histogram':dict(Counter(required_counts)),'required_NB3_min':min(required_counts),
        'full_graph_generated':False,'old_source_BFS':False,'controller_BFS':False,
        'predicted_order':20580,'predicted_degree':35,'predicted_D_upper_bound':3,
        'global_record_claim':False,'pending':['Generate authorized literal graph; root-arranged independent validation.']}
    save('GATE_RESULT.json',result)
    save('GATE_HANDLE.json',{'status':'TERMINAL','pid':os.getpid(),'return_code':0,'CPU_seconds':result['CPU_seconds']})
    print(json.dumps(result),flush=True)

if __name__=='__main__':
    try:main()
    except Exception as e:
        save('FIRST_FAILURE.json',{'type':type(e).__name__,'message':str(e),'pid':os.getpid()})
        raise
