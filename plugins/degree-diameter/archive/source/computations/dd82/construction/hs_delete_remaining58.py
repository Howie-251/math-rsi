"""Other seven-edge deletion shapes on a fixed HS labeling; exact full coverage."""
from hs_augmentation import ROOT,ARCHIVE,base,dump,verify
import argparse,importlib.util,itertools,json,os,resource,subprocess,sys,time
import networkx as nx

def run(kind):
    out=ROOT/f'computations/dd82/construction/hs_augmentation/delete_{kind}_58'
    out.mkdir(parents=True,exist_ok=True);assert not (out/'result.json').exists()
    original,ns=base();center=0;w=min(ns[center]);leaves=sorted(ns[center]-{w})
    children_w=ns[w]-{center};outside=set(range(50))-{center}-ns[center]
    if kind=='broom':extra=(leaves[0],min(ns[leaves[0]]-{center}))
    elif kind=='independent_w':extra=(w,min(children_w))
    elif kind=='independent_near':extra=next((u,v) for u,v in original if u in outside and v in outside and bool({u,v}&children_w))
    elif kind=='independent_far':extra=next((u,v) for u,v in original if u in outside-children_w and v in outside-children_w)
    else:raise ValueError(kind)
    deleted={tuple(sorted((center,v))) for v in leaves}|{tuple(sorted(extra))}
    assert len(deleted)==7 and deleted<=set(original)
    old=[e for e in original if e not in deleted];adj=[set() for _ in range(50)]
    for u,v in old:adj[u].add(v);adj[v].add(u)
    degrees=[8-len(s) for s in adj]
    fixed={center:set(range(1,8))}
    required={v:{0} for v in leaves+[w]}
    # Permute the seven new labels other than0 to normalize one row.
    if kind=='broom':fixed[leaves[0]]={0,1,2}
    elif kind=='independent_w':fixed[w]={0,1}
    else:fixed[leaves[0]]={0,1}
    ports={v:set(fixed.get(v,required.get(v,set()))) for v in range(50)}
    F=nx.DiGraph()
    for v in range(50):
        rem=degrees[v]-len(ports[v]);assert rem>=0
        F.add_edge('s',('v',v),capacity=rem)
        for a in range(8):
            if a not in ports[v]:F.add_edge(('v',v),('a',a),capacity=1)
    for a in range(8):F.add_edge(('a',a),'t',capacity=8-sum(a in s for s in ports.values()))
    flow,plan=nx.maximum_flow(F,'s','t');assert flow==sum(degrees[v]-len(ports[v]) for v in range(50))
    for v in range(50):ports[v]|={a for a in range(8) if plan[('v',v)].get(('a',a),0)}
    def expanded(p):return sorted(old+[(v,50+a) for v,s in p.items() for a in sorted(s)])
    dump(out/'seed.json',dict(n=58,edges=expanded(ports),ports={str(v):sorted(s) for v,s in ports.items()}));verify(out/'seed.json')
    spec=importlib.util.spec_from_file_location('remaining_hs_counter',ARCHIVE)
    mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
    em=mod.CNFEmitter(out/'input.cnf');B=[[em.new_var(f'port_{v}_{a}') for a in range(8)] for v in range(50)]
    for v,row in enumerate(B):
        if v in fixed:
            for a,var in enumerate(row):em.add_clause(var if a in fixed[v] else -var)
        else:
            mod.enforce_exact(em,row,degrees[v],f'row_{v}')
            for a in required.get(v,set()):em.add_clause(row[a])
    for a in range(8):mod.enforce_exact(em,[B[v][a] for v in range(50)],8,f'column_{a}')
    lost=[]
    for u,v in itertools.combinations(range(50),2):
        if v in adj[u] or adj[u]&adj[v]:continue
        lost.append([u,v]);terms=[]
        for a in range(8):
            q=em.new_var('old_shared');mod.add_iff_and(em,q,B[u][a],B[v][a]);terms.append(q)
        em.add_clause(*terms)
    for v in range(50):
        for a in range(8):em.add_clause(B[v][a],*[B[u][a] for u in sorted(adj[v])])
    for a,b in itertools.combinations(range(8),2):
        terms=[]
        for v in range(50):
            q=em.new_var('new_shared');mod.add_iff_and(em,q,B[v][a],B[v][b]);terms.append(q)
        em.add_clause(*terms)
    em.finish();dump(out/'encoding.json',dict(n=58,kind=kind,deleted_edges=sorted(deleted),old_edges=old,auxiliary_edges=[],fixed_ports={str(v):sorted(s) for v,s in fixed.items()},required_ports={str(v):sorted(s) for v,s in required.items()},row_degrees=degrees,port_variables=B,old_pairs_requiring_repair=lost,variables=em.variable_count,clauses=em.clause_count,scope='One explicit old deletion embedding; no automorphism completeness assumption.'))
    cmd=[str(ROOT/'.tools/lean-4.24.0-linux/bin/cadical'),'--lrat','-t','30',str(out/'input.cnf'),str(out/'proof.lrat')]
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(30,31));resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3));resource.setrlimit(resource.RLIMIT_FSIZE,(128*1024**2,128*1024**2))
    start=time.monotonic();before=resource.getrusage(resource.RUSAGE_CHILDREN)
    with (out/'solver.log').open('w') as f:
        try:rc=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,preexec_fn=limits,timeout=35).returncode
        except subprocess.TimeoutExpired:rc=None
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    result=dict(kind=kind,status={10:'SAT_CANDIDATE',20:'RAW_UNSAT',0:'UNKNOWN',-24:'CPU_LIMIT',-25:'OUTPUT_LIMIT'}.get(rc,'PROCESS_FAILURE'),exit_code=rc,command=cmd,wall_seconds=time.monotonic()-start,cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,cpu_budget_seconds=30,pinned_cpu=min(os.sched_getaffinity(0)))
    if rc==10:
        values={abs(lit):lit>0 for line in (out/'solver.log').read_text().splitlines() if line.startswith('v ') for lit in map(int,line.split()[1:]) if lit}
        ports={v:{a for a,var in enumerate(row) if values[var]} for v,row in enumerate(B)}
        dump(out/'candidate.json',dict(n=58,edges=expanded(ports),ports={str(v):sorted(s) for v,s in ports.items()}));result['independent_graph_check']=json.loads(verify(out/'candidate.json'))
    elif rc==20:
        checker=[str(ROOT/'.tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim'),'--no-trim',str(out/'input.cnf'),str(out/'proof.lrat')]
        checked=subprocess.run(checker,capture_output=True,text=True,timeout=20);(out/'certificate_check.log').write_text(checked.stdout+checked.stderr)
        result['certificate_check']=dict(command=checker,exit_code=checked.returncode,verified=checked.returncode==20 and 's VERIFIED' in checked.stdout.splitlines())
        if result['certificate_check']['verified']:result['status']='CHECKED_UNSAT'
    dump(out/'result.json',result);print(json.dumps(result),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('kind',choices=['broom','independent_w','independent_near','independent_far']);args=parser.parse_args()
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))});run(args.kind)
