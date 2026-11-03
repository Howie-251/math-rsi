"""Six/seven-edge HS star deletion: exact remaining attachment SAT."""
from hs_augmentation import ROOT, ARCHIVE, base, dump, verify
import argparse,importlib.util,itertools,json,os,resource,subprocess,sys,time

def run(kind):
    out=ROOT/f'computations/dd82/construction/hs_augmentation/delete_{kind}_58'
    out.mkdir(parents=True,exist_ok=True)
    assert not (out/'result.json').exists(), 'Do not repeat unchanged experiment'
    original,ns=base();center=0;retained=min(ns[center]) if kind=='star6' else None
    leaves=sorted(ns[center]-({retained} if retained is not None else set()))
    deleted={tuple(sorted((center,v))) for v in leaves}
    old=[e for e in original if tuple(e) not in deleted]
    adj=[set() for _ in range(50)]
    for u,v in old:adj[u].add(v);adj[v].add(u)
    H=[(0,7)] if kind=='star6' else [];hn=[set() for _ in range(8)]
    for a,b in H:hn[a].add(b);hn[b].add(a)
    fixed=({center:set(range(1,8)),**{v:{0,i+1} for i,v in enumerate(leaves)}} if kind=='star6'
           else {center:set(range(8)),leaves[0]:{0,1}})
    free=[v for v in range(50) if v not in fixed]
    capacities=[8-len(hn[a])-sum(a in s for s in fixed.values()) for a in range(8)]
    if kind=='star6':assert capacities==[1]+[6]*7
    # All new-new pairs are covered by the fixed incidence geometry itself.
    assert all(b in hn[a] or hn[a]&hn[b] or any(a in s and b in s for s in fixed.values())
               for a,b in itertools.combinations(range(8),2))
    seed=dict(fixed)
    if kind=='star6':
        colors=[a for a,c in enumerate(capacities) for _ in range(c)]
        seed.update({v:{a} for v,a in zip(free,colors)})
    else:
        for v in leaves:
            seed[v]={0,1}
            seed.update({w:{a} for w,a in zip(sorted(ns[v]-{center}),range(2,8))})
        assert len(seed)==50
    def expanded(ports):
        return sorted(old+[(50+a,50+b) for a,b in H]+[(v,50+a) for v,s in ports.items() for a in sorted(s)])
    dump(out/'seed.json',dict(n=58,edges=expanded(seed),ports={str(v):sorted(s) for v,s in seed.items()}))
    verify(out/'seed.json')
    spec=importlib.util.spec_from_file_location('hs_cardinality',ARCHIVE)
    mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
    em=mod.CNFEmitter(out/'input.cnf')
    B=[[em.new_var(f'port_{v}_{a}') for a in range(8)] for v in range(50)]
    for v,row in enumerate(B):
        if v in fixed:
            for a,var in enumerate(row):em.add_clause(var if a in fixed[v] else -var)
        elif 8-len(adj[v])==1:
            em.add_clause(*row)
            for u,w in itertools.combinations(row,2):em.add_clause(-u,-w)
        else:mod.enforce_exact(em,row,8-len(adj[v]),f'old_degree_{v}')
    for a,c in enumerate(capacities):mod.enforce_exact(em,[B[v][a] for v in free],c,f'fiber_{a}')
    lost=[]
    for u,v in itertools.combinations(range(50),2):
        if v in adj[u] or adj[u]&adj[v]:continue
        lost.append([u,v]);terms=[]
        for a in range(8):
            q=em.new_var('shared_port');mod.add_iff_and(em,q,B[u][a],B[v][a]);terms.append(q)
        em.add_clause(*terms)
    for v in range(50):
        for a in range(8):em.add_clause(B[v][a],*[B[w][a] for w in sorted(adj[v])],*[B[v][b] for b in sorted(hn[a])])
    em.finish()
    dump(out/'encoding.json',dict(n=58,center=center,retained_neighbor=retained,deleted_edges=sorted(deleted),
        auxiliary_edges=H,fixed_ports={str(v):sorted(s) for v,s in fixed.items()},free_vertices=free,
        remaining_capacities=capacities,port_variables=B,old_pairs_requiring_repair=lost,
        variables=em.variable_count,clauses=em.clause_count,
        scope=f'This fixed HS labeling and {kind} repair geometry. Full graph coverage encoded; no global n58 claim.'))
    seconds=60;cmd=[str(ROOT/'.tools/lean-4.24.0-linux/bin/cadical'),'--lrat','-t',str(seconds),str(out/'input.cnf'),str(out/'proof.lrat')]
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds+1))
        resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
        resource.setrlimit(resource.RLIMIT_FSIZE,(256*1024**2,256*1024**2))
    before=resource.getrusage(resource.RUSAGE_CHILDREN);start=time.monotonic()
    with (out/'solver.log').open('w') as f:
        try:rc=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,timeout=seconds+5,preexec_fn=limits).returncode
        except subprocess.TimeoutExpired:rc=None
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    result=dict(status={10:'SAT_CANDIDATE',20:'RAW_UNSAT',0:'UNKNOWN',-24:'CPU_LIMIT',-25:'OUTPUT_LIMIT'}.get(rc,'PROCESS_FAILURE'),
        exit_code=rc,wall_seconds=time.monotonic()-start,cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
        cpu_budget_seconds=seconds,pinned_cpu=min(os.sched_getaffinity(0)),variables=em.variable_count,clauses=em.clause_count,command=cmd)
    if rc==10:
        values={abs(lit):lit>0 for line in (out/'solver.log').read_text().splitlines() if line.startswith('v ')
                for lit in map(int,line.split()[1:]) if lit}
        ports={v:{a for a,var in enumerate(row) if values[var]} for v,row in enumerate(B)}
        dump(out/'candidate.json',dict(n=58,edges=expanded(ports),ports={str(v):sorted(s) for v,s in ports.items()}))
        result['independent_graph_check']=json.loads(verify(out/'candidate.json'))
    if rc==20:
        checker=[str(ROOT/'.tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim'),'--no-trim',str(out/'input.cnf'),str(out/'proof.lrat')]
        checked=subprocess.run(checker,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=20)
        (out/'certificate_check.log').write_text(checked.stdout)
        result['certificate_check']=dict(command=checker,exit_code=checked.returncode,verified=checked.returncode==20 and 's VERIFIED' in checked.stdout.splitlines())
        if result['certificate_check']['verified']:result['status']='CHECKED_UNSAT'
    dump(out/'result.json',result);print(json.dumps(result),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('kind',choices=['star6','star7'])
    args=parser.parse_args();os.sched_setaffinity(0,{min(os.sched_getaffinity(0))});run(args.kind)
