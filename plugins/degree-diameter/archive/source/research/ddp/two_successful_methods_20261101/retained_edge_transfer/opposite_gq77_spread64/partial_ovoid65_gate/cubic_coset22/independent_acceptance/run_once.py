#!/usr/bin/env python3
"""Independent literal acceptance. Reads no producer code or center cache."""
import collections
import csv
import json
import os
from pathlib import Path
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
SOURCE_DIR = HERE.parents[2]
CANDIDATE = HERE.parent / 'graph_d65_D3_n161150.edges'
BUDGET = 120.0
START_SELF = time.process_time()
START_CHILD = resource.getrusage(resource.RUSAGE_CHILDREN)

def used():
    now = resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time() - START_SELF + now.ru_utime + now.ru_stime - START_CHILD.ru_utime - START_CHILD.ru_stime

def run(command, stem, allowance):
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    wall = time.monotonic()
    def limit():
        resource.setrlimit(resource.RLIMIT_CPU, (int(allowance), int(allowance) + 1))
    with (HERE / (stem + '.log')).open('w') as log:
        completed = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT,
                                   preexec_fn=limit, env={**os.environ, 'OMP_NUM_THREADS': '1'})
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    record = dict(command=command, exit_code=completed.returncode,
                  CPU_user_seconds=after.ru_utime-before.ru_utime,
                  CPU_system_seconds=after.ru_stime-before.ru_stime,
                  CPU_total_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                  wall_seconds=time.monotonic()-wall, workers=1,
                  CPU_limit_seconds=int(allowance))
    (HERE / (stem + '_TIME.json')).write_text(json.dumps(record, indent=2)+'\n')
    if completed.returncode:
        raise RuntimeError(f'{stem} failed, exit {completed.returncode}; see log')
    return record

def main():
    # The point order is the explicit task rule. Spread order is read directly
    # from the accepted source PARAMETERS, and is never sorted.
    points = [57,119,165,251,265,347,399,71,133,179,216,279,312,364,85,147,193,230,293,326,378,1]
    params = json.loads((SOURCE_DIR/'PARAMETERS.json').read_text())
    spread = params['spread_line_labels']
    assert len(spread) == 50
    assert spread == [row['line_id'] for row in params['spread']]
    assert [row['index'] for row in params['spread']] == list(range(50))
    inputs = dict(point_ids_outer=points, spread_line_ids_inner=spread,
                  rule='center_i = 400 * point_ids_outer[i//50] + spread_line_ids_inner[i%50]',
                  source_parameters=str(SOURCE_DIR/'PARAMETERS.json'),
                  source_edgefile=str(SOURCE_DIR/'graph_d64_D3_n160050.edges'),
                  candidate_edgefile=str(CANDIDATE),
                  producer_CENTERS_or_code_read=False)
    (HERE/'INDEPENDENT_INPUTS.json').write_text(json.dumps(inputs, indent=2)+'\n')
    (HERE/'INPUTS.txt').write_text('22 50\n'+' '.join(map(str,points))+'\n'+' '.join(map(str,spread))+'\n')
    assert CANDIDATE.is_file(), 'Complete candidate required before acceptance'
    compile_record = run(['g++','-O2','-std=c++17',str(HERE/'validator.cpp'),'-o',str(HERE/'validator')], 'COMPILE', min(30,BUDGET-used()))
    remaining = BUDGET-used()-1
    run_record = run([str(HERE/'validator'),str(SOURCE_DIR/'graph_d64_D3_n160050.edges'),str(CANDIDATE),str(HERE/'INPUTS.txt'),str(HERE),str(remaining)], 'VALIDATION', remaining)
    raw = json.loads((HERE/'RAW_RESULT.json').read_text())
    with (HERE/'NEW_ROOT_BFS.csv').open() as stream:
        histograms = collections.Counter(tuple(int(row[f'd{i}']) for i in range(4))
                                         for row in csv.DictReader(stream))
    raw['new_root_BFS_histogram_distribution'] = [dict(distance_histogram=list(hist), roots=count)
                                                for hist,count in sorted(histograms.items())]
    total = used()
    assert total < BUDGET
    raw.update(total_measured_CPU_seconds_including_compile_and_driver=total,
               compile_receipt=compile_record, validation_receipt=run_record,
               CPU_budget_seconds=BUDGET,
               source_D3_and_closed_concrete_Lean='Inherited accepted source160050; not reconstructed or recompiled',
               all_pairs_D3='General immutable-full-open-neighborhood clone lemma, PLAIN_PROOF.md',
               diameter_exact=3, radius_two_crude_capacity_upper_bound=4291,
               concrete_Lean_performed_here=False, public_global_record_or_priority_claimed=False)
    (HERE/'SUMMARY.json').write_text(json.dumps(raw, indent=2)+'\n')
    (HERE/'RESULT.json').write_text(json.dumps(raw, indent=2)+'\n')
    (HERE/'TERMINAL.json').write_text(json.dumps(dict(status='INDEPENDENT_ACCEPTANCE_PASS',running=False,
        candidate_file_complete_and_freshly_read=True,old_root_BFS_runs=0,
        new_root_BFS_runs=raw['new_root_BFS_runs'],CPU_budget_seconds=BUDGET,
        new_root_BFS_histogram_distribution=raw['new_root_BFS_histogram_distribution'],
        total_measured_CPU_seconds_including_compile_and_driver=total,workers=1),indent=2)+'\n')
    print(json.dumps({'status':'PASS','new_BFS':raw['new_root_BFS_runs'],'total_CPU_seconds':total}))

if __name__ == '__main__':
    main()
