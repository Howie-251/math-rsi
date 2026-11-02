"""Count one fixed critical slot in the integral quaternion module; no graph BFS."""
from pathlib import Path
import json
import time

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / 'CONTROL_CAPACITY_ROOT.json').read_text())
mt = data['Q8_multiplication']
started = time.process_time()
prediction = {
    'kind': 'pre-enumeration structural prediction on the already fixed torsor-voltage model',
    'question': 'Do universal quaternion-module identities force too few endpoints in the raw-thinnest slots, independently of finite-field matrices?',
    'predictions': [
        {'D': 9, 'source_base': 2, 'target_controller': 20, 'raw_count': 29, 'predicted_universal_distinct_less_than': 25},
        {'D': 10, 'source_base': 2, 'target_controller': 24, 'raw_count': 66, 'predicted_universal_distinct_less_than': 49},
    ],
    'scope': 'Integral Hamilton quaternion coefficients acting on a chosen vector. No target graph or source360 BFS. Counts at least the module size refute this obstruction, and do not certify coverage.',
}
(HERE / 'UNIVERSAL_ENDPOINT_PREDICTION_ROOT.json').write_text(json.dumps(prediction, indent=2) + '\n')
zero = (0, 0, 0, 0)


def rotate(h, vector):
    out = [0, 0, 0, 0]
    for k, a in enumerate(vector):
        unit = mt[h][k]
        out[unit % 4] += a * (-1 if unit >= 4 else 1)
    return tuple(out)


def negative(vector):
    return tuple(-a for a in vector)


rows = [[] for _ in range(5)]


def add_edge(a, b, h, vector):
    inverse = next(t for t in range(8) if mt[h][t] == 0)
    rows[a].append((b, h, vector))
    rows[b].append((a, inverse, negative(rotate(inverse, vector))))


for b in [2, 3, 4]:
    add_edge(0, b, 0, zero)
add_edge(1, 4, 0, zero)
add_edge(1, 2, 5, zero)
add_edge(1, 3, 6, (0, -1, 0, 0))
for b, vector in [(2, (1, 0, 0, 0)), (3, (0, 0, 1, 0)), (4, (0, 1, 0, 0))]:
    rows[b].append((b, 4, vector))
assert all(len(x) == 3 for x in rows)
images = {9: [], 10: []}
all_prefixes = 0


def walk(base, h, vector, previous, depth):
    global all_prefixes
    all_prefixes += 1
    vertex = 8 * base + h
    if depth <= 9 and vertex == 20:
        images[9].append(vector)
    if vertex == 24:
        images[10].append(vector)
    if depth == 10:
        return
    for b, g, w in rows[base]:
        new_h = mt[h][g]
        if 8 * b + new_h == previous:
            continue
        translated = rotate(h, w)
        walk(b, new_h, tuple(vector[k] + translated[k] for k in range(4)), vertex, depth + 1)


walk(2, 0, zero, -1, 0)
assert all_prefixes == 3070
assert len(images[9]) == 29 and len(images[10]) == 66
results = {}
for diameter, values in images.items():
    unique = sorted(set(values))
    required = 25 if diameter == 9 else 49
    results[str(diameter)] = {
        'source_base': 2,
        'target_controller': 20 if diameter == 9 else 24,
        'raw_count': len(values),
        'universal_distinct_count': len(unique),
        'required_module_size': required,
        'strict_universal_obstruction': len(unique) < required,
        'universal_quaternion_endpoints': unique,
        'endpoint_multiplicities': [{'coeff': u, 'multiplicity': values.count(u)} for u in unique],
    }
output = {
    'model': 'fixed torsor Q8 voltages evaluated from integral quaternion module',
    'results': results,
    'new_graphs': 0,
    'new_BFS': 0,
    'source360_BFS': 0,
    'CPU_seconds': time.process_time() - started,
}
(HERE / 'UNIVERSAL_ENDPOINT_RESULT_ROOT.json').write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps({d: {k: v for k, v in row.items() if k not in ['universal_quaternion_endpoints', 'endpoint_multiplicities']} for d, row in results.items()}))
