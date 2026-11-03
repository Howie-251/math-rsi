"""One saved nonfaithful p31 cyclic triangle-head graph, independently reconstructed."""
import json
import resource
import subprocess
import sys
import time
from collections import Counter, deque
from pathlib import Path

START = time.process_time()
CHILD_START = resource.getrusage(resource.RUSAGE_CHILDREN)
OUT = Path(__file__).resolve().parent
PROJECT = OUT.parents[3]
stem = OUT / (sys.argv[1] if len(sys.argv) > 1 else 'production.best')
saved = json.loads(Path(str(stem)+'.json').read_text())
P, R, A_ORDER, K_ORDER, H_ORDER, INDEX = 31, 9, 93, 30, 6, 5
LEAVES, BLOCKS, HEADS, N = 2790, 465, 93, 3348
BLOCK_START, HEAD_START = 2790, 3255
S = set(saved['S'])
powers = [pow(R,i,P) for i in range(K_ORDER)]
U = {powers[INDEX*i] for i in range(H_ORDER)}
assert len(set(powers)) == 15 and len(U) == 3


def encode(x,w,i):
    return x % P + P*(w % 3) + A_ORDER*(i % K_ORDER)


def decode(g):
    a, i = g % A_ORDER, g // A_ORDER
    return a % P, a // P, i


def multiply(g,h):
    x,w,i = decode(g)
    y,v,j = decode(h)
    return encode(x+powers[i]*y,w+v,i+j)


def inverse(g):
    x,w,i = decode(g)
    return encode(-powers[-i % K_ORDER]*x,-w,-i)


def orbit(a):
    return {(u*(a % P)) % P + P*(a // P) for u in U}


def require_match(condition,stage,details):
    if not condition:
        Path(str(stem)+'.independent_mismatch.json').write_text(json.dumps({
            'status':'STOPPED_AT_MISMATCH_NO_RERUN','stage':stage,'details':details,
        },indent=2)+'\n')
        raise AssertionError(stage)


assert len(S) == len(saved['S']) == 6 and 0 not in S
assert {inverse(s) for s in S} == S
assert all(multiply(s,inverse(s)) == multiply(inverse(s),s) == 0 for s in S)
expected_edges = set()
for g in range(LEAVES):
    for s in S:
        v = multiply(g,s)
        assert g != v
        expected_edges.add(tuple(sorted((g,v))))
    a, i = g % A_ORDER, g // A_ORDER
    expected_edges.add((g,BLOCK_START+a+A_ORDER*(i % INDEX)))
for j in range(INDEX):
    for a in range(A_ORDER):
        expected_edges.add((BLOCK_START+a+A_ORDER*j,HEAD_START+a))
triangle_edges = set()
for x in range(P):
    triangle = [HEAD_START+x+P*w for w in range(3)]
    for i,j in [(0,1),(0,2),(1,2)]:
        triangle_edges.add((triangle[i],triangle[j]))
assert len(triangle_edges) == 93
expected_edges |= triangle_edges

edge_path = Path(str(stem)+'.edges')
tokens = list(map(int,edge_path.read_text().split()))
n,m = tokens[:2]
assert (n,m) == (N,11718) and len(tokens) == 2+2*m
edge_list = [tuple(sorted(pair)) for pair in zip(tokens[2::2],tokens[3::2])]
actual_edges = set(edge_list)
assert len(actual_edges) == m and all(0 <= u < v < n for u,v in edge_list)
require_match(actual_edges == expected_edges,'independent_edge_set',{
    'missing_expected_edges':sorted(expected_edges-actual_edges),
    'unexpected_saved_edges':sorted(actual_edges-expected_edges),
})
assert {e for e in actual_edges if e[0] >= HEAD_START} == triangle_edges
adj = [[] for _ in range(n)]
for u,v in edge_list:
    adj[u].append(v)
    adj[v].append(u)
assert set(map(len,adj)) == {7}

layers = [('leaf',0,BLOCK_START),('block',BLOCK_START,HEAD_START),('head',HEAD_START,N)]
roots, distances = [], []
for layer,root,_ in layers:
    dist = [-1]*n
    dist[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u]+1
                queue.append(v)
    assert -1 not in dist
    distances.append(dist)
    roots.append({'layer':layer,'root':root,'missing':sum(d > 5 for d in dist),
                  'distance_histogram':dict(sorted(Counter(dist).items())),
                  'missing_by_target_layer':[sum(d > 5 for d in dist[lo:hi]) for _,lo,hi in layers]})
require_match([r['missing'] for r in roots] == saved['graph']['root_missing'],'root_missing',roots)
require_match([r['missing_by_target_layer'] for r in roots] == saved['graph']['root_missing_by_target_layer'],
              'root_layer_missing',roots)
ordered_bad = sum(size*root['missing'] for size,root in zip([LEAVES,BLOCKS,HEADS],roots))
assert ordered_bad % 2 == 0
weighted_bad = ordered_bad // 2
assert weighted_bad == saved['graph']['bad_unordered_pairs']
ll,lb,lh = roots[0]['missing_by_target_layer']
bl,bb,bh = roots[1]['missing_by_target_layer']
hl,hb,hh = roots[2]['missing_by_target_layer']
assert LEAVES*lb == BLOCKS*bl and LEAVES*lh == HEADS*hl and BLOCKS*bh == HEADS*hb
pair_types = {'LL':LEAVES*ll//2,'LB':LEAVES*lb,'LH':LEAVES*lh,
              'BB':BLOCKS*bb//2,'BH':BLOCKS*bh,'HH':HEADS*hh//2}
assert sum(pair_types.values()) == weighted_bad

words = [{0}]
for _ in range(3):
    words.append(words[-1] | {multiply(w,s) for w in words[-1] for s in S})
HS = {a for s in S for a in orbit(s % A_ORDER)}
BB_sets = []
for j in range(INDEX):
    reachable = {P,2*P} | HS
    for w in words[3]:
        if (w // A_ORDER) % INDEX == j:
            reachable |= orbit(w % A_ORDER)
    for s in words[1]:
        x,w,i = decode(s)
        reachable |= orbit((powers[(j-i) % K_ORDER]*x) % P + P*w)
    BB_sets.append(reachable)
actual_BB = [{a for a in range(A_ORDER) if distances[1][BLOCK_START+a+A_ORDER*j] <= 5}
             for j in range(INDEX)]
mismatches = [{'a':a,'j':j,'predicted':a in BB_sets[j],
               'BFS_distance':distances[1][BLOCK_START+a+A_ORDER*j]}
              for j in range(INDEX) for a in range(A_ORDER) if (a in BB_sets[j]) != (a in actual_BB[j])]
require_match(not mismatches,'BB_all_actual_targets',mismatches)
unseen, field_orbits = set(range(1,P)), []
while unseen:
    o = {u*min(unseen) % P for u in U}
    field_orbits.append(sorted(o))
    unseen -= o
compressed_orbits = [[x+P*w for x in o] for w in range(3) for o in [[0]]+field_orbits]
BB_orbit_masks = []
for reachable in BB_sets:
    assert all(all(a in reachable for a in o) or all(a not in reachable for a in o) for o in compressed_orbits)
    BB_orbit_masks.append(sum(1 << i for i,o in enumerate(compressed_orbits) if o[0] in reachable))
require_match(BB_orbit_masks == saved['BB_masks'],'saved_BB_orbit_masks',{
    'independent':BB_orbit_masks,'saved':saved['BB_masks'],
})
BB_missing = sum(A_ORDER-len(a) for a in BB_sets)
assert BB_missing == saved['BB_missing'] == roots[1]['missing_by_target_layer'][1]

# Only this named graph, only one full-source checker invocation.
process = subprocess.run([str(PROJECT/'computations/ddp/verify_graph'),str(edge_path),'7','5'],
                         capture_output=True,text=True)
assert process.returncode in (0,1),process.stderr
complete = json.loads(process.stdout)
assert complete['roots_checked'] == N
assert complete['min_degree'] == complete['max_degree'] == 7
assert complete['unreachable_unordered_pairs'] == 0
assert complete['bad_unordered_pairs'] == weighted_bad
children = resource.getrusage(resource.RUSAGE_CHILDREN)
python_cpu = time.process_time()-START
checker_cpu = children.ru_utime+children.ru_stime-CHILD_START.ru_utime-CHILD_START.ru_stime
result = {
    'status':'COMPLETE_ONE_SAVED_NONFAITHFUL_P31_GRAPH_NO_SEARCH',
    'input':edge_path.name,'generators':sorted(S),'n':n,'m':m,
    'selection':saved['selection'],'action_order':15,'K_order':30,'H_order':6,
    'independent_edges_exactly_equal':True,'simple':True,'connected':True,'degree':7,
    'head_triangle_edges_checked':len(triangle_edges),
    'representative_roots':roots,'weighted_bad_unordered_pairs':weighted_bad,
    'bad_unordered_pairs_by_type':pair_types,'full_graph_check':complete,
    'BB_target_count':BLOCKS,'BB_all_targets_pointwise_match':True,'BB_missing':BB_missing,
    'BB_orbit_masks':BB_orbit_masks,'BB_saved_orbit_masks_match':True,
    'BB_actual_masks':[sum(1 << a for a in reachable) for reachable in actual_BB],
    'BB_block_distances_in_label_order':distances[1][BLOCK_START:HEAD_START],
    'python_cpu_seconds':python_cpu,'checker_cpu_seconds':checker_cpu,
    'total_verification_cpu_seconds':python_cpu+checker_cpu,
    'scope':'Only the named nonfaithful p31 minBB fallback graph; independent edges, three roots, all BB targets, one full3348root generic check. Not a minimum-bad-pair selection. No calibration or other sample checked.',
}
Path(str(stem)+'.independent_check.json').write_text(json.dumps(result,indent=2)+'\n')
final = dict(complete)
final.update({'selection':saved['selection'],'bad_unordered_pairs_by_type':pair_types,
              'independent_reconstruction_cpu_seconds':python_cpu,
              'generic_checker_cpu_seconds':checker_cpu,
              'total_verification_cpu_seconds':python_cpu+checker_cpu})
(OUT/'best.independent_verify.json').write_text(json.dumps(final,indent=2)+'\n')
print(json.dumps(final,indent=2))
print(json.dumps({'BB_missing':BB_missing,'BB_all_targets_pointwise_match':True,
                  'root_missing':[r['missing'] for r in roots]},indent=2))
