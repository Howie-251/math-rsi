#!/usr/bin/env python3
"""One bounded complete-selector CEGIS batch, no random restarts."""
from collections import deque
from pathlib import Path
import json
import math
import os
import resource
import shutil
import subprocess
import time

HERE=Path(__file__).resolve().parent
PROJECT=HERE.parents[3]
SOURCE=PROJECT/'research/ddp/more_graphs_20261027/d13_D4_current6804/source6804.edges'
SOLVER=PROJECT/'.tools/lean-4.24.0-linux/bin/cadical'
os.chdir(HERE)
def total_cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
def child_cpu():
    b=resource.getrusage(resource.RUSAGE_CHILDREN);return b.ru_utime+b.ru_stime
start=total_cpu()
def elapsed():return total_cpu()-start
def save(name,value):Path(name).write_text(json.dumps(value,indent=2)+'\n')
save('HANDLE.json',{'phase':'PREPARING','driver_pid':os.getpid(),'running':True})
for stem in ('prepare','check_candidate'):
    subprocess.run(['g++','-O3','-std=c++17',stem+'.cpp','-o',stem],check=True)
subprocess.run(['./prepare',str(SOURCE)],check=True)
model=json.loads(Path('MODEL.json').read_text())
prepare_total=elapsed()
print(json.dumps({'event':'PREP_COMPLETE','aggregate_cpu':prepare_total,**model}),flush=True)

matching={};edge_selector={};owner=[0]*6804
for line in Path('SELECTORS.tsv').read_text().splitlines():
    e,u,v=map(int,line.split());matching[e]=(u,v);edge_selector[(min(u,v),max(u,v))]=e;owner[u]=owner[v]=e
adj=[[] for _ in range(6804)]
for line in SOURCE.read_text().splitlines():
    if not line.strip() or line.startswith('#'):continue
    u,v=map(int,line.split());adj[u].append(v);adj[v].append(u)
adjsets=list(map(set,adj))
extras=[];nextvar=model['variables'];c1cache={};cut_records=[]
def variable():
    global nextvar
    nextvar+=1;return nextvar
def OR_variable(lits):
    lits=sorted(set(lits))
    if len(lits)==1:return lits[0]
    v=variable();extras.append([-v,*lits])
    for x in lits:extras.append([-x,v])
    return v
def c1(u):
    if u not in c1cache:c1cache[u]=OR_variable(owner[v] for v in [u,*adj[u]])
    return c1cache[u]
def c2(u):return 3402+u+1
def AND_term(lits):
    lits=sorted(set(lits))
    assert not any(-x in lits for x in lits)
    if len(lits)==1:return lits[0]
    v=variable()
    for x in lits:extras.append([-v,x])
    extras.append([v,*[-x for x in lits]])
    return v
def exact_pair_cut(x,y,selected):
    # Establish that the failed old pair is not originally at distance <=3.
    seen={x};front={x}
    for _ in range(3):
        front={v for u in front for v in adj[u]}-seen;seen|=front
    assert y not in seen
    paths=0;deleted_sets=set()
    for a in adj[x]:
        for b in adj[a]:
            for c in adj[b]:
                if c not in adjsets[y]:continue
                paths+=1;vertices=(x,a,b,c,y)
                used=frozenset(edge_selector[e] for u,v in zip(vertices,vertices[1:]) if (e:=(min(u,v),max(u,v))) in edge_selector)
                assert used and used&selected
                deleted_sets.add(used)
    assert paths>0
    minimal=[s for s in deleted_sets if not any(t<s for t in deleted_sets)]
    before=len(extras)
    terms=[AND_term([-e for e in s]) for s in sorted(minimal,key=lambda z:(len(z),sorted(z)))]
    terms += [AND_term([owner[x],c2(y)]),AND_term([c1(x),c1(y)]),AND_term([c2(x),owner[y]])]
    extras.append(terms)
    rec={'x':x,'y':y,'original_distance':4,'all_original_length4_paths':paths,
         'distinct_matching_sets':len(deleted_sets),'inclusion_minimal_matching_sets':[sorted(s) for s in minimal],
         'new_clauses':len(extras)-before,'extra_clauses_total':len(extras)}
    cut_records.append(rec)
    with Path('CUTS.jsonl').open('a') as out:out.write(json.dumps(rec)+'\n')
    return rec

solver_cpu=0.;rounds=[];terminal='BUDGET_STOP';hit=False
for round_id in range(8):
    remaining=min(60-solver_cpu,88-elapsed())
    seconds=math.floor(remaining)
    if seconds<1:break
    cnf=Path('base.cnf')
    if extras:
        cnf=Path(f'round_{round_id}.cnf')
        with cnf.open('w') as out,Path('base.cnf').open() as base:
            base.readline();out.write(f'p cnf {nextvar} {model["clauses"]+len(extras)}\n');shutil.copyfileobj(base,out)
            for clause in extras:out.write(' '.join(map(str,clause))+' 0\n')
    sol=Path(f'round_{round_id}.model');log=Path(f'round_{round_id}.log')
    before=child_cpu();wall=time.monotonic()
    with log.open('w') as output:
        process=subprocess.Popen([str(SOLVER),'-q','-t',str(seconds),'-w',str(sol),str(cnf)],stdout=output,stderr=subprocess.STDOUT)
        save('HANDLE.json',{'phase':'SOLVER','driver_pid':os.getpid(),'solver_pid':process.pid,'round':round_id,
             'solver_time_limit_wall_seconds':seconds,'solver_cpu_used_before':solver_cpu,'aggregate_cpu_before':elapsed(),'running':True})
        print(json.dumps({'event':'SOLVER_STARTED','round':round_id,'pid':process.pid,'wall_limit':seconds,'aggregate_cpu':elapsed()}),flush=True)
        code=process.wait()
    used=child_cpu()-before;solver_cpu+=used
    rec={'round':round_id,'solver_exit_code':code,'solver_cpu_seconds':used,'solver_wall_seconds':time.monotonic()-wall}
    rounds.append(rec)
    if code==20:terminal='RAW_UNSAT_NO_PROOF_LOG';break
    if code!=10:terminal='UNKNOWN';break
    values=[]
    for line in sol.read_text().splitlines():
        if line.startswith('v '):values.extend(map(int,line.split()[1:]))
    selected={x for x in values if 1<=x<=3402}
    assert 1<=len(selected)<=6
    assert any(any(v//81==0 for v in matching[e]) for e in selected)
    selection=Path(f'round_{round_id}.selected')
    selection.write_text(''.join(f'{matching[e][0]} {matching[e][1]}\n' for e in sorted(selected)))
    save(f'round_{round_id}.parameters.json',{'selected_ids':sorted(selected),'removed_edges':[matching[e] for e in sorted(selected)],'hub':6804})
    rec['selected_ids']=sorted(selected)
    available=87-elapsed()
    if available<0.5:terminal='BUDGET_BEFORE_CANDIDATE_CHECK';break
    check=subprocess.run(['./check_candidate',str(SOURCE),str(selection),str(available)],check=True,capture_output=True,text=True)
    validation=json.loads(check.stdout);rec['candidate_check']=validation
    save(f'round_{round_id}.check.json',validation)
    if validation['status']=='HIT_D_AT_MOST_4':
        hit=True;terminal='HIT_PENDING_PARENT_INDEPENDENT_CHECK';save('HIT_PARAMS.json',{'selected_ids':sorted(selected),'removed_edges':[matching[e] for e in sorted(selected)],'validation':validation});break
    if validation['status']!='FAIL':terminal='BUDGET_DURING_CANDIDATE_CHECK';break
    x,y=validation['root'],validation['target'];assert x<6804 and y<6804, 'R3 cover CNF failed its independent new-root check'
    if elapsed()>86:terminal='BUDGET_BEFORE_COUNTEREXAMPLE_CUT';break
    rec['exact_old_pair_cut']=exact_pair_cut(x,y,selected)
    print(json.dumps({'event':'EXACT_OLD_PAIR_CUT','round':round_id,'x':x,'y':y,'aggregate_cpu':elapsed(),'solver_cpu':solver_cpu}),flush=True)
else:terminal='EIGHT_ROUND_LIMIT'
result={'status':terminal,'complete_selector_scope':True,'maximum_selected_matching_edges':6,
        'solver_rounds':len(rounds),'solver_aggregate_cpu_seconds':solver_cpu,'aggregate_cpu_seconds':elapsed(),
        'prepare_compile_cpu_seconds':prepare_total,'rounds':rounds,'exact_old_pair_cuts':len(cut_records),
        'actual_candidate_checks':sum('candidate_check' in r for r in rounds),'hit':hit,
        'raw_unsat_certified':False,'running':False,'pending':['parent independent graph check'] if hit else []}
save('RESULT.json',result);save('TERMINAL.json',result);save('HANDLE.json',{'phase':'TERMINAL','driver_pid':os.getpid(),'running':False,'status':terminal})
print(json.dumps({'event':'TERMINAL',**result}),flush=True)
