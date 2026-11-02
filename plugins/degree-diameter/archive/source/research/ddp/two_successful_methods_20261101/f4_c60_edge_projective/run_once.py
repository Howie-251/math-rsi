#!/usr/bin/env python3
"""One finite edge-projectivity CNF and at most one solver invocation."""
import argparse
import importlib.util
import itertools
import json
import math
import os
import resource
import subprocess
import time
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
spec=importlib.util.spec_from_file_location('gf4',HERE.parent/'f4_c60_global_projective/check_once.py')
F=importlib.util.module_from_spec(spec);spec.loader.exec_module(F)
def save(name,obj):(HERE/name).write_text(json.dumps(obj,indent=2)+'\n')
def cpu():return time.process_time()
def childcpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime

def prepare():
    start=cpu()
    P=json.loads((HERE.parent/'f7_c60_d35/PARAMETERS.json').read_text())
    C=P['controller'];inv=P['inverse_ports'];L=[[0,0,1]]+[[1,t,F.mul(t,t)] for t in range(4)]
    H=[F.H(t) for t in [None,0,1,2,3]]
    proj=[[None if i==p else F.point(F.mv(H[p],L[i])[1:]) for i in range(5)] for p in range(5)]
    PG={(1,t) for t in range(4)}|{(0,1)};pgl=[]
    for vals in itertools.product(range(4),repeat=4):
        Q=[list(vals[:2]),list(vals[2:])]
        if F.det2(Q) and F.normalized(Q)==Q:pgl.append(Q)
    assert len(pgl)==60
    def info(p,Q):
        r=inv[p];im={i:F.point(F.mv(Q,proj[p][i])) for i in range(5) if i!=p}
        pts=set(im.values())|{proj[r][j] for j in range(5) if j!=r}
        good=[[i,j] for i in im for j in range(5) if j!=r and im[i]!=proj[r][j]]
        return {'pencil_full':pts==PG,'good_turns':good}
    templates=[]
    for p in range(5):
        pool=[]
        for qi,Q in enumerate(pgl):
            fw=info(p,Q);rv=info(inv[p],F.inverse(Q))
            assert fw['pencil_full']==rv['pencil_full']
            if fw['pencil_full']:pool.append({'PGL_index':qi,'Q':Q,'forward':fw,'reverse':rv})
        assert len(pool)==48;templates.append(pool)
    edges=[];dart={};nv=0
    for u in range(60):
        for p,v in enumerate(C[u]):
            if u>=v:continue
            assert C[v][inv[p]]==u
            idx=len(edges);pool=[]
            for t in templates[p]:
                nv+=1;pool.append({'selector':nv,**t})
            edges.append({'edge':idx,'source':u,'target':v,'port':p,'reverse_port':inv[p],'choices':pool})
            dart[u,p]=(idx,False);dart[v,inv[p]]=(idx,True)
    assert len(edges)==150 and nv==7200
    clauses=[]
    for e in edges:
        xs=[z['selector'] for z in e['choices']];clauses.append(xs)
        ss=list(range(nv+1,nv+len(xs)));nv+=len(xs)-1
        clauses.append([-xs[0],ss[0]])
        for i in range(1,len(xs)-1):
            clauses.extend([[-xs[i],ss[i]],[-ss[i-1],ss[i]],[-xs[i],-ss[i-1]]])
        clauses.append([-xs[-1],-ss[-1]])
    nb=[[] for _ in range(3600)]
    for u in range(60):
        for p,q,r in itertools.product(range(5),repeat=3):
            if q==inv[p] or r==inv[q]:continue
            a=C[u][p];b=C[a][q];v=C[b][r]
            ei,rev=dart[a,q]
            nb[60*u+v].append({'ports':[p,q,r],'vertices':[u,a,b,v],
                               'central_edge':ei,'reverse':rev,'turn':[inv[p],r]})
    required=[]
    for u in range(60):
        for v in range(60):
            if v in C[u]:continue
            ws=nb[60*u+v];covered=set()
            for w in ws:
                side='reverse' if w['reverse'] else 'forward'
                covered.update(z['selector'] for z in edges[w['central_edge']]['choices'] if w['turn'] in z[side]['good_turns'])
            clauses.append(sorted(covered))
            required.append({'source':u,'target':v,'clause':sorted(covered),'words':ws})
    assert len(required)==3300
    with (HERE/'model.cnf').open('w') as f:
        f.write(f'p cnf {nv} {len(clauses)}\n')
        for c in clauses:f.write(' '.join(map(str,c))+' 0\n')
    save('SELECTOR_MAP.json',edges)
    save('PAIR_COVERAGE.json',required)
    save('INPUT.json',{'controller':C,'inverse_ports':inv,'directions':L,'field_polynomial':'w^2+w+1'})
    result={'status':'PREPARED_NOT_SOLVED','pid':os.getpid(),'prepare_CPU_seconds':cpu()-start,
        'selectors':7200,'total_variables':nv,'clauses':len(clauses),'controller_edges':150,
        'choices_per_edge':48,'all_PGL_candidates_per_edge':60,'required_pair_clauses':3300,
        'empty_pair_clauses':sum(not x['clause'] for x in required),'whole_CPU_budget':60,
        'solver_wall_window_seconds':48,'solver_hard_CPU_seconds':49,'solver_calls':0,
        'graph_generated':False,'proof_logging':False}
    save('MODEL.json',result);print(json.dumps(result),flush=True)

def accept(positive):
    P=json.loads((HERE/'INPUT.json').read_text());C=P['controller'];inv=P['inverse_ports'];L=P['directions']
    edges=json.loads((HERE/'SELECTOR_MAP.json').read_text())
    pairs=json.loads((HERE/'PAIR_COVERAGE.json').read_text())
    # Verify the literal complete CNF model, including one-hot auxiliaries.
    for line in (HERE/'model.cnf').read_text().splitlines():
        if line.startswith('p'):continue
        lits=[int(x) for x in line.split()[:-1]]
        assert any((x in positive) if x>0 else (-x not in positive) for x in lits)
    H=[F.H(t) for t in [None,0,1,2,3]];T=[[None]*5 for _ in range(60)];selection=[]
    for e in edges:
        chosen=[z for z in e['choices'] if z['selector'] in positive];assert len(chosen)==1
        z=chosen[0];p=e['port'];r=e['reverse_port'];Q=z['Q']
        D=[[1,0,0],[0,Q[0][0],Q[0][1]],[0,Q[1][0],Q[1][1]]]
        A=F.mm(F.mm(F.inverse(H[r]),D),H[p]);B=F.inverse(A)
        u,v=e['source'],e['target'];T[u][p]=A;T[v][r]=B
        selection.append({'edge':e['edge'],'source':u,'target':v,'port':p,'reverse_port':r,'selector':z['selector'],'PGL_index':z['PGL_index'],'Q':Q})
    pencils=[]
    for u in range(60):
        for p,v in enumerate(C[u]):
            r=inv[p];A=T[u][p]
            assert F.mm(T[v][r],A)==F.identity(3) and F.mv(A,L[p])==L[r]
            images={F.point(F.mv(H[r],F.mv(A,L[i]))[1:]) for i in range(5) if i!=p}
            images|={F.point(F.mv(H[r],L[j])[1:]) for j in range(5) if j!=r}
            assert len(images)==5
            pencils.append({'source':u,'target':v,'port':p,'projective_directions':[list(x) for x in sorted(images)]})
    routes=[]
    for pair in pairs:
        good=[]
        for w in pair['words']:
            p=w['ports'][1];a=w['vertices'][1];i,j=w['turn']
            if F.det3(F.mv(T[a][p],L[i]),L[inv[p]],L[j]):good.append(w)
        assert good
        routes.append({'source':pair['source'],'target':pair['target'],'word':good[0]})
    params={**P,'field':4,'fiber_size':64,'field_encoding':'0,1,w,w+1','dart_matrices':T,
        'selected_edge_projectivities':selection,'order':3840,'degree':20,'expected_edges':38400,
        'vertex_label':'64*u+x0+4*x1+16*x2',
        'edge_rule':'(u,x)->(C[u][p],T[u][p]*x+t*L[inv[p]]), t in F4',
        'global_record_claim':False}
    save('PARAMETERS.json',params)
    save('ROUTE_CERTIFICATE.json',{'rank3_pairs':routes,'adjacent_pencils':pencils})
    G=[set() for _ in range(3840)]
    for u in range(60):
        for p,v in enumerate(C[u]):
            for x in range(64):
                y=F.mv(T[u][p],[x%4,x//4%4,x//16]);d=L[inv[p]]
                G[64*u+x].update(64*v+sum((y[j]^F.mul(t,d[j]))*4**j for j in range(3)) for t in range(4))
    assert all(len(row)==20 and u not in row for u,row in enumerate(G))
    assert all(u in G[v] for u,row in enumerate(G) for v in row)
    with (HERE/'graph_d20_D3_n3840.edges').open('w') as f:
        f.write('3840 38400\n')
        for u,row in enumerate(G):
            for v in sorted(row):
                if u<v:f.write(f'{u} {v}\n')
    return {'graph_generated':True,'n':3840,'m':38400,'simple':True,'undirected':True,
            'regular_degree':20,'diameter_by_complete_route_certificate':3,'Moore_20_D2':401,
            'graph_BFS_performed':False,'independent_validation':'PENDING_ROOT','global_record_claim':False}

def solve():
    start=cpu();base_child=childcpu();M=json.loads((HERE/'MODEL.json').read_text());prep=M['prepare_CPU_seconds']
    assert not (HERE/'SOLVER_HANDLE.json').exists(), 'This batch permits only one solver call.'
    remaining=60-prep-(cpu()-start);hard=min(49,math.floor(remaining-8));window=min(48,hard-1)
    assert window>=1
    command=[str(ROOT/'.tools/lean-4.24.0-linux/bin/cadical'),'-t',str(window),'-w',str(HERE/'solver_solution.txt'),str(HERE/'model.cnf')]
    def limit():resource.setrlimit(resource.RLIMIT_CPU,(hard,hard))
    with (HERE/'solver.log').open('w') as log:
        p=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,preexec_fn=limit)
        handle={'status':'RUNNING','driver_pid':os.getpid(),'solver_pid':p.pid,'command':command,
            'solver_hard_CPU_seconds':hard,'solver_wall_window_seconds':window,
            'prepare_CPU_seconds':prep,'observation_timeouts':0}
        save('SOLVER_HANDLE.json',handle);print(json.dumps(handle),flush=True)
        while True:
            try:p.wait(timeout=5);break
            except subprocess.TimeoutExpired:
                handle['observation_timeouts']+=1;save('SOLVER_HANDLE.json',handle)
    used=childcpu()-base_child
    result={'status':{10:'SAT',20:'RAW_UNSAT'}.get(p.returncode,'UNKNOWN'),
        'driver_pid':os.getpid(),'solver_pid':p.pid,'solver_return_code':p.returncode,
        'solver_calls':1,'solver_CPU_seconds':used,'prepare_CPU_seconds':prep,
        'observation_timeouts':handle['observation_timeouts'],'graph_generated':False,
        'proof_logging':False,'independent_UNSAT_check':False}
    if p.returncode==10:
        data=(HERE/'solver_solution.txt').read_text();positive=set()
        for line in data.splitlines():
            if line.startswith('v '):positive.update(int(x) for x in line.split()[1:] if int(x)>0)
        assert positive
        result.update(accept(positive));result['status']='SAT_COMPLETE_ROUTE_CERTIFICATE_AND_LITERAL_GRAPH'
    result['driver_CPU_seconds']=cpu()-start
    result['whole_CPU_seconds']=prep+used+result['driver_CPU_seconds']
    result['whole_budget_seconds']=60
    save('TERMINAL.json',result)
    save('SOLVER_HANDLE.json',{**handle,'status':'TERMINAL','return_code':p.returncode,'solver_CPU_seconds':used})
    print(json.dumps(result),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--prepare-only',action='store_true');parser.add_argument('--solve',action='store_true')
    args=parser.parse_args();assert args.prepare_only!=args.solve
    if args.prepare_only:prepare()
    else:solve()
