"""Fixed Hoffman-Singleton augmentation: exact attachment CNF, bounded CaDiCaL."""
from pathlib import Path
import argparse,importlib.util,itertools,json,os,resource,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"computations/dd82/construction/hs_augmentation"
ARCHIVE=ROOT/"context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/code/n62/n62_ab_cnf.py"
def dump(p,x):p.write_text(json.dumps(x,indent=2)+"\n")
def base():
    edges=set()
    def add(a,b):edges.add(tuple(sorted((a,b))))
    for i in range(5):
        for j in range(5):
            add(5*i+j,5*i+(j+1)%5)
            add(25+5*i+j,25+5*i+(j+2)%5)
            for k in range(5):add(5*i+j,25+5*k+(i*k+j)%5)
    ns=[set() for _ in range(50)]
    for a,b in edges:ns[a].add(b);ns[b].add(a)
    assert len(edges)==175 and all(len(s)==7 for s in ns)
    assert all(len(ns[a]&ns[b])==(0 if b in ns[a] else 1)
               for a,b in itertools.combinations(range(50),2))
    return sorted(edges),ns
def auxiliary(kind):
    if kind=="star58":return 8,[(0,i) for i in range(1,8)]
    if kind=="petersen60":
        pairs=list(itertools.combinations(range(5),2))
        return 10,[(i,j) for i,j in itertools.combinations(range(10),2)
                   if set(pairs[i]).isdisjoint(pairs[j])]
    raise ValueError(kind)
def expand(edges,H,assignment):
    return sorted(edges+[(50+a,50+b) for a,b in H]+[(x,50+a) for x,a in enumerate(assignment)])
def verify(path):
    return subprocess.run([sys.executable,str(ROOT/"computations/dd82/construction/verify_hs_candidate.py"),str(path)],check=True,capture_output=True,text=True).stdout
def run(kind,seconds):
    target=OUT/kind;target.mkdir(parents=True,exist_ok=True)
    assert not (target/"result.json").exists(),"No unchanged repeat"
    edges,ns=base();k,H=auxiliary(kind)
    hs=[set() for _ in range(k)]
    for a,b in H:hs[a].add(b);hs[b].add(a)
    assert all(b in hs[a] or hs[a]&hs[b] for a,b in itertools.combinations(range(k),2))
    capacities=[8-len(s) for s in hs]
    assert sum(capacities)==50
    seed=[a for a,cap in enumerate(capacities) for _ in range(cap)]
    dump(target/"seed.json",dict(n=50+k,auxiliary=kind,assignment=seed,edges=expand(edges,H,seed)))
    verify(target/"seed.json")
    spec=importlib.util.spec_from_file_location("dd82_cardinality",ARCHIVE)
    mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
    emitter=mod.CNFEmitter(target/"input.cnf")
    x=[[emitter.new_var(f"attach_{v}_{a}") for a in range(k)] for v in range(50)]
    for row in x:
        emitter.add_clause(*row)
        for a,b in itertools.combinations(row,2):emitter.add_clause(-a,-b)
    for a,cap in enumerate(capacities):
        mod.enforce_exact(emitter,[x[v][a] for v in range(50)],cap,f"fiber_{a}")
    coverage=0
    for v in range(50):
        for b in range(k):
            for a in range(k):
                if a!=b and a not in hs[b]:
                    emitter.add_clause(-x[v][b],*[x[y][a] for y in sorted(ns[v])]);coverage+=1
    normalization=[]
    if kind=="star58":
        # Chosen old center attachment p=0. Leaf permutations fix one complete
        # rainbow closed neighborhood in HS minus p; this follows from coverage.
        p=0;q=min(ns[p]);rainbow=[q]+sorted(ns[q]-{p})
        normalization=[(p,0)]+[(v,a+1) for a,v in enumerate(rainbow)]
    elif kind=="petersen60":normalization=[(0,0)]
    for v,a in normalization:emitter.add_clause(x[v][a])
    emitter.finish()
    dump(target/"encoding.json",dict(kind=kind,n=50+k,base_edges=edges,auxiliary_edges=H,
        capacities=capacities,assignment_variables=x,variables=emitter.variable_count,
        clauses=emitter.clause_count,coverage_clauses=coverage,normalization=normalization,
        meaning="Each old vertex chooses one new neighbor. For x assigned b and a outside closed H-neighborhood of b, some HS neighbor of x is assigned a.",
        scope="This fixed base and auxiliary graph, with recorded normalization; not arbitrary target graphs."))
    cmd=[str(ROOT/".tools/lean-4.24.0-linux/bin/cadical"),"--lrat","-t",str(seconds),str(target/"input.cnf"),str(target/"proof.lrat")]
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds+1))
        resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
        resource.setrlimit(resource.RLIMIT_FSIZE,(256*1024**2,256*1024**2))
    start=time.monotonic();before=resource.getrusage(resource.RUSAGE_CHILDREN)
    with (target/"solver.log").open("w") as f:
        try:r=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,timeout=seconds+5,preexec_fn=limits);rc=r.returncode
        except subprocess.TimeoutExpired:rc=None
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    report=dict(kind=kind,n=50+k,status={10:"SAT_CANDIDATE",20:"RAW_UNSAT",0:"UNKNOWN",-24:"CPU_LIMIT",-25:"OUTPUT_LIMIT"}.get(rc,"PROCESS_FAILURE"),
        exit_code=rc,wall_seconds=time.monotonic()-start,cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
        cpu_budget_seconds=seconds,pinned_cpu=next(iter(os.sched_getaffinity(0))),command=cmd,
        variables=emitter.variable_count,clauses=emitter.clause_count,proof_checked=False)
    if rc==10:
        values={}
        for line in (target/"solver.log").read_text().splitlines():
            if line.startswith("v "):
                for lit in map(int,line.split()[1:]):
                    if lit:values[abs(lit)]=lit>0
        assignment=[]
        for row in x:
            choices=[a for a,var in enumerate(row) if values[var]]
            assert len(choices)==1;assignment.append(choices[0])
        dump(target/"candidate.json",dict(n=50+k,auxiliary=kind,assignment=assignment,edges=expand(edges,H,assignment)))
        report["independent_graph_check"]=json.loads(verify(target/"candidate.json"))
    dump(target/"result.json",report);print(json.dumps(report),flush=True)
if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("kind",choices=["star58","petersen60"]);parser.add_argument("--seconds",type=int,default=60)
    args=parser.parse_args();os.sched_setaffinity(0,{min(os.sched_getaffinity(0))});run(args.kind,args.seconds)
