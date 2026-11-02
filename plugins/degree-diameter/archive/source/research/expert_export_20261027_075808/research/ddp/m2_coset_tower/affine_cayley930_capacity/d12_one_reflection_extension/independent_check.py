"""Independently rebuild and fully check the single saved 930-point graph."""
import json
import resource
import subprocess
import time
from pathlib import Path

start = time.process_time()
c0 = resource.getrusage(resource.RUSAGE_CHILDREN)
out = Path(__file__).resolve().parent
project = out.parents[4]
saved = json.loads((out/'best.json').read_text())
S = saved['S']
assert len(S) == len(set(S)) == 12 and 0 not in S
assert len({pow(3, j, 31) for j in range(30)}) == 30

def multiply(a, b):
    x, j = a % 31, a // 31
    y, k = b % 31, b // 31
    return (x + pow(3, j, 31)*y) % 31 + 31*((j+k) % 30)

def inverse(a):
    x, j = a % 31, a // 31
    return (-pow(3, -j, 31)*x) % 31 + 31*((-j) % 30)

assert {inverse(a) for a in S} == set(S)
expected = {tuple(sorted((v, multiply(v, s)))) for v in range(930) for s in S}
data = list(map(int, (out/'best.edges').read_text().split()))
assert data[:2] == [930, 5580] and len(data) == 11162
edges = list(zip(data[2::2], data[3::2]))
assert all(0 <= u < v < 930 for u, v in edges)
assert len(set(edges)) == 5580 and set(edges) == expected
run = subprocess.run([str(project/'computations/ddp/verify_graph'),
                      str(out/'best.edges'), '12', '3'],
                     capture_output=True, text=True)
assert run.returncode in (0, 1), run.stderr
v = json.loads(run.stdout)
assert v['n'] == v['roots_checked'] == 930 and v['m'] == 5580
assert v['min_degree'] == v['max_degree'] == 12
assert v['unreachable_unordered_pairs'] == 0
assert v['diameter'] == saved['diameter'] == 4
assert v['bad_unordered_pairs'] == saved['bad_unordered_pairs'] == 31155
assert {int(d): n for d, n in v['ordered_distance_histogram'].items()} == {
    int(d): 930*n for d, n in saved['root_distance_histogram'].items()}
c1 = resource.getrusage(resource.RUSAGE_CHILDREN)
own = time.process_time()-start
child = c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime
v.update(simple=True, connected=True, independent_edges_exactly_equal=True,
         independent_reconstruction_CPU_seconds=own, generic_checker_CPU_seconds=child,
         total_CPU_seconds=own+child,
         scope='Only saved best930 degree12 extension graph; one generic all930root check; no search.')
(out/'best.independent_check.json').write_text(json.dumps(v, indent=2)+'\n')
print(json.dumps(v, indent=2))
