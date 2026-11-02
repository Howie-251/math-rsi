#!/usr/bin/env python3
from pathlib import Path
import collections
import json
import os
import resource
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
INPUT = ROOT / 'research/ddp/more_graphs_20261027/d15_loop_completed_quotient_probe/affine_relation_recovery/source15552_AFFINE_RELATIONS.json'
BUDGET = 20.0
PREP_CHARGE = 0.2
resource.setrlimit(resource.RLIMIT_CPU, (19, 20))


def save(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def signed(x):
    return -1 if x == 2 else x


def convert(a):
    return {'from': a['from'], 'to': a['to'],
            'B': [[signed(x) % 2 for x in row] for row in a['B']],
            'v': [signed(x) % 2 for x in a['v']],
            'c': [signed(x) % 2 for x in a['c']]}


def decode(n):
    return [(n >> i) & 1 for i in range(4)]


def encode(x):
    return sum(z << i for i, z in enumerate(x))


def step(a, x, t):
    return [(sum(a['B'][i][j] * x[j] for j in range(4)) + a['c'][i] + t * a['v'][i]) % 2 for i in range(4)]


save('HANDLE.json', {'pid': os.getpid(), 'phase': 'new_binary_relation_basic_gate', 'running': True,
                     'worker_count': 1, 'CPU_budget_seconds': BUDGET, 'preparation_charge_seconds': PREP_CHARGE})
raw = json.loads(INPUT.read_text())
arcs = raw['arcs']
assert raw['controller_count'] == 192 and len(arcs) == 960
by_from = collections.defaultdict(list)
for a in arcs:
    by_from[a['from']].append(a)
first = by_from[0]
assert len(first) == 5
binary = [convert(a) for a in first]
save('NEW_BINARY_GLOBAL_TYPES.json', {'rule': '0→0,1→1,2→integer−1,then mod2',
                                     'parameter_domain': 'F2^4, noise F2', 'types_in_controller0_target_order': binary})
checked = 0
virtual_stays = 0
failure = None
for p, original in enumerate(first):
    a = binary[p]
    reverse_original = [z for z in by_from[a['to']] if z['to'] == 0]
    reverse = [convert(z) for z in reverse_original]
    for code in range(16):
        x = decode(code)
        outputs = [step(a, x, t) for t in range(2)]
        if outputs[0] == outputs[1]:
            failure = {'kind': 'DUPLICATE_NOISE_OUTPUTS', 'global_type': p, 'input_coordinates': x,
                       'output_coordinates': outputs[0], 'original_arc': original, 'binary_arc': a}
            break
        for t, y in enumerate(outputs):
            u, v = code, 16 * a['to'] + encode(y)
            if u == v:
                virtual_stays += 1
                continue
            checked += 1
            candidates = [{'reverse_controller': r['to'], 'noise': s, 'coordinates': step(r, y, s),
                           'label': 16 * r['to'] + encode(step(r, y, s))}
                          for r in reverse for s in range(2)]
            if not any(z['label'] == u for z in candidates):
                failure = {'kind': 'ACTUAL_DIRECTED_RELATION_NOT_RECIPROCAL', 'global_type': p,
                           'source_label': u, 'target_label': v,
                           'input_controller': 0, 'output_controller': a['to'],
                           'input_coordinates': x, 'noise': t, 'output_coordinates': y,
                           'original_arc': original, 'signed_integer_B': [[signed(z) for z in row] for row in original['B']],
                           'signed_integer_v': [signed(z) for z in original['v']], 'binary_arc': a,
                           'reverse_original_arcs': reverse_original, 'reverse_binary_arcs': reverse,
                           'all_actual_reverse_noise_candidates': candidates,
                           'reverse_target_arc_count': len(reverse), 'entire_global_labels_are_distinct': u != v}
                break
        if failure:
            break
    if failure:
        break

graph_roots = 0
graph_generated = False
if failure:
    status = 'STOP_SIGNED_F2_TRUE_INVERSE_FAILURE' if failure['kind'] == 'ACTUAL_DIRECTED_RELATION_NOT_RECIPROCAL' else 'STOP_SIGNED_F2_DUPLICATE_NEIGHBORS'
    save('COUNTEREXAMPLE.json', failure)
else:
    # This branch is only for a basic-gate survivor; no old graph is parsed.
    actual = [convert(a) for a in arcs]
    adj = [set() for _ in range(3072)]
    for a in actual:
        for code in range(16):
            u = 16 * a['from'] + code
            for t in range(2):
                v = 16 * a['to'] + encode(step(a, decode(code), t))
                if u != v:
                    adj[u].add(v)
    bad = next(((u, v) for u in range(3072) for v in adj[u] if u not in adj[v]), None)
    if bad:
        failure = {'kind': 'FULL_NEW_RELATION_NOT_RECIPROCAL', 'edge': list(bad)}
        status = 'STOP_SIGNED_F2_TRUE_INVERSE_FAILURE'
        save('COUNTEREXAMPLE.json', failure)
    else:
        assert max(map(len, adj)) <= 10
        graph_generated = True
        status = 'UNKNOWN_NEW_TARGET_RADIUS4_CPU_CAP'
        for root in range(3072):
            if PREP_CHARGE + time.process_time() > BUDGET - 0.5:
                break
            d = [-1] * 3072
            d[root] = 0
            queue = collections.deque([root])
            while queue:
                v = queue.popleft()
                if d[v] == 4:
                    continue
                for w in adj[v]:
                    if d[w] < 0:
                        d[w] = d[v] + 1
                        queue.append(w)
            graph_roots += 1
            missing = next((v for v in range(3072) if d[v] < 0), None)
            if missing is not None:
                status = 'STOP_NEW3072_DIAMETER4_FAILURE'
                failure = {'kind': 'NEW_TARGET_PAIR_NO_WALK_AT_MOST4', 'source': root, 'target': missing}
                save('COUNTEREXAMPLE.json', failure)
                break
        else:
            status = 'NEW3072_D4_CANDIDATE_PENDING_ROOT_ACCEPTANCE'
            edges = [(u, v) for u in range(3072) for v in sorted(adj[u]) if u < v]
            with (HERE / 'graph_d10_D4_n3072.edges').open('w') as out:
                out.write(f'3072 {len(edges)}\n')
                for u, v in edges:
                    out.write(f'{u} {v}\n')

result = {'status': status,
          'prediction': 'Actual type1/reverse-type3 signed-F2 relation fails to return x=0 after noise1; no automatic transfer.',
          'prediction_supported': bool(failure and failure.get('source_label') == 0 and failure.get('target_label') == 183),
          'hypothetical_target': {'order': 3072, 'maximum_degree': 10, 'diameter': 4},
          'input': str(INPUT.relative_to(ROOT)), 'coefficient_rule': '0→0,1→1,2→integer−1 then mod2; no field homomorphism claimed',
          'source_controller_count': 192, 'source_relation_records_read': 960,
          'global_types_read': 5, 'new_true_arc_reverse_tests_before_stop': checked,
          'new_actual_global_stays_skipped': virtual_stays, 'counterexample': failure,
          'graph_generated': graph_generated, 'new_target_BFS_roots': graph_roots,
          'old_F3_field_rank_graph_BFS_Lean_checks': 0, 'solver_ARIS_remote_install_or_hash': 0,
          'alternative_lift_or_field': 0, 'exact_scope': 'Only the specified literal signed-integer then F2 transfer of these actual five templates/controller.',
          'not_excluded': ['other binary relations', 'other generators or integer lifts', 'general degree10 diameter4 graphs'],
          'preparation_charge_seconds': PREP_CHARGE, 'actual_process_CPU_seconds': time.process_time(),
          'total_charged_CPU_seconds': PREP_CHARGE + time.process_time(), 'CPU_budget_seconds': BUDGET,
          'worker_count': 1, 'root_files_modified': False, 'graph_parameter_Lean_increment': [0, 0, 0],
          'next': 'STOP_REPORT_EXACT_WITNESS_NO_SYMMETRIZATION_OR_SECOND_LIFT'}
save('RESULT.json', result)
if failure and failure.get('source_label') == 0:
    explanation = ('The actual binary forward relation sends controller0/coordinate0 to controller11/coordinate(1,1,1,0), label183. '
                   'The only reverse-controller relation produces labels2 or13, never0. The endpoints differ, so deleting virtual self loops does not remove this failure. '
                   'Forcing undirected union adjacency would be a different untested rule and would lose the stated ten-forward-neighbor degree guarantee.')
else:
    explanation = f'Actual status{status}; detailed evidence is in RESULT.json and COUNTEREXAMPLE.json if applicable.'
(HERE / 'NOTE.md').write_text(f'''# Literal signed-F2 transfer result

{explanation}

The signed integer B3*v1 residual−3e1 disappears in characteristic3 and survives as e1 in characteristic2, outside the span of the binary reverse noise direction(1,1,1,1). Thus some old integer identities survive (type0), while the required full reverse relation does not. No field-homomorphism assumption was used.

The old signed-five-frame gate is different: it stopped before binary arc construction on a projective-frame prerequisite. Here the new literal-coefficient rule was actually tested and stopped on its own concrete nonreciprocal edge. The accepted F3 source and all its old graph/field/rank/formal checks remain inherited; none was rerun. See PAPER_INTERFACE.md for the independent paper prediction.

Actual new target graph/BFS counts:{graph_generated}/{graph_roots}. No symmetrization, second lift, other characteristic, ARIS, solver, Lean or review follows. This closes only the specified literal signed rule, not all binary constructions or(10,4). Budget20CPU includes preparation0.2 and the single process; root owns acceptance and global documents.
''')
terminal = {'status': status, 'running': False, 'all_processes_terminal': True,
            'preparation_charge_seconds': PREP_CHARGE, 'actual_process_CPU_seconds': time.process_time(),
            'total_charged_CPU_seconds': PREP_CHARGE + time.process_time(), 'CPU_budget_seconds': BUDGET,
            'worker_count': 1, 'no_timer_reset': True, 'no_automatic_continuation': True}
save('TERMINAL.json', terminal)
save('HANDLE.json', {'pid': os.getpid(), 'phase': 'terminal', **terminal})
print(json.dumps({'result': result, 'terminal': terminal}, ensure_ascii=False, indent=2))
