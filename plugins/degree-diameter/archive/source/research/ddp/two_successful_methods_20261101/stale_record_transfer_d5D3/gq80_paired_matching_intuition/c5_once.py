#!/usr/bin/env python3
"""One actual C5 action and exact side-capacity gate; no solver/BFS."""
import csv
from collections import Counter
import itertools
import json
import os
from pathlib import Path
import random
import resource
import time
import traceback

START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(8,8))
HERE=Path(__file__).resolve().parent
REPO=next(p for p in HERE.parents if (p/'AGENTS.md').is_file())
OLD=REPO/'research/ddp/breadth_20261027_wave11/gq80_paired_matchings'
PRIOR=1.100792823
PREPARATION=0.25
SEED=202611010503

def write(name,data):
    (HERE/name).write_text(json.dumps(data,indent=2)+'\n')

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(4))%3 for j in range(4)] for i in range(4)]

def mv(a,x):
    return tuple(sum(a[i][j]*x[j] for j in range(4))%3 for i in range(4))

def mp(a,n):
    ans=[row[:] for row in ID]
    for _ in range(n):
        ans=mm(ans,a)
    return ans

def norm(x):
    first=next(v for v in x if v)
    scale=1 if first==1 else 2
    return tuple(scale*v%3 for v in x)

def cycles(perm):
    unseen=set(range(len(perm)))
    result=[]
    while unseen:
        first=min(unseen)
        cycle=[first]
        nxt=perm[first]
        while nxt!=first:
            assert nxt in unseen and nxt not in cycle
            cycle.append(nxt)
            nxt=perm[nxt]
        unseen.difference_update(cycle)
        result.append(cycle)
    return result

def pairings(items):
    if not items:
        yield []
    else:
        a=items[0]
        for j in range(1,len(items)):
            b=items[j]
            rest=items[1:j]+items[j+1:]
            for tail in pairings(rest):
                yield [(a,b)]+tail

write('C5_HANDLE.json',{'status':'RUNNING','pid':os.getpid(),'single_worker':True,
                        'stage':'new action search then cached-model compression and side enumeration',
                        'prior_CPU_seconds':PRIOR,'preparation_charge_CPU_seconds':PREPARATION,
                        'process_hard_CPU_seconds':8,'wholecase_CPU_cap_seconds':10})
result={}
try:
    geometry=json.loads((OLD/'geometry.json').read_text())
    original=json.loads((OLD/'model.json').read_text())
    points=[tuple(p) for p in geometry['points']]
    lines=[tuple(l) for l in geometry['lines']]
    point_index={p:i for i,p in enumerate(points)}
    line_index={l:i for i,l in enumerate(lines)}
    ID=[[int(i==j) for j in range(4)] for i in range(4)]
    NEGID=[[(-v)%3 for v in row] for row in ID]
    J=[[0,1,0,0],[2,0,0,0],[0,0,0,1],[0,0,2,0]]
    rng=random.Random(SEED)
    trials=[]
    A=None
    for trial in range(64):
        candidate=[row[:] for row in ID]
        factors=[]
        for _ in range(6):
            index=rng.randrange(40)
            c=1+rng.randrange(2)
            v=points[index]
            row=[sum(v[k]*J[k][j] for k in range(4))%3 for j in range(4)]
            transvection=[[(ID[i][j]+c*v[i]*row[j])%3 for j in range(4)] for i in range(4)]
            candidate=mm(candidate,transvection)
            factors.append([index,c])
        power=mp(candidate,5)
        ok=power in (ID,NEGID) and candidate not in (ID,NEGID)
        trials.append({'trial':trial,'six_transvection_pointID_coefficient_factors':factors,
                       'fifth_power':'I' if power==ID else '-I' if power==NEGID else 'other',
                       'noncentral_order5_candidate':ok})
        if ok:
            A=candidate if power==ID else [[-v%3 for v in row] for row in candidate]
            break
    write('C5_ACTION_SEARCH_TRIALS.json',{'seed':SEED,'max_trials':64,'actual_trials':trials,
                                         'matrix_found':A is not None})
    if A is None:
        raise RuntimeError('NO_ORDER5_ACTION_IN_AUTHORIZED64_PRODUCTS; source matching family remains UNKNOWN')
    assert A!=ID and mp(A,5)==ID
    transpose=[list(x) for x in zip(*A)]
    assert mm(mm(transpose,J),A)==J
    pp=[point_index[norm(mv(A,p))] for p in points]
    lp=[line_index[tuple(sorted(pp[p] for p in line))] for line in lines]
    assert sorted(pp)==list(range(40)) and sorted(lp)==list(range(40))
    perms=[pp,lp]
    side_cycles=[cycles(perm) for perm in perms]
    assert all(len(cs)==8 and all(len(c)==5 for c in cs) for cs in side_cycles)
    incidence={(p,40+l) for l,line in enumerate(lines) for p in line}
    action_incidence={(pp[p],40+lp[l-40]) for p,l in incidence}
    assert len(incidence)==160 and action_incidence==incidence
    write('C5_ACTION_AND_BINDING.json',{'status':'PASS_NEW_ACTION_ON_CACHED_GEOMETRY',
        'J':J,'matrix_A':A,'matrix_order5_identity':True,'matrix_preserves_literal_J':True,
        'point_permutation':pp,'line_permutation':lp,
        'point_5cycles':side_cycles[0],'line_5cycles':side_cycles[1],
        'all160_incidence_action_bindings_pass':True,
        'geometry_source':str((OLD/'geometry.json').relative_to(REPO)),
        'old_GQ_or_field_regenerated':False,'source_D4_BFS_roots':0,
        'action_search_actual_products':len(trials),'seed':SEED})
    orbit_of=[]
    position=[]
    for cs in side_cycles:
        oo={v:i for i,cyc in enumerate(cs) for v in cyc}
        pos={v:j for cyc in cs for j,v in enumerate(cyc)}
        orbit_of.append(oo)
        position.append(pos)
    variables=original['variables']
    old_var_id={(0 if v['side']=='point' else 1,v['u'],v['v']):i for i,v in enumerate(variables)}
    far=original['far_pair_covers']
    far_id={(r['side'],r['x'],r['y']):i for i,r in enumerate(far)}
    raw_blocks=[]
    excluded=[]
    for side in range(2):
        visited=set()
        perm=perms[side]
        for old_id,v in enumerate(variables):
            if (0 if v['side']=='point' else 1)!=side or old_id in visited:
                continue
            u,w=v['u'],v['v']
            edges=[]
            for _ in range(5):
                edges.append(tuple(sorted((u,w))))
                u,w=perm[u],perm[w]
            assert len(set(edges))==5
            ids=sorted(old_var_id[(side,*e)] for e in edges)
            visited.update(ids)
            degree=Counter(x for e in edges for x in e)
            if max(degree.values())>1:
                assert max(degree.values())==2 and len(degree)==5
                excluded.append({'side':side,'edges':sorted(edges),'original_variable_ids':ids,
                                 'reason':'within an odd5orbit, invariant edge block has degree2 notmatching'})
                continue
            oi,oj=sorted({orbit_of[side][x] for x in degree})
            first=side_cycles[side][oi][0]
            mate=next(y if x==first else x for x,y in edges if first in (x,y))
            shift=position[side][mate]
            kinds={('far' if (side,*e) in far_id else 'collinear_or_concurrent') for e in edges}
            assert len(kinds)==1
            raw_blocks.append({'side':side,'orbit_pair':[oi,oj],'shift':shift,
                               'edges':sorted(edges),'original_variable_ids':ids,
                               'old_geometry_kind':next(iter(kinds))})
    raw_blocks.sort(key=lambda b:(b['side'],*b['orbit_pair'],b['shift']))
    assert len(raw_blocks)==280 and len(excluded)==32
    blocks=[]
    original_to_block={}
    pair_to_blocks={}
    for block_id,block in enumerate(raw_blocks):
        block={'block_id':block_id,**block}
        blocks.append(block)
        for old_id in block['original_variable_ids']:
            original_to_block[old_id]=block_id
        pair_to_blocks.setdefault((block['side'],*block['orbit_pair']),[]).append(block_id)
    assert all(len(v)==5 for v in pair_to_blocks.values())
    degree_rows=[]
    for side in range(2):
        for orbit in range(8):
            degree_rows.append({'side':side,'orbit':orbit,'block_ids':[
                b['block_id'] for b in blocks if b['side']==side and orbit in b['orbit_pair']], 'rhs':1})
    assert all(len(r['block_ids'])==35 for r in degree_rows)
    cover_rows=[]
    visited=set()
    for old_row,row in enumerate(far):
        if old_row in visited:
            continue
        side=row['side']
        u,v=row['x'],row['y']
        row_ids=[]
        for _ in range(5):
            row_ids.append(far_id[(side,*sorted((u,v)))])
            u,v=perms[side][u],perms[side][v]
        assert len(set(row_ids))==5
        visited.update(row_ids)
        support={original_to_block[x] for x in row['vars'] if x in original_to_block}
        for oid in row_ids:
            assert {original_to_block[x] for x in far[oid]['vars'] if x in original_to_block}==support
        cover_rows.append({'cover_orbit_id':len(cover_rows),'side':side,'representative_pair':[row['x'],row['y']],
                           'original_far_row_ids':sorted(row_ids),'block_ids':sorted(support),'minimum':1})
    assert len(visited)==1080 and len(cover_rows)==216
    write('C5_COMPRESSED_EXACT_MODEL.json',{'schema':'C5_equivariant_unrestricted_paired_matchings_v1',
        'original_model':str((OLD/'model.json').relative_to(REPO)),
        'original_variables':1560,'original_far_covers':1080,
        'action_binding':'C5_ACTION_AND_BINDING.json','block_variables':blocks,
        'excluded_nonmatching_edge_orbits':excluded,
        'degree_equations':degree_rows,'exact_far_orbit_cover_rows':cover_rows,
        'block_variable_count':280,'degree_equation_count':16,'far_orbit_cover_count':216,
        'collinear_or_concurrent_blocks_retained':True,'girth5_imposed':False,
        'extra_cuts_added':[],'all5original_rows_in_each_orbit_fold_to_same_OR':True})
    block_masks=[0]*280
    for row in cover_rows:
        for block_id in row['block_ids']:
            block_masks[block_id]|=1<<row['cover_orbit_id']
    perfect_orbit_pairings=list(pairings(list(range(8))))
    assert len(perfect_orbit_pairings)==105
    side_stats=[]
    for side in range(2):
        best=-1
        best_witness=None
        ties=0
        counts=Counter()
        n=0
        fname='C5_POINT_MATCHINGS.tsv' if side==0 else 'C5_LINE_MATCHINGS.tsv'
        with (HERE/fname).open('w',newline='') as stream:
            out=csv.writer(stream,delimiter='\t')
            out.writerow(['matching_index','block0','block1','block2','block3','distinct_covered','cover_mask_hex'])
            for pairing in perfect_orbit_pairings:
                choices=[pair_to_blocks[(side,*pair)] for pair in pairing]
                for selected in itertools.product(*choices):
                    mask=block_masks[selected[0]]|block_masks[selected[1]]|block_masks[selected[2]]|block_masks[selected[3]]
                    covered=mask.bit_count()
                    out.writerow([n,*selected,covered,hex(mask)])
                    counts[covered]+=1
                    if covered>best:
                        best=covered
                        ties=1
                        best_witness={'matching_index':n,'block_ids':list(selected),'cover_mask_hex':hex(mask),
                                      'matching_edges':[e for b in selected for e in blocks[b]['edges']],
                                      'original_variable_ids':sorted(x for b in selected for x in blocks[b]['original_variable_ids'])}
                    elif covered==best:
                        ties+=1
                    n+=1
        assert n==65625
        side_stats.append({'side':side,'orbit_pairings':105,'shift_choices_each_pairing':625,
                           'actual_matchings_visited':n,'maximum_distinct_far_orbits_covered':best,
                           'number_of_argmax_matchings':ties,'first_argmax':best_witness,
                           'coverage_histogram':dict(sorted(counts.items())),'all_matchings_file':fname})
    mask0=int(side_stats[0]['first_argmax']['cover_mask_hex'],16)
    mask1=int(side_stats[1]['first_argmax']['cover_mask_hex'],16)
    union=mask0|mask1
    missed=[i for i in range(216) if not (union>>i)&1]
    comparison={'maximum_point_contribution':side_stats[0]['maximum_distinct_far_orbits_covered'],
                'maximum_line_contribution':side_stats[1]['maximum_distinct_far_orbits_covered'],
                'sum_of_side_maxima':sum(r['maximum_distinct_far_orbits_covered'] for r in side_stats),
                'target_far_orbits':216,'actual_two_first_argmax_union':union.bit_count(),
                'actual_two_first_argmax_overlap':(mask0&mask1).bit_count(),
                'actual_two_first_argmax_uncovered_ids':missed,
                'actual_two_first_argmax_uncovered_rows':[cover_rows[i] for i in missed]}
    write('C5_SIDE_CAPACITY_AND_ARGMAX.json',{'sides':side_stats,'comparison':comparison,
        'block_contribution_masks_hex':[hex(m) for m in block_masks],
        'joint_full_65625_squared_search_performed':False})
    hit=not missed
    if hit:
        selected_ids=set(side_stats[0]['first_argmax']['original_variable_ids']+side_stats[1]['first_argmax']['original_variable_ids'])
        assert len(selected_ids)==40
        assert all(sum(v in selected_ids for v in r['vars'])==1 for r in original['degree_equations'])
        witnesses=[]
        for i,row in enumerate(far):
            chosen=sorted(set(row['vars'])&selected_ids)
            assert chosen
            witnesses.append({'old_far_row':i,'side':row['side'],'pair':[row['x'],row['y']],
                               'selected_cover_variable_ids':chosen})
        edges=set(incidence)
        for old_id in selected_ids:
            v=variables[old_id]
            side=0 if v['side']=='point' else 1
            edges.add((40*side+v['u'],40*side+v['v']))
        assert len(edges)==200
        degree=Counter(x for e in edges for x in e)
        assert len(degree)==80 and set(degree.values())=={5}
        (HERE/'C5_graph_d5_D3_n80.edges').write_text('80 200\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
        write('C5_HIT_MATCHINGS_AND_EXACT_COVERS.json',{'n':80,'m':200,'degree':5,
              'point_matching':side_stats[0]['first_argmax']['matching_edges'],
              'line_matching_local_labels':side_stats[1]['first_argmax']['matching_edges'],
              'selected_original_variable_ids':sorted(selected_ids),
              'all80_original_degree_equalities_pass':True,'all1080_exact_far_covers':witnesses,
              'source_incidence_all_retained':True,'candidate_BFS_roots':0,
              'status':'CANDIDATE_COMPLETE_EXACT_MODEL_PENDING_ROOT_FRESH_ACCEPTANCE'})
    barrier=comparison['sum_of_side_maxima']<216
    result={'status':'HIT80_EXACT_COVERS_PENDING_FRESH_ACCEPTANCE' if hit else
                     'C5_SINGLE_SIDE_CAPACITY_BARRIER_SUPPORTED' if barrier else 'CAPACITY_BARRIER_PREDICTION_REFUTED_C5_EXISTENCE_UNKNOWN',
            'action_found':True,'actual_action_products_tested':len(trials),
            'point_orbits':8,'line_orbits':8,'orbit_length':5,
            'compressed_variables':280,'compressed_degree_equations':16,'compressed_exact_cover_orbits':216,
            'excluded_intraodd_orbit_blocks_each_side':16,
            'retained_collinear_or_concurrent_blocks_each_side':[
                sum(b['side']==side and b['old_geometry_kind']=='collinear_or_concurrent' for b in blocks) for side in range(2)],
            'point_matchings_enumerated':65625,'line_matchings_enumerated':65625,
            'capacity_barrier_prediction':'maxP+maxL<216','capacity_barrier_supported':barrier,
            'capacity_comparison':comparison,'actual_argmax_pair_hit':hit,
            'all_joint_pairs_searched':False,'solver_calls':0,'source_or_candidate_BFS_roots':0,
            'old_geometry_regenerated':False,'old_field_laws_retested':False,
            'actual_new_graphs_written':1 if hit else 0,
            'scope':'One actual bound free C5 collineation and the full unrestricted C5-equivariant paired-matching subfamily; not WLOG for original family',
            'next':'STOP; root fresh-verifies hit or chooses evidence-driven nextstep; no new action/solver/timer automatically'}
except Exception as exc:
    result={'status':'UNKNOWN_ACTION_OR_BINDING_STAGE_FAILED','error_type':type(exc).__name__,
            'error':str(exc),'traceback':traceback.format_exc(),
            'scope':'Only this authorized single action/capacity attempt; no family exclusion',
            'solver_calls':0,'source_or_candidate_BFS_roots':0,'next':'STOP, preserve actual failure'}
actual=time.process_time()-START
total=PRIOR+PREPARATION+actual
result.update({'prior_case_CPU_seconds':PRIOR,'new_preparation_charge_CPU_seconds':PREPARATION,
               'actual_new_process_CPU_seconds':actual,'wholecase_CPU_seconds':total,'wholecase_CPU_cap_seconds':10})
write('C5_RESULT.json',result)
write('C5_TERMINAL.json',{**result,'terminal':True,'active_processes':0})
write('C5_HANDLE.json',{'status':result['status'],'pid':os.getpid(),'terminal':True,
                       'active_processes':0,'wholecase_CPU_seconds':total})
print(json.dumps({k:v for k,v in result.items() if k not in ('capacity_comparison','traceback')}))
if 'capacity_comparison' in result:
    print(json.dumps(result['capacity_comparison']))
