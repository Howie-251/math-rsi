#!/usr/bin/env python3
"""All projectivities for one literal global five-conic C60 construction."""
import itertools
import json
import os
import resource
import time
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
def save(n,x):(HERE/n).write_text(json.dumps(x,indent=2)+'\n')
def mul(a,b):
    c=0
    while b:
        if b&1:c^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return c
def isum(xs):
    z=0
    for x in xs:z^=x
    return z
def mv(A,v):return [isum(mul(a,b) for a,b in zip(row,v)) for row in A]
def mm(A,B):return [[isum(mul(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def identity(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def fi(a):return next(b for b in range(1,4) if mul(a,b)==1)
def inverse(A):
    n=len(A);X=[r[:]+z[:] for r,z in zip(A,identity(n))]
    for j in range(n):
        k=next(k for k in range(j,n) if X[k][j]);X[k],X[j]=X[j],X[k]
        c=fi(X[j][j]);X[j]=[mul(c,x) for x in X[j]]
        for k in range(n):
            if k!=j:
                c=X[k][j];X[k]=[x^mul(c,y) for x,y in zip(X[k],X[j])]
    return [r[n:] for r in X]
def point(v):
    c=fi(next(x for x in v if x));return tuple(mul(c,x) for x in v)
def normalized(A):
    c=fi(next(x for r in A for x in r if x));return [[mul(c,x) for x in r] for r in A]
def det2(A):return mul(A[0][0],A[1][1])^mul(A[0][1],A[1][0])
def det3(a,b,c):return isum([mul(a[0],mul(b[1],c[2])^mul(b[2],c[1])),mul(a[1],mul(b[0],c[2])^mul(b[2],c[0])),mul(a[2],mul(b[0],c[1])^mul(b[1],c[0]))])
def H(t):return [[0,0,1],[1,0,0],[0,1,0]] if t is None else [[1,0,0],[t,1,0],[0,t,1]]

def main():
    start=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(10,10))
    save('HANDLE.json',{'status':'RUNNING','pid':os.getpid(),'CPU_limit':10})
    source=json.loads((HERE.parent/'f7_c60_d35/PARAMETERS.json').read_text())
    C=source['controller'];inv=source['inverse_ports'];ts=[None,0,1,2,3]
    L=[[0,0,1]]+[[1,t,mul(t,t)] for t in range(4)]
    assert all(det3(*(L[j] for j in ids)) for ids in itertools.combinations(range(5),3))
    hs=[H(t) for t in ts];hsinv=[inverse(M) for M in hs]
    proj=[[None if i==p else point(mv(hs[p],L[i])[1:]) for i in range(5)] for p in range(5)]
    PGL=[]
    for a in itertools.product(range(4),repeat=4):
        Q=[list(a[:2]),list(a[2:])]
        if det2(Q) and normalized(Q)==Q:PGL.append(Q)
    assert len(PGL)==60
    PG={(1,t) for t in range(4)}|{(0,1)}
    words=[[[] for v in range(60)] for u in range(60)]
    nb2=[[[] for v in range(60)] for u in range(60)]
    for u in range(60):
        for p,q in itertools.product(range(5),repeat=2):
            if q!=inv[p]:nb2[u][C[C[u][p]][q]].append([p,q])
        for p,q,r in itertools.product(range(5),repeat=3):
            if q==inv[p] or r==inv[q]:continue
            a=C[u][p];b=C[a][q];v=C[b][r]
            words[u][v].append({'ports':[p,q,r],'vertices':[u,a,b,v],
                                'central_port':q,'turn':[inv[p],r]})
    required=[(u,v) for u in range(60) for v in range(60) if v not in C[u]]
    assert len(required)==3300
    masks=[{(i,j):0 for i in range(5) if i!=p for j in range(5) if j!=inv[p]} for p in range(5)]
    bounds=[]
    for k,(u,v) in enumerate(required):
        for w in words[u][v]:masks[w['central_port']][tuple(w['turn'])]|=1<<k
        b=1+15*len(words[u][v])+(15 if u==v else 15*len(nb2[u][v]))
        bounds.append({'source':u,'target':v,'NB2':len(nb2[u][v]),'NB3':len(words[u][v]),'all_NB3_rank_deficient_union_bound':b})
    necessity=all(z['all_NB3_rank_deficient_union_bound']<64 for z in bounds)
    ext=[]
    for u in range(60):
        for p in [0,1,4]:
            v=C[u][p]
            ext.append({'source':u,'target':v,'port':p,'NB2':len(nb2[u][v]),'NB3':len(words[u][v])})
    external_pencil_necessary=all(z['NB2']==0 and z['NB3']==0 for z in ext)
    forced=json.loads((HERE.parent/'f4_c60_forced_turn_gate/FORCED_TURNS.json').read_text())
    forcedsets=[{tuple(z) for z in x['forced_turns']} for x in forced['global_port_groups']]
    def portinfo(p,Q):
        r=inv[p];images={i:point(mv(Q,proj[p][i])) for i in range(5) if i!=p}
        bad={(i,j) for i in images for j in range(5) if j!=r and images[i]==proj[r][j]}
        good=set(masks[p])-bad;cover=0
        for z in good:cover|=masks[p][z]
        pencil=set(images.values())|{proj[r][j] for j in range(5) if j!=r}
        return {'port':p,'Q':Q,'bad_turns':[list(z) for z in sorted(bad)],'good_turns':[list(z) for z in sorted(good)],
                'pencil_points':[list(z) for z in sorted(pencil)],'pencil_full':pencil==PG,
                'forced_ok':not(bad&forcedsets[p]),'covered_required_pairs':cover.bit_count(),'cover':cover}
    components=[];records=[]
    for p in [0,2,4]:
        cand=[]
        for qi,Q in enumerate(PGL):
            if p==4:
                sq=mm(Q,Q)
                if sq[0][1] or sq[1][0] or sq[0][0]!=sq[1][1]:continue
                mu=next(c for c in range(1,4) if mul(mul(c,c),sq[0][0])==1)
                Q=[[mul(mu,x) for x in row] for row in Q]
                assert mm(Q,Q)==identity(2)
            infos=[portinfo(p,Q)]
            if p!=4:infos.append(portinfo(inv[p],inverse(Q)))
            cm=0
            for z in infos:cm|=z['cover']
            rec={'component_port':p,'PGL_index':qi,'Q':Q,'ports':infos,'cover':cm,
                 'forced_ok':all(z['forced_ok'] for z in infos),'pencil_full':all(z['pencil_full'] for z in infos)}
            cand.append(rec)
            records.append({**{k:v for k,v in rec.items() if k!='cover'},'ports':[{k:v for k,v in z.items() if k!='cover'} for z in infos]})
        components.append(cand)
    assert [len(x) for x in components]==[60,60,16]
    full=(1<<3300)-1;counts=Counter();solutions=[];first=None
    for a,b,s in itertools.product(*components):
        counts['all_projectivity_triples']+=1
        if not all(x['forced_ok'] for x in [a,b,s]):continue
        counts['forced_admissible_triples']+=1
        if a['cover']|b['cover']|s['cover']!=full:continue
        counts['rank_cover_solutions']+=1
        external=a['pencil_full'] and s['pencil_full']
        if external:counts['rank_and_external_pencil_solutions']+=1
        sufficient=external and b['pencil_full']
        if sufficient:
            counts['all_pencil_sufficient_solutions']+=1
            if first is None:first=(a,b,s)
        solutions.append({'PGL_indices':[x['PGL_index'] for x in [a,b,s]],'external_pencil':external,'all_pencil':sufficient})
    for key in ['forced_admissible_triples','rank_cover_solutions','rank_and_external_pencil_solutions','all_pencil_sufficient_solutions']:counts[key]+=0
    save('PROJECTIVITIES.json',records)
    save('SOLUTIONS.json',solutions)
    save('CONTROLLER_WORD_CAPACITY.json',{'required_pairs':bounds,'external_darts':ext,'rank_necessity_count_guard':necessity,
                                         'external_pencil_necessity_guard':external_pencil_necessary})
    status='SUFFICIENT_GRAPH_FOUND' if first else 'NO_FULL_PENCIL_CERTIFICATE'
    if not counts['rank_cover_solutions'] and necessity:status='PURE_LINEAR_GLOBAL_CONIC_DOMAIN_EXCLUDED_BY_RANK_NECESSITY'
    elif not counts['rank_and_external_pencil_solutions'] and necessity and external_pencil_necessary:status='PURE_LINEAR_GLOBAL_CONIC_DOMAIN_EXCLUDED_BY_RANK_AND_EXTERNAL_PENCIL'
    result={'status':status,'pid':os.getpid(),'components':[len(x) for x in components],
        'counts':dict(counts),'rank_necessity_guard':necessity,'rank_deficient_capacity_max':max(z['all_NB3_rank_deficient_union_bound'] for z in bounds),
        'external_pencil_necessity_guard':external_pencil_necessary,'directions':L,'field_polynomial':'w^2+w+1',
        'graph_generated':False,'global_record_claim':False}
    if first:
        T=[None]*5
        for p,rec in zip([0,2,4],first):
            Q=rec['Q'];D=[[1,0,0],[0,Q[0][0],Q[0][1]],[0,Q[1][0],Q[1][1]]]
            T[p]=mm(mm(hsinv[inv[p]],D),hs[p])
            if p!=4:T[inv[p]]=inverse(T[p])
        assert all(mm(T[inv[p]],T[p])==identity(3) and mv(T[p],L[p])==L[inv[p]] for p in range(5))
        route=[]
        for u,v in required:
            w=next(w for w in words[u][v] if det3(mv(T[w['central_port']],L[w['turn'][0]]),L[inv[w['central_port']]],L[w['turn'][1]]))
            route.append({'source':u,'target':v,**w})
        P={'field':4,'field_polynomial':'w^2+w+1','field_encoding':'0,1,w,w+1','fiber_dimension':3,
           'fiber_size':64,'controller':C,'inverse_ports':inv,'directions':L,'matrices':T,
           'PGL_indices':[x['PGL_index'] for x in first],'order':3840,'degree':20,'expected_edges':38400,
           'vertex_label':'64*controller+x0+4*x1+16*x2','edge_rule':'(u,x)->(C[u][p],T[p]*x+t*L[inv[p]]),t in F4',
           'global_record_claim':False}
        save('PARAMETERS.json',P);save('ROUTE_CERTIFICATE.json',route)
        tables=[]
        for p in range(5):
            table=[]
            for x in range(64):
                y=mv(T[p],[x%4,x//4%4,x//16]);d=L[inv[p]]
                table.append([sum((y[j]^mul(t,d[j]))*4**j for j in range(3)) for t in range(4)])
            tables.append(table)
        G=[set() for _ in range(3840)]
        for u in range(60):
            for p,v in enumerate(C[u]):
                for x in range(64):G[64*u+x].update(64*v+y for y in tables[p][x])
        assert all(len(row)==20 and u not in row for u,row in enumerate(G))
        assert all(u in G[v] for u,row in enumerate(G) for v in row)
        with (HERE/'graph_d20_D3_n3840.edges').open('w') as f:
            f.write('3840 38400\n')
            for u,row in enumerate(G):
                for v in sorted(row):
                    if u<v:f.write(f'{u} {v}\n')
        result.update({'graph_generated':True,'n':3840,'m':38400,'simple':True,'undirected':True,'regular_degree':20,
                       'diameter_by_route_certificate_and_Moore2':3,'graph_BFS':False,'independent_validation':'PENDING_ROOT'})
    result['CPU_seconds']=time.process_time()-start
    save('RESULT.json',result);save('HANDLE.json',{'status':'TERMINAL','pid':os.getpid(),'return_code':0,'CPU_seconds':result['CPU_seconds']})
    print(json.dumps(result),flush=True)

if __name__=='__main__':main()
