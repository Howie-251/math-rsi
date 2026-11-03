"""One bounded full H-empty HS59 experiment: all old deletions and ports variable."""
from hs_augmentation import ROOT,ARCHIVE,base,dump,verify
import importlib.util,itertools,json,os,random,resource,subprocess,sys,time
import networkx as nx
OUT=ROOT/'computations/dd82/construction/hs59_empty_auxiliary'

def make_seed(original,ns):
    rng=random.Random(20261011)
    selected=None
    for attempt in range(1,101):
        shuffled=list(original);rng.shuffle(shuffled);used=set();deleted=[]
        for u,v in shuffled:
            if u not in used and v not in used:
                deleted.append((u,v));used.update((u,v))
                if len(deleted)==11:break
        if len(deleted)!=11:continue
        retained=[set(s) for s in ns]
        for u,v in deleted:retained[u].remove(v);retained[v].remove(u)
        if all(retained[x]&used for x in range(50)):
            selected=(sorted(deleted),used,attempt);break
    assert selected is not None, 'No qualifying matching seed in fixed bounded construction'
    deleted,endpoints,attempt=selected
    F=nx.DiGraph();source='source';sink='sink'
    for x in range(50):
        F.add_edge(source,x,capacity=2 if x in endpoints else 1)
        for a in range(9):F.add_edge(x,50+a,capacity=1)
    for a in range(9):F.add_edge(50+a,sink,capacity=8)
    value,flow=nx.maximum_flow(F,source,sink);assert value==72
    ports={x:{a for a in range(9) if flow[x][50+a]} for x in range(50)}
    if 0 not in ports[0]:
        chosen=min(ports[0]);ports={x:{chosen if a==0 else (0 if a==chosen else a) for a in S} for x,S in ports.items()}
    old=[e for e in original if e not in deleted]
    expanded=sorted(old+[(x,50+a) for x,S in ports.items() for a in sorted(S)])
    dump(OUT/'seed.json',dict(n=59,edges=expanded,deleted_edges=deleted,ports={str(x):sorted(S) for x,S in ports.items()},auxiliary_edges=[],seed=20261011,matching_attempt=attempt,endpoint_retained_total_domination=True))
    report=json.loads(verify(OUT/'seed.json'))
    full=json.loads((OUT/'seed.verification.json').read_text())
    assert all(d==8 for d in full['degrees']) and full['edges']==236
    report['bad_pair_types']=dict(__import__('collections').Counter(('old' if u<50 else 'new')+'-'+('old' if v<50 else 'new') for row in full['bad_pairs'] for u,v in [row['pair']]))
    report['matching_attempt']=attempt
    return report

def run():
    OUT.mkdir(parents=True,exist_ok=True)
    assert not (OUT/'result.json').exists() and not (OUT/'solver.log').exists(), 'Never repeat this experiment'
    original,ns=base();seed_check=make_seed(original,ns)
    spec=importlib.util.spec_from_file_location('hs59_empty_generic_counter',ARCHIVE)
    mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
    em=mod.CNFEmitter(OUT/'input.cnf')
    R={e:em.new_var(f'retain_{e[0]}_{e[1]}') for e in original}
    B=[[em.new_var(f'port_{x}_{a}') for a in range(9)] for x in range(50)]
    def rv(x,y):return R[tuple(sorted((x,y)))]
    def conjunction(a,b,kind):
        q=em.new_var(kind);mod.add_iff_and(em,q,a,b);return q
    for x in range(50):
        old_vars=[rv(x,y) for y in sorted(ns[x])]
        mod.enforce_exact(em,old_vars+B[x],8,f'old_degree_{x}')
        em.add_clause(*old_vars)  # H empty rules out an old vertex with no retained old neighbor.
        em.add_clause(*B[x])      # redundant consequence of old degree eight.
    for a in range(9):mod.enforce_exact(em,[B[x][a] for x in range(50)],8,f'new_degree_{a}')
    mod.enforce_exact(em,[-q for q in R.values()],11,'deleted_edge_count')
    em.add_clause(B[0][0])
    # Exact old-old coverage: Q has zero/one old common neighbors.
    for x,y in itertools.combinations(range(50),2):
        terms=[conjunction(B[x][a],B[y][a],'old_pair_shared_new') for a in range(9)]
        if y in ns[x]:terms.append(rv(x,y))
        else:
            common=ns[x]&ns[y];assert len(common)==1;w=next(iter(common))
            terms.append(conjunction(rv(x,w),rv(y,w),'old_pair_retained_two_path'))
        em.add_clause(*terms)
    # Exact old-new coverage. There is no new-new edge.
    for x in range(50):
        for a in range(9):
            em.add_clause(B[x][a],*[conjunction(rv(x,y),B[y][a],'old_new_old_path') for y in sorted(ns[x])])
    # Exact new-new coverage.
    for a,b in itertools.combinations(range(9),2):
        em.add_clause(*[conjunction(B[x][a],B[x][b],'new_pair_shared_old') for x in range(50)])
    # E_x is true exactly at deleted-edge endpoints.
    E=[em.new_var(f'deletion_endpoint_{x}') for x in range(50)]
    for x in range(50):
        deleted_literals=[-rv(x,y) for y in sorted(ns[x])]
        em.add_clause(-E[x],*deleted_literals)
        for lit in deleted_literals:em.add_clause(E[x],-lit)
    # Every old vertex needs a retained neighbor carrying an extra old-new port.
    for x in range(50):
        em.add_clause(*[conjunction(rv(x,y),E[y],'retained_endpoint_neighbor') for y in sorted(ns[x])])
    em.finish()
    dump(OUT/'encoding.json',dict(n=59,auxiliary_edges=[],HS_edges=original,retained_edge_variables={f'{x},{y}':q for (x,y),q in R.items()},port_variables=B,endpoint_variables=E,variables=em.variable_count,clauses=em.clause_count,normalization='B[0][0]=true; new-label permutation only',retained_min_degree=1,deleted_edges=11,coverage='All 1225 old-old, 450 old-new, and 36 new-new pairs in the same complete graph',scope='Every extension of this explicit HS graph with H empty and no old-old additions; all 175 original old edges and all 450 old-new edges are variable.'))
    seconds=30;cmd=[str(ROOT/'.tools/lean-4.24.0-linux/bin/cadical'),'--lrat','-t',str(seconds),str(OUT/'input.cnf'),str(OUT/'proof.lrat')]
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds))
        resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
        resource.setrlimit(resource.RLIMIT_FSIZE,(128*1024**2,128*1024**2))
    before=resource.getrusage(resource.RUSAGE_CHILDREN);start=time.monotonic()
    with (OUT/'solver.log').open('w') as log:
        try:rc=subprocess.run(cmd,stdout=log,stderr=subprocess.STDOUT,timeout=seconds+5,preexec_fn=limits).returncode
        except subprocess.TimeoutExpired:rc=None
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    status={10:'SAT_CANDIDATE',20:'RAW_UNSAT',0:'UNKNOWN',-9:'CPU_LIMIT',-24:'CPU_LIMIT',-25:'OUTPUT_LIMIT',None:'WALL_LIMIT'}.get(rc,'PROCESS_FAILURE')
    result=dict(status=status,exit_code=rc,wall_seconds=time.monotonic()-start,cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,cpu_budget_seconds=seconds,pinned_cpu=min(os.sched_getaffinity(0)),memory_limit_GiB=4,proof_limit_MiB=128,proof_bytes=(OUT/'proof.lrat').stat().st_size if (OUT/'proof.lrat').exists() else 0,variables=em.variable_count,clauses=em.clause_count,command=cmd,seed_independent_check=seed_check,solver_attempts=1)
    if rc==10:
        values={abs(q):q>0 for line in (OUT/'solver.log').read_text().splitlines() if line.startswith('v ') for q in map(int,line.split()[1:]) if q}
        kept=[e for e,q in R.items() if values[q]]
        ports={x:{a for a,q in enumerate(row) if values[q]} for x,row in enumerate(B)}
        expanded=sorted(kept+[(x,50+a) for x,S in ports.items() for a in sorted(S)])
        dump(OUT/'candidate.json',dict(n=59,edges=expanded,deleted_edges=[e for e in original if e not in kept],ports={str(x):sorted(S) for x,S in ports.items()},auxiliary_edges=[]))
        result['independent_graph_check']=json.loads(verify(OUT/'candidate.json'))
    if rc==20:
        checker=[str(ROOT/'.tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim'),'--no-trim',str(OUT/'input.cnf'),str(OUT/'proof.lrat')]
        checked=subprocess.run(checker,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=30)
        (OUT/'certificate_check.log').write_text(checked.stdout)
        result['certificate_check']=dict(command=checker,exit_code=checked.returncode,verified=checked.returncode==20 and 's VERIFIED' in checked.stdout.splitlines())
        if result['certificate_check']['verified']:result['status']='CHECKED_UNSAT'
    dump(OUT/'result.json',result);print(json.dumps(result),flush=True)

if __name__=='__main__':
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))});run()
