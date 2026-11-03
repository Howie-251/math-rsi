"""Break C5: release five C matchings or all ten outer-fiber matchings."""
from hs_augmentation import ROOT,ARCHIVE,dump,verify
import argparse,importlib.util,itertools,json,os,resource,subprocess,sys,time

def run(mode,overlap_cuts):
    directory=ROOT/'computations/dd82/construction'
    out=directory/(f'petersen_release_{mode}_matchings'+('_overlap' if overlap_cuts else ''));out.mkdir(exist_ok=True)
    assert not (out/'result.json').exists(),'No unchanged rerun'
    source=(directory/'petersen_all_matchings_run/candidate.best.edges' if mode.startswith('twin_')
            else directory/'petersen_six_fibers.best.edges')
    rows=[list(map(int,line.split())) for line in source.read_text().splitlines()]
    assert rows[0]==[60,240]
    original={tuple(sorted(e)) for e in rows[1:]};assert len(original)==240
    released=({(i,j) for i,j in itertools.combinations(range(6),2) if j>=4} if mode=='twin_nine' else
              {(0,4),(0,5),(1,4),(1,5),(4,5)} if mode=='twin_five' else
              {tuple(sorted((i,(i+2)%5))) for i in range(5)} if mode=='five'
              else set(itertools.combinations(range(5),2)))
    fixed={e for e in original if tuple(sorted((e[0]//10,e[1]//10))) not in released}
    assert len(fixed)==240-10*len(released)
    dump(out/'seed.json',dict(n=60,edges=sorted(original),source=str(source)))
    verify(out/'seed.json')
    spec=importlib.util.spec_from_file_location('petersen_counter',ARCHIVE)
    mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
    em=mod.CNFEmitter(out/'input.cnf');variables={}
    for i,j in sorted(released):
        for u in range(10*i,10*i+10):
            for v in range(10*j,10*j+10):variables[u,v]=em.new_var('released_matching_edge')
    def var(u,v):return variables.get(tuple(sorted((u,v))))
    def exactly_one(row):
        em.add_clause(*row)
        for a,b in itertools.combinations(row,2):em.add_clause(-a,-b)
    for i,j in sorted(released):
        for u in range(10*i,10*i+10):exactly_one([var(u,v) for v in range(10*j,10*j+10)])
        for v in range(10*j,10*j+10):exactly_one([var(u,v) for u in range(10*i,10*i+10)])
    adj=[set() for _ in range(60)]
    for u,v in fixed:adj[u].add(v);adj[v].add(u)
    cut_count=0
    if overlap_cuts:
        # Eleven route slots to ten targets permit at most one shared label
        # between the source-internal and target-internal neighbor triples.
        for i,j in sorted(released):
            for u in range(10*i,10*i+10):
                source=sorted(w for w in adj[u] if w//10==i);assert len(source)==3
                for v in range(10*j,10*j+10):
                    target=sorted(w for w in adj[v] if w//10==j);assert len(target)==3
                    for x,y in itertools.combinations(source,2):
                        for a,b in itertools.permutations(target,2):
                            em.add_clause(-var(u,v),-var(x,a),-var(y,b));cut_count+=1
    conjunctions={};coverage=0
    for u,v in itertools.combinations(range(60),2):
        if v in adj[u] or adj[u]&adj[v]:continue
        terms=set();direct=var(u,v)
        if direct:terms.add(direct)
        for w in range(60):
            if w in (u,v):continue
            left,right=var(u,w),var(v,w)
            if w in adj[u] and right:terms.add(right)
            elif w in adj[v] and left:terms.add(left)
            elif left and right:
                key=tuple(sorted((left,right)))
                if key not in conjunctions:
                    q=em.new_var('two_variable_path');mod.add_iff_and(em,q,*key);conjunctions[key]=q
                terms.add(conjunctions[key])
        em.add_clause(*sorted(terms));coverage+=1
    em.finish()
    dump(out/'encoding.json',dict(n=60,fixed_edges=sorted(fixed),released_fiber_pairs=sorted(released),
        edge_variables=[[u,v,q] for (u,v),q in variables.items()],variables=em.variable_count,clauses=em.clause_count,
        coverage_clauses=coverage,necessary_overlap_cut_clauses=cut_count,scope=('Retain only six Petersen internal graphs and the four-core-fiber induced graph of the 20-bad-pair candidate; release all nine matchings incident to fiber 4 or 5.' if mode=='twin_nine' else 'Repair the 20-bad-pair double-HS candidate by independently releasing 04,05,14,15,45; retain all internal Petersen edges and ten other matchings.' if mode=='twin_five' else 'All five formerly C matchings independent; fixed six internal Petersen graphs and ten saved A/B matchings.' if mode=='five'
        else 'All ten outer-fiber matchings independent; fixed six Petersen graphs and five saved infinity-to-outer A matchings.')))
    cmd=[str(ROOT/'.tools/lean-4.24.0-linux/bin/cadical'),'--lrat','-t','30',str(out/'input.cnf'),str(out/'proof.lrat')]
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(30,31));resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3));resource.setrlimit(resource.RLIMIT_FSIZE,(128*1024**2,128*1024**2))
    before=resource.getrusage(resource.RUSAGE_CHILDREN);start=time.monotonic()
    with (out/'solver.log').open('w') as f:
        try:rc=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,preexec_fn=limits,timeout=35).returncode
        except subprocess.TimeoutExpired:rc=None
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    result=dict(status={10:'SAT_CANDIDATE',20:'RAW_UNSAT',0:'UNKNOWN',-24:'CPU_LIMIT',-25:'OUTPUT_LIMIT'}.get(rc,'PROCESS_FAILURE'),exit_code=rc,
        wall_seconds=time.monotonic()-start,cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,cpu_budget_seconds=30,
        pinned_cpu=min(os.sched_getaffinity(0)),command=cmd,variables=em.variable_count,clauses=em.clause_count)
    if rc==10:
        values={abs(lit):lit>0 for line in (out/'solver.log').read_text().splitlines() if line.startswith('v ') for lit in map(int,line.split()[1:]) if lit}
        edges=fixed|{e for e,q in variables.items() if values[q]}
        dump(out/'candidate.json',dict(n=60,edges=sorted(edges)));result['independent_graph_check']=json.loads(verify(out/'candidate.json'))
    elif rc==20:
        checker=[str(ROOT/'.tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim'),'--no-trim',str(out/'input.cnf'),str(out/'proof.lrat')]
        r=subprocess.run(checker,capture_output=True,text=True,timeout=20);(out/'certificate_check.log').write_text(r.stdout+r.stderr)
        result['certificate_check']=dict(command=checker,exit_code=r.returncode,verified=r.returncode==20 and 's VERIFIED' in r.stdout.splitlines())
        if result['certificate_check']['verified']:result['status']='CHECKED_UNSAT'
    dump(out/'result.json',result);print(json.dumps(result),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--release',choices=['five','ten','twin_five','twin_nine'],default='five');parser.add_argument('--local-overlap-cuts',action='store_true');args=parser.parse_args()
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))});run(args.release,args.local_overlap_cuts)
