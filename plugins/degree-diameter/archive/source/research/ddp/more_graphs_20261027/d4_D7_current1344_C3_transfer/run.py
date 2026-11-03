"""One fixed global-G-symmetric C3 transfer; no source diameter rerun."""
from collections import Counter, deque
import json
import os
from pathlib import Path
import resource
import time

P = Path(__file__).resolve().parent
start = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (5, 6))
def save(name, x):
    (P / name).write_text(json.dumps(x, indent=2) + '\n')
save('RUN_HANDLE.json', dict(pid=os.getpid(), status='ACTUAL_PROCESS_RUNNING', command='python run.py', CPU_limit=5))
src = json.loads((P / 'SOURCE.json').read_text())
W = [tuple(x - 1 for x in row) for row in src['W_images_1based']]
I = tuple(range(32))
def mul(g, h):
    # GAP image-list permutations act on the right: j^(g*h)=(j^g)^h.
    return tuple(h[g[j]] for j in range(32))
def inverse(g):
    a = [0] * 32
    for i, j in enumerate(g): a[j] = i
    return tuple(a)
for w in W: assert sorted(w) == list(I)
assert all(mul(w, w) == I for w in W[:4])
group = [I]; index = {I: 0}
for g in group:
    for w in W:
        h = mul(g, w)
        if h not in index:
            index[h] = len(group); group.append(h)
assert len(group) == 672
volts = W + [inverse(W[4]), inverse(W[5])]
right = [[index[mul(g, w)] for w in volts] for g in group]
ports = [[(0, 0, 0, 1), (0, 1, 0, 2), (1, 4, 0, 5), (1, 5, 1, 6)],
         [(1, 2, 0, 3), (1, 3, 0, 4), (0, 6, 0, -5), (0, 7, -1, -6)]]
def vertex(c, g, s): return c * 2016 + 3 * g + s
def neighbors(c, g, s):
    return [(cc, right[g][j], (s + shift) % 3, name) for cc, j, shift, name in ports[c]]

checks = []; witnesses = []; failed = False
for rootbase in range(2):
    masks = [[0] * 672 for _ in range(2)]
    counts = Counter(); routes = {}
    bylength = [0] * 9
    stack = [(rootbase, 0, 0, -1, ())]
    while stack:
        c, g, s, prev, word = stack.pop()
        d = len(word); bylength[d] += 1; masks[c][g] |= 1 << s
        counts[c, g, s] += 1
        routes.setdefault((c, g), []).append((s, word))
        if d < 8:
            current = vertex(c, g, s)
            for cc, gg, ss, name in neighbors(c, g, s):
                if vertex(cc, gg, ss) != prev:
                    stack.append((cc, gg, ss, current, word + (name,)))
    assert bylength == [1, 4, 12, 36, 108, 324, 972, 2916, 8748]
    missing = sum(3 - m.bit_count() for row in masks for m in row)
    chk = dict(root_base=rootbase, identity_root=vertex(rootbase, 0, 0), walks_by_length=bylength,
               exact_reached_states_R8=4032-missing, exact_missing_states_R8=missing,
               endpoint_sheet_masks=masks, full_R8=missing == 0)
    checks.append(chk)
    if missing:
        c, g = next((c, g) for c in range(2) for g in range(672) if masks[c][g] != 7)
        witness = dict(source_base=rootbase, source_group=0, source_sheet=0,
                       target_base=c, target_group=g, target_group_permutation_images_1based=[x+1 for x in group[g]],
                       reached_sheet_mask=masks[c][g], missing_sheets=[s for s in range(3) if not (masks[c][g] >> s) & 1],
                       complete_NB_walks_to_this_base_group=[dict(sheet=s, word=list(w)) for s, w in routes.get((c,g),[])],
                       walk_counts_per_sheet=[counts[c,g,s] for s in range(3)])
        witnesses.append(witness); failed = True
        break

result = dict(status='FIXED_SYMMETRIC_C3_FAMILY_REJECTED_BY_EXACT_R8' if failed else 'EXACT_ENDPOINT_GATE_PASSED',
              target_Delta=4, target_D=8, savedL=3243, hypothetical_n=4032, hypothetical_m=8064,
              actual_n=None, actual_global_D=None, group_order_recovered=672,
              representative_endpoint_checks=len(checks), checks=checks, witnesses=witnesses,
              ordinary_bad_unordered_pairs=None, source_D7_BFS_repeated=0, candidate_BFS_roots=0,
              explicit_graph_exported=False, other_sheet_assignments_tested=0,
              prediction='REFUTED' if failed else 'SUPPORTED_BY_EXACT_WORD_COVERAGE')
if not failed:
    adj = []
    for c in range(2):
        for g in range(672):
            for s in range(3):
                adj.append([vertex(cc,gg,ss) for cc,gg,ss,_ in neighbors(c,g,s)])
    assert len(adj)==4032
    assert all(len(set(row))==4 and u not in row for u,row in enumerate(adj))
    assert all(u in adj[v] for u,row in enumerate(adj) for v in row)
    roots=[]
    for root in [0,2016]:
        dist=[-1]*4032;dist[root]=0;q=deque([root])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if dist[v]<0: dist[v]=dist[u]+1;q.append(v)
        roots.append(dict(root=root,visited=sum(d>=0 for d in dist),eccentricity=max(dist),distance_histogram=dict(Counter(dist))))
    assert all(x['visited']==4032 and x['eccentricity']<=8 for x in roots)
    f=P/'graph_d4_D8_n4032.edges'
    with f.open('w') as out:
        out.write('4032 8064\n')
        for u,row in enumerate(adj):
            for v in row:
                if u<v:out.write(f'{u} {v}\n')
    result.update(status='COMPLETE_D8_HIT_REQUIRES_PARENT_ACCEPTANCE',actual_n=4032,actual_m=8064,
                  actual_global_D=max(x['eccentricity'] for x in roots),roots=roots,candidate_BFS_roots=2,
                  explicit_graph_exported=True,graph_file=str(f),simple=True,degree=4,connected=True)
save('group_permutation_images0based.json',group)
result['process_CPU_seconds']=time.process_time()-start
save('RESULT.json',result)
save('checkpoint.json',dict(status=result['status'],running=False,pending=[],candidate_BFS_roots=result['candidate_BFS_roots'],CPU_seconds=result['process_CPU_seconds']))
save('RUN_HANDLE.json',dict(pid=os.getpid(),status=result['status'],running=False,completed=True,command='python run.py',CPU_limit=5,CPU_seconds=result['process_CPU_seconds']))
print(json.dumps({k:v for k,v in result.items() if k not in ['checks','witnesses']}))
if witnesses: print(json.dumps(witnesses[0]))
