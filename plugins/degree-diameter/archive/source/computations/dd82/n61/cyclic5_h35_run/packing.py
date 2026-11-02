"""One fixed H: necessary ordinary six-point parent and special complement."""
import collections
import json
from pathlib import Path
import time

root = Path(__file__).resolve().parent
start, cpu = time.monotonic(), time.process_time()
n = 35
full = (1 << n)-1
adj = [0]*n
for line in (root/'candidate.edges').read_text().splitlines():
    x, y = map(int, line.split())
    adj[x] |= 1 << y
    adj[y] |= 1 << x
data = json.loads((root/'candidate_check.json').read_text())
f, g = data['f'], data['g']


def bits(mask):
    while mask:
        b = mask & -mask
        yield b.bit_length()-1
        mask -= b


closed = [adj[v] | (1 << v) for v in range(n)]
allowed = []
for v in range(n):
    ball = closed[v]
    for w in bits(adj[v]):
        ball |= adj[w]
    allowed.append(full ^ ball)

nodes = packings = color_pass = 0
found = None
limited = False


def dfs(chosen, choices):
    global nodes, packings, color_pass, found, limited
    nodes += 1
    if nodes % 1024 == 0 and (time.process_time()-cpu >= 8 or time.monotonic()-start >= 12):
        limited = True
        return
    if len(chosen) == 6:
        packings += 1
        if any(sorted(collections.Counter(c[v] for v in chosen).values()) != [1,1,1,1,2]
               for c in (f, g)):
            return
        color_pass += 1
        occupied = 0
        for v in chosen:
            occupied |= closed[v]
        assert occupied.bit_count() == 30
        complement = full ^ occupied
        if any(adj[v] & complement for v in bits(complement)):
            return
        found = {'A': chosen, 'P': list(bits(complement))}
        return
    while choices and choices.bit_count() >= 6-len(chosen):
        b = choices & -choices
        choices -= b
        v = b.bit_length()-1
        dfs(chosen+[v], choices & allowed[v])
        if found is not None or limited:
            return


dfs([], full)

# A second direct necessary check on this same actual H: hole neighbors must
# split between two H-independent parent classes, hence induce bipartite H.
hole_neighborhood_checks = []
for z in range(n):
    neighbors = []
    for v in range(n):
        if v != z and not (adj[z] >> v & 1) and not (adj[z] & adj[v]) and f[z] != f[v] and g[z] != g[v]:
            neighbors.append(v)
    subset = sum(1 << v for v in neighbors)
    colors, bipartite = {}, True
    for v in neighbors:
        if v in colors:
            continue
        colors[v] = 0
        queue = [v]
        for x in queue:
            for y in bits(adj[x] & subset):
                if y in colors:
                    if colors[y] == colors[x]:
                        bipartite = False
                else:
                    colors[y] = 1-colors[x]
                    queue.append(y)
    hole_neighborhood_checks.append({'z': z, 'hole_neighbors': neighbors, 'bipartite': bipartite})

if found is not None:
    # Verify returned actual sets using ordinary sets, without the search masks.
    aset, pset = set(found['A']), set(found['P'])
    balls = [{v} | set(bits(adj[v])) for v in aset]
    assert all(not (x & y) for k, x in enumerate(balls) for y in balls[k+1:])
    assert set.union(*balls) == set(range(n))-pset
    assert all(not (set(bits(adj[v])) & pset) for v in pset)

result = dict(status='PACKING_FOUND' if found else 'INCOMPLETE_RESOURCE_LIMIT' if limited else 'EXHAUSTED_NO_PACKING',
              complete=not found and not limited, nodes=nodes, six_packings_checked=packings,
              color_pass=color_pass, witness=found, hole_neighborhood_checks=hole_neighborhood_checks,
              cpu_seconds=time.process_time()-cpu, wall_seconds=time.monotonic()-start)
(root/'packing_result.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k != 'hole_neighborhood_checks'}))
