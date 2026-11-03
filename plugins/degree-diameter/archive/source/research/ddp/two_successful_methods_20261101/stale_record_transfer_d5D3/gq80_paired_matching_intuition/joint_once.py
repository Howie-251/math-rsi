#!/usr/bin/env python3
"""One complete bitset-superset join of saved C5 matching masks."""
import csv
import json
import os
from pathlib import Path
import resource
import signal
import time
import traceback

START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(6,7))
signal.signal(signal.SIGXCPU,lambda signum,frame: (_ for _ in ()).throw(RuntimeError('CPU_SOFT_LIMIT_STOP')))
HERE=Path(__file__).resolve().parent
REPO=next(p for p in HERE.parents if (p/'AGENTS.md').is_file())
OLD=REPO/'research/ddp/breadth_20261027_wave11/gq80_paired_matchings'
PRIOR=1.700985481
PREPARATION=0.25
ALL=(1<<216)-1

def write(name,data):
    (HERE/name).write_text(json.dumps(data,indent=2)+'\n')

def read_matchings(name):
    answer=[]
    with (HERE/name).open() as stream:
        for row in csv.DictReader(stream,delimiter='\t'):
            answer.append({'index':int(row['matching_index']),
                           'blocks':[int(row[f'block{i}']) for i in range(4)],
                           'covered':int(row['distinct_covered']),
                           'mask':int(row['cover_mask_hex'],16)})
    assert len(answer)==65625
    return answer

def old_eid(side,u,v):
    u,v=sorted((u,v))
    assert u<v
    return 780*side+u*(79-u)//2+(v-u-1)

write('JOINT_HANDLE.json',{'status':'RUNNING','pid':os.getpid(),'single_worker':True,
                           'stage':'read saved matching masks and buildQ membership',
                           'prior_CPU_seconds':PRIOR,'new_preparation_charge_CPU_seconds':PREPARATION,
                           'process_soft_CPU_seconds':6,'process_hard_CPU_seconds':7,'wholecase_CPU_cap_seconds':10})
counts={'P_capacity_pruned':0,'P_eligible_total':0,'Q_capacity_pruned':0,'Q_eligible_total':0,
        'P_eligible_queried':0,'P_queries_empty':0,'P_with_partner_found':0,'membership_AND_steps':0}
hit=None
finished=False
queries=[]
try:
    ps=read_matchings('C5_POINT_MATCHINGS.tsv')
    qs=read_matchings('C5_LINE_MATCHINGS.tsv')
    model=json.loads((HERE/'C5_COMPRESSED_EXACT_MODEL.json').read_text())
    eligible_q=[q for q in qs if q['covered']>=102]
    counts.update({'P_capacity_pruned':sum(p['covered']<103 for p in ps),
                   'P_eligible_total':sum(p['covered']>=103 for p in ps),
                   'Q_capacity_pruned':65625-len(eligible_q),'Q_eligible_total':len(eligible_q)})
    width=(len(eligible_q)+7)//8
    byte_membership=[bytearray(width) for _ in range(216)]
    for qid,q in enumerate(eligible_q):
        remaining=q['mask']
        while remaining:
            lowest=remaining&-remaining
            orbit=lowest.bit_length()-1
            byte_membership[orbit][qid//8]|=1<<(qid%8)
            remaining^=lowest
    membership=[int.from_bytes(row,'little') for row in byte_membership]
    write('JOINT_Q_MEMBERSHIP.json',{'eligibleQ_count':len(eligible_q),
        'eligibleQ_position_to_original_matching_index':[q['index'] for q in eligible_q],
        'membership_bitset_for_each_of216_orbits_hex':[hex(row) for row in membership],
        'Q_capacity_threshold':102,'bit_order':'least significant bit is eligibleQposition0'})
    write('JOINT_DOMAIN.json',{'P_total':65625,'Q_total':65625,'all_pairs_implicit':4306640625,
        'exact_single_side_maxima':{'P':114,'Q':113},'P_required_at_least':103,'Q_required_at_least':102,
        'counts_after_capacity_prune':counts,
        'proof':'Anyfullunion needs216; P<103 plus Q<=113, or Q<102 plus P<=114, is strictly insufficient',
        'old_action_or_side_enumeration_repeated':False})
    all_q=(1<<len(eligible_q))-1
    with (HERE/'JOINT_ALL_P_STAGES.tsv').open('w',newline='') as stream:
        output=csv.writer(stream,delimiter='\t')
        output.writerow(['original_P_index','P_coverage','stage','missing_orbits_checked',
                         'Q_survivor_counts_after_each_AND','final_Q_survivors','selected_original_Q_index'])
        for p in ps:
            if p['covered']<103:
                output.writerow([p['index'],p['covered'],'CAPACITY_PRUNED','','',0,''])
                continue
            if hit:
                output.writerow([p['index'],p['covered'],'NOT_TESTED_AFTER_FIRST_HIT','','','',''])
                continue
            counts['P_eligible_queried']+=1
            remaining=ALL^p['mask']
            candidates=all_q
            checked=[]
            survivor_counts=[]
            while remaining and candidates:
                lowest=remaining&-remaining
                orbit=lowest.bit_length()-1
                candidates&=membership[orbit]
                checked.append(orbit)
                survivor_counts.append(candidates.bit_count())
                counts['membership_AND_steps']+=1
                remaining^=lowest
            if candidates:
                qid=(candidates&-candidates).bit_length()-1
                q=eligible_q[qid]
                assert (p['mask']|q['mask'])==ALL
                counts['P_with_partner_found']+=1
                hit={'P':p,'Q':q,'eligibleQ_position':qid,'partners_for_this_P':candidates.bit_count(),
                     'actual_union_covered':216,'overlap':(p['mask']&q['mask']).bit_count()}
                output.writerow([p['index'],p['covered'],'HIT',','.join(map(str,checked)),
                                 ','.join(map(str,survivor_counts)),candidates.bit_count(),q['index']])
            else:
                counts['P_queries_empty']+=1
                output.writerow([p['index'],p['covered'],'NO_Q_SUPERSET',','.join(map(str,checked)),
                                 ','.join(map(str,survivor_counts)),0,''])
            queries.append({'P_index':p['index'],'missing_orbits_checked':checked,
                            'Q_survivor_counts_after_each_AND':survivor_counts,
                            'final_Q_survivors':candidates.bit_count()})
    finished=not hit and counts['P_eligible_queried']==counts['P_eligible_total']
    if hit:
        blocks=model['block_variables']
        selected_blocks=hit['P']['blocks']+hit['Q']['blocks']
        selected_original={v for b in selected_blocks for v in blocks[b]['original_variable_ids']}
        assert len(selected_original)==40
        point_edges=[tuple(e) for b in hit['P']['blocks'] for e in blocks[b]['edges']]
        line_edges=[tuple(e) for b in hit['Q']['blocks'] for e in blocks[b]['edges']]
        assert len(point_edges)==len(set(point_edges))==20
        assert len(line_edges)==len(set(line_edges))==20
        P={u:v for e in point_edges for u,v in (e,e[::-1])}
        Q={u:v for e in line_edges for u,v in (e,e[::-1])}
        assert sorted(P)==sorted(Q)==list(range(40))
        assert {old_eid(0,*e) for e in point_edges}|{old_eid(1,*e) for e in line_edges}==selected_original
        geometry=json.loads((OLD/'geometry.json').read_text())
        lines=[set(line) for line in geometry['lines']]
        incident=[set(row) for row in geometry['point_incident_lines']]
        source_edges={(p,40+l) for l,line in enumerate(lines) for p in line}
        edges=source_edges|set(point_edges)|{(40+u,40+v) for u,v in line_edges}
        assert len(source_edges)==160 and len(edges)==200
        degree=[0]*80
        for u,v in edges:
            assert 0<=u<v<80
            degree[u]+=1
            degree[v]+=1
        assert set(degree)=={5}
        # This is one first-hit original-cover audit, not oldfield/GQ generation or sourceBFS.
        Cpoint=[set().union(*(lines[l] for l in incident[x])) for x in range(40)]
        Cline=[set().union(*(incident[p] for p in lines[l])) for l in range(40)]
        cover_witnesses=[]
        for side,(closed,neighbors,mate,opposite_mate) in enumerate([
            (Cpoint,incident,P,Q),(Cline,lines,Q,P)]):
            for x in range(40):
                for y in range(x+1,40):
                    if y in closed[x]:
                        continue
                    own={old_eid(side,x,z) for z in closed[y]}|{old_eid(side,y,z) for z in closed[x]}
                    relay={old_eid(1-side,a,b) for a in neighbors[x] for b in neighbors[y]}
                    assert len(own)==25 and len(relay)==16 and len(own|relay)==41
                    chosen=(own|relay)&selected_original
                    assert chosen
                    mx,my=mate[x],mate[y]
                    if mx==y:
                        actual_path=[40*side+x,40*side+y]
                    elif mx in closed[y]:
                        common=min(neighbors[mx]&neighbors[y])
                        actual_path=[x,mx,40+common,y] if side==0 else [40+x,40+mx,common,40+y]
                    elif my in closed[x]:
                        common=min(neighbors[x]&neighbors[my])
                        actual_path=[x,40+common,my,y] if side==0 else [40+x,common,40+my,40+y]
                    else:
                        a=next(a for a in sorted(neighbors[x]) if opposite_mate[a] in neighbors[y])
                        b=opposite_mate[a]
                        actual_path=[x,40+a,40+b,y] if side==0 else [40+x,a,b,40+y]
                    assert len(actual_path)-1<=3
                    assert all(tuple(sorted((u,v))) in edges for u,v in zip(actual_path,actual_path[1:]))
                    cover_witnesses.append({'original_far_row_id':len(cover_witnesses),'side':side,'pair':[x,y],
                        'original41_variable_ids':sorted(own|relay),
                        'selected_cover_variable_ids':sorted(chosen),'actual_vertex_path':actual_path})
        assert len(cover_witnesses)==1080
        (HERE/'JOINT_graph_d5_D3_n80.edges').write_text('80 200\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
        action=json.loads((HERE/'C5_ACTION_AND_BINDING.json').read_text())
        write('JOINT_HIT_PARAMETERS.json',{'n':80,'m':200,'degree':5,'target_D':3,
            'matrix_A':action['matrix_A'],'point_permutation':action['point_permutation'],
            'line_permutation':action['line_permutation'],
            'P_original_matching_index':hit['P']['index'],'Q_original_matching_index':hit['Q']['index'],
            'point_block_ids':hit['P']['blocks'],'line_block_ids':hit['Q']['blocks'],
            'point_matching20':point_edges,'line_matching20_local_labels':line_edges,
            'selected_original_variable_ids':sorted(selected_original),
            'all160_source_incidence_edges_retained':True,'all80_degrees5':True,
            'all216_orbit_covers_pass':True,'all1080_original_far_clauses_and_actual_paths_pass':True,
            'source_geometry_regenerated':False,'original1560model_regenerated_or_read':False,
            'candidate_BFS_roots':0,'fresh_acceptance':'PENDING_ROOT_INDEPENDENT_CHECK'})
        write('JOINT_ALL1080_ACTUAL_COVER_BINDINGS.json',{'source_schema':'original closedC own25/relay16 exactfar clauses',
            'first_hit_audit_count':1,'far_clauses':cover_witnesses,'actual_simple_degree5_80_200':True,
            'allpair_proof':'Original opposite-side<=3 and collinear same-side<=2 retained; all1080 remaining pairs have actual<=3paths',
            'non_D2':'Moore(5,2)=26<80','BFS_roots':0})
    result={'status':'HIT80_ACTUAL_CLAUSES_AND_PATHS_PENDING_FRESH_ACCEPTANCE' if hit else
                     'COMPLETE_NO_THIS_C5_EQUIVARIANT_PAIRED_MATCHING_FAMILY',
            'full_pair_domain_implicit':4306640625,'full_P_domain':65625,'full_Q_domain':65625,
            'counts':counts,'complete_all_P_exhaustion':finished,
            'remaining_eligible_P':counts['P_eligible_total']-counts['P_eligible_queried'],
            'hit':None if not hit else {'P_index':hit['P']['index'],'Q_index':hit['Q']['index'],
                'P_coverage':hit['P']['covered'],'Q_coverage':hit['Q']['covered'],'union':216,'overlap':hit['overlap'],
                'P_blocks':hit['P']['blocks'],'Q_blocks':hit['Q']['blocks']},
            'positive_prediction_supported':bool(hit),'explicit_joint_pair_iterations':0,
            'old_action_or_geometry_recomputed':False,'old1560model_recomputed_or_read':False,
            'single_side_matching_enumeration_repeated':False,'solver_calls':0,'source_or_candidate_BFS_roots':0,
            'new_graphs_written':1 if hit else 0,
            'scope':'One actual cached freeC5 action and all of its equivariant point/lineperfectmatching pairs; not unrestricted GQ80',
            'next':'STOP; root fresh-verifies first hit or accepts this exact fixed-C5 exclusion; no new action/timer automatically'}
except Exception as exc:
    result={'status':'UNKNOWN_JOINT_GATE_STOPPED_WITHOUT_COMPLETION','error_type':type(exc).__name__,
            'error':str(exc),'traceback':traceback.format_exc(),'counts':counts,
            'remaining_eligible_P':counts['P_eligible_total']-counts['P_eligible_queried'],
            'hit_identified_before_error':None if not hit else {'P_index':hit['P']['index'],'Q_index':hit['Q']['index']},
            'scope':'No familyNO; preserve completed queries only','next':'STOP, no timeout restart'}
actual=time.process_time()-START
total=PRIOR+PREPARATION+actual
result.update({'prior_case_CPU_seconds':PRIOR,'new_preparation_charge_CPU_seconds':PREPARATION,
               'actual_new_process_CPU_seconds':actual,'wholecase_CPU_seconds':total,'wholecase_CPU_cap_seconds':10})
write('JOINT_RESULT.json',result)
write('JOINT_TERMINAL.json',{**result,'terminal':True,'active_processes':0})
write('JOINT_HANDLE.json',{'status':result['status'],'pid':os.getpid(),'terminal':True,'active_processes':0,
                          'wholecase_CPU_seconds':total})
print(json.dumps(result))
