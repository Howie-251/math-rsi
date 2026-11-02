"""Verify only the saved 272-vertex Cayley graph, without rerunning enumeration."""
import json
import resource
import subprocess
import time
from collections import Counter, deque
from pathlib import Path

start = time.process_time()
children_start = resource.getrusage(resource.RUSAGE_CHILDREN)
out = Path(__file__).resolve().parent
project = out.parents[3]
stem = out/'production.best'
saved = json.loads(Path(str(stem)+'.json').read_text())
n, m, degree, target = 272, 1088, 8, 3
S = set(saved['S'])
assert len(S) == len(saved['S']) == degree and 0 not in S
powers = [pow(3,i,17) for i in range(16)]
assert len(set(powers)) == 16

def product(g,h):
    x,z = g % 17,g//17
    y,t = h % 17,h//17
    return (x+powers[z]*y) % 17 + 17*((z+t) % 16)

def inverse(g):
    x,z = g % 17,g//17
    return -powers[-z % 16]*x % 17 + 17*(-z % 16)

assert {inverse(s) for s in S} == S
assert all(product(s,inverse(s)) == product(inverse(s),s) == 0 for s in S)
expected = {tuple(sorted((g,product(g,s)))) for g in range(n) for s in S}
assert len(expected) == m and all(u < v for u,v in expected)
edge_path = Path(str(stem)+'.edges')
tokens = list(map(int,edge_path.read_text().split()))
assert tokens[:2] == [n,m] and len(tokens) == 2+2*m
edges = [tuple(sorted(e)) for e in zip(tokens[2::2],tokens[3::2])]
actual = set(edges)
assert len(actual) == m and all(0 <= u < v < n for u,v in edges)
if actual != expected:
    Path(str(stem)+'.independent_mismatch.json').write_text(json.dumps({
        'missing_expected':sorted(expected-actual),'unexpected_saved':sorted(actual-expected)
    },indent=2)+'\n')
    raise AssertionError('Independent edge mismatch; no rerun')
adj = [[] for _ in range(n)]
for u,v in edges:
    adj[u].append(v)
    adj[v].append(u)
assert set(map(len,adj)) == {degree}
dist = [-1]*n
dist[0] = 0
queue = deque([0])
while queue:
    u = queue.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u]+1
            queue.append(v)
assert -1 not in dist
hist = dict(sorted(Counter(dist).items()))
assert hist == {int(k):v for k,v in saved['root_distance_histogram'].items()}
missing = sum(d > target for d in dist)
assert missing == saved['root_deficit_gt3_or_unreachable']
assert n*missing//2 == saved['bad_unordered_pairs']

# Exactly one existing generic checker invocation, all 272 roots, target D3.
proc = subprocess.run([str(project/'computations/ddp/verify_graph'),str(edge_path),
                       str(degree),str(target)],capture_output=True,text=True)
assert proc.returncode in (0,1),proc.stderr
complete = json.loads(proc.stdout)
assert complete['n'] == n and complete['m'] == m and complete['roots_checked'] == n
assert complete['min_degree'] == complete['max_degree'] == degree
assert complete['unreachable_unordered_pairs'] == 0
assert complete['diameter'] == max(dist) == saved['diameter']
assert complete['bad_unordered_pairs'] == n*missing//2
assert {int(k):v for k,v in complete['ordered_distance_histogram'].items()} == {
    d:n*count for d,count in hist.items()}
children_end = resource.getrusage(resource.RUSAGE_CHILDREN)
own_cpu = time.process_time()-start
checker_cpu = (children_end.ru_utime+children_end.ru_stime
               -children_start.ru_utime-children_start.ru_stime)
final = dict(complete)
final.update({'simple':True,'connected':True,'target_diameter':target,
              'independent_edges_exactly_equal':True,'root_0_distance_histogram':hist,
              'root_0_missing':missing,'independent_reconstruction_CPU_seconds':own_cpu,
              'generic_checker_CPU_seconds':checker_cpu,'total_CPU_seconds':own_cpu+checker_cpu,
              'scope':'Only production.best.edges; no enumeration or other graph checked.'})
(out/'best.independent_verify.json').write_text(json.dumps(final,indent=2)+'\n')
details = dict(final)
details.update({'status':'COMPLETE_ONE_SAVED_CAYLEY272_FULL_SOURCE_VERIFICATION',
                'input_edges':'production.best.edges','S':sorted(S),
                'group_product':'(x,j)(y,t)=(x+3^j*y mod17,j+t mod16)',
                'group_inverse':'(-3^(-j mod16)x mod17,-j mod16)',
                'encoding':'x+17*j','root_0_distances':dist,
                'all_root_ordered_histogram_matches_Cayley_root_weighting':True})
Path(str(stem)+'.independent_check.json').write_text(json.dumps(details,indent=2)+'\n')
print(json.dumps(final,indent=2))
