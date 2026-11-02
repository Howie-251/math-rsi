"""One independent edge reconstruction and all-root check of saved best812."""
import json
import resource
import subprocess
import time
from pathlib import Path

start = time.process_time()
child0 = resource.getrusage(resource.RUSAGE_CHILDREN)
out = Path(__file__).resolve().parent
project = out.parents[4]
saved = json.loads((out/'production.best.json').read_text())
S = saved['S']
assert len(S) == len(set(S)) == 12 and 0 not in S
assert len({pow(2, j, 29) for j in range(28)}) == 28

def inverse(a):
    x, j = a % 29, a // 29
    return (-pow(2, -j, 29)*x) % 29 + 29*((-j) % 28)

def multiply(a, b):
    x, j = a % 29, a // 29
    y, k = b % 29, b // 29
    return (x+pow(2, j, 29)*y) % 29 + 29*((j+k) % 28)

from_components = []
for x,j in zip(saved['fields'], saved['pair_phases']):
    a = x+29*j
    from_components += [a, inverse(a)]
assert from_components == S and {inverse(s) for s in S} == set(S)
expected = {tuple(sorted((v, multiply(v,s)))) for v in range(812) for s in S}
data = list(map(int, (out/'production.best.edges').read_text().split()))
assert data[:2] == [812,4872] and len(data) == 9746
edges = list(zip(data[2::2], data[3::2]))
assert all(0 <= u < v < 812 for u,v in edges)
assert len(set(edges)) == 4872 and set(edges) == expected
run = subprocess.run([str(project/'computations/ddp/verify_graph'),
                      str(out/'production.best.edges'), '12', '3'],
                     capture_output=True, text=True)
assert run.returncode in (0,1), run.stderr
v = json.loads(run.stdout)
assert v['n'] == v['roots_checked'] == 812 and v['m'] == 4872
assert v['min_degree'] == v['max_degree'] == 12
assert v['unreachable_unordered_pairs'] == 0
assert v['diameter'] == saved['diameter'] == 4
assert v['bad_unordered_pairs'] == saved['bad_unordered_pairs'] == 15022
assert {int(d):n for d,n in v['ordered_distance_histogram'].items()} == {
    int(d):812*n for d,n in saved['root_distance_histogram'].items()}
child1 = resource.getrusage(resource.RUSAGE_CHILDREN)
own = time.process_time()-start
child = child1.ru_utime+child1.ru_stime-child0.ru_utime-child0.ru_stime
v.update(simple=True, connected=True, independent_edges_exactly_equal=True,
         independent_reconstruction_CPU_seconds=own, generic_checker_CPU_seconds=child,
         total_CPU_seconds=own+child,
         scope='Only saved best812; exact component and edge reconstruction; one all812root check.')
(out/'production.best.independent_check.json').write_text(json.dumps(v,indent=2)+'\n')
print(json.dumps(v,indent=2))
