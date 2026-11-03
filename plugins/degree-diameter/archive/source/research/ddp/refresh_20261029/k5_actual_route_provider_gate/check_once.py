#!/usr/bin/env python3
"""Complete real-route provider gate; no full graph, BFS, SAT, or hashes."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import resource
import time

HERE = Path(__file__).resolve().parent
START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (20, 21))
FULL = (1 << 81) - 1


def save(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


assert not (HERE / 'HANDLE.json').exists(), 'This batch has already started.'
save('HANDLE.json', dict(pid=os.getpid(), status='RUNNING_REAL_ROUTE_PROVIDER_GATE', running=True))
print(json.dumps(dict(pid=os.getpid(), status='RUNNING_REAL_ROUTE_PROVIDER_GATE')), flush=True)
base = json.loads((HERE.parent / 'k5_q16_NB4_quotient_gate/BASE_INPUT.json').read_text())
M, V = base['matrices'], base['noise_vectors']
adj = base['port_neighbors']
inv = base['inverse_ports']
chords = {tuple(e): i + 1 for i, e in enumerate(base['chords_low_to_high'])}
coords = [[(x // (3 ** j)) % 3 for j in range(4)] for x in range(81)]


def encode(x):
    return sum(int(a) * 3 ** i for i, a in enumerate(x))


steps = [[[encode([(sum(M[p][i][j] * coords[x][j] for j in range(4)) + t * V[p][i]) % 3
                   for i in range(4)]) for t in range(3)] for x in range(81)] for p in range(4)]


def step_image(mask, p):
    out = 0
    while mask:
        bit = mask & -mask
        x = bit.bit_length() - 1
        for y in steps[p][x]:
            out |= 1 << y
        mask ^= bit
    return out


words = [((), 1)]
frontier = words[:]
for length in range(1, 5):
    frontier = [(w + (p,), step_image(mask, p)) for w, mask in frontier for p in range(4)]
    words.extend(frontier)
assert len(words) == 341
reduced4 = [(w, image) for w, image in words if len(w) == 4 and all(w[i + 1] != inv[w[i]] for i in range(3))]
assert len(reduced4) == 108 and all(image == FULL for w, image in reduced4)
assert all(image & 1 for w, image in words)

records = []
raw_words = []
for root in range(5):
    grouped = {}
    for word, image in words:
        u = root
        free = []
        for p in word:
            v = adj[u][p]
            e = tuple(sorted((u, v)))
            letter = chords.get(e, 0) * (1 if u < v else -1)
            if letter:
                if free and free[-1] == -letter:
                    free.pop()
                else:
                    free.append(letter)
            u = v
        key = (u, tuple(free))
        grouped[key] = grouped.get(key, 0) | image
        raw_words.append(dict(root=root, ports=word, target=u, freeword=free, field_image=image))
    current = []
    for (target, free), image in sorted(grouped.items()):
        parity = 0
        for letter in free:
            parity ^= 1 << (abs(letter) - 1)
        current.append(dict(target=target, freeword=list(free), paritymask=parity,
                            field_image=image, image_size=image.bit_count()))
    records.append(current)
save('REAL_ROUTE_CACHE.json', dict(base_input=str(HERE.parent / 'k5_q16_NB4_quotient_gate/BASE_INPUT.json'),
     raw_words_per_base_root=341, grouped_keys_per_root=list(map(len, records)),
     group_word_reduction_only=True, source_field_coordinate=0, roots=records))
save('RAW_WORDS.json', raw_words)
parities = [[(a & mask).bit_count() & 1 for mask in range(64)] for a in range(64)]
passes, failures = [], Counter()
witnesses = []
tested = 0
for a in range(64):
    for b in range(64):
        if time.process_time() - START > 19.5:
            save('TERMINAL.json', dict(status='UNKNOWN_PREFIX', tested=tested, total=4096,
                 CPU_seconds=time.process_time() - START, running=False))
            raise SystemExit(2)
        bad = None
        for root, rows in enumerate(records):
            # The four bit planes are thresholds >=1, >=2, >=3, >=4.
            thresholds = [[0, 0, 0, 0] for _ in range(20)]
            for row in rows:
                c = parities[a][row['paritymask']] + 2 * parities[b][row['paritymask']]
                levels = thresholds[4 * row['target'] + c]
                image = row['field_image']
                levels[3] |= levels[2] & image
                levels[2] |= levels[1] & image
                levels[1] |= levels[0] & image
                levels[0] |= image
            for slot, levels in enumerate(thresholds):
                missing = FULL ^ levels[3]
                if missing:
                    x = (missing & -missing).bit_length() - 1
                    v, c = divmod(slot, 4)
                    providers = [j for j, row in enumerate(rows)
                                 if row['target'] == v and row['field_image'] >> x & 1
                                 and parities[a][row['paritymask']] + 2 * parities[b][row['paritymask']] == c]
                    assert len(providers) < 4
                    bad = dict(root_base=root, target_base=v, coset=c, field_coordinate=x,
                               providers=providers, provider_count=len(providers), required=4)
                    break
            if bad:
                break
        values = [((a >> j) & 1) + 2 * ((b >> j) & 1) for j in range(6)]
        if bad:
            failures[f"{bad['root_base']}->{bad['target_base']}"] += 1
            witnesses.append(dict(component_masks=[a, b], chord_V4_values=values, obstruction=bad))
        else:
            passes.append(dict(component_masks=[a, b], chord_V4_values=values))
        tested += 1
save('PASS_ASSIGNMENTS.json', passes)
save('FAILURE_WITNESSES.json', witnesses)
result = dict(status='COMPLETE_ACTUAL_ROUTE_PROVIDER_GATE_HAS_PASS' if passes else 'COMPLETE_ACTUAL_ROUTE_PROVIDER_GATE_ALL4096_REJECTED',
              completed_UTC=datetime.now(timezone.utc).isoformat(), pid=os.getpid(),
              prediction_at_least_one_pass='SUPPORTED' if passes else 'REFUTED',
              full_projection_assignments=4096, tested=tested, passed=len(passes), failed=len(witnesses),
              words_per_base_root=341, roots=5, field_points_per_fiber=81, target_decks_per_coset=4,
              grouped_keys_per_root=list(map(len, records)), first_failure_slots=dict(failures),
              remaining_Q16_full_assignments=len(passes) * 4 ** 6,
              actual_D4_lift_family_excluded=not passes,
              scope='Fixed K5 base/porting, stored F3^4 chart, ordinary Q16 voltages. Necessary actual R4 gate, all words0..4 included.',
              source_graph_reads=0, BFS_runs=0, solver_calls=0, generated_80_controllers=0,
              generated_6480_graphs=0, CPU_seconds=time.process_time() - START, CPU_budget=20,
              workers=1, running=False, pending=[])
save('RESULT.json', result)
save('TERMINAL.json', result)
save('HANDLE.json', result)
print(json.dumps(result, ensure_ascii=False), flush=True)
