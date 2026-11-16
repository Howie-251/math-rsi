"""One shared 202-plane color/hitset gate, bounded at20CPU/120active-wall total.

prepare only encodes/builds, never calls solve. run may prepare first if needed.
The same receipt carries preparation costs into the one authorized solve/check.
Waiting between explicit prepare/run stages is not active wall time.
"""
import argparse
from collections import defaultdict
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if p.name == "ar4math")
INPUT = HERE.parent / "h9_binding/JOINT_INPUT.json"
LIB = "/tmp/n62_sms_install/lib/libsmscadical.a"
CAP_CPU, CAP_WALL = 20.0, 120.0


class Encoding:
    def __init__(self):self.n=0;self.clauses=[]
    def var(self):self.n+=1;return self.n
    def clause(self, *lits):self.clauses.append(list(lits))
    def atmost(self, xs, cap):
        # Prefix count implication; forward clauses suffice for an upper bound.
        if len(xs) <= cap:return
        if cap == 0:
            for x in xs:self.clause(-x)
            return
        previous = None
        for x in xs:
            row = [self.var() for _ in range(cap+1)]
            self.clause(-x,row[0])
            if previous:
                for j in range(cap+1):self.clause(-previous[j],row[j])
                for j in range(1,cap+1):self.clause(-x,-previous[j-1],row[j])
            previous=row
        self.clause(-previous[cap])


def encode(out):
    data=json.loads(INPUT.read_text());e=Encoding()
    colors={r['fold']:e.var() for r in data['split_fibers']}
    incident=defaultdict(list)
    for a,b in data['split_edges']:
        y=e.var();u,v=colors[a],colors[b]
        # y <=> (u == v), all four truth cases.
        e.clause(-y,-u,v);e.clause(-y,u,-v);e.clause(y,u,v);e.clause(y,-u,-v)
        incident[a].append(y);incident[b].append(y)
    fibers={r['fold']:r for r in data['split_fibers']}
    for f,r in fibers.items():e.atmost(incident[f],r['same_edge_cap'])
    allpins=sorted({p for plane in data['plane_candidates'] for row in plane['line_potential_pin_providers'] for p in row})
    pins={p:e.var() for p in allpins}
    pin_to_fiber={p:f for f,r in fibers.items()for p in r['actual_pins']}
    for p,x in pins.items():
        if p in pin_to_fiber:
            for y in incident[pin_to_fiber[p]]:e.clause(-x,-y)
    e.atmost(list(pins.values()),11)
    planes={r['plane_id']:e.var() for r in data['plane_candidates']}
    e.clause(*planes.values());e.atmost(list(planes.values()),1)
    membership=defaultdict(list)
    for plane in data['plane_candidates']:
        s=planes[plane['plane_id']]
        for row in plane['line_potential_pin_providers']:e.clause(-s,*[pins[p]for p in row])
        for p in set(plane['actual_pin_ids91'])&set(pins):membership[p].append(s)
    # A core certificate may be chosen wholly in its plane; this does not force a role quota.
    for p,x in pins.items():e.clause(-x,*membership[p])
    with (out/'model.cnf').open('w') as f:
        f.write(f'p cnf {e.n} {len(e.clauses)}\n')
        for row in e.clauses:f.write(' '.join(map(str,row))+' 0\n')
    mapping=dict(colors=colors,pins=pins,planes=planes)
    (out/'VARIABLES.json').write_text(json.dumps(mapping,separators=(',',':'))+'\n')
    return dict(variables=e.n,clauses=len(e.clauses),color_variables=len(colors),same_edge_variables=6006,
                distinct_pin_variables=len(pins),plane_selectors=len(planes),pin_cap=11,
                all202_in_one_model=True,solve_entered=False,solver_calls=0,SAT_models=0,
                fully_checked_assignments=0,status='READY_NOT_SOLVED')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=['prepare','run']);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();out=args.output.resolve()
    if args.mode=='run':
        state=json.loads((ROOT/'research/ddp/expert15_20261114/STATE.json').read_text())
        assert state['status']=='ACTIVE','Goal not ACTIVE'
    out.mkdir(parents=True,exist_ok=True)
    prior=json.loads((out/'PREP_RESULT.json').read_text())if(out/'PREP_RESULT.json').exists()else None
    cpu0=time.process_time();wall0=time.monotonic();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
    def cpu():
        r=resource.getrusage(resource.RUSAGE_CHILDREN)
        return time.process_time()-cpu0+r.ru_utime+r.ru_stime-r0.ru_utime-r0.ru_stime
    prior_cpu=prior['whole_CPU']if prior else 0;prior_wall=prior['active_wall']if prior else 0
    def remaining():return CAP_CPU-prior_cpu-cpu()
    def run(command,name):
        rem=remaining();wall=CAP_WALL-prior_wall-(time.monotonic()-wall0)
        if rem<=0 or wall<=0:raise TimeoutError('whole gate budget exhausted')
        def limits():
            sec=max(1,math.ceil(rem));resource.setrlimit(resource.RLIMIT_CPU,(sec,sec))
            resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
        with(out/name).open('w')as f:
            subprocess.run(command,check=True,stdout=f,stderr=subprocess.STDOUT,timeout=wall,
                           preexec_fn=limits,env={**os.environ,'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1'})
    result=None
    try:
        if not prior:
            assert not(out/'MODEL.json').exists(),'partial preparation exists; inspect instead of overwrite'
            model=encode(out);(out/'MODEL.json').write_text(json.dumps(model,indent=2)+'\n')
            run(['g++','-O2','-std=c++17',str(HERE/'solve_cnf.cpp'),LIB,'-lpthread','-o',str(out/'solve_cnf')],'COMPILE.log')
            prior=dict(status='READY_NOT_SOLVED',whole_CPU=cpu(),active_wall=time.monotonic()-wall0,
                       CPU_cap=CAP_CPU,active_wall_cap=CAP_WALL,solver_calls=0,SAT_models=0,
                       fully_checked_assignments=0,mathematical_graphs=0,model=model)
            (out/'PREP_RESULT.json').write_text(json.dumps(prior,indent=2)+'\n')
        if args.mode=='prepare':print(json.dumps(prior));return
        assert not(out/'RUN_HANDLE.json').exists(),'one shared solve only; do not reset timer'
        (out/'RUN_HANDLE.json').write_text(json.dumps(dict(running=True,driver_pid=os.getpid(),solver_calls=0))+'\n')
        soft=remaining()-2.0
        if soft<=0:raise TimeoutError('insufficient CPU left for solve and direct check')
        run([str(out/'solve_cnf'),str(out/'model.cnf'),str(out),str(soft)],'SOLVE.log')
        result=json.loads((out/'NATIVE_RESULT.json').read_text())
        if result['solver_return_code']==10:
            truth={int(x)for x in(out/'ASSIGNMENT.txt').read_text().split()if int(x)>0}
            variables=json.loads((out/'VARIABLES.json').read_text())
            selected=[int(k)for k,v in variables['planes'].items()if v in truth];assert len(selected)==1
            candidate=dict(status='PENDING_DIRECT_CHECK_NOT_GRAPH',plane_id=selected[0],
                colors={k:int(v in truth)for k,v in variables['colors'].items()},
                pins=[int(k)for k,v in variables['pins'].items()if v in truth])
            (out/'CANDIDATE.json').write_text(json.dumps(candidate,indent=2)+'\n')
            run([sys.executable,str(HERE/'check_assignment.py'),str(out/'CANDIDATE.json'),str(out)],'CHECK.log')
            check=json.loads((out/'CHECK_RESULT.json').read_text());result.update(status=check['status'],fully_checked_assignments=1,
                                                                                 plane_id=check['plane_id'],pin_count=check['pin_count'],tail_slots=check['tail_slots'])
    except (OSError,AssertionError,ValueError,TimeoutError,subprocess.SubprocessError)as exc:
        progress=json.loads((out/'SOLVE_PROGRESS.json').read_text())if(out/'SOLVE_PROGRESS.json').exists()else{}
        # Keep a real SAT model count even when the later direct checker fails.
        result=dict(result or {}, status='UNKNOWN_PROCESS_OR_BUDGET',error=str(exc),
                    solver_calls=(result or {}).get('solver_calls',progress.get('solver_calls',0)),
                    SAT_models=(result or {}).get('SAT_models',0),
                    fully_checked_assignments=0,proof_checked=False)
    if result is not None:
        result.update(running=False,whole_CPU=prior_cpu+cpu(),active_wall=prior_wall+time.monotonic()-wall0,
                      CPU_cap=CAP_CPU,active_wall_cap=CAP_WALL,new_graphs=0,BFS_calls=0,
                      further_continuation_authorized=False,
                      scope='Fixed4074 split fibers, fixed160 exterior loads and202 potential mapped-plane core certificates; not actual graph distance validation')
        result['CPU_cap_exceeded']=result['whole_CPU']>CAP_CPU
        (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
        (out/'RUN_HANDLE.json').write_text(json.dumps(dict(running=False,status=result['status']))+'\n')
        print(json.dumps(result))


if __name__=='__main__':main()
