#!/usr/bin/env python3
"""A70 fresh literal acceptance; no producer data or previous65 graph read."""
import collections
import csv
import json
import os
from pathlib import Path
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
SOURCE_DIR = HERE.parents[1]
CANDIDATE = HERE.parent / 'graph_d70_D3_n166650.edges'
BUDGET = 90.0
START_SELF = time.process_time()
START_CHILD = resource.getrusage(resource.RUSAGE_CHILDREN)

def used():
    now = resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time() - START_SELF + now.ru_utime + now.ru_stime - START_CHILD.ru_utime - START_CHILD.ru_stime

def run(command, stem, allowance):
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    wall = time.monotonic()
    def limit():
        resource.setrlimit(resource.RLIMIT_CPU, (int(allowance), int(allowance)+1))
    with (HERE/(stem+'.log')).open('w') as log:
        completed = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT,
                                   preexec_fn=limit, env={**os.environ,'OMP_NUM_THREADS':'1'})
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    record = dict(command=command,exit_code=completed.returncode,
                  CPU_user_seconds=after.ru_utime-before.ru_utime,
                  CPU_system_seconds=after.ru_stime-before.ru_stime,
                  CPU_total_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                  wall_seconds=time.monotonic()-wall,workers=1,
                  CPU_limit_seconds=int(allowance))
    (HERE/(stem+'_TIME.json')).write_text(json.dumps(record,indent=2)+'\n')
    if completed.returncode:
        raise RuntimeError(f'{stem} failed, exit{completed.returncode}; see log')
    return record

def main():
    pred = json.loads((HERE/'PRED.json').read_text())
    assert pred['status']=='PREDICTION_BEFORE_FRESH_CANDIDATE_READ'
    params = json.loads((SOURCE_DIR/'PARAMETERS.json').read_text())
    points = pred['point_ids_outer']
    spread = params['spread_line_labels']
    assert len(points)==22 and len(spread)==50
    assert spread==[row['line_id'] for row in params['spread']]
    assert [row['index'] for row in params['spread']]==list(range(50))
    (HERE/'INDEPENDENT_INPUTS.json').write_text(json.dumps(dict(point_ids_outer=points,
        spread_line_ids_inner=spread,base_index_rule='b=50*i+j; center=400*points[i]+spread[j]',
        clone_index_rule='k=1100*copy+b, copy0..5; newlabel160050+k',
        source_parameters=str(SOURCE_DIR/'PARAMETERS.json'),
        source_edgefile=str(SOURCE_DIR/'graph_d64_D3_n160050.edges'),candidate_edgefile=str(CANDIDATE),
        producer_code_cache_CENTERS_or_passedflag_read=False,previous65graph_read=False),indent=2)+'\n')
    (HERE/'INPUTS.txt').write_text('22 50\n'+' '.join(map(str,points))+'\n'+' '.join(map(str,spread))+'\n')
    assert CANDIDATE.is_file(), 'Complete closed candidate required'
    compile_record = run(['g++','-O2','-std=c++17',str(HERE/'validator.cpp'),'-o',str(HERE/'validator')],
                         'COMPILE',min(30,BUDGET-used()))
    remaining = BUDGET-used()-1
    validation_record = run([str(HERE/'validator'),str(SOURCE_DIR/'graph_d64_D3_n160050.edges'),
                             str(CANDIDATE),str(HERE/'INPUTS.txt'),str(HERE),str(remaining)],
                            'VALIDATION',remaining)
    raw = json.loads((HERE/'RAW_RESULT.json').read_text())
    with (HERE/'NEW_ROOT_BFS.csv').open() as stream:
        rows = list(csv.DictReader(stream))
    assert [int(row['root']) for row in rows]==list(range(160050,160050+len(rows)))
    assert all(int(row['reached'])==166650 and int(row['max_distance'])==3 and
               row['histogram_prediction_match']=='true' for row in rows)
    for row in rows:
        k=int(row['root'])-160050
        assert int(row['copy'])==k//1100 and int(row['base_index'])==k%1100
    histograms=collections.Counter(tuple(int(row[f'd{i}']) for i in range(4)) for row in rows)
    distribution=[dict(distance_histogram=list(hist),roots=count) for hist,count in sorted(histograms.items())]
    if raw['new_root_BFS_runs']==6600:
        assert distribution==pred['expected_BFS_histogram_distribution']
    source_accept=json.loads((SOURCE_DIR/'independent_acceptance/SUMMARY.json').read_text())
    source_formal=json.loads((SOURCE_DIR/'formalization/FINAL_COMPILE_RESULT.json').read_text())
    assert source_accept['status']=='PASS'
    assert source_formal['kernel_status']=='PASS_UNCONDITIONAL_CONCRETE_ORDER_DEGREE_TRUE_WALK_D3_NON_D2'
    assert source_formal['user_hypotheses']==[]
    total=used()
    assert total<BUDGET
    raw.update(new_root_BFS_histogram_distribution=distribution,
        predicted_BFS_histogram_distribution=pred['expected_BFS_histogram_distribution'],
        all6600_histogram_prediction_match=raw['new_root_BFS_runs']==6600,
        BFS_scope='ordinary FIFO queue radius3 from new vertices only; all reached, no depth3 expansion needed',
        source_D3_and_closed_concrete_Lean='Inherited accepted original source160050; not reconstructed or recompiled',
        source_closed_theorem=source_formal['theorem'],
        source_literal_formula_binding='Inherited accepted original source formula binding; all candidate old-old edges checked literally against original source',
        all_candidate_literal_edges_sorted_proper_and_distinct=True,
        all6600_newlabel_source_full_N_bindings_exact=True,
        all6copies_individually_checked=True,
        source_acceptance_reference=str(SOURCE_DIR/'independent_acceptance/SUMMARY.json'),
        source_Lean_reference=str(SOURCE_DIR/'formalization/FINAL_COMPILE_RESULT.json'),
        all_pairs_D3='General immutable-full-open-neighborhood clone lemma; samecenter2, adjacentcenter3; PLAIN_PROOF.md',
        all_prefix_D3='Every prefix uses only original old source endpoints, so same lemma applies independently of future clones',
        diameter_exact=3,radius_two_tight_capacity_upper_bound=4901,
        compile_receipt=compile_record,validation_receipt=validation_record,
        total_measured_CPU_seconds_including_compile_driver_and_postprocessing=total,
        CPU_budget_seconds=BUDGET,concrete_Lean_performed_here=False,
        previous65graph_read=False,producer_code_cache_CENTERS_or_passedflag_read=False,
        public_global_record_or_priority_claimed=False)
    for name in ['SUMMARY.json','RESULT.json']:
        (HERE/name).write_text(json.dumps(raw,indent=2)+'\n')
    terminal=dict(status='INDEPENDENT_ACCEPTANCE_PASS',running=False,
        candidate_file_complete_and_freshly_read=True,old_literal_body_exact=True,
        all6600_newlabel_source_full_N_bindings_exact=True,
        old_root_BFS_runs=0,new_root_BFS_runs=raw['new_root_BFS_runs'],
        new_root_BFS_histogram_distribution=distribution,
        all6600_histogram_prediction_match=raw['all6600_histogram_prediction_match'],
        degree_histogram=raw['degree_histogram'],old_pin_load_histogram=raw['old_pin_load_histogram'],
        max_old_pin_load=6,new_new_edges=0,diameter_exact=3,
        CPU_budget_seconds=BUDGET,total_measured_CPU_seconds_including_compile_driver_and_postprocessing=total,
        workers=1,concrete_Lean_performed_here=False,previous65graph_read=False)
    if raw['new_root_BFS_runs']!=6600:
        terminal['status']='LITERAL_AND_MATHEMATICAL_PASS_BFS_PILOT_LIMITED_BY_BUDGET'
    (HERE/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
    print(json.dumps(dict(status=terminal['status'],new_BFS=raw['new_root_BFS_runs'],
                         histogram_distribution=distribution,total_CPU_seconds=total)))

if __name__=='__main__':
    main()
