#!/usr/bin/env python3
"""Execute the sole actual solver window on the already prepared fixed-Q CNF."""
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import time
import traceback

START=time.process_time()
# A child can lower the inherited hard cap to20; the prior hard6 could not be raised.
resource.setrlimit(resource.RLIMIT_CPU,(4,24))
signal.signal(signal.SIGXCPU,lambda signum,frame: (_ for _ in ()).throw(RuntimeError('PARENT_CPU_SOFT4_STOP')))
HERE=Path(__file__).resolve().parent
REPO=next(p for p in HERE.parents if (p/'AGENTS.md').is_file())
OLD=REPO/'research/ddp/breadth_20261027_wave11/gq80_paired_matchings'
SOLVER=REPO/'.tools/lean-4.24.0-linux/bin/cadical'
PREPARATION=0.05
FAILED_CHILD_RESERVE=0.01
child_cpu=0.0
solver_calls=0
process=None
solver_return=None

def write(name,obj):
    (HERE/name).write_text(json.dumps(obj,indent=2)+'\n')

def child_limit():
    resource.setrlimit(resource.RLIMIT_CPU,(20,20))

initial=json.loads((HERE/'ASYM_RESULT.json').read_text())
assert initial['status']=='UNKNOWN_SINGLE_FIXED_Q_PFREE_WINDOW_CLOSED' and initial['solver_return_code']==1
assert "invalid option '-t19'" in (HERE/'ASYM_ACTUAL_SOLVER.stderr').read_text()
assert not (HERE/'ASYM_ACTUAL_SOLVER.stdout').read_text().strip()
write('ASYM_COMMAND_FORMAT_FAILURE_RESULT.json',initial)
(HERE/'ASYM_COMMAND_FORMAT_FAILURE.stderr').write_text((HERE/'ASYM_ACTUAL_SOLVER.stderr').read_text())
(HERE/'ASYM_COMMAND_FORMAT_FAILURE.stdout').write_text((HERE/'ASYM_ACTUAL_SOLVER.stdout').read_text())
prior=initial['wholecase_CPU_seconds']
fixed=json.loads((HERE/'ASYM_FIXED_Q.json').read_text())
prepared=json.loads((HERE/'ASYM_MODEL.json').read_text())
write('ASYM_ACTUAL_EXECUTION.json',{'status':'ABOUT_TO_EXECUTE_FIRST_SOLVER',
    'source_launch_failure':'ASYM_INITIAL_LAUNCH_FAILURE_RESULT.json',
    'initial_failure_was_before_solver_exec':True,'solver_search_windows_before_this_process':0,
    'earlier_argument_rejected_exec_attempts':1,'argument_rejection_result':'ASYM_COMMAND_FORMAT_FAILURE_RESULT.json',
    'prior_case_CPU_seconds_including_failure_child_reserve':prior,
    'failed_preexec_child_conservative_CPU_reserve':FAILED_CHILD_RESERVE,
    'new_preparation_charge_CPU_seconds':PREPARATION,'CNF_reused_not_regenerated':True,
    'Q_reselected':False,'model_rebuilt':False,'wholecase_CPU_cap_seconds':30})
try:
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    wall0=time.monotonic()
    with (HERE/'ASYM_ACTUAL_SOLVER.stdout').open('w') as stdout, (HERE/'ASYM_ACTUAL_SOLVER.stderr').open('w') as stderr:
        process=subprocess.Popen([str(SOLVER),'-t','19',str(HERE/'ASYM_FIXED_Q_PFREE.cnf')],
            stdout=stdout,stderr=stderr,preexec_fn=child_limit)
        solver_calls=1
        write('ASYM_HANDLE.json',{'status':'ACTUAL_FIRST_SOLVER_RUNNING','pid':os.getpid(),
            'solver_pid':process.pid,'single_worker':True,'sole_actual_solver_call':1,
            'configured_command':[str(SOLVER),'-t','19','ASYM_FIXED_Q_PFREE.cnf'],
            'solver_hard_CPU_seconds':20,'parent_soft_CPU_seconds':4,'parent_inherited_hard_CPU_seconds':24,
            'prior_case_CPU_seconds':prior,'wholecase_CPU_cap_seconds':30})
        print(json.dumps({'stage':'ACTUAL_FIRST_CADICAL_EXECUTED','solver_pid':process.pid,
            'Q_index':fixed['old_Q_index'],'Q_coverage':fixed['old_coverage'],
            'Q_triangles':fixed['concurrent_Q_edge_triangle_count'],
            'remaining_far_rows':len(prepared['remaining_P_far_clauses']),
            'P_variables_not_explicitly_unit_false':prepared['P_variables_not_explicitly_unit_false'],
            'DIMACSvariables':prepared['DIMACS_variables'],'DIMACSclauses':prepared['DIMACS_clauses']}),flush=True)
        wall_guard=False
        try:
            solver_return=process.wait(timeout=22)
        except subprocess.TimeoutExpired:
            process.kill()
            solver_return=process.wait()
            wall_guard=True
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    child_cpu=(after.ru_utime+after.ru_stime)-(before.ru_utime+before.ru_stime)
    solver_wall=time.monotonic()-wall0
    if solver_return==10:
        assignment={}
        for line in (HERE/'ASYM_ACTUAL_SOLVER.stdout').read_text().splitlines():
            if line.startswith('v '):
                for value in map(int,line.split()[1:]):
                    if value:
                        assignment[abs(value)]=value>0
        checked_clauses=0
        with (HERE/'ASYM_FIXED_Q_PFREE.cnf').open() as stream:
            for line in stream:
                if line.startswith(('c','p')) or not line.strip():
                    continue
                clause=list(map(int,line.split()))[:-1]
                assert any(assignment.get(abs(x),False)==(x>0) for x in clause)
                checked_clauses+=1
        assert checked_clauses==prepared['DIMACS_clauses']
        original=json.loads((OLD/'model.json').read_text())
        geometry=json.loads((OLD/'geometry.json').read_text())
        selected_p={v for v in range(780) if assignment.get(v+1,False)}
        selected_q=set(fixed['selected_original_Q_variable_ids'])
        selected=selected_p|selected_q
        assert len(selected_p)==20 and len(selected)==40
        assert all(sum(x in selected for x in row['vars'])==1 for row in original['degree_equations'])
        assert all(set(row['vars'])&selected for row in original['far_pair_covers'])
        assert any(assignment[r['P_edge_var']] and not assignment[r['C5_image_P_edge_var']]
                   for r in prepared['nonC5_invariance_existential_boundary_encoding'])
        pedges=[(original['variables'][v]['u'],original['variables'][v]['v']) for v in sorted(selected_p)]
        qedges=[tuple(e) for e in fixed['line_matching20_local_labels']]
        P={u:v for e in pedges for u,v in (e,e[::-1])}
        Q={u:v for e in qedges for u,v in (e,e[::-1])}
        lines=[set(l) for l in geometry['lines']]
        incident=[set(ls) for ls in geometry['point_incident_lines']]
        CP=[set().union(*(lines[l] for l in incident[p])) for p in range(40)]
        CL=[set().union(*(incident[p] for p in lines[l])) for l in range(40)]
        source_edges={(p,40+l) for l,line in enumerate(lines) for p in line}
        edges=source_edges|set(pedges)|{(40+u,40+v) for u,v in qedges}
        assert len(source_edges)==160 and len(edges)==200
        degrees=[0]*80
        for u,v in edges:
            assert 0<=u<v<80
            degrees[u]+=1;degrees[v]+=1
        assert set(degrees)=={5}
        witnesses=[]
        for row_id,row in enumerate(original['far_pair_covers']):
            side,x,y=row['side'],row['x'],row['y']
            closed,neighbors,mate,opposite=(CP,incident,P,Q) if side==0 else (CL,lines,Q,P)
            mx,my=mate[x],mate[y]
            if mx==y:
                path=[40*side+x,40*side+y]
            elif mx in closed[y]:
                common=min(neighbors[mx]&neighbors[y])
                path=[x,mx,40+common,y] if side==0 else [40+x,40+mx,common,40+y]
            elif my in closed[x]:
                common=min(neighbors[x]&neighbors[my])
                path=[x,40+common,my,y] if side==0 else [40+x,common,40+my,40+y]
            else:
                a=next(a for a in sorted(neighbors[x]) if opposite[a] in neighbors[y])
                b=opposite[a]
                path=[x,40+a,40+b,y] if side==0 else [40+x,a,b,40+y]
            assert len(path)-1<=3 and all(tuple(sorted((u,v))) in edges for u,v in zip(path,path[1:]))
            witnesses.append({'original_far_row':row_id,'side':side,'pair':[x,y],
                'selected_cover_variable_ids':sorted(set(row['vars'])&selected),'actual_vertex_path':path})
        (HERE/'ASYM_graph_d5_D3_n80.edges').write_text('80 200\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
        write('ASYM_HIT_PARAMETERS_AND_ALL1080_COVERS.json',{'n':80,'m':200,'degree':5,
            'fixed_Q_old_index':fixed['old_Q_index'],'point_matching20':pedges,'line_matching20_local_labels':qedges,
            'selected_original_variable_ids':sorted(selected),'all80_original_matching_equalities_pass':True,
            'all1080_original_far_clauses_and_actual_paths':witnesses,'all_DIMACSclauses_pass':True,
            'P_breaks_actual_C5':True,'source_incidence_all_retained':True,'candidate_BFS_roots':0,
            'status':'PENDING_ROOT_FRESH_ACCEPTANCE'})
        status='SAT80_COMPLETE_ACTUAL_CLAUSE_PATH_BINDING_PENDING_FRESH_ACCEPTANCE'
        new_graphs=1
    elif solver_return==20:
        status='RAW_SOLVER_UNSAT_THIS_FIXED_Q_PFREE_MODEL_NO_FORMAL_UNSAT_CERTIFICATE'
        new_graphs=0
    else:
        status='UNKNOWN_SINGLE_FIXED_Q_PFREE_WINDOW_CLOSED'
        new_graphs=0
    result={'status':status,'selected_Q_old_index':fixed['old_Q_index'],'selected_Q_coverage':fixed['old_coverage'],
        'Q_triangle_count':fixed['concurrent_Q_edge_triangle_count'],
        'P_variables':780,'P_variables_not_explicitly_unit_false':prepared['P_variables_not_explicitly_unit_false'],
        'matching_equalities':40,'remaining_far_clauses':len(prepared['remaining_P_far_clauses']),
        'DIMACSvariables':prepared['DIMACS_variables'],'DIMACSclauses':prepared['DIMACS_clauses'],
        'solver_calls':solver_calls,'solver_return_code':solver_return,
        'configured_solver_seconds':19,'solver_hard_CPU_seconds':20,
        'actual_solver_CPU_seconds':child_cpu,'actual_solver_wall_seconds':solver_wall,'wall_guard_triggered':wall_guard,
        'initial_launch_failure_preserved':'ASYM_INITIAL_LAUNCH_FAILURE_RESULT.json',
        'argument_rejected_exec_preserved':'ASYM_COMMAND_FORMAT_FAILURE_RESULT.json',
        'earlier_solver_search_windows':0,'earlier_argument_rejected_exec_attempts':1,
        'source_or_candidate_BFS_roots':0,'old_action_or_side_enumeration_repeated':False,
        'Q_reselected':False,'CNF_or_model_rebuilt':False,'new_graphs':new_graphs,
        'scope':'Only fixedQindex1361 with arbitrarypointperfectmatching and full-validcuts; commonC5 excluded by alreadyacceptedNO',
        'other_Q_Pfree_family':'UNKNOWN_NOT_TESTED','UNSAT_proof_logged_or_checked':False,
        'next':'STOP; noQ2/no secondsolver/timer; rootdispositions fixedQ actual result'}
except Exception as exc:
    if process is not None and process.poll() is None:
        process.kill();process.wait()
    if process is not None:
        after=resource.getrusage(resource.RUSAGE_CHILDREN)
        child_cpu=(after.ru_utime+after.ru_stime)-(before.ru_utime+before.ru_stime)
    result={'status':'UNKNOWN_ASYM_ACTUAL_SOLVER_OR_BINDING_FAILURE','error_type':type(exc).__name__,
        'error':str(exc),'traceback':traceback.format_exc(),'solver_calls':solver_calls,
        'solver_return_code':solver_return,'actual_solver_CPU_seconds':child_cpu,
        'scope':'No generalfamilyNO; preserve soleactualwindow','next':'STOP no retry'}
parent_cpu=time.process_time()-START
total=prior+PREPARATION+parent_cpu+child_cpu
result.update({'prior_case_CPU_seconds_including_failure_child_reserve':prior,
    'new_preparation_charge_CPU_seconds':PREPARATION,'actual_parent_process_CPU_seconds':parent_cpu,
    'wholecase_CPU_seconds':total,'wholecase_CPU_cap_seconds':30})
write('ASYM_SOLVER_RESULT.json',result)
write('ASYM_SOLVER_TERMINAL.json',{**result,'terminal':True,'active_processes':0})
write('ASYM_RESULT.json',result)
write('ASYM_TERMINAL.json',{**result,'terminal':True,'active_processes':0})
write('ASYM_HANDLE.json',{'status':result['status'],'pid':os.getpid(),'terminal':True,'active_processes':0,
                         'wholecase_CPU_seconds':total})
print(json.dumps(result),flush=True)
