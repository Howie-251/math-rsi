import time
START=time.process_time();WALL=time.time()
import resource,subprocess,json,math
from pathlib import Path
D=Path(__file__).resolve().parent
BUDGET=15
def totalcpu():
    z=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-START+z.ru_utime+z.ru_stime
phase='compile_new_subset_owner_toy'
steps=[]
try:
    commands=[('compile',['g++','-O2','-std=c++17','INDEPENDENT_UNIFORM_MULTICOPY_TOY.cpp','-o','INDEPENDENT_UNIFORM_MULTICOPY_TOY']),
              ('toy',['./INDEPENDENT_UNIFORM_MULTICOPY_TOY'])]
    for name,cmd in commands:
        phase=name
        remaining=max(1,math.floor(BUDGET-totalcpu()))
        def limits():
            resource.setrlimit(resource.RLIMIT_CPU,(remaining,remaining+1))
        before=totalcpu()
        p=subprocess.run(cmd,cwd=D,capture_output=True,text=True,timeout=remaining+2,preexec_fn=limits)
        used=totalcpu()-before
        (D/f'INDEPENDENT_UNIFORM_MULTICOPY_{name}.stdout').write_text(p.stdout)
        (D/f'INDEPENDENT_UNIFORM_MULTICOPY_{name}.stderr').write_text(p.stderr)
        steps.append(dict(step=name,exit_code=p.returncode,CPU_seconds=used))
        assert p.returncode==0,(name,p.returncode)
        assert totalcpu()<BUDGET
    r=json.loads((D/'INDEPENDENT_UNIFORM_MULTICOPY_TOY_RESULT.json').read_text())
    result=dict(status='PASS_PREDICTION_SUPPORTED_WITH_PLAIN_PROOF',
                scope='uniform full-source-N copies k>=1, old adj fixed, every old non-D saturated at cap delta+k, nonempty finite new helper batch',
                exact_route_condition='h in S_c union closedNB(S_T(c))',
                degree_cost='a_h+d_h<=Delta, with a counting distinct offdiag clone classes',
                necessary_bound='R*(R-1)<=floor((Delta+2)^2/4)',
                balanced=dict(R=65,delta=81,M=4160,excluded_uniform_k=[1,45],max_excluded_cap=126,bound_at_max=4096,next_cap=127,bound_at_next=4160),
                Payne=dict(R=64,delta=80,M=4032,excluded_uniform_k=[1,44],max_excluded_cap=124,bound_at_max=3969,next_cap=125,bound_at_next=4032),
                toy=r,steps=steps,total_CPU_seconds=totalcpu(),
                prior_singleton_toy_reexecuted=False,largegraphs_generated=0,old_geometry_or_field_retests=0,
                BFS_runs=0,Lean_runs=0,solver_calls=0,automatic_k2_or_other_graph_production=False,
                excluded_scope_not_extended_to=['nonuniform copies','joint construction before saturation','changes to old edges','higher cap','different initial code','entire A family'])
    (D/'INDEPENDENT_UNIFORM_MULTICOPY_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    terminal=dict(status=result['status'],total_CPU_seconds=totalcpu(),wall_seconds=time.time()-WALL,
                  CPU_budget_seconds=BUDGET,single_worker=True,steps=steps,
                  all_processes_terminal=True,no_automatic_continuation=True,
                  measurement_boundary='New toy compile+run, subprocess orchestration, imports/aggregation. Interactive authoring excluded.')
    (D/'INDEPENDENT_UNIFORM_MULTICOPY_TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
    print(json.dumps(terminal,indent=2))
except Exception as e:
    fail=dict(status='FAILED_OR_UNKNOWN_NO_CONTINUATION',phase=phase,error=str(e),steps=steps,
              total_CPU_seconds=totalcpu(),all_processes_terminal=True)
    (D/'INDEPENDENT_UNIFORM_MULTICOPY_RESULT.json').write_text(json.dumps(fail,indent=2)+'\n')
    (D/'INDEPENDENT_UNIFORM_MULTICOPY_TERMINAL.json').write_text(json.dumps(fail,indent=2)+'\n')
    raise
