"""Rebuild and verify only profile.best.edges, then record its index-two coordinates."""
import json
import resource
import subprocess
import time
from collections import Counter, deque
from pathlib import Path

start = time.process_time()
child_start = resource.getrusage(resource.RUSAGE_CHILDREN)
out = Path(__file__).resolve().parent
project = out.parents[3]
saved = json.loads((out/'profile.best.json').read_text())
n, m, degree, target = 820, 4920, 12, 3
S = saved['candidate']['S']
assert len(S) == len(set(S)) == degree and 0 not in S
powers = [pow(36,j,41) for j in range(20)]
assert len(set(powers)) == 20 and powers[10] == 40

def product(g,h):
    x,j = g % 41,g//41
    y,k = h % 41,h//41
    return (x+powers[j]*y) % 41+41*((j+k) % 20)

def inverse(g):
    x,j = g % 41,g//41
    return (-powers[-j % 20]*x) % 41+41*(-j % 20)

assert {inverse(s) for s in S} == set(S)
assert all(product(s,inverse(s)) == product(inverse(s),s) == 0 for s in S)
expected = {tuple(sorted((g,product(g,s)))) for g in range(n) for s in S}
assert len(expected) == m and all(u < v for u,v in expected)
edge_path = out/'profile.best.edges'
tokens = list(map(int,edge_path.read_text().split()))
assert tokens[:2] == [n,m] and len(tokens) == 2+2*m
edges = [tuple(sorted(pair)) for pair in zip(tokens[2::2],tokens[3::2])]
actual = set(edges)
assert len(actual) == m and all(0 <= u < v < n for u,v in edges)
if actual != expected:
    (out/'profile.best.independent_mismatch.json').write_text(json.dumps({
        'missing_expected':sorted(expected-actual),'unexpected_saved':sorted(actual-expected)
    },indent=2)+'\n')
    raise AssertionError('Independent reconstruction differs; checker not run')
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
        if dist[v] < 0:
            dist[v] = dist[u]+1
            queue.append(v)
assert -1 not in dist
hist = dict(sorted(Counter(dist).items()))
missing = sum(d > target for d in dist)
assert hist == {int(k):v for k,v in saved['root_distance_histogram'].items()}
assert missing == saved['candidate']['root_deficit']

# One generic invocation on the one original saved graph; no second graph built.
proc = subprocess.run([str(project/'computations/ddp/verify_graph'),str(edge_path),
                       str(degree),str(target)],capture_output=True,text=True)
assert proc.returncode in (0,1),proc.stderr
complete = json.loads(proc.stdout)
assert complete['n'] == n and complete['m'] == m and complete['roots_checked'] == n
assert complete['min_degree'] == complete['max_degree'] == degree
assert complete['unreachable_unordered_pairs'] == 0
assert complete['diameter'] == max(dist) == saved['candidate']['diameter']
assert complete['bad_unordered_pairs'] == n*missing//2 == saved['bad_unordered_pairs']
assert {int(k):v for k,v in complete['ordered_distance_histogram'].items()} == {
    d:n*count for d,count in hist.items()}

# Generator-level coordinates only, not an additional expanded graph or BFS.
A = [(s % 41,(s//41)//2) for s in S if (s//41) % 2 == 0]
B = [(36*x % 41,k) for x,k in A]
T = [(s % 41,(s//41)//2) for s in S if (s//41) % 2]
def h_inverse(z):
    x,k = z
    return (-pow(25,-k,41)*x % 41,-k % 10)
def psi(z):
    x,k = z
    return (-pow(36,-2*k-1,41)*x % 41,(-k-1) % 10)
assert len(A) == len(B) == len(T) == 6
assert {h_inverse(s) for s in A} == set(A)
assert {h_inverse(s) for s in B} == set(B)
assert {psi(s) for s in T} == set(T)

child_end = resource.getrusage(resource.RUSAGE_CHILDREN)
own_cpu = time.process_time()-start
checker_cpu = (child_end.ru_utime+child_end.ru_stime
               -child_start.ru_utime-child_start.ru_stime)
final = dict(complete)
final.update({'simple':True,'connected':True,'target_diameter':target,
              'independent_edges_exactly_equal':True,'root_0_distance_histogram':hist,
              'root_0_missing':missing,'independent_reconstruction_CPU_seconds':own_cpu,
              'generic_checker_CPU_seconds':checker_cpu,'total_CPU_seconds':own_cpu+checker_cpu,
              'scope':'Only profile.best.edges; one generic all-820-root call plus one root histogram; no search or other graph.'})
(out/'best.independent_verify.json').write_text(json.dumps(final,indent=2)+'\n')
details = dict(final)
details.update({'status':'COMPLETE_ONE_SAVED_AFFINE820_FULL_SOURCE_VERIFICATION',
                'input_edges':'profile.best.edges','S':S,
                'group_product':'(x,j)(y,k)=(x+36^j*y mod41,j+k mod20)',
                'group_inverse':'(-36^(-j)*x mod41,-j mod20)',
                'encoding':'x+41*j','root_0_distances':dist,
                'all_root_ordered_histogram_matches_Cayley_root_weighting':True,
                'index_two_subgroup':{'group':'F41 semidirect_25 C10','order':410,
                    'original_vertex_to_two_orbit':'(x,j) -> (j mod2,x,floor(j/2))',
                    'A':A,'B':B,'T':T,'internal_degree':6,'cross_degree':6,
                    'tau':'(x,k)->(36*x mod41,k)',
                    'Psi':'(x,k)->(-36^(-2*k-1)*x mod41,-k-1 mod10)',
                    'generator_constraints_checked':True,
                    'second_graph_generated':False,'second_graph_BFS_runs':0}})
(out/'profile.best.independent_check.json').write_text(json.dumps(details,indent=2)+'\n')
print(json.dumps(final,indent=2))
