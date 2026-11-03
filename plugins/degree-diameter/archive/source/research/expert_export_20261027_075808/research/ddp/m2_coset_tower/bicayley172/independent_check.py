"""Check the single saved two-orbit graph from its explicit edge list."""
import json
from pathlib import Path
import resource
import subprocess
import time

start = time.process_time()
child0 = resource.getrusage(resource.RUSAGE_CHILDREN)
out = Path(__file__).resolve().parent
project = out.parents[3]
saved = json.loads((out/'profile.best.json').read_text())
q, g = 43, 86
fields = iter(saved['field_values'])
internal = []
for pairs in saved['pair_counts']:
    s = []
    for _ in range(pairs):
        x = next(fields)
        s += [(x, 0), (-x % q, 0)]
    for _ in range(saved['internal_degree']-2*pairs):
        s.append((next(fields), 1))
    assert len(s) == len(set(s)) and (0, 0) not in s
    internal.append(s)
cross_count = 7-saved['internal_degree']
cross = [(0 if i == 0 else next(fields), int(i >= cross_count-saved['odd_cross']))
         for i in range(cross_count)]
assert next(fields, None) is None and len(cross) == len(set(cross))

def product(a, b):
    x, j = a
    y, k = b
    return ((x + (-1 if j else 1)*y) % q, j ^ k)

def encode(side, v):
    return side*g + v[0] + q*v[1]

expected = set()
for x in range(q):
    for j in range(2):
        v = (x, j)
        for side in range(2):
            for s in internal[side]:
                expected.add(tuple(sorted((encode(side, v), encode(side, product(v, s))))))
        for t in cross:
            expected.add(tuple(sorted((encode(0, v), encode(1, product(v, t))))))
data = list(map(int, (out/'profile.best.edges').read_text().split()))
assert data[:2] == [172, 602] and len(data) == 1206
edges = list(zip(data[2::2], data[3::2]))
assert all(0 <= u < v < 172 for u, v in edges)
assert len(set(edges)) == 602 and set(edges) == expected
check = subprocess.run([str(project/'computations/ddp/verify_graph'),
                        str(out/'profile.best.edges'), '7', '3'], capture_output=True, text=True)
assert check.returncode in (0, 1), check.stderr
result = json.loads(check.stdout)
assert result['n'] == result['roots_checked'] == 172 and result['m'] == 602
assert result['min_degree'] == result['max_degree'] == 7
assert result['unreachable_unordered_pairs'] == 0
assert result['diameter'] == saved['diameter'] == 4
assert result['bad_unordered_pairs'] == saved['bad_unordered_pairs'] == 688
assert result['bad_unordered_pairs'] == 43*sum(saved['root_misses'])
child1 = resource.getrusage(resource.RUSAGE_CHILDREN)
own = time.process_time()-start
child = child1.ru_utime+child1.ru_stime-child0.ru_utime-child0.ru_stime
result.update(simple=True, connected=True, independently_rebuilt_edges_equal=True,
              independent_reconstruction_CPU_seconds=own, checker_CPU_seconds=child,
              total_CPU_seconds=own+child,
              scope='Only the saved best172 graph; one all172root check, no search.')
(out/'profile.best.independent_verify.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
