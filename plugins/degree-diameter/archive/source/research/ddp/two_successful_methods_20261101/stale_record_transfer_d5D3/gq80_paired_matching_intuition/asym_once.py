#!/usr/bin/env python3
"""One deterministic Q-profile selection and one fixed-Q/free-P SAT window."""
import csv
import importlib.util
import itertools
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import time
import traceback

START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(5,6))
signal.signal(signal.SIGXCPU,lambda signum,frame: (_ for _ in ()).throw(RuntimeError('PARENT_CPU_SOFT_STOP')))
HERE=Path(__file__).resolve().parent
REPO=next(p for p in HERE.parents if (p/'AGENTS.md').is_file())
OLD=REPO/'research/ddp/breadth_20261027_wave11/gq80_paired_matchings'
PRIOR=3.272020095
PREPARATION=0.25
SOLVER=REPO/'.tools/lean-4.24.0-linux/bin/cadical'
CHILD_CPU=0.0
solver_return=None
best=None
state='PREPARING'

def write(name,data):
    (HERE/name).write_text(json.dumps(data,indent=2)+'\n')

def eid(u,v):
    u,v=sorted((u,v))
    assert u<v
    return u*(79-u)//2+(v-u-1)

def solver_limit():
    resource.setrlimit(resource.RLIMIT_CPU,(20,20))

write('ASYM_HANDLE.json',{'status':'PREPARING','pid':os.getpid(),'single_worker':True,
    'prior_CPU_seconds':PRIOR,'new_preparation_charge_CPU_seconds':PREPARATION,
    'wholecase_CPU_cap_seconds':30,'sole_solver_configured_seconds':19,'solver_hard_CPU_seconds':20})
try:
    geometry=json.loads((OLD/'geometry.json').read_text())
    model=json.loads((HERE/'C5_COMPRESSED_EXACT_MODEL.json').read_text())
    action=json.loads((HERE/'C5_ACTION_AND_BINDING.json').read_text())
    original=json.loads((OLD/'model.json').read_text())
    lines=[set(line) for line in geometry['lines']]
    incident=[set(row) for row in geometry['point_incident_lines']]
    CP=[set().union(*(lines[l] for l in incident[p])) for p in range(40)]
    CL=[set().union(*(incident[p] for p in lines[l])) for l in range(40)]
    preps=[cycle[0] for cycle in action['point_5cycles']]
    lreps=[cycle[0] for cycle in action['line_5cycles']]
    blocks=model['block_variables']
    profiles={}
    for block in blocks:
        if block['side']!=1:
            continue
        profiles[block['block_id']]={
            'i_line_reps':[sum(u in CL[l] and v in CL[l] for u,v in block['edges']) for l in lreps],
            'j_point_reps':[sum(u in incident[p] and v in incident[p] for u,v in block['edges']) for p in preps]}
    write('ASYM_Q_BLOCK_PROFILES.json',{'i_definition':'Qedges entirely within closedC(line)',
        'j_definition':'Qedges entirely within4line pencil(point)',
        'line_representatives':lreps,'point_representatives':preps,'block_integer_coefficients':profiles,
        'linear_coefficients_preserve_multiplicity':True})
    qcounts={'visited':0,'eligible':0,'fail_i_only':0,'fail_j_only':0,'fail_both':0}
    with (HERE/'C5_LINE_MATCHINGS.tsv').open() as input_stream, (HERE/'ASYM_ALL_Q_PROFILE_GATE.tsv').open('w',newline='') as output_stream:
        out=csv.writer(output_stream,delimiter='\t')
        out.writerow(['old_Q_index','old_coverage','eligible','i_eight_line_reps','j_eight_point_reps','four_Q_blocks'])
        for row in csv.DictReader(input_stream,delimiter='\t'):
            selected=[int(row[f'block{i}']) for i in range(4)]
            iv=[sum(profiles[b]['i_line_reps'][k] for b in selected) for k in range(8)]
            jv=[sum(profiles[b]['j_point_reps'][k] for b in selected) for k in range(8)]
            bad_i=max(iv)>3
            bad_j=max(jv)>1
            ok=not(bad_i or bad_j)
            qcounts['visited']+=1
            if ok:
                qcounts['eligible']+=1
                candidate={'old_Q_index':int(row['matching_index']),'old_coverage':int(row['distinct_covered']),
                           'Q_block_ids':selected,'i_line_reps':iv,'j_point_reps':jv}
                if best is None or (-candidate['old_coverage'],candidate['old_Q_index'])<(-best['old_coverage'],best['old_Q_index']):
                    best=candidate
            else:
                qcounts['fail_both' if bad_i and bad_j else 'fail_i_only' if bad_i else 'fail_j_only']+=1
            out.writerow([row['matching_index'],row['distinct_covered'],int(ok),','.join(map(str,iv)),','.join(map(str,jv)),','.join(map(str,selected))])
    assert qcounts['visited']==65625
    write('ASYM_Q_SELECTION.json',{'status':'SELECTED_UNIQUE_Q' if best else 'NO_Q_SURVIVES_PROVEN_NECESSARY_PROFILE',
        'counts':qcounts,'selection_rule':'eligibleQ maximum oldcoverage, then minimum oldmatchingindex',
        'selected':best,'old_action_and_Qenumeration_repeated':False,
        'profile_proof':'PAPER_INTERFACE.md unrestricted i_x+3j_x<=3'})
    if best is None:
        result={'status':'COMPLETE_NO_C5_Q_WITH_FREE_P_BY_Q_NECESSARY_PROFILE','Q_profile_counts':qcounts,
                'solver_calls':0,'scope':'Only Q invariant under actualC5, arbitraryP; validQconditions already impossible',
                'new_graphs':0,'next':'STOP; no alternateQ or action'}
    else:
        qedges=[tuple(e) for b in best['Q_block_ids'] for e in blocks[b]['edges']]
        Q={u:v for e in qedges for u,v in (e,e[::-1])}
        assert len(qedges)==20 and sorted(Q)==list(range(40))
        q_selected={v for b in best['Q_block_ids'] for v in blocks[b]['original_variable_ids']}
        iq=[sum(u in CL[l] and v in CL[l] for u,v in qedges) for l in range(40)]
        jq=[sum(u in incident[p] and v in incident[p] for u,v in qedges) for p in range(40)]
        assert max(iq)<=3 and max(jq)<=1
        triangle_count=sum(v in CL[u] for u,v in qedges)
        best.update({'line_matching20_local_labels':qedges,'selected_original_Q_variable_ids':sorted(q_selected),
                     'concurrent_Q_edge_triangle_count':triangle_count,
                     'actual_i_Q_all40lines':iq,'actual_j_Q_all40points':jq})
        write('ASYM_FIXED_Q.json',best)
        clauses=[]
        degree_rows=[r for r in original['degree_equations'] if r['side']==0]
        assert len(degree_rows)==40
        for row in degree_rows:
            xs=[v+1 for v in row['vars']]
            assert len(xs)==39 and max(xs)<=780
            clauses.append(xs)
            clauses.extend([[-a,-b] for a,b in itertools.combinations(xs,2)])
        covers_remaining=[]
        covers_satisfied=[]
        for row_id,row in enumerate(original['far_pair_covers']):
            if q_selected.intersection(row['vars']):
                covers_satisfied.append(row_id)
            else:
                xs=sorted(v+1 for v in row['vars'] if v<780)
                clauses.append(xs)
                covers_remaining.append({'original_far_row_id':row_id,'side':row['side'],'pair':[row['x'],row['y']],
                                         'positive_P_DIMACS_clause':xs})
        # Existence of x_e=1,x_g(e)=0 excludes only the already-closed common-C5 subset.
        pp=action['point_permutation']
        noninvariance=[]
        next_id=781
        for var in range(780):
            old=original['variables'][var]
            assert old['side']=='point'
            image=eid(pp[old['u']],pp[old['v']])+1
            assert image!=var+1
            w=next_id
            next_id+=1
            clauses.extend([[-w,var+1],[-w,-image]])
            noninvariance.append({'w':w,'P_edge_var':var+1,'C5_image_P_edge_var':image})
        clauses.append([r['w'] for r in noninvariance])
        counter_path=REPO/'research/ddp/more_graphs_20261027/small_d5_D3_gq80_route_overlap_cuts_20261028/girth5_local_budget_cnf_20261028/counter_encoding.py'
        spec=importlib.util.spec_from_file_location('saved_atmost_three_encoding',counter_path)
        counter=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(counter)
        cuts=[]
        for p in range(40):
            xs=[eid(u,v)+1 for u,v in itertools.combinations(sorted(CP[p]),2)]
            bound=3-3*jq[p]
            assert len(xs)==78 and bound in (0,3)
            if bound==0:
                clauses.extend([[-x] for x in xs])
                record={'family':'i_P','root_point':p,'bound':0,'P_vars':xs,'encoding':'negativeunits'}
            else:
                added,meta=counter.atmost_three(xs,next_id)
                clauses.extend(added)
                next_id=meta['last_aux']+1
                record={'family':'i_P','root_point':p,'bound':3,'P_vars':xs,'encoding':'saved sequential unary atmost3','aux':meta}
            cuts.append(record)
        for l in range(40):
            xs=[eid(u,v)+1 for u,v in itertools.combinations(sorted(lines[l]),2)]
            bound=(3-iq[l])//3
            assert len(xs)==6 and bound in (0,1)
            if bound==0:
                clauses.extend([[-x] for x in xs])
            else:
                clauses.extend([[-a,-b] for a,b in itertools.combinations(xs,2)])
            cuts.append({'family':'j_P','root_line':l,'bound':bound,'fixed_i_Q':iq[l],'P_vars':xs,
                         'encoding':'negativeunits' if bound==0 else 'pairwiseatmost1'})
        with (HERE/'ASYM_FIXED_Q_PFREE.cnf').open('w') as stream:
            stream.write(f'p cnf {next_id-1} {len(clauses)}\n')
            for clause in clauses:
                stream.write(' '.join(map(str,clause))+' 0\n')
        explicit_negative_units={-c[0] for c in clauses if len(c)==1 and -780<=c[0]<0}
        write('ASYM_MODEL.json',{'original_model':str((OLD/'model.json').relative_to(REPO)),
            'P_original_edge_variables':780,'matching_equations':40,'all_collinearP_choices_retained_initially':True,
            'fixed_Q':best,'old_far_rows_satisfied_by_Q':covers_satisfied,'remaining_P_far_clauses':covers_remaining,
            'nonC5_invariance_existential_boundary_encoding':noninvariance,'fullvalid_i_j_cuts':cuts,
            'proof':'PAPER_INTERFACE.md i_x+3j_x<=3, unrestricted; no girth5restriction',
            'DIMACS_variables':next_id-1,'DIMACS_clauses':len(clauses),'fixed_Q_Pfree_only':True,
            'P_variables_forced_false_by_explicit_negativeunits':len(explicit_negative_units),
            'P_variables_not_explicitly_unit_false':780-len(explicit_negative_units),
            'no_second_Q_or_solver':True})
        print(json.dumps({'stage':'MODEL_READY_ONE_SOLVER_STARTING','selected_Q_index':best['old_Q_index'],
                          'selected_Q_coverage':best['old_coverage'],'Q_profile_counts':qcounts,
                          'concurrent_Q_triangle_count':triangle_count,
                          'P_variables_not_explicitly_unit_false':780-len(explicit_negative_units),
                          'remaining_far_clauses':len(covers_remaining),'DIMACSvariables':next_id-1,
                          'DIMACSclauses':len(clauses)}),flush=True)
        before=resource.getrusage(resource.RUSAGE_CHILDREN)
        solver_wall_start=time.monotonic()
        with (HERE/'ASYM_SOLVER.stdout').open('w') as stdout, (HERE/'ASYM_SOLVER.stderr').open('w') as stderr:
            process=subprocess.Popen([str(SOLVER),'-t19',str(HERE/'ASYM_FIXED_Q_PFREE.cnf')],
                stdout=stdout,stderr=stderr,preexec_fn=solver_limit)
            state='SOLVER_RUNNING'
            write('ASYM_HANDLE.json',{'status':state,'pid':os.getpid(),'solver_pid':process.pid,'single_solver':True,
                'configured_command':[str(SOLVER),'-t19','ASYM_FIXED_Q_PFREE.cnf'],
                'solver_hard_CPU_seconds':20,'prior_CPU_seconds':PRIOR,'wholecase_CPU_cap_seconds':30})
            wall_guard=False
            try:
                solver_return=process.wait(timeout=22)
            except subprocess.TimeoutExpired:
                process.kill()
                solver_return=process.wait()
                wall_guard=True
        after=resource.getrusage(resource.RUSAGE_CHILDREN)
        CHILD_CPU=(after.ru_utime+after.ru_stime)-(before.ru_utime+before.ru_stime)
        solver_wall=time.monotonic()-solver_wall_start
        assignment={}
        if solver_return==10:
            for line in (HERE/'ASYM_SOLVER.stdout').read_text().splitlines():
                if line.startswith('v '):
                    for literal in map(int,line.split()[1:]):
                        if literal:
                            assignment[abs(literal)]=literal>0
            assert all(any(assignment.get(abs(lit),False)==(lit>0) for lit in clause) for clause in clauses)
            selected_p={v for v in range(780) if assignment.get(v+1,False)}
            assert len(selected_p)==20
            all_selected=selected_p|q_selected
            assert all(sum(v in all_selected for v in row['vars'])==1 for row in original['degree_equations'])
            assert all(set(row['vars'])&all_selected for row in original['far_pair_covers'])
            assert any(assignment[r['P_edge_var']] and not assignment[r['C5_image_P_edge_var']] for r in noninvariance)
            pedges=[(original['variables'][v]['u'],original['variables'][v]['v']) for v in sorted(selected_p)]
            P={u:v for e in pedges for u,v in (e,e[::-1])}
            edges={(p,40+l) for l,line in enumerate(lines) for p in line}|set(pedges)|{(40+u,40+v) for u,v in qedges}
            assert len(edges)==200
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
                    'selected_cover_variable_ids':sorted(set(row['vars'])&all_selected),'actual_vertex_path':path})
            (HERE/'ASYM_graph_d5_D3_n80.edges').write_text('80 200\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
            write('ASYM_HIT_PARAMETERS_AND_ALL1080_COVERS.json',{'n':80,'m':200,'degree':5,
                'fixed_Q_old_index':best['old_Q_index'],'point_matching20':pedges,'line_matching20_local_labels':qedges,
                'selected_original_variable_ids':sorted(all_selected),'all80_original_matching_equalities_pass':True,
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
        result={'status':status,'selected_Q_old_index':best['old_Q_index'],'selected_Q_coverage':best['old_coverage'],
            'Q_profile_counts':qcounts,'fixed_Q_profile':{'i_Q_all40lines':iq,'j_Q_all40points':jq},
            'P_variables':780,'matching_equalities':40,'remaining_far_clauses':len(covers_remaining),
            'fullvalid_cuts':80,'noninvariance_boundary_witnesses':780,
            'DIMACSvariables':next_id-1,'DIMACSclauses':len(clauses),'solver_calls':1,
            'solver_return_code':solver_return,'configured_solver_seconds':19,'solver_hard_CPU_seconds':20,
            'actual_solver_CPU_seconds':CHILD_CPU,'actual_solver_wall_seconds':solver_wall,'wall_guard_triggered':wall_guard,
            'source_or_candidate_BFS_roots':0,'old_action_or_side_enumeration_repeated':False,
            'old_geometry_or_field_regenerated':False,'new_graphs':new_graphs,
            'scope':'Only this deterministically selected fixed C5-Q and arbitrary P perfectmatching, retainingcollinearP and excludingonly oldknown commonC5NO',
            'other_Q_Pfree_family':'UNKNOWN_NOT_TESTED','UNSAT_proof_logged_or_checked':False,
            'next':'STOP; root fresh-verifies SAT or dispositions fixedQ UNSAT/UNKNOWN; noQ2/timer/seed'}
except Exception as exc:
    result={'status':'UNKNOWN_ASYM_INTERFACE_OR_PROCESS_FAILURE','stage':state,'error_type':type(exc).__name__,
            'error':str(exc),'traceback':traceback.format_exc(),'selected_Q':best,
            'solver_return_code':solver_return,'actual_solver_CPU_seconds':CHILD_CPU,
            'scope':'No generalfamilyNO; preserve actual model and soleprocess result','next':'STOP no retry'}
parent_cpu=time.process_time()-START
total=PRIOR+PREPARATION+parent_cpu+CHILD_CPU
result.update({'prior_case_CPU_seconds':PRIOR,'new_preparation_charge_CPU_seconds':PREPARATION,
               'actual_parent_process_CPU_seconds':parent_cpu,'wholecase_CPU_seconds':total,'wholecase_CPU_cap_seconds':30})
write('ASYM_RESULT.json',result)
write('ASYM_TERMINAL.json',{**result,'terminal':True,'active_processes':0})
write('ASYM_HANDLE.json',{'status':result['status'],'pid':os.getpid(),'terminal':True,'active_processes':0,
                         'wholecase_CPU_seconds':total})
print(json.dumps(result),flush=True)
