"""One fixed PSL2(F25)/unipotent-C5 valence5+matching profile."""
from collections import Counter, deque
from pathlib import Path
import json
import resource
import runpy
import time

OUT = Path(__file__).resolve().parent
OLD = OUT.parent / 'q25_c4_profile'
N = 1560
START = None
STATE = {'stage': 'not_started', 'completed': 0}


class BudgetReached(Exception):
    pass


def cpu():
    return time.process_time() - START


def checkpoint():
    if cpu() >= 58:
        raise BudgetReached()


def save(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2) + '\n')


def root_R5(masks):
    seen = front = 1
    for _ in range(5):
        nxt = 0
        while front:
            bit = front & -front
            front -= bit
            nxt |= masks[bit.bit_length() - 1]
        front = nxt & ~seen
        seen |= front
    return seen


def orbital(item, perms, bits):
    start = item['representative_pair'][1]
    edges, todo = {start}, [start]
    popped = 0
    while todo:
        if not popped % 512:
            checkpoint()
        a, b = divmod(todo.pop(), N)
        popped += 1
        for p in perms:
            u, v = p[a], p[b]
            if u > v:
                u, v = v, u
            code = u * N + v
            if code not in edges:
                edges.add(code)
                todo.append(code)
    masks = [0] * N
    for code in edges:
        a, b = divmod(code, N)
        assert a != b
        masks[a] |= bits[b]
        masks[b] |= bits[a]
    assert len(edges) == N * item['degree'] // 2
    assert all(row.bit_count() == item['degree'] for row in masks)
    assert masks[0] == sum(bits[v] for v in item['root_neighbors'])
    return masks, edges


def prepare():
    STATE['stage'] = 'new_C5_action_preparation'
    module = runpy.run_path(str(OLD / 'run.py'))
    field = module['PSL25']()
    old = json.loads((OLD / 'inputs.json').read_text())
    # Reconstruct the saved group exactly from its cached C4 cosets, rather
    # than calling elements() or regenerating the old action/graphs.
    G = {field.mul(tuple(x), tuple(h))
         for x in old['right_coset_representatives'] for h in old['H']}
    assert len(G) == 7800
    G = sorted(G)
    G.remove(field.I)
    G.insert(0, field.I)
    index = {g: i for i, g in enumerate(G)}
    H = [(1, t, 0, 1) for t in range(5)]
    Hset = set(H)
    S = (2, 0, 0, 3)
    U1, Uu = (1, 1, 0, 1), (1, 5, 0, 1)
    W = field.canon((0, field.neg[1], 1, 0))
    generators = [U1, Uu, W]
    assert field.mul(S, S) == field.I
    assert field.mul(field.mul(S, U1), field.inv(S)) == field.inv(U1)
    checkpoint()
    # Checking the image of the cyclic generator is sufficient here.
    normalizer = {g for g in G
                  if field.mul(field.mul(g, U1), field.inv(g)) in Hset}
    assert len(normalizer) == 100
    lookup = [-1] * len(G)
    reps = []
    for x in G:
        if lookup[index[x]] >= 0:
            continue
        j = len(reps)
        members = {index[field.mul(x, h)] for h in H}
        assert len(members) == 5 and all(lookup[z] < 0 for z in members)
        reps.append(x)
        for z in members:
            lookup[z] = j
    assert len(reps) == N and all(v >= 0 for v in lookup)
    assert reps[0] == field.I
    perms = [[lookup[index[field.mul(s, x)]] for x in reps]
             for s in generators]
    assert all(sorted(p) == list(range(N)) for p in perms)
    # This is new-action transitivity, not a repeat of the old group audit.
    reached, todo = {0}, [0]
    while todo:
        v = todo.pop()
        for p in perms:
            w = p[v]
            if w not in reached:
                reached.add(w)
                todo.append(w)
    assert len(reached) == N
    checkpoint()
    normalizer_cosets = {lookup[index[x]] for x in normalizer}
    assert len(normalizer_cosets) == 20
    involutions = {x for x in G[1:] if field.mul(x, x) == field.I}
    invol_N = involutions & normalizer
    outside = involutions - normalizer
    assert len(involutions) == 325 and len(invol_N) == 25 and len(outside) == 300
    matching_root = lookup[index[S]]
    assert matching_root != 0
    assert {lookup[index[field.mul(h, S)]] for h in H} == {matching_root}
    matching_conjugates = {
        lookup[index[field.mul(field.mul(n, S), field.inv(n))]]
        for n in normalizer}
    matching_all = {lookup[index[t]] for t in invol_N}
    assert matching_conjugates == matching_all and len(matching_all) == 5
    choices, keys = [], set()
    remaining = set(outside)
    Hinv = [field.inv(h) for h in H]
    while remaining:
        t = min(remaining)
        orbit = {field.mul(field.mul(h, t), hi) for h, hi in zip(H, Hinv)}
        assert len(orbit) == 5 and orbit <= remaining
        remaining -= orbit
        neighbors = tuple(sorted({lookup[index[field.mul(h, t)]] for h in H}))
        assert len(neighbors) == 5 and not set(neighbors) & normalizer_cosets
        assert neighbors not in keys
        keys.add(neighbors)
        choices.append({'id': len(choices), 'degree': 5, 'involution': t,
                        'H_conjugacy_class': sorted(orbit),
                        'representative_pair': [0, lookup[index[t]]],
                        'root_neighbors': neighbors})
    assert len(choices) == 60
    matching = {'id': 'matching', 'degree': 1, 'involution': S,
                'representative_pair': [0, matching_root],
                'root_neighbors': [matching_root]}
    save('inputs.json', {
        'field': old['field'], 'group_order': len(G), 'H': H,
        'right_coset_count': N, 'right_coset_representatives': reps,
        'permutation_generators': generators, 'left_permutations': perms,
        'new_action_transitive_orbit_size': len(reached),
        'normalizer': sorted(normalizer), 'normalizer_order': len(normalizer),
        'normalizer_cosets': sorted(normalizer_cosets),
        'total_involutions': len(involutions), 'normalizer_involutions': len(invol_N),
        'outside_involutions': len(outside),
        'matching_cosets_N_conjugacy_orbit': sorted(matching_conjugates),
        'fixed_matching': matching, 'external_valence5_items': choices,
        'scope_count': 60, 'target_Delta': 6, 'target_D': 5, 'savedL': 1518,
        'group_elements_reused_from': 'q25_c4_profile/inputs.json C4 representatives times H4',
        'new_group_elements_enumeration': False,
    })
    return choices, matching, perms, normalizer_cosets, reps, H


def run():
    global START
    START = time.process_time()
    resource.setrlimit(resource.RLIMIT_CPU, (60, 61))
    assert json.loads((OUT / 'PREDICTION.json').read_text())['frozen_before_candidate_evaluation']
    assert not (OUT / 'RESULT.json').exists(), 'This fixed branch already has a terminal result.'
    cases, hit = [], None
    try:
        choices, matching, perms, normalizer_cosets, reps, H = prepare()
        bits = [1 << v for v in range(N)]
        normalizer_mask = sum(bits[v] for v in normalizer_cosets)
        fixed_masks, fixed_edges = orbital(matching, perms, bits)
        preparation = cpu()
        save('prepare.json', {'status': 'READY', 'CPU_seconds': preparation,
                             'scope': 60, 'n': N, 'normalizer_cosets': 20})
        print(json.dumps({'stage': 'READY', 'CPU_seconds': preparation,
                          'n': N, 'scope': 60}), flush=True)
        STATE['stage'] = 'fixed60_R5'
        for item in choices:
            checkpoint()
            masks5, edges5 = orbital(item, perms, bits)
            masks = [a | b for a, b in zip(fixed_masks, masks5)]
            assert all(row.bit_count() == 6 for row in masks)
            seen = root_R5(masks)
            nn = (seen & normalizer_mask).bit_count()
            case = {'case_index': item['id'], 'involution': item['involution'],
                    'root_R5_reached': seen.bit_count(), 'root_R5_missing': N - seen.bit_count(),
                    'normalizer_R5_reached': nn, 'normalizer_R5_missing': 20 - nn,
                    'outside_R5_reached': seen.bit_count() - nn,
                    'outside_R5_missing': 1540 - (seen.bit_count() - nn)}
            cases.append(case)
            STATE['completed'] = len(cases)
            if len(cases) == 1:
                dist = [-1] * N
                dist[0] = 0
                todo = deque([0])
                while todo:
                    v = todo.popleft()
                    if dist[v] == 5:
                        continue
                    row = masks[v]
                    while row:
                        bit = row & -row
                        row -= bit
                        w = bit.bit_length() - 1
                        if dist[w] < 0:
                            dist[w] = dist[v] + 1
                            todo.append(w)
                assert sum(bits[v] for v, d in enumerate(dist) if d >= 0) == seen
                save('first_calibration.json', {
                    'one_new_ordinary_root_R5_matches_bitset': True,
                    'degree6_every_vertex': True, 'n': N,
                    'root_reached': seen.bit_count(),
                    'distance_histogram_0_to_5': dict(Counter(d for d in dist if d >= 0)),
                    'roots': 1, 'old_graph_BFS': 0})
            if not case['root_R5_missing']:
                all_edges = fixed_edges | edges5
                assert len(all_edges) == 4680
                edgefile = OUT / 'hit1560.edges'
                with edgefile.open('w') as f:
                    f.write('1560 4680\n')
                    for code in sorted(all_edges):
                        a, b = divmod(code, N)
                        f.write(f'{a} {b}\n')
                hit = {'status': 'PRODUCER_FULL_HIT_PENDING_ROOT', 'n': N, 'm': 4680,
                       'max_degree': 6, 'target_D': 5, 'savedL': 1518,
                       'field': 'GF25=F5[u]/(u^2-2), code a+5b', 'H': H,
                       'matching': matching, 'external_orbital': item,
                       'coset_representatives': reps, 'edgefile': edgefile.name,
                       'rule': 'Union of the two unordered-pair G-orbits under left multiplication on right H cosets.',
                       'producer_full_root_R5': True,
                       'transitive_action': True, 'independent_check_pending': True,
                       'new_lower_bound_claimed': False}
                save('hit_parameters.json', hit)
                print(json.dumps({'stage': 'FULL_HIT', 'case': item['id'], 'CPU_seconds': cpu()}), flush=True)
                break
            if len(cases) == 8:
                elapsed = cpu() - preparation
                forecast = preparation + elapsed * 60 / 8
                save('profile8.json', {'completed': 8, 'CPU_seconds': elapsed,
                                      'projected_total_CPU_seconds': forecast,
                                      'budget_CPU_seconds': 60})
                if forecast > 57:
                    STATE['stage'] = 'first8_forecast_exceeds_budget'
                    break
    except BudgetReached:
        STATE['stage'] = 'CPU_budget_stop'
    except AssertionError as exc:
        save('structural_stop.json', {'stage': STATE['stage'], 'reason': str(exc),
                                     'completed': STATE['completed'], 'CPU_seconds': cpu()})
        raise
    complete = len(cases) == 60
    status = ('COMPLETE_HIT_PENDING_ROOT' if hit else
              'COMPLETE_NO_HIT_FIXED60' if complete else 'BUDGET_UNKNOWN_NO_HIT')
    save('cases.json', cases)
    result = {'status': status, 'running': False, 'n': N,
              'target_Delta': 6, 'target_D': 5, 'savedL': 1518,
              'evaluated': len(cases), 'scope_count': 60, 'unprocessed': 60 - len(cases),
              'scope_exhausted': complete, 'full_hits': int(hit is not None),
              'minimum_root_R5_missing': min((x['root_R5_missing'] for x in cases), default=None),
              'normalizer_R5_reached_range': [min((x['normalizer_R5_reached'] for x in cases), default=None),
                                                max((x['normalizer_R5_reached'] for x in cases), default=None)],
              'outside_R5_reached_range': [min((x['outside_R5_reached'] for x in cases), default=None),
                                             max((x['outside_R5_reached'] for x in cases), default=None)],
              'P1_NORMALIZER_COVER': ('SUPPORTED' if any(x['normalizer_R5_missing'] == 0 for x in cases)
                                      else 'REFUTED' if complete else 'UNRESOLVED'),
              'CPU_seconds': cpu(), 'CPU_budget_seconds': 60,
              'new_ordinary_root_calibrations': int(bool(cases)), 'old_graph_BFS': 0,
              'allsource_BFS': 0, 'old_group_enumerations': 0,
              'actual_D': None, 'ordinary_bad_unordered_pairs': None,
              'scope': 'Only fixed PSL2(F25)/F5-unipotent-C5 action, fixed normalizer matching S and all60 external involution H-classes.',
              'decision': 'Stop this branch; no automatic field/subgroup followup.'}
    save('RESULT.json', result)
    save('terminal.json', result)
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    run()
