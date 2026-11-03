#!/usr/bin/env python3
"""Semilinear field/shift/domain and exact72controller unique-route gates.
No old-source BFS, fiber graph, solver or Lean is run here.
"""
import itertools
import json
import time
from collections import Counter,defaultdict
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
L=[(0,0,1)]+[(1,t,(0,1,3,2)[t]) for t in range(4)]
N=(0,1,0)
INV=(0,1,3,2)

def mul(a,b):
    out=0
    while b:
        if b&1:out^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return out
def square(a):return mul(a,a)
def frob(v,s):return tuple(square(a) for a in v) if s else tuple(v)
def dot(a,b):
    out=0
    for x,y in zip(a,b):out^=mul(x,y)
    return out
def mv(A,x):return tuple(dot(row,x) for row in A)
def invert(A):
    n=len(A);R=[list(row)+[int(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next(k for k in range(j,n) if R[k][j]);R[j],R[k]=R[k],R[j]
        z=INV[R[j][j]];R[j]=[mul(z,x) for x in R[j]]
        for k in range(n):
            if k==j:continue
            z=R[k][j]
            R[k]=[x^mul(z,y) for x,y in zip(R[k],R[j])]
    return [row[n:] for row in R]
def norm(x):
    z=next(z for z in x if z)
    return tuple(mul(INV[z],a) for a in x)
def apply(T,x):return mv(T['A'],frob(x,T['sigma']))
def save(path,data):path.write_text(json.dumps(data,indent=2)+'\n')

def maps():
    out=[];pgl=[];points={p:i for i,p in enumerate(L)}
    for vals in itertools.product(range(4),repeat=4):
        a,b,c,d=vals;det=mul(a,d)^mul(b,c)
        if not det:continue
        if next(z for z in vals if z)!=1:continue
        pgl.append(vals)
        M=[[square(a),0,square(b)],[mul(a,c),det,mul(b,d)],[square(c),0,square(d)]]
        for sigma in range(2):
            alpha=2 if sigma==0 else 3;s=mul(alpha,INV[det])
            A=[[mul(s,z) for z in row] for row in M]
            AI=invert(A);B=[list(frob(row,sigma)) for row in AI]
            T={'h':[[a,b],[c,d]],'det_h':det,'sigma':sigma,'scale':s,'alpha':alpha,'A':A,'reverse_A':B}
            R={'A':B,'sigma':sigma}
            T['conic_permutation']=[points[norm(apply(T,p))] for p in L]
            T['reverse_conic_permutation']=[points[norm(apply(R,p))] for p in L]
            assert sorted(T['conic_permutation'])==list(range(5))
            assert all(T['reverse_conic_permutation'][T['conic_permutation'][p]]==p for p in range(5))
            assert apply(T,N)==(0,alpha,0)
            ralpha=3
            assert apply(R,N)==(0,ralpha,0)
            for U,al in [(T,alpha),(R,ralpha)]:
                assert {1,2,al,mul(al,square(2) if sigma else 2)}=={1,2,3}
            for x in itertools.product(range(4),repeat=3):
                assert apply(R,apply(T,x))==x and apply(T,apply(R,x))==x
            out.append(T)
    assert len(pgl)==60 and len(out)==120
    assert len({tuple(z['conic_permutation']) for z in out})==120
    domains={(p,r):[i for i,z in enumerate(out) if z['conic_permutation'][p]==r] for p in range(5) for r in range(5)}
    assert all(len(pool)==24 for pool in domains.values())
    return out,domains

def controller_gate(name,path,Ts,domains):
    folder=HERE/name;folder.mkdir(exist_ok=True)
    C=[set() for _ in range(72)]
    with path.open() as f:
        assert tuple(map(int,next(f).split()))==(72,180)
        for line in f:
            a,b=map(int,line.split());assert a!=b;C[a].add(b);C[b].add(a)
    C=[sorted(row) for row in C]
    assert all(len(row)==5 for row in C)
    reverse=[[C[v].index(u) for v in row] for u,row in enumerate(C)]
    edges=[];dart={}
    for u,row in enumerate(C):
        for p,v in enumerate(row):
            if u>=v:continue
            r=reverse[u][p];ei=len(edges)
            edges.append({'edge':ei,'source':u,'target':v,'port':p,'reverse_port':r,'all24_maps':domains[p,r]})
            dart[u,p]=(ei,False);dart[v,r]=(ei,True)
    assert len(edges)==180
    routes=defaultdict(list);close=[]
    for u in range(72):
        short={u,*C[u]};short.update(C[a][q] for a in C[u] for q in range(5));close.append(short)
        for p,a in enumerate(C[u]):
            for q,b in enumerate(C[a]):
                for r,v in enumerate(C[b]):
                    ei,rev=dart[a,q]
                    i=reverse[u][p];j=r
                    normal=[j,i] if rev else [i,j]
                    routes[u,v].append({'vertices':[u,a,b,v],'ports':[p,q,r],'central_edge':ei,'reverse':rev,'middle_incoming_port':i,'middle_outgoing_port':j,'normalized_forbidden_entry':normal})
    required=[];unique=[];constraints=[{} for _ in edges]
    allreachable=0
    for u in range(72):
        assert close[u]|{v for v in range(72) if routes[u,v]}==set(range(72))
        for v in range(72):
            if v in close[u]:continue
            ws=routes[u,v];assert ws
            row={'source':u,'target':v,'word_count':len(ws),'words':ws}
            required.append(row)
            if len(ws)==1:
                w=ws[0];unique.append(row);key=tuple(w['normalized_forbidden_entry'])
                constraints[w['central_edge']].setdefault(key,[]).append({'source':u,'target':v,'word':w})
    empty=[];hist=Counter()
    for e,cs in zip(edges,constraints):
        allowed=[];removed=[]
        for mi in e['all24_maps']:
            perm=Ts[mi]['conic_permutation']
            bad=[key for key in cs if perm[key[0]]==key[1]]
            if bad:
                key=bad[0];removed.append({'map_index':mi,'forbidden_entry':key,'unique_route_witness':cs[key][0]})
            else:allowed.append(mi)
        e['unique_forbidden_entries']=[{'entry':key,'ordered_unique_pairs':pairs} for key,pairs in sorted(cs.items())]
        e['surviving_maps']=allowed;e['eliminated_maps']=removed;hist[len(allowed)]+=1
        if not allowed:empty.append(e['edge'])
    save(folder/'INPUT.json',{'source_path':str(path.relative_to(ROOT)),'controller':C,'reverse_ports':reverse,'directions':L,'nucleus':N,'internal_shift_coefficients':[1,2],'field_polynomial':'w^2+w+1'})
    save(folder/'EDGE_DOMAINS.json',edges)
    save(folder/'DISTANCE3_ROUTES.json',required)
    if empty:save(folder/'EMPTY_EDGE_CERTIFICATE.json',edges[empty[0]])
    result={'status':'UNIQUE_ROUTE_DOMAIN_EMPTY_CONTROLLER_RULE_EXCLUDED' if empty else 'UNIQUE_ROUTE_GATE_PASS_SAT_NOT_RUN','controller_vertices':72,'controller_edges':180,'local_port_convention':'sorted neighbors; reverse actual lookup','length3_controller_words_enumerated':9000,'ordered_distance3_pairs':len(required),'distance3_word_count_histogram':dict(sorted(Counter(x['word_count'] for x in required).items())),'maximum_distance3_word_count':max(x['word_count'] for x in required),'unique_ordered_distance3_pairs':len(unique),'unique_forbidden_entry_counts_per_edge':dict(sorted(Counter(len(x) for x in constraints).items())),'surviving_domain_cardinality_histogram':dict(sorted(hist.items())),'empty_domain_edges':empty,'new_fiber_graphs':0,'solver_calls':0,'old_source_D3_BFS':0}
    save(folder/'UNIQUE_ROUTE_GATE.json',result)
    return result

def main():
    start=time.process_time();assert (HERE/'PRED.json').exists()
    Ts,domains=maps()
    save(HERE/'SEMILINEAR_MAPS.json',Ts)
    save(HERE/'DOMAIN_CHECK.json',{'PGL2_projectivities':60,'semilinear_maps':120,'distinct_conic_permutations':120,'all25_port_pair_domains':24,'reverse_composition_checks':120*64*2,'nucleus_forward_alpha_by_sigma':[2,3],'nucleus_reverse_alpha_by_sigma':[3,3],'forward_and_reverse_C4_shift_union':'{1,2,alpha,alpha*Frob_sigma(2)}={1,2,3} for all120maps','field_polynomial':'w^2+w+1','actual_checks_pass':True})
    sources=[('Exoo72',ROOT/'research/ddp/more_graphs_20261027/d5_exoo72_extension/root_cover_preflight/source.edges'),('Michel72',ROOT/'research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/source/source72.edges')]
    res={name:controller_gate(name,path,Ts,domains) for name,path in sources}
    survivors=[name for name,r in res.items() if not r['empty_domain_edges']]
    result={'status':'BOTH_CONTROLLERS_UNIQUE_ROUTE_DOMAIN_EMPTY' if not survivors else 'CONTROLLER_DOMAIN_SURVIVOR_ONE_SAT_ALLOWED','sources':res,'surviving_controllers':survivors,'preferred_for_single_SAT':survivors[0] if survivors else None,'CPU_seconds':time.process_time()-start,'preprocessing_CPU_budget_seconds':120,'workers':1,'solver_calls':0,'new_graphs':0,'remaining_gate':'One60CPU SAT permitted only if survivor exists and complementary route proof is sound.'}
    save(HERE/'PREPROCESS_RESULT.json',result)
    print(json.dumps(result))

if __name__=='__main__':main()
