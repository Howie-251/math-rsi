"""Joint H/B construction for HS minus one edge, n=59; no fixed controller."""
from hs_augmentation import ROOT, ARCHIVE, base, dump, verify
import importlib.util,itertools,json,os,resource,subprocess,sys,time

OUT=ROOT/'computations/dd82/construction/hs59_one_delete'

def run():
    OUT.mkdir(parents=True,exist_ok=True)
    assert not (OUT/'result.json').exists(), 'Do not repeat unchanged experiment'
    original,ns=base();u=0;v=min(ns[u]);old=[e for e in original if e!=(u,v)]
    adj=[set() for _ in range(50)]
    for x,y in old:adj[x].add(y);adj[y].add(x)
    U=sorted(adj[u]);V=sorted(adj[v]);assert len(set(U+V))==12
    fixed={u:{0,1},v:{0,2}}
    Hseed=[(a,8) for a in range(8)]+[(3,4),(5,6)]
    hdeg=[sum(a in e for e in Hseed) for a in range(9)]
    ports={**fixed,**{x:{2} for x in U},**{x:{1} for x in V}}
    caps=[8-hdeg[a]-sum(a in s for s in ports.values()) for a in range(9)]
    colors=[a for a,c in enumerate(caps) for _ in range(c)]
    free=[x for x in range(50) if x not in ports]
    assert len(colors)==len(free) and min(caps)>=0
    ports.update({x:{a} for x,a in zip(free,colors)})
    def expanded(P,H):return sorted(old+[(x,50+a) for x,S in P.items() for a in sorted(S)]+[(50+a,50+b) for a,b in H])
    dump(OUT/'seed.json',dict(n=59,deleted_edge=[u,v],auxiliary_edges=Hseed,ports={str(x):sorted(s) for x,s in ports.items()},edges=expanded(ports,Hseed)))
    seed_check=json.loads(verify(OUT/'seed.json'))
    spec=importlib.util.spec_from_file_location('hs59_cardinality',ARCHIVE)
    mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
    em=mod.CNFEmitter(OUT/'input.cnf')
    B=[[em.new_var(f'port_{x}_{a}') for a in range(9)] for x in range(50)]
    H={e:em.new_var(f'H_{e[0]}_{e[1]}') for e in itertools.combinations(range(9),2)}
    def hv(a,b):return H[tuple(sorted((a,b)))]
    for x,row in enumerate(B):
        if x in fixed:
            for a,q in enumerate(row):em.add_clause(q if a in fixed[x] else -q)
        else:
            em.add_clause(*row)
            for q,r in itertools.combinations(row,2):em.add_clause(-q,-r)
    for a in range(9):mod.enforce_exact(em,[B[x][a] for x in range(50)]+[hv(a,b) for b in range(9) if b!=a],8,f'new_degree_{a}')
    mod.enforce_exact(em,list(H.values()),10,'H_edges')
    lost=[]
    for x,y in itertools.combinations(range(50),2):
        if y in adj[x] or adj[x]&adj[y]:continue
        lost.append([x,y]);terms=[]
        for a in range(9):
            q=em.new_var(f'BB_{x}_{y}_{a}');mod.add_iff_and(em,q,B[x][a],B[y][a]);terms.append(q)
        em.add_clause(*terms)
    assert len(lost)==13
    for x in range(50):
        for a in range(9):
            terms=[B[x][a]]+[B[y][a] for y in sorted(adj[x])]
            for b in range(9):
                if b==a:continue
                q=em.new_var(f'BH_{x}_{a}_{b}');mod.add_iff_and(em,q,B[x][b],hv(a,b));terms.append(q)
            em.add_clause(*terms)
    # Only u and v have multiple new neighbors. Thus 01 and 02 are already
    # covered; every other pair requires an H edge or a two-step H walk.
    for a,b in itertools.combinations(range(9),2):
        if (a,b) in [(0,1),(0,2)]:continue
        terms=[hv(a,b)]
        for c in range(9):
            if c in (a,b):continue
            q=em.new_var(f'HH_{a}_{b}_{c}');mod.add_iff_and(em,q,hv(a,c),hv(c,b));terms.append(q)
        em.add_clause(*terms)
    em.finish()
    dump(OUT/'encoding.json',dict(n=59,deleted_edge=[u,v],fixed_ports={str(x):sorted(s) for x,s in fixed.items()},
        base_edges=original,retained_edges=old,port_variables=B,H_variables={f'{a},{b}':q for (a,b),q in H.items()},
        old_pairs_requiring_repair=lost,variables=em.variable_count,clauses=em.clause_count,
        scope='Every nine-new-vertex extension of this HS labeling after deleting edge (0,1), allowing arbitrary H. Equal endpoint port sets are analytically excluded; distinct sets are normalized by new-vertex permutation only.',
        coverage='A_prime+A_prime^2+BB^T; B+A_prime*B+BH; H+H^2+B^T*B, all exact.'))
    seconds=60
    cmd=[str(ROOT/'.tools/lean-4.24.0-linux/bin/cadical'),'--lrat','-t',str(seconds),str(OUT/'input.cnf'),str(OUT/'proof.lrat')]
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds+1));resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3));resource.setrlimit(resource.RLIMIT_FSIZE,(256*1024**2,256*1024**2))
    before=resource.getrusage(resource.RUSAGE_CHILDREN);start=time.monotonic()
    with (OUT/'solver.log').open('w') as f:
        try:rc=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,timeout=seconds+5,preexec_fn=limits).returncode
        except subprocess.TimeoutExpired:rc=None
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    result=dict(status={10:'SAT_CANDIDATE',20:'RAW_UNSAT',0:'UNKNOWN',-24:'CPU_LIMIT',-25:'OUTPUT_LIMIT'}.get(rc,'PROCESS_FAILURE'),exit_code=rc,
        wall_seconds=time.monotonic()-start,cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
        cpu_budget_seconds=seconds,pinned_cpu=min(os.sched_getaffinity(0)),memory_limit_GiB=4,variables=em.variable_count,clauses=em.clause_count,command=cmd,seed_independent_check=seed_check)
    if rc==10:
        values={abs(q):q>0 for line in (OUT/'solver.log').read_text().splitlines() if line.startswith('v ') for q in map(int,line.split()[1:]) if q}
        P={x:{a for a,q in enumerate(row) if values[q]} for x,row in enumerate(B)}
        HH=[e for e,q in H.items() if values[q]]
        dump(OUT/'candidate.json',dict(n=59,edges=expanded(P,HH),ports={str(x):sorted(s) for x,s in P.items()},auxiliary_edges=HH))
        result['independent_graph_check']=json.loads(verify(OUT/'candidate.json'))
    if rc==20:
        checker=[str(ROOT/'.tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim'),'--no-trim',str(OUT/'input.cnf'),str(OUT/'proof.lrat')]
        checked=subprocess.run(checker,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=20)
        (OUT/'certificate_check.log').write_text(checked.stdout)
        result['certificate_check']=dict(command=checker,exit_code=checked.returncode,verified=checked.returncode==20 and 's VERIFIED' in checked.stdout.splitlines())
        if result['certificate_check']['verified']:result['status']='CHECKED_UNSAT'
    dump(OUT/'result.json',result);print(json.dumps(result),flush=True)

if __name__=='__main__':
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))});run()
