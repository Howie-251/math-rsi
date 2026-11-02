"""Compile, check one independently calibrated graph, and stop after 2000 HH passes."""
import json
import math
from pathlib import Path
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent


def cpu():
    own = resource.getrusage(resource.RUSAGE_SELF)
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    return own.ru_utime + own.ru_stime + child.ru_utime + child.ru_stime


start = cpu()
limit = 60.0
runs = []


def run(args, log):
    remaining = max(1, math.ceil(limit - (cpu() - start)))
    def child_limit():
        resource.setrlimit(resource.RLIMIT_CPU, (remaining, remaining))
    before = cpu()
    wall = time.monotonic()
    with (HERE / log).open('w') as output:
        result = subprocess.run(args, stdout=output, stderr=subprocess.STDOUT,
                                preexec_fn=child_limit)
    runs.append({'command': list(map(str, args)), 'log': log,
                 'returncode': result.returncode,
                 'cpu_seconds': cpu() - before,
                 'wall_seconds': time.monotonic() - wall})
    if result.returncode:
        raise RuntimeError(f'{log}: exit {result.returncode}')


run(['g++', '-O3', '-std=c++17', str(HERE/'profile.cpp'), '-o', str(HERE/'profile')], 'compile.log')
old = json.loads((HERE.parent/'d7_f64_three_pairs/search.best.json').read_text())
projected = [x + 64*(i % 21) for x, i in old['S_coordinates']]
run([str(HERE/'profile'), 'check', *map(str, projected), str(HERE/'baseline')], 'baseline.log')
baseline = json.loads((HERE/'baseline.json').read_text())
independent = json.loads((HERE/'CENTRAL_QUOTIENT_CHECK.json').read_text())
expected = {}
for row in independent['fixed_root_checks']:
    miss = row['quotient_missing_by_target_layer']
    expected[row['root_type']] = [miss['leaf'], miss['block'], miss['head']]
assert baseline['block_root_target_missing'] == expected['block']
assert baseline['head_root_target_missing'] == expected['head']
assert baseline['BB_missing'] == expected['block'][1]
expected_masks = [0]*7
block_row = next(r for r in independent['fixed_root_checks'] if r['root_type']=='block')
quotient_dist = block_row['quotient_distance_by_vertex']
for b in range(448):
    if 0 <= quotient_dist[1344+b] <= 5:
        expected_masks[b//64] |= 1 << (b%64)
assert baseline['BB_masks'] == expected_masks
preflight = {'old_graph': '../d7_f64_three_pairs/search.best.edges',
             'independent_reference': 'CENTRAL_QUOTIENT_CHECK.json',
             'all_448_BB_targets_match_independent_BFS': True,
             'all_three_target_layer_counts_match_for_both_fixed_roots': True,
             'block_root_target_missing': expected['block'],
             'head_root_target_missing': expected['head']}
(HERE/'preflight.json').write_text(json.dumps(preflight, indent=2)+'\n')
remaining = limit - (cpu() - start) - 0.5
run([str(HERE/'profile'), str(remaining), '2000', '0', str(HERE/'profile')], 'profile.log')
terminal = json.loads((HERE/'profile.terminal.json').read_text())
metadata = {
    'field': 'F2[t]/(t^6+t+1)', 'field_polynomial_binary': 67,
    'primitive_element': 2, 'action_element': 8, 'action_order': 21,
    'original_quotient_order': 42, 'central_quotient_order': 21,
    'Hbar_quotient_step': 7, 'Hbar_order': 3,
    'original_layer_sizes': [2688,448,64], 'quotient_layer_sizes': [1344,448,64],
    'normalized_involution_projections': '[(1,0),(y,0)] for y=0,...,63; identity and repeated projections retained',
    'pair_representatives_file': 'profile.quotient_pairs.json',
    'pair_representative_order': 'ascending encoded group id g=x+64*j with g<inverse(g)',
    'pair_indices': '0<=a<=b<640, allowing repeated projected pairs',
    'input_order': 'y outer; a middle; b inner ascending a,...,639',
    'raw_total': 13127680, 'HH_total_from_independent_scope': 5693310,
    'first_normalization': 'simultaneous nonzero field scaling only; H and K preserved',
    'no_additional_quotient_unit_or_projective_reduction': True,
    'lift_rules': [
        'Each noninvolutory quotient inverse pair has exactly two distinct C42 inverse-pair lifts.',
        'Repeated pair projections require the two distinct lifts; different projections admit either lift independently.',
        'Nonzero involution projection x has lifts (x,0) and (x,21).',
        'Zero involution projection has only the nonidentity lift (0,21).',
        'For y=1 the two involution lifts must be distinct.',
        'No C42 lifts were searched in this profile.'
    ],
    'filters': ['exact HH multiplicative-orbit coverage',
                'exact BB: Hbar W3 Hbar union Kbar W1 Hbar union Hbar W1 Kbar',
                'only after BB pass: quotient block/head BFS to every target layer'],
    'leaf_leaf_acceptance': 'quotient LL is not sufficient; original C42 LL must be checked',
    'profile_is_prefix_not_representative_sample': True,
    'profile_HH_target': 2000,
    'authorized_full_enumeration': False
}
(HERE/'profile_metadata.json').write_text(json.dumps(metadata, indent=2)+'\n')
summary = {'worker_count':1, 'cumulative_cpu_limit_seconds':limit,
           'cumulative_cpu_seconds':cpu()-start, 'runs':runs,
           'preflight':'preflight.json', 'profile_metadata':'profile_metadata.json',
           'terminal':terminal, 'continued_after_profile':False,
           'C42_lift_assignments_checked':0}
(HERE/'run_profile.terminal.json').write_text(json.dumps(summary, indent=2)+'\n')
print(json.dumps({k:v for k,v in terminal.items() if k not in ['BB_missing_histogram','BH_survivors']}, indent=2))
print('cumulative_cpu_seconds', cpu()-start)
