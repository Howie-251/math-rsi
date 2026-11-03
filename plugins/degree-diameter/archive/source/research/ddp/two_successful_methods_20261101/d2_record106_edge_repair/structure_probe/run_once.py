import time
start = time.process_time()
import collections
import json
from pathlib import Path
import resource
resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
D = Path(__file__).resolve().parent
C = D.parent
prior = json.loads((C/'internal_pin_rewiring/TERMINAL.json').read_text())['case_CPU_seconds']
A = [set() for _ in range(106)]
with (C/'source106.header.edges').open() as f:
    f.readline()
    for line in f:
        u, v = map(int, line.split())
        A[u].add(v); A[v].add(u)
fixed = {7, 17, 23, 34, 46, 54, 59, 105}
signatures = [('fixed', v) if v in fixed else ('free', tuple(sorted(A[v]&fixed)))
              for v in range(106)]
def colors_of(keys):
    table = {}
    return [table.setdefault(k, len(table)) for k in keys]
colors = colors_of(signatures)
rounds = 0
while True:
    keys = [(colors[v], tuple(sorted(collections.Counter(colors[w] for w in A[v]).items())))
            for v in range(106)]
    updated = colors_of(keys)
    rounds += 1
    if updated == colors:
        break
    colors = updated
classes = collections.defaultdict(list)
for v, c in enumerate(colors):
    classes[c].append(v)
unique = {}
for u in range(106):
    bycolor = collections.defaultdict(list)
    for v in A[u]:
        if v not in fixed:
            bycolor[colors[v]].append(v)
    unique[u] = {c: vs[0] for c, vs in bycolor.items() if len(vs) == 1}
accepted, rejected, incomplete = [], [], []
for image in classes[colors[0]]:
    perm = {f: f for f in fixed}
    inverse = {f: f for f in fixed}
    perm[0] = image; inverse[image] = 0
    queue = [0]
    fail = None
    for u in queue:
        for color, v in unique[u].items():
            if color not in unique[perm[u]]:
                fail = 'unique-neighbor mismatch'; break
            w = unique[perm[u]][color]
            if v in perm:
                if perm[v] != w:
                    fail = 'forced image conflict'; break
            elif w in inverse:
                fail = 'injectivity conflict'; break
            else:
                perm[v] = w; inverse[w] = v; queue.append(v)
        if fail:
            break
    if fail:
        rejected.append(dict(image_of_0=image, reason=fail, forced_labels=len(perm)))
    elif len(perm) < 106:
        incomplete.append(dict(image_of_0=image, forced_labels=len(perm)))
    else:
        p = [perm[v] for v in range(106)]
        if all({p[w] for w in A[v]} == A[p[v]] for v in range(106)):
            accepted.append(p)
        else:
            rejected.append(dict(image_of_0=image, reason='actual adjacency mismatch'))
generator = next((p for p in accepted if p != list(range(106))), None)
orbits = []
order = None
if generator:
    power = list(range(106)); order = 0
    while True:
        power = [generator[v] for v in power]; order += 1
        if power == list(range(106)):
            break
        assert order <= 106
    unseen = set(range(106))
    while unseen:
        v = min(unseen); orbit = [v]; w = generator[v]
        while w != v:
            orbit.append(w); w = generator[w]
        unseen -= set(orbit); orbits.append(orbit)
profiles = json.loads((C/'CRITICAL_EDGE_PROFILES.json').read_text())['profiles']
directional = sum(len(r['u_unique_via_v_targets'])+len(r['v_unique_via_u_targets']) for r in profiles)
assert directional % 2 == 0
twins = collections.defaultdict(list)
for u in range(106):
    twins[tuple(sorted(A[u]))].append(u)
twins = [vs for vs in twins.values() if len(vs) > 1]
common_before = sorted(A[7]&A[12])
def changed(deleted, added):
    B = [set(x) for x in A]
    for u, v in deleted:
        B[u].discard(v); B[v].discard(u)
    for u, v in added:
        B[u].add(v); B[v].add(u)
    return B
first = changed([(7, 17)], [])
second = changed([(7, 105)], [])
both = changed([(64, 0), (7, 17), (7, 105), (5, 1)], [(64, 7), (7, 5)])
route = dict(twins17_105=A[17] == A[105], common_7_12=common_before,
    common_after_deleting7_17=sorted(first[7]&first[12]),
    common_after_deleting7_105=sorted(second[7]&second[12]),
    two_repair_64_to_5_common=sorted(both[64]&both[5]),
    two_repair_7_to_12_adjacent=12 in both[7],
    two_repair_7_to_12_common=sorted(both[7]&both[12]))
assert route['twins17_105'] and common_before == [17, 105]
assert route['common_after_deleting7_17'] == [105]
assert route['common_after_deleting7_105'] == [17]
assert route['two_repair_64_to_5_common'] and not route['two_repair_7_to_12_adjacent']
assert not route['two_repair_7_to_12_common']
T = {34, 54}; closed = T | A[34] | A[54]
result = dict(status='ORDER7_ACTION_FOUND' if order == 7 else 'SYMMETRY_UNRESOLVED',
    prediction_order7_supported=order == 7, fixed_labels=sorted(fixed),
    color_refinement_rounds=rounds, color_classes=list(classes.values()),
    color_class_sizes=sorted(map(len, classes.values())),
    complete_verified_permutations=accepted, rejected=rejected, incomplete=incomplete,
    generator=generator, generator_order=order, orbits=orbits,
    open_twin_classes=twins, critical_directional_count=directional,
    unique_common_neighbor_nonadjacent_pairs=directional//2,
    total_nonadjacent_pairs=106*105//2-582,
    spare_closed_neighborhood_size=len(closed),
    controlled_route_predictions=route, new_graph_or_Lean_increment=0,
    graph_BFS=0, source_validity_reruns=0, solver_calls=0,
    prior_case_CPU_seconds=prior, batch_CPU_seconds=time.process_time()-start,
    case_CPU_seconds=prior+time.process_time()-start, case_CPU_budget_seconds=20)
(D/'RESULT.json').write_text(json.dumps(result, indent=2)+'\n')
(D/'TERMINAL.json').write_text(json.dumps(dict(status=result['status'],running=False,
    case_CPU_seconds=prior+time.process_time()-start,case_CPU_budget_seconds=20),indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in [
    'complete_verified_permutations','generator','orbits','color_classes']},ensure_ascii=False))
print('orbits',orbits)
