"""One CPU-bounded complete phase-capacity attempt; no candidate graph search."""
from pathlib import Path
from collections import Counter
import json
import math
import os
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
assert not (HERE/'capacity.terminal.json').exists(), 'No restart of an existing run'

def cpu():
    own = resource.getrusage(resource.RUSAGE_SELF)
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    return own.ru_utime+own.ru_stime+child.ru_utime+child.ru_stime

start,wall = cpu(),time.monotonic()
source_preparation = json.loads((HERE/'source_preparation.json').read_text())['CPU_seconds']
scalar = [pow(3,j,17) for j in range(48)]
assert len(set(scalar)) == 16 and scalar[8] == scalar[24] == 16
assert [j for j in range(48) if scalar[j] == 1] == [0,16,32]
assert sum(math.comb(p+23,p) for p in range(7)) == 593775
inverse_pairs = [set() for _ in range(24)]
involutions = []
for j in range(48):
    for x in range(17):
        if (x,j) == (0,0):
            continue
        inv = (-pow(3,-j,17)*x % 17,-j % 48)
        if inv == (x,j):
            involutions.append((x,j))
        else:
            assert j != 24
            inverse_pairs[min(j,48-j)].add(tuple(sorted(((x,j),inv))))
assert set(j for x,j in involutions) == {24} and len(involutions) == 17
assert list(map(len,inverse_pairs)) == [8]+[17]*23

with (HERE/'compile.log').open('w') as log:
    subprocess.run(['g++','-O3','-std=c++17','capacity.cpp','-o','capacity'],
                   cwd=HERE,stdout=log,stderr=subprocess.STDOUT,check=True)
compile_cpu = cpu()-start
subprocess.run([str(HERE/'capacity'),'calibrate',str(HERE),'0'],check=True)
sys.path.insert(0,str(HERE.parent/'axis_cayley272'))
from symbolic_affine_words import affine_word_forms
product = [[(i+j) % 48 for j in range(48)] for i in range(48)]
inverse = [-j % 48 for j in range(48)]
checks = []
for case in json.loads((HERE/'calibration.cpp.json').read_text()):
    components = [{'phase':j,'kind':'pair'} for j in case['pair_phases']]
    components += [{'phase':24,'kind':'involution'} for _ in range(case['involution_count'])]
    reference = affine_word_forms(17,product,inverse,scalar,components)
    assert reference['raw_counts'] == case['raw_capacity']
    assert reference['form_counts'] == case['form_counts']
    packed = [sorted(sum(x << (5*i) for i,x in enumerate(c)) for c in forms)
              for forms in reference['forms']]
    assert packed == case['packed_forms']
    checks.append({'pair_phases':case['pair_phases'],'involution_count':case['involution_count'],
                   'all_48_coefficient_sets_match':True,'raw_convolution_matches_words':True,
                   'field_assignments_or_graphs_tested':False})
preparation = cpu()-start+source_preparation
(HERE/'calibration.check.json').write_text(json.dumps({'status':'PASS_TWO_PURE_SYMBOLIC_CASES',
    'checks':checks,'compile_and_group_arithmetic_CPU_seconds':compile_cpu,
    'preparation_CPU_seconds':preparation},indent=2)+'\n')
metadata = {'group':'F17 additive semidirect_3 C48 = AGL1(17) direct C3',
    'n':816,'degree':12,'target_diameter':3,'saved_general_graph_threshold':810,
    'Q':17,'M':48,'R':3,'action_order':16,'action_kernel_phases':[0,16,32],
    'center':'{(0,0),(0,16),(0,32)}','center_order':3,
    'group_product':'(x,j)(y,k)=(x+3^j*y mod17,j+k mod48)',
    'group_inverse':'(-3^(-j)*x mod17,-j mod48)',
    'direct_product_map':'(x,j)->((x,j mod16),j mod3)',
    'scalar_powers':scalar,'inverse_pair_phases':list(range(24)),
    'inverse_pair_class_sizes':[8]+[17]*23,'inverse_pairs_total':399,
    'nonidentity_involutions':17,'involution_phase':24,
    'pattern_counts_by_pair_count':[math.comb(p+23,p) for p in range(7)],
    'total_patterns':593775,'component_slots_max':12,'bits_per_coefficient':5,
    'maximum_used_bits':60,'capacity':'a^3+a^2+(2-2d)*a+(1-d)*delta0 in Z[C48]',
    'capacity_threshold_per_phase':17,
    'pattern_order':'p=0..6; lexicographic nondecreasing pair phases0..23',
    'component_order':'pair slots followed by independent phase24 involution slots',
    'normalization':'First component with chi!=1 set0 by common translation; remaining nonzero vector modulo common scalar',
    'anchor_skips_pair_phases':[0,16],
    'normalization_count_per_capacity_survivor':'(17^(12-p-1)-1)/16; marked inputs only, not executed',
    'all_chi1_no_anchor':'No-involution patterns supported only on phases0,16 miss quotient fibers and cannot pass plain capacity',
    'field_assignments_tested':0,'graphs_generated':0,'BFS_runs':0,
    'CPU_budget_seconds':120,'worker_count':1,'automatic_restarts':0}
(HERE/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
remaining = 120-preparation-5
assert remaining > 0

def cap():
    hard = math.ceil(remaining)+1
    resource.setrlimit(resource.RLIMIT_CPU,(hard,hard))

with (HERE/'capacity.log').open('w') as log:
    process = subprocess.Popen([str(HERE/'capacity'),'run',str(HERE),str(remaining)],
                              stdout=log,stderr=subprocess.STDOUT,preexec_fn=cap)
    run = {'status':'RUNNING','pid':process.pid,'driver_pid':os.getpid(),
           'worker_count':1,'start_cursor':0,'scope_patterns':593775,
           'preparation_CPU_seconds':preparation,'capacity_process_CPU_limit':remaining,
           'completion_reserve_CPU_seconds':5,'total_CPU_budget_seconds':120}
    (HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n')
    print(json.dumps(run),flush=True)
    code = process.wait()
assert code == 0,f'Process exit {code}; preserve outputs, no automatic restart'
terminal = json.loads((HERE/'capacity.terminal.json').read_text())
survivors = [json.loads(line) for line in (HERE/'survivors.jsonl').open()]
summary = {'status':terminal['status'],'patterns_completed':terminal['completed_phase_patterns'],
    'plain_pass':terminal['plain_pass'],'symbolic_pass':len(survivors),
    'remaining_marked_projective_inputs_not_executed':sum(r['projective_marked_inputs'] for r in survivors),
    'minimum_capacity_histogram':dict(sorted(Counter(r['minimum_symbolic_capacity'] for r in survivors).items())),
    'tight17_fiber_count_by_phase':[sum(r['symbolic_capacity'][j] == 17 for r in survivors) for j in range(48)],
    'branches':[],'field_assignments_tested':0,'graphs_generated':0,'BFS_runs':0}
assert len(survivors) == terminal['symbolic_pass']
for branch in terminal['branches']:
    group = [r for r in survivors if r['pair_count'] == branch['pairs']]
    examples = []
    if group:
        for r in sorted(group,key=lambda r:(r['minimum_symbolic_capacity'],r['cursor']))[:3]:
            examples.append({k:r[k] for k in ['cursor','pair_phases','involution_count',
                'minimum_symbolic_capacity','tightest_phases','anchor_component','projective_marked_inputs']})
    summary['branches'].append({**branch,'surviving_minimum_capacity_histogram':dict(sorted(
        Counter(r['minimum_symbolic_capacity'] for r in group).items())),
        'representative_tightest_survivors':examples})
(HERE/'SURVIVOR_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
total = cpu()-start+source_preparation
assert total < 120,('Total CPU exceeded explicit task budget',total)
run.update(status=terminal['status'],running=False,exit_code=code,
           next_cursor=terminal['next_cursor'],total_recorded_CPU_seconds=total)
(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n')
terminal.update(preparation_CPU_seconds=preparation,total_recorded_CPU_seconds=total,
                CPU_budget_seconds=120,worker_count=1,restarts=0,
                wall_seconds=time.monotonic()-wall,
                remaining_marked_projective_inputs_not_executed=summary['remaining_marked_projective_inputs_not_executed'])
(HERE/'terminal.json').write_text(json.dumps(terminal,indent=2)+'\n')
print(json.dumps(terminal,indent=2),flush=True)
